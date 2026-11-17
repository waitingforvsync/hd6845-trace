#!/usr/bin/env python3
"""Register every die shot to the reference frame and resample it into that frame.

The reference frame is the metal shot of the second chip (hd6845metal2ndchip.jpg);
all coordinates in this project are its pixels. Each other shot is matched against a
reference picture of the same kind (metal against metal, stripped against stripped),
because like-for-like matching is far more reliable than matching across kinds.

For each shot: a coarse global offset is found at 1/8 scale, local offsets are then
measured on a grid of patches by phase correlation of edge images, an affine map is
fitted robustly, and what the affine leaves over is smoothed into a correction field
(different stitching of the two dies shows up there). The shot is resampled with
affine + correction and written to cache/<name>.npy.

  usage: align.py [--record] [name ...]        (default: all that are missing)

Shots (name: source file, matched against):
  acid     hd6845acid2ndchip.jpg   chip 2, metal stripped         against metal
  metal1   hd6845metal.jpg         chip 1, metal intact           against metal
  acid1    hd6845acid.jpg          chip 1, metal stripped         against acid
  acid1b   hd6845acid2.jpg         chip 1, second stripped shot   against acid

The fit is written to cache/align.json (untracked: each machine's own fit, which can differ
from another machine's by a fraction of a pixel, and is what that machine's cache was resampled
with). trace/align.json is the project's recorded fit, read by tools/build.py to place the photos
in the SVG; only --record writes it, and only the coordinator, who builds out/, uses --record.
Tracing never reads either file.
"""
import json
import os
import sys
import numpy as np
import cv2
from PIL import Image

Image.MAX_IMAGE_PIXELS = None
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = os.path.join(ROOT, 'cache')
N = 768        # patch size
STEP = 900     # grid step

SHOTS = {
    'acid':   ('hd6845acid2ndchip.jpg', 'metal'),
    'metal1': ('hd6845metal.jpg', 'metal'),
    'acid1':  ('hd6845acid.jpg', 'acid'),
    'acid1b': ('hd6845acid2.jpg', 'acid'),
}
FILES = {'metal': 'metal.npy', 'acid': 'acid_aligned.npy', 'metal1': 'metal1.npy',
         'acid1': 'acid1.npy', 'acid1b': 'acid1b.npy'}


def edges(a):
    g = cv2.cvtColor(np.ascontiguousarray(a), cv2.COLOR_RGB2GRAY).astype(np.float32)
    g = cv2.GaussianBlur(g, (0, 0), 2)
    e = cv2.magnitude(cv2.Sobel(g, cv2.CV_32F, 1, 0), cv2.Sobel(g, cv2.CV_32F, 0, 1))
    return (e - e.mean()) / (e.std() + 1e-6)


