#!/usr/bin/env python3
"""Runs of poly-coloured pixels along rows (or columns), as text: dlat_polyruns.py row|col A B0 B1 [A ...]

row Y X0 X1 [Y ...]: for each y, the x runs (5 px or longer) where the clean shot is protected
poly (salmon: R > 190, R - G 35..75, G - B > 25) and where the chip-2 stripped shot is poly
(orange: R - G > 28, R > 105). col X Y0 Y1 [X ...] the same down columns. Each sample is a
3x3 mean. For following a poly that runs partly under metal (salmon in the clean shot) and
partly in the open (orange in chip 2): the tracing guide's trap 10. Not evidence of a
contact or a join; look at the junctions.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, view
mode = sys.argv[1]; b0, b1 = int(sys.argv[3]), int(sys.argv[4])
As = [int(sys.argv[2])] + [int(a) for a in sys.argv[5:]]
def runs(m, base):
    out = []; i = 0; n = len(m)
    while i < n:
        if m[i]:
            j = i
            while j < n and m[j]: j += 1
            if j - i >= 5: out.append(f"{base+i}-{base+j-1}")
            i = j
        else: i += 1
    return ' '.join(out) or '-'
for a in As:
    res = []
    for lay in ('acid1b', 'acid'):
        if mode == 'row':
            p = view.raw(lay, b0, a - 1, b1 - b0, 3)[..., :3].astype(float).mean(axis=0)
        else:
            p = view.raw(lay, a - 1, b0, 3, b1 - b0)[..., :3].astype(float).mean(axis=1)
        R, G, B = p[:, 0], p[:, 1], p[:, 2]
        m = ((R > 190) & (R - G > 35) & (R - G < 75) & (G - B > 25)) if lay == 'acid1b' else ((R - G > 28) & (R > 105))
        res.append(runs(m, b0))
    print(f"{mode} {a}: clean salmon {res[0]}   |   chip-2 orange {res[1]}")
