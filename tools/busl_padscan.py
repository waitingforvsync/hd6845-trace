#!/usr/bin/env python3
"""Pads along one thin metal track, from the dark ring beside it in both metal shots (text).

usage: busl_padscan.py v X Y0 Y1 [--off 16] [--min 20]     a vertical piece at x = X
       busl_padscan.py h Y X0 X1 [--off 16] [--min 20]     a horizontal piece at y = Y

A contact pad on a thin metal is about 40 px square with a dark ring: beside the track, 14-19 px
from its centre line, the ring is dark for the pad's whole length (36-44 px) on every side from
which no line leaves the pad. Where the track only crosses a row, the same flank shows the row's
two edge lines (6-10 px each) with the bright row between. So: at every px along the piece the
red of each flank (mean over off-3 .. off+2 px from the centre line) is read in the chip-2 metal
shot and in chip 1's, and the stretches of --min px or more where one flank is under 80 in BOTH
chips are printed (side, start-end, length). Calibrated on the pads (6817,9990), (5713,12443)
(42-46 px on the east flank) against the crossings of x 6798 at y 14540-14720 (6-8 px).
A corner of the track itself, a neighbouring track 16 px away and a wide dark feature beside the
track also read so: an aid that says where to look; every stretch it lists is read on a view, and
a track with none is still looked at where a tap is suspected.
"""
import sys
import numpy as np
a = sys.argv[1:]
off = 16; mn = 20
if '--off' in a:
    i = a.index('--off'); off = int(a[i + 1]); del a[i:i + 2]
if '--min' in a:
    i = a.index('--min'); mn = int(a[i + 1]); del a[i:i + 2]
d, c, p0, p1 = a[0], int(a[1]), int(a[2]), int(a[3])
def flank(name, sgn):
    m = np.load('cache/%s.npy' % name, mmap_mode='r')
    lo, hi = (c + off - 3, c + off + 3) if sgn > 0 else (c - off - 2, c - off + 4)
    if d == 'v': return np.asarray(m[p0:p1, lo:hi, 0], dtype=float).mean(axis=1)
    return np.asarray(m[lo:hi, p0:p1, 0], dtype=float).mean(axis=0)
n = 0
for sgn, side in ((-1, 'west' if d == 'v' else 'north'), (1, 'east' if d == 'v' else 'south')):
    t = (flank('metal', sgn) < 80) & (flank('metal1', sgn) < 80)
    s = None
    for i, v in enumerate(list(t) + [False]):
        if v and s is None: s = i
        elif not v and s is not None:
            if i - s >= mn:
                print('  %s flank dark %d-%d (%d px), centre %d' % (side, p0 + s, p0 + i - 1, i - s, p0 + (s + i) // 2)); n += 1
            s = None
print('%s %d, %d..%d: %d stretches' % (d, c, p0, p1, n))
