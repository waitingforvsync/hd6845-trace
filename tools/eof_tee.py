#!/usr/bin/env python3
"""tee.py h Y0 Y1 XA XB | v X0 X1 YA YB: look for poly leaving a poly row (h) or column (v) along its two
flanks: samples 7 px outside each edge every 3 px; prints the stretches of 9 px or more where the clean shot
is salmon (poly under metal: R>195, R-G>35, G-B>25) or the chip-2 AND chip-1 metal shots are orange (open
poly: chip 2 R>140, R-G>35, B<80; chip 1 R>120, G<100, B<60). A branch shows on one flank; a blob on both
flanks at one place is something lying across (look at it). An aid: every hit is looked at on a view."""
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
