# lc1: left-centre random logic, the top strip (x 4400-6450, y 6900-8067)

Package `lc1` (part 1 of 3 of the left-centre logic; `lc2`, `lc3` are the strips south of
y 8067 and y 9233). Trace: `trace/lc1.txt`. Views and the survey: `cache/scratch/lc1/`
(`survey.md` lists every measurement with the command that gave it). Traced by Chris Evans'
session (the claim is held for it by mattgodbolt; no write access yet, so the branch goes in
as a pull request).

## Status

2026-11-17 21:55 -0800. **Partial.** Traced: gate column W (x 4750-5100, y 6940-8067: eight gates, 17 transistors),
where each of its wires goes (wiring), the first gate of cluster E (2 transistors), and **the gate that drives
`lc1_w7040`: the upper unit of a latch** (5 transistors, a copy of `tl1`'s cell `tl1_ub`; its lower unit lies south
of y 8067, in `lc2`). 24 transistors in all; full extraction with every trace file: 0 errors, 0 warnings. Not
traced: the west half of cluster E, the other lines of the diagonal bundle and the crossing field, the metal bus
west of x 4750.

```
lc_step   = NOT lc1_w7040                      firm (and the join to ur's lc_step poly is drawn)
rcs_x1 = NOT lc1_w7170                      firm
rst = NOR(lpstb_b, res_b)          firm
rst_n = NOT rst                      firm
rst_a = NOT rst_n                      firm
rst_b = NOT rst_n                      firm
rst_c = NOT rst_n                      firm
lc1_w7990 = NOT rst_c                      firm
lc1_w7780 = NOT lc1_w7733                      firm (cluster E, gate E1)
lc1_w7040 = NOT( rst_c  OR  ck_out AND lc1_w7862  OR  lc1_w7928 )
                                               marked: depends on the cell's ? load tie, as every copy of tl1_ub
```

("firm" as `tools/unsure.py --equations` uses it: no `?` item in the trace is involved.)

**The scan line counter's step pulse is made here**: `lc_step` (which clocks the scan line
counter and the 4-bit counter `c4l`, `notes/blocks/ur.md`) is the output of gate 1, an
inverter of the poly row `lc1_w7040`, which arrives from the east along y 7030-7050. That row is
followed back (below) to the gate cluster E in the south-east of this strip, where it ends on the output box of
**the upper unit of a latch** (Logic, "Latch D"): `lc1_w7040` = NOT(`rst_c` OR `ck_out` AND `lc1_w7862` OR
`lc1_w7928`). `rst_c` is the buffered NOR of this strip's gate column, here the latch's clear;
`ck_out` is its enable, on a metal from far north of the strip; `lc1_w7862` and `lc1_w7928` come up from the
latch's lower unit in `lc2` (by `lc2`'s latch B, a copy of the same pair: the inverse of the data and the
other half's output). Believed, not traced (the lower unit is not drawn): `lc_step` is the inverse of what the
latch holds, and is forced high while `rst_c` is high. Believed, from the user (2026-11-17), not followed to
a pin: latch D's enable is a chip-wide inverted clock (traced since, 2026-11-20: it is `ck_out`, the clock buffer's output, not inverted) and `rst_c` a chip-wide reset of some kind.

The rest of the column is a small tree: a two-input NOR (`rst`, inputs two poly rows
from the east), its inverse `rst_n`, and three inverters of that (`rst_a`,
`rst_b`, `rst_c`: three copies of NOR's output, each leaving east on its own row),
then `lc1_w7990` = NOT `rst_c`, which leaves south. Gate 2 is a separate inverter whose
input arrives from the south on a thin metal and whose output leaves north on a metal.
Believed, not traced: three buffered copies of one signal is the pattern of `rst_ck`,
`rst_rc`, `rst_lat` (`notes/operation.md`).

## Inventory

Supply rails (metal, both run through the whole strip and on):

| Rail | x | What |
|---|---|---|
| rail 1 | 4755-4803 | VCC, by structure: every load's contact box lies under it. Not followed to a pad |
| rail 2 | 4928-4980 | VSS, by structure: every pull-down's source contact lies under it. Its top is at y 6948; from there an arm goes west (y 6975-7028) and north along x 4842-4893 out of the strip |

The column's build (calibrated on gate 2, in the open; `survey.md`, "Vocabulary here"):

- **Load**: a diffusion box under rail 1 with the VCC contact, a poly block just east of the
  rail in the open, the channel under it, and the output diffusion leaving east. The load's
  gate is tied to the output by a buried contact box on an extension of the poly block
  (top or bottom) over a stub of the output diffusion.
- **Pull-down**: the output diffusion runs east under rail 2; a poly row crosses it there and
  for 30-60 px beyond the rail's east edge (one wide device; in gates 1, 4, 5, 7 also 20-25 px
  west of the rail), with the VSS contact on the other side of the row, under the rail.
- **Output**: east of the rail the output diffusion ends under a poly box with a buried
  contact (nested outlines in every shot, x about 5010-5048); the poly leaves east or north.
- Colours here: under the rails field is pink, diffusion tan, a gate bright salmon; in the
  open field is olive, diffusion pinkish-tan between dark edges (green where it is wide),
  poly orange and textured. `tools/classmap.py --open` segments this area well.

