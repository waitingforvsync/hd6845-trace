# lc2: left-centre random logic, middle strip (x 4400-6450, y 8067-9233)

## Status

2026-11-18 18:47 -0600 (run 6, Matt Godbolt, on Fable 5.2). **Partial: three lines of the staircase of metals west of latch B
drawn** (piece H, wiring only). Two joins to `lc1`, without an uncertain item:

- **`lc2_w8474` is `lc1_w7170`**, the input of `lc1`'s gate 2: its metal runs on from the pad (5232,8214), north, west
  along y 8172 and north as `lc1`'s thin metal T1. So latch B's data `lc2_w8450` = NOT `lc1_w7170`, and `lc1_w7140`
  is the same inverse made a second time. The extraction prints `lc1_w7170` for the net.
- **`lc1_w7468`** (`lc1`'s metal M_c2) comes down the staircase and runs south through the whole strip without a
  contact, into `lc3`.
- Row 4's metal (`lc3_w9299`) is drawn up the staircase to `lc1`'s strip at x 5422-5438.

Full extraction: 2361 nets, 4241 transistors, 0 errors, 0 warnings.

Earlier:

2026-11-18 18:28 -0600 (run 5, Matt Godbolt, on Fable 5.2). **Partial: the gate column south of latch B drawn** (piece G:
8 transistors, hand-drawn; 38 in the package), **as corrected by review round 5**. Under latch B's VSS rail
(x 5545-5848, y 8880-9256) are two gates on one column of diffusion:

```
lc2_w8450 = NOT lc2_w8474                                               DEPENDS (the load's tie, as every load)
lc2_w9125 = NOT( lc2_w9034 AND lc2_w9079  OR  lc3_w9299 AND lc2_w9210 )   DEPENDS (the load's tie)
```

**Latch B's data is the inverse of `lc2_w8474`** (the net from `lc1`'s metal x 6341, run 4): an inverter (58/19,
load 30/60) whose drain is contacted by latch B's data metal, the thin metal x 5618-5634, which runs on south into
`lc3` (`lc3_m5626`). Below it an AND-OR-INVERT gate (four pull-downs of 136/20 in two series pairs, load 38/36):
its inputs are three rows from the west and the net of `lc3`'s upper inverter's input `lc3_w9299` (one metal
through row 4's pad and on south); its output node has no metal on it and leaves, as far as found, on a poly row
east under the VCC rail and south into `lc3` (`lc2_w9185`, joined to the node through uncertain items:
Ambiguity 8). The first drawing of this piece (one five-input NOR strapped by both thin metals) was wrong: the
node between rows 3 and 4 has no VSS contact, and four contacts of the thin metals were not there (review round
5). The thin metal through latch B (x 5749-5763) has no contact found anywhere in the strip; it is `lc3`'s
`lc3_m5756`. Full extraction: 2366 nets, 4239 transistors, 0 errors, 0 warnings.
Run 4's pieces are reviewed (rounds 3 and 4) but **not yet on main**: the merge gate's model check fails on one
Sonnet response of another session (the branch is `lc2`).

2026-11-18 17:22 -0600 (run 4, Matt Godbolt, on Fable 5.2). **Partial: the inverter below latch C and the thin metal
it drives drawn** (piece E: 2 transistors, a copy of `tl5_inv`, and wiring):

```
lc2_w9124 = NOT lc2_w8822        DEPENDS (the cell's ? load tie); the pull-down and its gate's join are firm
```

Latch C's output Na goes by its metal (south from the pad (6257,8822), west, south) to the inverter's gate row, and the
inverter's output is on **the thin metal x 5967-5981 that runs north through latch C and latch D's lower unit** and out
of the strip at y 8067: the counterpart of `tl1`'s thin metal W. Over three tie boxes of the latches' cells neither
metal shot shows it for 33-40 px; it is drawn uncertain there and taken to pass over (Ambiguity 6). Full extraction:
2362 nets, 4232 transistors, 0 errors, 0 warnings. Run 3's piece is on main (b2a42d5).

Same run, piece F (wiring only): **latch B's clear is `lc1_w7864` too** (`lc1`'s metal x 5466-5486 comes south
without a break to the clear pad), so one signal clears latches B, C and D; latch B's output Na leaves north on
the metal x 5508-5524; `lc2_w8474`'s row is drawn on west to a pad (5428,8648) in the run of a metal x 5421-5437 (corrected by review
round 3: the metal runs on both ways, has a pad (5428,8516) with a poly west and a third contact (5429,8994) whose poly is
the first gate row of the column south of latch B); a poly from latch C's clear pad leaves the strip south-east. One merged equation prints another name: `lc2_w8215` (latch B's Nb)
reads `lc1_w7864` where it read `lc2_w8254` (input identified; no logic changed). Full extraction: 2361 nets,
4232 transistors, 0 errors, 0 warnings.

2026-11-18 16:28 -0600 (run 3, Matt Godbolt, on Fable 5.2). **Partial: the lower unit of latch D and the bus field
east of the latches drawn** (piece D: 6 transistors in one copy of `tl1_ua`, and wiring). Latch D is the latch
whose upper unit `lc1` drew: its output's inverse is `lc_step`, the step pulse of the scan line counter. With
the lower unit it extracts in full (full extraction: 2365 nets, 4230 transistors, 0 errors, 0 warnings):

```
lc1_w7862 = NOT lc1_w7780                                         FIRM (the data's inverse)
lc1_w7928 = NOT( lc1_w7040  OR  lc1_w7780 AND lc1_w7908 )          DEPENDS (the cell's ? load tie)
lc1_w7040 = NOT( lc1_w7862 AND lc1_w7908  OR  lc1_w7864  OR  lc1_w7928 )   DEPENDS (as before, in lc1)
lc_step   = NOT lc1_w7040
```

So latch D is open while `lc1_w7908` is high, takes `lc1_w7780` (= NOT `lc1_w7733`, `lc1`'s gate E1) and is
cleared by `lc1_w7864`: `lc_step` is the inverse of what it holds, and high while the clear is high. The bus
field gives three joins, none through an uncertain item: **latch C's clear is `lc1_w7864`**, the clear of latch D
(a poly cross-under and a metal); latch C's enable `lc2_w8646` runs north out of the strip and has a branch
east; latch C's data `lc2_w8906` comes from the north on a metal 20 px east of the strip (Logic, "Latch D's
lower unit and the bus field"). One merged equation prints another name for one net: `lc2_w8688` (latch C's
Nb) now reads `lc1_w7864` where it read `lc2_w8731` (input identified; no logic changed).

