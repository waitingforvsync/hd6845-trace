# tl1: top-left random logic, the westmost strip (x 2100-2817, y 2500-6350)

Package `tl1` (part 1 of 6 of the top-left logic). Trace: `trace/tl1.txt`. Views:
`cache/scratch/tl1/`. The strip contains the west half of the first gate cluster, which
`tla` began (rails R1 = VSS x 2600-2650, R2 = VCC x 2778-2834, thin metal W x 2689-2703; see
`notes/blocks/tla.md`); this package draws what `tla` did not. Nothing of `tla`'s is redrawn.

## Status

2026-11-17 21:13 +0000. **Partial.** Nine gates with their loads (28 transistors), the vertical metals of the
tracks x 2283, 2326, 2370, 2414, 2457, 2500 with their pads and rows (y 2790-5480 and
y 5900-6350), the two pieces of the thin metal x 2557-2573 over the west column, the two
pieces of the thin metal x 2742, and one long wire down the west side (`tl1_w3333`) are
traced and extract with 0 errors and 0 warnings in the full extraction. **The west column
is traced from y 3558 to y 5000** (above and below it is `tla`'s). Main results: **the
driver of `rcs_e4` is found**, a wide two-input NOR at y 4778-5000; **its first input
`tl1_w4678` is one side of a cross-coupled pair of gates** (y 4340-4800: a latch that is
open while `tl1_w3594` is high and then takes `tl1_w4243`, with `tl1_w4025` forcing it
low); **the column y 3732-4215 is a copy of y 4340-4800**, 608 px higher, a second latch
of the same build (open while `tl1_w3636` is high, data `tl1_w2857`), whose output through
the inverter `tl1_w4243` is the first latch's data. `tl1_w3636` = NOR(`tl1_w3594`,
`tl1_w3678`), so the two are never open together: a master and slave. The small cluster
below (y 5650-6350), the north-west corner (y 2500-2790), thin metal W and the wiring west
of x 2260 are surveyed only: see Inventory and Not done.

```
rcs_e4    = NOR(tl1_w4678, tl1_w4937)     (2607,4852), (2607,4936)   marked: only the load's tie is uncertain
tl1_w3636 = NOR(tl1_w3594, tl1_w3678)     (2570,3592), (2570,3678)   firm
tl1_w4243 = NOT tl1_w4287                 (2626,4284)                marked: only the load's tie is uncertain
second latch (y 4340-4800):
tl1_w4360 = NOT tl1_w4243                                            (2660,4422)   firm
tl1_w4703 = NOT(tl1_w4243 AND tl1_w3594 OR tl1_w4678)                (2614,4461), (2614,4501), (2631,4575)   marked: the ties of the two loads
tl1_w4678 = NOT(tl1_w4025 OR tl1_w3594 AND tl1_w4360 OR tl1_w4703)   (2570,4634), (2618,4715), (2618,4761), (2722,4755)   marked: the ties of the two loads
first latch (y 3732-4215, the copy):
tl1_w3752 = NOT tl1_w2857                                            (2660,3814)   firm
tl1_w4287 = NOT(tl1_w2857 AND tl1_w3636 OR tl1_w4070)                (2614,3853), (2614,3893), (2631,3967)   marked likewise; = tl1_w4095 by an alias
tl1_w4070 = NOT(tl1_w4025 OR tl1_w3636 AND tl1_w3752 OR tl1_w4287)   (2570,4026), (2618,4107), (2618,4153), (2722,4147)   marked likewise
```

