#!/usr/bin/env python3
"""The fourteen rows of the left array at its east edge (x 4700-4790): each row's diffusion line and
south band where they cross from the array to the bus field's row ends, as numbers (no image).

usage: eof_rowx.py [ROW ...]        rows 0-13, default all

Per row and per line (N = the diffusion line, centre y 11815 + the row's offset; B = the band, centre
y 11963 + offset, but in s1 and s3 the bus field's row east of the jog, y 11922 and y 12984):
  edges   at x 4710, 4756, 4794: the darkest sample above and below the centre within 24 px, in chip
          2's metal shot (y and red), i.e. the line's two edge lines; `M` if metal (R > 177, G > 150) lies there instead;
  along   at y = centre, x 4696 .. 4792 in steps of 8: chip 2's metal shot R/G/B (metal is R > 177,
          G > 128; open poly orange, blue under 75; open diffusion plain, blue 85-95);
  under   at each track (x 4736 and x 4780 +-8: the brightest column 30 px off the line, taken as metal
          if chip 2 reads R > 170, G > 140 or chip 1 R > 170 there): the clean shot's R/G/B on the line
          under the track's centre and 30 px off it under the same track (the control: field under
          metal, pink; diffusion under metal is tan, poly cream). The control is south of a diffusion
          line (the track's pad lies 45-49 px north of it) and north of a band. 38 crossings in all.
Written for `eof` run 43 (piece `rj`). Offsets are those of the cell `eof_mx`.
"""
import os, sys
import numpy as np
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ld = lambda n: np.load(os.path.join(ROOT, 'cache', n), mmap_mode='r')
OFFS = [(0,-477),(0,0),(0,477),(0,954),(0,1431),(0,1909),(0,2386),(1,3079),(1,3557),(1,4034),(1,4684),(1,5162),(1,5639),(1,6116)]
BAND = {1: 11922, 3: 12984 - 954}
m, m1, a, c = ld('metal.npy'), ld('metal1.npy'), ld('acid_aligned.npy'), ld('acid1b.npy')
def mean(arr, x, y, h=1):
    return arr[y-h:y+h+1, x-h:x+h+1].reshape(-1, 3).astype(float).mean(0)
def ismetal(x, y):
    v = mean(m, x, y)
    return v[0] > 177 and v[1] > 150
def edges(x, yc):
    if ismetal(x, yc): return '   M   '
    col = [(mean(m, x, y)[0], y) for y in range(yc-24, yc+25)]
    up = min(col[:20]); dn = min(col[29:])
    return '%d(%3.0f) %d(%3.0f)' % (up[1], up[0], dn[1], dn[0])
rows = [int(r) for r in sys.argv[1:]] or range(14)
for r in rows:
    dx, dy = OFFS[r]
    for nm, y0 in (('N', 11815), ('B', BAND.get(r, 11963))):
        yc = y0 + dy
        print('s%-2d %s y %d  edges 4710: %s  4756: %s  4794: %s' % (r, nm, yc, edges(4710+dx, yc), edges(4756+dx, yc), edges(4794+dx, yc)))
        print('      along m2: ' + ' '.join('%3.0f/%3.0f/%3.0f' % tuple(mean(m, x+dx, yc)) for x in range(4696, 4793, 8)))
        # the tracks: at x 4736 and x 4780 (+-8), the brightest column 30 px off the line (south of a
        # diffusion line, whose north side has the track's pad; north of a band)
        off = 30 if nm == 'N' else -30
        for tx in (4736, 4780):
            red, x = max((mean(m, tx+dx+o, yc+off)[0], tx+dx+o) for o in range(-8, 9))
            g2, r1 = mean(m, x, yc+off)[1], mean(m1, x, yc+off)[0]
            if not ((red > 170 and g2 > 140) or r1 > 170) or (red < 150 and r1 < 150): continue
            if abs(g2 - mean(m, x, yc+off)[2]) < 60 and r1 < 170: continue      # open ground, not metal
            v, k = mean(c, x, yc, 2), mean(c, x, yc+off, 2)
            print('      under track x %d (chip 2 %3.0f, chip 1 %3.0f): clean %3.0f/%3.0f/%3.0f  control(%+d) %3.0f/%3.0f/%3.0f' % (x, red, r1, v[0], v[1], v[2], off, k[0], k[1], k[2]))
