#!/usr/bin/env python3
"""Dark stretches along a thin vertical metal, and what the clean shot shows under each.

usage: tl1_wgaps.py X0 X1 Y0 Y1 [THR] [MINLEN]
For each row: the brightest 4 px window of (R+G)/2 across x X0..X1, in each metal shot.
Prints the stretches where BOTH shots stay below THR (default 165) for MINLEN rows or more
(default 10), with the clean shot's mean colour at the line's centre and whether it looks
protected (pink / tan / salmon: metal was above in chip 1) or open (khaki, green, dark red).
"""
import os, sys
import numpy as np
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
x0, x1, y0, y1 = map(int, sys.argv[1:5])
thr = float(sys.argv[5]) if len(sys.argv) > 5 else 165
minlen = int(sys.argv[6]) if len(sys.argv) > 6 else 10
ms = [np.load(os.path.join(ROOT, 'cache', f), mmap_mode='r') for f in ('metal.npy', 'metal1.npy')]
a = np.load(os.path.join(ROOT, 'cache', 'acid1b.npy'), mmap_mode='r')
def best(m, y):
    v = m[y, x0:x1 + 1, :2].astype(float).mean(axis=1)
    w = np.convolve(v, np.ones(4) / 4, 'valid')
    return w.max(), x0 + int(w.argmax()) + 2
rows = [(best(ms[0], y), best(ms[1], y)) for y in range(y0, y1)]
dark = [r[0][0] < thr and r[1][0] < thr for r in rows]
i = 0; n = 0; tot = 0
while i < len(dark):
    if not dark[i]: i += 1; continue
    j = i
    while j < len(dark) and dark[j]: j += 1
    if j - i >= minlen:
        xc = int(np.median([rows[k][1][1] for k in range(max(0, i - 6), i)] or [(x0 + x1) // 2]))
        px = a[y0 + i + 3:y0 + j - 3, xc - 2:xc + 3].astype(float).reshape(-1, 3)
        r, g, b = px.mean(axis=0) if len(px) else (0, 0, 0)
        kind = 'open?' if (abs(r - g) < 30 and b < 112 and r < 185) or g > r + 12 else 'protected'
        print('%d-%d  %3d px  max metal %3d  metal1 %3d   clean %3d/%3d/%3d at x %d  %s' % (
            y0 + i, y0 + j - 1, j - i, max(r_[0][0] for r_ in rows[i:j]), max(r_[1][0] for r_ in rows[i:j]), r, g, b, xc, kind))
        n += 1; tot += j - i
    i = j
print('%d dark stretches, %d px of %d' % (n, tot, len(rows)))
