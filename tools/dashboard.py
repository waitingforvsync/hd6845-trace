#!/usr/bin/env python3
"""Build the tracing dashboard: a static page of who is working on what, and progress.

usage: tools/dashboard.py [--out DIR]      (default: _site)

Reads only what is in git, with the standard library, so that a GitHub Action can run it
without the image cache:
  claims/*.md                  active claims (who, since, region, status)
  notes/work-packages.md       the master list (every package, its region and status)
  out/floorplan_legend.txt     the functional blocks of the floor plan
  out/report.txt, its history  extraction figures now, and transistors traced over time
  out/netlist.json             transistor positions (counted per package region)
  notes/ambiguities.md         open and resolved ambiguities
  git log                      who touched each package's files, contributors, recent commits,
                               last commit on each claim's branch
  dashboard/die.jpg            the die at 1/16 scale
Writes DIR/index.html and DIR/die.jpg. .github/workflows/dashboard.yml runs it on every push
with DIR = _site/dashboard and publishes it at https://waitingforvsync.github.io/hd6845-trace/dashboard/.
"""
import argparse
import collections
import datetime
import glob
import html
import json
import os
import re
import shutil
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
W, H = 19838, 21025
REGION_RE = re.compile(r'(\d+)\s*-\s*(\d+)\s*x\s*(\d+)\s*-\s*(\d+)')
E = html.escape


