"""List every drawn item of the loaded trace files that touches a rectangle.
usage: tools/tc2_items.py X0 Y0 X1 Y1      (TRACE= for all blocks)
Prints layer, uncertain flag, bounds, net name (from the extraction) where known."""
import sys
sys.path.insert(0, 'tools')
import tracelib
from shapely.geometry import box
x0, y0, x1, y1 = map(float, sys.argv[1:5])
t = tracelib.Trace()
r = box(x0, y0, x1, y1)
for it in t.items:
    g = getattr(it, 'geom', None)
    if g is None or not g.intersects(r):
        continue
    b = [int(v) for v in g.bounds]
    print(getattr(it, 'layer', '?'), '?' if getattr(it, 'unsure', False) else ' ', b,
          getattr(it, 'block', ''), getattr(it, 'src', ''), getattr(it, 'line', ''))
