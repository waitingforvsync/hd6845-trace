#!/usr/bin/env python3
"""The two load units beside rail G (piece `ol`) in each of the fourteen rows of the left array, as text.

usage: eof_olrows.py [ROW ...]        rows 0-13, default all

Master coordinates are those of row s1 (cells eof_mx / eof_hj / eof_ol); row k is read at the cell's
offset. One line per row:

  chU, chL   the y extent of each plate's channel under rail G at x 4180 (clean shot: bright salmon,
             R over 228 and R-G over 55), from seeds y 11640 and y 11770
  stripU/L   chip-1 metal shot R-G on the plate's bottom strip at x 4157 (y 11668 / 11812): poly on
             oxide is over 45
  boxU/L     the same at the box centre (y 11692 / 11834): poly on silicon (a buried contact) reads
             plain, under 35, as at the pilot's known box (14536,14941)
  gap        the stretch between the upper box and the lower plate, x 4157, y 11708-11716: the largest
             R-G in chip 2's and chip 1's metal shots and in chip 2's stripped shot. Field is under
             about 20 in all three; a poly there (which would join the two units) is over 35
  col        chip-1 metal shot R-G on the column south of the lower box (x 4157, y 11870): poly
  d2         the supply diffusion at x 4208 in the clean shot, y 11628-11870 step 2: lowest and highest
             red, and how many samples are not tan (R 185-215, G 160-190, B 120-150)
  tabs       the west diffusion at x 4133 in the clean shot: y extents of the tan runs from seeds
             y 11640 and y 11780, and the colour between them at y 11718 (pink = field)
  d5|d2      the dark line between the greenish box and d2 along y 11834 (chip-2 metal shot, x
             4186-4212): its width at half depth, and the same for the upper unit along y 11690
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


def extent(a, x, y, test, reach=120):
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


def salmon(p):
    return p[0] > 228 and p[0] - p[1] > 55


def tan(p):
    return 185 <= p[0] <= 215 and 160 <= p[1] <= 190 and 115 <= p[2] <= 150


def halfwidth(a, y, x0, x1):
    r = [mean(a, x, y)[0] for x in range(x0, x1 + 1)]
    lo, hi = min(r), max(r)
    half = (lo + hi) / 2
    return sum(1 for v in r if v < half)


def main():
    rows = [int(r) for r in sys.argv[1:]] or list(range(14))
    M, M1, C, A = ld('metal.npy'), ld('metal1.npy'), ld('acid1b.npy'), ld('acid_aligned.npy')
    rg = lambda a, x, y: mean(a, x, y)[0] - mean(a, x, y)[1]
    print('row  chU          chL          stripU/L  boxU/L   gap m/m1/a   col   d2 min/max/bad  tabs                    between      d5|d2 d3|d2')
    for k in rows:
        dx, dy = OFFS[k]
        chu = extent(C, 4180 + dx, 11640 + dy, salmon)
        chl = extent(C, 4180 + dx, 11770 + dy, salmon)
        su, sl = rg(M1, 4157 + dx, 11668 + dy), rg(M1, 4157 + dx, 11812 + dy)
        bu, bl = rg(M1, 4157 + dx, 11692 + dy), rg(M1, 4157 + dx, 11834 + dy)
        g = [max(rg(a, 4157 + dx, y + dy) for y in range(11708, 11717, 2)) for a in (M, M1, A)]
        col = rg(M1, 4157 + dx, 11870 + dy)
        d2 = [mean(C, 4208 + dx, y + dy) for y in range(11628, 11871, 2)]
        bad = sum(1 for p in d2 if not tan(p))
        tu = extent(C, 4133 + dx, 11640 + dy, tan)
        tl = extent(C, 4133 + dx, 11780 + dy, tan)
        b = mean(C, 4133 + dx, 11718 + dy)
        print('s%-2d  %-12s %-12s %3.0f/%-3.0f   %3.0f/%-3.0f  %3.0f/%3.0f/%3.0f  %3.0f   %3.0f/%3.0f/%-2d      %-11s %-11s %3.0f/%3.0f/%3.0f  %2d    %2d'
              % (k, fmt(chu, dy), fmt(chl, dy), su, sl, bu, bl, g[0], g[1], g[2], col,
                 min(p[0] for p in d2), max(p[0] for p in d2), bad, fmt(tu, dy), fmt(tl, dy), b[0], b[1], b[2],
                 halfwidth(M, 11834 + dy, 4186 + dx, 4212 + dx), halfwidth(M, 11690 + dy, 4186 + dx, 4212 + dx)))


if __name__ == '__main__':
    main()
