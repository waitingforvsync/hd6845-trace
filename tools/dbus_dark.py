#!/usr/bin/env python3
"""Dark edge lines along a cut:  dbus_dark.py LAYER col X Y0 Y1 [half]   or   ... row Y X0 X1 [half]

Prints the runs where brightness (R+G+B, mean over 2*half+1 px across the cut) falls below
0.62 of the cut's median: outlines of poly, diffusion and contacts in the stripped shots.
LAYER: metal, metal1, acid (aligned), acid1b.
"""
import os, sys
import numpy as np
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
F = {'metal': 'metal.npy', 'acid': 'acid_aligned.npy', 'metal1': 'metal1.npy', 'acid1b': 'acid1b.npy'}
def runs(p, thr):
    out, run = [], None
    for i, v in enumerate(p):
        if v < thr:
            run = [i, i] if run is None else [run[0], i]
        elif run is not None:
            out.append(run); run = None
    if run: out.append(run)
    return out
def main():
    lay, kind, c, a, b = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
    h = int(sys.argv[6]) if len(sys.argv) > 6 else 3
    A = np.load(os.path.join(ROOT, 'cache', F[lay]), mmap_mode='r')
    if kind == 'col':
        p = A[a:b, c - h:c + h + 1].astype(float).sum(axis=2).mean(axis=1)
    else:
        p = A[c - h:c + h + 1, a:b].astype(float).sum(axis=2).mean(axis=0)
    thr = np.median(p) * 0.62
    print(lay, kind, c, ' '.join(f'{a + r[0]}-{a + r[1]}' for r in runs(p, thr)))
main()
