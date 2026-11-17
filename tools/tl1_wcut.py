#!/usr/bin/env python3
"""Where could a vertical thin metal be cut?  usage: tl1_wcut.py X0 X1 Y0 Y1 [MINLEN]

For each row the mean colour across X0..X1 (the line's own width, inside its edge lines) in
both metal shots is classed: M metal (R > 177 and G > 128), D dark (R < 115: an edge line, a
ring, metal on a slope), G ground-like (neither: bare ground reads about 150/140 in chip 2
and 120-140/110-125 in chip 1). A cut needs bare ground between two end edges. Prints every
run of at least MINLEN rows (default 6) that is not metal in either shot, with its classes
per shot as a string (one character per 2 rows).
"""
import os, sys
import numpy as np
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
x0, x1, y0, y1 = map(int, sys.argv[1:5])
minlen = int(sys.argv[5]) if len(sys.argv) > 5 else 6
ms = [np.load(os.path.join(ROOT, 'cache', f), mmap_mode='r') for f in ('metal.npy', 'metal1.npy')]
def cls(m, y):
    r, g = m[y, x0:x1 + 1, :2].astype(float).mean(axis=0)
    return 'M' if r > 177 and g > 128 else 'D' if r < 115 else 'G'
c = [(cls(ms[0], y), cls(ms[1], y)) for y in range(y0, y1)]
i = 0
while i < len(c):
    if 'M' in c[i]:
        i += 1; continue
    j = i
    while j < len(c) and 'M' not in c[j]:
        j += 1
    if j - i >= minlen:
        a = ''.join(c[k][0] for k in range(i, j, 2)); b = ''.join(c[k][1] for k in range(i, j, 2))
        print(f'{y0+i}-{y0+j-1} {j-i:3d} px  chip2 {a}  chip1 {b}')
    i = j
