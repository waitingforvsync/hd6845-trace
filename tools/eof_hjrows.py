#!/usr/bin/env python3
"""The south band's west stretch (piece `hj`) in each of the fourteen rows of the left array, as text.

usage: eof_hjrows.py [ROW ...]        rows 0-13, default all

Master coordinates are those of row s1 (cell eof_mx / eof_hj); row k is read at the cell's offset.
For each row it prints, with the y extents found by scanning from a seed on the feature:

  up     the upper band in the open at x 4325 (chip-2 metal shot: orange = poly)
  jog    the block under rail H at x 4298 (clean shot: cream = poly under metal), its y extent
  lowH   the lower band under rail H at x 4272 (clean shot), its y extent
  gap    the lower band in the open gap at x 4238 (chip-2 metal shot), its y extent, and the chip-2
         stripped shot's red minus green 14 px north and south of it (field: under about 20)
  lowG   the lower band under rail G at x 4195 (clean shot), its y extent
  junc   the clean shot along y 11986 at x 4160..4170 step 2 (R/G/B): the band meets the column
         where no sample is pink (R-G over 60 with B over 110) or green (G over R)
  col    the column at x 4158 (chip-2 metal shot): its y extent through the junction, i.e. where
         its foot ends
  h3     the poly west of the column at y 11998, x 4142 / 4120 / 4100 (chip-2 metal shot,
         'P' orange poly, '.' not), and its y extent at x 4120

Classes: chip-2 metal shot orange (poly in the open) = R-G over 28 and B under 78 and R over 125;
clean shot cream (poly under metal) = R over 195, G 135-190, B under 135.
"""
import os
import sys
import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ld = lambda n: np.load(os.path.join(ROOT, 'cache', n), mmap_mode='r')
OFFS = [(0, -477), (0, 0), (0, 477), (0, 954), (0, 1431), (0, 1909), (0, 2386), (1, 3079),
        (1, 3557), (1, 4034), (1, 4684), (1, 5162), (1, 5639), (1, 6116)]


def mean(a, x, y, h=1):
    return a[y - h:y + h + 1, x - h:x + h + 1].reshape(-1, 3).astype(float).mean(0)


def orange(p):
    return p[0] - p[1] > 28 and p[2] < 78 and p[0] > 125


def cream(p):
    return p[0] > 195 and 135 <= p[1] <= 190 and p[2] < 135


def extent(a, x, y, test, reach=40):
    """y extent of the run of samples passing `test` around the seed (x, y); None if the seed fails."""
    if not test(mean(a, x, y)):
        return None
    y0 = y
    while y - y0 < reach and test(mean(a, x, y0 - 1)):
        y0 -= 1
    y1 = y
    while y1 - y < reach and test(mean(a, x, y1 + 1)):
        y1 += 1
    return y0, y1


def fmt(e, dy):
    return 'none' if e is None else '%d-%d' % (e[0] - dy, e[1] - dy)


def main():
    rows = [int(r) for r in sys.argv[1:]] or list(range(14))
    M = ld('metal.npy')
    C = ld('acid1b.npy')
    A = ld('acid_aligned.npy')
    print('row   up(4325)     jog(4298)    lowH(4272)   gap(4238) N/S field   lowG(4195)   col foot(4158)  h3 4142/4120/4100  h3 y(4120)')
    for k in rows:
        dx, dy = OFFS[k]
        up = extent(M, 4325 + dx, 11964 + dy, orange)
        jog = extent(C, 4298 + dx, 11975 + dy, cream, 60)
        lowh = extent(C, 4272 + dx, 11986 + dy, cream)
        gap = extent(M, 4238 + dx, 11987 + dy, orange)
        if gap:
            n = mean(A, 4238 + dx, gap[0] - 14)
            s = mean(A, 4238 + dx, gap[1] + 14)
            fld = '%+.0f/%+.0f' % (n[0] - n[1], s[0] - s[1])
        else:
            fld = '?'
        lowg = extent(C, 4195 + dx, 11986 + dy, cream)
        col = extent(M, 4158 + dx, 11975 + dy, orange, 70)
        h3 = ''.join('P' if orange(mean(M, x + dx, 11998 + dy)) else '.' for x in (4142, 4120, 4100))
        h3y = extent(M, 4120 + dx, 11998 + dy, orange)
        print('s%-3d  %-11s  %-11s  %-11s  %-11s %-9s  %-11s  %-14s  %-17s  %s' % (
            k, fmt(up, dy), fmt(jog, dy), fmt(lowh, dy), fmt(gap, dy), fld, fmt(lowg, dy),
            fmt(col, dy), h3, fmt(h3y, dy)))
    print()
    print('junction, clean shot along y 11986 (master), x 4160 4162 4164 4166 4168 4170:')
    for k in rows:
        dx, dy = OFFS[k]
        cells = []
        bad = ''
        for x in range(4160, 4172, 2):
            p = mean(C, x + dx, 11986 + dy, 0)
            cells.append('%3.0f/%3.0f/%3.0f' % tuple(p))
            if (p[0] - p[1] > 60 and p[2] > 110) or p[1] > p[0]:
                bad = '   <-- pink or green'
        print('s%-3d  %s%s' % (k, '  '.join(cells), bad))


if __name__ == '__main__':
    main()
