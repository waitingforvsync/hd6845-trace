#!/usr/bin/env python3
"""Is there a contact pad at X,Y? The four-sided ring test, as text (run from the repository's root).

usage: bd1_ring4.py X,Y [X,Y ...]            test the given points
       bd1_ring4.py --audit FILE [--max 400]  test every "NO CONTACT DRAWN" spot of a tools/bd1_audit.py output
       bd1_ring4.py --file NAME               walk every thin metal that trace/NAME.txt draws (a 4 px grid inside
                                              each item) and list the pad-like places with no drawn contact

A contact on a thin metal shows in both metal shots as a bright centre inside a dark ring that closes on all
four sides and is wider than the track: 13-16 px from the centre every side is still ring or pad outline. On a
plain track that distance is bare ground to the east and west and metal to the north and south; where a poly
row crosses under a track its edge lines lie about 10 px from the row's centre, and at 13-16 px the metal is
bright again. For each point the centre is searched within +-8 px (the brightest 5 x 5 patch of red); on each
of the four sides the darkest 3 x 3 mean of red at 13-16 px from the centre is taken. Printed per chip: the
centre's red and the four sides N E S W. PAD if all four sides are under 125 in both chips and the centre is
150 or more in at least one.
Controls on 2026-11-27: the pads (13628,16626), (16384,17169), (13716,16495), (13629,16235), (13262,16456) test
PAD; the plain crossings (13630,15999), (13478,16594), (13564,16421), (13693,15185), (13716,16628) do not.
An aid, not a proof: every PAD is looked at; a pad beside a wide metal or under a blemish can be missed.
LIMITS found the same day (re-read item R4, trunks): the geometry holds only for metals about 12-14 px wide over
rows 30 px or more apart. On a track 18-20 px wide its own edge lines lie 10-16 px from the centre, and a 20 px
poly row under it puts its edges there too: every such crossing tests PAD (--file trunks: 179 places, of which
the 21 looked at were all plain crossings). A diagonal track or a diagonal poly under a track tests PAD as well.
So --file is a way to list places to look at on a thin line, not a count of contacts; the reliable signature
of a contact stays the clean shot's hole (tools/bd1_audit.py, list 3), where the clean shot has no
interference colours.
"""
import sys, re, numpy as np
from scipy import ndimage as ndi
M = [np.load('cache/metal.npy', mmap_mode='r'), np.load('cache/metal1.npy', mmap_mode='r')]
def test(x, y):
    res = []; ok = True
    for a in M:
        r = np.asarray(a[y - 30:y + 31, x - 30:x + 31, 0], float)
        c = ndi.uniform_filter(r, 5)
        sub = c[30 - 8:30 + 9, 30 - 8:30 + 9]
        j, i = np.unravel_index(sub.argmax(), sub.shape); cy, cx = 22 + j, 22 + i
        sides = []
        for dy, dx in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            vals = []
            for d in range(13, 17):
                yy, xx = cy + dy * d, cx + dx * d
                vals.append(r[yy - 1:yy + 2, xx - 1:xx + 2].mean() if dx == 0 else r[yy - 1:yy + 2, xx - 1:xx + 2].mean())
            sides.append(min(vals))
        res.append((c[cy, cx], sides, (x - 30 + cx, y - 30 + cy)))
        ok &= max(sides) < 125
    ok &= max(c for c, _, _ in res) >= 150
    return ok, res
pts = []
if '--file' in sys.argv:
    # every thin metal that trace/NAME.txt draws, sampled every 4 px; PADs clustered; drawn contacts subtracted
    import os
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import tracelib
    from PIL import Image, ImageDraw
    name = sys.argv[sys.argv.index('--file') + 1]
    tr = tracelib.Trace()
    cons = np.array([(it.geom.centroid.x, it.geom.centroid.y) for it in tr.items if it.layer == 'C'])
    found = []
    for it in tr.items:
        if it.layer != 'M' or ('/%s.txt' % name) not in it.src: continue
        b = [int(v) for v in it.geom.bounds]
        b = [b[0] - 3, b[1] - 3, b[2] + 3, b[3] + 3]    # a margin, so that the distance transform sees the item's edges
        im = Image.new('L', (b[2] - b[0] + 1, b[3] - b[1] + 1), 0)
        g = it.geom
        for poly in (g.geoms if hasattr(g, 'geoms') else [g]):
            ImageDraw.Draw(im).polygon([(x - b[0], y - b[1]) for x, y in poly.exterior.coords], fill=1)
        m = np.array(im, bool)
        dt = ndi.distance_transform_edt(m)
        if dt.max() > 14: continue                      # a wide metal: not this test's business
        grid = np.zeros_like(m); grid[::4, ::4] = True
        ys, xs = np.nonzero(m & (dt >= 4) & grid)       # a 4 px grid, 4 px in from the item's edges
        for y, x in zip(ys, xs):
            X, Y = x + b[0], y + b[1]
            if not (40 < X < 19790 and 40 < Y < 20980): continue
            ok, res = test(X, Y)
            if ok: found.append((res[1][2][0], res[1][2][1], it.src.split('/')[-1].split(' ')[0]))
    # cluster
    cl = []
    for x, y, src in found:
        for c in cl:
            if abs(c[0] - x) <= 12 and abs(c[1] - y) <= 12: c[3] += 1; break
        else: cl.append([x, y, src, 1])
    und = [c for c in cl if not len(cons) or np.hypot(cons[:, 0] - c[0], cons[:, 1] - c[1]).min() > 16]
    print('%d pad-like places on %s\'s thin metals; %d of them more than 16 px from every drawn contact:' % (len(cl), name, len(und)))
    for x, y, src, n in sorted(und, key=lambda c: (c[2], c[1], c[0])):
        print('   %d,%d  on %s  (%d samples)' % (x, y, src, n))
    sys.exit(0)
if '--audit' in sys.argv:
    f = sys.argv[sys.argv.index('--audit') + 1]
    mx = int(sys.argv[sys.argv.index('--max') + 1]) if '--max' in sys.argv else 400
    for line in open(f):
        m = re.match(r'\s+(\d+),(\d+)\s+(\d+) px2\s+\*\*NO CONTACT', line)
        if m and int(m.group(3)) <= mx: pts.append((int(m.group(1)), int(m.group(2))))
else:
    pts = [tuple(map(int, a.split(','))) for a in sys.argv[1:] if ',' in a]
n = 0
for x, y in pts:
    ok, res = test(x, y)
    if ok: n += 1
    if ok or '--audit' not in sys.argv:
        print('%d,%d  %s  ' % (x, y, 'PAD' if ok else '-  ') + ' | '.join('centre %d at %d,%d  N %d E %d S %d W %d' % (c, p[0], p[1], *s) for c, s, p in res))
print('%d points, %d PAD' % (len(pts), n))
