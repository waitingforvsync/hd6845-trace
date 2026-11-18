#!/usr/bin/env python3
"""Checks of the five unit loads (piece 8), as text.
usage: tools/tc2_loadchk.py
For each copy (dy): (1) the clean shot down the gate at x 8088 and x 8114: where the poly is
channel-bright (R > 235), i.e. the channel's extent in y; (2) along the band's row and a field
row above it, x 8056-8066: the darkest red value in both metal shots (a diffusion outline is
dark, an opening is not) and whether the clean shot shows the green of open field in the gap."""
import os, numpy as np
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
L = {n: np.load(os.path.join(ROOT, 'cache', f + '.npy'), mmap_mode='r') for n, f in
     (('metal', 'metal'), ('metal1', 'metal1'), ('clean', 'acid1b'))}
def px(n, x, y):
    return np.asarray(L[n][y - 1:y + 2, x - 1:x + 2, :3]).astype(int).reshape(-1, 3).mean(0)
for dy in (-499, -369, -130, 0, 130):
    out = ['dy %5d' % dy]
    for x in (8088, 8114):
        ys = [y for y in range(5215 + dy, 5345 + dy) if px('clean', x, y)[0] > 235]
        out.append('x %d bright y %d-%d (%d)' % (x, ys[0] - dy, ys[-1] - dy, ys[-1] - ys[0] + 1))
    for name, y in (('band', 5290), ('field', 5255)):
        m = min(px('metal', x, y + dy)[0] for x in range(8054, 8066))
        m1 = min(px('metal1', x, y + dy)[0] for x in range(8054, 8066))
        g = max(px('clean', x, y + dy)[1] - px('clean', x, y + dy)[0] for x in range(8044, 8060))
        out.append('%s row: darkest R chip2 %d chip1 %d, clean max G-R %d' % (name, m, m1, g))
    print('; '.join(out))
