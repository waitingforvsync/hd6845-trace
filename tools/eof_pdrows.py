#!/usr/bin/env python3
"""The two pull-downs west of the strap (piece `pd`) in each of the fourteen rows of the left array, as text.

usage: eof_pdrows.py [ROW ...]        rows 0-13, default all

Master coordinates are those of row s1 (cell eof_pd); row k is read at the cell's offset (those of
eof_mx). One line per row, each value the mean of a 5 x 5 patch (3 x 3 where marked *):

  poly   chip-2 metal shot BLUE at seven places on the gate poly: the stem (4060,11620), the bar
         (4066,11668), the join of PA and the C (4080,11766), the C's west strip (4060,11795*), the arm
         (4066,11818), the stub over active (4087,11840*) and its overhang (4087,11858*). Open poly is
         under 72.
  open   the same BLUE at four places that are not poly: the field north of the active edge
         (4082,11628*), the sliver north of the bar (4082,11648*), D_w (4066,11718), the inner box
         (4085,11793*). Over 72.
  Dw-F   chip-2 stripped shot red minus green on D_w (4068,11718) and on the field (4084,11597):
         diffusion is the higher by 10 or more
  notch  clean shot red minus blue under the strap's east margin at (4136,11668) (the upper tab: tan,
         over 50) and at (4136,11716) (the notch: pink field, under 50)
  row    clean shot GREEN under rail F at (4020,11577) (field), (4020,11597) (the gate's row: poly,
         higher by 15 or more), (4020,11616) (field)
  east   clean shot at (4097,11766*), (4097,11793*), (4097,11820*): R/G each; poly in the strap's margin
         is salmon (R over 215), the box's open east side tan (R under 205)
"""
import os, sys
import numpy as np
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OFF = [(0,-477),(0,0),(0,477),(0,954),(0,1431),(0,1909),(0,2386),(1,3079),(1,3557),(1,4034),(1,4684),(1,5162),(1,5639),(1,6116)]
ld = lambda n: np.load(os.path.join(ROOT, 'cache', n), mmap_mode='r')
M, A, K = ld('metal.npy'), ld('acid_aligned.npy'), ld('acid1b.npy')
def v(arr, x, y, h, d):
    return arr[y+d[1]-h:y+d[1]+h+1, x+d[0]-h:x+d[0]+h+1].reshape(-1, 3).mean(0)
rows = [int(a) for a in sys.argv[1:]] or range(14)
print('row  poly: stem bar join strip arm stub over | open: field sliver Dw box | Dw-F | notch tab/notch | row f/p/f | east 766 793 820')
for k in rows:
    d = OFF[k]
    poly = [v(M, 4060, 11620, 2, d)[2], v(M, 4066, 11668, 2, d)[2], v(M, 4080, 11766, 2, d)[2], v(M, 4060, 11795, 1, d)[2],
            v(M, 4066, 11818, 2, d)[2], v(M, 4087, 11840, 1, d)[2], v(M, 4087, 11858, 1, d)[2]]
    opn = [v(M, 4082, 11628, 1, d)[2], v(M, 4082, 11648, 1, d)[2], v(M, 4066, 11718, 2, d)[2], v(M, 4085, 11793, 1, d)[2]]
    a1, a2 = v(A, 4068, 11718, 2, d), v(A, 4084, 11597, 2, d)
    n1, n2 = v(K, 4136, 11668, 2, d), v(K, 4136, 11716, 2, d)
    r = [v(K, 4020, y, 2, d)[1] for y in (11577, 11597, 11616)]
    e = [v(K, 4097, y, 1, d) for y in (11766, 11793, 11820)]
    print('s%-3d %s | %s | %+3d %+3d | %3d %3d | %3d %3d %3d | %s' % (
        k, ' '.join('%3d' % p for p in poly), ' '.join('%3d' % p for p in opn), a1[0]-a1[1], a2[0]-a2[1],
        n1[0]-n1[2], n2[0]-n2[2], r[0], r[1], r[2], ' '.join('%3d/%3d' % (q[0], q[1]) for q in e)))
