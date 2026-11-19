#!/usr/bin/env python3
"""Build the tracing dashboard: who is working on what, progress, open questions, package pages.

usage: tools/dashboard.py [--out DIR]      (default: _site)

Reads only what is in git, with the standard library, so that a GitHub Action can run it
without the image cache:
  claims/*.md                  active claims (who, since, region, status)
  notes/work-packages.md       the master list (packages, regions, status) and the Re-read list
  notes/ambiguities.md         the ambiguity register
  notes/blocks/*.md            each package's notes (rendered on its own page)
  out/floorplan_legend.txt     the functional blocks of the floor plan
  out/report.txt, its history  extraction figures now, and transistors traced over time
  out/netlist.json             transistor positions (counted per package region)
  git log                      who touched each package's files, contributors, XP, recent
                               commits, last commit on each claim's branch
  dashboard/die.jpg            the die at 1/16 scale
Writes DIR/index.html, DIR/p/PREFIX.html (one page per package), DIR/version.json and
DIR/die.jpg. .github/workflows/dashboard.yml runs it on every push with DIR = _site/dashboard
and publishes it at https://waitingforvsync.github.io/hd6845-trace/dashboard/.
"""
import argparse
import collections
import datetime
import glob
import html
import json
import math
import os
import re
import shutil
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = 'https://github.com/waitingforvsync/hd6845-trace'
W, H = 19838, 21025
REGION_RE = re.compile(r'(\d+)\s*-\s*(\d+)\s*x\s*(\d+)\s*-\s*(\d+)')
POINT_RE = re.compile(r'\((\d{3,5}),\s*(\d{3,5})\)')
E = html.escape
STALE_HOURS = 24


def git(*args):
    # TZ=UTC with the *-local date formats: a plain %ad shows each author's own offset, so a
    # timeline of several people's commits would mix timezones.
    r = subprocess.run(['git', *args], cwd=ROOT, capture_output=True, text=True,
                       env=dict(os.environ, TZ='UTC'))
    return r.stdout if r.returncode == 0 else ''


def field(text, name):
    m = re.search(r'^\|\s*%s\s*\|\s*(.*?)\s*\|\s*$' % re.escape(name), text, re.M)
    return m.group(1) if m else ''


def regions(text):
    return [tuple(int(v) for v in m.groups()) for m in REGION_RE.finditer(text)]


def inline(s):
    s = E(s)
    s = re.sub(r'`([^`]+)`', r'<code>\1</code>', s)
    s = re.sub(r'\*\*([^*]+)\*\*', r'<b>\1</b>', s)
    s = re.sub(r'(?<![\w*])\*([^*\s][^*]*)\*(?![\w*])', r'<i>\1</i>', s)
    s = re.sub(r'\[([^\]]+)\]\((https?://[^)\s]+)\)', r'<a href="\2">\1</a>', s)
    return s


def short(s, n):
    return s if len(s) <= n else s[:n].rsplit(' ', 1)[0] + ' ...'


def plain(s):
    return re.sub(r'[`*]', '', s)


def epoch_ms(s):
    """'2026-11-17 08:29 -0600' or ISO -> ms since the epoch (0 if unknown)."""
    for fmt in ('%Y-%m-%d %H:%M %z', '%Y-%m-%dT%H:%M:%S%z'):
        try:
            return int(datetime.datetime.strptime(s.strip(), fmt).timestamp() * 1000)
        except ValueError:
            pass
    return 0


def markdown(text):
    """A small Markdown renderer for the block notes: headings, paragraphs, lists, tables,
    code blocks, inline code, bold, italics, links."""
    out, para, lst, table, code = [], [], None, [], None

    def flush():
        nonlocal para, lst, table
        if para:
            out.append('<p>%s</p>' % inline(' '.join(para)))
            para = []
        if lst:
            tag, items = lst
            out.append('<%s>%s</%s>' % (tag, ''.join('<li>%s</li>' % inline(' '.join(i)) for i in items), tag))
            lst = None
        if table:
            rows = [[c.strip() for c in r.strip().strip('|').split('|')] for r in table
                    if not set(r.replace('|', '').strip()) <= set('-: ')]
            if rows:
                head, body = rows[0], rows[1:]
                out.append('<div class="tw"><table><thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>' % (
                    ''.join('<th>%s</th>' % inline(c) for c in head),
                    ''.join('<tr>%s</tr>' % ''.join('<td>%s</td>' % inline(c) for c in r) for r in body)))
            table = []

    for line in text.split('\n'):
        if code is not None:
            if line.strip().startswith('```'):
                out.append('<pre><code>%s</code></pre>' % E('\n'.join(code)))
                code = None
            else:
                code.append(line)
            continue
        s = line.strip()
        if s.startswith('```'):
            flush()
            code = []
            continue
        m = re.match(r'^(#{1,6})\s+(.*)$', s)
        if m:
            flush()
            lvl = min(6, len(m.group(1)) + 1)
            out.append('<h%d>%s</h%d>' % (lvl, inline(m.group(2)), lvl))
            continue
        if s.startswith('|'):
            if para or lst:
                p, t = para, table
                flush()
                table = t
            table.append(s)
            continue
        if table:
            flush()
        m = re.match(r'^(\s*)([-*]|\d+\.)\s+(.*)$', line)
        if m and not para:
            tag = 'ol' if m.group(2)[0].isdigit() else 'ul'
            if lst and lst[0] == tag:
                lst[1].append([m.group(3)])
            else:
                flush()
                lst = (tag, [[m.group(3)]])
            continue
        if not s:
            flush()
            continue
        if lst and line.startswith((' ', '\t')):
            lst[1][-1].append(s)
            continue
        if lst:
            flush()
        para.append(s)
    if code is not None:
        out.append('<pre><code>%s</code></pre>' % E('\n'.join(code)))
    flush()
    return '\n'.join(out)


# ------------------------------------------------------------------------------------- data
def read_claims():
    out = []
    for p in sorted(glob.glob(os.path.join(ROOT, 'claims', '*.md'))):
        name = os.path.basename(p)[:-3]
        if name == 'README':
            continue
        t = open(p).read()
        br = field(t, 'Branch') or name
        last = ''
        for ref in ('origin/' + br, br):
            last = git('log', '-1', '--format=%ad', '--date=format-local:%Y-%m-%d %H:%M %z', ref).strip()
            if last:
                break
        st = field(t, 'Status') or 'tracing'
        claimed = field(t, 'Claimed')
        activity = max(epoch_ms(claimed), epoch_ms(last)) if last else epoch_ms(claimed)
        out.append(dict(prefix=name, who=field(t, 'Who'), claimed=claimed, region=field(t, 'Region'),
                        what=field(t, 'What'), last=last, status=st, merged=st.startswith('merged'),
                        activity=activity, text=t))
    return out


def read_handoffs():
    out = []
    for p in sorted(glob.glob(os.path.join(ROOT, 'handoffs', '*.md'))):
        if os.path.basename(p) == 'README.md':
            continue
        t = open(p).read()
        m = re.match(r'(.+?)-\d{8}-\d{6}(?:-[0-9a-f]{7})?(?:-\d+)?\.md$', os.path.basename(p))
        out.append(dict(file=os.path.basename(p), prefix=m.group(1) if m else '?', who=field(t, 'Who'),
                        merged=field(t, 'Merged'), written=field(t, 'Written'), continuing=field(t, 'Continuing')))
    return out


