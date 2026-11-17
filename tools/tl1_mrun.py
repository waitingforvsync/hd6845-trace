#!/usr/bin/env python3
"""Runs of metal / no metal along a vertical (or horizontal) track, by the follower's test.

usage: tl1_mrun.py X0 X1 Y0 Y1 [MINLEN] [--h]
For each row y (with --h: each column x of the band Y0..Y1 between X0 and X1) the brightest
4 px window across X0..X1 is tested in each metal shot with the follower's test (R > 177 and
G > 128). Prints the runs of at least MINLEN rows (default 12) where NEITHER shot has metal,
and the runs where both have it. Ground between lines reads about 150/140 and fails the test;
thin dim metal can fail it too (tracing guide, trap 19): a "none" run is a place to look at,
not a proof of a break.
"""
import os, sys
import numpy as np
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
args = [a for a in sys.argv[1:] if not a.startswith('--')]
horiz = '--h' in sys.argv
x0, x1, y0, y1 = map(int, args[:4])
minlen = int(args[4]) if len(args) > 4 else 12
ms = [np.load(os.path.join(ROOT, 'cache', f), mmap_mode='r') for f in ('metal.npy', 'metal1.npy')]
def is_metal(m, i):
    if horiz:
        p = m[y0:y1 + 1, i, :2].astype(float)
    else:
        p = m[i, x0:x1 + 1, :2].astype(float)
    k = np.ones(4) / 4
    r = np.convolve(p[:, 0], k, 'valid'); g = np.convolve(p[:, 1], k, 'valid')
    return bool(((r > 177) & (g > 128)).any())
rng = range(x0, x1) if horiz else range(y0, y1)
st = []
for i in rng:
    a, b = is_metal(ms[0], i), is_metal(ms[1], i)
    st.append('both' if a and b else 'none' if not (a or b) else 'one')
i = 0
lst = list(rng)
while i < len(st):
    j = i
    while j < len(st) and st[j] == st[i]:
        j += 1
    if st[i] != 'one' and j - i >= minlen:
        print(f'{lst[i]}-{lst[j-1]}  {j-i:4d} px  {st[i]}')
    i = j
