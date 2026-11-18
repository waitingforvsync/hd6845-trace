#!/usr/bin/env python3
"""List the items of all trace files (not tl5's) that lie in a rectangle: tl5_others.py x0 y0 x1 y1.
Used to see what other blocks have drawn in the strip before joining onto it."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
os.environ['TRACE'] = ''
import tracelib
from shapely.geometry import box
x0, y0, x1, y1 = map(float, sys.argv[1:5])
r = box(x0, y0, x1, y1)
t = tracelib.Trace()
for it in t.items:
    if it.src.startswith('tl5'):
        continue
    if it.geom.intersects(r):
        b = it.geom.bounds
        print(it.layer, ('?' if it.uncertain else ' '), '%d,%d:%d,%d' % b, it.src, it.block)
for l in t.labels:
    if x0 <= l.x <= x1 and y0 <= l.y <= y1:
        print('N', l.layer, l.x, l.y, l.name, l.src)
