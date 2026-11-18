# lc2: left-centre random logic, middle strip (x 4400-6450, y 8067-9233)

## Status

2026-11-18 03:48 +0000. **Surveyed; nothing drawn.** There is no `trace/lc2.txt` yet. One session: the known
cells were tried (`findcell`), the region was surveyed at 0.62x and 1.25x, and one piece
(latch B) was laid over the photos as copies of `tl1`'s cells and fits; it was left out of
the trace because one of its ends (the poly on the box at (5615,8212)) could not be read, and
its inputs are not followed. The draft is below, ready to resume.

Before this package only `urch` had geometry in the region: the tracks of `sl0`..`sl4` at
x 4258-4640, y 8067-8200 (north-west corner) and the pads (4420,8590), (4380,9066) at the west
edge. Everything else in the region is undrawn.

## Inventory (from `cache/scratch/lc2/survey.png` 0.62x, `sv_[abcd]_[am].png` 1.25x; coordinates +-20)

| Where | What | State |
|---|---|---|
| x 4400-4640, y 8067-8200 | `urch`'s five tracks (nested corners) | drawn by `urch` |
| x 4480-5330, y 8380-9160 | west gate cluster: rails at x ~4760, ~4930, ~5110 (which supply: not read), many horizontal poly rows with pads at x 4480-4560 and x 5230-5330, loads at x 4850-4900 and 5010-5060 | not traced, not tried at more than 0.62x |
| x 4450-5350, y 8180-8330 | horizontal poly rows / metals above that cluster with pads at x 4500-4530 and 5130-5220 | not traced |
| x 5200-5600, y 8067-9233 | vertical bus (metals and polys), staircases at y 8380-8480 and y 8700-8780 | not traced |
| x 5590-5895, y 8055-8560 | **latch B**: `tl1_ub` + `tl1_ua` upside down (below) | fits on overlay; NOT in the trace |
| x 5887-6142, y 8589-9029 | **latch C** (believed): `findcell` `tl1_ub` at 3352,3999 rot=180 (0.76, centre 6014,8684) and `tl1_ua` at 3351,4439 rot=180 (0.68, centre 6014,8904) | not overlaid, not checked |
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

## Latch B: what was seen (believed, NOT extracted)

The copy maps master (x, y) to (x + 3059, 12893 - y). Overlays at 2.6x (`b_ov_a.png`,
`b_ov_m.png`) and 4x on the clean shot (`b4_1a.png`, `b4_2a.png`, `b4_3a.png`): every outline
of both cells lies on a feature within about 5 px. If it is the copy it looks like:
Na = NOT(data AND en OR Nb), Nb = NOT(clr OR en AND NOT data OR Na): open while en is high.

| Item | Seen | How |
|---|---|---|
| VSS rail x 5660-5705, VCC rail x 5840-5890 | metals in the metal shot; which supply is **by structure only** (loads on the east rail) | 2.6x |
| stack's own VSS box, contact (5680,8088) | ring in the rail, speck in the clean shot; reaches y ~8055, north of the region's edge | 4x `b4_1a.png`, `b4_1m.png` |
| VCC contacts: long ring (5857, 8255-8350); (5862,8446) | rings in the metal shot, specks in the clean shot | 2.6x / 4x |
| thin metal x 5615, pads (5615,8120) and (5621,8532) | the inverter's output to the stack's top gate, as in the master | 2.3x `b_west.png` |
| thin metal x 5801, rings (5800,8190), (5800,8397) | as the master's x 2742; drawn in the draft from the master's numbers | 2.6x only |
| en: rows y 8168 and y 8390, pads with contacts (5555,8168), (5555,8387) on one metal x 5555 | `follow.py 5555 8300`: south end 8390, north to (5558,7646) in `lc1` (candidate contact (5560,8153)) | `j_data_m.png` 5x two metal shots: the metal ends on the pad (5555,8387); no metal y 8405-8440 |
| data: row y 8423-8441, L-shaped pad, contact (5557,8452); a second metal goes south from it (x 5555 to y ~8612, east to x ~5626, south) | `j_data_m.png`, `j_data_a.png` 5x four shots; the route beyond is the follower's, not looked at | |
| clr: row y 8250-8268 west to a pad with a contact about (5470,8255) | 2.3x only; its metal not followed | |
| Na out: row y 8336-8356 from the box (5603-5627, 8330-8358) west to a pad with a contact about (5515,8340) on a vertical metal x ~5515 | 2.3x only | |
| **the box (5603-5628, 8198-8228) on Nb** | **not resolved** (`j_qbox.png`, 5x clean and chip-2 stripped): no row goes west from it as in the master; a rounded outline at x 5585-5600, y 8195-8235 west of it. Whether the poly ends there or turns is not read | open |
| a dark vertical feature x 5722-5740, y 8040-8120 in the gap between the rail and thin W, across the strip y 8097-8111 that takes the third pull-down's source to the VSS box | taken as the etch lines beside the metals (greenish between the lines at y 8070-8090 in the chip-2 stripped shot, `px.py col 5730 8050 8130 4`), not a poly; `b6_top_a.png` | weak: re-read |
| a poly L at x 5850-5900, y 8510-8560 south-east of the cell | not the latch's; not followed | |

Draft that was overlaid (not committed as a trace file; put it in `trace/lc2.txt` to resume):

```
@block lc2
@requires tl1
@w M=20 P=18
@s 28x28
@inst tl1_ub 3059,3523 mx=2662.5 rot=180 o=2662.5,4685
@inst tl1_ua 3059,3963 mx=2662.5 rot=180 o=2662.5,4465
D 5659,8062:5714,8115
C 5680,8088
M 5801,8179 y8409 w=12
P 5784,8381:5821,8411
C 5801,8397
P 5784,8167:5821,8205
C 5801,8190
```

## Ports

None: no wire is drawn. (`ports.d/lc2.txt` is not written yet.)

## Ambiguities

1. The box (5615,8212), above. Settle with a per-copy comparison against `tl1`'s two copies
   and `tl5`'s (`cellcheck.py`), and the chip-2 stripped shot at 4x over x 5570-5640, y 8185-8300.

## Not done

Everything. In order:

1. Latch B: resolve Ambiguity 1; add the rails, the VCC contact (5857,8300), the six rows to
   their pads; profile every gate past both channel ends (`px.py`); view every pad and 50 px
   beyond at 4x in two shots (only the en and data pads were); extract.
2. Latch B's tracks: en north along x 5555 into `lc1`; data south from (5557,8452); clr from
   (5470,8255); Na from (5515,8340).
3. Latch C and the inverter below it (overlay the `findcell` hits first).
4. The west gate cluster (x 4480-5330, y 8380-9160): the largest piece; not a known cell.
5. The bus fields and the unit halves on the north and south edges (with `lc1` / `lc3`).

Tool note: `view.py` has no `--notrace`; images wider than about 1300 px (6x of 130 px in two
panels) are downscaled and wasted.

## Review
