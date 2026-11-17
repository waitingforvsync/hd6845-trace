#!/usr/bin/env python3
"""Estimate what the tracing has cost, from this machine's Claude Code transcripts.

usage: tools/costs.py [--who NAME] [--out FILE] [--print]

Reads every session transcript Claude Code kept for this repository and its worktrees
(~/.claude/projects/<repo path with / as ->*/**.jsonl, subagents included) and prices each API
response from its usage record: input, cache writes (5-minute and 1-hour), cache reads,
output, at the model's published per-token API price. A response logged as several
transcript entries is counted once. On a Claude subscription nothing is billed per token,
so the figures are API-equivalent costs, not bills: for interest only.

Each response is attributed to the package whose files (trace/PREFIX.txt (or a file of that block,
such as trace/PREFIX_x.txt), notes/blocks/PREFIX.md, floorplan.d/PREFIX.txt) the next commit by NAME touched within six
hours of it; a response followed by a commit that touches no package, or by none, counts as
"coordination". A commit touching several packages splits the cost evenly. This is rough.

Writes costs/<NAME>.json (NAME defaults to git's user.name): totals, and the split by package,
model and day. Only numbers leave the transcripts: no text, no file contents. The dashboard
(tools/dashboard.py) adds up every costs/*.json; commit yours with your package's merge.
The merge gate (tools/mergecheck.py) reads the models recorded for your package: tracing is
done with Claude Fable 5.2 (user, 2026-11-17).
"""
import argparse
import collections
import datetime
import glob
import json
import os
import re
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# $ per million tokens: input, output, 5-minute cache write, 1-hour cache write, cache read.
# From the Claude API pricing reference (models.md / prompt-caching.md), 2026-11-03.
PRICES = {
    'claude-fable-5-2': (8.00, 40.00, 10.00, 16.00, 0.20),
    'claude-mythos-5-2': (8.00, 40.00, 10.00, 16.00, 0.20),
    'claude-fable-5-1': (10.00, 50.00, 12.50, 20.00, 0.25),
    'claude-mythos-5-1': (10.00, 50.00, 12.50, 20.00, 0.25),
    'claude-fable-5': (10.00, 50.00, 12.50, 20.00, 1.00),
    'claude-opus-5-5': (4.00, 20.00, 5.00, 8.00, 0.20),
    'claude-opus-5': (5.00, 25.00, 6.25, 10.00, 0.50),
    'claude-opus-4-8': (5.00, 25.00, 6.25, 10.00, 0.50),
    'claude-opus-4-7': (5.00, 25.00, 6.25, 10.00, 0.50),
    'claude-opus-4-6': (5.00, 25.00, 6.25, 10.00, 0.50),
    'claude-sonnet-5-5': (2.00, 10.00, 2.50, 4.00, 0.10),
    'claude-sonnet-5': (2.00, 10.00, 2.50, 4.00, 0.20),
    'claude-sonnet-4-6': (3.00, 15.00, 3.75, 6.00, 0.30),
    'claude-haiku-5-5': (0.10, 0.50, 0.125, 0.20, 0.01),
    'claude-haiku-4-5': (1.00, 5.00, 1.25, 2.00, 0.10),
}
PRICE_SOURCE = 'Claude API list prices per million tokens, as of 2026-11-03'


