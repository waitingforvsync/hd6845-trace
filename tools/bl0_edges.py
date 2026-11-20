#!/usr/bin/env python3
"""Edge lines along a cut, as text: where the dark outline lines lie and what colour is between.

usage: bl0_edges.py row Y X0 X1 [layer] [--half N] [--thr T]
       bl0_edges.py col X Y0 Y1 [layer] [--half N] [--thr T]

layer: metal, metal1, acid, acid1b (default acid1b). Each sample is the mean over 2N+1 px
across the cut (default N=3). A dark line is a run where brightness (R+G+B) is under T times
the cut's median (default 0.72) ; printed: the dark runs (start-end) and, between them, the
segment with its mean R G B and red minus green. Edges are good to about 2 px. Text only.
"""
import os, sys
import numpy as np
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
F = {'metal': 'metal.npy', 'acid': 'acid_aligned.npy', 'metal1': 'metal1.npy', 'acid1': 'acid1.npy', 'acid1b': 'acid1b.npy'}

def main():
    a = sys.argv[1:]
    half, thr = 3, 0.72
    if '--half' in a:
        i = a.index('--half'); half = int(a[i + 1]); del a[i:i + 2]
    if '--thr' in a:
        i = a.index('--thr'); thr = float(a[i + 1]); del a[i:i + 2]
    if len(a) < 4:
        sys.exit(__doc__)
    kind, p, q0, q1 = a[0], int(a[1]), int(a[2]), int(a[3])
    layer = a[4] if len(a) > 4 else 'acid1b'
    im = np.load(os.path.join(ROOT, 'cache', F[layer]), mmap_mode='r')
    if kind == 'row':
        s = np.asarray(im[p - half:p + half + 1, q0:q1 + 1, :3], dtype=float).mean(axis=0)
    else:
        s = np.asarray(im[q0:q1 + 1, p - half:p + half + 1, :3], dtype=float).mean(axis=1)
    b = s.sum(axis=1)
    dark = b < thr * np.median(b)
    print(f'{kind} {p} {q0}-{q1} {layer}: median brightness {np.median(b):.0f}, dark under {thr * np.median(b):.0f}')
    i, n = 0, len(b)
    while i < n:
        j = i
        while j < n and dark[j] == dark[i]:
            j += 1
        seg = s[i:j].mean(axis=0)
        if dark[i]:
            print(f'  {q0 + i:6d}-{q0 + j - 1:<6d} dark  ({j - i} px, min {b[i:j].min():.0f})')
        else:
            print(f'  {q0 + i:6d}-{q0 + j - 1:<6d} {j - i:4d} px  {seg[0]:4.0f} {seg[1]:4.0f} {seg[2]:4.0f}  r-g {seg[0] - seg[1]:+4.0f}')
        i = j

main()
