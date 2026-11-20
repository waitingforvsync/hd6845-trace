# cdp4: central datapath, bottom part (x 7600-10850, y 11200-14000)

Trace: `trace/cdp4.txt`. Scratch: `cache/scratch/cdp4/`. Own tool: `tools/cdp4_tri.py`
(layers of one region in a single row). Median composite of the eight row C cells:
`--comp cdp4_c` (master frame x 8360-8800, y 12790-13300).

## Status

Traced and shipped (extracts clean: 194 transistors, no errors, no open nets), top to
bottom: the lower half of row R1 (8-bit latch row, upside down, selector source b),
channel 1 bus lines, rows A and B (4-way pass-transistor selector per slice), row C
(pull-down on the selector node, then an 8-bit latch row, selector source d), channel 2
(row C latch inputs from the left, selector output to the right), row D (6-bit latch
row under s1..s6, selector source c of s2..s7), supply rails for y 11480-14062.

Run 2 (2026-11-19): **the corner gate group** (x 7550-7870, y 13640-14055; 7 transistors, no
uncertain item): `cdp4_rst` = NOR of six select rows with one load. With every file loaded the
extraction is 2380 nets, 4369 transistors, 0 errors, 0 warnings. See "Corner gate group" under Logic.

Run 3 (2026-11-19 21:27 -0600): **the upper half of row R1** (y 11050-11492; 65 transistors, no
uncertain item): **the comparator of the eight bus lines `cdp4_bus_s0`..`s7` with R15.** Per slice an
exclusive-OR of the bus line with the R15 latch's `q`, whose output gates a wide pull-down on one
diffusion wire through the row; the wire has one load east of s0 and is `bus_eq_r15`, the net `busl`
followed from the row's west end to gate 1 of the NAND beside `cdp3`'s row C. With every file loaded:
2390 nets, 4437 transistors, 0 errors, 0 warnings. See "Row R1 upper" under Logic.

Not traced: the wiring right of x 10600 and below y 14060.

## Conventions

- Eight slices, pitch 390.3. Master slice for all cells is **s2** (third from the left).
  Offsets from findcell: s0 -782, s1 -391, s2 0, s3 391, s4 781, s5 1170, s6 1560, s7 1951.
- Slices are tagged by position (s0 leftmost). **Bit order not established**, but two of
  the selector's four sources are only six bits wide and occupy s2..s7 (in s0 and s1
  those inputs are strapped to VSS), so s0 and s1 are the two high bits if the narrow
  sources are zero-extended.
- Rails, two per slice, vertical wide metal: **VSS** at x 8404 + offset (x 8381-8427 in
  s2), **VCC** at x 8619 + offset (x 8597-8641). How known: all three depletion loads of
  the row C latch hang from a land contacted by the x 8619 rail, the pull-down sources
  sit on lands contacted by the x 8404 rail. A ninth VSS rail at x 10746 (right of s7)
  takes s7's pull-downs; it ends at y 13300. The s0 VCC rail bends left below y 13540.
- Reading the clean shot here: poly over field is salmon even in the open; poly over a
  channel in the open is dark red-brown and textured; diffusion in the open is pink,
  under metal tan; field in the open khaki, under metal pink. Open poly has a light rim
  about 8 px wide that looks like field. Narrow features (under 20 px) show only their
  outlines, so their layer cannot be told from colour.

## Inventory (rows, top to bottom)

| y | What | Slices | State |
|---|---|---|---|
| 11050-11492 | row R1 upper: the comparator of the bus lines with R15 (cells `cdp4_xr`, `cdp4_xpd`), its match line and the line's load | 8 | traced (run 3) |
| 11490-11850 | row R1 lower: the row C latch cell upside down, strobe `wr_r15` (poly line y 11837) | 8 | traced |
| 11860-12190 | channel 1: eight poly bus lines from the left edge, one per slice | 8 | traced |
| 12200-12800 | rows A and B: four pass transistors per slice onto node n | 8 | traced |
| 12800-12950 | row C top: contact of n, pull-down of n gated by `cdp4_rst` | 8 | traced |
| 12950-13300 | row C latch (`cdp4_lat`), strobe `cdp4_ld` | 8 | traced |
| 13310-13650 | channel 2: eight poly lines, each in two pieces (in from the left, n out to the right) | 8 | traced |
| 13660-13695 | six poly links at y 13677: output of the row D cell under slice K to the foot of the c track of slice K+1 | 6 | traced |
| 13700-14060 | row D: the same latch cell, six copies under s1..s6, strobe `cdp4_ld6` | 6 | traced |
| 14060-14700 | fan-out wiring below row D into the random logic | - | not traced |

## Logic

### Rows A and B: 4-way selector (traced)

Per slice four pass transistors (W about 195, L 23-28) share node `cdp4_n_sK` (metal
x 8548-8564 in s2):

```
n <-> a   when sel1     a: s2..s7 a track from row R1 (x 8509 at y 11790, jogs to x 8467 at y 12178)
n <-> b   when sel2     b: track from row R1 (x 8729), all eight slices
n <-> d   when sel3     d: buffered output of the row C latch (x 8729), all eight slices
n <-> c   when sel4     c: s2..s7 a track that runs down through row C and channel 2 into row D
```

