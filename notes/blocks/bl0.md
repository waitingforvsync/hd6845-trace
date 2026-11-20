# bl0: the gate group that the buffered RES and LPSTB pins reach

Lead group (user, 2026-11-20): **what the chip does while RES is low and LPSTB is high**. The gate
group lies between the left bus field and the bottom-left logic (x 5850-6330, y 15200-15800); its wires
are followed from there. Geometry: `trace/bl0.txt`. Ports: `ports.d/bl0.txt`. Coordinates are
metal-shot pixels. Evidence: `cache/scratch/bl0/` (`survey.md` holds every measurement with its command).

## Status

Run 1 (richtw1's session, Claude Fable 5.2; 2026-11-20). Two pieces, 11 transistors, 11 nets, no uncertain
item; not yet reviewed.

- **Piece `pin`** (the gate group, x 5850-6330, y 15200-15800; 7 transistors). `lpstb_nres` =
  NOR(`bl0_lpstb_n`, `res_b`) with `bl0_lpstb_n` = NOT `lpstb_b`: **`lpstb_nres` is high while LPSTB is
  high and RES is low, and only then**, the condition in which the reset NOR (`rst` = NOR(`lpstb_b`,
  `res_b`), `lc1`) does not reset. A third gate on the same rail, `bl0_w15412` = NOT `bl0_w15088`, inverts
  a line that only passes by.
- **Piece `g1`** (2026-11-20 12:38 +0100; 4 transistors and 3,300 px of wire). `lpstb_nres` has one load: a gate in the
  left column of the memory address counter (`larr`), at the gap between its carry groups s0-s6 and s7-s9:

  ```
  bl0_w14308 = NOT( bl0_w14113 OR lpstb_nres )
  larr_l0_g1 is pulled to vss while bl0_w14308 is high
  ```

  `larr_l0_g1` is `larr`'s line that every row of s7-s9 pulls low while its bit is 0, and it is the carry
  into s10 (`notes/blocks/larr.md`). So, with `larr`'s rows (`TRACE=bl0,larr tools/netlist.py`): the carry
  into s10 can be high only while s7, s8 and s9 hold 1 **and** (`bl0_w14113` OR `lpstb_nres`) is high.
  **While RES is low and LPSTB is high the term `bl0_w14113` is overridden**: the counter's top four rows
  step whenever s7-s9 are all ones, whatever `bl0_w14113` says. What `bl0_w14113` is (believed: the carry
  out of s0-s6) and what pulls `larr_l0_g1` up are not traced yet.
- `bl0_w14308` has two more loads on the same metal, not followed: see Not done.

## Inventory

| Piece | x | y | What |
|---|---|---|---|
| U rail | 6013-6328 | 15216-15800+ | wide metal U: left arm x 6013-6067 (four pull-down contacts), top bar y 15216-15268, right arm x 6273-6328; `vss` by the loads' orientation |
| inner rail | 6187-6241 | 15317-15800+ | wide metal inside the U, top end y 15317, three load contacts; `vcc` by the loads' orientation |
| G1 | 5924-6242 | 15312-15445 | inverter: gate band y 15357-15380 on a diffusion box x 5957-6090 (W 133); load plate x 6155-6188 |
| G2 | 5895-6242 | 15441-15567 | inverter of `lpstb_b`: gate band y 15487-15510 (W 50); load plate x 6127-6188 (26/61) |
| G3, G4 | 5895-6242 | 15571-15779 | NOR: gate bands y 15618-15640 and 15705-15728 on one column (W 71 each), output between them; load plate x 6113-6155 |
| pin lines | 5856-6450 | 15000-15729 | `res_b`: track x 6366 to a pad (6363,15132), metal west along y 15133 and south at x 5866 to G4's pad (5910,15719); `lpstb_b`: track x 6408 to a pad (6408,15176), metal west along y 15177 and south at x 5910 to G2's pad (5910,15501) |
| `bl0_w15088` | 5700-6450 | 15075-15380 | metal y 15080-15100 between pads (5755,15088) and (6320,15088); middle pad (5932,15088) with a poly column south to G1 |
| `lpstb_nres`'s wire | 2537-5986 | 14339-15690 | poly row y 15676 west to a pad (4867,15675); track x 4867 north to a pad (4867,14436); poly row y 14436 west across the left array to x 2798; north under the left column's vcc rail (x 2798-2818) to y 14362; west along y 14371; gate band y 14339-14361 under the vss rail |
| left-column NOR | 2517-2836 | 14105-14460 | under the vss rail x 2605-2655: source box with a contact (2618,14228), gate band A y 14253-14274 (`bl0_w14113`, by a poly up the west side from the row y 14105-14122), output node, gate band B (`lpstb_nres`), source with contacts (2620,14385), (2633,14433); margin x 2580-2603; load plate x 2706-2748 on the output strip y 14292-14326, box and contact (2803,14312) on the vcc rail x 2783-2832 |
| `bl0_w14308`'s wire | 2432-2777 | 14292-14708 | buried contact (2566,14308), poly row west to a pad (2459,14307), metal x 2450-2468 south through a pad (2459,14505) to a pad (2459,14700); the second pad is on the poly row y 14467-14494, the third on a row y 14688-14708 |
| pull-down on `larr_l0_g1` | 2660-2860 | 14434-14533 | the row y 14467-14494 over a diffusion x 2689-2760 between two field islands (x 2661-2687, x 2760-2777); source joined to the NOR's lower source by a neck y 14434-14446; drain east as a strip y 14517-14533 under the vcc rail onto `larr`'s diffusion at x 2850 |

## Logic

Traced (extraction, `tools/t.sh bl0 netlist.py`: 8 nets, 7 transistors, 0 errors, 0 warnings):

```
bl0_w15412  = NOT bl0_w15088
bl0_lpstb_n = NOT lpstb_b
lpstb_nres  = NOR(bl0_lpstb_n, res_b)          = lpstb_b AND NOT res_b
```

| Transistor | W/L | Gate | Between |
|---|---|---|---|
| G1 pull-down | 133/23 | `bl0_w15088` | `vss`, `bl0_w15412` |
| G1 load | 65/33 | `bl0_w15412` | `vcc`, `bl0_w15412` |
| G2 pull-down | 51/22 | `lpstb_b` | `vss`, `bl0_lpstb_n` |
| G2 load | 26/61 | `bl0_lpstb_n` | `vcc`, `bl0_lpstb_n` |
| G3 pull-down | 71/22 | `bl0_lpstb_n` | `vss`, `lpstb_nres` |
| G4 pull-down | 71/23 | `res_b` | `vss`, `lpstb_nres` |
| G3/G4 load | 40/42 | `lpstb_nres` | `vcc`, `lpstb_nres` |

How each connection was read (4x in the chip-2 metal and stripped shots and the clean shot: `q1`-`q6.png`;
5-6x: `q7`-`q9.png`; overlays `o_a1b.png`, `o_met.png`):

- One diffusion column under the U's left arm, x 6008-6058, in three separate pieces: y 15312-15403 (G1),
  y 15441-15545 (G2), y 15571-15779 (G3, G4). Between the pieces the clean shot shows field under the rail
  (130/149/106 at y 15413-15438 and y 15548-15568, against 186-191/166-172/122-124 for the nodes):
  `tools/bl0_edges.py col 6035 15290 15790`. Gate bands by the clean shot's red top edge and dark bottom
  edge on that column.
- Each output leaves the column both ways: east as a diffusion strip under its load plate to a box with a
  contact on the inner rail, and (G1, G3/G4) west by a buried contact onto the end of a poly row
  (boxes x 5955-5988 at y 15399-15430 and y 15661-15691). G2's output goes west by a narrow neck to a
  buried contact (x 5955-5988, y 15525-15552) on the end of an L-shaped poly that is G3's gate.
- Each load plate is tied to its own output: boxes (6091-6124, 15404-15441), (6125-6155, 15471-15498),
  (6103-6142, 15711-15746), each reached by an arm of the output's diffusion.
- `res_b` and `lpstb_b` are busl's two tracks: each ends on a pad whose metal turns west
  (`tools/follow.py 6300 15132 W`, `6300 15174 W`: corners (5862,15137), (5910,15181)).
- Every place where a metal of the piece crosses a poly was read as text in both metal shots and the
  clean shot (`tools/textmap.py`, ten crossings, with the pad (5910,15501) as the known contact): two
  dark bars with bright metal between and no green hole at each; no contact.
- The poly column of `bl0_w15088` ends in G1's band and is not on the row below it:
  `px.py col 5936 15372 15408 3 metal,acid,metal1` gives 12 px of field between two edge lines
  (chip-2 metal 166/151/92, stripped 149/154/83, chip-1 metal 148/124/68).

Believed, not traced: this is the test mode of the 6845 family (other data sheets; Hitachi's says only
that RES resets while LPSTB is low). What `lpstb_nres` does is traced from its loads (next pieces).

### Piece `g1`: where `lpstb_nres` goes

Traced (`tools/t.sh bl0 netlist.py`: 11 nets, 11 transistors, 0 errors, 0 warnings; with `larr`:
`TRACE=bl0,larr .venv/bin/python tools/netlist.py`, 0 errors):

```
bl0_w14308 = NOR(bl0_w14113, lpstb_nres)
larr_l0_g1 : pulled to vss by bl0_w14308 (W/L 71/27) and by larr_n4_s7, larr_n4_s8, larr_n4_s9 (larr's rows)
```

| Transistor | W/L | Gate | Between |
|---|---|---|---|
| band A | 71/21 | `bl0_w14113` | `vss`, `bl0_w14308` |
| band B | 71/22 | `lpstb_nres` | `vss`, `bl0_w14308` |
| load | 34/42 | `bl0_w14308` | `vcc`, `bl0_w14308` |
| group-line pull-down | 71/27 | `bl0_w14308` | `vss`, `larr_l0_g1` |

How it was read (`lc_*.png` 2.25x, `lcz_*.png` and `lcn_*.png` 3.6x, `lq0`-`lq10.png` 4x three shots,
overlays `og1_acid1b.png`, `og1_metal.png`; measurements in `survey.md`):

- **The wire.** The row y 15676 is poly from the gate group to the pad (4867,15675) (chip-2 stripped
  shot, red minus green over 10 at every sample but two 6 px edge bars; no pad on the way at 1.15x,
  `rw_metal.png`). The track x 4867 is one metal between its two pads (`tl5_tracks.py v 4867 14415 15700`:
  no stretch of 25 px without metal; the two greenish spots it lists at y 14898 and y 15375 are rows that
  cross under it, with 9 px edge bars and no ring: `textmap.py`). The row y 14436 is poly from the pad
  (4867,14436) to x 2798 (the same test: three edge bars of 7-9 px) with no contact hole on it
  (`tl5_tracks.py h 14436 2845 4850`: six stretches of 6-11 px, none under +5); it turns north under the
  vcc rail as an L without a pad (`lq4.png`).
- **The NOR.** Gate bands by the clean shot's red top edge and dark bottom edge on the column x 2630:
  A y 14253-14274, B y 14339-14361. Above A a box with a contact (ring in both metal shots, speck in the
  clean shot); between A and B the output node, with **no contact** (clean shot plain, rail's metal
  unbroken: profile along x 2645); below B the source with two contacts. Both sources are on the same
  rail, so the node between the bands is the output of a NOR, as in the gate group's G3/G4. The diffusion
  is wider than the rail on the west (margin x 2580-2603: an edge line crosses both bands at x 2580).
- **The output** leaves three ways: east as a strip under the load plate to a box with a contact on the
  other rail (the strip is joined to the node under the rail: `px.py row 14308 2640 2706 4`, tan to x 2664,
  the 8 px line of the rail's protected margin, then open diffusion's green to x 2696, plain in the
  chip-2 metal shot); north from the strip by an L of diffusion to the buried contact of the plate's
  finger (the load's tie); west from the margin by a buried contact (2553-2580, 14294-14321) onto a poly
  row to the pad (2459,14307).
- **The metal x 2459** is one piece through three pads (`tl5_tracks.py v 2459 14290 14780`: 18-21 px
  without metal at each ring, 76 px south of the third: it ends there; contact holes at y 14309, 14507,
  14701).
- **The pull-down on `larr_l0_g1`.** The row y 14467-14494 from the second pad crosses field under the
  vss rail (below the band the clean shot has no diffusion: 147/145/111 against 190/175/130) and then a
  diffusion between two field islands. Inside the west island the chip-2 shots read field (metal
  168/148/87, stripped red minus green -7 and -8, against 169/131/91 and +25 on the diffusion beside it).
  The source side is joined to the NOR's lower source by a neck north of that island
  (`bl0_edges.py row 14440 2640 2720`: uniform from the rail's edge to x 2720 in the chip-2 metal and
  stripped shots, no edge line). The drain side leaves east as a strip between two edge lines under the
  vcc rail and runs into the box of `larr`'s contact (2892,14523) (`lq10.png`).
- **The rails.** x 2605-2655 carries all the pull-down contacts and x 2783-2832 the load's: `vss` and
  `vcc`. They are the left edge column's two rails, which `tla`, `tl1` and `ur` name the same way further
  north (each by the loads); the stretch between is not drawn.

Believed, not traced: `bl0_w14113` is the carry out of the counter's first seven rows, so that
`larr_l0_g1` = (carry out of s0-s6) AND s7 AND s8 AND s9 in normal operation; and RES low with LPSTB
high is the 6845 family's test mode, here letting the top four rows count without the low seven.

## Ports

| Name | Layer | Where | Direction | Note |
|---|---|---|---|---|
| `res_b` | M | (6359-6373, 15000) | in | busl's track x 6366 |
| `lpstb_b` | M | (6401-6415, 15000) | in | busl's track x 6408 |
| `res_b` | P | (6450, 15122-15142) | ? | poly row on east from the pad (6363,15132), seen to x 6790 |
| `lpstb_b` | P | (6450, 15166-15186) | ? | poly row on east from the pad (6408,15176), seen to x 6790 |
| `bl0_w15088` | P | (6450, 15078-15098) | ? | poly row on east from the pad (6320,15088), seen to x 6790 |
| `bl0_w15088` | P | (5700, 15078-15098) | ? | poly row on west to a pad (4909,15088); a track x 4909 from the north ends there |
| `bl0_w15088` | M | (5750-5764, 15700) | ? | thin metal south from the pad (5755,15088), followed to about (5762,15768) |
| `bl0_w15412` | P | (5600, 15401-15425) | out | poly row west to a pad (4909,15414), track x 4909 south |
| `bl0_w14113` | P | (2500, 14105-14122), (2860, 14105-14122) | in | the row runs on both ways (west under the wide metal, east into the array) |
| `bl0_w14308` | P | (2405, 14688-14708), (2550, 14688-14708) | out | the row of the metal's third pad (2459,14700) runs on both ways |
| `larr_l0_g1` | D | (2860, 14517-14533) | ? | onto `larr`'s diffusion (2850-2880, 14508-14540) and its contact (2892,14523) |
| `vss` | M | (2605-2655, 14090), (2605-2655, 14560) | - | the left edge column's rail, on both ways |
| `vcc` | M | (2783-2832, 14090), (2783-2832, 14560) | - | the same |
| `vss` | M | (6013-6067, 15800), (6273-6328, 15800) | - | both arms of the U run on south |
| `vcc` | M | (6187-6241, 15800) | - | the inner rail runs on south |

## Ambiguities

1. **Which rail is which supply.** Neither rail is followed to a named supply. The loads (gate tied to
   the output, other end on the inner rail) make the inner rail `vcc` and the U `vss`. Settled by
   following either rail to a drawn supply.
2. **G2's output strip east of the rail (x 6075-6127, y 15521-15547).** Its south flank reads orange in
   the chip-2 shots (167/109/60 at y 15535-15537), like poly. Read as diffusion: on its centre line the
   chip-2 metal shot is plain and uniform from the rail to the load's arm (174-181/130/89-99,
   `px.py row 15531 6070 6124 6`), the stripped shot's red minus green is +17 to +39 all along, and strip
   and arm are one outlined area at 5x (`q7.png`). The orange is the flank of the edge line (trap 38).
   As poly it would have no end on the rail's side.
3. **G2's output neck west of the rail (x 5988-6008, y 15524-15542).** Only 10-14 px bright between its
   edge lines (`px.py col 5994 / 6000 / 6004 15512 15556 4`), narrower than a drawn diffusion wire; at 6x
   (`q8.png`) it is continuous from the box's east side to the rail in both chip-2 shots. Read as the
   diffusion that joins G2's output to the buried contact of the L-shaped poly. No other feature reaches
   that box.
4. **A pale spot at (6706,15176)** on `lpstb_b`'s poly row under the track x 6711 (`bd1_n2`, `eof`),
   in the chip-2 stripped shot only. Both metal shots show a plain crossing (no ring, no pad) and the
   clean shot plain poly (`textmap.py 6670 15140 6745 15210 3 --acid`, `spot.png`). Read as a blemish:
   no contact. (East of this piece's drawn end; noted because it would join LPSTB to the latch on R4's match.)

5. **The left-column rails' identity** (as Ambiguity 1): `vss` x 2605-2655 and `vcc` x 2783-2832 by the
   loads, here and in three other packages; no drawn metal joins the stretches or reaches a pad.
6. **The west margin above gate band A** (x 2580-2603, y 14228-14253): drawn as part of the margin from a
   small outlined box seen at 3.6x; only band A's width depends on it (71 or 48).
7. **The field islands at both ends of the pull-down on `larr_l0_g1`.** Read as field from the chip-2
   shots (above). If the west one were diffusion the transistor would be 98 wide instead of 71; nothing
   else changes.
8. **A bump of the load plate** west of its body (x 2692-2706, y 14262-14290, an outlined corner at 4x,
   `lq3.png`) is not drawn. As poly it would lie beside the diffusion L, not on it.

## Review

Not yet reviewed.

## Not done

- **`bl0_w14113`'s source**: the poly row y 14105-14122 beyond x 2500 and beyond x 2860.
- **`bl0_w14308`'s third load**: the poly row y 14688-14708 on the pad (2459,14700), both ways.
- **What pulls `larr_l0_g1` up**, and the source of `larr_cin_s7` (the poly row y 14559-14574 from the
  left column, `larr`'s port), which decides whether s7-s9 also count freely in the test condition.
- In the same cell, seen and not drawn: a poly row y 14165-14182 from a pad (2567,14177) (a metal from the
  north, x 2555-2577) east under both rails with no transistor under the vss rail; a track x 2493-2512
  over `bl0_w14308`'s row; the wide metal west of x 2440.
- `bl0_w15412` west of x 5600: the row to the pad (4909,15414), the track x 4909 south to about
  (4905,16094) (contact candidate (4913,15856)), and its loads (the left array's Gap 2).
- `bl0_w15088`: its west row to the pad (4909,15088) and the track x 4909 north (follower: to
  (4908,10660), contact candidates (4908,11984), (4908,10699)); its thin metal south of y 15700; its
  poly row east of x 6450.
- `res_b`'s and `lpstb_b`'s poly rows east of x 6450 (towards the bottom-centre logic).
- Both rails of the gate group south of y 15800; the rest of the master-list row's region (the bus
  wiring x 4780-5850, the tracks x 6452-6841, the gate group south of y 15800).
