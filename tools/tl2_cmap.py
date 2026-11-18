#!/usr/bin/env python3
"""A rectangle of the clean shot as a text class map: tl2_cmap.py X0 Y0 X1 Y1 [STEP]

One character per sample (STEP px, default 3), the class of tools/classmap.py at that pixel:
  D diffusion under metal (tan)     C poly over a channel under metal (bright salmon)
  P poly over field under metal     . field under metal (pink)
  # dark (an edge line, a pit)      d / , / p  open diffusion / field / poly (unreliable)
  ? none of these
Right where metal was above (within about 10 px of a metal's edge), wrong in the open
(tracing guide, trap 18): there decide in the chip-2 shots. A reading aid, like
tools/railprof.py but in two dimensions; check every gate on a view.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import view
import classmap


def main():
    a = sys.argv[1:]
    if len(a) < 4:
        sys.exit(__doc__)
    x0, y0, x1, y1 = map(int, a[:4])
    st = int(a[4]) if len(a) > 4 else 3
    rgb = view.raw('acid1b', x0, y0, x1 - x0, y1 - y0)
    cls = classmap.classify(rgb[..., :3])
    xs = list(range(0, x1 - x0, st))
    # column ruler: a mark every 30 px
    print('x %d..%d step %d' % (x0, x0 + xs[-1], st))
    print('      ' + ''.join('|' if (x0 + x) % 30 < st else ' ' for x in xs)
          + '   | at x = multiples of 30')
    for y in range(0, y1 - y0, st):
        print('%5d %s' % (y0 + y, ''.join(cls[y, x] for x in xs)))


if __name__ == '__main__':
    main()