(`tools/unsure.py --equations`: `tl1_w3636`, `tl1_w4360`, `tl1_w3752` FIRM; the others DEPEND
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
| 4590-4800 | VSS box, a column west of R1 with `tl1_w4025`'s gate, the node with a buried contact to `tl1_w4678`'s row, under R1 two gates in series (`tl1_w3594`, `tl1_w4360`) down to the VSS box of the wide NOR; east of R1 the node's strip under thin metal W, a third pull-down (`tl1_w4703`) at its south end and the load at its north end | **traced**: the node is `tl1_w4678` |
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
output of the unit above (low when `tl1_w4025` is high, or `tl1_w3594` and `tl1_w4360` are
both high, or `tl1_w4703` is high), so
`rcs_e4 = (tl1_w4025 OR tl1_w3594 AND tl1_w4360 OR tl1_w4703) AND NOT tl1_w4937`;
what those inputs are is not known.

### The unit that drives `tl1_w4678` (y 4590-4800) and its copy (y 3982-4215): traced

```
tl1_w4678 = NOT( tl1_w4025  OR  tl1_w3594 AND tl1_w4360  OR  tl1_w4703 )
tl1_w4070 = NOT( tl1_w4025  OR  tl1_w3636 AND tl1_w3752  OR  tl1_w4095 )      (the copy)
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
along y 4353-4372, under R1 over field (pink above and below it there), through the gap
(where the gap's outline makes a ring on it at x 2660-2680), onto the output node of the
inverter of the unit above (next section): `tl1_w4360` = NOT `tl1_w4243`.

**The copy.** `tools/findcell.py 2535 4590 2790 4780` (clean shot) finds the unit again at
0,-608 with score 0.94, and the unit above it (2535-2790 x 4345-4585) at 0,-608 with 0.93. The
geometry is a cell (`tl1_ub`) placed twice; the overlay of the copy was checked on `o7.png`
(2.9x, clean shot and metal): VSS box with a contact (2620,4002), arm, `tl1_w4025`'s row
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
tl1_w4360 = NOT tl1_w4243                               copy: tl1_w3752 = NOT tl1_w2857
tl1_w4703 = NOT( tl1_w4243 AND tl1_w3594  OR  tl1_w4678 )
                                copy: tl1_w4287 = NOT( tl1_w2857 AND tl1_w3636  OR  tl1_w4070 )
```

Views: `u1_a.png`, `u1_m1.png` (4.1x, clean shot and chip-1 metal), `u2_a.png`, `u2_m.png`
(6x, four shots, y 4500-4608), `u3_a.png`, `u3_a2.png` (6x, both stripped shots, y 4338-4488),
`u4_all.png` (the west box, master and copy, three shots, 6.5x); overlays `v1_m.png`,
`v1_c.png` (4.1x, each copy singly). Master coordinates; the copy agrees item by item.

**The inverter (y 4345-4460).**
- Pull-down: the row y 4452-4470 (`tl1_w4243`, from the pad (2283,4462)) turns north at the
  rail's east edge as a vertical poly x 2653-2668 and crosses the diffusion between the
  rail's VSS box (2600-2650, 4403-4447, contact (2620,4420)) and the part under thin W.
  `tools/px.py col 2658 4376 4480 3`: one salmon band from y 4391 to y 4466 with two single
  edge lines (y 4400-4403, y 4439-4442: the diffusion's edges) and no field between; between
  the lines it is 245-254/177-187/120-132, poly over a channel, outside them 220-227/152-176,
  poly over field; the copy reads the same. Its top is a free rounded cap (y 4388). W/L 37/15.
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
tl1_w4678 = NOT( tl1_w3594 AND NOT tl1_w4243  OR  tl1_w4703  OR  tl1_w4025 )
```

While `tl1_w3594` is high, `tl1_w4678` follows `tl1_w4243` and `tl1_w4703` is its inverse;
while it is low the pair holds; `tl1_w4025` high forces `tl1_w4678` low. The copy is the
same with `tl1_w3636` for `tl1_w3594`, `tl1_w2857` for `tl1_w4243`, and its inverse output
`tl1_w4287` goes through the inverter at y 4215-4345 to be this pair's data: `tl1_w4243`
is the copy's `tl1_w4070` again. Since `tl1_w3636` = NOR(`tl1_w3594`, `tl1_w3678`), the first
latch is open only while `tl1_w3594` and `tl1_w3678` are both low and the second while
`tl1_w3594` is high: **`tl1_w4678` is `tl1_w2857` taken through two latches in turn, with
`tl1_w4025` clearing both** (traced, marked by the four `?` ties), and
`rcs_e4` = NOT `tl1_w4678` AND NOT `tl1_w4937`. What `tl1_w2857`, `tl1_w3594`, `tl1_w3678`,
`tl1_w4025`, `tl1_w4937` are is not known: all five come from the east on poly rows.

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
  the copy of `tl1_ua`: `tl1_w4287` = NOT(`tl1_w2857` AND `tl1_w3636` OR `tl1_w4070`).
- Output: metal x 2283, y 4230-4474, to a pad (2283,4462) whose row y 4452-4470 runs east
  across the stack of `tl1_ua` (gate 1 of the three-input gate) and north at the rail's edge
  as the inverter's gate (`tl1_w4360`).

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
| `tl1_w2857` | P | (2817,2857), east | into the block (its other ends are gates) | row above the cluster; the data of the first latch (gate 1 of `tl1_w4287`, and the inverter `tl1_w3752`) |
| `tl1_w3678` | P | (2817,2812), east | into the block (a gate is its only other end) | gate 2 of the NOR |
| `tl1_w3594` | P | (2817,2899), east | into the block (its other ends are four gates) | gate 1 of the NOR `tl1_w3636`; the enable of the second latch (a series gate in each of its two gates) |
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
- **Thin metal W (x 2689-2703): its pieces and contacts. One pass made (2026-11-17), not
  resolved, nothing drawn.** What was measured (`tools/tl1_wgaps.py 2684 2708 3030 5990 125 6`:
  the rows where the brightest 4 px across the line stay dark in both metal shots;
  `tools/tl1_wmap.py`: text map; strips `w_all.png` 1.15x, three shots, y 3000-6000):
  - From `tla`'s contact (2738,3027) to about y 5952 the line is at the same x throughout
    and no stretch is fully dark (below 125) for more than 20 px; `tla`'s end at y 4002 and
    the earlier "short piece y 4042-4086" are follower stops. Bright pieces between dark
    crossings all the way, each crossing over an edge or a box underneath.
  - The two longest dim stretches (below 165 in both shots) are over the tie boxes of the
    two `tl1_ub` units: y 4607-4647 and y 4004-4040 (37-41 px; fully dark for 20 and 34 px).
    At 6.5x (`w4_all.png`, both metal shots and the clean shot, master and copy): no bright
    metal at W's x between the plate's bar and the node's box; the box (2678-2697,
    4622-4645) has two paler spots in the metal shots and a **green-yellow centre inside a
    dark outline in the clean shot**, in both copies; W resumes at y 4648 and is wide over
    the node box (y 4665-4692). Readings: (a) one metal, dark over a buried contact (tracing
    guide, trap 22; but that trap says the clean shot shows no green there); (b) W is cut
    there and the box is open diffusion; (c) a contact of W on the box. (b) and (c) put W on
    the nodes of two different gates and on `rcs_u3288_n`, which cannot all be right; (a) is
    the only reading that gives a circuit (W as one long wire from `rcs_u3288_n`'s strong
    load to the small cluster, passing over the loads), and it is **not shown**.
  - Other dark stretches of 10 px or more between y 4002 and y 4940: y 4350-4361 (the
    inverter's buried contact), y 4500-4508 (the tie box of `tl1_w4703`), y 4739-4772 (the
    third pull-down's gate band), y 4909-4916 (the wide NOR's tie). No ring with a bright
    centre anywhere on the line in the strips.
  - Not looked at: the south end (about y 5952-5990), `tla`'s piece `rcs_thin_w`
    (y 4940-5330) against `rcs_u3288_n`. If W is one metal those two names are one net.
  Next: the box (2678-2697, 4622-4645) against a load tie that certainly has no metal over
  it (an east-column tie beside thin E's gaps) and against a known contact of a thin metal
  on diffusion, in the clean shot at 6x; W's south end at 5x.
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

