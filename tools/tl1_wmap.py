#!/usr/bin/env python3
"""Brightness of both metal shots across a thin vertical metal, as text.

usage: tl1_wmap.py X0 X1 Y0 Y1 [YSTEP]
One line per y: for each x (step 2) a digit 0-9 = (R+G)/2 scaled 60..230, metal shot then
metal1. A thin metal is a run of 7-9; bare ground or poly is 4-6; an edge line 0-3.
"""
import os, sys
import numpy as np
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
x0, x1, y0, y1 = map(int, sys.argv[1:5])
st = int(sys.argv[5]) if len(sys.argv) > 5 else 4
ms = [np.load(os.path.join(ROOT, 'cache', f), mmap_mode='r') for f in ('metal.npy', 'metal1.npy')]
def line(a, y):
    p = a[y - 1:y + 2, x0:x1].astype(float).mean(axis=0)
    v = (p[:, 0] + p[:, 1]) / 2
    return ''.join(str(int(min(9, max(0, (t - 60) / 17)))) for t in v[::2])
print('x %d..%d step 2      metal | metal1' % (x0, x1))
for y in range(y0, y1, st):
    print('%5d  %s | %s' % (y, line(ms[0], y), line(ms[1], y)))
