#!/usr/bin/env python3
"""Rename a signal everywhere: trace files, notes, plan, floor plan.

usage: rename.py OLD NEW [OLD NEW ...] [--dry]

Use it the moment a signal is identified (rule 2 of notes/signals.md). Each OLD is replaced
by NEW as a whole word in trace/*.txt (labels, aliases and comments; cell, block and file
names are left alone), notes/**/*.md, PLAN.md, CLAUDE.md, floorplan.txt, floorplan.d/*.txt and
ports.d/*.txt,
and a line "| OLD | NEW | |" is added to "Former names" in notes/signals.md (once: a pair
already there is not added again). An @alias line that would then alias a name to itself is
dropped.

Records of renames are left as written, so that the command can be run again in a branch
after merging main (the catch-up the journal asks for) without rewriting main's own records:
in the documents, a line that says "old name" or "former name", and in notes/journal.md a line
with "->" (a rename record or a catch-up command). These are the lines `signals.py --docs`
passes over.

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
    def keep(path, line):
        """A record of a rename: the old name stands there on purpose (as signals.py --docs)."""
        return ('old name' in line or 'former name' in line.lower()
                or (path == 'notes/journal.md' and '->' in line))

    def sub_doc(path, text):
        out, k = [], 0
        for line in text.split('\n'):
            if not keep(path, line):
                line, k1 = rx.subn(lambda q: m[q.group(1)], line)
                k += k1
            out.append(line)
        return '\n'.join(out), k

    docs = (glob.glob('notes/*.md') + glob.glob('notes/blocks/*.md') + ['PLAN.md', 'CLAUDE.md', 'floorplan.txt']
            + glob.glob('floorplan.d/*.txt') + glob.glob('ports.d/*.txt'))
    for path in sorted(docs):
        s = open(path).read()
        if path == 'notes/signals.md':
            head, sep, tail = s.partition('## Former names')
            head, k = sub_doc(path, head)
            have = set(tuple(c.strip() for c in l.split('|')[1:3]) for l in tail.split('\n') if l.startswith('|'))
            new = [kv for kv in m.items() if kv not in have]
            tail = tail.rstrip('\n') + '\n' + ''.join('| %s | %s | |\n' % kv for kv in new)
            s2 = head + sep + tail
            k += len(new)
        else:
            s2, k = sub_doc(path, s)
        if k:
            print('%4d  %s' % (k, path))
            total += k
            if not dry:
                open(path, 'w').write(s2)
    print(total, 'replacements' + (' (dry run)' if dry else ''))


if __name__ == '__main__':
    main()
