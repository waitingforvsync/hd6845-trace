#!/usr/bin/env python3
"""Continuity of a thin vertical metal as text: where is it dark, and for how long.

usage: tl3_thin.py X0 X1 Y0 Y1 [--thr N] [--min N]

For every y from Y0 to Y1 the brightest 3x3 mean (red channel) found between X0 and X1 in the
chip-2 metal shot and in the chip-1 metal shot, i.e. "is there metal anywhere across the
line's width at this y". It prints the stretches of y in which neither shot reaches the
threshold (default 144 = digit 9 of tools/textmap.py; metal is C-E there, an edge under the
metal 2-6), with for each the lowest and highest value seen in each shot, and, for comparison,
the stretches where only one shot is dark. --min drops stretches shorter than N px (default 3).

What it is for (tracing guide, traps 3, 19, 22): a thin metal is dark for 6-14 px where the
edge of a poly row or a diffusion passes under it, and for 30-80 px over a buried-contact box;
neither is a break. This lists every such stretch on a line in one call, so that the long ones
can be looked at and the short ones compared with the bars the same line has over plain rows.
It does not decide anything: a stretch dark in both shots is a place to read, not a break.
"""
import os
import sys
import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def take(a, flag, default):
    if flag in a:
        i = a.index(flag)
        v = int(a[i + 1])
        del a[i:i + 2]
        return v
    return default


def main():
    a = sys.argv[1:]
    thr = take(a, '--thr', 144)
    mn = take(a, '--min', 3)
    if len(a) != 4:
        sys.exit(__doc__)
    x0, x1, y0, y1 = map(int, a)
    shots = [np.load(os.path.join(ROOT, 'cache', f), mmap_mode='r') for f in ('metal.npy', 'metal1.npy')]

    def best(arr, y):
        blk = np.asarray(arr[y - 1:y + 2, x0 - 1:x1 + 2, 0], dtype=float)
        col = blk.mean(0)
        k = np.convolve(col, np.ones(3) / 3, mode='valid')
        return k.max()

    ys = list(range(y0, y1 + 1))
    v = np.array([[best(s, y) for s in shots] for y in ys])
    dark = v < thr

    def runs(mask):
        out, start = [], None
        for i, m in enumerate(mask):
            if m and start is None:
                start = i
            if not m and start is not None:
                out.append((start, i - 1))
                start = None
        if start is not None:
            out.append((start, len(mask) - 1))
        return [r for r in out if r[1] - r[0] + 1 >= mn]

    print('thin metal x %d-%d, y %d-%d: brightest sample across the width, threshold %d' % (x0, x1, y0, y1, thr))
    print('dark in BOTH metal shots:')
    for s, e in runs(dark[:, 0] & dark[:, 1]):
        print('  y %d-%d  %3d px   chip 2 %3.0f-%3.0f   chip 1 %3.0f-%3.0f'
              % (ys[s], ys[e], e - s + 1, v[s:e + 1, 0].min(), v[s:e + 1, 0].max(),
                 v[s:e + 1, 1].min(), v[s:e + 1, 1].max()))
    for k, name in ((0, 'chip 2'), (1, 'chip 1')):
        only = dark[:, k] & ~dark[:, 1 - k]
        r = runs(only)
        print('dark in %s only: %s' % (name, ', '.join('y %d-%d (%d)' % (ys[s], ys[e], e - s + 1) for s, e in r) or 'none'))


if __name__ == '__main__':
    main()