def git(*args):
    r = subprocess.run(['git', *args], cwd=ROOT, capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else ''


def transcript_dirs():
    base = os.path.expanduser('~/.claude/projects')
    common = git('rev-parse', '--path-format=absolute', '--git-common-dir').strip()
    main_root = os.path.dirname(common) if common.endswith('.git') else ROOT
    key = main_root.replace('/', '-').replace('.', '-')      # also matches its worktrees' folders
    return [d for d in glob.glob(os.path.join(base, key + '*')) if os.path.isdir(d)]


def ts(s):
    return datetime.datetime.fromisoformat(s.replace('Z', '+00:00'))


def responses():
    """One record per API response: (time, session, model, usage)."""
    seen, out = set(), []
    for d in transcript_dirs():
        for path in glob.glob(os.path.join(d, '**', '*.jsonl'), recursive=True):
            with open(path, errors='replace') as f:
                for line in f:
                    if '"usage"' not in line:
                        continue
                    try:
                        e = json.loads(line)
                    except ValueError:
                        continue
                    m = e.get('message')
                    if e.get('type') != 'assistant' or not isinstance(m, dict) or not m.get('usage'):
                        continue
                    key = m.get('id') or e.get('requestId') or e.get('uuid')
                    if key in seen:
                        continue
                    seen.add(key)
                    out.append((ts(e['timestamp']), e.get('sessionId', path), m.get('model', '?'), m['usage']))
    out.sort(key=lambda r: r[0])
    return out


def price(model, u):
    p = PRICES.get(model)
    known = p is not None
    p = p or PRICES['claude-opus-5-5']
    cc = u.get('cache_creation') or {}
    w1h = cc.get('ephemeral_1h_input_tokens', 0) or 0
    w5m = cc.get('ephemeral_5m_input_tokens', 0) or 0
    wall = u.get('cache_creation_input_tokens', 0) or 0
    if wall and not (w1h or w5m):
        w5m = wall
    tok = dict(input=u.get('input_tokens', 0) or 0, output=u.get('output_tokens', 0) or 0,
               cache_write_5m=w5m, cache_write_1h=w1h, cache_read=u.get('cache_read_input_tokens', 0) or 0)
    cost = (tok['input'] * p[0] + tok['output'] * p[1] + w5m * p[2] + w1h * p[3] + tok['cache_read'] * p[4]) / 1e6
    return tok, cost, known


def package_commits(who):
    out = []
    pat = re.compile(r'^(?:trace/([a-z][a-z0-9_]*)\.txt|notes/blocks/([a-z][a-z0-9_]*)\.md|floorplan\.d/([a-z][a-z0-9_]*)\.txt)$')
    cur = None
    for line in git('log', '--all', '--author=' + who, '--format=@@%aI', '--name-only').splitlines():
        if line.startswith('@@'):
            cur = [ts(line[2:]), set()]
            out.append(cur)
        elif line.strip() and cur:
            m = pat.match(line.strip())
            if m:
                cur[1].add(next(g for g in m.groups() if g))
    out.sort(key=lambda c: c[0])
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--who', default=git('config', 'user.name').strip() or 'unknown')
    ap.add_argument('--out')
    ap.add_argument('--print', action='store_true')
    a = ap.parse_args()
    commits = package_commits(a.who)
    times = [c[0] for c in commits]
    import bisect
    by_pkg = collections.defaultdict(lambda: dict(cost=0.0, responses=0, models=collections.Counter()))
    by_model = collections.defaultdict(lambda: dict(cost=0.0, responses=0))
    by_day = collections.defaultdict(float)
    tot = collections.Counter()
    total_cost, unknown = 0.0, set()
    rs = responses()
    for t, sess, model, u in rs:
        tok, cost, known = price(model, u)
        if not known:
            unknown.add(model)
        total_cost += cost
        tot.update(tok)
        by_model[model]['cost'] += cost
        by_model[model]['responses'] += 1
        by_day[t.date().isoformat()] += cost
        i = bisect.bisect_left(times, t)
        pk = []
        if i < len(commits) and (commits[i][0] - t).total_seconds() <= 6 * 3600:
            pk = sorted(commits[i][1])
        for p in pk or ['(coordination)']:
            by_pkg[p]['cost'] += cost / max(1, len(pk))
            by_pkg[p]['responses'] += 1
            by_pkg[p]['models'][model] += 1
    rec = dict(who=a.who, generated=datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds'),
               price_source=PRICE_SOURCE, unpriced_models=sorted(unknown), responses=len(rs),
               first=rs[0][0].isoformat() if rs else None, last=rs[-1][0].isoformat() if rs else None,
               total_cost=round(total_cost, 2), tokens=dict(tot),
               by_model={k: dict(cost=round(v['cost'], 2), responses=v['responses']) for k, v in by_model.items()},
               by_package={k: dict(cost=round(v['cost'], 2), responses=v['responses'], models=dict(v['models']))
                           for k, v in sorted(by_pkg.items(), key=lambda kv: -kv[1]['cost'])},
               by_day={k: round(v, 2) for k, v in sorted(by_day.items())})
    out = a.out or os.path.join(ROOT, 'costs', '%s.json' % re.sub(r'[^A-Za-z0-9_.-]+', '_', a.who))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    json.dump(rec, open(out, 'w'), indent=1)
    print('costs: %s, %d responses, $%.2f API-equivalent -> %s' % (a.who, len(rs), total_cost, os.path.relpath(out, ROOT)))
    if a.print:
        for k, v in list(rec['by_package'].items())[:15]:
            print('  %-16s $%9.2f  %6d responses' % (k, v['cost'], v['responses']))
        for k, v in rec['by_model'].items():
            print('  model %-20s $%9.2f  %6d responses' % (k, v['cost'], v['responses']))


if __name__ == '__main__':
    main()
