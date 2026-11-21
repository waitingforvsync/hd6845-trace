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

Run 4 (2026-11-21 14:07 -0600): **the read bus** (x 10840-11230, y 10343-18305; wiring only, 16 contacts, no transistor, no
uncertain item): the selector's eight output rows `cdp4_n_s0`..`s7` each end east of the array on a pad
with a contact on one thin metal track, and the same track starts on the end pad of `cdp3`'s bus N row
`cdp3_n_c#` of the same column: **R12-R17 are read onto one 8-bit bus** (`cdp3_n_c#`, with `cdp4_n_s#` an
alias). Each track runs on south to a corner in the bottom bus field and turns east. With every file
loaded: 2517 nets, 4782 transistors, 0 errors, 0 warnings. See "The read bus" under Logic.

Run 5 (2026-11-21 14:28 -0600): **the read bus, columns 1-7, east along the bottom bus to x 16000** (wiring only, 42 pads with
contacts, 21 poly hops, no transistor, no uncertain item): each of the seven horizontals runs east to a
pad, hops in poly under the vertical trunks, climbs a diagonal to its row, and hops twice more under
rails; no tap on the way. With every file loaded: 2517 nets, 4796 transistors, 0 errors, 0 warnings. See
"The read bus, east" under Logic.

Run 6 (2026-11-21 14:48 -0600): **the read bus, columns 1-7, from x 16000 to their turn north** (wiring only, 13 pads with
contacts, seven poly columns, no transistor, no uncertain item): each row ends on a pad, a poly column goes
north under the bundle of horizontal metals, and columns 2-7 step east and come up on six metal tracks
x 16580-16798 that go on north; column 1's column runs into a gate group at about (16060-16230,
17290-17480). With every file loaded: 2517 nets, 4796 transistors, 0 errors, 0 warnings. See "The read
bus, the turn north" under Logic.

Run 7 (2026-11-21 15:06 -0600): **the read bus's six tracks north to their ends: column 7 is data bit 0** (wiring only, five
pads with contacts, no transistor, no uncertain item). Column 7's track turns east onto the metal `dbus`
draws from the pad of `dbus_do0_in`, the gate of D0's output chain: **`d0_out_n` = NOT `cdp3_n_c7`** in the
extraction (firm). Columns 2-5 end on pads in the staircase beside `dbus`'s `d5_out_n`..`d2_out_n` pads,
each with a poly row west toward a column of five units; column 6 ends on a pad whose poly goes round to
the fifth unit. With every file loaded: 2516 nets, 4796 transistors, 0 errors, 0 warnings. See "The read
bus, north to the output units" under Logic.

Run 8 (2026-11-21 15:32 -0600): **the data output inverters of bits 5-1** (x 16480-16800, y 15800-16460, in `bd2`'s region;
cell `cdp4_ro`, five copies, 10 transistors): **`d5_out_n` = NOT `cdp3_n_c2`, `d4_out_n` = NOT `cdp3_n_c3`,
`d3_out_n` = NOT `cdp3_n_c4`, `d2_out_n` = NOT `cdp3_n_c5`, `d1_out_n` = NOT `cdp3_n_c6`** (firm), with
run 7's `d0_out_n` = NOT `cdp3_n_c7`: the read bus's column K is data bit 7 - K for K = 2..7, and each
`d#_out_n` line is drawn by `dbus` to its pad cell. Also the thin metal of `dbus_le` on south through the
units, marked uncertain over four output boxes (Ambiguity 15). With every file loaded: 2517 nets, 4807
transistors, 0 errors, 0 warnings. See "The data output inverters" under Logic.

Not traced: the rest of the wiring right of x 10600 (the two thin metals x 10809 and x 10853, the rails'
ends) and below y 14060.

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
| 10343-18305, x 10840-11230 | the read bus: eight thin metal tracks east of the array, from `cdp3`'s bus N pads through the selector outputs' pads to their corners in the bottom bus | 8 | traced (run 4) |

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

### The read bus (run 4, 2026-11-21; traced)

East of the ninth VSS rail ten thin vertical metals (12 px wide, pitch 43.5) run straight through the
bus field: x 10809 and x 10853 (two other nets, not drawn) and the eight read-bus tracks x 10897, 10940,
10984, 11027, 11070, 11113, 11157, 11201. The same centre at every cut from y 10150 to y 17450
(`tools/busl_mdrawn.py h Y 10700 11520`, 29 cuts). Per column / slice K (c7 = s7 on the track x 10897,
c0 = s0 on x 11201):

| K | `cdp3`'s bus N row, pad (the track's top end) | `cdp4`'s n row, pad (the track runs through) | corner | horizontal |
|---|---|---|---|---|
| 7 | y 10361, (10894,10360) | y 13633, (10896,13636) | (10897,18298) | y 18298 |
| 6 | y 10404, (10938,10404) | y 13590, (10939,13592) | (10940,18256) | y 18256 |
| 5 | y 10447, (10982,10446) | y 13548, (10983,13549) | (10984,18213) | y 18213 |
| 4 | y 10490, (11025,10490) | y 13505, (11027,13507) | (11027,18170) | y 18170 |
| 3 | y 10535, (11068,10534) | y 13463, (11070,13462) | (11070,18128) | y 18128 |
| 2 | y 10577, (11112,10577) | y 13420, (11113,13420) | (11113,18085) | y 18085 |
| 1 | y 10621, (11156,10621) | y 13376, (11156,13377) | (11157,18040) | y 18040 |
| 0 | y 10664, (11199,10664) | y 13333, (11199,13333) | (11201,17910) | y 17909 | 

**Column 0 is drawn in `trace/regs.txt`** (piece `n0` of `regs` run 6, Kieran Connell's session, merged to main
while this run was in review): the same track, the same two pads and row ends, read independently, and on
east along y 17908 to the inverter `regs_w17462` = NOT `cdp3_n_c0`. This package's copy of column 0 (reviewed
in round 3 with the rest) was taken out again before the merge, so that the wire is drawn once; columns 1-7
are drawn here.

