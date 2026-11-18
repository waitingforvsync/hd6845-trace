#!/usr/bin/env python3
"""A poly row (or column) in the top-left bus fields as one line of text, from the clean shot.

usage: tl2_row.py row Y X0 X1 [--step 4] [--half 3]
       tl2_row.py col X Y0 Y1 [--step 4] [--half 3]

Each character is the median colour of a patch (step px along the line, 2*half+1 across it) of
the clean shot (acid1b), classed with the colours measured in the bus field x 3085-3540 of the
top-left logic (tl2's notes): P salmon, poly under metal (R >= 195, G >= 150); p poly in the
open, dark and speckled (B < 95, R > G + 15); g green or grey-green, a contact hole or the
rim of an open poly (G >= R - 5); f pink, field (R > 175, G < 150, B >= 95); . anything else.
A ruler line gives x (or y) every 100 px. A hint for where a row runs and where it stops: an
end it reports is then looked at in a view (tracing guide, traps 8 and 12).
"""
import sys, os, argparse
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import view

ap = argparse.ArgumentParser()
ap.add_argument('kind', choices=['row', 'col'])
ap.add_argument('c', type=int)
ap.add_argument('a0', type=int)
ap.add_argument('a1', type=int)
ap.add_argument('--step', type=int, default=4)
ap.add_argument('--half', type=int, default=3)
a = ap.parse_args()
n = a.a1 - a.a0
if a.kind == 'row':
    im = view.raw('acid1b', a.a0, a.c - a.half, n, 2 * a.half + 1).astype(float)   # h, w, 3
    im = im.transpose(1, 0, 2)                                                    # along, across, 3
else:
    im = view.raw('acid1b', a.c - a.half, a.a0, 2 * a.half + 1, n).astype(float)
out = []
for i in range(0, n - a.step + 1, a.step):
    r, g, b = np.median(im[i:i + a.step].reshape(-1, 3), axis=0)
    if r >= 195 and g >= 150:
        ch = 'P'
    elif g >= r - 5:
        ch = 'g'
    elif b < 95 and r > g + 15:
        ch = 'p'
    elif r > 175 and g < 150 and b >= 95:
        ch = 'f'
    else:
        ch = '.'
    out.append(ch)
ruler = [' '] * len(out)
for v in range((a.a0 // 100 + 1) * 100, a.a1, 100):
    k = (v - a.a0) // a.step
    for j, c in enumerate(str(v)):
        if k + j < len(ruler):
            ruler[k + j] = c
print(''.join(ruler))
print(''.join(out))
