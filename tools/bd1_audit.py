#!/usr/bin/env python3
"""Audit the drawn metal of a wiring region against the photos, as text (re-read item R1's method).

usage: bd1_audit.py X0 Y0 X1 Y1 [--gap 14] [--hole 24] [--only NAME]   (run from the repository's root; set TRACE as
                                                             usual, or leave it unset to load every trace file)
       bd1_audit.py --tiles NAME [--size 1500]    every tile of the die that trace/NAME.txt draws in, with --only NAME

--only NAME tests only the metals, polys and contacts that trace/NAME.txt draws (lists 1, 3, 4); the other files
still count as drawn for list 2, which is then limited to metal within 40 px of one of NAME's metals.

Four lists, each to be LOOKED AT on a view: the tool only says where to look.

1. BREAK: places where a drawn thin metal (26 px wide or less) has no metal in either metal shot along --gap px
   or more of its length. A dark bar across a metal (an edge underneath, a contact's ring) is up to about 12 px,
   so shorter stretches are not listed. Metal test as tools/follow.py: red >= 177 and green >= 128, here in at
   least one of the two chips, anywhere across the drawn width.
2. UNDRAWN METAL: connected pieces of metal seen in BOTH metal shots, 200 px2 or more, that lie more than 6 px
   from every drawn metal of the loaded trace files (so also the undrawn continuation of a drawn line).
3. HOLES: spots under drawn metal where the clean shot has the colour of a contact hole (red minus green under
   --hole, red >= 110: the olive of a hole, not the dark of an outline), 30 px2 or more, with the nearest drawn
   contact; "NO CONTACT DRAWN" when none lies within 14 px. And every drawn contact in the region with no such
   hole within 14 px ("no hole").
4. POLY GAP: spots inside a drawn thin poly (26 px wide or less, 4 px in from its edges) that have the colour of
   field: a poly drawn through a gap (tracing guide: "a knot hides a break").
Limits: under a wide rail the clean shot's diffusion is tan (red minus green about 20), so rails are skipped for
list 3 (metals wider than 26 px); a contact on open diffusion beside a metal is not found; the colours drift
across the die (tracing guide, trap 1).
"""
import sys, os
import numpy as np
from scipy import ndimage as ndi
from PIL import Image, ImageDraw
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tracelib

def opt(name, d):
    return float(sys.argv[sys.argv.index(name) + 1]) if name in sys.argv else d
def sopt(name):
    return sys.argv[sys.argv.index(name) + 1] if name in sys.argv else None
