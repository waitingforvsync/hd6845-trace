# Claim: bc2

Written by `tools/claim.py take`. Removed by the coordinator when the work is
merged, or by `tools/claim.py release` if it is abandoned.

| Field | Value |
|---|---|
| Who | mattgodbolt |
| Claimed | 2026-11-27 09:43 -0600 |
| Region | 9100-10250 x 14650-16300; 7540-9200 x 14590-14670; 7740-9800 x 14370-14460 |
| What | bc2 run 4: the centre block's west rail (x 9462-9510): its first unit (y 14940-15110: two pull-downs, a load beside the middle rail, output by the poly row y 15042 west to the pad (9183,15043)), and the two bus lines that feed it, y 14611 and y 14655 (lines 6 and 7 of bc1's 13-line bus), end to end from busl's row ends at x 7550 (lc2_w9079, lc3_e9756) to the pads (9183,14977) and (9142,15086); then the next units down the rail. Runs 2-3 (six gates on the east rail, an inverter, two bus lines) are reviewed and wait on this branch for the merge gate, which fails on main itself (see the cdp4 claim) |
| Branch | bc2 |
| Status | tracing |
