"""Colour profile along a line in several shots: tools/tl1_prof.py x0 y0 x1 y1 [--half 2] [--step 3] [--layers metal,metal1,acid1b]
Prints mean R,G,B of a (2*half+1)-wide strip across the line at each step. For judging whether a
metal is continuous through a pad (tracing guide, trap 16) or where a poly ends."""
import sys, os
import numpy as np
a = [x for x in sys.argv[1:] if not x.startswith('--')]
def opt(n, d):
    return sys.argv[sys.argv.index(n) + 1] if n in sys.argv else d
x0, y0, x1, y1 = map(int, a[:4])
half = int(opt('--half', 2)); step = int(opt('--step', 3))
layers = opt('--layers', 'metal,metal1,acid1b').split(',')
F = {'metal': 'metal.npy', 'acid': 'acid_aligned.npy', 'acid1b': 'acid1b.npy', 'metal1': 'metal1.npy'}
arr = {l: np.load(os.path.join('cache', F[l]), mmap_mode='r') for l in layers}
n = max(abs(x1 - x0), abs(y1 - y0)) // step
print('   x    y  ' + '  '.join(f'{l:>11}' for l in layers))
for i in range(n + 1):
    x = x0 + (x1 - x0) * i // max(n, 1); y = y0 + (y1 - y0) * i // max(n, 1)
    out = []
    for l in layers:
        if abs(y1 - y0) >= abs(x1 - x0):
            p = arr[l][y - 1:y + 2, x - half:x + half + 1]
        else:
            p = arr[l][y - half:y + half + 1, x - 1:x + 2]
        m = p.reshape(-1, p.shape[-1]).mean(0)
        out.append('%3d %3d %3d' % (m[0], m[1], m[2]))
    print(f'{x:5d} {y:5d}  ' + '  '.join(out))
