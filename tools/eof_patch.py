#!/usr/bin/env python3
"""Mean colour of rectangles in three shots, as text: eof_patch.py X0 X1 Y0 Y1 [Y0 Y1 ...]

For each rectangle x X0..X1, y Y0..Y1 prints the mean R,G,B in the chip-2 stripped shot (acid), the
chip-2 metal shot and the clean shot (acid1b), and red minus green in the first two. For telling a
small open diffusion from field in a gap between two metals (tracing guide, traps 21 and 28): compare
with a known diffusion and a known field patch of the same column in the same call.
"""
import os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import view


def main():
    a = [int(t) for t in sys.argv[1:]]
    x0, x1 = a[0], a[1]
    print("x %d-%d            acid R-G  metal R-G   acid R,G,B     metal R,G,B    clean R,G,B" % (x0, x1))
    for i in range(2, len(a) - 1, 2):
        y0, y1 = a[i], a[i + 1]
        m = {}
        for lay in ('acid', 'metal', 'acid1b'):
            rgb = np.asarray(view.raw(lay, x0, y0, x1 - x0, y1 - y0), dtype=float)[..., :3]
            m[lay] = rgb.reshape(-1, 3).mean(0)
        f = lambda v: "%3.0f,%3.0f,%3.0f" % tuple(v)
        print("y %5d-%5d     %6.1f    %6.1f     %s    %s    %s" % (
            y0, y1, m['acid'][0] - m['acid'][1], m['metal'][0] - m['metal'][1],
            f(m['acid']), f(m['metal']), f(m['acid1b'])))


if __name__ == '__main__':
    main()
