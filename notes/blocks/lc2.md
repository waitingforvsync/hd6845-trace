# lc2: left-centre random logic, middle strip (x 4400-6450, y 8067-9233)

## Status

2026-11-18 23:15 -0600 (run 10, Matt Godbolt, on Fable 5.2). **Partial: the west cluster's east column: a second
toggle flip-flop, clocked by the first** (piece N, 20 transistors; 80 in the package; reviewed, rounds 16-18), **and the strip's last wiring** (piece P: four
through lines in the south-east corner, the west ends of three gate rows; reviewed, round 17). Run 9 is on main (87cff0c).

```
lc2_w8992 = NOT( lc2_w8298 & lc2_w9034 | lc2_w8450 | lc2_w8914 )          master   (depends: the lc2_w8450 term, as in the first)
lc2_w8914 = NOT( lc2_w8298 & lc2_w8862 | lc2_w8992 )                      master   FIRM
lc2_w9034 = NOT( lc2_w8862 & ( lc2_w8298 | lc2_w8914 ) )                  slave    FIRM
lc2_w8862 = NOT( lc1_w7170 & lc2_w9034 & ( lc2_w8298 | lc2_w8992 ) )      slave    (depends only on old uncertain metal of lc1_w7170)
```

The east column is the west column turned 180 degrees: the west column's own geometry is now the cell `lc2_ff`
(nothing of it changed: `sameconn.py`), and the east column is a copy of it with its own supplies and bus wiring.
Its clock is `lc2_w8298`, the first flip-flop's slave output (track C north to row C, then the fifth staircase line
south to the copy's clock pad): **the two are a two-stage ripple counter**, both cleared while `lc1_w7170` is low. The
second stage's slave output `lc2_w9034` **is row 2 of the AND-OR-INVERT south of latch B** (`lc2_w9125` =
NOT(`lc2_w9034` & `lc2_w9079` | `lc2_w9210` & `lc3_w9299`): its first input is now identified), is the gate of a
pull-down under the east rail south of the column (`lc2_w9171`, on into `lc3`), and leaves south into `lc3`. Full
extraction: 2379 nets, 4282 transistors, 0 errors, 0 warnings.

Earlier:

2026-11-18 22:15 -0600 (run 9, Matt Godbolt, on Fable 5.2). **Partial: the west column of the west cluster is
traced: gates K3 and K4** (pieces L and M, 11 transistors; 60 in the package; L reviewed, rounds 12-13; M reviewed, rounds 14-15). Run 8 is on main (bd81e81). **With latch K they are a toggle flip-flop**:

```
lc2_w8552 = NOT( lc2_w8475 & lc2_w8298 | lc2_w8450 | lc2_w8725 )          master, K1   (depends: the lc2_w8450 term)
lc2_w8725 = NOT( lc2_w8475 & lc2_w8692 | lc2_w8552 )                      master, K2   FIRM
lc2_w8298 = NOT( lc2_w8692 & ( lc2_w8475 | lc2_w8725 ) )                  slave, K3    FIRM
lc2_w8692 = NOT( lc1_w7170 & lc2_w8298 & ( lc2_w8475 | lc2_w8552 ) )      slave, K4    (depends only on track A being lc1_w7170)
```

`lc2_w8475` is the clock: the master follows the slave while it is high, the slave follows the master while it is
low, and each takes the other's outputs crossed, so the pair changes state once per pulse. `lc1_w7170` low clears it
(`lc2_w8450` = NOT `lc1_w7170` on the master, `lc1_w7170` itself in series in the slave: cleared, `lc2_w8552` = 0,
`lc2_w8692` = 1, `lc2_w8298` = 0). **Two names became one net each**: K3's output (`lc2_w8857`) is track C,
`lc2_w8298`; K4's output (`lc2_w8930`) is K2's data row, `lc2_w8692`. The older names are kept (`@alias`). The clock
arrives from the south-west on an L-shaped metal (not followed). Full extraction: 2366 nets, 4262 transistors,
0 errors, 0 warnings.

Earlier:

2026-11-18 20:56 -0600 (run 8, Matt Godbolt, on Fable 5.2). **Partial: the west gate cluster begun: its supplies and its
first latch** (piece K, 9 transistors; 49 in the package; reviewed, round 11: no findings that change a connection). Runs 4-7 are on main (a243a9d).

```
lc2_w8552 = NOT( lc2_w8475 & lc2_w8298  |  lc2_w8450  |  lc2_w8725 )     depends on uncertain items (the lc2_w8450 term)
lc2_w8725 = NOT( lc2_w8475 & lc2_w8692  |  lc2_w8552 )                   FIRM
```

The cluster (x 4580-5330, y 8330-9240) is two gate columns that share a VCC rail in the middle (x 4924-4980: `lc1`'s
rail 1, which jogs east above the cluster) with VSS rails outside (east, x 5104-5150: `lc1`'s rail 2 after its jog;
west, x 4752-4803: named by structure). The top two gates of the west column are a **gated cross-coupled latch**: two
AND-OR-INVERT gates, each with a series pair under the west rail (enable `lc2_w8475` and a data row) and a third
pull-down east of the rail gated by the other gate's load poly. Gate K1 has a fourth pull-down, `lc2_w8450`
(= NOT `lc1_w7170`, by track B): a clear. `lc2_w8298` (track C) sets it, `lc2_w8692` is the other data row (its source is
south, not traced). (The first reading of K1, shipped as c371889, was a plain two-input NAND: wrong, see the section.)
Full extraction: 2363 nets, 4252 transistors, 0 errors, 0 warnings.

Earlier:

2026-11-18 19:28 -0600 (run 7, Matt Godbolt, on Fable 5.2). **Partial: gate 9 of `lc1`'s gate column drawn** (piece I, 2 transistors,
hand-drawn on the pattern of `lc1`'s gates 7 and 8; 40 in the package; not yet reviewed):

```
lc2_w8127 = NOT lc1_w7990          FIRM
```

Its output row runs east under `lc1_w7468`'s horizontal metal to a pad (5127,8080), whose metal goes back north
into `lc1`'s strip (not drawn there). Same run (2026-11-18 19:31 -0600), piece J (wiring only): **the three poly rows above the west
cluster** (y 8205-8306). Each runs from the west pad of a staircase line to a pad on a metal track that comes up
the west side of the cluster: `lc1_w7170` (`lc2_w8474`) goes to the track x 4466-4484, which runs down the cluster to
about y 9794; the fourth staircase line (`lc2_w8907`) to the track x 4508-4526; a fifth line (`lc2_w8298`, begun at
its pad (5234,8300)) to the track x 4553-4571. So the signals that go to latch B's inverter and to `lc1`'s gate 2
come from, or go to, the west gate cluster. Full extraction: 2362 nets, 4243 transistors, 0 errors, 0 warnings.

Earlier:

2026-11-18 18:47 -0600 (run 6, Matt Godbolt, on Fable 5.2). **Partial: three lines of the staircase of metals west of latch B
drawn** (piece H, wiring only). Two joins to `lc1`, without an uncertain item:

- **`lc2_w8474` is `lc1_w7170`**, the input of `lc1`'s gate 2: its metal runs on from the pad (5232,8214), north, west
  along y 8172 and north as `lc1`'s thin metal T1. So latch B's data `lc2_w8450` = NOT `lc1_w7170`, and `lc1_w7140`
  is the same inverse made a second time. The extraction prints `lc1_w7170` for the net.