ONLY = sopt('--only')
if '--tiles' in sys.argv:
    import subprocess
    name = sopt('--tiles'); size = int(opt('--size', 1500))
    t = tracelib.Trace(); seen = set()
    for it in t.items:
        if ('/%s.txt' % name) in it.src and it.layer in 'MPC':
            b = it.geom.bounds
            for tx in range(int(b[0]) // size, int(b[2]) // size + 1):
                for ty in range(int(b[1]) // size, int(b[3]) // size + 1):
                    seen.add((tx, ty))
    for tx, ty in sorted(seen):
        sys.stdout.flush()
        subprocess.run([sys.executable, __file__, str(tx * size), str(ty * size), str((tx + 1) * size), str((ty + 1) * size), '--only', name, '--brief'])
    sys.exit(0)
BRIEF = '--brief' in sys.argv
a = [v for v in sys.argv[1:] if not v.startswith('--') and v.lstrip('-').isdigit()]
x0, y0, x1, y1 = map(int, a[:4])
GAP = int(opt('--gap', 14)); HOLE = opt('--hole', 24)
W, H = x1 - x0, y1 - y0
tr = tracelib.Trace()
def raster(items):
    im = Image.new('L', (W, H), 0); d = ImageDraw.Draw(im)
    for it in items:
        g = it.geom
        for poly in (g.geoms if hasattr(g, 'geoms') else [g]):
            d.polygon([(x - x0, y - y0) for x, y in poly.exterior.coords], fill=1)
    return np.array(im, bool)
hits = tr.query(x0, y0, x1, y1)
mine = (lambda it: ('/%s.txt' % ONLY) in it.src) if ONLY else (lambda it: True)
metal_items = [it for it in hits if it.layer == 'M']
def minwidth(it):
    r = it.geom.minimum_rotated_rectangle
    c = list(r.exterior.coords)
    e = sorted(np.hypot(c[i+1][0]-c[i][0], c[i+1][1]-c[i][1]) for i in range(2))
    return e[0]
drawn = raster(metal_items)
# a drawn metal is "thin" where its local width is 26 px or less: distance transform of the mask
dt = ndi.distance_transform_edt(drawn)
core = ndi.maximum_filter(dt, 31)
thin = drawn & (core <= 13.5)
if ONLY:
    own = raster([it for it in metal_items if mine(it)])
    thin &= own
m2 = np.asarray(np.load('cache/metal.npy', mmap_mode='r')[y0:y1, x0:x1, :3], float)
m1 = np.asarray(np.load('cache/metal1.npy', mmap_mode='r')[y0:y1, x0:x1, :3], float)
ac = np.asarray(np.load('cache/acid1b.npy', mmap_mode='r')[y0:y1, x0:x1, :3], float)
def met(m):
    return (m[..., 0] >= 177) & (m[..., 1] >= 128)
s2, s1 = met(m2), met(m1)
seen_any = ndi.binary_dilation(s2 | s1, iterations=2)
seen_both = s2 & s1

print('region %d,%d - %d,%d: %d drawn metal items of %d files' % (x0, y0, x1, y1, len(metal_items), len(tr.files)))
# 1. breaks
bare = thin & ~seen_any
# remove bare pixels that have seen metal across the drawn width: label thin metal's cross-sections by erosion-free
# rule: a bare spot counts only if no seen metal lies within 9 px in the direction ACROSS the track; approximated by
# opening the bare mask along both axes.
lab, n = ndi.label(ndi.binary_opening(bare, structure=np.ones((3, 3))))
out = []
for i, sl in enumerate(ndi.find_objects(lab), 1):
    h = sl[0].stop - sl[0].start; w = sl[1].stop - sl[1].start
    blob = lab[sl] == i
    if max(h, w) < GAP or min(h, w) < 10: continue      # a sliver along an edge is the drawn width, not a break
    # the blob must span most of the track's width somewhere along GAP px
    cy = (sl[0].start + sl[0].stop) // 2; cx = (sl[1].start + sl[1].stop) // 2
    # fraction of the drawn thin metal in the bounding box that is bare
    frac = blob.sum() / max(1, thin[sl].sum())
    if frac < 0.75: continue
    near = any(it.layer == 'C' and abs(it.geom.centroid.x - cx - x0) <= 25 and abs(it.geom.centroid.y - cy - y0) <= 25 for it in hits)
    out.append((cx + x0, cy + y0, w, h, frac, '  (a drawn contact is within 25 px: its ring)' if near else '  **LOOK**'))
print('\n1. BREAK candidates (drawn thin metal with no metal in either shot): %d' % len(out))
for cx, cy, w, h, f, note in sorted(out, key=lambda t: (t[0] // 30, t[1])):
    print('   %d,%d  %dx%d px  bare %.0f%%%s' % (cx, cy, w, h, 100 * f, note))
# 2. undrawn metal
und = seen_both & ~ndi.binary_dilation(drawn, iterations=6)
if ONLY:
    und &= ndi.binary_dilation(own, iterations=40)
lab, n = ndi.label(ndi.binary_opening(und, structure=np.ones((3, 3))))
out = []
for i, sl in enumerate(ndi.find_objects(lab), 1):
    area = (lab[sl] == i).sum()
    if area < 200: continue
    out.append((sl[1].start + x0, sl[0].start + y0, sl[1].stop + x0, sl[0].stop + y0, area))
print('\n2. UNDRAWN METAL (seen in both shots, more than 6 px from any drawn metal): %d' % len(out))
for t in sorted(out, key=lambda t: (t[1] // 40, t[0])):
    print('   %d,%d - %d,%d  %d px2' % t)
# 3. holes
hole = (ac[..., 0] - ac[..., 1] < HOLE) & (ac[..., 0] >= 110) & ndi.binary_erosion(thin, iterations=2)
lab, n = ndi.label(ndi.binary_opening(hole, structure=np.ones((2, 2))))
cons = [(it.geom.centroid.x, it.geom.centroid.y, it) for it in hits if it.layer == 'C']
allcons = cons
found = []
print('\n3. HOLES in the clean shot under drawn thin metal:')
for i, sl in enumerate(ndi.find_objects(lab), 1):
    area = (lab[sl] == i).sum()
    if area < 30: continue
    cy = (sl[0].start + sl[0].stop) / 2 + y0; cx = (sl[1].start + sl[1].stop) / 2 + x0
    best = min(cons, key=lambda c: np.hypot(c[0] - cx, c[1] - cy)) if cons else None
    d = np.hypot(best[0] - cx, best[1] - cy) if best else 1e9
    found.append((cx, cy))
    print('   %d,%d  %d px2  %s' % (cx, cy, area, ('contact %s at %d,%d' % (best[2].src.split('/')[-1], best[0], best[1])) if d <= 14 else '**NO CONTACT DRAWN** (nearest %d px)' % d))
print('\n   drawn contacts on thin metal with no hole within 14 px:')
for cx, cy, it in cons:
    if not (x0 <= cx < x1 and y0 <= cy < y1): continue
    if not thin[int(cy) - y0, int(cx) - x0]: continue
    if not any(np.hypot(fx - cx, fy - cy) <= 14 for fx, fy in found):
        r = ac[int(cy) - y0 - 4:int(cy) - y0 + 5, int(cx) - x0 - 4:int(cx) - x0 + 5].reshape(-1, 3).mean(0)
        print('   %d,%d  %s  clean %d/%d/%d' % (cx, cy, it.src.split('/')[-1], r[0], r[1], r[2]))
# 4. poly gaps: field under a drawn thin poly
polys = [it for it in hits if it.layer == 'P' and mine(it)]
pm = raster(polys)
pdt = ndi.distance_transform_edt(pm)
pthin = pm & (ndi.maximum_filter(pdt, 31) <= 13.5)
core_p = ndi.binary_erosion(pthin, iterations=4)
r, g, b = ac[..., 0], ac[..., 1], ac[..., 2]
pink = (r - g > 40) & (g - b < 14) & (r > 150)                 # field under metal
m2r, m2g, m2b = m2[..., 0], m2[..., 1], m2[..., 2]
plain2 = (m2r > 120) & (m2r - m2g < 30) & ~met(m2)             # plain (field or diffusion) in chip 2's metal shot, not metal
fieldish = core_p & (pink | (plain2 & ~seen_any & (g >= r - 12) & (r > 90)))
lab, n = ndi.label(ndi.binary_opening(fieldish, structure=np.ones((3, 3))))
out = []
for i, sl in enumerate(ndi.find_objects(lab), 1):
    h = sl[0].stop - sl[0].start; w = sl[1].stop - sl[1].start
    area = (lab[sl] == i).sum()
    if area < 60 or min(h, w) < 6: continue
    out.append(((sl[1].start + sl[1].stop) // 2 + x0, (sl[0].start + sl[0].stop) // 2 + y0, w, h, area))
print('\n4. POLY GAP candidates (field colour inside a drawn thin poly: pink under metal in the clean shot, or plain in')
print('   chip 2\'s metal shot and not red in the clean shot, in the open): %d' % len(out))
for t in sorted(out, key=lambda t: (t[1] // 40, t[0])):
    print('   %d,%d  %dx%d px  %d px2' % t)
