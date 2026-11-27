# bc2: bottom-centre random logic, right part (x 9000-11000, y 14050-16300)

Scratch: `cache/scratch/bc2/`. Coordinates are metal-shot pixels.

## Status

2026-11-18 09:56 +0100: **two latch units traced** (east gate column: unit a, `tl1_ua` + `tl1_ub` at
7940,10454, and unit b at 7941,10930; 11 transistors each, 22 in all), traced on claude-opus.
Unit b is active (unit a's VSS box got its south edge 15279, which let copy b in with 0 errors), with
its own input and output rows to their pads. Unit a's enable metal x 10441 does **not** reach unit b's
enable pads (a break at y 15400-15414; it jogs west to x 10398 instead): units a and b have separate
enables. Not reviewed.
Everything else in the region is still survey only (below).

Earlier (2026-11-18 04:48 +0100, survey):
2026-11-18 04:48 +0100: **survey only. Nothing is traced; there is no trace file, no ports file and no
floor-plan fragment yet.** The run was stopped (budget) after the survey and the cell search.
Everything below was read at 0.57-0.9x (`survey.png`, `colL.png`, `colR.png`: metal and
clean shot side by side) unless a zoom is given: positions are to about 10 px and nothing
here is a connection.

## Inventory

**Known cells (the result worth resuming from).** `tools/findcell.py` on the clean shot,
region 9000,14050:11000,16300, masters `tl1_ua` (2532-2838 x 4350-4600) and `tl1_ub`
(2535-2838 x 4347-4797); `bc1_drv` gave no hit; `tl5_inv` was not run to the end.

| Place (offset from tl1's master) | Score ua / ub | Overlay |
|---|---|---|
| 7940,10454 (unit at x 10472-10778, y 14801-15251) | 0.76 / 0.76 | fits at 2.7x on the clean shot and 2.55x on the metal shot (`ia.png`, `ma.png`) |
| 7941,10930 (same column, 476 lower) | 0.76 / 0.77 | fits (`ib.png`, `mb.png`) |
| 6857,11495 (x 9389-9695, y 15842-16292) | 0.84 / 0.83 | fits on the clean shot (`ic.png`); its VCC box is taller than the master's; metal not looked at |
| 7101..7104,11625 mirrored mx=2686 (centre 9788,16150) | 0.65 / 0.66 | not overlaid: unconfirmed |

So the east gate column is a stack of tl1's unit (inverter + two cross-coupled three-input
gates: the latch with enable and clear that `tl4` and `tl5` also place), pitch 476. Whether
there are more copies above y 14800 and below y 15750 in that column was not tested (no hit
at 0.5; the column's gates run from y 14600 to y 16100).

Seen for the copies at 7940,10454 and 7941,10930 (`ma.png`, `mb.png`, and `w_acid1b.png`,
`w_metal.png` at 3.4x), **not drawn, not verified**:
- rail over the pull-downs' boxes x 10540-10597 (VSS by structure), rail over the loads' boxes
  x 10718-10775 (VCC by structure); neither followed to a supply.
- a ring below the stack at (10558,15258) (the box the copy needs of its own, as in `tl4`);
  the loads' long ring on the VCC rail y 14988-15070 at x 10745.
- thin metal x 10682 from a pad (10681,14953) to a pad (10681,15156) (the master's thin metal
  x 2742).
- west of copy a, rows ending on pads with contacts: (10395,14912) row y 14912 (cell row
  4452-4470, data), (10441,14958) row y 14955 (enable), (10395,15000) row y 15000 (the
  ua node's row), (10395,15087) row y 15087 (cell row 4625-4643), (10441,15172) row y 15172
  (enable again; the two pads at x 10441 lie on one vertical metal). Metals at the pads:
  a metal from the north-west ends on the pad (10395,15000) by a corner at about (10350,15000);
  a separate metal x 10395 starts at the pad (10395,15087) and runs south.
- **copy b's inputs differ**: its rows y 15563 and 15606 run on west past x 10340 under two
  vertical metals without pads there, and its top row's pad is at about (10352,15388). Read
  each copy's inputs on its own (self-check item 5).

**Rest of the region** (survey scale):
- Supplies: wide vertical metals x 9466-9510 (y 14140 to the bottom; contacts along it: the
  west gate column's rail), x 9640-9684, x 9812-9857 (from y 14480 down), x 10543-10597 and
  x 10720-10770 (east column). Wide horizontal bands y 14080-14120 (x 10200-10600),
  y 14210-14250 (x 9640-10600), y 14490-14530 (x 9640-9850). Which is VSS and which VCC is
  not established.
- West gate column x 9380-9900, y 14880-16300: gates on the rails x 9488 and x 9660 / 9835,
  load plates (clean shot) at x 9640-9700 and x 9800-9870 about every 150-240 px, large pale
  diffusions x 9450-9560 at y 15350-15750 and y 15950-16250. Not read.
- East gate column x 10470-10780, y 14600-16100: see above.
- Bus of horizontal metal lines y 14590-14700 from x 9000 (continuing `bc1`'s 13-line bus)
  to about x 10300, lines turning south as nested L's at x 9050-9450 (y 14700-15100).
- Nested L's top left: horizontal lines y 14130-14530 from x 9000, turning south at
  x 9300-10100.
- Vertical thin metals: x 9092, 9136, 9178, 9221, 9265, 9353, 9396 (pitch about 43) west of the
  west column; x 9959, 10001, 10045, 10089, 10131, 10175, 10219, 10262, 10305, 10349, 10392,
  10437 between the columns, with poly rows and pads between x 10000 and x 10500
  (y 14950-16050); five thin verticals x 10806, 10848, 10892, 10935, 10978 on the east edge
  (inside `bw`'s field).
- Two contacts in a row at about y 14555, x 10500-10560, with a thin horizontal metal from
  there east across the east rails (y 14555).

## Ambiguities

- The rails over latch unit a are named VSS (x 10568) and VCC (x 10746) by structure (the pull-downs' boxes and the loads' boxes, as in `tl1`), not followed to a supply.

## Latch unit a (x 10380-10778, y 14800-15285)

`@inst tl1_ua 7940,10454` and `@inst tl1_ub 7940,10454` (tag a): both cells at one offset, as in
`tl1`, `tl5`. Overlay `a_c.png` (clean) and `a_m.png` (metal), 2.5x: every gate of the cells lies
on a poly row over diffusion, the cell's contacts sit on the rails (VSS x 10540-10597, VCC
x 10718-10775) or on rings. Drawn by hand: both rails over the unit (by structure, not followed to
a supply), the VSS box below the stack with its ring (10558,15258) (south edge 15279: `px.py col 10560`
and `col 10580` in acid1b, pale diffusion to y 15272, dark edge 15276-15284, copy b's top poly row from
15286; `s1_seam.png`, 5x; `sameconn.py` against 7fdf5b3: connections identical), the VCC long ring
(10745,14988-15070), the thin metal x 10682 between its pads (10681,14953), (10681,15156), and the
rows west of x 10484 to their pads (`a_w.png`, 4x, clean and metal side by side: each pad a ring
in the metal shot, each row continuous poly in the clean shot):

| Net | Row | Pad | Metal at the pad |
|---|---|---|---|
| `bc2_w14912` data (inverter and upper AND) | y 14905-14922 | (10395,14912) | goes west, not followed |
| `bc2_w14955` enable (both ANDs) | y 14947-14964 and y 15163-15180 | (10441,14955), (10441,15172) | one vertical metal x 10441; north of y 14940 not followed; south it runs to y 15398, jogs west along y 15386-15398 to the metal x 10398, which runs on south (not followed); see "Latch unit b" |
| `rst_a` clear | y 15079-15096 | (10395,15087) | metal x 10395 south, joined by `eof`'s piece `isrc` (2026-11-19) to the net that `trunks` and `bd1` call `rst_a`; renamed in the refresh of 2026-11-19 (glossary, Former names) |
| `bc2_w15000` output (upper gate's node) | y 14992-15010 | (10395,15000) | a metal from the north-west ends on it, not followed |

Equations (`unsure.py --equations`: the inverter FIRM, the two gates DEPENDS only by feedback):
- `bc2_w14876` = NOT `bc2_w14912`
- `bc2_w15000` = NOT( `bc2_w14912` AND `bc2_w14955` OR `bc2_w15029` )
- `bc2_w15029` = NOT( `rst_a` OR `bc2_w14955` AND `bc2_w14876` OR `bc2_w15000` )

The same D latch with enable and clear as `tl5` and `lc2` place. Widths: `px.py col 10554`
(acid) gives poly y 14905-14922 and y 14947-14966 at the two upper AND gates, matching the
cell's L 18; the other transistors' sizes are the master's, not profiled.

## Latch unit b (x 10212-10779, y 15277-15752)

`@inst tl1_ua 7941,10930` and `@inst tl1_ub 7941,10930` (tag b). Overlay `b_top.png`, `b_bot.png`,
`b_rail.png` (2.5x) and `b_cells_ov.png` (2x, clean + metal): every gate of the cells lies on a poly row
over diffusion and every contact on a box or ring. Drawn by hand: the VSS rail x 10568 (w 56) and the
VCC rail x 10746 (w 50) over y 15270-15746, the VCC long ring (10745,15505) (ring y 15470-15550), the
thin metal x 10682 y 15416-15644 with its contacts (10681,15429), (10681,15632), the copy's own VSS box
below its stack `D 10540,15706:10596,15752` with the contact (10558,15731) (`b_box.png`, 4x), and the
rows west of the cells to their pads.

Copy b was first held: copy b's top poly row (y 15280-15297) crossed unit a's VSS box, drawn to
y 15285. With that box ending at 15279 (unit a, above), the full extraction is 0 errors, 0 warnings,
4126 transistors (11 more).

**Rows west of copy b** (each read from its gate to its pad at 4.4-8x in acid1b and a metal shot, and
acid / metal1 where in doubt: `b_data.png`, `b_en1.png`, `b_clr.png`, `b_pads_w.png`, `b_r606.png`,
`b_out5.png`, `b_v8.png`, `b_mnorth.png`). Each pad: a ring in the metal shot and a green centre on a
poly pad in acid1b. Colour scans (acid1b G-R) along rows y 15389, 15563, 15607 find no contact but the
pads. The rows pass under the thin metals x 10310, 10355, 10398, 10441 without contacts (the dark bars
across them in the clean shot are the gaps between metals). **b's inputs are not a's.**

| Net | Cell row | Row (drawn) | Pad | Metal at the pad |
|---|---|---|---|---|
| `bc2_w15388` data (inverter and upper AND) | master 4452-4470 | y 15381-15399 (`px.py col 10420`) | round, (10352,15388) | metal x 10353 south (not followed); the pad is NOT on the horizontal metal y 15392 just east of it (x 10374-10384 reads as poly under oxide: R+G ~270 like the bare row at x 10462-10480, metal 320-400) |
| `bc2_w15432` enable (both ANDs) | 4492-4510 and 4708-4728 | y 15423-15441 and 15640-15658 (`px.py col 10466` acid) | (10441,15432), (10441,15650) | one metal x 10441 from y 15418 south past both pads, on south beyond y 15718 (not followed) |
| `bc2_w15565` clear | 4625-4643 | y 15555-15573 (`col 10300`) | (10226,15565), x 10212-10246 | metal x 10226 north (not followed); it ends on the pad |
| `bc2_w15607` lower gate's node (output) | 4668-4688 (buried contact at x 10492 in the cell) | y 15599-15617 | (10267,15607), x 10250-10288 | metal x 10267 from the north (crosses the clear row with no contact) ends on it |

The upper gate's node (`bc2_w15476`, the cell's stub x 10473-10516, y 15467-15487) ends in a rounded
end at x ~10467 (`b_out5.png`, 6x): no row west, no pad, unlike unit a's output row y 15000. So unit b
takes out the other side of the latch from unit a.

**Unit a's enable metal does not reach unit b.** The metal x 10441 from a's lower enable pad
(10441,15172) is continuous south to y 15398 (stripe test, metal and metal1: the line 2-3x brighter
than its own edges at every y down to 15386; the dark band 15376-15384 is the data row's top edge
printing through, the line still brighter than its edges there). At y 15386-15398 it turns west to
x 10390 (both metal shots), into the metal x 10398 that runs on south (north of y 15386 the track
x 10398 is bare up to the L at y 15306). Between y 15400 and the outline of the pad ring (10441,15432)
at y 15414 there is no metal: at y 15408-15412 the line's place, its edges and the flanks read alike
(R+G 246-285, bare oxide) in both metal shots, whereas at a's pad (10441,15172) the metal runs straight
into the ring's outline (`b_x441k.png` against `a_x441k.png`, 6x, metal + metal1 + acid1b). The data row's
bottom edge accounts for y 15400-15406 only. So b's enable `bc2_w15432` is a net of its own (the
previous drawing, one metal y 15180-15665, joined them).

Equations (`unsure.py --equations`: the inverter FIRM, the two gates DEPENDS only by feedback, as for a):
- `bc2_w15352` = NOT `bc2_w15388`
- `bc2_w15476` = NOT( `bc2_w15388` AND `bc2_w15432` OR `bc2_w15607` )
- `bc2_w15607` = NOT( `bc2_w15565` OR `bc2_w15432` AND `bc2_w15352` OR `bc2_w15476` )

Sizes: the cells' (the master's). Checked against unit a rather than drawn anew: per transistor, the
normalised correlation of a 100x60 patch around each of b's 11 gates with the same patch of unit a
(476 px north) is 0.83-0.97 in acid1b, 0.74-0.93 in acid and 0.85-0.98 in the metal shot, all at one
offset (b = a + (0..1, 477)). `px.py row 15411` (between b's two upper AND gates t1898, t1899) gives
the diffusion x 10542-10580 between dark edges, the same as `row 14935` at unit a (x 10543-10580);
gate lengths at x 10554 / 10560 (acid): y 15383-15400, 15426-15442, 15497-15513, each L 16-18. The
channel widths of the master were not re-profiled here (t1898/t1899 are drawn W 72 over x 10519-10591;
the tan between their gates spans x 10542-10580, with a lighter strip x 10516-10524 west of a dark line
x 10528-10536: a question for `tl1`'s master, the same in a and b).

Not drawn: a dark V in the clean shot at x 10420-10445, y 15615-15635, between the row `bc2_w15607` and
the enable pad (10441,15650); acid reads bare field there (`b_v8.png`, 8x), so no poly joins them.

## Not done

In order:
1. Where the latch units' wires go: north of y 14940 on the metal x 10441 (a's enable), the metal
   x 10398 south of y 15440 (a's enable again), the metals at a's data, clear and output pads, and
   b's metals x 10353 (data, south of y 15440), x 10441 (enable, south of y 15665), x 10226 (clear,
   north of y 15515), x 10267 (output, north of y 15515). None is followed.
2. Test the east column above y 14800 and below y 15750 for further copies; overlay the copy
   at 6857,11495 on the metal shot and the mirrored candidate at all.
3. The channel widths of the latch cell (the master's, see "Latch unit b"); not re-profiled here.
4. West gate column; the routing (bus, L bundles, vertical tracks, among them the thin metals
   x 10310, 10355, 10398 west of unit b); joins to `bc1`'s bus ends at x 9000, to `bw` and to `cdp4`;
   floor-plan fragment.

## Run 2 (2026-11-27): the centre block, piece `inv`

Matt Godbolt, on Claude Fable 5.2, 2026-11-27 08:11 -0600. The centre block of the bottom-centre logic (x 9100-10250,
y 14650-16300) was untraced: three rails with gate columns between them and nested wires on both sides. This
piece is its first three units on the east rail, x 9640-10110, y 14815-15300: 6 transistors, 3 named outputs, no
uncertain item. Views in `cache/scratch/bc2/`: `m1_top`, `top_m`, `top2_m` (overviews), `u1_*`, `e1_*`, `e1e_*`,
`e1w_*`, `e1n_*`, `knot` (photos at 3-8x), `wire_e_m`, `ov23_c`, `ov_w` (overlays).

### The rails

Three wide metals run down the block: W (x 9440-9500), M (x 9640-9700), E (x 9806-9866).

- **M is VCC**: its top is the stem x 9550-9600 (the stem steps east at y 14700-14750 onto x 9640-9700) of the
  west piece, x 9347-9818, of the wide band y 14130-14180; that piece turns north at its east end as the
  datapath's rail x 9765-9818, which `cdp4` labels `vcc` (`N M 9789,11800 vcc`; metal down x 9790 from y 13990
  to y 14170 in both chips, crossed by poly rows). Every load of the block lies beside M. (The first version
  of this note said the band runs east to the rail x 10746: wrong, the band is two pieces with bare ground at
  x 9815-9941 and x 9987-10158; found by review round 2.)
- **E is VSS**: its top turns west at y 14500-14550 to x 9640-9690 and north into the band y 14222-14268, which
  is metal along y 14245 from x 9654 to x 10593 (three 4 px edge lines on the way), where the VSS rail x 10570
  stands. The units' pull-downs lie under E.
- **W** comes from the band y 14270-14300 from the west; not decided (it crosses the positions of both the
  VCC rail x 8534 and the VSS rail x 8712).

The two bands are not drawn: M and E are labelled `vcc` and `vss` over this piece's units (joined by name).

### Cell `bc2_einv`: an inverter on the E rail (master: the top unit, gate band y 14947-14963)

- **Pull-down** under the rail: VSS land (9828-9868, 14900-14945) with its contact (9843,14922) (pits in the
  clean shot, ring in both metal shots); gate band y 14947-14963 (salmon under the rail); output land
  y 14967-14998 (x 9805-9870). Channel 44 wide (the VSS land's width, x 9824-9868), 16 long.
- **Output**: the land has a tab east of the rail (bright green in the clean shot at (9879-9885, 14985-14990))
  into a framed box (9890-9928, 14980-15014: heavy outline, an L-shaped lighter interior, tan in chip 2's
  stripped shot), from which a poly leaves east.
- **Load** beside the M rail: the output land runs west as a band y 14978-15000 under a poly block
  (9698-9754, 14955-15022) to the VCC land under M (9642-9696, 14945-15005; contact (9668,14963)). In chip 2's
  stripped shot the block is three orange bands (y 14958-14970, 14978-15000, 15008-15020) separated by one dark
  line each (y 14970-14977, y 15001-15008): the band's two edges under one poly (view `knot`, 8x). Channel 22
  wide, 56 long.
- **Tie**: a diffusion wire x 9758-9776 leaves the band north (tan in the stripped shot, orange-west /
  plain-east in chip 2's metal shot down x 9762-9771 from y 14937 to y 14994) and turns west at y 14932-14950
  into a framed box (9726-9756, 14930-14952; pinkish window) on the block's top.

Copies at +130 and +260 (`tools/findcell.py` on the clean shot: 0.84 and 0.87); overlay `ov23_c`: lands, bands,
blocks and boxes lie on the features. Two more partial matches (+440: 0.60, +613: 0.62) are not placed: units of
another build.

    bc2_e14955 = NOT bc2_p14823
    bc2_e15085 = NOT tl6_p6143
    bc2_e15215 = NOT tl6_p6101

### Inputs and outputs (drawn to this piece's edges; view `wire_e_m`, overlay `ov_w`)

- **Unit 1.** Input `bc2_p14823`: the band's poly runs on east of the rail to x 9976 and north as a column
  x 9950-9976 **under the thin metal of the unit's own output** (clean shot salmon from y 14858 to y 14960, no
  hole; `cdp4_candh.py v 9963,14900 9963,14930`: plain) to the poly row y 14815-14832, which comes from the west
  (port at the rail's east edge). Output: the box's poly ends on a pad (9963,15000); a thin metal north to
  y 14870, west to a pad (9897,14869); its poly row y 14860-14878 leaves west under the rail (port). Between
  the band's end and the pad the clean shot is pink under the thin metal (y 14966-14980): field.
- **Unit 2.** Input `tl6_p6143`: the band ends east on a pad (9963,15087) of a thin metal that comes from the
  north on x 10007, turns west at y 15046 and runs on south on x 9963 through the pad (`tools/follow.py`: north
  to a corner (10004,14436) and west to a pad (9722,14437); south to y 15742). Output: the box's poly east under
  that metal (no contact) to a pad (10006,15131), the north end of a thin metal x 10007 south (follow: to
  y 15570). So x 10007 carries two nets: the input above y 15046, the output below y 15122.
- **Unit 3.** Input `tl6_p6101`: the band's poly east under the metals x 9963 and x 10007 (no contact) to a tap
  pad (10050,15217) on the thin metal x 10052, which runs through (follow: north to a corner (10052,14390) and a
  pad (9764,14394); south to y 15526). Output: the box's poly east under x 9963, x 10007 and x 10052 (no contact)
  to a pad (10094,15261), the north end of a thin metal south (follow: a corner (10089,15698), west to
  (10003,15696)); bare ground north of the pad.
- The four pads test as pads and the six crossings as plain (`cdp4_candh.py`: clean shot minimum R-G 32-47 at
  the crossings, -23 to -37 at the pads).

The pads (9722,14437) and (9764,14394) lie on two of the poly bus lines y 14354-14873 that `bc1` draws west of
x 9300: the two inputs come off that bus.

### Ambiguities (run 2)

1. **The pull-down's width** (settled by review round 2): east of the rail the gate band lies on field (north of
   it chip 2's stripped shot reads R-G +1 to +6 at x 9880; south of it the tab's edge y 14978 is a separate line
   from the band's edge y 14967), so the green strips beside it in the clean shot are the poly's rims. The channel
   is the VSS land's width, 44.
2. **The framed boxes** (three output boxes, three ties) are drawn `B`: heavy outline, lighter interior, at the
   end of a poly with no other driver (the load's gate) or of the output poly.
3. **W's supply** is not decided; nothing drawn rests on it.

### Not done (run 2)

- The rest of the block: the E rail's units below y 15300 (two more of another build at about y 15400 and
  y 15570, and on), the W rail's units, the M rail's other loads, the nested wires on both sides and the bus
  rows y 14690-14880 east of x 9870.
- The six wires of this piece beyond its edges (ports).
- The two supply bands.

## Run 2, piece `nand` (2026-11-27): three two-input NANDs on the E rail

Same run, after piece `inv`'s review. Region x 9640-10190, y 15290-15830: 9 transistors, 3 named outputs, no
uncertain item (full extraction 2,527 nets, 4,853 transistors, 0 errors). Views in `cache/scratch/bc2/n2/`:
`u4_c`, `u4_m` (2.8x), `k4` (the load knot, 7x), `b4` (the output box, 7x), `o5_m`, `o5_c`, `o6_m` (4x), sheet
`x1`, overlay `ov_c`.

    bc2_e15343 = NAND( bc2_e15215, bc2_e15085 )
    bc2_e15517 = NAND( tl6_p6101, bc2_e15085 )
    bc2_e15690 = NAND( bc2_e15215, tl6_p6143 )

With piece `inv` (`bc2_e15085` = NOT `tl6_p6143`, `bc2_e15215` = NOT `tl6_p6101`): three of the four minterms of
the two wires `tl6_p6143` and `tl6_p6101`, each active low: `bc2_e15343` is low when both are low,
`bc2_e15517` when `tl6_p6101` is high and `tl6_p6143` low, `bc2_e15690` when `tl6_p6143` is high and
`tl6_p6101` low. A two-bit decode; what the two bits are is not known (they come off the poly bus above).

### Cell `bc2_enand` (master: the unit with bands y 15334-15352 and y 15378-15396)

Under the rail (`tools/bd2_umap.py 9796 15290 9960 15650 4 4`): VSS land y 15298-15332 with its contact
(9842,15311) | band 1 y 15334-15352 | strip y 15354-15376 | band 2 y 15378-15396 | output land y 15394-15436;
the diffusion is x 9805-9868 from y 15322 down (the land's top part x 9828-9868). The strip has no contact and
no exit east or west (closed outlines both sides): two pull-downs in series, about 78 wide (the diffusion's edge
lines cross both bands at x 9796-9800 and x 9876-9880: review round 3). The bands' west end caps
lie west of the rail at x 9782-9800. Output box (9896-9930, 15420-15446) on a tab of the land east of the rail,
its poly east along y 15424-15442. Load and tie are `bc2_einv`'s: block (9698-9754, 15397-15462) over the band
y 15417-15440 from the VCC land under M (9642-9696, 15380-15440; contact (9659,15399)), three orange bands with
one dark line between each in chip 2's stripped shot (view `k4`); tie wire x 9757-9773 north from the band into
the box (9728-9756, 15370-15396) on the block's top.

Copies at +174 and +347 (`tools/findcell.py`, clean shot: 0.93 and 0.89); overlay `ov_c`.

### Inputs and outputs

The four thin metals of piece `inv` run on south and each ends here on a pad at the east end of a band:

| Metal | Net | Tap | End |
|---|---|---|---|
| x 10093 | `bc2_e15215` | (10091,15345): band 1 of unit 15343 | south to y 15698, west to the pad (10006,15696): band 1 of unit 15690 |
| x 10007 | `bc2_e15085` | (10006,15391): band 2 of unit 15343 | the pad (10006,15566): band 2 of unit 15517 |
| x 10052 | `tl6_p6101` | (10050,15217): the inverter (piece `inv`) | the pad (10050,15522): band 1 of unit 15517 |
| x 9963 | `tl6_p6143` | (9963,15087): the inverter | the pad (9963,15738): band 2 of unit 15690 |

Outputs: `bc2_e15343`'s row y 15424-15442 east under all four metals to a pad (10137,15435), the south end of the
thin metal x 10137 (bare ground on x 10137 from y 15464 to y 15584), which runs north (`tools/follow.py`: to the
pad (10135,14783) of a bus row); `bc2_e15517`'s row y 15598-15616 east to a pad (10137,15608), whose metal goes
east and north on x 10172-10191 (seen on north to a corner at y 14735 and a pad (10092,14740)); `bc2_e15690`'s row
y 15771-15789 east to a pad (10006,15782), whose metal goes east and south on x 10050. Each is drawn to this
piece's edge (ports).

Crossings (`cdp4_candh.py`, and the four it flagged on a four-shot sheet, `x1`): every band and row under a thin
metal is a plain crossing (the row not widened, salmon, no hole). The test's flags at (9963,15563), (10007,15430),
(10093,15430), (10052,15343) were dark specks beside the row; its flags at (10007,15607), (10052,15607),
(9963,15780) are places with no metal at all (the open poly's green rim). The eight pads test as pads.

### Ambiguities (piece `nand`)

4. **The strip between the two bands** is taken as an internal node: no contact on it, closed outlines east and
   west of the rail. If it had an exit the gate would not be a plain NAND.
5. The boxes are drawn `B` as in piece `inv`.

### Not done (piece `nand`)

- The three outputs beyond their ports; the next unit down the E rail (from y 15830); the W rail's units; the M
  rail's west-side loads; the bus rows.

## Run 3 (2026-11-27), piece `bus2`: the decode's two inputs are `tl6_p6101` and `tl6_p6143`

Matt Godbolt, on Claude Fable 5.2, 2026-11-27 08:47 -0600. Wiring only: two bus lines end to end, x 7545-10052, y 14377-14454,
and their thin metals down to piece `inv`'s (y 14660). No transistor, no uncertain item. Full extraction 2,525
nets (two joins), 4,853 transistors, 0 errors. Views in `cache/scratch/bc2/n4/`: `a` (west ends, 4x), `b`
(x 8220-8680), `c` (x 9340-9800), `w` (x 6700-7800 with `busl`'s rows), `gap` (x 7530-7790, 5x); each metal over
clean shot.

### What it establishes

The two wires that piece `inv` called `bc2_m10052` and `bc2_m10007` are **`tl6_p6101` and `tl6_p6143`**: the two
nets `busl` brought across the left bus field from the top-left logic to "a poly row at the field's foot toward
the bottom-centre logic's bus (y 14393, 14437)" (its ports (7550,14393) and (7550,14437)). So

    bc2_e15215 = NOT tl6_p6101          bc2_e15085 = NOT tl6_p6143
    bc2_e15343 = NAND(bc2_e15215, bc2_e15085)     low when both are low
    bc2_e15517 = NAND(tl6_p6101, bc2_e15085)      low when tl6_p6101 = 1, tl6_p6143 = 0
    bc2_e15690 = NAND(bc2_e15215, tl6_p6143)      low when tl6_p6101 = 0, tl6_p6143 = 1

all firm. The glossary has `tl6_p6101`, `tl6_p6143` and `tl6_p6187` as "believed three of R8's outputs" (north
ends not followed): if so this is the decode of a two-bit field of R8. The third, `tl6_p6187`, arrives at
y 14870, the height of `bc1`'s bus line `bc1_s1` (y 14873), one input of `bc1`'s own three-NAND decode: a
lead, not followed here.

### The two lines

Lines 2 and 3 of the 13-line bus that `bc1` describes (its y 14397 and y 14439). Each is metal where it is free
and poly under the two groups of three wide vertical metals, with a pad and contact at each change:

| | `tl6_p6101` (y 14394) | `tl6_p6143` (y 14437) |
|---|---|---|
| poly row from `busl`'s end (x 7550) under `bc1`'s vertical metals | to the pad (7795,14394) | to the pad (7838,14438) |
| metal | x 7795-8250 | x 7838-8293 |
| pad, poly under `bc1`'s rails x 8335-8555, pad | (8250,14394) - (8598,14394) | (8293,14438) - (8641,14437) |
| metal | x 8598-9378 | x 8641-9421 |
| pad, poly under the W rail, M's stem and E's feeder (x 9455-9690), pad | (9378,14394) - (9764,14393) | (9421,14438) - (9722,14438) |
| thin metal east, south | to x 10052, down to the tap (10050,15217) and the end pad (10050,15522) | to x 10007, down, west at y 15046, down x 9963 to the pad (9963,15087) and the end pad (9963,15738) |

Evidence: `tools/tl5_tracks.py h 14394 7700 9800` and `h 14437 ...`: metal in both chips on the metal stretches
(no gap of 8 px), no metal on the poly stretches except the wide verticals crossing them, and in the clean shot
a hole (red minus green under 24) only at the eight pads and the two east ones; `cdp4_padc.py` on the ten pads:
hole, and ring with bright centre in at least one metal shot each ((9378,14394): chip 1 only; (9764,14393): a
small red-centred hole, ring and bright centre in both metal shots). Under the wide metals the rows are salmon
and unbroken in the clean shot (views `b`, `c`); the dark rings beside them at x 8320, 8400, 8480, 8560, 9520,
9610, 9700 lie in the gaps between two metals (the layers note's trap), not on the rows.
`tools/eof_tee.py` on the poly stretches: no branch.

**The join to `busl`'s rows** (x 7550-7778 / 7821): each row runs on east from `busl`'s drawn end under `bc1`'s
vertical metals x 7575-7760 to its pad: poly throughout (`tl5_tracks.py rows row 7520 7800 4 14392 14437`: poly
under metal or in the open at every sample but the 8-12 px dark edges of the metals; no pink field). No contact
to any of the verticals: chip 1's metal shot is plain bright metal over both rows. One place needs saying: under
the wide metal x 7664-7708 the clean shot shows the row y 14393 as three small patches of different colours
(grey, green, orange-red, 59-136 red against 200 or more for salmon) and chip 2's metal shot is dim there
(138-156 at x 7680-7688), while chip 1's is bright right across (201-219) with only the row's two edge lines
(down x 7685: dark at y 14380 and y 14404, 221-223 between). No ring in either chip: read as residue on the two
dies, not a contact (Ambiguity 6).

### Ambiguities (run 3)

6. **(7664-7708, 14393)**: residue or a contact of `tl6_p6101`'s row to the wide vertical metal there. Read as no
   contact (no ring in either metal shot). If it were one, `tl6_p6101` would be on that metal too (it is in
   `bc1`'s undrawn bundle; nothing else would change here).
7. **The pad (9768,14393)**'s hole is small and red-centred in the clean shot; the contact rests on both metal
   shots.
8. **(9476,14438)**, row B under the W rail's west margin (review round 4): the clean shot has a dark bar across the
   row, chip 1's other stripped shot a green spot with a ring, chip 2's stripped shot a small green spot at
   (9470,14431); neither metal shot has a ring and the row is not widened. The same kind of spot as Ambiguity 6: not
   a contact.
9. **(8940,14398)**: a dark notch on line A's metal in both chips; the metal is continuous beside it and the clean
   shot is plain field beneath: not a break or a tap.

### Not done (run 3)

- `tl6_p6187` / `bc1_s1` (the lead above); the other bus lines east of x 9300.
- The centre block's east rail from y 15800 (first look in `cache/scratch/bc2/n3/notes.md`: an inverter at
  y 15805-15935 fed from a pad (10008,15866), then an irregular group).

## Review

**Model note: latch unit a was traced AND reviewed on claude-opus, not claude-fable-5-2**
(the contributor's Fable allowance is exhausted). The survey was on Fable.

Round 1 (full review of latch unit a at commit c4baf0a, 2026-11-18 08:39 +0000, a fresh agent on claude-opus).
Checked at 3-5x in the clean, stripped and metal shots with profiles: each of the five rows
(y 14912, 14955, 15000, 15087, 15172) one poly from its pad to the cell, field between
neighbours, none continuing west past its pad; the pad (10395,15000) on `bc2_w15000` and
not on `bc2_w15029`; the metal x 10441 continuous between the two enable pads (it runs on
past both: drawn only between them) and touching no other pad; no further vertical metal
through the unit besides the cell's own; the thin metal x 10682 and its contacts on rings;
the VCC long ring on its rail; the VSS box and ring; the extraction (0 errors; the three
equations as stated). Not checked: gate overhangs of ten of the eleven transistors; the
copies' contact boxes one by one above 1.6x; the metal shot at 5x for x 10600-10800 above
y 14920. Note from the tracer of unit b (not yet merged): this unit's VSS box
`D 10530,15235:10586,15285` is about 5 px too long at its south edge (photo: y about
15279); geometry only here, but it blocks unit b's top row.

Round 1 (latch unit a): no findings.

### Latch unit b (also traced and reviewed on claude-opus)

Round 1 (full review of what changed since c4baf0a: unit a's VSS box south edge
15285 -> 15279, and all of unit b; 2026-11-18 09:05 +0000, a fresh agent on claude-opus). Two tracers had
disagreed on whether the metal x 10441 joins unit a's enable to unit b's; the reviewer
settled it independently and first: **separate**. Column and row profiles in `metal` and
`metal1`: the line is bright (R+G 350-440) at y 15250-15370 against 250-305 beside it; at
y 15386-15398 the bright stretch runs WEST to the metal x 10398 (x 10420 bright, x 10460
not); at y 15404-15412 there is no bright core and no side edges (flat 236-253, at or below
bare ground); b's pad has its own rounded outline at y about 15412 and the clean shot shows
the gap strip round it. The trace has the turn on `bc2_w14955` and b's enable as
`bc2_w15432`. (The joined version was never on main.)
Also checked: each of b's rows to its own pad and no other, no contact at any metal
crossing (metal x 10267 passes over the clear row without one); the data pad separate from
the y 15392 metal; the dark V at (10420-10445, 15615-15635) rightly undrawn; b's two enable
pads on one metal touching no other pad; 4x overlays (every contact on a ring; boxes and
rings on their rails); the output row on the lower node `bc2_w15607`; the thin metal
x 10682 absent between y 15256 and 15412 (units a and b rightly separate there);
`tools/sameconn.py c4baf0a`: only additions, unit a's connections identical; extraction
0 errors; `bc2_w15352 = NOT bc2_w15388` firm, the two latch equations depend only on the
master cell's `?` load ties. Geometry only: t1898/t1899 are drawn W 72 and read about 66
(the 38 px reading in the notes is the clean shot's margin effect beside the rail); it is
the tl1 master cell's width, unit a reads the same. Not checked: the gate widths of t1893
and t1894; anything beyond y 15746.

Round 1 (latch unit b): no findings.

### Round 2 (full review), 2026-11-27: run 2, piece `inv` (traced and reviewed on Claude Fable 5.2)

A fresh Claude Fable 5.2 agent, on commit e4d7fa8, 17 images in `cache/scratch/bc2/review-2/`. Told to suspect:
the load (one poly over one band, the tie wire), the output box's joins to the land and to each unit's pad, unit
1's input column under its own output metal, the gate band's east part (over diffusion or field), the two copies
against the master, each thin metal's ends and crossings (x 10007's two pieces), the supply claim for M and E,
anything undrawn.

**No finding changes a connection.** Three findings, all confirmed and fixed:

1. **M's supply evidence was wrong** (M = VCC holds): the band y 14130-14180 is two pieces; M's stem hangs on the
   west one, which turns north as the datapath's rail x 9765-9818 (`cdp4`: `vcc`), not on the piece that reaches
   the rail x 10746. Notes and trace comment corrected.
2. **Unit 2's VCC land** is taller (y 15033-15135) and has a second contact at (9662,15055) (pits, ring in both
   metal shots): drawn. Probably also the VCC end of an undrawn load west of M (open poly at x 9596-9628, y 15055).
3. **Pull-down width**: the VSS land's west edge is x 9824 (drawn 9828): channel 44, and the band east of the rail
   lies on field (Ambiguity 1 settled).

Checked and found correct by the reviewer: the load in all three units (one poly block with single 6-8 px dark
lines over one band; the tie wire diffusion, unbroken into the band; `tools/cellcheck.py`: 0.96 and 0.97 for the
copies); tab, box and poly to each pad joined in all three; unit 1's row y 14815-14832 ending at x 9977 into the
column, the column salmon with no hole under the metal, field between the band and the pad (9963,15000); 10-12 px
of bare ground at y 15023-15033 between that pad and unit 2's input corner; x 10007 two pieces with no metal at
y 15052-15126; nothing north of the pad (10094,15261); x 9963 and x 10052 through their pads; no contact at any
crossing; no hidden branch on eight polys; E's band continuous along y 14245 from x 9640 to x 10594; no contact
to E on the output lands. Could not check: the clean shot at the loads (displaced or inverted there: the load
reading rests on both chip-2 shots and chip 1's metal shot); diffusion continuity exactly under the rail-edge
lines; the wires beyond y 14660-15300.

Connections before and after the fixes (commit e4d7fa8 against the fixed tree):

    tools/t.sh bc2 sameconn.py e4d7fa8            ->  connections identical
    .venv/bin/python tools/sameconn.py e4d7fa8    ->  connections identical

Recorded 2026-11-27 08:25 -0600.

Round 2: no findings that change a connection.

### Round 3 (full review), 2026-11-27: run 2, piece `nand`

A fresh Claude Fable 5.2 agent, on commit 787a3c0, 28 images in `cache/scratch/bc2/review-3/`. Told to suspect:
series or parallel (the strip between the bands: a contact, an exit), which metal each of the eleven pads is
on and where each thin metal ends, the fourteen crossings (the tracer's pad test gave false alarms), the two pads
on x 10137, the copies against the master, the load and tie, anything undrawn.

**No finding changes a connection.** Three geometry remarks, confirmed and fixed:

1. The pull-down diffusion under the bands is x 9798-9878, not x 9805-9868 (edge lines across both bands and on
   the strip rows in three shots): W about 78.
2. Unit 2's output metal's north leg is x 10172-10191 (drawn centred on x 10176).
3. The output band east of the load is y 15425-15443 at x 9775-9800 (drawn y 15417-15440).

Checked and found correct by the reviewer: the series stack in all three units (no contact on the strip in the
clean shot or either metal shot; the strip closed at both rail edges with field outside; the west end caps
separate from each other and from the tie wire); two specks that are not contacts ((9831,15372), (9820,15770): one
chip only, no ring); all nine pads with their contacts; the metal ends (x 9963 at y 15743; x 10007 through its tap
to y 15571; x 10052 at y 15527; x 10093 through its tap, round the corner to (10006,15696), not joined to x 9963;
x 10137 on its pad at y 15435 with no metal from y 15442 to y 15604; unit 2's pad on the foot of the x 10181 metal
only; unit 3's output east and south on x 10050); all 14 crossings plain; the rows continuous with no branch
(`tools/eof_tee.py` on all nine); load, tie and output box identical in the three units, the VCC land joined to
the channel with no edge line, the band unbroken to the rail; `tools/cellcheck.py`: 0 of 44 blocks bad in two
shots; nothing undrawn at x 9700-9800 or x 9870-9950. Could not check: chip 2's stripped shot under the rail
(fringes: "no contact on the strip" rests on the clean shot and both metal shots); the tie wire's class by colour
(read as diffusion from its closed outline, as in `bc2_einv`); a green patch in the clean shot under the rail
between consecutive units (read as field between two closed lands).

Connections before and after the fixes (commit 787a3c0 against the fixed tree):

    tools/t.sh bc2 sameconn.py 787a3c0            ->  connections identical
    .venv/bin/python tools/sameconn.py 787a3c0    ->  connections identical

Recorded 2026-11-27 08:41 -0600.

Round 3: no findings that change a connection.

### Round 4 (full review), 2026-11-27: run 3, piece `bus2`

A fresh Claude Fable 5.2 agent, on commit b5d1c34, 23 images in `cache/scratch/bc2/review-4/`. Told to suspect: the
join to `busl`'s rows at the west end (the same row, no track step, no contact to the verticals there, the
coloured patches at (7664-7708,14393)), each of the ten pads (a contact; the metal leaving only as drawn; a
second poly), the metal stretches (a tap in mid-run, a break), the poly under the wide metals, the east pads'
joins to the thin metals, the thin metals to y 14660.

**No finding changes a connection.** One geometry remark, fixed: the pad drawn at (9764,14393) is about 5 px west
of its place (ring x 9750-9790, bright centre x 9763-9773 in both metal shots): moved to (9768,14393). Three
remarks for the notes, recorded as Ambiguities 6 (agreed: not a contact; the row y 14351 has the same green patch
under the same metal, chip 1's metal bright across, no ring, the row not widened), 8 and 9.

Checked and found correct by the reviewer: the west join (rows y 14393 and y 14437 unbroken from x 7300 to their
pads with no track step: column maps at 25 positions and row profiles in four shots; no ring or hole at the
metals x 7578-7622, 7664-7708, 7746-7757); the ten pads (ring and bright centre in both metal shots, except
(9378,14394), which rests on chip 1 and the clean shot's hole; the two east pads also pitted boxes in chip 2's
stripped shot; metal leaving only on the drawn side, bare ground north and south of each in all four shots); the
metal runs (no gap of 8 px in both chips; field under their whole length in the clean shot, so no poly passes
beneath; no tee); the poly under the six wide metals (salmon and unbroken, no ring in either metal shot; the gap
rings absent from both chip-2 shots; no branch); the east thin metals (continuous, clean corners, crossing the
poly rows y 14607 and y 14650 with edge bars only); the extraction. Not checked: `busl`'s own drawing west of
x 7545; under the wide metals chip 2's stripped shot is fringed, so those readings rest on the clean shot and
the two metal shots.

Connections before and after the fix (commit b5d1c34 against the fixed tree):

    tools/t.sh bc2 sameconn.py b5d1c34            ->  connections identical
    .venv/bin/python tools/sameconn.py b5d1c34    ->  connections identical

Recorded 2026-11-27 08:59 -0600.

Round 4: no findings that change a connection.

## Corrections (coordinator, from the handoffs of 2026-11-20)

- "Latch unit a", row `bc2_w14912` ("goes west, not followed"): the pad (10395,14912) is the south end of a thin metal x 10397 that comes from north of y 14570 (`eof` run 17, at 1.28x and by `tools/eof_mrun.py col 10395 14640 15030`; not read at high zoom).
- Not done 1 ("the metals at a's ... output pads ... x 10441 north of y 14940 ... x 10267 (output, north of y 15515). None is followed"): these three are followed (`eof`, pieces `in172`, `in390`): unit a's output `bc2_w15000` and enable `bc2_w14955` gate the NOR T at the top of this column (`eof_w15172`, the set of the latch behind the ripple counter's clock), and unit b's lower node `bc2_w15607` is one input of that latch's clear.

## Corrections (coordinator, from the handoffs of `cdp3`, `cdp4` runs 4-15, `eof` runs 36-51 and `regs` runs 5-6, 2026-11-21)

- The east column's VSS rail (`M 10568,15270 y15746 w=56` in `trace/bc2.txt`) runs on south as one metal to at
  least y 17590 (`eof` run 51; the reviewer agrees); `eof` draws y 17227-17590 of it. The stretch y
  15746-17227 is drawn by no one.
- An undrawn unit at about (10620-10780, 15750-15860): a depletion load from the VCC rail's contact box
  (10722-10775, 15782-15848), plate x 10685-10716, tie box (10622-10650, 15760-15790); its output is the track
  x 10808 (`cdp4_w10808`, `cdp4` run 12), which runs north into `tr1`'s gate row. Pull-downs not found.

## Corrections (coordinator, from the handoffs of `eof` runs 55-62, 2026-11-23)

- The table row of `bc2_w14955` ("south it runs to y 15398, jogs west along y 15386-15398 to the metal x 10398,
  which runs on south ...") and its Not done: the metal x 10398 is followed (`eof` runs 55, 56, 59): south to a
  corner (10398,15738), west to (10354,15738), south onto a pad (10354,15781), a poly hop to the pad
  (10354,15867) and the thin metal x 10353 / 10397 / 10441 to the output pad (10441,17168) of a NOR under the
  VSS rail x 10548-10598: **`bc2_w14955` = NOR(`rst_lat`, `ck_out`)** (firm; `bc2_w14955` is an alias). The
  port `bc2_w14955` M (10398,15440) in `ports.d/bc2.txt` is met.
- Copy b's enable `bc2_w15432` ("it goes on south (metal shot continuous to y 15718 at least; not followed)"):
  followed by `eof` run 60 (piece `en432`) through the pad (10441,15650), corners (10441,15788), (10393,15788),
  (10393,15828), (10180,15828) to an end pad (10180,16128), whose row runs west (no driver yet). The port
  (10441,15665) is met.
- Copy b's data `bc2_w15388` ("metal x 10353 from the pad south (not followed)"): followed by `eof` run 61
  (piece `d388`): corners (10353,15698), (10311,15698), (10311,15740), a pad (10268,15738), a poly hop to a pad
  (10268,15868), a metal x 10268 to an end pad (10268,16389), whose row runs east toward the rail column (no
  driver yet). The port (10353,15440) is met.
- R31: the lines `M 10441,15180 y15392`, `M 10441,15392 x10398`, `M 10398,15386 y15440` and the reading "not
  joined to copy b's pad" were confirmed on Fable by review round 72 of `eof`.

## Corrections (coordinator, from the handoff of `eof` run 70, 2026-11-24)

- The `bc4` part of the rail column: the unit at x 10420-10775, y 17630-17765 is `eof`'s piece `u17690`,
  `eof_w17734` = NOT `rst_lat` (firm; a weak load 24/94), on `rst_lat`'s branch row y 17682-17698; its output
  leaves west by a pad (10439,17734) and a thin metal x 10441 south (drawn to y 18010).
