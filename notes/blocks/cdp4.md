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

Not traced: the upper half of row R1 (y 11100-11490: source of the 6-bit a inputs, of
the bus taps and of the in tracks of the R1 latch), the wiring right of x 10600 and
below y 14060.

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
| ~11100-11500 | row R1 upper: complex cell | 8 | not traced |
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
- Data: in tracks `cdp4_in8b_sK` (x 8465 + dx), contact at (8466 + dx, 11809), run **up**
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
- Data: in tracks `cdp4_in6_s1`..`s6` (x 8465 + dx) start just above each cell's in
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
| `cdp4_in_s0`..`s7` | poly | x 7600, y 13333, 13376, 13420, 13463, 13505, 13548, 13590, 13633 | from outside | data into the row C latch |
| `cdp4_n_s0`..`s7` | poly | x 10850, same y as `in` of the same slice | driven inside | selector output |
| `cdp4_a_s2`..`s7` | metal | x 8509 + offset, y 11790 (drawn end; the track continues up through the R1 latch) | from R1 upper | selector input a (6 bits) |
| (bus tap) | metal | x 8555 + offset, y 11790 (drawn end; continues up through the R1 latch) | to/from R1 upper | joins `cdp4_bus_sK` |
| `cdp4_in8b_s0`..`s7` | metal | x 8465 + offset, y 11499 (drawn end; continues up) | from R1 upper | data into the R1 latch |
| `wr_r15` | poly | y 11837; believed to cross x 7600 (ends not examined) | from outside | R1 latch strobe |
| `cdp4_in6_s1`..`s6` | metal | x 8073, 8465, 8855, 9245, 9635, 10025 at y 14059 (drawn end; continues down) | from outside (below) | data into the row D latch |
| `cdp4_ld6` | metal | x 7947, y 13840 (drawn end; continues down) | from outside (below) | row D latch strobe |
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

## Not done

- **Row R1 upper** (y 11100-11490): not looked at beyond the survey. The a tracks
  (x 8509, s2..s7), the bus taps (x 8555) and the in tracks of the R1 latch (x 8465)
  come from there. Expect a 6-bit source for a; what the bus taps and channel 1 carry
  is unknown.
- Ends of `wr_r15` (poly, y 11837).
- Right of x 10600: the n lines' contacts beyond x 10850, thin vertical metals at
  x 10795-10905, the end of the s7 VCC rail.
- Below y 14060: where the six in tracks of row D, `cdp4_ld6` and the rails go (fan-out
  at y 14060-14700). The s0 VCC rail's bend below y 13540 and the wide metal at
  x 7700-7990, y 13650-14060 left of row D. The s7 VSS rail between y 13300 and 13694.

## Corrections (coordinator, from the handoffs of 2026-11-19, second batch)

- Ports, `cdp4_bus_s0`..`s7` ("unknown, per-slice line between row R1 and the left") and
  `cdp4_in_s0`..`s7` ("from outside, data into the row C latch") **are the same eight nets** (`busl`, piece
  `ch1`): for each slice the channel-1 row and the channel-2 row are joined in the left bus field by a
  metal track between poly pads, and the same net ends on one poly row of the left array (s7 .. s1 at
  y 11488, 11922, 12442, 12984, 13397, 13874, 14351; s0 just south of `busl`'s region). The field holds
  no transistor; which end drives is not traced.

## Corrections (coordinator, from the handoffs of 2026-11-19, third batch)

- Ports, `rsel14_buf`, `rsel15_buf`, `rsel17_buf`, `rsel16_buf` (`cdp4`'s selects 1-4), `cdp4_rst`, `cdp4_ld` "from outside": the selects come from south of y 15000
  on tracks x 6538-6668 and each also feeds a gate band of the corner gate group; `cdp4_rst` from the
  corner gate group (believed); `cdp4_ld` from `bc1`'s strobe driver (`bc1_ld_a`, marked: AMB-038). The
  "contact near that strobe line at (7557,12975)" is the pad (7556,12983) (`busl`, piece `ctl`).
- Ports, `cdp4_in6_s1`, `cdp4_in6_s2` "from outside (below)": from `cdp3`'s row A cells, columns c2 and
  c3, by line g (`cdp3_g_c2`, `cdp3_g_c3`; `busl`, piece `d6`).
- `wr_r15` ("ends not examined"): the row does not enter the left bus field; its west end is at about
  x 7603-7640, y 11825-11850, under the metal x 7600-7645 (`busl`, run 6).

## Corrections (coordinator, from the handoffs of 2026-11-19, fourth batch)

- The strobe of row R1's lower half ("ends not examined") runs east as one poly row y 11824-11844 to a pad (11243,11830) on the write strobe of R15 (`regs` run 1, firm): **row R1's lower half is R15**. Its west end is at about (7603-7640, 11825-11850) (`busl` run 6).
- The four selects are the read selects of R14-R17 (`regs` run 2, firm: sel1 R14's, sel2 R15's, sel3 R17's, sel4 R16's): the four-way selector is the read multiplexer of R14-R17. Source a is what R14 reads, row R1's lower half is R15, latch row C is what R17 reads, latch row D what R16 reads. The corner gate group takes two more select rows, y 13744 and y 13852 (believed R13's and R12's read selects, by taps at (6492,13744) and (6450,13852): `regs` run 3).
