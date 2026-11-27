# Claim: bd2

Written by `tools/claim.py take`. Removed by the coordinator when the work is
merged, or by `tools/claim.py release` if it is abandoned.

| Field | Value |
|---|---|
| Who | mattgodbolt |
| Claimed | 2026-11-27 06:43 -0600 |
| Region | 16230-16500 x 15380-15880; 15880-16420 x 16540-17420 |
| What | bd2 run 4: the gate group right of the bundle (x 16240-16490, y 15400-15860): the loads of wr_data_e_n and ar_load_n, where wr_data_e_n goes, and the source of bd2_x (the second term of the address register's load strobe). Run 3 (the column y 16529-17400: dbus_le's driver, the read gate rd_data_e) is reviewed and waits on this branch for the merge gate, which fails on main itself (see the cdp4 claim) |
| Branch | bd2 |
| Status | tracing |
