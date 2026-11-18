# lc1: left-centre random logic, the top strip (x 4400-6450, y 6900-8067)

Package `lc1` (part 1 of 3 of the left-centre logic; `lc2`, `lc3` are the strips south of
y 8067 and y 9233). Trace: `trace/lc1.txt`. Views and the survey: `cache/scratch/lc1/`
(`survey.md` lists every measurement with the command that gave it). Traced by Chris Evans'
session (the claim is held for it by mattgodbolt; no write access yet, so the branch goes in
as a pull request).

## Status

2026-11-17 17:20 -0800. **Partial: gate column W traced** (x 4750-5100, y 6940-8067): eight
gates, 17 transistors, each with its load, tie, pull-downs and output. Full extraction with
every trace file: 0 errors, 0 warnings. Not traced: everything east of x 5110 (the bus wiring
x 5100-5600, the crossing field x 5600-6450 north of y 7500, the gate cluster E at x 5450-6250
south of y 7550) and the metal bus west of x 4750 (`urch`'s channel).

```
lc_step   = NOT lc1_w7040                      firm (and the join to ur's lc_step poly is drawn)
lc1_w7140 = NOT lc1_w7170                      firm
lc1_w7304 = NOR(lc1_w7257, lc1_w7343)          firm
lc1_w7468 = NOT lc1_w7304                      firm
lc1_w7606 = NOT lc1_w7468                      firm
lc1_w7734 = NOT lc1_w7468                      firm
lc1_w7864 = NOT lc1_w7468                      firm
lc1_w7990 = NOT lc1_w7864                      firm
```

("firm" as `tools/unsure.py --equations` uses it: no `?` item in the trace is involved.)

**The scan line counter's step pulse is made here**: `lc_step` (which clocks the scan line
counter and the 4-bit counter `c4l`, `notes/blocks/ur.md`) is the output of gate 1, an
inverter of the poly row `lc1_w7040`, which arrives from the east along y 7030-7050. What
drives that row is not traced yet.

