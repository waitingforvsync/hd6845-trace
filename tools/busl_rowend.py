#!/usr/bin/env python3
"""Where a horizontal row line (two dark edge lines in the clean shot) runs and stops, as text.

usage: busl_rowend.py YC X0 X1 [--thr 115] [--win 18]

Walks from X0 to X1 in 2 px steps. At each x it looks in the clean shot (acid1b) for the darkest
pixel (red, 3 px mean along x) in the windows above and below the centre line; the line is
"present" where both are under --thr and the strip between them is paler than both by 30. The
centre follows the edges (so a slow drift or a small step is followed). Prints the present runs,
the gaps of 10 px or more, and the edge positions every 100 px. An aid: every end it reports is
still read on a view (a pad, a corner and a crossing all look like an end to it).
"""
import os, sys
import numpy as np
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
a = sys.argv[1:]
thr, win = 115, 18
for k in ('--thr', '--win'):
    if k in a:
        i = a.index(k); v = int(a[i + 1]); del a[i:i + 2]
        if k == '--thr': thr = v
        else: win = v
yc, x0, x1 = map(int, a[:3])
B = np.load(os.path.join(ROOT, 'cache', 'acid1b.npy'), mmap_mode='r')
st = 2 if x1 > x0 else -2
pres = []; yc_f = float(yc); log = []
for x in range(x0, x1, st):
    c = int(round(yc_f))
    col = np.asarray(B[c - win:c + win + 1, x - 1:x + 2, 0]).astype(float).mean(axis=1)
    up = col[:win - 3]; dn = col[win + 4:]
    iu = int(up.argmin()); idn = int(dn.argmin()) + win + 4
    mid = col[iu + 3:idn - 2].max() if idn - iu > 6 else 0
    ok = up[iu] < thr and dn[idn - win - 4] < thr and mid > max(up[iu], dn[idn - win - 4]) + 30 and 12 <= idn - iu <= 34
    pres.append((x, ok, c - win + iu, c - win + idn))
    if ok:
        yc_f += 0.3 * (((c - win + iu) + (c - win + idn)) / 2.0 - yc_f)
s = None; last = None
for x, ok, u, d in pres + [(x1, None, 0, 0)]:
    if ok and s is None: s = (x, u, d)
    if s is not None and ok: last = (x, u, d)
    if not ok and s is not None:
        log.append((s, last)); s = None
out = []
for (s, e) in log:
    if out and abs(s[0] - out[-1][1][0]) < 10: out[-1] = (out[-1][0], e)
    else: out.append((s, e))
for s, e in out:
    if abs(e[0] - s[0]) >= 6:
        print('present x %5d .. %5d   edges y %d/%d .. %d/%d' % (s[0], e[0], s[1], s[2], e[1], e[2]))
