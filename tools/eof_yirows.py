#!/usr/bin/env python3
"""The inverter of line Y that drives eof_pdg_s# (piece `yi`) in each of the fourteen rows of the left array, as text.

usage: eof_yirows.py [ROW ...]        rows 0-13, default all

Master coordinates are those of row s1 (cell eof_yi); row k is read at the cell's offset (those of
eof_mx). One line per row, each value the mean of a 5 x 5 patch (3 x 3 where marked *):

  poly   chip-2 metal shot BLUE at six places where the poly lies in the open: the load block
         (3890,11603) and (3890,11640), the gate row in gap 1 (3936,11599*) and in gap 2 (3982,11599*),
         Y's arm in gap 2 (3982,11669), Y's horizontal part in gap 1 (3936,11731*). Open poly is under 70.
  open   the same BLUE at six open places that are not poly: N (3936,11640) and (3936,11680), the band
         in gap 2 (3982,11649*), R1 (3984,11691*), the field north of the band (3982,11625), the field
         south of the load block (3890,11690). Over 70.
  N-F    chip-2 stripped shot red minus green on N (3936,11660) and on the field (3890,11690):
         diffusion is the higher by 10 or more
  load   clean shot RED under Vm6 on the block over field (3912,11603), over the load strip
         (3912,11638: a channel is the brighter, by 12 or more) and on the block's foot (3912,11668)
  Yblk   clean shot RED under the segmented metal on Y's block over active (3958,11676) and over
         field (3958,11722), and under rail F on Y's arm over active (4012,11659) and over field
         (4012,11631): the channel is the brighter of each pair
  band   clean shot R/G under the segmented metal on the band (3958,11649*: tan, R-G under 30) and on
         the field north of it (3958,11621: pink, R-G over 45), and under rail F's margin west of Y's
         arm (3994,11649*: tan)
  box    clean shot R/G in the two buried-contact boxes: the load's (3912,11692*) and Y's (3924,11778*):
         tan (R-G under 40)
  Y      clean shot R/G on Y's diffusion under Vm6 (3912,11812): tan
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
print('row  poly: blk blk row1 row2 arm hor | open: N N band R1 fld fld | N-F | load f/ch/foot | Yblk ch/f ch/f | band t f t | box L Y | Y')
for k in rows:
    d = OFF[k]
    poly = [v(M, 3890, 11603, 2, d)[2], v(M, 3890, 11640, 2, d)[2], v(M, 3936, 11599, 1, d)[2], v(M, 3982, 11599, 1, d)[2],
            v(M, 3982, 11669, 2, d)[2], v(M, 3936, 11731, 1, d)[2]]
    opn = [v(M, 3936, 11640, 2, d)[2], v(M, 3936, 11680, 2, d)[2], v(M, 3982, 11649, 1, d)[2], v(M, 3984, 11691, 1, d)[2],
           v(M, 3982, 11625, 2, d)[2], v(M, 3890, 11690, 2, d)[2]]
    a1, a2 = v(A, 3936, 11660, 2, d), v(A, 3890, 11690, 2, d)
    ld_ = [v(K, 3912, y, 2, d)[0] for y in (11603, 11638, 11668)]
    yb = [v(K, 3958, 11676, 2, d)[0], v(K, 3958, 11722, 2, d)[0], v(K, 4012, 11659, 2, d)[0], v(K, 4012, 11631, 2, d)[0]]
    bd = [v(K, 3958, 11649, 1, d), v(K, 3958, 11621, 2, d), v(K, 3994, 11649, 1, d)]
    bx = [v(K, 3912, 11692, 1, d), v(K, 3924, 11778, 1, d)]
    yy = v(K, 3912, 11812, 2, d)
    print('s%-3d %s | %s | %+3d %+3d | %3d %3d %3d | %3d %3d %3d %3d | %s | %s | %3d/%3d' % (
        k, ' '.join('%3d' % p for p in poly), ' '.join('%3d' % p for p in opn), a1[0]-a1[1], a2[0]-a2[1],
        ld_[0], ld_[1], ld_[2], yb[0], yb[1], yb[2], yb[3],
        ' '.join('%3d/%3d' % (q[0], q[1]) for q in bd), ' '.join('%3d/%3d' % (q[0], q[1]) for q in bx), yy[0], yy[1]))