- **In s0 and s1 the a and c contacts are strapped to the VSS rail** (metal tab from the
  rail to the contact pad at 8465 + offset, y 12352 and y 12654; no track). So a and c
  are 6-bit sources, b and d 8-bit.
- sel1..sel4: horizontal poly lines y 12223, 12481, 12530, 12786, entering across the
  left edge and ending at x 10590. The gates are branches of these lines. The sel2 and
  sel3 transistors lie under the VCC rail, which has no contact there.
- Every slice checked (mosaics in both layers, overlays, cellcheck).

### Row C top: pull-down of n (traced)

`cdp4_n_sK` has a contact at (8556,12830) to a diffusion strip that runs right, under
the VCC rail, to a diffusion block crossed by the poly line `cdp4_rst` (y 12874); below
the line the block continues right onto the VSS contact land of the **next** slice
(8794,12917). So `n = 0` while rst is high. The width of that transistor is uncertain
(Ambiguities 3).

### Row C latch `cdp4_lat` (traced), 8 bits

Same family as `rdp3_lat` of the right datapath (lower two thirds nearly identical),
plus a buffer. Per slice, 7 transistors:

```
a   <- in      pass transistor 68/22, gate = cdp4_ld (the strobe poly loops round the in contact)
n2  = NOT a    pull-down 56/22 (source on the VSS land), load L2 31/50
q   = NOT n2   pull-down 51/23 to the next slice's VSS land, load L1 29/40
d   = NOT n2   pull-down 85/23 to the next slice's VSS land, load LX 26/29   (buffer)
```

- `in` (`cdp4_in_sK`): metal track x 8453-8477, contact at (8466,12990), runs down
  through the cell to channel 2.
- `d` is a second inverter on n2, logically equal to q, with a strong load and a wide
  pull-down. Its land carries the contact (8712,13027) of the d track, which goes up to
  the sel3 transistor of row B. q itself is not used outside the cell: its metal strap
  ((8668,13152) on the L1 gate pad to (8679,13237) on the output land) and the buried
  contact to a poly strip are there as in `rdp3_lat`, but the strip is a stub ending at
  y 13298.
- n2's poly: L2's gate block, down its right side, along y 13181-13201 under the strap,
  up the right edge of the cell (x 8744-8767, y 12998-13201) as the gate of both
  pull-downs.
- The n track (x 8547-8565) and the c track (x 8500-8521) cross the cell with no contact.
- Hold path: not understood (Ambiguities 1). As traced the latch is dynamic.
- Poly band along the bottom (y 13264-13288, x 8388-8650) tied to the VSS rail by the
  contact (8401,13275); nothing seen crossing it.

Instances: all eight identical in poly/diffusion and metal except the c track
(cellcheck median 0.94-0.95; the only differing blocks in s0, s1 are the missing track).

### Channel 1 (traced)

Eight poly lines `cdp4_bus_s0..s7` at y 12180 (s0), 12137, 12093, 12052, 12008, 11964,
11922, 11877 (s7). Each comes from the left edge and ends on a contact at x 8555 +
offset under a metal track that goes up into row R1 (at the position where, in the
upside-down latch, the n track would pass).

### Channel 2 (traced)

Line K at y 13333 (s0), 13376, 13420, 13463, 13505, 13548, 13590, 13633 (s7) is **two
separate pieces of poly**:

- left piece `cdp4_in_sK`: from the left edge to a contact pad under the in track
  (8465 + offset): data into the row C latch;
- right piece, part of `cdp4_n_sK`: from a contact pad under the n track (8556 + offset)
  to the right edge: the selector output leaving the array. s7's piece ends on a
  contact at about (10896,13634) to a vertical metal; the others run on beyond x 10930.

Between the two pads, under the c track, the clean shot shows field (checked at 3.4x on
s2 in four shots; the other slices only at 1x in metal).

### Row R1 lower: 8-bit latch, upside down (traced)

Eight copies of `cdp4_lat` mirrored top to bottom (`lr_s0`..`lr_s7`: `dx,-1466 mx=8610
rot=180 o=8610,13132.5`, s7 dy -1467). Checked: cellcheck median 0.92-0.93 with 1-5
differing blocks of 132, metal overlay of s1, s2, s3, both layers of s7.

- Strobe `wr_r15`: the poly line at y 11837 along the bottom edge of the row. Its
  ends were not examined (drawn x 7600-10600).
- Data: the in tracks, `cdp3`'s bit lines `cdp3_bl_cK` (x 8465 + dx), contact at (8466 + dx, 11809), run **up**
  through the cell and on into the upper half of R1.
- Output: the d land's contact falls at (8712 + dx, 11772) under the top end of the b
  track, so `cdp4_b_sK` is the buffered output of this latch.
- The bus-tap track (x 8555) and, in s2..s7, the a track (x 8509) cross the cell with no
  contact, where the n and c tracks cross the row C cell. Both come from the upper half.
- s7's pull-downs end on a land under the ninth VSS rail (contact 10745,11652).

### Row D: 6-bit latch (traced)