def git(*args):
    r = subprocess.run(['git', *args], cwd=ROOT, capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else ''


def field(text, name):
    m = re.search(r'^\|\s*%s\s*\|\s*(.*?)\s*\|\s*$' % re.escape(name), text, re.M)
    return m.group(1) if m else ''


def regions(text):
    return [tuple(int(v) for v in m.groups()) for m in REGION_RE.finditer(text)]


def md(s):
    s = E(s)
    s = re.sub(r'`([^`]+)`', r'<code>\1</code>', s)
    return re.sub(r'\*\*([^*]+)\*\*', r'<b>\1</b>', s)


def short(s, n):
    return s if len(s) <= n else s[:n].rsplit(' ', 1)[0] + ' ...'


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
            last = git('log', '-1', '--format=%ad', '--date=format:%Y-%m-%d %H:%M', ref).strip()
            if last:
                break
        st = field(t, 'Status') or 'tracing'
        out.append(dict(prefix=name, who=field(t, 'Who'), claimed=field(t, 'Claimed'), region=field(t, 'Region'),
                        what=field(t, 'What'), last=last, status=st, merged=st.startswith('merged')))
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
            cols = None
            continue
        cells = [c.strip() for c in line.strip('|').split('|')]
        if cols is None:
            cols = [c.lower() for c in cells]
            continue
        if set(line.replace('|', '').strip()) <= set('-: ') or 'prefix' not in cols or 'region' not in cols:
            continue
        get = lambda k: cells[cols.index(k)] if k in cols and cols.index(k) < len(cells) else ''
        status = get('status') if 'status' in cols else ''
        rows.append(dict(label=get('prefix'), prefixes=re.findall(r'`([a-z][a-z0-9_]*)`', get('prefix')),
                         region=get('region'), what=get('what'), status=status, kind=status_kind(status),
                         section=section))
    return rows


def package_history(prefixes):
    """Authors (by commits) and first/last date of the commits that touched a package's files."""
    paths = []
    for p in prefixes:
        paths += ['trace/%s.txt' % p, 'notes/blocks/%s.md' % p, 'floorplan.d/%s.txt' % p]
    if not paths:
        return {}
    log = git('log', '--format=%an\t%ad', '--date=format:%Y-%m-%d', '--', *paths)
    rows = [l.split('\t') for l in log.splitlines() if '\t' in l]
    if not rows:
        return {}
    who = collections.Counter(a for a, _ in rows)
    return dict(who=who.most_common(), first=rows[-1][1], last=rows[0][1], commits=len(rows))


def transistors_in(nl, regs):
    if not nl or not regs:
        return 0
    return sum(1 for t in nl if any(x0 <= t[0] <= x1 and y0 <= t[1] <= y1 for x0, x1, y0, y1 in regs))


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
    for line in git('log', '--format=%H\t%ad', '--date=format:%Y-%m-%d %H:%M', '--', 'out/report.txt').splitlines():
        h, d = line.split('\t')
        head = git('show', '%s:out/report.txt' % h)[:300]
        m = re.search(r'(\d+) nets, (\d+) transistors', head)
        if m:
            pts.append((d, int(m.group(2))))
    pts.reverse()
    return pts


def ambiguity_counts():
    t = open(os.path.join(ROOT, 'notes', 'ambiguities.md')).read()
    heads = re.findall(r'^## AMB-\d+.*$', t, re.M)
    resolved = sum(1 for h in heads if 'resolved' in h.lower())
    return len(heads), resolved


def reread_counts():
    t = open(os.path.join(ROOT, 'notes', 'work-packages.md')).read()
    sec = t.split('## Re-read list', 1)[1].split('\n## ', 1)[0] if '## Re-read list' in t else ''
    rows = [l for l in sec.splitlines() if re.match(r'^\| R\d+ ', l)]
    done = sum(1 for l in rows if l.rstrip(' |').split('|')[-1].strip().lower().startswith(('done', '~~')))
    return len(rows), done


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


def contributors():
    out = []
    for line in git('shortlog', '-sn', '--no-merges', 'HEAD').splitlines():
        n, name = line.strip().split('\t', 1)
        last = git('log', '-1', '--author=' + name, '--format=%ad', '--date=format:%Y-%m-%d %H:%M').strip()
        out.append((name, int(n), last))
    return out


# ------------------------------------------------------------------------------------- page
CSS = """
.viz-root{color-scheme:light;--surface:#fcfcfb;--card:#ffffff;--ink:#0b0b0b;--ink2:#52514e;--ink3:#8a8984;--line:#e6e5e0;
 --partial:#2a78d6;--active:#eb6834;--done:#1baf7a;--todo:#9a9994;--series:#2a78d6}
@media (prefers-color-scheme:dark){:root:where(:not([data-theme="light"])) .viz-root{color-scheme:dark;--surface:#1a1a19;--card:#222220;
 --ink:#f0efec;--ink2:#c3c2b7;--ink3:#8f8e86;--line:#33332f;--partial:#3987e5;--active:#d95926;--done:#199e70;--todo:#77766f;--series:#3987e5}}
:root[data-theme="dark"] .viz-root{color-scheme:dark;--surface:#1a1a19;--card:#222220;--ink:#f0efec;--ink2:#c3c2b7;--ink3:#8f8e86;--line:#33332f;
 --partial:#3987e5;--active:#d95926;--done:#199e70;--todo:#77766f;--series:#3987e5}
*{box-sizing:border-box}body{margin:0}
.viz-root{background:var(--surface);color:var(--ink);font:15px/1.5 system-ui,-apple-system,"Segoe UI",sans-serif;min-height:100vh}
main{max-width:1240px;margin:0 auto;padding:24px 16px 64px}h1{font-size:24px;margin:0 0 4px}h2{font-size:18px;margin:36px 0 12px}h3{font-size:15px;margin:0 0 8px}
.dim{color:var(--ink2)}.mut{color:var(--ink3)}code{font:13px ui-monospace,SFMono-Regular,Menlo,monospace}
.stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:12px;margin:20px 0}
.stat{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:12px 14px}.stat .v{font-size:24px;font-weight:600}.stat .l{color:var(--ink2);font-size:13px}
.grid{display:grid;grid-template-columns:minmax(0,6fr) minmax(0,5fr);gap:28px}@media(max-width:900px){.grid{grid-template-columns:1fr}}
.die{width:100%;height:auto;border-radius:8px;background:#000;display:block}
.pk{stroke-width:45;fill-opacity:.16}.pk.todo{fill:none;stroke:var(--todo);stroke-dasharray:160 120;stroke-width:35}
.pk.partial{fill:var(--partial);stroke:var(--partial)}.pk.done{fill:var(--done);stroke:var(--done)}
.pk.active{fill:var(--active);stroke:var(--active);stroke-width:110;fill-opacity:.32}
.fb{fill:none;stroke:#fff;stroke-opacity:.7;stroke-width:25}.fb:hover,.pk:hover{stroke-width:120;fill-opacity:.35}
.lbl{fill:#fff;font:600 380px system-ui,sans-serif;paint-order:stroke;stroke:#000;stroke-width:60;pointer-events:none}
svg[data-layer="blocks"] .pk,svg[data-layer="blocks"] .lbl{display:none}svg[data-layer="packages"] .fb{display:none}
.key{display:inline-flex;align-items:center;gap:6px;margin:10px 16px 0 0;font-size:13px;color:var(--ink2)}.sw{width:12px;height:12px;border-radius:3px;display:inline-block}
.seg button,.filters button{font:inherit;font-size:13px;margin:0 6px 8px 0;padding:3px 12px;border-radius:99px;border:1px solid var(--line);background:var(--card);color:var(--ink);cursor:pointer}
.seg button.on,.filters button.on{border-color:var(--ink)}
.lists{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:20px}@media(max-width:900px){.lists{grid-template-columns:1fr}}
.col{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:14px;max-height:620px;overflow:auto}
.item{padding:9px 0;border-bottom:1px solid var(--line);font-size:14px}.item:last-child{border:0}.item .h{display:flex;gap:8px;align-items:baseline;flex-wrap:wrap}
.tag{display:inline-flex;align-items:center;gap:5px;font-size:12px;color:var(--ink2)}.tag i{width:9px;height:9px;border-radius:2px;display:inline-block}
.tw{overflow-x:auto}table{border-collapse:collapse;width:100%;font-size:14px}th,td{text-align:left;vertical-align:top;padding:7px 8px;border-bottom:1px solid var(--line)}th{font-weight:600;color:var(--ink2);font-size:13px}
td.n,th.n{text-align:right;font-variant-numeric:tabular-nums}
.chart{position:relative}.chart svg{width:100%;height:auto;display:block}.gridl{stroke:var(--line);stroke-width:1}.axis{fill:var(--ink3);font-size:12px}
.line{fill:none;stroke:var(--series);stroke-width:2}.xh{stroke:var(--ink3);stroke-width:1}.dot{fill:var(--series);stroke:var(--surface);stroke-width:2}
.tip{position:absolute;pointer-events:none;background:var(--card);border:1px solid var(--line);border-radius:8px;padding:6px 10px;font-size:13px;box-shadow:0 2px 8px rgba(0,0,0,.12);display:none;white-space:nowrap}
.top{display:flex;justify-content:space-between;align-items:center;gap:12px;flex-wrap:wrap}.theme button{margin-bottom:0}
.commits{list-style:none;padding:0;margin:0;font-size:14px}.commits li{padding:6px 0;border-bottom:1px solid var(--line)}
"""

JS = """
function setTheme(t){if(t==='auto')delete document.documentElement.dataset.theme;else document.documentElement.dataset.theme=t;
 document.querySelectorAll('.theme button').forEach(x=>x.classList.toggle('on',x.dataset.theme===t));try{localStorage.setItem('theme',t)}catch(e){}}
document.querySelectorAll('.theme button').forEach(b=>b.onclick=()=>setTheme(b.dataset.theme));
try{setTheme(localStorage.getItem('theme')||'auto')}catch(e){setTheme('auto')}
function setLayer(l){document.querySelectorAll('.seg:not(.theme) button').forEach(x=>x.classList.toggle('on',x.dataset.layer===l));
 document.getElementById('die').dataset.layer=l;document.getElementById('key-pk').style.display=l==='blocks'?'none':'';
 try{sessionStorage.setItem('layer',l)}catch(e){}}
document.querySelectorAll('.seg:not(.theme) button').forEach(b=>b.onclick=()=>setLayer(b.dataset.layer));
try{const l=sessionStorage.getItem('layer');if(l)setLayer(l);const y=sessionStorage.getItem('scroll');
 if(y!==null){sessionStorage.removeItem('scroll');requestAnimationFrame(()=>window.scrollTo(0,+y))}}catch(e){}
const live=document.getElementById('live');let checked=null,timer=null;
function showLive(){live.textContent=checked?'Checks for updates every minute; last checked '+checked.toLocaleTimeString([], {hour:'2-digit',minute:'2-digit'})+'.':'Checks for updates every minute.'}
async function check(){try{const r=await fetch('version.json?t='+Date.now(),{cache:'no-store'});
 if(r.ok){const v=(await r.json()).version;checked=new Date();
  if(v&&v!==VERSION){try{sessionStorage.setItem('scroll',String(window.scrollY))}catch(e){}location.reload();return}}}catch(e){}
 showLive()}
function start(){if(!timer){timer=setInterval(check,60000)}}
function stop(){clearInterval(timer);timer=null}
document.addEventListener('visibilitychange',()=>{if(document.hidden)stop();else{check();start()}});
showLive();start();
const P=JSON.parse(document.getElementById('series').textContent),svg=document.getElementById('prog'),tip=document.getElementById('tip');
if(P.length){const W=760,H=260,L=56,R=16,T=12,B=28,t0=Date.parse(P[0][0]),t1=Date.parse(P[P.length-1][0])||t0+1,
 ymax=Math.ceil(Math.max(...P.map(p=>p[1]))/500)*500||500,X=t=>L+(W-L-R)*((t-t0)/Math.max(1,t1-t0)),Y=v=>H-B-(H-T-B)*v/ymax;
 let g='';for(let v=0;v<=ymax;v+=ymax/5){g+=`<line class="gridl" x1="${L}" x2="${W-R}" y1="${Y(v)}" y2="${Y(v)}"/><text class="axis" x="${L-8}" y="${Y(v)+4}" text-anchor="end">${v.toLocaleString()}</text>`}
 const days=[...new Set(P.map(p=>p[0].slice(0,10)))];days.forEach(d=>{const x=X(Date.parse(d+'T00:00'));if(x>=L&&x<=W-R)g+=`<text class="axis" x="${x}" y="${H-8}" text-anchor="middle">${d.slice(5)}</text>`});
 const pts=P.map(p=>[X(Date.parse(p[0].replace(' ','T'))),Y(p[1])]);
 g+=`<path class="line" d="M${pts.map(p=>p.join(',')).join('L')}"/><line class="xh" id="xh" y1="${T}" y2="${H-B}" style="display:none"/><circle class="dot" id="dot" r="4" style="display:none"/>`;
 g+=`<rect x="${L}" y="${T}" width="${W-L-R}" height="${H-T-B}" fill="transparent" id="hit"/>`;svg.innerHTML=g;
 const hit=document.getElementById('hit'),xh=document.getElementById('xh'),dot=document.getElementById('dot');
 hit.onmousemove=e=>{const r=svg.getBoundingClientRect(),mx=(e.clientX-r.left)*W/r.width;let i=0,b=1e9;pts.forEach((p,j)=>{const d=Math.abs(p[0]-mx);if(d<b){b=d;i=j}});
  xh.setAttribute('x1',pts[i][0]);xh.setAttribute('x2',pts[i][0]);xh.style.display='';dot.setAttribute('cx',pts[i][0]);dot.setAttribute('cy',pts[i][1]);dot.style.display='';
  tip.innerHTML=`<b>${P[i][1].toLocaleString()}</b> transistors<br><span class="mut">${P[i][0]}</span>`;tip.style.display='block';
  tip.style.left=Math.min(r.width-150,pts[i][0]*r.width/W+12)+'px';tip.style.top=(pts[i][1]*r.height/H-50)+'px'};
 hit.onmouseleave=()=>{tip.style.display='none';xh.style.display='none';dot.style.display='none'}}
"""


def page(d):
    claims, master, figs = d['claims'], d['master'], d['figs']
    claimed = {c['prefix']: c for c in claims}

    def state(r):
        return 'active' if any(p in claimed for p in r['prefixes']) else r['kind']

    # ---- die: packages layer + functional blocks layer
    svg = []
    order = {'todo': 0, 'partial': 1, 'done': 2, 'active': 3}
    for r in sorted(master, key=lambda r: order[state(r)]):
        s = state(r)
        for x0, x1, y0, y1 in regions(r['region']):
            svg.append('<rect class="pk %s" x="%d" y="%d" width="%d" height="%d"><title>%s: %s\n%s</title></rect>'
                       % (s, x0, y0, x1 - x0, y1 - y0, E(re.sub('[`*]', '', r['label'])),
                          {'active': 'in progress', 'todo': 'to do'}.get(s, s), E(short(re.sub('[`*]', '', r['what']), 160))))
    for c in claims:
        for x0, x1, y0, y1 in regions(c['region']):
            svg.append('<rect class="pk active" x="%d" y="%d" width="%d" height="%d"><title>%s (%s): %s</title></rect>'
                       '<text class="lbl" x="%d" y="%d">%s</text>'
                       % (x0, y0, x1 - x0, y1 - y0, E(c['prefix']), E(c['who']), E(c['what']), x0 + 80, y0 + 420, E(c['prefix'])))
    for b in d['blocks']:
        x0, y0, x1, y1 = b['box']
        svg.append('<rect class="fb" x="%d" y="%d" width="%d" height="%d"><title>%s (%s)\n%s</title></rect>'
                   % (x0, y0, x1 - x0, y1 - y0, E(b['name']), E(b['kind']), E(short(b['desc'], 200))))
    die = ('<svg id="die" data-layer="packages" viewBox="0 0 %d %d" class="die" role="img" aria-label="Die shot with the tracing packages">'
           '<image href="die.jpg" width="%d" height="%d" preserveAspectRatio="none"/>%s</svg>' % (W, H, W, H, ''.join(svg)))
    key = ('<div id="key-pk">%s</div>' % ''.join(
        '<span class="key"><i class="sw" style="%s"></i>%s</span>' % (st, lb) for st, lb in (
            ('background:var(--active)', 'in progress'), ('background:var(--partial)', 'partly done'),
            ('background:var(--done)', 'done'), ('border:2px dashed var(--todo)', 'to do'))))

    # ---- the three lists
    def tag(kind, text):
        col = {'active': 'var(--active)', 'partial': 'var(--partial)', 'done': 'var(--done)', 'todo': 'var(--todo)'}[kind]
        return '<span class="tag"><i style="background:%s"></i>%s</span>' % (col, text)

    def whos(h):
        return ', '.join('%s (%d)' % (E(a), n) for a, n in h.get('who', [])) or '<span class="mut">no commits yet</span>'

    act = []
    for c in claims:
        act.append('<div class="item"><div class="h"><code>%s</code> <b>%s</b> %s</div><div class="dim">%s</div>'
                   '<div class="mut">claimed %s; last commit %s</div></div>'
                   % (E(c['prefix']), E(c['who']), tag('active', 'merged, awaiting coordinator' if c['merged'] else 'tracing'),
                      md(short(c['what'], 200)), E(c['claimed']), E(c['last'] or 'none yet')))
    todo, done = [], []
    for r in master:
        s, h = state(r), d['hist'].get(r['label'], {})
        nt = d['tcount'].get(r['label'], 0)
        if s == 'active':
            continue
        label = md(r['label'])
        if s == 'done':
            done.append((h.get('last', ''), '<div class="item"><div class="h">%s %s</div><div class="dim">%s</div>'
                         '<div class="mut">by %s%s</div></div>'
                         % (label, tag('done', 'done'), md(short(r['what'], 150)), whos(h),
                            '; %s to %s; %d transistors in its region' % (h['first'], h['last'], nt) if h else '')))
        else:
            left = r['status'] if s == 'partial' else r['what']
            todo.append('<div class="item"><div class="h">%s %s</div><div class="dim">%s</div>%s</div>'
                        % (label, tag(s, 'partly done' if s == 'partial' else 'to do'), md(short(left, 260)),
                           '<div class="mut">so far by %s; %d transistors in its region</div>' % (whos(h), nt) if h else ''))
    done.sort(reverse=True)
    lists = ('<div class="lists"><div class="col"><h3>In progress (%d)</h3>%s</div><div class="col"><h3>To do (%d)</h3>%s</div>'
             '<div class="col"><h3>Done (%d)</h3>%s</div></div>'
             % (len(act), ''.join(act) or '<p class="mut">Nothing claimed right now.</p>', len(todo), ''.join(todo),
                len(done), ''.join(x for _, x in done)))

    # ---- tables
    contrib = ('<table><thead><tr><th>Contributor</th><th class="n">Commits</th><th>Last commit</th></tr></thead><tbody>%s</tbody></table>'
               % ''.join('<tr><td>%s</td><td class="n">%d</td><td>%s</td></tr>' % (E(n), c, E(l)) for n, c, l in d['contrib']))
    commits = '<ul class="commits">%s</ul>' % ''.join(
        '<li><span class="mut">%s</span> <b>%s</b> %s</li>' % (E(dt), E(a), E(s)) for dt, a, s in d['commits'])
    ntot, nres = d['amb']
    rtot, rdone = d['reread']
    n_done = sum(1 for r in master if state(r) == 'done')
    n_part = sum(1 for r in master if state(r) == 'partial')
    n_todo = sum(1 for r in master if state(r) == 'todo')
    stat = lambda v, l: '<div class="stat"><div class="v">%s</div><div class="l">%s</div></div>' % (v, l)
    stats = ''.join([
        stat('{:,}'.format(figs.get('transistors', 0)), 'transistors traced'),
        stat('{:,}'.format(figs.get('nets', 0)), 'nets'),
        stat(len(claims), 'packages in progress'),
        stat(n_done, 'packages done'), stat(n_part, 'partly done'), stat(n_todo, 'to do'),
        stat(figs.get('errors', '?'), 'extraction errors'), stat(figs.get('open_joins', '?'), 'open joins'),
        stat('%d / %d' % (ntot - nres, ntot), 'ambiguities open'), stat('%d / %d' % (rtot - rdone, rtot), 're-read items open'),
        stat(len(d['contrib']), 'contributors')])
    return """<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>HD6845S trace status</title><style>%s</style></head><body><div class="viz-root"><main>
<div class="top"><h1>HD6845S die trace</h1><div class="seg theme" role="group" aria-label="Colour theme"><button data-theme="auto" class="on">Auto</button><button data-theme="light">Light</button><button data-theme="dark">Dark</button></div></div>
<p class="dim">Who is working on what, and how far the trace has got. Built %s. <span id="live" class="mut"></span> Claims are made with <code>tools/claim.py</code>; the workflow is <code>notes/workflow.md</code>.</p>
<div class="stats">%s</div>
<div class="grid"><section><h2>The die</h2><div class="seg"><button class="on" data-layer="packages">Tracing packages</button><button data-layer="blocks">Functional blocks</button></div>
%s%s<p class="mut">Hover a region for its name and status. Package regions overlap where wiring crosses blocks.</p></section>
<section><h2>Transistors traced</h2><div class="chart"><svg id="prog" viewBox="0 0 760 260" role="img" aria-label="Transistors traced over time"></svg><div class="tip" id="tip"></div></div>
<p class="mut">From each version of <code>out/report.txt</code> on main.</p>
<h2>Contributors</h2><div class="tw">%s</div></section></div>
<h2>Packages</h2>%s
<h2>Recent commits on main</h2>%s
</main></div><script type="application/json" id="series">%s</script><script>const VERSION=%s;%s</script></body></html>""" % (
        CSS, E(d['built']), stats, die, key, contrib, lists, commits, json.dumps(d['series']), json.dumps(d['version']), JS)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', default=os.path.join(ROOT, '_site'))
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    master = read_master()
    nl = None
    p = os.path.join(ROOT, 'out', 'netlist.json')
    if os.path.exists(p):
        nl = [(t['x'], t['y']) for t in json.load(open(p))['transistors']]
    hist, tcount = {}, {}
    for r in master:
        hist[r['label']] = package_history(r['prefixes'])
        tcount[r['label']] = transistors_in(nl, regions(r['region']))
    log = git('log', '-30', '--first-parent', '--format=%ad\t%an\t%s', '--date=format:%Y-%m-%d %H:%M', 'HEAD')
    head = git('log', '-1', '--format=%h, %ad', '--date=format:%Y-%m-%d %H:%M %z', 'HEAD').strip()
    d = dict(claims=read_claims(), master=master, figs=report_figures(), hist=hist, tcount=tcount,
             blocks=floor_blocks(), series=progress_series(), amb=ambiguity_counts(), reread=reread_counts(),
             contrib=contributors(),
             commits=[tuple(l.split('\t', 2)) for l in log.splitlines() if l.count('\t') >= 2],
             built='%s from commit %s' % (datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M UTC'), head))
    d['version'] = d['built']
    open(os.path.join(a.out, 'index.html'), 'w').write(page(d))
    json.dump({'version': d['version']}, open(os.path.join(a.out, 'version.json'), 'w'))
    shutil.copy(os.path.join(ROOT, 'dashboard', 'die.jpg'), os.path.join(a.out, 'die.jpg'))
    print('dashboard: %d claims, %d packages, %d blocks, %d progress points -> %s'
          % (len(d['claims']), len(master), len(d['blocks']), len(d['series']), a.out))


if __name__ == '__main__':
    main()
