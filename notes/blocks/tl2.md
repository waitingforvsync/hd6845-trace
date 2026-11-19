# tl2: top-left random logic, the second strip (x 2817-3533, y 2500-6350)

Package `tl2` (part 2 of 6 of the top-left logic). Trace: `trace/tl2.txt`. Views:
`cache/scratch/tl2/`. Most of the strip is `tla`'s east gate column on rail R3 (VSS,
x 2950-3000; traced, `notes/blocks/tla.md`) and the bus field east of it. This package draws
what `tla`, `tl1`, `r9m` and `ur` did not. Nothing of theirs is redrawn.

## Status

2026-11-18 12:33 +0000 (run 5, Tom Seddon). **Partial: the wiring north of y 2630 drawn** (piece 5;
wiring only, no transistor), and the "poly bar" of Not done looked at (nothing there). Three
things were undrawn north of the cluster, east of `tl1`'s pads:

```
tl1_w3333   metal y 2554 from tl1's pad (2826,2553) east to a pad (3453,2553); poly NORTH from the pad,
            x 3450-3470, out of the strip at y 2500: the third latch's data comes from the band north of the strips
tl1_w2592   tl1's row y 2591 on east to a pad (2868,2596); metal east along y 2598, north at x 3503,
            east along y 2509 out of the strip at x 3533
vss         the east arm (y 2893-2948) of tl1's wide metal x 2733-2785 is one metal with the top of R3
```

No uncertain item on any of them. R3 therefore hangs from the same VSS plane as R1 (`tl1`'s
notes: the plane's lower edge at y 2507; drawn here east of `tl1`'s piece to its end at x 3388).
Full extraction: 2346 nets, 4158 transistors, 0 errors, 0 warnings.

2026-11-18 11:00 +0000 (run 4, Tom Seddon). **Partial: `rcs_cond_lat`'s poly followed to its end, and the
junction of AMB-009 re-read** (pieces 3 and 4; 2 transistors added, one of `tla`'s changed
from a pass transistor to a pull-down). The poly that `tla` left "not followed" west under R3
at y 4010-4030 is the gate poly of the load of an undrawn inverter between R2 and R3
(y 4005-4145), whose pull-down is gated by the west end of `rcs_cond`'s band:

```
tl2_w4080    = NOT rcs_cond                    piece 3: the inverter's node. Marked: only the load's tie is uncertain
rcs_cond_lat = tl2_w4080                       through that tie (`?`, as every load tie of the cluster): an alias
rcs_cond     = NOR(rcs_cond_n, tl3_w3982)      piece 4: tla had NOT rcs_cond_n and a pass transistor. FIRM
```

So `rcs_cond_lat` is not a dynamic latch node: it is the output of a static inverter,
NOT `rcs_cond`. The junction that made it one (AMB-009: a buried contact from the top of
`tla`'s column at (3045,4515) to the pad at the foot of `rcs_cond_lat`'s metal) is not there: the
column's top is a diffusion band that runs west to the VSS box of piece 2, with a strip of
field between it and the pad (both chip-2 shots and the chip-1 metal shot). The band of
`tl3_w3982` is therefore a second pull-down of `rcs_cond`'s gate (`trace/tla.txt` corrected in a
commit of its own). With these the pair of AND-OR-INVERT units of run 3 reads as a **transparent
latch for `rcs_cond`**, with true and inverted data and `clk_tl` as its enable:

```
rcs_n4200  = NOT( (clk_tl AND rcs_cond)     OR rcs_x1 OR rcs_bd3330 )
rcs_bd3330 = NOT( (clk_tl AND NOT rcs_cond) OR rcs_n4200 )
```

while `clk_tl` is high (CLK high) `rcs_bd3330` follows `rcs_cond` and `rcs_n4200` its inverse; while
it is low the pair holds; `rcs_x1` high forces `rcs_n4200` low. (Marked: the pair's cross-coupling
and `rcs_cond_lat` = NOT `rcs_cond` each run through one load tie.) Full extraction: 2347 nets,
4158 transistors, 0 errors, 0 warnings.

