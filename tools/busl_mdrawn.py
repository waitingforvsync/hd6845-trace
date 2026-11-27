#!/usr/bin/env python3
"""The metals crossing a cut, and which of them some package draws (text).

usage: busl_mdrawn.py h Y X0 X1 [--half 2] [--min 6]     a row
       busl_mdrawn.py v X Y0 Y1 [--half 2] [--min 6]     a column

The runs along the cut where both metal shots pass the follower's metal test (as
tools/busl_both.py), one per line: start-end, centre, width, and the file and line of the metal
item of any package (every trace file, uncertain items too) that covers the run's centre, or
UNDRAWN. For finding the tracks of a wiring field that are left. A thin or dim metal does not
pass the test (tracing guide, trap 19) and is not listed: an aid, not a list of all metals.
"""
import os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.pop('TRACE', None)
import tracelib
from shapely.geometry import Point
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
        w = np.median(np.asarray(m[c - half:c + half + 1, p0:p1, :3], dtype=float), axis=0)
    else:
        w = np.median(np.asarray(m[p0:p1, c - half:c + half + 1, :3], dtype=float), axis=1)
    return (w[:, 0] > 177) & (w[:, 1] > 128)
t = test(m2) & test(m1)
tr = tracelib.Trace()
if d == 'h': items = tr.query(p0, c - 5, p1, c + 5)
else: items = tr.query(c - 5, p0, c + 5, p1)
items = [it for it in items if it.layer == 'M']
s = None; n = 0; u = 0
for i, v in enumerate(list(t) + [False]):
    if v and s is None: s = i
    elif not v and s is not None:
        if i - s >= mn:
            mid = p0 + (s + i - 1) // 2
            pt = Point(mid, c) if d == 'h' else Point(c, mid)
            who = [it for it in items if it.geom.contains(pt)]
            n += 1
            if who:
                w = '%s%s' % ('?' if who[0].uncertain else '', os.path.relpath(who[0].src.split(' <- ')[0], tracelib.ROOT))
            else:
                w = 'UNDRAWN'; u += 1
            print('%d-%d  %d (%d)  %s' % (p0 + s, p0 + i - 1, mid, i - s, w))
        s = None
print('%s %d: %d metals, %d undrawn' % (d, c, n, u))
