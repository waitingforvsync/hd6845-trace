#!/usr/bin/env python3
"""Several small rectangles in two (or more) shots as one image: one column per rectangle,
one row per layer. Each tile is rendered by tools/view.py (so the trace can be outlined).

usage: tl6_tiles.py OUT W H SCALE X,Y [X,Y ...] [--layers metal,acid1b] [--trace] [--grid N]
X,Y is each tile's CENTRE. TRACE is honoured (TRACE= for every block's geometry).
"""
import os, sys, subprocess
from PIL import Image
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
a = sys.argv[1:]
layers = 'metal,acid1b'; trace = False; grid = '50'
if '--layers' in a: i = a.index('--layers'); layers = a[i + 1]; del a[i:i + 2]
if '--grid' in a: i = a.index('--grid'); grid = a[i + 1]; del a[i:i + 2]
if '--trace' in a: a.remove('--trace'); trace = True
out, w, h, sc = a[0], int(a[1]), int(a[2]), a[3]
pts = [tuple(int(v) for v in p.split(',')) for p in a[4:]]
sd = os.path.join(ROOT, os.environ.get('HD_SCRATCH', 'cache/scratch/tl6'))
os.makedirs(sd, exist_ok=True)
tiles = []
for k, (x, y) in enumerate(pts):
    f = os.path.join(sd, '_tile%d.png' % k)
    cmd = [os.path.join(ROOT, '.venv/bin/python'), os.path.join(ROOT, 'tools/view.py'),
           str(x - w // 2), str(y - h // 2), str(w), str(h), '--scale', sc, '--grid', grid,
           '--layers', layers, '--stack', 'v', '--out', f]
    if trace: cmd += ['--trace', '--nofill']
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, cwd=ROOT)
    tiles.append(Image.open(f).convert('RGB'))
W = sum(t.width for t in tiles) + 6 * (len(tiles) - 1); H = max(t.height for t in tiles)
im = Image.new('RGB', (W, H), (255, 0, 255)); x = 0
for t in tiles: im.paste(t, (x, 0)); x += t.width + 6
p = out if '/' in out else os.path.join(sd, out)
im.save(p); print(p, im.size)
for k in range(len(pts)): os.remove(os.path.join(sd, '_tile%d.png' % k))
