# Claim: lc3

Written by `tools/claim.py take`. Removed by the coordinator when the work is
merged, or by `tools/claim.py release` if it is abandoned.

| Field | Value |
|---|---|
| Who | mattgodbolt |
| Claimed | 2026-11-19 07:17 -0600 |
| Region | 4750-6450 x 9233-10400 |
| What | left-centre logic part 3, continued (Fable). SPLIT WITH eof (run 6): the west flip-flop copy at y 9185-9990 is eof's piece ff3 (pushed to origin/eof first; lc3 drops its own drawing of it and will use eof's names eof_w9255, eof_w9332, eof_w9505, eof_w9472). lc3 has DRAWN the turned east copy, stage E4 (x 4990-5450, y 9150-9945, '@inst lc2_ff 260,716 rot=180 o=4826,8810', branch lc3 b7bcf40, in review: clock lc2_w9034, slave output = lc2_w9210, the last input of lc2_w9125) and IS DRAWING the unit below both columns (x 4440-5450, y 9960-10580: lc2_ff's latch K in the west column, its gates K3 and K4 turned in the east one, joined by five poly rows under the rails at y 10380-10555: believed stage 0, whose slave output is eof_w9255), from eof's ports at y 9990 on. Please leave E4 and that unit to lc3. Then the gate pair's R31 review and the rest of the strip east of x 5460 |
| Branch | lc3 |
| Status | tracing |
