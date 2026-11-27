# Claim: cdp4

Written by `tools/claim.py take`. Removed by the coordinator when the work is
merged, or by `tools/claim.py release` if it is abandoned.

| Field | Value |
|---|---|
| Who | mattgodbolt |
| Claimed | 2026-11-27 05:25 -0600 |
| Region | 7600-7700 x 14000-14100 |
| What | cdp4 housekeeping, no tracing, READY BUT NOT MERGED: branch cdp4 (e0a534b) commits the four measuring scripts the merged notes of cdp4, cdp3 and eof cite from an untracked scratch folder, as tools/cdp4_cand.py, cdp4_candh.py, cdp4_padc.py, cdp4_track.py. The merge gate fails for every branch at check 4b on a line already on main: notes/journal.md:3544 names the former name bl0_w15566 (the catch-up command of the 2026-11-25 refresh) on a line without '->', so tools/signals.py --docs reports it. The journal is the coordinator's file; this branch and any later ones of mine wait for that line (put the command on the '->' line, or reword it) |
| Branch | cdp4 |
| Status | tracing |