Six copies of `cdp4_lat` (`ldr_s1`..`ldr_s6`, findcell dy 759, dx -392, 0, 390, 780,
1170, 1560), under slices s1..s6. Checked: cellcheck (median 0.90-0.93; the differing
blocks are the missing c and n tracks), metal overlay of s1, s2, s3 and s6, clean-shot
overlay of s6.

- Strobe `cdp4_ld6`: poly line y 13721 from a contact at (7946,13720), left of the s1
  cell, to the last cell (x 10330). A metal line goes down from the contact (x 7947,
  seen to y 13840).
- Data: in tracks `cdp3_g_c2`..`s6` (x 8465 + dx) start just above each cell's in
  contact and run down through the cell and **out of the bottom of the array**.
- Output: the buffered output (d land) of the cell under slice K goes up in metal to a
  poly contact at (8727 + dx, 13677); a poly link runs right from there to a contact
  under the foot of the c track of slice **K+1** (8511 + offset, 13677). So
  `cdp4_c_s2`..`s7` are the six bits of row D, one slice to the right of their cells.
- The cell under s6 takes its VSS from a piece of rail at x 10355 that starts at
  y 13694, below the link poly; the s7 rail was followed down only to row C.
- No n track, no selector, no pull-down in this row.

### Believed, not traced

A read-back multiplexer: two 8-bit and two 6-bit sources onto an 8-bit bus that leaves
to the right (towards the data pads), with the bus pulled low by `cdp4_rst`. The widths
fit the 6845's 14-bit registers split 6 + 8 (cursor R14/R15 and light pen R16/R17 are
the readable ones). Rows C (8 bit, data from the left) and D (6 bit, data from below)
would be one such pair, the R1 latch (8 bit) and the 6-bit a source above it the other. sel1..sel4 would then be the read enables of four
registers. None of this is traced; the sources of sel1..sel4, rst, ld and the in lines
lie left of x 7600.

### Row R1 upper: the comparator of the bus lines with R15 (run 3, 2026-11-19; traced)

Master slice s2; coordinates are s2's unless said. Read on a median picture of slices s2..s7
(`tools/composite.py r1u`), then checked on each slice (`tools/cellcheck.py`).

**Metal.** Only verticals cross the row: the VSS rail (x 8381-8427), the in track (x 8455-8478, `cdp3`'s
bit line `cdp3_bl_c#`: one metal, renamed from this block's placeholder at the refresh of 2026-11-20), the a track (x 8500-8522, `cdp3`'s line f: `cdp3_f_c#` =
`cdp4_a_s#`, alias; s2..s7), the bus-tap track (x 8545-8568; **its top end is at y 11062**: it starts in
this row) and the VCC rail (x 8597-8641). In and a have no contact in this row or in the R15 latch below.
In s0 and s1 a metal stands at the a position too (x 7729, x 8119) but is a stub from y 11068 to y 11843
with no contact at all (unconnected metal).

**Per slice, cell `cdp4_xr`** (7 transistors; identical in all eight slices):

    cdp4_xr_s#_nor = NOR(cdp4_bus_s#, cdp4_lr_s#_q)
    cdp4_xr_s#_ne  = NOT((cdp4_bus_s# AND cdp4_lr_s#_q) OR cdp4_xr_s#_nor)      = cdp4_bus_s# XOR cdp4_lr_s#_q

- The bus tap's metal has two contacts, each on a poly pad: (8556,11261), whose poly runs east along
  y 11261-11283 and turns south as a gate (x 8696-8722, y 11261-11370); and (8556,11449), whose poly runs
  west along y 11446-11468 to x 8478.
- `q` is the R15 latch's poly (`cdp4_lr_s#_q`, x 8723-8745 at the row's south edge), which runs up the
  east side: wide at y 11410-11450, then x 8742-8767 up to y 11275.
- Node `nor`: diffusion along the south edge (y 11474-11492 under the a and tap tracks, a column
  x 8620-8652 under the VCC rail, y 11455-11492 in the open to the east). Pull-downs to VSS: under the south
  tap poly (channel x 8488-8532; VSS north of it) and under `q` (x 8723-8745; VSS east of it, the strip
  x 8768-8795 under the next slice's VSS rail, which runs south to that slice's VSS contact). Load: the
  poly plate under the VCC rail (x 8596-8674, y 11385-11433) over the column from the VCC contact
  (8618,11345); the plate is tied to `nor` by a buried contact in the box (8672-8700, 11412-11452).
- Poly H (y 11392-11412, from x 8408 to the plate) carries `nor` west over a field island
  (x 8465-8590, y 11362-11420) to the gate of `ne`'s pull-down: it crosses `ne`'s west column
  (x 8425-8462), south of which is the VSS land with the rail's contact (8400,11455).
- Node `ne`: a land (x 8425-8535, y 11267-11289), its west column, and a strip y 11290-11306 east under
  the tap and the VCC rail (no contact) to the open, where it widens (x 8668-8795, y 11290-11360) and is
  crossed by the two gates in series: the bus tap's (x 8696-8722), then `q` (x 8742-8767), then the VSS
  strip. Load: the band y 11333-11357 from the VCC contact west to `ne`'s column under a poly
  (x 8483-8527) that is tied to `ne` by a buried contact at the west end of its pad (8438-8462, 11298-11320).