- **North end.** `cdp3` draws its bus N rows to x 10850; each runs on east as one poly row under the
  tracks west of its own and ends in a pad about 34 px square with a contact (ring and bright centre in
  both metal shots, green hole in the clean shot: `cache/scratch/cdp4/padc.py`). The track starts there:
  no metal north of any pad (`tools/tl5_tracks.py v X 10300 13760`; `tools/follow.py X 13290 N` ends on
  each pad). The diagonals north-east of the staircase are `regs`' and `wrs`' write strobe lines.
- **`cdp4`'s staircase.** Each selector output row runs on east of x 10850 to a pad of the same kind; the
  track has a 17 px ring on each side of the bright centre and metal directly beyond both rings
  (`tools/textmap.py 11176 13306 11228 13362 3`), so it runs through.
- **No other contact.** Every contact candidate `tools/follow.py` lists on the eight tracks (about 110)
  was read as three strips, along the track in both metal shots and in the clean shot
  (`cache/scratch/cdp4/cand.py`): none has a pad's pattern (bright, a dark ring of 12-15 px, a bright
  centre, a ring, bright; the metal widened). The dark bars across the tracks are edges underneath:
  `wr_r15`'s poly row (y 11819-11851), the two long edges of the diffusion-coloured rectangle of
  AMB-040 (y 11919-11927, 12178-12186; the tracks cross it, tan under them, with no contact), the n
  rows, three more poly rows that cross all eight tracks (y 10700-10722, `cdp3`'s row H line;
  y 14558-14576; y 16380-16397: named by the review), and the poly diagonals of the bottom bus
  (y 17500-18300). So the rows `cdp4_n_s#` pass under
  the lower-numbered tracks, and the tracks over everything else, without contact.
- **South end.** Nested corners, no pad: each track turns east onto a horizontal metal (drawn to
  x 11230). `tools/follow.py 10940 13700 S` runs column 6's on east to x 12810. Column 0's track turns
  east at (11201,17910) onto the bottom bus metal y 17909, which `regs` draws to the gate of its inverter.

    read bus bit of column K = cdp3_n_cK = cdp4_n_sK
    pulled to: cdp3_cq_cK (rsel12_buf; VSS in c0, c1), cdp3_hq_cK (rsel13_buf), cdp3_f_cK (rsel14_buf;
    VSS in s0, s1), cdp4_b_sK (rsel15_buf), cdp4_c_sK (rsel16_buf; VSS in s0, s1), cdp4_d_sK (rsel17_buf),
    and to VSS by cdp4_rst (while none of R12-R17 is read)

**Believed, not traced**: the eight horizontals lead to the data output path (column 0's reaches an
inverter of `regs`); with `cdp3`'s bit line of column 2 being `db_b5`, column K would be data bit 7 - K.

### The read bus, east along the bottom bus (run 5, 2026-11-21; traced)

Columns 1-7 only (`cdp3_n_c1`..`c7`); column 0 is `regs`' piece `n0`, which runs one row pitch further
north by the same kind of route to its inverter. Each line, from its port of run 4 at x 11230:

| K | horizontal y | hop 1: pads (poly row between) | diagonal (45 degrees, 260 px) | row y | hop 2: pads | hop 3: pads |
|---|---|---|---|---|---|---|
| 1 | 18038 | (12851,18038) - (13174,18035) | (13284,18039) - (13543,17779) | 17777 | (14456,17776) - (14672,17777) | (15712,17776) - (15926,17777) |
| 2 | 18082 | (12808,18082) - (13219,18079) | (13302,18082) - (13562,17822) | 17821 | (14499,17821) - (14716,17821) | (15754,17821) - (15969,17821) |
| 3 | 18125 | (12853,18124) - (13174,18120) | (13324,18125) - (13583,17866) | 17864 | (14457,17864) - (14673,17864) | (15712,17864) - (15926,17864) |
| 4 | 18168 | (12808,18168) - (13219,18163) | (13346,18169) - (13605,17909) | 17908 | (14500,17908) - (14715,17907) | (15755,17906) - (15969,17906) |
| 5 | 18211 | (12851,18210) - (13174,18208) | (13368,18212) - (13627,17953) | 17951 | (14456,17951) - (14671,17951) | (15711,17951) - (15926,17951) |
| 6 | 18255 | (12807,18254) - (13219,18249) | (13390,18256) - (13650,17996) | 17994 | (14499,17994) - (14715,17994) | (15755,17994) - (15969,17993) |
| 7 | 18298 | (12852,18298) - (13174,18296) | (13412,18298) - (13672,18039) | 18037 | (14457,18037) - (14672,18037) | (15713,18037) - (15926,18039) |

- **The horizontals** (thin metal, 12 px): `tools/follow.py 11400 Y E` ends each on its pad; the 68 contact
  candidates it lists were put through the pad test (`cache/scratch/cdp4/candh.py`): no ring pattern in
  either metal shot at any (five small clean-shot specks).
- **Hop 1**, under the vertical trunks (x 12880-13130): seven straight poly rows, each between a west pad
  (x 12808 or 12852, alternating) and an east pad (x 13219 or 13174) at the same y; read in the clean shot
  at 2.9x (`hop1_c.png`): no row steps a track.
- **Diagonals**: east of its pad each line runs east, climbs 260 px north-east and runs east on its row;
  the ends are from a walk along the metal (`cache/scratch/cdp4/track.py X0 Y0 14440 60`, which cannot
  leave a line: it re-centres within 7 px every 2 px) and an overlay (`ov5d.png`). North-west of them, in
  the same fan, are `regs`' three lines (column 0's and two write/select lines).
- Crossings named by the review (round 4), none with a pad, ring or pits: a poly column x 12732-12756 under
  all seven horizontals; a poly diagonal under column 1's metal at x 11222-11265; and **a diffusion
  rectangle x 11513-11728, from y 18278 southwards, under column 7's metal, in no trace file** (clean shot
  191/173/127 under the metal): a lead for `busb`.
- A poly column x 13706-13730 crosses under all seven rows (y 17750-18060): the rows are bright between
  its two edge bars, with no pad: no tap (`x13718.png`, three shots at 3.2x; tracing guide, trap 15). Whose
  it is was not followed.
