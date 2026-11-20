# tl1: top-left random logic, the westmost strip (x 2100-2817, y 2500-6350)

Package `tl1` (part 1 of 6 of the top-left logic). Trace: `trace/tl1.txt`. Views:
`cache/scratch/tl1/`. The strip contains the west half of the first gate cluster, which
`tla` began (rails R1 = VSS x 2600-2650, R2 = VCC x 2778-2834, thin metal W x 2689-2703; see
`notes/blocks/tla.md`); this package draws what `tla` did not. Nothing of `tla`'s is redrawn.

## Status

2026-11-18 12:00 +0000, **run 5** (Tom Seddon; two pieces on top of what is described below, which
stands). Full extraction 2,346 nets, 4,158 transistors, 0 errors, 0 warnings; no transistor added.

- **`tl1_w5936` is followed from its corner at (2094,5935) to the north edge of the strip: it is
  one net with the poly along the north edge** (which had a name of its own, after its y: glossary,
  Former names). The wire goes up
  the west margin by two cross-unders of the MA driver lines: poly x 2094 north to y 4958, west to
  a pad (1978,4957), metal x 1980 north to a pad (1979,4200), poly east and north along x 2137 to
  y 3200, west to a pad (2068,3200), metal x 2064 north to a pad (2064,2507) on the west end of
  the north-edge poly, which turns north out of the strip at (2380,2498). No uncertain item on it.
  Since `tl1_w5936` = NOT `tl2_w6070` (`tl2`'s upper inverter), **the third latch's buffered output
  leaves the strip northwards**. Logic, "`tl1_w5936`: up the west margin".
- **The inverter's gate in cell `tl1_ua` is about 21 px long, not 12** (re-read item R35, raised by
  `tl4` on its copy): `P 2651,4388:2672,4470`. The three inverters here (and every copy of the
  cell elsewhere) are 37/21. Logic, "The inverter's gate length". Sizes only.
- Thin metal W: one more measurement (Not done); still not decided, nothing drawn.

Earlier status (2026-11-17, dp111):

