# tl2: top-left random logic, the second strip (x 2817-3533, y 2500-6350)

Package `tl2` (part 2 of 6 of the top-left logic). Trace: `trace/tl2.txt`. Views:
`cache/scratch/tl2/`. Most of the strip is `tla`'s east gate column on rail R3 (VSS,
x 2950-3000; traced, `notes/blocks/tla.md`) and the bus field east of it. This package draws
what `tla`, `tl1`, `r9m` and `ur` did not. Nothing of theirs is redrawn.

## Status

2026-11-18 01:58 +0000 (run 3, Tom Seddon). **Partial: the gate column begun.** Run 3 traces the
gate column east of R3 where `tla` left it (y 3690-4620). Piece 1, the unit at y 3690-3840
(2 transistors): two pull-downs with no load of their own, whose node is `tla`'s `rcs_bc3460`
by a diffusion strip under the rail and thin metal E. So, extracted, on geometry without `?`:

```
rcs_bc3460 = NOR(rcs_e3, rcs_e4, tl2_w3722, clk_tl)      tla had NOR(rcs_e3, rcs_e4)
```

and `rcs_u3425` = NOT `rcs_bc3460` = `rcs_e3` OR `rcs_e4` OR `tl2_w3722` OR `clk_tl`. The
step formula of `tla` does not change (the two new terms cancel out of it, as `rcs_x1` does:
see "The gate column east of R3"); `rcs_c1` does. Full extraction: 2270 nets, 4045 transistors,
0 errors, 0 warnings.

2026-11-18 00:25 +0000 (run 2, Tom Seddon). **Partial: two pieces.** Run 2 added the wiring of the
bus field east of the first cluster: the ten undrawn metal pieces of its tracks D and F-J with
their 24 contacts, and the poly row from every pad, drawn to the strip's edges or onto tla's,
tl1's and tl3's ends (no transistor). Five joins between names of other packages came out of it,
all on geometry without `?`, and one correction to `tla`'s trace (see "The bus field's east tracks"):

```
rcs_x1 = rcs_g4240 = tl1_w4025 = tl3_w3506       one net: track I (y 3494-5380)
tl3_w3982 = the gate of tla's pass transistor     tracks F (middle piece) and J (lower piece); NOT clk_tl
tl1_w3594 = tl3_w3722                             track H (upper piece)
tl1_w2637 = tl3_w3333                             track D (upper piece) and the row y 3202
rcs_a2 = tl3_w3765, tl3_w3419 = tl3_w3896         tla's row y 3761; track J (upper piece)
```

