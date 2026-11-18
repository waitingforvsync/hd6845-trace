#!/usr/bin/env python3
"""What lies under a wide metal, as one line of text per cut: the clean shot classified with
tools/textmap.py's rule along a row or a column, to find contacts and diffusion under a rail.

usage: tools/t.sh tc2 tc2_band.py row Y0,Y1,... X0 X1 [STEP]     (default STEP 6)
       tools/t.sh tc2 tc2_band.py col X0,X1,... Y0 Y1 [STEP]

One character per sample (3x3 mean of the clean shot, acid1b):
  '.'  field under metal (pink: red over 170, green minus blue under 18)
  'g'  green over red (a contact's hole, open ground, a heavy outline)
  hex  (red - green) / 8: protected diffusion 2-3, protected poly 5-9
A header line gives the position of every tenth sample. Calibrate on a known contact box
under a rail near by before reading (tracing guide, trap 1): here the VSS boxes (6548,5092)
and (8060,6155) read as runs of 2-3 with 'g' pits. It does not see what the metal shots
show: every candidate is then looked at (tracing guide, traps 15 and 22)."""
import os, sys
import numpy as np
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def main():
    if len(sys.argv) < 5: sys.exit(__doc__)
    kind = sys.argv[1]; cuts = [int(v) for v in sys.argv[2].split(',')]
    a, b = int(sys.argv[3]), int(sys.argv[4]); st = int(sys.argv[5]) if len(sys.argv) > 5 else 6
    c = np.load(os.path.join(ROOT, 'cache', 'acid1b.npy'), mmap_mode='r')
    ps = list(range(a, b, st))
    hdr = [' '] * len(ps)
    for i in range(0, len(ps), 10):
        t = str(ps[i])
        for j, ch in enumerate(t):
            if i + j < len(ps): hdr[i + j] = ch
    print('      ' + ''.join(hdr))
    for q in cuts:
        d = ''
        for p in ps:
            x, y = (p, q) if kind == 'row' else (q, p)
            v = np.asarray(c[y - 1:y + 2, x - 1:x + 2, :3]).reshape(-1, 3).mean(0)
            if v[1] > v[0]: d += 'g'
            elif v[0] > 170 and v[1] - v[2] < 18: d += '.'
            else: d += '%X' % min(15, int((v[0] - v[1]) / 8))
        print('%5d %s' % (q, d))
if __name__ == '__main__':
    main()
