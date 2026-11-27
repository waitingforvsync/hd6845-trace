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

## Run 3, piece `inv7` (2026-11-27): the inverter below the decode on the E rail

Same run. Region x 9640-10030, y 15805-16080: 2 transistors, no uncertain item. Views in `cache/scratch/bc2/n3/`:
`s_c`, `s_m` (2.5x), `u7_a` (4.4x, chip 2 stripped), `u7k` (the tie knot, 8x), overlay `ov7_a`.

    bc2_e15864 = NOT bc2_m15867

- **Pull-down** under the rail (`tools/bd2_umap.py 9796 15796 9900 15950 4 4`): VSS land (9824-9868,
  15816-15852) with its contact (9843,15838); gate band y 15856-15872; output land y 15872-15908, which widens
  west to the rail's edge at y 15896-15912.
- **Input**: the band's poly runs east to a pad (10007,15867) (hole in the clean shot, ring in both metal
  shots), the north end of a thin metal x 10002-10014 that goes south (drawn to y 15960: port; seen to about
  y 16190, where it turns east). Placeholder `bc2_m15867`.
- **Output**: a tab of the land east of the rail into a framed box (9898-9928, 15898-15928), its poly east to a
  pad (9963,15912), a thin metal south to a pad (9963,16062), whose poly is not drawn (port).
