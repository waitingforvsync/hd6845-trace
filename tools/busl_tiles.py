#!/usr/bin/env python3
"""Several small places in one image: each as a row of layers, rows stacked.

usage: busl_tiles.py OUT W H SCALE LAYERS X,Y [X,Y ...] [--trace]

Each X,Y is the centre of a W x H rectangle (die px), rendered with tools/view.py in each of
LAYERS (comma separated) at SCALE with a 50 px grid; one row per place. With --trace the
package's trace (TRACE in the environment) is outlined. Keep the result under 1400 px a side.
"""
import os, subprocess, sys
from PIL import Image
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
a = sys.argv[1:]
tr = '--trace' in a
if tr: a.remove('--trace')
out, w, h, sc, layers = a[0], int(a[1]), int(a[2]), float(a[3]), a[4].split(',')
rows = []
for k, p in enumerate(a[5:]):
    x, y = map(int, p.split(','))
    ims = []
    for l in layers:
        f = os.path.join(ROOT, 'cache', 'scratch', 'busl', '_tile_%d_%s.png' % (k, l))
        cmd = [os.path.join(ROOT, '.venv/bin/python'), os.path.join(ROOT, 'tools/view.py'), str(x - w // 2), str(y - h // 2),
               str(w), str(h), '--scale', str(sc), '--grid', '50', '--layers', l, '--out', f]
        if tr: cmd += ['--trace', '--nofill']
        subprocess.run(cmd, check=True, capture_output=True)
        ims.append(Image.open(f).convert('RGB'))
    rows.append(ims)
W = sum(i.width for i in rows[0]) + 4 * (len(layers) - 1); H = sum(r[0].height for r in rows) + 4 * (len(rows) - 1)
im = Image.new('RGB', (W, H), (255, 0, 255)); y = 0
for r in rows:
    x = 0
    for i in r:
        im.paste(i, (x, y)); x += i.width + 4
    y += r[0].height + 4
im.save(out); print(out, im.size)
for k in range(len(rows)):
    for l in layers:
        os.remove(os.path.join(ROOT, 'cache', 'scratch', 'busl', '_tile_%d_%s.png' % (k, l)))