def status_kind(s):
    s = s.strip().lower()
    if s.startswith(('done', 'checked')):
        return 'done'
    if s.startswith(('not traced', 'not done', 'queued')) or not s:
        return 'todo'
    return 'partial'


def read_master():
    rows, section, cols = [], '', None
    for line in open(os.path.join(ROOT, 'notes', 'work-packages.md')):
        line = line.rstrip('\n')
        if line.startswith('## '):
            section, cols = line[3:].strip(), None
            continue
        if not line.startswith('|'):
            continue    # a blank line inside a table must not make its next row a header
        cells = [c.strip() for c in line.strip('|').split('|')]
        if [c.lower() for c in cells][:1] == ['prefix'] or cols is None:
            cols = [c.lower() for c in cells]
            continue
        if set(line.replace('|', '').strip()) <= set('-: ') or 'prefix' not in cols or 'region' not in cols:
            continue
        get = lambda k: cells[cols.index(k)] if k in cols and cols.index(k) < len(cells) else ''
        status = get('status') if 'status' in cols else ''
        prefixes = re.findall(r'`([a-z][a-z0-9_]*)`', get('prefix'))
        m = re.match(r'`([a-z]+)(\d+)`\s*-\s*`\1(\d+)`', get('prefix'))
        if m:
            prefixes = ['%s%d' % (m.group(1), k) for k in range(int(m.group(2)), int(m.group(3)) + 1)]
        rows.append(dict(label=get('prefix'), prefixes=prefixes, region=get('region'), what=get('what'),
                         status=status, kind=status_kind(status), section=section))
    return rows


