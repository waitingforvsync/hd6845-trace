# lc2: left-centre random logic, middle strip (x 4400-6450, y 8067-9233)

## Status

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
| x 5840-6140, y 9025-9155 | inverter (believed): `tl1`'s inverter (2535 4215 2835 4345) at 3306,4809 rot=180 (0.73, centre 5991,9089); `tla`'s in1 unit (3820 4040 4120 4150) also hits there (0.79) | not checked |
| x 5887-6142, y 8067-8290 | **latch D's lower unit**: `tl1_ua` at 3351,3703 rot=180 (the upper unit is `lc1`'s copy of `tl1_ub`); VSS rail x 6015-6063 | **traced** (run 3) |
| x 5600-5900, y 8880-9233 | gate cluster that runs on south into `lc3` (weak hits: `tl1` inverter 3059,4663 unturned 0.59; `tla` in1 0.53) | not traced |
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

## Ports

`ports.d/lc2.txt` (kept in step with this). Latch B: enable `lc2_w8169` north on metal x 5560 at y 8067 (into
`lc1`; believed to run to (5558,7646)); clear `lc2_w8254`, output `lc2_w8341` and data `lc2_w8450` end on stubs
of their metals (pads (5472,8254), (5514,8341), (5558,8450): the metals run on, not followed); the rails vss
and vcc at y 8060/8067 and y 8560. Latch C: output Na `lc2_w8822` on a stub over its pad (6257,8822); its vss
rail (x 6019-6061) at y 9030, and vcc (x 5840-5890) at y 9030.

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
| `lc2_w8474` | P | 5835, 8634-8652 | ? | drawn end: the poly runs on west |
| `lc2_w8172` | M | 6422-6440, 8067 | ? | from the north |
| `lc2_w8172` | M | 6450, 8163-8181 | ? | on east |
| `lc2_w8906` | M | 6462-6480, 8067 | in | latch C's data, north (20 px east of the strip) |

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

## Not done

Run 3 (2026-11-18 16:28 -0600):

- **`lc2_w8474`'s poly west of (5835,8643)**: it runs on west along y 8634-8652 past x 5560 (not followed), and its
  metal x 6332-6350 north of y 8067 (`lc1` has no port there).
- North of y 8067 (in `lc1`'s strip, not drawn by it): latch C's enable metal x 6159-6177, the node's row
  x 6401-6415 (`lc2_w8083`), the metal x 6422-6440 (`lc2_w8172`), latch C's data metal x 6462-6480.
- East of x 6450: metals A (`lc1_w7908`), B (`lc2_w8646`) and the turn of `lc2_w8172` (y 8163-8181).
- The thin metal x 5962-5982 through latch D's lower unit (the counterpart of `tl1`'s thin metal W, as x 5748-5764
  through latch B and x ~5971 through latch C): bright from y 8040 to y 8600 in `d1_m.png`; not drawn, its
  contacts not looked for.
- Latch C's clear, enable and data are followed (above); its Na metal south of the pad (6257,8822) is not.
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
