"""List the trace items of every block that touch a rectangle: tools/tl1_items.py x0 y0 x1 y1 [--full]
Run without TRACE to see all blocks. Used to find what is already drawn in the tl1 strip."""
import sys, collections
sys.path.insert(0, 'tools')
import tracelib
from shapely.geometry import box
a = [x for x in sys.argv[1:] if not x.startswith('--')]
x0, y0, x1, y1 = map(float, a[:4])
r = box(x0, y0, x1, y1)
t = tracelib.Trace()
cnt = collections.Counter()
for it in t.items:
    if it.geom.intersects(r):
        cnt[(it.src.split(':')[0], it.layer)] += 1
        if '--full' in sys.argv:
            b = it.geom.bounds
            print(it.src, it.layer, '?' if it.uncertain else '', [round(v) for v in b])
for k, v in sorted(cnt.items()):
    print(k, v)
for l in t.labels:
    if x0 <= l.x <= x1 and y0 <= l.y <= y1:
        print('label', l.src, l.layer, l.x, l.y, l.name)