- `ne` drives the pull-down's gate: a buried contact in the box (8460-8482, 11248-11270) under the in
  track (no contact to that metal: `tools/textmap.py 8446 11236 8490 11276 3` shows no hole) takes it to
  the poly stub x 8458-8480 and poly B (y 11205-11228).

**The match line and its pull-downs** (cell `cdp4_xpd` in s1..s7; s0 by hand): a diffusion wire through
all eight slices (y 11104-11125 under each VSS rail, y 11114-11137 across the tracks, y 11108-11125 in the
open east of each slice). In s1..s7 poly A (y 11138-11162) with a leg down its east end (x 8630-8655) lies
over the wire's diffusion, with the source pocket (x 8448-8630, y 11163-11200) inside the L and the line on
its north and east: one transistor of W about 255. The pocket joins the VSS box (8387-8437, 11172-11232;
rail contact (8400,11197)) through the gap between the rail and the in track. The leg runs on south as
poly B's east end. In s0 poly A is shorter (x 7625-7822) and its leg (x 7802-7822) lies on field: W 145.

    bus_eq_r15 = NOR(cdp4_xr_s0_ne, ..., cdp4_xr_s7_ne)        high when all eight bus lines equal R15's q

- **Load**, in the open ground east of s0: a diffusion (7838-7968, 11160-11228) from a VCC contact
  (7850,11190), under a pad of s0's VCC rail, east under a poly gate (x 7903-7945) to a strip
  (x 7947-7968) that runs up into the line. The gate's head (7918-7945, 11105-11142) has a buried contact on
  the line: gate tied to the line.
- **West end**: the line runs on west of x 7600 as `busl`'s band to the pad with the contact (7555,11118)
  (`busl`, piece `kb`), a metal north along x 7555 and the poly row y 9450: gate 1 of `cdp3`'s NAND beside
  row C. **East end**: the line stops under the ninth VSS rail (x 10766), no contact.
- s7's VSS strip lies under the ninth rail and widens to a land with the rail's contact (10745,11458).

How the layers were told apart (the method, for the next reader): in the clean shot the gaps between the
metal tracks carry dark and green residue strips (x 8437-8448, 8483-8495, 8528-8537, 8572-8585 in s2) that
are not features, and the large khaki blocks east of each slice (x 8655-8755, y 11045-11250) are open field
(chip-2 stripped shot: red minus green about 0). Whether a diffusion crosses a gap was measured there in
the chip-2 stripped shot on the composite: field 0 or negative, diffusion and poly positive
(columns x 8445, 8489, 8533, 8583, 8666; the numbers are in `cache/scratch/cdp4/survey.md`).

**Believed, not traced**: the eight bus lines are address bits (`busl`: each ends on a row of the left
array, which holds the 14-bit address counter), R15 is the cursor's low byte, so `bus_eq_r15` would be
"address low byte equals cursor low byte", and the NAND in `cdp3` would combine it with the high six bits
compared in `cdp3`'s row A (`g_eq_r14`, not followed). Which bus line is which address bit, and whether
`q` is the latch's true or inverted sense, are not established here (the row C latch notes give the
cell's senses).

### Corner gate group: `cdp4_rst` = NOR of six select rows (run 2, 2026-11-19; traced)

Region x 7550-7870, y 13640-14055, left of row D. One gate, seven transistors:

`cdp4_rst` = NOR(`rsel14_buf`, `rsel13_buf_u`, `rsel17_buf`, `rsel12_buf_u`, `rsel16_buf`, `rsel15_buf`)

