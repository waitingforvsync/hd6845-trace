#!/usr/bin/env python3
"""Centre of a contact's bright spot near a guessed place, from both metal shots (text).

usage: busl_padc.py X,Y [X,Y ...] [--r 16]

For each place: within +-r px, the centroid of the brightest pixels (red, 5x5 mean, within 12 of
the local maximum) inside the dark ring, in the chip-2 metal shot and in chip 1's (metal1), and
the darkest ring radius found. Prints both centres; they should agree within 3 px. An aid for
placing a contact that a view has already shown; it finds a bright spot whether or not there is
a contact.
"""
import sys
import numpy as np
from scipy.ndimage import uniform_filter
r = 16
args = [a for a in sys.argv[1:]]
if '--r' in args:
    i = args.index('--r'); r = int(args[i + 1]); del args[i:i + 2]
m2 = np.load('cache/metal.npy', mmap_mode='r')
m1 = np.load('cache/metal1.npy', mmap_mode='r')
for a in args:
    x, y = [int(v) for v in a.split(',')]
    out = []
    for m in (m2, m1):
        w = np.asarray(m[y - r - 3:y + r + 4, x - r - 3:x + r + 4, 0], dtype=float)
        s = uniform_filter(w, 5)[3:-3, 3:-3]
        yy, xx = np.mgrid[-r:r + 1, -r:r + 1]
        # the spot nearest the guess: weight brightness down with distance
        sc = s - 1.5 * np.hypot(xx, yy)
        j = np.unravel_index(sc.argmax(), sc.shape)
        pk = s[j]
        sel = (s > pk - 12) & (np.hypot(xx - xx[j], yy - yy[j]) < 9)
        out.append((x + xx[sel].mean(), y + yy[sel].mean(), pk))
    print('%d,%d  chip 2: %.0f,%.0f (R %.0f)   chip 1: %.0f,%.0f (R %.0f)' % (x, y, *out[0], *out[1]))
