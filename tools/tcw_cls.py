#!/usr/bin/env python3
"""A rectangle of the chip-2 stripped shot (acid, aligned) as a class map in text, for the
open areas of tcw where nothing is under metal.

usage: tcw_cls.py X0 Y0 X1 Y1 [STEP]     (STEP default 4; each sample a 3x3 mean)

Characters (thresholds measured at known spots of tcw's last inverter, y 4200-4400:
diffusion arm (6580,4295) 165/141/105, field (6600,4350) 156/153/102, poly (6650,4295)
191/157/76):
  P  poly: blue under 84 and red over 125
  d  diffusion: red - green 16 or more, blue 88 or more
  .  field: red - green under 10
  #  dark (an edge): red under 118
  ?  none of these
Only for OPEN areas: under a rail the stripped shot shows fringes (use tools/railprof.py).
"""
import os, sys
import numpy as np
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def main():
    a = sys.argv[1:]
    if len(a) < 4:
        sys.exit(__doc__)
    x0, y0, x1, y1 = map(int, a[:4]); st = int(a[4]) if len(a) > 4 else 4
    A = np.load(os.path.join(ROOT, 'cache', 'acid_aligned.npy'), mmap_mode='r')
    print('x %d..%d step %d' % (x0, x1, st))
    for y in range(y0, y1, st):
        row = ''
        for x in range(x0, x1, st):
            r, g, b = A[y-1:y+2, x-1:x+2, :3].reshape(-1, 3).mean(0)
            if r < 118: c = '#'
            elif b < 84 and r > 125: c = 'P'
            elif r - g >= 16 and b >= 88: c = 'd'
            elif r - g < 10: c = '.'
            else: c = '?'
            row += c
        print('%5d %s' % (y, row))
main()
