#!/usr/bin/env python3
"""busc_pits.py X0 Y0 X1 Y1: dark specks in the clean shot (contact pits on diffusion or pads): connected groups of
pixels with R < 120 whose bounding box is at most 26 px a side and which are surrounded by light tan
(mean R of a 40 px box > 150). Prints centre, size. Run from the repository's root."""
import sys, numpy as np
from scipy import ndimage as ndi
a = np.load('cache/acid1b.npy', mmap_mode='r')
x0, y0, x1, y1 = map(int, sys.argv[1:5])
r = np.asarray(a[y0:y1, x0:x1, 0], float); g = np.asarray(a[y0:y1, x0:x1, 1], float)
lab, n = ndi.label((r < 120) & (g < 110))
for i, sl in enumerate(ndi.find_objects(lab), 1):
    h = sl[0].stop - sl[0].start; w = sl[1].stop - sl[1].start
    if h > 26 or w > 26 or h * w < 16: continue
    cy = (sl[0].start + sl[0].stop) // 2; cx = (sl[1].start + sl[1].stop) // 2
    box = r[max(0, cy-20):cy+20, max(0, cx-20):cx+20]
    if np.median(box) < 150: continue
    print('%d,%d  %dx%d  n=%d  around R %d' % (cx + x0, cy + y0, w, h, (lab[sl] == i).sum(), np.median(box)))
