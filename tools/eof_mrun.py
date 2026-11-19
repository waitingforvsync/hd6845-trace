#!/usr/bin/env python3
"""Metal runs along a cut, as text: where each metal line lies at one y (or one x).

usage: eof_mrun.py row Y X0 X1 [Y ...]      cuts along rows Y (several Y allowed after X1)
       eof_mrun.py col X Y0 Y1 [X ...]      cuts down columns X

For each cut it prints the runs of 5 px or more that pass the follower's metal test (red > 177 and
green > 128, mean over 5 px across the cut) in EITHER metal shot (chip 2 `metal`, chip 1 `metal1`),
each as centre(length). A straight track gives the same centre at every cut; a diagonal moves by the
cut spacing; a pad's ring is a gap in the run. Bare ground bright in chip 2 only can pass (tracing
guide, trap 30): the second line of each cut is chip 1 alone.

An aid for placing a metal's centre line and corners (the follower does not report diagonals); every
end and pad is still read on a view or a text map.
"""
import os, sys
import numpy as np
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ld = lambda n: np.load(os.path.join(ROOT, 'cache', n), mmap_mode='r')


def runs(t, a0, minlen=5):
    out = []; s = None
    for i, v in enumerate(list(t) + [False]):
        if v and s is None:
            s = i
        if not v and s is not None:
            if i - s >= minlen:
                out.append('%d(%d)' % (a0 + (s + i - 1) // 2, i - s))
            s = None
    return ' '.join(out) or 'none'


def cut(arr, kind, c, a0, a1, half=2):
    if kind == 'row':
        s = arr[c - half:c + half + 1, a0:a1 + 1].astype(float).mean(0)
    else:
        s = arr[a0:a1 + 1, c - half:c + half + 1].astype(float).mean(1)
    return (s[:, 0] > 177) & (s[:, 1] > 128)


def main():
    a = sys.argv[1:]
    if len(a) < 4 or a[0] not in ('row', 'col'):
        sys.exit(__doc__)
    kind = a[0]; c0, a0, a1 = int(a[1]), int(a[2]), int(a[3])
    m2, m1 = ld('metal.npy'), ld('metal1.npy')
    for c in [c0] + [int(v) for v in a[4:]]:
        t2, t1 = cut(m2, kind, c, a0, a1), cut(m1, kind, c, a0, a1)
        print('%s %5d  either: %s' % (kind, c, runs(t2 | t1, a0)))
        print('           chip 1: %s' % runs(t1, a0))


main()
