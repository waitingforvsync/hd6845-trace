#!/usr/bin/env python3
"""Mosaic of small windows round a list of points, one column per point, one row per shot.

usage: tl5_pads.py X,Y [X,Y ...] [--w 110] [--h 110] [--scale 4] [--layers metal,acid1b] --out NAME

Each window is centred on its point; a tick marks the centre and the point's coordinates are
printed on the tile. For checking pads, contacts and wire ends (and 50 px beyond them) in two
or more shots at once. Output goes to cache/scratch/tl5/ unless NAME has a folder.
"""
import argparse, os
import numpy as np, cv2
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
F = {'metal': 'metal.npy', 'acid1b': 'acid1b.npy', 'metal1': 'metal1.npy', 'acid': 'acid_aligned.npy'}
ap = argparse.ArgumentParser()
ap.add_argument('pts', nargs='+')
ap.add_argument('--w', type=int, default=110)
ap.add_argument('--h', type=int, default=110)
ap.add_argument('--scale', type=float, default=4.0)
ap.add_argument('--layers', default='metal,acid1b')
ap.add_argument('--out', required=True)
a = ap.parse_args()
rows = []
for L in a.layers.split(','):
    arr = np.load(os.path.join(ROOT, 'cache', F[L]), mmap_mode='r')
    tiles = []
    for p in a.pts:
        x, y = map(int, p.split(','))
        x0, y0 = x - a.w // 2, y - a.h // 2
        t = np.ascontiguousarray(arr[y0:y0 + a.h, x0:x0 + a.w])
        t = cv2.resize(t, (int(a.w * a.scale), int(a.h * a.scale)), interpolation=cv2.INTER_CUBIC)
        t = cv2.cvtColor(t, cv2.COLOR_RGB2BGR)
        H, W = t.shape[:2]
        for (cx, cy) in ((W // 2, 0), (W // 2, H - 1)):
            cv2.line(t, (cx, cy - 8), (cx, cy + 8), (255, 255, 0), 1)
        for (cx, cy) in ((0, H // 2), (W - 1, H // 2)):
            cv2.line(t, (cx - 8, cy), (cx + 8, cy), (255, 255, 0), 1)
        cv2.putText(t, '%d,%d %s' % (x, y, L), (4, 14), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 0), 3)
        cv2.putText(t, '%d,%d %s' % (x, y, L), (4, 14), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 255, 255), 1)
        cv2.rectangle(t, (0, 0), (W - 1, H - 1), (255, 0, 255), 1)
        tiles.append(t)
    rows.append(np.hstack(tiles))
img = np.vstack(rows)
out = a.out if os.sep in a.out else os.path.join(ROOT, 'cache', 'scratch', 'tl5', a.out)
os.makedirs(os.path.dirname(out), exist_ok=True)
cv2.imwrite(out, img)
print(out, img.shape[1], img.shape[0])
