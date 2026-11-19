"""Build tutorial/data/ for the tutorial page: photo crops and the worked example's geometry.

Run from the repository root with the project's Python (shapely, opencv):
    TRACE=examples/pilot ../hd6845-trace/.venv/bin/python tutorial/export.py
Reads the aligned die photos from cache/ (or HD_CACHE) and trace/examples/pilot.txt, writes
  data/die_<shot>.jpg      the whole die at 1/8
  data/L4_<shot>_<col>_<row>.jpg, L2_...  the whole die in tiles at 1/4 (8192 px) and 1/2 (4096 px)
  data/ex_<shot>.jpg       the example's rectangle at the photo's own resolution
  data/example.json        polygons by layer, channels, nets, transistors, recovered gates
Nothing here edits the repository's trace or tools.
"""
import json
import os
import sys

import cv2
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, 'tools'))
os.environ.setdefault('TRACE', 'examples/pilot')
import netlist  # noqa: E402

CACHE = os.environ.get('HD_CACHE') or os.path.join(ROOT, 'cache')
if not os.path.exists(os.path.join(CACHE, 'metal.npy')):
    CACHE = os.path.join(os.path.dirname(ROOT), 'hd6845-trace', 'cache')
OUT = os.path.join(HERE, 'data')
SHOTS = {'metal': 'metal.npy', 'metal1': 'metal1.npy', 'acid': 'acid_aligned.npy', 'acid1b': 'acid1b.npy'}
EX = (14260, 14860, 390, 440)          # x y w h: the example, with a margin
W, H = 19838, 21025


def save(path, rgb, q=88):
    cv2.imwrite(path, cv2.cvtColor(rgb, cv2.COLOR_RGB2BGR), [cv2.IMWRITE_JPEG_QUALITY, q])


def photos():
    for shot, f in SHOTS.items():
        a = np.load(os.path.join(CACHE, f), mmap_mode='r')
        x, y, w, h = EX
        save(os.path.join(OUT, 'ex_%s.jpg' % shot), np.array(a[y:y + h, x:x + w]), 92)
        if shot in ('metal', 'acid1b'):
            small = cv2.resize(np.array(a[::2, ::2]), (2480, 2630), interpolation=cv2.INTER_AREA)
            save(os.path.join(OUT, 'die_%s.jpg' % shot), small, 78)
            for step, size in ((4, 8192), (2, 4096)):       # lazy levels: 1/4 and 1/2 of the photo's size
                for r, y in enumerate(range(0, H, size)):
                    for c, x in enumerate(range(0, W, size)):
                        sub = np.array(a[y:y + size:step, x:x + size:step]) if step == 1 else cv2.resize(
                            np.array(a[y:y + size, x:x + size]), None, fx=1 / step, fy=1 / step, interpolation=cv2.INTER_AREA)
                        save(os.path.join(OUT, 'L%d_%s_%d_%d.jpg' % (step, shot, c, r)), sub, 74)
        print('photos', shot, flush=True)


def ring(poly):
    return [[round(x - EX[0], 1), round(y - EX[1], 1)] for x, y in list(poly.exterior.coords)[:-1]]


def geometry():
    nl = netlist.Netlist()
    tr = nl.trace
    by_layer = {}
    for layer, polys, key in (('M', nl.metal, 'M'), ('P', nl.poly, 'P'), ('D', nl.diff, 'D')):
        by_layer[layer] = [dict(pts=ring(p), net=nl._node_of(key, i)) for i, p in enumerate(polys)]
    gates, passes = nl.recover_logic()      # sets each transistor's kind (load or not)
    chans = []
    for t in nl.transistors:
        chans.append(dict(id=t.id, pts=ring(t.geom), gate=t.gate, a=t.c1, b=t.c2, kind=t.kind,
                          w=round(t.w), l=round(t.l), at=[round(t.x - EX[0]), round(t.y - EX[1])]))
    def lands_on(g):
        pa = sum(p.intersection(g).area for p in nl.poly)
        da = sum(p.intersection(g).area for p in nl.diff)
        return 'P' if pa >= da else 'D'
    contacts = [dict(pts=ring(it.geom), to=lands_on(it.geom)) for it in tr.items if it.layer == 'C']
    buried = [ring(it.geom) for it in tr.items if it.layer == 'B']
    holes = sum(len(p.interiors) for p in nl.metal + nl.poly + nl.diff)
    assert holes == 0, 'polygons with holes are not exported'
    nets = {n.id: dict(name=n.name, names=n.names, layers=n.layers) for n in nl.nodes.values()}
    logic = [dict(out=g[0], expr=g[1], tr=g[2]) for g in gates]
    return dict(origin=[EX[0], EX[1]], size=[EX[2], EX[3]], layers=by_layer, channels=chans,
                contacts=contacts, buried=buried, nets=nets, logic=logic,
                labels=[dict(layer=l.layer, x=round(l.x - EX[0]), y=round(l.y - EX[1]), name=l.name) for l in tr.labels])


if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    if '--geometry-only' not in sys.argv:
        photos()
    g = geometry()
    json.dump(g, open(os.path.join(OUT, 'example.json'), 'w'), separators=(',', ':'))
    print('geometry:', {k: len(v) for k, v in g['layers'].items()}, len(g['channels']), 'transistors')
