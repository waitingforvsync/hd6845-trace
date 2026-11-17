#!/usr/bin/env python3
"""Check the net names of the trace against the glossary notes/signals.md.

usage: signals.py            (through tools/t.sh BLOCK to look at one block)
       signals.py --docs     list former names that still occur in notes, plan, floor plan, ports or trace files

Prints the names no row of the glossary covers, and the open joins (names ending in _u).
In a glossary pattern `#` is a number and `*` any run of letters, digits and underscores;
patterns are the backticked items in the first column of the tables above "Former names".
tools/build.py runs the same check and puts the result into out/report.txt.
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tracelib

GLOSSARY = os.path.join(tracelib.ROOT, 'notes', 'signals.md')


def patterns():
    out = []
    for line in open(GLOSSARY):
        if line.startswith('## Former names'):
            break
        if not line.startswith('|'):
            continue
        first = line.split('|')[1]
        for p in re.findall(r'`([^`]+)`', first):
            rx = ''.join(r'\d+' if ch == '#' else r'[A-Za-z0-9_]+' if ch == '*' else re.escape(ch) for ch in p)
            out.append(re.compile(rx + r'\Z'))
    return out


def check(names):
    """(names not covered by the glossary, open joins) for an iterable of net names."""
    pats = patterns()
    missing = sorted(n for n in set(names) if not any(p.match(n) for p in pats))
    opens = sorted(n for n in set(names) if n.endswith('_u'))
    return missing, opens


def stale_in_docs():
    """Former names (from the glossary's last table) that still occur in the documents."""
    import glob
    olds = set()
    on = False
    for line in open(GLOSSARY):
        if line.startswith('## Former names'):
            on = True
        elif on and line.startswith('|') and not line.startswith('|---') and not line.startswith('| Old'):
            c = [t.strip() for t in line.split('|')]
            old, new, ex = c[1], c[2], c[3] if len(c) > 3 else ''
            if '#' in old:
                rx = ''.join(r'(?:\d+|[KN])' if ch == '#' else re.escape(ch) for ch in old)
            else:
                rx = re.escape(old)
            olds.add((old, re.compile(r'(?<![A-Za-z0-9_])' + rx + r'(?![A-Za-z0-9_])')))
    files = (glob.glob(os.path.join(tracelib.ROOT, 'notes', '*.md')) + glob.glob(os.path.join(tracelib.ROOT, 'notes', 'blocks', '*.md'))
             + [os.path.join(tracelib.ROOT, f) for f in ('PLAN.md', 'CLAUDE.md', 'floorplan.txt')]
             + glob.glob(os.path.join(tracelib.ROOT, 'floorplan.d', '*.txt')) + glob.glob(os.path.join(tracelib.ROOT, 'ports.d', '*.txt'))
             + glob.glob(os.path.join(tracelib.ROOT, 'trace', '*.txt')))
    hits = []
    for path in sorted(files):
        text = open(path).read()
        if path == GLOSSARY:
            text = text.split('## Former names')[0]
        for n, line in enumerate(text.splitlines(), 1):
            if 'old name' in line or 'former name' in line.lower():
                continue
            if path.endswith(os.path.join('notes', 'journal.md')) and '->' in line:
                continue      # a rename record in the journal names the old name on purpose (old -> new)
            for old, rx in olds:
                if rx.search(line):
                    hits.append('%s:%d: %s' % (os.path.relpath(path, tracelib.ROOT), n, old))
    return hits


def main():
    if '--docs' in sys.argv:
        hits = stale_in_docs()
        print('\n'.join(hits) if hits else 'no former names left in the documents')
        return
    import netlist
    nl = netlist.Netlist(tracelib.load())
    names = [n.name for n in nl.nodes.values() if n.names]
    missing, opens = check(names)
    print('%d named nets; %d not in notes/signals.md; %d open joins (_u)' % (len(set(names)), len(missing), len(opens)))
    if missing:
        print('not in the glossary: ' + ' '.join(missing))
    if opens:
        print('open joins: ' + ' '.join(opens))


if __name__ == '__main__':
    main()
