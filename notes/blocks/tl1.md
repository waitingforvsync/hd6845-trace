# tl1: top-left random logic, the westmost strip (x 2100-2817, y 2500-6350)

Package `tl1` (part 1 of 6 of the top-left logic). Trace: `trace/tl1.txt`. Views:
`cache/scratch/tl1/`. The strip contains the west half of the first gate cluster, which
`tla` began (rails R1 = VSS x 2600-2650, R2 = VCC x 2778-2834, thin metal W x 2689-2703; see
`notes/blocks/tla.md`); this package draws what `tla` did not. Nothing of `tla`'s is redrawn.

## Status

2026-11-17 20:32 +0000. **Partial.** Three gates with their loads (8 transistors), the pull-downs of two more
(6 transistors, loads not traced), the vertical metals of the tracks x 2283, 2326, 2370, 2414,
2457, 2500 with their pads and rows (y 2790-5480 and y 5900-6350), the two pieces of the thin
metal x 2557-2573 over the west column, the two pieces of the thin metal x 2742, and one long
wire down the west side (`tl1_w3333`) are traced and extract with 0 errors and 0 warnings in
the full extraction. Main results: **the driver of `rcs_e4` is found**, a wide two-input NOR
in the west column at y 4778-5000; **its first input `tl1_w4678` is the output node of the
unit above it** (y 4590-4800), whose pull-downs are traced; and **the column y 3740-4215 is a
copy of y 4345-4800**, 608 px higher. The two units at y 3740-3960 and y 4340-4585 (copies of
each other), every load east of R1 in y 3740-4800 except the inverter's, the small cluster
below (y 5650-6350), the north-west corner (y 2500-2790) and the wiring west of x 2260 are
surveyed only: see Inventory and Not done.

```
rcs_e4    = NOR(tl1_w4678, tl1_w4937)     (2607,4852), (2607,4936)   marked: only the load's tie is uncertain
tl1_w3636 = NOR(tl1_w3594, tl1_w3678)     (2570,3592), (2570,3678)   firm
tl1_w4243 = NOT tl1_w4287                 (2626,4284)                marked: only the load's tie is uncertain
pull-downs only (the loads are not traced, so the extraction prints no equation):
tl1_w4678 : to VSS through tl1_w4025, or through tl1_w3594 and tl1_w4360 in series    (2570,4634), (2618,4715), (2618,4761)   no `?`
tl1_w4070 : to VSS through tl1_w4025, or through tl1_w3636 and tl1_w3752 in series    (2570,4026), (2618,4107), (2618,4153)   no `?` (a copy)
```

(`tools/unsure.py --equations`: `tl1_w3636` FIRM; `rcs_e4` and `tl1_w4243` DEPEND on the `?`
tie of the load's gate, as `tla`'s inverter does. The pull-downs and every join below are
drawn without `?`. With a load, the two new nodes would read
`tl1_w4678 = NOT(tl1_w4025 OR tl1_w3594 AND tl1_w4360)` and
`tl1_w4070 = NOT(tl1_w4025 OR tl1_w3636 AND tl1_w3752)`: **believed** until the loads are
traced.)

## Inventory (survey of the strip, 0.88x, `sv0.png`-`sv2.png`; details 2.6-2.7x `b1`-`b3`)

**findcell** (clean shot, region 2440-2850 x 2500-6350) with `tla`'s units as masters:

| Master (`tla`) | Hits in the strip |
|---|---|
| NOR unit of `rcs_in2`, 2535-2790 x 5120-5290 | **(-1,-1562), score 0.92**: the unit at y 3558-3728. Next best 0.53 |
| inverter `tla_w3505`, 2535-2790 x 3170-3290 | **(0,+1041), score 0.93**: the unit at y 4211-4331; (+1,+1822) 0.93 is `rcs_w2`'s inverter, already traced |
| selector `tla_w3417`, 2535-2790 x 3290-3550 | none above 0.55 |
| top unit, 2535-2790 x 3040-3170; `rcs_w2`'s unit 2535-2790 x 5030-5125 | none above 0.53 |

So only two of the untraced units are copies; the rest of the column is of the non-standard
kind (wide diffusions under R1 with several gates across).

