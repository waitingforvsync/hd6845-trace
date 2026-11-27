#!/usr/bin/env python3
"""Width and layer of a horizontal row line along its length, in all four shots (text).

usage: busl_roww.py YC X0 X1 [--step 6] [--win 24] [--all]

For a row whose centre line is about y = YC, at every --step px from X0 to X1 and in each of the
four shots (chip-2 metal, chip-1 metal, chip-2 stripped as aligned, clean shot), it reads the red
channel down the column (3 px mean along x) from YC - win to YC + win, takes the darkest sample
above the centre (YC - win .. YC - 5) and below it (YC + 5 .. YC + win) as the row's two edge
lines, and calls the row "seen" in that shot when both are darker than the strip between them by
25 or more. The width is the distance between the two edge centres. It also reads, on the centre
line (5 px mean down the column), the chip-2 stripped shot's red minus green (poly 25 and over
under the field's tracks and in the open, field under 10) and the clean shot's.

Prints: the number of samples; the samples where fewer than two shots see a row 16-30 px wide
(a break, or a place the edge lines are hidden: read it on a view); the samples where two or
more shots see a row 32 px wide or more (a pad or a widening: read it on a view); the samples
where the chip-2 stripped shot's red minus green on the centre line is under 12 (field colour);
and the range of the centre (mean of the two edges) in the shots that see the row. With --all,
one line per sample as well: x, then width/centre per shot ('-' when not seen), then the two
red-minus-green values.

An aid for a row drawn straight under a field of tracks: it says where to look, and every place
it lists is still read on a view. A neighbouring row's pad ring within the window reads as a
wide row here.
"""
import sys
import os
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SHOTS = [('m2', 'metal.npy'), ('m1', 'metal1.npy'), ('a2', 'acid_aligned.npy'), ('cl', 'acid1b.npy')]


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    opts = sys.argv[1:]
    if len(args) < 3:
        print(__doc__)
        return 2
    yc, x0, x1 = int(args[0]), int(args[1]), int(args[2])
    step = 6
    win = 24
    show = '--all' in opts
    for i, a in enumerate(opts):
        if a == '--step':
            step = int(opts[i + 1])
        if a == '--win':
            win = int(opts[i + 1])
    # option values are also in args: drop them
    arrs = [(n, np.load(os.path.join(ROOT, 'cache', f), mmap_mode='r')) for n, f in SHOTS]
    low, wide, fieldc = [], [], []
    centres = []
    n = 0
    for x in range(x0, x1 + 1, step):
        n += 1
        res = []
        for name, a in arrs:
            col = np.asarray(a[yc - win:yc + win + 1, x - 1:x + 2, 0], dtype=float).mean(axis=1)
            up = col[:win - 4]
            dn = col[win + 5:]
            iu = int(np.argmin(up))
            idn = int(np.argmin(dn)) + win + 5
            mid = col[iu + 4:idn - 3].mean() if idn - iu > 8 else col[win]
            ok = (mid - col[iu] >= 25) and (mid - col[idn] >= 25)
            w = idn - iu
            c = yc - win + (iu + idn) / 2.0
            res.append((ok, w, c))
        a2 = arrs[2][1]
        cl = arrs[3][1]
        pa = np.asarray(a2[yc - 2:yc + 3, x - 1:x + 2, :3], dtype=float).mean(axis=(0, 1))
        pc = np.asarray(cl[yc - 2:yc + 3, x - 1:x + 2, :3], dtype=float).mean(axis=(0, 1))
        rg_a = pa[0] - pa[1]
        rg_c = pc[0] - pc[1]
        good = [r for r in res if r[0] and 16 <= r[1] <= 30]
        big = [r for r in res if r[0] and r[1] >= 32]
        if len(good) < 2:
            low.append(x)
        if len(big) >= 2:
            wide.append(x)
        if rg_a < 12:
            fieldc.append((x, int(round(rg_a))))
        for r in good:
            centres.append(r[2])
        if show:
            cells = ' '.join(('%2d/%7.1f' % (r[1], r[2])) if r[0] else '    -     ' for r in res)
            print('%5d  %s   a2 r-g %4d  clean r-g %4d' % (x, cells, rg_a, rg_c))

    def runs(xs):
        out = []
        for x in xs:
            if out and x - out[-1][1] <= step:
                out[-1][1] = x
            else:
                out.append([x, x])
        return ' '.join('%d' % a if a == b else '%d-%d' % (a, b) for a, b in out) or 'none'

    print('row y %d, x %d..%d step %d: %d samples' % (yc, x0, x1, step, n))
    print('fewer than two shots see a row 16-30 px wide: %s' % runs(low))
    print('two or more shots see a row 32 px or wider:   %s' % runs(wide))
    print('chip-2 stripped red minus green under 12 on the centre line: %s'
          % (' '.join('%d(%d)' % t for t in fieldc) or 'none'))
    if centres:
        print('centre (shots that see the row): %.1f .. %.1f, median %.1f'
              % (min(centres), max(centres), float(np.median(centres))))
    return 0


if __name__ == '__main__':
    sys.exit(main())
