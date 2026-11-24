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