- **`lc1_w7468`** (`lc1`'s metal M_c2) comes down the staircase and runs south through the whole strip without a
  contact, into `lc3`.
- Row 4's metal (`lc3_w9299`) is drawn up the staircase to `lc1`'s strip at x 5422-5438.
- After review round 7: a fourth line of the staircase (from a pad (5190,8258) to the strip's south edge on x 5386) and
  a poly row y 8898-8915 from its contact (5386,8951) to the output box of the inverter that makes latch B's data. The row
  ends on the box behind a dark line: read as a buried contact, drawn uncertain (Ambiguity 11). If it is one, the
  fourth line carries `lc2_w8450`. `lc1`'s T1 between y 8067 and y 8150 is now marked uncertain, so `lc2_w8474` =
  `lc1_w7170` rests on it.

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
| the fourth line, `lc2_w8907` (`lc2_w8450` if Ambiguity 11's box is a contact) | a pad (5190,8258) (poly west from it), east along y 8251-8267 to x 5300; south to y 8439; east to x 5343; south to y 8520; east to x 5386; south through the strip's edge, with a contact (5386,8951) on a pad whose poly goes north under the metal and east as the row y 8898-8915 to drain A's box | `tl5_tracks.py h 8259 5150 5312`, `v 5300 8250 8446`, `h 8439`, `v 5343 8430 8530`, `h 8520`, `v 5386 8510 9256`: no break, one hole at y 8951; `textmap.py 5172 8236 5232 8282 --acid` (west pad: ring, centre, hole); `textmap.py 5362 8888 5416 8976 --acid` (the contact: centre in chip 1, hole 12 px, pit; the poly under the metal from y 8897 to y 8962); `tl5_tracks.py rows row 5360 5612 4 8907` (one poly x 5376-5612); `follow.py 5300 8300 S` (the metal runs on to y 9707 in `lc3`) |
| `lc2_w8474` = `lc1_w7170` | from (5385,8440) north to y 8385; west to x 5341; north to y 8214; west to the pad (5232,8214), which lies in its run; north to y 8172; west along y 8164-8180 to x 5037; north as `lc1`'s thin metal T1 | `v 5341 8208 8392`, `h 8386`, `h 8215`: no break; pad: `textmap.py 5196 8192 5262 8236 --acid` (ring, bright centre, green hole, pit; its poly leaves west along y 8205-8220); `textmap.py 5196 8150 5262 8204` (the metal y 8165-8180 turns south at x 5223-5238 into the pad); `h 8170 4960 5260` (metal x 5031-5241); `textmap.py 5016 8140 5074 8190` (an L at x 5031-5043); T1 above it is thin and dim (values 9-B, with dark bars where rows pass under it) and fails the metal test (`v 5038 8055 8190`), as `lc1` found |

## Gate 9 of `lc1`'s gate column (run 7, piece I): traced

The ninth gate of the column that `lc1` drew (its notes, "Inventory": VCC rail x 4755-4803, VSS rail x 4928-4980,
the column's build) straddles the strips' boundary. Views `n1.png` (3.3x), `n2.png`, `n3.png` (5.2x, clean and chip-2
stripped), overlay `o11_a.png` (3x).

| Item | Where | Seen |
|---|---|---|
| VCC contact box under rail 1 | (4758-4806, 8058-8132), contact (4777,8092) | tan box with specks in the clean shot, pitted in the chip-2 stripped shot |
| load | plate x 4808-4848, y 8045-8160, with a foot east along y 8132-8160 to a ringed box (4878-4905, 8115-8150): the tie | orange in the chip-2 stripped shot, nested outlines at the box in both shots |
| drain | a strip (4803-4866, 8060-8102) from the VCC box under the plate, then a band y 8102-8128 east under rail 2 to the output box | outlines in both shots |
| pull-down (131/21 after round 10: the diffusion is x 4910-5041, wider than the rail) | the gate row y 8071-8092 crosses the band's column under rail 2 (VSS contact (4955,8045) north of it, under `lc1`'s piece of the rail); the row runs from a rounded end at x 4893 east to `lc1_w7990`'s poly under the metal M_c2 (x 5072-5092) | `n2.png`: one salmon row into the poly from the north; 8 px of outline between it and the output's pad at x 5105 |
| output | box (5012-5043, 8108-8138; corrected by round 10), reaching under the thin metal T1 (no contact: review round 7); a row east along y 8118-8136 under `lc1_w7468`'s horizontal metal (no ring, no hole) to x 5140; a neck north (x 5118-5132) to a pad (5127,8080) with a green centre; metal north out of the strip | `n2.png`; `tl5_tracks.py v 5127 7900 8100` (ring y 8059-8099, hole at y 8084); `follow.py 5127 8050 N` (the metal runs far north into `lc1`'s strip, to about (5669,6848)) |

Rail 1 is drawn on to y 8160 only: `tl5_tracks.py v 4779 8060 9240 --half 12` shows it with short bars to y 8198 and
then many bars and a 44 px stretch without metal at y 8259-8303; the rails through the west cluster are to be read
with the cluster.

## The three rows above the west cluster (run 7, piece J): traced

Wiring only. Views `w2.png` (1.42x, clean over metal), `w3.png` (4x, the west pads), overlay `o12.png` (1.5x).

| Row | From (east) | To (west) | Seen |
|---|---|---|---|
| A, y 8205-8220, `lc1_w7170` | the pad (5232,8214) in the run of `lc2_w8474`'s metal | a pad (4626,8213) on a metal that comes east along y 8203-8221 from a corner (4475,8212) of the track x 4466-4484 | `tl5_tracks.py rows row 4560 5260 5 8212` (poly all the way); `h 8212 4590 5240`: holes only at x 4627 and x 5232 (the pads); the row passes under a metal x 4668-4712 and both rails |
| B, y 8248-8263, `lc2_w8907` | the west pad (5190,8258) of the fourth staircase line | a pad (4583,8258) on the metal y 8250-8268 from the corner (4517,8259) of the track x 4508-4526 | `rows ... 8254`; `h 8254 4560 5200`: holes only at x 4584 and x 5190. **The two rails jog east over this row** (rail 1 at x 4757-4888, rail 2 at x 4929-5147: round 10; not drawn): no hole and no pad on the row under them (trap 13) |
| C, y 8291-8306, `lc2_w8298` | a pad (5234,8300), where a fifth staircase line begins (metal east 15 px and south on x 5249-5265; a stub drawn) | a pad (4626,8301) on the metal y 8292-8310 from the corner (4562,8301) of the track x 4553-4571 | `rows ... 8298`; `h 8298 4600 5250`: holes only at x 4627 and x 5233 |

The five pads: `textmap.py 4598 8194 4650 8232`, `4562 8238 4614 8276`, `4604 8280 4656 8318`, `5214 8278 5280 8334` (ring and
bright centre in both chips, green hole in the clean shot at each). The three tracks are drawn from y 8330: they run
on south down the west side of the cluster (`follow.py 4475 8400 S`: to y 9794, with eight contact candidates;
`4517 8400 S`: to y 9360; `4562 8400 S`: to y 8520). They are inside `urch`'s `sl4` track, which turns east 11 px north
of the first of them.

## The west gate cluster: supplies and latch K (run 8, piece K): traced

Views `w1_a.png`, `w1_m.png` (1.15x), `x3_c2.png` (chip-2 stripped, 1.38x), `x4_m.png` (2.3x, the feeds), `x1`-`x8`
(2.6-6x), `y1`-`y16` (1.6-10x: `y4` the stack, `y6`, `y9_m` K2's east side at 8x, `y8_a`, `y8_c` K1's east side at 10x,
`y11`, `y12_c`, `y13_c` the VSS fingers, `y14` K1's load poly and tail, `y15` the clear row at 9x, `y16` the tracks),
overlays `o14_a.png`, `o14_c.png` (4x, clean and chip-2 stripped), `o15_a.png`, `o15_m.png` (3.9x); measurements in
`cache/scratch/lc2/survey.md`.

**Supplies.** Three wide metals run down the cluster:

| Metal | Supply | How it is fed |
|---|---|---|
| middle, x 4924-4980 | VCC | `lc1`'s rail 1 (x 4755-4803) comes down to y 8205, jogs east (a band y 8205-8270 to x 4892), down x 4840-4892 to y 8350, east in a block (x 4840-4980, y 8324-8400) and south. `tl5_tracks.py v 4954 8230 8420 --half 12`: 41 px without metal (y 8283-8324, open ground in the clean shot) between this block and rail 2's piece above it |
| east, x 5104-5150 (x 5084-5150 from y 8368) | VSS | `lc1`'s rail 2 (x 4928-4980) comes down to y 8283 and jogs east (y 8228-8283, to x 5150) onto it. `h 8300 4920 5160 --half 2`: at y 8300 the only metal is x 5104-5148 |
| west, x 4752-4803 | VSS **by structure** | a block (x 4666-4803, y 8300-8348) joins it to a wide vertical metal x 4668-4712 that comes from the north through `lc1`'s strip (not drawn there). The pull-down stacks' top nodes are on it; the loads are on the middle rail |

The three are drawn to y 8770 (they run on south). The contact boxes under the middle rail at x ~4935-4955
(y 8440, 8580, 8690, 8840, 8985, 9110, 9225) are loads' VCC contacts.

**Latch K** (x 4500-4985, y 8350-8750): gates K1 (above) and K2.

```
lc2_w8552 = NOT( lc2_w8475 & lc2_w8298  |  lc2_w8450  |  lc2_w8725 )      K1
lc2_w8725 = NOT( lc2_w8475 & lc2_w8692  |  lc2_w8552 )                    K2
```

Under the west rail (`railprof.py 4758 4796 8340 8640`, `4756 4768 8590 8950`):

| y | K1 | y | K2 |
|---|---|---|---|
| 8352-8465 | VSS: the rail's contact column (contacts (4775,8362), (4775,8398-8442)) | 8594-8638 | VSS node (contact (4783,8605): `textmap.py 4764 8594 4800 8624`) |
| 8466-8492 | row 1, `lc2_w8475` | 8639-8660 | row a, `lc2_w8475` |
| 8493-8515 | node | 8661-8680 | node |
| 8516-8538 | row 2, `lc2_w8298` | 8681-8703 | row b, `lc2_w8692` |
| 8539-8564 | output node `lc2_w8552` | 8704-8740 | output node `lc2_w8725` |

| Item | Reading | Seen |
|---|---|---|
| `lc2_w8475` (the enable) | the thin metal x 4641-4655 with a pad on row 1 (4648,8474) and one on row a (4648,8647); it runs on south | `textmap.py 4634 8456 4668 8496`, `4634 8632 4668 8664`; `y5_m.png` (4.4x, both metal shots): one continuous metal through both pads |
| rows 1, 2, a, b **end at the rail's east edge** (x 4800-4812) | the pink column x 4800-4815 beside the rail has no row edge crossing it | `y4.png` (3.6x), `y8_a.png` (10x) |
| row 2, `lc2_w8298` | from track C's pad (4561,8516); track C runs on south past the pad | `textmap.py 4546 8496 4582 8534`; `y16.png` (3.3x metal) |
| row b, `lc2_w8692` | west to x 4580, then south on a vertical poly x 4578-4596 (to y ~8900: not followed) | `y3_a.png` (3.6x) |
| K1's third pull-down, gate `lc2_w8725` | a finger of the VSS column runs east at y 8443-8462 to x 4878 (tan against olive field in the chip-2 stripped shot, open to the west: `y11.png` 7x, `y12_c.png` 8x); a tongue (x 4842-4872) joins it to the output's open diffusion; across the tongue the poly of the pad (4892,8481) (orange-red, the colour of the gates west of the rail) | `y8_a.png`, `y8_c.png` (10x) |
| ... its gate's source | the pad (4892,8481) is the north end of the thin metal x 4882-4899, whose south end is the pad (4892,8694) on K2's load poly | `y7_m.png` (4.2x both metal shots); `textmap.py 4874 8676 4912 8712` |
| K2's third pull-down, gate `lc2_w8552` | a finger of K2's VSS node east at y 8606-8628 to x 4868, a tongue (x 4836-4866) down to K2's open diffusion; across it the end (x 4832-4876, y 8630-8658) of the tail of K1's load poly | `y9_m.png` (8x), `y6_a.png`, `y6_c.png` (8x), `y13_c.png`; `px.py row 8644 4826 4904` (the 10 px dark line at x 4865-4874 between the end and the tail is the tongue's edge under the poly, as at the column's edge under the rows) |
| K1's fourth pull-down, gate `lc2_w8450` (**uncertain**) | the row y 8596-8612 from track B's pad (4517,8604) crosses the column west of the rail (orange-red at x 4700-4738) between K1's output box and the strip above row a, and ends at x 4756 beside K2's VSS box | `y15.png` (9x), `textmap.py 4500 8588 4536 8622`, `y16.png`. See Ambiguity 12 |
| K1's output | under the rail y 8539-8564; east into an open diffusion (4820-4868, 8500-8562); west to a ringed box (4700-4730, 8540-8576), whose poly row runs west (y 8552-8572) to a pad (4604,8560) on the thin metal x 4598-4611, which runs on south | `textmap.py 4590 8542 4624 8580`; `opendiff.py` |
| K1's load | poly (4868-4922, 8520-8590) over a diffusion strip y 8537-8565 between the open diffusion and a VCC box (4925-4985, 8540-8595, contact (4955,8580)); a foot west onto a ringed box (4830-4862, 8555-8587) on the output diffusion (the tie); a tail south (x 4873-4897, to y 8656) to K2's third pull-down | `y14.png` (7.5x), `x7.png` |
| K2's output | under the rail y 8704-8747; east into an open diffusion (4810-4866, 8712-8745); west to a ringed box (4706-4736, 8711-8747), whose poly runs west and then south on x 4622-4640 (to a row y 8813-8829: not followed) | `px.py col 4775`, `col 4820`, `row 8728`; `y3_a.png` |
| K2's load | the poly of the pad (4892,8694) (box 4872-4920, 8674-8716) runs south over a diffusion strip y 8722-8745 (red-dotted) between the open diffusion and a VCC box (4930-4985, 8665-8745, contact (4948,8689)), and west onto a ringed box (4842-4872, 8677-8703) on the tongue (the tie) | `y6_a.png`, `y9_m.png` (8x); `textmap.py 4936 8672 4972 8740` |

**How the first reading went wrong** (c371889: K1 as a plain NAND with row 1 running on east to the pad (4892,8481)).
Row 1 and the poly of that pad are in line and 30 px apart, with the rail's edge between; the 2.8x overlay looked
continuous. The 9 px of "field" measured between that poly and the output diffusion were the dark edge line (dark
pixels read as red-minus-green near zero in the chip-2 stripped shot too). It came apart when the same thin metal's
other pad turned out to be on K2's load poly.

## The west gate cluster: gate K3 (run 9, piece L): traced

(Piece M found that this section's `lc2_w8857` is track C's net `lc2_w8298`, and `lc2_w8930` is `lc2_w8692`: the
extraction prints the older names; the two labels stay in the trace as aliases, and are used below for the places.)

Views `z1_a.png`, `z1_m.png` (2.9x), `z2_a.png`, `z2_m.png` (6x, east side), `z3_a.png`, `z3_m.png` (6x, the stack),
`z4_a.png`, `z4_c.png` (9x), `z4_m.png` (4.6x, both metal shots), `z6_m.png` (6.3x, both metal shots), `z7_a.png`,
`z7_m.png` (6.3x, south of it); overlays `o16_a.png`, `o16_m.png` (4.3x); measurements in `cache/scratch/lc2/survey.md`.

```
lc2_w8857 = NOT( lc2_w8930 & ( lc2_w8725 | lc2_w8475 ) )
```

The west rail is wider here: x 4741-4812 from y 8800 (`tl5_tracks.py h 8848 4690 4850 --half 2`: metal x 4753-4812;
`h 8950`: 4758-4813). Under it (`railprof.py 4758 4796 8750 9245`):

| y | What |
|---|---|
| 8773-8805 | VSS box (4752-4798, 8762-8806), contact (4768,8780) (`textmap.py 4752 8764 4790 8800`) |
| 8812-8825 | row c, `lc2_w8725`: K2's output poly (x 4622-4640 south from its box) turns east at y 8810-8829; it ends at x 4797 (pink under the rail at x 4800-4815) |
| 8835-8860 | node N; it runs on east under the rail's east part (E: x 4802-4816, down to y 8900; pale and continuous at y 8838-8856, `z3_a.png`) |
| 8867-8889 | row d, `lc2_w8475`: from a pad (4649,8865) on the thin metal x 4641-4655 (`textmap.py 4632 8848 4668 8884`); under the rail it steps down and ends at x 4789 (round 12: a plain end cap, no hook) |
| 8890-8940 | box S: contact (4752,8908) to the rail, so VSS (`textmap.py 4732 8840 4816 8950`, `z6_m.png`: the metal over the box is the rail's; the lines in it are R/16 = 7 dips, the features beneath) |

N is between two VSS nodes, so it is not an end of a stack by itself: its only way out is east.

| Item | Reading | Seen |
|---|---|---|
| the strip, `lc2_w8930` | a vertical poly x 4818-4838 from y 8812 to y 8943, where it ends (round 12: `px.py col 4828 8920 8962`: peach to y 8941, pink from 8944) and leaves by an arm east at y 8925-8945 (drawn to x 4876; under the output's thin metal without a contact). It lies along E's east edge; beyond it an open diffusion X (4842-4866, 8805-8900: a plain pinkish lens in both metal shots). Taken as a gate between E and X (channel y 8838-8900) | `z4_m.png`, `z4_a.png`, `z4_c.png`; `tl5_tracks.py rows col 8796 8960 4 4828`. **Not seen directly**: Ambiguity 15 |
| load | one poly: a ringed box (4865-4895, 8803-8832) on X (the tie), a plate (4868-4925, 8836-8876) over a diffusion strip y 8846-8868 from X to a VCC box (4930-4985, 8805-8885, contact (4946,8830)), and a pad box (4868-4900, 8872-8904) | `z2_m.png` (6x), `o16_m.png`; `textmap.py 4932 8812 4962 8842` |
| ... a second strip | the poly east of the ringed box (x 4898-4925, y 8805-8836) is as red as the plate (`px.py col 4912 8798 8884`: clean 130-187/58-104/28-84 against the plate's 132-178/81-115/46-65 and a pad box's 232/159/128): drawn as an uncertain second load strip. It only strengthens the load | |
| output | the pad (4882,8890) (`textmap.py 4864 8872 4900 8904`) on a thin metal that steps west to x 4859-4873 and runs south to a pad (4862,8998) (drawn to y 8975) | `z7_m.png` (6.3x) |

## The west gate cluster: gate K4, and the flip-flop (run 9, piece M): traced

Views `z8_a.png`, `z8_m.png` (2.9x), `z9_a.png`, `z9_m.png` (5.6x), `z10_a.png`, `z10_c.png`, `z10_m.png` (8x, east side),
`z12_a.png`, `z12_m.png` (8x, lower east side), `z13.png`, `z13_m.png` (8.8x, four shots, the head of the load),
`z14_a.png`, `z14_m.png` (2.95x, the west side), `z15.png` (5.5x, node T), `z16.png`; overlays `o17_a.png`, `o17_m.png`
(4.3x); measurements in `cache/scratch/lc2/survey.md`.

```
lc2_w8692 = NOT( lc1_w7170 & lc2_w8298 & ( lc2_w8475 | lc2_w8552 ) )
```

The west rail is x 4757-4808 here and x 4757-4820 from y 9045 (`tl5_tracks.py h` at y 8990, 9030, 9052 ... 9185).
Under it (`railprof.py 4758 4796 8750 9245`):

| y | What |
|---|---|
| 8961-8976 | node T, the output (`lc2_w8692`) |
| 8977-8991 | row, `lc2_w8298`: from the pad box (4845-4885, 8975-9018) of the pad (4862,8998), where K3's output thin metal ends, west across the column and on to the END pad (4560,8996) of track C |
| 9001-9019 | node |
| 9020-9034 | row, `lc1_w7170`: from a pad (4473,9038) on track A; it ends at x 4826 |
| 9043-9062 | node Z |
| 9063-9078 | row, `lc2_w8552`: from the END pad (4604,9080) of the thin metal x 4597-4611 |
| 9087-9128 | VSS node, contact (4775,9100) |
| 9135-9148 | row, `lc2_w8475`: from the END pad (4648,9124) of the thin metal x 4641-4655 |
| 9158-9174 | node Z again |

| Item | Reading | Seen |
|---|---|---|
| Z is one node | in the metal shot one outlined shape (4826-4856, 9042-9175: top line y 9040, right side x 4852-4858, bottom line y 9175) lies east of the rail; the nodes y 9043-9062 and 9158-9174 are pale (diffusion under metal) east to x ~4828, the VSS node between them only to x ~4808 (pink beyond). So a diffusion strip x 4838-4852 joins the two round the VSS node and the two rows' end caps | `z12_m.png`, `z12_a.png` (8x); `px.py row 9052`, `row 9166`, `row 9010 4796 4876` |
| the stack's outline | x 4708-4855, y 8975-9178 in the metal shot: the column runs west of the rail to x 4708 (rows orange-red from x ~4705) | `o17_m.png`, `z8_a.png` |
| the pads | track C ends on (4560,8996) (`textmap.py 4544 8978 4580 9012`; nothing of the track at y 9016-9031); track A (4473,9038) (`textmap.py 4458 9022 4494 9056`), and it runs on south; (4604,9080) and (4648,9124) (`textmap.py 4588 9064 4622 9096`, `4632 9108 4666 9140`) | `z14_m.png`, `z14_a.png` |
| the clock's source | at the pad (4648,9124) an L-shaped metal arrives: y 9112-9132 from x 4560, then south at x 4553-4575 (drawn to y 9190) | `z14_m.png`, `z8_m.png` |
| node T east | a pale band y 8956-8972 from under the rail east to x ~4900; at its end a ringed box (4880-4905, 8922-8950) to the north and a diffusion strip to the south | `z15.png` (5.5x, three shots), `z11.png`, `z13.png`; review round 14: `tband.png`, `head.png` |
| T's load | the strip runs south from the band's end, x 4886-4900 beside the pad box (14 px between two poly edges: drawn uncertain) and x 4878-4900 below it, under a plate (4857-4926, 9040-9098; channel colour, `px.py col 4890 9040 9100`: 157-197/81-134/40-69) into an open diffusion (4878-4985, 9102-9132; `opendiff.py`: 4883-4909 x 9108-9130) joined to a VCC box (4932-4985, 9085-9132, contact (4952,9108)). W/L 22/58 | review round 14 (`neck.png`, `east_strip.png`, `east_strip2.png`); `px.py row 9014 4846 4906` (pink field south of the pad box: no neck), `col 4894 8950 9046` (uniform y 8962-9034) |
| the load's gate, T's tie, and K3's gate | the plate is one poly with a long poly x 4904-4926 that runs north over field (`px.py col 4914`: 71-140/38-91, darker than the plate's channel) to the ringed box, where it is tied to T and is one with the arm of K3's strip (`lc2_w8930`): so K3's series gate is T | `z13.png`, `z13_m.png`; round 14: the green rim at x 4903 runs y 8960-9036 and is absent at y 9040-9092; one bottom outline at y ~9096 |
| node T west, and K2's data row | T's band runs west of the rail to a ringed box (4694-4724, 8920-8954); on it ends the row y 8897-8916 that comes from the vertical poly x 4578-4596, K2's row b (`lc2_w8692`) | `z14_m.png` (the box with its ring), `z15.png` |

**What the four gates are.** With `c` = `lc2_w8475`: while `c` is high the master is open (`lc2_w8552` = NOT
`lc2_w8298`, `lc2_w8725` = NOT `lc2_w8692`) and the slave holds (`lc2_w8298` = NOT `lc2_w8692` and back); while `c` is
low the master holds and the slave is open (`lc2_w8298` = NOT(`lc2_w8692` & `lc2_w8725`), `lc2_w8692` =
NOT(`lc2_w8298` & `lc2_w8552`)). Stepped by hand from `lc2_w8552` = 1: `c` low gives `lc2_w8298` = 1, `lc2_w8692` = 0;
`c` high then gives `lc2_w8552` = 0, `lc2_w8725` = 1: it toggles. Outputs seen leaving: `lc2_w8298` on track C north to
row C and the fifth staircase line (pad (5234,8300)); the rest not followed.

## The west gate cluster: the east column, a second flip-flop (run 10, piece N): traced

Views `e1_a.png`, `e2_a.png` (2.9x, the first overlay of the turned west geometry on the clean shot), `e3_m.png`,
`e4_m.png`, `e5_m.png` (3.4x, the copy on the metal shot, in three parts), `e6_m.png` (5.5x, where the output leaves),
`e7_a.png` (6x), `e8_m.png` (5x, the clock's join); measurements in `cache/scratch/lc2/survey.md`.

**The copy.** `tools/t.sh lc2 findcell.py 4700 8440 4952 9180 --region 4900,8250:5400,9260 --min 0.3`:
`rot=180 o=4826,8810`, moved by 258,-66, score 0.62 (the K1/K2 east side alone: 0.64). A point (x,y) of the master is
at (9910-x, 17554-y). The west column's sections were rewritten as the cell `lc2_ff` (192 lines; the master stands
where it stood) plus the master's own lines (supplies, the bus tracks north of the cell, the clock's L-shaped metal,
the top of K1's contact column with its two contacts, the large open diffusion): `tools/t.sh lc2 sameconn.py 87cff0c`
and `.venv/bin/python tools/sameconn.py 87cff0c` both ended `connections identical` after the rewrite and before the
copy was added. One edge of the master moved for the copy's sake: K1's VCC box, east edge 4985 to 4978 (its copy
then stays clear of the master's long poly x 4904-4926, as the box (4932-4985, 8958-9018) does in the photo).

What the copy lands on (metal shot, 3.4x): the VSS contact (5135,8454) on a ring at (5130,8448); contact
(5142,8774) on a ring (5135,8770); pads (5262,8430), (5306,8474), (5350,8558), (5261,8689), (5261,8907),
(5306,8994), (5350,9038), (5262,9080) on pads within 4-10 px; the rows, the boxes, the load plates and the VCC boxes
under the middle rail on theirs. The middle rail is shared; the copy's VSS rail is the cluster's east rail
(x 5097-5150, drawn on to y 9160: `tl5_tracks.py h` at y 8800, 8900, 9000, 9120).

**The copy's own wiring.**

| Item | Reading | Seen |
|---|---|---|
| clock | the fifth staircase line: from row C's pad (5234,8300) (`lc2_w8298`) the metal goes east and then south at x 5247-5263 to the copy's clock pad (5260,8431) | `e8_m.png` (5x): one bright strip from the pad (5232,8300) to the pad; `tl5_tracks.py v 5260 8300 8440`: hole at y 8431 |
| the clear's two forms | the copy's row of the slave's series input ends on the pad (5428,8516) of the metal x 5421-5437 (`lc1_w7170`, drawn in run 5); the copy's clear row meets the row y 8941-8958 from the pad (5386,8951) on the fourth staircase line (`lc2_w8907` = `lc2_w8450`, drawn in runs 6-7) | `e3_m.png`, `e5_m.png` |
| the bottom of the column | the master's stack hangs from K1's contact column; the copy's ends in a box with a contact (5133,9105) to the east rail | `e5_m.png`: ring (5115-5150, 9090-9125) |
| output `lc2_w9034` | from its end pad (5343,9038) the pad's poly also leaves EAST as row 2 of the AND-OR-INVERT south of latch B (piece P; review round 16); track C' (x 5335-5352) runs on south from the pad, turns west along y 9160-9178 to x 5248-5262 and south across y 9233 into `lc3`; in its run a pad (5254,9208) whose poly leaves west along y 9200-9220 (drawn to x 5215) | `e6_m.png` (5.5x), `e7_a.png` (6x) |

**South of the column** (review round 16). The east rail runs on south (x 5084-5148; the dark bars at y 9158-9161 and
9176-9179 are edges beneath it). Under it (`railprof.py 5114 5148 9080 9300`): field y 9148-9166, a node y 9167-9181
(`lc2_w9171`), a gate y 9182-9195, a VSS node y 9205-9251 with a contact (5124,9224), and in `lc3` a second gate
y 9252-9266 and a node below it. The first gate is the poly from the pad (5254,9208) on the output's L-shaped metal:
`lc2_w9034`. The node `lc2_w9171` runs west past the rail's edge to a strip x 5060-5078 that goes south beside the
rail (outlined in the metal shot, dull in the clean shot: `s3.png` 10x, `px.py row 9172 5052 5112`): taken as a
diffusion joining it to the node below the second gate, as node Z's strip does in the flip-flop (review round 17:
diffusion, chip-2 stripped red minus green +12 to +18 along y 9166-9286, no poly on it, ending about y 9290 where it
turns under the rail); drawn to y 9256. The node also has a dead-end tab east of the rail to x ~5202 (round 17). Where the node's load is, is `lc3`'s (a VCC box with a contact (4950,9225), a ringed box near
(5020,9203) and a red-dotted plate (5000-5045, 9235-9300) are there: not drawn).

**The counter.** Stage 1 (west) changes state once per pulse of `lc2_w8475`; its slave output `lc2_w8298` is stage 2's
clock, so stage 2 changes once per two pulses. Both are held clear while `lc1_w7170` is low.

## The strip's last wiring (run 10, piece P): traced

Views `r1_m.png`, `r5_m.png` (1.15x, the whole strip with the trace), `r2.png` (1.9x), `o18_m.png` (2.05x, the through
lines), `r3_a.png`, `r3_m.png` (3.8x), `o19_m.png` (4.4x, the row ends).

**Four through lines in the south-east corner** (x 6280-6450, y 8600-9233; metal, no contact in the strip). Named by
their x at the south edge.

| Line | Enters (east edge) | Path | Leaves (south edge) |
|---|---|---|---|
| `lc2_x6299` | y 8630 | diagonal south-west to x 6342 at y 8738, south, west at y 9034 | x 6299 |
| `lc2_x6342` | y 8692 | diagonal to x 6385 at y 8757, south, west at y 9076 | x 6342 |
| `lc2_x6387` | y 8756 | diagonal to x 6428 at y 8778, south, west at y 9121 | x 6387 |
| `lc2_x6432` | y 9165 | west to x 6432, south | x 6432 |

`tl5_tracks.py h Y 6280 6450 --half 2` at y 8600, 8640 ... 9150 (14 heights: the metals' x at each);
`follow.py 6298|6342|6385|6430 9220 N --gap 16` (corners at (6299,9034), (6346,9076), (6393,9120), (6436,9168)). The
diagonal poly of `lc1_w7864` passes under the upper three: no contact (`textmap.py 6326 8800 6360 8832`,
`6366 8840 6402 8876`, `6412 8886 6446 8918`: metal bright, no ring, no hole). `follow.py` offered contact
candidates at (6384,8858) and (6471,9051): the first is that crossing, the second is outside the strip.

**The west ends of rows 2, 3, 5 of the AND-OR-INVERT south of latch B.**

| Row | West end | Seen |
|---|---|---|
| 2, `lc2_w9034` | runs west under the four staircase metals (no pad or ring on any) to the end pad (5343,9038) of the second flip-flop's output track | `r3_m.png`, `r3_a.png`, `o19_m.png`; `tl5_tracks.py rows row 5330 5560 5 9036`: poly all the way. The box above it at (5500-5540, 8960-9015) is open field (`px.py col 5520 8950 9066`), and the red-dotted stretch of the row there is the look of poly in a gap between metals, not a channel |
| 3, `lc2_w9079` | ends on a pad (5520,9081) of a thin metal x 5509-5527 that runs south into `lc3` | `textmap.py 5502 9060 5540 9096`; `tl5_tracks.py v 5518 9060 9233` |
| 5, `lc2_w9210` | runs west under the staircase metals to a pad (5341,9211) of a metal that starts there and runs south into `lc3` | `textmap.py 5324 9190 5360 9226`; `e6_m.png`: the pad is separate from the L-shaped metal above it |

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
| `lc1_w7170` (`lc2_w8474`) | M | 5030-5046, 8067 | ? | run 6: the metal of the pads (5232,8214), (5428,8516), (5428,8648), (5429,8994), north as `lc1`'s T1 (meets `lc1`'s port) |
| `lc2_w8907` (`lc2_w8450`) | M | 5378-5394, 9233 | ? | round 7: the staircase's fourth line on south into `lc3` (to y 9707 by the follower) |
| `lc2_w8907` | P | 5240, 8941-8958 | ? | round 8: drawn end: a second poly of the pad (5386,8951) runs on west into the gate cluster at x 5150-5240 |
| `lc2_w8298` | M | 5249-5265, 8334 | ? | run 7: drawn end: the fifth staircase line runs on south (`follow.py 5260 8350 S`: to y 9056) |
| `lc2_w8127` | M | 5118-5136, 8067 | out | run 7: gate 9's output, north into `lc1` (no port of `lc1` there) |
| `lc1_w7990` | P | 5072-5092, 8067 | in | run 7: gate 9's input (meets `lc1`'s port) |
| `vcc` | M | 4755-4803, 8067 | - | run 7: rail 1 from `lc1` (run 8: on to the cluster's middle rail) |
| `vss` | M | 4928-4980, 8067 | - | round 10: rail 2 from `lc1` (run 8: on to the cluster's east rail) |
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
| `vcc`, `vss` | M | 4924-4980, 4757-4820; y 9190 | - | run 9: the middle and west rails, drawn ends (they run on south into `lc3`) |
| `vss` | M | 4668-4712, 8067 | - | run 8: the west rail's feed, north into `lc1` (no port of `lc1` there); VSS by structure |
| `lc1_w7170` | M | 4466-4484, 9060 | ? | run 9: drawn end: track A runs on south past the pad (4473,9038) |
| `lc2_w8907` | M | 4508-4526, 8700 | ? | run 8: drawn end: track B runs on south (no pad to y 9150) |
| `lc2_w8475` | M | 4553-4575, 9190 | in | run 9: drawn end: the clock's L-shaped metal, from the south |
| `lc2_w9034` | M | 5247-5263, 9233 | out | run 10: the second flip-flop's slave output, south into `lc3` |
| `lc2_x6299`, `lc2_x6342`, `lc2_x6387`, `lc2_x6432` | M | 6450, y 8630, 8692, 8756, 9165 | ? | run 10: the four through lines at the east edge |
| the same four | M | x 6299, 6342, 6387, 6432; 9233 | ? | run 10: at the south edge, into `lc3` |
| `lc2_w9079` | M | 5509-5527, 9233 | in | run 10: row 3's thin metal, from `lc3` |
| `lc2_w9210` | M | 5334-5350, 9233 | in | run 10: row 5's metal, from `lc3` |
| `lc2_w9171` | D | 5062-5078, 9256 | ? | rounds 16-17: the top node of the stack south of the east column leaves by its strip, on into `lc3` |
| `vss` | D | 5104-5158, 9256 | - | round 17: that stack's VSS node, on into `lc3` |
| `vss` | M | 5084-5148, 9256 | - | round 16: the east rail on south into `lc3` |

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

11. **The row y 8898-8915 at drain A's box: a buried contact, drawn uncertain** (review round 7). The row comes from
   the pad (5386,8951) of the staircase's fourth line and ends at the west side of the box (5608-5640, 8904-8930),
   on which `lc2_w8450`'s metal has its contact. The chip-2 stripped shot shows poly colour up to x 5596, a 3 px dip
   at x 5599 and tan-to-poly values on to the pit (`textmap.py 5590 8886 5626 8934 --acid`); the clean shot a dark
   line 7 px wide at x 5600-5607. A row that ends on a diffusion box behind the box's outline is how the outputs of
   `lc1`'s column leave their boxes, and the row has no other end here. Drawn `?P`/`?B`. If it is not a contact,
   the fourth line and the row are a net of their own with the pad (5190,8258)'s poly as their only other end.

12. **Latch K: the column west of the rail, and K1's clear** (run 8). Under the rail (x 4752-4800) the gates are certain
   (`railprof.py`). West of it, x 4702-4752, all five rows (1, 2, the row from track B, a, b) turn from peach to
   orange-red at x ~4700 in the clean shot, and are yellow-orange in the chip-2 stripped shot (the colours of the gate
   of K1's third pull-down); but the narrow strips between the rows measure near field there (red minus green -4 to
   +15 at x 4712 and 4728, y 8580-8628; 13-24 between rows 1 and 2), each being 10-15 px between two dark edge lines.
   Drawn as uncertain diffusion (`?D`). For rows 1, 2, a, b it only widens channels that exist under the rail. **For the
   row from track B it decides a transistor**: K1's output box to the strip above row a (K2's VSS node), gate
   `lc2_w8450`. Adopted because the row ends at x 4756 on nothing else (no pad, no box): without the column it
   would do nothing. `tools/unsure.py --equations lc2_w8552`: without the uncertain items the term goes.
13. **The west rail is VSS by structure only** (run 8): its feed x 4668-4712 comes from north of the strip. Also: a
   large open diffusion (4588-4741, 8354-8424; `opendiff.py`) beside the contact column is drawn as one with it (only
   the rail's etch line lies between them). **It is larger than drawn**: in the clean shot the area under tracks C
   (to y 8430), B (to y 8540) and A (the whole way south) is the pale tan of diffusion under metal, and the chip-2
   stripped shot has interference fringes there (`y16.png`, `y16_c.png`): not drawn, not understood (Not done).
14. **Latch K, east of the rail** (run 8): two outlined shapes are taken as field: the strip (4812-4832, 8655-8705)
   west of K2's tongue (an outline that hooks from row a's end down to y 8708: `y9_m.png`), and the ringed end
   (4822-4842, 8466-8492) of the gate of K1's third pull-down, drawn as that poly's end over field. If either were a
   diffusion joined at both ends it would short an output to VSS, so neither can be.

15. **Gate K3: the strip x 4818-4838 as a gate** (run 9). That the strip crosses a diffusion joining E to X is inferred:
   N has no other way out (VSS above and below, no contact, nothing west), X has the load, and the edge lines of E
   (y 8834, 8904) run on under the strip. But the strip is peach there in the clean shot, not the orange-red of the
   other gates, and the chip-2 stripped shot is mixed (`px.py row 8855 4776 4876`). Drawn firm; if it is wrong, X has
   no pull-down at all. Also the second load strip (`?D`), above.

16. **Gate K4** (run 9, after review round 14). (a) The diffusion strip from T's band south to the plate is 14 px wide
   beside the pad box, between two poly edges; chip-2 colours do not separate so narrow a diffusion from field (it
   reads field-like there, red minus green -5 to -24), the clean shot has it dull to tan and uniform down its length.
   It is drawn `?D` for y 8970-9020. It is adopted because the plate below has a channel, the plate's poly is tied to
   T at the ringed box, and there is no neck from the pad box (pink field at y 9014): the load's source must be T.
   (b) What is under the ringed box's outline (T's band, the gate poly, K3's arm) is not seen. (c) My first reading
   (shipped as 514d86b) had the plate as a second load on `lc2_w8298` and the long poly as a 14/175 load: wrong.

17. **The east column as a copy** (run 10). The copy is exact geometry turned, so it carries the master's uncertain items
   to the same places (the diffusion west of the rail, here east of it; the strip to the slave's second load) and
   its fit is to within 4-10 px. Not separately read: every transistor of the copy. Read separately: its pads, its
   contacts, its clock, its clears' pads, its output's way out, the bottom of its column.

## Not done

Run 5:

- (Done: the gate column south of latch B, latch B's data wire, the thin metal through latch B.)
- The ringed box (5813-5831, 9156-9178) in the output's poly block and what lies under it (Ambiguity 8); the box on
  node D's west lobe (Ambiguity 9); the area (5785-5830, 9200-9265) below the block is field (round 6: red minus green 0-2 in the chip-2 stripped shot).
- The output poly's leg x 5924-5940 runs on south in `lc3`'s strip to about y 9540 and turns east along y 9525-9545 (round 6; not drawn by `lc3`).
- (Done, run 10: rows 2, 3 and 5 west of x 5545; the fifth staircase line is the second flip-flop's clock, and the pads near it are the flip-flop's.)
- (The VCC box (4932-4985, 8958-9018) seen by review round 14 is the copy's: drawn in run 10.) Seen by review round 14, not drawn: a diffusion under track A from y 9083 south (no contact to the track down to y 9199).
- (Done: both columns of the west cluster, the through lines, the row ends.) Left at the strip's edges: tracks A and B south of their drawn ends (y 9060, 8700) and the first stage's clock metal south of y 9190 (into `lc3`); the stack under the east rail south of y 9160 beyond its first gate, with its load (`lc3`'s: VCC box with contact (4950,9225), ringed box near (5020,9203), plate (5000-5045, 9235-9300)); a vertical metal x 4420-4442 at the west edge with pads (4432,8708) and (4432,9186), the upper pad's poly leaving west along y 8693-8710 (in `urch`'s channel, whose region overlaps this one: `urch`'s `sl4` pad (4420,8590) is just north of it); what the other outputs of the two stages reach, if anything.
- **The diffusion under tracks A, B, C** (Ambiguity 13): pale tan under the three tracks from y 8340, to y 8430 (C), 8540 (B) and on south (A); what it joins and whether any poly crosses it is not read.
- (Done, run 7: gate 9 of `lc1`'s column.) Its output's metal north of y 8067; rail 1 south of y 8160 and rail 2 south of y 8067.
- Geometry from round 7, not changed: latch B's VSS box's diffusion runs on north of y 8062 (tan to y 8050 at x 5682); a green patch (5858-5872, 8228-8236) under the VCC rail between two VCC boxes, no ring.
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
3. The west gate cluster (x 4480-5330, y 8330-9240): the largest piece; not a known cell. Survey of run 7
   (`w1_a.png`, `w1_m.png` 1.15x; `x1_a.png`, `x1_m.png` 2.6x; `x2.png` 5.2x; `x3_c2.png`, the chip-2 stripped shot at 1.38x):
   two gate columns, roughly mirror images. Left: poly rows at x 4630-4750 and x 4800-4880 either side of a wide metal
   x 4752-4800 (contacts under it at about y 8355-8440, 8590, 8770, 8910, 9110, 9220). Middle: a column of contact boxes
   at x ~4935 (y 8440, 8565, 8700, 8840, 8985, 9110, 9225) under the wide metal x 4926-4978. Right: rows at x 5080-5230
   with contacts at about (5125,8440), (5140,8640), (5120,8770), (5115,8950), (5140,9110) under the wide metal x 5095-5148
   and pads at x 5245-5300. The left column's rows come from pads on the tracks A, B, C of the rows above the cluster
   (track C ends on a pad (4562,8513); track B has a pad at about (4517,8607)) and on thin metals x ~4605 and x ~4648.
   At the top of the left column a diffusion column x 4700-4747 is crossed by two rows in series (y 8462-8485 from the pad
   (4648,8475); y 8505-8525 from track C's pad), with a ringed box below (4702-4728, 8540-8575); a large open diffusion
   (4575-4728, 8350-8425) lies above them. Which wide metal is which supply is not settled (their feeds above y 8330
   are the jogs of the rails noted above).
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

Round 7 (full review of run 6's piece H and the first review on Fable 5.2 of latch B, re-read item R31; 2026-11-18 19:10 -0600,
a fresh agent on claude-fable-5-2, at commit 5d95658; images in `cache/scratch/lc2/review-7/`, 18 used). Told to
suspect every corner of the three staircase lines, the corner (5083,8128) and the pad beside it, the corner
(5037,8172) and the dim T1, the turn at the pad (5232,8214), contacts in mid-run; latch B's copies, rows, pads,
the end of the enable metal, the clear pad, the Nb stub. Found correct: every corner and step (no bridge, no
swap); the corner (5083,8128) an L (the bar y 8110-8118 is the top edge of the row beneath) with no metal from the
pad (5123,8080) to the horizontal; both metals arriving on the pad (5232,8214); row 4's metal apart from
`lc1_w7864`'s jog at the north edge; the long runs without pad or hole; latch B's two copies (clean shot 3.9x,
metal 2.75x) and its three equations; its five rows each to its own pad; no row from the Nb stub; the enable
metal ending on the lower pad (no metal y 8404-8436); the clear metal ending on its pad; the thin metals x 5801
and x 5624 (holes only at their pads). Findings, each checked by the tracer:
1. **An undrawn poly row y 8898-8915** from drain A's contact box west to x 5377, south under the metal x 5378-5394
   (changes a connection if its join is one: `lc2_w8450` gets a branch). Confirmed, and followed: it ends on a
   pad with a contact (5386,8951) in the run of the staircase's fourth line (`textmap.py 5362 8888 5416 8976
   --acid`), which was read leg by leg from its west pad (5190,8258) to the strip's edge. Fixed: the row, the pad,
   the contact and the fourth line drawn; the row's end on the box drawn uncertain (Ambiguity 11).
2. **T1 between y 8067 and y 8150 should be marked uncertain** (no netlist change): it is bright only at x 5032-5037
   and dark for 19 px at y 8130-8148 over an undrawn diffusion box, with green under it in the clean shot; the
   reviewer reads one metal with no contact (same width and brightness either side, unbroken east edge line, no
   bright centre, no hole, the same signature over `lc1`'s gate 8 box). Fixed: that stretch is `?M`.
3. Omissions near piece H, no connection of the three lines changed: gate 9 of `lc1`'s column and its output row
   under `lc1_w7468`'s horizontal to the pad (5123,8080). Listed in Not done as the next piece.
4. Geometry only, not changed: latch B's VSS box's diffusion runs on north of y 8062; a green patch
   (5858-5872, 8228-8236) under the VCC rail.
Not checked by the reviewer: gate widths inside the cells; poly under the rails in the chip-2 stripped shot; where
the row of finding 1 goes south (followed by the tracer, above); the thin metal x 5749-5763.

Round 7: one finding that changes a connection, fixed (a fix check follows).

Round 8 (fix check of round 7's fixes, 2026-11-18 19:21 -0600, a fresh agent on claude-fable-5-2, against commit 5d95658, at commit
98f72a2; images in `cache/scratch/lc2/review-8/`). Confirmed: the fourth line one metal with every corner intact and
open ground to each neighbour; its west pad (5190,8258) a contact where the metal ends; (5386,8951) its only contact
from y 8520 to y 9233, and the metal running on south; the row y 8898-8915 one poly from x 5377 to x 5600 with field
on both sides and no pad or hole under the three metals; its east end abutting the box behind one 8 px edge line,
with no field or green rim, not passing on ("buried contact is likely; uncertain is fair"); T1's `?M`; both
`sameconn.py` runs (only the name `lc2_w8907` added). Findings, each checked by the tracer:
1. **The pad (5386,8951) has a second poly, west** (changes a connection: another branch of the net leaves): a row
   y 8943-8958 joins the pad with no outline at x 5372 and runs under the metals x 5342, 5300 and 5258 and on as
   open poly to at least x 5152, into the undrawn gate cluster. Confirmed (`q1.png`, 3.9x; `px.py col 5280` and
   `col 5240`: dark red-brown at y 8943-8955; `tl5_tracks.py rows row 5040 5380 4 8950`). Fixed: drawn from the pad to
   x 5240, a drawn end.
2. Geometry only: the fourth line's step drawn along y 8439 lies at y 8425-8441 (the 12 px dark stretch was its
   south edge). Confirmed (`tl5_tracks.py h 8432 5290 5352`: no gap). Fixed: redrawn at y 8432.

Round 8: one finding that changes a connection, fixed (a fix check follows).

Round 9 (fix check of round 8's fixes, 2026-11-18 19:26 -0600, a fresh agent on claude-fable-5-2, against commit 98f72a2, at commit
499c804; images in `cache/scratch/lc2/review-9/`). Checked: the row y 8941-8958 (one poly, joined to the pad's contact
hole with no line between; salmon under the three metals and orange between two edges in the three gaps; no tap
where the metals x 5258, 5300, 5342 cross it; green field at x 5406-5416 between the pad and `lc1_w7170`'s row; no
other poly from the pad: pink field south of it; open poly on west of x 5240, as declared); the step at y 8432 (metal
bright y 8426-8438, clear of the line above and the pad ring below); both `sameconn.py` runs (connections identical).

Round 9: no findings.

Round 10 (full review of run 7's pieces I and J, 2026-11-18 19:50 -0600, a fresh agent on claude-fable-5-2, at commit d00fad9; images
in `cache/scratch/lc2/review-10/`, 22 used). Told to suspect swaps, taps and pads in mid-run on the three rows, the
metal along row B, every end pad all round, the three west tracks' corners and `urch`'s `sl4` beside them; gate 9's
tie box, the gate row's join and its clearance from the output's pad, the output box, the pad (5127,8080), the VSS
contact, contacts from T1 or the horizontal metal. Found correct: rows A, B, C straight and continuous with no
swap, tap, pad or branch, and no hole or ring under either rail (a blotch on row C at (4820,8296) is residue in
chip 1 only); the six end pads, one poly and one metal each; the west tracks (each corner one metal, about 30 px of
ground between neighbours, each ending at its pad; track A clear of `sl4`); gate 9's tie box a ringed buried
contact in both chips, the gate row joined to `lc1_w7990`'s poly and clear of the pad (green ground at
x 5094-5104), the neck and pad carrying only the metal north, the VSS contact, no contact from T1 or from the metal
y 8120-8136. Findings, all geometry or comment, each checked by the tracer:
1. Gate 9's pull-down is about three times wider than drawn: the diffusion spans x 4910-5041 on both sides of the
   gate row (drawn x 4942-4985). Confirmed (`px.py row 8098`: tan from x 4920 under the rail, and tan again under T1
   at x 5022-5034; `lc1`'s gates 7 and 8 have the same east part). Fixed: 131/21.
2. Gate 9's load channel is 66 wide, not 42 (edges at y 8060-8064 and y 8128-8132, none at y 8102). Confirmed
   (`px.py col 4840`). Fixed: 68/40.
3. The output box was drawn about 15 px too far west: it is x 5012-5043, y 8108-8138, reaching under T1 (the
   "undrawn box" of round 7). Fixed.
4. The "metal along row B" is two metals, the rails jogging east: rail 1 (VCC) x 4757-4888 at y 8208-8265 and on
   south at x 4840-4888; rail 2 (VSS) x 4929-5147 at y 8228-8290 and on south at x 5105-5147 across row C; no metal at
   x 4888-4929. Comment and notes corrected; rail 2's metal at y 8067-8160 added (it was missing). The jogs
   themselves are not drawn (Not done).
Also from the reviewer: `urch` draws `sl4` 10 px south of the metal (photo y 8164-8180): for the handoff.
Not checked: whether the drain has a field notch at x 4992-5015, y 8102-8112 (W only); `lc1` draws nothing to
receive `lc2_w8127` north of y 8067.

After the fixes: `tools/t.sh lc2 sameconn.py d00fad9`: `connections identical`;
`.venv/bin/python tools/sameconn.py d00fad9`: `connections identical`.

Round 10: no findings that change a connection.

Round 11 (full review of run 8's piece K: the west cluster's supplies and latch K, 2026-11-18 21:15 -0600, a fresh agent
on claude-fable-5-2, at commit 5145fc0; images `cache/scratch/lc2/review-11/`, 19 of them). Told to suspect: the VSS
fingers east of the rail and whether the polys across the tongues are gates; whether rows 1, 2, a, b end at the rail's
edge; the thin metal x 4882-4899 between its two pads; the pad (4892,8694)'s poly and K2's load; the row from track B
and the column west of the rail; the two outlined shapes taken as field; the large open diffusion; whether the west
rail is VSS; anything left out.

Checked and found correct (4-6.5x in two or more shots, with `px.py`, `textmap.py`, `follow.py`): both equations, all
nine transistors, the three rail feeds. Rows 1, 2, a, b end at the rail's east edge (row 1: a field stripe x 4814-4822
in both chip-2 shots and chip-1 metal, on four rows, `j1_k1east.png`; row a: pink field x 4802-4816). The fingers: tan
unbroken past the rail's edge at y 8452 and 8617, stopping 5 px short at y 8415 where field lies outside; chip-2
stripped red minus green 13-20 on the fingers, 0-2 on field; neither reaches the middle rail. Both tongue gates are
orange like the row gates, not olive like the tie boxes. The gate to the pad (4892,8481): one piece. The arm to the
tail: one piece (`j3_k2east.png`). The thin metal x 4882-4899 ends on both pads, no ring or hole between, bare ground
north of 8461 and south of 8704 (`j2_thin.png`). The pad (4892,8694): one line to the load poly below and one to the
tie box (`j5_k2load.png`); K1's tie and foot likewise (`j9_k1tie.png`). The track-B row: the column's edge lines at
x 4700 and 4736-4740 run through every gap; its east end overhangs a field pocket and stops short of K2's VSS box
(`j6_clear.png`). Both outlined shapes are field. The large open diffusion: only the rail's margin line between it and
the contact column. Pads on tracks B, C and both thin metals real; no contact at any crossing, none on tracks A-C over
the pale diffusion (`w1_tracks.png`, `w2_tracktop.png`). Nothing left out beyond the Not done list.

Findings, all geometry only, all confirmed by my own measurements and fixed:

1. K2's third pull-down gate: the poly's west end is at x ~4817 (drawn 4832), the tongue's west edge ~4830 (drawn 4836)
   (`px.py row 8646 4808 4842`: poly stripe x 4817-4826 in the clean shot and chip-2 metal, edge line 4829-4832).
2. The VCC block `M 4840,8324:4980,8400`: west of x 4924 the metal ends at y ~8368 (`tl5_tracks.py v 4880 8320 8420
   --half 4`: no metal 8368-8419). Now to y 8370.
3. The east rail is wider from y 8368: x ~5084-5150 (`tl5_tracks.py h 8500 5060 5170`: metal from x 5084). Added.
4. K2's output node under the rail ends at y ~8740 (drawn 8747) (`px.py col 4770`: tan to y 8736, pink from 8748).

Could not check: the 12 px gap at y 8578-8590 between K1's output box and the track-B row reads field-like in colour
(fringe), so the clear transistor's north end rests on the column's edge lines alone: `?D` stays (Ambiguity 12). West
rail as VSS: its feed runs north to y ~5741 (`follow.py`), drawn by no package; nothing in view contradicts it. Track A
at y 8560-8696 seen only at 3x. The extent of the diffusion under tracks A-C, the east column and everything south of
y 8750 were not reviewed.

After the fixes: `tools/t.sh lc2 sameconn.py 5145fc0`: `connections identical`;
`.venv/bin/python tools/sameconn.py 5145fc0`: `connections identical`.

Round 11: no findings that change a connection.

Round 12 (full review of run 9's piece L: gate K3, 2026-11-18 22:00 -0600, a fresh agent on claude-fable-5-2, at commit
8c767ac; images `cache/scratch/lc2/review-12/`, 16 of them). Told to suspect: the strip x 4818-4838 as a gate and
whether X is diffusion; N one with E; box S's contact and the rail; row d's hook and row c's end; the load poly, its
ringed box and second strip; the output's thin metal; the column west of the rail; anything left out.

Checked and found correct: the equation and all five transistors. The strip is a gate (clean-shot means 247/176/122
beside E against 229/170/120 and 227/166/115 over field; row c reads 242/172/120 on its gate and 220/157/117 on its
end cap); lower X is diffusion (`b2.png`, `e1.png`). N is one with E (tan continuous at y 8838-8852, x 4735-4815, no
contact on either; `d1.png`). Row c ends at x 4797 (20 px of pink field before the strip's top; `k1.png`). Box S and
the VSS box contact the same rail (`h1.png`, `k1.png`). The contacts at (4646,8865) and (4881,8890) are real. The load
is one poly, the VCC contact real, no other contact on the thin metal to y 8975 (`g1.png`).

Findings, each confirmed by my own measurement and fixed:

1. **Where a wire goes on** (not the equation): `lc2_w8930` does not come from the south. The strip ends at y ~8943
   (`px.py col 4828 8920 8962`: clean peach to y 8941, pink from 8944; `z11.png` 9x) and leaves by an arm east at
   y 8925-8945, one poly with the strip in both chip-2 shots (reviewer: `px.py row 8935`, `i1.png`), under the output's
   thin metal without a contact. Drawn now, to x 4876; the port moved from (4818-4838, 8950) to (4876, 8925-8945).
   In the clean shot a ringed outline (4832-4850, 8920-8942) lies between strip and arm: taken with the reviewer as
   one poly.
2. Geometry: the stack's diffusion runs west to x ~4707 from y 8786 to 8895 (rows c and d about 72 wide). Added.
3. Geometry: K2's output poly south was drawn at x 4613-4631; it is x 4622-4640.
4. Geometry: the strip's channel and X reach y 8900, not 8880.
5. Geometry: the load poly's lower part (the pad box) reaches x 4925, not 4900.
6. Geometry: row d ends at x ~4789 in a plain end cap; no hook.
7. Geometry: the rail's corner (4741-4757, 8938-8960) is bare; the output metal leaves the pad's south-west corner.
8. The second load strip's evidence does not discriminate (poly over field at (4912, 8877-8901) is as red): stays `?D`.

Could not check: X's upper part (4846-4858, 8806-8838) reads like field in chip-1 metal and chip-2 stripped, though
closed by an edge at y 8801 with no edge against lower X: the ringed box rests on its outline. A long buried contact
under the strip cannot be excluded by colour alone (Ambiguity 15). Metal continuity over y 8971-8990, beyond the drawn
end. Undrawn and not followed (Not done): a poly row y 8898-8920 ending at x ~4705, a box (4698-4712, 8928-8948),
polys at (4880-4925, 8925-8960), a line at y 8954.

After the fixes: `tools/t.sh lc2 sameconn.py 8c767ac`: `connections identical`;
`.venv/bin/python tools/sameconn.py 8c767ac`: `connections identical`.

Round 12: one finding that changes where a wire leaves (the port of `lc2_w8930`), fixed; seven geometry-only, fixed.

Round 13 (fix check of round 12's fixes to gate K3, 2026-11-18 22:13 -0600, a fresh agent on claude-fable-5-2, changes
since 8c767ac; images `cache/scratch/lc2/review-13/`, 9 of them). All seven corrections hold in the photos and none
changes a connection. The arm is one poly with the strip: the clean shot's ring (4832-4850, 8920-8942) is absent from
both chip-2 shots and both metal shots (row 8934 continuous poly x 4830-4850), so it is not a buried contact; no
contact and no diffusion under the thin metal. The wider diffusion's edge is at x 4706-4708 in all four shots (top
y 8786, bottom ~8897; chip-2 stripped red minus green +11 to +13 inside, 0 to -9 outside) and stays clear of the row
y 8898-8920, the box (4698-4712, 8928-8948) and K2's box. The vertical poly's edges are x 4620 and 4639. One edge line
at y 8902-8905 from E to X. The pad box reaches x ~4922, crosses no diffusion, stays off the VCC box. Row d: a plain
end cap at x ~4790. The rail's corner and the thin metal's diagonal: right. Note: east of x 4876 the arm's band has
cross lines at x ~4880-4886 and 4902-4906 before the vertical poly x 4908-4922 (now drawn in piece M as the ringed
box at the head of K4's load: for piece M's review). `tools/t.sh lc2 sameconn.py 8c767ac` and
`.venv/bin/python tools/sameconn.py 8c767ac`: both `connections identical`.

Round 13: no findings.

Round 14 (full review of run 9's piece M: gate K4, 2026-11-18 22:45 -0600, a fresh agent on claude-fable-5-2, at commit
514d86b; images `cache/scratch/lc2/review-14/`, 14 used). Told to suspect: Z as one node; T's band east; the ringed
box, the head diffusion and the long strip as a load; the west box and the row from the vertical poly; the second
load; the pads and the tracks' ends; row 1's length; anything left out.

Checked and found correct: the equation and both merges of names. Z is one node (closed outline, tan strip
x 4838-4852, `z_strip.png`; the VSS node ends at x ~4806 with pink beyond; rows 3 and 4 end at x 4820-4824, row 2 at
~4828; green field between the strip and the plate). T's band is continuous east, diffusion-tan under the thin metal,
clear of the arm and of row 1 (`tband.png`, `head.png`). The long poly does not touch K3's pad box. The west box, the
row and the vertical poly x 4578-4596 are one poly with no contacts (`westbox.png`, `west_m.png`). All five pads, both
contacts, the end of track C and the L-shaped metal are as drawn; no other contact on tracks A, B, C or the thin
metals.

Findings:

1. **Changes a transistor's nets** (not the equation): the plate (4864-4902, 9040-9098) is T's load, not a second load
   on `lc2_w8298`, and the 14/175 load does not exist. No neck or buried contact at (4868-4890, 9012-9044): the clean
   shot has field directly south of the pad box's poly, which ends at y ~9010 (`px.py row 9014`: pink
   186-201/103-125/98-122 at x 4850-4878; mine agrees). The diffusion under the plate runs north as a strip
   x 4886-4900 into T's band (`px.py col 4894`: uniform y 8962-9031). Plate and long poly are one poly (the green rim
   at x 4903 stops at y 9036; one bottom outline). The long poly lies over field (`px.py col 4914`: 71-140/38-91; my
   plate channel reads 157-197/81-134). The head "open diffusion" (4880-4925, 8905-8922) is a poly-to-poly field gap
   (`opendiff.py` does not list it). Confirmed and fixed: neck, second load, long strip and head diffusion removed;
   the strip from T's band to the plate drawn (`?D` beside the pad box, Ambiguity 16); the plate joined to the long
   poly. Load of `lc2_w8692` now 22/58.
2. Geometry: the west rail reaches x ~4820 at y 8960-8966. Added.
3. Geometry: the pad box's poly ends at about x 4880, y 9012. Fixed.
4. Geometry: the north-east corner of the row y 8897-8916 is chamfered (not drawn).

Left out, no connection found inside the piece (Not done): a VCC box (4932-4985, 8958-9018) with a contact
(4950,8990), probably the east column's; a diffusion under track A from y 9083 south with no contact to the track.
Could not check: poly continuity across the two ringed boxes' outlines; overlaps under 4 px; chip-2 colours do not
separate narrow diffusion from field (finding 1 rests on the clean shot and on edges).

After the fixes: `tools/t.sh lc2 sameconn.py 514d86b` and `.venv/bin/python tools/sameconn.py 514d86b`: both
`connections identical` (4263 transistors became 4262; each one added or removed lies in parallel with one on the
same three nets). The tool calls it the same, because both outputs keep a load; the plate's gate and source did move
from `lc2_w8298` to `lc2_w8692`, so it is counted as a change.

Round 14: one finding that changes a transistor's nets, fixed; three geometry-only.

Round 15 (fix check of round 14's fixes to gate K4, 2026-11-18 23:05 -0600, a fresh agent on claude-fable-5-2, changes
since 514d86b; images `cache/scratch/lc2/review-15/`, 8 of them; 5-6x in three or four shots with `px.py` and
`textmap.py`). Finding 1 of round 14 is right: no neck (the pad box's bottom edge line is unbroken from x 4848 to 4886
at y 9016 in both chips, field below it); the strip runs from T's band (y 8962) to the plate's top edge (y 9036) with
no line across it at x 4893; below the pad box it has its own west edge at x 4873, the line that continues under the
plate and down the open diffusion; plate and long poly are one poly (a single 8 px line at x 4901-4905 between them);
the plate's channel lies only between the strip and the open diffusion, which is continuous south of the poly's foot
to the VCC box; the long poly is over field from y 8958 to 9040; the undrawn VCC box (4932-4985, 8958-9018) has its
own west outline and does not reach under the long poly; the former head diffusion is a field gap; T's band still
joins the ringed box, which is still under the poly; the strip abuts the pad box's poly and the long poly without
crossing either and is 26 px clear of the node-Z strip. Findings 2 and 3 right. `lc2_w8692` has one load (22/58 at
(4889,9069)), `lc2_w8298` two.

Geometry or notes only: (1) keep the `?` on the narrow strip: peak red minus green reads as diffusion in chip 1 (+33
metal, +27 clean) but as field in chip 2 (+19 metal, -7 stripped; the node-Z strip reads +33, +14): kept (Ambiguity
16). (2) The plate's west edge is at about x 4857 (drawn 4864), beside the node-Z strip, not across it: fixed.

After the fix: `tools/t.sh lc2 sameconn.py 8159796`: `connections identical`;
`.venv/bin/python tools/sameconn.py 8159796`: `connections identical`.

Round 15: no findings that change a connection.

Round 16 (full review of run 10's piece N: the east column, 2026-11-18 23:38 -0600, a fresh agent on claude-fable-5-2,
at commit d197845; images `cache/scratch/lc2/review-16/`, 25 used). Told to suspect: where the copy does not fit;
things the east column has that the master lacks, or the reverse; collisions with earlier geometry and with the
master under the shared VCC rail; the clock; the clears; the output's way out; the copied uncertain items.

Checked and found correct: `sameconn.py 87cff0c`, both forms: additions only, 19 transistors, the four equations. The
stack order under the east rail is the master's reversed (`railprof.py`); T and box S are separate. Overlay at 4-5x,
metal and clean shots: all 21 contacts on rings or holes, all seven buried-contact boxes, every row on its pad; the
shared VCC boxes are one box with one long contact each; the copy's long poly clears the master's K1 box. The clock:
one metal from the pad (5234,8300) to the pad (5255,8431) (8x, `follow.py`); the thin metals and track C' continuous
through their pads. The fourth staircase line is separate from the pads (5258,8427), (5302,8473), (5341,8560). The
`lc1_w7170` row reaches the pad (5428,8516) under the staircase metal with no contact; the clear row is one with the
pad (5386,8951)'s row. The output's L-shaped metal is one piece; the pad (5340,9208) is separate from it. No copy of
the master's large open diffusion or L-shaped metal. The copied uncertain items measure the same as in the master.

Findings:

1. **Changes a connection**: the pad (5349,9038) on track C' has a poly leaving east as well: the row y ~9025-9046 to
   x 5545, where it meets the drawn end of gate row 2 (`lc2_w9034`); under the metals x 5386, 5429, 5473 with no pad
   or ring (`row9038.png` 5.4x in three shots; `px.py row 9036`, `col 5368`). So the second stage's slave output is
   an input of `lc2_w9125`. Confirmed (I had the same row in a scratch draft, read independently while the review
   ran: `r3_m.png`, `r3_a.png`); drawn in piece P; the label `lc2_w9038` (never on main) is replaced by `lc2_w9034`.
2. **A transistor the trace lacked**: the east rail does not end at y 9160; under it south of the column,
   `railprof.py`: diffusion 9167-9181, gate 9182-9195, diffusion 9205-9239 with a contact ring (5127,9225); the gate
   is the poly from the pad (5254,9208), `lc2_w9034` (`south.png`). Confirmed (`railprof.py 5114 5148 9080 9300`;
   `s1.png`, `s2_a.png`, `s2_c.png`) and drawn: rail, column, contact, gate, the node `lc2_w9171` and its uncertain
   strip (section above). Also undrawn, `lc3`'s: a VCC box (4950,9225), a ringed box near (5020,9203).
3. Geometry: the east rail at y 8640-8750 reaches x ~5160 (added); the bottom VSS box runs to y ~9135 (fixed); the
   copy's rows for `lc1_w7170` and `lc2_w9034` east of the rail lie ~8 px north of where the copy puts them (photo
   y 8507-8528 and 8550-8571): both still meet their pads; left as the cell has them (Ambiguity 17).

Not checked: whether the two copied uncertain items are diffusion at all; the pad (5428,8516) is dark in the chip-2
metal shot (accepted from chip 1 and both stripped shots); load-tie junctions seen only at 4-6x; whether the pad
(5340,9208)'s poly reaches row 5 (it does: piece P).

Round 16: two findings that change connections (a row, a transistor), fixed; geometry fixed.

Round 17 (2026-11-18 23:56 -0600, a fresh agent on claude-fable-5-2, changes since d197845; images
`cache/scratch/lc2/review-17/`, 16 of them): a fix check of round 16's fixes to piece N, and the first review of
piece P (the four through lines, the west ends of rows 2, 3, 5).

Piece N's fixes, confirmed: the gate y 9182-9198 is one poly from the pad (5254,9208) by the diagonal, crosses the
column (edge line at x 5104 under it) and ends at x 5086, short of the strip; the contact (5124,9224) is rail to the
VSS node (ring in both metal shots, pits); the rail is continuous (its dark bars are 7-9 px in both chips); the node
is separate from the box above (two edge lines, field y 9143-9158); the strip x 5062-5078 is diffusion (chip-2
stripped +12 to +18 along y 9166-9286, no poly), joins the node at its top and ends about y 9290 in `lc3`; the rail
reaches x 5162 at y 8715; the box bottom is y 9136.

Piece P: no findings. B1: the four lines as drawn, separate, no pad, ring or hole (the dark patch at (6422,8653) is
in chip 2 only, the speck at (6432,8776) in the clean shot only); nothing else in the corner. B2: one poly from the
pad (5343,9038) to x 5545, no contact under the metals at x 5386, 5430, 5473; the box above is field. B3: pad and
contact (5520,9081) present, no metal north of it, no other contact to y 9233. B4: one poly, no contacts, pad and
contact (5341,9211) present; field at y 9183-9189 separates the pad from the L-shaped metal.
Both `sameconn.py d197845` runs showed only the intended differences.

Findings:

1. **Where a wire leaves, in the ports file only**: `ports.d/lc2.txt` had `lc2_w9171 D 5104-5158,9256`; the column at
   that edge is the VSS node, as the extraction has it; `lc2_w9171` leaves only by the strip. Fixed in the ports file
   and the Ports table (the port is `vss`). No geometry change.
2. Geometry: the node `lc2_w9171` also runs east of the rail to x ~5202 (chip-2 stripped row 9172, x 5162-5183: red
   minus green +20 to +26 against -5 on field; chip-2 metal 169/131/92, like known open diffusion), a dead-end tab
   above the diagonal poly. Added. The strip's `?` dropped on the reviewer's reading.

Not checked: the ringed box (5020,9203) and the VCC box (4950,9225) (Not done: with that stack's load).

Round 17: one finding on a port's name, fixed; one geometry-only.
