#!/usr/bin/env python3
"""busc_rings.py X0 Y0 X1 Y1 [MIN]: contact rings in the metal shots (run from the repository's root).
A contact shows in both metal shots as a bright centre inside a dark ring. Score of a point: mean red of the
7 x 7 px centre minus mean red of the annulus of radius 11-15 px, the smaller of the two chips' values.
Prints the local maxima with a score of MIN (default 45) or more: x,y score(chip 2 / chip 1)."""
import sys, numpy as np
from scipy import ndimage as ndi
m2 = np.load('cache/metal.npy', mmap_mode='r'); m1 = np.load('cache/metal1.npy', mmap_mode='r')
x0, y0, x1, y1 = map(int, sys.argv[1:5]); mn = float(sys.argv[5]) if len(sys.argv) > 5 else 45
pad = 20
def score(a):
    r = np.asarray(a[y0-pad:y1+pad, x0-pad:x1+pad, 0], float)
    c = ndi.uniform_filter(r, 7)
    yy, xx = np.mgrid[-15:16, -15:16]; d = np.hypot(yy, xx); k = ((d >= 11) & (d <= 15)).astype(float); k /= k.sum()
    return c - ndi.convolve(r, k)
s2, s1 = score(m2), score(m1); s = np.minimum(s2, s1)
mx = (s == ndi.maximum_filter(s, 21)) & (s >= mn)
for y, x in sorted(zip(*np.nonzero(mx))):
    if pad <= y < s.shape[0]-pad and pad <= x < s.shape[1]-pad:
        print('%d,%d  %d (%d / %d)' % (x + x0 - pad, y + y0 - pad, s[y, x], s2[y, x], s1[y, x]))