- **Hop 2**, under a thin metal x ~14535 and a rail x 14580-14620: straight rows between pads x 14456 /
  14499 and x 14672 / 14716. **Hop 3**, under a wide rail x 15790-15880: pads x 15712 / 15755 and x 15926 /
  15969. Under both rails the rows lie on field (`tools/railprof.py 15800 15870 17740 18060` and
  `14585 14615 17740 18060`: "poly over field" for all seven, field between; its one "diffusion" band,
  y 17795-17807 under the second hop's rail, is a greenish patch 16 px wide in the clean shot between two
  rows, not under either: `tools/px.py row 17801 14560 14650 8`): no transistor.
- Drawn to x 16000 (ports). East of that (`tools/follow.py 16010 Y E`, not drawn): column 1's metal ends at
  (16148,17777), column 2's at (16516,17820), and columns 3-7 turn north at corners x 16558, 16602, 16646,
  16690, 16732; `regs`' inverter output (NOT column 0) runs east on the row y 17735 just above.

### The read bus, the turn north (run 6, 2026-11-21; traced)

East of x 16000 the seven rows fan into a staircase:

| K | row y | corner | end pad (contact) | poly: column x, arm y, column x | top pad (contact) | track north |
|---|---|---|---|---|---|---|
| 1 | 17777 | - | (16145,17776) | x 16148 north to y 17480 (drawn end) | - | - |
| 2 | 17821 | - | (16513,17820) | x 16517, arm y 17470 | (16579,17473) | x 16580 |
| 3 | 17864 | (16557,17864) | (16557,17775) | x 16560, arm y 17517, x 16626 | (16623,17427) | x 16624 |
| 4 | 17907 | (16601,17907) | (16601,17820) | x 16605, arm y 17558, x 16671 | (16666,17473) | x 16667 |
| 5 | 17951 | (16643,17951) | (16643,17775) | x 16650, arm y 17629, x 16711 | (16709,17427) | x 16711 |
| 6 | 17994 | (16687,17994) | (16687,17820) | x 16693, arm y 17672, x 16758 | (16752,17473) | x 16755 |
| 7 | 18038 | (16730,18038) | (16730,17776) | x 16735, arm y 17714, x 16802 | (16796,17430) | x 16798 |

- Columns 1 and 2 run straight east onto their pads; columns 3-7 turn north at nested corners and end on
  pads at y 17775 / 17820 (the metal overlay `ov6_m.png`).
- **The metal row y 17729-17741 just north of the y 17775 pads is another net** (`regs`' inverter output,
  NOT column 0) and is not joined to them: between it and each pad's ring the two metal shots read open poly
  (155-179/91-112/44-68 in chip 2, 127-155/74-100/36-50 in chip 1 at y 17752-17760, `tools/px.py col X
  17724 17796 4 metal,metal1` at x 16145, 16557, 16643, 16730), which is the pad's poly column going north.
  `tools/follow.py` bridges that gap and runs columns 3 and 7 onto that row (tracing guide, trap 30).
- **The poly columns** pass north under four horizontal metals (y about 17605, 17648, 17691 (`trunks`), 17735
  (`regs`)) with no contact (the metals are bright over them, no ring). Each of columns 3-7 steps east on an
  arm that lies in the gap between two of those metals (or, columns 2-4, north of them under a wide metal
  band y 17505-17565) and goes on north to its top pad. Read in the clean shot at 3x (`z6_c.png`, `z6_c7.png`,
  overlay `ov6_c.png`), in the chip-2 metal and stripped shots at 2x (`z6_ma.png`), and the three arms in
  gaps by colour: `tools/px.py row Y 16630 16800 8 metal,metal1,acid1b` at y 17628, 17672, 17715 gives
  orange poly (chip 2 about 166/113/56) from x 16646 to 16710, from x 16686 to 16762 and from x 16726 on
  east, and field between (172/143/79), as drawn.
- **Top pads**: six pads in two rows (y 17473 and y 17427), each with ring and bright centre in both metal
  shots, each the south end of a thin metal track that goes north (`tools/follow.py X 17380 N --max 600`
  runs every one to y 16780 and beyond). Drawn to y 17380 (ports).
- **Column 1** is different: its poly column x 16139-16157 runs north beside `trunks`' metal x 16163-16178
  (two edge lines at x 16138 and x 16156 with orange between and plain field west of it at y 17500 and
  y 17600: `tools/px.py row`), to y 17465, where it **turns west** as a band y 17463-17485, orange in both
  metal shots from x 16150 to x 16084 (found by the review, round 5: `tools/px.py row 17474 16060 16166`;
  plain ground north of the corner). Drawn to y 17480 (port, on the corner); the band west of x 16139 and
  what it reaches are not drawn. North of it is a gate group (a diffusion area x 16075-16150, y 17360-17410,
  poly rows y 17325-17345 and y 17413-17437, a framed box at (16100-16125, 17415-17445); `z6_c1t.png`).

### The read bus, north to the output units (run 7, 2026-11-21; traced)

