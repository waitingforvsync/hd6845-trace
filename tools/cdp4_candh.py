#!/usr/bin/env python3
"""The pad test of cdp4_cand.py for a horizontal (h) or vertical (v) thin metal, with an automatic verdict.

usage: cdp4_candh.py [-v] h|v X,Y [X,Y ...]     (run from the repository's root: it reads cache/*.npy)

Along the track through each point (+-33 px, step 3, median over 5 px across) in
chip-2 and chip-1 metal red: PAD if in BOTH chips there is a bright centre (>= 160) of 2-6 samples within
+-9 px of the point with a dark run (< 112) of 3 or more samples within 24 px on each side of it. Also the
clean shot's minimum red-green on the centre line within +-9 px. Prints every point with -v, else only PAD
ones and a count."""
import sys, numpy as np
m2 = np.load('cache/metal.npy', mmap_mode='r'); m1 = np.load('cache/metal1.npy', mmap_mode='r')
ac = np.load('cache/acid1b.npy', mmap_mode='r')
a = sys.argv[1:]; verbose = '-v' in a
if verbose: a.remove('-v')
o = a[0]; H = '0123456789ABCDEF'
def strip(m, x, y):
    v = []
    for t in range(-33, 34, 3):
        if o == 'v': v.append(np.median(np.asarray(m[y+t-1:y+t+2, x-2:x+3, 0], float)))
        else: v.append(np.median(np.asarray(m[y-2:y+3, x+t-1:x+t+2, 0], float)))
    return v
def padlike(v):
    n = len(v); c = n // 2
    for i in range(c - 3, c + 4):
        if v[i] < 160: continue
        # extend bright centre
        l = i
        while l > 0 and v[l-1] >= 150: l -= 1
        r = i
        while r < n - 1 and v[r+1] >= 150: r += 1
        if r - l + 1 > 7: continue
        def dark(seq): 
            run = 0
            for q in seq[:8]:
                if q < 112: run += 1
                else:
                    if run >= 3: return True
                    run = 0
            return run >= 3
        if dark(v[l-1::-1] if l > 0 else []) and dark(v[r+1:]): return True
    return False
npad = 0
for p in a[1:]:
    x, y = map(int, p.split(','))
    s2, s1 = strip(m2, x, y), strip(m1, x, y)
    if o == 'v': c = np.asarray(ac[y-9:y+10, x-3:x+4, :3], float); rg = np.median(c[..., 0] - c[..., 1], axis=1).min()
    else: c = np.asarray(ac[y-3:y+4, x-9:x+10, :3], float); rg = np.median(c[..., 0] - c[..., 1], axis=0).min()
    pad = padlike(s2) or padlike(s1) or rg < 30
    npad += pad
    if verbose or pad:
        print('%5d,%5d %s | %s  clean min %4d  %s' % (x, y, ''.join(H[min(15, int(q)//16)] for q in s2), ''.join(H[min(15, int(q)//16)] for q in s1), rg, 'PAD' if pad else ''))
print('%d points, %d pad-like' % (len(a) - 1, npad))
