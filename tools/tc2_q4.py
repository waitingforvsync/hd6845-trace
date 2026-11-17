#!/usr/bin/env python3
"""Four shots of one rectangle in a 2 x 2 tile (clean, chip-2 stripped / chip-2 metal, chip-1 metal).
usage: tools/tc2_q4.py X Y W H --scale S [--grid N] [--trace] [--layers a,b,c,d] --out NAME.png
Keep W x S and H x S under about 640 so that the tile stays under 1300 px a side."""
import argparse, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import view
from PIL import Image

ap = argparse.ArgumentParser()
ap.add_argument('x', type=int); ap.add_argument('y', type=int)
ap.add_argument('w', type=int); ap.add_argument('h', type=int)
ap.add_argument('--scale', type=float, default=4.0)
ap.add_argument('--grid', type=int, default=25)
ap.add_argument('--trace', action='store_true')
ap.add_argument('--layers', default='acid1b,acid,metal,metal1')
ap.add_argument('--out', default='q4.png')
a = ap.parse_args()
ls = a.layers.split(',')
ps = [view.panel(l, a.x, a.y, a.w, a.h, a.scale, a.grid, a.trace, None, False) for l in ls]
pw, ph = ps[0].size
cols = 2
rows = (len(ps) + 1) // 2
im = Image.new('RGB', (pw * cols + 6, ph * rows + 6 * (rows - 1)), (255, 0, 255))
for i, p in enumerate(ps):
    im.paste(p, ((i % 2) * (pw + 6), (i // 2) * (ph + 6)))
out = a.out if '/' in a.out else view.scratch_path(a.out)
im.save(out)
print(out, im.size)