| Gate | y | VCC contact | VSS contact | Gate row (poly) | Output |
|---|---|---|---|---|---|
| 1 | 6960-7100 | (4777,7025) | (4960,7075) | y 7030-7050, from x 4893 east past x 5140: `lc1_w7040` | box (5006-5053, 6985-7022), poly north beside it and north-west to (5021,6890): `lc_step` |
| 2 | 7107-7245 | (4777,7138) | (4960,7215) | y 7158-7182 to the pad (5082,7170); metal south and west to the thin metal T1 (x 5030-5046), which runs south out of the strip: `lc1_w7170` | box (5008-5048, 7116-7156), poly east to the pad (5082,7105), metal M_a (x 5070-5090) north out of the strip: `rcs_x1` |
| 3 | 7275-7375 | (4777,7315) | (4960,7215) and (4960,7388) | two rows from the east crossing a diffusion column under T1 (x 5022-5040): `lpstb_b` (y 7248-7267), `res_b` (y 7334-7352) | box (5010-5046, 7284-7320) on the column between the rows, poly east to the pad (5082,7302), strap M_c1 south to the pad (5082,7388): `rst` |
| 4 | 7402-7505 | (4777,7442) | (4960,7388) | y 7420-7447 from x 4892, east and up to the pad (5082,7388): `rst` | box (5024-5050, 7464-7490), poly east to the pad (5083,7474) on the metal M_c2 (x 5073-5093), which runs south out of the strip: `rst_n` |
| 5 | 7525-7632 | (4777,7572) | (4962,7525) | y 7552-7578 from x 4892 to the pad (5082,7563) on M_c2 | box (5024-5050, 7590-7620), poly row east along y 7597-7615: `rst_a` |
| 6 | 7668-7755 | (4777,7722) | (4960,7655) | y 7681-7701 to the pad (5082,7692) on M_c2 | box (5012-5048, 7713-7747), poly row east along y 7725-7743: `rst_b` |
| 7 | 7785-7897 | (4777,7830) | (4958,7790) | y 7809-7835 from x 4892 to the pad (5082,7822) on M_c2 | box (5012-5048, 7853-7882), poly row east along y 7855-7873 and a poly south under M_c2 (x 5072-5092) to gate 8's row: `rst_c` |
| 8 | 7923-8017 | (4777,7968) | (4955,7910) | y 7942-7962, east to the poly under M_c2 | box (5012-5048, 7983-8012), poly east and south under M_c2 out of the strip: `lc1_w7990` |

A ninth gate of the same build straddles the south boundary (VSS contact (4955,8045), gate
row y 8076-8099): `lc2`'s.

## Logic

Traced (the equations above are what `tools/netlist.py` recovers):