| K | track | corner east | corner north | end pad (contact) | poly from the pad |
|---|---|---|---|---|---|
| 2 | x 16580 | (16580,16540) | (16818,16540) | (16818,15866) | a row west, y 15866 |
| 3 | x 16624 | (16624,16582) | (16861,16582) | (16861,15996) | a row west, y 15996 |
| 4 | x 16667 | (16667,16626) | (16905,16626) | (16905,16128) | a row west, y 16128 |
| 5 | x 16711 | (16711,16672) | (16948,16672) | (16948,16257) | a row west, y 16257 |
| 6 | x 16755 | - | - | (16752,16713) | east to x 16800, north on x 16790-16810 to y 16384, west |
| 7 | x 16798 | (16798,16714) | - | - (joins `dbus`'s metal at x 16950) | - |

- **The tracks** run north from their top pads without a break, a pad or a crossing
  (`tools/tl5_tracks.py v X Y0 17400` for all six: no stretch of 8 px without metal in both chips except
  one 9 px bar on column 4 at y 17259-17267 and column 6's pad; no hole in the clean shot).
- **Columns 2-5** turn east at nested corners and north again (`tools/follow.py X 17380 N`; overlay
  `ov7_cor.png`). The north legs are crossed by the poly rows of the staircase, as pairs of edge bars
  22 px apart (`tools/tl5_tracks.py v 16818 15850 16535`: rows at y 15954, 15998, 16084, 16126, 16214, 16259,
  16344), with a hole in the clean shot only at each track's own end pad. Each end pad (ring, bright
  centre, hole: `r7_end.png`, 2.5x both shots) carries a poly row that runs WEST under the tracks west of
  it and under the thin metal x 16762-16780 (`dbus_le`), toward the column of units at x 16600-16790. Drawn
  to x 16790 (ports).
- **The end pads interleave with `dbus`'s output pads** on the same track positions: `d5_out_n`
  (16864,15827), `d4_out_n` (16907,15957), `d3_out_n` (16950,16087), `d2_out_n` (16993,16217), `d1_out_n`
  (17034,16343), each with its own poly row west into the same units. Between an output pad and the read
  bus pad 170 px south of it on the same track position there is no metal (two metals end to end on one
  track position: tracing guide, trap 33). **Believed, not traced**: each unit is an inverter from the read
  bus row just south-west of an output pad to that output (column 2 to `d5_out_n`, 3 to `d4_out_n`, 4 to
  `d3_out_n`, 5 to `d2_out_n`, 6 to `d1_out_n`), which would make column K data bit 7 - K, as columns 7
  (below) and the data bus bit lines say.
- **Column 6** ends on a pad (16752,16713) south of the corners. Its poly leaves east (y 16700-16724; orange
  in both metal shots between the pad's ring and column 7's metal, salmon in the clean shot), passes under
  the corner of column 7's track, runs north as a column x 16790-16810 under the four horizontals of
  columns 5, 4, 3, 2 (pairs of edge bars at x 16783-16798 and 16805-16815 on each: `tools/tl5_tracks.py h`)
  to y 16384 and turns west as a band y 16372-16395 (`r7_c6.png`). Drawn to x 16780 (port).
- **Column 7** turns east at (16798,16714) and runs along y 16714 onto the metal that `dbus` draws from the
  pad (16993,16451) of `dbus_do0_in` (`M 16993,16440 y16712 x16950`; `dbus`'s notes had followed it "west to
  x 16795, then south to (16797,17434)"). One metal, no pad between: `@alias cdp3_n_c7 dbus_do0_in`.

    d0_out_n = NOT cdp3_n_c7        (dbus's pull-down t at (17378,16454); firm)

So **the read bus's column 7 is data bit 0**: with `cdp3`'s bit line of column 2 being `db_b5`, the datapath's
column K is bit 7 - K for writing, and for reading at least in column 7.

### The data output inverters (run 8, 2026-11-21; traced)

Five copies of one cell, `cdp4_ro`, at pitch 130 (`tools/findcell.py 16480 15925 16800 16055`, clean shot:
dy -130 (0.90), +130 (0.94), +261 (0.92), +391 (0.93); `tools/cellcheck.py cdp4_ro`: median 0.96-0.98 in the
clean and the metal shot, 0-3 differing blocks of 35), between the VCC rail x 16491-16540 and the VSS rail
x 16666-16712, which `dlat` draws from the north to y 15790 and which run on south through the units (drawn
here to y 16440 and to the VSS rail's end at y 16446; the VCC rail goes on to about y 16478). Master: unit
`u2`, the one whose output box takes `d4_out_n`. Read on the median picture of the five
(`tools/composite.py cdp4_ro 16470,15915:16810,16065 --offsets "0,-130 0,130 0,261 0,391"`; the metal
composite is the clear one: `u_w6.png`, `u_e6.png`), edges measured by ten cuts (`tools/px.py ... --comp
cdp4_ro`), overlay on the single shots (`ov8_u2.png`, `ov8_u1.png`, `ov8_u5.png`).

    d(7-K)_out_n = NOT cdp3_n_cK        K = 2 (unit u1) .. 6 (unit u5); 2 transistors each

Coordinates of the master:

- **Load.** A diffusion box (16497-16547, 15950-16012) under the VCC rail with the rail's contact
  (16510,15978). In unit u1 only, the box runs on north to y 15772 and has a second contact of the rail
  at (16512,15794) (review, round 7; drawn outside the cell). A strip leaves it east (y 15954-15982) under the poly plate (16548-16603, 15937-15998): in
  the metal shots the plate is three orange bands with the strip's two edge lines across it (y 15951-15956,
  15979-15985). W/L 28/54.
- **Output node.** East of the plate the strip (y 15959-15979, pinker than the field beside it in the
  metal composite: 175/128/81 against 164/142/82) runs east to the VSS rail and under it. A branch
  (x 16614-16632) goes south from it to y 16025 and west into a small heavy-outlined box
  (16581-16611, 16002-16027), where the plate's tab (x 16585-16607, from the plate's foot) ends: the buried
  contact that ties the load's gate to the output.
- **Pull-down.** Under the VSS rail a diffusion column x 16683-16722: the output strip above (y 15960-15984),
  the gate (the read bus row, salmon, y 15985-16007, its west end at x 16657) and the source box below
  (y 16010-16056) with the rail's contact (16697,16032; ring and bright centre in the metal composite,
  specks in the clean one). W/L 42/22 (the column's edges at x 16680 and x 16722: review, round 7). West of the column, under the rail's west part, the clean shot is
  pink below the gate (field): one transistor.
- **Output.** East of the rail the strip (y 15960-15977) runs into a framed box (16746-16782, 15948-15976),
  the buried contact with the poly row of `d#_out_n`, which `dbus` draws from its pad to within 30 px west
  of the pad; the rows are drawn on here to the boxes (y 15824, 15954, 16085, 16215, 16345), under the read
  bus tracks they cross (no contact: reviewed with run 7).
- The read bus rows of run 7 (ports at x 16790, and column 6's band at (16780,16384)) are the gate rows.

**The thin metal of `dbus_le`** (x 16768-16782) comes from the north (`dlat` draws it to (16774,15935),
over unit u1's box) and runs on south over the other four output boxes. Drawn to y 16450, uncertain over
each box: Ambiguity 15.

**Believed, not traced**: with `dpad`'s cells (the pin is the inverse of `d#_out_n` while `d_hiz` is low),
pin D(7-K) carries the read bus's column K in true sense. Columns 1 and 0 (bits 6 and 7) are not joined to
`d6_out_n`, `d7_out_n` yet (`regs`' inverter on column 0; column 1's gate group).

### Corner gate group: `cdp4_rst` = NOR of six select rows (run 2, 2026-11-19; traced)

Region x 7550-7870, y 13640-14055, left of row D. One gate, seven transistors:

`cdp4_rst` = NOR(`rsel14_buf`, `rsel13_buf`, `rsel17_buf`, `rsel12_buf`, `rsel16_buf`, `rsel15_buf`)

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
| `d5_out_n`..`d1_out_n` | poly | onto `dbus`'s rows at x 16822, 16870, 16912, 16957, 16957 (y 15824, 15954, 16085, 16215, 16345) | driven inside | the outputs of the data output inverters (run 8) |
| `dbus_le` | metal | x 16775, y 15930 (onto `dlat`'s end) and y 16450 (drawn end; goes on south) | from outside (believed from the south) | the data input latches' enable, passing through the units (run 8; uncertain over four boxes) |
| `vcc`, `vss` | metal | x 16515 and x 16689 at y 15780 (onto `dlat`'s rails); `vcc` drawn to y 16440 (goes on to about y 16478), `vss` ends at y 16446 | - | the units' rails |
| `cdp3_n_c7` (= `cdp4_n_s7` = `dbus_do0_in`) | metal | (16950-16962, 16714): onto `dbus`'s metal | driven inside | the read bus, column 7 = the gate of D0's output chain (run 7) |
| `cdp3_n_c1` (= `cdp4_n_s1`) | poly | x 16148, y 17480 (drawn end, on the corner where the column turns west as a band y 17463-17485, seen to x 16084) | driven inside | the read bus, column 1 (runs 4-6) |
| `cdp4_n_s0` | poly | x 10850, y 13333 | driven inside | selector output of slice 0: on east to its pad (11200,13330) on the read bus track of column 0, drawn by `regs` (piece `n0`) |
| `cdp4_a_s2`..`s7` = `cdp3_f_c2`..`c7` | metal | x 8511 + offset, y 11048 (the end of `cdp3`'s line f, y 11052) | from `cdp3`'s row A | selector input a (6 bits); crosses row R1 with no contact (run 3) |
| (bus tap) | metal | x 8556 + offset, top end y 11062 | inside | `cdp4_bus_sK` up to the comparator's two gate polys (run 3) |
| `cdp3_bl_c0`..`c7` (the in tracks of s0..s7) | metal | x 8466 + offset, y 11048 (the end of `cdp3`'s bit line) | from `cdp3` | data into the R15 latch; crosses row R1 upper with no contact (run 3) |
| `bus_eq_r15` | diffusion | x 7600, y 11095-11127 (`busl`'s band ends there) | driven inside | the comparator's match line, out to `cdp3`'s NAND (run 3) |
| `wr_r15` | poly | y 11837; believed to cross x 7600 (ends not examined) | from outside | R1 latch strobe |
| `cdp3_g_c2`..`s6` | metal | x 8073, 8465, 8855, 9245, 9635, 10025 at y 14059 (drawn end; continues down) | from outside (below) | data into the row D latch |
| `cdp4_ld6` | metal | x 7947, y 13840 (drawn end; continues down) | from outside (below) | row D latch strobe |
| `rsel14_buf`, `rsel17_buf`, `rsel16_buf`, `rsel15_buf` | poly | x 7550, y 13701, 13809, 13961, 14004 (`busl`'s row ends) | from outside | gates of the corner group's pull-downs 1, 3, 5, 6 |
| `rsel13_buf`, `rsel12_buf` | poly | x 7550, y 13751 and y 13873 (blocks at the step; the rows go on west as `busl`'s undrawn rows y 13744, y 13852) | from outside | gates of pull-downs 2 and 4; open joins |
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
   run 3's reading of two taps. `ck_out`'s track crosses row 2 at (7145,13728-13749) (AMB-039):
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

13. **The corner of column 7's track lies over another net's poly corner** (run 4). A poly row comes from
   the west along y 18288-18306, turns south under the track's corner (10897,18298) and runs as a column
   x 10888-10908 to the pad (10900,18470), which `trunks` draws on `rst_ck`'s link. Read as no contact at
   the corner: the metal is continuous round it with no ring and no widened pad, and the clean shot under
   it is salmon (red minus green 48-72) with no hole, where the pad (10896,13636) of the same track has
   ring rows and a centre of 16-32 (`tools/textmap.py 10868 18270 10926 18330 3 --acid` against
   `10868 13608 10926 13664`). A contact would short the read bus to `rst_ck`. The poly is not drawn (not
   this package's net; a lead for `busb`).
14. **Marks not drawn** (run 4). Chip-1 dirt across the tracks at (10940-11030, 15590-15600), (11070,15638),
   (11114,15655), (11158,15688), (11202,15724) (clean shot all green and chip 1's metal shot dark there,
   chip 2's metal bright); a particle in the clean shot at (11140-11215, 12215-12295); two rings about
   10 px across in the clean shot only at (11113,12921) and (11156,12928), on field under tracks 2 and 1
   (no pad, no ring in either metal shot); a dark patch on chip 2's metal at (11098-11122, 12885-12900).
   From the review (round 3): more 8-15 px clean-shot rings on field under tracks at (10897,12808),
   (10984,12847), (10984,13245), (11113,12322), (11113,13235), (11201,12808); chip-1 stain patches at
   (11157,15356-15412) and (11201,15204-15264); blemishes in both chips, 7-15 px apart between them, at
   (10897,12390), (10984,13937), (11201,15240), with field under each (not breaks). Under the chip-1 stain
   (y 15530-15790) the tracks' continuity rests on chip 2 alone.

15. **`dbus_le`'s thin metal over the output boxes** (run 8). The metal x 16768-16782 is dark in both metal
   shots for 53-60 px over each output box (y 15937-15990, 16067-16124, 16197-16255, 16323-16383;
   `tools/tl5_tracks.py v 16771 15800 16520`) and bright between (y 15990-16067, 16124-16197, 16255-16323,
   16383-16456); the clean shot is greenish under it at each box. Readings: one metal that passes over the
   boxes (the tracing guide's trap 27; `dlat` draws it so over unit u1's box); or pieces. No contact onto a
   box is read (no pad; a contact at every box would short five outputs to the latch enable). Drawn `M`
   between the boxes and `?M` over them, so `dbus_le` here is joined to `dlat`'s piece only through
   uncertain items (`tools/unsure.py` lists it). What would settle it: its far end (south of y 16450, toward
   the NOR that PR #17 reported as its driver).

## Not done

- (Done, run 3: row R1 upper.) Left from it: `g_eq_r14`, the NAND's other input (not followed); which
  address bit each bus line is; the three thin vertical metals east of the ninth VSS rail (x 10790-10910).
- Ends of `wr_r15` (poly, y 11837).
- Right of x 10600: (done, run 4: the n lines' contacts and the read bus tracks.) Left: the two thin
  metals x 10809 (the follower ends it at (10809,15738)) and x 10853 (to (10852,17652)), both through
  the whole field from north of y 10150; the end of the s7 VCC rail; the ninth VSS rail's end (y 13300).
- From the review of run 7 (round 6): `dbus`'s `d7_c` metal (port (16950,16750-16766)) goes on west along
  y 16758 to a corner near (16838,16758) and south on x ~16840 to about y 17306, in no trace file and no
  ports file (it does not touch the read bus: no metal at x 16803-16835 on y 16758). And the thin metal
  x 16762-16780 that these notes call `dbus_le` is **not one metal** south of `dlat`'s end: no metal in
  either chip for 20-60 px at every unit (y 15937-15990, 16067-16124, 16197-16255, 16323-16383,
  `tools/tl5_tracks.py v 16771 15840 16400`): to be read with the units.
- From run 8: `dbus_le`'s thin metal south of y 16450 (a 15 px dark bar at y 16456-16471, then on to about
  y 16505; PR #17: west at y 16498); the VCC rail south of y 16440 (to about y 16478: whether it meets the
  horizontal metal y 16493-16508 below it is not read; 12 px of dark between them at x 16515); what lies
  west of the VCC rail (x < 16490) beside the units.
- From run 6: column 1's poly band west of
  (16139,17474) (seen to x 16084) and what it drives (the gate group at about x 16060-16230, y 17290-17480).
- From run 5: the poly column x 13706-13730 under the rows.
- From run 4: the undrawn poly from the west along
  y 18297 that turns south under column 7's corner to `rst_ck`'s pad (10900,18470) (Ambiguity 13); the
  structure of AMB-040 under and east of the tracks (the diffusion-coloured rectangle y 11919-12186,
  whose west end has contacts of the s7 VCC rail at x 10565).
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

### Run 4 (the read bus)

Round 3 (full review, 2026-11-21 14:22 -0600; a fresh Fable reviewer, images in `cache/scratch/cdp4/review-3/`;
commit before the round 1429ae0). Piece: the read bus, x 10840-11230, y 10343-18305 (16 pads, eight tracks,
seven corners). Told to suspect: the corner of column 7's track over the poly corner of `rst_ck`'s column
(Ambiguity 13); whether each track runs through its `cdp4` pad; a missed pad or tap along the 7,900 px of
each track (the stretches y 11840-12300 on columns 1 and 0, the clean-shot marks, the bar on column 5 at
y 14575, the chip-1 stain, the poly-diagonal zone); the rows' continuity and their crossings of the lower
tracks and of the two undrawn metals x 10809, x 10853; two metals end to end on one track; a one-pitch step.

It checked: straightness by `tools/busl_mdrawn.py h` at 70 cuts (every centre within 3 px); continuity by
`tools/tl5_tracks.py v X 10300 18330` on all eight (no stretch over 16 px without metal in both chips apart
from pad rings, ends and one 21 px crossing of a poly diagonal on column 1 at y 17844-17865); the eight
north pads at 3x in three shots (ring, bright centre, hole, pits; no metal north; the poly ends on each);
both staircases by views and overlays (row K on the claimed track), with text maps of three `cdp4` pads
(metal directly beyond both rings in both chips) and `tl5`'s rings of 16-22 px on all eight; a scan of the
clean shot under each track (only the known crossings, the stain and specks; no ring or pad in either metal
shot); the corners in both metal shots (nested, order kept, no west arm, nothing south; column 0 turns east
at (11201,17908) onto y 17904-17913); Ambiguity 13 at 5x in three shots and by text maps (no contact: the
corner looks like the plain crossings of the same poly column at y 18380 and y 18425 and unlike that
poly's pad (10897,18468); clean-shot red minus green 48-71 under the corner against 8-32 in the pad
(10896,13636); south of y 18307 the column is open poly); the extraction of `cdp4` with `cdp3`.

No finding. Notes only, taken into the notes: three more poly rows cross the tracks without contact
(Logic, "No other contact"); more marks for Ambiguity 14.

Not checked by it: the horizontals east of x 11230; the rectangle y 11919-12186 beyond "no track has a
ring or pad on it"; continuity under the chip-1 stain (y 15530-15790) rests on chip 2 alone; the pad
(10983,13549) in the chip-2 stripped shot (residue); `tools/ports.py` (it could not run it).

After the round, on merging main (fe17f17): `regs` run 6 had reached main with column 0 of the bus drawn
in `trace/regs.txt` (the same track, pads and row ends, read independently). This package's copy of
column 0 (two row ends, two pads with contacts, the track, a label, an alias) was removed so that the wire
is drawn once. No connection changes with every file loaded:

- `.venv/bin/python tools/sameconn.py fe17f17`: connections identical
- `tools/t.sh cdp4 sameconn.py 70bbbc9`: 12 differences, all one thing: with `cdp4` loaded alone the
  selector node of slice 0 is again named `cdp4_n_s0` (its alias to `cdp3_n_c0` and the track now live in
  `trace/regs.txt`); no transistor's nets and no other name differ.

Round 3: no findings.

### Run 5 (the read bus, east along the bottom bus)

Round 4 (full review, 2026-11-21 14:41 -0600; a fresh Fable reviewer, images in `cache/scratch/cdp4/review-4/`, 26;
commit before the round 1127424). Piece: columns 1-7 from x 11220 to x 16000 (42 pads, 21 poly hops, the
diagonal fan). Told to suspect: a step or a bridge in each of the three hops, and a transistor or a contact
under their rails; the pad-to-row correspondence through the fan of ten parallel diagonals; column 6 against
the thin metal x ~14535, where `tools/follow.py` went wrong; missed taps on the long metals, above all east
of x 13200 where the clean shot is unreliable; the poly column x 13706-13730; each of the 42 pads; the join
with run 4's corners at x 11220.

It checked: the join (3x); each hop at 4x in the clean and the chip-2 stripped shot and in metal (seven
straight rows in and out in the same order, no step, no bridge; field under the rails: the rows keep one
colour, no diffusion edge line crosses them in either metal shot, `tools/railprof.py` reports no gate);
column 6 is not joined to the thin metal x ~14535 (19 px of open poly between its pad's ring and that
metal, which the follower's 24 px gap bridged); all seven pad-to-row correspondences, with a walk of its own
along every drawn metal segment at 1 px in both metal shots (metal within 6 px of the drawn centre along
every diagonal) and cuts at x 13450 and x 13690 (`regs`' lines above these, in order); taps, by the same
walk (no branch, no dark stretch of 6 px or more except pad rings, the named crossings and a chip-2 speck
at (14080,17775)); all 42 pads (one pad, one contact, its own metal on one side only, field beyond); the
extraction and `tools/unsure.py`.

- Finding 1, **geometry only**, confirmed (`tools/px.py row Y X0 X1 5 metal,metal1` through each pad: ring
  x 13158-13165, bright centre 13170-13175, ring 13180-13197 for columns 1, 3, 5, 7; ring 13200-13210, centre
  13215-13220, ring 13225-13240 for columns 2, 4, 6): the east pads of hop 1 were drawn 9-15 px too far
  west (their centres had been taken from the clean shot, which has interference colours there). Moved to
  x 13174 and x 13219; the drawn boxes overlapped the real pads before and the ends are the same.
- Finding 2, **comments only**: three crossings the notes did not name (Logic, "Crossings named by the
  review"), none with a pad.

`tools/t.sh cdp4 sameconn.py 1127424`: connections identical.
`.venv/bin/python tools/sameconn.py 1127424`: connections identical.

Not checked by it: under the three rails the chip-2 stripped shot shows only fringes, so "field" there rests
on the clean shot and the two metal shots; the long runs were seen in the stripped shots only at 1.3-1.6x;
nothing east of x 16000.

Round 4: no findings that change a connection.

### Run 6 (the read bus, the turn north)

Round 5 (full review, 2026-11-21 15:00 -0600; a fresh Fable reviewer, images in `cache/scratch/cdp4/review-5/`, 19;
commit before the round 3249ad8). Piece: x 15990-16820, y 17380-18060 (13 pads, seven poly columns, six
tracks). Told to suspect: the poly staircase under and between the metals (which bottom pad is joined to
which top pad; the alternative that a column runs straight north); the near-touching places between
neighbouring columns; a contact from the row y 17735, the horizontal metals or the wide band onto a column;
the pads at y 17775 against the row y 17735; each pad all round; column 1's column; the corners.

It checked: cuts along y 17753, 17735, 17690, 17648 and 17604 (exactly six polys each, at the traced x) and
views at 4x in the clean, chip-2 stripped and metal shots; arms 5, 6, 7 as continuous orange poly in both
metal shots and the stripped shot (rows y 17626, 17669, 17712), arms 3 and 4 under the band as salmon in
the clean shot with field between them and beyond their ends (cuts at x 16541, 16586, 16620, 16649, 16692);
the straight-north reading ruled out (each south column ends at its arm with field beyond; no north column
continues south of its arm); the gaps between neighbours, all field in three shots, the narrowest (8-12 px)
being column 3's north column against pad 4's west edge (x 16642-16650) and column 5's against pad 6's;
10-12 px of open poly, not metal, between the row y 17735 and pads 1, 3, 5, 7; no hole or ring along the
four metals or the band, no diffusion (`tools/opendiff.py`); all 13 pads (one ring, one bright centre in
both metal shots; field north of every top pad and south of pads 2, 4, 6); column 1 as one poly from
y 17468 to its pad; the corners (no T) and the rows' crossings of other nets' polys at x 16286-16580; the
extraction alone and with `regs` and `trunks`.

- Finding, **comment only**, confirmed (`tools/px.py row 17474 16060 16166 8 metal,metal1`: orange from
  x 16084 to x 16150): column 1's poly does not go on north of y 17465, it turns west there as a band
  y 17463-17485. The drawn end (16148,17480) is on the corner, so the port is on the net; the notes' "goes on
  north" is corrected (Logic, Ports, Not done). No geometry changed after the round:

`tools/t.sh cdp4 sameconn.py 3249ad8`: connections identical.
`.venv/bin/python tools/sameconn.py 3249ad8`: connections identical.

Not checked by it: under the wide band the chip-2 stripped shot is fringes, so arms 3 and 4 rest on the
clean shot and the edge lines in both metal shots; "no poly under the thin metals north of the top pads"
rests on the clean shot alone; nothing beyond the ports.

Round 5: no findings that change a connection.

### Run 7 (the read bus, north to the output units)

Round 6 (full review, 2026-11-21 15:22 -0600; a fresh Fable reviewer, images in `cache/scratch/cdp4/review-6/`, 15;
commit before the round 87c5f4f). Piece: x 16560-16970, y 15840-17390 (six tracks, five pads, five poly
rows or columns, the join of column 7 with `dbus_do0_in`). Told to suspect: the join (one metal from the
corner (16798,16714) to `dbus`'s pad (16993,16451)?); a contact where column 6's poly passes under column 7's
corner; that poly's continuity across the 12 px gap, along its column and at its turn west; the pad pairs on
one track position (read bus pad below, `d#_out_n` pad above); the nested corners; taps on the long runs;
the rows west of the end pads; each pad all round.

It checked: the join by `tools/tl5_tracks.py` h 16714 and v 16993 (no gap of 8 px or more in both chips
except 6-8 px edge bars at x 16808-16812 and y 16722-16726) and views of the corner and the pad; nothing on
x 16798 north of the corner; no contact at (16800,16713) at 5.5x in four shots (clean shot uniform salmon,
red minus green 40-56, against 8-17 in column 6's pad; no widening of metal or poly); the poly continuous
across the gap (both metal shots orange at x 16776); the column one poly from y 16384 to y 16712 with no
hole under the four horizontals, ending at y ~16375 with 12 px of field before `d1_out_n`'s row (it turns
west only); column 6's pad (poly east only); no metal in either chip between each pad pair; each row on its
claimed pad; the nesting (`tools/follow.py --gap 16`, an overlay); no clean-shot hole on any track,
horizontal or leg except the five pads; the rows continuous to x 16790; the joined extraction.

No finding. Notes only (taken into Not done): an undrawn metal of `dbus`'s `d7_c` inside the region, which
does not touch the six nets; the thin metal x 16762-16780 is in pieces south of `dlat`'s end.

Not checked by it: under the thin metals the chip-2 stripped shot is fringed, so "no contact" at the
crossings rests on the clean shot and both metal shots; the pad centres of columns 2, 3 and 5 are dull in
chip 2 and were accepted from chip 1, the clean-shot hole and the stripped shot; nothing west of the ports.

Round 6: no findings.

### Run 8 (the data output inverters)

Round 7 (full review, 2026-11-21 15:52 -0600; a fresh Fable reviewer, images in `cache/scratch/cdp4/review-7/`, 17;
commit before the round c79aa21). Piece: x 16480-16800, y 15780-16460 (the cell `cdp4_ro` and its four
copies, 10 transistors; the two rails; the five `d#_out_n` row ends; `dbus_le`'s thin metal). Told to
suspect: whether each output box is a buried contact or a metal contact from the thin metal over it, unit
by unit; which outlined regions are diffusion (the output strip, the branch, the plain area south of the tie
box, under the rail west of the column); other polys reaching the plate; the gate row's west end and a
second transistor on it; the copies, above all u1 and u5; anything undrawn; Ambiguity 15.

It checked: the five output boxes against three real pads of the same kind of metal at 3.5x in four shots
(no widened pad, no green hole, no pits; the small bright spot is not metal-bright, and the tie box, which
has no metal over it, shows the same spot): none is a metal contact; the pairing (each row straight from
pad to box or rail at one y under every track); the output strip and the branch as one outlined region
with no edge between, pinker than field in both chips and with blue 83-86 (not poly); the plain area as
field (`tools/opendiff.py`: none); pink field below the gate at x 16670 with an edge line across the gate
at x 16677-16680 in both metal shots (one transistor); the gate row's end at x 16657-16662, 15 px of field
short of the branch; no other poly at the plate; the rails (no break over 9 px in both chips; VSS ends at
about y 16446); the copies by `tools/cellcheck.py` in four layers; the extraction and `tools/unsure.py`.

- Finding 1, **geometry only** (it adds a contact, between metal and diffusion that are both `vcc`: no net,
  transistor or equation changes), confirmed (`tools/textmap.py 16484 15760 16556 15830 4`: ring and bright
  centre at x 16504-16516, y 15788-15800 in both metal shots; `tools/px.py col 16520 15760 15890 8 acid1b`:
  one tan box from y 15776 to y 15872): unit u1's VCC box runs on north to y 15772 and has a second contact
  of the rail at (16512,15794). Drawn outside the cell (`D 16497,15772:16547,15826`, `C 16512,15794`).
- Finding 2, **geometry only**: the pull-down's column is x 16680-16722 (W 42, was 39). Changed in the cell.

`tools/t.sh cdp4 sameconn.py c79aa21`: connections identical.
`.venv/bin/python tools/sameconn.py c79aa21`: connections identical.

Not checked by it: the thin metal's continuity over the boxes (Ambiguity 15 stands; `dlat` draws the same
dark stretch over u1's box as plain metal); the plate's foot into the tie box and the branch into it pass
through 9-12 px dark frames, and the field between each output box and its gate row is only 6-8 px (pink,
all five alike): read from structure, not measurable; the thin metal's end south of the piece (no metal at
y 16506-16529); the pads and rows east of x 16790 (run 7's and `dbus`'s).

Round 7: no findings that change a connection.

## Corrections (coordinator, from the handoffs of 2026-11-20)

- Row R1 upper, "Believed, not traced" and Not done ("`g_eq_r14`, the NAND's other input (not followed)"): followed by `cdp3` (row A): it is the match line of the comparator of line g (`cdp3_g_c#`) with R14.
- The strobe polys `wr_r15` (y 11837), `cdp4_ld` and `cdp4_ld6` are drawn as straight lines; in `cdp3`'s copy of the same latch cell the strobe `wr_r14` is a serpentine (field under each bit line and a-track metal at the band's height, the band joined through each cell's loop). Probably the same here; geometry only as far as seen (Re-read item R48).

## Corrections (coordinator, from the handoffs of 2026-11-20, second batch)

- The corner gate group, rows 2 and 4 "believed `rsel13_buf`, `rsel12_buf`": traced (`busl` run 8, pieces `r12`, `r13`; firm): the rows y 13744 and y 13852 are drawn from pads with contacts on the two select tracks ((6495,13744), (6452,13854)) onto this package's ports at x 7550, so **`cdp4_rst` = NOR(`rsel12_buf`, `rsel13_buf`, `rsel14_buf`, `rsel15_buf`, `rsel16_buf`, `rsel17_buf`)**, the six read selects of R12-R17 (believed: the selector's nodes are held low except while one of them is read). Row 4's poly begins at x 7528 (the foot of the step from row y 13852), 17 px west of `P 7545,13873`. The two open-join labels of the ports are renamed at the next refresh.

## Corrections (coordinator, from the handoffs of `busl` run 16, 2026-11-21)

- "The VSS plate at the foot of the s0 rail west of x 7550 and south of y 14055": drawn by `busl` (piece `vb`): the plate reaches x 7491 and a wide metal runs south from it to y 15000.
