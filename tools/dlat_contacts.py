#!/usr/bin/env python3
"""Check the metal contacts of the four `dlat_lat` copies against both metal shots and the
clean shot, as text.

For each contact of the cell (master coordinates, the bit-5 copy) and each copy (bit 5 at
0,0; bits 6, 7 at +477, +954; bit 4 mirrored about y 14350) prints: the brightness (red) of
the centre (5x5 mean) and of a ring of radius 15 in both metal shots, where the brightest
7x7 patch within +-10 px lies (dx,dy from the drawn centre), and the clean shot's red minus
green at the centre (a contact hole measures low or green against poly 50-70 and field 60+).
A metal contact: bright centre (over about 150) in a darker ring, in both chips.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, view

CONTACTS = [('M_d top', 16576, 14455), ('M_d bottom', 16578, 14658), ('M_c top', 16766, 14389),
            ('M_c bottom', 16756, 14792), ('le band B', 16819, 14436), ('le band D', 16818, 14654),
            ('VSS top', 16697, 14350), ('VSS mid', 16701, 14530), ('VSS bottom', 16702, 14729),
            ('VCC N3', 16512, 14710), ('VCC long (top)', 16512, 14540), ('VCC long (bottom)', 16512, 14595)]
COPIES = [('bit5', lambda y: y), ('bit6', lambda y: y + 477), ('bit7', lambda y: y + 954),
          ('bit4', lambda y: 28700 - y)]

def look(lay, x, y):
    a = view.raw(lay, x - 20, y - 20, 41, 41)[..., :3].astype(float)
    r = a[..., 0]
    c = r[18:23, 18:23].mean()
    ang = np.linspace(0, 2 * np.pi, 24, endpoint=False)
    ring = np.mean([r[int(round(20 + 15 * np.sin(t))), int(round(20 + 15 * np.cos(t)))] for t in ang])
    best = (-1, 0, 0)
    for dy in range(-10, 11):
        for dx in range(-10, 11):
            v = r[20 + dy - 3:20 + dy + 4, 20 + dx - 3:20 + dx + 4].mean()
            if v > best[0]:
                best = (v, dx, dy)
    return c, ring, best[1], best[2], a

print(f"{'contact':18s} {'copy':5s} {'x,y':12s}  chip2 c/ring  peak   chip1 c/ring  peak   clean R-G")
for name, x, y in CONTACTS:
    for cp, f in COPIES:
        yy = f(y)
        c2, r2, dx2, dy2, _ = look('metal', x, yy)
        c1, r1, dx1, dy1, _ = look('metal1', x, yy)
        b = view.raw('acid1b', x - 2, yy - 2, 5, 5)[..., :3].astype(float).mean(axis=(0, 1))
        print(f"{name:18s} {cp:5s} {x},{yy:<6d}  {c2:4.0f}/{r2:4.0f}  {dx2:+3d},{dy2:+3d}   {c1:4.0f}/{r1:4.0f}  {dx1:+3d},{dy1:+3d}   {b[0]-b[1]:+5.0f}")