2026-11-18 03:02 +0000 (run 3, Tom Seddon). **Partial: the gate column east of R3 traced where
`tla` had left it** (y 3690-3840 and y 4230-4530; 7 transistors in two pieces, and one of
`tla`'s transistors found to be two). Both pieces complete gates that `tla` had named without
their drivers or all their inputs:

```
rcs_bc3460 = NOR(rcs_e3, rcs_e4, tl2_w3722, clk_tl)                 piece 1; tla had NOR(rcs_e3, rcs_e4). FIRM
rcs_bd3330 = NOT( rcs_n4200 OR (clk_tl AND rcs_cond_lat) )           piece 2; no driver was known. Marked: the load's tie
rcs_n4200  = NOT( rcs_x1 OR rcs_bd3330 OR (clk_tl AND rcs_cond) )    tla's unit, with a second gate on its third
                                                                     pull-down. Marked: the same tie
```

Piece 1 is two pull-downs with no load of their own, whose node is `tla`'s `rcs_bc3460` by a
diffusion strip under the rail and thin metal E. Piece 2 is a second AND-OR-INVERT unit below
`tla`'s `rcs_n4200`: a load, a pull-down gated by `rcs_n4200`, and a pull-down gated by
`clk_tl` in series with one gated by `rcs_cond_lat`. Its node is `rcs_bd3330` (a buried contact
onto the row y 4374, drawn without `?`). **The poly that is its load's gate (`tl2_w4260`) also
runs north and is a gate of `rcs_n4200`'s unit**: the band y 4230-4250 under R3, which `tla`
had drawn as one poly with `rcs_x1`'s row; the two are separate polys over two columns of
diffusion (the review's two rounds; `tla`'s trace corrected, commit 0239da7). Through the
load's tie, which is `?` like every load tie of the cluster, that poly is the node, so **the
two units are a cross-coupled pair**: a latch that can change only while `clk_tl` is high
(`rcs_cond` high forces `rcs_n4200` low, `rcs_cond_lat` high forces `rcs_bd3330` low) and holds
while it is low, with `rcs_x1` a third input that forces `rcs_n4200` low at any time. The join
of `tl2_w4260` and `rcs_bd3330` is only through that `?` tie (`tools/unsure.py --names
rcs_bd3330`): an assumption, see Ambiguity 17. `rcs_x1`'s driver is still not found. `tla`'s
step formula does not change. Full extraction: 2271 nets, 4051 transistors, 0 errors,
0 warnings.

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
| x 2785-3175, y 4230-4530 | **run 3, piece 2**: the AND-OR-INVERT unit that drives `rcs_bd3330`, cross-coupled (through its load's tie) with `tla`'s `rcs_n4200`: load between R2 and thin E (y 4275-4349), the node's column under thin E and the gap, a wire under R3 (y 4344-4356), columns under R3's east edge and under the thin metal x 3025-3059, three gates (`rcs_n4200`'s band y 4370-4390, the `clk_tl` row y 4407-4424, the arm y 4462-4481 of `rcs_cond_lat`'s pad), a VSS box with a contact (2990,4513), the buried contact (3048-3072, 4362-4390) to the row y 4374 |
| x 2786-2990, y 4005-4145 | **run 4, piece 3**: the inverter of `rcs_cond`: VCC box under R2 (contact (2804,4084)), load plate in the open (x 2843-2896, y 4048-4110) on `rcs_cond_lat`'s poly, node box under thin E with a narrow strip south to the tie, pull-down in the gap between thin E and R3 (gate: the west end of `tla`'s g1 band, turned north), source on `tla`'s VSS box (contact (2985,4070)) |
| x 3004-3063, y 4504-4530 | **run 4, piece 4**: the top of `tla`'s column above the band of `tl3_w3982`: a diffusion band west to piece 2's VSS box; no tie to the pad above (AMB-009) |
| y 2500-2960 | horizontal metal tracks and rows north of the cluster: `tla`'s (y 2728), run 2's (y 2640, 2812 and the rows), and **run 5, piece 5**: `tl1_w3333`'s metal y 2554 with its east pad (3453,2553) and the poly north from it; `tl1_w2592`'s pad (2868,2596) and metal y 2598 / x 3503 / y 2509; the VSS arm y 2893-2948 onto R3's top; the VSS plane's lower edge (y 2507, to x 3388) |
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
(contact (2978,3815)) the column east of the rail (x 3030-3068) holds one more unit of the
cluster's kind, but without a load:

- **VSS link.** A diffusion strip y 3696-3709 from the upper VSS box east across the rail's edge
  to the top of the column.
- **Gate 1, `tl2_w3722`** (the row y 3712-3733 from track F's bottom pad (3322,3722)): on west
  under track A without a contact, across the column, west end at x 3012-3018. W/L 38/21.
- **Node box**, x 3030-3068, y 3737-3793 (west of it, x 3014-3023, is field: chip-2 stripped
  148-163/141-156/91, `px.py row 3745 3008 3080 3`; the first drawing had the edge at x 3022,
  review round 1).
- **Gate 2, `clk_tl`** (the row y 3798-3817 from track B's top pad (3150,3812), contact on
  `tla`'s metal): across the column, west end x 3010. W/L 38/19. Below it the column meets
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

Seen beside the piece (`tla`'s ground): the load plate of `rcs_bc3460` (x 2850-2897, y 3862-3925)
has a tab at its **top** right (x 2868-2900, y 3830-3862) beside an oval with a heavy outline
(x 2898-2925, y 3850-3878) on the node's strip, which is wider there (west to x 2900 from
y 3845; drawn `?D`). This run read the oval as the load's tie box; the reviewer read it as an
island of field with the strip round it (clean shot 174/132/121 inside, no green hole). Not
settled (Ambiguity 15). `tla` draws the tie at the plate's **bottom** (`B 2908,3932:2932,3959`,
with a tail `D 2913,3911:2929,3957` and the plate down to y 3960), where both stripped shots
show field (`p1_tie.png`). Whichever it is, the plate is on its node and the connection is the
same. Thin metal E over the oval is bright and wide at y 3844-3856, dark at y 3832-3841 and
y 3874-3880 (`textmap.py 2884 3790 2944 3915 3 --acid`), like `tla`'s other ties under it
(compared with `textmap.py 2884 4600 2944 4672 3` and `2884 5222 2944 5282 3`): read, as `tla`
does and as the reviewer did, as passing over without a contact.

#### Piece 2: the unit that drives `rcs_bd3330`, half of a latch (traced 2026-11-18; 5 transistors)

An AND-OR-INVERT unit of the same family as `tla`'s `rcs_n4200` directly above it, laid out
round a rectangle of field under R3 (x 2953-2985, y 4358-4440: pink, 174-191/117-139/121-127,
`px.py col 2965 4330 4530 5`). Its node is called X here; it is the net `rcs_bd3330`.

- **Load.** A strip y 4307-4330 from `tl1`'s VCC box under R2 (contact (2805,4308)) east under
  a poly plate (x 2846-2894, y 4275-4349, under `tla`'s strap) to a node box under thin metal E
  (x 2898-2936, y 4307-4338). W/L 23/48. The strap has no contact on the plate
  (`textmap.py 2838 4262 2895 4410 3`: bright A-D over the plate in both chips; its one contact
  is the pad below, bright centre (2866,4394) in a dark ring, green hole in the clean shot).
  **The plate's gate poly, `tl2_w4260`, is also a gate of `rcs_n4200`'s unit** (found by the
  review's two rounds, each confirmed by the tracer): the plate's upper part runs east as an arm
  (y 4275-4292) into a vertical poly in the gap between thin E and R3 (x 2927-2947). That poly
  runs **north** to y 4235 and turns east into the band y 4230-4250 under R3 (x 2945-3000),
  which crosses the west column of `rcs_n4200`'s third pull-down, and **south** into a
  heavy-outlined box (about x 2912-2950, y 4298-4334) that sits on the node's diffusion. `tla`
  had the band as the west end of `rcs_x1`'s row (`rcs_g4240`), one poly over one diffusion; the
  row from the east ends at x 3020, 20 px short of the band, and the diffusion under them is two
  columns (x 2950-2990 and x 3030-3066) with an island of field between (`tla`'s trace corrected,
  commit 0239da7: one transistor 117/20 became two, 41/20 gated by `tl2_w4260` and 37/19 gated by
  `rcs_x1`). The poly is drawn firm. **The box, the tie, is drawn uncertain (`?P`, `?D`, `?B`)**,
  as every load tie of this cluster is: it has a heavy outline and a paler centre in all four
  shots (`review-5/j12_tiebox.png`, 10x), which is how a buried contact looks. The poly has no
  other end (the plate, the gate under R3 and the box are all of it), so without the tie it
  would be a gate net that nothing drives.
- **X's diffusion**, one piece, west to east: the column under thin E and in the gap
  (x 2903-2950, y 4334-4366); a narrow wire under R3 along the top of the field rectangle
  (y 4344-4356, tan core 7 px between a dark line at y 4340 and the rectangle's outline at
  y 4358: `px.py col 2970 4336 4362 2`; 196-201/159-166/130-146 from x 2952 to x 2997 without a
  break: `px.py row 4348 2940 3004 3`); a strip down R3's east edge (x 2990-3010, y 4344-4403:
  `px.py col 2998 4300 4530 5`); a band y 4390-4403 east across the 24 px gap between R3 and
  the thin metal x 3025-3059 (`rcs_cond_lat`'s); and a column under that metal (x 3028-3054)
  with a wider top (x 3028-3070, y 4362-4402).
- **Output.** In the upper right of that top a heavy-outlined box (x 3048-3072, y 4362-4390):
  a buried contact to the west end of the row y 4374, the poly from track D's bottom pad
  (3237,4376), i.e. `tla`'s `rcs_bd3330` (which gates `rcs_u3288` = NOR(`rcs_g3245`,
  `rcs_bd3330`) at (3046,3330)). Drawn without `?`.
- **Pull-down 1, gate `rcs_n4200`.** `tla`'s strap ends at y 4400 on a pad with a contact
  (2866,4394). The pad's poly runs east along y 4370-4390, under thin E and through the gap,
  and ends at R3's west edge (x 2950-2953). It crosses the column: W/L 44/20. Below it the
  column goes on as a stub in the gap (to y 4418) and as a strip under thin E (x 2905-2924)
  south to y 4510, where it turns east along y 4492-4510 into the VSS box under R3.
- **Pull-downs 2 and 3 in series, gates `clk_tl` and `rcs_cond_lat`.** The row y 4407-4424
  from track B's pad (3150,4418) (contact on `tla`'s metal, `clk_tl`; not drawn by `tla`) runs
  west under track A without a contact, under the thin metal and R3 to x 2977. It crosses both
  columns (two channels, 20/17 and 26/17, in parallel between X and the node below,
  `tl2_w4452`). Below the row the columns join again, widen west under R3 (x 2957-3009,
  y 4445-4462) and pass under the second gate, a band y 4462-4481 that is the west arm of
  `rcs_cond_lat`'s pad (`tla`: pad x 3024-3066, y 4455-4522, contact (3045,4485)); W/L 52/19.
  Below it a VSS box (x 2957-3009, y 4482-4530) with a contact to R3 at (2990,4513), drawn by
  nobody before.

Extracted (`tl2_w4260` is aliased to `rcs_bd3330` in the trace, across the `?` tie):

```
rcs_bd3330 = NOT((clk_tl & rcs_cond_lat) | rcs_n4200)             DEPENDS (tools/unsure.py --equations): the load's tie
rcs_n4200  = NOT((clk_tl & rcs_cond) | rcs_bd3330 | rcs_x1)       DEPENDS; without ?: NOT((clk_tl & rcs_cond) | rcs_x1 | tl2_w4260)
t62 (2870,4318) 23/48 load   t63 (2925,4380) 44/20 gate rcs_n4200   t64 (2983,4472) 52/19 gate rcs_cond_lat
t65 (3041,4416) 26/17 and t71 (3000,4416) 20/17, gate clk_tl, between the node and tl2_w4452
in tla's unit: t67 (2970,4240) 41/20 gate tl2_w4260, t68 (3048,4240) 37/19 gate rcs_x1, both rcs_n4200 <-> vss
```

What is firm and what is not. Firm: the pull-downs of both units, the node's buried contact to
`rcs_bd3330`'s row, and the poly `tl2_w4260` from the plate to the gate under R3. Marked: that
the box at the poly's south end ties it to the node. With the tie the two AND-OR-INVERT units
are a **cross-coupled pair**:

- while `clk_tl` (CLK polarity) is low, `rcs_bd3330` = NOT `rcs_n4200` and `rcs_n4200` =
  NOR(`rcs_bd3330`, `rcs_x1`): the pair holds, and `rcs_x1` high forces `rcs_n4200` low (and so
  `rcs_bd3330` high);
- while `clk_tl` is high, `rcs_cond` high also forces `rcs_n4200` low, and `rcs_cond_lat` high
  forces `rcs_bd3330` low. `rcs_cond_lat` is `rcs_cond` as it was while `tl3_w3982` was last
  high (`tla`'s pass transistor), so in steady state the two agree and both outputs are then low
  for as long as the clock is high: **believed**, from the equations; not simulated.

`rcs_bd3330` goes on, by the row y 4374 and track D's piece, to `rcs_u3288` =
NOR(`rcs_g3245`, `rcs_bd3330`), whose inverse drives thin metal W. `rcs_x1` (the clear of
tl1's two latches and tl3's two, an input of `rcs_b1`) is an input of this pair and not its
output; its driver is still to be found east of x 3533 on the row y 5371 (run 2).

Evidence (views in `cache/scratch/tl2/`; text tools as cited; `tools/tl2_cmap.py` is new, the
class map of `tools/classmap.py` as text, right only under metal):

- Reference colours of the clean shot under R3 here (`px.py pt`): poly over field 209-227/172-177/
  120 ((2975,4020), (2990,4020)), plate over field 227/169/123, plate or gate over a channel
  241/170/122 and 238-247/158-186/117-131, diffusion 190-200/163-167/135-142 ((2998,4375),
  (2960,4452)), field 185/124/125. The narrow wire under R3 is 198/163/135: diffusion, not poly.
- **The poly from the plate to the gate under R3**: `px.py row 4283 2876 2950 3 acid1b,acid,metal`: one
  salmon band 215-230/160-175/113-125 from x 2876 to x 2927 (the arm, under the strap's margin and
  thin E), dark red-brown open poly from x 2936; `px.py col 2938 4214 4340 6 acid1b,acid,metal,metal1`:
  in the gap, chip-2 metal 150-172/116-138/58-75 and chip-2 stripped 142-183/95-141/53-77 (orange,
  blue low) at every sample from y 4238 to y 4292, between edges at y 4226-4232 and y 4298-4304;
  the gap's bare field lower down is 159-170/137-147/78-86. View `r5_check1.png` (5.4x, three
  shots, with `tla`'s row outlined); the reviewer's `review-5/j10_gap_poly.png`, `j11_corner.png`.
  The poly's top (y 4233-4235) stays 5 px clear of `tla`'s node strip y 4203-4228.
- **The band under R3 and `rcs_x1`'s row are two polys** (review round 2, confirmed):
  `px.py row 4241 2984 3040 3 acid1b,acid,metal,metal1`: gate poly to x 2999, pink field under R3's
  margin at x 3002-3008, green open field at x 3011-3017 (121-141/146-168/96-108), poly again
  from x 3020; `px.py col 3014 4196 4300 4`: down the gap the clean shot is green
  (110-132/163-174/85-98) from y 4228 to y 4260 and both metal shots are 97/88/50, where the rows
  that do cross this gap (y 4416, y 4470) are a dark red-brown bar in the clean shot and orange
  152-169/108-130/50-65 in the metal shot; `review-6/gap_m.png` (the gap at four rows side by
  side). Diffusion colours above the island (y 4196-4212) and below it (y 4276-4288).
- **Load**: `tl2_cmap.py 2780 4252 2962 4350 3`: channel class at x 2846-2888, y 4312-4327 under
  the strap, the VCC box west of it, diffusion east of the plate to x 2936; `p2_load.png`
  (3.6x, three shots), overlay `p2_ov3.png` (4x).
- **Gate of `rcs_n4200`**: `px.py row 4380 2884 2972 3 acid1b,acid,metal,metal1`: poly over
  field from the pad (218-231/164-168/123-127), channel-bright under thin E (230-247/139-173/
  81-125, x 2908-2926), dark red-brown open poly in the gap (x 2929-2944; orange in both metal
  shots, 162-174/105-150/52-62), end at x 2953-2956 (under R3's edge; the reviewer's reading), pink field
  under R3 from x 2959.
  `px.py col 2912 4296 4440 6`: under thin E tan above the band (y 4338-4362), the band
  238-245 red at y 4374-4386, tan below. Views `p2_gap.png` (5x, four shots), `p2_tl.png`.
- **The source's path to VSS**: `p2_src.png` (5.6x, chip-2 stripped, chip-1 metal, clean): one tan
  L under thin E and along y 4492-4510, closed by a red line at y 4510-4515, into the box under
  R3; `px.py col 2938 4326 4520 4`: diffusion colours in the gap at y 4498-4506.
- **The two gates under R3**: `px.py col 2998 4300 4530 5`: tan y 4347-4402, gate-bright
  y 4410-4420, tan y 4435-4455, gate-bright y 4465-4475, tan y 4490-4505;
  `tl2_cmap.py 2925 4320 3078 4535 3`: channel class x 2994-3006 and x 3024-3051 on the upper
  row, x 2958-3009 on the lower band.
- **The `clk_tl` row** is one poly through the gap between R3 and the thin metal and on to track
  B's pad: `px.py col 3014 4380 4500 3 metal,metal1,acid`: orange poly (blue 50-65) at
  y 4410-4425 between two edges; `px.py row 4414 2950 3140 5`; no contact of track A on it
  (`textmap.py 3090 4396 3132 4436 3`). Pad (3150,4418): seen with its ring on `s3_b.png`.
- **The lower band is the arm of `rcs_cond_lat`'s pad**: the same column profile shows orange
  poly (blue 53-63) in the gap at y 4464-4479, and `px.py row 4471 2924 3072 4`: gate-bright
  from x 2956 to x 3008, the gap's dark bar x 3014-3026, the pad's salmon from x 3028; both
  metal shots show the band's two edge lines running through the gap into the pad's outline
  (`p2_m.png`, 4.3x). Its west end is a rounded poly end at x 2930 in the gap (`p2_gap.png`).
- **X's band across the gap** (y 4390-4403): tan on both sides at the same y
  (`px.py row 4398 2984 3070 4`: 189-199/162-191 to x 3008 and from x 3024), a 10 px dark bar
  between (the artefact of a 24 px gap, trap 2), and in both metal shots the band's top edge
  crosses the gap as a dark line at y 4386-4389 with bare ground below it down to the row's
  edge (`px.py col 3014`); chip-2 stripped red minus green 28-48 there against 10-23 on the
  gap's ground at y 4491-4500.
- **The buried contact** (3048-3072, 4362-4390): `p2_n.png` (four shots, about 5.6x as read)
  and `p2_tr.png` (5x): a closed box about 20 x 26 with a heavy outline on its west and south
  sides in both stripped shots, tan inside, in the top of the column; the row's poly (dark
  red-brown in the clean shot, orange in chip-1's metal shot) reaches x 3072-3075.
- **VSS contact (2990,4513)**: `textmap.py 2946 4484 3018 4545 3 --acid`: a bright centre
  (C-D in chip 1 at x 2982-2994, y 4508-4517) in a dark ring under R3, and a green hole in the
  clean shot at x 2985-2997, y 4508-4517.
- Overlays: `p2_ov1.png` (2.5x, chip-2 stripped | clean with the trace), `p2_ov2.png`,
  `p2_ov3.png` (4x, clean shot).

### The inverter of `rcs_cond` west of R3 (run 4, piece 3)

Views: `r4_a.png` (2.05x), `r4_b.png`, `r4_c.png`, `r4_d.png` (4.5x, four shots), `r4_e.png`,
`r4_f.png` (4.6x beside the standard load unit 182 px north: not a copy; `findcell.py` with
`tla`'s load unit finds nothing above 0.56), `r4_g.png` (3.8x, the VCC box, four shots);
overlays `r4_ov1.png`, `r4_ov2.png`. The measurements, with their commands, are in
`cache/scratch/tl2/survey.md` (run 4).

- **VCC box under R2** (x 2786-2840, y 4066-4112), drawn by nobody before: a dark outline in the
  clean shot, a contact ring in both metal shots centred (2804,4084), a green hole in the clean
  shot at x 2797-2811, y 4078-4087. Above it (y 4045-4063) the clean shot has an olive patch in
  pink field and neither metal shot a ring: nothing.
- **Load.** A strip y 4068-4094 runs east from the box under a poly plate in the open
  (x 2843-2896, y 4048-4110: orange in the chip-2 stripped shot, 163-184/133-162/66-79; the
  strip's edges cross it as dark lines at y 4064-4068 and y 4092-4096, and the band between them
  is channel-bright in the clean shot, 193-222/101-152) into a box under thin metal E
  (x 2897-2936, y 4067-4102, flat tan 197-209/176-186/135-146): the node, `tl2_w4080`.
- **The plate is on `rcs_cond_lat`'s poly.** From the plate's top a vertical poly x 2878-2898 runs
  north to the row y 4011-4030 (`px.py col 2888 4000 4064 3`: poly colours in both chip-2 shots
  from y 4015 to y 4060 with no dark line across, 164-183/126-149/62-80 stripped); the row runs
  east under thin E (salmon 216-228/165-177/110-124 in the clean shot: poly over field) and
  through the gap (orange 132-163/105-128 stripped) onto `tla`'s piece under R3 and the pad
  (3040,4028) of `rcs_cond_lat`'s metal. No contact of R3 on the row: a dim spot in the chip-2
  metal shot at (2974,4023) has no dark ring, is not in the chip-1 metal shot, and the clean
  shot has no green hole there (`textmap.py 2944 3996 3012 4052 2 --acid`).
- **Pull-down.** The node's box goes on east through the 28 px gap between thin E and R3: its
  edge lines (y 4064-4068 and y 4100-4104) cross the gap from x 2840 to x 2960 in both metal
  shots (`r4_c.png`). A vertical poly lies in the gap (x 2938-2953; orange at x 2939-2945 in the
  chip-2 stripped shot, channel-bright 247/154-175/110-126 at x 2948-2951 in the clean shot under
  R3's margin, against 130-148/55-108 on the same poly at y 4108-4132 over field), and east of it
  the diffusion runs under R3's west edge onto `tla`'s VSS box (D 2968,4045:3018,4105, contact
  (2985,4070)): tan at x 2954 and from x 2963 in the clean shot, R3's edge line between them
  (x 2957-2960); the chip-2 stripped shot has no dark line there (141-177/97-152 from x 2954 to
  x 2966).
- **The gate is `rcs_cond`.** The vertical poly's south end is the west end of `tla`'s g1 band
  (P 2985,4103:3095,4128, from the contact (3105,4112) on bus line A's piece A3): the band runs
  on west under R3 over field (`px.py row 4118 2926 3000 3`: salmon 224-228/155-169/112-123 at
  x 2950-2965, one dark line x 2968-2971 where the diffusion under g1 begins, channel 240-253
  from x 2974; `tla` draws that diffusion from x 2990) into the gap and turns north. Between the
  band and the node's diffusion the poly has one dark line 6-8 px wide (y 4100-4106 at x 2941,
  all four shots): the diffusion's lower edge under the poly. The poly's north end is free at
  y 4052: 20 px of field lie between it and `rcs_cond_lat`'s row (`px.py col 2941 4026 4060 2`:
  bare ground in both metal shots at y 4036-4042, 155/156/88 and 139/137/75; the row's lower
  edge line at y 4030-4034, the end's at y 4048-4052). A green ring in the clean shot at
  (2937,4039), in that field, is the patch enclosed by the two metals' margins, the row and the
  poly's end: nothing is there in either chip-2 shot (tracing guide, trap 2).
- **Nothing else is on the node**: thin E has no contact on the box (`px.py col 2914 4056 4160 3`:
  bright in both metal shots from y 4068 to y 4131, no ring; the clean shot flat tan with no
  green hole), and a narrow strip (x 2907-2921) runs south from the box under thin E to y 4138.
- **The tie** (`?P`, `?D`, `?B`): directly below the plate a box with a heavy outline
  (x 2872-2900, y 4113-4141; lighter inside at x 2880-2893, y 4122-4136, 170/140/97 stripped) in
  both metal shots and the chip-2 stripped shot (`r4_f.png`, `r4_ov4.png`; the review's
  `review-8/tie_ma.png`), its top outline being the plate's bottom edge (the 10 px of dark at
  y 4113-4123); its bottom outline runs on east as one line to x 2925, under thin E, past the
  south end of the node's narrow strip (`textmap.py 2860 4096 2930 4150 2 --acid`). Read as a
  buried contact of the plate's tab onto a diffusion that comes west from the strip's end, the
  usual tie of a load at the end of its poly; neither link is resolved across the outlines, so
  all three items are drawn uncertain, like every load tie of the cluster. (The first drawing
  had the box 25 px east, on the strip's end; the review placed it.) Nothing else leaves the
  node, so if the plate were not tied to it the unit would drive nothing.

So `tl2_w4080` = NOT `rcs_cond` (the pull-down, the node and the plate's poly are drawn without
`?`), and through the tie `rcs_cond_lat` = `tl2_w4080` (`@alias rcs_cond_lat tl2_w4080`;
Ambiguity 19). `tools/unsure.py --equations rcs_cond`: `rcs_cond_lat = NOT rcs_cond` DEPENDS (on
the tie: without it the load's gate is not on its node), `rcs_cond = NOR(rcs_cond_n, tl3_w3982)`
FIRM.

### The top of `tla`'s column: AMB-009 re-read (run 4, piece 4)

`tla` had the band of `tl3_w3982` (y 4535-4558) as a pass transistor from `rcs_cond`'s node up to
the column's top end, and that end tied to the pad (3024-3066, 4455-4522) at the foot of
`rcs_cond_lat`'s metal by a buried contact drawn `?B` (AMB-009), which made `rcs_cond_lat` a dynamic
latch. AMB-009's reasons were the pad's heavy lower edge, that no other poly left the pad, and
that the circuit made sense. Run 3 found the pad's west arm (a gate of piece 2) and piece 3
finds the metal's other end on an inverter's load, so the pad needs no tie. Read again
(`r4_amb9.png` 3.1x, `r4_amb9b.png` 9x, four shots each; overlay `r4_ov3.png`):

- **Pad and column top are two features.** Down x 3044 (`px.py col 3044 4486 4540 2`): the pad's
  lower outline at y 4496-4504, a lighter strip at y 4506-4510 whose red and green are equal in
  the chip-2 metal shot (72/73/42, 120/104/60), the chip-1 metal shot (108/105/48) and the chip-2
  stripped shot (66/72/26, 59/65/35), then a second outline at y 4512-4516, then the band. At 9x
  the second outline runs east along y 4513 and turns south at x 3064 as the column's east edge;
  at its west end it curves up to the pad's corner. A buried contact is one box where poly
  overlaps diffusion; here there are two outlines with field between.
- **The column's top is a band that runs west to R3.** `px.py row 4522 2962 3072 3`: from x 3016
  to x 3055 the chip-2 stripped shot is 166-174/136-153/92-105 and the metal shot 170-179/
  135-139/88-95, the colours of the open column at y 4568 (158-167/151-159/94-101 and 166-173/
  140-145/84-92: `px.py row 4568 3004 3076 4 acid,metal`), where x 3012-3020 beside the column is
  field (151/153/93 and 156/144-152/82-85). So at y 4514-4530 the diffusion is 20 px wider to the
  west than the column and reaches R3's east edge. Under R3 the clean shot is tan at
  x 3001-3010 (196-203/143-178/113-129) up to the pits of piece 2's VSS contact (2990,4513); the
  one dark line between (x 3008-3014 stripped, x 3013-3016 clean) is R3's edge line. (AMB-009's
  "two dark lines at x 2998 and x 3018" are the contact's pit and that edge line.)

- **The join is also seen in the open** (review round 1): east of R3 the VSS box comes out from
  under the rail as a strip x 3009-3019 from y 4490 down into the band, uniform in both metal
  shots and the chip-2 stripped shot (`px.py col 3015 4480 4532 4`: 108-132/89-106/65-81
  stripped from y 4492 to y 4524, no line across); the clean shot's dark line at x 3014-3022
  is in neither metal shot. Drawn `D 3004,4490:3019,4530`.

Drawn: `D 3004,4514:3063,4530` here; in `trace/tla.txt` the `?B` removed, the pad's poly ended at
y 4504 and the column begun at y 4514. The band of `tl3_w3982` is then a pull-down from
`rcs_cond`'s node to VSS: `rcs_cond` = NOR(`rcs_cond_n`, `tl3_w3982`), that is NOT `rcs_cond_n`
AND NOT `tl3_w3982`. `tla`'s step formula does not use `rcs_cond` and does not change.

### North of y 2630 (run 5, piece 5; wiring only)

Survey `n5_sv.png`, `n5_sv2.png` (1.7x, metal over clean, every package's trace outlined,
x 2800-3550, y 2470-2980); junctions `n5_a.png` (4.4x, four shots, x 3400-3540, y 2475-2625) and
`n5_b.png` (5x, four shots, x 2800-2915, y 2560-2635); overlays `n5_ov1.png`-`n5_ov4.png`. Under
every metal here the clean shot is protected field (pink): no diffusion, no transistor. In the
band y 2690-2980 everything else already had an outline; the tops of tracks A, B and C are
`tla`'s (pads (3108,2985), (3150,3067); C turns west along y 2728).

- **`tl1_w3333`** (traced). `tl1`'s metal from its pad (2826,2553) runs east along y 2546-2562
  (`follow.py 3000 2553 E`: end (3460,2556); `W`: end (2822,2556)) to a pad: ring x 3440-3478,
  y 2535-2572 with a bright centre at (3455,2553) in chip 2 and (3452,2553) in chip 1, a salmon
  pad x 3446-3472, y 2536-2568 with a green hole in the clean shot and a pit in the chip-2
  stripped shot. **A poly leaves the pad north**, x 3450-3470: orange between two edge lines in
  both metal shots and the chip-2 stripped shot (`px.py row 2520 3370 3540 4`: 154-174/113-120/
  58-66 metal, 139-161/117-129/63-72 stripped at x 3454-3466; edge lines x 3446-3450 and
  x 3470-3474), dark red with a green rim in the clean shot, on north past y 2475. So the data
  of `tl1`'s third latch comes from the band north of the strips.
- **`tl1_w2592`** (traced). `tl1`'s row y 2582-2600 (drawn there to x 2817) runs on east to a
  pad: ring x 2852-2892, y 2578-2616, bright centre (2868,2596) in both metal shots, green hole
  in the clean shot. The row is poly without a break up to the pad (`px.py row 2591 2804 2900 4`:
  orange 157-167/107-128/57-75 in the metal shot from x 2804 to x 2848; in the clean shot open
  poly to x 2844 and salmon from x 2848; the dark stretch x 2848-2860 in the chip-2 stripped
  shot is the pad's outline at the metal's edge). The metal leaves the pad east along y 2590-2607,
  turns north at x 3494-3512 and east again along y 2501-2518, out of the strip at x 3533
  (`follow.py 3000 2597 E`: corners (3506,2593) and (3504,2511), on east to x 3752). **At its
  corner it passes `tl1_w3333`'s pad without touching**: the pad's ring ends at x 3478, the metal
  begins at x 3492, bare ground between in both metal shots (`n5_a.png`; trap 16).
- **VSS** (traced). The east arm of `tl1`'s wide metal x 2733-2785 is y 2893-2948 and runs
  without a break onto the top of R3 (`px.py row 2930 2776 3024 8`: bright from x 2776 to
  x 3000 in both chips, one dark sample at x 2920 in chip 2 only; edge at x 3004). **The arm
  lies over the poly row y 2890-2908 (`tl1_w3594`), with no contact.** The tracer first drew it
  y 2915-2948, from the bright stretch y 2916-2944 (`px.py col 2800|2825|2860|2940 2896 2968 4
  metal,metal1`), taking the row to lie beside it; the review showed otherwise: the arm's east
  edge line (x 3003-3008) runs up to y 2893 in both metal shots (`review-9/armtop.png`, 6x), the
  row is protected salmon in the clean shot from y 2892 to y 2904, more than 20 px from the
  bright stretch, as far east as x 3004 and open poly from x 3008 (`px.py row 2900 2960 3044 4`,
  `px.py col 2990 2880 2924 3`), and over the row the chip-2 metal shot is dim with red equal to
  green (87-133/67-125) where the open row east of the arm is orange (144-169/94-115/42-61).
  The dark line y 2908-2913 across the arm is the row's lower edge underneath (trap 3). The row
  is uniform under the arm, without a green hole. `tl1` drew the arm y 2905-2955 at
  x 2785-2817: 12 px short at the top, a width only. The dark line across R3 at y 2970-2978 is not a gap: 6-10 px in both chips, it runs on
  beyond the rail on both sides (`px.py row 2974 2930 3030 5`) and the clean shot is protected
  through it (`px.py col 2978 2960 2992 2`): the top edge of the poly row under the rail there.
  The plane above: lower edge y 2507, east end x 3388 (`px.py col 2900|3200|3370 2484 2530 3`,
  `px.py row 2490 3330 3420 5`); nothing in the strip east of x 2832 joins it.

**The "poly bar" along y 5655-5670 (Not done since run 2) is not a feature.** `b5_sv.png` (3.3x,
three shots, x 3170-3550, y 5590-5720) and `px.py col 3350 5606 5704 3 metal,acid,acid1b`: between
`amr_eq_r3`'s row (y 5621-5639) and `tla`'s metal along y 5667-5687 the strip y 5648-5660 has the
colours of the open field south of the metal in all three shots (metal 159-167/136-140/81-85
against 162-164/138-140/84-89 at y 5699-5702; stripped 153-167/122-150/83-103 against 157-159/
144-147/101; clean 130-153/113-146/81-100 against 130/110/85), and none of poly's (the row beside
it: stripped 149-167/106-136/64-71). What the 1.8x clean-shot view showed as a bar is the strip of
open field between the metal's protected margin and the row's green rim, with its dark outline
(trap 2).

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
| `tl1_w3333` | M | x 2848, y 2546-2562 | out | tl1's metal from the pad (2826,2553), to tl1's third latch; comes through the strip from the pad (3453,2553) |
| `tl1_w3333` | P | x 3450-3470, y 2500 | in | the poly north from the pad (3453,2553): the wire's source is north of the strips |
| `tl1_w2592` | P | x 2817, y 2582-2600 | ? | tl1's row y 2591, on east to the pad (2868,2596) |
| `tl1_w2592` | M | x 3533, y 2501-2518 | ? | the metal from that pad: y 2598, north at x 3503, east along y 2509 (follow.py: on to x 3752) |
| `vss` | M | x 2817, y 2893-2948 | - | the east arm of tl1's wide metal, onto R3's top; it lies over the row y 2899 without a contact |
| `vss` | M | x 2832-3388, y 2500 | - | the plane's lower edge (y 2507), on north |

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

9. **The buried contact of piece 2's output** (3048-3072, 4362-4390) (run 3). The box is plain in
   both stripped shots; the 5-8 px between it and the visible end of the row's poly (x 3072-3075)
   lie under the edge line of the thin metal x 3025-3059 in every shot. Drawn joined, without
   `?`. If the row ended short of the box, `rcs_bd3330` would have no driver and the unit no
   output; nothing else leaves the node.
10. **The band of piece 2's node across the gap between R3 and the thin metal** (3006-3032,
   4390-4403) (run 3): the gap is a dark bar in both stripped shots. Drawn without `?` on the
   evidence listed under piece 2 (tan on both sides, the band's top edge crossing the gap in
   both metal shots). If it were field, the node's west part (load, the two pull-down paths)
   and its east part (the buried contact) would be two nets.
11. **The same gap below the `clk_tl` row** (3006-3032, 4436-4450): no edge of its own can be told
   from the two gates' edges there; drawn `D` since the review (chip-2 stripped at x 3015 reads as
   the band above the gate does, 151-158/108-120/91-95). If it is field, the column under the thin
   metal below the row (x 3028-3054, y 4425-4448) is a dead-end stub and the row's east channel
   does nothing; the equation is the same either way. What lies under the row itself in the gap
   cannot be read: drawn as two channels (20 and 26 wide); one channel about 64 wide is as
   likely. Size only.
12. **Is that stub tied to `rcs_cond_lat`'s pad?** The stub's bottom edge (y 4449) and the pad's
   red top outline (y 4454-4460) are adjacent, with a strip 7 px high between tan and the edge
   that is green in the clean shot under the metal (`px.py col 3040 4424 4472 2`;
   `textmap.py 3012 4352 3072 4512 3 --acid`: `g` at y 4442-4448 across x 3024-3050). Read as
   two features at minimum spacing (no box, no overlap: tan ends at y 4440, salmon begins at
   y 4462). A buried contact there would tie `rcs_cond_lat` to the node between the two series
   gates, i.e. to the drain of the transistor it gates: not a circuit. Not drawn.
13. **The end of `rcs_n4200`'s gate poly** (x 2950-2953) and the east edge of the diffusion it
   crosses (x 2947-2950) coincide within what the photos resolve (both at R3's west edge). If
   the diffusion passed the poly's end the gate would be bypassed. Drawn with the poly 5 px
   past the stub.
14. **Piece 2's load tie** (`?P`, `?D`, `?B` at 2926-2950, 4296-4342): the box at the south end
   of `rcs_x1`'s poly in the gap. That it is a buried contact onto the node's diffusion is read
   from its heavy outline, its paler centre and its place, as for the other loads of the cluster;
   it is not resolved further at 10x. See Ambiguity 17 for what rests on it.
15. **Piece 1: where the tie of `rcs_bc3460`'s load is.** `tla` draws it at the plate's bottom,
   where the photos show field. At the plate's top an oval (2898-2925, 3850-3878) lies on this
   package's strip: a tie box (the tracer) or an island of field inside a wider strip (the
   reviewer). Not settled; `?D 2903,3845:2917,3890` is the widening. Same connection either way
   (the plate must be on its node). `tla`'s geometry is left as it is (handoff).
16. Under thin metal E the clean shot's colour is 200-207/161-166/135-141 from y 4398 to
   y 4500 (the source strip of piece 2), between this cluster's diffusion (190-200/163-167/
   135-142) and nothing else: read as diffusion on `p2_src.png`, where the strip has one outline
   with the turn east. Thin E has no contact on it (bright in both metal shots, `p2_gap.png`).

17. **`tl2_w4260` = `rcs_bd3330`: joined only through piece 2's `?` tie** (run 3; an assumption,
   tracing guide trap 17). Firm: the node of piece 2 is `rcs_bd3330` (buried contact, Ambiguity
   9); `tl2_w4260` is one poly, the gate of piece 2's load and the west gate of `rcs_n4200`'s
   third pull-down. Assumed: that the box at the poly's south end ties it to the node, which
   makes the two units a latch. The names are aliased in `trace/tl2.txt` (`@alias rcs_bd3330
   tl2_w4260`), not renamed. For it: the poly has no other end, so without the tie two gates
   hang on a net nothing drives; the box has a heavy outline and a paler centre in four shots.
   What would settle it: a better photo of the box. (The first fix after review round 1 had
   this poly joined to `rcs_x1`, taking `tla`'s row as one poly; round 2 found the break.)
18. `tla`'s VSS arm (y 3818-3836) below piece 1's gate 2 is the source of that transistor. In the
   chip-2 stripped shot the 10 px between the two gate rows read field-like there (150-156/141-153/
   96-100 at x 3032-3060, `px.py row 3830 3008 3080 4 acid,metal`); the column's east edge line
   (x 3068) is present and its west edge line (x 3030) absent at that y, as for an arm coming
   from the west. Left as `tla` drew and had reviewed it; the reviewer of run 3 could not check
   it either.

19. **`rcs_cond_lat` = `tl2_w4080`: joined only through piece 3's `?` tie** (run 4; an assumption,
   tracing guide trap 17). Firm: the pull-down gated by `rcs_cond` on `tl2_w4080`; the load's plate is one poly with
   `rcs_cond_lat`'s row, pad and metal. Assumed: that the plate is tied to the node (the loop
   below the plate and the band to the strip's end, Logic). For it: the node has no other exit,
   and `rcs_cond_lat` no other driver since piece 4. Aliased, not renamed.