So the selector's nodes `cdp4_n_s#` are pulled low whenever none of the six rows is high. Four of
the rows are the read selects of R14-R17 (firm, joined through `busl`'s rows at x 7550). The other
two, y 13759 and y 13873 here (`busl`'s undrawn rows y 13744 and y 13852), are named as open joins
of `rsel13_buf` and `rsel12_buf` on the strength of `regs` run 3 (taps at (6492,13744) and
(6450,13852), read, not drawn): **believed**. If that holds, `cdp4_rst` is high exactly when none
of R12-R17 is being read.

Layout (unlike the cells of the rows):

- The s0 VSS rail (x 7599-7645) runs on south over a diffusion column x 7584-7655, y 13660-14055,
  with three contacts: (7610,13720), (7610,13838), (7610,13995).
  From y 14022 the rail widens west into a plate (about x 7488-7645, y 14022-14075 in both metal
  shots), which covers row 6's step block without a contact; drawn only for x 7550-7645, y 14024-14055.
- Six poly rows cross the column, two round each contact: centres y 13688, 13759, 13803, 13873,
  13958, 14028 (clean shot, column x 7635). East of the rail each row ends in a head x 7660-7715.
  Each is one pull-down, W about 128, L 23.
- The three diffusion pockets that carry the contacts (between rows 1-2, 3-4, 5-6) are closed on
  the east by three field islands at the heads' ends: closed loops x 7707-7727 y 13677-13775,
  x 7707-7737 y 13790-13893, x 7700-7728 y 13950-14045. So the pockets are VSS.
- Everything else inside the outline is one diffusion, the output: a strip above row 1
  (y 13660-13677), a neck between rows 2 and 3 (y 13773-13790), the big segment between rows 4 and
  5 (y 13885-13947) and a strip below row 6 (y 14042-14055), joined along the east by a bus
  x 7727-7747 (north of y 13780) and x 7738-7757 (south). The outline is a single thin line in the
  chip-2 shots: the diffusion's edge.
- Load: a diffusion box x 7775-7823, y 13825-13977 under the s0 VCC rail (which bends west at
  y 13547-13593 from x 7815-7859 to x 7772-7818 and runs on south), contact ring (7798,13850), gate
  poly y 13900-13937, W 48, L 37. The gate's west end is a tongue (7733-7765, 13912-13935) in a box
  (7722-7760, 13905-13945) on the bus: a buried contact, gate tied to the output. The load's
  source joins the bus by a passage y 13961-13972 at x 7750-7780: the outline comes south at
  x 7757, turns round at (7757-7775, 13958) and goes back north as the load box's west edge, so the
  bus and the load's diffusion are on the same side of one line (`px.py col 7760 13940 13990 3
  acid,acid1b,metal1`: dark at y 13955-13958 and 13973-13979, light at 13961-13970 in the chip-2
  stripped shot and in chip 1's metal shot).
- Output: the big segment goes on west of the column into the box (7537-7582, 13903-13940). The
  column's west edge is a dark line at x 7581-7584 at the pockets (y 13722, 13840, 13998) in both
  metal shots and the chip-2 stripped shot, and is absent at y 13920 (`px.py row 13920 7560 7604 3
  metal,metal1,acid`: flat 175/135/88 from x 7572 to 7590). In the box the poly of `cdp4_rst`
  (`busl`'s `P 7462,13906:7532,13927`) ends as a tongue: the same construction as the east box,
  mirrored. Drawn as a buried contact. This is reading (a) of AMB-038.

Why the diffusion is on the inside of the outline: the load's box has a metal contact and a gate
across it, so it is diffusion, and the outline's U-turn puts the bus on the same side. The
islands are closed curves inside it, so they are the other class.

## Ports

| Name | Layer | Where it crosses | Direction | What |
|---|---|---|---|---|
| `rsel14_buf` | poly | x 7600, y 12223 | from outside | select n <-> a |
| `rsel15_buf` | poly | x 7600, y 12481 | from outside | select n <-> b |
| `rsel17_buf` | poly | x 7600, y 12530 | from outside | select n <-> d (row C latch) |
| `rsel16_buf` | poly | x 7600, y 12786 | from outside | select n <-> c |
| `cdp4_rst` | poly | x 7600, y 12874; right end x 10705 | from outside | pulls every n low |
| `cdp4_ld` | poly | x 7600, y 12962; right end about x 10600 | from outside | row C latch strobe |
| `cdp4_bus_s0`..`s7` | poly | x 7600, y 12180, 12137, 12093, 12052, 12008, 11964, 11922, 11877 | unknown | per-slice line between row R1 and the left |
| `cdp4_bus_s0`..`s7` | poly | x 7600, y 13333, 13376, 13420, 13463, 13505, 13548, 13590, 13633 | from outside | data into the row C latch |
| `cdp4_n_s0`..`s7` | poly | x 10850, same y as `in` of the same slice | driven inside | selector output |
| `cdp4_a_s2`..`s7` = `cdp3_f_c2`..`c7` | metal | x 8511 + offset, y 11048 (the end of `cdp3`'s line f, y 11052) | from `cdp3`'s row A | selector input a (6 bits); crosses row R1 with no contact (run 3) |
| (bus tap) | metal | x 8556 + offset, top end y 11062 | inside | `cdp4_bus_sK` up to the comparator's two gate polys (run 3) |
| `cdp3_bl_c0`..`c7` (the in tracks of s0..s7) | metal | x 8466 + offset, y 11048 (the end of `cdp3`'s bit line) | from `cdp3` | data into the R15 latch; crosses row R1 upper with no contact (run 3) |
| `bus_eq_r15` | diffusion | x 7600, y 11095-11127 (`busl`'s band ends there) | driven inside | the comparator's match line, out to `cdp3`'s NAND (run 3) |
| `wr_r15` | poly | y 11837; believed to cross x 7600 (ends not examined) | from outside | R1 latch strobe |
| `cdp3_g_c2`..`s6` | metal | x 8073, 8465, 8855, 9245, 9635, 10025 at y 14059 (drawn end; continues down) | from outside (below) | data into the row D latch |
| `cdp4_ld6` | metal | x 7947, y 13840 (drawn end; continues down) | from outside (below) | row D latch strobe |
| `rsel14_buf`, `rsel17_buf`, `rsel16_buf`, `rsel15_buf` | poly | x 7550, y 13701, 13809, 13961, 14004 (`busl`'s row ends) | from outside | gates of the corner group's pull-downs 1, 3, 5, 6 |
| `rsel13_buf_u`, `rsel12_buf_u` | poly | x 7550, y 13751 and y 13873 (blocks at the step; the rows go on west as `busl`'s undrawn rows y 13744, y 13852) | from outside | gates of pull-downs 2 and 4; open joins |
| `cdp4_rst` | poly | (7532,13916), the end of `busl`'s poly | driven inside | output of the corner group |
| `vss` | metal | x 7622, 8013, 8404, 8795, 9185, 9574, 9964, 10355, 10746 at y 11480; x 8013..10355 at y 14062; 7622 drawn to y 13650 | - | rails |
| `vcc` | metal | x 7837, 8228, 8619, 9010, 9400, 9789, 10179, 10570 at y 11480; x 8228..10179 at y 14062; 7837 drawn to y 13530, 10570 to y 13650 | - | rails |

Seen left of the region at 0.68x (`cache/scratch/cdp4/left_edge.png`), not traced: a
bundle of about nine vertical metal lines at x 7330-7570. The poly lines from the array
run under it; contacts seen at about (7557,12170) and (7513,12128) (bus s0, s1),
(7513,12740), (7470,12868) (on or near rst), (7557,12905), (7557,12975) (near ld).

## Ambiguities

1. **Hold path of the latch** (8510-8655 x 13220-13265; the same structure as AMB-1 of
   `notes/blocks/rdp3.md`). Node a's poly ends on a buried contact (8511-8540 x
   13226-13258) to a small land under the n track. From there two stripes run right,
   under the VCC rail, to within a few pixels of the output land (q, left edge x 8653):
   S1 y 13226-13240 and S2 y 13247-13261. On the 8-cell composite both look salmon
   (poly-like) under the rail and both seem to start at the land. Readings: S1 a
   diffusion link (then a = q and the latch is a static pair that the in pass transistor
   overpowers, which would explain the separate buffer for d); or S2 the gate of a weak
   device between the lands; or no link (dynamic). Drawn: S1 as `?D` on node a stopping
   7 px short of the output land, S2 as unconnected poly `cdp4_<tag>_x2`. Would settle
   it: a sharper photo of 8540-8660 x 13215-13265, or the same answer in rdp3.
2. **Box in q's drain** (8702-8725 x 13141-13168): brown in the metal shots, dark and
   textured in the clean shot, no metal over it. rdp3 saw the same outline under a
   metal track and drew an uncertain contact. Not drawn here. If it were poly it would
   be an island with no effect.
3. **Width of the rst pull-down.** Diffusion above and below `cdp4_rst` is seen in the
   gap between the VCC rail and the d track (x 8651-8718) and under the d track
   (x 8727-8745); whether both parts cross the line was not settled. Drawn as one block
   x 8651-8745 (W 94). Connectivity is the same either way.
4. **Pull-down of d.** Drawn as the d land plus the wedge below it (down to the diagonal
   edge ending at (8733,13089)) crossing the n2 gate, W 85. The top edge of the crossing
   (y 13002) and the bottom edge (y 13089) are seen across the gate in three shots; a
   field band about 20 px wide separates this diffusion from q's (L1 output end and the
   drain below y 13124). An earlier reading took that band for a diffusion strap; the
   stripped shots show it field-coloured.
5. **LX gate tie.** The LX gate block (8604-8633) is joined to the buried contact at
   8657-8686 x 13010-13046 by a bar along the top (y 12990-13017) that lies under the VCC
   rail; seen in the clean shot at 5.9x, not in the metal shots.
6. Channel 2 pads: only s2 was checked at high zoom for the gap between the two pads.
7. The poly and diffusion of row D and of the R1 latch were not re-read shape by shape:
   the cells are placed on the strength of findcell, cellcheck and overlays (every
   contact of the cell lands on a contact in the photo). The ambiguities of the row C
   cell apply to them as well. In these two rows the n-track and c-track positions are
   used differently (see Logic).

8. **The two open rows of the corner group** (run 2). Rows 2 and 4 are drawn from x 7550 east
   only; west of that they are in `busl`'s region and not drawn there. Their names rest on `regs`
   run 3's reading of two taps. `tc2_sr_g`'s track crosses row 2 at (7145,13728-13749) (AMB-039):
   the group shows only that the row's east end is a gate and has no other contact, which does not
   decide that crossing.
9. **Marks not drawn** (run 2). A ring about 10 px across at (7558,13793) on the top edge of row 3,
   under `cdp4_ld`'s thin metal, in the clean shot only: neither chip-2 shot nor chip 1's metal
   shot has a contact ring there. A dark spot on the VCC rail at (7790,14026) and a green dot at
   (7803,13965) in the chip-2 metal shot, with nothing under them in the clean shot. The tan strip
   x 7835-7848 along the group's east side is the gap between two metals (`notes/layers.md`).

10. **Three buried contacts of the comparator cell are read from their look** (run 3): the box under the
   in track (8460-8482, 11248-11270: `ne` to the pull-down's gate poly), the box east of the plate
   (8672-8700, 11412-11452: the plate and poly H to `nor`), the pad's west end (8438-8462, 11298-11320: the
   gate of `ne`'s load to `ne`); and the head of the match line's load gate (7918-7945, 11105-11142). Each
   is a framed box with an inner outline at a poly end, as the latch cell's buried contacts are, and each
   is what its gate needs (without the first, poly A has no driver; without the second, poly H has none).
   Drawn firm.
11. **The VCC box of the match line's load** (run 3): a line at x 7875 between the contact's box and the
   diffusion west of the gate is read as the edge of the rail's pad (the rail bulges east to x 7878 for
   y 11160-11225 in the metal shot), not as a diffusion edge: it is one line, and the diffusion's top and
   bottom edges (y 11160, y 11228) run through it. Drawn firm as one diffusion.
12. **A tab of the match line under the top end of s0's tap track** (run 3, found by the review): only in
   s0 the line's diffusion runs up under the tap track to y 11074 in a framed box (7766-7788, 11074-11098;
   clean shot tan 195/170/129 at (7776,11084), pink field there in the other seven slices). Both metal
   shots show the track bright at y 11078-11088 between dark bars (y 11060-11076, 11091, 11100). Read as
   no contact by the tracer and by the reviewer: the bright stretch is the full track width, the clean shot
   has no hole (`tools/textmap.py 7752 11056 7800 11112 3 --acid`), and a contact would short
   `cdp4_bus_s0` to the comparator's output `bus_eq_r15`. Not conclusive: `busl`'s contact (7555,11118) on
   the same line shows no hole in the clean shot either. The tab is drawn; no contact is drawn.

## Not done

- (Done, run 3: row R1 upper.) Left from it: `g_eq_r14`, the NAND's other input (not followed); which
  address bit each bus line is; the three thin vertical metals east of the ninth VSS rail (x 10790-10910).
- Ends of `wr_r15` (poly, y 11837).
- Right of x 10600: the n lines' contacts beyond x 10850, thin vertical metals at
  x 10795-10905, the end of the s7 VCC rail.
- The VSS plate at the foot of the s0 rail west of x 7550 and south of y 14055 (a greenish patch in
  the clean shot at about (7500-7545, 14040-14065) is not looked at).
- The corner group's rails south of y 14050, and the wide metal x 7860-7910, y 13650-14100 east
  of the s0 VCC rail (with its band east along y 13650-13690), which is not followed.
- Below y 14060: where the six in tracks of row D, `cdp4_ld6` and the rails go (fan-out
  at y 14060-14700). The s0 VCC rail's bend below y 13540 and the wide metal at
  x 7700-7990, y 13650-14060 left of row D. The s7 VSS rail between y 13300 and 13694.

## Corrections (coordinator, from the handoffs of 2026-11-19, second batch)

- Ports, `cdp4_bus_s0`..`s7` ("unknown, per-slice line between row R1 and the left") and
  `cdp4_bus_s0`..`s7` ("from outside, data into the row C latch") **are the same eight nets** (`busl`, piece
  `ch1`): for each slice the channel-1 row and the channel-2 row are joined in the left bus field by a
  metal track between poly pads, and the same net ends on one poly row of the left array (s7 .. s1 at
  y 11488, 11922, 12442, 12984, 13397, 13874, 14351; s0 just south of `busl`'s region). The field holds
  no transistor; which end drives is not traced.

## Corrections (coordinator, from the handoffs of 2026-11-19, third batch)

- Ports, `rsel14_buf`, `rsel15_buf`, `rsel17_buf`, `rsel16_buf` (`cdp4`'s selects 1-4), `cdp4_rst`, `cdp4_ld` "from outside": the selects come from south of y 15000
  on tracks x 6538-6668 and each also feeds a gate band of the corner gate group; `cdp4_rst` from the
  corner gate group (believed); `cdp4_ld` from `bc1`'s strobe driver (`bc1_ld_a`, marked: AMB-038). The
  "contact near that strobe line at (7557,12975)" is the pad (7556,12983) (`busl`, piece `ctl`).
- Ports, `cdp3_g_c2`, `cdp3_g_c3` "from outside (below)": from `cdp3`'s row A cells, columns c2 and
  c3, by line g (`cdp3_g_c2`, `cdp3_g_c3`; `busl`, piece `d6`).
- `wr_r15` ("ends not examined"): the row does not enter the left bus field; its west end is at about
  x 7603-7640, y 11825-11850, under the metal x 7600-7645 (`busl`, run 6).

## Corrections (coordinator, from the handoffs of 2026-11-19, fourth batch)

- The strobe of row R1's lower half ("ends not examined") runs east as one poly row y 11824-11844 to a pad (11243,11830) on the write strobe of R15 (`regs` run 1, firm): **row R1's lower half is R15**. Its west end is at about (7603-7640, 11825-11850) (`busl` run 6).
- The four selects are the read selects of R14-R17 (`regs` run 2, firm: sel1 R14's, sel2 R15's, sel3 R17's, sel4 R16's): the four-way selector is the read multiplexer of R14-R17. Source a is what R14 reads, row R1's lower half is R15, latch row C is what R17 reads, latch row D what R16 reads. The corner gate group takes two more select rows, y 13744 and y 13852 (believed R13's and R12's read selects, by taps at (6492,13744) and (6450,13852): `regs` run 3).

## Review

### Run 2 (corner gate group)
Full review, 2026-11-19, of the piece as shipped in `c2927c3` (the corner gate group, 7
transistors), by a fresh Fable reviewer; images in `cache/scratch/cdp4/review-1/` (14).

Told to suspect: which side of the thin outline is diffusion and whether the three loops are
field islands; the passage from the bus to the load's source; the west box (buried contact, or a
contact from the thin metal x 7556); the east box; cuts in a row's poly and the joins of rows 1
and 6 to `busl`'s row ends; the ring (7558,13793); contacts missed on either rail; the VCC rail's
bend.

Checked and found correct (4x, two or more shots, with `px.py`, `textmap.py`, `railprof.py`,
`follow.py`, `opendiff.py`): the diffusion side and the islands (red minus green +20 to +28 on
pockets, bus, neck and strips against -12 to -20 on the islands and outside the outline in the
chip-2 stripped shot; the clean shot agrees); the bus continuous; the passage (the bus's east edge
line is absent at y 13961-13970 in both metal shots and the chip-2 stripped shot); the west box
(the column's west edge absent at y 13912-13930 in three shots; no hole, pad or ring: reading (a)
of AMB-038); the east box; six gates under the rail (`railprof.py` calls row 5 "poly over field",
but it has diffusion on both sides); the rows' joins to `busl`; the ring is in the clean shot
only; the three VSS contacts and the VCC contact are real and none is missed; the VCC bend.

Could not check: the thin metal x 7556 over the west box (dark at y 13900-13946 in both metal
shots: `busl`'s `?M`); row continuity across the 6-9 px edge line at x 7579-7582; rows 2 and 4
west of x 7550; the passage's last 6 px under the rail's edge line.

Finding 1, geometry only, confirmed (`px.py row 14031 7540 7650 8 metal,metal1`: metal from
x 7556 to 7644 in both shots; `px.py col 7570 14000 14060 6`: metal from y 14030): the VSS rail
widens west into a plate from y 14022, over row 6's step block, with no contact. Fixed: drawn as
`M 7550,14024:7645,14055` (the part inside the region). No connection changes:

- `tools/t.sh cdp4 sameconn.py c2927c3`: connections identical
- `.venv/bin/python tools/sameconn.py c2927c3`: connections identical

Round 1: no findings that change a connection.

### Run 3 (row R1 upper)

Round 1 (full review, 2026-11-19 21:45 -0600; a fresh Fable reviewer, images in
`cache/scratch/cdp4/review-2/`; commit before the round bae8129). Piece: row R1 upper, x 7540-10800,
y 11040-11500, with the stubs and tracks down to y 11843. Told to suspect: the four buried contacts, the
leg of poly A into poly B, the neck between the pocket and the VSS box, `q`'s poly into the latch, poly
H's west end and crossings, the load east of s0, the separation of `ne`'s strip from the VCC band, the
stubs and a tracks, and anything left out. It checked, at 4x or more and with profiles on the composite:
channel against field by poly colour (A, leg, B, H, the load gates, the plate, s0's leg), the neck (chip-2
stripped red minus green 13-23 against -1 to -7 on field), no VCC contact at (8619,11180), field between
`ne`'s strip and the VCC band at y 11310-11325, no contact of the in track at the box or the pad, both tap
pads, `q` across y 11495, the load's diffusion at x 7890, both stubs' ends (y 11844, both chips), both ends
of the row, the copies (`cellcheck.py`, three shots), the extraction, `unsure.py`, `opendiff.py`.

- Finding 1, **geometry only** (no connection changes as drawn): an undrawn diffusion tab of the line
  under the top end of s0's tap track (7765-7795, 11065-11098), with the question whether the track has
  a contact on it; the reviewer reads no contact. Confirmed by the tracer (9x views `f1-*.png`, text map):
  the tab is there, no contact is read. Drawn (`D 7766,11074:7788,11114`), recorded as Ambiguity 12.
- Finding 2, **geometry only**: the pad `P 8466,11297:8519,11323` over-covered its north-east corner (at
  x 8512 the poly is y 11316-11325 only). Fixed: `P 8466,11297:8506,11323` and `P 8500,11314:8521,11325`;
  field either way.
- Not checkable by the reviewer: the four buried contacts beyond their look in both chips (Ambiguity 10);
  a 10 px dark stretch between the north tap pad's west edge and `ne`'s land (x 8538-8548) with no field
  gap resolvable (the pad is drawn 10 px clear of the land; a contact there would not change a net, both
  being on different nets only if apart: they are drawn apart, as the composite's field at x 8533,
  y 11240-11258 and the land's edge at x 8540 show); the a tracks and stubs over y 11500-11795 sampled only.

`tools/t.sh cdp4 sameconn.py bae8129`: connections identical.
`.venv/bin/python tools/sameconn.py bae8129`: connections identical.

Round 1: no findings that change a connection.

## Corrections (coordinator, from the handoffs of 2026-11-20)

- Row R1 upper, "Believed, not traced" and Not done ("`g_eq_r14`, the NAND's other input (not followed)"): followed by `cdp3` (row A): it is the match line of the comparator of line g (`cdp3_g_c#`) with R14.
- The strobe polys `wr_r15` (y 11837), `cdp4_ld` and `cdp4_ld6` are drawn as straight lines; in `cdp3`'s copy of the same latch cell the strobe `wr_r14` is a serpentine (field under each bit line and a-track metal at the band's height, the band joined through each cell's loop). Probably the same here; geometry only as far as seen (Re-read item R48).
