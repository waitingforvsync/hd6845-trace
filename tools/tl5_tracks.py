#!/usr/bin/env python3
"""Checks along a straight piece of a thin metal track, and rows through a track field, as text.

usage: tl5_tracks.py v X Y0 Y1 [--half N]      a vertical piece: metal test and contact scan
       tl5_tracks.py h Y X0 X1 [--half N]      a horizontal piece
       tl5_tracks.py rows col Y0 Y1 STEP X [X ...]    the clean shot down columns X, one char per sample
       tl5_tracks.py rows row X0 X1 STEP Y [Y ...]    the same along rows Y

v / h: (1) the follower's metal test (median red > 177 and green > 128 across 2*half+1 px, default
half 3) in both metal shots: prints the stretches of 8 px or more where NEITHER chip passes, and the
stretches of 20 px or more where chip 2 or chip 1 alone fails. A break in a metal is 25 px or
more without metal in both; a ring of a contact or an edge underneath is shorter (tracing guide,
traps 3, 19). (2) the clean shot (acid1b) along the same line: stretches of 6 px or more where
red - green (9 px across, smoothed over 5) is under 24: the green hole of a contact on a pad, or
open ground (where the piece has no metal). Each is given as centre(length,minimum).

rows: P poly under metal (cream: red > 205, green > 150), p poly in the open (red - green > 25,
red < 195, blue < 110), k pink (field under metal), . anything else. A row that steps a track
between two cuts shows as a shifted run.

An aid: every end and pad it points at is still read on a view.
"""
import os, sys
import numpy as np
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ld = lambda n: np.load(os.path.join(ROOT, 'cache', n), mmap_mode='r')

def runs(t, a0, minlen):
    out = []; s = None
    for i, v in enumerate(list(t) + [False]):
        if v and s is None: s = i
        if not v and s is not None:
            if i - s >= minlen: out.append((a0 + s, a0 + i - 1))
            s = None
    return out

def strip(arr, kind, c, a0, a1, half):
    if kind == 'v':
        return np.asarray(arr[a0:a1, c - half:c + half + 1, :3]).astype(float)
    return np.asarray(arr[c - half:c + half + 1, a0:a1, :3]).astype(float).transpose(1, 0, 2)

def main():
    a = sys.argv[1:]
    if a[0] == 'rows':
        B = ld('acid1b.npy'); kind = a[1]; a0, a1, st = map(int, a[2:5])
        for c in map(int, a[5:]):
            s = ''
            for p in range(a0, a1, st):
                v = (B[p - 1:p + 2, c - 2:c + 3] if kind == 'col' else B[c - 2:c + 3, p - 1:p + 2])
                r, g, b = np.asarray(v).reshape(-1, 3)[:, :3].mean(axis=0)
                s += ('P' if r > 205 and g > 150 else 'p' if r - g > 25 and r < 195 and b < 110
                      else 'k' if r > 170 and r - g > 45 and b > 110 else '.')
            print('%5d %s' % (c, s))
        return
    half = 3
    if '--half' in a:
        i = a.index('--half'); half = int(a[i + 1]); del a[i:i + 2]
    kind, c, a0, a1 = a[0], int(a[1]), int(a[2]), int(a[3])
    res = {}
    for nm, f in (('chip2', 'metal.npy'), ('chip1', 'metal1.npy')):
        s = strip(ld(f), kind, c, a0, a1, half)
        res[nm] = (np.median(s[:, :, 0], axis=1) > 177) & (np.median(s[:, :, 1], axis=1) > 128)
    f = lambda rr: ' '.join('%d-%d' % r for r in rr) or 'none'
    print('no metal in both (>= 8 px):', f(runs(~res['chip2'] & ~res['chip1'], a0, 8)))
    print('chip 2 fails (>= 20 px):  ', f(runs(~res['chip2'], a0, 20)))
    print('chip 1 fails (>= 20 px):  ', f(runs(~res['chip1'], a0, 20)))
    s = strip(ld('acid1b.npy'), kind, c, a0, a1, 4)
    d = np.convolve((s[:, :, 0] - s[:, :, 1]).mean(axis=1), np.ones(5) / 5, 'same')
    out = []
    for r0, r1 in runs(d < 24, a0, 6):
        out.append('%d(%d,%d)' % ((r0 + r1) // 2, r1 - r0 + 1, int(d[r0 - a0:r1 - a0 + 1].min())))
    print('clean shot, red - green < 24:', ' '.join(out) or 'none')

main()
