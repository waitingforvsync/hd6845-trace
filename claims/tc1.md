# Claim: tc1

Written by `tools/claim.py take`. Removed by the coordinator when the work is
merged, or by `tools/claim.py release` if it is abandoned.

| Field | Value |
|---|---|
| Who | mattgodbolt |
| Claimed | 2026-11-27 09:16 -0600 |
| Region | 6400-6760 x 2500-2700; 8340-9960 x 2880-2960 |
| What | tc1: the missing links of R8's four high bits and their neighbours: (1) west of x 6750 the lines r8_b4_q (metal y 2575), r8_b5_q (poly y 2619), tc1_bus2858 (poly y 2530) and tc1_m7100 (poly y 2659) across to tl6's ports at x 6400 (tl6_p6187, tc2_m6404, tl6_p6143, tcw_m6278), and the ground branch's west end down to tcw's rail; (2) east of x 8350 the polys tc1_bus2814 (y 2898) and tc1_bus2858 (y 2941) by pads, metals and one poly underpass each to R8's bit 6 and bit 7 outputs in cdp1's row. With bc1 / bc2's pieces of today this names the inputs of the two skew decodes in the bottom-centre logic. Branch tc1 contains branch bc1 (the alias chain needs it). All of it waits for the merge gate, which fails on main itself (see the cdp4 claim) |
| Branch | tc1 |
| Status | tracing |
