"""Dark edge lines along a column or a row of the chip-2 stripped shot, as text.

usage: tl4_edges.py col X Y0 Y1 [X ...]      down the column(s) X
       tl4_edges.py row Y X0 X1 [Y ...]      along the row(s) Y

Samples `acid` (5 px across the line of travel, averaged) and prints the centres of the runs
where red is under 115: the outlines of poly and of pads. A poly row lies between two such
lines about 20 px apart (orange between them, red - blue over 70, printed as 'P' after the
gap; khaki field is printed as 'f'). An aid for measuring row and pad edges in a crossing
field; every edge is still checked on an overlay.
"""
import os, sys
import numpy as np
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A = np.load(os.path.join(ROOT, 'cache', 'acid_aligned.npy'), mmap_mode='r')

def main():
    a = sys.argv[1:]
    kind, a0, a1 = a[0], int(a[2]), int(a[3])
    for c in [int(a[1])] + [int(v) for v in a[4:]]:
        if kind == 'col':
            s = np.asarray(A[a0:a1, c - 2:c + 3, :3]).astype(float).mean(axis=1)
        else:
            s = np.asarray(A[c - 2:c + 3, a0:a1, :3]).astype(float).mean(axis=0)
        dark = s[:, 0] < 115
        out = []; i = 0; n = len(dark); prev = 0
        while i < n:
            if dark[i]:
                j = i
                while j < n and dark[j]: j += 1
                if i > prev:
                    seg = s[prev:i]
                    out.append('P' if (seg[:, 0] - seg[:, 2]).mean() > 70 else 'f')
                out.append('%d' % (a0 + (i + j - 1) // 2))
                prev = j; i = j
            else:
                i += 1
        if prev < n:
            seg = s[prev:n]
            out.append('P' if (seg[:, 0] - seg[:, 2]).mean() > 70 else 'f')
        print('%s %d: %s' % (kind, c, ' '.join(out)))

main()
