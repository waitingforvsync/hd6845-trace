#!/usr/bin/env python3
"""Build everything in out/ from trace/.

  out/hd6845s.svg     the trace as an SVG in metal-shot coordinates, with Inkscape
                      layers and all five die photos linked as background layers
  out/netlist.json    extracted transistor netlist
  out/report.txt      rule-check report and recovered gates; at the end, the net names
                      that notes/signals.md does not cover and the open joins
  out/floorplan.jpg   the die at reduced scale with the functional blocks outlined
  out/floorplan.svg   the same outlines as a stand-alone SVG over the photo
  out/floorplan_legend.txt   every block as a line of text (number, kind, name, box, description)

floorplan.txt (repo root) and floorplan.d/*.txt list the blocks, one per line. The
fragments in floorplan.d are written by whoever traces a block and are drawn on top:
  x0,y0:x1,y1  kind  name | description
kind is one of: pad io array pla logic route test power unknown
A leading '?' on the kind marks the identification as provisional.

Only the coordinator runs the build (HD_COORD=1 tools/build.py): it rewrites the tracked
files in out/. Anyone else can use --check, which prints the summary lines and writes nothing.
"""
import argparse
import json
import os
import sys
from xml.sax.saxutils import escape

import numpy as np
from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tracelib
import netlist as netlist_mod

ROOT = tracelib.ROOT
OUT = os.path.join(ROOT, 'out')
W, H = 19838, 21025     # metal shot

LAYER_NAMES = {'D': 'diffusion', 'P': 'poly', 'M': 'metal', 'C': 'contact', 'B': 'buried', 'A': 'annotation'}
KIND_COL = {
    'pad': (255, 255, 255), 'io': (255, 200, 0), 'array': (0, 220, 255),
    'pla': (255, 0, 255), 'logic': (255, 80, 80), 'route': (150, 150, 150),
    'test': (120, 120, 255), 'power': (255, 140, 0), 'unknown': (255, 255, 0),
}


def read_floorplan():
    import glob
    paths = [os.path.join(ROOT, 'floorplan.txt')] + sorted(glob.glob(os.path.join(ROOT, 'floorplan.d', '*.txt')))
    blocks = []
    for path in paths:
        if os.path.exists(path):
            _read_floorplan_file(path, blocks)
    return blocks


def _read_floorplan_file(path, blocks):
    for n, line in enumerate(open(path), 1):
        line = line.split('#', 1)[0].strip()
        if not line:
            continue
        head, _, desc = line.partition('|')
        tok = head.split()
        try:
            lead = tok[0].startswith('?')       # some fragments put the ? on the coordinates
            a, b = tok[0].lstrip('?').split(':')
            x0, y0 = map(float, a.split(','))
            x1, y1 = map(float, b.split(','))
            kind = tok[1]
        except (ValueError, IndexError):
            print(f'{os.path.basename(path)}:{n}: skipped, not a floor-plan line: {line[:60]}')
            continue
        prov = kind.startswith('?') or lead
        kind = kind.lstrip('?')
        if kind not in KIND_COL:
            print(f'{os.path.basename(path)}:{n}: skipped, unknown kind {kind}')
            continue
        blocks.append(dict(x0=min(x0, x1), y0=min(y0, y1), x1=max(x0, x1), y1=max(y0, y1),
                           kind=kind, prov=prov, name=' '.join(tok[2:]), desc=desc.strip()))
    return blocks


PHOTOS = [   # (layer name, file, size, key in trace/align.json, visible)
    ('photo-clean-chip1', 'hd6845acid2.jpg', (19860, 21053), 'acid1b', False),
    ('photo-stripped-chip1', 'hd6845acid.jpg', (19872, 21056), 'acid1', False),
    ('photo-metal-chip1', 'hd6845metal.jpg', (19885, 21057), 'metal1', False),
    ('photo-stripped-chip2', 'hd6845acid2ndchip.jpg', (19857, 21029), 'acid', False),
]


def photo_matrix(key):
    """SVG matrix placing a raw photo in reference (chip-2 metal) coordinates.

    Uses the affine part of the registration only; tools/align.py also applies a
    smooth correction of up to a pixel or two that an SVG transform cannot express.
    """
    rec = json.load(open(os.path.join(ROOT, 'trace', 'align.json')))
    if key in rec and 'ref_to_src_affine' in rec[key]:
        T = np.array(rec[key]['ref_to_src_affine'])
    else:
        T = np.array(rec.get('acid_old_affine', rec)['metal_to_acid'])
    A = np.linalg.inv(T[:, :2])
    t = -A @ T[:, 2]
    return 'matrix(%.8f %.8f %.8f %.8f %.4f %.4f)' % (A[0, 0], A[1, 0], A[0, 1], A[1, 1], t[0], t[1])


