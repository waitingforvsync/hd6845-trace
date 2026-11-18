# bc2: bottom-centre random logic, right part (x 9000-11000, y 14050-16300)

Scratch: `cache/scratch/bc2/`. Coordinates are metal-shot pixels.

## Status

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

None recorded: nothing was traced.

## Not done

Everything. In order:
1. Place `tl1_ua` / `tl1_ub` at 7940,10454 and 7941,10930 (`@requires tl1`), each with its
   own rails, VSS box and contact below the stack, VCC ring, thin metal x 10682 with its pads,
   and its input rows and pads (listed above: verify each at 4x in two shots first; widths by
   `tools/px.py`). The cell's own contacts report "no metal over it" until the rails are drawn.
2. Test the east column above y 14800 and below y 15750 for further copies; overlay the copy
   at 6857,11495 on the metal shot and the mirrored candidate at all.
3. West gate column; the routing (bus, L bundles, vertical tracks); joins to `bc1`'s bus ends
   at x 9000, to `bw` and to `cdp4`; ports file and floor-plan fragment.

## Review
