#!/usr/bin/env python3
"""Median of the nineteen ral_cell copies (five RA, fourteen MA turned 90 degrees, eleven
of those mirrored) in the master's frame, written as composite ral_c19 for view.py --comp.

usage: ral_comp19.py [--groups]
--groups also writes the two groups separately over a wider window (13950-14480 x
4180-4620, which takes in the VCC contact of inverter 1's load and the bar's west end):
ral_cr (the five RA copies) and ral_cm (the fourteen MA copies). The two groups sit in
different surroundings and under different metal, so what both medians show belongs to
the cell; the chip-1 metal shot (metal1) of ral_cm was the clearest view of inverter 1.
The MA copies are undone with the inverse of their @inst transform (their placements are
listed below; they are drawn in trace/mal.txt):
a master point p maps to the copy at R90(mirror(p)) + offset, about o = (14235,4395).
"""
import json, os, sys
import numpy as np
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
X0, Y0, X1, Y1 = 13990, 4240, 14460, 4600
O = (14235, 4395)
RA = [0, 434, 868, 1431, 1865]
MA = [(-11576, 3760, 1), (-11576, 4366, 1), (-11576, 4973, 1), (-11576, 5581, 1),
      (-11576, 6232, 1), (-11576, 6839, 1), (-11576, 7641, 1), (-11575, 8335, 1),
      (-11575, 8987, 1), (-11575, 11111, 1), (-11575, 11806, 1), (-11574, 12880, 0),
      (-11574, 13530, 0), (-11574, 14181, 0)]
F = {'metal': 'metal.npy', 'acid': 'acid_aligned.npy', 'acid1b': 'acid1b.npy', 'metal1': 'metal1.npy'}
def median(x0, y0, x1, y1, ra, ma):
    ys, xs = np.mgrid[y0:y1, x0:x1]
    out = {}
    for lay, fn in F.items():
        A = np.load(os.path.join(ROOT, 'cache', fn), mmap_mode='r')
        stack = []
        for dx in ra:
            stack.append(np.asarray(A[y0:y1, x0 + dx:x1 + dx]))
        for dx, dy, mx in ma:
            px = (2 * O[0] - xs) if mx else xs
            py = ys
            # rotate 90 degrees clockwise about O (as seen on the photo: x' = ox - (y-oy), y' = oy + (x-ox))
            rx = O[0] - (py - O[1]); ry = O[1] + (px - O[0])
            sx = (rx + dx).astype(int); sy = (ry + dy).astype(int)
            stack.append(np.asarray(A[sy, sx]))
        out[lay] = np.median(np.stack(stack), axis=0).astype(np.uint8)
    return out


def write(name, x0, y0, x1, y1, ra, ma):
    out = median(x0, y0, x1, y1, ra, ma)
    d = os.path.join(ROOT, 'cache', 'comp'); os.makedirs(d, exist_ok=True)
    for lay, a in out.items():
        np.save(os.path.join(d, '%s_%s.npy' % (name, lay)), a)
    json.dump({'x0': x0, 'y0': y0, 'w': x1 - x0, 'h': y1 - y0, 'n': len(ra) + len(ma)},
              open(os.path.join(d, name + '.json'), 'w'))
    print('%s: median of %d copies, %d x %d' % (name, len(ra) + len(ma), x1 - x0, y1 - y0))


write('ral_c19', X0, Y0, X1, Y1, RA, MA)
if '--groups' in sys.argv:
    write('ral_cr', 13950, 4180, 14480, 4620, RA, [])
    write('ral_cm', 13950, 4180, 14480, 4620, [], MA)
