# lc2: left-centre random logic, middle strip (x 4400-6450, y 8067-9233)

## Status

2026-11-18 03:53 +0000. **Latch B traced** (`trace/lc2.txt`, 11 transistors, all in `tl1`'s
cells). 2026-11-18 04:35 +0000. **Latch C traced** (11 transistors, t1140-t1150, all in two
`tl1` cell copies; hand-drawn: the rails, the VSS box and contact, the long VCC contact, the thin
metal x 5928 with its two contacts, the five input rows with their pads); no reviewer yet. The
rest of the region is surveyed only (inventory below). Both pieces were traced on
**claude-opus** (Opus 5.5), not Fable 5.2: the project's rule is Fable; the coordinator
discloses it. The inverter below latch C was not started. Four equations (two per latch) are
DEPENDS only because of `tl1`'s `?` load ties in the cells.

Before this package only `urch` had geometry in the region: the tracks of `sl0`..`sl4` at
x 4258-4640, y 8067-8200 (north-west corner) and the pads (4420,8590), (4380,9066) at the west
edge.

## Inventory (from `cache/scratch/lc2/survey.png` 0.62x, `sv_[abcd]_[am].png` 1.25x; coordinates +-20)

| Where | What | State |
|---|---|---|
| x 4400-4640, y 8067-8200 | `urch`'s five tracks (nested corners) | drawn by `urch` |
| x 4480-5330, y 8380-9160 | west gate cluster: rails at x ~4760, ~4930, ~5110 (which supply: not read), many horizontal poly rows with pads at x 4480-4560 and x 5230-5330, loads at x 4850-4900 and 5010-5060 | not traced, not tried at more than 0.62x |
| x 4450-5350, y 8180-8330 | horizontal poly rows / metals above that cluster with pads at x 4500-4530 and 5130-5220 | not traced |
| x 5200-5600, y 8067-9233 | vertical bus (metals and polys), staircases at y 8380-8480 and y 8700-8780 | not traced |
| x 5590-5895, y 8055-8560 | **latch B**: `tl1_ub` + `tl1_ua` upside down (below) | **traced** (`trace/lc2.txt`) |
| x 5840-6275, y 8525-9030 | **latch C**: `tl1_ub` at 3352,3999 rot=180 and `tl1_ua` at 3352,4439 rot=180 (latch B turned left-right), rows and pads east | **traced** (`trace/lc2.txt`), not reviewed |
| x 5840-6140, y 9025-9155 | inverter (believed): `tl1`'s inverter (2535 4215 2835 4345) at 3306,4809 rot=180 (0.73, centre 5991,9089); `tla`'s in1 unit (3820 4040 4120 4150) also hits there (0.79) | not checked |
| x 5890-6140, y 8067-8290 | south end of a unit that lies mostly in `lc1` (`tl1_ua` at 3351,3703 rot=180, 0.68, centre 6014,8168); rail x 6010-6060 | not checked |
| x 5600-5900, y 8880-9233 | gate cluster that runs on south into `lc3` (weak hits: `tl1` inverter 3059,4663 unturned 0.59; `tla` in1 0.53) | not traced |
| x 6100-6450, y 8067-8560 | bus field: vertical polys x 6240, 6330 with pads at y 8200-8350, rows y 8120-8170, metals turning at y 8480-8530 | not traced |
| x 6150-6450, y 8560-9233 | metals running diagonally south-west to north-east (x 6250-6450), pads at (6145,8725), (6145,8860), (6130,9080) | not traced |

`findcell` (clean shot, --region 4400,8067:6450,9233, --min 0.5), all hits:
`tl1_ua` (2535 4340 2790 4590): 3059,3963 mx=2662.5 rot=180 (0.82); 3351,4439 rot=180 (0.68);
3351,3703 rot=180 (0.68). `tl1_ub` (2535 4590 2790 4780): 3059,3523 mx=2662.5 rot=180 (0.85);
3352,3999 rot=180 (0.76). `tl1` inverter: 3306,4809 rot=180 (0.73); 3059,4663 (0.59).
`tl1` NOR (2535 3558 2842 3742): none. `tla` in3 (2840 5120 3070 5290): 2711,3439 mx rot=180
(0.50, not a copy by eye). `tla` in1: 2018,5006 mx=3970 rot=180 (0.79); 1774,4837 mx=3970 (0.53).

## Latch B (x 5590-5895, y 8055-8560): traced