- **Load** beside M: a poly block x 9698-9782, y 15845-15912 over the band y 15862-15882 from the VCC land under M
  (9642-9696, 15850-15900; contact (9665,15877)): in chip 2's stripped shot three orange bands (y 15850-15858,
  15862-15882, 15888-15905) with one dark line between each (W 20, L 84: a weaker load than `bc2_einv`'s).
- **Tie**: the band's east end is the top of a diffusion strip x 9786-9800 between the block and the rail
  (chip 2's metal shot 133-179 / 104-137 / 73-91 down it at y 15866, 15876, 15895, 15925: pinker than field, blue
  above poly's; stripped R-G +15..+29), which runs south to y 15937 and widens west at y 15915-15937 into a framed
  box (9746-9772, 15912-15940) under a tab of the block's bottom (view `u7k`).
- **The strip meets the output land** at y 15896-15912 across the rail's west edge line (x 9800-9809): the land
  is tan to x 9804 under the rail there (`bd2_umap` rows 15900-15912) and the strip is diffusion to x 9800; the
  6 px between lie under the edge line (Ambiguity 10).

### Ambiguities (piece `inv7`)

10. **The join of the tie strip to the output land** rests on two diffusions meeting under the rail's 6-9 px
    edge line. If they did not meet, the load would have no connection to the output, which a gate cannot lack.

## Run 4 (2026-11-27): two more bus lines, and the W rail's first unit

Matt Godbolt, on Claude Fable 5.2, 2026-11-27 09:46 -0600. Views in `cache/scratch/bc2/w1/`; survey notes `w1/notes.md`.

### Piece `bus3`: bus lines y 14611 and y 14655 end to end (wiring; no transistor, no uncertain item)

Lines 6 and 7 of `bc1`'s 13-line bus, built like lines y 14394 / y 14437 (piece `bus2`). Views `b_west`
(x 7540-7870, 4x), `b_mid` (x 8220-8690), `b_east` (x 8960-9220, 5x), `west` (the legs' ends), `row823`.

| line | from `busl` (x 7545) | pads | corner, leg south | ends |
|---|---|---|---|---|
| y 14611 | `lc2_w9079` (its row y 14611) | (7837,14611), (8292,14611), (8641,14611) | x 9184 | pad (9183,14977): the unit's upper gate row |
| y 14655 | `lc3_e9756` (its row y 14654) | (7794,14654), (8249,14653), (8597,14654) | x 9141 | through the pad (9140,14826), on to the pad (9141,15087): the unit's lower gate row |

- Each: a poly row from `busl`'s end under the vertical metals x 7575-7760 to its first pad (salmon, unbroken, no
  hole; `tools/eof_tee.py`: no branch); a metal east over field; a poly underpass under the three wide metals
  x 8330-8550 between two pads (salmon, no hole, no branch); a metal east to the corner and south.
  `tools/tl5_tracks.py h 14611 7540 9200` and `h 14655 ...`: metal in both chips except at the pads, the
  underpasses and 8 px ridges where the metal crosses `eof`'s poly columns (x 9000-9008; x 8999-9006, 9021-9029,
  9042-9050). All nine pads: hole in the clean shot, ring in a metal shot (`padc`; chip 2 shows none at
  (8597,14654), chip 1 does).
- East of x 9000 both metals lie lengthwise over poly rows that `eof` drew (`bc2_w15607`'s y 14600-14621,
  `eof_w15172`'s y 14644-14664) and cross its poly column x 9005-9023: no contact (`eof`'s reading, and here:
  salmon unbroken, no ring).
- **The pad (9140,14826)** lies on the leg x 9141, which passes through it (bright - ring - bright both ways). Its
  poly row y 14815-14832 runs east under the vertical metals x 9180, 9225, 9268, 9355, 9400 (plain salmon, no
  ring: view `row823`; the stretch x 9285-9340 is in the open), the three rails and the thin metal x 9552 to the
  input row of `bc2_e14955` (drawn from x 9872 in piece `inv`): `tools/tl5_tracks.py rows row 9120 9960 12
  14823`: poly all the way. So **`bc2_p14823` is `lc3_e9756`** (alias), and `bc2_e14955` = NOT `lc3_e9756`.
- `cache/scratch/cdp4/candh.py` is of no use at these crossings (a row's two edges under a vertical metal are
  its "pad" pattern: 7 of 25 plain crossings flagged); each crossing was read on a view instead.

### Piece `w1`: the W rail's first unit (3 transistors; no uncertain item since review round 6)

    bc2_w15042 = NOR(lc2_w9079, lc3_e9756)

Region x 9140-9700, y 14940-15170. Views `u1_acid`, `u1_acid1b`, `u1_metal` (5x), `col` (the column, both
stripped shots, 7x), `ld_*` (the load end, 8x, four shots), `x9399`, overlay `ov_m`.

- **Where it stands.** The pull-downs are in the open gap between the thin metal x 9390-9408 and the W rail
  (x 9463-9513). There the clean shot misleads (trap 28: rings, a khaki arm, green stripes at the rail's edge), so
  the column is read from the chip-2 metal shot and chip 2's stripped shot.
- **Lands.** Under the rail a land (9462-9506, 14944-14988) with a contact (9479,14965) and an arm west
  y 14968-14984 to x 9416 (stripped red - green 20-26 against -8..8 for the open field above it); 140 px south the
  next land (9458-9502, 15104-15158; contact (9480,15128)) with an arm y 15104-15118
  (`tools/bd2_umap.py 9450 15096 9530 15160 4 4`).
- **Gate rows.** y 14991-15008 from the pad (9183,14977) and y 15078-15095 from the pad (9141,15087): poly
  (chip-2 metal shot orange, blue 48-64) to end caps at x 9458 under the rail's edge.
- **The column** x 9416-9446 between the two arms. Its east edge is a dark line at x 9445-9448 in both metal
  shots that crosses both gate rows (`tools/px.py row 14999 ...`, `row 15086 ...`: 53-64 / 48-55 there
  between poly at 120-170) and both stretches between the rows (`row 15020`, `15024`, `15066`: 48-84), and
  is absent on the two arms (`row 14976`, `15110`), in the open field (`row 14952`) and at y 15042, where the
  strip leaves east. A line that prints through poly is a diffusion edge (trap 28). Which side of it is the
  diffusion: the rows end 12-14 px east of it (a gate's overlap) and run on west, so the channel is west of it.
  W 38, L 17 each (review round 6: the column's west edge is x 9408, under the thin metal's margin).
- **The two stretches between the gates and the box were drawn `?D`** (Ambiguity 11; firm since review round 6): chip 2's stripped shot reads
  red - green 8-15 on the upper (y 15012-15028) and -4..6 on the lower (y 15058-15072) at x 9426 / 9434, between
  the arms' 17-26 and the field's -8..8; both are 12-16 px between two dark lines.
- **Output.** In the column's middle a framed box (9412-9442, 15030-15056): the end of the middle poly row
  (y 15034-15051; poly at x 9416-9426 inside it, blue 60-67) on the column, a buried contact. The row runs west
  under the thin metals to a pad (9183,15043) (hole, ring), from which a metal x 9178-9192 goes south (drawn
  to y 15130: port; the follower runs it to y 15784 and east to x 9274). The upper leg x 9184 ends on the pad
  (9183,14977) 66 px north: no metal between the two pads.
- **Strip and load.** A diffusion strip y 15038-15058 leaves the column east (stripped red - green 19-26 at
  x 9441-9453; tan under the rail and under the thin metal x 9552: `tools/bd2_umap.py`), passes under a poly
  block (9578-9632, 15020-15100; its edges print through the block at y 15031-15038 and y 15060-15066) and ends
  on the VCC land under the M rail (contact (9662,15055), drawn in run 2). W 20, L 54.
- **Tie.** A finger of the strip runs south under the thin metal (x 9548-9558, to y 15077), then a framed box
  (y 15078-15106) to which the block's bottom-left corner reaches (open red-brown poly at x 9566-9580,
  y 15090-15105).
- **The thin metal x 9552 (`bc2_e15343`'s, not drawn here) has no contact there.** The clean shot over the box
  reads R 174-209, G 146-181 throughout, with no green centre and no dark core, where the certain pad on the
  same metal, (9552,14785), has both; the bright - dark - bright - dark - bright pattern of both metal shots is
  the metal lying over the box's frame. The same at the next unit's box (9552,15270). (`padc`'s hole count
  there, 502, counts tan pixels.) The thin metal x 9399 has no contact at the middle row either (no ring, plain
  salmon).
- **The rail is VSS** by the gate's build (pull-downs on its lands, the load's far end on the M rail, which is
  VCC by drawing). Its join to a ground rail is not drawn.

### Piece `w2`: the W rail's second unit and its inputs (3 transistors, no uncertain item)

2026-11-27 10:07 -0600. Views in `cache/scratch/bc2/w2/`: `west` (the rows' west ends, 4x), `p568a`, `p568c` (pads of the bus
line), overlay `ov_m`; unit 1's views `col2`, `u2k` in `w1/`.

    bc2_w15216 = NOR(lc2_w9125, bc2_e14955)        (lc2_w9125 is the wire busl also calls lc3_e9798)

With `bc2_e14955` = NOT `lc3_e9756`: high when `lc3_e9756` is high and `lc2_w9125` is low.

- **The unit is a copy of the first, 174 px south** (unit 1 is now the cell `bc2_wnor`; `sameconn` against the
  commit before: identical). Measured, not assumed: gate rows y 15165-15182 and y 15252-15269 and the middle row
  y 15208-15225 (`tools/px.py col 9376 ...`: 174 px below unit 1's, each); the same dark line x 9445-9448
  across both gate rows and both stretches between them, absent on the arms and at the strip (`tools/px.py row Y
  9406 9466 3 metal,metal1` for Y = 15150 arm, 15172 row, 15194, 15215 strip, 15240, 15260 row, 15283 arm); the
  middle row's poly end at x 9418-9424 inside the box and plain diffusion at x 9439-9457 east of it; the tie under
  the thin metal x 9552 (finger tan to y 15248, box y 15252-15279, no hole: `tools/px.py col 9552 15180 15300 4
  acid1b`).
- **Lands.** Upper arm: land 2's lower arm y 15142-15158 (land 2 has two arms west with field between them:
  stripped red - green -8..1 at y 15125-15137). Lower arm: the next land (9458-9502, 15278-15314) with a contact
  (9479,15292) (`tools/bd2_umap.py 9450 15262 9530 15340 4 4`; `padc`: hole, ring in both chips).
- **Load.** The strip ends on the VCC land of the inverter `bc2_e15215` under the M rail (contact (9668,15223),
  piece `inv`): `tools/bd2_umap.py 9626 15196 9704 15250 3 3`.
- **Upper gate row** from a pad (9227,15173), the south end of the leg x 9226 of **bus line y 14568**, built like
  the others: `busl`'s row `lc3_e9798` (port (7550,14567)) to a pad (7794,14569), a metal east, a pad
  (8250,14568), an underpass under the three wide metals, a pad (8597,14567), a metal east over field (nothing
  under it: `tools/tl5_tracks.py rows row 7540 9240 12 14568`) to the corner x 9226 and south
  (`tools/tl5_tracks.py h 14568 7540 9240`, `v 9226 14560 15180`: metal in both chips but for the pads, the
  underpass and 8-10 px ridges at the rows the leg crosses). No branch on the poly stretches.
- **Lower gate row** from a pad (9312,15261), the south end of a thin metal x 9307-9319 that starts on the pad
  (9314,14870) (`tools/follow.py 9312 15215 N`: ends there), which is the west end of `bc2_e14955`'s output row
  y 14860-14878: poly all the way from the row's drawn end at x 9872 (`tools/tl5_tracks.py rows row 9300 9890 10
  14869`), under the E, M and W rails and the thin metals x 9552, 9399, 9355 without contact (no branch).
- **Output.** The middle row runs west under the thin metals x 9399, 9355, 9313, 9269 to x 9222, below the pad
  (9227,15173) and 18 px clear of it, and turns south in the open as a poly column x 9222-9240 (drawn to y 15300:
  port).
- Not drawn: the W rail south of y 15330 (the next land down is 32 px tall and there is no third unit of this
  build under it).

### Ambiguities (run 4)

11. *(Closed by review round 6: both stretches are firm.)* **The column's two stretches between the gates and the box** (`?D` at (9416-9446, 15008-15034) and
    (9416-9446, 15054-15076)). For: the edge line x 9445-9448 runs the column's whole length between the arms; a
    gate row needs diffusion on both sides; the box sits in the column. Against: the stripped shot's colour is
    weak there (above). Without them the two pull-downs do not reach the output.

## Run 5 (2026-11-27): a six-input NOR under the W rail, and two more bus lines

Matt Godbolt, on Claude Fable 5.2, 2026-11-27 10:57 -0600. Views in `cache/scratch/bc2/w3/` (`a_c`, `a_m`, `a_a`: y 15370-15595
in the clean, metal and chip-2 stripped shots, 5x; `b_c`, `b_a`: y 15590-15830; `ld`, `out_m`: the load end;
`j781`: the junction at (9245,15780); overlay `ov_a`) and `s1/` (the west channel south of unit 2).

### Piece `w3`: the NOR (7 transistors, no uncertain item)

    bc2_w15739 = NOR(bc2_p15520, busl_x7122, tc2_r5718, bc2_w15216, bc2_p15781, bc2_w15042)

- **Under the rail** (x 9463-9513; the clean shot is reliable there: `tools/bd2_umap.py 9440 15330 9580 15560 4 5`,
  `... 15560 ... 15750 4 4`, `... 15750 9660 15990 4 5`): one diffusion column x 9462-9506 from y 15382 to
  y 15830. Four lands with a contact to the rail: y 15382-15418 (9477,15400), y 15508-15547 (9478,15528),
  y 15638-15680 (9485,15660), y 15795-15830 (9475,15813) (`padc`: hole and ring each). Six salmon gate bands:
  y 15422-15440, 15482-15499, 15552-15570, 15612-15628, 15683-15702, 15770-15786. Between them three nodes: N1
  (y 15440-15482), N2 (y 15570-15612), N3 (y 15702-15770), each between two gates that lead to a land.
- **The three nodes are one.** Each has a diffusion neck east across the gap between the rail and the thin metal
  x 9545-9560: y 15461-15473, y 15591-15603, y 15734-15762 (in the gap, by trap 28's test on the centre line:
  `tools/px.py col 9530 15440 15492 3 metal,acid`, `col 9528 15570 15612 ...`, `col 9528 15700 15772 ...`:
  chip-2 metal plain with blue 80-93, stripped red - green 17-42, between two dark lines, field outside). The necks
  end in one wide diffusion strip x 9542-9590 from y 15457 south: tan under the thin metal
  (`bd2_umap`: `d` on x 9548-9566 from y 15460 to y 15790, pink field above y 15455), and east of the thin metal
  plain with stripped red - green 20-31 at x 9572-9584 (`tools/px.py row 15520 9516 9616 4 metal,acid`, `row
  15650`) inside an outline that starts at the corner (9597,15452) (`row 15440`: no line, field) and runs down
  x 9590-9597; field west of the thin metal (x 9524-9536: red - green -14..9).
  (Review round 8: the colour alone does not set the strip off from the ground east of it and above its outline,
  red - green 11-24 there against 17-29 inside; the closed outline, y 15455 and x 9594 into the tie box, carries
  the reading.)
- **No contact of the thin metal x 9552** (`bc2_e15343`'s) to the strip under it: the clean shot is plain tan at
  the follower's candidates (9552,15614) and (9552,15787) (R 192-200, G 166-180, no hole, no core).
- **Load** at the strip's south end: under the thin metal the strip runs to y 15797 and turns east at
  y 15770-15797 under a poly block (9572-9628, 15750-15818: three orange bands in chip 2's stripped shot, the
  strip's edges printing through at y 15768 and y 15800 and running on west of the block in the metal shot) onto
  the VCC land of the NAND `bc2_e15690` under the M rail (contact (9659,15746); `tools/bd2_umap.py 9626 15700 9704
  15810 3 4`: the land reaches x 9632 at y 15768-15790). W 27, L 56.
- **Tie**: a stem of the block runs north (x 9575-9598, open red-brown poly from y 15705) over the strip's
  south-east corner, in a framed box (9575-9598, 15722-15747) (views `ld`, `out_m`).
- **Output**: node N3 has an arm west out from under the rail, y 15733-15748 (`tools/px.py col 9447 15700 15776 3
  metal,acid`: plain, blue 88, red - green 20-34 between two dark lines), to a framed box (9402-9440,
  15727-15752) that holds the end of a poly row y 15732-15747 (`tools/px.py row 15740 9366 9470 3
  metal,acid,acid1b`: poly to x 9423 inside the frame, diffusion from x 9438: the same build as the first unit's
  middle box). The row runs west under the thin metal x 9399 (salmon, no hole) to a pad (9356,15739); a metal goes
  west and south from it (drawn to y 15800: port; `tools/follow.py 9330 15738 W`: south on x 9314 to y 15919,
  east to x 9363). No arm of this kind at N1 or N2 (the framed shapes in the gap there are in the clean shot
  only: plain in both metal shots).
- **The six gates' wires** (`tools/tl5_tracks.py rows row 9100 9470 8 15432 15491 15520 15562 15620 15651 15693
  15781`):
  1. y 15422-15440: a poly row from the west along y 15511-15530 (port at x 9160, placeholder `bc2_p15520`) to
     x 9320, north on x 9300-9320, east. It ends 20 px short of gate 2's pad (9357,15522).
  2. y 15482-15499: `busl_x7122`: bus line y 14481's leg x 9357 ends on the pad (9357,15522); its row east to
     x 9440, north on x 9412-9440, east.
  3. y 15552-15570: `tc2_r5718`: bus line y 14524's leg x 9270 ends on the pad (9270,15566); its row east.
  4. y 15612-15628: `bc2_w15216`: the second unit's output column x 9222-9240 runs on south to a pad
     (9226,15391); a thin metal south to y 15652 and east to a pad (9268,15652); its row east to x 9440, north
     on x 9415-9440, east.
  5. y 15683-15702: a poly row from the west along y 15772-15790 (port at x 9160, placeholder `bc2_p15781`),
     lengthwise under the metal of gate 6's wire without contact (salmon, no hole), to x 9242; north on
     x 9222-9242, east. It ends 13 px short of gate 6's pad (pink field between: view `j781`).
  6. y 15770-15786: `bc2_w15042`: the first unit's output metal x 9185 runs on south to y 15784 and east to a
     pad (9271,15784); its row east.
- The W rail is drawn on to y 15840; it goes on south (more lands and gate bands from y 15850: not drawn).

### Piece `bus4`: bus lines y 14524 and y 14481 end to end (wiring)

Built like the others (`tools/tl5_tracks.py h 14524 7540 9380`, `h 14481 ...`, `rows row ...`, `v 9270 14515
15575`, `v 9357 14472 15535`; `padc` on each pad): y 14524 is `busl`'s `tc2_r5718` (pads (7837,14524),
(8294,14524), (8641,14525); corner x 9270; south to the pad (9270,15566)); y 14481 is `busl_x7122` (pads
(7794,14481), (8250,14481), (8597,14481); corner x 9357; south to the pad (9357,15522)). Nine of the 13 lines
are now drawn end to end.

## Run 6 (2026-11-27), piece `dec`: where two of the three decode lines go (wiring; no join, no uncertain item)

Matt Godbolt, on Claude Fable 5.2, 2026-11-27 11:23 -0600. Views in `cache/scratch/bc2/w4/` (`e343`, `hop`: the south end of the
thin metal x 9552; overlays `ov_399`, `ov_517`) and `w1/` (`n_end`, `e_end`, `x9399`), `s1/` (`end399_m`,
`end399_c`). Connections unchanged (`tools/sameconn.py`): both wires only grow.

- **`bc2_e15517`** (low for R8 bits 7,6 = 0,1). Its metal x 10172-10191 runs on north from y 15290 to a corner at
  y 14740 and west onto a pad (10092,14740) (`tools/tl5_tracks.py v 10181 14720 15620`: metal in both chips from
  y 14740; it does not go on south of the turn at y 15608: `v 10181 15590 15720`). A poly row y 14731-14749 runs
  west (`tools/tl5_tracks.py rows row 8600 10200 12 14741`: poly from x 9416 to x 10150; no hole on it but the
  two pads': `h 14740 9380 10150`; `tools/eof_tee.py`: no branch) under the thin metals x 10052 and x 10007 and
  the E, M and W rails (review round 9: the M rail's metal is wide here, x 9552-9686 at y 14747 and north, undrawn
  north of y 14750; no thin metal x 9963 at this height) to a pad (9397,14740). **The bus metal of line y 14741 does not reach that pad**: no metal
  and no poly on the track from x 9106 to x 9390 (the bus line ends west of x 9100). A thin metal x 9392-9406 runs
  south from the pad (`v 9399 14725 15815`: no break in both chips at once), over the rows of the W rail's two
  units, of the six-input NOR and of its output without contact (review rounds 6, 7, 8), to y 15800-15814, west
  to x 9350, and ends on a pad (9357,15824) (hole in the clean shot, ring in both metal shots). The pad's poly
  goes south to a row y 15855-15875 that runs west (seen; not drawn: port).
- **`bc2_e15343`** (low for bits 7,6 = 0,0). Its metal x 10137 runs on north to a pad (10135,14783)
  (`v 10137 14760 15300`); a poly row y 14777-14793 west (`rows row 9540 10150 10 14785`: poly all the way; no
  branch) under the same thin metals and the E and M rails to a pad (9552,14785); a thin metal x 9545-9560 south
  (`v 9552 14770 15330`, `v 9552 15320 15800`: no break). It passes over the tie boxes of the W rail's units and
  lies lengthwise over the wide strip of the six-input NOR, without contact (review rounds 6, 7, 8). **Drawn to
  y 15835 (port).** Below that, measured but not understood: a contact pad at (9558,15860) (dark ring
  y 15845-15851, bright centre y 15857-15866 in both metal shots, a green centre in the clean shot) inside a
  framed box (9548-9568, 15848-15868) to which a poly row y 15847-15870 comes from a pad (9420,15862) in the
  west, and metal again on the same x from y 15884 to y 15932 over a diffusion. Whether the box is that row's
  end pad, a diffusion's contact, or both, is not read: the next piece.
- **`bc2_e15690`** (bits 7,6 = 1,0): not drawn further. Its metal x 10050 runs south to y 16125 and east along
  y 16118-16135 to x 10140, lengthwise over a poly row that runs from x 10040 to a pad (10180,16127); no hole
  under the metal's east end (view `e690`). Where its contact is, is not read.
- The other bus lines: the metals of lines y 14698 (`rst_c`) and y 14741 (`lc2_w8450`) end west of x 9100
  (`tools/tl5_tracks.py h 14698 8600 10200`: metal to about x 9079 and a leg at x 9093-9100; `h 14741`: to
  about x 9106), and line y 14785 (`lc3_w9947`) has no metal east of x 8600 but the piece `eof` drew: all three
  end in `bc1`'s region.

## Run 7 (2026-11-27), piece `w5`: an AND-OR-INVERT under the W rail (4 transistors; 3 uncertain items, one tie)

Matt Godbolt, on Claude Fable 5.2, 2026-11-27 11:42 -0600. Region x 9250-9700, y 15895-16140. Views in `cache/scratch/bc2/w4/`:
`s_c`, `s_m` (x 9390-9650, 4.9x), `w_c`, `w_m` (west of the rail, 5x), `l2_c`, `l2_m` (the load side, 6.5x),
`x2` (node X2), `pb_*` (the pad's south-west corner, 12x), `gc` (gate C's west end), overlay `ov5`.

    bc2_w16035 = NOT( bc2_p16067 OR (bc2_w15739 AND bc2_m15997) )        (depends on the tie, Ambiguity 12)

- **Under the rail** (clean shot; `tools/bd2_umap.py 9424 15836 9534 16140 3 4` and a column classed at x 9470,
  9480, 9492): south of the six-input NOR's land 4 the rail lies over field from y 15866 to y 15900, crossed by one
  poly row (y 15848-15862: not a gate, field on both sides; not drawn). Then one diffusion column x 9458-9503:
  land 5 (y 15908-15942; contact (9473,15917)), **gate A** (y 15946-15960), node X1 (y 15964-15986), **gate B**
  (y 15988-16004), node X2 (y 16008-16058), **gate C** (y 16060-16074), land 6 (y 16078-16134; contact
  (9480,16107): ring in both metal shots, pits). X1 and X2 have no contact (`padc` counts metal at (9480,16030),
  but view `x2` shows bright unringed metal over plain tan in both shots). So X2 is pulled to land 6 through C and
  to land 5 through A and B in series.
- **Gate A is `bc2_w15739`.** The six-input NOR's output metal runs on from its port: south on x 9314 to
  y 15919, east to x 9356 and south through a pad (9356,15955) (hole, ring; `tools/tl5_tracks.py v 9314 15790
  15930`, `v 9357 15900 16150`: no break but the pad; the metal goes on south past y 16150: port). The pad's row
  y 15946-15960 runs east under the thin metal x 9420 (no pad pattern, no hole) to the rail and ends at x 9524.
- **Gate B**: a row y 15988-16004 from a pad (9312,15997) (hole, ring in chip 1), the north end of a thin metal
  x 9305-9320 that comes from the south (`tools/follow.py 9312 16060 S`: 2,150 px, to (9552,17868)); under the
  thin metals x 9357 and x 9420 without contact (`cdp4/candh.py` flags (9422,15997) as pad-like, clean-shot
  minimum +37: a row's edges, no hole). Placeholder `bc2_m15997`.
- **Gate C** (corrected in review rounds 10 and 11): the band's west end is closed at x 9452 (field beyond); it
  runs on east past the rail's edge, turns south as a column x 9530-9549 (orange, unbroken in both metal shots,
  y 16062-16104) and east as a row y 16088-16106 under the thin metal x 9552 (no hole, no ring). **From x 9578
  to x 9631 that poly is the plate of another transistor** (review round 11): it runs on south to about y 16158,
  with one edge line at y 16110-16118 (the same in all four shots as the strip-edge line y 16016-16022 across the
  load above), channel-bright poly y 16118-16142, a second edge line y 16142-16148; a diffusion strip
  y 16116-16142 leaves it east onto the VCC land and west (tan x 9564-9574). So `bc2_p16067` is the gate of a
  pull-up from VCC, the load of the next gate south, whose tie and output are not read. Drawn to the plate's
  west edge x 9578 (port); the plate and its strip are the next piece.
- **Load.** X2 leaves the rail east at y 16022-16048 (`tools/px.py row 16035 9500 9650 3 metal,acid,acid1b`):
  diffusion across the gap (plain, blue 82-86), tan under the thin metal x 9545-9560, to x 9575; then under a
  poly x 9579-9628 (orange in the open, salmon under the thin metal x 9594-9608) onto a VCC land under the M rail
  (9635-9691, 16026-16072; contact (9663,16043)). W 26, L 49.
- **The load's gate** is the south part of a poly pad (9540-9628, 15978-16050): `tools/px.py col 9620 15970 16062
  3 metal,acid,acid1b` has poly from y 15982 to y 16045 with one dark line at y 16018-16021, the strip's north
  edge printing through (two polys would show a gap). The pad has a contact (9597,15995) (hole, ring in both
  chips), from which a thin metal x 9594-9608 runs south (`v 9600 15970 16210`: to about y 16173; drawn to
  y 16060: port).

### Ambiguities (run 7)

12. **The tie of the load** (`?D 9541,15996:9561,16024`, `?P 9541,15990:9561,16014`, `?B 9538,15992:9564,16020`;
    moved in review round 10). It is the framed box (9538-9564, 15992-16020) at the pad's south-west corner,
    under the thin metal x 9552: heavy east and west frames that the field control at y 15958 lacks, a weak
    south line onto the strip, the pad's top band on its north: the first unit's tie, mirrored. The overlap of
    poly and diffusion inside it cannot be resolved (its centre in chip 2's stripped shot is grey, not
    poly-coloured like the control), hence `?`. The first reading (a finger at x 9566-9578) was wrong: an edge
    line crosses its foot at y 16016-16022 and the pocket reads field.
13. *(Closed in review round 10.)* **X2's exit west**: the arm (x 9441-9457, y 16016-16047, no edge line inside,
    stripped red - green 16-37 as on the strip east) and the buried contact of the row y 16040's end on it are
    confirmed by the reviewer (the box has the x-structure of the six-input NOR's output box: frames x 9402-9414
    and x 9429-9438, interior x 9414-9426) and are drawn firm. So X2 leaves on the poly row y 16031-16049 west
    to a pad (9270,16041), the north end of a thin metal going south (`tools/follow.py`: to y 16351).
    **The thin metal x 9415-9430 has NO contact on that box** (drawn as one before the review: wrong).

**Read and NOT drawn** (measurements in `cache/scratch/bc2/w1/notes.md`, last sections; verdicts of review round
10 below): (a) the thin metal x 9552 of `bc2_e15343` passes over the tie box (9538-9564, 15992-16020) and over the
box (9548-9568, 15848-15868) further north **without contact** (reviewer; the tracer's first reading of both as
contact pads was wrong); its continuity over the first cannot be shown from the metal shots (dark y 15992-16006
and y 16010-16029). Whether it ends at y 16104 over gate C's poly row is not shown (review round 11): both
chips are dark from y 16104 to y 16142 and bright again on the same line from y 16142, over a dark-framed tan
block (9550-9558, 16118-16137); on the row itself nothing is visible (no hole, no ring, the metal not widened). (b) The vertical poly x 9507-9529, y 15895-15932
is one poly with gate A (reviewer: one 7 px line at y 15933-15939 with orange poly on both sides) and is a gate
between land 5 and the diffusion (9536-9575, 15885-15932): `bc2_w15739` gates a second pull-down, not drawn yet
(the next piece), whose node has a poly block (9579-9628, 15890-15935) and the M rail's land east of it and a
framed box (9548-9568, 15848-15868) north of it at which a poly row from the pad (9420,15862), the block's stem
and a diffusion finger meet.

## Run 8 (2026-11-27), piece `w6`: the second pull-down of `bc2_w15739` (2 transistors; 4 uncertain items, one box)

Matt Godbolt, on Claude Fable 5.2, 2026-11-27 12:36 -0600. Region x 9400-9700, y 15840-15945. Views in `cache/scratch/bc2/w4/`:
`k_acid1b`, `k_metal`, `k_acid` (8x), `pa_*` (the box, 12x, four shots), `hop` (the row from the west, three
shots), `r_c`, `r_m`, overlay `ov6`.

    bc2_w15915 = NOT bc2_w15739                 (depends on the tie, Ambiguity 14)

- **The gate** is a branch of gate A's poly north along the rail's east edge, x 9507-9529, y 15898-15946
  (`tools/px.py col 9516 15868 15972 3 metal,acid,acid1b`: salmon y 15901-15931, one dark line y 15934-15940,
  salmon again from y 15943: one poly, the line a diffusion edge; review round 10 read it so independently: one
  7 px line with orange poly on both sides at x 9524). West of it land 5 (tan to x 9503), east of it a node:
  `tools/px.py row 15915 9450 9644 3 metal,acid,acid1b`, `row 15903`, `row 15928`: tan from x 9536 to x 9573,
  the two dark lines inside it (x 9543, x 9564) being the edges of the thin metal x 9545-9562 that lies over it.
  The poly is brighter over the channel (241-243 at y 15904-15925 against 187-225 at its ends). W 31, L 22 (review round 13: the active strip is y 15901-15932; the branch has an end cap to y 15884).
- **The node** (9536-9574, 15898-15934): tan under the thin metal x 9552 of `bc2_e15343`, which has no contact
  to it (plain tan 186-198 / 152-174 down x 9558 from y 15884 to y 15926; the metal not widened; review round 10).
  Field south of it (pink under the metal from y 15941).
- **Load**: the node's band y 15907-15934 runs east under a poly block x 9579-9628, y 15890-15938
  (`tools/px.py col 9605 15880 15948 ...`, `col 9622 ...`: poly from y 15892 to y 15956 with two dark lines, y 15904-15910 and
  y 15934-15938, the band's two edges: corrected in review round 13, the tracer had the second as the block's bottom) onto the VCC land under the M
  rail (`tools/bd2_umap.py 9626 15880 9704 15975 3 4`: the land reaches west to x 9635 at y 15904-15932;
  contact (9662,15938), drawn in run 3, whose review noted it as "probably the supply end of an undrawn load
  west of the M rail"). W 27, L 49.
- **The block's stem** runs north, x 9579-9600, to y 15850 (`tools/px.py col 9588 15838 15945 ...`: orange poly
  from y 15853 to y 15901 without a line: one poly with the block); a dark frame closes it at y 15845.
- **The row from the west**: a pad (9420,15862) (hole in its middle, ring in both metal shots: `padc`; it is the
  north end of the thin metal x 9415-9430, which goes south: no metal north of it) with a poly row y 15849-15865
  east: open poly x 9440-9455, salmon under the rail (over field: land 4 ends at y 15830 and the column starts
  again at y 15908, so it is no gate), orange in the gap to x 9538
  (`tools/tl5_tracks.py rows row 9400 9560 5 15857`; `tools/px.py row 15858 9432 9582 3 ...`).

### Ambiguities (run 8)

14. **The box (9548-9568, 15848-15868): the node's tie and its exit** (`?D 9553,15862:9567,15900`,
    `?P 9562,15850:9582,15866`, `?P 9538,15850:9556,15866`, `?B 9548,15848:9568,15868`). A diffusion finger
    runs north from the node (tan x 9555-9566 at y 15890; a pale box y 15870-15880; green in chip 2's stripped
    shot at (9557,15874)) into a framed box, at which the stem (from x 9578 in the east) and the row (to x 9538
    in the west) both arrive: 12 px of frame lie between the row's end and the box's middle, 15 px between the
    middle and the stem. Review round 10: "row, stem and a diffusion finger meet at it; whether row and stem
    each join cannot be told." Drawn: both join (the stem makes the block a tied load; the row takes the output
    west to the pad (9420,15862) and the thin metal x 9420). If only the stem joins, the gate has no exit; if
    only the row joins, the block is a pull-up gated by something else. The thin metal x 9552 passes over this
    box without contact (review round 10: no hole, the box's interior off-centre from the metal).

## Run 9 (2026-11-27), piece `w7`: two series gates under the W rail, and four thin metals' routes (2 transistors, no uncertain item)

Matt Godbolt, on Claude Fable 5.2, 2026-11-27 13:01 -0600. Region x 9250-9640, y 15900-16365. Only what is firm is drawn; what is
seen and not read is listed at the end. Views in `cache/scratch/bc2/w7/`: `g_c`, `g_m` (the gates, 6.5x),
`gw_c`, `gw_m` (the rows' west ends), `end420` (the end of the thin metal x 9420), `p270`, `p600` (two end
pads), `e_acid1b`, `e_acid`, `e_metal` (east of the rail, 7x), overlay `ov7`.

- **Under the rail** (clean shot; `tools/bd2_umap.py 9424 16132 9534 16260 3 4`, `... 16256 ... 16330`, and
  columns classed at x 9470, 9482, 9494, 9504): south of land 6 the rail lies over field (y 16138-16168). Then a
  diffusion column x 9458-9508: a node (y 16170-16195), **gate D** (y 16198-16216), a node (y 16220-16242),
  **gate E** (y 16244-16264 at x 9490, stepped 6 px lower west of x 9475), land 7 (y 16268-16330 and on; contact
  (9476,16290): a dark dot in the clean shot, ring and bright centre in the metal shot, pits below it). The upper
  node has no contact (plain tan; bright mottled metal without a ring). So the upper node, placeholder
  `bc2_w16182`, is pulled to ground through D and E in series.
- **Gate D is `bc2_m15997`.** The thin metal x 9305-9320 (from the pad (9312,15997), gate B of `bc2_w16035`)
  runs on south (`tools/tl5_tracks.py v 9313 15990 16260`) through a pad (9313,16215): ring and bright centre in
  both metal shots, a green hole in the pad's middle in the clean shot (6 of 9 samples of the middle 7 x 7 px green,
  against 9 of 9 at the certain contact (9356,15955) and 0 of 9 at the pass-over (9421,16040)); the metal goes on
  south (port at y 16250; `tools/follow.py`: far south). The pad's row y 16204-16222 runs east
  (`tools/tl5_tracks.py rows row 9240 9470 6 16208`; no branch: `tools/eof_tee.py`) under the thin metals
  x 9357 and x 9420 without contact (no hole; the dark ring at (9378-9402, 16205-16220) in the clean shot lies in
  a gap between two metals and has plain orange poly in the metal shot) to the rail.
- **Gate E is `bc2_w15915`** (through run 8's `?B`). The thin metal x 9415-9430 from the pad (9420,15862) runs
  south (profile down x 9423 from y 16050 to y 16290 in both chips and the clean shot: metal but for 6-10 px
  ridges at the rows it crosses, over field or plain salmon, no hole; wider, 17-18 px, at y 16068-16074 over
  field) and ends by a step west on a pad (9407,16262): a green hole in the pad's middle (9 of 9), ring and bright
  centre in chip 2's metal shot. The pad's row y 16250-16270 runs east to the rail, stepping up 6 px at x 9475.
- **The node's neck east**: y 16170-16184 across the gap (`tools/px.py row 16176 9500 9584 3 metal,acid,acid1b`:
  plain, blue 83-91, stripped red - green 15-29 at x 9521-9539, against 7-10 at y 16150 and 1-9 at y 16232;
  `col 9528 16100 16220 4`: the two edge lines at y 16160-16168 and y 16184-16188) into a tan block under the
  thin metal x 9552 (`tools/bd2_umap.py 9504 16096 9584 16216 3 4`). Drawn to x 9542: port.
- **`bc2_w16035`'s two exits to their pads** (wiring): the thin metal x 9600 runs south to its end on a poly pad
  (9580-9625, 16180-16215) with a contact (9597,16197) (`v 9600 16000 16215`: ring y 16174-16192 and
  y 16201-16214 round a centre with a hole; 9 of 9); the thin metal from the pad (9270,16041) runs south to a pad
  (9270,16345) (ring, bright centre, hole: view `p270`), whose poly row y 16336-16354 goes east (drawn to
  x 9345: port).

**Seen and NOT drawn** (not read to the standard of a drawing):
- the block under the thin metal x 9552 that the neck enters (about 9540-9575, y 16116-16240): it reaches the
  strip under the plate of `bc2_p16067` (y 16116-16142) in the north; under the thin metal at y 16104-16142 both
  chips are dark over tan without a hole (a framed box: a tie of gate C's poly onto this block?); a poly row
  y 16240-16262 crosses its south part. If the box is a tie, `bc2_p16067` is this node and the plate is its
  load: `bc2_p16067` = NAND(`bc2_m15997`, `bc2_w15915`). Not drawn, not claimed.
- the east ends of bands D and E at the rail's edge (x 9514): in the gap beyond stands a rounded outline
  (9518-9535, 16192-16268) that is plain in chip 2's metal shot and olive in its stripped shot; whether either
  band runs on into it is not read.
- a dark dot at (9447,16233) in the clean shot, in a tan patch west of the lower node (no metal over it).
- a tan block west of the rail at (9390-9455, 16285-16330) beside land 7.
- the poly leaving the pad (9580-9625, 16180-16215) south (x 9600-9620, to about y 16260).

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

### Round 5 (full review), 2026-11-27: run 3, piece `inv7`

A fresh Claude Fable 5.2 agent, on commit 3370fb2, 12 images in `cache/scratch/bc2/review-5/`. Told to suspect:
the join of the tie strip to the output land under the rail's edge line (Ambiguity 10) and any other place the
load's band could meet the output, the strip and its box, whether the load is one poly block, the three pads and
their metals' directions, the band and the output poly east of the rail, and anything undrawn on these nets.

**No finding changes a connection.** Three geometry remarks, all fixed:

- the gate band is y 15857-15879, not 15856-15872 (clean shot at x 9844 salmon y 15858-15876; orange y 15860-15877
  east of the rail in chip 2's shots): L about 21, not 16;
- the load block's west end is x 9691 under M's margin, not 9698;
- the VCC land runs on south under M to about y 15966 with a second contact (9662,15938) (hole in the clean shot,
  ring in both metal shots; `tools/bd2_umap.py 9640 15896 9700 15984 4 4`): drawn; the M rail drawn on to y 15980.

**Ambiguity 10: the join stands**, on the reviewer's own evidence: chip 1's metal shot has no extra edge at the
junction (at y 15901 / 15907 the rail's edge line is no wider or darker than beside plain field, while at y 15876
and y 15928 it is 6 px wider westward); the clean shot's rows y 15901 / 15907 have no green field strip (the mirror
image of the tab's crossing at the rail's east edge); and the direct alternative is out (x 9808-9822,
y 15856-15880 is the band's poly end cap, the land's west edge x 9824 is dark in all shots, pink field at
y 15882-15896). The 6 px under the edge line themselves stay unseen.

Checked and found correct by the reviewer: the strip is diffusion y 15865-15928 with no crossing line; the tie box
and the output box match the pilot box; the load is one poly block and the VCC land enters under it with no field
between; no contact on the output land; three pads with contacts, no metal north of either upper pad, the x 9963
metal continuous y 15936-16042; field between the band and the output poly; nothing undrawn touches these nets.
Not checked: the x 10007 metal south of y 16000; the poly leaving the pad (9963,16062).

Connections before and after the fixes (commit 3370fb2 against the fixed tree):

    tools/t.sh bc2 sameconn.py 3370fb2            ->  connections identical
    .venv/bin/python tools/sameconn.py 3370fb2    ->  connections identical

Recorded 2026-11-27 09:17 -0600.

Round 5: no findings that change a connection.

### Round 6 (full review), 2026-11-27: run 4, pieces `bus3` and `w1`

A fresh Claude Fable 5.2 agent, on commit 1e94299, 19 images in `cache/scratch/bc2/review-6/`. Told to suspect, for
`w1`: whether there is a diffusion column at all and on which side of the line x 9445-9448; the two `?D`; the
middle box (buried contact, a third gate, or a row ending short); a contact of the thin metal x 9552 at
(9552,15097); the finger and the tab; the strip under the block to the VCC land; the lands; contacts of the
vertical metals to the three rows; no metal between the pads (9183,14977) and (9183,15043). For `bus3`: a step of
one track, each pad, contacts from the rows and underpasses to the metals above, the corners and legs, the pad
(9140,14826) on the leg, the row y 14815-14832.

**No finding changes a connection.** The extraction's `bc2_w15042` = NOR(`lc2_w9079`, `lc3_e9756`) stands.

- **The two `?D` are firm** (the reviewer's own evidence, by another route than the tracer's). The column's WEST
  outline is readable in the clean shot under the thin metal's margin: at y 15016, 15022, 15066, 15070 a heavy
  outline at x 9406-9410 and tan at x 9414-9418 (182/163/104, 167/158/114), identical to the arms (y 14976, 15110),
  where the field rows y 14950 and y 15126 are pink through x 9412 (`tools/px.py row Y 9398 9426 2 acid1b`;
  `tools/bd2_umap.py 9384 14936 9420 15130 3 4`). And there is no boundary against the strip:
  `tools/px.py col 9442 14960 15124 3 metal,metal1,acid` is unbroken plain from y 15017 to y 15068 in all three
  shots (minimum 128, an edge dips below 80): the line x 9445-9448 turns east into the strip's edges, so both
  stretches are one region with the strip. Drawn now as one `D` from arm to arm. Ambiguity 11 closed.
- **Column position: correct**, west of the line: the pocket x 9450-9460 is field, the rows' caps end at x 9460.
- **Middle box: a buried contact, not a gate**: its interior is plain (154/126/69, 136/121/59, against
  170/124/58 and 145/86/50 on the gate rows); east of it a neck x 9439-9446 is diffusion with no poly (blue 78-83),
  so the row does not cross the column; the row is salmon under the thin metal up to the frame.
- **(9552,15097): no contact**: the metal keeps its width there (bright x 9547-9557, as at y 15047); the clean shot
  has no hole or core (204/162/128 to 197/175/116) where the pad (9552,14785) has a 40 px ring and a dark core
  (77-103); chip 2's stripped shot shows the same orange ghost as over the finger, not a pitted box; the box at
  (9552,15270) looks identical. The finger is tan and continuous with the strip; the tab's open poly
  (x 9569-9580, y 15090-15105) reaches the frame.
- Geometry, all fixed: the column's west edge is about x 9408 (W about 38, not 30); the strip is y 15035-15053
  west of the thin metal and about y 15036-15063 under the block; the block's bottom is about y 15105; the pad
  (9183,14977) and its row overlapped by only 3 px as drawn.

Checked and found correct. `w1`: both lands and contacts, both arms joined; the strip unbroken under the rail, the
gap x 9520-9538 and the thin metal, with no contact; the block touches nothing else; no hole or pad at any crossing
of x 9225, 9268, 9311, 9355, 9399 or of x 9183 over the lower row; bare ground between the pads (9183,14977) and
(9183,15043); the leg x 9141 ends on (9141,15087); no poly west of the three pads. `bus3`: metals unbroken with no
step (only 8-9 px ridges); rows and underpasses straight, no break over 5 px, no branch; all pads contacts;
corners y 14611 at x 9184 and y 14654 at x 9141; no hole over `eof`'s rows or at the corners; the leg passes
through (9140,14826); the row y 14815-14832 unbroken to x 9872 with no hole. Not checked: that the W rail is
ground (only that it is separate from the M rail at y 14540-14880); the output metal south of y 15130; the thin
metal's other boxes; `busl`'s side of x 7545 and `eof`'s rows themselves.

Connections before and after the fixes (commit 1e94299 against the fixed tree):

    tools/t.sh bc2 sameconn.py 1e94299            ->  connections identical
    .venv/bin/python tools/sameconn.py 1e94299    ->  connections identical

Recorded 2026-11-27 10:03 -0600.

Round 6: no findings that change a connection.

### Round 7 (full review), 2026-11-27: run 4, piece `w2`

A fresh Claude Fable 5.2 agent, on commit 3e2c859, 20 images in `cache/scratch/bc2/review-7/`. Told that the
cell's master stands and that what is unchecked is whether the copy fits the second unit, and the unit's own
wiring; to suspect: every feature of the copy against the photo, the edge line x 9445-9448, both arms' joins to
their lands (land 2's second arm), the middle box, a contact of the thin metal at (9552,15270), the strip's end
on the M rail's land, anything the first unit does not have; bus line y 14568, its pads, its leg's crossings and
its end; the inverter's output row to the pad (9314,14870), the thin metal x 9313 and its crossings; the output
row's turn south and its clearance from the pad (9227,15173).

**No findings.** Geometry within 3-4 px everywhere measured; nothing changed in the trace.

Checked and found correct by the reviewer. The copy: the edge line dark in both metal shots at y 15172, 15194,
15240, 15260 and absent at 15150, 15215, 15283; the column tan in the clean shot under the thin metal's margin
on both arms, both stretches and the box, against grey field at y 15130 and y 15302 on; both arms join their
lands (the land's west edge line x 9454-9458 present on the field rows y 15128, 15306, absent on the arm rows
y 15150, 15284), field between land 2's two arms; the middle box a buried contact (poly ends at x 9418-9426
inside a heavy frame, plain diffusion east of it); the strip tan under the W rail and the thin metal, reaching
the M rail's land at x 9635-9645 only on rows y 15211-15232; no contact at (9552,15270) (tan, no hole or core,
the metal does not widen); nothing extra against unit 1. Upper input: three pads are contacts, row and underpass
straight on y 14568, metal continuous in both chips over x 7819-8229 and x 8623-9235 and down the leg to the pad
(9227,15173), no pad or hole at any crossing, no metal beyond the corner or south of the pad. Lower input: the
row poly and unbroken from x 9872 to the pad (9314,14870) with no hole or ring under the three rails and the
thin metals and no branch; the thin metal x 9313 continuous y 14891-15239, ending on both pads. Output: the row
turns south at x 9222-9240, plain field between it and the pad's ring at y 15198-15204 in all four shots, field
west of x 9218. Beyond the piece: the output column runs past its port to a pad with a contact at about
(9228,15388), a thin metal going on south. Not checked: `busl` west of x 7530; the thin metal x 9552's own
continuity over the tie box; the rails' supply identity; the W rail north of y 14860 and south of y 15330.

Recorded 2026-11-27 10:42 -0600.

Round 7: no findings.

### Round 8 (full review), 2026-11-27: run 5, pieces `w3` and `bus4`

A fresh Claude Fable 5.2 agent, on commit 6871ead, 24 images in `cache/scratch/bc2/review-8/`. Told to suspect,
for `w3`: the three necks and the wide strip (one net? diffusion or a poly wire? how wide), a contact of the thin
metal x 9545-9560 to the strip, whether all six bands are gates and the column continuous through them, the load,
the tie box and the stem, the output box (buried contact or gate) and any other exit of the net, the two gaps
(gate 1's corner against the pad (9357,15522); gate 5's row end against the pad (9271,15784)), the L turns, the
pads, contacts at the rows' crossings, and a missed transistor in the gap west of the rail. For `bus4`: pads,
track steps, contacts to the metals above, corners and legs.

**No finding changes a connection.** Verdicts, on the reviewer's own evidence:

- **Necks and wide strip: one net.** `tools/px.py row 15466 / 15595 / 15745`: the clean shot tan to x 9518 and
  from x 9542, and between them both metal shots plain with no edge crossing; the necks' centres are diffusion,
  not poly (chip 2 blue 81-93, chip 1 green 114-118). Under the thin metal the strip is unbroken tan y 15464-15784,
  pink field above y 15458; east of it no line crosses x 9580 from y 15464 to y 15710.
- **Thin metal x 9545-9560: no contact** (`tools/textmap.py` over y 15440-15830 against the pad (9552,14785): no
  ring, no widening, no hole; a dark notch at y 15533-15545 is in chip 2 only).
- **Gate 1's corner and the pad (9357,15522): separate** (plain ground at x 9330-9338 in both metal shots, green
  in the clean shot, unbroken y 15495-15550). **Gate 5's row and the pad (9271,15784): separate** (pink field at
  x 9247-9256 under the metal on rows 15776 / 15781 / 15786; the salmon poly ends at x 9235).
- **Output box: a buried contact; the arm is joined to N3** (both metal shots plain at x 9442-9457; the clean
  shot's dark line at x 9454 is the rail's margin edge, absent from the other three shots); the row ends on the
  pad (9356,15739), which has ring and hole.

Geometry, fixed: N1's neck is y 15458-15476 and N2's y 15587-15603 (drawn 12 px each); N3's neck has no south
edge in the gap: at x 9530-9545 diffusion runs y 15730-15795, round the east end of gate 6's poly (drawn; land 4
stays separate, field at x 9512 from y 15798); the tie box's frame is x 9568-9600, y 15718-15748 in three shots
and the "stem from y 15705" shows in the clean shot only (stem drawn from y 15718). And the notes' "field
outside" for the strip east of the thin metal was stronger than the colours allow (corrected above).

Notes: the pad (8641,14525) has no green hole in the clean shot; its contact rests on ring and bright centre in
both metal shots and a pitted box in chip 2's stripped shot. The thin metals x 9399 and x 9552 are drawn by no
package at y 15290-15840; x 9399 is dark over the output box's west frame at y 15720-15756 (trap 27) and has no
contact to any of the six rows or the output row.

Checked and found correct. `w3`: six gate bands, four contacts, no seventh band, no contact on a node; the
patches in the gap west of the rail are field (no missed pull-down); every pad has a contact and nothing leaves
it beyond what is drawn; no contact at any row crossing under x 9185, 9228, 9270, 9314, 9357 or on the
lengthwise row y 15772-15790; load, VCC land tab and the three L turns as drawn; no hidden branch
(`tools/eof_tee.py`). `bus4`: six pads with contacts, no track step, no contact to the metals over rows or
underpasses; corners at x 9270 (y 14524) and x 9357 (y 14481), nothing beyond; legs continuous to their end pads.
Not checked: poly continuity exactly under the rail's west edge line (x 9453-9462); the legs at 5x along their
length; the south ends of the thin metals x 9552 and x 9399; the sources of `bc2_p15520` and `bc2_p15781` (both
run on west past x 9040); the rails' supply identities.

Connections before and after the fixes (commit 6871ead against the fixed tree):

    tools/t.sh bc2 sameconn.py 6871ead            ->  connections identical
    .venv/bin/python tools/sameconn.py 6871ead    ->  connections identical

Recorded 2026-11-27 11:14 -0600.

Round 8: no findings that change a connection.

### Round 9 (full review), 2026-11-27: run 6, piece `dec`

A fresh Claude Fable 5.2 agent, on commit c8ed645, 13 images in `cache/scratch/bc2/review-9/`. Told to suspect: a
contact from either poly row to a metal above it, a link between the two rows, a contact along the thin metals
x 9399 and x 9552 where earlier reviews had not looked (with the caveat that a thin metal over a row's edges or
a framed box looks like a pad in the metal shots), each of the five pads and what leaves it, the corner
(10181,14740), and the claim that the bus metal of line y 14741 does not reach the pad (9397,14740).

**No finding changes a connection.** Geometry, fixed: the arm of `bc2_e15517`'s metal west onto its end pad is
y 15797-15808 (drawn on y 15807; now y 15802). Description, corrected above: there is no thin metal x 9963 at
y 14740 / 14785, and row A lies under a wide metal from x 9552 to x 9686 (the M rail's metal, wider there), with
no contact (metal unbroken in both chips, no hole; a thin diagonal mark at (9670,14741) is in the clean shot
only).

Checked and found correct by the reviewer: all five pads are contacts, and nothing else leaves them (no metal
north or west of (9397,14740) or (9552,14785); only the undrawn poly south of (9357,15824)); no metal north or
east of the corner (10181,14740), the metal x 10181 continuous y 14737-15617 with no widening or hole and nothing
south of y 15618; about 10 px of bare ground between that arm and the pad (10135,14783); the two rows straight
under the E, M and W rails and x 10007, x 10052, field between them throughout, no branch, pad or channel; the
thin metal x 9399 never widened and without a hole from y 14760 to y 15800 (rows y 14823, y 14869 and
y 15280-15420 viewed); the same for x 9552, the boxes (9552,15097) and (9552,15270) passed over; the bus metal of
line y 14741 turns south at x 9085-9105, and from there to x 9390 the track holds only crossing vertical metals
and bare ground. Not checked: x 9552 below y 15835 and the poly south of (9357,15824); x 9399 at y 14990-15270
and y 15420-15790 by text scans only.

Connections before and after the fix (commit c8ed645 against the fixed tree):

    tools/t.sh bc2 sameconn.py c8ed645            ->  connections identical
    .venv/bin/python tools/sameconn.py c8ed645    ->  connections identical

Recorded 2026-11-27 11:34 -0600.

Round 9: no findings that change a connection.

### Round 10 (full review), 2026-11-27: run 7, piece `w5`

A fresh Claude Fable 5.2 agent, on commit 79b0b7e, 13 images in `cache/scratch/bc2/review-10/`. Told what was
drawn firm (the column and its three gate bands, the rows of A and B and their pads, gate C's band, the strip
east, the load, the pad and its contact), what was drawn `?` (the tie at x 9566-9578; the exit west with a
contact of the thin metal x 9420), and asked for independent verdicts on things read and not drawn (the thin
metal x 9552 at (9552,16007) and (9558,15860); the vertical poly beside land 5).

**Two findings change a connection; both fixed:**

- **F1. `C 9421,16040` was not a contact.** The "pad" is a framed box with the x-structure of the six-input
  NOR's output box, which has no metal over it; clean-shot interior tan (red - green +24..+33), only its south
  rim green (as that box's and the gate bands'), where the certain contact (9356,15955) has a 12 px hole of
  -10..-27 in a 34 px pad; chip 2's stripped shot centre red - green 57-68 (pass-over control (9552,15097): 72;
  certain contacts 4-32); the metal is 10 px wide at the box and 16 px at y 16067: no pad. The contact and the
  metal stub are taken out: the thin metal x 9420 is not on the row y 16040 or on X2. (The tracer's evidence had
  been `candh`'s flag and a clean-shot minimum of -17, which was the rim.)
- **F2. Gate C's open end was on the wrong side**: closed at x 9452 in the west; the band runs on east and south
  (now drawn: see the piece's notes). The port moved from (9447,16067) to (9632,16097).

Verdicts on the questions: the pad and the block are **one poly** (the line y 16018-16022 is 7 px, identical to
the strip's south-edge line y 16048-16052; geometry: the block ends at about y 16064); **no tie finger at
x 9566-9578** (field; an edge line across its foot): the tie is the framed box under the thin metal (moved, kept
`?`: Ambiguity 12); **the arm west and its buried contact: yes** (now firm: Ambiguity 13 closed); **no contact of
the thin metal x 9552 at (9552,16007)** (clean interior tan 186-194/151-172, no hole, where the certain contact
(9140,14826) reads green 105-142/111-141; metal 10-12 px, no pad) and **a pass-over at (9558,15860)** (the box's
interior is off-centre from the metal, no hole, stripped red - green 50-70); **the vertical poly beside land 5
is one poly with gate A and is a gate** (not drawn in this piece). Geometry, fixed: the arm is x 9441-9457,
y 16016-16047; the VCC contact is centred about (9660,16048).

Checked and found correct: the column under the rail (lands, A, X1, B, X2, C), its two contacts, no contact on
X1 or X2, no fourth band, field east and west of X1; the pads (9356,15955) (metal through), (9312,15997) and
(9270,16041) (metals' north ends); the row y 16040 ends at its box; no holes where the rows of A, B and y 16040
pass under x 9312, 9357, 9420; the strip east, the load (L about 54), the contact (9597,15995) at the metal's
north end. Could not check: the thin metal x 9552 at y 16104-16142; the pad (9420,15862); gate C's row east of
x 9630; land 6's contact (text map only).

Lesson for the tracer (also for the guide's trap 27): `candh`'s "PAD" and a negative clean-shot minimum are not a
contact when the box under a thin metal has a green RIM; the test is a hole in the box's middle and a widened
metal.

Connections before and after the fixes (commit 79b0b7e against the fixed tree; the removed contact joined
only a stub of its own, so the extraction's nets do not change):

    tools/t.sh bc2 sameconn.py 79b0b7e            ->  connections identical
    .venv/bin/python tools/sameconn.py 79b0b7e    ->  connections identical

Recorded 2026-11-27 12:05 -0600.

Round 10: two findings that change a connection (a contact that is not one; a wire's open end), fixed. Fix check next.

### Round 11 (fix check), 2026-11-27: run 7, piece `w5`

A fresh Claude Fable 5.2 agent, on the changes 79b0b7e..70a523a only, 12 images in `cache/scratch/bc2/review-11/`.
Asked to check: gate C's corrected route and its no-contact claims, and what is seen where the thin metal x 9552
ends; the load's gate poly to y 16064; the tie's box; the exit west drawn firm and the removal of the contact
(9421,16040); the VCC contact.

**One finding changes a connection, fixed:** the "row east" of gate C drawn to a port at x 9632 is not a wire.
Its east end is closed at x 9631, and from x 9578 to x 9631 the poly runs on south to about y 16158 as the plate
of a transistor: one edge line y 16110-16118 (width, depth and colours in all four shots those of the strip-edge
line y 16016-16022 across the load above: `tools/px.py col 9622`, `col 9601`), channel-bright poly
y 16118-16142, a second edge line y 16142-16148, a lip to y 16158, then field; a diffusion strip about
y 16116-16142 leaves it east onto the VCC land (whose edge steps from x 9646 to x 9634 there, as at the upper
strip) and west (tan x 9564-9574). So `bc2_p16067` is the gate of a second, undrawn pull-up from VCC. The row is
now drawn only to the plate's west edge (x 9578), and the port says what it is.

The rest holds: gate C's west end closed at about x 9450; band, column and row one poly (the column is
x 9530-9549: drawn so); no contact at x 9594-9608 and none visible at the thin metal x 9545-9560 on the row.
**B** correct (the plate ends at y 16062-16064, pink field y 16066-16084 before the row; the top band continuous
salmon x 9542-9590). **C**: the box is where drawn (frames x 9536-9544 and x 9556-9564, y 15994-16002 and
y 16012-16020), interior tan, no hole, the metal not widened: nothing contradicts a tie. **D** correct (the arm
x 9442-9456 matches the strip east in all four shots, tan on to x 9430; the row's poly orange to x 9400; the box's
centre without a hole and the metal 10 px wide: no contact; gate C's band stays clear). **E** correct
((9660,16048) lies inside the rail's slot contact (9652-9675, 16040-16120); the land runs on south past y 16150).

Connections before and after this fix (commit 70a523a against the fixed tree; a wire's drawn end moved, no net
changes):

    tools/t.sh bc2 sameconn.py 70a523a            ->  connections identical
    .venv/bin/python tools/sameconn.py 70a523a    ->  connections identical

Recorded 2026-11-27 12:22 -0600.

Round 11: one finding that changes a connection (a wire's end is a transistor's plate), fixed. Last fix check next.

### Round 12 (last fix check), 2026-11-27: run 7, piece `w5`

A fresh Claude Fable 5.2 agent, on the one change 70a523a..b13214a, 5 images in `cache/scratch/bc2/review-12/`.
Asked: is gate C's row right as drawn to x 9578 and free of contacts; is the statement about what lies beyond
(the plate of a transistor) right; is the column's new x right.

**No findings.** The column runs into the row with no edge line (x 9535, y 16076-16104 orange in both metal
shots); the row is continuous to x 9578 (salmon under the thin metal, orange in both metal shots at x 9568-9588);
the thin metal x 9552 has no contact on it (edge minima at x 9542 / 9564 at y 16060, 16097 and 16150: no pad; no
green hole, the same colours as at the x 9600 crossing); no branch (`tools/eof_tee.py`). Beyond x 9578: field
south of the row at x 9571 and x 9576, none at x 9583; poly y 16088-16158 at x 9583, 9602, 9622, crossed only by
single 6-8 px edge lines at y 16114 and y 16144, the band between brighter; tan diffusion west (x 9565-9574) and
east (x 9636 on): the net is that transistor's gate. The column's west edge is x 9528-9530. Noted for whoever
draws that transistor: the thin metal x 9552 is dark in both chips over y 16104-16140, over the strip's west
end, and no tie was looked for, so "load" is unproven. Nothing changed in the trace.

Recorded 2026-11-27 12:31 -0600.

Round 12: no findings.

### Round 13 (full review), 2026-11-27: run 8, piece `w6`

A fresh Claude Fable 5.2 agent, on commit 6783e1a, 17 images in `cache/scratch/bc2/review-13/`. Told to suspect:
whether the branch is one poly with band A and a gate with diffusion on both flanks; the load's band under the
block to the M rail's land; every drawn poly end (the tracer mis-ended wires in run 7); another exit or a contact
on the node; the uncertain box's three joins, each separately, against two certain boxes; the pad (9420,15862).

**No finding changes a connection.** Geometry, all fixed: the load block's poly runs to y 15956 (orange in three
shots at y 15941-15953, outline at y 15956, field from y 15962; nothing touches the extra strip); the branch has
an end cap to y 15884 and ends there (field y 15873-15879 between it and the row); the active strip is
y 15901-15932 (W 31).

Verdicts: the branch is **one poly with band A** (the lines y 15897-15900 and y 15934-15938 are the active
strip's two edges, 7 px each, orange poly beyond both) and **a gate** (land 5's tan reaches x 9503; the clean
shot brighter over the channel; the strip east of the gate pinker than field, bounded by the same two edge
lines, no vertical edge before the node); **no contact** of the thin metal on the node; the load's band correct
(both lines cross the whole block; tan reaches west to x 9635 only at y 15906-15930, the land's edge line absent
there); the stem one poly with the block, field above y 15842 and east of it; the pad (9420,15862) a real
contact with plain ground north and west; the row continuous under the rail with field south of it.

**The box** (Ambiguity 14; it is of the same kind as both reference boxes): the finger **yes** (tan continuous
from y 15884 to the node, field north of the box); the stem's poly **probably yes** (its west edge steps west at
the box's height only; the frame is 9 px, as on the reference tie's joined side); the row's poly **probably yes,
cannot be proved** (its two edge lines continue to x 9548 in both metal shots; the clean shot there is not field
pink but not salmon either); **no metal contact** (the metal keeps its edges, chip 2's stripped shot shows a
pink ghost without pits). "`?` on all four box items is right": they stay `?`.

Not checked: the thin metal's continuity over the box; the thin metal x 9420 south of y 15990.

Connections before and after the fixes (commit 6783e1a against the fixed tree):

    tools/t.sh bc2 sameconn.py 6783e1a            ->  connections identical
    .venv/bin/python tools/sameconn.py 6783e1a    ->  connections identical

Recorded 2026-11-27 12:52 -0600.

Round 13: no findings that change a connection.

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
