#!/usr/bin/env python3
"""Block-by-block displacement of a mirrored copy of a cell against its master.

usage: dlat_shift.py [LAYER] [BLOCK] [SEARCH]     (defaults: acid1b 48 18)

The master rectangle is `dbus_lat`'s (17230,8885)-(17590,9370); the copy is the bit-5
latch of the column x 16488-16848 (mirrored about a vertical line, moved by -742,5444:
x' = 34078 - x, y' = y + 5444). For each BLOCK x BLOCK block of the mirrored master the
best normalised cross-correlation within +-SEARCH px in the copy is found; prints, per
block, dx,dy (how far the copy's feature lies from the mirrored master's place) and the
score. Text only. Written to see whether the copy is a rigid mirror image (it is not:
its metal contacts lie 6-12 px west of the mirrored places).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, cv2, view

lay = sys.argv[1] if len(sys.argv) > 1 else 'acid1b'
B = int(sys.argv[2]) if len(sys.argv) > 2 else 48
S = int(sys.argv[3]) if len(sys.argv) > 3 else 18
X0, Y0, X1, Y1 = 17230, 8885, 17590, 9370
W, H = X1 - X0, Y1 - Y0
CX0, CY0 = 34078 - X1, Y0 + 5444
gray = lambda a: cv2.cvtColor(np.ascontiguousarray(a[..., :3]), cv2.COLOR_RGB2GRAY)
m = gray(view.raw(lay, X0, Y0, W, H))[:, ::-1]
c = gray(view.raw(lay, CX0 - S, CY0 - S, W + 2 * S, H + 2 * S))
print(f"layer {lay}: block {B}, search +-{S}; columns are copy x, rows copy y; dx,dy score")
print('      ' + ''.join(f"{CX0 + bx:>14d}" for bx in range(0, W - B + 1, B)))
for by in range(0, H - B + 1, B):
    row = []
    for bx in range(0, W - B + 1, B):
        t = np.ascontiguousarray(m[by:by + B, bx:bx + B])
        if t.std() < 8:
            row.append('      -       '); continue
        w = np.ascontiguousarray(c[by:by + B + 2 * S, bx:bx + B + 2 * S])
        r = cv2.matchTemplate(w, t, cv2.TM_CCOEFF_NORMED)
        _, s, _, loc = cv2.minMaxLoc(r)
        row.append(f"{loc[0] - S:+4d},{loc[1] - S:+3d} {s:.2f} ")
    print(f"{CY0 + by:6d}" + ''.join(f"{v:>14s}" for v in row))
