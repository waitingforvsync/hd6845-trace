"""Dark runs along a straight metal track, in both metal shots.

  tools/t.sh tc2 tc2_runs.py col X Y0 Y1 [HALF]     (or: row Y X0 X1 [HALF])

Takes the median over +-HALF px across the track (default 3) of the follower's metal test
(R > 177 and G > 128) per pixel along it, and prints every run where the test fails, with
its length, for chip 2 (`metal`) and chip 1 (`metal1`) separately. A poly or diffusion edge
underneath prints as a run of 3-10 px; a contact ring as 8-15 px either side of a bright
centre; a break as 25 px or more in both shots (skill recipe "Metal break or poly edge?").
Thin dim metals fail the test everywhere (tracing guide, trap 19): not for those.
"""
import sys, os
import numpy as np
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def main():
    kind = sys.argv[1]; a, b, c = map(int, sys.argv[2:5]); half = int(sys.argv[5]) if len(sys.argv) > 5 else 3
    for name in ('metal', 'metal1'):
        im = np.load(os.path.join(ROOT, 'cache', name + '.npy'), mmap_mode='r')
        if kind == 'col':
            seg = np.asarray(im[b:c, a - half:a + half + 1, :3]).astype(int); seg = np.median(seg, axis=1)
        else:
            seg = np.asarray(im[a - half:a + half + 1, b:c, :3]).astype(int); seg = np.median(seg, axis=0)
        ok = (seg[:, 0] > 177) & (seg[:, 1] > 128)
        runs = []; s = None
        for i, v in enumerate(ok):
            if not v and s is None: s = i
            if v and s is not None: runs.append((b + s, b + i - 1)); s = None
        if s is not None: runs.append((b + s, c - 1))
        print(name, ' '.join(f'{p}-{q}({q - p + 1})' for p, q in runs if q - p + 1 >= 3))
main()
