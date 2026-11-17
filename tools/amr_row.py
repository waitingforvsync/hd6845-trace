#!/usr/bin/env python3
"""Continuity of a horizontal poly row in the clean shot:  amr_row.py Y X0 X1 [OFF]

For every x from X0 to X1 the colour at the row's centre (y = Y, searched +-5) is compared
with the mean of the two flanks OFF px above and below (default 21: half the 43 px pitch of
the channels' rows). Prints the stretches of 8 px or more where the centre does not differ
from the flanks, i.e. where no row is seen. It does not detect a track step (a neighbour
then stands at this y): look for those on a strip view.
"""
import os, sys
import numpy as np
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
Y=int(sys.argv[1]); x0=int(sys.argv[2]); x1=int(sys.argv[3]); off=int(sys.argv[4]) if len(sys.argv)>4 else 21
a=np.load(os.path.join(ROOT, 'cache', 'acid1b.npy'), mmap_mode='r')
reg=np.array(a[Y-off-8:Y+off+9,x0:x1]).astype(float)
c=off+8
d=np.zeros(x1-x0)
for i in range(x1-x0):
    col=reg[:,max(0,i-2):i+3].mean(1)
    dm=0
    for s in range(-5,6):
        cen=col[c+s-4:c+s+5].mean(0); fl=(col[c+s-off-3:c+s-off+4].mean(0)+col[c+s+off-3:c+s+off+4].mean(0))/2
        dm=max(dm,np.abs(cen-fl).sum())
    d[i]=dm
runs=[];st=None
for i,v in enumerate(d<45):
    if v and st is None: st=i
    if not v and st is not None:
        if i-st>=8: runs.append((x0+st,x0+i-1,int(d[st:i].mean())))
        st=None
if st is not None and x1-x0-st>=8: runs.append((x0+st,x1-1,int(d[st:].mean())))
print('row',Y,x0,x1,'median d',int(np.median(d)),'weak runs:',runs)
