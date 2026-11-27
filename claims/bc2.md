# Claim: bc2

Written by `tools/claim.py take`. Removed by the coordinator when the work is
merged, or by `tools/claim.py release` if it is abandoned.

| Field | Value |
|---|---|
| Who | mattgodbolt |
| Claimed | 2026-11-27 08:42 -0600 |
| Region | 9100-10250 x 14650-16300; 7740-9800 x 14370-14460 |
| What | bc2 run 3: the two bus lines y 14394 and y 14437 (lines 2 and 3 of bc1's 13-line bus) end to end, from their west-end contacts at x 7790 / 7831 to the pads (9764,14394) and (9722,14437) where the thin metals into bc2's two-bit decode start: which nets the decode's two inputs are (also R10 for these two lines); then on down the centre block's east rail (y 15800 on). Run 2 (three inverters, three NANDs) is reviewed and waits on this branch for the merge gate, which fails on main itself (see the cdp4 claim) |
| Branch | bc2 |
| Status | tracing |
