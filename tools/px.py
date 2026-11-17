#!/usr/bin/env python3
"""Colour profiles of the die as text: rows, columns and points, in any of the shots.

usage: px.py row Y X0 X1 STEP [layers] [--r N] [--comp NAME]     samples along a row
       px.py col X Y0 Y1 STEP [layers] [--r N] [--comp NAME]     samples down a column
       px.py pt X,Y[,R] [X,Y[,R] ...] [layers] [--r N] [--comp NAME]   single points

layers  comma list from metal, metal1, acid, acid1, acid1b, or `all` (= metal,metal1,acid,acid1b);
        default acid1b,metal. `acid` is the chip-2 stripped shot as aligned
        (cache/acid_aligned.npy), like every other tool.
--r N   half-size of the patch each sample is the mean of: default 1 (3x3) for row and col,
        2 (5x5) for pt; a point written X,Y,R has its own.
--comp NAME   read the median composite NAME (tools/composite.py) instead of the die;
        coordinates stay those of the master.

One line per sample: x, y, then R G B per layer. No image is made, so it costs nothing to
read. Use it to settle what the eye cannot: a profile across a junction (does the poly
reach the pad, or is there field between), across a strip (a diffusion wire in the open is
a strip between two dark edges, a little redder than field), along a thin metal (bare ground
or metal), or on a patch whose class is in doubt. Compare with a known feature nearby: the
colours drift across the die (tracing guide, trap 1).

The shared form of tools/tc1_px.py (same output for the same row, col and pt arguments) and
tools/larr_px.py (same numbers; that one prints all four layers with slashes).
"""
import json
import os
import sys
import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
F = {'metal': 'metal.npy', 'acid': 'acid_aligned.npy', 'metal1': 'metal1.npy', 'acid1': 'acid1.npy',
     'acid1b': 'acid1b.npy'}
ALL = ['metal', 'metal1', 'acid', 'acid1b']


def is_point(t):
    return ',' in t and t[0].isdigit()


def take(args, flag):
    """Remove `flag VALUE` from args and return VALUE (None if absent)."""
    if flag not in args:
        return None
    i = args.index(flag)
    if i + 1 >= len(args):
        sys.exit('%s needs a value' % flag)
    v = args[i + 1]
    del args[i:i + 2]
    return v


def main():
    a = sys.argv[1:]
    comp = take(a, '--comp')
    r_opt = take(a, '--r')
    if not a or a[0] not in ('row', 'col', 'pt'):
        sys.exit(__doc__)
    mode = a[0]
    if mode == 'pt':
        r0 = int(r_opt) if r_opt else 2
        pts = []
        for t in a[1:]:
            if is_point(t):
                p = list(map(int, t.split(',')))
                pts.append((p[0], p[1], p[2] if len(p) > 2 else r0))
        rest = [t for t in a[1:] if not is_point(t)]
        lay = rest[0] if rest else None
    else:
        if len(a) < 5:
            sys.exit(__doc__)
        r0 = int(r_opt) if r_opt else 1
        c, p0, p1, st = map(int, a[1:5])
        lay = a[5] if len(a) > 5 else None
        pts = [(c, v, r0) if mode == 'col' else (v, c, r0) for v in range(p0, p1 + 1, st)]
    layers = ALL if lay == 'all' else lay.split(',') if lay else ['acid1b', 'metal']
    bad = [l for l in layers if l not in F]
    if bad:
        sys.exit('unknown layer %s (known: %s)' % (' '.join(bad), ', '.join(F)))
    ox = oy = 0
    if comp:
        d = os.path.join(ROOT, 'cache', 'comp')
        j = json.load(open(os.path.join(d, comp + '.json')))
        ox, oy = j['x0'], j['y0']
        A = {l: np.load(os.path.join(d, '%s_%s.npy' % (comp, l))) for l in layers}
    else:
        A = {l: np.load(os.path.join(ROOT, 'cache', F[l]), mmap_mode='r') for l in layers}
    print('     x     y  ' + '  '.join('%-11s' % l for l in layers))
    for x, y, r in pts:
        u, v = x - ox, y - oy
        print('%6d %5d  ' % (x, y) + '  '.join(
            '%3d %3d %3d' % tuple(A[l][v - r:v + r + 1, u - r:u + r + 1].reshape(-1, 3).mean(0)) for l in layers))


if __name__ == '__main__':
    main()