Earlier runs (dp111):

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
| x 5836-6230, y 9040-9150 | **the inverter below latch C**: `tl5_inv` flipped top to bottom (`@inst tl5_inv 933,4239 mx=5082 rot=180 o=5082,4848`, findcell 0.86); its output on the thin metal x 5967-5981 | **traced** (run 4) |
| x 5887-6142, y 8067-8290 | **latch D's lower unit**: `tl1_ua` at 3351,3703 rot=180 (the upper unit is `lc1`'s copy of `tl1_ub`); VSS rail x 6015-6063 | **traced** (run 3) |
| x 5545-5848, y 8880-9256 | **the gate column south of latch B**: the inverter that makes latch B's data (row y 8948) and an AND-OR-INVERT gate (rows y 9034, 9079, 9166, 9210) on one diffusion column x 5620-5756 under the VSS rail and the two thin metals; loads east (plates (5798-5837, 8887-8972) and (5795-5831, 9060-9146)) | **traced** (run 5, corrected by review round 5) |
| x 6140-6490, y 8067-8560 | bus field east of the latches: seven vertical metals from the north (x 6168, 6212, 6256, 6297, 6341, 6431, 6471), two horizontal metals (A y 8250-8268, B y 8292-8310), three poly cross-unders, ten pads | **traced** (run 3) |
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

## Latch D's lower unit and the bus field east of the latches (run 3): traced