def path_d(g):
    parts = []
    polys = [g] if g.geom_type == 'Polygon' else list(g.geoms)
    for p in polys:
        for ring in [p.exterior] + list(p.interiors):
            c = list(ring.coords)
            parts.append('M' + ' L'.join(f'{x:.1f},{y:.1f}' for x, y in c[:-1]) + 'Z')
    return ' '.join(parts)


def hexcol(c):
    return '#%02x%02x%02x' % c


def svg_layer(name, body, visible=True):
    style = '' if visible else ' style="display:none"'
    return (f'<g inkscape:groupmode="layer" inkscape:label="{name}" id="layer-{name}"{style}>\n'
            + body + '</g>\n')


def floorplan_svg_body(blocks):
    s = []
    for b in sorted(blocks, key=lambda b: -(b['x1'] - b['x0']) * (b['y1'] - b['y0'])):
        col = hexcol(KIND_COL[b['kind']])
        dash = ' stroke-dasharray="60 40"' if b['prov'] else ''
        w, h = b['x1'] - b['x0'], b['y1'] - b['y0']
        name = b['name'] + (' ?' if b['prov'] else '')
        s.append(f'<rect x="{b["x0"]:.0f}" y="{b["y0"]:.0f}" width="{w:.0f}" height="{h:.0f}" '
                 f'fill="{col}" fill-opacity="0.10" stroke="{col}" stroke-width="10"{dash}>'
                 f'<title>{escape(b["name"])}: {escape(b["desc"])}</title></rect>\n')
        # one line, sized so that it fits the block's width and a third of its height
        fs = max(14, min(150, (w - 30) / max(4, len(name)) / 0.58, h * 0.33))
        s.append(f'<text x="{b["x0"] + 16:.0f}" y="{b["y0"] + fs + 8:.0f}" font-family="sans-serif" '
                 f'font-size="{fs:.0f}" fill="#ffffff" stroke="#000000" stroke-width="{max(2, fs / 10):.0f}" '
                 f'paint-order="stroke">{escape(name)}</text>\n')
    return ''.join(s)


def build_svg(tr, nl, blocks):
    head = (f'<?xml version="1.0" encoding="UTF-8"?>\n'
            f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" '
            f'xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape" '
            f'width="{W}" height="{H}" viewBox="0 0 {W} {H}">\n'
            f'<title>HD6845S trace (coordinates are pixels of hd6845metal2ndchip.jpg)</title>\n')
    out = [head]
    for name, fname, (pw, ph), key, vis in PHOTOS:
        out.append(svg_layer(name,
                             f'<image xlink:href="../dieshots/{fname}" x="0" y="0" '
                             f'width="{pw}" height="{ph}" transform="{photo_matrix(key)}"/>\n', vis))
    out.append(svg_layer('photo-metal-chip2',
                         f'<image xlink:href="../dieshots/hd6845metal2ndchip.jpg" x="0" y="0" '
                         f'width="{W}" height="{H}"/>\n'))
    for layer in ('D', 'P', 'M', 'C', 'B'):
        col = hexcol(tracelib.COLOURS[layer])
        body = []
        for it in tr.items:
            if it.layer != layer:
                continue
            extra = ' stroke="#ffff00" stroke-width="3"' if it.uncertain else ''
            body.append(f'<path d="{path_d(it.geom)}"{extra}><title>{escape(it.src)}</title></path>\n')
        op = '0.75' if layer in ('C', 'B') else '0.4'
        out.append(f'<g inkscape:groupmode="layer" inkscape:label="{LAYER_NAMES[layer]}" '
                   f'id="layer-{LAYER_NAMES[layer]}" fill="{col}" fill-opacity="{op}" '
                   f'stroke="{col}" stroke-width="1.5">\n' + ''.join(body) + '</g>\n')
    lab = []
    for lb in tr.labels:
        lab.append(f'<circle cx="{lb.x:.0f}" cy="{lb.y:.0f}" r="3" fill="#fff" stroke="#000"/>'
                   f'<text x="{lb.x + 6:.0f}" y="{lb.y + 5:.0f}" font-family="monospace" font-size="14" '
                   f'fill="#fff" stroke="#000" stroke-width="2.5" paint-order="stroke">'
                   f'{escape(tracelib.canonical(lb.name))}</text>\n')
    out.append(svg_layer('labels', ''.join(lab)))
    tl = []
    for t in nl.transistors:
        tl.append(f'<text x="{t.x:.0f}" y="{t.y:.0f}" font-family="monospace" font-size="10" '
                  f'text-anchor="middle" fill="#ff0" stroke="#000" stroke-width="2" '
                  f'paint-order="stroke">t{t.id}<title>gate {escape(nl.nm(t.gate))}: '
                  f'{escape(nl.nm(t.c1))} - {escape(nl.nm(t.c2))}</title></text>\n')
    out.append(svg_layer('transistors', ''.join(tl)))
    out.append(svg_layer('floorplan', floorplan_svg_body(blocks), False))
    out.append('</svg>\n')
    with open(os.path.join(OUT, 'hd6845s.svg'), 'w') as f:
        f.write(''.join(out))


