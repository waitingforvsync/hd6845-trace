#!/usr/bin/env python3
"""Numbers for a list of metal-contact places, as one line each (no image).

usage: eof_cchk.py X,Y [X,Y ...]

For each place, searched within 8 px for the best centre: in both metal shots (red channel,
3x3 means) the brightest sample near the centre and the darkest on a ring of radius 14-20 px in
the four directions (N, S, W, E), and in the clean shot (acid1b) the lowest red minus green
within 7 px of the centre (5x5 mean). A metal contact on a poly pad has a bright centre
(over about 150) inside a dark ring (under about 100) in both chips and a green or dull hole in
the clean shot (red minus green under about 24; a pad's poly without a hole is 40-70). The
direction whose ring is NOT dark is the one the pad's own metal leaves by. An aid for listing
the contacts along a route that another package drew; each doubtful one is still read on a
text map (tools/textmap.py) or a view.
"""
import os
import sys
import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ld = lambda n: np.load(os.path.join(ROOT, 'cache', n), mmap_mode='r')


def mean(a, x, y, h=1):
    return a[y - h:y + h + 1, x - h:x + h + 1].reshape(-1, 3).astype(float).mean(0)


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    m, m1, c = ld('metal.npy'), ld('metal1.npy'), ld('acid1b.npy')
    print('   place        clean hole (R-G min at)   chip 2: centre  ring N S W E     chip 1: centre  ring N S W E')
    for t in sys.argv[1:]:
        x0, y0 = map(int, t.split(','))
        best = None
        for dy in range(-8, 9, 2):
            for dx in range(-8, 9, 2):
                v = mean(c, x0 + dx, y0 + dy, 2)
                d = v[0] - v[1]
                if best is None or d < best[0]:
                    best = (d, x0 + dx, y0 + dy)
        d, hx, hy = best
        out = []
        for a in (m, m1):
            cen = max(mean(a, hx + dx, hy + dy)[0] for dx in (-3, 0, 3) for dy in (-3, 0, 3))
            ring = []
            for ux, uy in ((0, -1), (0, 1), (-1, 0), (1, 0)):
                ring.append(min(mean(a, hx + ux * r, hy + uy * r)[0] for r in range(12, 23, 2)))
            out.append('%3d   %3d %3d %3d %3d' % ((cen,) + tuple(ring)))
        print('%6d,%-6d  %4d at %d,%d          %s          %s' % (x0, y0, d, hx, hy, out[0], out[1]))


if __name__ == '__main__':
    main()
