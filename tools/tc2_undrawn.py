#!/usr/bin/env python3
"""Candidates for undrawn poly and diffusion in a rectangle: pixels of the clean shot (acid1b)
that have the protected colour of poly (salmon) or of diffusion (tan) and lie more than 8 px
from every drawn item of that layer (all loaded blocks: run with TRACE= for the whole chip),
grouped, largest first.

usage: TRACE= .venv/bin/python tools/tc2_undrawn.py X0 Y0 X1 Y1 [MINAREA]   (default 250 px2)

Colour rules (calibrated in tc2's region: notes/blocks/tc2.md, "Colours used"):
  poly under metal       R 205-255, G 140-185, B 95-135, R-G 40-75
  diffusion under metal  R 185-212, G 155-185, B 120-145, R-G 15-45
It sees nothing in the open (poly dark red-brown, diffusion pinkish there) and the colours
drift, so it lists candidates to look at, never findings: every group is then viewed."""
import sys, os
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tracelib
from PIL import Image, ImageDraw
from scipy import ndimage
x0, y0, x1, y1 = map(int, sys.argv[1:5]); mina = int(sys.argv[5]) if len(sys.argv) > 5 else 250
im = np.asarray(np.load(os.path.join(tracelib.ROOT, 'cache', 'acid1b.npy'), mmap_mode='r')[y0:y1, x0:x1, :3]).astype(int)
R, G, B = im[..., 0], im[..., 1], im[..., 2]
t = tracelib.Trace()
def mask(layers):
    m = Image.new('L', (x1 - x0, y1 - y0), 0); d = ImageDraw.Draw(m)
    for it in t.items:
        if it.layer in layers:
            g = it.geom.buffer(8)
            b = g.bounds
            if b[2] < x0 or b[0] > x1 or b[3] < y0 or b[1] > y1: continue
            for poly in (g.geoms if hasattr(g, 'geoms') else [g]):
                d.polygon([(px - x0, py - y0) for px, py in poly.exterior.coords], fill=1)
    return np.asarray(m).astype(bool)
rules = {'poly': ((R >= 205) & (G >= 140) & (G <= 185) & (B >= 95) & (B <= 135) & (R - G >= 40) & (R - G <= 75), 'P'),
         'diffusion': ((R >= 185) & (R <= 212) & (G >= 155) & (G <= 185) & (B >= 120) & (B <= 145) & (R - G >= 15) & (R - G <= 45), 'DCB')}
for name, (c, layers) in rules.items():
    c = ndimage.binary_opening(c & ~mask(layers), iterations=2)
    lab, n = ndimage.label(c)
    out = []
    for i, sl in enumerate(ndimage.find_objects(lab), 1):
        a = int((lab[sl] == i).sum())
        if a >= mina:
            out.append((a, x0 + sl[1].start, y0 + sl[0].start, x0 + sl[1].stop, y0 + sl[0].stop))
    print('%s: %d groups of %d px2 or more' % (name, len(out), mina))
    for a, ax, ay, bx, by in sorted(out, reverse=True)[:60]:
        print('  %5d px2  x %d-%d  y %d-%d' % (a, ax, bx, ay, by))
