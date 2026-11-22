#!/usr/bin/env python3
"""Run tools/eof_tee.py on both flanks of every long straight poly segment in a trace file.

usage: eof_teeall.py trace/FILE.txt     (run from the repository's root)

It takes each plain `P` line (not `?P`, and skipping lines with `[` or `:`), splits its path into segments, and
for each horizontal or vertical segment of 120 px or more runs `eof_tee.py h|v` along the segment's edges
(centre +- w/2, default w=18), leaving out 30 px at each end where the segment's own corners and pads would
show. It prints only the segments with a hit, with the eof_tee.py arguments to repeat them, then a count.

Why: re-read item R52 (wires drawn as one plain poly "with no tap" whose flanks were read by eye only) means
scanning every long segment of several trace files; `eof` run 53 used this on `cdp4`'s and `bl0`'s wires.
Everything eof_tee.py says about its limits holds here: look at every hit on a view, and "none" is not a
proof. Diagonal and short segments are not scanned.
"""
import re, subprocess, sys

if len(sys.argv) != 2:
    sys.exit(__doc__)
f = sys.argv[1]
hits = segs = 0
for n, line in enumerate(open(f), 1):
    l = line.split('#')[0].strip()
    if not l.startswith('P ') or '[' in l or ':' in l:
        continue
    m = re.search(r'w=(\d+)', l)
    w = int(m.group(1)) if m else 18
    pts = []
    x = y = None
    for tok in l[2:].split():
        if tok.startswith('w='):
            continue
        if ',' in tok:
            try:
                x, y = map(int, tok.split(','))
            except ValueError:
                break
        elif tok[0] == 'x':
            x = int(tok[1:])
        elif tok[0] == 'y':
            y = int(tok[1:])
        else:
            break
        pts.append((x, y))
    for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
        if y0 == y1 and abs(x1 - x0) >= 120:
            a, b = sorted((x0, x1))
            args = ['h', y0 - w // 2, y0 + w // 2, a + 30, b - 30]
        elif x0 == x1 and abs(y1 - y0) >= 120:
            a, b = sorted((y0, y1))
            args = ['v', x0 - w // 2, x0 + w // 2, a + 30, b - 30]
        else:
            continue
        segs += 1
        out = subprocess.run([sys.executable, 'tools/eof_tee.py'] + [str(v) for v in args],
                             capture_output=True, text=True, check=True).stdout
        bad = [o for o in out.splitlines() if not o.endswith('none')]
        if bad:
            hits += 1
            print('%s:%d %s' % (f, n, ' '.join(map(str, args))))
            for o in bad:
                print('   ', o)
print(segs, 'segments,', hits, 'with hits')
