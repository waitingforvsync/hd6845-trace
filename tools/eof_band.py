#!/usr/bin/env python3
"""Class a narrow band between two edge lines over the WHOLE band: eof_band.py h|v [-p] NAME X0 X1 Y0 Y1 [NAME X0 X1 Y0 Y1 ...]

A band 8-15 px wide between two polys or two edge lines has, in chip 2's two shots, a greenish flank on one
side and a reddish flank on the other (north green and south red for a horizontal band; for a vertical band
the flank east of a dark line is red and the flank west of one green), so a single row, or a patch on one
flank, classes it as whatever that flank looks like (tracing guide, trap 38). This prints the mean colour over
the band's rows (h: a horizontal band, means taken along x) or columns (v: a vertical band, means taken along
y), in the chip-2 metal shot and the chip-2 stripped shot, and red minus green of it. The band is taken to be
the run of rows (columns) that are not dark (red >= 120 in that shot) nearest the middle of the rectangle, so
the edge lines drop out and so does a bright poly beyond them: give a rectangle centred on the band that
contains both its edge lines, and check the printed extent.

Always give a CONTROL in the same call: a band of the same width that is certainly field, between the same
kind of edges nearby. In the unit at x 8222-8558, y 17263-17634 (notes/blocks/eof.md, piece g174e) seven
diffusion bands read +31..+40 (metal) and +17..+26 (stripped), the field control +14.0 and -3.4, and a
field pocket between two poly ends +3.8 and -7.7.

-p also prints every row or column (metal, stripped, clean).
"""
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import view


def main():
    a = sys.argv[1:]
    if len(a) < 6 or a[0] not in ('h', 'v'):
        sys.exit(__doc__)
    axis = 1 if a[0] == 'h' else 0
    a = a[1:]
    verbose = False
    if a[0] == '-p':
        verbose, a = True, a[1:]
    for i in range(0, len(a) - 4, 5):
        name = a[i]
        x0, x1, y0, y1 = [int(t) for t in a[i + 1:i + 5]]
        out = {}
        for lay in ('metal', 'acid', 'acid1b'):
            rgb = np.asarray(view.raw(lay, x0, y0, x1 - x0, y1 - y0), dtype=float)[..., :3]
            out[lay] = rgb.mean(axis)
        print("== %s  x %d-%d  y %d-%d  (%s)" % (name, x0, x1, y0, y1, 'rows' if axis == 1 else 'columns'))
        if verbose:
            first = y0 if axis == 1 else x0
            for k in range(len(out['metal'])):
                m, c, b = out['metal'][k], out['acid'][k], out['acid1b'][k]
                print("  %5d  metal %3.0f/%3.0f/%3.0f %+4.0f   stripped %3.0f/%3.0f/%3.0f %+4.0f   clean %3.0f/%3.0f/%3.0f" % (
                    first + k, m[0], m[1], m[2], m[0] - m[1], c[0], c[1], c[2], c[0] - c[1], b[0], b[1], b[2]))
        for lay, label in (('metal', 'metal'), ('acid', 'stripped')):
            r = out[lay]
            bright = r[:, 0] >= 120
            # the band is the run of not-dark rows (columns) nearest the middle of the rectangle: a poly
            # or a wide area beyond an edge line is bright too and must not be counted
            runs, k = [], 0
            while k < len(r):
                if bright[k]:
                    j = k
                    while j + 1 < len(r) and bright[j + 1]:
                        j += 1
                    runs.append((k, j))
                    k = j + 1
                else:
                    k += 1
            if not runs:
                print("  %-8s all dark" % label)
                continue
            mid = (len(r) - 1) / 2.0
            k, j = min(runs, key=lambda t: 0 if t[0] <= mid <= t[1] else min(abs(t[0] - mid), abs(t[1] - mid)))
            first = (y0 if axis == 1 else x0)
            sel = slice(k, j + 1)
            print("  %-8s band %d-%d (%2d px), mean %3.0f/%3.0f/%3.0f  R-G %+5.1f" % (
                label, first + k, first + j, j - k + 1, *r[sel].mean(0), (r[sel, 0] - r[sel, 1]).mean()))


if __name__ == '__main__':
    main()
