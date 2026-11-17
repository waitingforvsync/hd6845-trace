# tl1: top-left random logic, the westmost strip (x 2100-2817, y 2500-6350)

Package `tl1` (part 1 of 6 of the top-left logic). Trace: `trace/tl1.txt`. Views:
`cache/scratch/tl1/`. The strip contains the west half of the first gate cluster, which
`tla` began (rails R1 = VSS x 2600-2650, R2 = VCC x 2778-2834, thin metal W x 2689-2703; see
`notes/blocks/tla.md`); this package draws what `tla` did not. Nothing of `tla`'s is redrawn.

## Status

2026-11-17 19:44 +0000. **Partial.** Three gates (8 transistors) and the vertical metals of the tracks
x 2283, 2326, 2370, 2414, 2457, 2500 with their pads and rows (y 2790-5480 and y 5900-6350) are traced and extract with 0 errors and
0 warnings in the full extraction. Main result: **the driver of `rcs_e4` is found**, a wide
two-input NOR in the west column at y 4778-5000. Five units of the west column (y 3740-4215,
y 4345-4778), the small cluster below (y 5650-6350), the north-west corner (y 2500-2790)
and the wiring west of x 2260 are surveyed only: see Inventory and Not done.

```
rcs_e4    = NOR(tl1_w4678, tl1_w4937)     (2607,4852), (2607,4936)   marked: only the load's tie is uncertain
tl1_w3636 = NOR(tl1_w3594, tl1_w3678)     (2570,3592), (2570,3678)   firm
tl1_w4243 = NOT tl1_w4287                 (2626,4284)                marked: only the load's tie is uncertain
```

