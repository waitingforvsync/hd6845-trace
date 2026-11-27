#!/usr/bin/env python3
"""Walk a thin metal east and print where it is: for placing the ends of a diagonal.

usage: cdp4_track.py X0 Y0 X1 [STEP]     (run from the repository's root: it reads cache/*.npy)

It will walk a thin metal east from (X0,Y0) to X1, re-centring on the metal's bright
run in each column (max of chip-2 and chip-1 red, 5 px wide column strip, search +-7 px about the previous
centre), and print the centre every STEP px (default 20) and where the slope changes. An aid for placing
the ends of a diagonal; the result is checked on an overlay."""
import sys, numpy as np
m2 = np.load('cache/metal.npy', mmap_mode='r'); m1 = np.load('cache/metal1.npy', mmap_mode='r')
x0, y0, x1 = map(int, sys.argv[1:4]); step = int(sys.argv[4]) if len(sys.argv) > 4 else 20
y = float(y0); pts = []
for x in range(x0, x1 + 1, 2):
    yi = int(round(y))
    a = np.maximum(np.asarray(m2[yi-9:yi+10, x-2:x+3, 0], float).mean(axis=1), 0)
    b = np.asarray(m1[yi-9:yi+10, x-2:x+3, 0], float).mean(axis=1)
    ok = (a > 177) | (b > 177)
    idx = np.nonzero(ok)[0]
    if len(idx) >= 4:
        # take the run nearest the centre
        runs = np.split(idx, np.nonzero(np.diff(idx) > 1)[0] + 1)
        r = min(runs, key=lambda r: abs(r.mean() - 9))
        if len(r) >= 4 and abs(r.mean() - 9) <= 7:
            y = yi - 9 + r.mean()
    pts.append((x, y))
out = []
for i, (x, yy) in enumerate(pts):
    if (x - x0) % step == 0: out.append('%d,%d' % (x, round(yy)))
print(' '.join(out))
# slope changes: compare slope over 16 px windows
prev = None
for i in range(8, len(pts) - 8, 2):
    s = (pts[i+8][1] - pts[i-8][1]) / 32.0
    k = 0 if abs(s) < 0.25 else (-1 if s < 0 else 1)
    if prev is not None and k != prev: print('  slope %d -> %d near %d,%d' % (prev, k, pts[i][0], round(pts[i][1])))
    prev = k
