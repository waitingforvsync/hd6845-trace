#!/usr/bin/env python3
"""Centres of the row lines crossing a vertical cut, from the chip-2 metal shot (text).

usage: busl_rowy.py X Y0 Y1 [--half 2] [--horizontal]

Down the column X (mean over 2*half+1 px across) it finds the dark edge lines (red under 110)
and pairs each with the next one 14-34 px further on when the strip between them is bright
(red over 125). Prints for each pair the two edges, the centre, the width between the edge
centres, the strip's mean colour and a guess of the layer from its blue (poly under 70,
diffusion 75 and over; calibrated in the left bus field's open columns: poly 52-57, diffusion
80-87). With --horizontal the cut is the row Y=X and runs from X0=Y0 to X1=Y1 (for vertical
lines). Use it in a column with no metal above. An aid for placing rows; not evidence of
where a row ends.
"""
import sys, argparse
import numpy as np
ap = argparse.ArgumentParser()
ap.add_argument('x', type=int); ap.add_argument('y0', type=int); ap.add_argument('y1', type=int)
ap.add_argument('--half', type=int, default=2)
ap.add_argument('--horizontal', action='store_true')
a = ap.parse_args()
m = np.load('cache/metal.npy', mmap_mode='r')
if a.horizontal:
    s = np.asarray(m[a.x - a.half:a.x + a.half + 1, a.y0:a.y1, :3], dtype=float).mean(axis=0)
else:
    s = np.asarray(m[a.y0:a.y1, a.x - a.half:a.x + a.half + 1, :3], dtype=float).mean(axis=1)
dark = s[:, 0] < 110
runs = []
i = 0
while i < len(dark):
    if dark[i]:
        j = i
        while j < len(dark) and dark[j]:
            j += 1
        runs.append((i, j - 1)); i = j
    else:
        i += 1
used = set()
for k in range(len(runs) - 1):
    if k in used:
        continue
    a0, a1 = runs[k]; b0, b1 = runs[k + 1]
    ca, cb = (a0 + a1) / 2, (b0 + b1) / 2
    if 14 <= cb - ca <= 34 and b0 - a1 > 4:
        mid = s[a1 + 2:b0 - 1].mean(axis=0)
        if mid[0] > 125:
            kind = 'poly' if mid[2] < 70 else ('diffusion' if mid[2] >= 75 else '?')
            print('edges %d..%d / %d..%d  centre %.0f  width %.0f  strip %3.0f/%3.0f/%3.0f  %s' % (
                a.y0 + a0, a.y0 + a1, a.y0 + b0, a.y0 + b1, a.y0 + (ca + cb) / 2, cb - ca, mid[0], mid[1], mid[2], kind))
            used.add(k + 1)
