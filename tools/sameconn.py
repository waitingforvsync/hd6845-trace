#!/usr/bin/env python3
"""Did a change to the geometry change any connection? Compares the extraction of the
working tree with that of an earlier commit, ignoring sizes, positions and net numbers.

usage: tools/t.sh PREFIX sameconn.py COMMIT [AFTER]        the package's own files (TRACE=PREFIX)
       .venv/bin/python tools/sameconn.py COMMIT [AFTER]   every trace file: the full extraction

COMMIT is the commit before the change (any git revision). Its trace/ folder is written to
a scratch folder and extracted with the same TRACE selection; nothing in the working tree
or in git is changed. AFTER, if given, is a second commit to compare with instead of the
working tree. Compared:

  1. the nets' names: which names are on one net together (a join or a split of named
     nets shows here);
  2. every transistor's terminals: the nets of its gate and of its two channel ends. An
     unnamed net is identified by what is connected to it, not by its number. Width,
     length and position are ignored, and so is how many transistors lie in parallel on
     the same three nets (a channel redrawn as two segments is the same connection; the
     counts are printed);
  3. the recovered equations (tools/netlist.py's "gates");
  4. the counts of errors and warnings (printed, not compared).

The last line is `connections identical` (exit status 0) or `CONNECTIONS DIFFER` (1),
with each difference listed above it. This is the proof the review rule asks for when a
finding is fixed as geometry only (notes/workflow.md, step 6): run it both ways and put
both last lines in the notes' Review section.

tools/names.py compare is the stricter test used for renames: there the geometry must not
move at all and only names may change. Here the names must not change and the geometry may.

Limits. It sees only what is drawn: a wire that is redrawn to leave the package somewhere
else (a moved port, a route that turns where it was drawn straight on) is a changed
connection even when both versions end on nothing here, so a fix of that kind goes to a fix
check whatever this prints. Unnamed nets are matched by their surroundings (colour refinement), which cannot
tell apart two changes that swap one unnamed net for another with exactly the same
connections. Named nets, which every port and gate output should be, are matched exactly.
"""
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)


def dump(trace_dir):
    """Child process: extract with trace/ taken from trace_dir, print what is compared."""
    sys.path.insert(0, HERE)
    import tracelib
    import netlist
    tracelib.TRACE_DIR = trace_dir
    nl = netlist.Netlist(tracelib.Trace())
    gates, passes = nl.recover_logic()
    json.dump({'nodes': {str(n.id): sorted(n.names) for n in nl.nodes.values()},
               'transistors': [[t.gate, t.c1, t.c2] for t in nl.transistors],
               'gates': [[out, expr] for out, expr, tids in gates],
               'errors': len(nl.errors), 'warnings': len(nl.warnings)}, sys.stdout)


def extract(trace_dir):
    r = subprocess.run([sys.executable, os.path.abspath(__file__), '--dump', trace_dir],
                       capture_output=True, text=True, cwd=ROOT)
    if r.returncode != 0:
        sys.exit('extraction of %s failed:\n%s' % (trace_dir, r.stderr.strip()[-2000:]))
    return json.loads(r.stdout)


def colours(d):
    """A name for every net that does not depend on its number: its names, or for an
    unnamed net a digest of what is connected to it (refined a few times)."""
    col = {n: ('+'.join(names) if names else '(unnamed)') for n, names in d['nodes'].items()}
    unnamed = [n for n, names in d['nodes'].items() if not names]
    ts = [[str(v) for v in t] for t in d['transistors']]
    inc = {n: [] for n in unnamed}
    for i, (g, a, b) in enumerate(ts):
        for role, n in (('g', g), ('c', a), ('c', b)):
            if n in inc:
                inc[n].append((role, i))

    def tcol(t):
        g, a, b = t
        return '%s : %s <-> %s' % ((col[g],) + tuple(sorted((col[a], col[b]))))

    for _ in range(6):
        tc = [tcol(t) for t in ts]
        new = {}
        for n in unnamed:
            sig = sorted({'%s %s' % (role, tc[i]) for role, i in inc[n]})
            new[n] = '(unnamed %s)' % hashlib.md5('\n'.join(sig).encode()).hexdigest()[:8]
        col.update(new)
    return col, [tcol(t) for t in ts]