20. **The gate poly of piece 3 across the diffusion's lower edge** (x 2938-2953, y 4100-4106): one
   dark line 6-8 px wide in all four shots, read as the diffusion's edge under one poly (two poly
   ends would need two outlines and field, about 15 px). If it were a break, the poly in the gap
   (y 4052-4098) would be a piece joined to nothing and the node would have no pull-down.
21. **The join of piece 3's diffusion to `tla`'s VSS box across R3's west edge** (x 2953-2968):
   hidden by the rail's edge line in the clean shot, as at every rail gate of the cluster; the
   chip-2 stripped shot has no line there. Drawn joined. Likewise **the join of piece 4's band to
   piece 2's VSS box across R3's east edge** (x 3004-3016): one edge line, tan on both sides. If
   the band did not reach the box, the column's top would be a dead end and the band of
   `tl3_w3982` would do nothing; it cannot be on the pad (Logic, piece 4).
22. **Piece 3's tie box** (x 2872-2900, y 4113-4141): that the plate's poly enters it across its
   top outline, and that the diffusion under it is joined to the node's strip 7 px to the east,
   are both read from the box's shape and place, not seen (Logic). If either is not so, the
   tie is not there.
23. Sizes (run 4): the pull-down of piece 3 is drawn 35/19 (the box's height by the poly's
   width, x 2938-2957: its east edge is under R3's margin); the load 26/53. `tla` draws the diffusion under its g1 band from x 2990;
   its west edge line is at x 2968-2971 (`px.py row 4118`), so that transistor is about 20 px
   wider than drawn (`tla`'s geometry, left as it is: a width).

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

### Run 3 (the gate column east of R3: pieces 1 and 2)

Round 1 (full review of both pieces, 2026-11-18 02:40 +0000, a fresh agent on claude-fable-5-2, at commit
57acc95; 25 images in `cache/scratch/tl2/review-5/`). Told to suspect, in piece 2: the buried
contact (3048-3072, 4362-4390) and whether the row y 4374 reaches it; the node's band across the
gap between R3 and the thin metal; whether the band y 4462-4481 is one poly with `rcs_cond_lat`'s
pad and its west end free; a tie between the column under the thin metal and that pad; whether
`rcs_n4200`'s crossing is a gate and passes the diffusion's edge; the narrow wire under R3 and
the strip under thin E. In piece 1: the node's strip (diffusion, continuous into `tla`'s box,
nothing crossing) and the two joins across R3's east edge. In both: the two contacts on track B,
the rows under track A, every gate crossing its diffusion, undrawn polys.
It checked each at 4.3-6.5x in at least two shots with profiles: the buried contact (the same
double outline as `tla`'s two on this column), the band across the gap (chip-2 stripped red
minus green 26-50 against green field above y 4385), the lower band and the pad (poly colour in
the gap in both metal shots, edges continuous; west end free in field), the column and the pad
(a strip of field between them in both stripped shots: not tied), `rcs_n4200`'s crossing (a
gate; the poly ends at x ~2956), the wire under R3 and the strip under thin E with its turn
(diffusion; no contact of thin E: text map y 4336-4520), piece 1's arm, strip and joins, both
track B contacts (bright centre, ring, green hole), no contact under track A at y 3722 or y 4414,
all gates crossing fully, `tools/opendiff.py` (no undrawn diffusion).
Findings, each checked by the tracer:
1. **Changes a connection. Confirmed.** Piece 2's load-tie poly (`?P 2928,4275:2948,4330`) does
   not start at y 4275: the poly in the gap x 2927-2946 runs on north to y 4233 and turns east
   into `tla`'s row y 4230-4250 (`rcs_g4240` = `rcs_x1`). Tracer: `px.py col 2938 4214 4340 6`
   (poly colours in both chip-2 shots from y 4238 to y 4292) and `r5_check1.png` (5.4x). Fixed:
   `P 2927,4235:2948,4300` drawn firm, the box kept `?`; the node now carries `rcs_x1` and
   `rcs_bd3330` (alias; Ambiguity 17), and the unit is the driver of `rcs_x1`.