`tl1`'s pair of units upside down: `@inst tl1_ub 3059,3523 mx=2662.5 rot=180 o=2662.5,4685`,
`@inst tl1_ua 3059,3963 mx=2662.5 rot=180 o=2662.5,4465` (findcell, clean shot, 0.85 / 0.82).
The copy maps master (x, y) to (x + 3059, 12893 - y). Overlay `ov_c.png` (2.5x clean shot, all
of the latch) and the earlier `b_ov_a.png`, `b_ov_m.png` (2.6x), `b4_1a.png`..`b4_3a.png` (4x
clean): every outline lies on a feature within about 5 px.

```
lc2_w8532 = NOT lc2_w8450                                              FIRM
lc2_w8341 = NOT( lc2_w8450 AND lc2_w8169  OR  lc2_w8215 )              DEPENDS (tl1's ? load tie)
lc2_w8215 = NOT( lc2_w8254  OR  lc2_w8169 AND lc2_w8532  OR  lc2_w8341 )  DEPENDS (tl1's ? load tie)
```

A latch open while the enable `lc2_w8169` is high: data `lc2_w8450`, clear `lc2_w8254`
(forces `lc2_w8215` low, so `lc2_w8341` high), outputs `lc2_w8341` (Na, taken west) and
`lc2_w8215` (Nb, not taken out: see (a)). Transistors (extraction): t129-t139 at
(5630-5808, 8132-8472); widths are the cell's (W/L 72/18 and 81-83/19-21 for the series
gates, 35-43/18-22 for the single pull-downs, loads 26-28/50-53).

What the copy has of its own (drawn by hand in `trace/lc2.txt`), and how each open item of the
survey was settled:

| Item | Reading | Seen |
|---|---|---|
| (a) the box (5603-5628, 8198-8228) on Nb | **no row leaves west**: the poly on the box is a stub with a closed rounded end at x ~5592 (dark outline x 5590-5598), as `tl5`'s latch b; the cell's poly (from x 5599) covers it, nothing more drawn | `px.py col 5585 8150 8460 4 acid`: poly (orange, red-green 40-55) on y 8162-8178, 8248-8264, 8336-8352, 8380-8394, 8424-8438 and **field (154/147/96) all through y 8186-8238**; `px.py row 8215 5570 5650`: dark edge 5590-5594, box from 5600 |
| (b) the six rows west of the cells (x < 5599) | enable y 8165-8185 to pad (5558,8169) and y 8383-8401 to pad (5558,8386), both on the metal x 5550-5571; clear y 8247-8266 to pad (5472,8254); Na y 8334-8354 to pad (5514,8341); data y 8423-8441 to the L-shaped pad (5558,8450); the Nb box: no row | `w4.png` 3.9x clean shot and chip-2 metal side by side (x 5450-5620, y 8150-8470): each row orange without a break from the cell to its pad, each pad a ring with a bright centre in the metal shot and a green speck on salmon in the clean shot; the column profile above |
| (c) gate widths | the cell's (profiled in `tl1`); here the rows' east ends were profiled along y 8128, 8178, 8259, 8392, 8432 (`px.py row`, chip-2 stripped, x 5596-5776): orange to x ~5710, the gap's edge lines at 5716-5728; the clear gate's row orange to 5638, edge 5644, poly again 5650 (ends ~5655, past the column's edge 5647) | weak: the stripped shot is noisy under the rail; the copy's widths are not measured independently |
| (d) dark vertical feature x 5722-5740, y 8040-8120 | **not poly**: two dark edge lines at x 5724 and 5740 with a lighter middle (144-171/125-157/88-99 at y 8075; 168/141/109 at y 8104 on the strip), never orange (poly is 174/134/70 with low blue); the etch lines beside the metals, as the survey thought | `px.py row 8075` and `row 8104 5700 5760 4 acid,acid1b` |
| (e) thin metal x 5801 and its pads | metal x 5790-5813 continuous from the ring at (5802,8188) to the ring at (5802,8393), bare ground north of y 8168 and south of y 8410; pads salmon boxes x 5785-5825, y 8170-8205 and y 8375-8410 in the clean shot with green specks; contacts moved 2-4 px to the rings | `tm5801.png` 4.8x, chip-2 metal, chip-1 metal, clean shot |
| (f) enable metal | x 5550-5571, bright without a break from y 8030 to the upper pad's ring (y 8150); drawn from the region edge y 8067 to the lower pad, where it ends (rings and dark y 8395-8443, bright metal again from y 8475: the data pad's own metal, going south) | `px.py col 5560 8030 8160 10 metal,metal1`, `col 5560 8395 8530 8`; survey `j_data_m.png` 5x |
| (f) clear, Na, data metals | drawn only over their pads (stubs); they run on, not followed | `bm.png` 2.4x metal |
| (f) rails | VSS x 5659-5705 (the stack's VSS boxes and contacts (5680,8088), (5687,8283), (5677,8475) under it), VCC x 5840-5890 (the loads' boxes; long contact ring x 5845-5870, y 8255-8350, drawn as `C 5857,8302 s=24x95`; ring (5862,8446) in the cell): which supply **by structure only** | `bm.png`, `ov_c.png` |
| the copy's own VSS box above the stack | D 5659-5714, 8062-8115, contact (5680,8088): ring in the rail, speck in the clean shot | survey `b4_1a.png`, `b4_1m.png` 4x |

