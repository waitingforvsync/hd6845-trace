#!/usr/bin/env python3
"""Several rectangles with the trace outlined, in one image (overlay checks of scattered spots).

usage: dbus_ovl.py LAYER SCALE OUT x,y,w,h [x,y,w,h ...] [--cols N] [--grid G]

Each rectangle is rendered with view.panel (trace outlined, not filled) and the panels are
laid out in N columns (default 1). Honours TRACE and HD_SCRATCH like view.py.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image
import view
def main():
    a = sys.argv[1:]
    cols, grid = 1, 50
    if '--cols' in a:
        i = a.index('--cols'); cols = int(a[i + 1]); del a[i:i + 2]
    if '--grid' in a:
        i = a.index('--grid'); grid = int(a[i + 1]); del a[i:i + 2]
    layer, scale, out = a[0], float(a[1]), a[2]
    ims = [view.panel(layer, *map(int, r.split(',')), scale=scale, grid=grid, trace=True, fill=False) for r in a[3:]]
    rows = [ims[i:i + cols] for i in range(0, len(ims), cols)]
    W = max(sum(im.width for im in r) + 4 * (len(r) - 1) for r in rows)
    H = sum(max(im.height for im in r) for r in rows) + 4 * (len(rows) - 1)
    canvas = Image.new('RGB', (W, H), (255, 0, 255))
    y = 0
    for r in rows:
        x = 0
        for im in r:
            canvas.paste(im, (x, y)); x += im.width + 4
        y += max(im.height for im in r) + 4
    p = view.scratch_path(out)
    canvas.save(p)
    print(p, canvas.size)
main()
