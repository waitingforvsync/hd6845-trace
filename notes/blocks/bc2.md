# bc2: bottom-centre random logic, right part (x 9000-11000, y 14050-16300)

Scratch: `cache/scratch/bc2/`. Coordinates are metal-shot pixels.

## Status

2026-11-18 05:36 +0100: **one latch unit traced** (east gate column, unit a: `tl1_ua` + `tl1_ub` at
7940,10454, 11 transistors), traced on claude-opus (Fable allowance exhausted). Not reviewed.
**Unit b (7941,10930) placed, fitted, and held**: its lines are in `trace/bc2.txt` commented out
(see "Latch unit b"), because with them the extraction has one error at the seam with unit a.
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
a supply), the VSS box below the stack with its ring (10558,15258), the VCC long ring
(10745,14988-15070), the thin metal x 10682 between its pads (10681,14953), (10681,15156), and the
rows west of x 10484 to their pads (`a_w.png`, 4x, clean and metal side by side: each pad a ring
in the metal shot, each row continuous poly in the clean shot):

| Net | Row | Pad | Metal at the pad |
|---|---|---|---|
| `bc2_w14912` data (inverter and upper AND) | y 14905-14922 | (10395,14912) | goes west, not followed |
| `bc2_w14955` enable (both ANDs) | y 14947-14964 and y 15163-15180 | (10441,14955), (10441,15172) | one vertical metal x 10441 (drawn between the pads only) |
| `bc2_w15087` clear | y 15079-15096 | (10395,15087) | metal x 10395 south, not followed |
| `bc2_w15000` output (upper gate's node) | y 14992-15010 | (10395,15000) | a metal from the north-west ends on it, not followed |

Equations (`unsure.py --equations`: the inverter FIRM, the two gates DEPENDS only by feedback):
- `bc2_w14876` = NOT `bc2_w14912`
- `bc2_w15000` = NOT( `bc2_w14912` AND `bc2_w14955` OR `bc2_w15029` )
- `bc2_w15029` = NOT( `bc2_w15087` OR `bc2_w14955` AND `bc2_w14876` OR `bc2_w15000` )

The same D latch with enable and clear as `tl5` and `lc2` place. Widths: `px.py col 10554`
(acid) gives poly y 14905-14922 and y 14947-14966 at the two upper AND gates, matching the
cell's L 18; the other transistors' sizes are the master's, not profiled.

## Latch unit b (x 10300-10779, y 15277-15746): placed, held

`@inst tl1_ua 7941,10930` and `@inst tl1_ub 7941,10930` (tag b). Overlay `b_top.png`, `b_bot.png`,
`b_rail.png` (2.5x, clean and metal side by side): every gate of the cells lies on a poly row over
diffusion and every contact on a box or ring. Drawn (active): the VSS rail x 10568 (w 56) and the
VCC rail x 10746 (w 50) over y 15270-15746, and the thin metal x 10682 y 15416-15644. Written but
commented out with the cells (a contact needs the cells' diffusion under it): the VCC long ring
(10745,15505) (metal shot, ring y 15470-15550), the thin metal's contacts (10681,15429),
(10681,15632) (rings in the metal shot).

**Why held.** With the two `@inst` lines active, `netlist.py`: 1 error, "channel at 10558,15284: 1
diffusion terminals". Copy b's top poly row (master y 4350-4367, here 15280-15297) crosses unit a's
hand-drawn VSS box `D 10530,15235:10586,15285`. `px.py col 10535` (acid1b, acid): diffusion
y 15258-15276, dark edge y 15279-15285, poly (acid orange) y 15288-15300. So the box ends at about
y 15279 and the row starts at about 15287; both drawn items are about 5 px long into the gap (the
same row at unit a reads 14809-14821 against the drawn 14804). Fix: unit a's box south edge to
15279 (unit a's line; not changed here while it is under review), then uncomment the five lines.
Tested in the working tree only (not committed): with that edge at 15279 and the five lines
active, the full extraction gives 0 errors, 0 warnings, 4126 transistors (11 more), and unit a's
equations are unchanged.

Widths (lengths) at copy b, `px.py col` in acid: x 10554 poly y 15383-15400 and y 15426-15442 (the two
upper AND gates), x 10560 poly y 15497-15513 (the pull-down row; unit a's same row 15019-15036): each
L 16-18, the cell's 18, and each 476 below unit a's. Channel widths not profiled.

Copy b's own VSS box below its stack is drawn (active): `D 10540,15706:10596,15752` with the contact
(10558,15731) on the VSS rail (`b_box.png`, 4x: pale box in the clean shot, dark edge from y 15752;
ring in the metal shot).

Rows west of copy b, read on `b_w.png` (2.4x, clean + metal; **not drawn**, positions to ~5 px):
| Cell row (copy a's net) | Row y | Seen |
|---|---|---|
| data (a: `bc2_w14912`) | 15380-15397 | poly west to a pad (10352,15388), ring in the metal shot; a metal from the pad runs south at x ~10355 (and the L above it, y ~15300, x 10300-10350) |
| enable (a: `bc2_w14955`) | ~15431 | pad (10441,15432), ring, on the vertical metal x 10441 |
| enable again | ~15648 | pad (10441,15648), ring, on the same metal x 10441 (continuous y 15400-15720 in the metal shot) |
| output (a: `bc2_w15000`) | ~15476 | no pad west of the cell's own contact (10479,15476) seen at 2.4x |
| clear (a: `bc2_w15087`) | ~15563 | runs on west past x 10300 (under the metals x 10355, 10441) |
| ? | ~15606 | runs on west past x 10300 |

The metal x 10441 (x 10430-10450) is continuous in the metal shot from copy a's lower enable pad
(10441,15172) to y 15400 (`b_x441.png`, 3x, metal + clean), and on to y 15720 (`b_w.png`): so units
a and b very likely share the enable (believed; not yet drawn; whether it has a break or a contact
between y 15188 and 15400 under copy b's data row y 15388 was looked at only at 3x).

## Not done

In order:
1. **The metal x 10441 is not only the enable's link between its two pads**: in the metal shot
   (`a_w.png`, `a_m.png`) it runs on north of y 14940 and south of y 15188, about 55 px west of
   the cell's own thin metal x 10500 (the extra vertical seen in another copy). Not drawn
   beyond the pads; where it goes (and so where the enable comes from) is not followed. Likewise
   the metals at the data, clear and output pads.
1b. Copy b: fix unit a's VSS box south edge (15285 -> 15279), uncomment the cells and the three
   contacts, re-run the extraction; then draw its rows to their pads (table under "Latch unit b";
   rows y 15563 and 15606 go on west, not followed),, then draw the enable pads' rows east to the cells (y ~15431, ~15648) and check the metal x 10441
   at 4x+ between y 15188 and 15400.
   Channel widths of b not profiled (three gate lengths were: above).
2. Test the east column above y 14800 and below y 15750 for further copies; overlay the copy
   at 6857,11495 on the metal shot and the mirrored candidate at all.
3. West gate column; the routing (bus, L bundles, vertical tracks); joins to `bc1`'s bus ends
   at x 9000, to `bw` and to `cdp4`; ports file and floor-plan fragment.

## Review
