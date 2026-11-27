#!/usr/bin/env python3
"""List what lies under the wide VSS plane of `tlb` along horizontal cuts, as text.

usage: tlb_scan.py X0 X1 Y [Y ...]
       tlb_scan.py v Y0 Y1 X [X ...]     the same down vertical cuts

For each cut (median of 9 rows around Y, clean shot acid1b): runs of poly colour
(R > 175 and R - G > 30, at least 8 px) and of dark edge (max channel < 110, at least 4 px).
Under this plane the clean shot's field is fringed green and pink, so only poly (salmon with
dark edges) is reliable; anything this lists must be looked at on a view.
"""
import os, sys
import numpy as np
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
a = np.load(os.path.join(ROOT, 'cache', 'acid1b.npy'), mmap_mode='r')
V = sys.argv[1] == 'v'
if V: del sys.argv[1]
x0, x1 = int(sys.argv[1]), int(sys.argv[2])
def runs(mask, minlen):
    out = []; s = None
    for i, m in enumerate(mask):
        if m and s is None: s = i
        if not m and s is not None:
            if i - s >= minlen: out.append((x0 + s, x0 + i - 1))
            s = None
    return out
for y in map(int, sys.argv[3:]):
    p = (np.median(np.asarray(a[x0:x1, y-4:y+5, :3]).astype(int), axis=1) if V else
         np.median(np.asarray(a[y-4:y+5, x0:x1, :3]).astype(int), axis=0))
    R, G = p[:, 0], p[:, 1]
    poly = (R > 175) & (R - G > 30)
    dark = p.max(axis=1) < 110
    print('x' if V else 'y', y, 'poly', ' '.join('%d-%d' % r for r in runs(poly, 8)))
    print('x' if V else 'y', y, 'dark', ' '.join('%d-%d' % r for r in runs(dark, 4)))
