#!/usr/bin/env python3
"""The second transistor on line Y and its gate line (piece `yg`) in each of the fourteen rows of the left array, as text.

usage: eof_ygrows.py [ROW ...]        rows 0-13, default all

Master coordinates are those of row s1 (cell eof_yg); row k is read at the cell's offset (those of
eof_mx). One line per row, each value the mean of a 3 x 3 patch unless marked (5: 5 x 5):

  poly   chip-2 metal shot BLUE on the poly column where it lies in the open, east of the thin metal:
         (3974,11790), (3974,11810). Open poly is under 70.
  open   the same BLUE at open places that are not poly: the strip east of the column (3989,11790),
         (3989,11810); the field north of it (3988,11750, 5) and south of it (3988,11842, 5). 65 and
         more (the strip 76 and more).
  S-F    chip-2 stripped shot red minus green on the strip (3989,11795; mean of x 3988-3990,
         y 11780-11812) and on the field north (3988,11750, 5) and south (3988,11842, 5) of it:
         the strip is the higher than the field north of it in every row (by 7 to 34); the place south
         of it (between the pad and rail F, green in the clean shot) is no clean control (0 to +21)
  chan   clean shot RED on the column under the thin metal's margin over the active band (3968,11795, 5)
         and on its head over field (3968,11762): the channel is the brighter by 12 or more
  Y      clean shot R/G on Y's diffusion west of the column (3950,11795, 5): tan (R-G under 30)
  pad    clean shot R/G on the pad's poly north of the hole (3962,11834: cream, R-G over 40) and in
         the hole (3958,11848, 5: R-G under 25); chip-2 stripped shot red minus green in the pad
         (3950,11846: poly, over 30)
  fld    clean shot R/G between the pad and rail F (3988,11848, 5): open field, green (G over R)
  thin   the brightest 3 x 3 RED across x 3954-3966 in chip 2 / chip 1 at y 11748 (below the wide
         metal's end), 11762 (on the column's head), 11790, 11810 (on the column), 11831 (above the pad)
  gap    the same across x 3950-3966, the brightest of y 11868-11874 (between the pad's south edge
         and the foot band's north edge), chip 2 / chip 1; and beside the metal at x 3974 (no metal
         there: the control)
  wide   the same at y 11720 (the wide metal) and y 11900 (the wide metal south of the pad)
"""
import os, sys
import numpy as np
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OFF = [(0,-477),(0,0),(0,477),(0,954),(0,1431),(0,1909),(0,2386),(1,3079),(1,3557),(1,4034),(1,4684),(1,5162),(1,5639),(1,6116)]
ld = lambda n: np.load(os.path.join(ROOT, 'cache', n), mmap_mode='r')
M, M1, A, K = ld('metal.npy'), ld('metal1.npy'), ld('acid_aligned.npy'), ld('acid1b.npy')
def v(arr, x, y, h, d):
    return arr[y+d[1]-h:y+d[1]+h+1, x+d[0]-h:x+d[0]+h+1].reshape(-1, 3).mean(0)
def box(arr, x0, x1, y0, y1, d):
    return arr[y0+d[1]:y1+d[1]+1, x0+d[0]:x1+d[0]+1].reshape(-1, 3).mean(0)
def best(arr, x0, x1, ys, d):
    return max(v(arr, x, y, 1, d)[0] for y in ys for x in range(x0, x1 + 1))
rows = [int(a) for a in sys.argv[1:]] or range(14)
print('row  poly  | open: strip strip fN fS | S-F: strip fN fS | chan ch/head | Y | pad cream hole acid | fld | '
      'thin 748 762 790 810 831 (c2/c1) | gap c2/c1 ctl c2/c1 | wide 720 900')
for k in rows:
    d = OFF[k]
    poly = [v(M, 3974, y, 1, d)[2] for y in (11790, 11810)]
    opn = [v(M, 3989, 11790, 1, d)[2], v(M, 3989, 11810, 1, d)[2], v(M, 3988, 11750, 2, d)[2], v(M, 3988, 11842, 2, d)[2]]
    s = box(A, 3988, 3990, 11780, 11812, d); fn = v(A, 3988, 11750, 2, d); fs = v(A, 3988, 11842, 2, d)
    ch = [v(K, 3968, 11795, 2, d)[0], v(K, 3968, 11762, 1, d)[0]]
    yy = v(K, 3950, 11795, 2, d)
    pc = v(K, 3962, 11834, 1, d); ph = v(K, 3958, 11848, 2, d); pa = v(A, 3950, 11846, 1, d)
    fl = v(K, 3988, 11848, 2, d)
    thin = ['%3d/%3d' % (best(M, 3954, 3966, [y], d), best(M1, 3954, 3966, [y], d)) for y in (11748, 11762, 11790, 11810, 11831)]
    ys = range(11868, 11875)
    gap = '%3d/%3d %3d/%3d' % (best(M, 3950, 3966, ys, d), best(M1, 3950, 3966, ys, d), best(M, 3974, 3974, ys, d), best(M1, 3974, 3974, ys, d))
    wide = ['%3d/%3d' % (best(M, 3950, 3966, [y], d), best(M1, 3950, 3966, [y], d)) for y in (11720, 11900)]
    print('s%-3d %3d %3d | %3d %3d %3d %3d | %+3d %+3d %+3d | %3d %3d | %3d/%3d | %3d/%3d %3d/%3d %+3d | %3d/%3d | %s | %s | %s' % (
        k, poly[0], poly[1], opn[0], opn[1], opn[2], opn[3], s[0]-s[1], fn[0]-fn[1], fs[0]-fs[1], ch[0], ch[1],
        yy[0], yy[1], pc[0], pc[1], ph[0], ph[1], pa[0]-pa[1], fl[0], fl[1], ' '.join(thin), gap, ' '.join(wide)))
