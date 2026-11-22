#!/usr/bin/env python3
"""Look for poly leaving a poly row or column along its two flanks (a hidden branch), as text.

usage: eof_tee.py h Y0 Y1 XA XB     a row whose edges are y Y0 and Y1, from x XA to XB
       eof_tee.py v X0 X1 YA YB     a column whose edges are x X0 and X1, from y YA to YB
       (run from the repository's root; it reads cache/acid1b.npy, cache/metal.npy, cache/metal1.npy)

It samples 7 px outside each edge every 3 px and prints the stretches of 9 px or more where the clean shot
is salmon (poly under metal: R > 195, R-G > 35, G-B > 25) or BOTH metal shots are orange (open poly: chip 2
R > 140, R-G > 35, B < 80; chip 1 R > 120, G < 100, B < 60). A branch shows on one flank; a blob on both
flanks at one place is something lying across the wire (look at it).

Why: a branch whose first 25 px lie in the gap between two metals shows in the clean shot only as a dark
ring, and a survey at 2x takes the row for another net's (eof run 52, found by review round 63: the tee at
(10366,17690); `eof_tee.py v 10346 10364 17625 17800` finds it). Limits: the colours drift across the die
(tracing guide, trap 1): where the clean shot has interference colours a flank can read salmon over field
(hop 1 of the read bus at (13130,18099): the chip-2 stripped shot decided, field); a branch narrower than
9 px along the flank, or one that leaves under a metal where the clean shot is not salmon, is missed. An
aid: every hit is looked at on a view, and "none" is not a proof.
"""
import sys, numpy as np
ac=np.load('cache/acid1b.npy',mmap_mode='r'); m2=np.load('cache/metal.npy',mmap_mode='r'); m1=np.load('cache/metal1.npy',mmap_mode='r')
def px(a,x,y): return np.asarray(a[y-1:y+2,x-1:x+2,:3],float).reshape(-1,3).mean(0)
def poly(x,y):
    c=px(ac,x,y); a=px(m2,x,y); b=px(m1,x,y)
    if c[0]>195 and c[0]-c[1]>35 and c[1]-c[2]>25: return 'P'
    if a[0]>140 and a[0]-a[1]>35 and a[2]<80 and b[0]>120 and b[1]<100 and b[2]<60: return 'p'
    return '.'
o,e0,e1,a0,a1=sys.argv[1],*map(int,sys.argv[2:6])
for name,e in (('first flank',e0-7),('second flank',e1+7)):
    s=''.join(poly(t,e) if o=='h' else poly(e,t) for t in range(a0,a1,3))
    runs=[];i=0
    while i<len(s):
        if s[i]!='.':
            j=i
            while j<len(s) and s[j]!='.': j+=1
            if j-i>=3: runs.append('%d-%d(%s)'%(a0+3*i,a0+3*j,s[i]))
            i=j
        else: i+=1
    print(name,'at',e,':',' '.join(runs) or 'none')
