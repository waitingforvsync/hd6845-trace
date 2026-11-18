#!/usr/bin/env python3
"""Several small squares of the die side by side, one row per shot: for checking many pads or
wire ends in one image.
usage: tools/tc2_tiles.py SIZE SCALE X,Y [X,Y ...] [--layers metal,acid1b] [--trace] --out NAME.png
Each X,Y is the centre of a SIZE x SIZE square. Keep (number of squares) x SIZE x SCALE under 1300."""
import argparse, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import view
from PIL import Image
ap = argparse.ArgumentParser()
ap.add_argument('size', type=int); ap.add_argument('scale', type=float)
ap.add_argument('pts', nargs='+')
ap.add_argument('--layers', default='metal,acid1b')
ap.add_argument('--grid', type=int, default=25)
ap.add_argument('--trace', action='store_true')
ap.add_argument('--out', default='tiles.png')
a = ap.parse_args()
rows = []
for l in a.layers.split(','):
    row = []
    for p in a.pts:
        x, y = map(int, p.split(','))
        row.append(view.panel(l, x - a.size // 2, y - a.size // 2, a.size, a.size, a.scale, a.grid, a.trace, None, False))
    rows.append(row)
pw, ph = rows[0][0].size
im = Image.new('RGB', ((pw + 4) * len(a.pts), (ph + 4) * len(rows)), (255, 0, 255))
for j, row in enumerate(rows):
    for i, p in enumerate(row):
        im.paste(p, (i * (pw + 4), j * (ph + 4)))
out = a.out if '/' in a.out else view.scratch_path(a.out)
im.save(out); print(out, im.size)