def main():
    if len(sys.argv) == 3 and sys.argv[1] == '--dump':
        return dump(sys.argv[2])
    if len(sys.argv) not in (2, 3) or sys.argv[1].startswith('-'):
        sys.exit(__doc__)
    scratch = os.environ.get('HD_SCRATCH') or os.path.join('cache', 'scratch')
    scratch = scratch if os.path.isabs(scratch) else os.path.join(ROOT, scratch)
    os.makedirs(scratch, exist_ok=True)

    def at(rev):
        """(short commit, extraction of trace/ as it is at that revision)."""
        r = subprocess.run(['git', 'rev-parse', '--verify', '--quiet', rev + '^{commit}'], cwd=ROOT,
                           capture_output=True, text=True)
        if r.returncode != 0:
            sys.exit('not a commit: %s' % rev)
        commit = r.stdout.strip()
        with tempfile.TemporaryDirectory(dir=scratch, prefix='sameconn-') as d:
            names = subprocess.run(['git', 'ls-tree', '-r', '--name-only', commit, 'trace/'], cwd=ROOT,
                                   capture_output=True, text=True).stdout.split('\n')
            for f in names:
                if not f.endswith('.txt'):
                    continue
                p = os.path.join(d, f[len('trace/'):])
                os.makedirs(os.path.dirname(p), exist_ok=True)
                with open(p, 'wb') as o:
                    o.write(subprocess.run(['git', 'show', '%s:%s' % (commit, f)], cwd=ROOT, capture_output=True).stdout)
            return commit[:7], extract(d)

    a = sys.argv[1:]
    c0, before = at(a[0])
    c1, after = at(a[1]) if len(a) > 1 else ('the working tree', extract(os.path.join(ROOT, 'trace')))

    which = os.environ.get('TRACE') or 'every trace file'
    print('sameconn: %s, %s against %s' % (which, c0, c1))
    for tag, x in (('before', before), ('after ', after)):
        print('  %s  %d nets, %d transistors, %d errors, %d warnings'
              % (tag, len(x['nodes']), len(x['transistors']), x['errors'], x['warnings']))
    diffs = []

    pa = {frozenset(v) for v in before['nodes'].values() if v}
    pb = {frozenset(v) for v in after['nodes'].values() if v}
    for s in sorted(pa - pb, key=sorted):
        diffs.append('names: on one net before, not after: %s' % ' '.join(sorted(s)))
    for s in sorted(pb - pa, key=sorted):
        diffs.append('names: on one net after, not before: %s' % ' '.join(sorted(s)))

    ca, ta = colours(before)
    cb, tb = colours(after)
    for t in sorted(set(ta) - set(tb)):
        diffs.append('transistor before only: gate %s' % t)
    for t in sorted(set(tb) - set(ta)):
        diffs.append('transistor after only:  gate %s' % t)
    if not diffs and len(ta) != len(tb):
        print('  note: %d transistors became %d; each one added or removed lies in parallel with one that'
              ' is on the same three nets on both sides' % (len(ta), len(tb)))

    def eqs(x, col):
        return {'%s = %s' % (col[str(out)], re.sub(r'\bn\d+\b', '(unnamed)', expr)) for out, expr in x['gates']}
    ea, eb = eqs(before, ca), eqs(after, cb)
    for e in sorted(ea - eb):
        diffs.append('equation before only: %s' % e)
    for e in sorted(eb - ea):
        diffs.append('equation after only:  %s' % e)

    for line in diffs:
        print('  ' + line)
    if diffs:
        print('CONNECTIONS DIFFER (%d differences)' % len(diffs))
        sys.exit(1)
    print('connections identical')


if __name__ == '__main__':
    main()