- Gates 1, 2, 4-8 are inverters; gate 3 is a NOR of two.
- Gate 3's two pull-downs (W about 38) lie east of rail 2, their east half **under the thin
  metal T1**: the output band passes under rail 2 without a device (pink field either side
  of the band there), joins a diffusion column x 5002-5040 (its west edge is the dark line at x 4999-5002 that
  crosses both rows in the metal shot; the rows' end caps are at x 4984), and the two rows cross that
  column above and below the output box. Evidence: `px.py col 5031` (tan diffusion at y
  7232-7244, 7274-7280, 7325-7328, 7361-7370; bright salmon gate at 7250-7262 and 7337-7349)
  against `px.py col 5046` (pink field above and below both rows). Above the upper row the
  column turns west (y 7228-7244) into gate 2's VSS box; below the lower row it turns west
  (y 7358-7374) into gate 4's VSS box.
- T1 is the metal on gate 2's row pad: from the pad (5082,7170) south to y 7226, west to
  x 5035, then south (centred x 5043 down to y 7380, x 5038 below). It is dim or dark in both metal shots over y 7240-7380 (it lies on the
  column and the boxes: traps 19, 22) but the clean shot is protected under it all the way,
  and it is bright again from y 7380 to the south boundary. No pad on it inside the strip.
- M_c2 carries `rst_n` from gate 4's output pad to the row pads of gates 5, 6, 7 and on
  south. Four poly rows pass under M_c1 / M_c2 without contact: `res_b` under M_c1,
  `rst_a` and `rst_b` under M_c2, and the two vertical polys of `rst_c` and
  `lc1_w7990` lie under M_c2 lengthwise (text maps against the known pad (5082,7563): bright
  metal, protected poly, no green hole; `survey.md`).
- Sizes (W/L from the extraction): loads 30/37 (gate 1), 37/44 (2), 25/60 (3), 66/38 (4),
  65/40 (5), 40/47 (6), 68/40 (7), 27/60 (8); pull-downs 138/20 (1), 67/24 (2), 38/19 and
  38/18 (3), 110/24 (4), 99/26 (5), 77/20 (6), 110/24 (7), 77/20 (8). Gates 4, 5, 7 are one
  cell (an L-shaped load poly with a foot, the channel the full height of the VCC box);
  gates 6 and 8 are alike but for the tie. Good to about 15 %: see Ambiguities 2, 3.

### Where the column's wires go (wiring, traced)

| Net | Route (all drawn) |
|---|---|
| `lc1_w7040` (gate 1's input, the inverse of `lc_step`) | row y 7030-7050 east to x 5150; south-east as the lowest line of the diagonal poly bundle (centre line x = y - 1890) to (5454,7344); east as a poly row y 7334-7354 across the crossing field (under a dozen vertical metals; two metals lie on it lengthwise without contact: x 5575-5678, which is `rst_c`'s own branch north, and x 6098-6307) to a pad with a contact (6341,7345); metal east along y 7337-7355 to x 6472 (22 px outside the strip), south along x 6463-6481 to a pad with a contact (6471,7930); poly west along y 7944-7962 to its end at x 6126, against a diffusion in gate cluster E (not drawn, not resolved) |
| `lpstb_b` (gate 3) | row east to a pad (5235,7258); metal V3 (x 5224-5246) north out of the strip |
| `res_b` (gate 3) | row east to a pad (5190,7345); metal V2 (x 5180-5200) north out of the strip |
| `rst` (gate 3's output) | besides gate 4: a poly row y 7379-7397 from the pad (5082,7388) east across the whole strip and out at x 6450 (seen to x 6710) |
| `rst_a` (gate 5's output) | row east to a pad (5124,7605); metal M_b (x 5115-5135) north out of the strip |
| `rst_b` (gate 6's output) | row east to a pad (5126,7735); metal east, north along x 5159-5181, east along y 7425-7447, north as V4 (x 5288-5310) out of the strip |
| `rst_c` (gate 7's output) | row east to a pad (5126,7866); metal east, north along x 5202-5222, east along y 7510-7530 to a pad (5299,7520); poly east under the metal V5 to a pad (5429,7520); from it metal east to a pad (5583,7519), from which a poly row goes on east along y 7509-7527 to a pad (6253,7517), where the metal x 6247-6263 takes it south to latch D's clear row (pad (6255,7996)) and out of the strip, and a metal goes north (x 5576-5592 to y 7346, east along y 7338-7354 to x 5668, lying on `lc1_w7040`'s row without contact, north along x 5660-5676 to y 6976, east to x 5713, north out of the strip); and from the pad (5429,7520) metal south along x 5419-5439, a jog east at y 8003, out of the strip at x 5466-5486 |

### Gate E1 (cluster E), traced

`lc1_w7780` = NOT `lc1_w7733`. An inverter of the column's build under the cluster's east VSS rail
(x 6015-6063): VCC box x 5843-5898 under the cluster's VCC rail (x 5840-5892, contact (5862,7768)), load poly
x 5900-5942 with the channel under its lower block (y 7750-7776), tie box (5959-5983, 7711-7745) under the thin
metal x 5965-5982, output band y 7748-7777 east under that metal and the rail, pull-down row y 7724-7744, VSS
contact (6043,7702), output box (6105-6134, 7760-7792). Input row east to a pad (6298,7713), metal north to the
pad (6297,7561) at the east end of the poly row y 7561 (drawn 50 px; its west end is the pad (5537,7561)).
Output row y 7772-7788 east through a pad (6296,7781) and out of the strip; metal south from that pad out of
the strip.

Believed: nothing beyond what is said under Status.

### Latch D, upper unit (cluster E, x 5887-6142, y 7833-8043), traced

`lc1_w7040` = NOT(`rst_c` OR `ck_out` AND `lc1_w7862` OR `lc1_w7928`): marked (the cell's `?` load tie).

The gate group that two passes could not read by itself is **`tl1`'s unit `tl1_ub` turned 180 degrees**:
`@inst tl1_ub 3352,3243 rot=180 o=2662.5,4695` (`findcell 2535 4590 2790 4800 --layer acid1b`: 0.75, centre
(6014,7938); `lc2`'s latch B as the master, mirrored: 0.78). The copy maps master (x, y) to (8677 - x, 12633 - y).
It was found when `lc2`'s notes (dp111, merged 2026-11-18) described latch B, 290 px to the south-west: the two
latches stand back to back on the VCC rail x 5840-5892. Overlays `eyes/latchD-ov-c.png` (4.6x clean),
`eyes/d-ov1.png`, `eyes/d-ov2.png` (3.2x clean and metal): every outline lies on a feature within about 5 px.
Side by side with latch B mirrored (`eyes/cmp-c.png`, `eyes/cmp-m.png`, 3.4x): the same structure line for line,
the rounded outline in the gap x 5978-6016 included; the one difference is at the output box, where here a poly
row leaves east (`lc1_w7040`) and latch B's box has a closed stub.

The unit is a four-input gate on the node of the box (6100-6126, 7940-7968), which the row of `lc1_w7040`
(y 7944-7962) joins: a load (channel at (5930,7998), VCC box under the rail, contact (5865,8027)) and three
paths to VSS:

| Path | Device(s) | Gate |
|---|---|---|
| clear | (6106,7999), 35/18, to the VSS box of the contact (6049,8023) by the arm y 8017-8035 | row y 7988-8006, east to the pad (6255,7996) on the metal x 6247-6263, which comes from the pad (6253,7517) at the east end of `rst_c`'s row and runs on south (followed to y 8218): **`rst_c`** |
| series pair | (6058,7918), 83/19, on the output side; (6058,7872), 81/21, on the VSS side (the copy's own VSS box y 7808-7858, contact (6047,7832)) | lower row y 7900-7918, east to the pad (6213,7908) on the metal x 6204-6221: **`ck_out`**, the enable. Upper row y 7859-7881, east end the pad (6117,7862) on the thin metal x 6096-6110 (the cell's), which runs south out of the strip: **`lc1_w7862`** |
| third | (5956,7878), 43/22, on the strip under the thin metal x 5965-5982 | the poly from the pad (5929,7929), which a thin metal x 5918-5932 joins to the south: **`lc1_w7928`** |

`ck_out`'s metal comes from the north: x 6007-6025 from beyond y 6900 (`follow.py 6012 7410 N`: straight to
y 6150), east along y 7421-7439, south along x 6204-6221 through the pad and on south, where `lc2`'s lower unit
has its enable row (`follow.py 6213 7950 S`: contact candidate (6212,8141)). No tap seen on it in the strip.

What the lower unit is (believed, from `lc2`'s latch B, the same pair of cells; nothing of it is drawn):
`tl1_ua` at `3351,3703 rot=180 o=2662.5,4465` (findcell 0.68, centre (6014,8168)), an inverter of the data and
the gate NOT(data AND enable OR `lc1_w7040`). Then `lc1_w7862` is the inverse of the data, `lc1_w7928` the
other half's output, and the pair is a latch that is open while `ck_out` is high and cleared by `rst_c`
(`lc1_w7040` low, so `lc_step` high). The latch's data arrives in `lc2`.

Colours that had misled the earlier passes, settled by the copy: the strip y 7837-7854 (x 5937-6075) is the
cell's diffusion joining the two VSS-side ends (its chip-2 colours read as poly here); the row of `rst_c`
along y 7517 is dark red-brown in the clean shot at x 5640-5750 and x 6065-6160, which is poly with no metal
near it (`notes/layers.md`), orange in both chip-2 shots (`eyes/d-r12.png`, 5x).

## Ports

Also in `ports.d/lc1.txt`. The strip's edges are y 6900 (north), y 8067 (south), x 4400,
x 6450. Wires that end inside the strip, undrawn beyond, are listed with where the drawing
stops.

| Name | Layer | Where | Direction | What |
|---|---|---|---|---|
| `vcc` | M | x 4755-4803 at y 6900 and at y 8067 | - | rail 1, runs on both ways |
| `vss` | M | x 4842-4893 at y 6900; x 4928-4980 at y 8067 | - | rail 2 and its arm north |
| `vcc` | M | x 5840-5892 at y 8067 | - | cluster E's VCC rail (its top is at y 7682), runs on south |
| `vss` | M | x 6015-6063 at y 8067 | - | cluster E's east VSS rail, runs on south (drawn north to y 7560, where it goes on) |
| `lc_step` | P | (5012-5030, 6890) | out | joins `ur`'s poly, which ends at (5012,6900) |
| `rcs_x1` | M | x 5070-5090 at y 6900 | out | M_a, north; still metal at y 6840 |
| `rst_a` | M | x 5117-5133 at y 6900 | out | M_b, north (followed to y 6800) |
| `res_b` | M | x 5180-5200 at y 6900 | in | V2, from the north (followed to y 6844) |
| `lpstb_b` | M | x 5224-5246 at y 6900 | in | V3, from the north (followed to y 6800) |
| `rst_b` | M | x 5288-5310 at y 6900 | out | V4, north (followed to y 6720, where it turns east) |
| `rst_c` | M | x 5705-5721 at y 6900 | out | the branch north from the pad (5583,7519) (followed to y 6365) |
| `lc1_w7170` | M | x 5030-5046 at y 8067 | in | T1, south (gate 2's input) |
| `rst_n` | M | x 5073-5093 at y 8067 | out | M_c2, south |
| `lc1_w7990` | P | x 5072-5092 at y 8067 | out | under M_c2, south |
| `rst_c` | M | x 5466-5486 at y 8067 | out | south (followed to y 8262) |
| `lc1_w7780` | M | x 6287-6307 at y 8067 | out | south from the pad (6296,7781) (followed to y 8175) |
| `rst` | P | (6450, 7379-7397) | out | the long row, on east (seen to x 6710) |
| `lc1_w7780` | P | (6450, 7772-7788) | out | gate E1's output row, on east (seen to x 6710) |
| `ck_out` | M | x 6007-6025 at y 6900; x 6204-6221 at y 8067 | in | latch D's enable: from the north (followed to y 6150), through the pad (6213,7908) and on south to the lower unit |
| `rst_c` | M | x 6247-6263 at y 8067 | out | the clear's metal, on south from the pad (6255,7996) (followed to y 8218) |
| `lc1_w7862` | M | x 6096-6110 at y 8067 | in | the cell's thin metal from the pad (6117,7862): from the lower unit in `lc2` (believed: the inverse of the latch's data) |
| `lc1_w7928` | M | x 5918-5932 at y 8067 | in | thin metal from the pad (5929,7929): from the lower unit in `lc2` (believed: its output plate, pad about (5934,8133)) |
| `lc1_w7733` | P | (6240, 7552-7570) | in | drawn end of the row y 7561 west of the pad (6297,7561); its west end is a pad (5537,7561) |

`lc1_w7040`'s metal leaves the strip at (6450, 7337-7355), turns south 22 px outside it and comes
back in as poly at (6450, 7944-7962): both crossings are drawn, with the 22 px outside.

## Ambiguities

1. **The join of gate 1's output box to the `lc_step` poly** (5046-5053, 6985-7010). The
   poly comes down x 5050-5068 beside the box and ends at y about 7008 (orange in both
   chip-2 shots at y 6965-7004, plain at y 7016: `px.py row`). Between it and the box's
   interior there is a dark line at x 5046-5050, read as the box's edge and the buried
   window's, not as a gap between two polys. Read at 6.4x in four shots (`j_lcstep.png`).
   The reviewer of round 1 compared the profile across it with gate 2's exit, where the join
   is not in doubt, and found them identical. Working assumption: joined.
2. **How far each pull-down's channel reaches** (sizes only). Drawn to x 5046 (gate 1),
   5040 (3, 4, 5, 7), 5022 (6, 8), 5012 (gate 2, to a dark line that crosses the row at x 5012).
   In the open the diffusion edges are judged from outlines in the metal shot and the class
   map; they are good to about 10 px. Gate 3's column was drawn 18 wide at first (the edge
   of T1's protected margin taken for the diffusion's edge) and is 38: round 1.
3. **The loads of gates 4, 5, 7**: the channel is drawn the full height of the VCC box
   (W 65), with a drain strip x 4850-4866 beside the poly, from a 5.3x view (`l4z.png`); the
   strip is narrow and its colour is not conclusive (`px.py row 7430`). If the diffusion
   crosses only at the bottom, W is about 25. The connection is the same.
4. **Rail names.** `vcc` and `vss` are from the orientation of the loads, for the column's two
   rails and for cluster E's two; none is followed to a pad or to a named supply.
5. **`rst`'s long row** (y 7379-7397, x 5096-6450) was followed at 3x in three views and
   at 1.2x over all of it; the 12 px between the pad (5082,7388) and the metal M_b is poly by
   its colour in the chip-2 shots (`survey.md`). No tap was seen on it; taps without a pad
   would not show (trap 15 says there are none).
6. **Latch D's upper unit is a cell copy.** Its geometry is `tl1_ub`'s, checked here by overlay and against
   `lc2`'s latch B, not re-read line by line; what `tl1` left uncertain in the cell (the load tie, `?`) is
   uncertain here too, so `lc1_w7040`'s equation is marked.
7. **The arm from the clear device to the VSS box** (x 6073-6085, y 8017-8035): the clean shot has a dark
   stretch there (`px.py row 8022`, `survey.md`), which the third look took for a break. The cell has the arm,
   and latch B shows the same picture at the same place (`eyes/cmp-c.png`). Working assumption: joined, as the
   cell.
8. **The thin metal x 5965-5982** crosses the unit (the strip under it carries the third pull-down). It is not
   drawn; no contact to the unit is known (`lc2`'s review found none on its continuation through latch B).
   `follow.py` lists contact candidates on it at (5971,7883) and (5973,7856): not looked at closely.

## Review

**Round 1: full review, 2026-11-17 17:41 -0800.** Piece: gate column W (x 4750-5140, y 6890-8067), `trace/lc1.txt`
at commit d0eb7d7. Reviewer: a fresh Claude Fable 5.2 agent, images in `cache/scratch/lc1/review-1/`
(27). Told to suspect: the join of gate 1's box to the `lc_step` poly and to `ur`'s; gate 3 (no
device under rail 2, both small devices under T1, both column ends on VSS); T1's continuity and
contacts; the six pads on the metal x 5073-5093 and hidden contacts under it; second pull-downs on
any row; the load ties; the rails' identity.

It checked (4x or more, profiles, text maps, the follower): suspicion 1 (the box-to-wire profile
equals gate 2's exit; the wire ends at y 7006; the poly is `ur`'s), suspicion 2 (no gate under
rail 2 on gate 3's band; both column ends reach the VSS boxes), suspicion 3 (T1 continuous to
y 8067, the dark stretches are pass-overs), suspicion 4 (all pads real, M_c2 one piece, the strap
separate, no contact at any crossing), suspicion 5 (one pull-down per gate but gate 3's two),
suspicion 6 for ties 2, 6, 8. Not checked: the rails beyond structure; the VCC contacts, ties 3, 4,
5, 7 and the load widths (2.5x overlays only); tie 1 (blurred under the VSS arm).

Findings, each checked by the tracer:

1. `rst_a`'s row ends on a metal contact at (5123,7606) and its metal runs north; the trace had
   the row as "going on east". **Changes a connection** (a contact exists; the port moves to the
   north edge). Confirmed (the tracer's own views `C2c.png`, `C2m.png` and `follow.py 5124 7500 N`
   had found the same while the review ran). Fixed: pad, contact and the metal M_b drawn.
2. Gate 3's two pull-downs are W about 37, not 18: the column's west edge is the dark line at
   x 4999-5001. Geometry only. Confirmed (`px.py row 7257 / 7343 4972 5024 3 metal`: orange poly
   x 4984-4996, a dark line at 4999-5002, orange again from 5005: an end cap, the channel's edge,
   the channel). Fixed: column x 5002-5040, rows from x 4984.
3. T1 is centred x 5045 over y 7226-7378 and steps west at y 7380; gate 2's exit poly is y
   7118-7136; (5053-5070, 7402-7418) is field. Geometry only. Confirmed for the exit poly (`px.py
   col 5058`: orange at y 7121-7133) and the corner; T1's centre taken as 5043. Fixed.
4. `ur`'s poly end is drawn 9 px west of the photo's: `ur`'s file, not changed (it overlaps).

Connections of the column after the fixes: `tools/t.sh lc1 sameconn.py d0eb7d7` lists only the
gate added since (`lc1_w7780 = NOT lc1_w7733`, its two transistors and two names); nothing of the
column differs. Because finding 1 changes a connection, a second round follows.

Round 1: one finding that changes a connection, fixed.

**Round 2: fix check of round 1 and full review of two new pieces, 2026-11-17 18:00 -0800.** `trace/lc1.txt` at
commit 3107183. Reviewer: a fresh Claude Fable 5.2 agent, images in `cache/scratch/lc1/review-2/`
(33). Part A: the three fixes of round 1. Part B: the pieces "wires" (where the column's wires go)
and "E1". Told to suspect: `lc1_w7040`'s route (the turn into the diagonal, a one-line slip in the
bundle, which row it becomes, taps, the nest of L-shaped metals at x 6472, the pad (6471,7930));
`rst`'s long row (the join in the metal gap at x 5100-5112, breaks, steps, taps);
`rst_c`'s poly link under V5 and its two arms; `rst_b`'s corners; E1's tie under the thin
metal, other devices on its row, its three pads, the two metals at x 6297; the rail names.

Part A: all three fixes right (the pad (5124,7605) has a ring and a green hole and M_b runs north
only, without contact on the rows it crosses; the column's west edge lies between x 4992 and 5010;
T1, the exit poly and the corner right; the 12 px join at x 5100-5112 is poly in both metal shots).
Both `sameconn` runs against d0eb7d7 differed only by gate E1.

Part B, checked and found correct (4x or more, sheared text maps along the diagonal, text maps,
the follower): `lc1_w7040` end to end (the turn at x 5141, the lowest band at constant offset from
x 5130 to 5466, the row y 7344, no taps, the metal x 6098-6307 separate from the pad, the corner
at x 6472, the pad (6471,7930), the row west); `rst`'s row straight and unbroken with no
taps; `rst_c`'s link and both arms at (5429,7520); `rst_b`'s corners; both pads of gate
3's inputs; all of E1 (the tie the least certain: read as a pass-over of the thin metal, which is
not widened and shows no pits). Not checked: the rail names; the row y 7561 west of x 6240 and the
row east of x 5640; whether E1's pull-down reaches east of the rail (width only).

Findings, each checked by the tracer:

1. `rst_c` has a metal branch north from the pad (5583,7519) that the trace lacked: x 5575-5593
   north to y 7347, east to x 5670, north to y 6975, east to x 5712, north out of the strip. It is
   the "lengthwise metal x 5575-5678" on `lc1_w7040`'s row. **Changes a connection** (a wire
   leaves the package at a place the trace did not have). Confirmed (`pad5583.png`, 6x, both
   metal shots: the metal from the north ends on the pad's ring as the one from the west does;
   `textmap 5556 7476 5612 7540`: the ring is about 15 px on the north side and 12 px on the
   west; `follow.py 5584 7480 N` and `5666 7300 N`; `br_top.png` for the jog at y 6976). Fixed:
   the metal drawn, the port added.
2. The row y 7953 was drawn 18 px past the poly's end. Geometry only. Fixed (ends at x 6126).
3. E1's load extension is y 7713-7730, not to 7743. Geometry only. Fixed.
4. `lc1_w7040`'s diagonal was drawn 6-8 px north-east of the band. Geometry only. Fixed (10 px
   west).

Round 2: one finding that changes a connection, fixed.

**Round 3: fix check, 2026-11-17 18:12 -0800.** The changes from commit 3107183 to a5daf42 (round 2's four fixes).
Reviewer: a fresh Claude Fable 5.2 agent, images in `cache/scratch/lc1/review-3/`. It checked each
change at 4x or more in two shots with row profiles and text maps, and both `sameconn` runs
against 3107183 (`connections identical`).

- Change 1 (`rst_c`'s metal north): right. One piece through all four corners in both metal
  shots; on the pad (ring 15 px on the north side against 13 px on the west, a green hole in the
  clean shot); no pad, ring or hole under it anywhere, the 95 px on `lc1_w7040`'s row included;
  separate from the parallel metals x 5700-5722 and x 5615-5635; still metal at y 6900 and y 6820.
- Change 2 (the row y 7953 ends at x 6126): right.
- Change 3 (E1's load extension): right.
- Change 4 (the diagonal moved 10 px west): **wrong way. Geometry only.** The poly's centre line
  is x = y - 1890; the trace had it at x = y - 1909 (and at y - 1899 before round 2's fix), mostly
  on the field beside the band, though it still met both rows and touched nothing. Confirmed
  (`px.py row 7160 5240 5300 4 metal`: orange x 5260-5276; `px.py row 7310 5390 5450 4 metal`:
  orange x 5410-5426). Fixed: `P 5128,7040 x5150 5454,7344 x6325 w=18`.

The connections are the same before and after that fix:

    tools/t.sh lc1 sameconn.py a5daf42            ->  connections identical
    .venv/bin/python tools/sameconn.py a5daf42    ->  connections identical

Round 3: no findings that change a connection.

### Round 4: full review of one new piece, "latch D, upper unit" (2026-11-17 22:00 -0800)

A fresh agent (Claude Fable 5.2), images in `cache/scratch/lc1/review-4/`. It covered only the new piece (the
cell copy, its own contacts, the clear and enable wires, the two thin metals, the join of `lc1_w7040`'s row),
at commit `51889ca`. Told to suspect: the arm from the clear device to the VSS box (clean shot dark), the strip
y 7837-7854 (diffusion or poly), the rounded outline in the gap x 5978-6016 (one poly or two), the undrawn thin
metal x 5965-5982 (a contact to the unit?), the row y 7517 through its two dark stretches, the enable metal's
corners and pad, where the thin metal of `lc1_w7928` ends, the VCC contact's place.

Checked and found correct (its words, shortened): the cell copy by overlay and side by side with the master
turned 180 degrees; the arm (diffusion-coloured band between edges in both chip-2 shots, the same profile in the
master and in `lc2`'s latch B; no evidence beyond that, the clean shot being dark there); the strip y 7837-7854
is diffusion; field at x 5998 from y 7862 to 7930 in both metal shots, so `lc1_w7862` and `lc1_w7928` are
separate polys; no contact on the thin metal x 5965-5982 at (5973,7856), (5971,7883), (5971,7905) or over the tie
box; the row y 7517 is one poly from x 5596 to the pad (6253,7517), no tap; the enable metal is one metal
through both corners and the pad (6213,7908) with no other hole from y 6900 to y 8067, and the metal
x 6160-6180 is separate; the clear metal ends north on the pad (6253,7517) and passes through the pad
(6255,7996); the thin metal of `lc1_w7928` stops at the pad (5929,7929); the VSS contact and its box, both
series gates, the pad (6117,7862) apart from the enable row; the output box and the row's join; the equation
and the devices. Not checked: the cell's interior line by line; anything south of y 8067.

Findings, all geometry only, all confirmed and fixed:

| Finding | Changes a connection? | Outcome |
|---|---|---|
| The two thin metals lie 6-9 px west of where drawn: `lc1_w7862`'s at x 6096-6110 (the cell has it at 6105-6119), `lc1_w7928`'s at x 5918-5932 (drawn 5925-5937) | no | confirmed (`px.py row 7980` and `8030`, metal shot: bright x 5918-5931 and x 6096-6108). `lc1_w7928`'s metal moved; for `lc1_w7862` a metal is drawn at the measured place beside the cell's; the ports follow |
| The VCC contact is a long ring (y 8003 to the strip's edge and on), not a square at (5865,8027) | no | confirmed (`px.py col 5865`: specks at y 8021-8027 and 8057); drawn 16 x 60 |
| The enable metal's east-west piece lies on the undrawn poly row y 7432 for all its length; no contact | no | a comment in the trace (trap 13) |
| An undrawn T-shaped metal (bar y 7515-7548, x 5755-6062, arm x 5884-5930 from the north) lies on `rst_c`'s row for 300 px; no contact | no | a comment in the trace; the metal is in Not done |

Connections before and after the fixes:

```
tools/t.sh lc1 sameconn.py 51889ca            -> connections identical
.venv/bin/python tools/sameconn.py 51889ca    -> connections identical
```

Round 4: no findings that change a connection.

## Not done

- **Latch D's lower unit** is `lc2`'s (y 8043-8293): `@inst tl1_ua 3351,3703 rot=180 o=2662.5,4465` (findcell
  0.68; not overlaid), with the enable row's pad about (6212,8141), the data row, the plate's pad about
  (5934,8133) on the thin metal x 5918-5932, and the unit's own contacts. Until it is drawn `lc1_w7862` and
  `lc1_w7928` are open inputs.
- **Cluster E, the rest**: the thin metal x 5965-5982 (through; contact candidates (5971,7883), (5973,7856)),
  the metal x 6160-6180 (from the row y 7475 south through a pad (6162,7650) and on to y 8866), the upper VCC
  box under the rail (y 7895-7965, contact (5865,7930)), the gate under the east VSS rail at y 8049-8066 (the
  lower unit's).
- The west half of cluster E (x 5650-5840): not looked at beyond the rail profile. The pads
  (5472,7866) and (5515,7910) feed rows into it; the pad (5537,7561) is the west end of
  `lc1_w7733`'s row.
- **The diagonal poly bundle and the crossing field** (x 5100-6450, y 6900-7500): about nine more
  lines come in from the north and north-west, turn east at y 6953-7300 and end on pads at
  x 6145-6190 ((6185,6953), (6145,6996), (6190,7040), (6145,7127) = `tla`'s, (6190,7169),
  (6148,7213), (6190,7257), (6148,7300)); rows y 7432 (pad (5542,7432)), 7473 (`bw`'s pad
  (5838,7470)), 7517, 7561; the vertical metals of the field.
- Other metals of x 5100-5600: V5 (x 5331-5351, down from the north to y 7570, west, south along
  x 5247-5270, west along y 7900-7920, south along x 5115-5137 out of the strip); the metal from
  the pad (5538,7433) (west, then south along x 5376-5399); the pads (5558,7649), (5583,7519).
  A C-shaped poly in the open: row y 7728-7747, vertical x 5404-5422, row y 7944-7963.
- x 4400-4750: the metal bus (`urch`'s channel), about eight thin metals and a wide one at
  x 4684-4716; `urch`'s pad (4400,7068) is here.
- The ninth gate of column W at y 8040-8140 (`lc2`).
- The T-shaped metal over `rst_c`'s row (bar y 7515-7548, x 5755-6062; arm x 5884-5930 from the north) and the
  poly row y 7432 under the enable metal's east-west piece: seen by review round 4, not drawn.

## Corrections (coordinator, from the handoffs of 2026-11-19)

- "Two metals lie on [`lc1_w7040`'s row] lengthwise without contact: ... x 6098-6307": that metal is
  `rst_ck` (`eof` run 2). Ports: the second through line is `res_b`, the third through line is `lpstb_b`, `rcs_x1`
  drives `rcs_x1`, line X (the first through line of the left-centre strips) is `rst_a`. "Believed, from the user: ... `rst_c` a chip-wide reset
  of some kind": traced, it is a buffered NOR(`lpstb_b`, `res_b`); the believed "three buffered copies ...
  the pattern of `rst_ck`, `rst_rc`, `rst_lat`" does not hold: they are copies of the reset. Not in the
  ports: an undrawn poly (`tl3_w3982`) enters at about (5065-5083, 6900), beside and under M_a. The
  polys of `res_b`, `lpstb_b` and the reset copy run on south below their pads into the diagonal bundle
  at (5150,6900), (5203,6900), (5266,6900): three of the bundle's undrawn lines.
- From `lc2`: `lc1_w7928`'s pad is at (5927,8131) on the lower unit's load plate; `ck_out`'s pad is
  at (6212,8128) and the metal runs on through it, south and east along y 8250-8268; `rst_c` ends on
  the pad (6254,8214) and is latch C's (and B's) clear; **latch D's data is `lc1_w7780`**. `lc1_w7170`'s
  metal T1 runs on to a pad (5232,8214) and a row west to a track down `lc2`'s west cluster: it is
  `lc2_w8474`, the clear of `lc2`'s counter. `lc1_w7990` drives `lc2`'s gate 9, whose output metal
  re-enters at x 5118-5136 and runs far north. Wires crossing y 8067 with no port here: `lc2_w8646`
  (x 6159-6177), `lc2_w8083` (poly x 6401-6415), `lc2_w8474` (x 6332-6350), `rst_ck` (
  x 6422-6440), `lc2_w8341` (x 5508-5524), `lc2_w9124` (thin metal x 5967-5981), row 4's metal
  (x 5422-5438). Geometry: in the `tl1_ub` instance the pad of `lc1_w7862` has its hole at (6105,8265)
  against (6115,8272) drawn.

## Corrections (coordinator, from the handoffs of 2026-11-19, second batch)

- Ports, `lc1_w7780` P (6450, 7772-7788) "seen to x 6710" (`eof` run 5): the row ends on a pad with a
  contact (6815,7778), whose metal goes south (drawn by nobody). The poly one track down at
  (6450, 7812-7832) is another net: row 3 of `eof`'s gate `g7700` (`eof_w7777`).
- That poly runs on west inside this strip to a pad with a contact (6339,7824), whose metal x 6333-6349
  goes south onto `lc2`'s metal of `lc2_w8474`: drawn by `eofw` (`trace/eofw.txt`, wire 3). So the gate
  on `rst_ck`'s tap row is one more load of `lc1_w7170`.
- **The wire this block called w7908, latch D's enable, is the gate line of `tc2`'s latch** (and that net is `ck_out`: `tl4` runs 11-12) (`eofw`: a metal
  staircase from `lc2`'s end (6450,8259) to a T (7273,8710), north to row 2 of `eof`'s gate and on to
  `tc2`'s metal (7837,6400); firm, resting on two joins read without `?`: `notes/blocks/eofw.md`,
  Ambiguities 1 and 2). No driver was met on any of it; "believed a chip-wide inverted clock" stands
  untested.
- **`lc1_w7170`'s driver is found** (`lc3`, run 2b): `lc1_w7170` = NOT `rst_c`, the lower inverter of
  `lc3`'s gate pair; `rst_c` comes from a metal that enters `lc3` at (6450,9455).

## Corrections (coordinator, from the handoffs of 2026-11-19, fourth batch)

- The diagonal bundle's "about nine more lines": drawn since by `eof`: the rows y 7170 (`lpstb_b`), 7214 (`res_b`), 7257 (`rst_a`), 7300 (`tl3_w3982`) with their pads, and the middle row y 6996 with its pad (6146,6997) (`bd1_n2`, to `tl5`'s bus poly x 5412); `rcs_e4`'s by `tla`. Left: the rows y 6953 and 7040.
- "`lc1_w7040` ... to a pad with a contact (6471,7930)": the metal that stands 25 px south of that pad on the same x (the L at y 7978) is `tl3_w3982`'s, not joined.
- `lc1_w7928` has one more load: the first of three inverters at x 7416-7606, y 8068-8448 (`eof` run 12), by a poly row y 8040.

## Corrections (coordinator, from the handoffs of 2026-11-20, third batch)

- Ports, `lc1_w7780` P (6450, 7772-7788) "gate E1's output row; seen to x 6710": the row runs on to an end pad with a contact (6819,7780) and from there down the left bus field to a pad (7100,15175) and a poly row y 15218 toward the bottom-centre logic's west rail (`busl`, piece `ga`, 2026-11-20; no tap; load open). It is not joined to the poly that lies on the same line east of x 6870, which is `eof`'s row of `lc1_w7170` coming up from y 7821.
- Latch D's enable ("No driver was met on any of it; believed a chip-wide inverted clock"): the net is `ck_out`, the clock buffer's output (`tl4` runs 11-12, firm joins; the metal x 6016 from (6016,6900) is one with `tl6`'s at (6016,6350)). Not inverted: it is `ck_out` itself.
- Of the diagonal bundle from `tl5`'s polys x 5368 / 5412 / 5455: the south-west diagonal (x - y = -1439) and its row y 7041 to the end pad (6188,7042) are drawn by `busl` (piece `gd`): `tl5_w2722`; the middle one is `eof`'s `bd1_n2`; the north-east one (x - y = -1306; seen as poly for y 6830-6950; the row y 6953 and the pad (6190,6955) lie where it would land) is not followed. `rcs_mv`'s poly column x 6236 through the band above the strip is drawn by `busl` (piece `fc`).

## Corrections (coordinator, from the handoff of `busl` run 14, 2026-11-21)

- Ports, "`rst` (gate 3's output) ... out at x 6450 (seen to x 6710)": the row runs on east under twelve tracks to an end pad (7076,7388) and by `busl`'s piece `xn` (the metal x 7078, a poly hop, a diagonal, the track x 6906) down the left bus field to the gate that clears the light pen flag (`bl0_w17610`). In the extraction `rst` now gates two pull-downs: the inverter that makes `rst_n` and this clear.
