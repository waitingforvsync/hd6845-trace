#!/usr/bin/env python3
"""Poly lines along a cut, as text: where a bundle of poly rows (or diagonals) lies at one x or y.

usage: eof_rows.py col X Y0 Y1 [--thr N] [--half N]     a cut down column X
       eof_rows.py row Y X0 X1 [--thr N] [--half N]     a cut along row Y
       eof_rows.py diag X0 Y0 X1 Y1 [--step N] [--reach N]   along a slanted line from X0,Y0 to X1,Y1

diag: every `step` px (default 12) along the line it cuts across it (perpendicular, `reach` px to
either side, default 50) and prints the poly runs as offset(length): the followed line stays near
offset 0, its neighbours in the bundle at their pitch either side; negative offsets are on the left
when looking from X0,Y0 to X1,Y1.

For each of the two stripped shots it prints the runs of 6 px or more that read as poly, each as
centre(length):
  acid   chip 2, stripped: red - green > thr (default 30) and red > 90 (poly is orange there in
         the open: red over green by 40-80; field is under 25; under a metal's ghost it shows only
         fringes, so read those stretches in the clean shot's line)
  clean  chip 1, clean (acid1b): salmon under metal (red > 205, red - green > 45) or dark
         red-brown in the open (red - green > 25, red < 195, blue < 110)
Each sample is the mean over 2*half+1 px across the cut (default half 2). A bundle that keeps its
order shows the same number of runs at every cut; a line that steps a track shows as a shifted
run. An aid for following one line through a bundle: every end and pad is still read on a view.
"""
import os, sys
import numpy as np
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ld = lambda n: np.load(os.path.join(ROOT, 'cache', n), mmap_mode='r')


def runs(t, a0, minlen=6):
    out = []; s = None
    for i, v in enumerate(list(t) + [False]):
        if v and s is None:
            s = i
        if not v and s is not None:
            if i - s >= minlen:
                out.append('%d(%d)' % (a0 + (s + i - 1) // 2, i - s))
            s = None
    return ' '.join(out) or 'none'


def test(name, R, G, B, thr):
    if name == 'acid ':
        return (R - G > thr) & (R > 90)
    return ((R > 205) & (R - G > 45)) | ((R - G > 25) & (R < 195) & (B < 110))


def diag(a, thr):
    step, reach = 12, 50
    if '--step' in a:
        i = a.index('--step'); step = int(a[i + 1]); del a[i:i + 2]
    if '--reach' in a:
        i = a.index('--reach'); reach = int(a[i + 1]); del a[i:i + 2]
    x0, y0, x1, y1 = [float(v) for v in a[1:5]]
    L = np.hypot(x1 - x0, y1 - y0)
    ux, uy = (x1 - x0) / L, (y1 - y0) / L
    nx, ny = uy, -ux                      # left of the direction of travel (y is down)
    shots = [(n, ld(f)) for n, f in (('acid ', 'acid_aligned.npy'), ('clean', 'acid1b.npy'))]
    offs = np.arange(-reach, reach + 1)
    for d in np.arange(0, L + 1, step):
        cx, cy = x0 + ux * d, y0 + uy * d
        out = []
        for name, A in shots:
            acc = np.zeros((len(offs), 3))
            for k in (-2, -1, 0, 1, 2):   # mean over 5 px along the line
                xs = np.rint(cx + ux * k - nx * offs).astype(int)
                ys = np.rint(cy + uy * k - ny * offs).astype(int)
                acc += np.asarray(A[ys, xs]).astype(float)
            acc /= 5
            on = test(name, acc[:, 0], acc[:, 1], acc[:, 2], thr)
            out.append('%s %s' % (name.strip(), runs(on, -reach, 5)))
        print('%5d,%-5d  %s' % (cx, cy, '   '.join(out)))


def main():
    a = sys.argv[1:]
    thr, half = 30, 2
    if '--thr' in a:
        i = a.index('--thr'); thr = int(a[i + 1]); del a[i:i + 2]
    if '--half' in a:
        i = a.index('--half'); half = int(a[i + 1]); del a[i:i + 2]
    if a[0] == 'diag':
        return diag(a, thr)
    mode, c, p0, p1 = a[0], int(a[1]), int(a[2]), int(a[3])
    for name, f in (('acid ', 'acid_aligned.npy'), ('clean', 'acid1b.npy')):
        A = ld(f)
        if mode == 'row':
            s = np.asarray(A[c - half:c + half + 1, p0:p1]).astype(float).mean(0)
        else:
            s = np.asarray(A[p0:p1, c - half:c + half + 1]).astype(float).mean(1)
        R, G, B = s[:, 0], s[:, 1], s[:, 2]
        if name == 'acid ':
            on = (R - G > thr) & (R > 90)
        else:
            on = ((R > 205) & (R - G > 45)) | ((R - G > 25) & (R < 195) & (B < 110))
        print('%s %s %d: %s' % (name, mode, c, runs(on, p0)))


if __name__ == '__main__':
    main()
