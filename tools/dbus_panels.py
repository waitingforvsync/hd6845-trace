#!/usr/bin/env python3
"""Several different rectangles of the die in one image, each with its own grid labels.

usage: dbus_panels.py --scale S [--grid N] [--cols C] --out NAME  X,Y,W,H,LAYER [X,Y,W,H,LAYER ...]

LAYER: metal, metal1, acid (aligned), acid1b. Panels are laid out left to right, C per row
(default: all in one column). Each panel is labelled with its layer and has grid lines every
N px labelled with die coordinates. A bare NAME lands in cache/scratch/dbus/. No trace is
drawn: this is for looking at corners, ends and junctions of several wires at once.
"""
import argparse, os
import numpy as np, cv2
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
F = {'metal': 'metal.npy', 'acid1b': 'acid1b.npy', 'metal1': 'metal1.npy', 'acid': 'acid_aligned.npy'}
ap = argparse.ArgumentParser()
ap.add_argument('--scale', type=float, default=4.0)
ap.add_argument('--grid', type=int, default=50)
ap.add_argument('--cols', type=int, default=1)
ap.add_argument('--out', required=True)
ap.add_argument('rects', nargs='+')
a = ap.parse_args()
arrs = {}
panels = []
for r in a.rects:
    x, y, w, h, lay = r.split(',')
    x, y, w, h = int(x), int(y), int(w), int(h)
    if lay not in arrs:
        arrs[lay] = np.load(os.path.join(ROOT, 'cache', F[lay]), mmap_mode='r')
    p = np.ascontiguousarray(arrs[lay][y:y + h, x:x + w])
    p = cv2.resize(p, (int(w * a.scale), int(h * a.scale)), interpolation=cv2.INTER_CUBIC)
    p = cv2.cvtColor(p, cv2.COLOR_RGB2BGR)
    g = a.grid
    for gx in range((x // g + 1) * g, x + w, g):
        X = int((gx - x) * a.scale)
        cv2.line(p, (X, 0), (X, p.shape[0]), (255, 255, 0), 1)
        cv2.putText(p, str(gx), (X + 2, 11), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 0), 2)
        cv2.putText(p, str(gx), (X + 2, 11), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (255, 255, 255), 1)
    for gy in range((y // g + 1) * g, y + h, g):
        Y = int((gy - y) * a.scale)
        cv2.line(p, (0, Y), (p.shape[1], Y), (255, 255, 0), 1)
        cv2.putText(p, str(gy), (2, Y - 2), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 0), 2)
        cv2.putText(p, str(gy), (2, Y - 2), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (255, 255, 255), 1)
    cv2.putText(p, lay, (p.shape[1] - 60, p.shape[0] - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0), 2)
    cv2.putText(p, lay, (p.shape[1] - 60, p.shape[0] - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1)
    panels.append(p)
rows = []
for i in range(0, len(panels), a.cols):
    row = panels[i:i + a.cols]
    hh = max(p.shape[0] for p in row)
    row = [cv2.copyMakeBorder(p, 0, hh - p.shape[0], 0, 4, cv2.BORDER_CONSTANT, value=(255, 0, 255)) for p in row]
    rows.append(np.hstack(row))
ww = max(r.shape[1] for r in rows)
rows = [cv2.copyMakeBorder(r, 0, 4, 0, ww - r.shape[1], cv2.BORDER_CONSTANT, value=(255, 0, 255)) for r in rows]
img = np.vstack(rows)
out = a.out if os.sep in a.out else os.path.join(ROOT, 'cache', 'scratch', 'dbus', a.out)
os.makedirs(os.path.dirname(out), exist_ok=True)
cv2.imwrite(out, img)
print(out, img.shape[1], img.shape[0])
