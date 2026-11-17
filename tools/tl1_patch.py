#!/usr/bin/env python3
"""Mean colour of small patches in every shot, for comparing one kind of spot with another.

usage: tl1_patch.py HALF X,Y[:label] ...
Prints, for each point, the mean R/G/B of the (2*HALF+1)^2 patch in metal, metal1, acid1b and
acid (aligned), and the clean shot's G-R ("greenness": a metal contact's hole on diffusion reads
positive or near zero; tan under metal about -25; salmon poly about -70).
"""
import os, sys
import numpy as np
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
names = [('metal', 'metal.npy'), ('metal1', 'metal1.npy'), ('acid1b', 'acid1b.npy'), ('acid', 'acid_aligned.npy')]
arrs = [(n, np.load(os.path.join(ROOT, 'cache', f), mmap_mode='r')) for n, f in names]
h = int(sys.argv[1])
print(f"{'point':>26}  " + '  '.join(f'{n:>11}' for n, _ in arrs) + '   clean G-R')
for a in sys.argv[2:]:
    pt, _, lab = a.partition(':')
    x, y = map(int, pt.split(','))
    out = []; gr = 0
    for n, m in arrs:
        p = m[y - h:y + h + 1, x - h:x + h + 1, :3].astype(float).reshape(-1, 3).mean(axis=0)
        out.append('%3d/%3d/%3d' % tuple(p))
        if n == 'acid1b':
            gr = p[1] - p[0]
    print(f'{(pt + " " + lab):>26}  ' + '  '.join(out) + f'   {gr:+.0f}')
