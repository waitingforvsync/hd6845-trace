#!/usr/bin/env python3
"""Rename a signal everywhere: trace files, notes, plan, floor plan.

usage: rename.py OLD NEW [OLD NEW ...] [--dry]

Use it the moment a signal is identified (rule 2 of notes/signals.md). Each OLD is replaced
by NEW as a whole word in trace/*.txt (labels, aliases and comments; cell, block and file
names are left alone), notes/**/*.md, PLAN.md, CLAUDE.md, floorplan.txt, floorplan.d/*.txt and
ports.d/*.txt,
and a line "| OLD | NEW | |" is added to "Former names" in notes/signals.md. An @alias line
that would then alias a name to itself is dropped.

It does not rename names that a cell builds from a template and a tag (`{}`): change the
template or the tag in the trace file for those, then run this for the notes with the
concrete names. It does not add NEW to the tables of notes/signals.md: do that by hand,
with what the signal is; tools/build.py says so if you forget. Run the extraction after.
"""
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main():
    args = [a for a in sys.argv[1:] if a != '--dry']
    dry = '--dry' in sys.argv
    if not args or len(args) % 2:
        sys.exit(__doc__)
    m = dict(zip(args[0::2], args[1::2]))
    rx = re.compile(r'(?<![A-Za-z0-9_])(' + '|'.join(sorted(map(re.escape, m), key=len, reverse=True))
                    + r')(?![A-Za-z0-9_{<])')
    os.chdir(ROOT)
    total = 0
    for path in sorted(glob.glob('trace/*.txt')):
        out, k = [], 0
        for line in open(path):
            code, sep, com = line.partition('#')
            t = code.split()
            if t and t[0] in ('@cell', '@inst', '@requires', '@block'):
                out.append(line)
                continue
            nc, k1 = rx.subn(lambda q: m[q.group(1)], code)
            nm, k2 = rx.subn(lambda q: m[q.group(1)], com)
            k += k1 + k2
            t = nc.split()
            if len(t) >= 3 and t[0] == '@alias' and t[1] == t[2]:
                continue
            out.append(nc + sep + nm)
        if k:
            print('%4d  %s' % (k, path))
            total += k
            if not dry:
                open(path, 'w').write(''.join(out))
    docs = (glob.glob('notes/*.md') + glob.glob('notes/blocks/*.md') + ['PLAN.md', 'CLAUDE.md', 'floorplan.txt']
            + glob.glob('floorplan.d/*.txt') + glob.glob('ports.d/*.txt'))
    for path in sorted(docs):
        s = open(path).read()
        if path == 'notes/signals.md':
            head, sep, tail = s.partition('## Former names')
            head, k = rx.subn(lambda q: m[q.group(1)], head)
            tail = tail.rstrip('\n') + '\n' + ''.join('| %s | %s | |\n' % kv for kv in m.items())
            s2 = head + sep + tail
            k += len(m)
        else:
            s2, k = rx.subn(lambda q: m[q.group(1)], s)
        if k:
            print('%4d  %s' % (k, path))
            total += k
            if not dry:
                open(path, 'w').write(s2)
    print(total, 'replacements' + (' (dry run)' if dry else ''))


if __name__ == '__main__':
    main()