def read_ambiguities():
    t = open(os.path.join(ROOT, 'notes', 'ambiguities.md')).read()
    parts = re.split(r'^(## AMB-\d+.*)$', t, flags=re.M)
    out = []
    for i in range(1, len(parts), 2):
        head, body = parts[i], parts[i + 1]
        num = int(re.match(r'## AMB-(\d+)', head).group(1))
        title = re.sub(r'^## AMB-\d+[:\s]*', '', head)
        title = re.sub(r'\s*\((?:\d{4}-\d\d-\d\d|resolved[^)]*|open[^)]*|assumed[^)]*|mostly resolved)\)\s*', ' ', title).strip()
        h = head.lower()
        state = 'open' if 'mostly resolved' in h else 'resolved' if '(resolved' in h else 'assumed' if 'assumed' in h else 'open'
        m = POINT_RE.search(head + body)
        at = (int(m.group(1)), int(m.group(2))) if m else None
        if at is None:
            r = regions(head + body)
            at = ((r[0][0] + r[0][1]) // 2, (r[0][2] + r[0][3]) // 2) if r else None
        out.append(dict(id='A%d' % num, title=title, state=state, at=at,
                        anchor='amb-%03d' % num, line=t[:t.find(head)].count('\n') + 1))
    return out


def read_reread(master):
    t = open(os.path.join(ROOT, 'notes', 'work-packages.md')).read()
    sec = t.split('## Re-read list', 1)[1].split('\n## ', 1)[0] if '## Re-read list' in t else ''
    by_prefix = {p: r for r in master for p in r['prefixes']}
    out = []
    for line in sec.splitlines():
        m = re.match(r'^\| (R\d+) \|', line)
        if not m:
            continue
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        block, region, what, status = cells[1], cells[2], cells[3], cells[-1]
        st = status.lower()
        state = 'done' if st.startswith(('done', '~~')) else 'standing' if st.startswith('standing') else 'open'
        r = regions(region)
        if not r:
            for p in re.findall(r'`([a-z][a-z0-9_]*)`', block)[:1]:
                if p in by_prefix:
                    r = regions(by_prefix[p]['region'])
        at = ((r[0][0] + r[0][1]) // 2, (r[0][2] + r[0][3]) // 2) if r else None
        out.append(dict(id=m.group(1), title=plain(short(block + ': ' + what, 200)), state=state, at=at))
    return out


def report_figures():
    p = os.path.join(ROOT, 'out', 'report.txt')
    if not os.path.exists(p):
        return {}
    t = open(p).read()
    m = re.search(r'(\d+) nets, (\d+) transistors, (\d+) errors, (\d+) warnings', t)
    oj = re.search(r'open joins, names ending in _u \((\d+)\)', t)
    return dict(nets=int(m.group(1)), transistors=int(m.group(2)), errors=int(m.group(3)),
                open_joins=int(oj.group(1)) if oj else 0) if m else {}


def progress_series():
    pts = []
    for line in git('log', '--format=%H\t%ad', '--date=format-local:%Y-%m-%dT%H:%MZ', '--', 'out/report.txt').splitlines():
        h, d = line.split('\t')
        m = re.search(r'(\d+) nets, (\d+) transistors', git('show', '%s:out/report.txt' % h)[:300])
        if m:
            pts.append((d, int(m.group(2))))
    pts.reverse()
    return pts


def floor_blocks():
    p = os.path.join(ROOT, 'out', 'floorplan_legend.txt')
    out = []
    if os.path.exists(p):
        for line in open(p):
            if line.startswith('#'):
                continue
            f = line.rstrip('\n').split('\t')
            m = re.match(r'(\d+),(\d+):(\d+),(\d+)', f[3]) if len(f) > 3 else None
            if m:
                out.append(dict(kind=f[1], name=f[2], box=tuple(int(v) for v in m.groups()),
                                desc=f[4] if len(f) > 4 else ''))
    return out


def read_commits():
    """Every non-merge commit: author, ISO date, subject, files."""
    out, cur = [], None
    for line in git('log', '--no-merges', '--format=@@%an\t%ad\t%s', '--date=iso-strict', '--name-only').splitlines():
        if line.startswith('@@'):
            a, d, s = line[2:].split('\t', 2)
            cur = dict(author=a, date=d, subject=s, files=[])
            out.append(cur)
        elif line.strip() and cur:
            cur['files'].append(line.strip())
    return out


def tm(utc):
    """'YYYY-MM-DD HH:MM' (UTC) -> a <time> the page script shows in the viewer's own timezone."""
    return '<time class="lt" datetime="%sZ">%s UTC</time>' % (utc.replace(' ', 'T'), E(utc))


STAMP = re.compile(r'(\d{4}-\d\d-\d\d \d\d:\d\d) ([+-]\d{4})')


def localize(h):
    """In HTML, every 'YYYY-MM-DD HH:MM +ZZZZ' (the claim files' stamps, in their writer's own zone)
    becomes a <time> that the page script shows in the viewer's zone."""
    def one(m):
        d = datetime.datetime.strptime(m.group(0), '%Y-%m-%d %H:%M %z').astimezone(datetime.timezone.utc)
        return tm(d.strftime('%Y-%m-%d %H:%M'))
    return STAMP.sub(one, h)


def utc_minute(iso):
    """An ISO date with its author's offset -> 'YYYY-MM-DD HH:MM' in UTC, for display."""
    return datetime.datetime.fromisoformat(iso).astimezone(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M')


def package_history(prefixes, commits):
    pats = [re.compile(r'^(trace/%s(_[^/]*)?\.txt|notes/blocks/%s\.md|floorplan\.d/%s\.txt)$' % (p, p, p)) for p in prefixes]
    rows = [c for c in commits if any(any(pt.match(f) for pt in pats) for f in c['files'])]
    if not rows:
        return {}
    who = collections.Counter(c['author'] for c in rows)
    return dict(who=who.most_common(), first=utc_minute(rows[-1]['date'])[:10], last=utc_minute(rows[0]['date'])[:10], commits=len(rows),
                recent=[(utc_minute(c['date']), c['author'], c['subject']) for c in rows[:12]])


MODEL_NAME = {'claude-fable-5-2': 'Fable 5.2', 'claude-opus-5-5': 'Opus 5.5', 'claude-sonnet-5-5': 'Sonnet 5.5',
              'claude-haiku-5-5': 'Haiku 5.5', 'claude-fable-5-1': 'Fable 5.1', 'claude-opus-5': 'Opus 5'}


def read_costs():
    out = {}
    for p in glob.glob(os.path.join(ROOT, 'costs', '*.json')):
        try:
            r = json.load(open(p))
            out[r.get('who') or os.path.basename(p)[:-5]] = r
        except ValueError:
            pass
    return out


def package_cost(costs, prefixes):
    """API-equivalent dollars and models for a package, over every contributor's report."""
    total, review, models = 0.0, 0.0, collections.Counter()
    for r in costs.values():
        for k, v in r.get('by_package', {}).items():
            if any(k == p or k.startswith(p + '_') for p in prefixes):
                total += v.get('cost', 0)
                review += v.get('review_cost', 0)
                models.update({m: n for m, n in v.get('models', {}).items() if m != '<synthetic>'})
    return total, models, review


def money(x):
    return '$%s' % ('{:,.0f}'.format(x) if x >= 100 else '{:,.2f}'.format(x))


def models_text(models):
    return ', '.join(MODEL_NAME.get(m, m) for m, _ in models.most_common()) or 'unknown'


def transistors_in(nl, regs):
    if not nl or not regs:
        return 0
    return sum(1 for t in nl if any(x0 <= t[0] <= x1 and y0 <= t[1] <= y1 for x0, x1, y0, y1 in regs))


# ------------------------------------------------------------------------------------- XP
TITLES = ['Probe', 'Polysilicon Apprentice', 'Diffusion Scout', 'Contact Finder', 'Gate Keeper', 'Netlist Smith',
          'Die Whisperer', 'Silicon Archaeologist', 'Mask Master', 'Grand Tracer']


def level_of(xp):
    lv = int(math.sqrt(xp / 100)) + 1
    lo, hi = 100 * (lv - 1) ** 2, 100 * lv ** 2
    return lv, TITLES[min(lv, len(TITLES)) - 1], (xp - lo) / (hi - lo), hi - xp


def xp_table(commits, master, hist, tcount, claims):
    people = collections.defaultdict(lambda: dict(xp=0, commits=0, claims=0, done=0, partial=0, transistors=0.0,
                                                  days=collections.Counter(), badges=[], night=False, fixes=0,
                                                  renames=0, reviews=0, carto=False, wiring=0, gates=0, amb=0))
    for c in commits:
        p = people[c['author']]
        p['commits'] += 1
        p['xp'] += 10
        day = c['date'][:10]
        p['days'][day] += 1
        hour = int(c['date'][11:13])
        if hour < 5:
            p['night'] = True
        s = c['subject'].lower()
        if s.startswith('claim ') and any(f.startswith('claims/') for f in c['files']):
            p['claims'] += 1
            p['xp'] += 25
        if re.search(r'\b(fix|fixes|fixed|correct|corrected|correction)\b', s):
            p['fixes'] += 1
        if 'rename' in s:
            p['renames'] += 1
        if 'review' in s:
            p['reviews'] += 1
        if 'amb-' in s:
            p['amb'] += 1
        if any(f.startswith('floorplan.d/') for f in c['files']):
            p['carto'] = True
    for r in master:
        h = hist.get(r['label'], {})
        if not h:
            continue
        total = sum(n for _, n in h['who'])
        for a, n in h['who']:
            p = people[a]
            if r['kind'] == 'done':
                p['done'] += 1
                p['xp'] += 150
                if tcount.get(r['label'], 0):
                    p['gates'] += 1
                else:
                    p['wiring'] += 1
            elif r['kind'] == 'partial':
                p['partial'] += 1
                p['xp'] += 50
            share = tcount.get(r['label'], 0) * n / total
            p['transistors'] += share
            p['xp'] += int(share)
    out = []
    for name, p in people.items():
        days = sorted(p['days'])
        streak = best = 0
        prev = None
        for d in days:
            dd = datetime.date.fromisoformat(d)
            streak = streak + 1 if prev and (dd - prev).days == 1 else 1
            best = max(best, streak)
            prev = dd
        b = []
        if p['claims']:
            b.append(('🏁', 'First claim', 'made a claim with tools/claim.py'))
        if p['gates']:
            b.append(('🔬', 'Gate hunter', 'a finished package with transistors in it'))
        if p['wiring']:
            b.append(('🧵', 'Wire wrangler', 'a finished wiring package'))
        if p['done'] >= 5:
            b.append(('🏗️', 'Block builder', 'five or more finished packages'))
        if p['night']:
            b.append(('🦉', 'Night owl', 'a commit between midnight and 5 am, local time'))
        if max(p['days'].values() or [0]) >= 15:
            b.append(('🏃', 'Marathon', '15 or more commits in one day'))
        if best >= 3:
            b.append(('🔥', '%d-day streak' % best, 'commits on %d days in a row' % best))
        if p['fixes'] >= 3:
            b.append(('🧹', 'Bug squasher', 'three or more fixes or corrections'))
        if p['renames']:
            b.append(('🏷️', 'Name giver', 'renamed a signal once its purpose was known'))
        if p['reviews']:
            b.append(('🤝', 'Second pair of eyes', 'a commit that records a review'))
        if p['amb']:
            b.append(('❓', 'Question keeper', 'worked on the ambiguity register'))
        if p['carto']:
            b.append(('🗺️', 'Cartographer', 'drew blocks on the floor plan'))
        if p['commits'] >= 100:
            b.append(('💯', 'Centurion', '100 commits'))
        lv, title, frac, need = level_of(p['xp'])
        out.append(dict(name=name, xp=p['xp'], level=lv, title=title, frac=frac, need=need, commits=p['commits'],
                        done=p['done'], partial=p['partial'], transistors=int(p['transistors']), claims=p['claims'],
                        streak=best, badges=b))
    out.sort(key=lambda r: -r['xp'])
    return out


# ------------------------------------------------------------------------------------- page parts
CSS = """
.viz-root{color-scheme:light;--surface:#fcfcfb;--card:#ffffff;--ink:#0b0b0b;--ink2:#52514e;--ink3:#8a8984;--line:#e6e5e0;
 --partial:#2a78d6;--active:#eb6834;--done:#1baf7a;--todo:#9a9994;--series:#2a78d6;--track:#ecebe6}
@media (prefers-color-scheme:dark){:root:where(:not([data-theme="light"])) .viz-root{color-scheme:dark;--surface:#1a1a19;--card:#222220;
 --ink:#f0efec;--ink2:#c3c2b7;--ink3:#8f8e86;--line:#33332f;--partial:#3987e5;--active:#d95926;--done:#199e70;--todo:#77766f;--series:#3987e5;--track:#2d2d2a}}
:root[data-theme="dark"] .viz-root{color-scheme:dark;--surface:#1a1a19;--card:#222220;--ink:#f0efec;--ink2:#c3c2b7;--ink3:#8f8e86;--line:#33332f;
 --partial:#3987e5;--active:#d95926;--done:#199e70;--todo:#77766f;--series:#3987e5;--track:#2d2d2a}
*{box-sizing:border-box}body{margin:0}a{color:inherit}
.viz-root{background:var(--surface);color:var(--ink);font:15px/1.5 system-ui,-apple-system,"Segoe UI",sans-serif;min-height:100vh}
main{max-width:1240px;margin:0 auto;padding:24px 16px 64px}h1{font-size:24px;margin:0 0 4px}h2{font-size:18px;margin:36px 0 12px}h3{font-size:15px;margin:0 0 8px}
.dim{color:var(--ink2)}.mut{color:var(--ink3)}code{font:13px ui-monospace,SFMono-Regular,Menlo,monospace}
.top{display:flex;justify-content:space-between;align-items:center;gap:12px;flex-wrap:wrap}
.stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:12px;margin:20px 0}
.stat{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:12px 14px}.stat .v{font-size:24px;font-weight:600}.stat .l{color:var(--ink2);font-size:13px}
.grid{display:grid;grid-template-columns:minmax(0,6fr) minmax(0,5fr);gap:28px}@media(max-width:900px){.grid{grid-template-columns:1fr}}
.die{width:100%;height:auto;border-radius:8px;background:#000;display:block}
.pk{stroke-width:45;fill-opacity:.16}.pk.todo{fill:var(--todo);fill-opacity:.1;stroke:var(--todo);stroke-dasharray:160 120;stroke-width:35}.pk.wide{pointer-events:none;fill:none}
.pk.partial{fill:var(--partial);stroke:var(--partial)}.pk.done{fill:var(--done);stroke:var(--done)}
.pk.active{fill:var(--active);stroke:var(--active);stroke-width:110;fill-opacity:.32}
.fb{fill:none;stroke:#fff;stroke-opacity:.7;stroke-width:25}a:hover .fb,.fb:hover{stroke-width:120;fill-opacity:.35}a:hover .pk,.pk.todo:hover{stroke-width:130;fill-opacity:.6}svg[data-hl] .pk{fill-opacity:.04;stroke-opacity:.3}svg[data-hl=active] .pk.active,svg[data-hl=partial] .pk.partial,svg[data-hl=done] .pk.done,svg[data-hl=todo] .pk.todo{fill-opacity:.55;stroke-opacity:1;stroke-width:130}.key[data-state]{cursor:default}.key[data-state]:hover{text-decoration:underline}
.lbl{fill:#fff;font:600 380px system-ui,sans-serif;paint-order:stroke;stroke:#000;stroke-width:60;pointer-events:none}
.qm circle{fill:#fff;stroke:#111;stroke-width:40}.qm text{fill:#111;font:700 230px system-ui,sans-serif;text-anchor:middle;dominant-baseline:central}
.qm.reread circle{fill:#111;stroke:#fff}.qm.reread text{fill:#fff}.qm:hover circle{stroke-width:90}
svg[data-layer="blocks"] .pk,svg[data-layer="blocks"] .lbl{display:none}svg[data-layer="packages"] .fb{display:none}svg[data-q="off"] .qm{display:none}
.key{display:inline-flex;align-items:center;gap:6px;margin:10px 16px 0 0;font-size:13px;color:var(--ink2)}.sw{width:12px;height:12px;border-radius:3px;display:inline-block}
.seg button,.filters button{font:inherit;font-size:13px;margin:0 6px 8px 0;padding:3px 12px;border-radius:99px;border:1px solid var(--line);background:var(--card);color:var(--ink);cursor:pointer}
.seg button.on,.filters button.on{border-color:var(--ink)}.theme button{margin-bottom:0}
.chk{font-size:13px;color:var(--ink2);margin-left:6px}
.lists{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:20px}@media(max-width:900px){.lists{grid-template-columns:1fr}}
.col{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:14px;max-height:620px;overflow:auto}
.item{padding:9px 0;border-bottom:1px solid var(--line);font-size:14px}.item:last-child{border:0}.item .h{display:flex;gap:8px;align-items:baseline;flex-wrap:wrap}
.item a{text-decoration:none}.item a:hover{text-decoration:underline}
.tag{display:inline-flex;align-items:center;gap:5px;font-size:12px;color:var(--ink2)}.tag i{width:9px;height:9px;border-radius:2px;display:inline-block}
.stale{display:none;font-size:12px;font-weight:600;color:var(--ink);border:1px solid var(--ink);border-radius:99px;padding:0 7px}.is-stale .stale{display:inline-block}
.tw{overflow-x:auto}table{border-collapse:collapse;width:100%;font-size:14px}th,td{text-align:left;vertical-align:top;padding:7px 8px;border-bottom:1px solid var(--line)}th{font-weight:600;color:var(--ink2);font-size:13px}
td.n,th.n{text-align:right;font-variant-numeric:tabular-nums}
.chart{position:relative}.chart svg{width:100%;height:auto;display:block}.gridl{stroke:var(--line);stroke-width:1}.axis{fill:var(--ink3);font-size:12px}
.line{fill:none;stroke:var(--series);stroke-width:2}.xh{stroke:var(--ink3);stroke-width:1}.dot{fill:var(--series);stroke:var(--surface);stroke-width:2}
.tip{position:absolute;pointer-events:none;background:var(--card);border:1px solid var(--line);border-radius:8px;padding:6px 10px;font-size:13px;box-shadow:0 2px 8px rgba(0,0,0,.12);display:none;white-space:nowrap}
.commits{list-style:none;padding:0;margin:0;font-size:14px}.commits li{padding:6px 0;border-bottom:1px solid var(--line)}
.xp{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:16px}
.card{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:16px}
.who{display:flex;gap:12px;align-items:center}.av{width:44px;height:44px;border-radius:50%;display:grid;place-items:center;font-weight:700;color:#fff;background:var(--ink3);flex:none}
.lvl{font-size:13px;color:var(--ink2)}.bar{height:8px;border-radius:99px;background:var(--track);margin:10px 0 4px;overflow:hidden}.bar i{display:block;height:100%;background:var(--series);border-radius:99px}
.badges{display:flex;flex-wrap:wrap;gap:6px;margin-top:10px}.badge{font-size:12px;border:1px solid var(--line);border-radius:99px;padding:2px 8px;color:var(--ink2)}
.mini{display:grid;grid-template-columns:repeat(4,1fr);gap:6px;margin-top:10px;text-align:center}.mini b{display:block;font-size:16px}.mini span{font-size:11px;color:var(--ink3)}
.notes h2{font-size:17px;margin:28px 0 8px}.notes h3{font-size:15px;margin:20px 0 6px}.notes p,.notes li{max-width:860px}.notes table{font-size:13px}
.notes pre{background:var(--card);border:1px solid var(--line);border-radius:8px;padding:10px;overflow:auto}
.crumb{font-size:14px;margin:0}.minimap{max-width:420px}h1 code{font-size:inherit}
"""

THEME_JS = """
document.querySelectorAll('time.lt').forEach(t=>{const d=new Date(t.dateTime);if(!isNaN(d)){t.title=t.textContent;
 t.textContent=d.toLocaleString([],{year:'numeric',month:'2-digit',day:'2-digit',hour:'2-digit',minute:'2-digit'})}});
function setTheme(t){if(t==='auto')delete document.documentElement.dataset.theme;else document.documentElement.dataset.theme=t;
 document.querySelectorAll('.theme button').forEach(x=>x.classList.toggle('on',x.dataset.theme===t));try{localStorage.setItem('theme',t)}catch(e){}}
document.querySelectorAll('.theme button').forEach(b=>b.onclick=()=>setTheme(b.dataset.theme));
try{setTheme(localStorage.getItem('theme')||'auto')}catch(e){setTheme('auto')}
const live=document.getElementById('live');let checked=null,timer=null;
function showLive(){if(live)live.textContent=checked?'Checks for updates every minute; last checked '+checked.toLocaleTimeString([], {hour:'2-digit',minute:'2-digit'})+'.':'Checks for updates every minute.'}
async function check(){try{const r=await fetch(VROOT+'version.json?t='+Date.now(),{cache:'no-store'});
 if(r.ok){const v=(await r.json()).version;checked=new Date();
  if(v&&v!==VERSION){try{sessionStorage.setItem('scroll:'+location.pathname,String(window.scrollY))}catch(e){}location.reload();return}}}catch(e){}
 showLive()}
function start(){if(!timer){timer=setInterval(check,60000)}}
function stop(){clearInterval(timer);timer=null}
document.addEventListener('visibilitychange',()=>{if(document.hidden)stop();else{check();start()}});
try{const y=sessionStorage.getItem('scroll:'+location.pathname);if(y!==null){sessionStorage.removeItem('scroll:'+location.pathname);requestAnimationFrame(()=>window.scrollTo(0,+y))}}catch(e){}
document.querySelectorAll('[data-activity]').forEach(el=>{const t=+el.dataset.activity;if(t&&Date.now()-t>STALE_MS){el.classList.add('is-stale');
 const h=Math.round((Date.now()-t)/3600000);const s=el.querySelector('.stale');if(s)s.textContent='stale: '+(h>=48?Math.round(h/24)+' days':h+' h')+' quiet'}});
const ns=document.querySelectorAll('.is-stale').length,sv=document.getElementById('stale-count');if(sv)sv.textContent=ns;
showLive();start();
"""

INDEX_JS = """
function setLayer(l){document.querySelectorAll('.seg.layer button').forEach(x=>x.classList.toggle('on',x.dataset.layer===l));
 document.getElementById('die').dataset.layer=l;document.getElementById('key-pk').style.display=l==='blocks'?'none':'';
 try{sessionStorage.setItem('layer',l)}catch(e){}}
document.querySelectorAll('.key[data-state]').forEach(k=>{const d=document.getElementById('die');
 k.onmouseenter=()=>d.dataset.hl=k.dataset.state;k.onmouseleave=()=>d.removeAttribute('data-hl')});
document.querySelectorAll('.seg.layer button').forEach(b=>b.onclick=()=>setLayer(b.dataset.layer));
const qbox=document.getElementById('showq');function setQ(on){document.getElementById('die').dataset.q=on?'on':'off';qbox.checked=on;try{sessionStorage.setItem('q',on?'1':'0')}catch(e){}}
qbox.onchange=()=>setQ(qbox.checked);
try{const l=sessionStorage.getItem('layer');if(l)setLayer(l);const q=sessionStorage.getItem('q');if(q!==null)setQ(q==='1')}catch(e){}
const P=JSON.parse(document.getElementById('series').textContent),svg=document.getElementById('prog'),tip=document.getElementById('tip');
if(P.length){const W=760,H=260,L=56,R=16,T=12,B=28,t0=Date.parse(P[0][0]),t1=Date.parse(P[P.length-1][0])||t0+1,
 ymax=Math.ceil(Math.max(...P.map(p=>p[1]))/500)*500||500,X=t=>L+(W-L-R)*((t-t0)/Math.max(1,t1-t0)),Y=v=>H-B-(H-T-B)*v/ymax;
 let g='';for(let v=0;v<=ymax;v+=ymax/5){g+=`<line class="gridl" x1="${L}" x2="${W-R}" y1="${Y(v)}" y2="${Y(v)}"/><text class="axis" x="${L-8}" y="${Y(v)+4}" text-anchor="end">${v.toLocaleString()}</text>`}
 for(let d=new Date(t0);;d.setDate(d.getDate()+1)){d.setHours(0,0,0,0);if(+d>t1)break;const x=X(+d);if(x>=L&&x<=W-R)g+=`<text class="axis" x="${x}" y="${H-8}" text-anchor="middle">${String(d.getMonth()+1).padStart(2,'0')}-${String(d.getDate()).padStart(2,'0')}</text>`}
 const pts=P.map(p=>[X(Date.parse(p[0])),Y(p[1])]);
 g+=`<path class="line" d="M${pts.map(p=>p.join(',')).join('L')}"/><line class="xh" id="xh" y1="${T}" y2="${H-B}" style="display:none"/><circle class="dot" id="dot" r="4" style="display:none"/>`;
 g+=`<rect x="${L}" y="${T}" width="${W-L-R}" height="${H-T-B}" fill="transparent" id="hit"/>`;svg.innerHTML=g;
 const hit=document.getElementById('hit'),xh=document.getElementById('xh'),dot=document.getElementById('dot');
 hit.onmousemove=e=>{const r=svg.getBoundingClientRect(),mx=(e.clientX-r.left)*W/r.width;let i=0,b=1e9;pts.forEach((p,j)=>{const d=Math.abs(p[0]-mx);if(d<b){b=d;i=j}});
  xh.setAttribute('x1',pts[i][0]);xh.setAttribute('x2',pts[i][0]);xh.style.display='';dot.setAttribute('cx',pts[i][0]);dot.setAttribute('cy',pts[i][1]);dot.style.display='';
  tip.innerHTML=`<b>${P[i][1].toLocaleString()}</b> transistors<br><span class="mut">${new Date(P[i][0]).toLocaleString([],{dateStyle:'short',timeStyle:'short'})}</span>`;tip.style.display='block';
  tip.style.left=Math.min(r.width-150,pts[i][0]*r.width/W+12)+'px';tip.style.top=(pts[i][1]*r.height/H-50)+'px'};
 hit.onmouseleave=()=>{tip.style.display='none';xh.style.display='none';dot.style.display='none'}}
"""


def shell(title, body, version, root, extra_js=''):
    return """<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>%s</title><style>%s</style></head><body><div class="viz-root"><main>%s</main></div>
<script>const VERSION=%s,VROOT=%s,STALE_MS=%d;%s%s</script></body></html>""" % (
        E(title), CSS, localize(body), json.dumps(version), json.dumps(root), STALE_HOURS * 3600 * 1000, THEME_JS, extra_js)


THEME_BTNS = ('<div class="seg theme" role="group" aria-label="Colour theme"><button data-theme="auto" class="on">Auto</button>'
              '<button data-theme="light">Light</button><button data-theme="dark">Dark</button></div>')
STATE_COL = {'active': 'var(--active)', 'partial': 'var(--partial)', 'done': 'var(--done)', 'todo': 'var(--todo)'}
STATE_NAME = {'active': 'in progress', 'partial': 'partly done', 'done': 'done', 'todo': 'to do'}


def tag(kind, text=None):
    return '<span class="tag"><i style="background:%s"></i>%s</span>' % (STATE_COL[kind], E(text or STATE_NAME[kind]))


def whos(h):
    return ', '.join('%s (%d)' % (E(a), n) for a, n in h.get('who', [])) or '<span class="mut">no commits yet</span>'


def claim_item(c, link):
    return localize('<div class="item" data-activity="%d"><div class="h"><a href="%s"><code>%s</code></a> <b>%s</b> %s <span class="stale">stale</span></div>'
            '<div class="dim">%s</div><div class="mut">claimed %s; last commit %s</div></div>'
            % (c['activity'], link, E(c['prefix']), E(c['who']),
               tag('active', 'merged, awaiting coordinator' if c['merged'] else c['status']),
               inline(short(c['what'], 200)), E(c['claimed']), E(c['last'] or 'none yet')))


def die_svg(d, state, page_of, root, view=None, highlight=None):
    claimed = {c['prefix']: c for c in d['claims']}
    svg, order = [], {'todo': 0, 'partial': 1, 'done': 2, 'active': 3}
    for r in sorted(d['master'], key=lambda r: order[state(r)]):
        s = state(r)
        if highlight is not None and r is not highlight:
            continue
        link = page_of.get(r['label'])
        for x0, x1, y0, y1 in regions(r['region']):
            wide = ' wide' if x1 - x0 > 0.9 * W and y1 - y0 > 0.9 * H else ''
            rect = ('<rect class="pk %s%s" x="%d" y="%d" width="%d" height="%d"><title>%s: %s\n%s</title></rect>'
                    % (s, wide, x0, y0, x1 - x0, y1 - y0, E(plain(r['label'])), STATE_NAME[s], E(short(plain(r['what']), 160))))
            svg.append('<a href="%s%s">%s</a>' % (root, link, rect) if link else rect)
    if highlight is None:
        for c in d['claims']:
            for x0, x1, y0, y1 in regions(c['region']):
                svg.append('<a href="%sp/%s.html"><rect class="pk active" x="%d" y="%d" width="%d" height="%d"><title>%s (%s): %s</title></rect></a>'
                           '<text class="lbl" x="%d" y="%d">%s</text>'
                           % (root, E(c['prefix']), x0, y0, x1 - x0, y1 - y0, E(c['prefix']), E(c['who']), E(c['what']),
                              x0 + 80, y0 + 420, E(c['prefix'])))
        for b in d['blocks']:
            x0, y0, x1, y1 = b['box']
            svg.append('<rect class="fb" x="%d" y="%d" width="%d" height="%d"><title>%s (%s)\n%s</title></rect>'
                       % (x0, y0, x1 - x0, y1 - y0, E(b['name']), E(b['kind']), E(short(b['desc'], 200))))
        for q in d['questions']:
            if q['at'] is None or q['state'] in ('resolved', 'done'):
                continue
            cls = 'reread' if q['id'].startswith('R') else 'amb'
            svg.append('<a href="#q-%s"><g class="qm %s"><circle cx="%d" cy="%d" r="230"/><text x="%d" y="%d">%s</text>'
                       '<title>%s %s (%s)</title></g></a>' % (q['id'], cls, q['at'][0], q['at'][1], q['at'][0], q['at'][1],
                                                            q['id'], q['id'], E(q['title']), q['state']))
    vb = view or (0, 0, W, H)
    return ('<svg id="die" data-layer="packages" data-q="on" viewBox="%d %d %d %d" class="die" role="img" aria-label="Die shot">'
            '<image href="%sdie.jpg" width="%d" height="%d" preserveAspectRatio="none"/>%s</svg>'
            % (vb[0], vb[1], vb[2], vb[3], root, W, H, ''.join(svg)))


def index_page(d, state, page_of):
    claims, master, figs = d['claims'], d['master'], d['figs']
    act = [claim_item(c, 'p/%s.html' % E(c['prefix'])) for c in claims]
    todo, done = [], []
    for r in master:
        s, h = state(r), d['hist'].get(r['label'], {})
        nt = d['tcount'].get(r['label'], 0)
        if s == 'active':
            continue
        link = page_of.get(r['label'])
        label = '<a href="%s">%s</a>' % (link, inline(r['label'])) if link else inline(r['label'])
        pc, pm, pr = package_cost(d['costs'], r['prefixes'])
        cost = '; about %s%s (%s)' % (money(pc), ', review %s' % money(pr) if pr else '', models_text(pm)) if pc else ''
        if s == 'done':
            done.append((h.get('last', ''), '<div class="item"><div class="h">%s %s</div><div class="dim">%s</div>'
                         '<div class="mut">by %s%s%s</div></div>'
                         % (label, tag('done'), inline(short(r['what'], 150)), whos(h),
                            '; %s to %s; %d transistors' % (h['first'], h['last'], nt) if h else '', cost)))
        else:
            left = r['status'] if s == 'partial' else r['what']
            todo.append('<div class="item"><div class="h">%s %s</div><div class="dim">%s</div>%s</div>'
                        % (label, tag(s), inline(short(left, 260)),
                           '<div class="mut">so far by %s; %d transistors%s</div>' % (whos(h), nt, cost) if h else ''))
    done.sort(reverse=True)
    lists = ('<div class="lists"><div class="col"><h3>In progress (%d)</h3>%s</div><div class="col"><h3>To do (%d)</h3>%s</div>'
             '<div class="col"><h3>Done (%d)</h3>%s</div></div>'
             % (len(act), ''.join(act) or '<p class="mut">Nothing claimed right now.</p>', len(todo), ''.join(todo),
                len(done), ''.join(x for _, x in done)))

    qrows = []
    for q in d['questions']:
        if q['state'] in ('resolved', 'done'):
            continue
        href = ('%s/blob/main/notes/ambiguities.md#L%d' % (REPO, q['line'])) if q['id'].startswith('A') else \
            '%s/blob/main/notes/work-packages.md#re-read-list' % REPO
        qrows.append('<tr id="q-%s"><td><b>%s</b></td><td>%s</td><td>%s</td><td class="mut">%s</td><td><a href="%s">notes</a></td></tr>'
                     % (q['id'], q['id'], inline(short(q['title'], 220)), E(q['state']),
                        '(%d, %d)' % q['at'] if q['at'] else 'no single place', href))
    questions = ('<div class="tw"><table><thead><tr><th>#</th><th>Question</th><th>State</th><th>Where</th><th></th></tr></thead>'
                 '<tbody>%s</tbody></table></div>' % ''.join(qrows))

    xp = '<div class="xp">%s</div>' % ''.join(
        '<div class="card"><div class="who"><div class="av" style="background:%s">%s</div><div><b>%s</b>'
        '<div class="lvl">Level %d &middot; %s</div></div></div>'
        '<div class="bar" title="%d XP; %d to the next level"><i style="width:%.0f%%"></i></div>'
        '<div class="mut" style="font-size:12px">%s XP &middot; %s to level %d</div>'
        '<div class="mini"><div><b>%d</b><span>commits</span></div><div><b>%d</b><span>packages done</span></div>'
        '<div><b>%s</b><span>transistors</span></div><div><b>%s</b><span>API-equivalent</span></div></div>'
        '<div class="badges">%s</div></div>'
        % (('var(--partial)', 'var(--active)', 'var(--done)')[i % 3], E(''.join(w[0] for w in p['name'].split()[:2]).upper()),
           E(p['name']), p['level'], E(p['title']), p['xp'], p['need'], 100 * p['frac'], '{:,}'.format(p['xp']),
           '{:,}'.format(p['need']), p['level'] + 1, p['commits'], p['done'], '{:,}'.format(p['transistors']),
           money(d['costs'][p['name']]['total_cost']) if p['name'] in d['costs'] else '&ndash;',
           ''.join('<span class="badge" title="%s">%s %s</span>' % (E(t), e, E(n)) for e, n, t in p['badges'])
           or '<span class="mut" style="font-size:12px">no badges yet</span>')
        for i, p in enumerate(d['xp']))

    contrib_commits = '<ul class="commits">%s</ul>' % ''.join(
        '<li><span class="mut">%s</span> <b>%s</b> %s</li>' % (tm(dt), E(a), E(s)) for dt, a, s in d['recent'])
    handoff_html = ('<div class="tw"><table><thead><tr><th>Package</th><th>Who</th><th>Merged</th><th>Written</th><th>Claim</th>'
                    '<th></th></tr></thead><tbody>%s</tbody></table></div>' % ''.join(
                        '<tr><td><a href="p/%s.html"><code>%s</code></a></td><td>%s</td><td><a href="%s/commit/%s"><code>%s</code></a></td>'
                        '<td class="mut">%s</td><td>%s</td><td><a href="%s/blob/main/handoffs/%s">proposals</a></td></tr>'
                        % (E(h['prefix']), E(h['prefix']), E(h['who']), REPO, E(h['merged']), E(h['merged']), E(h['written']),
                           'kept' if h['continuing'].startswith('yes') else 'released', REPO, E(h['file'])) for h in d['handoffs'])
                    if d['handoffs'] else '<p class="mut">None: the coordinator is up to date.</p>')
    n_open_q = sum(1 for q in d['questions'] if q['state'] not in ('resolved', 'done'))
    amb_open = sum(1 for q in d['questions'] if q['id'].startswith('A') and q['state'] != 'resolved')
    amb_all = sum(1 for q in d['questions'] if q['id'].startswith('A'))
    rr_open = sum(1 for q in d['questions'] if q['id'].startswith('R') and q['state'] != 'done')
    rr_all = sum(1 for q in d['questions'] if q['id'].startswith('R'))
    cnt = collections.Counter(state(r) for r in master)
    spend = sum(r.get('total_cost', 0) for r in d['costs'].values())
    bymodel = collections.Counter()
    for r in d['costs'].values():
        for m, v in r.get('by_model', {}).items():
            if m != '<synthetic>':
                bymodel[m] += v.get('cost', 0)
    spend_rows = ''.join('<tr><td>%s</td><td class="n">%s</td><td class="n">%s</td><td class="n">%s</td><td>%s</td><td class="mut">%s</td></tr>' % (
        E(w), money(r.get('total_cost', 0)), money(r.get('review_cost', 0)), '{:,}'.format(r.get('responses', 0)),
        money(r.get('by_package', {}).get('(coordination)', {}).get('cost', 0)), E((r.get('generated') or '')[:16].replace('T', ' ')))
        for w, r in sorted(d['costs'].items(), key=lambda kv: -kv[1].get('total_cost', 0)))
    spend_html = ('<div class="tw"><table><thead><tr><th>Reported by</th><th class="n">API-equivalent</th><th class="n">of which review</th><th class="n">responses</th>'
                  '<th>of which coordination</th><th>report written</th></tr></thead><tbody>%s</tbody></table></div>'
                  '<p class="mut">By model: %s. From each contributor\'s Claude Code transcripts (<code>tools/costs.py</code>), '
                  'priced at API list prices; on a subscription nothing is billed per token. Just for interest. Contributors who have '
                  'not committed a <code>costs/</code> report show as &ndash;.</p>'
                  % (spend_rows or '<tr><td colspan="6" class="mut">No reports yet.</td></tr>',
                     ', '.join('%s %s' % (MODEL_NAME.get(m, m), money(c)) for m, c in bymodel.most_common()) or 'none'))
    stat = lambda v, l, i='': '<div class="stat"><div class="v"%s>%s</div><div class="l">%s</div></div>' % (
        ' id="%s"' % i if i else '', v, l)
    stats = ''.join([
        stat('{:,}'.format(figs.get('transistors', 0)), 'transistors traced'), stat('{:,}'.format(figs.get('nets', 0)), 'nets'),
        stat(len(claims), 'packages in progress'), stat('0', 'stale claims (24 h quiet)', 'stale-count'),
        stat(len(d['handoffs']), 'handoffs awaiting the coordinator'),
        stat(cnt['done'], 'packages done'), stat(cnt['partial'], 'partly done'), stat(cnt['todo'], 'to do'),
        stat(figs.get('errors', '?'), 'extraction errors'), stat(figs.get('open_joins', '?'), 'open joins'),
        stat('%d / %d' % (amb_open, amb_all), 'ambiguities open'), stat('%d / %d' % (rr_open, rr_all), 're-read items open'),
        stat(len(d['xp']), 'contributors'),
        stat(money(spend) if spend else '&ndash;', 'API-equivalent spend so far'),
        stat(('$%.2f' % (spend / figs['transistors'])) if spend and figs.get('transistors') else '&ndash;', 'per transistor traced')])
    key = ('<div id="key-pk">%s<span class="key"><svg width="16" height="16" viewBox="0 0 16 16"><circle cx="8" cy="8" r="6" fill="#fff" stroke="#111" stroke-width="2"/></svg>ambiguity</span>'
           '<span class="key"><svg width="16" height="16" viewBox="0 0 16 16"><circle cx="8" cy="8" r="6" fill="#111" stroke="#fff" stroke-width="2"/></svg>re-read item</span></div>'
           % ''.join('<span class="key" data-state="%s"><i class="sw" style="%s"></i>%s</span>' % (k, st, lb) for k, st, lb in (
               ('active', 'background:var(--active)', 'in progress'), ('partial', 'background:var(--partial)', 'partly done'),
               ('done', 'background:var(--done)', 'done'), ('todo', 'border:2px dashed var(--todo)', 'to do'))))
    body = """<div class="top"><h1>HD6845S die trace</h1>%s</div>
<p class="dim">Who is working on what, and how far the trace has got. Built %s. <span id="live" class="mut"></span></p>
<div class="stats">%s</div>
<div class="grid"><section><h2>The die</h2><div class="seg layer"><button class="on" data-layer="packages">Tracing packages</button><button data-layer="blocks">Functional blocks</button>
<label class="chk"><input type="checkbox" id="showq" checked> open questions (%d)</label></div>
%s%s<p class="mut">Click a package for its page; hover any region or marker for its name. Package regions overlap where wiring crosses blocks.</p></section>
<section><h2>Transistors traced</h2><div class="chart"><svg id="prog" viewBox="0 0 760 260" role="img" aria-label="Transistors traced over time"></svg><div class="tip" id="tip"></div></div>
<p class="mut">From each version of <code>out/report.txt</code> on main.</p>
<h2>Recent commits on main</h2>%s</section></div>
<h2>Packages</h2>%s
<h3 style="margin-top:20px">Handoffs awaiting the coordinator (%d)</h3>%s
<h2>Open questions</h2><p class="dim">Ambiguities (A) from <code>notes/ambiguities.md</code> and re-read items (R) from the master list, placed on the die where their notes give a place.</p>%s
<h2>What it has cost</h2>%s
<h2>Collaboration XP</h2><p class="mut">For fun. 10 XP a commit, 25 a claim, 150 for each finished package you worked on (50 if partly done), plus your share of its transistors. Level n needs 100&middot;(n&minus;1)&sup2; XP.</p>%s
<script type="application/json" id="series">%s</script>""" % (
        THEME_BTNS, E(d['built']), stats, n_open_q, die_svg(d, state, page_of, ''), key, contrib_commits, lists,
        len(d['handoffs']), handoff_html, questions, spend_html, xp,
        json.dumps(d['series']))
    return shell('HD6845S trace status', body, d['version'], '', INDEX_JS)


def package_page(prefix, row, d, state, page_of):
    claim = next((c for c in d['claims'] if c['prefix'] == prefix), None)
    s = 'active' if claim else (state(row) if row else 'todo')
    h = package_history([prefix], d['commits'])
    notes_p = os.path.join(ROOT, 'notes', 'blocks', prefix + '.md')
    notes = markdown(open(notes_p).read()) if os.path.exists(notes_p) else '<p class="mut">No notes yet.</p>'
    regs = regions((row or {}).get('region', '') + ' ' + (claim['region'] if claim else ''))
    mini = ''
    if regs:
        x0 = min(r[0] for r in regs); x1 = max(r[1] for r in regs); y0 = min(r[2] for r in regs); y1 = max(r[3] for r in regs)
        pad = max(1200, int(0.35 * max(x1 - x0, y1 - y0)))
        vx0, vy0 = max(0, x0 - pad), max(0, y0 - pad)
        vx1, vy1 = min(W, x1 + pad), min(H, y1 + pad)
        hl = dict(row) if row else dict(region=claim['region'], label=prefix, what=claim['what'])
        if row is None:
            hl.update(kind='todo', prefixes=[prefix])
        mini = ('<div class="minimap">%s<p class="mut">Region %s. <a href="../index.html">Whole die</a></p></div>'
                % (die_svg(dict(d, master=[hl]), lambda r: s if r is hl else state(r), {}, '../',
                           view=(vx0, vy0, vx1 - vx0, vy1 - vy0), highlight=hl), E(', '.join('%d-%d x %d-%d' % r for r in regs))))
    files = [f for f in ('trace/%s.txt' % prefix, 'notes/blocks/%s.md' % prefix, 'floorplan.d/%s.txt' % prefix)
             if os.path.exists(os.path.join(ROOT, f))]
    links = ' &middot; '.join('<a href="%s/blob/main/%s">%s</a>' % (REPO, f, f) for f in files)
    hist_links = ' &middot; '.join('<a href="%s/commits/main/%s">history of %s</a>' % (REPO, f, os.path.basename(f)) for f in files[:2])
    facts = []
    if claim:
        facts.append('<div class="col" style="max-height:none;margin-bottom:16px" data-activity="%d"><h3>Claimed</h3>%s</div>'
                     % (claim['activity'], claim_item(claim, '#').replace('data-activity', 'data-x')))
    facts.append('<p>%s &nbsp;<span class="dim">%s</span></p>' % (tag(s), inline((row or {}).get('status', '')) if row else ''))
    if row:
        facts.append('<p><b>What</b>: %s</p>' % inline(row['what']))
    facts.append('<p><b>Who</b>: %s%s</p>' % (whos(h), ' <span class="mut">(%s to %s, %d commits)</span>' % (h['first'], h['last'], h['commits']) if h else ''))
    if row:
        facts.append('<p><b>Transistors</b>: %d <span class="mut">(each transistor counted once, for the most specific package whose region holds it)</span></p>' % d['tcount'].get(row['label'], 0))
    pc, pm, pr = package_cost(d['costs'], [prefix])
    facts.append('<p><b>Cost</b>: %s</p>' % ('about %s API-equivalent (review %s), by %s' % (money(pc), money(pr), models_text(pm)) if pc
                                             else '<span class="mut">no cost report covers it</span>'))
    if links:
        facts.append('<p class="dim">%s<br>%s</p>' % (links, hist_links))
    recent = ('<h2>Recent commits</h2><ul class="commits">%s</ul>' % ''.join(
        '<li><span class="mut">%s</span> <b>%s</b> %s</li>' % (tm(dt), E(a), E(sub)) for dt, a, sub in h['recent'])) if h else ''
    body = """<div class="top"><p class="crumb"><a href="../index.html">&larr; Dashboard</a></p>%s</div>
<h1><code>%s</code></h1><p class="mut" id="live"></p>
<div class="grid"><section>%s</section><section>%s</section></div>%s
<h2>Notes</h2><div class="notes">%s</div>""" % (THEME_BTNS, E(prefix), ''.join(facts), mini, recent, notes)
    return shell('%s: HD6845S trace' % prefix, body, d['version'], '../')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', default=os.path.join(ROOT, '_site'))
    a = ap.parse_args()
    os.makedirs(os.path.join(a.out, 'p'), exist_ok=True)
    master = read_master()
    nl = None
    p = os.path.join(ROOT, 'out', 'netlist.json')
    if os.path.exists(p):
        nl = [(t['x'], t['y']) for t in json.load(open(p))['transistors']]
    commits = read_commits()
    hist = {r['label']: package_history(r['prefixes'], commits) for r in master}
    # each transistor counts once, for the most specific package whose region holds it (regions
    # overlap: wiring packages span other blocks), so per-package and per-person figures add up
    tcount = collections.Counter()
    boxes = [(r['label'], b, (b[1] - b[0]) * (b[3] - b[2])) for r in master for b in regions(r['region'])]
    for x, y in (nl or []):
        inside = [(area, label) for label, (x0, x1, y0, y1), area in boxes if x0 <= x <= x1 and y0 <= y <= y1]
        if inside:
            tcount[min(inside)[1]] += 1
    claims = read_claims()
    claimed = {c['prefix'] for c in claims}
    state = lambda r: 'active' if any(x in claimed for x in r['prefixes']) else r['kind']
    log = git('log', '-30', '--first-parent', '--format=%ad\t%an\t%s', '--date=format-local:%Y-%m-%d %H:%M', 'HEAD')
    head = git('log', '-1', '--format=%h, %ad', '--date=format-local:%Y-%m-%d %H:%M %z', 'HEAD').strip()
    built = '%s from commit %s' % (datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M UTC'), head)
    d = dict(claims=claims, master=master, figs=report_figures(), hist=hist, tcount=tcount, commits=commits, costs=read_costs(), handoffs=read_handoffs(),
             blocks=floor_blocks(), series=progress_series(),
             questions=read_ambiguities() + read_reread(master),
             xp=xp_table(commits, master, hist, tcount, claims),
             recent=[tuple(l.split('\t', 2)) for l in log.splitlines() if l.count('\t') >= 2],
             built=built, version=built)
    # one page per package: every prefix on the master list, every notes file, every claim
    prefixes = {}
    for r in master:
        for x in r['prefixes']:
            prefixes.setdefault(x, r)
    for f in glob.glob(os.path.join(ROOT, 'notes', 'blocks', '*.md')):
        prefixes.setdefault(os.path.basename(f)[:-3], None)
    for c in claims:
        prefixes.setdefault(c['prefix'], None)
    page_of = {r['label']: 'p/%s.html' % r['prefixes'][0] for r in master if r['prefixes']}
    for x, row in sorted(prefixes.items()):
        open(os.path.join(a.out, 'p', '%s.html' % x), 'w').write(package_page(x, row, d, state, page_of))
    open(os.path.join(a.out, 'index.html'), 'w').write(index_page(d, state, page_of))
    json.dump({'version': d['version']}, open(os.path.join(a.out, 'version.json'), 'w'))
    shutil.copy(os.path.join(ROOT, 'dashboard', 'die.jpg'), os.path.join(a.out, 'die.jpg'))
    print('dashboard: %d claims, %d packages, %d package pages, %d open questions, %d contributors -> %s'
          % (len(claims), len(master), len(prefixes), sum(1 for q in d['questions'] if q['state'] not in ('resolved', 'done')),
             len(d['xp']), a.out))


if __name__ == '__main__':
    main()
