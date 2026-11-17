#!/usr/bin/env python3
"""Find large OPEN DIFFUSIONS in a rectangle that the trace does not draw as diffusion.

usage: TRACE=tc1 .venv/bin/python tools/tc1_green.py X0 Y0 X1 Y1 [--min AREA]

Why: in the top-centre logic the clean shot (acid1b) shows a LARGE diffusion in the open as
bright green, and open field as khaki-brown. The layer legend's "open diffusion is green"
and this block's "a diffusion wire in the open is not green" are both true (wires are
narrow, drains are large), and it is easy to read a green area as field. Calibrated
2026-11-17 on known spots (7x7 means, R/G/B):

                                   clean (acid1b)   chip-2 stripped (acid)   chip-2 metal
  large open diffusion (L2, L3 drains)  118/155/90      160/147/89               166/130/82
  open field, empty (7110,4250)         151/138/100     155/154/99               168/138/88
  field between two poly rows           90/104/61       143/139/87               167/152/85

So: clean shot green (G - R over 20, G over 130) AND chip-2 stripped shot R - G of 8 or
more (field is 0-4 there, diffusion 13-17) = large open diffusion. This tool marks those
pixels, groups them, and prints every group of at least AREA px2 (default 150) with the
share of it that the loaded trace covers with a diffusion item. A group with a low share is
a diffusion the trace calls nothing, or field.
It says nothing under metal (protected colours) and nothing about narrow strips.
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


def main():
    a = [t for t in sys.argv[1:] if not t.startswith('--')]
    x0, y0, x1, y1 = map(int, a[:4])
    amin = int(sys.argv[sys.argv.index('--min') + 1]) if '--min' in sys.argv else 150
    C = np.load(os.path.join(ROOT, 'cache', 'acid1b.npy'), mmap_mode='r')[y0:y1, x0:x1].astype(np.float32)
    A = np.load(os.path.join(ROOT, 'cache', 'acid_aligned.npy'), mmap_mode='r')[y0:y1, x0:x1].astype(np.float32)
    C = cv2.GaussianBlur(C, (0, 0), 1.5)
    A = cv2.GaussianBlur(A, (0, 0), 1.5)
    m = ((C[..., 1] - C[..., 0]) > 20) & (C[..., 1] > 130) & ((A[..., 0] - A[..., 1]) >= 8)
    m = cv2.morphologyEx(m.astype(np.uint8), cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
    n, lab, st, cen = cv2.connectedComponentsWithStats(m, connectivity=8)
    tr = tracelib.Trace()
    items = tr.items if hasattr(tr, 'items') else tr.all_items()
    dif = prep(unary_union([it.geom for it in items if it.layer == 'D']))
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


main()
