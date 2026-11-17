#!/usr/bin/env python3
"""A rectangle of the die as small text maps, for judging contacts and metal breaks
without an image.

usage: textmap.py X0 Y0 X1 Y1 [STEP] [--acid]     (STEP default 3 px; each sample a 3x3 mean)

Three maps side by side, one character per sample:
  1. chip-2 metal shot, red / 16 as a hex digit   (metal C-E, bare ground 9-A, edges 2-6)
  2. chip-1 metal shot, the same                  (bare ground is darker there: 7-9)
  3. clean shot (acid1b), (red - green) / 8 as a hex digit, 'g' where green exceeds red,
     '.' where the class map's rule says field under metal (pink: red over 170 and
     green - blue under 18)
     (protected poly 7-9, protected diffusion 2-3, contact holes and open ground 'g')
--acid adds a fourth:
  4. chip-2 stripped shot (acid), (red - green) / 2 as a hex digit, '-' where green
     exceeds red. In the open this is the map that tells a large diffusion from field
     (tracing guide, trap 21): field 0-2, diffusion 6-8, poly F.

The digit ranges were measured in the top-centre logic (`tc1`, `tcw`); the colours drift
across the die, so read a known feature near your own first (tracing guide, trap 1).

What a real contact of a thin metal looks like in maps 1 and 2 (measured on the pads
(6318,3740) and (6400,3788) of `tcw`): a dark ring (2-3) about 40 px across with a bright
centre (B-D) about 12 px across, in both chips, and in map 3 a hole of 'g' about 12 px
across inside the pad. A break in a metal line is 9-A (chip 2) and 7-9 (chip 1) across the
line's width with no ring; an edge of something underneath is a dark bar 6-14 px long with
metal on both sides; a thin metal passing over a buried contact is dark for 35-80 px with
no bright centre, no 'g' hole and no widening (trap 22).

The shared form of tools/tc1_hex.py: without --acid the output is the same.
"""
import os
import sys
import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main():
    a = [t for t in sys.argv[1:] if t != '--acid']
    with_acid = '--acid' in sys.argv[1:]
    if len(a) < 4:
        sys.exit(__doc__)
    x0, y0, x1, y1 = map(int, a[:4])
    st = int(a[4]) if len(a) > 4 else 3
    m = np.load(os.path.join(ROOT, 'cache', 'metal.npy'), mmap_mode='r')
    m1 = np.load(os.path.join(ROOT, 'cache', 'metal1.npy'), mmap_mode='r')
    c = np.load(os.path.join(ROOT, 'cache', 'acid1b.npy'), mmap_mode='r')
    ac = np.load(os.path.join(ROOT, 'cache', 'acid_aligned.npy'), mmap_mode='r') if with_acid else None

    def mean(arr, x, y):
        return arr[y - 1:y + 2, x - 1:x + 2].reshape(-1, 3).mean(0)

    xs = list(range(x0, x1, st))
    print('x %d..%d step %d   chip-2 metal R/16 | chip-1 metal R/16 | clean (R-G)/8, g = greener%s'
          % (x0, xs[-1], st, ' | chip-2 stripped (R-G)/2, - = greener' if with_acid else ''))
    for y in range(y0, y1, st):
        r = ''.join('%X' % min(15, int(mean(m, x, y)[0] / 16)) for x in xs)
        r1 = ''.join('%X' % min(15, int(mean(m1, x, y)[0] / 16)) for x in xs)
        d = ''
        for x in xs:
            v = mean(c, x, y)
            if v[1] > v[0]:
                d += 'g'
            elif v[0] > 170 and v[1] - v[2] < 18:
                d += '.'
            else:
                d += '%X' % min(15, int((v[0] - v[1]) / 8))
        line = '%5d %s | %s | %s' % (y, r, r1, d)
        if with_acid:
            e = ''
            for x in xs:
                v = mean(ac, x, y)
                e += '-' if v[1] > v[0] else '%X' % min(15, int((v[0] - v[1]) / 2))
            line += ' | ' + e
        print(line)


if __name__ == '__main__':
    main()
