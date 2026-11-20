# bl0: the gate group that the buffered RES and LPSTB pins reach

Lead group (user, 2026-11-20): **what the chip does while RES is low and LPSTB is high**. The gate
group lies between the left bus field and the bottom-left logic (x 5850-6330, y 15200-15800); its wires
are followed from there. Geometry: `trace/bl0.txt`. Ports: `ports.d/bl0.txt`. Coordinates are
metal-shot pixels. Evidence: `cache/scratch/bl0/` (`survey.md` holds every measurement with its command).

## Status

Run 5 (Matt Godbolt's session, Claude Fable 5.2; 2026-11-20 10:41 -0600). One piece of wiring, no transistor,
no uncertain item: the three wires of the cross-coupled pair.

- **Piece `w5`** (wiring, 4,400 px). **The line that clears the pair is `busl_x6906`**, a track of the left
  bus field: from `busl`'s port (6841,15000) it runs on south to a pad (6842,16217), under the bus of
  horizontal metals as a poly column to a pad (6842,16562), south as a thin metal, east along y 17086 and
  south at x 6970 to a pad (6970,17561), whose poly row is the gate of the fifth unit's first pull-down.
  Its source is north of the left bus field (`busl`'s follower: to about (7078,8778)), not traced.
  `bl0_w17687` (band D) comes from a pad (7142,17713), a thin metal south and east to a pad (7424,17822)
  and a poly row east; `bl0_w17610`'s metal ends on a pad (7384,17779) with a poly row east. Both rows go
  on east under the supply rail into the routing field south of the gate column: not followed.

Run 4 (Matt Godbolt's session, Claude Fable 5.2; 2026-11-20 10:22 -0600). One piece, 9 transistors, no uncertain item;
reviewed (round 6: no finding that changes a connection): the fourth and fifth units under the rail x 7292-7342, a cross-coupled pair that `bl0_w17210` sets.

- **Piece `u45`** (9 transistors, x 7172-7522, y 17370-17755):

  ```
  bl0_w17440 = NOT( bl0_w17210 OR bl0_w17610 )
  bl0_w17610 = NOT( bl0_w17440 OR busl_x6906 OR (bl0_w17337 AND bl0_w17687) )
  ```

  With `bl0_w17337` = NOT `bl0_w17210`: **a latch that the gated light pen strobe sets** (`bl0_w17210`
  high makes `bl0_w17440` low and, if `busl_x6906` is low, `bl0_w17610` high; it stays so after the
  strobe ends) and that is cleared by `busl_x6906`, or by `bl0_w17687` once the strobe is low again.
  `busl_x6906` and `bl0_w17687` are poly rows from the west, not followed. `bl0_w17610` leaves on a
  poly to a pad (7188,17605) and a metal south (not followed); `bl0_w17440` goes nowhere else.

Run 3 (Matt Godbolt's session, Claude Fable 5.2; 2026-11-20 10:03 -0600). One piece, 2 transistors and 300 px
of wire, no uncertain item; reviewed (round 4: one finding that changes a connection, fixed; round 5, the fix check: no findings). The first loads of `bl0_w17210`.

- **Piece `u3`** (2 transistors). The metal of `bl0_w17210` (x 7178-7198) has two pads and ends on the
  second: (7188,17300), the gate of the third unit under the rail, and (7188,17472), the gate of the
  fourth. The third unit is drawn: an inverter, **`bl0_w17337` = NOT `bl0_w17210`**. Its output goes west
  onto a pad (7144,17340), from which a thin metal x 7137-7152 runs south to a pad (7143,17647) whose
  poly row is a gate band of the fifth unit under the rail (not followed). The thin metal on the same x
  north of the pad is another net: it turns west 35 px short of the pad (review round 4).
- **Surveyed, not drawn**: the fourth and fifth units (y 17420-17750), one compound structure on a wide
  diffusion west of the rail; what is read of it is under Not done.

Run 2 (Matt Godbolt's session, Claude Fable 5.2; 2026-11-20 06:38 -0600). Three pieces, 5 transistors, no uncertain item;
reviewed (round 3: no finding that changes a connection). Both pin lines followed south of y 16250 to the gate they end on.

- **Piece `xu`** (wiring). Each line goes under the bus of five horizontal metals as a poly column to a
  second pad ((6885,16516), (6929,16560)), south as a thin metal, east at a corner to a third pad
  ((6951,17038), (6990,16996)) and east as a poly row to a gate column under a rail x 7292-7342 in the
  bottom-centre logic. No transistor and no contact on the way.
- **Piece `n1`** (3 transistors). The two rows are the two gate bands of one gate, in series:
  **`bl0_w17085` = NOT(`lpstb_b` AND `res_b`)**. Neither row goes anywhere else: both end 25 px east of
  the column. So `res_b` has no second use beyond this gate (and `lc1`'s reset NOR and run 1's NOR).
- **Piece `n2`** (2 transistors). The next unit under the same rail inverts it: **`bl0_w17210` =
  `lpstb_b` AND `res_b`**, high while LPSTB is high and RES is high: the light pen strobe, passed only
  while the chip is not being reset. It leaves on a metal x 7178-7198 south to a pad (7188,17300), which
  is the gate of the third unit of the column (not drawn).

Run 1 (richtw1's session, Claude Fable 5.2; 2026-11-20). Four pieces, 13 transistors, 12 nets, no uncertain
item. All four pieces reviewed: round 1 (`pin`, `g1`) one finding, fixed; round 2 (the fix, `s7`, `pe`) no
finding that changes a connection.

- **Piece `pin`** (the gate group, x 5850-6330, y 15200-15800; 7 transistors). `lpstb_nres` =
  NOR(`bl0_lpstb_n`, `res_b`) with `bl0_lpstb_n` = NOT `lpstb_b`: **`lpstb_nres` is high while LPSTB is
  high and RES is low, and only then**, the condition in which the reset NOR (`rst` = NOR(`lpstb_b`,
  `res_b`), `lc1`) does not reset. A third gate on the same rail, `bl0_w15412` = NOT `bl0_w15088`, inverts
  a line that only passes by.
- **Pieces `g1` and `s7`** (6 transistors and 3,300 px of wire). `lpstb_nres` has one load: a NOR in the
  left column of the memory address counter (`larr`), at the gap between its carry groups s0-s6 and
  s7-s9. With `larr`'s rows (`TRACE=bl0,larr .venv/bin/python tools/netlist.py`, 0 errors):

  ```
  bl0_w14308  = NOT( larr_l0_g0 OR lpstb_nres )
  larr_cin_s7 = NOT bl0_w14308                       = larr_l0_g0 OR lpstb_nres
  larr_l0_g1  : pulled to vss while bl0_w14308 is high (and by each of s7, s8, s9 whose bit is 0)
  ```

  `larr_l0_g0` is `larr`'s line that every row of s0-s6 pulls low while its bit is 0; `larr_cin_s7` is
  the carry into s7; `larr_l0_g1` is the same kind of line for s7-s9 and is the carry into s10
  (`notes/blocks/larr.md`). So, as far as the lines are pulled up (their pull-ups are not found):

  - normally the carry into s7 is "s0-s6 all ones", and the carry into s10 is "s0-s9 all ones";
  - **while RES is low and LPSTB is high the carry into s7 is forced on**, and the carry into s10 is
    "s7-s9 all ones": the counter's upper seven rows count on every step, whatever the lower seven hold.

  Believed, not traced: this is the 6845 family's test mode (it lets the upper half of the 14-bit
  address counter be exercised in 128 steps instead of 16,384).
- **Piece `pe`** (wiring). Both pin lines go on from the gate group: each poly row runs east to a pad
  ((6885,15130), (6929,15177)) and a track runs south from it to a pad ((6882,16170), (6928,16217)); a
  poly column goes on south from each under a bus of horizontal metals. Not followed further.

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
| left-column NOR | 2517-2836 | 14105-14460 | under the vss rail x 2605-2655: source box with a contact (2618,14228), gate band A y 14253-14274 (`larr_l0_g0`: a poly up the west side, x 2517-2539, to a buried contact (2513-2545, 14100-14125) on the west end of a diffusion wire y 14105-14122 that runs east under both rails into the box of `larr`'s contact (2893,14114)), output node, gate band B (`lpstb_nres`), source with contacts (2620,14385), (2633,14433); margin x 2580-2603; load plate x 2706-2748 on the output strip y 14292-14326, box and contact (2803,14312) on the vcc rail x 2783-2832 |
| `bl0_w14308`'s wire | 2432-2777 | 14292-14708 | buried contact (2566,14308), poly row west to a pad (2459,14307), metal x 2450-2468 south through a pad (2459,14505) to a pad (2459,14700); the second pad is on the poly row y 14467-14494, the third on a row y 14688-14708 |
| pull-down on `larr_l0_g1` | 2660-2860 | 14434-14533 | the row y 14467-14494 over a diffusion x 2689-2760 between two field islands (x 2661-2687, x 2760-2777); source joined to the NOR's lower source by a neck y 14434-14446; drain east as a strip y 14517-14533 under the vcc rail onto `larr`'s diffusion at x 2850 |
| carry into s7 | 2520-2850 | 14559-14757 | inverter under the vss rail: output node y 14660-14686, gate band y 14687-14708 (the row of the metal's third pad), source box with a contact (2622,14736); output west by a buried contact (2548-2577, 14643-14670) and a poly x 2520-2540 north to the row y 14559-14574 (`larr_cin_s7`); load plate x 2740-2777 on the strip (y 14662-14678 from the rail, y 14654-14690 under the plate), box and contact (2805,14674) on the vcc rail |
| pin lines on | 6365-6946 | 15116-16250 | `res_b`: poly row y 15132 east to a pad (6885,15130), track x 6875-6895 south to a pad (6882,16170), poly column south; `lpstb_b`: poly row y 15176 east to a pad (6929,15177), track x 6919-6939 south to a pad (6928,16217), poly column south |
| pin lines under the bus | 6869-7385 | 16250-17056 | `res_b`: poly column x 6877-6899 to a pad (6885,16516), thin metal x 6879-6897 south, corner y 17039, pad (6951,17038), poly row y 17029-17051 east; `lpstb_b`: poly column x 6920-6942 to a pad (6929,16560), thin metal x 6921-6939, corner y 16995, pad (6990,16996), poly row y 16986-17007 east; both rows end at x 7385 |
| the gate of both pins | 7203-7522 | 16941-17108 | under the rail x 7292-7342: source box y 16941-16967 with a contact (7308,16960), band A y 16986-17007 (`lpstb_b`), node y 17007-17029 (no contact), band B y 17029-17051 (`res_b`), output node to y 17092; column x 7289-7360; output strip east y 17074-17092, under the load plate (x 7404-7465, y 17040-17108; diffusion y 17061-17091) to a box (7468-7522, 17030-17090) with a contact (7493,17052) on the supply rail x 7470-7520; the plate's finger (7405-7430, 17023-17042) on a buried contact at the end of an L of diffusion (neck x 7390-7402 up from the strip, arm y 17021-17042 east); output tab west y 17074-17093, buried contact (7238-7268, 17072-17096), poly west to x 7203, south to y 17180 and east as the next band |
| the inverter after it | 7172-7522 | 17110-17235 | source box y 17110-17160 with a contact (7308,17130), band y 17160-17180, output node y 17182-17215 (x 7281-7357); strip east, load plate (7404-7465, 17165-17235; diffusion y 17190-17218), box with a contact (7488,17178) on the supply rail; finger and L as above (neck x 7383-7402, arm y 17142-17166); output tab west, buried contact (7238-7268, 17194-17226), poly west to a pad (7188,17210), metal x 7178-7198 south |
| the third unit | 7128-7522 | 17247-17356 | under the rail x 7292-7342: source box y 17247-17288 with a contact (7308,17265), band y 17290-17311 (the row of the pad (7188,17300)), output node y 17313-17341 (x 7286-7354); strip east, load plate (7406-7462, 17300-17362), finger on a buried contact (7402-7436, 17270-17298) at the end of a neck x 7384-7399, box on the supply rail (7468-7522, 17251-17350); west a tab, a buried contact (7236-7266, 17322-17352) and a poly row y 17334-17353 to a pad (7144,17340) |
| `bl0_w17337`'s track | 7127-7215 | 17324-17663 | thin metal x 7137-7152 from the pad (7144,17340) south to a pad (7143,17647), poly row east |
| the fourth unit | 7172-7522 | 17370-17582 | wide stack west of and under the rail (diffusion from the edge line x 7240 to x 7327): top node y 17425-17458 (`bl0_w17440`; a buried contact with a poly cap at its west end), band A y 17461-17483, a node, band B y 17504-17527 (A and B one poly, joined west of the stack at x 7185-7205), strip y 17528-17546 and the box of the rail contact (7322,17560); east: strip under the load plate (7408-7462, 17403-17447) to the supply box (7468-7522, 17370-17470), the plate one poly with the pad (7432,17470) and a finger on a buried contact (7372-7410, 17458-17492); below it the pull-down gated by `bl0_w17610` (poly 7362-7410, 17505-17528) down to a strip y 17537-17553 from the box |
| the fifth unit | 7172-7522 | 17528-17755 | open column x 7243-7292: row `busl_x6906` y 17549-17572 (from the strip of the fourth unit's box down to the node), buried contact (7240-7268, 17590-17620) with the poly of the pad (7188,17605), band C y 17636-17656 (`bl0_w17337`), band D y 17676-17698 (`bl0_w17687`), both also under the rail; box of the rail contact (7308,17727) and a strip y 17703-17722 east to x 7420; east of the rail the node's block (7364-7402, 17612-17664), buried contact (7366-7402, 17574-17614) under the finger of the load plate (7406-7462, 17575-17632), supply box (7468-7522, 17570-17660), and the pull-down gated by `bl0_w17440` (poly 7366-7420, 17668-17695; pad (7434,17684) of the thin metal x 7423-7441 from the pad (7432,17470)) |
| `busl_x6906` south of the bus field | 6826-7215 | 15000-17578 | track x 6834-6848 from y 15000 to a pad (6842,16217); poly column x 6836-6854 under the bus to a pad (6842,16562); thin metal south to y 17085, east to x 6970, south to a pad (6970,17561); poly row y 17549-17572 east under four tracks to the fifth unit |
| `bl0_w17687`'s wire | 7126-7465 | 17676-17838 | the row's west end on a pad (7142,17713); thin metal x 7137-7151 south to a corner (7151,17829), east to a pad (7424,17822); poly row east |
| `bl0_w17610`'s wire | 7178-7465 | 17595-17795 | from the pad (7188,17605) a metal south to a corner (7192,17786), east to a pad (7384,17779); poly row east |

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
bl0_w14308 = NOR(larr_l0_g0, lpstb_nres)
larr_l0_g1 : pulled to vss by bl0_w14308 (W/L 71/27) and by larr_n4_s7, larr_n4_s8, larr_n4_s9 (larr's rows)
larr_l0_g0 : pulled to vss by larr_n4_s0 ... larr_n4_s6 (larr's rows)
```

| Transistor | W/L | Gate | Between |
|---|---|---|---|
| band A | 71/21 | `larr_l0_g0` | `vss`, `bl0_w14308` |
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
- **`larr_l0_g0` onto band A** (corrected in review round 1). The row y 14105-14122 is a diffusion wire, not poly: in its open stretch x 2680-2770 the chip-2 metal shot is plain (167-177/131-139/86-91, against 158-170/111-124/63-70 on the poly row y 14174 beside it), chip 1's the same (142-156/114-125 against 129-157/67-92), and the clean shot green; under the rails it has the tan of the drain strip (206/166/135), not a gate band's salmon. Its east end is one piece with the box of `larr`'s contact (2893,14114); its west end is at x 2515, where band A's poly ends on it in a heavy-outlined box with a light centre, the same in profile as the output's buried contact (`px.py row 14112 2500 2556 4` against `row 14308 2540 2596 4`: dark walls 20-24 px apart, a plain centre, in both chip-2 shots).
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

### Piece `s7`: the carry into row s7

```
larr_cin_s7 = NOT bl0_w14308
```

| Transistor | W/L | Gate | Between |
|---|---|---|---|
| pull-down | 69/21 | `bl0_w14308` | `vss`, `larr_cin_s7` |
| load | 36/37 | `larr_cin_s7` | `vcc`, `larr_cin_s7` |

One cell south of the NOR and of the same build (`s7_*.png` 2.25x, `s7q1`-`s7q3.png` 4x three shots,
overlay `os7_acid1b.png`). The gate band is the poly row of the metal's third pad (2459,14700), which
runs east from the pad into the band (y 14687-14708 by the clean shot's edges on the column x 2630).
Above the band the output node (no contact: plain tan, no ring), below it a source box with a contact
(2622,14736). The node goes east as a strip (plain and uniform from the rail to the plate in the
chip-2 metal shot, `bl0_edges.py row 14668 2500 2850 metal`) under a load plate to a box with a contact
on the vcc rail, with the plate's arm tied back by a buried contact (2700-2724, 14695-14726); and west
by a tab to a buried contact (2548-2577, 14643-14670) on a poly that runs north as one orange run
(`bl0_edges.py col 2530 14550 14740 metal`: y 14560-14661) into the row y 14559-14574, which `larr`
draws from x 2850 east as `larr_cin_s7`. Field north of the node under the rail (green in the clean
shot, y 14590-14653): no second pull-down.

### Piece `pe`: the pin lines beyond the gate group

Wiring only. `res_b`'s poly row y 15132 and `lpstb_b`'s y 15176 are poly from their first pads to pads
at (6885,15130) and (6929,15177) (chip-2 stripped shot: one edge bar of 6 px, and the blemish of
Ambiguity 4), and end there (`er_pads.png`: bare ground east of each pad). From each a track runs south,
one metal to a pad at (6882,16170) and (6928,16217) (`tl5_tracks.py v 6883 15120 16240`, `v 6926 ...`: no
stretch without metal but the rings; where `res_b`'s track crosses `lpstb_b`'s row, two edge bars and no
hole). Each of those pads stands in a staggered row of pads whose polys go on south under a bus of
horizontal metals (`pe_end.png`).


### Pieces `xu`, `n1`, `n2` (run 2): where both pin lines end

South of the staggered pads the two lines stay side by side: poly columns under the bus of five
horizontal metals (field between them: pink in the clean shot under the metals, residue rows in the
gaps), pads, thin metals south (no break and no contact: `follow.py 6885 16600 S`, `6928 16640 S`), a
corner each, pads, and two poly rows east under three tracks (x about 7050, 7095, 7140) with field on
both sides all the way (`px.py row 16975 / 17017 / 17060 6960 7290 15 acid,acid1b`).

They end as the two gate bands of one column under a rail x 7292-7342, 25 px beyond its east edge
(`railprof.py 7295 7340 16860 17400`: diffusion 16950-16983, gate, diffusion 17011-17026, gate,
diffusion 17054-17091). The top box has the column's one contact to the rail ((7308,16960): a ring with a
bright centre in both metal shots); the node between the bands is 22 px high and has none; the lower
node is the output. With the rail as `vss` (the loads' other ends are on the rail x 7470-7520, which
`bc3` names `vcc`):

```
bl0_w17085 = NOT( lpstb_b AND res_b )       two pull-downs in series, W 71; load 30/60
bl0_w17210 = NOT bl0_w17085                  = lpstb_b AND res_b; pull-down W 50; load 28/61
```

Both loads are of run 1's build (plate over the output strip, the plate's finger on a buried contact at
the end of an L of diffusion from the strip). `bl0_w17085`'s only load is the inverter: its poly leaves
the buried contact west of the column, turns south at x 7203-7227 and east at y 17160-17180 across the
rail, ending at x 7358. `bl0_w17210` leaves west by a buried contact and a poly onto a pad (7188,17210),
and south on a metal x 7178-7198 to a pad (7188,17300) whose poly row is the gate band of the third unit
of the column (y 17290-17310; not drawn); the metal goes on south of that pad.

`lpstb_b` is high while LPSTB is high and `res_b` is high while RES is high (run 1: `lpstb_nres` =
`lpstb_b` AND NOT `res_b`). So `bl0_w17210` is the light pen strobe gated by "not reset". Believed, not
traced: it is what latches the light pen register; its loads are the next step.

### Piece `u3` (run 3): the third unit, and where `bl0_w17210`'s metal ends

The metal x 7178-7198 that leaves the pad (7188,17210) is one piece down to a pad (7188,17472) and ends
there (`px.py col 7188 17200 17800 10 metal,metal1`: bare ground at y 17540; `px.py row 17322 7160 7215 4`:
both edges of the metal between the pads). A second metal on the same x starts at a pad (7188,17600):
another net. So `bl0_w17210` has two loads by this metal: the poly row of the pad (7188,17300) and the poly
row of the pad (7188,17472).

The first is the gate band of the third unit under the rail, of the same build as the inverter above it:

```
bl0_w17337 = NOT bl0_w17210        = NOT( lpstb_b AND res_b );  pull-down W 46; load 28/56
```

Its output leaves west by a tab and a buried contact onto a poly row y 17334-17353, which passes under
the metal of `bl0_w17210` (a crossing: no ring, no hole in the clean shot;
`textmap.py 7125 17320 7210 17360 3`) to a pad (7144,17340). A thin metal x 7137-7152 starts at that pad
and runs south (`follow.py 7147 17400 S --gap 45`), over the poly row y 17550 with no pad, to a pad
(7143,17647), where it ends; that pad's poly row runs east: a gate band of the fifth unit under the rail.

**The thin metal on the same x north of the pad is not this net** (review round 4; the first drawing
joined them). It comes south from a pad (7144,16474) and turns west at a corner (7144,17305), 35 px
short of the pad, along y 17299-17311 to x 7103 and on south at x 7097-7110
(`px.py row 17305 7090 7160 5 metal,metal1`: metal from x 7100 to 7150; `px.py col 7144 17290 17345 3`
and `px.py row 17321 7120 7170 6 metal,acid1b`: bare ground and open green between the corner and the
pad's ring, y 17314-17326). The pad's own ring had hidden the gap from the follower. That net (north: a
poly column under the wide bus metal, pads (7144,16260) and (7141,15566), a poly row east into `bc1`'s
gate group; south: the reviewer's follower gives corners (7102,17868) and an end (7386,17864)) is not
drawn.

The unit is the only driver drawn on the net; its one load is the poly row of the south pad.

### Piece `u45` (run 4): the fourth and fifth units, a cross-coupled pair

**The pull-downs are wide.** A thin dark line x 7237-7243 from the buried contact at (7250,17435) south to
y 17722, east along y 17722 to x 7420 and north is the edge of a diffusion, not a wire: inside it the
bands between the poly rows are redder than outside (`px.py row 17497 7208 7292 6 acid,metal,acid1b`,
`row 17540`: chip-2 stripped red minus green 13-30 east of the line, about 0 west; `px.py col 7385 17700
17745 3`). The outlined khaki blocks beside the rail are field (`px.py pt 7358,17475`). So every row
that crosses x 7243-7292 has a channel there as well as under the rail.

**Unit 4.** Under the rail (`railprof.py 7295 7340 17200 18400`, `textmap.py 7280 17416 7366 17600 3`):
top node y 17425-17455 with no contact (a mark in chip 1's metal at (7310,17437) is not in chip 2 nor a
hole in the clean shot), band A, a node y 17485-17500 with no contact, band B, and a box with a rail
contact (7322,17560: ring and bright centre in both chips). Bands A and B are one poly: the pad
(7188,17472) of `bl0_w17210`'s metal has its poly running south at x 7185-7205 onto band B's west end with
no edge between (`px.py col 7194 17476 17540 3`); band B does not go further west. Both end at about
x 7327-7338 with field east of them (pink at x 7343-7353). So the top node is pulled to the rail through
two channels in series with the same gate.

East of the rail the top node's strip (y 17425-17452) runs under a load plate to the supply box. The
plate (y 17403-17447), the pad south of it (contact (7432,17470)) and a finger west onto a buried contact
(7372-7410, 17458-17492) are read as one poly: the dark line between plate and pad at y 17444-17450 has no
field colour and is taken as the strip's edge under the poly (`px.py col 7435 17396 17500 3`); the
strip runs straight into the buried contact (`px.py col 7392 17436 17500 3`). The diffusion goes on
south from the buried contact under a poly (7362-7410, 17505-17528; `px.py col 7388 17486 17566 3`) to a
strip y 17537-17553 that is one piece with the box of the rail contact (`px.py row 17545 7340 7412 4`):
a second pull-down on the top node. Its poly is `bl0_w17610`'s (below).

From the pad a thin metal x 7423-7441 runs south over the poly bar and the plate of unit 5 (dark bars
with the metal's edges still there at y 17604, 17645, 17664: `px.py row ... 7412 7452 4 metal,metal1`)
to a pad (7434,17684), where it ends (bare ground from y 17710).

**Unit 5.** The open column x 7243-7292 goes on south from the strip of unit 4's box: the row
`busl_x6906` (y 17549-17572, from the far west, ending at x 7297 with field between its end and the
box), a band of diffusion, a buried contact (7240-7268, 17590-17620) under the east end of a poly from a
pad (7188,17605), band C (the row of `bl0_w17337`'s pad (7143,17647)), a band, band D (`bl0_w17687`, a
row from the west), and the bottom strip. Under the rail the node is y 17603-17628 (field north of it,
y 17587-17597), then C, a node, D and the box of the rail contact (7308,17727). The bottom strip
y 17703-17722 runs from the edge line east under the rail to x 7420.

East of the rail the node goes on at y 17603-17612 (no outline between the rail and x 7374:
`px.py row 17607 7330 7412 4`) into a heavy dark box (7366-7402, 17574-17614), read as the buried
contact of the load plate's finger, and a block of diffusion (7364-7402, 17612-17664; chip-2 stripped red
minus green 14-20: `px.py col 7390 17596 17726 4`). The plate (7406-7462, 17575-17632) is one poly with
a bar x 7410-7438 north to the gate of unit 4's second pull-down; the strip under it (its top edge the
dark line y 17600) ends on the supply box (7468-7522, 17570-17660). South of the block a poly
(7366-7420, 17668-17695), the poly of the pad (7434,17684), lies between the block and the bottom strip:
a third pull-down on the node, gated by `bl0_w17440`.

```
bl0_w17440 = NOT( bl0_w17210 OR bl0_w17610 )                                 load 28/49
bl0_w17610 = NOT( bl0_w17440 OR busl_x6906 OR (bl0_w17337 AND bl0_w17687) )  load 27/56
```

Both firm (`tools/t.sh bl0 unsure.py --equations`). Write s for `bl0_w17210` (LPSTB high and RES high).
While s is high `bl0_w17440` is low, and `bl0_w17610` is high unless `busl_x6906` holds it low. When s
falls the pair holds: `bl0_w17610` stays high until `busl_x6906` is high, or `bl0_w17687` is high (which
counts only while s is low). **So `bl0_w17610` is a flag "a light pen strobe has been seen", set at the
strobe and cleared by one of two lines not yet followed.** What it does (believed: it times the latching
of R16/R17) is not traced: its poly goes to the pad (7188,17605), from which a metal on x 7178-7198
runs south to y 17775 and east to a pad at about (7385,17780).

### Piece `w5` (run 5): the three wires of the pair

`busl_x6906`. The row y 17549-17572 runs west from the fifth unit under four tracks (x 7144, 7103, 7060,
7015; plain crossings) to a pad (6970,17561). The thin metal from that pad goes north, west along y 17086
and north again to a pad (6842,16562) (`follow.py 6972 17530 N`: corners (6969,17086), (6841,17083), end
(6842,16557); no contact candidate; the metal is bright up to each pad's ring, `px.py col 6972 17515
17560 4`, `col 6842 16560 16610 5`). From that pad a poly column runs north under the bus of horizontal
metals (poly colours all the way, `px.py col 6846 16230 16550 8 acid1b,acid`; the dark rings across every
column at y 16330 and 16405 are the gaps between the metals) to a pad (6842,16217), where the track
x 6841 from the north ends (`px.py col 6841 16150 16215 6`). That track is `busl`'s `busl_x6906`, drawn
by `busl` to y 15000; between y 15000 and the pad it crosses `res_b`'s and `lpstb_b`'s poly rows (y 15132,
15176; the follower's candidate (6841,15121) is the edge bar of the first, no ring:
`textmap.py 6822 15104 6862 15140 3`). All four pads are rings with a bright centre in both metal shots.
With `busl` loaded the gate's input is `busl_x6906` (`TRACE=bl0,busl .venv/bin/python tools/netlist.py`).

`bl0_w17687`. Band D's row ends west at x 7128 on a pad (7142,17713); a thin metal runs south from it,
turns east at (7151,17829) and ends on a pad (7424,17822) (`follow.py 7145 17745 S`), whose poly row
(y 17811-17831) goes on east under the supply rail.

`bl0_w17610`. The metal from the pad (7188,17605) runs south, turns east at (7192,17786) and ends on a
pad (7384,17779) (`follow.py 7189 17730 S`); its poly row (y 17768-17790) goes on east under the supply
rail to a pad at about (7553,17775), from which a metal goes on east (seen, not drawn).

## Ports

| Name | Layer | Where | Direction | Note |
|---|---|---|---|---|
| `res_b` | M | (6359-6373, 15000) | in | busl's track x 6366 |
| `lpstb_b` | M | (6401-6415, 15000) | in | busl's track x 6408 |
| `busl_x6906` | M | (6834-6848, 15000) | in | `busl`'s track x 6841, on north |
| `bl0_w17687` | P | (7465, 17811-17831) | in | poly row east of the pad (7424,17822), under the supply rail and on |
| `bl0_w17610` | P | (7465, 17768-17790) | out | poly row east of the pad (7384,17779), under the supply rail to a pad at about (7553,17775) |
| `vss` | M | (7292-7342, 16925) | - | the gate column's rail, on north; it ends at y 17755 |
| `vcc` | M | (7470-7520, 17020), (7470-7520, 17670) | - | `bc3`'s rail x 7495 |
| `bl0_w15088` | P | (6450, 15078-15098) | ? | poly row on east from the pad (6320,15088), seen to x 6790 |
| `bl0_w15088` | P | (5700, 15078-15098) | ? | poly row on west to a pad (4909,15088); a track x 4909 from the north ends there |
| `bl0_w15088` | M | (5750-5764, 15700) | ? | thin metal south from the pad (5755,15088), followed to about (5762,15768) |
| `bl0_w15412` | P | (5600, 15401-15425) | out | poly row west to a pad (4909,15414), track x 4909 south |
| `larr_l0_g0` | D | (2876, 14105-14122) | in | the diffusion wire is one piece with the box of `larr`'s contact (2893,14114) |
| `larr_cin_s7` | P | (2850, 14559-14574) | out | onto `larr`'s poly row y 14566 |
| `bl0_w14308` | P | (2405, 14687-14708) | out | the third pad's row runs on west of the pad (not read) |
| `larr_l0_g1` | D | (2860, 14517-14533) | ? | onto `larr`'s diffusion (2850-2880, 14508-14540) and its contact (2892,14523) |
| `vss` | M | (2605-2655, 14090), (2605-2655, 14770) | - | the left edge column's rail, on both ways |
| `vcc` | M | (2783-2832, 14090), (2783-2832, 14770) | - | the same |
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

Run 2:

9. **A dark C-shaped mark on the wide metal of the bus at (6925,16365)**, over `lpstb_b`'s poly column,
   in the chip-2 shots only (metal: the C; stripped: a dark-red ring about 22 px across). Chip 1's metal shot
   has only a dim patch 12 px south at (6930,16375), and a small reddish ring on `res_b`'s column at
   (6884,16357) where chip 2 is plain. No mark is at the same place in both chips, none has a ring with a
   bright centre, and neither column has a pad under the wide metal (`s3.png`, `review-3/bus4.png`,
   `textmap.py 6860 16330 6950 16400 2 --acid`). Read as blemishes, not contacts. Under the wide metal
   the clean shot shows every column dark and textured, so it does not help there.
10. **A small dark mark on the rail at (7307,17058)**, over the output node of piece `n1`: about 6 px, no
   ring, no bright centre, and the clean shot is uniform there (`textmap.py 7280 16940 7356 17160 3`).
   Read as no contact (a contact to the rail there would short the gate's output to `vss`). The pinkish-white
   blob there in the chip-2 stripped shot reads 226/157/135 against 108-181 red at four real contacts: a
   fringe (review). Chip 1's metal also has a dark spot of about 8 px over the middle node at (7318,17018);
   chip 2 and the clean shot are plain there: no contact.
11. **Which supply the rail x 7292-7342 is.** Not followed to a named supply: `vss` by the orientation of
   the gates (sources on it, loads on the other rail, which `bc3` names `vcc`).

Run 3:

12. **Other drivers of `bl0_w17337`.** The track is drawn end to end with one driver (the third unit), and
   no pad or contact between its ends. Its south end's row is not traced: if it reaches a diffusion as
   well as a gate, the equation gets another term. Assumed none.
13. **The contact of the third unit's supply box.** The box (7468-7522, 17251-17350) is under the supply
   rail and has dark specks in the clean shot at (7488,17278) and (7497,17318) and a dimple in each metal
   shot at about y 17300 (chip 2) and y 17293 (chip 1), but no ring with a bright centre: wide metal
   does not show one (the reviewer could not check it either). The contact is drawn at (7495,17300); where exactly it is does not matter to the
   connection (the box is on `vcc` like the two boxes north of it).

Run 4:

14. **Plate and pad of unit 4 as one poly.** Between the load plate (y 17403-17447) and the pad
   (y 17450-17490) there is a dark line 6-8 px high and no field colour; it is read as the edge of the
   strip under one poly. If they were two polys, `bl0_w17440`'s metal and the gate it drives would hang
   on the buried contact alone (still `bl0_w17440`) and the load's gate would be tied nowhere.
15. **The buried contact of unit 5's load** is a heavy dark box (7366-7402, 17574-17614) in every shot,
   with no readable inside; that the plate's finger and the node's diffusion meet in it is read from its
   place (the node runs into it from the west, the block hangs below it, the plate's poly reaches it
   from the east) and from the build of the other four loads.
16. **Where the diffusion of the wide stacks ends under the rail's east side** (x 7327-7355): read from
   the clean shot only (rows end at x 7327-7338, pink beyond). If the top node reached the box of the
   rail contact east of the rows' ends, the node would be shorted to the rail.

## Review

**Round 1 (full review; Claude Fable 5.2 agent, 2026-11-20; pieces `pin` and `g1` at commit 7c7bc4a).**
Told to suspect: G2's neck and strip, the three buried contacts of the gate group, the pieces of its
diffusion column, the pads; in `g1` a contact on the NOR's output node, the rail's continuity, the
output's joins east and west, the tie, the field islands and the neck, the drain strip's join, the
metal x 2459 through its middle pad, band A's source, taps on the long rows and the track. It looked at
4x or more in two to four shots with profiles and text maps (27 images, `cache/scratch/bl0/review-1/`).

- **Finding 1 (changes a connection; confirmed, fixed).** The row y 14105-14122 was drawn as poly with
  ports at both ends; it is a diffusion wire that ends at x 2515 on a buried contact with band A's poly
  and at its east end is one piece with the box of `larr`'s contact (2893,14114). Checked by the tracer
  (`px.py row 14113 2680 2770 15 metal,metal1,acid,acid1b` against row 14174; the box by profile against
  the output's buried contact; `rvw_junc.png`). Fixed: the row is `D`, a `B` at (2513-2545, 14100-14125),
  the net is `larr_l0_g0` (the wire first named w14113 here), the west port is gone. The NOR's equation is unchanged.
- Found as drawn: every gate, load, tie and buried contact of the gate group; field between G1, G2 and
  G3 under the rail; the five pads and ten crossings; in `g1` no contact on the output node, the rail
  unbroken, the neck, the islands, the drain strip onto `larr`'s contact, the tie, the turn under the
  vcc rail, the track x 2459 through its three pads, the track x 4867 (four rows cross under it, also
  y 15043, none with a contact), no tap at (4185,14436).
- Not checked: every crossing of the two long rows at 4x (about 2x and text); the pad at about
  (5760,15765) where the thin metal x 5757 ends; the rails to named supplies.

Round 1: one finding, fixed.

**Round 2 (fix check of round 1's finding, and full review of the new pieces `s7` and `pe`; a fresh
Claude Fable 5.2 agent, 2026-11-20; commit 5f2676e against 7c7bc4a).** Told to suspect: the box at the
diffusion wire's west end, anything crossing the wire, its join to `larr`'s box; in `s7` the west exit
and its run north, whether the gate band's row is the pad's row, the tie, a contact on the output node;
in `pe` every pad, the spot at (6706,15176), every track crossing, the crossing at (6885,15176), the
tracks as single metals. 16 images (`cache/scratch/bl0/review-2/`), 4x to 6x in three shots, profiles and
text maps.

- Part A, found correct: the box (2516-2540, 14102-14124) is a buried contact of the same signature as
  the one at (2566,14307), with the poly one run up from band A ending in it; the row is diffusion
  (plain in chip 2, green in the clean shot's open stretches, tan under both rails), with no edge across
  it between x 2584 and 2872; a thin metal x 2556-2572 crosses it with no pad and no hole; its edge lines
  flare into the box of `larr`'s contact. Both `sameconn` runs show only the intended differences and `s7`.
- **Finding 1 (geometry only; confirmed, fixed).** `s7`'s output strip was drawn y 14664-14690 along its
  whole length: it is y 14662-14678 from the rail to x 2700 and y 14654-14690 under the plate
  (`bl0_edges.py col 2680 / 2695 / 2725 14640 14705 metal`). As drawn its bottom lay under the gate
  band's east end (pull-down 77 wide; it is 69) and the load was 26 wide (it is 36).
- **Finding 2 (geometry only; confirmed, fixed).** `res_b`'s poly column south of the pad (6882,16170) is
  x 6877-6899, drawn 6872-6892 (`bl0_edges.py row 16215 6855 6905 metal`); `lpstb_b`'s is x 6920-6942.
- Part B, found correct: in `s7` one poly from the box to the row y 14556-14577 and on to `larr`'s row,
  12 px of field between the hook and the gate row, the gate row one poly from x 2396 through the pad to
  x 2660, the metal ending on the pad (2459,14700), no contact on the output node, tie box and vcc
  contact; in `pe` the four pads, both rows ending at their pads with field beyond, ten track crossings
  with identical edge bars and no ring, the spot at (6706,15176) on chip 2 only, the crossing at
  (6885,15176), both tracks single metals with only field under them from y 15200 to 16150.
- Not checked: an undrawn pad (2708,14077) whose metal lies about 3 px north of the diffusion wire (the
  wire's edge line is unbroken beneath it in both metal shots: read as not joined); the poly columns
  south of y 16250; the gate row west of x 2396.

After the fixes: `tools/t.sh bl0 sameconn.py 5f2676e` ends `connections identical`;
`.venv/bin/python tools/sameconn.py 5f2676e` ends `connections identical`.

Round 2: no findings that change a connection.

### Run 2

Round 3 (full review of pieces `xu`, `n1`, `n2`; fresh Fable 5.2 reviewer; 2026-11-20 06:47 -0600; commit 71168d2; images
`cache/scratch/bl0/review-3/`). Told to suspect: series pair or NOR (which diffusion pieces of the column
have a contact; the mark at (7307,17058)); the gap y 17092-17110; the "U" of dark line east of the column;
the necks and finger ties; the tabs west of the column; the C mark at (6925,16365); undrawn branches or
gates along rows and columns; the output poly's branches; the metal from the pad (7188,17210). Checked at
4x or more with text maps and profiles: the two contacts (ring with bright centre in both metal shots),
no contact on the output node or the middle node, both gaps to the next unit (two edge lines in all four
shots), the U as one outline (chip-2 stripped red minus green: strip +22 to +29, neck +23, inside the U
-5 to -12), both necks and tabs as diffusion, both lines pad to pad with no contact candidate
(`follow.py`), the rows continuous to their rounded ends at x 7383 on field, one poly with no branch for
`bl0_w17085`, the metal from the pad going south only. Could not check: the plate fingers against the
box interiors (outline only), which supply each rail is, holes under the wide bus metal in the clean shot.

Findings, all geometry or comment only:

1. Ambiguity 9's "chip-2 metal shot only" was incomplete (marks in the chip-2 stripped shot and, elsewhere,
   in chip 1). Confirmed; the ambiguity is reworded. No contact.
2. A dark spot in chip 1's metal over `n1`'s middle node (7318,17018). Confirmed; added to Ambiguity 10.
3. `n2`'s output poly between pad and buried contact is y 17203-17223 (drawn 17198-17224). Fixed.
4. `n2`'s supply box ends at about y 17243 (drawn 17235). Fixed.

`tools/t.sh bl0 sameconn.py 71168d2`: connections identical. `.venv/bin/python tools/sameconn.py 71168d2`:
connections identical.

Round 3: no findings that change a connection.

### Run 3

Round 4 (full review of piece `u3`; fresh Fable 5.2 reviewer; 2026-11-20 10:13 -0600; commit 3be37d6; images
`cache/scratch/bl0/review-4/`). Told to suspect: the crossing at (7188,17340); the continuity and the end of
`bl0_w17210`'s metal; the four pads of the long track and the poly column under the bus; pads or contacts
the trace lacks; other connections of the output node; the neck, buried contact and finger of the load and
the supply box's contact; the unit's separation from its neighbours. Checked at 3-4x with profiles, text
maps and the followers: the metal of `bl0_w17210` continuous between its pads and ending on the second;
the crossing plain; the source contact, the single band, the output node without a rail contact, the
neck, buried contact and finger, the tab and buried contact west; the unit separate from `n2`; the pads
real; the crossings plain; no second poly on any pad. Could not check: the supply box's contact (specks,
no ring under wide metal).

Findings:

1. **Changes a connection.** The thin metal from the north does not reach the pad (7144,17340): it
   turns west at (7144,17305) and goes on south at x 7097-7110; bare ground between the corner and the
   pad. Confirmed (`px.py row 17305 7090 7160 5 metal,metal1`, `px.py col 7144 17290 17345 3`,
   `px.py row 17321 7120 7170 6 metal,acid1b`). Fixed: the north stretch (three pads, the poly column,
   the port into `bc1`) is taken out of the piece; `bl0_w17337` is the poly row, the pad, the metal south
   and the pad (7143,17647). The equation is unchanged; a port is gone.
2. Geometry: the load plate runs south to about y 17362 (drawn 17348) and the strip under it to 17350.
   Confirmed (`px.py col 7435 17340 17384 3`); fixed.
3. Geometry: the output poly row's edges are y 17334-17353 (drawn 17328-17348). Confirmed
   (`px.py col 7218 17318 17366 3`); fixed.
4. Comment: no edge parts the supply box from `n2`'s at x 7510. Both are `vcc`; left as drawn.

Round 4: one finding that changes a connection, fixed; three geometry or comment findings.

Round 5 (fix check of round 4's fixes; fresh Fable 5.2 reviewer; 2026-11-20 10:16 -0600; against commit 3be37d6; images
`cache/scratch/bl0/review-5/`). Checked at 4x with profiles in both metal shots and the clean shot: the
metal from the north ends at the corner (metal to y 17308, bare ground y 17317-17323, the pad's ring from
17326) and passes the pad without touching its ring; bare ground west of the pad (x 7112-7136); only the
poly row to the east; one continuous metal south from y 17370 to 17622 with a plain crossing of the poly
row y 17548-17570 (no hole, no widening); the metal ends on the pad (7143,17647), whose poly row east is
y 17638-17656; the plate to about y 17362 and the diffusion edge under it at 17348-17350; the output
row's edges. `tools/t.sh bl0 sameconn.py 3be37d6` and `.venv/bin/python tools/sameconn.py 3be37d6`: every
difference intended (none in names, transistors or equations; the port into `bc1` is gone).

Round 5: no findings.

### Run 4

Round 6 (full review of piece `u45`; fresh Fable 5.2 reviewer; 2026-11-20 10:36 -0600; commit f194b8a; images
`cache/scratch/bl0/review-6/`). Told to suspect: the thin line as a diffusion edge and the diffusion of the
open column all the way down; bands A and B as one poly and band B's ends; the east ends of the four
bands; plate and pad of unit 4 as one poly and its buried contact; the second pull-down's diffusion and
the bar's two joins; unit 5's buried contact, the node's passage into it, the block and the strip; the
thin metal from pad to pad and the transistor under its pad's poly; the rail contacts and their absence
on the four nodes; anything left out. Checked with profiles, text maps and `railprof.py`, 10 views: the
line as a real edge across all five rows in both metal shots, diffusion east of it; A and B continuous
salmon at x 7191; the diffusion edge crossing each band with the poly overhanging and field beyond;
plate and pad parted by a single line like the strip's top edge; pad and bar apart (20 px of field);
single edge lines where each diffusion enters under its plate and on both sides of the two cross-coupling
gates; the thin metal with dark bars of 10 px or less and holes only at its two pads; both rail contacts
real, none on the four nodes; the poly cap closed. Could not check: the diffusion across the rail's west
edge line (dark in every shot), the insides of the two buried contacts, the strip to the contact box at
x 7352-7366 (a line in each chip at a different x), the supply boxes' contacts beyond 3.4x.

Findings, all geometry only:

1. The open column's east edge under the row `busl_x6906` is x 7278, not 7292 (a field pocket x 7278-7305
   at y 17546-17599): the pull-down is about 35 wide. Confirmed (`px.py row 17560 7262 7300 3
   metal,metal1`: an edge line at x 7276-7279 across the poly); fixed.
2. Bands C and D lie 6-8 px further north under the rail than west of it. Fixed (each drawn in two parts).
3. Unit 5's load plate runs on south of the strip to y 17646 and ends on field. Fixed.
4. The bar is x 7416-7435 and the thin metal about x 7424-7447. Fixed.

`tools/t.sh bl0 sameconn.py f194b8a`: connections identical. `.venv/bin/python tools/sameconn.py f194b8a`:
connections identical.

Round 6: no findings that change a connection.

## Not done

- **What pulls `larr_l0_g0` and `larr_l0_g1` up** (neither pull-up is in `larr`'s rows or in the two
  cells drawn here), and the carry into s0.
- **`bl0_w17687`'s source**: the poly row east of the pad (7424,17822) (y 17811-17831; salmon to x 7620
  at least, a metal over it from about x 7545).
- **Where `bl0_w17610` goes**: the poly row east of the pad (7384,17779) to a pad at about (7553,17775)
  and the metal east of it.
- `busl_x6906`'s source is `busl`'s (north of y 10400).
- **The thin metal x 7137-7152 north of the pad (7144,17340)**, another net, seen and not drawn: from a pad
  (7141,15566) (poly row east into `bc1`'s group x 7190-7860, y 15570-16300) south to a pad (7144,16260),
  a poly column under the wide bus metal to a pad (7144,16474), metal south to a corner (7144,17305),
  west to x 7103 and on south at x 7097-7110 (follower: a corner (7102,17868), east to (7386,17864)).
  All four pads are real contacts and the column is over field (review round 4).
- The column north of piece `n1` has a band at y 16866-16884 (`railprof.py 7295 7340 16860 17400`), not
  drawn. All of this lies in `bc3`'s region.
- `bl0_w14308`'s row west of x 2396 (it runs on west of the pad (2459,14700)); the pad (2708,14077) just
  north of the diffusion wire of `larr_l0_g0` (read as not joined to it; its land is not read).
- In the two left-column cells, seen and not drawn: a poly row y 14165-14182 from a pad (2567,14177) (a
  metal from the north, x 2555-2577) east under both rails with no transistor under the vss rail; a
  track x 2493-2512 over `bl0_w14308`'s row; the wide metal west of x 2440; a poly row y 14770-14790
  from the west to a pad (2700,14785), from which a thin metal x 2688-2712 runs south between the rails.
- `bl0_w15412` west of x 5600 (surveyed, `survey.md`): the row to a pad (4909,15414), a track x 4909
  south to a corner at y 16088 and a pad (4866,16088), a poly row west across the left array's Gap 2 to
  x 2850, north and west to a pad (2700,15995) on that thin metal x 2688-2712. Its loads are not found.
- `bl0_w15088`: its west row to the pad (4909,15088) and the track x 4909 north (follower: to
  (4908,10660), contact candidates (4908,11984), (4908,10699)); its thin metal south of y 15700 (a pad
  at about (5760,15765)); its poly row east of x 6450 (seen past x 7000).
- Both rails of the gate group south of y 15800; the rest of the master-list row's region (the bus
  wiring x 4780-5850, the tracks x 6452-6841, the gate group south of y 15800).

## Corrections (coordinator, from the handoffs of 2026-11-20)

- G1's input ("a track x 4909 from the north reaches the west row's end; source not traced"; Not done, "its west row to the pad (4909,15088) and the track x 4909 north"): traced by `busl` run 9 (piece `p2`; firm). **The line is `rst_n`**, from `lc3`'s port (5475,10400) by a poly row y 10663, a pad (4907,10663) and the track x 4909, 4,400 px south without pad or contact. So `bl0_w15412` = NOT `rst_n`, a fourth copy of the reset in `rst`'s sense (high while RES and LPSTB are both low). The pad's contact is at (4909,15087); the track ends there (bare ground to y 15409, where `bl0_w15412`'s track begins on the same position). The port `P 5700,15078-15098` is met; `busl` drew the last 88 px of the track, the pad and the row from the pad to x 5700 inside this package's region. The label of G1's input is renamed at the next refresh.
- Seven more tracks arrive from `busl` at y 15000 and are not followed: the six through lines `lc3_e9577`..`lc3_e9793` (x 5322, 5279, 5235, 5192, 5148, 5105; the follower's ends (5326,15381), (5284,15859), (5239,16506), (5194,16981), (5151,17462), (5107,17938)) and `lc2_w8450`'s second branch (x 4822; follower: to (4823,16690)). A metal jog on the row y 15088 at x 5400-5500 is another net's track (x 5495 north, x 5410 south), not followed.