The rest of the column is a small tree: a two-input NOR (`lc1_w7304`, inputs two poly rows
from the east), its inverse `lc1_w7468`, and three inverters of that (`lc1_w7606`,
`lc1_w7734`, `lc1_w7864`: three copies of NOR's output, each leaving east on its own row),
then `lc1_w7990` = NOT `lc1_w7864`, which leaves south. Gate 2 is a separate inverter whose
input arrives from the south on a thin metal and whose output leaves north on a metal.
Believed, not traced: three buffered copies of one signal is the pattern of `inh_ck`,
`inh_rc`, `inh_lat` (`notes/operation.md`).

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
| 2 | 7107-7245 | (4777,7138) | (4960,7215) | y 7158-7182 to the pad (5082,7170); metal south and west to the thin metal T1 (x 5030-5046), which runs south out of the strip: `lc1_w7170` | box (5008-5048, 7116-7156), poly east to the pad (5082,7105), metal M_a (x 5070-5090) north out of the strip: `lc1_w7140` |
| 3 | 7275-7375 | (4777,7315) | (4960,7215) and (4960,7388) | two rows from the east crossing a diffusion column under T1 (x 5022-5040): `lc1_w7257` (y 7248-7267), `lc1_w7343` (y 7334-7352) | box (5010-5046, 7284-7320) on the column between the rows, poly east to the pad (5082,7302), strap M_c1 south to the pad (5082,7388): `lc1_w7304` |
| 4 | 7402-7505 | (4777,7442) | (4960,7388) | y 7420-7447 from x 4892, east and up to the pad (5082,7388): `lc1_w7304` | box (5024-5050, 7464-7490), poly east to the pad (5083,7474) on the metal M_c2 (x 5073-5093), which runs south out of the strip: `lc1_w7468` |
| 5 | 7525-7632 | (4777,7572) | (4962,7525) | y 7552-7578 from x 4892 to the pad (5082,7563) on M_c2 | box (5024-5050, 7590-7620), poly row east along y 7597-7615: `lc1_w7606` |
| 6 | 7668-7755 | (4777,7722) | (4960,7655) | y 7681-7701 to the pad (5082,7692) on M_c2 | box (5012-5048, 7713-7747), poly row east along y 7725-7743: `lc1_w7734` |
| 7 | 7785-7897 | (4777,7830) | (4958,7790) | y 7809-7835 from x 4892 to the pad (5082,7822) on M_c2 | box (5012-5048, 7853-7882), poly row east along y 7855-7873 and a poly south under M_c2 (x 5072-5092) to gate 8's row: `lc1_w7864` |
| 8 | 7923-8017 | (4777,7968) | (4955,7910) | y 7942-7962, east to the poly under M_c2 | box (5012-5048, 7983-8012), poly east and south under M_c2 out of the strip: `lc1_w7990` |

A ninth gate of the same build straddles the south boundary (VSS contact (4955,8045), gate
row y 8076-8099): `lc2`'s.

## Logic

Traced (the equations above are what `tools/netlist.py` recovers):

- Gates 1, 2, 4-8 are inverters; gate 3 is a NOR of two.
- Gate 3's two pull-downs are small (W about 18) and lie **under the thin metal T1**, east
  of rail 2: the output band passes under rail 2 without a device (pink field either side
  of the band there), joins a diffusion column x 5022-5040, and the two rows cross that
  column above and below the output box. Evidence: `px.py col 5031` (tan diffusion at y
  7232-7244, 7274-7280, 7325-7328, 7361-7370; bright salmon gate at 7250-7262 and 7337-7349)
  against `px.py col 5046` (pink field above and below both rows). Above the upper row the
  column turns west (y 7228-7244) into gate 2's VSS box; below the lower row it turns west
  (y 7358-7374) into gate 4's VSS box.
- T1 is the metal on gate 2's row pad: from the pad (5082,7170) south to y 7226, west to
  x 5030, then south. It is dim or dark in both metal shots over y 7240-7380 (it lies on the
  column and the boxes: traps 19, 22) but the clean shot is protected under it all the way,
  and it is bright again from y 7380 to the south boundary. No pad on it inside the strip.
- M_c2 carries `lc1_w7468` from gate 4's output pad to the row pads of gates 5, 6, 7 and on
  south. Four poly rows pass under M_c1 / M_c2 without contact: `lc1_w7343` under M_c1,
  `lc1_w7606` and `lc1_w7734` under M_c2, and the two vertical polys of `lc1_w7864` and
  `lc1_w7990` lie under M_c2 lengthwise (text maps against the known pad (5082,7563): bright
  metal, protected poly, no green hole; `survey.md`).
- Sizes (W/L from the extraction): loads 30/37 (gate 1), 37/44 (2), 25/60 (3), 66/38 (4),
  65/40 (5), 40/47 (6), 68/40 (7), 27/60 (8); pull-downs 138/20 (1), 67/24 (2), 18/19 and
  18/18 (3), 110/24 (4), 99/26 (5), 77/20 (6), 110/24 (7), 77/20 (8). Gates 4, 5, 7 are one
  cell (an L-shaped load poly with a foot, the channel the full height of the VCC box);
  gates 6 and 8 are alike but for the tie. Good to about 15 %: see Ambiguities 2, 3.

Believed: nothing beyond what is said under Status.

## Ports

Also in `ports.d/lc1.txt`. The strip's edges are y 6900 (north), y 8067 (south), x 4400,
x 6450. Wires that end inside the strip, undrawn beyond, are listed with where the drawing
stops.

| Name | Layer | Where | Direction | What |
|---|---|---|---|---|
| `vcc` | M | x 4755-4803 at y 6900 and at y 8067 | - | rail 1, runs on both ways |
| `vss` | M | x 4842-4893 at y 6900; x 4928-4980 at y 8067 | - | rail 2 and its arm north |
| `lc_step` | P | (5012-5030, 6890) | out | joins `ur`'s poly, which ends at (5012,6900) |
| `lc1_w7140` | M | x 5070-5090 at y 6900 | out | M_a, north; still metal at y 6840 |
| `lc1_w7170` | M | x 5030-5046 at y 8067 | in | T1, south (gate 2's input) |
| `lc1_w7468` | M | x 5073-5093 at y 8067 | out | M_c2, south |
| `lc1_w7990` | P | x 5072-5092 at y 8067 | out | under M_c2, south |
| `lc1_w7040` | P | (5140, 7030-7050) | in | gate 1's row; drawn to x 5140, goes on east inside the strip |
| `lc1_w7257` | P | (5140, 7248-7267) | in | gate 3's upper row; drawn to x 5140 |
| `lc1_w7343` | P | (5140, 7334-7352) | in | gate 3's lower row; drawn to x 5140 |
| `lc1_w7606` | P | (5140, 7597-7615) | out | gate 5's output row; drawn to x 5140 |
| `lc1_w7734` | P | (5110, 7725-7743) | out | gate 6's output row; a pad at about (5120,7735) not drawn |
| `lc1_w7864` | P | (5110, 7855-7873) | out | gate 7's output row; a pad at about (5120,7865) not drawn |

## Ambiguities

1. **The join of gate 1's output box to the `lc_step` poly** (5046-5053, 6985-7010). The
   poly comes down x 5050-5068 beside the box and ends at y about 7008 (orange in both
   chip-2 shots at y 6965-7004, plain at y 7016: `px.py row`). Between it and the box's
   interior there is a dark line at x 5046-5050, which continues south to y 7065 as the east
   edge of the diffusion, so it is read as that edge and the buried window's, not as a gap
   between two polys; the box's top edge lines run into the wire's west edge. Read at 6.4x in
   four shots (`j_lcstep.png`). Working assumption: joined (a poly that ends beside a buried
   box and nowhere else is the box's wire). What would settle it further: nothing in these
   photos; `ur`'s independent statement that the poly "ends on something at about
   (5030,7000-7150)" agrees.
2. **How far east each pull-down's channel reaches** (sizes only). Drawn to x 5046 (gates 1),
   5040 (4, 5, 7), 5022 (6, 8), 5012 (gate 2, to a dark line that crosses the row at x 5012).
   In the open the diffusion edges are judged from outlines in the metal shot and the class
   map; they are good to about 10 px. Connections do not depend on it.
3. **The loads of gates 4, 5, 7**: the channel is drawn the full height of the VCC box
   (W 65), with a drain strip x 4850-4866 beside the poly, from a 5.3x view (`l4z.png`); the
   strip is narrow and its colour is not conclusive (`px.py row 7430`). If the diffusion
   crosses only at the bottom, W is about 25. The connection is the same.
4. **Rail names.** `vcc` and `vss` are from the orientation of the loads; neither rail is
   followed to a pad or to a named supply inside this strip.

## Review

(not yet reviewed)

## Not done

- **The sources and destinations of the column's wires**, all inside this strip to the east:
  `lc1_w7040` (what makes `lc_step`: follow the row east from x 5140 first), `lc1_w7257`,
  `lc1_w7343`, `lc1_w7606`; the pads at about (5120,7735) and (5120,7865) on `lc1_w7734` and
  `lc1_w7864`.
- x 5100-5600: bus wiring (a diagonal poly bundle from the upper left, vertical metals x
  5140-5330, pads at (5210,7245), (5165,7300), (5100,7620), (5100,7700) and others). One of
  the diagonal polys passes just east of `lc_step`'s (x 5050-5067 at y 6840, under M_a).
- x 5600-6450, y 6900-7500: the crossing field (poly rows against vertical metals; pads at
  x 6110-6130). `tla`'s line (poly to the pad (6140,7124)) and `bw`'s metal x 5841 (pad
  (5838,7470)) are drawn by those blocks.
- x 5450-6250, y 7550-8067: gate cluster E (rails at about x 5680, 5900, 6020; loads near
  (5920,7740), (5880,7880)); continues south into `lc2`.
- x 4400-4750: the metal bus (`urch`'s channel), about eight thin metals and a wide one at
  x 4684-4716; `urch`'s pad (4400,7068) is here.
- The ninth gate at y 8040-8140 (`lc2`).