(`tools/unsure.py --equations`: `tl1_w3636` FIRM; the other two DEPEND on the `?` tie of
the load's gate, as `tla`'s inverter does. The pull-downs and every join below are drawn
without `?`.)

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
| 3740-3960 | pad with a contact (2562,3757) under the top end of a vertical metal x 2550-2575 that runs south over the column; its poly goes east under R1 to about x 2668. One diffusion under R1 (x 2572-2650, y 3795-3950) with a VSS contact (2620,3812) and two gate polys from the west across it (y 3841-3861 = `tl1_w2857`, y 3884-3904 = `tl1_w3636`): in series, by the look. Heavy box (2550-2575, 3925-3952) at the east end of the row y 3929-3949 (`tl1_w4287`). Load plate x 2725-2775, y 3760-3840. East of it a pad with a metal contact (2742,3893) at the top of a metal x 2735-2765 (to a contact (2745,4090)) | not traced (one pass at 4.5x in two shots, `u2a.png`, `u2c.png`: the gap between the metal x 2562 and R1 hides the column, chip 2's stripped shot is fringed there) |
| 4000-4215 | unit with two bent gate polys under R1 (y 4100-4120 = `tl1_w3636`'s row, and y 4140-4160), a pad with a contact (2555,4160), pad (2458,4026)'s row y 4017-4036 (`tl1_w4025`) | not traced |
| 4215-4345 | inverter (rail gate), a copy of `tla_w3505`'s | **traced**: `tl1_w4243` |
| 4340-4470 | like the top of the unit at y 3740: pad with a contact (2562,4360), poly east to about x 2670; row y 4452-4470 (`tl1_w4243`) | not traced |
| 4480-4650 | pads (2499,4503) (`tl1_w3594`) and (2458,4635) (`tl1_w4025`) feed it | not traced |
| 4650-4800 | two S-shaped gate polys under R1 (y 4703-4723 from `tl1_w3594`'s pad (2499,4718); y 4752-4772 from a pad with a contact (2555,4767) at the south end of the metal x 2557-2573). The row y 4668-4688 (`tl1_w4678`) ends at about x 2575-2590 on a tan column x 2553-2580, y 4650-4700 | not traced (`u7a.png`, 4.1x): **this is where `rcs_e4`'s first gate comes from** |
| 4778-5000 | wide NOR | **traced**: drives `rcs_e4` |
| 5000-5330 | `rcs_w2`, `rcs_in2` | `tla` |

**Tracks west of the column** (metal runs across x 2090-2460 at 30 heights, both chips;
`tools/tla_tracks.py`, `tools/follow.py`). Nine tracks at 43 px pitch:

| Track x | Pieces |
|---|---|
| 2110, 2153 | `ma1_drv_in`, `ma0_drv_in` (`mal`), full height |
| 2199 | north piece: from the east along y 2557, corner (2199,2557), south to about y 3308-3336 (contact candidate (2199,3336)): **not traced**. South of y 3371: `tla_w3376` (`tla`) |
| 2239 | `tla_w3461` (`tla`), y 3449-5646 |
| 2283 | y 2721-3126 and y 3188-3520 (`tla`); **y 3622-4126 `tl1_w3636`**; **y 4230-4474 `tl1_w4243`**; south of y 4914 `ma4_drv_in` (`mal`) |
| 2326 | `rcs_thin_e` y 2754-3347, `tla_w3417` y 3404-5551 (`tla`); **from a pad (2326,5978) south out of the strip: `tl1_w5978`**. A poly of another net lies under it y 4540-4985 (from the west along y 4547, leaves west along y 4980; seen again at 2.05x, `a4.png`, `a5.png`): not traced |
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
  y 4668-4688, where it arrives from the east, from the unit at y 4650-4800 (seen at 2.05x,
  2.6x, 4.1x and 4.3x: `a4`, `a5`, `b3`, `u7a`, `u8a`). Its driver is in that unit: not traced.
- Gate 2, `tl1_w4937`: pad with a contact (2370,4937) at the north end of a metal x 2370,
  south to y 5459, east to a pad with a contact (2521,5459); from there a poly row east along
  y 5450-5470 under the foot of the cluster. It is straight to x 3400 at 1.44x (`f2.png`) and
  goes on east into the second crossing field. Drawn to x 2817. Source not found.
- Load: node east under thin W to a plate x 2732-2770, y 4848-4914 and the VCC box under R2
  (contact (2800,4882)). No diffusion edge crosses the plate in the metal shots, so the
  channel may be as wide as the plate is tall (strong load, W/L up to 66/38); drawn 28-34/31-38.
  The plate's tab and its tie to the node (heavy box 2722-2765, 4915-4965 in both shots, 6x
  `u8d.png`) are not resolved: `?`.

So `rcs_e4` is high only while both `tl1_w4678` and `tl1_w4937` are low. What those are is
not known.

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

## Ports

| Name | Layer | Where it crosses | Direction | What |
|---|---|---|---|---|
| `rcs_e4` | M | (2500,5232), onto `tla`'s metal | driven here | the long control line of the step logic |
| `tl1_w4937` | P | (2817,5460), east | into the block | gate 2 of `rcs_e4`'s NOR; row under the foot, on east past x 3400 |
| `tl1_w4025` | P | (2817,5372), east | not known | row under the foot, on east past x 3400; on the same metal x 2457 the pads (2458,4026) and (2458,4635) |
| `tl1_w2857` | P | (2817,2857), east | not known | row above the cluster; the other end is a gate row y 3841-3861 |
| `tl1_w3678` | P | (2817,2812), east | into the block (a gate is its only other end) | gate 2 of the NOR |
| `tl1_w3594` | P | (2817,2899), east | not known (three gate-side pads) | gate 1 of the NOR |
| `tl1_w4678` | P | (2545,4678) | from the unit at y 4650-4800 | gate 1 of `rcs_e4`'s NOR |
| `tl1_w3636` | P | (2545,3894), (2545,4113) | driven here | into the units at y 3740 and y 4000 |
| `tl1_w4243` | P | (2545,4461) | driven here | into the unit at y 4340 |
| `tl1_w4287` | P | (2545,3939) | from the unit at y 3740-3960 (believed) | the inverter's input |
| `ck_out` | P | (2545,6063) | from `tla`'s trunk | a gate row into the small cluster |
| `tl1_w5978` | P, M | (2545,5978); (2326,6350) south | not known | row into the small cluster; metal x 2326 on south |
| `tl1_w6022` | P | (2545,6022), (2545,6195) | not known | joins two rows of the small cluster |
| `tl1_w5936` | P | (2110,5935), on to a corner (2096,5935) and north; (2545,6237) | not known | from the pad-ring side to a row of the small cluster |

The rows y 2812, 2857, 2899 were read at 2.5x (`n2.png`) from their pads to x 2820: straight,
under R1, thin metal E's north arm and a wide metal x 2735-2785, no pad.

## Ambiguities

- **The load of `rcs_e4`'s gate**: its width (28 to 66) and the tie of its gate (see above).
- **The joins across R1's west edge** (x 2600) in the wide NOR: as in `tla`.
- **The dark dots on R1** at (2625,2855) and on the wide metal at (2765,2820), (2775,2905) in
  the chip-2 metal shot, where the three rows pass under: no pad in the clean shot; taken as dirt.
- `tools/tla_tracks.py` reported the metal x 2457 broken at y 4683-4869 and the metal x 2500
  at y 5196-5238; `tools/follow.py` and the photos show both continuous (a poly lies beside or
  under them there). Its breaks need a look every time.

## Not done

- **Where `tl1_w4678` (first gate of `rcs_e4`'s NOR) comes from: two passes, not resolved.**
  Its row y 4668-4688 ends at x 2548 on a tan rectangle (2553-2573, 4655-4690) with a heavy
  outline on its west side and a heavy rounded bottom (y 4690-4697), right under the metal
  x 2557-2573 (`u7b.png`, 6x, clean shot and metal). The same shape, 123 px higher: a tan
  rectangle (2553-2573, 4535-4558) with a heavy rounded bottom (`u6b.png`, 6x). Under that
  metal, going down: tan end (4535-4558), pink = field (4563-4595), tan (4597-4620), the
  salmon row of `tl1_w4025` (4622-4643), pink (4645-4655), the tan rectangle (4655-4690).
  Readings: (a) each tan rectangle is the end of the row's poly on a buried contact to a
  diffusion under the metal; (b) the row `tl1_w4025` crosses a diffusion column there (a
  pass transistor into `tl1_w4678`, which would make `rcs_e4`'s first input a latched
  value). Neither is shown: under this metal the clean shot's tan and salmon could not be
  told apart with confidence, and the gap between the metal and R1 (x 2575-2600) hides what
  lies beside it. Next: the metal x 2557-2573 itself (where are its contacts: (2562,3757),
  (2555,4160)?, (2562,4360)?, (2555,4767)), then a profile down x 2563 in all four shots.
- The unit at y 4650-4800 (`u7a.png`, `u7b.png`): under R1, from the top: diffusion y 4668-4700
  (reaching east to x 2700), gate y 4702-4722 (`tl1_w3594`, from the pad (2499,4718)), diffusion
  y 4722-4747, gate y 4747-4773 (from the pad (2555,4767); its poly goes on east as a thin
  line along y 4745-4755), then the VSS box shared with `rcs_e4`'s NOR. West of x 2578 there
  is field between the gates, so the unit's output leaves east. Not traced.
- West column units at y 3740-3960, 4000-4215, 4340-4470, 4480-4650 (Inventory). Needed for each: 5-6x in `acid1b` and both metal
  shots; the gap between the metal x 2557-2573 and R1 (x 2575-2600) hides the column in the
  clean shot, so read the column in the metal shots.
- The vertical metal x 2557-2573 over the column, from the pad (2562,3757) south to the pad
  (2555,4767) (pieces? pads at (2555,4160), (2562,4360)): not followed.
- The metal x 2735-2765 from (2742,3893) to (2745,4090); thin metal W's contacts.
- The far ends of the rows `tl1_w4937`, `tl1_w4025` (east of x 2817, past x 3400) and of
  `tl1_w2857`, `tl1_w3678`, `tl1_w3594` (east of x 2817 along y 2812-2899).
- The metal x 2199's north piece (from the east along y 2553-2557 to a corner (2199,2556),
  south to y 3338: follow.py; its end at (2196,3338) not looked at).
- The poly under the metal x 2326, y 4540-4985 (`s3.png`, 2.15x): at the top it runs west
  along y 4533-4550 to a corner at about x 2165-2180 and north; at the bottom west along
  y 4972-4988 to about x 2131 and (not clear) south. Both ends leave among the pad-ring
  metals. Likewise `tl1_w5936`'s poly north of (2096,5925), and `tl1_w5978`'s metal south
  of y 6350.
- North of y 2790 and the small cluster south of y 5640: surveyed at low zoom only.
- The tie of the plate's tab in the two marked loads (2706-2754, 4287-4323) and (2712-2744, 4906-4960).

## Review