Rings and boxes in the latch with no drawn item of their own: the rounded outline x 5585-5600,
y 8195-8235 (the Nb stub's end, above); the poly L at x 5850-5900, y 8510-8560 south-east of
the cell (not the latch's, not followed).

## Ports

`ports.d/lc2.txt`: enable `lc2_w8169` north on metal x 5560 at y 8067 (into `lc1`; believed
to run to (5558,7646)); clear `lc2_w8254`, output `lc2_w8341` and data `lc2_w8450` end on
stubs of their metals (pads (5472,8254), (5514,8341), (5558,8450): the metals run on, not
followed); the rails vss and vcc at y 8060/8067 and y 8560. Latch C: enable `lc2_w8646` on metal
x 6167 at y 8580 (runs on north); clear `lc2_w8731`, Na `lc2_w8822`, data `lc2_w8906` on stubs
over their pads (6257,8731), (6257,8822), (6214,8906); its vss rail (x 6019-6061) at y 8530 and
9030, and vcc (x 5840-5890) at y 9030.

## Ambiguities

1. The latch's load ties are `tl1`'s `?` items (in the cells), so `lc2_w8215` and
   `lc2_w8341` are DEPENDS in `unsure.py --equations`.
2. The gate widths are the cell's; the copy's rows were profiled only at their east ends in
   the noisy chip-2 stripped shot (Latch B, (c)).

## Not done

- **An undrawn thin metal through latch B** (review round 1): x about 5748-5764, from north
  of y 8040 to south of y 8560, the copy's counterpart of tl1's "thin metal W" (the cells
  do not carry it). Continuous in both metal shots (`cache/scratch/lc2/review-1/m5750.png`,
  `w_south.png`); no contact ring seen on it inside the latch (a dark speck at (5758,8438)
  in the clean shot has no ring in either metal shot). Not drawn: follow it north into
  lc1's region and south into lc3's, and look for its contacts, before drawing it.
- t132 at (5716,8472): the cell gives L = 12 (poly x 5710-5722); the photo shows the poly
  at x about 5708-5727 (about 18 px). Geometry only; the cell copy was not changed.
- Gate-width profiles of the three loads (t133-t135) were not taken.

1. Latch B's tracks: clear from the pad (5472,8254), Na from (5514,8341), data south from
   (5558,8450); enable north of y 8067 is `lc1`'s region.
2. Latch C (x 5840-6275, y 8525-9030): **traced 2026-11-18 04:35 +0000 on claude-opus, not
   reviewed.** Cells: `@inst tl1_ub 3352,3999 rot=180 o=2662.5,4685`, `@inst tl1_ua 3352,4439
   rot=180 o=2662.5,4465` (master (x, y) -> (8677 - x, 13369 - y)), overlaid at 4x. Hand-drawn,
   each seen in both metal shots (`cache/scratch/lc2/vss.png`, `vbox.png`, `vcc.png`, `thin.png`,
   `east.png`, `mid.png`): east rail x 6019-6061, y 8530-9030 (VSS by structure: the pull-downs'
   boxes; the "dark" readings at y 8700 / 8990 of the earlier session are the dark bands where
   the metal steps over poly; a dark line at x 6065 in every row is its edge or a diffusion edge
   under it); its box D 6026-6076, 8543-8592 with the contact ring (6048,8566); west rail x
   5840-5890 (VCC by structure) through y 9030; the long VCC contact ring x 5848-5868, y
   8736-8826; the thin metal x 5928, y 8655-8872 with rings (5928,8665), (5928,8862). Rows (px.py
   col 6145 / 6235, chip-2 stripped) east from x 6120: enable y 8638-8654 and 8856-8870 to the
   pads (6168,8646), (6168,8862) on the metal x 6160-6175 (drawn y 8580-8880; north of 8580 not
   followed); clear y 8724-8742 to the pad (6257,8731); Na y 8812-8829 to the pad (6257,8822);
   data y 8899-8914 to the pad (6214,8906). Topology and equations match latch B's one for one.
   Still to do:
   - The pads (6257,8731) and (6257,8822) are on two separate metals (4x, `pads.png`: field,
     no metal, at x 6250 between y ~8750 and ~8800 in both metal shots): clear's metal runs on
     north from its pad, Na's south (x ~6250-6265). The data pad's metal x ~6203-6222 runs on
     north. A poly also leaves the clear pad to the south-east (acid1b, ~(6265,8755)): not followed.
   - Where the clear, Na, data and enable metals go (not followed).
   - An undrawn thin metal x ~5970-5985 runs through latch C from y 8525 to 9025, bright in both
     metal shots (`mid.png`): latch B's undrawn x 5748-5764 mirrored; no contact on it seen.
   - A bright strip x ~6066-6090 east of the VSS rail (segmented, `mid.png`): part of the rail
     or a separate metal: not read; nothing connects there in what is drawn.
   - Gate-width profiles (none taken); the inverter hit 3306,4809 rot=180 (0.73) not overlaid.
3. The west gate cluster (x 4480-5330, y 8380-9160): the largest piece; not a known cell.
4. The bus fields and the unit halves on the north and south edges (with `lc1` / `lc3`).

Tool note: `view.py` has no `--notrace`; images wider than about 1300 px (6x of 130 px in two
panels) are downscaled and wasted.

## Review

**Model note: latch B was traced AND reviewed on claude-opus, not claude-fable-5-2** (the
Fable allowance ran out; the survey before it was on Fable). The project's rule is Fable
for both: this piece wants a Fable review before it is relied on.

Round 1 (full review of latch B, 2026-11-18 04:02 +0000, a fresh agent on claude-opus). Told to suspect the gap
on the metal x 5560 (enable against data), the five input rows to their pads, the two cell
copies against the photo, the unmeasured gate widths, the VCC contact and VSS box. Checked:
the gap in both metal shots (dark at y 8394-8406, no metal to the data pad's ring at
y 8446: separate nets); all five rows unbroken to their pads with field between them and
none continuing west; no west row on the Nb box and none drawn; both copies overlaid at 3x
on the clean and a metal shot (every contact on a ring or box); widths within about 10 px
for t129-t132 and t136-t139; the VSS box, its contact and the long VCC ring; the dark bars
at x 5722-5740 not poly; the full extraction (0 errors, same 11 transistors, no merges).
No finding changes a connection of what is drawn. Two findings, both recorded in Not done:
an undrawn thin metal through the latch at x 5748-5764 (a net missing from the region; no
contact to the latch seen), and t132's channel length (12 drawn, about 18 in the photo;
geometry only). Not checked: the loads' width profiles; where the thin metal ends.

Round 1: no findings that change a drawn connection; one net (the thin metal) is missing
and is listed in Not done.

### Latch C (also traced and reviewed on claude-opus)

Round 1 (full review of latch C, added in 4dbf2e4; 2026-11-18 08:45 +0000, a fresh agent on claude-opus).
Checked at 4-5x in the clean and both metal shots with profiles: each of the five rows from
x 6120 to its own pad only, none joining a neighbour; the enable, Na and data pads closed
on the east; the enable metal joining its two pads, ending at y about 8872 and touching no
other pad; the clear and Na metals separate (field at x 6257, y 8772-8796 in both metal
shots); both cell copies (every gate over diffusion, every contact on a box); the thin
metal x 5928 with its two contacts; the extraction (0 errors; t1140-t1150 give the stated
equations; internal nodes are latch C's own; nothing merged with latch B).
No finding changes a connection. Geometry only, not changed: the VCC long contact at
(5858,8781) probably sits 5-8 px further east (x about 5850-5878; it is on latch C's box);
the VSS rail's west edge is about x 6014-6017 and the rail runs on south past y 9030; the
strip at x 6066-6090 is not metal. Recorded in Not done: clear's poly goes on south-east
from (6260,8752) toward (6350,8850), not followed; Na's metal turns west at y about 8935;
the undrawn thin metal at x about 5971 through the latch is continuous with no contact on
it (the counterpart of the one through latch B). Only roughly checked: gate widths of
t1142/t1143 and t1148/t1149; not checked: the other widths, and where the four pad metals
go beyond what is drawn.

Round 1 (latch C): no findings.
