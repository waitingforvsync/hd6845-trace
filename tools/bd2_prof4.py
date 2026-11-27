#!/usr/bin/env python3
"""A row or a column of the die as one character per sample in each of the four shots, as text.

usage: bd2_prof4.py row Y X0 X1 STEP
       bd2_prof4.py col X Y0 Y1 STEP        (run from the repository's root: it reads cache/*.npy)

Each sample is the mean of 3 x 3 px. One line per shot, under a header line that gives the tens digit of
the running coordinate. The classes are coarse and were set at x 15860-16300, y 16540-17130 (the colours
drift across the die: tracing guide, trap 1); they order features along a line and find edge lines, and a
doubtful patch is settled from raw numbers (tools/px.py).

metal, metal1 (the two metal shots):
   .  dark (edge line, outline): max(R,G) < 105       M  metal: R >= 185 and G >= 150
   o  orange, poly: R-G >= 38 and B < 72              d  pinker plain, diffusion-like: R-G >= 30
   f  plain (field; diffusion often reads f too: tell them by the outlines)
acid (chip 2 stripped):   .  dark   o  orange (R-G >= 28)   k  plain
acid1b (the clean shot):  .  dark   g  green (G >= R+8)   p  pink (field under metal)
   s  salmon or red (R-G >= 48: poly)   t  tan (diffusion under metal)   k  other
"""
import sys, numpy as np
L = {n: np.load('cache/%s.npy' % f, mmap_mode='r') for n, f in (('metal','metal'),('metal1','metal1'),('acid','acid_aligned'),('acid1b','acid1b'))}
def cm(v):
    r,g,b = v
    if max(r,g) < 105: return '.'
    if r >= 185 and g >= 150: return 'M'
    if r-g >= 38 and b < 72: return 'o'
    if r-g >= 30: return 'd'
    return 'f'
def ca(v):
    r,g,b = v
    if max(r,g) < 95: return '.'
    return 'o' if r-g >= 28 else 'k'
def cb(v):
    r,g,b = v
    if r < 110 and g < 110: return '.'
    if g >= r+8: return 'g'
    if g-b < 14 and r-g >= 30: return 'p'
    if r-g >= 48: return 's'
    if g-b >= 22 and r-g >= 12: return 't'
    return 'k'
F = {'metal': cm, 'metal1': cm, 'acid': ca, 'acid1b': cb}
mode = sys.argv[1]; a, b0, b1, st = map(int, sys.argv[2:6])
pts = [(x, a) for x in range(b0, b1+1, st)] if mode == 'row' else [(a, y) for y in range(b0, b1+1, st)]
print('%s %d from %d step %d; tens digit of the running coordinate:' % (mode, a, b0, st))
print('        ' + ''.join(str((p[0] if mode=='row' else p[1])//10 % 10) for p in pts))
for n in ('metal','metal1','acid','acid1b'):
    s = ''
    for x, y in pts:
        v = L[n][y-1:y+2, x-1:x+2].reshape(-1,3).mean(0)
        s += F[n](v)
    print('%-7s %s' % (n, s))
