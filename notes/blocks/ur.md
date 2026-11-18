# ur: upper rows of the left array (x 2918-4240, y 6543-10924): two more counters

Serial work, 2026-11-16. Trace: `trace/ur.txt` (the clock generator's cell is defined in
`trace/wl.txt`). Views: `cache/scratch/ur/`.

## Status

The nine rows are **nine more copies of the counter bit cell of the mid-right array**
(`trace/mra.txt`, `notes/blocks/mra.md`). Instanced, with their supply rails and clock
lines drawn: 252 transistors, plus 16 for the clock generator; extraction clean. They form

- a **4-bit counter**, rows u0-u3 (y 6543-8452): `c4l3` ... `c4l0` from the top;
- a **5-bit counter**, rows u4-u8 (y 8539-10924): `sl4` ... `sl0` from the top;

with an 87 px channel between them (y 8452-8539).

**The 5-bit counter is the scan line counter** (`sl0`-`sl4`; its rows were first tagged
c5l): its five outputs are drawn all the way to the comparator of R5, vertical total
adjust, in the upper right datapath, bit for bit (`notes/blocks/slbus.md`,
`notes/blocks/rdp1.md`). The 4-bit counter (`c4l0`-`c4l3`) is not identified: it shares
the scan line counter's clocks, so it counts scan lines too (the vertical sync width
counter is the obvious candidate; its four outputs leave east along y 6157-6280 and are
not followed).

Also traced: **their clock generator**, a second copy of the row counter's
(`notes/blocks/wl.md`), in the left column beside rows u0-u2 (16 transistors by
instancing; see below).

Not done: the carry-ins of `c4l0` and `sl0` (they enter from the left column at rows u3
and u8), where the nine master outputs go (they leave the rows to the east), the sources
of the six clock and control lines, the pieces of the line x 3478 (the mid-right array's
"la" line), and everything the mid-right array's cell itself still lacks (the unresolved
branch of the next-value network).

## How it was found

`tools/findcell.py` with the master rectangle of each of the four columns of the counter
cell (chain, col2, col3, col4) against the left array: nine hits each at dx -8807,
dy -3339, -2862, -2384, -1907, -1343, -866, -389, +88, +566 from the master row, scores
0.88-0.92 in the clean shot (0.67-0.78 for two columns of the bottom row, where the
bottom row of a group differs as it does in the mid-right array). An overlay of a whole
instanced row on the metal shot sits on the photo (`row_chk.png`).

Mosaics of the nine row boundaries (`lk1.png`, `lk2.png`, `tb1.png`, `tb2.png`):

- carry links row N -> row N+1 exist below u0, u1, u2 and below u4, u5, u6, u7; not below
  u3 and u8. So the carry runs upward inside each group, bit 0 at the bottom, as in the
  mid-right array;
- no row has the drain-tab extension: there are **no look-ahead lines** here. The 5-bit
  counter is a plain ripple chain;
- at u3 and u8 a poly arrives from the left (the left column): the carry-in of each
  counter. Not drawn yet.

## Clock and control lines (read in the metal shot at 2.1x at both ends and in the channel)

| Line | 4-bit counter (u0-u3) | 5-bit counter (u4-u8) |
|---|---|---|
| master clock, L1 (x 3693) | `lc_ck_m` | the same line, unbroken through the channel |
| slave clock, rail x 4218 | `lc_ck_s` | the same rail, unbroken through the channel |
| L3 (second pull-down of `_nx_g`, x 3780) | `c4l_l3`: from the north, ends plainly at y 8500 | `sl_l3`: the line that passes the 4-bit rows on the L2 position steps right in the channel onto L3 |
| pass-gate line "gab" (x 4095) | `c4l_gab`: from the north, ends plainly at y 8505 | `sl_gab`: the line that passes the 4-bit rows at x 3968 turns east in the channel and comes down the gab position |

So unlike the three counters of the mid-right array, **these two share one master and one
slave clock**; they differ in their L3 and gab lines.

Top ends (y 6330-6580): four horizontal poly lines come from the west along y 6365, 6410,
6455 and 6500.

- y 6500: ends on a contact (3715,6497) at the top of L1: the master clock.
- y 6455: runs on east to a contact (4212,6455) at the top of the slave rail.
- y 6410: contact (3757,6410) at the top of the line that becomes the 5-bit counter's L3;
  and a second contact (3968,6410) under a metal that arrives from the north.
- y 6365: not looked at.
- `sl_gab`'s line starts on a contact (3968,6520) fed by a poly from the east along
  y 6510-6530, and ends at the bottom on a contact (4087,11005).

The supply rails are named by structure (the cells are identical to the mid-right
array's): VSS x 3021, 3274, 3913; VCC x 3110, 3630, 4150. At the bottom the VSS rail
x 3913 runs into a wide horizontal metal (y 10930-10975).

## The clock generator (left column, x 2262-2837, y 6719-7729)

`tools/findcell.py` with the rectangle of the row counter's generator (11090,7890 to
11665,8900) finds one copy at dx -8828, dy -1171 (score 0.83; 0.92 for its right-hand
part). `trace/wl.txt` now defines the generator as the cell `wl_ckgen`; this block
places the copy with tag `lc`. Overlays on both shots sit on the photo (`gen_chk_m.png`,
`gen_chk_a.png`). The MA bundle's vertical metals pass over its two wide drivers.

```
lc_ck_s = NOR(lc_ck_m_dly, lc_step)        slave clock: metal x 2696 up to (2695,6590), poly east along y 6455
lc_ck_m = NOR(lc_step_n, lc_ck_s_dly)      master clock: metal x 2740 up to (2742,6630), poly north and east along y 6500
lc_step_n = NOT lc_step
```

So both counters of the left array step **once per pulse of `lc_step`**, as the row
counter does once per pulse of `rc_step`. They do not run on every clock cycle.

**One difference between the copies**, found on the overlay: the pad where the step
signal reaches gate band Gp is one metal track further west here, at (2412,7188). The
cell's contact had landed on the neighbouring metal x 2457, which is `clk_tl`, and the
first extraction read "the counters are clocked by CLK". At 4x that metal passes over the
band with no pad. The pad and contact are now outside the cell, drawn per copy.

**Where `lc_step` comes from**: the metal x 2400-2425 from the pad up to a contact
(2412,6278); poly east along y 6268-6290 to a contact (3345,6278); 90 px of metal south
to a contact (3345,6368); poly east along y 6355-6380 over the top of the counters to
x 5012; south down x 5003-5022 into the **left-centre logic** (followed to y 6900; it
ends on something at about (5030,7000-7150)). Not traced there.

What is left of the left column near the generator: the cell at y 7790-8000 is the
`clk_tl` inverter (`notes/blocks/tla.md`); the cells below it are not traced.

## Correction from `lc1` (coordinator, from pull request #20, 2026-11-18)

- "Where `lc_step` comes from ... it ends on something at about (5030,7000-7150). Not traced there": it
  ends on the output box of `lc1`'s gate 1 at (5006-5053, 6985-7022); `lc_step` = NOT `lc1_w7040`, the
  output of latch D's upper unit (`notes/blocks/lc1.md`).
- `trace/ur.txt`: the poly `P 3355,6368 x5012 y6900 w=20` is drawn about 9 px west of the photo's band
  (x 5011-5031) over its last stretch. Geometry only; it still overlaps.