def _wrap(d, text, f, maxw):
    lines, cur = [], ''
    for w_ in text.split():
        t = (cur + ' ' + w_).strip()
        if d.textlength(t, font=f) <= maxw or not cur:
            cur = t
        else:
            lines.append(cur)
            cur = w_
    lines.append(cur)
    return lines


def layout_labels(blocks, scale, d, font, size_max=22, size_min=9):
    """Decide where every block's label goes on the reduced image.

    A label is drawn inside its own block, clear of every smaller block that lies in it
    and of every label already placed; small blocks choose first. A block whose name does
    not fit at the smallest size gets a number instead and goes into the legend.
    Returns (placed, numbered): placed = list of (block index, x, y, lines, size);
    numbered = list of (number, block index, x, y).
    """
    n = len(blocks)
    R = [(b['x0'] * scale, b['y0'] * scale, b['x1'] * scale, b['y1'] * scale) for b in blocks]
    area = [(r[2] - r[0]) * (r[3] - r[1]) for r in R]
    Wd = int(max(r[2] for r in R)) + 4
    Hd = int(max(r[3] for r in R)) + 4
    taken = np.zeros((Hd, Wd), bool)          # labels placed so far
    order = sorted(range(n), key=lambda k: area[k])
    placed, unplaced = [], []

    def free_spot(occ, tw, th):
        """First window of tw x th in occ (bool) that is all False, scanning rows; or None."""
        hh, ww = occ.shape
        if tw > ww or th > hh:
            return None
        ii = np.zeros((hh + 1, ww + 1), np.int32)
        ii[1:, 1:] = occ.cumsum(0).cumsum(1)
        s = ii[th:, tw:] - ii[:-th, tw:] - ii[th:, :-tw] + ii[:-th, :-tw]
        ys, xs = np.nonzero(s == 0)
        if len(ys) == 0:
            return None
        return int(xs[0]), int(ys[0])

    for k in order:
        b = blocks[k]
        x0, y0, x1, y1 = [int(round(v)) for v in R[k]]
        x0, y0 = max(0, x0 + 2), max(0, y0 + 2)
        x1, y1 = min(Wd, x1 - 2), min(Hd, y1 - 2)
        if x1 - x0 < 8 or y1 - y0 < 8:
            unplaced.append(k)
            continue
        occ = taken[y0:y1, x0:x1].copy()
        for j in range(n):                      # smaller blocks inside this one
            if j != k and area[j] < area[k]:
                a0, b0, a1, b1 = R[j]
                if a0 < x1 and a1 > x0 and b0 < y1 and b1 > y0:
                    occ[max(0, int(b0) - y0 - 1):max(0, int(b1) - y0 + 2),
                        max(0, int(a0) - x0 - 1):max(0, int(a1) - x0 + 2)] = True
        label = b['name'] + (' ?' if b['prov'] else '')
        done = False
        top = size_max if area[k] > 9000 else min(size_max, 15)
        for size in range(top, size_min - 1, -1):
            f = font(size)
            lines = _wrap(d, label, f, x1 - x0 - 4)
            tw = int(max(d.textlength(l, font=f) for l in lines)) + 6
            th = len(lines) * (size + 2) + 4
            spot = free_spot(occ, tw, th)
            if spot is not None:
                px, py = spot[0] + x0, spot[1] + y0
                taken[py:py + th, px:px + tw] = True
                placed.append((k, px + 3, py + 1, lines, size))
                done = True
                break
        if not done:
            unplaced.append(k)
    unplaced.sort(key=lambda k: (round(R[k][1] / 60), R[k][0]))      # reading order
    numbered = []
    f = font(10)
    for num, k in enumerate(unplaced, 1):
        x0, y0, x1, y1 = R[k]
        t = str(num)
        tw, th = int(d.textlength(t, font=f)) + 5, 13
        cands = [(x0 + 2, y0 + 2), (x1 - tw - 1, y0 + 2), (x0 + 2, y1 - th - 1), (x1 - tw - 1, y1 - th - 1),
                 ((x0 + x1 - tw) / 2, (y0 + y1 - th) / 2), (x1 + 2, y0), (x0 - tw - 2, y0), (x0, y0 - th - 1),
                 (x0, y1 + 1)]
        best = None
        for cx, cy in cands:
            cx, cy = int(max(0, min(Wd - tw, cx))), int(max(0, min(Hd - th, cy)))
            if not taken[cy:cy + th, cx:cx + tw].any():
                best = (cx, cy)
                break
        if best is None:
            best = (int(max(0, min(Wd - tw, x0 + 2))), int(max(0, min(Hd - th, y0 + 2))))
        taken[best[1]:best[1] + th, best[0]:best[0] + tw] = True
        numbered.append((num, k, best[0], best[1]))
    return placed, numbered