2. Geometry only. Confirmed. Piece 1: the column's west edge is x ~3030, not 3022 (`px.py row
   3745 3008 3080 3`: field at x 3014-3023). Fixed (W 46 -> 38).
3. Geometry only. Undecidable. Piece 1: the node strip widens west to x 2900 under thin E from
   y ~3845 round an oval at (2909,3868), which the reviewer reads as an island of field and the
   tracer had read as the load's tie box. Drawn `?D 2903,3845:2917,3890`; Ambiguity 15.
4. Geometry only. Confirmed. `?D 3006,4436:3032,4450` reads as the band above the gate does: now
   `D`. `rcs_n4200`'s poly ends at x ~2956: extended. The tie box is larger than drawn: `?B`
   extended to y 4334.
Could not be checked by the reviewer: the buried contact's poly directly under the thin metal's
edge line (inferred by likeness to `tla`'s); `tla`'s VSS arm y 3818-3836, which reads field-like
in the chip-2 stripped shot (Ambiguity 18).
`tools/t.sh tl2 sameconn.py 57acc95` after the fixes: CONNECTIONS DIFFER (23 differences), every one
of them the join of `rcs_bd3330` with `rcs_g4240`+`rcs_x1`+`tl1_w4025` (the gates of that net,
the load's gate, the two equations): what finding 1 intends.

Round 1: one finding that changes a connection, fixed.

Round 2 (fix check, 2026-11-18 03:00 +0000, a fresh agent on claude-fable-5-2, against commit 57acc95, at
commit 41669bf; images in `cache/scratch/tl2/review-6/`). Told the four changes and asked whether
the new vertical poly is one poly from `tla`'s row to the arm and the box, clear of `tla`'s
diffusions north and east of it, whether `tla`'s row is continuous from that corner to its gate,
and whether the extended gate poly and the now-firm link touch anything. It found the changes
right (the poly one piece from y 4238 to y 4294 in four shots with nothing crossing, clear of the
strip to the north and the diffusion to the east; the arm one salmon band; the column's edge at
x 3028-3031; the gate poly's end followed by field; the link diffusion, clear of the row and the
pad; `sameconn` showing only the merge) and one error in what they joined:
1. **Changes a connection. Confirmed.** `tla`'s row `P 2945,4230:3400,4250` is broken at about
   x 3000-3020, in the gap between R3 and the thin metal, over an island of field (x 2990-3030,
   y 4222-4265): the new poly joins only the west piece (the gate over R3's column), and
   `rcs_x1` is only the east piece. So `rcs_bd3330` and `rcs_x1` are two nets and the alias was
   wrong. Tracer: `px.py row 4241 2984 3040 3`, `px.py col 3014 4196 4300 4` (clean shot green
   in the gap from y 4228 to y 4260; both metal shots not orange there), `review-6/gap_m.png`.
   Fixed: `tla`'s row and diffusion split (commit 0239da7, a commit of its own), the alias
   `rcs_x1` = `rcs_bd3330` removed, the poly labelled `tl2_w4260` and aliased to `rcs_bd3330`
   across the `?` tie. Now `rcs_n4200` = NOT((`clk_tl` AND `rcs_cond`) OR `rcs_x1` OR
   `rcs_bd3330`), and `rcs_bd3330`, `rcs_u3288` as before round 1's fix.

Round 2: one finding that changes a connection, fixed.

Round 3 (fix check, 2026-11-18 03:12 +0000, a fresh agent on claude-fable-5-2, against commit 41669bf, at
commit 733f03e; images in `cache/scratch/tl2/review-7/`). Told the one finding of round 2 and its
fixes in `trace/tla.txt` and `trace/tl2.txt`, and asked: is the break in the row real and are
the poly ends where drawn; does each gate piece cross its column, is there field between the
columns under and beside the gate, is the diffusion joined above and below; does the west band
join anything but the vertical poly; does the east row still reach its gate. Checked at 6-8x in
all four shots with profiles: the break is real in both chips (row y 4241: poly to x ~3001,
field x 3004-3016, poly from x ~3019; down x 3015 the clean shot green without interruption
y 4228-4261; both metal shots dim 87/79/43 in the gap where the rows y 4114, 4162, 4416 are
orange 170/125/55); the columns' edges are dark lines at x 2950/2990 and x 3028/3066, the island
field from y ~4220 to ~4267 with both poly ends inside it, diffusion across the gap above
(y <= 4216) and below (y 4274-4288); the west band joins only the vertical poly, no contact to
R3 and no other poly; the east row continuous from x 3020 to x 3400. `sameconn` against 41669bf
(26 and 32 differences): all intended; `rcs_u3288` is `tla`'s own NOR(`rcs_g3245`,
`rcs_bd3330`) again. No finding. Remarked, older than this change and geometry only: the west
edge of `tla`'s strip below the gate is at about x 2966 at y 4276, drawn 2950 (left; handoff).

Round 3: no findings.

### Run 4 (the inverter of `rcs_cond`, the column top: pieces 3 and 4, and the edit to `trace/tla.txt`)

Round 1 (full review of both pieces and of commit d64bc8c, 2026-11-18 11:27 +0000, a fresh agent on
claude-fable-5-2, at commit 57f4875; 12 images in `cache/scratch/tl2/review-8/`). Told to suspect:
whether there is field or one buried-contact box between `rcs_cond_lat`'s pad and the column top,
and whether the band y 4514-4530 is diffusion and reaches the VSS contact (2990,4513); the
junction of the gap poly with `tla`'s g1 band (an edge under one poly or a break), g1's run west
under R3, and the gap poly's free north end against the row y 4011-4030 (the green ring at
(2937,4039)); the vertical poly x 2878-2898 as one poly with the plate and the row; the node's
diffusion across the gap and across R3's west edge; the contact (2804,4084) and what else is
under R2; the tie; anything undrawn in x 2780-3070, y 4000-4150 and x 2990-3075, y 4490-4540.
It checked each with `px.py` / `textmap.py` profiles in all four shots and views at 4x or more:
the contact (ring with a bright centre in both metal shots, green hole; the pale patch at
(2804,4054) has no ring), the plate (one poly, y 4050-4109, single edge lines at y 4064 and
y 4094, tan boxes at both ends), the vertical poly (unbroken y 4015-4060 in both chip-2 shots)
and the row to its pad (no contact of thin E or R3; the dot at (2976,4022) is in the chip-2
metal shot only), the node across the gap (tan, channel-bright poly, one faint edge at x 2958,
tan from x 2961), the field between the row and the gap poly (y 4036-4044, 154-168/151-153 in
the metal shot against poly 170-183/125, the same in the chip-1 metal and chip-2 stripped
shots), the line at y 4100-4104 (a single 6 px diffusion edge, like the one at y 4062), g1
continuous from x 2947 to its contact (3105,4112), no contact of thin E on the node, the strip
between pad and band (khaki in the clean shot, green in the chip-2 stripped shot, red equal to
green in both metal shots, no poly across it), both extracted equations and `unsure.py`,
`opendiff.py` in both regions (nothing undrawn), no VSS contact between g1 and g2.
Findings, each checked by the tracer; all four are geometry only:
1. The VSS diffusion east of R3 at x 3009-3020, y 4490-4514 is not drawn, and it runs into
   piece 4's band with no edge. **Confirmed** (`px.py col 3015 4480 4532 4`, `px.py row 4502 3000
   3030 3`): `D 3004,4490:3019,4530` added. Same nets (the band was already on the box).
2. The tie's heavy-outlined box is at x 2872-2900, y 4113-4141, where the `?P` arm was drawn, not
   25 px east. **Confirmed** on the reviewer's `tie_ma.png` and `r4_ov4.png`: the three `?` items
   redrawn (`?P` tab, `?D` west from the strip's end, `?B` on the box). Same connection, still `?`.
3. The pull-down's gate poly is x 2938-2957, drawn 15 wide. **Confirmed** (`px.py row 4080`: channel
   colour to x 2951, the edge at x 2957-2960): drawn to x 2957.
4. Two comments in `trace/tla.txt` still said "pass transistor"; the name `rcs_cond_lat` now
   misleads. **Confirmed**: comments corrected; the rename is proposed in the handoff.
It could not check: the tie itself (both links cross heavy outlines); g1 under R3 at x 2953-2972
rests on the clean shot and the chip-1 metal shot only.
Connections before and after the fixes:
`tools/t.sh tl2 sameconn.py 57f4875`: `connections identical`;
`.venv/bin/python tools/sameconn.py 57f4875`: `connections identical`.

Round 1: no findings that change a connection.

### Run 5 (the wiring north of y 2630: piece 5)

Round 1 (full review of the piece, 2026-11-18 12:36-12:47 +0000, a fresh agent on claude-fable-5-2,
at commit 89fb577; 8 images in `cache/scratch/tl2/review-9/`). Told to suspect: the corner of the
y 2598 metal beside the pad (3453,2553) (trap 16) and whether the y 2554 metal ends on that pad;
the join of `tl1_w2592`'s poly row to the pad (2868,2596) across the pad's dark outline; that
what leaves the pad (3453,2553) north is poly and is on the pad; any contact or tap along the
two long metals, and whether the upper piece y 2501-2517 touches anything; the arm's continuity
into R3 and the dark line at y 2970-2978; anything undrawn in x 2817-3533, y 2500-2960; and the
negative claim about the "poly bar" at y 5648-5662.
It checked: the east pad at 4.4x in four shots and a 3 px text map (the metal ends on the pad;
bare ground at x 3484 on every row y 2536-2581 in both chips and an open green strip x 3478-3484
in the clean shot between the pad's ring and the vertical metal: two nets; `follow.py` from
(3300,2553) stops at x 3460); the poly north of the pad (x 3447-3472, continuous into the pad in
the clean and chip-2 stripped shots, straight north past y 2472); the west pad at 4.8x with
`px.py` rows 2591 and 2597 and column 2846 (orange poly up to the ring at x 2852 in both metal
shots; in the clean shot dark-red poly passes into salmon with no field between; the pad-to-metal
join profiles like `tl1`'s two pads); text maps along both metals (protected field throughout, no
ring present in both chips; single-chip blemishes at (3232,2596), (3060,2558), (3038,2602));
`follow.py` along the y 2598 metal (corners (3506,2593), (3504,2511), on to x 3752; nothing
touches the upper piece); the arm into R3 in both chips (one chip-2 blemish at (2920,2928)); the
line at y 2974 (6-8 px, beyond the rail both sides, protected poly under R3 at y 2978-2992); the
plane's edge (y 2507, east end x 3388); the bar at 4x in four shots (open field; a chip-2 blob at
(3255,5656) is in neither chip-1 shot); the extraction (0 errors, no `?` item in the piece).
Finding, checked by the tracer; geometry only:
1. The VSS arm's top edge is at about y 2893, not y 2915: the arm lies over the poly row
   y 2890-2908, and the notes' sentence that `tl1`'s y 2905 was too wide is wrong. **Confirmed**
   (`review-9/armtop.png`, 6x: the arm's east edge line runs up to y 2893 in both metal shots;
   `px.py row 2900 2960 3044 4` and `px.py col 2990 2880 2924 3`: the row is protected salmon in
   the clean shot west of x 3004 and from y 2892, open poly from x 3008; dim metal with red equal
   to green over the row, orange east of the arm). No contact on the row there. Redrawn
   `M 2810,2893:3004,2948`; the notes, the ports and the floor-plan line corrected. Same
   connections (the row was already drawn passing; a metal over a poly joins nothing without a
   contact).
It could not check: where the poly goes north of y 2470 (the plane extends east there, above
y 2465, so the poly may pass under it); the band y 2640-2890 was looked at only at 1.7x; under
the metals the chip-2 stripped shot is fringes and was not used.
Connections before and after the fix:
`tools/t.sh tl2 sameconn.py 89fb577`: `connections identical`;
`.venv/bin/python tools/sameconn.py 89fb577`: `connections identical`.

Round 1: no findings that change a connection.

## Not done

- **What is left in the gate column** (run 3 traced y 3690-3840 and y 4230-4530, run 4
  y 4005-4145 and the column top at y 4504-4530): the lower-left corner of piece 2's VSS box
  (field at x 2952-2961, y 4520-4529; the box is drawn as a rectangle: a shape only); `tla`'s tie
  of `rcs_bc3460`'s load (Ambiguity 15).
  **Sweep at tracing zoom** (run 5; run 4's was at 1.05x): the column x 2776-3086, y 2940-5340 in
  four views at 2.05x, metal | clean, with every package's trace outlined (`r5_col0.png`-
  `r5_col3.png`): no box, plate, pad or contact ring without an outline, except the tab and oval
  at the top of `rcs_bc3460`'s load plate ((2868-2902, 3832-3862); `r5_c1.png`, 5x, four shots),
  which is Ambiguity 15. Five marks on R2 in the chip-2 metal shot ((2810,3170), (2805,4362),
  (2806,4935), (2800,5130), (2820,5160)) are not contacts: chip 1's metal is bright at each, and
  the clean shot under them has the colour of the rail's centre line where there is no mark
  (`px.py pt ... metal,metal1,acid1b`: 139-174/131-150/106-122 at the marks, 150/144/111 at
  (2805,3743); the known contact (2804,4084) is 91/115/75). **Under the middle of R2 the clean
  shot is grey (red about equal to green), not pink**, between the boxes all the way down, so
  `tools/tla_contacts.py` lists a candidate every 50-100 px there (32 on R2, 51 on R3 against 19
  and 15 drawn contacts: `cache/scratch/tl2/railcontacts.py`); the comparison of candidates with
  drawn contacts that run 4's handoff proposed does not work on these rails. `r5_rails.png` (both
  rails, both metal shots, 1.1x, drawn contacts outlined) is too small to decide a ring.
  The strip south of the foot (x 2800-3550, y 5640-6360, `r5_south.png`, 0.9x): east of the small
  cluster there is only open field between `tla`'s metal (y 5677, x 3527) and the VSS metal
  (y 6250-6292); everything there has an outline.
- North of y 2630 is drawn (run 5, piece 5). Left there, all outside the strip: `tl1_w3333`'s poly
  north of (3460,2500) and the plane above y 2500 (the band y 2180-2500, in no package);
  `tl1_w2592`'s metal east of (3533,2509) (`follow.py`: east to x 3752, in `tl3`'s strip).
- The rows that leave east at x 3533 and the two metal arms (ports table): their far ends are
  in tl3's strip. `rcs_x1`'s driver is east of x 3533 on the row y 5371 (the rows y 4201 and y 5110 end on tl3's gates); `tl3_w3982`'s on track J's arm.
- (Done, run 5: the "poly bar" along y 5655-5670 is open field, not a feature: Logic, "North of
  y 2630", last paragraph.)
- `tla`'s bus pieces: tracks A-E are complete in `tla`'s trace between y 2940 and y 5700 as far
  as the follower shows (`cache/scratch/tl2/pieces_AE.txt`), except track B's two contacts above.
- The rows under the foot east of x 2817 are done (y 5371, 5458 by run 2; the others by `tla`,
  `bw`, `amrw`).
- `rcs_thin_e`'s row east of x 3533 (towards its driver) and `tla_w3376`'s metal south of
  y 6350.
- The VSS metal south of (3281,6350).

## Corrections from `tl1`, `tl3` (coordinator, from the handoffs of 2026-11-18, second batch)

- Ports, the row of `tl1_w5936`: the wire goes on up the west margin and leaves north at (2380,2498)
  (`tl1` run 5).
- Ports: the rows at x 3533, y 5371 (`rcs_x1`), 5415 (`tl3_w5025`), 5458 (`tl1_w4937`), 5498
  (`tl3_w4546`), the arms y 5374 (`tl3_w3982`) and 5435 (`tl3_w4763`), and the row y 2899 are drawn on
  in `tl3`. "`rcs_x1`'s driver is east of x 3533 on the row y 5371" is not so: that row ends on latch C's
  clear pad (4192,5373), whose metal goes on south and east to (4250,5895) and on into `tl5`'s row
  y 5890; the driver is beyond that.
- `tl1_w4937` is the net of `tl3`'s thin metal x 3948-3962, and by it `tl3_e3550` (AMB-032);
  `tl1_w3594` is `tcw_a` (AMB-033).

## Corrections (coordinator, from the handoffs of 2026-11-19)

- `tl1_w2592` is NOT `sl_eq_r5` (`r9m_l1w`), driven from the east (`eof`); "follow.py: on to x 3752"
  was the follower turning onto the wide metal x 3648-3760; the metal ends on the pad (3606,2510).
- `rcs_thin_e`'s row east of x 3533 ends on the pad (3973,6329), whose metal goes south to `ur`'s pad
  (3968,6410) (`tl3` run 11); `tl3_w3982`'s driver "on track J's arm": the arm leads to `tl5_w5936`;
  `tl3_w4763` is `tc1_o3527`.
