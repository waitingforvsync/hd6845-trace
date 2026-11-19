#!/usr/bin/env python3
"""How much of the die is traced, and which parts no work package covers.

usage: coverage.py [--out cache/scratch/cov/coverage.jpg] [--width 1300]

Rasterises every trace item at 1/25 scale and grows it by 100 die px (traced area);
reads every region "x0-x1 x y0-y1" from notes/work-packages.md (package area). Draws the
die (chip-2 metal shot) with:
  green  traced
  yellow not traced, inside some package's region (a package should pick it up)
  red    not traced and in no package's region: a gap in the master list
Supply metal, open field and the die margin show red or yellow too: read the picture,
not only the numbers. Then prints, for each of the 40 pads, how much of the pad square
carries traced metal (the pad squares are drawn only where someone drew them).
"""
import argparse
import os
import re
import sys

import numpy as np
from PIL import Image, ImageDraw

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tracelib

ROOT = tracelib.ROOT
W, H = 19838, 21025
S = 25                       # die px per raster px
REGION_RE = re.compile(r'(\d+)\s*-\s*(\d+)\s*x\s*(\d+)\s*-\s*(\d+)')


def polys(g):
    if g.geom_type == 'Polygon':
        return [g]
    return [p for p in getattr(g, 'geoms', []) if p.geom_type == 'Polygon']


def raster(items):
    im = Image.new('L', (W // S + 1, H // S + 1), 0)
    d = ImageDraw.Draw(im)
    for it in items:
        for p in polys(it.geom):
            pts = [(x / S, y / S) for x, y in p.exterior.coords]
            if len(pts) >= 3:
                d.polygon(pts, fill=255)
    return np.array(im) > 0


def grow(m, r):
    from scipy.ndimage import binary_dilation
    return binary_dilation(m, iterations=r)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', default=os.path.join(ROOT, 'cache', 'scratch', 'cov', 'coverage.jpg'))
    ap.add_argument('--width', type=int, default=1300)
    a = ap.parse_args()

    tr = tracelib.Trace()
    traced = raster(tr.items)
    try:
        traced_g = grow(traced, 4)
    except ImportError:
        traced_g = traced
    metal = raster(tr.by_layer('M'))

    master = open(os.path.join(ROOT, 'notes', 'work-packages.md')).read()
    pk = np.zeros_like(traced)
    for x0, x1, y0, y1 in (tuple(int(v) for v in m.groups()) for m in REGION_RE.finditer(master)):
        pk[y0 // S:y1 // S + 1, x0 // S:x1 // S + 1] = True
    # The stricter test: only the regions of rows in the Queue, which is what /trace6845 picks
    # from. A region named only by a done or partial row with no queue row is picked by no one
    # (2026-11-19: twelve partial packages and a strip west of the datapath were in that state).
    qtext = master.split('\n## Queue', 1)[1] if '\n## Queue' in master else ''
    qk = np.zeros_like(traced)
    for line in qtext.split('\n'):
        if not line.startswith('| `'):
            continue
        cells = line.split('|')
        for m in REGION_RE.finditer(cells[2] if len(cells) > 2 else ''):
            x0, x1, y0, y1 = (int(v) for v in m.groups())
            qk[y0 // S:y1 // S + 1, x0 // S:x1 // S + 1] = True

    gh, gw = traced.shape
    print('traced (grown 100 px): %.1f %% of the die rectangle' % (100 * traced_g.mean()))
    print('in some package region: %.1f %%' % (100 * pk.mean()))
    print('neither: %.1f %%' % (100 * (~traced_g & ~pk).mean()))
    print('in a Queue row\'s region: %.1f %%; untraced and in no Queue row: %.1f %%'
          % (100 * qk.mean(), 100 * (~traced_g & ~qk).mean()))

    photo = np.load(os.path.join(ROOT, 'cache', 'metal.npy'), mmap_mode='r') \
        if os.path.exists(os.path.join(ROOT, 'cache', 'metal.npy')) else None
    if photo is not None:
        base = np.asarray(Image.fromarray(np.ascontiguousarray(photo[::S, ::S][:gh, :gw])).convert('RGB'),
                          dtype=np.float32)
    else:
        base = np.full((gh, gw, 3), 128, np.float32)
    bh, bw = base.shape[:2]
    traced_g, pk = traced_g[:bh, :bw], pk[:bh, :bw]
    gh, gw = bh, bw
    tint = np.zeros_like(base)
    tint[traced_g] = (0, 200, 0)
    tint[~traced_g & pk] = (255, 220, 0)
    tint[~traced_g & ~pk] = (255, 0, 0)
    img = (0.55 * base + 0.45 * tint).clip(0, 255).astype(np.uint8)
    out = Image.fromarray(img)
    out = out.resize((a.width, int(a.width * gh / gw)))
    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    out.save(a.out, quality=88)
    print('picture:', a.out)

    print('\npads: traced metal over the central 300 x 300 px of each pad square')
    for line in open(os.path.join(ROOT, 'floorplan.txt')):
        m = re.match(r'(\d+),(\d+):(\d+),(\d+)\s+pad\s+(\d+)\s+(\S+)', line)
        if not m:
            continue
        x0, y0, x1, y1 = (int(v) for v in m.groups()[:4])
        cx, cy = (x0 + x1) // 2, (y0 + y1) // 2
        sub = metal[(cy - 150) // S:(cy + 150) // S, (cx - 150) // S:(cx + 150) // S]
        print('  pin %-3s %-8s %3.0f %%' % (m.group(5), m.group(6), 100 * sub.mean()))


if __name__ == '__main__':
    main()
