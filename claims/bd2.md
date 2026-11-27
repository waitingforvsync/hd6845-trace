# Claim: bd2

Written by `tools/claim.py take`. Removed by the coordinator when the work is
merged, or by `tools/claim.py release` if it is abandoned.

| Field | Value |
|---|---|
| Who | mattgodbolt |
| Claimed | 2026-11-27 05:25 -0600 |
| Region | 15880-16420 x 16540-17100; 15840-16420 x 17100-17420 |
| What | bd2 run 3: the left gate column below group 3 (x 15890-16150, y 16540-17100): the load of the rs_d inverter (bd2_rs_n), the band y 16681-16699 that rw_d taps, and the two-input NOR that drives dbus_le (the data input latches' enable; cdp4's port (16130,16865)); then the gate cluster south of it under the same rail (y 17100-17410) that feeds the NOR's second input |
| Branch | bd2 |
| Status | tracing |