def small_edges(a, q=8):
    H, W = a.shape[:2]
    hh, ww = H // q * q, W // q * q
    out = np.zeros((hh // q, ww // q), np.float32)
    for y0 in range(0, hh, q * 256):
        y1 = min(hh, y0 + q * 256)
        g = cv2.cvtColor(np.ascontiguousarray(a[y0:y1, :ww]), cv2.COLOR_RGB2GRAY)
        out[y0 // q:y1 // q] = cv2.resize(g, (ww // q, (y1 - y0) // q), interpolation=cv2.INTER_AREA)
    out = cv2.GaussianBlur(out, (0, 0), 1.5)
    return cv2.magnitude(cv2.Sobel(out, cv2.CV_32F, 1, 0), cv2.Sobel(out, cv2.CV_32F, 0, 1))


def coarse(ref, src, q=8):
    """(ox, oy) such that ref(x, y) shows what src(x - ox, y - oy) shows."""
    r, s = small_edges(ref, q), small_edges(src, q)
    h, w = s.shape
    t = s[h // 5:4 * h // 5, w // 5:4 * w // 5]
    pad = 160
    R = cv2.copyMakeBorder(r, pad, pad, pad, pad, cv2.BORDER_REPLICATE)
    res = cv2.matchTemplate(R, t, cv2.TM_CCOEFF_NORMED)
    _, sc, _, loc = cv2.minMaxLoc(res)
    return (loc[0] - pad - w // 5) * q, (loc[1] - pad - h // 5) * q, sc


def measure(ref, src, ox, oy):
    H, W = ref.shape[:2]
    win = cv2.createHanningWindow((N, N), cv2.CV_32F)
    pts = []
    for cy in range(N, H - N, STEP):
        for cx in range(N, W - N, STEP):
            x0, y0 = cx - ox - N // 2, cy - oy - N // 2
            if x0 < 0 or y0 < 0 or x0 + N > src.shape[1] or y0 + N > src.shape[0]:
                continue
            m = edges(ref[cy - N // 2:cy + N // 2, cx - N // 2:cx + N // 2])
            a = edges(src[y0:y0 + N, x0:x0 + N])
            (dx, dy), resp = cv2.phaseCorrelate(m, a, win)
            # ref (cx, cy) is at src (cx - ox + dx, cy - oy + dy)
            pts.append((cx, cy, dx - ox, dy - oy, resp))
    return np.array(pts)


def fit(P, thresh):
    keep = P[:, 4] > thresh
    for _ in range(5):
        Q = P[keep]
        X = np.c_[Q[:, 0], Q[:, 1], np.ones(len(Q))]
        cx, *_ = np.linalg.lstsq(X, Q[:, 2], rcond=None)
        cy, *_ = np.linalg.lstsq(X, Q[:, 3], rcond=None)
        Xa = np.c_[P[:, 0], P[:, 1], np.ones(len(P))]
        rx, ry = P[:, 2] - Xa @ cx, P[:, 3] - Xa @ cy
        r = np.hypot(rx, ry)
        keep = (P[:, 4] > thresh) & (r < 4.0)
    return cx, cy, rx, ry, keep


def residual_field(P, rx, ry, keep, shape):
    """Smooth field of what the affine leaves over, on a STEP grid, for remapping."""
    H, W = shape
    gx = np.arange(N, W - N, STEP)
    gy = np.arange(N, H - N, STEP)
    fx = np.zeros((len(gy), len(gx)), np.float32)
    fy = np.zeros_like(fx)
    wt = np.zeros_like(fx)
    for (cx, cy, *_), ax, ay, k in zip(P, rx, ry, keep):
        if not k:
            continue
        i, j = int(round((cy - N) / STEP)), int(round((cx - N) / STEP))
        if 0 <= i < len(gy) and 0 <= j < len(gx):
            fx[i, j], fy[i, j], wt[i, j] = ax, ay, 1
    # fill holes and smooth: normalised convolution
    k = (5, 5)
    sw = cv2.GaussianBlur(wt, k, 1.2) + 1e-6
    return cv2.GaussianBlur(fx * wt, k, 1.2) / sw, cv2.GaussianBlur(fy * wt, k, 1.2) / sw, gx, gy


def align(name):
    srcfile, refname = SHOTS[name]
    ref = np.load(os.path.join(CACHE, FILES[refname]), mmap_mode='r')
    if name == 'acid' and os.path.exists(os.path.join(CACHE, 'acid.npy')):
        src = np.load(os.path.join(CACHE, 'acid.npy'), mmap_mode='r')
    else:
        src = np.asarray(Image.open(os.path.join(ROOT, 'dieshots', srcfile)))
    ox, oy, sc = coarse(ref, src)
    P = measure(ref, src, ox, oy)
    thresh = 0.05
    cx, cy, rx, ry, keep = fit(P, thresh)
    rms_aff = float(np.sqrt((rx[keep] ** 2 + ry[keep] ** 2).mean()))
    fx, fy, gx, gy = residual_field(P, rx, ry, keep, ref.shape[:2])
    # residual after the correction field, at the measured points
    after = []
    for (px, py, *_), ax, ay, k in zip(P, rx, ry, keep):
        if k:
            i, j = int(round((py - N) / STEP)), int(round((px - N) / STEP))
            after.append(np.hypot(ax - fx[i, j], ay - fy[i, j]))
    rms_after = float(np.sqrt(np.mean(np.square(after))))
    print(f'{name}: coarse offset ({ox},{oy}) score {sc:.2f}; patches {len(P)}, used {int(keep.sum())}; '
          f'affine residual rms {rms_aff:.2f} px, after correction field {rms_after:.2f} px')

    H, W = ref.shape[:2]
    T = np.array([[1 + cx[0], cx[1], cx[2]], [cy[0], 1 + cy[1], cy[2]]])   # ref -> src
    out = np.lib.format.open_memmap(os.path.join(CACHE, FILES[name]), mode='w+',
                                    dtype=np.uint8, shape=(H, W, 3))
    # full-resolution correction field by bilinear upsampling of the grid
    BAND = 1024
    xs = np.arange(W, dtype=np.float32)
    jx = np.clip((xs - gx[0]) / STEP, 0, len(gx) - 1)
    for y0 in range(0, H, BAND):
        y1 = min(H, y0 + BAND)
        ys = np.arange(y0, y1, dtype=np.float32)
        iy = np.clip((ys - gy[0]) / STEP, 0, len(gy) - 1)
        mapj, mapi = np.meshgrid(jx.astype(np.float32), iy.astype(np.float32))
        cxf = cv2.remap(fx, mapj, mapi, cv2.INTER_LINEAR)
        cyf = cv2.remap(fy, mapj, mapi, cv2.INTER_LINEAR)
        X, Y = np.meshgrid(xs, ys)
        mx = (T[0, 0] * X + T[0, 1] * Y + T[0, 2] + cxf).astype(np.float32)
        my = (T[1, 0] * X + T[1, 1] * Y + T[1, 2] + cyf).astype(np.float32)
        s0 = max(0, int(my.min()) - 4)
        s1 = min(src.shape[0], int(my.max()) + 6)
        out[y0:y1] = cv2.remap(np.ascontiguousarray(src[s0:s1]), mx, (my - s0).astype(np.float32), cv2.INTER_LINEAR,
                               borderMode=cv2.BORDER_CONSTANT)
    out.flush()
    return {'source': srcfile, 'matched_against': refname, 'ref_to_src_affine': T.tolist(),
            'patches_used': int(keep.sum()), 'affine_residual_rms_px': rms_aff,
            'residual_after_correction_rms_px': rms_after}


def main():
    args = [a for a in sys.argv[1:] if a != '--record']
    record = '--record' in sys.argv[1:]
    names = args or [n for n in SHOTS if not os.path.exists(os.path.join(CACHE, FILES[n]))]
    jpath = os.path.join(ROOT, 'trace', 'align.json') if record else os.path.join(CACHE, 'align.json')
    seed = jpath if os.path.exists(jpath) else os.path.join(ROOT, 'trace', 'align.json')
    rec = json.load(open(seed)) if os.path.exists(seed) else {}
    if 'metal_to_acid' in rec:       # old single-shot format
        rec = {'acid_old_affine': rec}
    for n in names:
        rec[n] = align(n)
        with open(jpath, 'w') as f:
            json.dump(rec, f, indent=1)


if __name__ == '__main__':
    main()
