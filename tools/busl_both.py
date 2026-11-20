#!/usr/bin/env python3
"""Runs along a cut where BOTH metal shots pass the follower's metal test (text).

usage: busl_both.py h Y X0 X1 [--half 2] [--min 6]     a row
       busl_both.py v X Y0 Y1 [--half 2] [--min 6]     a column

The test is tools/follow.py's (red > 177 and green > 128), on the median over 2*half+1 px across
the cut, in the chip-2 metal shot and in chip 1's (aligned). Bare ground that is bright in chip 2
only (tracing guide, trap 30) does not pass, so in a bundle of diagonals the runs printed are the
metals and not the ground between them. Prints each run as start-end centre(width). An aid for
placing centres; every end is still read on a view.
"""
import sys
import numpy as np
a = sys.argv[1:]
half = 2; mn = 6
if '--half' in a:
    i = a.index('--half'); half = int(a[i + 1]); del a[i:i + 2]
if '--min' in a:
    i = a.index('--min'); mn = int(a[i + 1]); del a[i:i + 2]
d, c, p0, p1 = a[0], int(a[1]), int(a[2]), int(a[3])
m2 = np.load('cache/metal.npy', mmap_mode='r')
m1 = np.load('cache/metal1.npy', mmap_mode='r')
def test(m):
    if d == 'h':
        w = np.asarray(m[c - half:c + half + 1, p0:p1, :3], dtype=float)
        w = np.median(w, axis=0)
    else:
        w = np.asarray(m[p0:p1, c - half:c + half + 1, :3], dtype=float)
        w = np.median(w, axis=1)
    return (w[:, 0] > 177) & (w[:, 1] > 128)
t = test(m2) & test(m1)
out = []; s = None
for i, v in enumerate(list(t) + [False]):
    if v and s is None:
        s = i
    elif not v and s is not None:
        if i - s >= mn:
            out.append('%d-%d %d(%d)' % (p0 + s, p0 + i - 1, p0 + (s + i - 1) // 2, i - s))
        s = None
print('%s %d:' % (d, c), '  '.join(out) if out else 'none')
