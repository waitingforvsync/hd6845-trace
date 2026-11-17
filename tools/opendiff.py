#!/usr/bin/env python3
"""Find large OPEN DIFFUSIONS in a rectangle that the trace does not draw as diffusion.

usage: tools/t.sh BLOCK opendiff.py X0 Y0 X1 Y1 [--min AREA] [--rg N]

Why (tracing guide, trap 21): in the clean shot (acid1b) a LARGE diffusion in the open is
bright green, and open field is khaki-brown; `tools/classmap.py` (without --open) paints
both pale green, its colour for field in the open, and a green area is easily read as
field. The chip-2 stripped shot separates them. Calibrated 2026-11-17 in `tc1` on known
spots (7x7 means, R/G/B):

                                   clean (acid1b)   chip-2 stripped (acid)   chip-2 metal
  large open diffusion (L2, L3 drains)  118/155/90      160/147/89               166/130/82
  open field, empty (7110,4250)         151/138/100     155/154/99               168/138/88
  field between two poly rows           90/104/61       143/139/87               167/152/85

So: clean shot green (G - R over 20, G over 130) AND chip-2 stripped shot R - G of 8 or
more (field is 0-4 there, diffusion 13-17) = large open diffusion. This tool marks those
pixels, groups them, and prints every group of at least AREA px2 (default 150) with the
share of it that the loaded trace covers with a diffusion item. A group with a low share is
a diffusion the trace calls nothing, or field. --rg N changes the chip-2 threshold
(default 8).

Limits: it says nothing under metal (protected colours) and nothing about narrow strips (a
diffusion wire in the open is not green). The thresholds were measured in the top-centre
logic; the clean shot's colours drift across the die (trap 1), so before trusting an empty
list elsewhere, run it over a known open drain near your region and see that it is listed
(`tools/px.py pt X,Y acid1b,acid,metal` gives the three colours of a spot).

The shared form of tools/tc1_green.py: with the default thresholds the output is the same.
"""
import os
import sys
import numpy as np
import cv2

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tracelib
from shapely.geometry import Point
from shapely.ops import unary_union
from shapely.prepared import prep

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def opt(name, default):
    return int(sys.argv[sys.argv.index(name) + 1]) if name in sys.argv else default


def main():
    a, skip = [], False
    for t in sys.argv[1:]:
        if skip:
            skip = False
        elif t in ('--min', '--rg'):
            skip = True
        elif not t.startswith('--'):
            a.append(t)
    if len(a) < 4:
        sys.exit(__doc__)
    x0, y0, x1, y1 = map(int, a[:4])
    amin = opt('--min', 150)
    rg = opt('--rg', 8)
    C = np.load(os.path.join(ROOT, 'cache', 'acid1b.npy'), mmap_mode='r')[y0:y1, x0:x1].astype(np.float32)
    A = np.load(os.path.join(ROOT, 'cache', 'acid_aligned.npy'), mmap_mode='r')[y0:y1, x0:x1].astype(np.float32)
    C = cv2.GaussianBlur(C, (0, 0), 1.5)
    A = cv2.GaussianBlur(A, (0, 0), 1.5)
    m = ((C[..., 1] - C[..., 0]) > 20) & (C[..., 1] > 130) & ((A[..., 0] - A[..., 1]) >= rg)
    m = cv2.morphologyEx(m.astype(np.uint8), cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
    n, lab, st, cen = cv2.connectedComponentsWithStats(m, connectivity=8)
    tr = tracelib.Trace()
    dif = prep(unary_union([it.geom for it in tr.items if it.layer == 'D']))
    rows = []
    for i in range(1, n):
        if st[i, cv2.CC_STAT_AREA] < amin:
            continue
        ys, xs = np.nonzero(lab == i)
        idx = np.arange(0, len(xs), max(1, len(xs) // 200))
        inside = sum(dif.contains(Point(x0 + xs[k], y0 + ys[k])) for k in idx) / len(idx)
        rows.append((st[i, cv2.CC_STAT_AREA], x0 + st[i, 0], y0 + st[i, 1], x0 + st[i, 0] + st[i, 2], y0 + st[i, 1] + st[i, 3], inside))
    print('green (large open diffusion by the rule) groups of %d px2 or more in %d-%d x %d-%d:' % (amin, x0, x1, y0, y1))
    for ar, ax0, ay0, ax1, ay1, ins in sorted(rows, key=lambda r: (r[2], r[1])):
        print('  %5d px2  x %d-%d  y %d-%d   drawn as diffusion: %3d%%' % (ar, ax0, ax1, ay0, ay1, round(100 * ins)))
    if not rows:
        print('  none')


if __name__ == '__main__':
    main()