2026-11-17 22:03 +0000. **Partial.** Twelve gates with their loads (39 transistors), the vertical metals of the
tracks x 2283, 2326, 2370, 2414, 2457, 2500 with their pads and rows (y 2790-5480 and
y 5900-6350), the three pieces of the thin metal x 2557-2573 over the west column, the three
pieces of the thin metal x 2742, the rails R1 and R2 from y 5320 to the strip's south edge, and
one long wire down the west side (`tl4_w4068`) are
traced and extract with 0 errors and 0 warnings in the full extraction. **The west column
is traced from y 3558 to y 5000** (above and below it is `tla`'s) **and from y 5690 to
y 6175** (the small cluster's west half). Main results: **the
driver of `rcs_e4` is found**, a wide two-input NOR at y 4778-5000; **its first input
`tl1_w4678` is one side of a cross-coupled pair of gates** (y 4340-4800: a latch that is
open while `tl1_w3594` is high and then takes `tl1_w4243`, with `rcs_x1` forcing it
low); **the column y 3732-4215 is a copy of y 4340-4800**, 608 px higher, a second latch
of the same build (open while `tl1_w3636` is high, data `rcs_mn3852`), whose output through
the inverter `tl1_w4243` is the first latch's data. `tl1_w3636` = NOR(`tl1_w3594`,
`tl4_w4590`), so the two are never open together: a master and slave. **The west half of the
small cluster (y 5690-6175) is a third copy of the same pair of units**, 1345 px below the
master: a latch that is open while `ck_out` is high, takes `tl4_w4068` (the long wire from
the top of the strip), is cleared by `tl1_w5978`, and sends its output `tl1_w6022` east
along y 6195 out of the strip. **North of y 2790 there is only wiring**, now drawn: the rest
of `rcs_c1`'s poly line (west, north and out of the strip at (2413,2500)), two rows from the
north (`tl1_w2637`, `sl_eq_r5_n`), `tl4_w4068`'s row to its pad (2826,2553), R1 up to the
strip's north edge and a second wide metal x 2733-2785, which is VSS (a leg of the same plane as R1). Thin metal W is not decided and
not drawn; the wiring west of x 2260 below y 2600 is surveyed only: see Not done.

```
rcs_e4    = NOR(tl1_w4678, tl1_w4937)     (2607,4852), (2607,4936)   marked: only the load's tie is uncertain
tl1_w3636 = NOR(tl1_w3594, tl4_w4590)     (2570,3592), (2570,3678)   firm
tl1_w4243 = NOT tl1_w4287                 (2626,4284)                marked: only the load's tie is uncertain
second latch (y 4340-4800):
tl1_w4360 = NOT tl1_w4243                                            (2660,4422)   firm
tl1_w4703 = NOT(tl1_w4243 AND tl1_w3594 OR tl1_w4678)                (2614,4461), (2614,4501), (2631,4575)   marked: the ties of the two loads
tl1_w4678 = NOT(rcs_x1 OR tl1_w3594 AND tl1_w4360 OR tl1_w4703)   (2570,4634), (2618,4715), (2618,4761), (2722,4755)   marked: the ties of the two loads
first latch (y 3732-4215, the copy):
tl1_w3752 = NOT rcs_mn3852                                            (2660,3814)   firm
tl1_w4287 = NOT(rcs_mn3852 AND tl1_w3636 OR tl1_w4070)                (2614,3853), (2614,3893), (2631,3967)   marked likewise; = tl1_w4095 by an alias
tl1_w4070 = NOT(rcs_x1 OR tl1_w3636 AND tl1_w3752 OR tl1_w4287)   (2570,4026), (2618,4107), (2618,4153), (2722,4147)   marked likewise
third latch (y 5690-6175, the second copy, in the small cluster):
tl1_w5706 = NOT tl4_w4068                                            (2657,5766)   firm
tl1_w5841 = NOT(tl4_w4068 AND ck_out OR tl1_w6022)                   (2614,5806), (2614,5846), (2631,5920)   marked likewise
tl1_w6022 = NOT(tl1_w5978 OR ck_out AND tl1_w5706 OR tl1_w5841)      (2570,5979), (2618,6060), (2618,6106), (2722,6100)   marked likewise
```

(`tools/unsure.py --equations`: `tl1_w3636`, `tl1_w4360`, `tl1_w3752`, `tl1_w5706` FIRM; the others DEPEND
on the `?` ties of load gates. Every pull-down and every other join is drawn without `?`.
**What the `?` ties carry here is more than in a plain gate**: each latch gate's plate is
also the wire that takes its output to the other gate of the pair, so without the ties the
cross-coupling is not in the netlist. That a load's plate is on its own output is how the
logic family works; where exactly each tie sits is what is uncertain.)

## Inventory (survey of the strip, 0.88x, `sv0.png`-`sv2.png`; details 2.6-2.7x `b1`-`b3`)

**findcell** (clean shot, region 2440-2850 x 2500-6350) with `tla`'s units as masters:

| Master (`tla`) | Hits in the strip |
|---|---|
| NOR unit of `rcs_in2`, 2535-2790 x 5120-5290 | **(-1,-1562), score 0.92**: the unit at y 3558-3728. Next best 0.53 |
| inverter `tla_w3505`, 2535-2790 x 3170-3290 | **(0,+1041), score 0.93**: the unit at y 4211-4331; (+1,+1822) 0.93 is `rcs_w2`'s inverter, already traced |
| selector `tla_w3417`, 2535-2790 x 3290-3550 | none above 0.55 |
| top unit, 2535-2790 x 3040-3170; `rcs_w2`'s unit 2535-2790 x 5030-5125 | none above 0.53 |

So only two of the units are copies of `tla`'s; the rest of the column is of the non-standard
kind (wide diffusions under R1 with several gates across), traced as the cells `tl1_ua` and
`tl1_ub`, each placed twice.

**West column** (units between R1's VSS boxes, x 2540-2835), north to south:

| y | What | State |
|---|---|---|
| 2940-3590 | top unit, inverter, selector | `tla` |
| 3558-3742 | NOR, a copy of `rcs_in2`'s unit | **traced**: `tl1_w3636` |
| 3732-3982 | **a copy of the unit at y 4340-4590** (findcell, clean shot: 2535-2790 x 4345-4585 recurs at 0,-608, score 0.93): an inverter (`tl1_w3752`) and a three-input gate (`tl1_w4287`), cell `tl1_ua` | **traced** |
| 3982-4215 | **a copy of the unit at y 4590-4800** (findcell: 2535-2790 x 4590-4780 recurs at 0,-608, score 0.94) | **traced** (`tl1_w4070`), with its load |
| 4215-4345 | inverter (rail gate), a copy of `tla_w3505`'s | **traced**: `tl1_w4243` |
| 4340-4590 | an inverter (`tl1_w4360`: pull-down on a vertical poly at the rail's east edge, y 4403-4440; load plate in the open x 2722-2775, y 4352-4460) and a three-input gate (`tl1_w4703`: two series gates and a third gate under R1; load plate under the thin metal x 2742, y 4487-4568), cell `tl1_ua` | **traced** |
| 4590-4800 | VSS box, a column west of R1 with `rcs_x1`'s gate, the node with a buried contact to `tl1_w4678`'s row, under R1 two gates in series (`tl1_w3594`, `tl1_w4360`) down to the VSS box of the wide NOR; east of R1 the node's strip under thin metal W, a third pull-down (`tl1_w4703`) at its south end and the load at its north end | **traced**: the node is `tl1_w4678` |
| 4778-5000 | wide NOR | **traced**: drives `rcs_e4` |
| 5000-5330 | `rcs_w2`, `rcs_in2` | `tla` |

**Tracks west of the column** (metal runs across x 2090-2460 at 30 heights, both chips;
`tools/tla_tracks.py`, `tools/follow.py`). Nine tracks at 43 px pitch:

| Track x | Pieces |
|---|---|
| 2110, 2153 | `ma1_drv_in`, `ma0_drv_in` (`mal`), full height |
| 2199 | **north piece `tl4_w4068`**: from a pad (2563,2550) west along y 2553, corner (2199,2556), south to a contact (2197,3333). South of y 3371: `tla_w3376` (`tla`) |
| 2239 | `amr_eq_r3` (`tla`), y 3449-5646 |
| 2283 | y 2721-3126 and y 3188-3520 (`tla`); **y 3622-4126 `tl1_w3636`**; **y 4230-4474 `tl1_w4243`**; south of y 4914 `ma4_drv_in` (`mal`) |
| 2326 | `rcs_thin_e` y 2754-3347, `tla_w3417` y 3404-5551 (`tla`); **from a pad (2326,5978) south out of the strip: `tl1_w5978`**. The poly that lies under it y 4533-4988 is **`tl4_w4068`** (below) |
| 2370 | **y 2843-3863 `rcs_mn3852`**; **y 3925-4300 `tl1_w4287`**; **y 4925-5459 and east to (2521,5459) `tl1_w4937`**; from (2365,5847) south it is `ck_out`'s trunk (`tla`), with **a second contact (2372,6061)** found here |
| 2414 | `rcs_c1` y 2972-5082, `rcs_in2` y 5182-5411 (`tla`); **y 6010-6207 `tl1_w6022`**; `lc_step` from (2412,6278) (`ur`) |
| 2457 | **y 2800-3690 `tl4_w4590`**; **y 4012-5372 and east to (2521,5372) `rcs_x1`**; `clk_tl` from (2458,5587) (`tla`) |
| 2500 | **y 2886-4730 `tl1_w3594`**; **y 4882-5232 `rcs_e4`**, continuing as `tla`'s metal round to bus line C; **y 5924-6252 `tl1_w5936`** |

**North of y 2790** (traced: wiring only; `n3.png` 1.75x, `n4.png`-`n11.png` 2.2-4x, overlay
`n12.png`). No diffusion, no transistor: the plain olive areas are field. See Logic, "North
of y 2790".

**South of y 5640: the small cluster's west half** (traced; `sc0.png` 1.1x, `sc1.png` 2x,
`sc2*.png` 4x in four shots). Under the same rails (R1, thin W, R2 all run on south over the
foot and the small cluster and out of the strip at y 6350: `sc7.png`, `sc8.png`):

| y | What | State |
|---|---|---|
| 5330-5650 | the foot: poly rows only, under the rails (`tla`'s and this package's rows) | rails drawn |
| 5690-5935 | **a copy of the unit at y 4345-4590** (cell `tl1_ua`; findcell, clean shot: 0,+1345, score 0.91): inverter `tl1_w5706`, three-input gate `tl1_w5841` | **traced** |
| 5935-6175 | **a copy of the unit at y 4590-4800** (cell `tl1_ub`; findcell 1,+1344, score 0.94), with a VSS box of its own below (y 6123-6168, contact (2622,6145)): `tl1_w6022` | **traced** |
| 6183-6292 | three poly rows straight east under the rails: y 6186-6204 (`tl1_w6022`), y 6228-6246 (`tl1_w5936`), y 6272-6292 (`lc_step`, `ur`'s) | drawn to x 2817 |

findcell with `tla`'s five units and the wide NOR as masters finds nothing above 0.56 in
x 2440-2850, y 5600-6350. A VCC box under R2 at (2785-2835, 6065-6130) with a contact
(2805,6095) is closed towards the west (field between it and the pad (2742,6048)); a poly
leaves it east at y 6085-6110: an east load's, not drawn (Not done).

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
output of the unit above (low when `rcs_x1` is high, or `tl1_w3594` and `tl1_w4360` are
both high, or `tl1_w4703` is high), so
`rcs_e4 = (rcs_x1 OR tl1_w3594 AND tl1_w4360 OR tl1_w4703) AND NOT tl1_w4937`;
what those inputs are is not known.

### The unit that drives `tl1_w4678` (y 4590-4800) and its copy (y 3982-4215): traced

```
tl1_w4678 = NOT( rcs_x1  OR  tl1_w3594 AND tl1_w4360  OR  tl1_w4703 )
tl1_w4070 = NOT( rcs_x1  OR  tl1_w3636 AND tl1_w3752  OR  tl1_w4095 )      (the copy)
```

**The question left by the first round** (is the tan rectangle at the east end of
`tl1_w4678`'s row a buried contact, or does `rcs_x1`'s row make a pass transistor there?)
**is decided: both features are there, and the transistor is a pull-down to VSS.**
What lies under the thin metal x 2557-2573 is a column of diffusion like the NOR units'
column, x 2553-2588:

- Profile down x 2563 in four shots (`tools/px.py col 2563 4525 4700 3 all`), clean shot:
  pink = field y 4567-4591 (188/121/128); a dark edge at y 4594-4597 in all four shots; tan
  y 4600-4618 (195/175/140); the salmon row of `rcs_x1` y 4624-4642 (240/170/126); tan
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
  over red). `rcs_x1`'s row runs on over it to x 2598 and ends at the VSS box's edge.
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
along y 4353-4372, under R1 over field (pink above and below it there), through the gap
(where the gap's outline makes a ring on it at x 2660-2680), onto the output node of the
inverter of the unit above (next section): `tl1_w4360` = NOT `tl1_w4243`.

**The copy.** `tools/findcell.py 2535 4590 2790 4780` (clean shot) finds the unit again at
0,-608 with score 0.94, and the unit above it (2535-2790 x 4345-4585) at 0,-608 with 0.93. The
geometry is a cell (`tl1_ub`) placed twice; the overlay of the copy was checked on `o7.png`
(2.9x, clean shot and metal): VSS box with a contact (2620,4002), arm, `rcs_x1`'s row
y 4017-4036 (from the pad (2458,4026)), the box (2551-2575, 4055-4084), the two gates
(`tl1_w3636`'s row y 4104-4122 from the pad (2283,4113); the pad with a contact (2555,4159)),
the VSS box below with its own contact (2622,4188). Differences from the master, both at the
edges: the copy's stack ends on a VSS box of its own; and the poly on the copy's box is a
**stub** that ends in a round end at x 2532 (`q5.png`, 5x, three shots), where the master's
is the row of `tl1_w4678` going west. The copy's node `tl1_w4070` leaves by its load's plate only (to the
third gate of the unit above, as the master's also does). The north piece of the thin metal
(`tl1_w3752`, follow.py (2563,3756)-(2566,4172)) joins the pad (2562,3753), whose poly goes
east under R1 to a box (2660-2680, 3744-3764) (`q2.png`, 6x), and the pad (2555,4159).

**East of R1: a third pull-down and the load (third pass, 2026-11-17).** Read on both
copies singly, in four shots (`g1_*.png` 3.3x master and copy side by side, `g2_m_a.png`,
`g2_m_m.png`, `g2_c_a.png`, `g2_c_m.png` 5.5x, `g3_*.png` 4.3x, `g6_*.png` 4.55x side by side,
`g7_cvcc.png`; overlays `h1_m.png`, `h1_c.png`) and by profiles. The two earlier passes took
the transistor east of thin W for the load; it is a pull-down, and the load is at the
north end of the node's strip. Master coordinates; the copy is 608 px higher and agrees in
every item.

- **The node's strip.** From the box under thin W (x 2683-2716, y 4651-4697) a strip
  x 2697-2716 runs north to y 4622 and south to y 4734. `tools/px.py col 2706 4610 4802 4`
  (clean shot): tan without a break from y 4630 to y 4738 (172-204/151-181/111-139), the
  band y 4750-4762 (241-249/148-167/113-124: poly over a channel), tan again y 4774-4790,
  pink from y 4802. The copy (col 2706, y 4002-4194) reads the same.
- **The third pull-down, gate `tl1_w4703` (copy: `tl1_w4095`).** South of y 4734 the strip
  widens to x 2700-2743 (the inner outline curves from (2720,4725) to (2745,4735) in the
  chip-1 metal shot, plain ground inside; its east edge is the line x 2741-2745 that
  crosses the band) and the band y 4744-4766 crosses it: W/L about 43/22. The band is one
  poly with the pad (2742,4703) of the thin metal x 2742: pad (2725-2772, 4683-4724), a
  stem down the east side (x 2750-2772) and the band west to a rounded end at x 2682 under
  thin W (orange-brown without a break in the chip-1 metal shot, `g2_c_m.png`: the copy
  shows it best). The pad's top edge is closed (rounded corner (2772,4682)), with field
  between it and the plate (pink y 4668-4683 at x 2748; green in the chip-2 stripped shot).
  The band is not gate 2's poly (which ends at x 2670: review).
- **South of the band: VSS.** The diffusion ends in the heavy U outline at y 4797 and runs
  west along y 4782-4796, under thin W and through the gap, onto the rail's VSS box (the
  wide NOR's box (2600-2662, 4778-4845) in the master; the copy's own box (2600-2655,
  4170-4215)). `tools/textmap.py 2644 4764 2716 4804 2 --acid`: the chip-2 stripped shot is
  red over green without a break from x 2660 to x 2702 on rows y 4784-4794 and green
  (field) on rows y 4770-4780 and from y 4798; column x 2674 (in the gap) has the strip
  between dark edges at y 4784-4792 in the master and y 4177-4186 in the copy, like the
  node's strip at y 4680-4690. East of the U, x 2752-2768 is field in both stripped shots
  (row y 4786: khaki 160/145/100, red minus green 0 in the chip-2 shot): it does not reach
  the VCC box under R2. The earlier "salmon box that looks like a buried contact"
  (2718-2742, 4773-4800) is the part of this diffusion that thin W did not protect.
- **The load.** A plate x 2722-2772, y 4587-4666 under the thin metal x 2742 (three salmon
  bars with single edge lines between them at y 4618 and y 4650, which are the edges of the
  strip beneath, as in `tla`'s `rcs_in3` load). `tools/px.py col 2748 4584 4700 3`: the
  middle bar y 4623-4647 is 232-241/158-178/111-125 (row y 4635: up to 254/179/133), the
  colour of poly over a channel; the bars above and below are 212-223/153-166/107-124 and
  187-188/121-136/105-111, poly over field. The strip y 4622-4648 runs from the north end
  of the node's strip (tan at x 2696-2716 in row y 4635) to the VCC box under R2 (x 2778-2838,
  y 4525-4648, one box with one long contact ring y 4545-4640; `tla`'s box (2778-2842,
  4588-4627) with its contact (2812,4615) is its middle; the copy's box (to y 4042) has its
  own elongated contact ring (2793-2817, 3972-4022), drawn here, and is one with `tla`'s box
  (2785-2842, 3848-3925) above it). W/L about 26/50.
- **The tie (`?`).** The plate's top bar runs on west under thin W to x 2678, where a poly
  comes down into it from the third gate of the unit above (next section) (row y 4600:
  214-225/163-172/112-119 from x 2680 to x 2712, poly over field; dark red where neither
  thin metal protected it, x 2716-2728). Below its west end, beside the top of the node's
  strip, a box with a heavy outline (2673-2697, 4622-4648) in all four shots, in both
  copies; both metal shots are dark over it for 35 px (y 4612-4646), which is what a
  buried contact under a thin metal does (tracing guide, trap 22). Taken as the tie of the
  plate to the node (a tab down from the bar, the strip's top widened west, a buried
  contact). Not resolved at any zoom: drawn `?`, as the ties of the other loads here. The clean shot shows a green-yellow centre
  in the box (`w4_all.png`, 6.5x, both copies), which a buried contact under metal should
  not have: see Not done, thin metal W.
- **Thin metal W over the node**: W is bright and wide (x 2684-2704) over the node's box,
  y 4665-4692, with no ring in either metal shot and no green hole in the clean shot, in
  either copy. Not a contact by the tests of trap 22; nothing drawn. `tla`'s north piece
  of W "ends" at y 4002 exactly where the copy's dark stretch over the tie box begins
  (y 4006-4039): the follower's stop, not shown to be the metal's end (Not done).
- The copy's output: the poly on the copy's node box is a stub; `tl1_w4070` leaves by its
  plate's top bar to the third gate of the unit above (next section), as `tl1_w4678` does
  besides its row to the west.
- A second VCC box under R2 in the copy only, (2785-2832, 4062-4118) with a contact
  (2805,4090), closed towards the west (pink between it and the pad (2742,4095)): not part
  of this unit (an east load's, `tla`'s side); the master has field there. Not drawn.

### The unit at y 4340-4590 and its copy at y 3732-3982 (cell `tl1_ua`): traced

```
tl1_w4360 = NOT tl1_w4243                               copy: tl1_w3752 = NOT rcs_mn3852
tl1_w4703 = NOT( tl1_w4243 AND tl1_w3594  OR  tl1_w4678 )
                                copy: tl1_w4287 = NOT( rcs_mn3852 AND tl1_w3636  OR  tl1_w4070 )
```

Views: `u1_a.png`, `u1_m1.png` (4.1x, clean shot and chip-1 metal), `u2_a.png`, `u2_m.png`
(6x, four shots, y 4500-4608), `u3_a.png`, `u3_a2.png` (6x, both stripped shots, y 4338-4488),
`u4_all.png` (the west box, master and copy, three shots, 6.5x); overlays `v1_m.png`,
`v1_c.png` (4.1x, each copy singly). Master coordinates; the copy agrees item by item.

**The inverter (y 4345-4460).**
- Pull-down: the row y 4452-4470 (`tl1_w4243`, from the pad (2283,4462)) turns north at the
  rail's east edge as a vertical poly x 2651-2672 (run 5; first drawn 2653-2668) and crosses the diffusion between the
  rail's VSS box (2600-2650, 4403-4447, contact (2620,4420)) and the part under thin W.
  `tools/px.py col 2658 4376 4480 3`: one salmon band from y 4391 to y 4466 with two single
  edge lines (y 4400-4403, y 4439-4442: the diffusion's edges) and no field between; between
  the lines it is 245-254/177-187/120-132, poly over a channel, outside them 220-227/152-176,
  poly over field; the copy reads the same. Its top is a free rounded cap (y 4388). W/L 37/21
  (run 5: "The inverter's gate length" below; it was 37/15 as first drawn and 37/12 after a review).
- Node: tan under thin W, x 2672-2716, y 4403-4440 (row y 4422), and a column x 2690-2716
  north to y 4350.
- Output and tie: the row y 4353-4372 of the pad (2562,4361) (the thin metal x 2557-2573,
  `tl1_w4360`) lies on the column's top in a box with a heavy arch (2688-2720, 4350-4374):
  `tools/px.py col 2704 4338 4412 3` is tan (187-199/157-172/131-135), not salmon, on the
  rows where the poly is, in both copies: a buried contact. Drawn firm: the poly lies on the
  end of the diffusion (no diffusion north of it), which cannot be a gate.
- Load: the row runs on east into the stem (x 2722-2745, y 4352-4400) of a plate x 2722-2775,
  y 4395-4460 in the open (one orange L with one outline in the chip-2 stripped shot,
  `u3_a2.png`); the strip y 4412-4440 (two edge lines across the plate) runs to a VCC box of
  its own under R2 (2778-2834, 4410-4480; elongated contact ring about (2803,4447)).
  W/L 28/53.

**The three-input gate (y 4428-4595).**
- `tools/railprof.py 2604 2646 4380 4600`: diffusion y 4411-4450 (the VSS box), gate
  y 4451-4475 (`tl1_w4243`'s row), diffusion, gate y 4495-4519 (`tl1_w3594`'s row, from the
  pad (2499,4503)), diffusion y 4520-4566 (the node), gate y 4567-4590, diffusion (the VSS
  box of the unit below, contact (2628,4610)). The copy (`3772 3992`): the same, 608 higher.
- The node: under R1 (y 4520-4562); west of the rail to a buried contact (heavy box
  2552-2575, 4533-4560) with a poly on it, which in the master is a stub with a rounded end
  at x 2532 and in the copy is the row of `tl1_w4287` (y 3929-3949) from the pad (2372,3938);
  east through the gap and under thin W (`tools/textmap.py 2644 4512 2716 4566 2 --acid`:
  red over green without a break from x 2664 to x 2702 on rows y 4530-4554) and as a strip
  y 4527-4553 under the plate to the VCC box under R2 (the upper part, y 4525-4570, of the
  box that the unit below also uses; one long contact ring y 4545-4640).
- Load plate x 2722-2772, y 4487-4568, under the thin metal x 2742, whose top pad
  (2742,4496) is on the plate's top bar: `tools/px.py col 2748 4474 4592 3` gives the bar
  y 4489-4519, the bright bar over the channel y 4531-4549 (237-241/133-174/121-127) and a
  thin bottom bar y 4561-4567; pink field from y 4573. So **the thin metal x 2742 carries
  this gate's plate to the third pull-down of the unit below**. W/L 26/50.
- The tie (`?`): the top bar runs west under thin W to x 2683 (`px.py col 2695`: salmon
  y 4486-4495); below it a box with a heavy outline (2683-2708, 4500-4524), tan inside
  (y 4510-4519), on a tail of the node (tan again y 4525-4549). Drawn as a tab, a tail and
  a buried contact, all `?`.
- **The third gate (y 4565-4585) is the plate of the unit below.** Its poly has a rounded
  west end at x 2608 inside the rail, crosses the gap east of the rail and turns south at
  x 2680-2693 into the top bar of the plate of `tl1_w4678` (y 4587-4612).
  `tools/px.py col 2687 4552 4626 3`: salmon without a break from y 4567 to y 4609
  (217-230/147-168/105-121) in the master and from y 3959 to y 4001 in the copy. The gap:
  `tools/px.py row 4575 2650 2700 3 metal,metal1` is orange-brown at x 2665-2680 in both
  metal shots (155-165/102-124/51-61 and 135-144/71-87/38-48), where the same row through
  gate 2 of the unit below (y 4760, a known poly end) is plain ground (138-144/122-141/71-78);
  the copy (row y 3967) is orange-brown likewise. W/L 42/20.

**The pair.** Each of the two gates has the other's output on a pull-down: `tl1_w4703`
through the thin metal x 2742 onto the gate east of thin W in the unit below, `tl1_w4678`
through its plate's top bar onto the third gate here. With `tl1_w4360` = NOT `tl1_w4243`:

```
tl1_w4703 = NOT( tl1_w3594 AND tl1_w4243      OR  tl1_w4678 )
tl1_w4678 = NOT( tl1_w3594 AND NOT tl1_w4243  OR  tl1_w4703  OR  rcs_x1 )
```

While `tl1_w3594` is high, `tl1_w4678` follows `tl1_w4243` and `tl1_w4703` is its inverse;
while it is low the pair holds; `rcs_x1` high forces `tl1_w4678` low. The copy is the
same with `tl1_w3636` for `tl1_w3594`, `rcs_mn3852` for `tl1_w4243`, and its inverse output
`tl1_w4287` goes through the inverter at y 4215-4345 to be this pair's data: `tl1_w4243`
is the copy's `tl1_w4070` again. Since `tl1_w3636` = NOR(`tl1_w3594`, `tl4_w4590`), the first
latch is open only while `tl1_w3594` and `tl4_w4590` are both low and the second while
`tl1_w3594` is high: **`tl1_w4678` is `rcs_mn3852` taken through two latches in turn, with
`rcs_x1` clearing both** (traced, marked by the four `?` ties), and
`rcs_e4` = NOT `tl1_w4678` AND NOT `tl1_w4937`. What `rcs_mn3852`, `tl1_w3594`, `tl4_w4590`,
`rcs_x1`, `tl1_w4937` are is not known: all five come from the east on poly rows.

**`tl1_w4287` and `tl1_w4095` are one net in the drawing** (the copy's node has the row of
`tl1_w4287` on its west box and its plate carries the thin metal `tl1_w4095`), but only
through the `?` tie of the plate: an assumption, recorded as `@alias tl1_w4287 tl1_w4095`;
the names are not merged.

### The thin metal x 2742 (two pieces): traced

`tl1_w4703`: (2742,4496)-(2742,4703); `tl1_w4095`: (2742,3888)-(2742,4095) (follow.py:
(2740,4496)-(2741,4706), (2741,3890)-(2741,4100)). All four ends are contacts on poly pads
(mosaic at 3.9x in the metal shot and the clean shot, `m2_metal.png`, `m2_acid1b.png`: ring
with a bright centre, green centre on a salmon pad). The top pad is on the top bar of the
load plate of the three-input gate of `tl1_ua`, the bottom pad's poly is the gate of the
third pull-down of `tl1_ub`.

### The NOR at y 3558-3742: traced (a copy)

```
tl1_w3636 = NOR(tl1_w3594, tl4_w4590)
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
under R1 there: gate 2 of the three-input gate at y 3884-3904 (the first latch's enable)
and the series gate of `tl1_w4070` at y 4104-4122.

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
  ends on the buried contact (2550-2577, 3923-3954) on the node of the three-input gate of
  the copy of `tl1_ua`: `tl1_w4287` = NOT(`rcs_mn3852` AND `tl1_w3636` OR `tl1_w4070`).
- Output: metal x 2283, y 4230-4474, to a pad (2283,4462) whose row y 4452-4470 runs east
  across the stack of `tl1_ua` (gate 1 of the three-input gate) and north at the rail's edge
  as the inverter's gate (`tl1_w4360`).

### The third latch: the small cluster's west half (y 5690-6175): traced (a copy)

```
tl1_w5706 = NOT tl4_w4068                                          firm
tl1_w5841 = NOT( tl4_w4068 AND ck_out  OR  tl1_w6022 )             marked (the tie of its load)
tl1_w6022 = NOT( tl1_w5978  OR  ck_out AND tl1_w5706  OR  tl1_w5841 )   marked (likewise)
```

The cells `tl1_ua` and `tl1_ub` placed at (0,+1345). Evidence that it is a copy:
`tools/findcell.py` on the clean shot (scores in the Inventory); `tools/railprof.py 2604 2646
5650 6350` gives VSS box y 5756-5790, gate y 5797-5811, diffusion, gate y 5840-5854, node
y 5863-5910, gate y 5911-5924, VSS box, gate y 6049-6063, diffusion, gate y 6097-6113, VSS box
y 6124-6175: the master's stack 1345 lower; overlays of the placed cells on four shots at 4x
(`sc3Aa/m`, `sc3Ba/m`, `sc3Ca/m.png`) and with the rest at 2x (`sc12.png`); `tools/cellcheck.py`
(median ncc 0.95-0.97 clean shot, 0.94-0.95 metal, both cells). What goes where:

| Master's net | Here | How it arrives |
|---|---|---|
| `tl1_w4243` (data: gate 1 of the three-input gate, and the inverter's gate) | **`tl4_w4068`** | the row y 5793-5810 from the long wire down the west side |
| `tl1_w3594` (enable: gate 2 of the three-input gate; series gate of the lower unit) | **`ck_out`** | `tla`'s row y 5839-5859 from the trunk contact (2365,5847), and the row y 6054-6072 from the second trunk contact (2372,6061) |
| `rcs_x1` (clear: the pull-down west of the rail) | **`tl1_w5978`** | the row y 5969-5987 from the pad (2326,5978) |
| `tl1_w4678` (output, on the buried contact of the node's west box) | **`tl1_w6022`** | the row y 6013-6031 to the pad (2414,6022) |
| `tl1_w4360` (inverter's output, thin metal x 2557-2573) | **`tl1_w5706`** | follow.py: one metal (2563,5708)-(2568,6124), pad with a contact (2562,5706) to the pad (2555,6112) |
| `tl1_w4703` (other side, thin metal x 2742) | **`tl1_w5841`** | follow.py: (2740,5842)-(2742,6052); contacts (2742,5841) and (2742,6048) |

So the latch is **open while `ck_out` is high** (CLK low) and then `tl1_w6022` = `tl4_w4068`
AND NOT `tl1_w5978`; while `ck_out` is low it holds; `tl1_w5978` high forces `tl1_w6022` low.
Its output goes by the metal x 2414 (y 6010-6207) to the row y 6186-6204, which runs east
under R1, thin W and R2 and out of the strip (`sc11.png`, 2.9x, both stripped shots: straight,
no pad). Like the other two latches it is **marked**: the cross-coupling runs through the
`?` ties of the two load plates.

Read at the copy's edges, where a copy can differ:
- **`ck_out`'s row ends at the rail's east edge** (x about 2658), as the master's enable row
  does. `tla` had drawn it on to x 2735 and onto the pad (2745,5842), which would have put
  `ck_out` on the load plate of `tl1_w5841`. `tools/px.py row 5839|5843|5849 2646 2702 3
  metal,metal1,acid`: at x 2667-2676 (the gap between R1 and thin W) both metal shots are plain
  ground (148-161/109-148/75-81) and the chip-2 stripped shot is field-coloured (147/147/90),
  the same numbers as the master's rows y 4494-4504; mosaic of the three copies in four shots,
  `sc4.png`. Corrected in `trace/tla.txt` (commit ee9c0d0).
- The poly on the west box of the upper unit's node (2552-2575, 5878-5905) is a **stub** with a
  rounded end at x 2535, as in the master (`sc5.png`, 4x, three shots).
- The stack ends on a **VSS box of its own** (tan x 2600-2650, y 6123-6168, contact
  (2622,6145): ring in both metal shots, speck in the clean shot; `sc6.png`). R1 does not end
  there (it looks so at 4x because the contact's ring is at its edge): it runs on south.
- The VCC box of the two loads (x 2778-2838, y 5870-5993) has one elongated contact ring
  (x 2790-2815, y 5885-5985), drawn as one contact (2803,5935).
- **Thin metal W over the lower unit's tie box** (y 5952-5992): dark, as over the other two
  copies' (Not done, thin metal W). What the earlier survey took for W's south end is this.

### The tracks beside the small cluster (y 5900-6350): traced (wiring only)

`s1.png` (2.05x, metal and clean shot), overlay `o3.png`.

- **`ck_out` has a second contact on its trunk metal x 2370**, at (2372,6061), 214 px below
  `tla`'s (2365,5847): ring on the line in the metal shot, pad with a green centre in the
  clean shot. Its poly row runs east along y 6054-6072: the series gate of the third latch's
  lower unit.
- `tl1_w5978`: pad (2326,5978), row east y 5969-5987 (the third latch's clear); the metal
  x 2326 goes south out of the strip (not followed).
- `tl1_w6022` (the third latch's output): metal x 2414, y 6010-6207, joins two rows:
  y 6013-6031 (from the latch) and y 6186-6204 (east out of the strip).
- `tl1_w5936`: metal x 2500, y 5924-6252. The top pad's row runs **west** along y 5926-5944
  under all the tracks to a corner at (2094,5935) and turns north beside MA1's metal
  (`s2.png`; followed in run 5: "`tl1_w5936`: up the west margin"); nothing leaves the pad
  eastwards (`sc5.png`). The
  bottom pad's row runs east along y 6228-6246, under the rails and out of the strip
  (`sc11.png`). It only passes the small cluster.

### North of y 2790: wiring (traced)

Views: `n3.png` (1.75x, clean shot and metal), `n4.png` (2.7x, both stripped shots: the L's),
`n5.png` (3x, three shots: the rows under the two wide metals), `n6.png` (4x: the corner under
`tla`'s metal), `n7.png` and `n10.png` (3.4-3.6x: the pads at the east edge), `n8.png` (2.9x:
the lower corner), `n9.png` (2.2x: the rails), `n11.png` (3x: the north-west corner); overlay
`n12.png` (2x, chip-2 stripped shot).

- **`rcs_c1`'s poly line** (`tla` drew it from x 2330 east; its notes' Not done): it runs on
  west along y 2977-2995 to x 2258, north at x 2258-2274 to y 2713, east along y 2713-2728 to
  x 2420, and north at x 2405-2420 out of the strip at y 2500. Orange without a break in the
  chip-2 stripped shot. `tla`'s metal of `rcs_u3288` (y 2727, x 2283) lies half on it along
  both legs of the upper corner, with no pad and no ring, the metal evenly bright (`n6.png`):
  two nets (tracing guide, trap 13). It passes under the metals x 2283 and x 2326 at y 2986
  and under `tl4_w4068`'s metal at y 2553 without a pad. So `rcs_c1` = NOR(`rcs_a2`,
  `rcs_b1`) goes somewhere north of the strip.
- **Two nested L's**: polys from the north at x 2448-2463 and x 2493-2508 turn east into the
  rows y 2627-2645 (`tl1_w2637`) and y 2582-2600 (`sl_eq_r5_n`), which run under R1 and the
  second wide metal over field, without a pad. `tl1_w2637` ends on a pad with a contact
  (2827,2637) at the strip's east edge with a metal going on east along y 2630-2645;
  `sl_eq_r5_n` goes on to a pad with a contact at about (2867,2595), 50 px east of the strip
  (not drawn), also with a metal going east.
- **`tl4_w4068`'s row** (y 2543-2560) from its pad (2563,2550): east under R1 and the wide
  metal to a pad with a contact (2826,2553); a metal goes on east along y 2545-2562. So the
  third latch's data comes from the east along y 2553.
- **`tl4_w4590`'s row** (y 2803-2821) ends on a pad with a contact (2830,2811), a metal going
  on east along y 2803-2820 (`n10.png`). The rows of `rcs_mn3852` (y 2857) and `tl1_w3594`
  (y 2899) go on east as poly, the second under the wide metal's east arm.
- **R1** (x 2600-2650) is one rail from `tla`'s piece (y 3000) up to the strip's north edge;
  no contact under it here.
- **A second wide metal x 2733-2785 is VSS**: it and R1 are legs of one metal plane whose
  lower edge is at y ~2506 (review; `review4-1/k2.png`); from the north down to y 2955, where
  it turns east along y 2905-2955. It was first named `tl1_w2930` as a net of its own; both
  legs had been drawn to end at y 2500, 6 px short of the plane's edge.
- **The poly along the strip's north edge** (y 2498-2515; first given a name of its own): from a pad
  with a contact (2064,2507), 36 px west of the strip, east under the MA metals to a corner at
  x 2372-2388, where it turns north out of the strip. Run 5: the pad's metal is the north end of
  the wire up the west margin, so this poly is `tl1_w5936`.
- Not layout: a khaki blob with an outline at (2535-2562, 2650-2700) in the clean shot only
  (the chip-2 shots have a small dark mark at (2545,2680)); the dark dot (2628,2562) on R1 in
  the clean shot and (2628,2605) in the chip-2 metal shot (different places: dirt).

### `tl4_w4068`: a long wire from the top of the strip to the small cluster (traced, part `?`)

One net, about 4,700 px; its south end is the data input of the third latch (two gates:
(2657,5766) and (2614,5806)); at its north end it leaves the strip eastwards by a metal:

1. a pad with a contact (2826,2553) at the strip's east edge, from which a metal goes on
   east; its poly runs **west** along y 2543-2560 under the wide metal and R1 to a pad with
   a contact (2563,2550) (`n5.png`, `n7.png`);
2. metal west along y 2553 to a corner (2199,2556) and south at x 2199 to a contact
   (2197,3333) (`tools/follow.py`: one piece; overlay `o4.png`);
3. that contact's pad is a bulge on a vertical poly x 2170-2187 (free stub above it to y 3282,
   `w1.png` 3.1x, `r2.png`), which runs south to y 4550, east along y 4533-4550, **south under
   the metal x 2326** (the "poly of another net" of `tla`'s notes: no pad, no ring), west along
   y 4972-4988, south at x 2134-2149 to y 5810, and east along y 5793-5810 into the small
   cluster (`r1.png`), where it is gate 1 of the three-input gate under R1 and, turned north
   at the rail's east edge, the gate of the inverter (the third latch, above).

Evidence: the five corners at 2.3x (`r2.png`), the horizontal pieces and the piece under the
metal at 2.05-2.15x (`a4`, `a5`, `s3`, overlay `o5.png`). The three long stretches (x 2170-2187
y 3355-4535; x 2134-2150 y 4995-5795; the row y 5793-5810) were seen only in a 1.9x mosaic
(`v1.png`) and at 1.8x: they are alone in bare field, with nothing beside them to step onto,
but they are drawn `?P`, so the wire as one net is **marked**.

### `tl1_w5936`: up the west margin to the north edge (traced, run 5; no `?`)

The row y 5926-5944 from the top pad of the metal x 2500 was drawn to x 2110 with "a corner
and north, not followed", and a "second vertical poly x 2137-2147" stood in Not done. They are
two stretches of one wire, which ends on the west end of the poly along the strip's north
edge. South to north (views in `cache/scratch/tl1/`; the profiles are `tools/px.py`, clean shot
unless said):

| # | Stretch | Evidence |
|---|---|---|
| 1 | corner (2094,5935): the row's west end turns north | `w_h.png` 3.6x, three shots: the vertical comes down into the row; field west of x 2085 |
| 2 | poly x 2087-2100 north to y 4950, in the gap between `ma3_drv_in`'s metal (x 2061) and `ma1_drv_in`'s (x 2110) | `col 2093 4960 5946 6 acid1b,acid`: poly (R > 195, G > 135) at every sample except y 5182-5188 (a dot of dirt in the clean shot; the chip-2 values do not change there) and y 5240-5290, where dirt covers the west half (`col 2097 5176 5300 6`: 213-229 throughout); rows at y 5000, 5200, 5400, 5600, 5800, 5900: bright x 2088-2098 |
| 3 | corner, poly west along y 4950-4966 to a pad with a contact (1978,4957) | `w_d.png`, `w_d2.png` 3.4x, four shots: ring in chip 2's metal, pad x 1964-1998, y 4942-4973 with a green centre; `row 4958 1990 2106 4`: poly, dark only at the two gaps between the metals; no metal south of the pad |
| 4 | metal x 1980 (12 wide) north to a pad with a contact (1979,4200) | `tools/follow.py 1980 4230 S --trace`: `M 1980,4230 y4964 w=12`, one piece. Its one contact candidate, (1978,4722), is dirt: `w_g.png` 4x, four shots: the metal runs through, a dark mark on its east edge in chip 2, an arc of debris in chip 1, plain field under metal in the clean shot, nothing in the chip-2 stripped shot |
| 5 | poly east along y 4190-4206 under `ma2`, `ma3`, `ma1` to x 2144, corner, north along x 2129-2144 in the gap between `ma1_drv_in`'s metal and `ma0_drv_in`'s (x 2153) to y 3193 | `w_f.png` 3.6x three shots (pad: ring, green centre), `w_s.png` 2x; `row 4198 1990 2152 4`: poly, dark at the three gaps; `col 2137 3206 4204 6`: poly at every sample but one (dirt, about y 4130); rows at y 3300, 3600, 3900, 4150: bright x 2130-2142, edges 2128 and 2144. The corners lie in the gaps' open slivers, where the clean shot is dark: `col 2128 3176 3232 3 metal,acid,acid1b` and `col 2128 4170 4216 3`: poly-brown in chip 2's metal shot (about 145/95/45) from the bar into the vertical at both, the outer edge line at y 3188-3194 and y 4209-4212, field beyond |
| 6 | corner, poly west along y 3193-3208 to a pad with a contact (2068,3200) | `w_n.png` 3.4x, three shots: ring, green centre; one outline round bar and corner. `ma3_drv_in`'s metal ends 50 px lower, on its own contact (2063,3268) (`mal`) |
| 7 | metal x 2064 (12 wide) north to a pad with a contact (2064,2507) | `follow.py 2065 3180 N --trace`: `M 2064,3180 y2506 w=12`, one piece, no contact candidate |
| 8 | the pad is the west end of the north-edge poly (drawn before from x 2100) | `w_e.png` 3.6x: ring with a bright centre, pad x 2050-2088, y 2492-2520 with a green centre, poly east without a break (`row 2506 2084 2110 4`); no metal north of the pad |

Overlay `o_all.png` (3-3.6x, metal and clean shot at the four pads). Sweep of the margin
x 2040-2310, y 2480-6370 with `tl1`, `tla` and `mal` outlined on the clean shot (`w_sv.png`, 1x):
nothing else there is undrawn.

Before the rename the extraction reported one net at (2064,2854) carrying both names, the
row's and the north-edge poly's; no item on the path is uncertain (`tools/unsure.py` lists
nothing new), so the north-edge poly's name was merged into `tl1_w5936` with `tools/rename.py`
(glossary, Former names).

**Outside the strip.** The pads (2064,2507), (2068,3200), (1979,4200), (1978,4957), the two
metals and the poly west of x 2100 lie 0-140 px west of the strip's edge, among the MA driver
lines, where no package has drawn anything but those lines (`mal`). They are drawn here because
the wire begins and ends in this strip.

**What it is** (believed): the buffered output of the third latch (`tl1_w5936` = NOT `tl2_w6070`
= `tl1_w6022` again), taken round the whole first cluster to the band north of the strips. The
latch is open while `ck_out` is high and takes `tl4_w4068`.

### The inverter's gate length in `tl1_ua` (run 5; re-read item R35)

`tl4` found on its copy that the inverter's vertical gate is about 22 px long where the cell
had 12 (`P 2651,4388:2663,4470`, from a review that read the bright band of the clean shot).
At the master, `tools/tl1_band.py` (the mean over the band's rows, so that edge lines stand
out; R/G/B and red minus green):

| Rows | Clean shot | Chip-1 metal, x 2664-2672 | Chip-2 metal |
|---|---|---|---|
| the gate band, y 4408-4432 (`x 2642 2690 4408 4432 2`) | red outline x 2650-2654; bright 227-249/131-174 x 2654-2662; dark x 2666-2668; 118-143/73-87 x 2670-2674; 190/134 at x 2676, tan from x 2678 | 133-153/80-100/38-49, red minus green +45 to +54 | brown x 2662-2670, **dark 77-92 at x 2674-2678** |
| reference, the third gate's poly crossing the same gap over field, y 4568-4582 | - | 127-135/71-83/36-46, +52 to +57 | 151-157/111-124 at x 2666-2676: no dark line |
| reference, the node's diffusion crossing the gap with no poly, y 4530-4550 (and `tl1_ub`'s, y 4674-4694) | - | 137-146/103-110/63-72, +31 to +35 (109-116/82-87/56-59, +27 to +29) | 142-164/126-136 at x 2666-2676: no dark line |
| reference, field, y 4474-4488 | green (red minus green -3 to -34) x 2662-2682 | 118-137/103-123/64-77, +13 to +17 | 147-164/132-150: no dark line |
| the cap, y 4390-4398, and the row's east end, y 4455-4467 | salmon to x 2668 / 2664, green field from x 2672 / 2670 | - | dark 69-81 at x 2674-2676 (cap), 77 at x 2674-2676 (row end) |

So the gap x 2664-2672 on the gate's rows has the colour of poly in the chip-1 metal shot (as
on the third gate, unlike on both diffusion references), and an edge line at x 2674-2678 that
the reference rows do not have closes it in both metal shots, at the cap and at the row's end
as on the band. The dark line at x 2656-2660 of the metal shots is on every row, field
included: R1's edge, not a poly edge. The clean shot's bright band stops at x 2662 because
R1's protected margin stops there; in the gap it shows only the dark bar of trap 2. The gate is
x 2651 to about 2672-2675: drawn `P 2651,4388:2672,4470`, 37/21 (view `g_inv.png`, 6x, four
shots). Sizes only: `tools/sameconn.py` shows no connection changed by it.

## Ports

| Name | Layer | Where it crosses | Direction | What |
|---|---|---|---|---|
| `rcs_e4` | M | (2500,5232), onto `tla`'s metal | driven here | the long control line of the step logic |
| `tl1_w4937` | P | (2817,5460), east | into the block | gate 2 of `rcs_e4`'s NOR; row under the foot, on east past x 3400 |
| `rcs_x1` | P | (2817,5372), east | not known | row under the foot, on east past x 3400; on the same metal x 2457 the pads (2458,4026) and (2458,4635), each the gate of a pull-down (units at y 3982 and y 4590) |
| `rcs_mn3852` | P | (2817,2857), east | into the block (its other ends are gates) | row above the cluster; the data of the first latch (gate 1 of `tl1_w4287`, and the inverter `tl1_w3752`) |
| `tl4_w4590` | M | (2856,2811), east, from the pad (2830,2811) | into the block (a gate is its only other end) | gate 2 of the NOR |
| `tl1_w3594` | P | (2817,2899), east | into the block (its other ends are four gates) | gate 1 of the NOR `tl1_w3636`; the enable of the second latch (a series gate in each of its two gates) |
| `tl4_w4068` | M | (2852,2553), east, from the pad (2826,2553) | into the block (its other ends are two gates of the third latch) | long wire down the west side; the third latch's data |
| `rcs_c1` | P | (2405-2420,2500), north | driven in `tla` | `rcs_c1`'s poly line, on north: a gate of `eof`'s NOR `r5nor` (coordinator, 2026-11-19) |
| `tl1_w2637` | P, M | (2448-2463,2500) north; (2852,2637) east, from the pad (2827,2637) | driven from the north: the output of `eof`'s NOR `r5nor`, `tl1_w2637` = NOR(`tl1_w5936`, `rcs_c1`, `sl_eq_r5_n`) (coordinator, 2026-11-19) | passes: poly from the north, row y 2636, metal east |
| `sl_eq_r5_n` | P | (2493-2508,2500) north; (2817,2591) east | driven from the east (`eof`'s inverter on R5's match); its poly north ends as a gate of `eof`'s NOR `r5nor` (coordinator, 2026-11-19) | passes: poly from the north, row y 2591, on to a pad (2867,2595) |
| `tl1_w5936` | P | (2372-2388,2498) north | driven outside (`tl2`'s upper inverter, by the row y 6237) | the far end of the wire up the west margin: the north-edge poly turns north out of the strip |
| `vss` | M | (2600-2650,2500) north | - | R1, on north |
| `ck_out` | M, P | trunk contacts (2365,5847) (`tla`'s) and (2372,6061) | from `tla`'s trunk | the third latch's enable: two gate rows |
| `tl1_w5978` | M | (2326,6350) south | into the block (its other end is a gate) | the third latch's clear; metal x 2326 on south |
| `tl1_w6022` | P | (2817,6195), east | driven here | the third latch's output; row straight under the rails |
| `tl1_w5936` | P | (2817,6237) east | driven from the east (`tl2`'s upper inverter) | the row under the rails; by the metal x 2500 and the row y 5935 to the wire up the west margin |
| `vss` | M | (2600-2650,6350) south | - | R1, on south |
| `vcc` | M | (2780-2832,6350) south | - | R2, on south (seen at 2.1x to end at about y 6455 on a metal going east; `sc10.png`) |

The same ports, one per line: `ports.d/tl1.txt`.

The rows y 2812, 2857, 2899 were read at 2.5x (`n2.png`) from their pads to x 2820: straight,
under R1, thin metal E's north arm and the wide VSS metal x 2733-2785, no pad on
the way; the row y 2812 ends on a pad (2830,2811) (`n10.png`).

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
  the rail in both metal shots). If the arm were not joined, `rcs_x1`'s transistor would
  hang; if the node were not, `tl1_w4678` would have that one pull-down only.
- **Is thin metal W on the node `tl1_w4678` at about (2693,4688)?** No ring, no green hole,
  in either copy (Logic, "East of R1"): not drawn.
- **The tie of the load of `tl1_w4678` / `tl1_w4070`** (heavy box (2673-2697, 4622-4648), copy
  608 px higher): `?`. If the plate were not tied to the node, the load's gate would hang.
- **The join of the diffusion south of the third pull-down to the rail's VSS box** through
  the gap between R1 and thin W (x 2660-2682, y 4782-4796): covered by the gap's dark
  outline in the clean shot, as the node's strip is at y 4670-4698; read from the chip-2
  stripped shot (Logic). Drawn without `?`. If it were not joined, the third transistor
  would hang (the diffusion south of it has no other exit: closed U, field to the east).
- **The ties of the loads of `tl1_w4703` / `tl1_w4287`** (heavy box (2683-2708, 4500-4524),
  copy 608 px higher): `?`, like the ties of `tl1_w4678` / `tl1_w4070`. The four ties carry
  the cross-coupling of the two latches (Status).
- **`tl1_w4287` = `tl1_w4095`**: one net only through such a tie; an alias, not a rename.
- The joins across R1's edges in `tl1_ua` (the stack's part west of the rail at x 2578-2600;
  the node's west part at x 2590-2604; the node through the gap x 2660-2684) are covered by
  the rail's edge lines as everywhere in this column; drawn without `?` on the chip-2
  stripped shot's colours (Logic).
- The stack of `tl1_ua` is drawn to x 2650 under the row gates (the vertical gate poly
  begins at x 2653); the real east edge may be 5 px further: a width, not a connection.
- The gate of the third pull-down (the band y 4744-4766) is a different poly from gate 2
  (`tl1_w4360`, in the copy `tl1_w3752`), which ends in a rounded end at x ~2670 with plain
  ground across x 2672-2682 (review): 10 px apart.
## Not done

- The four `?` ties of the latch gates' loads: (2673-2697, 4622-4648), (2683-2708, 4500-4524)
  and the same 608 px higher. Until one is read, the cross-coupling and the alias
  `tl1_w4287` = `tl1_w4095` are assumptions.
- **Thin metal W (x 2689-2703): its pieces and contacts. Two passes made (2026-11-17), not
  decided, nothing drawn; `rcs_u3288_n` and `rcs_thin_w` stay two names.** By the rule of two
  honest passes this stops here; what is established, for whoever has a new method:
  - **W does not end in the small cluster.** The "south end at about y 5952-5990" of the
    first pass is the third copy of the dark stretch over a `tl1_ub` tie box (below). The
    line runs on at the same x over the small cluster and the three rows south of it, out
    of the strip at y 6350, and ends on a pad with a contact at about (2695,6410), whose
    poly leaves east along y 6400-6420 (`sc10.png`, 2.1x, metal and clean shot: outside this
    package's region, not drawn; `ur`'s `lc_ck_s` metal on the same track begins at its own
    contact (2695,6590), 150 px further south). `tools/tl1_mrun.py 2684 2708 5300 6360 10`
    (the follower's metal test in both shots): metal on both sides of every dark stretch.
  - **Between y 3027 and y 6410 no place was found where W shows bare ground.** `tools/
    tl1_wcut.py 2693 2701 3030 6420 14` lists every stretch without bright metal; the long
    ones that are not dark are dim metal, shifted 5 px east (text maps of y 5036-5104 and
    y 4262-4304: a line of A-B at x 2698-2704 in both chips). The long **dark** stretches,
    where a cut could hide, are the same three in each copy of the latch: over the
    inverter's buried contact and column (master y 4348-4404, 57 px), over the lower unit's
    tie box (y 4607-4650, 44 px) and over the third pull-down's band and VSS strip
    (y 4692-4780, 89 px).
  - **The comparison the first pass proposed, made** (`tools/tl1_patch.py`, `tools/textmap.py`,
    `tools/px.py col 2702`; three-copy median `w7_m.png`, `w7_a.png`, 6.5x; `w5_a.png`):

    | Spot | Both metal shots | Clean shot under W's centre |
    |---|---|---|
    | tie box of `tl1_ub`, three copies: (2689,4631), (2689,4023), (2689,5976) | no bright metal for 34 px (y 4612-4646), R 20-97 at x 2702: darker than bare ground; a paler patch (chip 2: 8-A of 16, chip 1: 5-7) at x 2684-2694 | **grey-green 150-163/149-173/120-126, red minus green -4 to +12**, a patch about 20 px across (x 2684-2704, y 4626-4644); tan (protected) from x 2706 east and from y 4648 south |
    | standard load ties under W, certainly passed over: the NOR copy's (2696,3690), `rcs_in2`'s (2696,5252) | **bright metal (B-D) over the box's centre**, dark bars of 9 px at the box's two edges | protected: 206/176/130, red minus green 30 |
    | buried contacts under a thin metal, drawn firm: (2563,4677) under the metal x 2565; (2704,4362) under W, three copies | dark 12-25 px at the box's edge | protected: 196-202/151-178/127-133 |
    | contacts of thin metals on poly pads: (2742,4496), (2562,4361); VSS contacts (2628,4610), (2620,4420) | ring, bright centre | 152-164/148-168/96-108, red minus green -4 to +15 |

    So the three `tl1_ub` tie boxes are **not** like the load ties and buried contacts that W
    certainly passes over: the clean shot's colour under W there is that of a contact hole
    (or of ground no metal protected), and the metal is dark for the length of a contact's
    ring. Trap 22's test (bright centre, green hole, widened pad) gives: no bright centre,
    a hole of contact colour, no pad (W widens only from 12 to about 18 px).
  - **Why nothing is drawn.** Reading (c), a contact of W on each box, joins the outputs of
    the three latches (`tl1_w4070`, `tl1_w4678`, `tl1_w6022`) and `rcs_u3288_n`. Then the
    extracted equations give a line that can never rise again once it has fallen
    (`tl1_w4703` = NOT(`tl1_w3594` AND `tl1_w4243` OR W) holds it low, since the two enables
    are never high together): not a circuit. A contact on the plate's tab alone (no tie)
    removes the cross-coupling and makes `tl1_w4678` constant. Reading (b), a cut, needs
    bare ground, and there is none (the 34 px are darker than ground at W's x, and the
    clean shot is protected tan on the node's strip from x 2706 through the whole stretch).
    Reading (a), one metal that is dark over the box, is the only one that gives a circuit
    (`rcs_u3288_n`'s strong load driving one 3,400 px wire to the pad (2695,6410)), and the
    clean shot's colour speaks against it. **The photos and the circuit disagree here**, in
    three copies alike; the `?` ties of the cells stand as they were.
  - What would settle it: a third die photographed with the metal on at higher resolution,
    or a method that tells a contact hole from a pit in the oxide beside a poly end (the
    box is where the plate's tab ends on the node's strip, 4 px from W's west edge). Also
    not looked at: the pad (2695,6410) at 5x.
  - **Run 5, one more comparison: `tla`'s tie box (2690-2712, 3056-3080) under W in the top
    unit** (drawn `?` there; W is on that node anyway, by its contact (2738,3027)).
    `tools/px.py col 2694|2698|2702 3040 3096 4 acid1b,metal,metal1`: **bright metal over the
    box's centre in both chips** (y 3064-3072: 145-204/155-180 chip 2, 140-194/148-159 chip 1)
    between dark bars at y 3052-3060 and y 3076, like the standard load ties of the table's
    second row and unlike the three `tl1_ub` boxes (`px.py col 2694|2698|2702 4604 4660 4`: no
    sample above 104 from y 4612 to y 4644 at x 2694 and 2702); the clean shot under it is
    193-202/150-176/115-140 at x 2694-2698 and greyer, 156-166/138-156/116-125, at x 2702. So
    a tie box under W does not by itself make W dark for 34 px: the three `tl1_ub` boxes
    remain different from every other box W passes. Nothing decided, nothing drawn.
- The far ends of the rows `tl1_w4937`, `rcs_x1` (east of x 2817, past x 3400) and of
  `rcs_mn3852`, `tl1_w3594` (east of x 2817 along y 2857, y 2899).
- `tl4_w4068`'s metal east of (2852,2553); `tl1_w2637`'s east of (2852,2637); `tl4_w4590`'s
  east of (2856,2811); `sl_eq_r5_n` east of x 2817 (pad at about (2867,2595)); the three polys
  north of y 2500 (`rcs_c1` at x 2413, `tl1_w2637` at x 2455, `sl_eq_r5_n` at x 2500);
  where the wide VSS metal x 2733-2785's east arm (y 2905-2955) goes.
- **`tl1_w5936` north of (2380,2498)** (run 5): the fourth poly that leaves north, 33 px west of
  `rcs_c1`'s. All four go into the band y 2180-2500, which no package has drawn.
  **Done since** (coordinator, 2026-11-19): all four end on one NOR drawn by `eof` (piece `r5nor`,
  `notes/blocks/eof.md`): `tl1_w2637` = NOR(`tl1_w5936`, `rcs_c1`, `sl_eq_r5_n`).
- `tl1_w5978`'s metal south of y 6350.
- (Done since: the "second vertical poly x 2137-2147" and `tl1_w5936`'s poly north of its corner
  are the wire of run 5; the VCC box under R2 at (2785-2835, 6065-6130) is drawn by `tl2`, as the
  box of its lower inverter's load, contact (2803,6092).)
- **Cell masters, re-read item R35(b)**, beyond the inverter's gate (done, run 5): the stack of
  `tl1_ua` (gates 1 and 2) measures x 2573-2643 between its edge lines against 2578-2650 drawn
  (`tools/tl1_band.py x 2566 2604 4474 4488 2` and `x 2638 2662 4474 4488 2`: edge lines at
  x 2570-2572 and x 2642-2644 in the clean shot): the width is right (70 against 72; `bc2` read
  about 66 on its copy), the place 5-7 px west; not changed. The third gate's west end and the
  width of its arm to the plate below (`tl3`: 9 px further west, 27 px wide) were not re-read:
  neither changes a transistor (the arm lies on field).
- `tl1_w5978`'s driver. (`tl1_w6022` and `tl1_w5936` east of x 2817 are `tl2`'s two inverters.)
- The six pad contacts (2370,4937), (2500,4894), (2521,5459), (2521,5372), (2372,6061), (2458,4635) were
  re-checked in one mosaic at 3x in both shots (`k_metal.png`, `k_acid1b.png`): ring with a bright
  centre, pad with a green centre, in all six. The other pads were read at 2.05-2.5x only.
- The tie of the plate's tab in the two marked loads (2706-2754, 4287-4323) and (2712-2744, 4906-4960).

## Review

Round 1 (full review, 2026-11-17 20:06 +0000, a fresh agent on claude-fable-5-2, at commit a3b1701). Told to
suspect the nine parallel tracks west of x 2540 (piece ends, pads, a tap on a piece), the
through-pad (2497,5238), the wide NOR's rail-edge joins, gates and load, the two cell
copies, the rows y 2812 / 2857 / 2899 under R1, and `tl4_w4068`'s corners and long
stretches. It checked all 24 pads (ring and green centre, 2.9x), every piece end with the
follower in both chips, the through-pad at 5x, the NOR's gates and contacts, the L
`tl1_w4678`, both copies by mosaic and a 4x overlay, the three rows in the clean shot, and
`tl4_w4068`'s five corners at 5x with a scan of both long stretches every 4 px.
No finding changes a connection. Findings, each checked by the tracer:
1. The NOR copy's VCC box is a box of its own below tla's (two edges, no tan between):
   redrawn from y 3626; still `vcc` through its own contact.
2. The inverter copy's VCC box is one diffusion about y 4188-4338 with three contact rings
   (confirmed on `review-1/invvcc.png`): the lower part and two contacts added.
3. The wide NOR's gate polys run on east to about x 2680: drawn; W is somewhat above 114.
Also: `tl4_w4068`'s three `?P` stretches were read end to end and are now firm.
The extraction's transistor list is unchanged by these edits.
Could not be checked: the diffusion's continuity across R1's west edge (x 2600) in the
wide NOR (the dark line there could be the etch boundary; if it were a break the output
contact would be cut off from the load; drawn without `?`: see Ambiguities), the load ties
(`?`), the far ends of the port rows.

Round 2 (fix check, 2026-11-17 20:10 +0000, a fresh agent on claude-fable-5-2, against commit a3b1701). The two
VCC boxes and the firmed stretches of `tl4_w4068` are right (each stretch at 4x at both ends
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

Round 2 of the second round of work: clean (no findings).

### Third round of work (the loads, cell `tl1_ua`, the two latches)

Round 1 (full review of what was added since 404455d, 2026-11-17 21:28 +0000, a fresh agent on
claude-fable-5-2). Told to suspect the four `?` ties, whether the cross-coupling is real in
both copies or drawn by analogy, the gap joins at x 2656-2684, whether the third
pull-down's far side is VSS, the vertical gate, the buried contact (2704,4362) and each
copy. Checked in master and copy each: the ties (not metal contacts; the same colour
gradient as two known buried contacts of this column; `?` is right), the cross-coupling
(one path each way, seen in both copies: the third gate's poly across the gap and south
into the plate; thin metal x 2742 pad to pad), the polys that must stay separate, the gap
joins by colour in three shots, the inverter's one-piece gate, the buried contact, both
copies by overlay and `cellcheck.py`. No finding changes a connection. Two geometry
findings, applied: the inverter's gate poly is x 2651-2663 (drawn 2653-2668); the two load
plates' east edge on the channel rows is about x 2758 (drawn 2772). `tools/sameconn.py`:
connections identical; the loads are now 26/36 and the inverters 37/12.
Could not be checked: whether poly overlaps diffusion inside the tie boxes (12-15 px
interiors), the third gate's west end under R1's edge line, thin W over the lower tie boxes.

Round 2 (fix check, 2026-11-17 21:34 +0000, a fresh agent on claude-fable-5-2, against commit 89ba1c4). The
inverter gate change is right (bright x 2654-2663 in the clean shot, edge line at x
2662-2664 in the chip-2 shot, master and copy). **The load-plate trim was wrong and is
reverted**: x 2758-2762 is the edge of thin metal x 2742 (its protected margin and ghost
outline), seen identically on the bar rows over field; the plate's outline runs on through
x 2762-2774 in both metal shots, and the sibling plate in the open has its east edge at
x 2773-2776. Checked by the tracer on `review3-2/gapM.png`: round 1's finding is refuted;
the plates are back at x 2772 (loads 26/50). The tracer had applied that finding without
looking at the photo first. Connections identical throughout.

Round 3 (fix check, 2026-11-17 21:35 +0000, a fresh agent on claude-fable-5-2, against commit 7f26d37). Rows on
both plates in master and copy, in the clean and the chip-2 shot: the poly's east edge at
x 2772-2775 on all eight rows; at 4x the drawn edge sits on the outline; 20 px or more of
clearance to the VCC box's contacts; `tools/sameconn.py`: connections identical; all four
loads 26/50.

Round 3 of the third round of work: clean (no findings).

### Fourth round of work (the third latch copy, the north wiring, the fix to tla's ck_out row)

Round 1 (full review of what was added since 43af615, 2026-11-17 22:15 +0000, a fresh agent on
claude-fable-5-2). Told to suspect the third copy's inputs (read from the photo, not the
masters), the `ck_out` row ends and the tla fix, the copy item by item, its rail-edge joins,
the contact (2803,5935), the R1/R2 extensions, `rcs_c1`'s poly under tla's metal, the pads
at the strip edge, and the self-check classes (widths, 50 px beyond each end, undrawn rings
and boxes). Checked: the `ck_out` rows at 6x in four shots (the tla fix is right), the copy
by 4x overlays and rail profiles, its inputs from their own pads, the contacts, the rails,
the four east-edge pads, `rcs_c1`'s loop at 6x in three shots.
One finding, which changes a connection: the wide metal x 2733-2785 (named `tl1_w2930`) is
the same metal as R1: both rise into one plane whose lower edge is at y ~2506, 6 px beyond
the drawn ends. Confirmed by the tracer on `review4-1/k2.png` (both metal shots): the
plane's edge drawn, the metal labelled `vss`, the name, its two ports and its notes
removed. No transistor affected. Minor, not changed: three polys from the north look about
5 px wider or further east than drawn.
Not checked: the `?` load ties, thin W, anything east of x 2850 or north of y 2440.

Round 2 (fix check, 2026-11-17 22:18 +0000, a fresh agent on claude-fable-5-2, against commit ca8efff). The
plane is metal without a break between the legs along y 2490 and 2496 in both chips; the
drawn item covers only metal (lower edge y 2506-2509; ground at y 2515-2528 between it and
the pad metals below); R1 is unbroken to tla's named VSS piece; the east arm has no contact
in the strip; `tools/sameconn.py`: the only difference is that name gone (terminals and
equations unchanged); the ports file parses.

Round 2: no findings.

### Fifth round of work (run 5, Tom Seddon: `tl1_w5936` up the west margin; the inverter's gate length)

Round 1 (full review of what was added since 0490f63, at commit 75d1136, 2026-11-18 12:13 +0000,
a fresh agent on claude-fable-5-2; 21 images in `cache/scratch/tl1/review-5/`). Pieces: W1 (the
wire `tl1_w5936`, x 1960-2400, y 2490-5950) and G1 (the inverter's gate in cell `tl1_ua`).
Told to suspect, W1: the two corners in the open slivers at (2137,3200) and (2137,4198), the
corners (2094,4958) and (2094,5935); at each of the four pads whether the thin metal ends on
it (trap 16), whether the contact is real (trap 22) and whether the poly reaches it; the long
poly stretches (profiled only; dark marks at y 5182-5188, 5240-5290); the two thin metals
between their pads. G1: whether the gate's east edge is at x ~2672-2676 or ~2663.
Checked, W1: the four pads with `tools/textmap.py` and 5x views (`p4957`, `p4200`, `p3200`,
`p2507`): dark ring with a bright centre in both metal shots, green hole in the clean shot,
the poly leaving each; bare ground beyond each metal end, and at y 3226-3244 between the pad
(2068,3200) and `ma3_drv_in`'s (2063,3268) in both chips; `tools/follow.py` from mid-line stops
at each pad; both thin metals at 3.3-3.5x in both chips with field under them end to end
(`m1980a/b`, `m2064a/b`), (1978,4722) is debris on chip 1, no ring where x 1980 crosses the MA4
poly; the corners at 6x (`c3200`, `c4198`) and with `tools/px.py` rows: poly-brown in both metal
shots through each corner, field beyond the bar; the corner (2094,4958): the vertical ends at
y ~4949 with green field at y 4928-4946, so it does not reach the MA4 poly; the corner
(2094,5935) at 4x (`c5935`); the long stretches at 2.5x in three shots (`s1a/b`, `s2a/b`) and by
a column scan of its own: the marks at y 5170-5192 and y 5236-5300 are on chip 1 only, a
small bulge at (2147-2154, 4048-4066) is in the clean shot only, the metals x 2110 and x 2153
are unbroken and ringless at all three places; no ring and no hole at any crossing under the
MA metals; the north-edge poly to its corner and north (`north.png`); a sweep of the margin at
1x with `tl1`, `tla` and `mal` outlined (`sv0`-`sv2`): nothing undrawn; `tools/sameconn.py
0490f63`: one difference, the intended join; `tools/unsure.py`: nothing on this net.
Checked, G1: its own `tools/tl1_band.py` runs at the master and both copies: in the gap
x 2664-2672 the gate rows have poly colour in both metal shots (chip 1 red minus green about
+50, blue 38-49; chip 2 blue 53-65; the diffusion-only row blue 63-72 and 82-88); an edge dip
at x 2674-2678 on the gate rows and on neither reference row; at the cap and the row's end
the edge at about x 2670-2674, so x 2672 is within tolerance; the cap is free (field at
y 4376-4384 between it and the output row, 16 px clear of the buried-contact box); 5.6x views
of the master and the north copy (`g_master`, `g_copyN`).
Findings: none.
Could not be checked: the south copy of the cell (+1345) was profiled, not viewed; the long
poly stretches were viewed at 2.5x, not 4x; the chip-2 stripped shot is unusable in the gaps
between the MA metals, so the corners rest on the two metal shots and the clean shot; the
clean shot alone cannot tell open poly from open narrow diffusion in G1's gap (that reading
rests on the metal shots); where the wire goes north of y 2498; anything west of x 1945.

Round 1: no findings.

## Note (coordinator, from the handoffs of 2026-11-17/18)

- From `tl2`: `tl1_w5936`'s port at (2817,6237) is driven from the east (`tl2`'s upper inverter), so
  it is an input of `tl1` (`ports.d/tl1.txt` updated). The VCC box `D 2785,4255:2842,4338` "with three
  contact rings": the lower contact (2805,4308) feeds `tl2`'s piece 2 load (the strip leaves the box
  east at y 4307-4330).
- The cells' geometry and the thin metal they omit: re-read item R35.

## Corrections from `tl2`, `tl3` (coordinator, from the handoffs of 2026-11-18, second batch)

- Not done: "`tl4_w4068`'s metal east of (2852,2553)" and "`sl_eq_r5_n` east of x 2817" are done in `tl2`
  (`notes/blocks/tl2.md`, "North of y 2630"): `tl4_w4068` comes from a poly that enters at
  (3460,2500) from the band north of the strips; `sl_eq_r5_n`'s metal leaves east at (3533,2509).
  The wide VSS metal x 2733-2785's east arm is y 2893-2948 (it covers the row y 2899, no contact) and
  is one metal with the top of R3; the arm is drawn 12 px short at the top (R36).
- `tl1_w4937` ("enters on a poly row from the east, not identified") is the net of `tl3`'s thin metal
  x 3948-3962 (firm: row and pad), and by that metal `tl3_e3550` (marked: AMB-032). So `rcs_e4` =
  NOR(`tl1_w4678`, `tl3_e3550`).
- `tl1_w3594` ("not identified; every known end is a gate") is `rst_ck`, marked, by `tl3`'s row y 2899 and
  the thin metal x 4099-4111 (AMB-033). Then `tl1_w3636` = NOR(`rst_ck`, `tl4_w4590`) and `rcs_a2` =
  NOR(`rst_ck`, `tl3_w3803`): the two latches in series are a master and a slave on `rst_ck`.
- The master's inverter box under thin W "protected: 196-202/151-178/127-133" at (2704,4362): four px
  lower, `px.py row 4366 2684 2722 3` gives 160-183/142-172/99-141 with a grey sample at x 2708, the
  same grey band as in `tl3`'s latch C (`tl3`). Nothing drawn changes.
- The VCC box (2785-2835, 6065-6130) is `tl2`'s, drawn there.
- Re-read items R41 (thin metal W, with `tools/tl3_thin.py`) and R42 apply here.

## Corrections (coordinator, from the handoffs of 2026-11-19)

- `sl_eq_r5_n` is NOT `sl_eq_r5` (`sl_eq_r5_n`), driven from the east by `eof`'s inverter in `cdp1`'s
  slice-0 position, and leaves north into the band `tlb`.
- `rst_ck` (and so `tl1_w3594`, marked) is `rst_ck` (`eof` run 2).

## Corrections (coordinator, from the handoffs of 2026-11-19, fourth batch)

- The signal on track A / line X / the first through line of the left-centre strips, which these notes call a clock, a strobe "once per scan line" or leave without a source, **is the reset**: `rst_a`, the buffered copy of `rst` = NOR(`lpstb_b`, `res_b`) made by `lc1`'s gate 5 (`eof` run 10, piece `isrc5`, firm). `rst_ck`, `rst_rc` and `rst_lat` are further buffered copies of it: high while the RES and LPSTB pins are both low, and only then. The belief "a strobe once per scan line" is withdrawn.
- `rcs_x1` = NOT `lc1_w7170`, and `lc1_w7170` = NOT `rst_c` (`eof` run 13, piece `rc`, firm): the clear of the step logic's five latches is the reset, two inverters later. Where these notes call its source open, it is found.

## Corrections (coordinator, from the handoffs of 2026-11-20, third batch)

- The net with five loads and no driver (`tl1_w3636`, `tl3_w4978`, `tl3_w3373`, `tl4_w4545`, `tl4_w4686`; "driver not found", "believed in `bc1`'s group"): the driver is the clock buffer. The net is `ck_out` (`tl4` runs 11-12, 2026-11-20, firm joins: the metal x 6016 across y 6350-6900, and from the left bus field's foot through the bottom-centre logic onto `eof`'s row of the clock). `tl3`'s latches A and B are latches on the buffered clock.
