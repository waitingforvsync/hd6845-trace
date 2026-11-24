# bl0: the gate group that the buffered RES and LPSTB pins reach

Lead group (user, 2026-11-20): **what the chip does while RES is low and LPSTB is high**. The gate
group lies between the left bus field and the bottom-left logic (x 5850-6330, y 15200-15800); its wires
are followed from there. Geometry: `trace/bl0.txt`. Ports: `ports.d/bl0.txt`. Coordinates are
metal-shot pixels. Evidence: `cache/scratch/bl0/` (`survey.md` holds every measurement with its command).

## Status

Run 12 (richtw1's session, Claude Fable 5.2; 2026-11-20 22:38 +0100). Two pieces of wiring, no transistor, no
uncertain item, seven new nets; reviewed (round 14: no findings): what the master list's row left in this package.

- **Piece `t6`** (wiring, 15,700 px). "The metal of another net on `rst_n`'s row" is the first of **six
  tracks** that cross y 15000 east of `cdp4_bus_s0`'s (x 5496, 5540, 5584, 5627, 5671, 5714; north of
  y 15000 they are in `busl`'s region and drawn by no one). The bundle steps west as nested L's, by 88 px
  round `cdp4_bus_s0`'s end and by 44 px below each of `lc3`'s through lines as it ends, and its lines
  end one by one, from the east, on a pad whose poly row runs west under the tracks into the left array:
  `cdp3_g_c7`, `cdp3_g_c6`, `cdp3_g_c5`, `cdp3_g_c4`, `cdp3_g_c3`, `cdp3_g_c2`, named by the y of
  the row. **Each of the left array's six lower rows so gets one poly row, 150 px south of the diffusion
  wire of its `lc3` line.** No pad, contact or branch on any of them between y 15000 and its end.
  Believed, not traced: they are `cdp3_g_c7`..`cdp3_g_c2` (the follower runs each track north to an end at
  the y of one of `bc1`'s six poly lines; `busl`'s region).
- **Piece `m7144`** (wiring, 4,400 px). The thin metal x 7137-7152 north of `bl0_w17337`'s pad is one
  wire, `bl0_w15566`, from a pad (7143,15566) whose poly row goes east into `bc1`'s gate group, under the
  wide bus metal as a poly column (pads (7143,16259), (7143,16474)), south, west and south inside the L
  of the clock's metal to a pad (7384,17866), by a poly row under the supply rail to a pad (7602,17866),
  by a metal east, 44 px north on another net's poly column (no contact) and east to a pad (8272,17821),
  whose poly row runs on east (seen as far as x 8690). No transistor, no branch.
- "The south row of `bl0_w17337`" of the master list's row is band C of the fifth unit, drawn in run 4
  (y 17636-17656, ending under the rail at x 7350): nothing was left of it.

Run 11 (Matt Godbolt's session, Claude Fable 5.2; 2026-11-20 12:06 -0600). One piece of wiring, no transistor, no
uncertain item; reviewed (round 13: no findings): the last two tracks from the left bus field.

- **Piece `w11`** (wiring, 2,500 px). `cdp4_bus_s0` (track x 5451): 45 px south of y 15000 it turns west
  onto a pad (5364,15044), whose poly row y 15033-15053 runs west under the tracks into the left array
  (port at x 4780). `lc2_w8450`'s second branch (track x 4822): south to a pad (4823,16713), whose poly
  row y 16703-16723 goes east into the bottom-left logic (port at x 4930).
- With this every track that `busl` hands over at y 15000 west of x 7000 is drawn to where it leaves
  this package's reach.

Run 10 (Matt Godbolt's session, Claude Fable 5.2; 2026-11-20 11:54 -0600). One piece of wiring, no transistor, no
uncertain item; reviewed (round 12: no findings): the other five through lines of `lc3`.

- **Piece `w10`** (wiring, 9,500 px). `cdp3_cw_c6`, `cdp3_cw_c5`, `cdp3_cw_c4`, `cdp3_cw_c3`, `cdp3_cw_c2` (tracks
  x 5279, 5235, 5192, 5148, 5105) each run on south from y 15000 to a contact on a diffusion box, at
  (5299,15849), (5252,16496), (5211,16975), (5170,17453), (5126,17929), and from each box a diffusion wire
  runs west under the tracks into the left array, like `cdp3_cw_c7`'s (run 9). **So the six lines enter
  the left array as six diffusion wires about 478 px apart, at y 15372, 15849, 16501, 16978, 17454,
  17931**: one per row of its lower part (believed; the array's side is `larr`'s).

Run 9 (Matt Godbolt's session, Claude Fable 5.2; 2026-11-20 11:40 -0600). One piece of wiring, no transistor, no
uncertain item; reviewed (round 11: no findings): three tracks of the left bus field followed on south of y 15000.

- **Piece `w9`** (wiring, 5,200 px).
  - `busl_x6820` (track x 6754): to a pad (6754,16217), under the bus of horizontal metals as a poly column
    to a pad (6754,16562), on south as a thin metal (drawn to y 17000; the follower runs it to a corner
    (6767,18040) and east past (7417,18035)).
  - `rcs_mv` (track x 6971): through a pad (6966,15305) whose poly row goes east (port), to a pad
    (6970,16175), a poly column under the bus to a pad (6970,16519), a thin metal to a pad (6968,16780)
    whose poly row goes east (port).
  - `cdp3_cw_c7` (track x 5322): to a contact (5345,15371) on a diffusion box, from which **a diffusion
    wire** y 15362-15382 runs west under the tracks and on past x 4780 into the left array (port).

Run 8 (Matt Godbolt's session, Claude Fable 5.2; 2026-11-20 11:28 -0600). One piece of wiring, no transistor, no
uncertain item; reviewed (round 10: no findings): the two other ends of `rst_n`'s line (the wire `bl0` called w15088).

- **Piece `w8`** (wiring, 1,000 px). East: the poly row y 15078-15098 runs on from the pad (6320,15088)
  under the tracks to x 7280 and on under `bc1`'s rail x 7292-7342, where it is salmon across the rail and
  ends at about x 7350: a gate of `bc1`'s undrawn column (port). South: the thin metal from the pad
  (5755,15088) ends on a pad (5737,15759), and a poly column goes on south from it under the horizontal
  metals at y 15800 and 15850 into the bottom-left logic (port).
- The thin metal x 2690-2710 of `bl0_w15412` (run 7) was looked at again at 6.5x in four shots: it runs
  over a diffusion strip of its own width at y 15845-15895 and is at the photos' limit there. It is part
  of the left column's cells (`larr`'s open work) and is left to that package.

Run 7 (Matt Godbolt's session, Claude Fable 5.2; 2026-11-20 11:16 -0600). One piece of wiring, no transistor, no
uncertain item; reviewed (round 9: no findings): `bl0_w15412` (the fourth copy of the reset) to the left array's left column.

- **Piece `w7`** (wiring, 3,600 px). `bl0_w15412` = NOT `rst_n` runs west on its poly row to a pad
  (4909,15415), south on a track to a pad (4868,16086), west as a poly row across the whole left array in
  its Gap 2, north and west to a pad (2700,15999) on a thin metal x 2690-2710 between the left
  column's rails. **Believed, not traced**: that thin metal is the force line of the MA output cells
  (`mal`'s `mal_frc_m#` pads; a metal tab from it to the pad of `mal_frc_m9` at (2728,15583) is seen), so
  reset forces the MA outputs through this copy. The thin metal itself is not drawn: it is narrow, dim
  in places, and must be read stretch by stretch (Not done).

Run 6 (Matt Godbolt's session, Claude Fable 5.2; 2026-11-20 10:59 -0600). One piece of wiring, no transistor, no
uncertain item; reviewed (round 8: no finding that changes a connection): the flag's output and its second clearing line to the gate groups they belong to.

- **Piece `w6`** (wiring, 3,600 px). **`bl0_w17610`** (the flag): poly row east under the supply rail to a pad
  (7555,17778), metal east to a pad (7795,17778), poly to a pad (7880,17777), a track north to a pad
  (7882,17389) and a poly row west into the gate column east of the supply rail (`bc3`'s region, not
  drawn by anyone). **`bl0_w17687`** (clears the flag once the strobe is low): its poly row runs east to
  a pad (7925,17821), a track runs north 2,125 px to a pad (7925,15696), and a poly row goes west into
  `bc1`'s gate group at about (7745,15690) (not drawn by anyone). Both ends are gates or outputs of
  other packages' undrawn groups: ports.

Run 5 (Matt Godbolt's session, Claude Fable 5.2; 2026-11-20 10:41 -0600). One piece of wiring, no transistor,
no uncertain item; reviewed (round 7: no finding that changes a connection): the three wires of the cross-coupled pair.

- **Piece `w5`** (wiring, 4,400 px). **The line that clears the pair is `rst`**, a track of the left
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
  bl0_w17610 = NOT( bl0_w17440 OR rst OR (bl0_w17337 AND bl0_w17687) )
  ```

  With `bl0_w17337` = NOT `bl0_w17210`: **a latch that the gated light pen strobe sets** (`bl0_w17210`
  high makes `bl0_w17440` low and, if `rst` is low, `bl0_w17610` high; it stays so after the
  strobe ends) and that is cleared by `rst`, or by `bl0_w17687` once the strobe is low again.
  `rst` and `bl0_w17687` are poly rows from the west, not followed. `bl0_w17610` leaves on a
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
  `res_b`), `lc1`) does not reset. A third gate on the same rail, `bl0_w15412` = NOT `rst_n`, inverts
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
| `rst_n` | 5700-6450 | 15075-15380 | metal y 15080-15100 between pads (5755,15088) and (6320,15088); middle pad (5932,15088) with a poly column south to G1 |
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
| the fifth unit | 7172-7522 | 17528-17755 | open column x 7243-7292: row `rst` y 17549-17572 (from the strip of the fourth unit's box down to the node), buried contact (7240-7268, 17590-17620) with the poly of the pad (7188,17605), band C y 17636-17656 (`bl0_w17337`), band D y 17676-17698 (`bl0_w17687`), both also under the rail; box of the rail contact (7308,17727) and a strip y 17703-17722 east to x 7420; east of the rail the node's block (7364-7402, 17612-17664), buried contact (7366-7402, 17574-17614) under the finger of the load plate (7406-7462, 17575-17632), supply box (7468-7522, 17570-17660), and the pull-down gated by `bl0_w17440` (poly 7366-7420, 17668-17695; pad (7434,17684) of the thin metal x 7423-7441 from the pad (7432,17470)) |
| `rst` south of the bus field | 6826-7215 | 15000-17578 | track x 6834-6848 from y 15000 to a pad (6842,16217); poly column x 6836-6854 under the bus to a pad (6842,16562); thin metal south to y 17085, east to x 6970, south to a pad (6970,17561); poly row y 17549-17572 east under four tracks to the fifth unit |
| `bl0_w17687`'s wire | 7126-7465 | 17676-17838 | the row's west end on a pad (7142,17713); thin metal x 7137-7151 south to a corner (7151,17829), east to a pad (7424,17822); poly row east |
| `bl0_w17610`'s wire | 7178-7465 | 17595-17795 | from the pad (7188,17605) a metal south to a corner (7192,17786), east to a pad (7384,17779); poly row east |
| `bl0_w17610` east and north | 7384-7899 | 17373-17795 | poly row y 17768-17790 to a pad (7555,17778); metal y 17771-17785 to a pad (7795,17778); poly to a pad (7880,17777); track x 7875-7889 north to a pad (7882,17389); poly row y 17378-17398 west |
| `bl0_w17687` east and north | 7424-7942 | 15680-17838 | poly row y 17811-17831 east to a pad (7925,17821); track x 7918-7932 north to a pad (7925,15696); poly row y 15682-15702 west |
| `bl0_w15412` to the left column | 2684-5600 | 15398-16103 | poly row y 15401-15425 west to a pad (4909,15415); track x 4902-4916 south, corner y 16087, pad (4868,16086); poly row y 16075-16097 west to x 2845; column x 2845-2867 north; row y 15988-16008 west under the supply rail to a pad (2700,15999) on the thin metal x 2690-2710 |
| `busl_x6820` south | 6738-6771 | 15000-17000 | track x 6747-6761 to a pad (6754,16217); poly column to a pad (6754,16562); thin metal on south |
| `rcs_mv` south | 6950-7040 | 15000-16797 | track x 6964-6978 through a pad (6966,15305) (poly row y 15291-15311 east) to a pad (6970,16175); poly column to a pad (6970,16519); thin metal to a pad (6968,16780) (poly row y 16770-16790 east) |
| `cdp3_cw_c7` south | 4780-5370 | 15000-15392 | track x 5315-5329 to a contact (5345,15371) on a diffusion box (5325-5370, 15350-15392); diffusion wire y 15362-15382 west |
| the other five through lines | 4780-5324 | 15000-17950 | tracks x 5279, 5235, 5192, 5148, 5105 to contacts (5299,15849), (5252,16496), (5211,16975), (5170,17453), (5126,17929) on diffusion boxes; diffusion wires west at y 15841-15856, 16493-16508, 16970-16985, 17447-17461, 17924-17938 |
| `cdp4_bus_s0` south | 4780-5459 | 15000-15060 | track x 5443-5459 to y 15045, west to a pad (5364,15044); poly row y 15033-15053 west |
| `lc2_w8450`, second branch | 4806-4930 | 15000-16730 | track x 4815-4829 to a pad (4823,16713); poly row y 16703-16723 east |
| six lines to the left array's lower rows | 4780-5721 | 15000-18097 | thin metals from y 15000 at x 5496, 5540, 5584, 5627, 5671, 5714, stepping west as nested L's (arms at y 15090-15308, 15438-15568, 15915-16046, 16565-16652, 17043-17086, 17521); end pads (5626,15522), (5538,15999), (5453,16649), (5322,17127), (5236,17603), (5106,18081); poly rows west at y 15522, 15999, 16649, 17126, 17603, 18081 |
| `bl0_w15566` | 7103-8360 | 15550-17883 | pad (7143,15566) with a poly row east; thin metal x 7137-7151 to a pad (7143,16259); poly column to a pad (7143,16474); thin metal south, corner y 17305, x 7103 south, corner y 17866, east to a pad (7384,17866); poly row y 17855-17875 under the supply rail to a pad (7602,17866); metal east, corner x 7970, north to y 17824, east to a pad (8272,17821); poly row east |

## Logic

Traced (extraction, `tools/t.sh bl0 netlist.py`: 8 nets, 7 transistors, 0 errors, 0 warnings):

```
bl0_w15412  = NOT rst_n
bl0_lpstb_n = NOT lpstb_b
lpstb_nres  = NOR(bl0_lpstb_n, res_b)          = lpstb_b AND NOT res_b
```

| Transistor | W/L | Gate | Between |
|---|---|---|---|
| G1 pull-down | 133/23 | `rst_n` | `vss`, `bl0_w15412` |
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
- The poly column of `rst_n` ends in G1's band and is not on the row below it:
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
`rst` (y 17549-17572, from the far west, ending at x 7297 with field between its end and the
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
bl0_w17610 = NOT( bl0_w17440 OR rst OR (bl0_w17337 AND bl0_w17687) )  load 27/56
```

Both firm (`tools/t.sh bl0 unsure.py --equations`). Write s for `bl0_w17210` (LPSTB high and RES high).
While s is high `bl0_w17440` is low, and `bl0_w17610` is high unless `rst` holds it low. When s
falls the pair holds: `bl0_w17610` stays high until `rst` is high, or `bl0_w17687` is high (which
counts only while s is low). **So `bl0_w17610` is a flag "a light pen strobe has been seen", set at the
strobe and cleared by one of two lines not yet followed.** What it does (believed: it times the latching
of R16/R17) is not traced: its poly goes to the pad (7188,17605), from which a metal on x 7178-7198
runs south to y 17775 and east to a pad at about (7385,17780).

### Piece `w5` (run 5): the three wires of the pair

`rst`. The row y 17549-17572 runs west from the fifth unit under four tracks (x 7144, 7103, 7060,
7015; plain crossings) to a pad (6970,17561). The thin metal from that pad goes north, west along y 17086
and north again to a pad (6842,16562) (`follow.py 6972 17530 N`: corners (6969,17086), (6841,17083), end
(6842,16557); no contact candidate; the metal is bright up to each pad's ring, `px.py col 6972 17515
17560 4`, `col 6842 16560 16610 5`). From that pad a poly column runs north under the bus of horizontal
metals (poly colours all the way, `px.py col 6846 16230 16550 8 acid1b,acid`; the dark rings across every
column at y 16330 and 16405 are the gaps between the metals) to a pad (6842,16217), where the track
x 6841 from the north ends (`px.py col 6841 16150 16215 6`). That track is `busl`'s `rst`, drawn
by `busl` to y 15000; between y 15000 and the pad it crosses three poly rows, `rst_n`'s (y 15078-15098; a dark speck
at (6842,15088) in chip 2 only, a blemish), `res_b`'s and `lpstb_b`'s (y 15132,
15176; the follower's candidate (6841,15121) is the edge bar of the first, no ring:
`textmap.py 6822 15104 6862 15140 3`). All four pads are rings with a bright centre in both metal shots.
With `busl` loaded the gate's input is `rst` (`TRACE=bl0,busl .venv/bin/python tools/netlist.py`).

`bl0_w17687`. Band D's row ends west at about x 7139 on a pad (7142,17713); a thin metal runs south from it,
turns east at (7151,17829) and ends on a pad (7424,17822) (`follow.py 7145 17745 S`), whose poly row
(y 17811-17831) goes on east under the supply rail.

`bl0_w17610`. The metal from the pad (7188,17605) runs south, turns east at (7192,17786) and ends on a
pad (7384,17779) (`follow.py 7189 17730 S`); its poly row (y 17768-17790) goes on east under the supply
rail to a pad at about (7553,17775), from which a metal goes on east (seen, not drawn).

### Piece `w6` (run 6): the flag's output and its second clearing line

`bl0_w17610`. The poly row of the pad (7384,17779) runs east under the supply rail to a pad (7555,17778);
a metal runs east to a pad (7795,17778); a poly goes on east, under the track x 7840 (no contact), to a
pad (7880,17777); a track x 7875-7889 runs north (`follow.py 7882 17740 N`: end (7880,17384); the
candidates (7883,17729) and (7882,17452) have no ring: `textmap.py 7868 17717 7898 17741 3`,
`7868 17440 7898 17464 3`) to a pad (7882,17389), whose poly row goes west under two tracks towards the
gate column east of the supply rail (x 7520-7780). Not followed: that column is `bc3`'s and undrawn.

`bl0_w17687`. The poly row of the pad (7424,17822) runs east to a pad (7925,17821). Between x 7545 and
7845 a metal of another net lies along it (it comes down the track x 7840 and leaves south at x 7555);
the row has no pad under it and the clean shot is one salmon row. From the pad a track x 7918-7932 runs
north (`follow.py 7925 17780 N`: end (7923,15694); five candidates, none with a ring in chip 2) to a pad
(7925,15696), whose poly row goes west under `bc1`'s tracks `bc1_ld_in2` and `bc1_ld_in1` into `bc1`'s
gate group at about (7745,15690). Not followed: that group is `bc1`'s and undrawn.

All six pads are rings with a bright centre in both metal shots and a hole in the clean shot (the pad
(7880,17777)'s centre is weak and small in chip 2: 169/148/79 against 217/207/122 in chip 1; ring in both,
hole in the clean shot), and the
metal is bright up to the ring on the side it arrives from (`px.py` rows and columns at each).

### Piece `w7` (run 7): `bl0_w15412` to the left column

The poly row of G1's output is one poly from the buried contact to a pad (4909,15415) (a scan of the
clean shot along y 15408 and 15413, x 4925-5610, finds no stretch of 6 px without poly colour). From the
pad a track x 4902-4916 runs south (`follow.py 4909 15440 S`: end (4905,16094); the one candidate,
(4913,15856), is a 6 px edge bar with no ring) to a corner at y 16087 and west onto a pad (4868,16086);
both pads are rings with a bright centre in both metal shots and a hole in the clean shot
(`textmap.py 4891 15397 4927 15431 3`, `4848 16068 4886 16104 3`). The pad's poly row runs west along
y 16075-16097 across the left array in its Gap 2: the same scan along y 16080 and 16086 from x 2848 to
4860 finds only two 6 px bars (x 2911, 4756: under tracks). With every package loaded the row makes no
transistor (`tools/netlist.py`: the count is unchanged) and touches nothing drawn. At x 2845-2867 it
turns north (`px.py col 2855 15985 16100 8`) and at y 15988-16008 west, under the left column's supply
rail x 2783-2832 (salmon under the rail, field above and below), to a pad (2700,15999).

That pad is on a thin metal x 2690-2710 which goes on both ways (bright up to the ring north and south:
`px.py col 2700 15966 16030 4 metal,metal1`). **Not drawn beyond the pad.** What is seen of it: it runs
past the pads that `mal` drew as `mal_frc_m#` (the gate tabs of the MA cells' force pull-downs), and at
y 15575-15581 a metal tab joins it to the pad of `mal_frc_m9` (2728,15583) (`textmap.py 2684 15548 2750
15604 3`: metal levels from x 2690 to 2738 in both chips). North it is followed to a pad (2700,14785)
(`follow.py 2700 15960 N`), south to at least y 16150. But it is only about 8 px wide in places, the
two-chip metal test fails on long stretches of it (`tl5_tracks.py v 2697 14700 18700`), a stretch
y 15852-15900 reads at bare-ground level in chip 2, and at y 15392-15470 it is dim and 6 px west. So
whether `bl0_w15412` reaches `mal_frc_m9` by one metal is not established.

### Piece `w8` (run 8): the other ends of `rst_n`'s line

East of the pad (6320,15088) the poly row y 15078-15098 runs on under the track bundle and the tracks
beyond it (a scan of the clean shot along y 15088 finds only short bars at the tracks; views `r8c.png`,
`r8d.png`), in the open at x 6850-7280, and under the rail x 7292-7342 of the bottom-centre logic, where
it is salmon across the whole rail and ends at about x 7350 (`px.py row 15088 7270 7372 6`). Under a
rail of that gate column a poly row is a gate band: `rst_n` gates a pull-down of `bc1`'s column at
y 15088. Drawn to x 7280.

South, the thin metal x 5750-5764 from the pad (5755,15088) runs 670 px (`follow.py 5757 15600 S` and
`N`: ends (5762,15768) and (5757,15088), no candidate) to a pad (5737,15759) that lies under its west
edge (ring and bright centre in both chips, a hole in the clean shot: `textmap.py 5716 15738 5772 15780
3`). A poly column x 5725-5745 goes on south from the pad under the two horizontal metals at y 15800 and
15850 (view `r8e.png`). Drawn to y 15800, the foot of this package's region.

### Piece `w9` (run 9): three tracks of the left bus field

`busl_x6820`. `busl`'s track x 6754 runs on from y 15000 (`follow.py 6754 15010 S`: end (6754,16220);
candidates (6755,15140) and (6755,15174) are the edges of `res_b`'s and `lpstb_b`'s rows, like those on
`rst`) to a pad (6754,16217), a poly column under the bus to a pad (6754,16562) (both rings with
a bright centre in both chips: `textmap.py 6736 16196 6774 16236 3`, `6736 16546 6774 16580 3`), and a
thin metal south (`follow.py 6754 16610 S`: a corner (6767,18040), east to (7417,18035), where the
metal goes on; candidates (6755,16627), (6755,16846), (6756,17352), (6967,18038) not read). Drawn to
y 17000, the foot of this package's region.

`rcs_mv`. `busl`'s track x 6971 passes through a pad (6966,15305) (metal bright up to the ring north and
south: `px.py col 6970 15276 15334 4`), whose poly row y 15291-15311 goes east, and runs on
(`follow.py 6971 15010 S`: end (6970,16178); its candidate (6971,15098) is `rst_n`'s row) to a pad
(6970,16175), a poly column under the bus to a pad (6970,16519), and a thin metal to a pad (6968,16780)
(`follow.py 6971 16560 S`), whose poly row y 16770-16790 goes east under the tracks x 7015, 7055 and on.
Four pads, each a ring with a centre (the pad (6970,16175)'s centre is weak in chip 2, strong in chip 1).

`cdp3_cw_c7`. `busl`'s track x 5322 ends on a large pad at (5345,15371) (`follow.py 5322 15010 S`). The
pad is on diffusion, not poly: the clean shot under it is tan with specks (red minus green 15-29 against
33-41 on this package's poly pads; `px.py pt 5330,15380 5362,15360 6982,17556 4878,16094`), and the strip
that leaves it west is tan too (red minus green about 10). The strip, y 15362-15382 between two edge
lines, runs west under the tracks without a break to x 4700 at least (edges at y 15359-15362 and
15380-15384 at every sample, 24 px apart; where no track covers it, x 5040-5085, it is khaki with
chip-2 stripped red minus green 9-19 and no poly colour: `px.py row 15371 5020 5100 5`). So the line
goes on as a diffusion wire into the left array. Between the box and `bl0_w15412`'s row 14 px south
there is field: no transistor.

### Piece `w10` (run 10): the other five through lines

`follow.py X 15010 S` for x 5279, 5235, 5192, 5148, 5105 ends at (5282,15858), (5239,16506),
(5196,16982), (5151,17462), (5107,17938). Each end is the same build as `cdp3_cw_c7`'s: the track merges
into the west side of a pad whose bright centre lies about 20 px east of the track and 9 px north of the
follower's end (text maps of both metal shots at each), on a box that is tan with specks in the clean
shot, and a strip leaves the box west between two edge lines 15-18 px apart. Measured every 6 px from
x 4700 to the box, the strips' edges are at y 15839/15857, 16491/16509, 16968/16986, 17445/17462 and
17922/17939 and their inside is tan (median red minus green 19-29, against 33-41 on poly pads); the
samples that do not fit are at the gaps between tracks. Views `r10_15850.png` and `r10_17453.png` (clean
and metal, 2.3x) show the strip unbroken past x 4760 in the first and fourth; the other three were read
from the measurement and the text maps only. The followers' contact candidates along the tracks (three
to six each) were not read one by one: they lie where the tracks cross the poly rows and the diffusion
wires of the lines before them.

### Piece `w11` (run 11): `cdp4_bus_s0` and `lc2_w8450`'s second branch

`cdp4_bus_s0`. `busl`'s track x 5451 turns west 45 px south of y 15000 and runs along y 15037-15053 to a
pad (5364,15044) (metal bright from x 5390 to 5456 at y 15045 in both chips; ring, bright centre and a
hole in the clean shot: `textmap.py 5346 15026 5384 15062 3`). The pad's poly row y 15033-15053 runs west
under every track of the region with no stretch of 6 px without poly colour from x 5350 to 4770 (scan of
the clean shot along y 15040 and 15045) and on into the left array. The metal that lies on `rst_n`'s
row just south (from the track x 5495, along y 15088 to x 5405 and south) is another net.

`lc2_w8450`. `busl`'s track x 4822 runs south to a pad (4823,16713) (`follow.py 4822 15010 S`: end
(4822,16718); metal bright to y 16688, then the ring; candidates (4823,15198), (4823,15305),
(4823,15548), (4823,15723) not read one by one). The pad's poly row y 16703-16723 goes east (poly colour
without a break from x 4845 to 4935). On its way the track crosses the diffusion wires of `cdp3_cw_c7`,
`cdp3_cw_c6` and `cdp3_cw_c5` (y 15372, 15849, 16500).

### Piece `t6` (run 12): six tracks to the six lower rows of the left array

What the master list called "one undrawn metal of another net on `rst_n`'s row" is the westmost of six
thin metals (11-14 px wide) that cross y 15000 between `cdp4_bus_s0`'s track and the gate group
(`cache/scratch/bl0/cut.py hs 15000 15000 20 5340 5760`, the follower's metal test in either chip along
a row: runs at x 5451, 5496, 5540, 5584, 5627, 5671, 5713). Wiring only: no transistor.

| Net | x at y 15000 | Arms (y of the arm, x it steps to) | End pad | Poly row west |
|---|---|---|---|---|
| `cdp3_g_c2` | 5496 | 15090 to 5410; 15438 to 5366; 15915 to 5322; 16565 to 5279; 17043 to 5236; 17521 to 5193; 18084 west | (5106,18081) | y 18070-18092 |
| `cdp3_g_c3` | 5540 | 15134 to 5453; 15481 to 5409; 15958 to 5366; 16608 to 5323; 17086 to 5279; 17603 west | (5236,17603) | y 17593-17614 |
| `cdp3_g_c4` | 5584 | 15177 to 5496; 15522 to 5453; 16001 to 5409; 16652 to 5366; 17127 west | (5322,17127) | y 17116-17137 |
| `cdp3_g_c5` | 5627 | 15221 to 5540; 15568 to 5497; 16046 to 5453 | (5453,16649) | y 16639-16659 |
| `cdp3_g_c6` | 5671 | 15264 to 5584; 15999 west | (5538,15999) | y 15988-16010 |
| `cdp3_g_c7` | 5714 | 15308 to 5627 | (5626,15522) | y 15511-15533 |

How it was read:

- **The staircases** on five views in the metal shot (`r12_a2.png` 2.4x with every package's trace,
  `r12_s2.png` 2.6x, `r12_s3z.png`, `r12_s4z.png`, `r12_s5z.png`, `r12_s6z.png` 2.1x with the clean
  shot) and by cuts: `cut.py hs 15000 18240 20 ...` (the runs along a row every 20 px) and `cut.py v X Y0
  Y1` at the middle of every arm (the arm's y). The first staircase steps every line two track positions
  (88 px) west, round the end of `cdp4_bus_s0`; the others one position (44 px), each below the end of
  one of `lc3`'s through lines, and at each of them the eastmost line left ends on its pad. One metal
  layer: nested L's cannot change their order, so the order at y 15000 is the order of the rows, east to
  west = north to south.
- **Every segment is one metal**: `tl5_tracks.py v|h` on all 47 segments (the two-chip metal test): no
  stretch without metal in both chips longer than 13 px, and those lie in pairs 20-26 px apart, the two
  edges of a poly row or of a diffusion wire underneath (rows y 15088, 15412, 15522, 15676, 15999,
  16649, 16712, 17126, 17213, 17405, 17603; a diffusion wire y 16056-16076). No hole in the clean shot on
  any segment but 9 px at y 16071 on four of the lines, where they cross that diffusion wire (tan
  between two dark edges under each line alike, bright metal over it in both metal shots: trap 36, not
  a contact) and 6 px at (5584,15770) (a speck).
- **The six pads are contacts**: ring and bright centre in the metal shots (chip 2's centre is dark on
  the pad (5538,15999), chip 1's bright: `r12_t5pad.png`, 5.5x both metal shots), and the green hole in
  the clean shot in each (`px.py pt`: red minus green +15, -22, -4, -23, -8, -8 at the six centres;
  views `r12_t6.png` 3.2x in three shots, `r12_s3z.png` .. `r12_t1z.png`). Nothing else leaves a pad.
- **The neighbouring track does not touch the pad** (trap 16): west of each pad but the last a track
  passes 44 px from the pad's centre. `px.py row` through each pad in both metal shots and the clean
  shot: between the track's edge and the ring 6-9 px are open poly, not metal (chip 2 120-167/64-137/
  30-60, chip 1 98-175/46-98/27-53; metal there is 180-230/120-200).
- **The rows are poly, each one piece from its pad to x 4780 and on**: at x 5060, in the open, chip 2's
  metal shot is orange with blue 48-70 across each (field beside 172/140/89), chip 1's has green
  66-107 (one sample over 90), the chip-2 stripped shot red over green by 24-55 against 0 on the field
  beside (`px.py col 5060 Y-22 Y+22 4 metal,metal1,acid,acid1b` for each row; trap 39); along each row
  the clean shot reads poly, under metal or in the open, with no break over 5 px but one
  (`tl5_tracks.py rows row 4740 5660 5 15522 15999 16649 17126 17603 18081`, with control rows): on the
  row y 15999 at x 4840-4865 the clean shot is dark, and both chip-2 shots and chip 1's metal shot show
  the poly there (`px.py row 15999 4812 4884 4`). No hole under any metal the rows pass under; the short
  green or dark stretches the hole test lists lie in the gaps between two metals (trap 2; at
  (4927,15522) the chip-2 shots show orange poly, `px.py row 15522 4910 4958 3`). Picture: `r12_rows.png`
  (all six rows, metal and chip-2 stripped).
- **Four arms lie on a poly row** (Ambiguity 17): no contact.
- Overlays: `r12_o1.png` (1.9x), `r12_o2.png` (1.6x), `r12_o3.png` (1.15x).

**Believed, not traced: these are `cdp3_g_c7` .. `cdp3_g_c2`.** `follow.py X 15010 N --gap 16` runs each
track north through one more staircase (each steps 88 px east at y 14440-14658) to an end at
(5760,14092), (5803,14135), (5761,14177), (5804,14223), (5756,14261), (5799,14304): the y of `bc1`'s six
poly lines (y 14089-14304, drawn from x 7000 east), which carry `cdp3_g_c2` .. `cdp3_g_c7`, the six lines
compared with R14 and latched by `cdp4`'s row D. If the poly lines run on west to those ends,
the wire `bl0` called w18081 is `cdp3_g_c2` and the wire `bl0` called w15522 is `cdp3_g_c7`, and the left array's rows get, from north to
south, `cdp4_bus_s7` .. `s0` (rows y 11488 .. 15043: `busl`, piece `ch1`; run 11 here) and then `cdp3_g_c7`
.. `c2` (rows y 15522 .. 18081): fourteen lines for fourteen rows. Nothing of this is read: the follower
is not evidence for an end (traps 14, 30), and the stretch is in `busl`'s region.

Also seen, other nets, not drawn (the bottom-left logic's): each of the lower rows has a second poly
row from a pad further south whose metal comes from the east (pads (5322,17213) and (5322,17405), rows y
17200-17225 and y 17395-17415; a row y 16705-16720; a diffusion wire y 16056-16076 from a unit at x
5500-5560, y 16090-16190); tracks join the bundle from the east at y 15810-15850 (x 5627, 5671), y
16240-16280 (x 5496, 5540), y 16690-16740 and y 16800-16900.

### Piece `m7144` (run 12): the thin metal north of `bl0_w17337`'s pad, `bl0_w15566`

One wire, 4,400 px, no transistor and no branch. From north to south:

- **A pad (7143,15566)** (ring and bright centre in both metal shots, a hole of 20 px in the clean shot:
  `tl5_tracks.py v 7144 15540 16290`). No metal north of it. **Its poly row y 15555-15577 runs east**
  (orange in the open at x 7215, `px.py col 7215 15546 15586 4`; poly in the clean shot to x 7340, under
  `bc1`'s rail x 7292-7342: `tl5_tracks.py rows row 7120 7420 4 15566`): drawn to x 7260, port. A metal x
  7179-7197 of another net crosses it at x 7188 (from a pad (7186,15520), whose own poly row goes east,
  south to a pad (7187,15696): `r12_b8.png`, 4.8x): no contact (the row is salmon under it, red minus
  green 36-63: `px.py col 7188 15520 15600 4`).
- **Thin metal x 7137-7151 south to a pad (7143,16259)**, one metal (dark stretches of 8-12 px in pairs
  where it crosses poly rows at y 15738, 15825, 15998). The clean shot is green under it at y 15763-15815
  (Ambiguity 19): no contact.
- **A poly column x 7134-7154 under the wide bus metal** (y 16340-16400) to **a pad (7143,16474)**: both
  pads have holes of 17-20 px; the column is over field (pink on both sides under the metal:
  `r12_b4.png`, 3.3x; so read by review round 4 too). The clock's column (`tl4`) is 44 px west.
- **Thin metal south to a corner (7144,17305)**, west to x 7103, south to a corner (7103,17866) and east
  to **a pad (7384,17866)** (`tl5_tracks.py` on the five segments: dark pairs at the rows y 16540, 16780
  (`rcs_mv`), 16866, 16996, 17040 and 17560 (`rst`), nothing longer than 16 px but the pads'
  rings). The corner is 35 px north of `bl0_w17337`'s pad (7144,17340): between the arm's edge (y
  17311) and the pad's ring (y 17326) both metal shots show bare ground (chip 2 91-147/99-137/55-85,
  chip 1 79-104/61-106) and the clean shot open colour (`px.py col 7144 17296 17352 3`), as review
  round 4 found. The wire runs inside the L of the clock's metal (x 7058, y 17908).
- **A poly row y 17855-17875 east under the supply rail x 7470-7520 to a pad (7602,17866)** (poly all the
  way, field north and south of it under the rail: `tl5_tracks.py rows row 7350 7640 4 17845 17866
  17887`; `r12_b1.png`, `r12_b7.png` 5.6x in four shots). The clock's branch x 7551-7566 (`tl4`) crosses
  it. The 18 px "hole" the test lists at x 7422 is dark open poly with no metal over it (orange in both
  chip-2 shots, `px.py row 17866 7366 7450 4`).
- **A metal east along y 17866 to a corner (7970,17866), north to y 17824 and east to a pad
  (8272,17821)** (`tl5_tracks.py h 17866 7570 7990`, `v 7970 17800 17890`, `h 17822 7950 8300`). The 44 px
  north-south arm lies on a poly column x 7962-7983 of another net, which comes south from a pad
  (7968,17778) and runs on south (Ambiguity 20): no contact.
- **The pad's poly row y 17812-17831 runs on east** (open poly from the ring, `px.py row 17821 8278
  8362 4`; `r12_b6.png`, 4.6x): drawn to x 8360, port. Seen, not read: poly to about x 8690 under four or
  five vertical metals, then a metal along the same y from x 8711 to 8955
  (`tl5_tracks.py rows row 8500 9100 5 17800 17821 17842`).

Overlays: `r12_ob12.png`, `r12_ob3.png`. So one line joins `bc1`'s gate group at (7260,15566) to
something east of x 8360 on the row y 17821; neither end is traced, and which end drives is not known.

## Ports

| Name | Layer | Where | Direction | Note |
|---|---|---|---|---|
| `res_b` | M | (6359-6373, 15000) | in | busl's track x 6366 |
| `lpstb_b` | M | (6401-6415, 15000) | in | busl's track x 6408 |
| `rst` | M | (6834-6848, 15000) | in | `busl`'s track x 6841, on north |
| `bl0_w17687` | P | (7790, 15682-15702) | in | poly row west of the pad (7925,15696), into `bc1`'s gate group at about (7745,15690) |
| `bl0_w17610` | P | (7760, 17378-17398) | out | poly row west of the pad (7882,17389), into the gate column east of the supply rail |
| `busl_x6820` | M | (6747-6761, 15000) | in | `busl`'s track x 6754, on north |
| `busl_x6820` | M | (6747-6761, 17000) | out | the thin metal on south: corner (6767,18040), east |
| `rcs_mv` | M | (6964-6978, 15000) | in | `busl`'s track x 6971, on north |
| `rcs_mv` | P | (7030, 15291-15311) | out | poly row east of the pad (6966,15305) |
| `rcs_mv` | P | (7040, 16770-16790) | out | poly row east of the pad (6968,16780), under the tracks and on |
| `cdp3_cw_c7` | M | (5315-5329, 15000) | in | `busl`'s track x 5322, on north |
| `cdp3_cw_c7` | D | (4780, 15362-15382) | out | diffusion wire on west into the left array |
| `cdp3_cw_c6` | M | (5272-5286, 15000) | in | `busl`'s track x 5279, on north |
| `cdp3_cw_c6` | D | (4780, 15841-15856) | out | diffusion wire on west into the left array |
| `cdp3_cw_c5` | M | (5228-5242, 15000) | in | `busl`'s track x 5235, on north |
| `cdp3_cw_c5` | D | (4780, 16493-16508) | out | diffusion wire on west into the left array |
| `cdp3_cw_c4` | M | (5185-5199, 15000) | in | `busl`'s track x 5192, on north |
| `cdp3_cw_c4` | D | (4780, 16970-16985) | out | diffusion wire on west into the left array |
| `cdp3_cw_c3` | M | (5141-5155, 15000) | in | `busl`'s track x 5148, on north |
| `cdp3_cw_c3` | D | (4780, 17447-17461) | out | diffusion wire on west into the left array |
| `cdp3_cw_c2` | M | (5098-5112, 15000) | in | `busl`'s track x 5105, on north |
| `cdp3_cw_c2` | D | (4780, 17924-17938) | out | diffusion wire on west into the left array |
| `cdp4_bus_s0` | M | (5443-5459, 15000) | in | `busl`'s track x 5451, on north |
| `cdp4_bus_s0` | P | (4780, 15033-15053) | out | poly row on west into the left array |
| `lc2_w8450` | M | (4815-4829, 15000) | in | `busl`'s track x 4822, on north |
| `lc2_w8450` | P | (4930, 16703-16723) | out | poly row east of the pad (4823,16713), into the bottom-left logic |
| `vss` | M | (7292-7342, 16925) | - | the gate column's rail, on north; it ends at y 17755 |
| `vcc` | M | (7470-7520, 17020), (7470-7520, 17670) | - | `bc3`'s rail x 7495 |
| `rst_n` | P | (7280, 15078-15098) | out | `rst_n`'s poly row on east: a gate band under `bc1`'s rail x 7292-7342, ending at about x 7350 |
| `rst_n` | P | (5700, 15078-15098) | ? | poly row on west to a pad (4909,15088); a track x 4909 from the north ends there |
| `rst_n` | P | (5725-5745, 15800) | out | `rst_n`'s poly column south of the pad (5737,15759), into the bottom-left logic |
| `bl0_w15412` | M | (2694-2706, 15972), (2694-2706, 16026) | out | the thin metal x 2690-2710 through the pad (2700,15999), on north and on south: believed the force line of the MA cells |
| `larr_l0_g0` | D | (2876, 14105-14122) | in | the diffusion wire is one piece with the box of `larr`'s contact (2893,14114) |
| `larr_cin_s7` | P | (2850, 14559-14574) | out | onto `larr`'s poly row y 14566 |
| `bl0_w14308` | P | (2405, 14687-14708) | out | the third pad's row runs on west of the pad (not read) |
| `larr_l0_g1` | D | (2860, 14517-14533) | ? | onto `larr`'s diffusion (2850-2880, 14508-14540) and its contact (2892,14523) |
| `vss` | M | (2605-2655, 14090), (2605-2655, 14770) | - | the left edge column's rail, on both ways |
| `vcc` | M | (2783-2832, 14090), (2783-2832, 14770) | - | the same |
| `vss` | M | (6013-6067, 15800), (6273-6328, 15800) | - | both arms of the U run on south |
| `vcc` | M | (6187-6241, 15800) | - | the inner rail runs on south |
| `cdp3_g_c2` | M | (5489-5503, 15000) | ? | track on north in the left bus field, drawn by no one (`busl`'s region); follower: to (5760,14092) |
| `cdp3_g_c2` | P | (4780, 18070-18092) | ? | poly row on west into the left array |
| `cdp3_g_c3` | M | (5533-5547, 15000) | ? | track on north; follower: to (5803,14135) |
| `cdp3_g_c3` | P | (4780, 17593-17614) | ? | poly row on west into the left array |
| `cdp3_g_c4` | M | (5577-5591, 15000) | ? | track on north; follower: to (5761,14177) |
| `cdp3_g_c4` | P | (4780, 17116-17137) | ? | poly row on west into the left array |
| `cdp3_g_c5` | M | (5620-5634, 15000) | ? | track on north; follower: to (5804,14223) |
| `cdp3_g_c5` | P | (4780, 16639-16659) | ? | poly row on west into the left array |
| `cdp3_g_c6` | M | (5664-5678, 15000) | ? | track on north; follower: to (5756,14261) |
| `cdp3_g_c6` | P | (4780, 15988-16010) | ? | poly row on west into the left array |
| `cdp3_g_c7` | M | (5707-5721, 15000) | ? | track on north; follower: to (5799,14304) |
| `cdp3_g_c7` | P | (4780, 15511-15533) | ? | poly row on west into the left array |
| `bl0_w15566` | P | (7260, 15555-15577) | ? | poly row east of the pad (7143,15566), on under `bc1`'s rail x 7292-7342 |
| `bl0_w15566` | P | (8360, 17811-17831) | ? | poly row east of the pad (8272,17821); seen to about x 8690 |

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

Run 12:

17. **Four arms of the six lines lie on a poly row with no contact.** `cdp3_g_c2`'s arm y 15090 lies on
   `rst_n`'s row for 90 px (x 5404-5499), and `cdp3_g_c4`'s arms y 15522, 16001 and 16652 lie on the rows
   of the pads of `cdp3_g_c7`, `cdp3_g_c6` and `cdp3_g_c5` for 45 px each. Read as no contact (trap
   13): no pad and no ring in either metal shot, the metal keeps its width, and the clean shot under
   each arm is salmon with red minus green 40-50 and no stretch under 24 (`tl5_tracks.py h 15088 5380
   5520`, `h 15522 5459 5490`, `h 16001 5415 5447`, `h 16652 5372 5403`; `px.py row 15088 5390 5510 6`).
   A contact on any of the last three would join two of the six lines.
18. **`cdp3_g_c6`'s metal on its pad (5538,15999).** The track x 5584 turns west 40 px short of the pad
   and reaches its ring from the east; in chip 2 the pad's centre is dark (95/77/50) and only chip 1
   shows the bright centre, and between the centre and the arm's metal there are 22 px that are dark or
   dim in both chips (a ring, a dim crescent, a second dark line: `px.py row 15999 5481 5565 3`). Read as
   the pad's own line (the same widths as at the pads (5322,17127) and (5236,17603), whose arms arrive
   the same way; a foot 25 px high against the track's 14; the clean shot's hole): `r12_t5pad.png`. If
   the arm ended short of the pad, the track would have no end and the row no source.
19. **The clean shot is green under `bl0_w15566`'s thin metal at y 15763-15815** (red minus green down to
   -65 over 53 px, where it is pink under the same metal north and south of it). Read as no contact:
   both metal shots show the metal at full width and brightness all along, with no ring and no pad
   (`textmap.py 7112 15740 7178 15830 3 --acid`), and the chip-2 stripped shot's stripe under the metal is
   the same there as north of it. What makes the clean shot green there is not known (a pad of another
   net, (7187,15778), lies 40 px east in a large green area).
20. **`bl0_w15566`'s 44 px north-south arm (x 7963-7977, y 17824-17866) lies on a poly column** x
   7962-7983 that comes south from a pad (7968,17778) and runs on south. Read as no contact: the
   column is salmon in the clean shot from y 17792 to 17892 with no hole, neither metal shot has a
   ring, and the dark line between the arm and the east-going metal (x 7978-7987 at y 17822) is the
   column's east edge under the metal, present along the whole column (`r12_b5.png`, 4.8x, both metal
   shots and the clean shot; `tl5_tracks.py v 7970 17800 17890`: no hole).
21. **Which way the seven wires drive** is not known: every end drawn is a pad on a poly row or a port.

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

1. The open column's east edge under the row `rst` is x 7278, not 7292 (a field pocket x 7278-7305
   at y 17546-17599): the pull-down is about 35 wide. Confirmed (`px.py row 17560 7262 7300 3
   metal,metal1`: an edge line at x 7276-7279 across the poly); fixed.
2. Bands C and D lie 6-8 px further north under the rail than west of it. Fixed (each drawn in two parts).
3. Unit 5's load plate runs on south of the strip to y 17646 and ends on field. Fixed.
4. The bar is x 7416-7435 and the thin metal about x 7424-7447. Fixed.

`tools/t.sh bl0 sameconn.py f194b8a`: connections identical. `.venv/bin/python tools/sameconn.py f194b8a`:
connections identical.

Round 6: no findings that change a connection.

### Run 5

Round 7 (full review of piece `w5`; fresh Fable 5.2 reviewer; 2026-11-20 10:52 -0600; commit 9cba725; images
`cache/scratch/bl0/review-7/`). Told to suspect: every place a metal reaches or leaves a pad (profiles
outside each ring on all four sides, after round 4's finding); each pad as a real contact; the corners
and the neighbouring tracks; the track's identity with `busl`'s; the poly column under the bus; the
crossings; second polys on the pads. Checked at 4.6-5.5x in four shots, with text maps, profiles and a
two-chip metal test along and beside every run: all seven pads (ring and bright centre in both chips;
(6842,16562) from text maps only; (6842,16217) has no hole in the clean shot but ring and centre in both
chips); the metal arriving on one side only of each pad; no metal between the pads (7143,17647) and
(7142,17713); no gap and no side branch on any run; the four corners; the poly column continuous over
field with nothing under the five bus metals; the crossings plain; the join with `busl` across y 15000.
Could not check: a khaki band and dark bar under the wide bus metal at y 16360-16378 (read as not a
diffusion: no edge line in either metal shot); the rows east of x 7465.

Findings, geometry or notes only:

1. A third poly row crosses the track x 6841, at y 15078-15098 (`rst_n`'s), with no contact. Notes and
   the trace's comment now say so.
2. Row D's west end is at about x 7139 (drawn 7128). Fixed.
3. The pads (7384,17779) and (7424,17822) reach about 5 px further north. Fixed.

`tools/t.sh bl0 sameconn.py 9cba725`: connections identical. `.venv/bin/python tools/sameconn.py 9cba725`:
connections identical.

Round 7: no findings that change a connection.

### Run 6

Round 8 (full review of piece `w6`; fresh Fable 5.2 reviewer; 2026-11-20 11:08 -0600; commit b3d1ee0; images
`cache/scratch/bl0/review-8/`). Told to suspect: the metal at every pad's ring on all four sides; each
pad as a contact; the track x 7918-7932 over its whole length (jogs, swaps, the five candidates, two
stretches dim in chip 1); the track x 7875-7889; wire 2's poly row under the metal that lies along it;
the crossing at (7840,17778); second polys or metals on the pads. Checked with a two-chip metal test
along both tracks and in strips beside them, text maps, profiles and 12 views: both tracks continuous
with no jog, swap or branch; the two dim stretches are dirt on chip 1 (chip 2 continuous, clean shot
unbroken); no candidate has a ring; another net's poly under the track at y 16210-16345 without contact;
the pads (7882,17389) and (7925,15696) with metal from the south only; the pads (7555,17778),
(7795,17778), (7925,17821) with ring and centre in both chips; wire 1's metal continuous over field; the
crossing at (7840,17778) plain (an arc in chip 1 only, the row uniform in the clean shot); wire 2's row
one poly of constant width with no hole, the metal over it ending at x 7845 and turning south at x 7555
with no ring; field under the rail; the port rows continuous. Not checked: the port rows beyond x 7740
and x 7720; where the neighbouring nets go.

Findings, notes or geometry only:

1. The pad (7880,17777)'s centre is weak in chip 2. Still a contact; the notes say so now.
2. Wire 1's row under the rail is y 17764-17787 (drawn 17768-17790). Fixed.

`tools/t.sh bl0 sameconn.py b3d1ee0`: connections identical. `.venv/bin/python tools/sameconn.py b3d1ee0`:
connections identical.

Round 8: no findings that change a connection.

### Run 7

Round 9 (full review of piece `w7`; fresh Fable 5.2 reviewer; 2026-11-20 11:24 -0600; commit 1a54640; images
`cache/scratch/bl0/review-9/`). Told to suspect: the 2,000 px row (breaks, a neighbouring row taken for
it, pads, diffusion under it, branches); the two corners and the passage under the supply rail; the
metal at each pad's ring on all four sides and each pad as a contact; the other track on x 4909. Checked:
the row y 15401-15425 one poly from x 4909 to 5986, under the wide metal x 4950-5020 with no ring; the
pad (4909,15415) a contact with metal south only and no metal for y 15093-15409 north of it; the track
continuous y 15436-16096, its candidate a row crossing; the pad (4868,16086) a contact, its arm joined
(the skirt is metal in both chips); the long row with no stretch of field in both stripped shots over
x 2845-4868, eight spots at 3.7x in three shots with both edge lines unbroken, no transistor in the
whole-die extraction; both corners one poly with field beyond; the row under the rail uniform; the pad
(2700,15999) a contact with the poly from the east and the thin metal bright on both sides of the ring.
Could not check: x 3157-3173, where the row lies under a track with dirt in both stripped shots (read
as continuous); 8 px between the column's west edge and the diffusion beside the rail at y 16086.

Round 9: no findings.

### Run 8

Round 10 (full review of piece `w8`; fresh Fable 5.2 reviewer; 2026-11-20 11:34 -0600; commit 4838f7c; images
`cache/scratch/bl0/review-10/`). Told to suspect: breaks, contacts at the dozen track crossings, branches
and a neighbouring row on the east row; the thin metal's continuity, its crossings and its end pad; the
poly column. Checked with text maps at 3 px, the two-chip metal test and views at 4x in four shots: the
row one poly from x 6450 to 7285 with both edge lines unbroken, every track bright across it with no
ring, salmon under the rail and ending at about x 7350-7355; the thin metal joined to the pad
(5755,15088) and continuous y 15109-15741, its two dark pairs the edges of the poly rows y 15400-15424
and y 15660-15684 with no hole; the pad (5737,15759) a contact with the metal ending on it and bare
ground south; the poly column leaving it south, nothing else. Could not check: the row through the
rail's edge line at x 7284-7292 (beyond the port); the poly inside the pad's foot; the column south of
y 15800. A correction to the notes of run 2: the tracks east of the bundle are at about x 6965, 7055,
7100 and 7188.

Round 10: no findings.

### Run 9

Round 11 (full review of piece `w9`; fresh Fable 5.2 reviewer; 2026-11-20 11:49 -0600; commit 2ffd23c; images
`cache/scratch/bl0/review-11/`). Told to suspect: `cdp3_cw_c7`'s strip as diffusion or poly, its
continuity, a poly crossing it, a join from a crossing track, the row south of the box; the metal at
every pad's ring on all four sides and each pad as a contact; the two poly columns under the bus and
whether each is the right one; the joins with `busl`'s tracks at y 15000; the row crossings; the thin
metal x 6754 south of the bus. Checked with text maps, the two-chip metal test and 15 views at 3-5.5x:
the three joins with `busl` (one net per name, no break from y 14950); the seven pads (ring and centre
in both chips; metal only on the claimed sides); the two columns straight from top pad to bottom pad,
field between columns, nothing under the five metals; the row crossings as bars with no pad; the thin
metal continuous in chip 2, its candidates chip-1 blemishes; the strip as diffusion in three shots
against the poly row beside it (chip-2 stripped red minus green +13 against +40; chip-2 metal
170/133/94 against 165/112/60), continuous from x 4772 to the box, no poly across it, no pad at any
crossing; no edge line across the poly row y 15401-15425 at the box. Could not check: the 8 px between
the box and that row by colour; the thin bus metals in chip 1 at high zoom; x 6754 at y 16660-16800 and
16870-17000 by view (profile and metal test only).

Round 11: no findings.

### Run 10

Round 12 (full review of piece `w10`; fresh Fable 5.2 reviewer; 2026-11-20 12:03 -0600; commit aa3ad04; images
`cache/scratch/bl0/review-12/`). Told that only two of the five strips had been viewed and that the
followers' candidates were unread, and to suspect: each strip as diffusion, its continuity, a poly
across it, a join or branch, a neighbouring strip taken for it; each track's whole length (a jog onto a
neighbour, a contact, above all where it crosses an earlier wire's strip); each end; the joins with
`busl`. Checked with profiles every 8 px along each strip, the two-chip metal test and a scan of the
gaps beside every track, text maps and 17 views: all five strips diffusion (tan under metal against
salmon on the poly row y 15413; in the open like the reference wire), continuous with both edge lines
21-23 px apart at every sample from x 4764 to the box, no poly across, still there at x 4750; the band
north of the fourth strip is field; every track continuous with bars of 8-17 px only and no metal
beside it; all 15 crossings of a track over an earlier strip plain; every candidate read, none a
contact; all five ends like the reference in four shots; the joins with `busl`. Could not check: the
tracks x 5148-5279 at y 15520-15700 in chip 1 (a blemish in both its shots; chip 2 only); the 16-20 px
dark stretch where each track enters its pad (read as the box's and strip's edges, as on the
reference); west of x 4750.

Round 12: no findings.

### Run 11

Round 13 (full review of piece `w11`; fresh Fable 5.2 reviewer; 2026-11-20 12:14 -0600; commit a588bab; images
`cache/scratch/bl0/review-13/`). Told to suspect: the track x 4822 over its whole length (the four unread
candidates, the crossings of three diffusion wires and of the poly rows, a jog onto a neighbour); both
end pads; `cdp4_bus_s0`'s corner and the other net's metal south of it; its poly row under a dozen
tracks; the joins with `busl`. Checked with the two-chip metal test, a per-row width scan of the track
in both metal shots, text maps and four views at 5-6x: the track one metal from y 14984 to the pad, 9-14
px wide throughout; the four candidates and the three strip crossings plain (the green there is residue
or spans the whole strip); the pad (4823,16713) a contact with metal from the north only and only the
east row leaving; the corner one metal, 32 px without metal south of it; the pad (5364,15044) a contact
(one lollipop outline in both metal shots); the row poly under every track and in every gap, bare
ground north and south in all eleven gaps, no hole, no diffusion under the wide metal; both joins with
`busl`. A correction to the brief, not the trace: the rows y 15088 and y 15412 end on pads at x 4909 and
do not cross the track x 4822. Not checked: beyond the two ports; the track between the listed crossings
on views (tools only).

Round 13: no findings.

### Run 12

Round 14 (full review of pieces `t6` and `m7144` together: two pieces of wiring of one build, thin metals,
pads and poly rows, no transistor; fresh Fable 5.2 reviewer; 2026-11-20 22:52 +0100; commit 1ae67e1; images
`cache/scratch/bl0/review-14/`, 34 of them). Told to suspect, for `t6`: the staircases (an arm onto the
wrong vertical piece, a line ending where another begins on one track position; four of them seen only at
2.1x), `cdp3_g_c6`'s arm into its pad (5538,15999) over 22 px that are dim in both chips, the arms into
the pads (5322,17127), (5236,17603), (5106,18081), the four arms lying on poly rows, the track 44 px west
of each pad, whether each row is poly and one piece to x 4780 (the row y 15999 dark in the clean shot at
x 4840-4865), anything crossing or tapping a row under the tracks or the wide metal x 4954-5018, a
second poly on a pad; for `m7144`: the corner (7144,17305) against the pad (7144,17340), the green
stretch under the thin metal at y 15763-15815 and the pad (7187,15778) beside it, the crossing
(7188,15566), the arm on the poly column at x 7970, the poly column under the bus metal, the row under
the supply rail, the west-east metals near other nets' pads, the pads (7602,17866) and (8272,17821).

Checked: all six staircases and the end at (5106,18081) in both metal shots at 3.7-5x (every arm joins
the claimed verticals, no line ends where another begins); the corner (5323,17086) against the pad
(5322,17127) (8 px of bare ground: the pad is `cdp3_g_c4`'s); the four arms into pads (one 6 px edge
line between foot and pad, no bare ground); the four arms on poly rows (text maps and two views: no
ring, no hole); the tracks 44 px west of each pad (open orange poly between, blue under 55); the six
rows (poly, one piece each to x 4780, orange in the open with blue 56-74 and redder than the diffusion
wire y 16066 under the same tracks; `railprof.py`: poly over field under the wide metal; no second poly
on any pad); the extraction (0 errors, no joined names). For `m7144`: the corner against the pad
(7144,17340) (bare ground y 17318-17322 in both chips; the clock's L separate); the pads on x 7144 at y
17340, 17635, 17700 against the metal x 7103 (10 px of bare ground); the green stretch (an area effect
of the clean shot, the metal at full width in both chips, the pad (7187,15778) separate); the crossing
(7188,15566) in four shots; the poly column under the bus (orange in the open, field on both sides
underneath, bare ground between it and the clock's pads); the row y 17866 under the supply rail (poly
over field; the clock's branch crosses without contact; 5x, four shots); the pad (7384,17866) against
both neighbours at 6x; the east run and the pad (8272,17821) (one metal, clear of the pad (7925,17821)
and of the clock's metal).

Two observations, neither a finding (the reviewer: "comment only"), both read again by the tracer:

- (7977,17821), Ambiguity 20: the chip-2 stripped shot has a greenish patch about 12 px across on the
  poly column under the inner corner of `bl0_w15566`'s metal (`px.py pt 7977,17821`: stripped 125/159/104,
  clean 172/155/90). Not a contact: no ring in either metal shot, no hole in the clean shot (red minus
  green 16-30), the bars at x 7955-7964 and 7978-7987 are 9 px edge lines (the reviewer's `m_x1`..`m_x3`,
  4.3x and 10x, four shots).
- (5192,15522): chip 2's metal shot has a ring-like blemish where `cdp3_cw_c4`'s track crosses
  `cdp3_g_c7`'s row (110/78/45). Chip 1 is bright there (197/161/71), the clean shot cream with no hole
  (209/166/108), the stripped shot has no box (the reviewer's `t_5192.png`, 9x): dirt on chip 2.

Not checked: anything north of y 15000 or beyond the ports at x 4780, 7260, 8360; under the wide metal
x 4954-5018 and under the bus y 16340-16400 only the clean shot and edge lines were usable (the chip-2
stripped shot shows fringes there); the pad (8272,17821) at 3.6x and a text map, not 4x; the straight
runs between staircases by `tl5_tracks.py` on every segment and overlays at about 1x, not at 4x.

Round 14: no findings.

## Not done

- **What pulls `larr_l0_g0` and `larr_l0_g1` up** (neither pull-up is in `larr`'s rows or in the two
  cells drawn here), and the carry into s0.
- **`bl0_w17687`'s source** is in `bc1`'s gate group (the poly row west of the pad (7925,15696)), and
  **`bl0_w17610`'s use** is in the gate column east of the supply rail (the poly row west of the pad
  (7882,17389); `bc3`'s region). Neither group is drawn; they are those packages' work.
- `rst`'s source is `busl`'s (north of y 10400).
- **`bl0_w15566`'s two ends** (the thin metal x 7137-7152 north of the pad (7144,17340): drawn in run 12, piece
  `m7144`): its north row east of x 7260 (under `bc1`'s rail x 7292-7342 at y 15566 and on: `bc1`'s gate
  group) and its south row east of x 8360 (poly to about x 8690 under four or five vertical metals, then
  a metal along y 17821 from x 8711 to 8955: read by text only).
- Beside `bl0_w15566`, other nets, seen and not drawn: a metal x 7179-7197 from a pad (7186,15520) (poly
  row east) to a pad (7187,15696) (poly row east); a pad (7187,15778) in a green area; a pad
  (7187,16430) with a metal south; the poly column x 7962-7983 south from a pad (7968,17778).
- The column north of piece `n1` has a band at y 16866-16884 (`railprof.py 7295 7340 16860 17400`), not
  drawn. All of this lies in `bc3`'s region.
- `bl0_w14308`'s row west of x 2396 (it runs on west of the pad (2459,14700)); the pad (2708,14077) just
  north of the diffusion wire of `larr_l0_g0` (read as not joined to it; its land is not read).
- In the two left-column cells, seen and not drawn: a poly row y 14165-14182 from a pad (2567,14177) (a
  metal from the north, x 2555-2577) east under both rails with no transistor under the vss rail; a
  track x 2493-2512 over `bl0_w14308`'s row; the wide metal west of x 2440; a poly row y 14770-14790
  from the west to a pad (2700,14785), from which a thin metal x 2688-2712 runs south between the rails.
- **The thin metal x 2690-2710 through the pad (2700,15999)** (`bl0_w15412`): believed the force line of
  the MA output cells. To read stretch by stretch at 6x or more in both metal shots: north to the pad
  (2700,14785) (the tab to `mal_frc_m9` at y 15575-15581; a possible break y 15852-15900; a dim, shifted
  stretch y 15392-15470; a short metal y 15860-15870 from x 2720 east), south past y 16136 towards
  `mal_frc_m10` (2729,16278), and how the other twelve pads are fed. It lies in `mal`'s and `larr`'s
  region.
- `rst_n` (the wire `bl0` called w15088) beyond this package: the gate under `bc1`'s rail at (7292-7342, 15088), and the
  poly column south of y 15800 at x 5725-5745 (the bottom-left logic, `bl1`/`bl2`).
- Beyond this package: `busl_x6820` south of y 17000; `rcs_mv`'s two poly rows east of x 7030 and x 7040
  (`bc1`, `bc3`); `cdp3_cw_c7`'s diffusion wire west of x 4780 (the left array).
- Beyond this package: `cdp4_bus_s0`'s poly row west of x 4780; `lc2_w8450`'s poly row east of x 4930.
- The six diffusion wires west of x 4780 (the left array's side).
- **The six lines of piece `t6` north of y 15000** (run 12; `busl`'s region, drawn by no one): the tracks x
  5496 .. 5714 from y 15000 north. The follower runs each through one staircase (88 px east at y
  14440-14658) to an end at (5760,14092), (5803,14135), (5761,14177), (5804,14223), (5756,14261),
  (5799,14304), the y of `bc1`'s six poly lines `cdp3_g_c2` .. `c7` (drawn from x 7000 east): to read, and
  if they join, the six names become `cdp3_g_c#`. And their six poly rows west of x 4780 (the left
  array's side).
- Seen in this package's region and drawn by no one (the bottom-left logic's wiring): tracks that join
  the six-line bundle from the east at y 15810-15850 (x 5627, 5671), y 16240-16280 (x 5496, 5540), y
  16690-16740 and y 16800-16900; a second poly row into each lower row of the left array, from pads
  (5322,17213) and (5322,17405) and their like (rows y 17200-17225, 17395-17415, 16705-16720); a
  diffusion wire y 16056-16076 under the bundle from a unit at x 5500-5560, y 16090-16190; the tracks
  east of the bundle at about x 7015, 7055 (`bc1`'s side).
- South of y 15800 (`bl1`/`bl2`'s region): both rails of the gate group and the gate group there.

## Corrections (coordinator, from the handoffs of 2026-11-20)

- G1's input ("a track x 4909 from the north reaches the west row's end; source not traced"; Not done, "its west row to the pad (4909,15088) and the track x 4909 north"): traced by `busl` run 9 (piece `p2`; firm). **The line is `rst_n`**, from `lc3`'s port (5475,10400) by a poly row y 10663, a pad (4907,10663) and the track x 4909, 4,400 px south without pad or contact. So `bl0_w15412` = NOT `rst_n`, a fourth copy of the reset in `rst`'s sense (high while RES and LPSTB are both low). The pad's contact is at (4909,15087); the track ends there (bare ground to y 15409, where `bl0_w15412`'s track begins on the same position). The port `P 5700,15078-15098` is met; `busl` drew the last 88 px of the track, the pad and the row from the pad to x 5700 inside this package's region. The label of G1's input is renamed at the next refresh.
- Seven more tracks arrive from `busl` at y 15000 and are not followed: the six through lines `cdp3_cw_c7`..`cdp3_cw_c2` (x 5322, 5279, 5235, 5192, 5148, 5105; the follower's ends (5326,15381), (5284,15859), (5239,16506), (5194,16981), (5151,17462), (5107,17938)) and `lc2_w8450`'s second branch (x 4822; follower: to (4823,16690)). A metal jog on the row y 15088 at x 5400-5500 is another net's track (x 5495 north, x 5410 south), not followed.

## Corrections (coordinator, from the handoffs of 2026-11-20, third batch)

- Run 2, "three tracks x about 7050, 7095, 7140": the tracks east of the bundle are at about x 6965, 7055, 7100 and 7188 (review round 10).
- Run 6, "a metal of another net lies along `bl0_w17687`'s row, x 7545-7845": that metal is the buffered clock, `ck_out` (`tl4` runs 11-12: the branch from the pad (7641,17908) along y 17824 to the track x 7840).
- The track x 7100 south of y 15000 beside this block's tracks is `lc1_w7780` (`busl` run 12: to an end pad (7100,15175) and a poly row y 15218 east); the track x 7103 further south (pads (7100,16303) / (7100,16432)) is the clock's (`tl4`).

## Corrections (coordinator, from the handoff of `regs` run 4, 2026-11-20)

- Not done ("Beyond this package: ... `lc2_w8450`'s poly row east of x 4930") and the Ports row (4930, 16703-16723) "into the bottom-left logic": the row is drawn on from there by `regs` (run 4, piece `w8450`): one poly to a corner (5845,16713) with no tap on the way, then to a gate band under the rail x 6008-6055 and, from a pad (5909,16800), by the track x 6408 and the bottom bus row y 18125 to the thin track x 10485 beside the bottom-centre logic's east gate column.

## Corrections (coordinator, from the handoff of `busl` run 14, 2026-11-21)

- Piece `t6`, the ports table and the sentence "believed ... the wire `bl0` called w18081 is `cdp3_g_c2` and the wire `bl0` called w15522 is `cdp3_g_c7`" (and `ports.d/bl0.txt`, "drawn by no one ... follower"): the six tracks are drawn north of y 15000 (`busl`, piece `a6`) and the six identities are firm: the wire `bl0` called w18081 = `cdp3_g_c2`, the wire `bl0` called w17603 = c3, the wire `bl0` called w17126 = c4, the wire `bl0` called w16649 = c5, the wire `bl0` called w15999 = c6, the wire `bl0` called w15522 = `cdp3_g_c7` (aliases until the refresh renames them).
- Piece `w5` and the pair's equations ("`rst` ... not followed", "its source lies north of the field"): the wire `busl` called x6906 is `rst` (`busl`, piece `xn`); the flag's equation is `bl0_w17610` = NOT(`bl0_w17440` OR `rst` OR (`bl0_w17337` AND `bl0_w17687`)), firm: the light pen flag is cleared by the unbuffered reset, NOR(`lpstb_b`, `res_b`).

## Corrections (coordinator, from the handoffs of `busl` run 15, 2026-11-21)

- `busl_x6820` ("busl's track x 6754 ... its north end not read"): it is `lc3_m5756` (`busl`, piece `xm`; an alias until a refresh).

## Corrections (coordinator, from the handoffs of `eof` runs 28-35, 2026-11-21)

- `bl0_w15566` ("poly row east of the pad (7143,15566), on under bc1's rail x 7292-7342"): the row is gate 3 of the NOR `eof_w15523` and ends at x 7347; the metal x 7179-7197 from a pad (7186,15520) to a pad (7187,15696), "another net", is `eof_w15523`, that NOR's output. The pad (7186,15520) is not on `ck_out`'s corner 35 px north.
- `bl0_w15566`'s unit at `bc1`'s rail ("a second net lies beside it"): the gate rows y 15427-15445 (`rcs_e4`), y 15493-15515 (`eof_w16040`) and y 15557-15580 (`bl0_w15566`) are the three inputs of that one NOR. Of the thin metal's crossings at y 15738, 15825, 15998 the first two are `eof_w15262` and `eof_w15128` (gates of the second NOR); the third is the row of another unit's exit box.
- `rcs_mv` ("a pad (6966,15305), whose poly row goes east (port)") and `rst_n` (Ports, (7280, 15078-15098)): drawn on by `eof`: gate 2 of `eof_w15262` (ending at x 7350) and the gate of the inverter `eof_w15128` = NOT `rst_n` (ending at x 7355). `bl0` draws the row of `rcs_mv` `w=20` on y 15301; measured y 15293-15317 (geometry only).

## Corrections (coordinator, from the handoffs of `cdp3`, `cdp4` runs 4-15, `eof` runs 36-51 and `regs` runs 5-6, 2026-11-21)

- The bus of five horizontal metals its pin lines pass under: two of them, y 16262 and y 16303, are the
  outputs of `eof`'s two inverters (`eof_w15998`, `eof_w16218`); they cross `rcs_mv`'s poly column between the
  pads (6970,16175) and (6970,16519) without a pad.
- "Also seen, other nets, not drawn" / Not done: the tracks at x 5627 / 5671, x 5496 / 5540 and the rows from
  the pads (5322,17213), (5322,17405) are `eof_w15998` and `eof_w16218` (drawn, `eof` run 37); the diffusion
  wire y 16056-16076 "from a unit at x 5500-5560, y 16090-16190" is the VCC feed of `eof`'s `cap998`.
- Where `rcs_mv`'s row goes on east ("port"): its load there is the lower select inverter of `eof`'s piece
  `selg` (`eof_ga` = NOT `rcs_mv`).
- The ports at x 4780 "into the left array": each row end now has its load in the left array's selector (`eof`
  run 43).
