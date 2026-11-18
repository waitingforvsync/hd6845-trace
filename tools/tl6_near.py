"""List the items of every trace file whose bounding box meets a rectangle.
   tools/tl6_near.py X0 Y0 X1 Y1 [--skip a,b]   (text; run with TRACE= for all blocks)"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
import tracelib
from shapely.geometry import box
a = sys.argv[1:]
x0, y0, x1, y1 = map(float, a[:4])
skip = a[5].split(',') if len(a) > 5 and a[4] == '--skip' else []
t = tracelib.Trace()
r = box(x0, y0, x1, y1)
for it in t.items:
    g = getattr(it, 'geom', None)
    if g is None or not g.intersects(r): continue
    blk = getattr(it, 'block', '?')
    if blk in skip: continue
    b = g.intersection(r).bounds
    print(blk, it.layer, ('?' if getattr(it, 'unsure', False) else ''), [round(v) for v in b], getattr(it, 'src', ''))