Views in `cache/scratch/lc2/` (this machine): `d1_a.png`, `d1_m.png` (2x, every package's trace), `d2_a.png`,
`d2_m.png` (4x, the unit with the copy outlined), `e1.png` (3.8x, the field's top, metal over clean), `e2.png`
(4.6x, four shots), `e3_m.png`, `e3_a.png` (3.6x, the field's lower part), `e4.png` (3.8x, the strip's east edge),
`e5.png`, `e6.png` (the poly under the VCC rail), overlays `o1_m.png`, `o2_a.png`. Every measurement with its
command is in `cache/scratch/lc2/survey.md`.

**The unit** (x 5887-6142, y 8067-8290) is `tl1_ua` turned 180 degrees, `@inst tl1_ua 3351,3703 rot=180
o=2662.5,4465` (the placement `lc1`'s notes gave; master (x, y) -> (8676 - x, 12633 - y)). On the 4x overlay
the two stack gates lie on the rows y 8118-8135 and y 8161-8180, the VSS contact on the ring (6056,8213) under
the rail, the load plate on the plate x 5904-5954, the inverter's gate on the poly that turns south from the
data row. Its own wiring, drawn by hand:

| Item | Reading | Seen |
|---|---|---|
| `lc1_w7928`'s thin metal x 5918-5932 | on south from `lc1` to a pad with a contact (5927,8131) on the unit's load plate; ends there | `textmap.py 5900 8090 5960 8160`: dark ring with a bright centre in both metal shots, a hole of `g` in the clean shot; no bright metal south of y 8144 |
| the node's row (the poly on the buried contact of the node's east box, the cell's stub) | east along y 8075-8092 under five metals, no pad, to x 6415; north along x 6401-6415 out of the strip at y 8067 | `e1.png`; `px.py col 6276` and `col 6385` (orange in the chip-2 stripped shot at y 8078-8090), `px.py row 8050 6385 6425` (poly x 6403-6412); the dark dots on it at x 6190, 6234, 6276, 6321 lie in the gaps between the metals and have no ring (trap 2) |
| enable: gate 2's row | east to a pad (6212,8128) **in the run** of `lc1_w7908`'s metal x 6203-6221, which goes on south and turns east along y 8250-8268 (metal A) out of the strip | `textmap.py 6180 8090 6330 8200`: ring, bright centre, `g` hole; bright metal on both sides of the pad; `tl5_tracks.py v 6212 8060 8275`, `h 8259 6195 6462` (A begins at x 6206: bare ground between it and the metal x 6168) |
| data: gate 1's row (also the inverter's gate) | east under the metals x 6168, x 6212, x 6256 to the pad (6297,8170) where `lc1_w7780`'s metal ends | the same text map: ring, centre, hole at the pad; under the three metals the clean shot has poly values and no hole, and the metals no ring; `px.py col 6150`, `col 6240` |
| VSS rail x 6015-6063 | one metal from `lc1`'s piece (y 8067) to latch C's (y 8530) | `tl5_tracks.py v 6039 8060 8540`: no stretch without metal longer than 21 px (the rows and boxes under it) |

**The bus field** (x 6140-6490, y 8067-8560), wiring only. Seven metals come down from `lc1`'s strip:

| Metal | What it is | Where it goes |
|---|---|---|
| x 6159-6177 | **latch C's enable `lc2_w8646`** | one metal from y 8067 to latch C's two pads (`tl5_tracks.py v 6168 8060 8590`: only the 8-12 px bars where rows pass under it; no hole); at y 8292-8310 a branch east (metal B), a T with no dark line across the join (`h 8301 6155 6462`), out of the strip at x 6450 |
| x 6203-6221 | `lc1_w7908`, latch D's enable | through latch D's pad, then east as metal A (above) |
| x 6248-6264 | `lc1_w7864`, latch D's clear | ends on a pad (6254,8214); a poly cross-under x 6247-6270 south beneath A and B to a pad (6256,8344); a metal x 6246-6266 south from it, continuous to latch C's clear pad (6257,8731) (`v 6256 8325 8750`). **Latch C's clear is `lc1_w7864`** |
| x 6287-6307 | `lc1_w7780`, latch D's data | ends on the data row's pad |
| x 6332-6350 | `lc2_w8474` | ends on a pad (6341,8214); poly south under A and B (x 6333-6357), west along y 8462-8485 under the metals x 6256 and x 6168, down a link x 6078-6096, west along y 8506-8523 under the VSS rail and the thin metals, south under the VCC rail (x 5859-5877, salmon in the clean shot to y 8652: `px.py col 5868`) and west again from under it along y 8634-8652. Drawn to x 5835; **it runs on west** (`tl5_tracks.py rows row 5560 5900 4 8642`: poly to x 5560 and beyond) |
| x 6422-6440 | `lc2_w8172` | lies on the poly of the next line from y 8117, turns east at y 8163-8181 and leaves the strip. Not on anything here (Ambiguity 3) |
| x 6462-6480 (20 px east of the strip) | **latch C's data `lc2_w8906`** | ends on a pad (6470,8127); its poly goes west 25 px and south (x 6420-6443) under A and B to a pad (6429,8386); a metal south, south-west on a diagonal and west along y 8508-8528 to a pad (6298,8516); a poly link west to a pad (6212,8516); a metal x 6202-6222 south to latch C's data pad (6214,8906) (`v 6212 8500 8925`, `h 8518 6285 6415`, `v 6430 8375 8505`) |

The ten pads: each has a dark ring with a bright centre in both metal shots. Six have a hole of `g` in the
clean shot ((5927,8131), (6212,8128), (6297,8170), (6429,8386), (6298,8516), (6212,8516)); four do not
((6254,8214), (6256,8344), (6341,8214): centre values 1-3 against 5-8 around; (6470,8127): a red centre), and
were read in the chip-2 stripped shot, where each has a pit in the poly (`textmap.py ... --acid` on each).
No metal has a contact where it only crosses a poly: A and B over the three cross-unders, the metals x 6168,
x 6212 and x 6256 over the rows (no ring, no widening; the clean shot's colour under A and B drifts from cream
to yellow to red from one poly to the next, trap 15, and is not used).

## The inverter below latch C and its thin metal (run 4): traced

Views: `f1.png` (2.6x, clean over metal), `f2.png` (3.1x, the copy outlined), overlays `o3_m.png` (2.75x), `o3_a.png`
(3.1x); measurements in `cache/scratch/lc2/survey.md`.

**The inverter** is `tl5`'s cell `tl5_inv` flipped top to bottom (x' = x + 933, y' = 13935 - y): on the overlay the VSS
contact lies on the ring (6047,9051) under the rail, the gate on the row y 9072-9093, the plate on the plate
(x 5903-5950, y 9080-9140), the node's box on the ringed box (6094-6138, 9105-9141), the tab on the ringed blob
(5925-5950, 9050-9080). Drawn by hand:

| Item | Reading | Seen |
|---|---|---|
| the load's VCC box | diffusion x 5840-5896, y 9066-9144 under the VCC rail, one long contact (5858, 9062-9148) | `px.py row 9104 5826 5905`, `col 5850 9050 9160` (tan between dark edges); `tl5_tracks.py v 5858 9050 9150`: ring ends at y 9062-9084 and y 9127-9149 in both chips, a hole 52 px long in the clean shot |
| the rails | VCC x 5840-5890 on south through the strip's edge (metal to y 9245); VSS x 6015-6063 ends at y 9176 | `v 5865 9030 9245 --half 10`, `v 6039 9030 9200 --half 10` |
| input | latch C's Na metal: x 6250-6262 south from its pad to y 8958, west along y 8946-8958, south on x 6205-6220 to a pad (6211,9082) at the east end of the gate row: **the input is `lc2_w8822`** | `textmap.py 6196 8922 6277 8972`: one bright L in both chips, no dark line across either corner; `v 6213 8880 9100`: **no metal for 35 px (y 8911-8945) between latch C's data pad and this metal's start**, so it is not the data metal, which shares its x; pad: ring and hole (`h 9082 6140 6235`) |
| output | the cell's output poly east to a pad (6168,9124), the end of the thin metal | `v 6169 9100 9225`: ring, hole at y 9124; `h 9126 6130 6195` |
| the thin metal | from the pad south on x 6162-6176, west along y 9205-9219 round the VSS rail's end, north on x 5967-5981 to y 8067 and on into `lc1` | `h 9212 5960 6185`: no break; `tl5_tracks.py h Y 5945 6005 --half 1` at ten heights from y 8170 to y 9150: metal at x 5966-5981 in every one; `v 5972 8060 9215`: the stretches without metal in both chips are 8-15 px (edges underneath) except three (Ambiguity 6) |

## Latch B's clear and output, and the west end of `lc2_w8474` (run 4, piece F): traced

Wiring only. Views `g1_m.png`, `g1_a.png` (1.9x, every package's trace), overlay `o4_m.png` (2x).

| Wire | Reading | Seen |
|---|---|---|
| latch B's clear | `lc1`'s metal x 5466-5486 (`lc1_w7864`, drawn by `lc1` to y 8067) runs on south to the clear pad (5472,8254): **latch B's clear is `lc1_w7864`** | `tl5_tracks.py v 5476 8055 8262`: metal without a break to the pad's ring (y 8234-8257), hole at y 8255; `follow.py 5474 8100 S` ends at the pad |
| latch B's output Na | the metal x 5508-5524 runs north from the pad (5514,8341) out of the strip; the clear's row passes under it without a contact | `v 5516 8055 8350`: two 8 px bars at y 8241-8249 and y 8265-8273 (the row's edges), no hole; the ring at y 8321-8338 |
| `lc2_w8474` | the row y 8634-8652 from under the VCC rail west under five metals (no pad, no hole) to a pad (5428,8648) **in the run of** a metal x 5421-5437 (review round 3). North the metal passes a pad (5428,8516), turns west along y 8468-8484 and north on x 5379-5391 (drawn to y 8440); south it runs through the strip's edge with a third contact (5429,8994), whose pad's poly goes north to the row y 8939-8958: **the first gate row of the column south of latch B is `lc2_w8474`**. Poly west from the pad (5428,8516) along y 8509-8526 (drawn to x 5400; `tl5_tracks.py rows row 5150 5445 4 8515`: poly to x 5150 and beyond) | `h 8643 5420 5845`: the only hole is the pad's; `v 5429 8500 8660`: metal between the two rings; `textmap.py 5404 8626 5452 8666 --acid`: ring, bright centre and green hole at the lower pad; `textmap.py 5398 8494 5452 8536 --acid`: at the upper pad a ring with a bright centre in chip 1, a weak centre (6-7) in chip 2, no green hole, a pit in the chip-2 stripped shot |

## The gate column south of latch B (run 5, piece G; corrected by review round 5): traced

Views `h1_a.png`/`h1_m.png` (3.2x), `h2`-`h13`, `k1.png` (3.5-6.5x, the clean shot, both chip-2 shots, the second
chip-1 stripped shot), overlay `o8_a.png` (2.9x, the whole column as now drawn); the reviewer's images in
`cache/scratch/lc2/review-5/`; every measurement with its command in `cache/scratch/lc2/survey.md`.

**Structure.** A column of diffusion x 5620-5756 lies under the VSS rail (x 5665-5711) and under the two thin
metals beside it (x 5618-5634 and x 5749-5763). Five poly rows from the west cross it; `tools/railprof.py 5662 5702
8880 9240` and `9195 9320` give the stack under the rail:

| y | What | Net |
|---|---|---|
| 8913-8936 | drain A (a band; narrow arms west to its contact box and east to the upper load) | `lc2_w8450` |
| 8939-8958 | row 1 (ends, rounded, at x 5722; channel x 5650-5708) | `lc2_w8474` |
| 8962-9027 | node B: one long contact under the rail (ring, bright blobs and green pits: `textmap.py 5660 8960 5722 9030 --acid`) | `vss` |
| 9024-9044 | row 2 | `lc2_w9034` |
| 9046-9066 | node C: the middle of the series pair of rows 2 and 3; nothing on it | (internal) |
| 9068-9090 | row 3 | `lc2_w9079` |
| 9092-9156 | **node D: no contact** (`textmap.py 5660 9088 5722 9162 --acid`: both metal shots plain bright over it, the clean shot one value, no ring, no pit); its diffusion runs east into the lower load's strip (`px.py row 9120`: tan without a break from x 5744 to x 5770) | `lc2_w9125` |
| 9156-9176 | row 4, with a pad (5560,9166) in the run of the metal x 5550-5568 | `lc3_w9299` |
| 9178-9198 | node E: the middle of the series pair of rows 4 and 5 | (internal) |
| 9200-9220 | row 5 | `lc2_w9210` |
| 9227-9282 | node F: one diffusion on south to the VSS contact (5680,9264) of `lc3`'s upper inverter | `vss` |

So row 1 with drain A and node B is an inverter, and rows 2-5 with node D are an AND-OR-INVERT gate: node D is
pulled low through rows 3 and 2 to node B, or through rows 4 and 5 to node F. Rows 2 and 3 end separately at
x 5768, as do rows 4 and 5 (`px.py row 9034`, `9056`, `9079` in `acid1` and `acid`; the reviewer's
`b1_rows23_east.png`). East of x 5710, below drain A's east arm, is field (`px.py col 5730`).

**The thin metals.** One contact: (5622,8910), the west thin metal on drain A's west box (`textmap.py 5602 8880 5650
8960`: ring y 8890-8937, centre y 8907-8913, the metal again from y 8940; a pad, a cream box, a pit). The pad lies
in the run of the metal: north it is latch B's data wire (from the pad (5558,8450) south, east along y 8607, south
on x 5626), south it runs on through the strip's edge into `lc3`'s `lc3_m5626`. **No other contact of either thin
metal in this column.** The first drawing had four more, on nodes C and E and on drain A's east arm, read from a
bright stretch between two dark bars and a greenish patch in the chip-2 stripped shot; the reviewer showed that the
same signs are there wherever these metals cross a 20 px band (node D, where a contact is excluded), and that none
has a ring, a widened metal or a hole in the clean shot. The east thin metal therefore touches nothing here: it
comes from `lc1` through latch B (dim and 5 px west of its line there) and runs on into `lc3`'s `lc3_m5756`.

**The loads.** Upper (the inverter's): drain A's east arm widens into a strip (y 8911-8940) under the plate's bar
and the plate (x 5776-5837) to the VCC box of latch C's cell, with a tail south (x 5762-5776) to a ringed box
(5757-5777, 8943-8972) on which the plate's foot lies (the tie, uncertain as in every load). Lower (the
AND-OR-INVERT's): node D's diffusion runs east as a strip (y 9104-9142) under the plate (x 5795-5831) to the VCC
box of the inverter below latch C; a tail north (x 5775-5791) to a ringed box (centre (5802,9053)) under the
plate's top bar (the tie; the mirror image, about x 5868, of the tie of the inverter below latch C).

**The AND-OR-INVERT's output.** Below the plate is a poly block (5797-5838, 9150-9198) with a second ringed box
(5813-5831, 9156-9178: a dark ring with a plain centre in both metal shots, green with a dark dot in the clean
shot, a pit in the chip-2 stripped shot). From the block a poly row runs east under the VCC rail (y 9176-9194) to
x 5940 and south on x 5924-5940 through the strip's edge (`tl5_tracks.py rows row 5790 5960 4 9184`, `rows col 9160
9270 4 5928 5936`). It is labelled `lc2_w9185` and joined to the plate, and so to node D, by one uncertain poly
(Ambiguity 8). Node D also has a box on its west lobe under the west thin metal (Ambiguity 9).

**Across the south edge.** `lc3`'s shapes begin at y 9255. Six items are drawn 23 px into `lc3`'s strip to meet them,
each seen without a break across y 9233-9255: the two rails, the two thin metals, the column (one diffusion
y 9227-9282 under the rail) and the metal x 5550-5568 (`tl5_tracks.py v 5560 9100 9320`: rings at y 9142-9187 and
y 9274-9293 with metal between: row 4's pad lies in its run). Two aliases record the joins: `lc3_m5626` is
`lc2_w8450`; `lc2_w9166` is `lc3_w9299`. The east thin metal carries `lc3`'s name `lc3_m5756`.

## The staircase of metals west of latch B (run 6, piece H): three lines traced

Wiring only. A bundle of metals comes from the north-west and steps east at right angles, each line one track at
a time (`b1_m.png` 1.1x, `b2_m.png` 3x, overlay `o9_m.png` 2.25x). Each leg was scanned with `tools/tl5_tracks.py v`
/ `h` (metal in both chips, holes in the clean shot); the commands and results are in `cache/scratch/lc2/survey.md`.

| Line | Path | Seen |
|---|---|---|
| row 4's metal, `lc3_w9299` | from `lc1` at x 5422-5438 south to y 8303; east to x 5475; south to y 8385; east to x 5518; south to y 8785; east to x 5560; south to the pad of gate row 4 (and on into `lc3`) | every leg without a break or a hole (`v 5426 8040 8306`, `h 8302`, `v 5474 8296 8396`, `h 8392`, `v 5517 8388 8792`, `h 8785`, `v 5561 8780 9150`: only the 8-15 px bars of the rows under it). It passes 26 px below latch B's clear pad and below its Na pad: bare ground between |
| `lc1_w7468` | `lc1`'s metal M_c2 (x 5073-5093) south to y 8128; east along y 8120-8136 to x 5387; south to y 8340; east to x 5425; south to y 8430; east to x 5473; south through the strip's edge | `textmap.py 5062 8100 5160 8146`: the vertical ends in a dark bar y 8112-8118 (darker than bare ground: an edge underneath) and the horizontal starts flush with its west edge: an L; `h 8128 5076 5395 --half 5`: one 12 px dip; `v 5473 8425 9260`: no hole. A pad (5123,8080) beside the corner is on another metal: no metal between it and the horizontal (values 8-9 at y 8103-8112) |
| `lc2_w8474` = `lc1_w7170` | from (5385,8440) north to y 8385; west to x 5341; north to y 8214; west to the pad (5232,8214), which lies in its run; north to y 8172; west along y 8164-8180 to x 5037; north as `lc1`'s thin metal T1 | `v 5341 8208 8392`, `h 8386`, `h 8215`: no break; pad: `textmap.py 5196 8192 5262 8236 --acid` (ring, bright centre, green hole, pit; its poly leaves west along y 8205-8220); `textmap.py 5196 8150 5262 8204` (the metal y 8165-8180 turns south at x 5223-5238 into the pad); `h 8170 4960 5260` (metal x 5031-5241); `textmap.py 5016 8140 5074 8190` (an L at x 5031-5043); T1 above it is thin and dim (values 9-B, with dark bars where rows pass under it) and fails the metal test (`v 5038 8055 8190`), as `lc1` found |

## Ports

`ports.d/lc2.txt` (kept in step with this). Latch B: enable `lc2_w8169` north on metal x 5560 at y 8067 (into
`lc1`; believed to run to (5558,7646)); clear `lc2_w8254`, output `lc2_w8341` and data `lc2_w8450` end on stubs
of their metals (pads (5472,8254), (5514,8341), (5558,8450): the metals run on, not followed); the rails vss
and vcc at y 8060/8067 and y 8560. Latch C's output Na `lc2_w8822` no longer leaves
the strip (run 4: it ends on the inverter below the latch); the VSS rail ends at y 9176.

Run 3 (latch D's lower unit and the bus field):

| Name | Layer | Where | Dir | What |
|---|---|---|---|---|
| `lc1_w7928` | M | 5918-5932, 8067 | out | the lower unit's node, by the thin metal to `lc1`'s upper unit (meets `lc1`'s port) |
| `lc1_w7928` (`lc2_w8083`) | P | 6401-6415, 8067 | out | the same node's row, north out of the strip (one net with the metal only through the cell's `?` tie) |
| `vss` | M | 6015-6063, 8067 | - | the east rail (meets `lc1`'s) |
| `lc2_w8646` | M | 6159-6177, 8067 | in | latch C's enable, north into `lc1`'s strip (no port of `lc1` there) |
| `lc2_w8646` | M | 6450, 8292-8310 | ? | its branch east (metal B) |
| `lc1_w7908` | M | 6203-6221, 8067 | in | latch D's enable (meets `lc1`'s port) |
| `lc1_w7908` | M | 6450, 8250-8268 | out | on east (metal A) |
| `lc1_w7864` | M | 6248-6264, 8067 | in | latch D's and latch C's clear (meets `lc1`'s port) |
| `lc1_w7780` | M | 6287-6307, 8067 | in | latch D's data (meets `lc1`'s port) |
| `lc2_w8474` | M | 6332-6350, 8067 | ? | the metal of the pad (6341,8214) |
| `lc2_w8474` | P | 5400, 8509-8526 | ? | drawn end (run 4): the poly from the pad (5428,8516) runs on west |
| `lc1_w7170` (`lc2_w8474`) | M | 5030-5046, 8067 | out | run 6: the metal of the pads (5232,8214), (5428,8516), (5428,8648), (5429,8994), north as `lc1`'s T1 (meets `lc1`'s port) |
| `lc2_w8474` | P | 5196, 8205-8220 | ? | run 6: drawn end: the poly of the pad (5232,8214) runs on west |
| `lc1_w7468` | M | 5073-5093, 8067 and 5465-5481, 9233 | in, out | run 6: `lc1`'s M_c2 down the staircase and through the strip into `lc3` |
| `lc3_w9299` | M | 5422-5438, 8067 | in | run 6: row 4's metal, north into `lc1` (`follow.py`: to about (5541,7433)) |
| `lc2_w8474` | M | 5421-5437, 9233 | ? | round 3: the metal runs on south into `lc3` |
| `lc1_w7864` | P | 6450, 8911-8936 | out | round 3: the poly from latch C's clear pad, south-east out of the strip |
| `lc2_w8341` | M | 5508-5524, 8067 | out | run 4: latch B's output Na, north into `lc1` |
| `lc1_w7864` | M | 5466-5486, 8067 | in | run 4: latch B's clear (meets `lc1`'s port) |
| `lc2_w8172` | M | 6422-6440, 8067 | ? | from the north |
| `lc2_w8172` | M | 6450, 8163-8181 | ? | on east |
| `lc2_w8906` | M | 6462-6480, 8067 | in | latch C's data, north (20 px east of the strip) |
| `lc2_w9124` | M | 5967-5981, 8067 | out | run 4: the thin metal, NOT latch C's Na, north into `lc1` (`lc1`'s notes, Ambiguity 8: it crosses the upper unit) |
| `vcc`, `vss` | M | 5840-5890 and 5659-5705, 9256 | - | run 5: both rails drawn on to `lc3`'s pieces |
| `lc3_m5756` | M | 5749-5763, 8067 | ? | run 5: the east thin metal, north through latch B into `lc1`; no contact found in the strip |
| `lc3_m5756` | M | 5749-5763, 9256 | ? | run 5: the same metal on south (meets `lc3`'s) |
| `lc2_w8450` | M | 5618-5634, 9256 | out | run 5: latch B's data, the west thin metal on south (joined to `lc3_m5626`) |
| `lc2_w9125` (`lc2_w9185`) | P | 5924-5940, 9256 | out | run 5: the AND-OR-INVERT's output poly, south into `lc3` (joined to the node through uncertain items) |
| `lc2_w9034`, `lc2_w9079`, `lc2_w9210` | P | 5545; y 9024-9044, 9068-9090, 9200-9220 | in | run 5: gate rows 2, 3, 5, drawn ends: they run on west |

## Ambiguities

1. The latch's load ties are `tl1`'s `?` items (in the cells), so `lc2_w8215` and
   `lc2_w8341` are DEPENDS in `unsure.py --equations`.
2. The gate widths are the cell's; the copy's rows were profiled only at their east ends in
   the noisy chip-2 stripped shot (Latch B, (c)).

3. **The metal x 6422-6440 over the top of latch C's data poly (y 8117-8181): no contact** (run 3). The metal
   comes from the north, lies on the poly x 6420-6443 for 64 px and turns east at y 8163-8181; the poly's top
   turns east to its own pad (6470,8127), on the metal x 6462-6480. A contact here would join `lc2_w8172` and
   `lc2_w8906`. Against one: both metal shots are bright along the 64 px with one dark bar at y 8110-8120 (the
   poly's top edge) and none below it, so no ring (`textmap.py 6396 8030 6462 8204 3 --acid`); the clean shot
   under it has values 3-5 and no hole; the poly is not a stub (it has its pad). For one: the clean shot under
   the metal is yellowish and speckled, not salmon (the clear's cross-under is the same colour under A and B,
   where a contact is impossible), and the chip-2 stripped shot has a small paler spot at (6426,8130), 6 x 9 px,
   at the poly's west edge. Working assumption: no contact. `e2.png` (4.6x, four shots), `e4.png`.
4. `lc1_w7928` and its row `lc2_w8083` are one net only through the `?` tie of the unit's load plate (the metal
   is on the plate, the row on the node's box): an alias, as `tl1`'s `tl1_w4287` / `tl1_w4095`.
5. The dark line 8 px wide at x 6439-6447 across the east turn of the metal x 6422-6440 (both chips) is read as
   the edge of the poly underneath, not a gap between two metals (bare ground between metals is 15 px or more
   here and 9-A in the chip-2 map; this is 3). If it were a gap, the piece east of it would be another net.

6. **The thin metal x 5967-5981 over three tie boxes: drawn uncertain, taken to pass over** (run 4). `tl5_tracks.py
   v 5972 8060 9215` finds no metal in either chip at y 8097-8136 (over the `?` tie box of latch D's lower unit, copy
   coordinates (5967-5995, 8113-8134)), y 8727-8759 (the tie box of latch C's `tl1_ub`, about (5988,8738)) and
   y 8833-8872 (the tie box of latch C's `tl1_ua`, (5968-5996, 8849-8870)). `textmap.py 5950 8090 5998 8150`, `5950 8718
   5998 8768`, `5950 8826 5998 8880` (with `--acid`): each is dark for the box's length; the first has a bright spot
   in chip 2 only (x 5974-5977, y 8111-8120; chip 1 has 4-6 there), the third a weaker one (chip 2 "CB" at y 8850,
   chip 1 none), the second none; the clean shot has no green hole on the metal's line in any of them. This is
   `tl1`'s open question about its thin metal W (re-read item R41): a contact on a tie box, a cut, or a metal that
   goes dark over the box. Here the metal's driver is known, which `tl1` did not have: it carries NOT `lc2_w8822`.
   A contact on the third box would tie the inverter's output to the plate of its own input's node, and one on the
   first to latch D's node `lc1_w7928`, another latch: neither is a circuit. A contact on the second (latch C's
   other node `lc2_w8688`, which is the inverse of `lc2_w8822` whenever the latch is settled) would be consistent
   but would make the inverter pointless. A cut at any of them would leave the stretch north of it without a
   driver here. Working assumption: one metal, no contact, as `tl3` drew its thin metals (its Ambiguity 11). The
   three stretches are `?M`, so the net's stretches north of each depend on them.

7. **Drain A: one diffusion, or a poly line with buried contacts** (run 5). The band under the rail (y 8913-8936)
   and its narrow arms (about 13 px between their edge lines) west to the contact box (5608-5640, 8904-8930) and
   east to the upper load are drawn as one diffusion. Against that: in the open gap at x 5730 the arm is dark
   red-brown in the clean shot and orange in the chip-2 stripped shot, as a poly would be, and the west box has
   poly values round its pit in the chip-2 stripped shot. For it: under the rail the clean shot shows one tan band
   with no line inside it (`h11.png`, 6.5x); a 13 px strip between two edge lines has no colour of its own
   (trap 4); and in the metal shots the gap's blue is 87-95, as diffusion (review round 5). Either way the same
   nets are joined.
8. **How the AND-OR-INVERT's output poly joins node D: not resolved** (run 5, after review round 5). The poly block
   below the lower plate (5797-5838, 9150-9198) is separated from the plate by a dark line at y 9143, which is
   also where the strip's lower edge runs under them (`px.py col 5818 9130 9210`: poly to y 9138, dark at y 9142-9146,
   poly again from y 9150). Either the block is the plate's continuation (drawn so, as an uncertain poly), or it
   is a separate poly whose ringed box (5813-5831, 9156-9178) is a buried contact onto a tab of node D's strip
   (not drawn). In both readings the row that leaves east carries node D, and the extraction joins them only
   through uncertain items (`lc2_w9185` is an alias). If neither holds, the row is another net and node D's only
   exits are its load and the box of Ambiguity 9. The plate's own tie is the box under its top bar.
9. **A box on node D under the west thin metal, (5594-5652, 9108-9138): not drawn** (run 5). A rounded rectangle in
   both chip-2 shots, poly-coloured west of the metal, diffusion tan under it, field west of it. It sits where the
   mirror image of the inverter below latch C has its output's buried contact, so it is probably node D's output
   box with a poly stub on it and no row leaving (as the stub on latch B's box). The thin metal over it is bright
   between two bars of 10-13 px with no hole and no widening: no contact (tracer and reviewer).
10. **The east thin metal x 5749-5763** (`lc3_m5756`) is drawn uncertain inside latch B (y 8114-8548: dim and 5 px
   west of its line, `textmap.py 5738 8108 5774 8206`) and over three stretches south of it where neither chip
   passes the metal test (`tl5_tracks.py v 5757 8920 9245 --half 6`). No contact was found on it anywhere in the
   strip, so its net is not known here.

## Not done

Run 5:

- (Done: the gate column south of latch B, latch B's data wire, the thin metal through latch B.)
- The ringed box (5813-5831, 9156-9178) in the output's poly block and what lies under it (Ambiguity 8); the box on
  node D's west lobe (Ambiguity 9); the area (5785-5830, 9200-9265) below the block is field (round 6: red minus green 0-2 in the chip-2 stripped shot).
- The output poly's leg x 5924-5940 runs on south in `lc3`'s strip to about y 9540 and turns east along y 9525-9545 (round 6; not drawn by `lc3`).
- Rows 2, 3 and 5 west of x 5545. The other lines of the staircase (run 6 drew three): one from a pad (5200,8258) east along y 8259 and south on x 5300, x 5343, x 5386 (`follow.py 5300 8300 S`: to y 9707); one from a pad (5235,8298) south on x 5260; pads (5257,8425), (5295,8472), (5341,8539), (5341,8562), (5341,9038); the pad (5123,8080) and its metal.
- Geometry noted by review round 5 and not re-measured: the upper load's channel may be y 8889-8935 (drawn
  8911-8940).

Run 3 (2026-11-18 16:28 -0600):

- (Done, run 4: the inverter below latch C and the thin metal x 5967-5981.) North of y 8067 the thin metal runs on
  through `lc1`'s upper unit (not drawn there). **A poly passes under the VCC rail at y 9178-9196** (salmon from
  x 5830 to x 5890) and goes on east in the open to x 5945, where it turns south (`o3_a.png`, `o3_m.png`): not drawn,
  part of the cluster that runs on into `lc3`.
- **`lc2_w8474`'s poly west of (5400,8517)** (run 4: drawn to there; it runs on west past x 5150), and its
  metal x 6332-6350 north of y 8067 (`lc1` has no port there).
- North of y 8067 (in `lc1`'s strip, not drawn by it): latch C's enable metal x 6159-6177, the node's row
  x 6401-6415 (`lc2_w8083`), the metal x 6422-6440 (`lc2_w8172`), latch C's data metal x 6462-6480.
- East of x 6450: metals A (`lc1_w7908`), B (`lc2_w8646`) and the turn of `lc2_w8172` (y 8163-8181).
- The thin metals through latch B (x 5748-5764) and the one drawn `?` here: R41's question (Ambiguity 6).
- From review round 2: the thin metal x 5962-5982 is dark for about 35 px over the `?` tie box of latch D's lower
  unit at about (5978,8118), with a bright spot in chip 2 only (x 5975-5981, y 8109-8121), none in chip 1 and no
  hole in the clean shot: to be measured as `tl1`'s thin W was when the metal is drawn. A strip under the VCC
  rail at x 5857-5878, y 8110-8152 reads as diffusion and is not drawn (VCC to VCC). The copy's gate 2 lies
  5-7 px north of where the cell puts it, and the copy's VCC contact about 8 px west (geometry of the cell copy).
- **R31**: latches B and C were traced and reviewed on Opus and still want a Fable review; run 3's review covers
  only run 3's piece.

- **An undrawn thin metal through latch B** (review round 1): x about 5748-5764, from north
  of y 8040 to south of y 8560, the copy's counterpart of tl1's "thin metal W" (the cells
  do not carry it). Continuous in both metal shots (`cache/scratch/lc2/review-1/m5750.png`,
  `w_south.png`); no contact ring seen on it inside the latch (a dark speck at (5758,8438)
  in the clean shot has no ring in either metal shot). Not drawn: follow it north into
  lc1's region and south into lc3's, and look for its contacts, before drawing it.
- t132 at (5716,8472): the cell gives L = 12 (poly x 5710-5722); the photo shows the poly
  at x about 5708-5727 (about 18 px). Geometry only; the cell copy was not changed.
- Gate-width profiles of the three loads (t133-t135) were not taken.

1. Latch B's tracks: clear and Na are drawn (run 4). **Data**: the metal from the pad (5558,8450) goes south to
   y 8607, east to x 5626 and south to a ring at about (5621,8908) at the top of the gate column under the VSS
   rail (x 5625-5760, y 8915-9240: five gate rows at y 8942-8955, 9028-9041, 9072-9085, 9159-9171, 9202-9214,
   `railprof.py 5662 5702 8880 9240`; two loads at (5800-5838, 8905-8968) and (5800-5840, 9060-9130) on the VCC
   boxes that latch C's cell and the inverter use): not drawn; it is the next piece. The thin metal x 5750-5763
   through latch B (dim and 5 px west of its line inside the latch, `textmap.py 5738 8108 5774 8206`) runs on
   south over that column's load tab at about (5770,8960) and on to y 9240: not drawn. The staircase of metals
   west of the latch (x 5400-5560) is not drawn (`follow.py 5421 8100 S`: south, east at y 8308, south, east at
   y 8387, south on x 5517 to y 8785, east, south on x 5559 to y 9142).
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

### Run 3: latch D's lower unit and the bus field (traced and reviewed on Fable 5.2)

Round 2 (full review of run 3's piece, 2026-11-18 16:47 -0600, a fresh agent on claude-fable-5-2, at commit bf266fb;
images in `cache/scratch/lc2/review-2/`, 13 used). The rounds of this section are counted through the package:
round 1 was each of the two Opus reviews above. Told to suspect: a contact of the metal x 6422-6440 on latch C's
data poly (Ambiguity 3); the dark line at x 6439-6447 across that metal's turn; the four pads with no green hole;
the T of metal B and the corner of metal A; the three cross-unders under A and B; `lc2_w8474`'s link, its row
under the VSS rail and its path under the VCC rail; the cell copy and which row is which gate; the node's row;
anything left out. Checked at 4-5.6x in the metal shots, the clean shot and the chip-2 stripped shot, with
`px.py`, `textmap.py`, `railprof.py`:
- Ambiguity 3: no contact (no ring or widening in either metal shot, no hole in the clean shot, no pit in the
  chip-2 stripped shot, where the pad (6470,8127) beside it has one; the yellowish colour is not evidence: the
  poly x 6258 is yellower still under A and B). The dark line at the turn is the poly's edge underneath (its
  profile matches the same edge under A and B). The poly arm to the pad (6470,8127) is joined.
- All ten pads: ring and bright centre in both metal shots and pits in the chip-2 stripped shot.
- B is a T on the metal x 6168 with no line across; A starts at x 6203 with 25-30 px of bare ground to x 6168.
- The three cross-unders are straight, pad to pad, without taps. `lc2_w8474`: the link is continuous, the lower
  row has field between x 6104 and x 6148 (it does not reach the pad (6212,8516)), poly over field under the VSS
  rail with field above latch C's box, plain salmon without a contact under the VCC rail, and on west.
- The cell copy: every item on a feature; the inverter's gate is on the lower row (data), the upper row goes to
  the pad (6212,8128). The node's row is one poly to x 6415 and north, with no contact under the five metals.
  The VSS rail is one metal. Nothing left out but the known thin metal.

Findings, all geometry only, each checked by the tracer:
1. The copy's gate 2 is drawn at y 8123-8141 and lies at y 8116-8136 in the photo. Confirmed (`px.py col 6150`:
   the row at y 8118-8134). It is the cell's item in this copy (5-7 px); the hand-drawn row y 8118-8135 east of it
   is right. Not changed: a cell copy is not redrawn item by item (re-read item R35 covers the masters).
2. The copy's VCC contact of the inverter's load is drawn at (5873,8186); the ring's centre is at x 5857-5872,
   y 8173-8197. Confirmed (`textmap.py 5842 8164 5890 8206`); the drawn contact overlaps the ring and is on the rail
   and the box. Not changed (the cell's item).
3. In `lc1`'s instance, not this package: the pad of `lc1_w7862` has its hole at (6105,8265) against (6115,8272)
   drawn. For the handoff.
Notes from the reviewer, in Not done: the thin metal x 5962-5982 is dark for about 35 px over the cell's `?` tie box
at about (5978,8118), with a bright spot in chip 2 only (read as a pass-over); a strip under the VCC rail at
x 5857-5878, y 8110-8152 reads as diffusion and is not drawn (it would join VCC to VCC).
Not checked by the reviewer: north of y 8067, east of x 6450, `lc2_w8474` west of x 5835.

No trace file changed after the review, and the connections are as reviewed:
`tools/t.sh lc2 sameconn.py bf266fb`: `connections identical`;
`.venv/bin/python tools/sameconn.py bf266fb`: `connections identical`.

Round 2: no findings that change a connection.

Round 3 (full review of run 4's pieces E and F and the first review on Fable 5.2 of latch C, re-read item R31;
2026-11-18 17:48 -0600, a fresh agent on claude-fable-5-2, at commit 9c85272; images in `cache/scratch/lc2/review-3/`). Told to
suspect: a contact of the thin metal x 5967-5981 on any of the three tie boxes or a break in it; the corner of Na's
metal and the gap between it and the data pad's metal; the inverter's copy; latch C's two copies, its five rows,
the two contacts of its thin metal and whether its clear and Na pads share a metal; the pad (5428,8516), the metal
x 5421-5437 between the two pads, taps on the row y 8634-8652; the metal x 5466-5486 to latch B's clear pad.
Checked at 4-4.4x with `px.py`, `textmap.py`, `tl5_tracks.py`, `follow.py`: latch C's copies, rows (each to its own
pad, no hole under the metals x 6167 and x 6212), thin metal x 5928 (two contacts, nothing between), clear and Na
pads on separate metals (75 px of open ground), the equations; the inverter (gate row from the pad (6211,9082),
output box joined to the pad (6168,9124), load strip into the VCC box, VSS rail's end y 9175); Na's metal one L,
bare ground y 8929-8937 between it and the data pad; the thin metal x 5967-5981 without a green hole anywhere on
its run (tie boxes 1 and 3 show a bright spot in chip 2 only, box 2 none); the metal x 5466-5486 unbroken to the
clear pad; x 5508-5524 over the clear row without a hole; the row y 8634-8652 one poly without pad or hole under
six metals. Findings, each checked by the tracer:
1. **The metal x 5421-5437 has both pads in its run** (changes a connection: where `lc2_w8474` leaves, and one
   more contact). Confirmed: `tl5_tracks.py v 5429 8440 8520` (metal at y 8470-8493 directly above the upper pad's
   ring), `textmap.py 5370 8456 5448 8500` (the metal turns west along y 8468-8484 and north on x 5379-5391),
   `v 5429 8640 9240` (metal to the strip's edge, a ring and a hole at y 8994), `textmap.py 5404 8972 5455 9016
   --acid` (ring, bright centre, green hole and pit at (5429,8994) on a poly pad), `tl5_tracks.py rows` (the pad's
   poly runs north under the metal to the row y 8939-8958, which runs east past x 5545: the first gate row of the
   column south of latch B). Fixed: the metal drawn from (5385,8440) through both pads to y 9233, the third pad
   and contact, its poly and the row to x 5545.
2. **A poly leaves latch C's clear pad (6257,8731)** south and diagonally south-east under three metals, out of
   the strip at x 6450 (changes a connection: a further branch of `lc1_w7864` leaves the strip). Confirmed on
   `r3_clr.png` (2.5x, clean and metal: one poly from the pad to the view's edge at (6470,8950), no pad where the
   three metals cross it). Fixed: drawn to the strip's edge (path corrected by the fix check, round 4).
3. Geometry only: latch C's copy of the cell's thin metal `lc2_w9005` lies at x 6096-6110 (drawn 6105-6119), its
   contacts at (6104,9002) and (6117,8600) against (6115,9008) and (6122,8602) drawn; on the same pads. The cell's
   items in this copy: not changed (as lc1's copy, round 2).
4. Recording: `lc2_w9124` had one label, so `tools/unsure.py` did not list its dependence on the three uncertain
   stretches. Fixed: a second label at (5974,8080).
Not checked by the reviewer: whether the thin metal is continuous across its three dark stretches; the pad
(5428,8516) (ring in both chips, centre in chip 1 only, no green hole: probably a contact, not proven); which
supply each rail is.

Round 3: two findings that change a connection, fixed (a fix check follows).

Round 4 (fix check of round 3's fixes, 2026-11-18 17:54 -0600, a fresh agent on claude-fable-5-2, against commit 9c85272, at
commit b14ffdb; images in `cache/scratch/lc2/review-4/`). Checked: the metal's corner (one metal x 5381-5437 along
y 8476 and up x 5385; bare ground x 5437-5466); its run y 8660-9233 (no branch; the only holes at y 8648 and y 8994);
the contact (5429,8994) (ring and bright centre in both chips, green hole) and its poly (north to the row
y 8939-8958 only, field between that row and the row y 8895-8915); the row y 8939-8958 (west end x 5425, one poly east
past x 5545 over field, no contact under the metals x 5472 and x 5560); the diagonal poly (leaves the pad itself,
one poly to x 6450, no hole, ring or pad where the three metals cross it); the second label; `sameconn.py` both ways.
One finding, geometry only, checked by the tracer:
1. The diagonal poly was drawn beside the real one: it runs east from the pad's foot along y 8750-8768 to about
   x 6285 and then at 45 degrees (centre y = x + 2473), 14-24 px north of the drawn line. Confirmed (`px.py col 6350`:
   the poly at y 8814-8834; `px.py row 8760`). Fixed: `P 6258,8742 y8758 x6285 6450,8923 w=20`; the port moved to
   (6450, 8911-8936).
After the fix: `tools/t.sh lc2 sameconn.py b14ffdb`: `connections identical`;
`.venv/bin/python tools/sameconn.py b14ffdb`: `connections identical`.

Round 4: no findings that change a connection.

Round 5 (full review of run 5's piece G, 2026-11-18 18:28 -0600, a fresh agent on claude-fable-5-2, at commit ea007da; images
in `cache/scratch/lc2/review-5/`, 19 used). The piece as reviewed claimed one five-input NOR whose three drains were
strapped by both thin metals. Told to suspect the five contacts of the thin metals and the places said to have
none, the VSS contacts of nodes B and D, drain A, the rows, row 4's pad, the joins across y 9233, the lower load's
link, the box in node D, the thin metal through latch B. Findings, each checked by the tracer:
1. **Node D (y 9092-9156) is not on VSS** (changes connections). Confirmed (`textmap.py 5660 9088 5722 9162 --acid`
   against `5660 8960 5722 9030`: plain bright metal and one clean value over node D, ring, blobs and pits over
   node B; the tracer's "hole 55 px long" was the plain diffusion under the rail). Its diffusion runs east into
   the lower load's strip (confirmed: `px.py row 9120`). So rows 2-5 are an AND-OR-INVERT gate on node D, and the
   uncertain link from the lower load to node C was field. Fixed: the contact and the link removed, node D joined
   to its strip.
2. **Four contacts of the thin metals were unsupported**: (5758,8923), (5757,9058), (5759,9189), (5626,9189)
   (changes connections). Confirmed: none has a ring, a pad or a hole; the greenish patch in the chip-2 stripped
   shot is also there where the metals cross node D; and with finding 1 nodes C and E are the middles of series
   pairs, where a strap makes no circuit. Fixed: removed. The east thin metal now touches nothing in the strip
   (label `lc3_m5756`); `lc2_w8450` = NOT `lc2_w8474`.
3. **The box on node D** (Ambiguity 9) now bears on where node D goes; the reviewer could not settle it. The tracer
   looked for another exit and found the poly block below the lower plate with its row east and south
   (`k1.png`, `textmap.py 5792 9140 5846 9204 --acid`, the two `rows` scans): drawn, joined to the plate by an
   uncertain poly (Ambiguity 8).
Geometry only: the VSS rail is x 5668-5713 (drawn 5659-5705: redrawn at x 5665-5711, as `lc3` has it); node B's
east edge is x 5710 above y 9005 (redrawn); the column narrows to x 5642-5723 near y 9240 (redrawn); the upper
load's channel may be y 8889-8935 (not re-measured: Not done).
Found correct by the reviewer: node B's contact; node F into `lc3`'s contact; rows 2-5 crossing the column and
ending separately; no other contact on a row; the contact (5622,8910) and the west metal through it to y 9300; row
4's pad and its metal to `lc3`'s pad; the lower strip into its VCC box; no contact where either metal crosses node
D or the west one node C; Ambiguity 7 (diffusion). Not checked: the thin metal through latch B beyond one 2.5x
view; the upper load's tie and strip end; the rails across y 9233 above 3.3x.

Round 5: three findings that change a connection, fixed (a fix check follows).

Round 6 (fix check of round 5's fixes, 2026-11-18 18:44 -0600, a fresh agent on claude-fable-5-2, against commit ea007da, at commit
7930f31; images in `cache/scratch/lc2/review-6/`, 8 used). Checked: node D (rail plain bright over it in both chips,
node B's contact with ring and holes; the strip unbroken tan x 5744-5768 at y 9120, its south edge line unbroken
x 5764-5836, its north edge open only at x 5774-5788 where the tail joins; the tail is diffusion); the four removed
contacts (no hole, ring or widening at any; nodes C and E end at x 5754 east and x 5617 west with field beyond;
rows 2/3 and 4/5 not joined at their east ends); the new output poly (block, row and leg one poly; the leg runs on
south to about y 9540 and turns east; no contact under the VCC rail; the dark line at y 9143 has the same place and
width inside the poly as the strip's edge beside it, so it is the diffusion's edge under one poly, which supports the
uncertain join; the ringed box has a plain centre with nothing visible under it or leading to it; the area below
the block is field; rows 4 and 5 end 20 px short of the block); the geometry changes; the labels and aliases; both
`sameconn.py` runs (only the intended differences).

Round 6: no findings.
