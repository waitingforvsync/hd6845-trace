#!/usr/bin/env python3
"""Where does a rectangle repeat nearby? dbus_localmatch.py x0 y0 x1 y1 dx0 dy0 [radius] [layer]

Normalised cross-correlation of the master rectangle (metal-shot pixels) against a window
around the guessed offset (dx0, dy0), searched +-radius px (default 20), at full resolution.
Prints the best offset and score per layer. Much faster than findcell.py when the copy's
place is roughly known. Check the placement by overlay all the same.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, cv2, view
x0, y0, x1, y1, dx0, dy0 = map(int, sys.argv[1:7])
r = int(sys.argv[7]) if len(sys.argv) > 7 else 20
layers = sys.argv[8].split(',') if len(sys.argv) > 8 else ['acid1b', 'metal', 'acid']
for lay in layers:
    t = cv2.cvtColor(np.ascontiguousarray(view.raw(lay, x0, y0, x1 - x0, y1 - y0)[..., :3]), cv2.COLOR_RGB2GRAY)
    w = cv2.cvtColor(np.ascontiguousarray(view.raw(lay, x0 + dx0 - r, y0 + dy0 - r, x1 - x0 + 2 * r, y1 - y0 + 2 * r)[..., :3]), cv2.COLOR_RGB2GRAY)
    m = cv2.matchTemplate(w, t, cv2.TM_CCOEFF_NORMED)
    _, s, _, loc = cv2.minMaxLoc(m)
    print(f"{lay:7s} best offset {dx0 - r + loc[0]},{dy0 - r + loc[1]}  score {s:.2f}")
