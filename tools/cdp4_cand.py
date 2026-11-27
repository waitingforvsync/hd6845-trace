#!/usr/bin/env python3
"""Is this spot on a thin vertical metal a contact pad? Three strips as text.

usage: cdp4_cand.py X,Y [X,Y ...]     (run from the repository's root: it reads cache/*.npy)

For each point on a thin vertical metal print three strips as hex digits:
along the centre line y-33..y+33 step 3 in chip-2 metal R/16 and chip-1 metal R/16 (median over 5 px
across), the clean shot (R-G)/8 along the same (g = negative), and across the track at y, x-24..x+24
step 3, chip-2 R/16 | chip-1 R/16. A contact pad: along = bright, dark ring, bright centre (~12 px),
dark ring, bright; across = ground, dark ring at +-15, bright centre. A plain track: across = ground,
dark edge at +-8, bright."""
import sys, numpy as np
m2 = np.load('cache/metal.npy', mmap_mode='r'); m1 = np.load('cache/metal1.npy', mmap_mode='r')
ac = np.load('cache/acid1b.npy', mmap_mode='r')
H = '0123456789ABCDEF'
def h(v): return H[max(0, min(15, int(v) // 16))]
def g(v): return 'g' if v < 0 else H[max(0, min(15, int(v) // 8))]
for p in sys.argv[1:]:
    x, y = map(int, p.split(','))
    al2 = ''.join(h(np.median(np.asarray(m2[yy-1:yy+2, x-2:x+3, 0], float))) for yy in range(y-33, y+34, 3))
    al1 = ''.join(h(np.median(np.asarray(m1[yy-1:yy+2, x-2:x+3, 0], float))) for yy in range(y-33, y+34, 3))
    cl = ''
    for yy in range(y-33, y+34, 3):
        a = np.asarray(ac[yy-1:yy+2, x-3:x+4, :3], float)
        cl += g(np.median(a[..., 0] - a[..., 1]))
    ax2 = ''.join(h(np.median(np.asarray(m2[y-2:y+3, xx-1:xx+2, 0], float))) for xx in range(x-24, x+25, 3))
    ax1 = ''.join(h(np.median(np.asarray(m1[y-2:y+3, xx-1:xx+2, 0], float))) for xx in range(x-24, x+25, 3))
    print('%5d,%5d  along %s | %s  clean %s  across %s | %s' % (x, y, al2, al1, cl, ax2, ax1))