so that the full extraction now reads `rcs_a2 = NOR(tl1_w3594, tl3_w3803)` (FIRM in
`tools/unsure.py --equations`), `rcs_cond_lat` is `rcs_cond` passed while `tl3_w3982` is high
(not while `clk_tl` is: the review found that `tla`'s gate row does not reach `clk_tl`'s pad), and the clear
of tl1's two latches, the clear of tl3's latch, `rcs_b1`'s input x1 and `rcs_n4200`'s input are
one signal. After merging main (tl3's later runs) nine more rows meet tl3's at x 3533 ("Joins made when main
was merged"): `rcs_x1` also clears tl3's latch B and resets the pair that makes `tl3_w3803`.
Full extraction: 2263 nets, 4034 transistors, 0 errors, 0 warnings.

Run 1, 2026-11-17 16:30 -0600 (Matt Godbolt). **One piece.** The east half of the small cluster below the
step logic (x 2817-3180, y 5900-6300) is traced: two inverters in series (4 transistors), which
buffer the third latch's output `tl1_w6022` onto `tl1_w5936`; rail R3 from y 5320 to its foot
and the VSS metal that leaves the foot; the two thin metals that pass over the units, each to
its south end in the strip. Full extraction: 0 errors, 0 warnings.

```
tl2_w6070 = NOT tl1_w6022     (2992,6109)   lower unit
tl1_w5936 = NOT tl2_w6070     (2992,5978)   upper unit
```

Not traced: the units of the gate column at y 3700-4620, the tracks north of y 2630, `tla`'s
undrawn contacts (see Not done).

## Inventory

| Where | What |
|---|---|
| x 2860-3100, y 2940-5300 | `tla`'s east gate column on R3 (traced by `tla`) |
| x 3085-3533, y 2630-5700 | bus field: ten vertical metal positions (pitch 43.5: A 3108, B 3152, C 3196, D 3240, E 3283, F 3326, G 3369, H 3413, I 3456, J 3499), in pieces, with poly rows and pads. `tla` drew A-E and G's upper piece; **run 2 drew the rest** (D upper, F x3, G lower, H x2, I x2, J x2) |
| x 2860-3100, y 3690-3840 | **run 3, piece 1**: two pull-downs on `rcs_bc3460` (gates: the rows y 3722 and y 3808) between `tla`'s VSS boxes, with the node's strip west under R3 and south under thin metal E |
| x 2860-3100, y 4320-4620 | `tla`'s east gate column where `tla` did not trace it: gates on the rows y 4374, 4418, 4470 |
| y 2500-2940 | horizontal metal tracks and rows north of the cluster, partly `r9m`'s and `tla`'s |
| x 2817-3180, y 5900-6300 | the small cluster's east half: **this piece** |
| x 2890-3533, y 6300-6350 | `rcs_thin_e`'s pad (2913,6327) and its poly row east (drawn); `lc_step`'s row y 6268-6290 is `ur`'s |

## Logic

### The small cluster's east half: two inverters (traced 2026-11-17)

Built like `tla`'s units on R3: the pull-down sits on a VSS box under the rail, its drain is a
strip that runs west under the rail to the node, and the load is a strip from a VCC box under
R2, under a poly plate between R2 and R3, with a tie box at the plate.

- **Lower unit, `tl2_w6070` = NOT `tl1_w6022`.** VSS box x 2968-3015, y 6095-6170, contact
  (2988,6144). Gate: `tl1`'s row y 6187-6203 (the third latch's output) runs on east under R2,
  the thin metals and R3, turns north at x 3101-3125 and west along y 6098-6120 across the top
  of the VSS box (W 47); its west end is at x 2953. Drain: tan under the rail, y 6064-6092. Node:
  a diffusion strip in the open gap between thin metal E and R3, x 2934-2947, y 6048-6120. Load:
  strip y 6093-6120 from a VCC box under R2 (x 2785-2833, y 6062-6122, contact (2803,6092):
  ring in both metal shots, specks in the clean shot, `c11.png`) under the plate x 2836-2925,
  y 6066-6122. Tie: box x 2895-2927, y 6042-6062 at the plate's top, reached by the node strip.
  Output: a strip east along y 6064-6084 to the buried contact B (box x 3038-3068, y 6050-6084).
- **Upper unit, `tl1_w5936` = NOT `tl2_w6070`.** VSS box x 2968-3015, y 5962-6040, contact
  (2986,6011). Gate: the poly from B east along y 6056-6076, north at x 3101-3125, west along
  y 5966-5990 across the top of the VSS box (W 47), west end x 2952. Drain: strip y 5942-5960
  north of the gate, west under the rail and through the gap to the node (x 2897-2930,
  y 5935-6005, under thin metal E), east to the buried contact A (box x 3038-3068, y 5924-5958).
  Load: strip y 5936-5962 from `tl1`'s VCC box under R2 (contact (2803,5935)) under the plate
  x 2842-2892, y 5915-5990. Tie: box x 2868-2897, y 5988-6008 below the plate.
  Output: poly from A east along y 5926-5947, south at x 3147-3170 round both loops, west along
  y 6228-6247, under R3, the thin metals and R2, to `tl1`'s row at x 2817.
- **The loops.** Each gate poly goes round a rectangle of bare ground east of the rail
  (x 3020-3095, y 5995-6050 and y 6125-6182) before it reaches its box. The rectangles and the
  20 px gaps between the polys are field: chip-2 stripped shot 157/152/104 inside, 159/155/103
  on open field east of the cluster, 168/158/94 in the gap (`px.py pt`). No diffusion under the
  loops was found; they are drawn as poly wires. What they are for is not known.

Evidence (commands in `cache/scratch/tl2/survey.md`):
- Clean-shot colours under R3, measured here: diffusion 200/178/137 (the VSS box away from
  its contact, the two drain strips), field 208/130/116, gate band over the box 245/175/122.
- The drain strip east of the rail is diffusion in the open: chip-2 stripped 176/154/104 at
  (3030,5950) between edges at y 5938 and 5960; the lower one the same at (3030,6073).
- The node strip of the lower unit: `px.py col 2940 5976 6160 6`: chip-2 stripped 180/135/101
  from y 6054 to 6114 between dark lines at y 6042-6048 and y 6120-6126, and field
  (165/155/95) above and below.
- Overlays: `o1.png` (clean shot, 3.3x), `o2.png` (chip-2 stripped and metal, 4.6x),
  `o3.png` (metal, 2.4x).

### The thin metals over the units

- `tla_w3376`'s metal x 2865-2877: one line from `tla`'s pad (2870,5502) south through the
  cluster and out of the strip at y 6350 (`follow.py 2870 6100 N` runs to y 5498, `S` to
  y 6374). Dim over the upper tie box (y 5981-6010), no pad, no bright centre.
- `rcs_thin_e` (thin metal E, x 2906-2920): on south from `tla`'s piece (y 5400) to a pad with
  a contact (2913,6327): bright centre in a dark ring in both metal shots and a green hole in
  the clean shot (`textmap.py 2886 6296 2946 6350 3`). From the pad a poly row runs east along
  y 6316-6337, under the VSS metal x 3257-3305 and `ur`'s metal x 3347, out of the strip at
  x 3533 (`c14.png`; `px.py row 6326 2930 3540 12`: poly colour all the way). The metal is dark
  from y 6038 to 6068 in both metal shots, over the lower tie box: no bright centre, and the
  clean shot is protected tan inside the box (`c10.png`, `textmap.py 2884 6020 2944 6090 3`):
  read as one metal passing over a buried contact (tracing guide, trap 22), not a contact and
  not a break. The follower stops on both sides of it.

### R3 and the VSS metal at its foot

R3 (x 2951-2999) runs on from `tla`'s end (y 5330) to y 6292 without a break (`px.py col 2962
5300 6310 10`: dark only at single samples where poly rows cross). At its foot a wide metal
runs east, y 6250-6292 to x 3160 and y 6238-6292 beyond, turns south at x 3257-3305 and leaves
the strip. `lc_step`'s row (`ur`) and the output row y 6228-6247 lie under or beside it without
a contact.

### The bus field's east tracks (run 2, traced 2026-11-18; wiring only)

East of the first cluster a bus field of ten vertical metal positions (pitch 43.5) carries
signals between the cluster's gates, tl1's west column (by the rows under the foot and above
the cluster) and tl3's column east of the strip. Every metal is in pieces; **every piece ends
on a pad with a contact, and from every pad a poly row leaves** east or west. Under the metals
poly of other nets runs lengthwise in three places (tracing guide, trap 10): under A, under G
and under I.

How it was read (commands and views in `cache/scratch/tl2/survey.md`):

- Pieces: `tools/follow.py` chained up each track (`cache/scratch/tl2/pieces.sh`), both chips'
  metal shots; every gap between two pieces of a track seen as plain ground at 2.6x
  (`bandA.png` .. `bandF.png`).
- Contacts: all 24 in one mosaic per shot (`pads_m.png`, `pads_a.png`, 3.2x): each has a ring
  with a bright centre in the metal shot and a green hole in a salmon pad in the clean shot.
  The other candidates of `tools/tla_contacts.py` on these tracks (F 4487, F 5528, H 2872,
  H 4047, H 4388, I 5405, J 3954, J 5399) are open ground beside a pad or a piece end: no
  ring in the metal shot.
- Rows: `tools/tl2_row.py` (a row as one line of text from the clean shot's colours: salmon
  poly under metal, dark poly in the open, pink field, green holes) for every row from x 3090
  to 3546, then an overlay of the drawn geometry on the clean shot at 2.6x over the whole field
  (`o1.png` .. `o6.png`) and on the metal shot (`om.png`).

The nets, north to south by their track piece. "Pad (x,y)" is a contact of the metal on a poly
pad.

| Net | Metal | Pads and rows |
|---|---|---|
| `tl1_w3678` | tl1's metal from the pad (2830,2811) east along y 2812 | pad (3154,2813); row east along y 2813 out of the strip (x 3533) |
| `tl1_w2637` = `tl3_w3333` | track D upper: tl1's metal from the pad (2827,2637) east along y 2640, south at x 3241 to y 3214 | pad (3240,3204); row east along y 3202 to x 3522, south (poly in the open) to y 3334, east into tl3's row y 3333: **the data of tl3's latch** |
| `rcs_bd3330` (tla) | track D middle (tla's, y 3314-4390) | its bottom pad (3237,4376), not drawn by tla; row west along y 4374 to x 3072 and on into the gate column (not traced) |
| `tl2_w3722` | track F upper, y 2630-3732 | top pad (3324,2639), row east along y 2639 out of the strip; bottom pad (3322,3722), row west along y 3722, drawn to x 3100 (it goes on west under track A into the gate column: not traced) |
| `tl3_w3982` | track F middle, y 4278-4470; track J lower, y 3972-5374 and east along y 5374 out of the strip (the follower: on to x 3607, south to (3608,5942), in tl3's strip) | F's bottom pad (3322,4460): row west along y 4461 to x 3105-3125, **south under track A** into the east end of tla's row y 4535-4558, **the gate row of tla's pass transistor at (3046,4546)** (`rcs_cond` to `rcs_cond_lat`). That row ends at x 3122 as the foot of this poly; it does **not** reach track B's pad (3152,4548), 14 px of field between, so this net is not `clk_tl` (review round 1; `tla`'s row corrected, commit 1915f94). F's top pad (3325,4287): row east along y 4285 through the pad of J's tap (3497,4287) and on out of the strip. J's top pad (3497,3982): row east into tl3's row y 3982, gate 2 of tl3's NOR 2. **Driver not found**: the net's two open ends are the row y 4285 at x 3533 and J's arm |
| `tl3_w4546` | track F lower, y 4538-5496, east along y 5496 | top pad (3322,4548), row east along y 4547 out of the strip; the arm's end pad (3518,5498), whose poly goes on east |
| `rcs_in1` (tla) | track G upper (tla's) | - |
| `tl3_w5025` | track G lower, y 5014-5424 | top pad (3368,5025), row east along y 5025; bottom pad (3368,5414), row east along y 5415; both out of the strip |
| `tl1_w3594` = `tl3_w3722` | track H upper, y 2890-3732 | top pad (3410,2899) in the middle of tl1's row y 2899, which runs on east out of the strip; bottom pad (3410,3722), row east into tl3's row y 3722: **gate 1 of tl3's NOR 1** |
| `tl3_w4763` | track H lower, y 4408-5435, east along y 5435 out of the strip (the follower: to (3571,5435)) | top pad (3410,4418), row east along y 4417 out of the strip; tap (3410,4764), row east into tl3's row y 4763 (gate 2 of tl3's NOR 4) |
| `rcs_g3245` (tla) | track I upper, y 2674-3256 | bottom pad (3452,3246) at the east end of tla's row y 3246; top pad (3454,2683), row east along y 2683 out of the strip |
| `rcs_x1` = `rcs_g4240` = `tl1_w4025` = `tl3_w3506` | track I lower, y 3494-5380: one metal, four contacts | top pad (3454,3504): its poly runs south (x 3446-3470) into the east end of tla's row y 3547 (`rcs_x1`; the row ends there) and east into tl3's row y 3506 (**the clear of tl3's latch**). Tap (3452,4199): poly west by a step (x 3402-3426, in the open) down to tla's row y 4240 (`rcs_g4240`), and east along y 4201 out of the strip. Tap (3452,5112): row east along y 5110 out of the strip. Bottom pad (3454,5371) in the middle of tl1's row y 5371 (`tl1_w4025`, **the clear of tl1's two latches**), which runs on east under J's arm out of the strip |
| `tl3_w3419` = `tl3_w3896` | track J upper, y 3408-3904 | top pad (3497,3418), row east into tl3's row y 3419 (the inverted output of tl3's latch); bottom pad (3497,3894), row east into tl3's row y 3896 (gate 1 of tl3's NOR 2) |
| `tl3_w3939` | none (poly) | tl3's row y 3939 (NOR 2's output) comes west to x 3460, runs **south under track I** (x 3451-3469) to y 4111 and east again out of the strip |
| `tl3_w4373` | none (poly) | a U open to the east: row y 4374 from x 3364, a vertical **under track G** (x 3364-3380) to y 4503, row y 4503; both rows out of the strip |
| `rcs_a2` = `tl3_w3765` | none (poly) | tla's row y 3761 from the pad (3103,3762) on track A, drawn by tla to x 3400, runs on east into tl3's row y 3765: **the output of tl3's NOR 1** |
| `tl1_w2857` | none (poly) | tl1's row y 2857, straight east through the strip, no pad |
| `tl1_w4937` | none (poly) | tl1's row y 5458 under the foot, straight east through the strip, no pad |

What follows from the joins (extracted, all on geometry without `?`):

```
rcs_a2    = NOR(tl1_w3594, tl3_w3803)       FIRM   (tl3's NOR 1; rcs_a2 is an input of rcs_c1, rcs_b1)
tl3_w3939 = NOR(tl3_w3419, tl3_w3982)       as in tl3 (NOR 2); tl3_w3982 is also the gate of the pass transistor
                                            rcs_cond -> rcs_cond_lat at (3046,4546), which tla had on clk_tl
rcs_b1    = NOR(rcs_a2, rcs_u3425, rcs_x1)         x1 is the common clear
rcs_n4200 = NOT((clk_tl AND rcs_cond) OR rcs_x1)
tl3_w3550 = NOT(rcs_x1 OR (tl3_w3233 AND tl3_w3373) OR tl3_w3419)     tl3's latch, cleared by x1
tl1_w4070, tl1_w4678 = NOT(rcs_x1 OR ...)                             tl1's two latches, cleared by x1
tl3_w3419 = NOT((tl1_w2637 AND tl3_w3373) OR tl3_w3550)               tl3's latch takes tl1_w2637
```

So one signal (`rcs_x1`) clears three latches (two in tl1's column, one in tl3's), forces
`rcs_b1` and `rcs_n4200` low, and has its driver east of the strip on one of three rows
(y 4201, 5110 or 5371 at x 3533: after the merge with main only y 5371 is left, see below); `tl1_w3594`, the enable of tl1's second latch, is also an
input of the NOR that makes `rcs_a2`. **Believed, not traced**: nothing about what these
signals are.

The junctions that decide these joins, each looked at above 4x in two shots or measured:

- **Track I's top pad and the end of `rcs_x1`'s row** (`j_itop.png`, 4.8x, metal and clean
  shot): the pad (hole at (3454,3505)), the poly south of it and the row y 3538-3556 are one
  salmon shape with one outline; east of x 3470 the row's line is field (`tl2_row.py row 3547`).
- **The step from track I's tap (3452,4199) down to `rcs_g4240`'s row** (`j_i4200.png`, 4.2x,
  chip-2 stripped and clean shot): poly in the open (dark red in the clean shot, orange in the
  chip-2 shot) from the pad's west side at x 3437 west to x 3402 and south to the row y 4240.
  Between the open poly and the pad a single dark line 6 px wide at x 3430-3436 in both shots
  (`px.py row 4198 3396 3472 4 acid1b,acid`): the edge of the metal pad's protected area, not
  two outlines with field between (see Ambiguities).
- **The poly under track A** (`c1.png`, `c3.png`, 3.8x and 4.2x, three shots; `px.py col 3115
  4440 4570 6`): salmon 220/170/122 without a break from y 4458 to 4548, into the east end of tla's
  row; pink field above y 4452 and below y 4558.
- **That row and track B's pad (3152,4548) are apart** (review round 1, confirmed by the tracer):
  `px.py col 3129 4436 4576 5 all` down the gap between tracks A and B: both metal shots are
  plain ground, R = G = 104-116, from y 4481 to 4556, with no edge line at y 4535 or y 4558
  (the row y 4461 in the same gap is orange, 151-170/119-126/55-62, between two dark lines);
  the clean shot is green, 136-144/161-165/90, like the field above and below.
  `px.py row 4547 3096 3172 4 all`: salmon to x 3116, green at x 3120-3132, the pad's rim from
  x 3136. `review-2/j_band1gap.png` (7x, four shots): the pad's outline is closed on its west side.
- **The row y 4285 between F's pad and J's pad** (`c2.png`, 5x, three shots): one band; dark
  and speckled where no metal lies over it (x 3388-3440), orange with a continuous outline in
  the chip-2 stripped shot.
- **G's lower top pad and `rc_stepreq_n`'s poly under track F** (`pads_a.png` tile 9, `o4.png`):
  the pad's west edge is at x 3352, the poly's east edge at x 3334, pink and a green rim
  between. Not joined.
- **The two U-shaped polys** (`o2.png`, `o3.png`; `px.py row 4440 3344 3396 4`: 213-221/152-160
  under track G against 191-198/107-117 on field under the same metal at y 4320).

**Joins made when main was merged (2026-11-18 01:15 +0000).** While this run was in review, `tl3`'s later runs
reached main with rows drawn from x 3533 east at the same places where this run's rows arrive
from the west. Nine of them meet (y within 2 px, both sides drawn to the shared edge), and the
extraction joins them. Each row was checked to be one poly across the edge
(`tools/t.sh tl2 tl2_row.py row Y 3500 3600 --step 2` for y 4111, 4201, 4285, 4374, 4416, 4503,
4547, 5025, 5110: poly without a break from x 3500 to x 3600; the first review had found that
every row of this run reaches x 3540 or beyond). No `?` item lies on any of them, and an independent reviewer has since checked all nine against
the photos (Review, run 2, round 3: no findings). Names: where
this run had a placeholder of its own, tl3's name is used instead (`tl3_w4546`, `tl3_w5025`,
`tl3_w4373`, which replace this run's first names for track F's lower piece, track G's lower
piece and the U-shaped poly); the rest are aliases in `trace/tl2.txt`:

| tl2's row (x 3533) | tl3's row | So |
|---|---|---|
| y 4111, lower arm of `tl3_w3939`'s loop | `tl3_w4112`, gate of the pair's upper unit | `tl3_w3803` = NOR(`tl3_w3939`, `tl3_w4243`): NOR 2's output resets the pair |
| y 4201, from track I's tap (`rcs_x1`) | `tl3_w4200`, the pair's lower unit, gate 1 | `tl3_w4243` = NOR(`rcs_x1`, `tl3_w3803`, `tl3_w3982`) |
| y 4285, from track J's tap (`tl3_w3982`) | `tl3_w4290`, the pair's lower unit, gate 2 | the same equation |
| y 4374, upper arm of the U | `tl3_w4373`, the inverter's output | the U takes it to the row y 4503 |
| y 4417, from track H's lower top pad (`tl3_w4763`) | `tl3_w4414`, the inverter's input | `tl3_w4373` = NOT `tl3_w4763` |
| y 4503, lower arm of the U | `tl3_w4503`, NOR 3 gate 1 | `tl3_w4546` = NOR(`tl3_w3803`, `tl3_w4373`) |
| y 4547, from track F's lower top pad | `tl3_w4546`, NOR 3's output | it goes down track F's lower piece to the pad (3518,5498) and on east |
| y 5025, from track G's lower top pad | `tl3_w5025`, latch B's inverted output | it goes down track G's lower piece to the row y 5415 and on east |
| y 5110, from track I's tap (`rcs_x1`) | `tl3_w5112`, the clear of latch B | **`rcs_x1` clears a fourth latch**, and resets the cross-coupled pair that makes `tl3_w3803` |

So `rcs_a2` = NOR(`tl1_w3594`, `tl3_w3803`) with `tl3_w3803` one side of a set-reset pair:
`tl3_w3803` = NOR(`tl3_w3939`, `tl3_w4243`), `tl3_w4243` = NOR(`rcs_x1`, `tl3_w3803`,
`tl3_w3982`) (marked in tl3: one `?` join inside the pair), and `tl3_w3939` =
NOR(`tl3_w3419`, `tl3_w3982`). `rcs_x1`'s driver can now only be on the row y 5371 east of
x 3533: its other two rows end on gates.

Not drawn by `tla` and seen here, in the part of its gate column that nobody has traced
(x 2860-3100, y 3700-4620): track B's contacts at (3150,3812) and (3150,4418), each on a pad
whose row runs west into the column (`o2.png`, `o3.png`). `tla`'s notes list them as gate
contacts of `clk_tl`; they are not in its trace. (Its fourth, (3152,4548), gates nothing: the
pad's only poly goes east to track D's pad (3228,4548).)

### The gate column east of R3 (run 3)

#### Piece 1: two more pull-downs on `rcs_bc3460` (traced 2026-11-18; 2 transistors)

Between `tla`'s VSS box at y 3655-3725 (contact (2985,3690)) and its VSS box at y 3795-3835
(contact (2978,3815)) the column east of the rail (x 3022-3068) holds one more unit of the
cluster's kind, but without a load:

- **VSS link.** A diffusion strip y 3696-3709 from the upper VSS box east across the rail's edge
  to the top of the column.
- **Gate 1, `tl2_w3722`** (the row y 3712-3733 from track F's bottom pad (3322,3722)): on west
  under track A without a contact, across the column, west end at x 3012-3018. W/L 46/21.
- **Node box**, x 3022-3068, y 3737-3793.
- **Gate 2, `clk_tl`** (the row y 3798-3817 from track B's top pad (3150,3812), contact on
  `tla`'s metal): across the column, west end x 3010. W/L 46/19. Below it the column meets
  `tla`'s VSS arm (y 3818-3836) of the lower box.
- **The node's strip.** From the node box an arm runs west under R3 (y 3757-3777) to x 2915,
  turns south and runs along x 2915-2935, under the east margin of thin metal E, to y 3882,
  where it enters `tla`'s node box of `rcs_bc3460` (x 2898-2932, y 3882-3915). The strip and
  that box are one diffusion; the box ends at y 3910.

So the unit is the second half of a four-input NOR whose first half and load are `tla`'s unit
at y 3892: `rcs_bc3460` = NOR(`rcs_e3`, `rcs_e4`, `tl2_w3722`, `clk_tl`) (extracted; no `?`
item of this package on it). What follows for `tla`'s step formula, with u = `rcs_u3425` =
NOT `rcs_bc3460`: `rcs_b1` = NOR(`rcs_x1`, `rcs_a2`, u), `rcs_c1` = NOT `rcs_a2` AND (`rcs_x1`
OR u), `rcs_in2` = `rcs_c1` AND NOT `rcs_e4`, `rcs_in3` = NOR(`rcs_e3`, `rcs_e4`), and step =
`rcs_in1` OR `rcs_in2` OR `rcs_in3`. While `rcs_e3` is high u is high whatever the new inputs
are, and while it is low `rcs_in3` decides: the step is still `rcs_in1` OR (NOT `rcs_e4` AND
NOT (`rcs_e3` AND `rcs_a2`)). The new inputs matter only for `rcs_c1` (which also leaves the
cluster west on the poly y 2985) and for `rcs_b1`. **Believed, not traced**: nothing about what
`tl2_w3722` is (its other end is the row y 2639 east out of the strip).

Evidence (views in `cache/scratch/tl2/`, all with `TRACE=tl2,tla,tl1`):

- The column in the open, decided in the chip-2 stripped shot (trap 18):
  `tools/t.sh tl2 px.py col 3046 3640 3850 5 acid1b,acid,metal`: diffusion (166/146/93) at
  y 3655-3660 (`tla`'s arm), **field** (151/149/87) at y 3675-3685, diffusion (160/140/92) at
  y 3698-3708, orange poly y 3712-3733, diffusion (163-167/139-146/92-99) y 3742-3792, poly
  y 3798-3819, a narrow band y 3828-3837, then `tla`'s gate of `rcs_e3`. So the diffusion above
  gate 1 is not the column of `rcs_b1`'s unit continued: it is a strip of its own, 12 px high.
  Views: `p1_col.png` (4.6x, chip-2 stripped, clean, metal), `p1_rows.png` (4.4x, chip-2 stripped
  over metal, x 3000-3190): both gate bands cross the column's two edge lines (x 3020, x 3070).
- **The two joins across the rail's east edge** (the VSS link at y 3700, the node arm at y 3766)
  are each crossed by one dark line, the rail-edge line of that shot, and the two chips have it
  at different x, so each shot shows diffusion where the other is dark:
  `px.py row 3766 2996 3030 2 acid1b,acid,metal,metal1`: clean shot tan (199-203/173-176/129-135)
  to x 3008 and dark at x 3012-3018; chip-2 stripped dark at x 3006-3010 and diffusion
  (144-172/103-144/90-102) from x 3014. `px.py row 3700 2996 3074 4 acid,metal,acid1b`: clean
  shot tan to x 3008, dark x 3012-3024; chip-2 stripped dark x 3008-3012, diffusion
  (140-165/121-145/86-97) from x 3016 to x 3060; `px.py col 3018 3684 3716 2 acid,metal,acid1b`:
  the link is y 3695-3703 there in both chip-2 shots. On `p1_col.png` the node box's outline
  opens west into the arm (rounded corners at (3018,3752) and (3018,3780)).
- **The strip under the rail and under thin E is diffusion, not poly** (`railprof.py` calls it
  poly over field): `px.py row 3766 2896 3080 6`: clean shot 195-202/173-178/127-135 from x 2944
  to x 3004 (diffusion under metal here is 200/178/137, poly 220/170/122, field 208/130/116);
  `px.py col 2975 3736 3800 4`: the band is y 3758-3774 between dark lines; `px.py col 2925
  3740 3920 6` and `px.py col 2924 3866 3900 2 acid1b,acid,metal,metal1`: tan
  (198-209/167-185/130-139) from y 3764 to y 3900 without a dark sample, into `tla`'s box; the
  box's bottom edge is the dark line at y 3910. Views: `p1_L.png` (4.4x, three shots, x 2850-2950,
  y 3740-3920), `p1_tie.png` (the same lower down, no overlay).
- **No contact of track A on gate 1's row**: `textmap.py 3084 3700 3132 3745 3`: the metal is
  bright (A-D) over the row's whole height in both chips, the clean shot is protected poly
  (5-8) with no `g` hole; dark bars only at the row's two edges.
- **Track B's top pad (3150,3812)**: a bright centre in a dark ring at the metal's end in the
  metal shot, a rounded box with pits in the chip-2 stripped shot (`p1_rows.png`), and the row's
  outline runs into the pad's.
- Overlay: `p1_ov.png` (2.2x, chip-2 stripped | clean with the trace).

Seen beside the piece and not drawn (they are `tla`'s): the load plate of `rcs_bc3460`
(x 2850-2897, y 3862-3925) has a tab at its **top** right (x 2868-2900, y 3830-3862) that ends
in a heavy-outlined oval box (x 2898-2925, y 3850-3878) on the node's strip: the load's tie.
`tla` draws that tie at the plate's **bottom** (`B 2908,3932:2932,3959`, with a tail
`D 2913,3911:2929,3957` and the plate down to y 3960), where both stripped shots show field
(`p1_tie.png`). The connection is the same (plate on its node); the geometry is not. Thin metal
E over the oval is bright and wide at y 3844-3856, dark at y 3832-3841 and y 3874-3880
(`textmap.py 2884 3790 2944 3915 3 --acid`), like `tla`'s other ties under it (compared with
`textmap.py 2884 4600 2944 4672 3` and `2884 5222 2944 5282 3`): read, as `tla` does, as passing
over.

## Ports

| Name | Layer | Where | Dir | What |
|---|---|---|---|---|
| `tl1_w6022` | P | x 2817, y 6187-6203 | in | the third latch's output (`tl1`): the lower inverter's gate |
| `tl1_w5936` | P | x 2817, y 6228-6247 | out | the upper inverter's output, on to `tl1`'s row and the metal x 2500 |
| `tla_w3376` | M | x 2865-2877, y 6350 | ? | thin metal on south |
| `rcs_thin_e` | P | x 3533, y 6316-6337 | ? | row east from the pad (2913,6327) |
| `vss` | M | x 3257-3305, y 6350 | - | the metal from R3's foot, on south |
| `tl1_w2857` | P | x 2817, y 2848-2866 | out | row y 2857 to tl1's gates; comes through the strip from the east |
| `tl1_w3594` | P | x 2817, y 2890-2908 | out | row y 2899 to tl1's gates; pad (3410,2899) of track H's upper piece on it |
| `tl1_w3678` | M | x 2848, y 2803-2821 | out | tl1's metal from the pad (2830,2811), on east to a pad (3154,2813) |
| `tl1_w2637` | M | x 2845, y 2631-2649 | in | tl1's metal from the pad (2827,2637), on east and south (track D upper) to tl3's latch data |
| `tl1_w4025` | P | x 2817, y 5362-5380 | out | row y 5371 to tl1's metal x 2457 (the clear of tl1's two latches); one net with rcs_x1 (alias) |
| `tl1_w4937` | P | x 2817, y 5449-5467 | out | row y 5458 to tl1's metal x 2370; comes through the strip from the east |
| `tl2_w3722` | P | x 3533, y 2630-2648 | ? | row y 2639 east from track F's top pad (3324,2639) |
| `rcs_g3245` | P | x 3533, y 2674-2692 | in | row y 2683 east from track I's top pad (3454,2683); the net's known end is a gate in tla |
| `tl1_w3678` | P | x 3533, y 2804-2822 | in | row y 2813 east from the pad (3154,2813) |
| `tl1_w2857` | P | x 3533, y 2848-2866 | in | row y 2857, straight through |
| `tl1_w3594` | P | x 3533, y 2890-2908 | ? | row y 2899 east of track H's pad; every known end is a gate |
| `tl1_w2637` | P | x 3540, y 3325-3343 | out | onto tl3's row y 3333 (tl3_w3333, the latch's data): alias |
| `tl3_w3419` | P | x 3540, y 3410-3428 | in | tl3's row y 3419 (the latch's inverted output) to track J's upper piece |
| `rcs_x1` | P | x 3540, y 3497-3515 | out | onto tl3's row y 3506 (tl3_w3506, the latch's clear): alias |
| `tl1_w3594` | P | x 3540, y 3713-3731 | out | onto tl3's row y 3722 (tl3_w3722, NOR 1 gate 1): alias |
| `rcs_a2` | P | x 3540, y 3755-3773 | in | tl3's row y 3765 (tl3_w3765, NOR 1's output) onto tla's row y 3761: alias |
| `tl3_w3419` | P | x 3540, y 3886-3904 | out | from track J's upper piece onto tl3's row y 3896 (tl3_w3896, NOR 2 gate 1): alias |
| `tl3_w3939` | P | x 3540, y 3930-3948 | in | tl3's row y 3939 (NOR 2's output), west to x 3460, south under track I |
| `tl3_w3982` | P | x 3540, y 3973-3991 | out | from track J's lower piece onto tl3's row y 3982 (NOR 2 gate 2) |
| `tl3_w3939` | P | x 3533, y 4102-4120 | out | the same poly back east along y 4111 |
| `rcs_x1` | P | x 3533, y 4192-4210 | ? | row y 4201 east from track I's tap (3452,4199) |
| `tl3_w3982` | P | x 3533, y 4276-4294 | ? | row y 4285 east of track J's tap (3497,4287) |
| `tl3_w4373` | P | x 3533, y 4365-4383 | ? | upper arm of the U-shaped poly under track G |
| `tl3_w4763` | P | x 3533, y 4408-4426 | ? | row y 4417 east from track H's lower top pad (3410,4418) |
| `tl3_w4373` | P | x 3533, y 4494-4512 | ? | lower arm of the U-shaped poly |
| `tl3_w4546` | P | x 3533, y 4538-4556 | ? | row y 4547 east from track F's lower top pad (3322,4548) |
| `tl3_w4763` | P | x 3540, y 4755-4773 | out | from track H's tap (3410,4764) onto tl3's row y 4763 (NOR 4 gate 2) |
| `tl3_w5025` | P | x 3533, y 5016-5034 | ? | row y 5025 east from track G's lower top pad (3368,5025) |
| `rcs_x1` | P | x 3533, y 5101-5119 | ? | row y 5110 east from track I's tap (3452,5112) |
| `rcs_x1` | P | x 3533, y 5362-5380 | ? | row y 5371 (tl1_w4025's) east of track I's bottom pad, under track J's arm |
| `tl3_w3982` | M | x 3533, y 5365-5383 | ? | track J's arm east along y 5374 (follow.py: to x 3607, then south to (3608,5942)) |
| `tl3_w5025` | P | x 3533, y 5406-5424 | ? | row y 5415 east from track G's bottom pad (3368,5414) |
| `tl3_w4763` | M | x 3533, y 5426-5444 | ? | track H's arm east along y 5435 (follow.py: to (3571,5435)) |
| `tl1_w4937` | P | x 3533, y 5449-5467 | in | row y 5458, straight through |
| `tl3_w4546` | P | x 3538, y 5482-5514 | ? | the pad (3518,5498) at the end of track F's arm; its poly goes on east |
| `rcs_bd3330` | P | x 3072, y 4365-4383 | ? | row y 4374 west from track D's pad (3237,4376); on west into the gate column |

## Ambiguities

1. **The lower unit's tie box under thin metal E** (2895-2927, 6042-6062). Thin E is dark
   over it for 30 px. Read as a pass-over (see above). If it were a contact, `rcs_thin_e`
   would be `tl2_w6070`; if the metal were cut there, the pad (2913,6327) and its row would be
   on another net than `tla`'s `rcs_thin_e`. Working assumption: one metal, no contact.
2. **The upper unit's node lies under thin metal E** (x 2897-2930, y 5935-6005) and
   `follow.py` gives a contact candidate (2912,5983). The metal dims there only from C-D to
   9-A (chip 2) with no ring, and not at all in chip 1; the clean shot is protected tan with
   no green hole. No contact drawn.
3. **The loops** are drawn as poly on field. A diffusion narrower than the poly under them
   (which would make each a long transistor) cannot be excluded from colour alone; the field
   colour of the rectangles and gaps, and the two units being complete without it, speak
   against it.
4. The joins of the lower node strip and of the two strips east of the rail to the diffusion
   under the rail are hidden by a rail-edge line in every shot (review round 1); drawn joined on
   the continuity of their outlines.
5. Sizes: the pull-downs' W (47) is the VSS box's width; the lower load's strip is read from
   the brighter band of the plate (y 6093-6120). No connection depends on these.
6. **The step between track I's tap pad (3452,4199) and `rcs_g4240`'s row** (run 2). The open
   poly of the step and the pad under the metal meet at a single dark line 6 px wide (x 3430-3436,
   both stripped shots). Read as the edge of the pad's protected area across one poly (tracing
   guide, trap 2); two polys abutting would need two outlines and field between, about 15 px.
   Drawn joined, without `?`. If it were a gap, `rcs_g4240` would be a net of its own with no
   driver found (its row ends there), and `rcs_n4200` would not be cleared by `rcs_x1`.
7. **Where the poly rows go on at x 3533** (run 2): each row was followed to x 3546 in the clean
   shot's colours (`tools/tl2_row.py`) and drawn to x 3533, or to x 3540 where tl3 has drawn
   the row's other part. The rows tl3 has not drawn (y 2639, 2683, 2813, 2857, 2899, 4201, 4285,
   4374, 4417, 4503, 4547, 5025, 5110, 5371, 5415, 5458, the pad (3518,5498)) pass under tl3's
   metal x 3540; whether any has a pad there was not looked at (tl3's strip).
8. Widths (run 2): rows are drawn 18 wide on their measured centres (the salmon core measures
   9-12), metals 18, pads 42 x 34. No connection depends on these.

## Review

Round 1 (full review, 2026-11-17 22:41 +0000, a fresh agent on claude-fable-5-2, at commit
7886411; 11 images in `cache/scratch/tl2/review-1/`). Piece: the small cluster's east half
with R3, the VSS metal and the two thin metals. Told to suspect: thin metal E dark over the
lower tie box (contact, break or pass-over), the follower's contact candidates (2912,5983) and
(2867,5980), diffusion under the loops and the boxes A and B, the lower node strip and its
joins, the upper drain strip under the rail, the lower load and its VCC box, the two rows
between x 2817 and x 3010, the pad (2913,6327) and its row.
It checked, at 3.3x and more in two or three shots and with text maps and profiles: thin E over
the tie box (pass-over: no bright centre, no pad, protected tan inside, green minus red at most
+1 against +44 and +52 at two real contacts); both candidates (not contacts); the lower node
strip (a feature in three shots; the gate's west end stays under the rail); both pull-downs;
the strips to A and B (diffusion, continuous) and the loops (plain poly on field, no edge
lines across them); the lower VCC box, contact and strip; both rows (continuous, no rings in
the chip-2 shots); R3 to its foot and the VSS metal (no contact to the rows); the pad
(2913,6327) (a contact) and its row to x 3530; the extraction, `opendiff.py`, `unsure.py`,
the ports at x 2817.
Findings, both geometry only, both checked by the tracer and fixed:
1. The upper load plate's west edge is at about x 2840, not 2848: confirmed (`px.py row 5950
   2834 2858 3`: chip-2 stripped 171/145/67 at x 2846, the edge at x 2840); drawn from x 2842.
2. The VSS contacts lie a few px east of where they were drawn: the clean shot's hole is at
   (2987,6011) for the upper one (94/127/84), and the metal shots' ring at about (2990,6146)
   for the lower; moved to (2986,6011) and (2988,6144).
Could not be checked: the joins of the lower node strip and of the two strips east of the rail
to the diffusion under the rail (a rail-edge line hides each in every shot; they rest on
outline continuity); the chip-2 stripped shot in the narrow gaps between the metals (fringes);
x 3200-3533 north of y 6215 was not surveyed.
`tools/t.sh tl2 sameconn.py 7886411`: `connections identical`.
`.venv/bin/python tools/sameconn.py 7886411`: `connections identical`.

Round 1: no findings that change a connection.

### Run 2 (the bus field's east tracks)

Round 1 (full review, 2026-11-18 00:58 +0000, a fresh agent on claude-fable-5-2, at commit 132750c; 14 images in
`cache/scratch/tl2/review-2/`). Piece: the bus field's east tracks (everything run 2 added to
`trace/tl2.txt`). Told to suspect: the step from the tap (3452,4199) to the row y 4240 (one poly
or two that abut); the poly under track A (does it reach tla's row, does it contact A); the top
pad (3454,3504) and the end of the row y 3547; the row y 4285 between F's and J's pads; the pad
(3368,5025) against the poly under track F; the two U-shaped polys; the four mid-piece taps and
hidden breaks or undrawn contacts on the long pieces; taps on the rows where other tracks cross
them; whether each row drawn to x 3533 reaches it; track D's upper piece and the row y 3202's
corner.
It checked, with text maps and profiles throughout and the junctions at 4-7x in three or four
shots: every metal end, corner and gap (all gaps bare); all 24 contacts (real, none missing on
any track, the four taps one metal through); the step at (3452,4199) (one poly: orange up to the
ring in both metal shots, the dark line at x 3430-3436 is the pad-edge line, the same at x 3474);
the pad (3454,3504) (its poly reaches the row y 3547, which ends at x 3470); the row y 4285
(continuous); the pad (3368,5025) (apart from the poly under F: green field at x 3340-3350); both
U polys (corners joined, no contact to G or I, J's pad (3497,3982) 15 px clear); the F and H pads
on y 3722 and the D and F pads on y 4548 (apart); J's arm over the row y 5371 (no contact); no
tap under any crossing track; every row drawn to x 3533 reaches x 3540 or beyond; the joins
into tl3 at y 3334, 3419, 3506, 3722, 3765, 3896, 3982, 4763; nothing undrawn in x 3085-3540.
One finding, which **changes a connection**:
1. `tla`'s row `P 3018,4535:3140,4558` (the gate row of the pass transistor at (3046,4546)) was
   drawn through to track B's pad (3152,4548), which is `clk_tl`. The row ends at x ~3121 as the
   foot of the poly under track A; the gap x 3122-3138 is field. So the poly under track A,
   track F's middle piece, track J's lower piece and `tl3_w3982` are not `clk_tl`, and neither
   is the pass transistor's gate. **Confirmed by the tracer** (`px.py col 3129 4436 4576 5 all`,
   `px.py row 4547 3096 3172 4 all`, `review-2/j_band1gap.png`: see "The junctions that decide
   these joins"). Fixed: `tla`'s row cut at x 3122 in a commit of its own (1915f94); in
   `trace/tl2.txt` the alias `clk_tl` = `tl3_w3982` removed and the net labelled `tl3_w3982`;
   notes, ports, glossary and `notes/operation.md` corrected. The pass transistor
   `rcs_cond` -> `rcs_cond_lat` is now gated by `tl3_w3982`.
Could not be checked: anything east of x 3547 (where J's arm goes); the rows y 3722 and y 4374
west of x 3085 and x 3072; tla's row between x 3018 and x 3085.

Round 1: one finding, fixed.

Round 2 (fix check, 2026-11-18 01:10 +0000, a fresh agent on claude-fable-5-2, against commit 132750c; 8 images in
`cache/scratch/tl2/review-3/`). Told what changed (tla's row cut at x 3122; the alias removed and
the net labelled `tl3_w3982`) and the finding it fixes. It checked, like for like against the row
y 4461 that does cross the same gap 85 px north: (a) no poly between x 3122 and the pad in any of
the four shots (clean: continuous green 132/163/86 from y 4512 to 4572, then pink to the pad's
outline at x ~3138; chip-2 stripped: the pad's outline at x 3132 unbroken from y 4520 to 4556;
both metal shots: plain ground, no edge lines at y 4535 or 4558); (b) the shortened row is one
poly from about x 3012 to 3122 and the foot of the poly under the bus metal is its east end
(it ends at about y 4554, 22 px of field before the pad of (3105,4590)); (c) the pad (3152,4548)
has no poly west, north or south, only the one east; (d) no other connection on the gate row: no
ring in the metal x 3108 and no green hole from y 4452 to 4556, field on both sides, and the row
does not go on west under the rail. `sameconn` against 132750c (3 differences for the package, 19
with every file): all are the `clk_tl` / `tl3_w3982` split.
One finding, geometry only (a comment): `trace/tla.txt`'s comment above the column still said
"gate clk_tl" and "while clk_tl is high". Confirmed and corrected in a commit of its own (fa2a849).
`tools/t.sh tl2 sameconn.py c260164`: `connections identical`.
`.venv/bin/python tools/sameconn.py c260164`: `connections identical`.

Round 2: no findings that change a connection.

Round 3 (check of the joins made at the merge, 2026-11-18 01:37 +0000, a fresh agent on claude-fable-5-2, against
commit 754f269; 8 images in `cache/scratch/tl2/review-4/`; asked for by the user after the merge).
No geometry of `tl2` had changed since round 2: what changed is that tl3's rows, drawn from x 3533
east, now meet nine of this run's rows, so that the extraction joins the nets ("Joins made when
main was merged"). Told to suspect: a break or an outline across a row under tl3's metal
x 3532-3548, which lies right over the boundary; a row stepping one track under that metal; a
contact from one of the rows to that metal; whether tl3's part of each row reaches the gate it
is drawn to. It checked: each of the nine rows is one poly from x 3480 to its target in tl3 (an
unbroken salmon band at constant y under the metal, x 3518-3562, in text maps at step 2 of all
nine crossings; east of it continuous in the chip-2 metal shot and both stripped shots at 4x,
with colour tables against field rows); no track step (column profiles at x 3520 and x 3575 show
the same rows at the same y: 4111, 4201, 4285, 4374, 4415, 4503, 4547, 5025, 5111; none ends or
starts under the metal); no contact to the metal x 3540 on any row, compared with the real
contact (3540,4590) (three spots looked at and dismissed: (3544,4287), a ring in the chip-2
metal shot only; (3540,4421), a paler patch in the clean shot with no ring in either metal shot;
(3547,4545), dirt on chip 2); on tl3's side rows 1-3, 6 and 9 reach the diffusion edge near
x 3595, rows 4, 7 and 8 their buried-contact boxes, and row 5 runs on past x 3640.
No finding. Two notes of the reviewer's, neither in this package's files: tl3's rectangle for the
row y 4281-4299 sits about 4 px low (the band is y 4277-4294); `tl3_w3803` = NOR(`tl3_w3939`,
`tl3_w4243`) still rests on tl3's own `?P 3704,4182:3728,4204`, independently of these joins.

Round 3: no findings.

## Not done

- **The gate column x 2860-3100, y 4320-4620** (`tla`'s east column where `tla` did not trace
  it; run 3's piece 1 did y 3690-3840): gates on the row y 4374 (`rcs_bd3330`, from track D's pad
  (3237,4376), drawn to x 3072), the row y 4418 from track B's undrawn contact (3150,4418)
  (`clk_tl`, by `tla`'s notes), and a band y 4458-4480 under R3 west of `rcs_cond_lat`'s pad
  (3045,4485); an undrawn pad with a green hole at (2862,4385) under the south end of
  `rcs_n4200`'s thin metal. `tools/t.sh tl2 railprof.py 2953 3001 3650 4680`: diffusion
  y 4449-4463, gate y 4464-4488, diffusion y 4489-4508 under the rail, drawn by nobody. Views:
  `s3_b.png` (2.1x), `s3_b2.png` (3.3x, both stripped shots).
- **North of y 2630**: the horizontal metals along y 2556 and y 2598 and the plane above them
  (`tools/follow.py` from (3326,2602) and (3326,2560): corners in `cache/scratch/tl2/survey.md`),
  tl1's metals east of (2852,2553) (`tl1_w3333`) and the pad at about (2867,2595) (`tl1_w2592`),
  the tops of tracks A-C.
- The rows that leave east at x 3533 and the two metal arms (ports table): their far ends are
  in tl3's strip. `rcs_x1`'s driver is east of x 3533 on the row y 5371 (the rows y 4201 and y 5110 end on tl3's gates); `tl3_w3982`'s on track J's arm.
- A poly bar in the open along y 5655-5670 from x 3212 east (`ft_a.png`), south of `amr_eq_r3`'s
  row: not looked at.
- `tla`'s bus pieces: tracks A-E are complete in `tla`'s trace between y 2940 and y 5700 as far
  as the follower shows (`cache/scratch/tl2/pieces_AE.txt`), except track B's two contacts above.
- The rows under the foot east of x 2817 are done (y 5371, 5458 by run 2; the others by `tla`,
  `bw`, `amrw`).
- `rcs_thin_e`'s row east of x 3533 (towards its driver) and `tla_w3376`'s metal south of
  y 6350.
- The VSS metal south of (3281,6350).
