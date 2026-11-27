#!/usr/bin/env python3
"""Row lines crossing a vertical cut, as text: the dark edge lines of the clean shot.

usage: busl_rows.py X Y0 Y1 [--half 3] [--thr 110]

Down the column X (mean over 2*half+1 px) of the clean shot (acid1b) it prints every run where
red is under --thr (an edge line or a dark open poly), with the colours of acid1b and of the
chip-2 stripped shot (aligned) 4 px either side. Two edges 14-30 px apart with a paler strip
between are one row line. Use it in an open column (no metal above), where field is khaki.
"""
import os, sys
import numpy as np
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
a = sys.argv[1:]
half, thr = 3, 110
for k in ('--half', '--thr'):
    if k in a:
        i = a.index(k); v = int(a[i + 1]); del a[i:i + 2]
        if k == '--half': half = v
        else: thr = v
x, y0, y1 = map(int, a[:3])
B = np.load(os.path.join(ROOT, 'cache', 'acid1b.npy'), mmap_mode='r')
A = np.load(os.path.join(ROOT, 'cache', 'acid_aligned.npy'), mmap_mode='r')
b = np.asarray(B[y0:y1, x - half:x + half + 1, :3]).astype(float).mean(axis=1)
c = np.asarray(A[y0:y1, x - half:x + half + 1, :3]).astype(float).mean(axis=1)
d = b[:, 0] < thr
s = None
for i, v in enumerate(list(d) + [False]):
    if v and s is None: s = i
    if not v and s is not None:
        e = i - 1
        def col(arr, j):
            j = min(max(j, 0), len(arr) - 1); return '%3d/%3d/%3d' % tuple(arr[j])
        print('dark y %5d-%5d (%2d)   above %s | %s   below %s | %s' % (
            y0 + s, y0 + e, e - s + 1, col(b, s - 5), col(c, s - 5), col(b, e + 5), col(c, e + 5)))
        s = None
