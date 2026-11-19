#!/usr/bin/env python3
"""Lists every trace item of every package that touches a rectangle (text; no image).

usage: busl_items.py X0 Y0 X1 Y1 [--layer M|P|D|C|B]

One line per item: layer (with ? if uncertain), its bounding box, the part of it inside the
rectangle, and the file and line it comes from. For a survey of what neighbours already draw.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.pop('TRACE', None)
import tracelib
from shapely.geometry import box

a = sys.argv[1:]
lay = None
if '--layer' in a:
    i = a.index('--layer'); lay = a[i + 1]; del a[i:i + 2]
x0, y0, x1, y1 = map(int, a[:4])
t = tracelib.Trace()
b = box(x0, y0, x1, y1)
rows = []
for it in t.query(x0, y0, x1, y1):
    if lay and it.layer != lay: continue
    g = it.geom.intersection(b)
    if g.is_empty or g.area < 1: continue
    bb = tuple(int(round(v)) for v in it.geom.bounds)
    cb = tuple(int(round(v)) for v in g.bounds)
    rows.append((it.layer, cb, bb, it.uncertain, os.path.relpath(it.src.split(' <- ')[0], tracelib.ROOT)))
for l, cb, bb, u, s in sorted(rows, key=lambda r: (r[0], r[1])):
    print('%s%s in %d,%d:%d,%d  whole %d,%d:%d,%d  %s' % ('?' if u else ' ', l, *cb, *bb, s))