**West column** (units between R1's VSS boxes, x 2540-2835), north to south:

| y | What | State |
|---|---|---|
| 2940-3590 | top unit, inverter, selector | `tla` |
| 3558-3742 | NOR, a copy of `rcs_in2`'s unit | **traced**: `tl1_w3636` |
| 3740-3960 | **a copy of the unit at y 4340-4585** (findcell, clean shot: 2535-2790 x 4345-4585 recurs at 0,-608, score 0.93). Pad with a contact (2562,3753) under the top end of the thin metal x 2557-2573 (north piece, to the pad (2555,4159)); its poly goes east under R1, over field, to a small box (2660-2680, 3744-3764). One diffusion under R1 (x 2572-2650, y 3795-3950) with a VSS contact (2620,3812) and two gate polys from the west across it (y 3841-3861 = `tl1_w2857`, y 3884-3904 = `tl1_w3636`): in series, by the look. Heavy box (2550-2575, 3925-3952) at the east end of the row y 3929-3949 (`tl1_w4287`). Load plate x 2725-2775, y 3760-3840. East of it a pad with a contact (2742,3888), the top of the thin metal x 2742 (to a contact (2742,4095)) | the thin metals and their pads **traced**; the unit not |
| 3982-4215 | **a copy of the unit at y 4590-4800** (findcell: 2535-2790 x 4590-4780 recurs at 0,-608, score 0.94) | **pull-downs traced** (`tl1_w4070`); load not |
| 4215-4345 | inverter (rail gate), a copy of `tla_w3505`'s | **traced**: `tl1_w4243` |
| 4340-4585 | Pad with a contact (2562,4361) under the top end of the south piece of the thin metal x 2557-2573; its poly (y 4353-4372) goes east under R1, over field, to a small ringed box (2660-2680, 4352-4372). Under R1, from the top: VSS box (2600-2648, 4403-4440, contact (2620,4420)), gate y 4450-4468 (`tl1_w4243`'s row), diffusion y 4470-4488, gate y 4490-4510 (`tl1_w3594`'s row, from the pad (2499,4503)), a large diffusion y 4520-4560 (x 2600-2660), gate y 4563-4585 (x 2603-2650; where its poly comes from is not read), then the VSS box of the unit below (y 4590-4640). West of R1 a heavy U outline (x 2548-2590, y 4520-4562) round a tan box (2553-2573, 4533-4558) under the thin metal, with a poly hairpin stub to x 2530 (`q4.png`: no poly between x 2335 and x 2530 at y 4525-4560 in three shots; in the copy above, the same box is the east end of `tl1_w4287`'s row). A salmon vertical bar x 2655-2668, y 4390-4440 east of the VSS box. A wide poly band x 2700-2780, y 4485-4520 with the top pad (2742,4496) of the thin metal x 2742 | the thin metals and their pads **traced**; the unit not (`q1a.png`, `q1m.png`, `p4.png`) |
| 4590-4800 | VSS box, a column west of R1 with `tl1_w4025`'s gate, the node with a buried contact to `tl1_w4678`'s row, and under R1 two gates in series (`tl1_w3594`, `tl1_w4360`) down to the VSS box of the wide NOR | **pull-downs traced**: the node is `tl1_w4678`; load not |
| 4778-5000 | wide NOR | **traced**: drives `rcs_e4` |
| 5000-5330 | `rcs_w2`, `rcs_in2` | `tla` |

**Tracks west of the column** (metal runs across x 2090-2460 at 30 heights, both chips;
`tools/tla_tracks.py`, `tools/follow.py`). Nine tracks at 43 px pitch:

| Track x | Pieces |
|---|---|
| 2110, 2153 | `ma1_drv_in`, `ma0_drv_in` (`mal`), full height |
| 2199 | **north piece `tl1_w3333`**: from a pad (2563,2550) west along y 2553, corner (2199,2556), south to a contact (2197,3333). South of y 3371: `tla_w3376` (`tla`) |
| 2239 | `tla_w3461` (`tla`), y 3449-5646 |
| 2283 | y 2721-3126 and y 3188-3520 (`tla`); **y 3622-4126 `tl1_w3636`**; **y 4230-4474 `tl1_w4243`**; south of y 4914 `ma4_drv_in` (`mal`) |
| 2326 | `rcs_thin_e` y 2754-3347, `tla_w3417` y 3404-5551 (`tla`); **from a pad (2326,5978) south out of the strip: `tl1_w5978`**. The poly that lies under it y 4533-4988 is **`tl1_w3333`** (below) |
| 2370 | **y 2843-3863 `tl1_w2857`**; **y 3925-4300 `tl1_w4287`**; **y 4925-5459 and east to (2521,5459) `tl1_w4937`**; from (2365,5847) south it is `ck_out`'s trunk (`tla`), with **a second contact (2372,6061)** found here |
| 2414 | `rcs_c1` y 2972-5082, `rcs_in2` y 5182-5411 (`tla`); **y 6010-6207 `tl1_w6022`**; `lc_step` from (2412,6278) (`ur`) |
| 2457 | **y 2800-3690 `tl1_w3678`**; **y 4012-5372 and east to (2521,5372) `tl1_w4025`**; `clk_tl` from (2458,5587) (`tla`) |
| 2500 | **y 2886-4730 `tl1_w3594`**; **y 4882-5232 `rcs_e4`**, continuing as `tla`'s metal round to bus line C; **y 5924-6252 `tl1_w5936`** |

**North of y 2790** (`n1.png`, 1.45x): only wiring. The metal x 2199 turns east at y 2557. Nested
poly L's at x 2440-2530, y 2590-2680 and three polys going north at x 2410, 2455, 2500 above
y 2620; the poly that continues `rcs_c1`'s line (x 2258-2272 north from y 2985, east along
y 2712-2725 to x 2415, north: `tla`'s Not done). The plain olive areas are field. Not traced.

**South of y 5640** (`sv2.png`, 0.88x only): the west half of the small cluster: units at about
y 5690-5790 (pad with a contact (2560,5710)), y 5850-5980, y 6000-6130, y 6170-6330, under the
same rails; contacts on the tracks at (2503,5934), (2327,5977), (2412,6020), (2373,6066),
(2555,6113), (2742,6045), (2412,6193), (2498,6235). Not traced.

## Logic

### The gate that drives `rcs_e4` (y 4778-5000): traced

```
rcs_e4 = NOR(tl1_w4678, tl1_w4937)
```

- One diffusion: a part west of R1 (heavy outline x 2548-2600, y 4820-4975) and a part under
  R1 (to x 2664), between two VSS boxes of the rail: above (y 4778-4845, elongated contact
  ring (2620,4810); `u8c.png`, 4.2x: tan without a break from the contact down to the gate) and
  below (y 4950-5000, contact (2620,4982)).
- Two poly lines cross all of it: y 4843-4862 and y 4926-4946 (W/L about 114/20 each: the
  widest pull-downs of the column, which fits a line with 17,000 px of wire). The part
  between them is the node. That the part west of the rail and the part under it are one
  diffusion rests on the outlines running across the rail's edge, as in `tla`'s units (the
  etch line sits on x 2600); if they were two, both gates would still be on the node.
- Output: buried contact (concentric box 2550-2579, 4874-4914) with the poly y 4884-4904, west
  to a pad with a contact (2500,4894) under the north end of the metal x 2500. **That metal
  runs south into the pad (2497,5238) of `rcs_e4`** (`tla`: the gate pad of `rcs_in2`'s unit,
  from which `tla`'s metal goes on to (2565,5321) and bus line C). Evidence that it is one
  metal through the pad (tracing guide, trap 16): `tools/follow.py 2500 5000 S` goes through
  the pad to `tla`'s corner (2511,5330), and `N` ends at y 4892; `tools/tl1_prof.py 2500 5170
  2500 5275` (both metal shots): ring 15 px on the north side of the pad centre, 12 px on the
  south side, bright metal in chip 1 right up to the ring; `j1.png` (6x, both chips): the
  line's two edge lines run into the ring.
- Gate 1, `tl1_w4678`: the poly is an L. It comes down x 2434-2452 from a corner at
  y 4668-4688, where it arrives from the east (seen at 2.05x, 2.6x, 4.1x and 4.3x: `a4`, `a5`,
  `b3`, `u7a`, `u8a`). Its east end lies on a buried contact on the output node of the unit
  at y 4590-4800 (next section).
- Gate 2, `tl1_w4937`: pad with a contact (2370,4937) at the north end of a metal x 2370,
  south to y 5459, east to a pad with a contact (2521,5459); from there a poly row east along
  y 5450-5470 under the foot of the cluster. It is straight to x 3400 at 1.44x (`f2.png`) and
  goes on east into the second crossing field. Drawn to x 2817. Source not found.
- Load: node east under thin W to a plate x 2732-2770, y 4848-4914 and the VCC box under R2
  (contact (2800,4882)). No diffusion edge crosses the plate in the metal shots, so the
  channel may be as wide as the plate is tall (strong load, W/L up to 66/38); drawn 28-34/31-38.
  The plate's tab and its tie to the node (heavy box 2722-2765, 4915-4965 in both shots, 6x
  `u8d.png`) are not resolved: `?`.

So `rcs_e4` is high only while both `tl1_w4678` and `tl1_w4937` are low. `tl1_w4678` is the
node of the unit above (pulled low by `tl1_w4025`, or by `tl1_w3594` and `tl1_w4360`
together); what those and `tl1_w4937` are is not known.

### The unit that drives `tl1_w4678` (y 4590-4800) and its copy (y 3982-4215): pull-downs traced

```
tl1_w4678: pulled to VSS by tl1_w4025, or by tl1_w3594 and tl1_w4360 in series
tl1_w4070: pulled to VSS by tl1_w4025, or by tl1_w3636 and tl1_w3752 in series   (the copy)
```

**The question left by the first round** (is the tan rectangle at the east end of
`tl1_w4678`'s row a buried contact, or does `tl1_w4025`'s row make a pass transistor there?)
**is decided: both features are there, and the transistor is a pull-down to VSS.**
What lies under the thin metal x 2557-2573 is a column of diffusion like the NOR units'
column, x 2553-2588:

- Profile down x 2563 in four shots (`tools/px.py col 2563 4525 4700 3 all`), clean shot:
  pink = field y 4567-4591 (188/121/128); a dark edge at y 4594-4597 in all four shots; tan
  y 4600-4618 (195/175/140); the salmon row of `tl1_w4025` y 4624-4642 (240/170/126); tan
  y 4648-4657; a dark line y 4660-4666 (the top edge of the row `tl1_w4678` on the box); tan
  y 4669-4684 (200/178/134); the heavy bottom y 4687-4696; pink again from y 4700 and the row
  of `tl1_w3594` at y 4711-4726. So the row crosses a diffusion (tan directly above and
  below it), which is a transistor. The "pink between the row and the rectangle" of the first
  round is one sample of the row's own red outline.
- The column's top is tied to VSS: rows y 4607 and y 4612 (`tools/px.py row`): the clean shot
  is tan without a break from x 2559 to x 2583, the chip-2 stripped shot has red minus green
  +15 to +37 at x 2589-2595 (diffusion; field there is 0 or below, as in row y 4580), and the
  metal shots show plain ground between two edge lines (y 4596, y 4616-4620) from the column
  to the rail. It is an arm (y 4598-4616) onto the VSS box under R1 (y 4590-4640, contact
  (2628,4610): ring in the metal, speck in the clean shot, `p4.png`).
- East edge of the column: a dark line at x 2586-2591, y 4620-4670 in both metal shots and the
  chip-2 stripped shot, with field east of it (stripped shot at x 2595, y 4652-4664: green
  over red). `tl1_w4025`'s row runs on over it to x 2598 and ends at the VSS box's edge.
- The node: below the row the column runs to y 4692. The row of `tl1_w4678` (y 4668-4688)
  ends on it in a box with a heavy outline on the west and south sides, x 2551-2575,
  y 4663-4692 (`p2a.png` 6.8x, `p3.png`): a buried contact. The thin metal above has no ring
  and no widening there (text map), so it is not on the box.
- From y 4670 the node widens east: the edge line y 4669 runs from x 2578 to the rail in both
  metal shots (`tools/textmap.py 2536 4636 2616 4800 3 --acid`), and below it the ground is
  plain down to gate 1's edge at y 4700. Column x 2589 (`tools/px.py col 2589 4640 4780 3`):
  y 4676-4700 is diffusion in the chip-2 shots (stripped 127/95/69, metal 171/133/86), the
  same as the diffusion between the two gates (y 4739-4745) and unlike the gate polys
  (blue 45-50 against 69-81). The clean shot is tan from the box to x 2588 in row y 4680. So
  the box, the gap and the diffusion under R1 at y 4668-4700 are one node.
- Under R1 and in the gap west of it (x 2580-2657), going down from the node: gate
  y 4702-4722 (`tl1_w3594`: the row from the pad (2499,4718) lies at y 4711-4726 under the
  thin metal and steps up in the gap), diffusion y 4722-4747, gate y 4750-4772 (from the pad
  with a contact (2555,4767): ring with a bright centre, green hole in the clean shot), then
  the VSS box of the wide NOR (contact (2620,4810)). Both gates end east of the rail in
  rounded ends at about x 2680 in the metal shots; gate 2's poly goes on under thin metal W
  (salmon at y 4745-4763 under it, where y 4700-4740 is pink) and east to about x 2762.
- The dark round spot at (2592,4738) in the gap between the gates is in the copy too, at
  (2592,4133); there is no metal over it. Taken as the gap's mark on the diffusion.

**`tl1_w4360`: the thin metal x 2557-2573, south piece.** `tools/follow.py` gives
(2563,4364)-(2565,4684) and then no metal for 24 px: the metal is dim (chip 2: 6-9 of 16)
from y 4687 to y 4711 over the box's heavy bottom edge and the row's top edge (tracing
guide, trap 22); from y 4714 it is bright again and its two edge lines run on into the pad
(2555,4767) in both metal shots (`p2m.png`), where it ends (bare ground from y 4789). Its top
end is a pad with a contact (2562,4361) (ring, bright centre, green hole: text map). The
follower's contact candidates on the way (y 4465, 4509, 4551, 4620) are the edges of the
rows and of the box underneath: no widening, no ring (`p4.png`). The top pad's poly runs east
along y 4353-4372, under R1 over field (pink above and below it there), to a small ringed
box (2660-2680, 4352-4372) in the unit at y 4340-4585, which is not traced. So `tl1_w4360`
has two drawn ends: gate 2 here, and that box. **Believed**: it is the output of the unit at
y 4340-4585.

**The copy.** `tools/findcell.py 2535 4590 2790 4780` (clean shot) finds the unit again at
0,-608 with score 0.94, and the unit above it (2535-2790 x 4345-4585) at 0,-608 with 0.93. The
geometry is a cell (`tl1_ub`) placed twice; the overlay of the copy was checked on `o7.png`
(2.9x, clean shot and metal): VSS box with a contact (2620,4002), arm, `tl1_w4025`'s row
y 4017-4036 (from the pad (2458,4026)), the box (2551-2575, 4055-4084), the two gates
(`tl1_w3636`'s row y 4104-4122 from the pad (2283,4113); the pad with a contact (2555,4159)),
the VSS box below with its own contact (2622,4188). Differences from the master, both at the
edges: the copy's stack ends on a VSS box of its own; and the poly on the copy's box is a
**stub** that ends in a round end at x 2532 (`q5.png`, 5x, three shots), where the master's
is the row of `tl1_w4678` going west. So the copy's node `tl1_w4070` has no drawn load of its
own gate: where it goes is east, not traced. The north piece of the thin metal
(`tl1_w3752`, follow.py (2563,3756)-(2566,4172)) joins the pad (2562,3753), whose poly goes
east under R1 to a box (2660-2680, 3744-3764) (`q2.png`, 6x), and the pad (2555,4159).

**The load is not traced** (two passes: `p5a.png` 6.8x clean, `p5m.png`, `p6.png`, `p7.png`
4.7x both stripped shots, `p8.png` 4.5x both metal shots, and a text map). What was seen,
for the next pass (master coordinates; the copy is 608 px higher):

- The node runs east under R1 (y 4668-4697), through the gap (dark there), under thin metal
  W (tan under W at y 4649-4697; pink at y 4700-4740). W (8-10 px wide at x 2689-2697) begins
  at about y 4648 and is wide and bright (x 2683-2703) over y 4665-4692, with a green patch
  in the clean shot at x 2686-2698, y 4688-4694 and a dark bar at y 4694-4700: a contact of
  W on the node, or the node's box with a buried contact under W as in the NOR units
  (tracing guide, trap 22). Not decided. If it is a contact, W (follow.py: on to y 5952, with
  candidates at y 4768, 4795, 4936, 5076, 5252, 5739, 5776, 5894, 5920) carries `tl1_w4678`.
- East of W a plain strip x 2703-2720 runs from y 4650 to y 4725 beside it (tan in the clean
  shot, bounded by a dark line at x 2722 in both metal shots), and widens to x 2703-2738 for
  y 4728-4795, ending in a heavy U outline (x 2717-2752, y 4775-4800).
- A poly band y 4742-4762 crosses that wider part: salmon under W and from x 2701 to x 2713,
  darker to x 2740, red blobs at x 2743-2762; from there a poly goes up x 2757-2772 to the pad
  (2742,4703) of the thin metal x 2742. Whether the band is one poly with gate 2 (it is
  salmon without a break under W in the text map) was not checked at a junction view.
- A salmon bar y 4652-4665, x 2715-2775, with field below it under the thin metal x 2742.
- Second pass, master and copy side by side (`tools/mosaic.py 2672 4640 115 165 --offsets
  "0,0 0,-608" --scale 5.4`, clean shot and chip-1 metal: `L_acid1b.png`, `L_metal1.png`);
  the two copies agree in all of this:
  - the tan strip east of W is diffusion, not margin: right beside it, under W, the field is
    pink (x 2683-2698, y 4697-4773). It is one tan band with the node's box under W
    (x 2683-2715, y 4651-4697) and runs on south at x 2700-2718;
  - where the band y 4744-4760 crosses it the poly is bright orange (x 2700-2715), the colour
    of poly over a channel: **a transistor there, between the node's strip and the diffusion
    south of the band** (x 2700-2741, y 4766-4797, closed by the heavy outline, with a
    salmon box (2718-2742, 4773-4800) in its corner that looks like a buried contact);
  - the band's poly (x 2709-2740) and a vertical poly x 2746-2768, y 4686-4768 are one
    brown area in the metal shot, joined at the bottom; a dark line at x 2741, y 4729-4797
    crosses the band (the east edge of that diffusion);
  - W's wide part (y 4645-4692) shows no ring in either copy in the chip-1 metal shot, and
    the clean shot no green hole under it in this view: against a contact of W there;
  - the round mark on W at (2697,4786) is in the master only: dirt.
  What is still missing for a circuit: which supply or node the diffusion south of the band
  is on, and whether the band is one poly with gate 2 across x 2678-2686 (the metal shot
  shows a rounded outline at x 2683 that may be the band's west end or W's edge line).
  Nothing of this is drawn.
- R2 has no VCC box between y 4640 and y 4760 (pink); the boxes are `tla`'s at y 4588-4627
  and y 4763-4802. West of the lower one, x 2755-2778, y 4775-4800 is field in the chip-2
  stripped shot.

### The thin metal x 2742 (two pieces): traced, pads only

`tl1_w4703`: (2742,4496)-(2742,4703); `tl1_w4095`: (2742,3888)-(2742,4095) (follow.py:
(2740,4496)-(2741,4706), (2741,3890)-(2741,4100)). All four ends are contacts on poly pads
(mosaic at 3.9x in the metal shot and the clean shot, `m2_metal.png`, `m2_acid1b.png`: ring
with a bright centre, green centre on a salmon pad). The top pad is part of a wide poly band
(x 2700-2780, y 4485-4520), the bottom pad a square (2725-2762, 4688-4726) whose poly goes on
south. Only the pads are drawn; what the bands are is part of the untraced loads.

### The NOR at y 3558-3742: traced (a copy)

```
tl1_w3636 = NOR(tl1_w3594, tl1_w3678)
```

`tla`'s `rcs_in2` unit moved by (-1,-1562) (findcell 0.92), checked on `c2.png` (3.3x, clean
shot and metal). Column x 2549-2591 between `tla`'s rail box (contact (2612,3550)) and the
box at y 3697-3742 (contact (2622,3722)). Gate 1: poly y 3582-3602 from a pad with a contact
(2500,3594) on the metal x 2500. Gate 2: poly y 3668-3688 from a pad with a contact
(2457,3678) at the south end of the metal x 2457. Output: buried contact (2547-2577,
3620-3652), poly west to a pad with a contact (2283,3636). Load to the VCC box (contact
(2803,3643)), which is the lower part of `tla`'s box (2785-2842, 3540-3612).

Where the output goes: metal x 2283, y 3622-4126, with pads at (2283,3894) and (2283,4113)
whose poly rows run east to the units at y 3740-3960 and y 4000-4215 and cross the diffusion
under R1 there (gates; those units are not traced, the rows are drawn to x 2545).

### The inverter at y 4215-4345: traced (a copy)

```
tl1_w4243 = NOT tl1_w4287
```

`tla`'s inverter `tla_w3505` moved by (0,+1041) (findcell 0.93), checked on `c1.png` (3.3x).
Rail gate: poly y 4275-4293 across R1 from a pad with a contact (2370,4287). Node under the
rail and west of it with the buried contact (2538-2582, 4229-4265); output poly y 4233-4253
west to a pad with a contact (2283,4243). VSS box below (contact (2622,4318)). The load's
strip runs onto `tla`'s VCC box (2785-2842, 4190-4262); the tie of the plate's tab is `?`
as in the master.

- Input: the metal x 2370, y 3925-4300, from a pad (2372,3938) whose poly row y 3929-3949
  ends on the heavy box (2550-2575, 3925-3952) of the unit at y 3740-3960. **Believed**: that
  box is the output of that unit (two series gates `tl1_w2857`, `tl1_w3636` on a diffusion
  with VSS at the top would make `tl1_w4287` = NAND). Not traced; nothing is claimed.
- Output: metal x 2283, y 4230-4474, to a pad (2283,4462) whose row y 4452-4470 runs east
  into the unit at y 4340-4470.

### The tracks beside the small cluster (y 5900-6350): traced (wiring only)

`s1.png` (2.05x, metal and clean shot), overlay `o3.png`. Each row runs east into the small
cluster, which is not traced; rows are drawn to x 2545.

- **`ck_out` has a second contact on its trunk metal x 2370**, at (2372,6061), 214 px below
  `tla`'s (2365,5847): ring on the line in the metal shot, pad with a green centre in the
  clean shot. Its poly row runs east along y 6054-6072: one more `ck_out` load in the small
  cluster.
- `tl1_w5978`: pad (2326,5978), row east y 5969-5987; the metal x 2326 goes south out of the
  strip (not followed).
- `tl1_w6022`: metal x 2414, y 6010-6207, joins two rows: y 6013-6031 and y 6186-6204.
- `tl1_w5936`: metal x 2500, y 5924-6252. The top pad's row runs **west** along y 5926-5944
  under all the tracks to a corner at about (2096,5935) and turns north under the edge of
  MA1's metal (`s2.png`; not followed); the bottom pad's row runs east along y 6228-6246.

### `tl1_w3333`: a long wire from the top of the strip to the small cluster (traced, part `?`)

One net, about 4,700 px, no gate on it inside what is traced:

1. a pad with a contact (2563,2550), whose poly goes on **east** under R1 along y 2543-2560
   (seen to x 2637, `w2.png`; drawn to x 2640);
2. metal west along y 2553 to a corner (2199,2556) and south at x 2199 to a contact
   (2197,3333) (`tools/follow.py`: one piece; overlay `o4.png`);
3. that contact's pad is a bulge on a vertical poly x 2170-2187 (free stub above it to y 3282,
   `w1.png` 3.1x, `r2.png`), which runs south to y 4550, east along y 4533-4550, **south under
   the metal x 2326** (the "poly of another net" of `tla`'s notes: no pad, no ring), west along
   y 4972-4988, south at x 2134-2149 to y 5810, and east along y 5793-5810 into the small
   cluster (drawn to x 2545; `r1.png`).

Evidence: the five corners at 2.3x (`r2.png`), the horizontal pieces and the piece under the
metal at 2.05-2.15x (`a4`, `a5`, `s3`, overlay `o5.png`). The three long stretches (x 2170-2187
y 3355-4535; x 2134-2150 y 4995-5795; the row y 5793-5810) were seen only in a 1.9x mosaic
(`v1.png`) and at 1.8x: they are alone in bare field, with nothing beside them to step onto,
but they are drawn `?P`, so the wire as one net is **marked**.

## Ports

| Name | Layer | Where it crosses | Direction | What |
|---|---|---|---|---|
| `rcs_e4` | M | (2500,5232), onto `tla`'s metal | driven here | the long control line of the step logic |
| `tl1_w4937` | P | (2817,5460), east | into the block | gate 2 of `rcs_e4`'s NOR; row under the foot, on east past x 3400 |
| `tl1_w4025` | P | (2817,5372), east | not known | row under the foot, on east past x 3400; on the same metal x 2457 the pads (2458,4026) and (2458,4635), each the gate of a pull-down (units at y 3982 and y 4590) |
| `tl1_w2857` | P | (2817,2857), east; (2545,3851) | not known | row above the cluster; the other end is a gate row y 3841-3861 |
| `tl1_w3678` | P | (2817,2812), east | into the block (a gate is its only other end) | gate 2 of the NOR |
| `tl1_w3594` | P | (2817,2899), east; (2545,4503) | not known (four gate-side pads) | gate 1 of the NOR; a gate of the unit at y 4590; a gate row of the unit at y 4340 |
| `tl1_w4678` | D | (2702,4684), east | driven here (pull-downs) | the node of the unit at y 4590-4800 and gate 1 of `rcs_e4`'s NOR; its load is east, not traced |
| `tl1_w4070` | D | (2702,4076), east | driven here (pull-downs) | the node of the copy at y 3982-4215; load and destination not traced |
| `tl1_w4360` | P | (2660,4362) | believed from the unit at y 4340-4585 | thin metal x 2557-2573, south piece; gate 2 of the unit at y 4590 |
| `tl1_w3752` | P | (2660,3754) | believed from the unit at y 3740-3960 | thin metal x 2557-2573, north piece; gate 2 of the unit at y 3982 |
| `tl1_w4703` | P | pads (2742,4497), (2742,4707) | not known | thin metal x 2742, south piece |
| `tl1_w4095` | P | pads (2742,3889), (2742,4099) | not known | thin metal x 2742, north piece |
| `tl1_w3636` | P | (2545,3894) | driven here | into the unit at y 3740 (its other row is gate 1 of the unit at y 3982) |
| `tl1_w4243` | P | (2545,4461) | driven here | into the unit at y 4340 |
| `tl1_w4287` | P | (2545,3939) | from the unit at y 3740-3960 (believed) | the inverter's input |
| `tl1_w3333` | P | (2640,2551) east; (2545,5801) east | not known | long wire down the west side |
| `ck_out` | P | (2545,6063) | from `tla`'s trunk | a gate row into the small cluster |
| `tl1_w5978` | P, M | (2545,5978); (2326,6350) south | not known | row into the small cluster; metal x 2326 on south |
| `tl1_w6022` | P | (2545,6022), (2545,6195) | not known | joins two rows of the small cluster |
| `tl1_w5936` | P | (2110,5935), on to a corner (2096,5935) and north; (2545,6237) | not known | from the pad-ring side to a row of the small cluster |

The same ports, one per line: `ports.d/tl1.txt`.

The rows y 2812, 2857, 2899 were read at 2.5x (`n2.png`) from their pads to x 2820: straight,
under R1, thin metal E's north arm and a wide metal x 2735-2785, no pad.

## Ambiguities

- The wide NOR (`rcs_e4`): the diffusion's continuity across R1's west edge at x 2600 is
  not seen directly (a dark line sits on the rail edge, as at every rail gate here); the
  outlines continue across. If it were a break, the output contact would be cut off from
  the load. Drawn firm; review round 1 could not decide it either.

- **The load of `rcs_e4`'s gate**: its width (28 to 66) and the tie of its gate (see above).
- **The joins across R1's west edge** (x 2600) in the wide NOR: as in `tla`.
- **The dark dots on R1** at (2625,2855) and on the wide metal at (2765,2820), (2775,2905) in
  the chip-2 metal shot, where the three rows pass under: no pad in the clean shot; taken as dirt.
- `tools/tla_tracks.py` reported the metal x 2457 broken at y 4683-4869 and the metal x 2500
  at y 5196-5238; `tools/follow.py` and the photos show both continuous (a poly lies beside or
  under them there). Its breaks need a look every time.

- **The unit at y 4590-4800** (and its copy): the joins of the column's arm and of the node
  across R1's west edge (x 2590-2600) are covered by the rail's edge line, as in every unit
  here; both are drawn without `?` on the evidence in the Logic section (tan to x 2588 in the
  clean shot, diffusion at x 2589-2595 in the chip-2 stripped shot, edge lines running into
  the rail in both metal shots). If the arm were not joined, `tl1_w4025`'s transistor would
  hang; if the node were not, `tl1_w4678` would have that one pull-down only.
- **Is thin metal W on the node `tl1_w4678` at about (2693,4688)?** See the load, above. Not
  drawn.
- **The band y 4742-4762 east of x 2684 (under thin W; orange where it crosses the strip
  x 2700-2715; the same 608 px higher) is NOT gate 2's poly**: gate 2 (`tl1_w4360`, in the
  copy `tl1_w3752`) ends in a rounded end at x ~2670 with plain ground across x 2672-2684
  (review). What that band is, and whether it reaches the pad (2742,4703) (`tl1_w4703`),
  is not traced.
## Not done

- **The loads of the units at y 4590-4800 and y 3982-4215** (the copy, 608 px higher) and
  whether thin metal W is on the node: Logic section, "The load is not traced", lists what
  was seen. Until then `tl1_w4678` and `tl1_w4070` have pull-downs only. Next: a junction
  view at 5x in the clean shot and both metal shots of (a) W over the node, x 2680-2710,
  y 4640-4705, against a known contact of W; (b) the band y 4742-4762 from x 2680 to x 2775
  and up to the pad (2742,4703); (c) the strip x 2703-2738, y 4650-4800 and its heavy U end.
  Use the copy (0,-608) as a second look at each: `tools/mosaic.py ... --offsets "0,0 0,-608"`.
- **The unit at y 4340-4585 and its copy at y 3740-3960** (Inventory has what was seen). The
  copy's output box is on `tl1_w4287`'s row; the master's box has a stub only. Trace the
  master as a cell and place it at 0,-608, then check the edges: the two rows from the west
  are `tl1_w4243`, `tl1_w3594` in the master and `tl1_w2857`, `tl1_w3636` in the copy; the
  third gate (y 4563-4585, copy y 3955-3977) has no row from the west. The small ringed box
  (2660-2680, 4352-4372) at the end of `tl1_w4360`'s pad poly (copy: `tl1_w3752`'s) and the
  salmon bar x 2655-2668, y 4390-4440 belong to it.
- Thin metal W: its pieces (north piece `rcs_u3288_n` to y 4002, `tla`; a short piece
  y 4042-4086; the south piece from y 4648 to y 5952) and their contacts. The follower's
  metal test fails on it (8 px wide, dim): profiles needed.
- The far ends of the rows `tl1_w4937`, `tl1_w4025` (east of x 2817, past x 3400) and of
  `tl1_w2857`, `tl1_w3678`, `tl1_w3594` (east of x 2817 along y 2812-2899).
- `tl1_w3333`: its ends (east of (2640,2551) under R1; east of (2545,5801) in the small
  cluster).
- `tl1_w5936`'s poly north of (2096,5925), `tl1_w5978`'s metal south of y 6350. A second
  vertical poly x 2137-2147, y 3192-4205 (free ends at both? `v1.png`, 1.9x) between MA1's
  and MA0's metals: not looked at.
- North of y 2790 and the small cluster south of y 5640: surveyed at low zoom only.
- The six pad contacts (2370,4937), (2500,4894), (2521,5459), (2521,5372), (2372,6061), (2458,4635) were
  re-checked in one mosaic at 3x in both shots (`k_metal.png`, `k_acid1b.png`): ring with a bright
  centre, pad with a green centre, in all six. The other pads were read at 2.05-2.5x only.
- The tie of the plate's tab in the two marked loads (2706-2754, 4287-4323) and (2712-2744, 4906-4960).

## Review

Round 1 (full review, 2026-11-17 20:06 +0000, a fresh agent on claude-fable-5-2, at commit a3b1701). Told to
suspect the nine parallel tracks west of x 2540 (piece ends, pads, a tap on a piece), the
through-pad (2497,5238), the wide NOR's rail-edge joins, gates and load, the two cell
copies, the rows y 2812 / 2857 / 2899 under R1, and `tl1_w3333`'s corners and long
stretches. It checked all 24 pads (ring and green centre, 2.9x), every piece end with the
follower in both chips, the through-pad at 5x, the NOR's gates and contacts, the L
`tl1_w4678`, both copies by mosaic and a 4x overlay, the three rows in the clean shot, and
`tl1_w3333`'s five corners at 5x with a scan of both long stretches every 4 px.
No finding changes a connection. Findings, each checked by the tracer:
1. The NOR copy's VCC box is a box of its own below tla's (two edges, no tan between):
   redrawn from y 3626; still `vcc` through its own contact.
2. The inverter copy's VCC box is one diffusion about y 4188-4338 with three contact rings
   (confirmed on `review-1/invvcc.png`): the lower part and two contacts added.
3. The wide NOR's gate polys run on east to about x 2680: drawn; W is somewhat above 114.
Also: `tl1_w3333`'s three `?P` stretches were read end to end and are now firm.
The extraction's transistor list is unchanged by these edits.
Could not be checked: the diffusion's continuity across R1's west edge (x 2600) in the
wide NOR (the dark line there could be the etch boundary; if it were a break the output
contact would be cut off from the load; drawn without `?`: see Ambiguities), the load ties
(`?`), the far ends of the port rows.

Round 2 (fix check, 2026-11-17 20:10 +0000, a fresh agent on claude-fable-5-2, against commit a3b1701). The two
VCC boxes and the firmed stretches of `tl1_w3333` are right (each stretch at 4x at both ends
and three places, profiled end to end in two shots); the netlists of the two versions are
identical. One finding: the wide NOR's gate polys run on under thin metal W to about
x 2697, not 2680 (salmon on exactly those rows in the clean shot, edge lines across W in
both metal shots; confirmed by the tracer on `review-2/C1.png`): drawn to x 2697. No ring
on W there and no other diffusion reached: no electrical effect.

Round 3 (fix check, 2026-11-17 20:13 +0000, a fresh agent on claude-fable-5-2, against commit efc2c51). Colour
profiles along both gate rows and four comparison rows in four shots: both polys end at
x 2697-2701, nothing gate-specific continues east of thin W, no pad; thin W has no ring
over either poly; the polys stop short of the load's `?` items; the netlist outputs of the
two versions are byte-identical.

Round 3 of the first round of work: clean (no findings).

### Second round of work (the units at y 3740-4215 and 4345-4800, the thin metals, ports)

Round 1 (full review of what was added since 526f8e1, 2026-11-17 20:43 +0000, a fresh agent on
claude-fable-5-2). Told to suspect the rail-edge joins at x 2590-2600, whether (2570,4634)
is a pull-down to VSS, the buried contact, the thin metal's continuity at y 4687-4711, gate
2's poly east of the rail, thin W on the node, and the copy at -608. Checked: the rail-edge
joins by colour in both chip-2 shots against field rows; the pull-down (tan above and below
the row, the arm to the box, contact (2628,4610) with ring and pits); the buried-contact box
in two stripped shots; both thin metals' pieces and pads; the copy by overlay item by item.
One finding, confirmed by the tracer on `review2-1/06_gap.png`: gate 2's poly was drawn
through the gap between R1 and thin W to x 2715; it ends at x ~2670. Cut at x 2672 in the
cell; the two ports that named the foreign band removed; no extracted connection changed.
Not decided (left undrawn): whether thin W contacts the node near (2693,4688).

Round 2 (fix check, 2026-11-17 20:46 +0000, a fresh agent on claude-fable-5-2, against commit 8fbdd7d). Gate 2's
poly ends between x 2668 and 2673 in the master and in the copy (7x in two shots, profiles
in four; plain ground at x 2673-2679, no poly edge lines down x 2676); the gate still
crosses the whole stack (east edge x 2655-2658; both transistors 81/21 as before);
`tools/sameconn.py 8fbdd7d`: connections identical; the ports file parses.

Round 2: no findings.

