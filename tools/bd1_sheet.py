#!/usr/bin/env python3
"""A contact sheet: one row per point, the four shots side by side, as one image.

usage: bd1_sheet.py OUT.png [--half 30] [--scale 4] X,Y [X,Y ...]     (run from the repository's root)

Each row shows the square of +-HALF px about the point in chip-2 metal, chip-1 metal, the clean shot and chip 2's
stripped shot, enlarged SCALE times (nearest neighbour then smoothed as tools/view.py does not: plain bicubic),
with the point's coordinates printed on the row and a tick at the centre of each panel's top and left edge.
For looking at a list of flagged spots (tools/bd1_audit.py) in one read instead of one view each.
"""
import sys, numpy as np
from PIL import Image, ImageDraw
args = sys.argv[1:]; out = args.pop(0)
def opt(n, d):
    if n in args:
        i = args.index(n); v = int(args[i + 1]); del args[i:i + 2]; return v
    return d
half = opt('--half', 30); sc = opt('--scale', 4)
L = [np.load('cache/%s.npy' % n, mmap_mode='r') for n in ('metal', 'metal1', 'acid1b', 'acid_aligned')]
pts = [tuple(map(int, a.split(','))) for a in args]
side = 2 * half * sc
sheet = Image.new('RGB', (4 * side + 3 * 4, len(pts) * (side + 4)), (255, 0, 255))
d = ImageDraw.Draw(sheet)
for r, (x, y) in enumerate(pts):
    for c, a in enumerate(L):
        im = Image.fromarray(np.asarray(a[y - half:y + half, x - half:x + half, :3])).resize((side, side), Image.BICUBIC)
        ox, oy = c * (side + 4), r * (side + 4)
        sheet.paste(im, (ox, oy))
        d.line([(ox + side // 2, oy), (ox + side // 2, oy + 8)], fill=(0, 255, 255)); d.line([(ox, oy + side // 2), (ox + 8, oy + side // 2)], fill=(0, 255, 255))
    d.text((4, r * (side + 4) + 4), '%d,%d' % (x, y), fill=(255, 255, 0))
sheet.save(out); print(out, sheet.size)
