#!/usr/bin/env python3
"""Extent of a poly row or column on a cut across it, from the two stripped shots (text).

usage: regs_polyy.py col X Y0 Y1 [X ...]     cuts down columns X: the runs of y where the cut reads poly
       regs_polyy.py row Y X0 X1 [Y ...]     cuts along rows Y

Two tests per cut, each on the 5 px median across the cut: (a) clean shot (acid1b, chip 1) red
minus green over 40 with red over 150 (poly under metal is salmon, 220/160; poly in the open
red-brown) and (b) chip-2 stripped shot (acid, aligned) red minus green over 22 with red over 110
(poly orange). Prints the runs of 8 px or more of each as start-end centre(width). An aid for
placing a row that views have already shown; it does not tell poly from a diffusion under metal
(tracing guide, trap 39), and dark edge lines split a run.
"""
import os, sys
import numpy as np
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ld = lambda n: np.load(os.path.join(ROOT, 'cache', n), mmap_mode='r')
a = sys.argv[1:]
if len(a) < 4 or a[0] not in ('col', 'row'):
    sys.exit(__doc__)
kind = a[0]
c0, lo, hi = int(a[1]), int(a[2]), int(a[3])
cuts = [c0] + [int(v) for v in a[4:]]
shots = (('clean', ld('acid1b.npy'), 40, 150), ('chip-2 stripped', ld('acid_aligned.npy'), 22, 110))


def runs(t, a0, mn=8):
    out = []; s = None
    for i, v in enumerate(list(t) + [False]):
        if v and s is None:
            s = i
        if not v and s is not None:
            if i - s >= mn:
                out.append((a0 + s, a0 + i - 1))
            s = None
    return out


for c in cuts:
    line = []
    for name, arr, d, rmin in shots:
        if kind == 'col':
            s = np.asarray(arr[lo:hi, c - 2:c + 3, :3]).astype(float)
            m = np.median(s, axis=1)
        else:
            s = np.asarray(arr[c - 2:c + 3, lo:hi, :3]).astype(float)
            m = np.median(s, axis=0)
        t = (m[:, 0] - m[:, 1] > d) & (m[:, 0] > rmin)
        line.append('%s: %s' % (name, ' '.join('%d-%d %d(%d)' % (p, q, (p + q) // 2, q - p + 1) for p, q in runs(t, lo)) or 'none'))
    print('%s %d   %s' % (kind, c, '   '.join(line)))
