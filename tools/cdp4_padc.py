#!/usr/bin/env python3
"""Where is the centre of the contact pad near X,Y? As text.

usage: cdp4_padc.py X,Y [X,Y ...]     (run from the repository's root: it reads cache/*.npy)

For each point, the centre of a contact pad near X,Y: centroid of the bright metal centre (chip 2 and chip 1,
R > 185 within +-9 px), and of the clean shot's hole (R-G < 24 within +-12), and the poly pad's extent in
the clean shot along the row and column through the centre (salmon: R > 185 and R-G > 30, or the hole)."""
import sys, numpy as np
m2 = np.load('cache/metal.npy', mmap_mode='r'); m1 = np.load('cache/metal1.npy', mmap_mode='r')
ac = np.load('cache/acid1b.npy', mmap_mode='r')
for p in sys.argv[1:]:
    x, y = map(int, p.split(','))
    out = []
    for m in (m2, m1):
        a = np.asarray(m[y-9:y+10, x-9:x+10, 0], float)
        ys, xs = np.nonzero(a > 185)
        out.append('%d,%d(n%d)' % (x-9+xs.mean(), y-9+ys.mean(), len(xs)) if len(xs) > 8 else 'none')
    a = np.asarray(ac[y-12:y+13, x-12:x+13, :3], float)
    ys, xs = np.nonzero(a[..., 0] - a[..., 1] < 24)
    out.append('%d,%d(n%d)' % (x-12+xs.mean(), y-12+ys.mean(), len(xs)) if len(xs) > 8 else 'none')
    def ext(line):
        ok = [(v[0] > 150 and v[0] - v[1] > -40 and not (v[0] - v[2] < 75 and v[0] > 170 and v[1] < 125)) and v[0] > 100 for v in line]
        return ok
    row = np.asarray(ac[y-1:y+2, x-40:x+41, :3], float).mean(axis=0)
    col = np.asarray(ac[y-40:y+41, x-1:x+2, :3], float).mean(axis=1)
    def pink(v): return v[0] > 165 and v[1] < 125 and v[2] > 105
    def dark(v): return v[0] < 110
    # east edge: first pink or dark-then-pink east of centre ; report first pink sample each way
    e = next((i for i in range(40, 81) if pink(row[i])), None)
    n = next((i for i in range(40, -1, -1) if pink(col[i])), None)
    s = next((i for i in range(40, 81) if pink(col[i])), None)
    out.append('pink E at x%s N at y%s S at y%s' % (x-40+e if e is not None else '?', y-40+n if n is not None else '?', y-40+s if s is not None else '?'))
    print(p, ' metal2 %s  metal1 %s  hole %s  %s' % tuple(out))