def build_floorplan(blocks, scale=1 / 6):
    a = np.load(os.path.join(ROOT, 'cache', 'metal.npy'), mmap_mode='r')
    step = round(1 / scale)
    scale = 1 / step
    # box-filter downsample
    hh, ww = (H // step) * step, (W // step) * step
    small = np.zeros((hh // step, ww // step, 3), np.float32)
    for y0 in range(0, hh, step * 256):
        y1 = min(hh, y0 + step * 256)
        blk = np.asarray(a[y0:y1, :ww]).astype(np.float32)
        blk = blk.reshape((y1 - y0) // step, step, ww // step, step, 3).mean(axis=(1, 3))
        small[y0 // step:y1 // step] = blk
    base = Image.fromarray((small * 0.7).astype(np.uint8)).convert('RGBA')
    lay = Image.new('RGBA', base.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(lay)
    try:
        _fb = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
        _fr = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
        ImageFont.truetype(_fb, 10)
        font = lambda s: ImageFont.truetype(_fb, s)
        fontr = lambda s: ImageFont.truetype(_fr, s)
    except OSError:
        font = fontr = lambda s: ImageFont.load_default()
    # big blocks first, so that the small ones are drawn on top of them
    for b in sorted(blocks, key=lambda b: -(b['x1'] - b['x0']) * (b['y1'] - b['y0'])):
        col = KIND_COL[b['kind']]
        box = [b['x0'] * scale, b['y0'] * scale, b['x1'] * scale, b['y1'] * scale]
        d.rectangle(box, fill=col + (30,), outline=col + (255,), width=1 if b['prov'] else 2)
    img = Image.alpha_composite(base, lay).convert('RGB')
    d = ImageDraw.Draw(img)
    placed, numbered = layout_labels(blocks, scale, d, font)
    for k, x, y, lines, size in placed:
        f = font(size)
        for l in lines:
            d.text((x, y), l, fill=(255, 255, 255), font=f, stroke_width=2, stroke_fill=(0, 0, 0))
            y += size + 2
    f10 = font(10)
    for num, k, x, y in numbered:
        col = KIND_COL[blocks[k]['kind']]
        t = str(num)
        tw = int(d.textlength(t, font=f10)) + 4
        d.rectangle([x, y, x + tw, y + 12], fill=(0, 0, 0), outline=col)
        d.text((x + 2, y), t, fill=(255, 255, 255), font=f10)

    # legend panel on the right: key of kinds, then the numbered blocks
    lh, colw = 15, 330
    rows = max(1, (img.size[1] - 190) // lh)
    ncol = max(1, -(-len(numbered) // rows))
    panel = Image.new('RGB', (ncol * colw + 16, img.size[1]), (24, 24, 24))
    pd = ImageDraw.Draw(panel)
    fr, fbold = fontr(11), font(12)
    pd.text((10, 8), 'HD6845S floor plan', fill=(255, 255, 255), font=font(15))
    y = 34
    for i, (kind, col) in enumerate(KIND_COL.items()):
        cx, cy = 10 + (i % 3) * 105, y + (i // 3) * 16
        pd.rectangle([cx, cy + 2, cx + 10, cy + 12], fill=col)
        pd.text((cx + 15, cy), kind, fill=(230, 230, 230), font=fr)
    y += 52
    pd.text((10, y), 'thin outline and "?": identification provisional', fill=(200, 200, 200), font=fr)
    pd.text((10, y + 15), 'numbers: blocks too small for their name', fill=(200, 200, 200), font=fr)
    y0 = y + 40
    for i, (num, k, _, _) in enumerate(numbered):
        b = blocks[k]
        cx = 8 + (i // rows) * colw
        cy = y0 + (i % rows) * lh
        pd.rectangle([cx, cy + 3, cx + 8, cy + 11], fill=KIND_COL[b['kind']])
        name = b['name'] + (' ?' if b['prov'] else '')
        t = '%d  %s' % (num, name)
        while pd.textlength(t, font=fr) > colw - 20 and len(t) > 8:
            t = t[:-2]
        pd.text((cx + 13, cy), t, fill=(240, 240, 240), font=fr)
    out = Image.new('RGB', (img.size[0] + panel.size[0], img.size[1]), (24, 24, 24))
    out.paste(img, (0, 0))
    out.paste(panel, (img.size[0], 0))
    out.save(os.path.join(OUT, 'floorplan.jpg'), quality=85)

    # every block as text: number (if it has one), kind, name, box, description
    numof = {k: num for num, k, _, _ in numbered}
    with open(os.path.join(OUT, 'floorplan_legend.txt'), 'w') as f:
        f.write('# no.\tkind\tname\tx0,y0:x1,y1 (metal-shot pixels)\tdescription\n')
        idx = sorted(range(len(blocks)), key=lambda k: (round(blocks[k]['y0'] / 500), blocks[k]['x0']))
        for k in idx:
            b = blocks[k]
            f.write('%s\t%s%s\t%s\t%d,%d:%d,%d\t%s\n' % (
                numof.get(k, '-'), '?' if b['prov'] else '', b['kind'], b['name'],
                b['x0'], b['y0'], b['x1'], b['y1'], b['desc']))

    with open(os.path.join(OUT, 'floorplan.svg'), 'w') as f:
        f.write(f'<?xml version="1.0" encoding="UTF-8"?>\n'
                f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" '
                f'viewBox="0 0 {W} {H}">\n'
                f'<image xlink:href="../dieshots/hd6845metal2ndchip.jpg" x="0" y="0" width="{W}" height="{H}"/>\n'
                + floorplan_svg_body(blocks) + '</svg>\n')
    print('floor plan: %d labels drawn in place, %d numbered' % (len(placed), len(numbered)))


def summary_lines(nl, missing, opens):
    yield nl.report().split('\n')[0]
    yield ('signal names: %d not in notes/signals.md%s; %d open joins (_u)'
           % (len(missing), (' (' + ' '.join(missing[:8]) + (' ...' if len(missing) > 8 else '') + ')') if missing else '',
              len(opens)))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--check', action='store_true',
                    help='extract and check, print the summary lines, write nothing')
    ap.add_argument('--no-floorplan', action='store_true', help='skip the floor-plan images')
    args = ap.parse_args()
    if not args.check and os.environ.get('HD_COORD') != '1':
        print('build: this rewrites out/, and only the coordinator runs it (HD_COORD=1 tools/build.py).\n'
              '       tools/build.py --check prints the report lines without writing.', file=sys.stderr)
        sys.exit(2)
    # Blocks are traced by several agents at once: leave out any file that does not
    # load on its own (work in progress) rather than fail the whole build.
    import glob
    good, bad = [], []
    for f in sorted(glob.glob(os.path.join(ROOT, 'trace', '*.txt'))):
        try:
            tracelib.Trace(files=[f])
            good.append(f)
        except Exception as e:           # noqa: BLE001 - report and carry on
            bad.append((os.path.basename(f), str(e).splitlines()[-1]))
    for name, why in bad:
        print(f'left out {name}: {why}')
    tr = tracelib.Trace(files=good)
    nl = netlist_mod.Netlist(tr)
    import signals as signals_mod
    missing, opens = signals_mod.check([n.name for n in nl.nodes.values() if n.names])
    if args.check:
        print('\n'.join(summary_lines(nl, missing, opens)))
        return
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, 'netlist.json'), 'w') as f:
        json.dump(nl.to_json(), f, indent=1)
    with open(os.path.join(OUT, 'report.txt'), 'w') as f:
        f.write(nl.report() + '\n')
        f.write('\nsignal names (notes/signals.md)\n')
        f.write('  not in the glossary (%d): %s\n' % (len(missing), ' '.join(missing) or '-'))
        f.write('  open joins, names ending in _u (%d): %s\n' % (len(opens), ' '.join(opens) or '-'))
    blocks = read_floorplan()
    build_svg(tr, nl, blocks)
    if not args.no_floorplan:
        build_floorplan(blocks)
    print('\n'.join(summary_lines(nl, missing, opens)))
    print(f'{len(tr.items)} shapes, {len(blocks)} floor-plan blocks -> out/')


if __name__ == '__main__':
    main()
