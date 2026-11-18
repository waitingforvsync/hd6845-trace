#!/usr/bin/env python3
"""Colour profile across a feature, averaged along it: the edges of a band as text.

usage: tl1_band.py x X0 X1 Y0 Y1 [STEP] [layers]    one line per x (X0..X1), mean over rows Y0..Y1
       tl1_band.py y Y0 Y1 X0 X1 [STEP] [layers]    one line per y (Y0..Y1), mean over columns X0..X1

layers  comma list from metal, metal1, acid, acid1b (default: all four). STEP default 1.

tools/px.py gives one 3x3 patch per sample, which on a 10 px sliver between two metals is
mostly noise and edge lines. This averages each sample over the whole length of the feature
(say the 25 rows of a gate band), so that a poly's two edge lines stand out as two dips and
the plateau between them can be compared with a plateau of known class beside it. Prints
R/G/B per layer and, per layer, R minus G (poly in the open is red-brown, R-G large; field
and narrow open diffusion are not).
"""
import os
import sys
import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
F = {'metal': 'metal.npy', 'acid': 'acid_aligned.npy', 'metal1': 'metal1.npy', 'acid1b': 'acid1b.npy'}


def main():
    a = sys.argv[1:]
    if len(a) < 5 or a[0] not in ('x', 'y'):
        sys.exit(__doc__)
    p0, p1, q0, q1 = map(int, a[1:5])
    rest = a[5:]
    step = 1
    layers = ['metal', 'metal1', 'acid', 'acid1b']
    for t in rest:
        if t.isdigit():
            step = int(t)
        else:
            layers = t.split(',')
    arr = {l: np.load(os.path.join(ROOT, 'cache', F[l]), mmap_mode='r') for l in layers}
    print('%5s  ' % a[0] + '   '.join('%-17s' % l for l in layers))
    for p in range(p0, p1 + 1, step):
        out = []
        for l in layers:
            if a[0] == 'x':
                v = np.asarray(arr[l][q0:q1 + 1, p:p + step]).reshape(-1, 3).mean(axis=0)
            else:
                v = np.asarray(arr[l][p:p + step, q0:q1 + 1]).reshape(-1, 3).mean(axis=0)
            out.append('%3d/%3d/%3d %+4d' % (v[0], v[1], v[2], v[0] - v[1]))
        print('%5d  ' % p + '   '.join(out))


if __name__ == '__main__':
    main()
