# eof: the end-of-frame lead group (follow tasks; spots across the die)

Queue row `eof` of `notes/work-packages.md`: wires whose ends decide the end-of-frame sequence,
followed to their gates. Only what no other package draws is in `trace/eof.txt`; the rest of each
path is other packages' geometry, named where it is used. Coordinates are metal-shot pixels;
images are in `cache/scratch/eof/`.

## Status

Run 1 (Tom Seddon's session, Claude Fable 5.2; 2026-11-18 23:30 to 23:50 +0000).
Three pieces, 2 transistors, no uncertain items.

- **Task 1, where R4's match goes: done** (piece `r4`, wiring only). `rc_eq_r4` is drawn end to
  end from R4's comparator to its loads: it is the net that `rdp3` called `rc_eq_r4` and `bd1`
  called `rc_eq_r4`, **the data input of the latch in the gate column beside the strobe channel
  and the input of inverter A there**.
- **Task 2, where R5's match goes: its first gate found and traced** (piece `r5inv`): at the
  west end of its row in the central datapath's channel `sl_eq_r5` is the only input of an
  inverter that nobody had drawn, **`sl_eq_r5_n` = NOT `sl_eq_r5`**; the output is the line that
  `r9m` and `tc2` had drawn without a driver. Piece `r5w` (wiring only) carries that line on
  west: `sl_eq_r5_n` is `tl4`'s bus line 1 (`sl_eq_r5_n`) and `tl1`/`tl2`'s `sl_eq_r5_n`, which
  leaves the top-left strips north at (2493-2508,2500) into the band y 2180-2500 (package
  `tlb`, not drawn by anyone). **No load of it is drawn yet.**

Run 2 (Tom Seddon's session, Claude Fable 5.2; 2026-11-19 00:13 +0000 on). Two more pieces, wiring
only, no uncertain items.

- **Task 3, `inh_ck`'s source: found** (piece `tcwa`). `inh_ck`'s metal, which `tl6` drew to
  (6105,6350), is drawn on south and east down a staircase of five corners to the west end of
  `trunks`' line "S" at (6690,8366): **`inh_ck` is `inh_ck`**, the output of the lone inverter of
  the input buffer row (`inh_ck` = NOT `inh_n`, `inh_n` = NOT `inh_src`), the net that holds
  `ck_b` low in the clock block. No uncertain item lies on the path (`tools/unsure.py`). On the
  way the metal has **one tap**, a contact (6427,7648) onto a poly row that runs 1,100 px east
  to a gate group nobody has drawn (x 7540-7670, y 7600-7750, at the west edge of `cdp2`'s row
  C): drawn to x 7530; the group is not traced.
- **Task 4, `rcs_x1`'s driver: found** (piece `x1`). The poly bus that leaves `tl5`'s strip south
  is drawn down to its pads and the pads' metals to `lc1`'s wires: **`rcs_x1` = NOT
  `lc1_w7170`**, the output of `lc1`'s gate 2 (its input comes up a thin metal from `lc2`'s
  strip, (5030-5046,8067)). The same piece joins three more lines: **`res_b` and `lpstb_b` are
  the two inputs of `lc1`'s NOR**, so `rst` = NOR(`lpstb_b`, `res_b`) (firm): high while
  RES and LPSTB are both low, **the chip's reset**; and `rst_a` (the clear
  of four latches of the top-left logic) is `rst_a`, one of the three buffered copies of
  that NOR.

Run 3 (richtw1's session, Claude Fable 5.2; 2026-11-19 11:50 +0100 on). One piece, 4 transistors,
no uncertain items.

- **Task 2, the loads of `sl_eq_r5_n`: its first load found and traced** (piece `r5nor`). The four
  polys that leave `tl1`'s strip north at x 2362-2515 all end in one gate in the band north of the
  strips, which nobody had drawn: a three-input NOR, **`tl1_w2637` = NOR(`tl1_w5936`, `rcs_c1`,
  `sl_eq_r5_n`)** (firm). `tl1_w2637` is the data of `tl3`'s latch A, so **latch A takes "R5's
  match AND NOT `rcs_c1` AND NOT `tl1_w5936`"**. The poly of `sl_eq_r5_n` ends on this gate.

Full extraction with run 3: 2,379 nets, 4,286 transistors, 0 errors, 0 warnings.

Run 4 (richtw1's session, Claude Fable 5.2; 2026-11-19 12:35 +0100 on). One piece, wiring only, no
uncertain items.

- **Task (b), `inh_src`'s source: not found; two of its three open ends followed** (piece `isrc`).
  `inh_src` (the signal whose copies are `inh_ck`, `inh_rc`, `inh_lat`) is a widely fanned-out line of
  the bottom-centre logic. **One end is the clear of `bc2`'s latch unit a** (its own name for the pad is under Former names in the glossary; joined:
  `bc2_w15029` = NOT((`bc2_w14876` AND `bc2_w14955`) OR `bc2_w15000` OR `inh_src`)). The bus line
  west of the pad (9770,18081) feeds a 2,470 px metal x 8968 with three pads and a west branch,
  each on a poly that goes on west into the gate column x 8650-8800 (repeated units; not followed).
  The third end (the poly y 16950 east of x 10470) is a gate row of the unit under the rail
  x 10540-10585 (looked at, not drawn). **Every end seen so far is a gate; the driver is still open.**

Run 5 (richtw1's session, Claude Fable 5.2; 2026-11-19 13:05 +0100 on). One piece, 4 transistors,
no uncertain items.

- **Task (c), the gate group at the end of `inh_ck`'s tap row: traced** (piece `g7700`). It is one
  gate under the VSS rail of the central datapath's column 0: **`eof_w7818` = NOT(`eof_w7777` AND
  (`inh_ck` OR `eof_w7718`))** (firm). Rows 1 and 2 are **not** two fingers of `inh_ck` (run 2's
  guess from a 2.7x view): their ends lie on a field island and are apart; row 2 is its own net.
  All three wires are followed to pads, none yet to a known net: the output goes west and north
  (two pads, a metal x 7272) to a pad (7272,6912) whose poly goes on north; `eof_w7718` has a pad
  (7267,7736) with two metals (north to a pad (7313,7215) with a poly row east; south, a long
  run); `eof_w7777` runs 1,180 px west through the crossing field, steps one track at (6886,7777)
  and enters `lc1`'s strip at (6450,7821). **It is not `lc1_w7780`**, which runs beside it one
  track up and ends on a pad (6815,7778).

Full extraction with run 5: 2,382 nets, 4,290 transistors, 0 errors, 0 warnings.

Run 6 (Tom Seddon's session, Claude Fable 5.2; 2026-11-19 12:47 +0000 on). One piece, 19 transistors (a cell
copy), the cell's own four uncertain diffusion items copied with it.

- **Task (d), the clock of `lc2`'s ripple counter: it is another flip-flop's output** (piece `ff3`). The
  L-shaped metal that `lc2` drew as the clock of its first flip-flop (`lc2_w8475`, from the south at
  (4553-4575,9190)) is the slave-output track of **a third copy of the flip-flop cell `lc2_ff`**, 780 px
  below `lc2`'s first, in `lc3`'s logic column A (x 4440-4990, y 9185-9990; `findcell` score 0.86, every
  pad and box of the copy on its feature). So **`lc2_w8475` = NOT(`eof_w9472` AND (`eof_w9255` OR
  `eof_w9505`))** (firm): the counter that `lc2` found has at least three stages, and this one is the
  stage *before* `lc2`'s first. It has the same clear lines (track A, `lc1_w7170`, ends on this copy's
  pad; track B, `lc2_w8907`, runs on south). **Its own clock, `eof_w9255`, again arrives by an L-shaped
  metal from the south** on the same track position (x 4553-4575): the chain goes on down the column
  (`findcell` has a weaker hit 781 px further down, score 0.52, and a turned copy in column B, 0.70:
  neither looked at).

Full extraction with run 6: 2,391 nets, 4,309 transistors, 0 errors, 0 warnings. The package by itself
now loads `lc2` and `lc1` (for the cell), whose own partial-load messages appear (2 errors, 46 warnings,
none on this package's lines).

Run 7 (Tom Seddon's session, Claude Fable 5.2; 2026-11-19 14:28 +0000 on). One piece, 1 transistor, three
uncertain items (the load's tie).

- **Task (e), `bd1`'s latch on R4's match: its lower half's load found, and the latch closes** (piece `r4lat`).
  East of the ground rail, where `bd1` had left "N2's load and the driver of `bd1_q`" untraced
  (x 13876-13995, y 15640-15705), the band that `bd1` drew as `bd1_q` is the top of a load block of the
  same build as the upper half's, 97 px below it: a poly block x 13937-13992 over a strip from the VCC land,
  whose west end turns south to N2. A heavy-outlined box at the band's west end is its tie, so **`bd1_q`
  is `bd1_n2`** and the two halves are a cross-coupled pair: **`bd1_n1` = NOT(`bd1_n2` OR (`inh_lat` AND
  `rc_eq_r4`)), `bd1_n2` = NOT((`bd1_an` AND `inh_lat`) OR `bd1_n1`)**: a transparent latch of R4's match,
  open while `inh_lat` is high, with `bd1_n2` the match as latched and `bd1_n1` its inverse (marked: both
  loads' ties are uncertain items). **Where the latch's outputs go is still open**: nothing leaves the
  lower half east or south (seen, `e_s2.png`); the one candidate is `bd1`'s old question at N1's west end
  (Not done).

Full extraction with run 7: 2,398 nets, 4,345 transistors, 0 errors, 0 warnings (the package by itself now
also loads `bd1`, with `sel` and `bd3`).

Full extraction after run 2: 2,351 nets, 4,232 transistors, 0 errors, 0 warnings; the package
by itself (it loads `rdp3`): 0 errors, 0 warnings.

## Inventory

| Piece | Where | What |
|---|---|---|
| `r4`, link A | x 13416-13667, y 9647-10705 | from `mrach`'s poly end (13425,9663): pad and contact (13433,9665), the upper piece of bundle track L2 (y 9652-9938), pad and contact (13432,9925), poly bar y 9916-9934 east under L3-L6, pad and contact (13650,9925), track L7 south to `rdp3`'s piece at y 10700 |
| `r4`, link B | x 13729-13747, y 13475-14695 | bundle track L9, straight, from `rdp3`'s end (13738,13480) to `bd1`'s track k15 (13738,14690) |

| `r5inv` | x 8330-8650, y 4700-4880 | an inverter in the slice-0 position of `cdp1`'s channel: C-shaped input poly (the west end of the row y 4719), pull-down under slice 0's VSS rail (contact (8431,4770)), node strip y 4824-4848 with a buried contact to the output's poly at its west end (box x 8358-8392), load block x 8550-8590 (an arm from its top west to the tie box) with its tie box x 8508-8538, y 4783-4815, VCC contact (8615,4838) |
| `r5w`, link C | x 4962-5183, y 2542-2560 | the poly row from `r9m`'s corner (5175,2550) west under rail RC and the supply metal x 4948-4997 to `tl4`'s row end (4967,2551) |
| `r5w`, link D | x 3528-4255, y 2494-2526 | `tl2`'s metal on to a pad with a contact (3606,2510), a poly bar under the wide metal x 3648-3760, a pad with a contact (3800,2510), a straight metal east to `tl4`'s bus line 1 at (4250,2512) |

| `tcwa`, link E | x 6098-6438, y 6345-8072 | `inh_ck`'s metal on from `tl6`'s end (6105,6350): south to a corner (6105,7346), east (on `lc1_w7040`'s poly row, no contact) to a corner (6298,7346), south to a corner (6298,7432), east (on another row) to a corner (6430,7432), south through the tap's pad to y 8067, where `lc2`'s piece (`inh_ck`) takes over |
| `tcwa`, the tap | x 6412-7530, y 7632-7664 | a pad with a contact (6427,7648) on that metal; its poly row y 7640-7656 east across the crossing field to the gate group at x 7540 (drawn to x 7530) |
| `tcwa`, link F | x 6445-6695, y 8165-8374 | from `lc2`'s end (6450,8172): east to a corner (6559,8172), south (on the poly of another net's pad (6558,8127), no contact) to a corner (6559,8367), east to `trunks`' end (6690,8366) |
| `x1` | x 5053-5253, y 6345-6905 | five vertical polys of `tl5`'s bus on south from y 6350 (x 5063, 5107, 5150, 5192, 5237), straight under nine horizontal metals; four end on pads with contacts (5105,6761), (5147,6803), (5190,6845), (5237,6803), each with a metal on south to one of `lc1`'s wires at y 6900 (M_a, M_b, V2, V3); the fifth (x 5063) has no pad and runs on south. **Below three of the pads the poly goes on** (x 5150 in the open; x 5192 under V2; x 5237 under V3) and bends south-east into `lc1`'s diagonal poly bundle: drawn to y 6900 (the last to y 6872) |

| `r5nor` | x 2250-2600, y 1900-2506 | a three-input NOR in the band north of `tl1`'s strip: pull-down band y 2428-2465 under three polys (x 2362-2386, 2405-2427, 2493-2515), two VSS pads with contacts (2397,2376), (2532,2384) under an arm of the VSS plane (x 2270-2590, y 2347-2404), output strip x 2450-2478 north to a load (poly block x 2436-2526, y 2238-2292, tie box x 2499-2529, y 2304-2330), a branch of the output round the west side (y 2309-2328, x 2331-2351) to the first pull-down's drain, the output's buried contact to `tl1_w2637`'s poly (box x 2446-2474, y 2440-2466); VCC by a diffusion strap x 2288-2549 north to a head with seven contacts (y 1940) under the supply plane; a metal island (x 2272-2543, y 2184-2232) with one contact (2467,2205) on the strap |

| `isrc`, link G | x 10209-10405, y 15083-15929 | from `trunks`' metal x 10225 (y 15886): pad and contact (10226,15912), poly north to pad and contact (10226,15783), metal north / east y 15654 / north x 10312 / east y 15308 / north x 10396 to `bc2`'s pad (10395,15087) |
| `isrc`, link H | x 8650-9770, y 15244-18098 | from `trunks`' pad (9770,18081): poly west to pad and contact (9554,18081), metal y 18083 west to pad and contact (8964,18081), poly north to pad and contact (8967,17735); from there a metal north x 8968 through tap pads (8966,16737), (8962,16172) to an end pad (8966,15260), and a metal west y 17737 to a pad (8688,17737); each of the four pads' polys goes on west (stubs drawn) |

| `g7700`, the gate | x 7541-7775, y 7585-7860 | VSS rail x 7552-7598 over a diffusion column x 7541-7611, y 7613-7820, with one contact (7572,7684); three poly rows across it: row 1 y 7638-7656 (`inh_ck`), row 2 y 7708-7728 (`eof_w7718`), row 3 y 7767-7787 (`eof_w7777`); a diffusion ring east of the rail (top strip y 7613-7628, strap x 7637-7654, bottom strip y 7745-7757) round a field island x 7612-7636 on which rows 1 and 2 end; the output node south of row 3: east by a T-shaped diffusion wire (arm y 7803-7817, vertical x 7643-7658, y 7783-7854) to the load's strip (y 7783-7809) and the tie box (7664-7690, 7832-7854); load plate x 7666-7721, y 7761-7827; VCC box x 7726-7773, y 7759-7808 with contact (7748,7779) under the wide metal x 7725-7775 |
| `g7700`, the output | x 7254-7545, y 6875-7839 | diffusion wire west from the column (y 7803-7822) to a buried contact (7490-7518, 7805-7832); poly row y 7812-7831 west to a pad with contact (7402,7822); thin metal x 7401 north to a pad with contact (7401,7606); poly west along y 7604 under two metals to a pad with contact (7273,7606); thin metal x 7272 north to a pad with contact (7272,6912); the pad's poly on north (drawn to y 6875) |
| `g7700`, row 2 | x 7244-7632, y 7198-7800 | poly y 7726-7745 west (a widened step at x 7500-7527) to a pad with contact (7267,7736); from the pad a metal east and north (corner (7315,7736)) to a pad with contact (7313,7215), whose poly row leaves east (drawn to x 7400), and a metal south (x 7268, drawn to y 7800) |
| `g7700`, row 3 | x 6450-7634, y 7767-7831 | poly y 7767-7787 west from its end cap (x 7634) across the crossing field to a corner (6886,7777), south one track, west along y 7812-7830 to `lc1`'s east edge x 6450 |

| `ff3`, the flip-flop | x 4578-4985, y 9220-9955 | `@inst lc2_ff 0,780`: `lc2`'s cell (gates K1-K4, 19 transistors) 780 px lower, under the same west rail (x 4752-4820) and middle rail (x 4924-4980). Under the west rail (`railprof.py 4752 4798 9200 9860`): K1's rows y 9245-9271, 9296-9309; K2's 9418-9442, 9461-9485; K3's 9592-9616, 9647-9671; K4's 9758-9781, 9801-9824, 9844-9859 and one more (y 9913-9932) |
| `ff3`, the copy's own | x 4458-4980, y 8695-9990 | K1's VSS node, a short box y 9196-9242 under the west rail with one contact (4765,9211) (the master has a long contact column there); both rails y 9185-9970; track C (x 4553-4571) from `lc2`'s end (y 9190) to the copy's row-2 pad (4561,9296); track A (x 4466-4484) from `lc2`'s end (y 9060) to its END pad with a contact (4473,9818); track B (x 4508-4526) from `lc2`'s end (y 8700) through the pad with a contact (4517,9384) of the clear row, drawn to y 9420; the clock's L-shaped metal from the END pad (4648,9904) west along y 9897-9919 and south on x 4553-4575, drawn to y 9990 |

| `r4lat` | x 13868-14004, y 15618-15728 | the load of the lower half of `bd1`'s latch: a poly block x 13937-13992, y 15644-15704 below `bd1`'s band (y 15630-15650, the net `bd1_q`), over a diffusion strip y 15659-15689 from the VCC land (x 14000) west to x 13916; the strip's west end (x 13919-13934) south by a dogleg as an arm x 13908-13929 to y 15728 and west along y 15712-15728 to N2 under the ground rail; the tie, a heavy-outlined box (13889-13913, 15660-15682) below the band's west end (uncertain); the poly from gate G4's block to the band (x 13895-13909, y 15618-15640) |

The bundle left of the right datapath has tracks L0..L11 at x 13348 + 43.4 k.

## Logic

Wiring only. What the join gives (traced; equations from the full extraction):

```
rc_eq_r4 = NOR(r4c_b0_x .. r4c_b6_x)                 rdp2: high when the row counter equals R4
bd1_an   = NOT rc_eq_r4                              bd1's inverter A            (firm)
bd1_n1   = NOT(bd1_n2 OR (inh_lat AND rc_eq_r4))     upper half of bd1's latch   (depends on bd1's ? items)
bd1_n2   = NOT((bd1_an AND inh_lat) OR bd1_n1)       lower half; its load is piece r4lat (run 7; depends: the tie)
```

(Until run 7 the lower half had no load and the first equation read `bd1_q` for `bd1_n2`: piece `r4lat`,
below, shows they are one net.)

`tools/unsure.py --equations`: `rc_eq_r4` FIRM, `bd1_an` FIRM, `bd1_n1` DEPENDS (on `bd1`'s
uncertain items, none of them on this wire). `tools/unsure.py` does not list `rc_eq_r4`: no
uncertain item lies on the path from the comparator's NOR to the two gates.

Traced since run 7 (piece `r4lat`; marked, the two load ties): the two halves are a transparent latch
of this signal, open while `inh_lat` is high; `inh_lat` is a copy of `inh_src`, the signal that also
stops `ck_b` (`inh_ck`) and the row counter's step (`inh_rc`). So **what R4's match does at the
end of the frame goes through this latch**. Where `bd1_n1`, `bd1_n2` and `bd1_an` go from the latch
is not found (Not done).

### The path, north to south

| Stretch | Drawn by | What | Evidence |
|---|---|---|---|
| comparator to the counter channel | `rdp2`, `mrach` | NOR at about (15000,8426); poly west and south to track T6 (= L0), contacts (13348,9360), (13349,9663); poly east along y 9663 to x 13425 | their notes; not re-read |
| **link A** | `eof` | the poly row runs on under L1 (`wr_r4`: no pad, no hole) to a pad with a contact (13433,9665), top of L2's upper piece; that metal ends on a pad with a contact (13432,9925); a poly bar goes east along y 9925 under L3 (`h_eq_r2`), L4, L5 (`rc1`), L6 with no contact, to a pad with a contact (13650,9925), top of L7 | `a_top.png` (2.8x, metal / chip-2 stripped / clean), `a_bar.png` (4x, three shots), overlay `ov_a.png`; text maps of both pads' rows and of the whole bar in both metal shots and the clean shot (each end pad: bright centre in a dark ring in both chips and a green hole in the clean shot; the bar plain between); `tools/follow.py` on both metals; `tools/tla_contacts.py` on both: no candidate |
| L7, L6, L5, link, L9 | `rdp3` | L7 from y 10700, jog west onto L6 at y 11507, onto L5 at y 12313, contact (13565,12826), poly link east under L6 and L7, contact (13736,12826), L9 south to y 13480 | read again here from text: `tools/follow.py 13651 10710 S` gives the two jogs and the end as drawn; its three contact candidates ((13651,11346), (13564,12585), (13563,12611)) are field under whole metal (text maps); the link's poly is continuous under L6 and L7 with no hole. The east contact: see Ambiguity 1 |
| **link B** | `eof` | L9, one straight metal y 13480-14690; crosses `hc5`'s poly (y 13880-13908) and `hc4`'s band (y 14010-14038) without a pad | `b_l9_m.png`, `b_l9_c.png` (2x strips, metal and clean shot, every package's trace outlined); follower positions every 200 px; text maps of the band crossing and of the one contact candidate (y 14222: field under whole metal) |
| k15 to the gates | `bd1` | k15 from y 14690, jog west at y 15087 to x 13652, contact (13655,15391), poly to gate P2 (in series with `inh_lat`'s P3 on node `bd1_n1`) and P4 (inverter A) | `tools/follow.py 13738 14700 S` gives the jog and the end as drawn; `d_bd1.png` (2.35x, all traces): the overlay sits on the features. The gate column itself was not re-read (`bd1`'s re-read item R1 stays) |

### Piece `r5inv`: the inverter on R5's match (traced)

```
sl_eq_r5 = NOR(r5c_b0_x .. r5c_b4_x)        rdp1: high when the scan line counter equals R5
sl_eq_r5_n  = NOT sl_eq_r5                      this piece (firm)
```

| Device | Where | W/L | Gate | Between |
|---|---|---|---|---|
| pull-down | (8427,4806) | 62/20 | `sl_eq_r5` (the C's lower arm, y 4796-4816) | `vss` (contact (8431,4770) of slice 0's rail) and the node |
| load | (8570,4839) | 38/40 | the node (tie box at the block's north-west corner) | the node and `vcc` (contact (8615,4838) of slice 0's rail) |

- **Input.** `cdp1` draws `sl_eq_r5`'s poly row y 4719 from x 10850 to x 8340 (one straight poly
  with no pad and no step in the clean shot at 2x, `t2_row.png`). At its west end the row turns
  south (x 8331-8351) and comes back east as a lower arm y 4796-4816: a C whose inside is
  field. The arm runs under the VSS rail and ends in a rounded end at x 8474; it does not reach
  the tie box 35 px further east (nothing orange at x 8480-8500 in either chip-2 shot).
- **Output.** The node strip's west end lies in a heavy-outlined box (x 8358-8392, y 4836-4864)
  with the end of the poly row that `tc2` drew from the pad (8290,4850): a buried contact. From
  there the net is `sl_eq_r5_n` (`tc2`'s piece 13 and `r9m`).
- **Supplies.** The two rails are slice 0's of the central datapath (`cdp1`'s notes: VSS
  x 8395-8440 widening here, VCC x 8620; `shm` labels both at y 3950); only the pieces over the
  gate are drawn here. The load hangs from the east rail and the pull-down from the west one,
  which agrees.
- Evidence: `t2_s1.png` (2.3x, all traces), `t2_g1.png` and `t2_g2.png` (3.6x, four shots),
  `t2_wbox.png`, `t2_tie.png` (4.2x, three shots), overlay `t2_ov.png`; profiles and text maps
  named in `trace/eof.txt`. `tools/opendiff.py 8320 4700 8670 4890`: no undrawn open diffusion;
  the two pockets (8372,4762) and (8555,4758) are field (chip-2 stripped shot red minus green -2).

### Piece `r5w`: the inverter's output on west (traced; wiring only)

| Stretch | Drawn by | What | Evidence |
|---|---|---|---|
| inverter to the top-left corner of `tl6` | `tc2`, `r9m` | the pads (8290,4850), (8246,4716), the row y 4676, the pad (7855,4676), the crossing field, the metal x 6022 / y 2599, the pad (5400,2596), a poly west along y 2596 and north at x 5175 to y 2550 | their notes; not re-read |
| **link C** | `eof` | from that corner the poly is a row y 2542-2560 running west under rail RC (x 5078-5127) and the wide supply metal (x 4948-4997), no contact to either, to `tl4`'s row end (4967,2551) | `t2_w2.png` (4x, three shots, all traces), overlay `ov_c.png`; text map of the row |
| bus line 1 | `tl4` | the pad (4908,2551), the metal along y 2555, a diagonal at x 4669-4712, y 2512 west to x 4250 | its notes |
| **link D** | `eof` | the metal runs on west, straight over plain field, to a pad with a contact (3800,2510); a poly bar y 2501-2517 under the wide vertical metal x 3648-3760 (no contact); a pad with a contact (3606,2510); the metal on west to `tl2`'s end (3533,2509) | `t2_w3.png` (4.4x, three shots), `t2_w4.png` (1.75x, the whole stretch), overlay `ov_d.png`; text map of both pads and the bar |
| to the band | `tl2`, `tl1` | `sl_eq_r5_n`: the metal x 3503 / y 2598, the pad (2868,2596), the row y 2591, a poly north out of the strips at (2493-2508,2500) | their notes |

The full extraction has one net with the three names and no gate on it but the inverter's own
load: **where NOT `sl_eq_r5` is used is north of y 2500** (or at a tap nobody has drawn).

### Piece `r5nor`: the first load of NOT R5's match (traced)

```
tl1_w2637 = NOR(tl1_w5936, rcs_c1, sl_eq_r5_n)     this piece (firm: tools/unsure.py --equations tl1_w2637)
          = sl_eq_r5 AND NOT rcs_c1 AND NOT tl1_w5936
```

| Device | Where | W/L | Gate | Between |
|---|---|---|---|---|
| pull-down 1 | (2374,2446) | 37/24 | `tl1_w5936` | `vss` (the finger x 2391-2401 from the west pad) and the output (the band's west end, by the strip round the west side) |
| pull-down 2 | (2416,2446) | 37/22 | `rcs_c1` | `vss` (the same finger) and the output |
| pull-down 3 | (2504,2446) | 37/22 | `sl_eq_r5_n` | the output and `vss` (the east pad's finger) |
| load | (2464,2265) | 28/54 | the output (tie box at the block's south-east foot) | the output and `vcc` (the strap) |

Traced: every device above, and with them the equation. Believed, not traced here: what the
inputs mean. `tl1_w2637` runs (by `tl1`, `tl2`, `tl3`) to the data input of `tl3`'s latch A
(`tl3_w3419` = NOT((`tl1_w2637` AND `tl3_w3373`) OR `tl3_w3550`); enable `tl3_w3373` = NOT
`tl4_w4590`, clear `rcs_x1`) and to `tl3_w3233` = NOT `tl1_w2637`. `tl1_w5936` is the buffered
output of `tl1`'s third latch (open while `ck_out` is high, takes `tl1_w3333`); `rcs_c1` =
NOT `rcs_a2` AND (`rcs_x1` OR `rcs_u3425`) is `tla`'s. So the end-of-frame path from R5 goes:
`sl_eq_r5` -> inverter (`r5inv`) -> this NOR, gated by those two -> latch A of the middle cluster.

- **The four polys.** `tl1` draws them to y 2500 (`tl1_w5936` as the row y 2498-2515). Each
  goes on north as a column between two dark edge lines, orange in both chip-2 shots (`z1.png`,
  `z2.png`, 5x, four shots; `textmap.py 2326 2340 2554 2476 3`: gate edges 2360/2388, 2403/2429,
  2491/2516). Three cross the band and end 25 px beyond its top edge, under the edge of the VSS
  arm (protected poly in the clean shot at y 2403-2420, pink field above: the clean map of
  `textmap.py 2326 2340 2554 2432 3`); the fourth, `tl1_w2637`, ends in a box on the band.
- **The band** y 2428-2465 (edge rows 2427-2430 and 2463-2466 dark from x 2331 to 2540). Above
  it the diffusion goes on only in four fingers; the pockets round the poly tops (x 2353-2362,
  2434-2443, 2476-2485, y 2412-2424) are field (greenish in both chip-2 shots).
- **The output node** is the strip x 2450-2478 from the band to the load, continuous under the
  VSS arm (`px.py col 2464 2226 2476 4`; tan between pink in the clean shot), with no ring and no
  hole where the arm crosses it. A branch leaves it west at y 2309-2328 and runs down the west
  side (x 2331-2351, under the arm) to the band's west end: a narrow diffusion wire (a strip
  between two dark edges, 177/129/84 in the chip-2 metal shot against 163/139/93 for field and
  blue 50-66 for the polys: `px.py col 2390 2288 2350 2`, `row 2335`, `row 2385`, `col 2344`,
  `row 2319 2430 2545 3`). So pull-down 1's far side is the output, not a fourth node.
- **`tl1_w2637`'s box** (x 2444-2475, y 2438-2465): a heavy-outlined inverted U on the band, at
  the top end of the poly, wider than the poly: a buried contact (`z1.png`, `z2.png`).
- **The load.** One poly block x 2436-2526, y 2238-2292: poly colour over its whole width
  (`px.py row 2265 2420 2535 3`), with the strip's two edges as dark lines under it at x 2449 and
  2478 and the part over the strip brighter in the clean shot. Its foot (x 2506-2526) runs from
  the south-east corner into a heavy-outlined box (x 2497-2530, y 2303-2330, light centre) at
  the end of a spur of the output strip (`textmap.py 2470 2284 2546 2344 3 --acid`; `z3.png`,
  `z4.png`, 4x, four shots): the tie.
- **VCC.** Above the load the strip widens (x 2447-2497) into a wide diffusion (x 2288-2549)
  that runs north, in the open (bright green in the clean shot, y 1965-2075; `px.py row 2020`),
  under two MA driver lines (`mal`'s, y 2092-2106 and 2136-2150; no ring, no hole:
  `textmap.py 2280 2080 2556 2160 6`) to a head (x 2262-2572, y 1915-1962) with seven contacts
  under the wide supply plane north of y 1963 (`s4.png`, `s5.png`, overlay `ov2.png`). **That the
  plane is VCC is taken from the load hanging from it** (tracing guide, section 3); the plane is
  not drawn by anyone (`padring`), only a piece over the head is in `trace/eof.txt`. The metal
  island x 2272-2543, y 2184-2232 over the strap's south end has one contact, (2467,2205), onto
  the strap, and reaches nothing else (`textmap.py 2262 2174 2560 2240 4`; `follow.py 2420 2219
  W` ends at x 2278): a strap.
- **VSS.** The arm x 2270-2590, y 2347-2404 is part of `tl1`'s VSS plane (no edge line between
  them at x 2584-2588 from y 2350 to 2402, where there is one above and below: `textmap.py 2540
  2326 2620 2416 4`), with a contact on each pad (ring with a centre in both metal shots, specks
  or a hole in the clean shot: (2397,2376), (2532,2384)).
- Overlays: `ov1.png` (2.6x, metal and clean, trace on both), `ov2.png`. `tools/opendiff.py 2240
  1890 2600 2510`: no undrawn open diffusion (the groups it lists at y 1892-1955 are colour
  fringes under the plane). West of the gate (x 2040-2330) there is nothing but the arm's end and
  the two MA lines (`s6.png`).

### Piece `isrc`: `inh_src` on from two of its open ends (traced; wiring only)

```
inh_n      = NOT inh_src                                              bd1 (X's driver)
bc2_w15029 = NOT((bc2_w14876 AND bc2_w14955) OR bc2_w15000 OR inh_src)   bc2's latch unit a: inh_src is its clear
```

The full extraction has one net `inh_src` with three gates on it: `bd1`'s two and now `bc2`'s
clear pull-down (10510,15088). `tools/unsure.py` does not list `inh_src`. `bc2`'s unit itself was
traced on another model and waits for its Fable review (re-read item R31); the join is this piece's.

| Stretch | Drawn by | What | Evidence |
|---|---|---|---|
| to (10225,15886) | `trunks` | the pad (10310,16950), poly, pad (10225,16820), metal x 10225 north | its notes |
| **link G**, two pads and a hop | `eof` | the metal ends on a pad with a contact (10226,15912); poly north (x 10218-10235) under the horizontal metal y 15822-15834, no hole, to a pad with a contact (10226,15783) | `b1.png` (1.5x, all traces); `textmap.py 10190 15750 10262 15930 3`: each pad a bright centre in a ring and a hole in the clean shot, poly 5-8 between |
| **link G**, the metal | `eof` | north to a corner (10228,15654), east to (10312,15654), north to (10312,15308), east to (10396,15308), north to `bc2`'s pad (10395,15087) (ring, bright centre in both chips, hole) | `follow.py 10224 15720 N`; `textmap.py 10195 15630 10345 15700 3`, `10285 15285 10425 15330 3`, `10366 15055 10430 15120 3`; `tl5_tracks.py v 10312 15320 15640`, `v 10397 15100 15300` (bars of 8-12 px: `bc2`'s rows, which its notes say pass under x 10310 without contact; no hole); overlay `ovg1.png` |
| the follower's candidate (10258,15655) | - | a blemish: dark on chip 2's metal, a speck in the clean shot, absent from chip 1's metal and chip 2's stripped shot; the L lies on field | `b3.png`, `b4.png` (4x, four shots) |
| **link H**, the hop | `eof` | from `trunks`' pad (9770,18081) the poly runs west under the metals x 9640-9684 and 9716-9732 to a pad with a contact (9554,18081) | `d2.png`; `tl5_tracks.py rows row 9560 9765 5 18074 18081 18088`; `textmap.py 9530 18056 9590 18104 3 --acid` |
| **link H**, y 18083 | `eof` | metal west, straight, to a pad with a contact (8964,18081) | `follow.py 9500 18082 W`; `tl5_tracks.py h 18083 8975 9545`: no hole; `textmap.py 8936 18056 8996 18104 3 --acid`; `d1.png` |
| **link H**, poly north | `eof` | from that pad north (x 8955-8973) under four horizontal metals (y ~17822, 17862, 17905, 18040) and the through metal y 17781 (no hole) to a pad with a contact (8967,17735) | `d3.png` (1.45x), `textmap.py 8938 17700 8998 17800 3 --acid`; overlay `ovh1.png` |
| **link H**, x 8968 | `eof` | metal north from the pad, 2,470 px, over the rows of the gate columns; it passes through two pads with contacts, (8966,16737) and (8962,16172), and ends on a pad with a contact (8966,15260) | `follow.py 8966 17650 N`; `tl5_tracks.py v 8968 15270 17715`: bars under 16 px, clean-shot holes only at y 16174 and 16738 (a 105 px stretch at y 16544 is plain tan under the metal, no hole; chip 1 dim at y 17209-17234 over a wide poly band); `textmap.py` of each pad (`8930 16715 8996 16760`, `8930 16150 8996 16195`, `8938 15234 8998 15285`, all `3 --acid`) |
| **link H**, the west branch | `eof` | from the pad (8967,17735) a second metal runs west along y 17737 to a pad with a contact (8688,17737); the ring between its end and the pad's centre is 12 px, as on the north side | `g1.png` (4.8x, both metal shots); `px.py row 17738 8926 8980 2 metal,metal1`; `follow.py 8850 17738 W`; `tl5_tracks.py h 17737 8700 8940`; `textmap.py 8650 17705 8722 17765 3 --acid` |
| the four polys beyond their pads | nobody | each goes on west: y 16737 and y 16165 into repeated units of the gate column x 8650-8800 (pitch 565; `f1.png`, `f2.png`), y 15258 into the column's north part (`f3.png`), y 17732 west of x 8650 | drawn as stubs of 20-25 px; ports |

Not drawn, looked at (`c1.png`-`c3.png`): `trunks`' poly y 16940-16958 east of x 10470 runs on under two
thin metals into the unit under the rail x 10540-10585 and crosses it as a gate row.

### Piece `tcwa`: `inh_ck` is `inh_ck` (traced; wiring only)

```
inh_n  = NOT inh_src                    the driver of "line X" (bd1, trunks)
inh_ck = NOT inh_n                      the lone inverter of the input buffer row (inrow)
inh_ck                                   one net: this piece, lc2's piece, trunks' line S
ck_b   = NOR(ck_clkn, ck_g4, inh_ck)    the clock block (firm)
```

The full extraction has one net carrying `inh_ck` (the clock block's and `inrow`'s label),
`inh_ck`, with thirteen gates on it: the clock block's (`ck_b`'s NOR), the
inverter's own load, and the eleven that were known as `inh_ck`'s (`tl1`'s two latches and the
NOR `tl1_w3636`, `rcs_a2`'s NOR, `tl3`'s latches B and C and the NOR `tl3_e4243`, `tl4`'s NOR
`tl4_w4545`, `tcw`'s pair `fld_a_in` / `tcw_o3820`). `tools/unsure.py`: the labelled pieces of
`inh_ck` (then under three names) in `clock`, `inrow`, `eof`, `fld`, `lc2`, `tl3`'s foot and
`tl4` stay one piece when every uncertain item is deleted (the second piece it lists is
`tl1_w3594`'s, across `tl3`'s `?M` thin metal: AMB-033, as before). `inh_ck` is kept as the name
the net is shown under (an alias in `trace/eof.txt`; the rename is proposed in the handoff).

Believed, not traced: what this says about the signal. The net that stops the horizontal
counter's master clock is the net on whose two levels the vertical control's master/slave latch
pairs work (`tl1`'s pair, `tl3`'s latches B and C) and that opens the field latch path of `tcw`.
That is the pattern of a strobe that marks one moment of every scan line (the vertical logic
steps once per line), not of a rarely used inhibit. What `inh_src` is remains open: its line is
followed into the bottom-centre logic (`notes/blocks/trunks.md`, `bd1.md`).

| Stretch | Drawn by | What | Evidence |
|---|---|---|---|
| `fld`'s pad to the strip's south edge | `tl6` | the pad (6400,4005), poly, metal U1 with the pad (5757,5632) of `tl4`'s row, the poly along y 6065, the metal to the corner (6105,6066) and south to (6105,6350) | its notes; not re-read |
| **link E**, x 6105 | `eof` | one straight metal y 6350-7346, 13 px wide, over the rows of the crossing field; no pad | `tl3_thin.py 6098 6113 6350 7335 --thr 144 --min 8`: one 8 px bar; `tl5_tracks.py v 6105 6350 7335`: bars of 8-10 px (row edges), no hole in the clean shot; `follow.py 6105 6300 S` |
| **link E**, corner (6105,7346) and the run east | `eof` | the metal turns east and lies on `lc1_w7040`'s poly row (y 7334-7354) for 190 px; no pad, no hole | `textmap.py 6074 7306 6150 7376 3 --acid`; `tl5_tracks.py h 7346 6120 6300`: no bar, no hole |
| **link E**, corner (6298,7346) | `eof` | the metal ends at x 6305 and turns south; **it does not reach `lc1`'s pad (6341,7345)**: 20 px of open poly lie between its end and the pad's ring, with open ground below the row there; the vertical x 6292-6305 runs from under the row to y 7438 and bare ground follows to y 7540 (it is not the metal of `lc1`'s pad (6297,7561)) | `k1_corner.png` (4x, four shots); `textmap.py 6270 7318 6380 7374 3`, `6270 7330 6330 7600 3 --acid`; `lc1`'s tracer and reviewer read the same ("the metal x 6098-6307 separate from the pad") |
| **link E**, corners (6298,7432), (6430,7432) | `eof` | east on a second poly row (y 7426-7440), no pad; south at x 6420-6436 | `textmap.py 6360 7408 6470 7462 3`; `tl5_tracks.py h 7432 6310 6425`; overlay `ov_e.png` |
| **link E**, x 6430 with **the tap** | `eof` | south to y 8067; at (6427,7648) a pad with a contact: ring y 7627-7668 with a bright centre in both metal shots, a pitted box in the chip-2 stripped shot, a dull hole in a poly pad in the clean shot; the metal passes through the pad and goes on | `k2_x6431.png` (4x, four shots); `textmap.py 6392 7606 6476 7690 3 --acid`; `tl5_tracks.py v 6431 7445 8160`: otherwise bars only |
| the tap's row | `eof` | from the pad a poly row y 7640-7656 east under two dozen vertical metals, no pad on it, to x 7540, where it becomes a gate over a diffusion under the wide metal x 7550-7600 (below) | `k6_rowA.png`, `k6_rowB.png` (2.3x, clean and metal); `tl5_tracks.py rows row 6440 7700 6 7630 ... 7666`; `k3_rowend.png`, `k7_group.png` |
| x 6431, y 8067-8172, corner, to x 6450 | `lc2` | its `inh_ck`: the metal lies on latch C's data poly for 64 px without a contact (its Ambiguity 3) and turns east | `textmap.py 6398 8090 6500 8200 3`: one 6 px bar at the poly's top edge, no ring, no hole; an L |
| **link F** | `eof` | east along y 8172 to a corner (6559,8172); south on the poly that leaves the pad (6558,8127) of another net (the pad's own metal arrives from the north; 18 px of open poly between its ring and this corner); corner (6559,8367); east over five poly columns to x 6690 | `textmap.py 6515 8060 6602 8200 3 --acid`, `6521 8322 6608 8400 3`; `tl5_tracks.py h 8172 6450 6545`, `v 6559 8190 8355`, `h 8367 6575 6760`: bars only, no hole; `k4_stair_m.png`, `k5_nestW.png`; overlay `ov_f.png` |
| the staircase to the contact (7034,8535) | `trunks` | corners (6757,8366), (6757,8452), (6930,8452), (6930,8536); the contact | `follow.py 6330 7432 E` gives every corner from (6430,7432) to the end (7038,8536) as drawn; `tl5_tracks.py` on each piece: bars only; `textmap.py 6950 8506 7070 8566 3 --acid`: ring, bright centre, hole |
| line S to the inverter | `trunks`, `clock`, `inrow` | poly (7034,8535)-(7034,8797), the metal down the left bus field (x 6862, step at y 13331, x 6798), poly under the supply buses, metal, poly under nine bus lines, the bottom bus line y 18428 (three poly hops), the turn at x 10268, the link to L4 and L6, L4 east, poly, metal to the inverter's output (13849,18590) | read by its package at 1x (re-read item R4). Here, by text only: `eof_cchk.py` on its nineteen contacts: seventeen have a hole in the clean shot (red minus green under 25), the other two, (7034,8797) and (8382,18428), a dull hole beside the centre on a text map; the centre is bright (over 150) in both metal shots at fifteen and in one shot at four ((9777,18425): chip 2 91; (6798,17990), (8602,18428), (12849,18384): chip 1 124-132), which were not looked at further; `follow.py 7032 8826 S` gives the diagonal, the step at y 13332 and the end (6797,16176) as drawn. The follower's contact candidates and the clean shot's dips on the two long metals are crossings without a pad (trap 15: `textmap.py 6826 9680 6900 9740 3 --acid`, `6762 14500 6836 14596 3`), and three long green stretches (y 16530-16690, 16822, 17483) are damage on chip 1 only (chip 2's metal is whole: `textmap.py 6768 16500 6834 16700 5 --acid`). **Taps of line S in poly under neighbouring lines were not looked for (R4 stays open).** |

**The gate group at the tap row's end** (run 2's look; **traced in run 5: piece `g7700`, which corrects this paragraph**: rows 1 and 2 do not meet). `k7_group.png` (1.95x, metal and clean),
`k3_rowend.png` (2.7x, four shots): a wide vertical metal x 7550-7600 over a diffusion column
(x 7545-7610, y 7610-7810) crossed by three poly rows, y 7640-7656 (this row, `inh_ck`), y 7705-7725
and y 7765-7785 (both from the west), with a metal contact (7575,7680) on the diffusion between
the first two; east of the metal an outline x 7610-7660, y 7610-7740 in which rows 1 and 2 appear
to meet (a U: if so both gates are `inh_ck`, two fingers round the contact), a strip east at
y ~7800 and what looks like a load with a contact (7745,7780) under a second wide metal
x 7722-7770. So `inh_ck` is a gate there. Nothing of it is drawn.

### Piece `g7700`: the gate on `inh_ck`'s tap row (traced)

```
eof_w7818 = NOT( eof_w7777 AND (inh_ck OR eof_w7718) )        firm (tools/unsure.py --equations eof_w7818)
```

Four transistors (full extraction): the load 26/55 (gate and source on `eof_w7818`, drain VCC),
row 3's pull-down 70/19 between the output and the inner node, and two pull-downs 70/18 and 70/20
(gates `inh_ck`, `eof_w7718`) from the inner node to VSS, side by side with one source contact
between them. Traced: the equation, and that `inh_ck` is one of its inputs (the tap row of piece
`tcwa` is the gate's row 1: one poly from the pad (6427,7648)). Believed, not traced: nothing about
what the gate is for. With `inh_ck` high the output is NOT `eof_w7777`; with it low,
NAND(`eof_w7777`, `eof_w7718`).

| Part | What the photos show | Evidence |
|---|---|---|
| the rail | metal x 7552-7598, straight through the unit; **VSS**: it runs south to y 8555, where it widens east into the metal x 7600-7646 that `cdp3` labels `vss` (column 0's rail) | `t8.png` (0.52x, y 6600-9000), `t9.png` (2.4x, both metal shots, the widening); `textmap.py 7530 7596 7620 7836 3` |
| the column | diffusion x 7541-7611, y 7613-7820 under the rail: protected-diffusion colour between the rows from y 7620 to 7818, field (pink) above 7617 and below 7824 | the same text map (clean shot's column) |
| the contact | one, (7572,7684): a dark ring y 7671-7695 with a bright centre in both metal shots, specks in the clean shot; no ring in the other three diffusion pieces | the same text map; `t2.png` |
| rows 1, 2, 3 | poly bands under the rail at y 7638-7655, 7709-7727, 7767-7786 (protected poly, 8-A in the clean map) | the same text map |
| **rows 1 and 2 are apart** | each ends in a cap at x 7632 on a field island (x 7612-7636, y 7628-7745); the patch between the caps (7617-7632, 7667-7700) is field: clean shot 153/151/90 against 152/146/93 for the field east of the strap, chip-2 metal 161/137/83 against poly's 157/120/60; no poly joins them | `t4.png` (4x, four shots); `px.py col 7622 7604 7750 3 all`, `px.py row 7680 7596 7670 3 all` |
| the ring | a diffusion strip leaves the column north of row 1 (y 7613-7628), runs down a strap x 7637-7654 (edges at x 7635 and 7656; clean 159/126/90, chip-2 metal 157/135/91, blue 88-93: a narrow diffusion in the open, trap 28) and comes back to the column south of row 2 (y 7745-7757): the two pull-downs' drains are one node | the same two profiles; `px.py col 7646 7735 7792 3` (strap bottom y 7758, field to 7778) |
| row 3 | ends in a cap x 7605-7634, free; in series between the ring's node and the output node | `t6.png`, `t7.png` (4.7x); `px.py col 7622 7740 7800 3` |
| the output node, east | from the column a diffusion arm y 7803-7817 east to a vertical x 7643-7658 (y 7783-7854); its top continues east as the strip y 7783-7809 under the load plate to the VCC box; its foot lies under the tie box | `px.py row 7810 7596 7672 3`, `col 7651 7770 7872 3`, `col 7625 7788 7842 3`, `row 7795 7636 7790 3` (one dim line 4-6 px at the plate's west edge, no field between arm and strip) |
| the load | plate x 7666-7721, y 7761-7827 over the strip (edges under it at y 7781 and 7811); a tab down to a heavy-outlined box (7664-7690, 7832-7854), interior paler: the tie to the output node | `px.py col 7690 7745 7862 3`, `row 7770 7640 7730 3`, `col 7676 7812 7866 3`, `row 7842 7630 7712 3`; `t10.png` (3.2x, four shots) |
| VCC | a diffusion box x 7726-7773, y 7759-7808 (protected tan with specks) with a contact (7748,7779), ring and bright centre, under the wide metal x 7725-7775. **Called VCC from the load's orientation only**; the metal is not followed to a known supply | `px.py col 7748 7740 7820 3 metal,acid1b`; `t5.png` |
| the output node, west | a diffusion wire from the column's west edge (y 7803-7822) to a heavy-outlined box (7490-7518, 7805-7832) at the east end of a poly row y 7812-7831; the row ends west on a pad with a contact (7402,7822) | `t11.png` (3.4x, four shots); `px.py row 7818 7380 7560 3`, `col 7500 7780 7850 3`, `col 7520 7690 7850 3`, `col 7530 / 7536 7788 7842 3`, `col 7460 7700 7850 3`; `textmap.py 7376 7790 7436 7850 3` |

**The three wires.**

| Wire | Followed to | Evidence |
|---|---|---|
| `eof_w7818` (output) | pad (7402,7822); a thin metal x 7395-7407 north over rows 3, 2 and 1 (bars only) to a pad with a contact (7401,7606), no metal beyond; that pad's poly west along y 7596-7612 under the metals x 7309-7322 (row 2's) and x 7345-7362 without a contact, to a pad with a contact (7273,7606); a thin metal x 7266-7278 north for 690 px (over four rows of the crossing field at y 7420-7570, then over bare field from about y 7410) to a pad with a contact (7272,6912); **the pad's poly goes on north** towards a row y ~6862 (drawn to y 6875; `bw`'s crossing field, not followed) | `follow.py 7400 7818 N` (end 7403,7602), `7270 7560 N --gap 16` (end 7272,6910); `textmap.py 7372 7570 7436 7640 3`, `7228 7576 7300 7630 3`, `7243 7480 7300 7582 3`, `7237 6868 7309 6934 3`; `tl5_tracks.py v 7272 6930 7590` (bars of 8-13 px, no hole); `px.py row 7604 7285 7400 5`; `t18.png`, `t20.png` |
| `eof_w7718` (row 2) | west under the output's metal x 7401 and the metal x 7345-7362 (no ring) to a pad with a contact (7267,7736). **Two metals on the pad** (Ambiguity 14): one east along the row and north (corner (7315,7736)) to a pad with a contact (7313,7215), whose poly row leaves east along y 7203-7221 (drawn to x 7400); one south from the pad (x 7262-7274), which `follow.py` takes 2,160 px to (6514,8254) (not checked, drawn to y 7800) | `t14.png` (3.1x, four shots), `t19.png`; `textmap.py 7222 7696 7336 7800 3`, `7285 7180 7345 7240 3`; `follow.py 7290 7735 E --gap 16`, `7270 7780 N --gap 16`, `7270 7780 S --gap 16` |
| `eof_w7777` (row 3) | west across the crossing field, no pad, to x 6877, where the poly turns south (x 6878-6895) and joins the row y 7812-7830, which runs on west to `lc1`'s edge x 6450 and beyond. **`lc1_w7780` is another poly**: its row y 7770-7790 ends from the west on a pad with a contact (6815,7778) (pad's east edge x 6835; field to 6877), whose metal goes south (not drawn by anyone) | `t12.png`, `t17.png` (1.9x, three shots: the whole row), `t13.png` (3.7x, the pad), `t15.png` (4.2x, the corner), `t16.png` (2.4x, the row y 7820); `px.py col 6886 7752 7846 3 metal1,acid1b` (one poly from y 7770 to 7828), `row 7777 6830 6900 3`, `row 7800 6860 6912 3`, `row 7820 6444 6900 6`, `col 6660 7795 7845 3` |

### Piece `ff3`: the flip-flop that clocks `lc2`'s ripple counter (traced: a cell copy)

```
eof_w9332 = NOT( eof_w9255 AND lc2_w8475  OR  eof_w9505  OR  lc2_w8450 )      K1, master latch   depends (the clear's term: the cell's ?D)
eof_w9505 = NOT( eof_w9255 AND eof_w9472  OR  eof_w9332 )                     K2                 FIRM
lc2_w8475 = NOT( eof_w9472 AND ( eof_w9255 OR eof_w9505 ) )                   K3, slave latch    FIRM
eof_w9472 = NOT( lc2_w8475 AND lc1_w7170 AND ( eof_w9255 OR eof_w9332 ) )     K4                 depends (the cell's ?D beside K4's pad box)
```

(`tools/unsure.py --equations NAME`, full extraction; `lc2_w8450` is `lc2_w8907`, track B, through `lc2`'s
uncertain buried contact, as in `lc2`'s first flip-flop.) Nineteen transistors, the cell's.

**Traced.** The four gates are `lc2`'s toggle flip-flop again (`notes/blocks/lc2.md`, "The counter"): with
`c` = `eof_w9255`, the master pair K1/K2 is open while `c` is high and takes the slave's outputs crossed,
the slave pair K3/K4 is open while `c` is low: one change of state per pulse of `c`. **Its slave output is
`lc2_w8475`, the clock of `lc2`'s first flip-flop**: the copy's track C (the metal x 4553-4571 that carries
K3's output back to K1's row 2 and K4's top row) is one metal with the L-shaped piece that `lc2` drew from
the END pad (4648,9124) of its own clock's thin metal. So the three flip-flops are a ripple chain in this
order: this one (clock `eof_w9255`), then `lc2`'s first (clock `lc2_w8475`), then `lc2`'s second (clock
`lc2_w8298`); each changes on the falling half of the one before. All three are held clear together:
track A (`lc1_w7170`, low = clear, the slave's K4) and track B (`lc2_w8907` = NOT `lc1_w7170`, the
master's K1) run down from `lc2`'s flip-flop to this one's pads.

**Believed, not traced.** That the chain goes on: this copy's clock arrives exactly as `lc2`'s did, by an
L-shaped metal from the south on the track-C position, with a contact at about (4563,10080) where the next
unit's row-2 pad would be (the follower; not looked at). What the counter counts and what it is for:
nothing traced says. A guess to test, not a finding: a chain of five or so toggle stages whose last two
outputs go into an AND-OR-INVERT (`lc2_w9125`, selected by two other lines) is what the cursor blink
divider of R10 bits 5-6 (1/16 or 1/32 of the field rate) would look like.

| Part | What the photos show | Evidence |
|---|---|---|
| the copy | every outline of `@inst lc2_ff 0,780` on its feature in the clean shot and the chip-2 metal shot: the ten pads, the two output boxes, the four tie boxes, the node box west of K4, the load plates, the vertical poly x 4578-4596, the thin metals x 4604, 4648, 4889 and K3's output metal | `findcell.py 4600 8350 4990 9190 --min 0.5 --region 4400,9100:5400,10500 --layer acid1b --cell lc2_ff` (0.86 at 0,780); `d_ov1.png` (1.38x, both shots), `d_ov2_1.png`, `d_ov2_2.png`, `d_ov2_3.png` (2.5x, clean and metal); `railprof.py 4752 4798 9200 9860` (the stack = the master's + 780, to 2 px) |
| **track C is `lc2`'s clock metal** | the metal x 4553-4571 is unbroken from the corner (4562,9122) of `lc2`'s L to a pad with a contact (4563,9296) (bright centre in a dark ring in both chips, green hole x 4556-4570, y 9292-9304 in the clean shot), whose poly leaves east only (K1's row 2), and on to an END pad with a contact (4560,9776) (K4's top row); no metal south of y 9780 | `follow.py 4564 9200 S` (end 4561,9780), `4562 9200 N` (corner 4569,9126 -> E, end 4651,9124); `tl5_tracks.py v 4562 9130 9840` (dark only at the two pads' rings and two 9 px bars where the clear row passes under; holes 9298, 9775); `textmap.py 4540 9272 4592 9324 2 --acid`; `d_s1.png` (1.7x), `d_r1.png`, `d_r2.png` (3x, three shots) |
| the thin clock metal x 4641-4655 | from row 1's pad (4648,9254) to the END pad (4648,9905) through the pads of rows a and d ((4648,9428), (4648,9645)); no metal between `lc2`'s END pad (4648,9124) and this one's top pad (y 9140-9249 bare in both chips) | `tl5_tracks.py v 4648 9140 9960` (holes 9254, 9428, 9645, 9905; no metal 9140-9249 and from 9912) |
| **the copy's clock feed** | an L-shaped metal from the END pad (4648,9905) west along y 9897-9919 and south on x 4553-4575: one metal into the pad's ring, the same picture as the master's L 780 px up | `textmap.py 4540 9890 4664 9936 3 --acid` against `4540 9110 4664 9156`; `d_padA.png` (2.8x, three shots); `follow.py 4564 9940 N` (corner (4570,9908) -> E, end (4652,9905)), `S` (a contact candidate (4563,10093), on to a corner (4568,10520)) |
| K1's VSS node | **differs from the master**: a box x 4752-4800, y 9196-9242 under the rail with one contact at (4765,9211) (a pit in the clean shot, a ring in both metal shots); field between it and `lc2`'s K4 column (y 9175-9196). The finger east (y 9223-9242) and the tongue are as in the master | `d_top.png` (4x, four shots); `textmap.py 4744 9186 4900 9262 4 --acid` against the master's `4744 8406 4900 8482`; `px.py col 4776 9150 9260 4` |
| track A | one metal from `lc2`'s pad (4473,9038) to an END pad with a contact (4473,9818) (ring 9796-9813, hole 9819; no metal 9823-9899); the pad's poly leaves east only (K4's second row). Under it lie two stretches of another net's diffusion (x 4458-4495, y 9088-9250 and y 9570-9725: flat tan under the track; review round 7), with no contact: metal C-E in both chips, no ring, no hole. West of the rail the pad's row lies 8 px below the cell's (own strip y 9808-9827) | `tl5_tracks.py v 4475 9040 9900`; `textmap.py 4455 9212 4497 9258 3`, `4455 9690 4497 9732 3`; `d_padA.png` |
| track B | one metal from `lc2`'s end to (4518,10170); a pad with a contact (4517,9384) (ring 9361-9378, hole 9385), poly east only (the clear row y 9376-9392; pink field west of the pad); no other hole from y 8690 | `follow.py 4517 8690 S`; `tl5_tracks.py v 4517 8690 9380`, `v 4517 9200 9500`; `d_padB.png` (4x, three shots) |
| the rails | the west rail has the master's outline 780 px lower (x 4752-4802; wider, x 4741-4812, at y 9580-9718; x 4757-4808, then 4757-4820 from y 9825); the middle rail x 4924-4980; both run on south of y 9970 | `d_ov3_m.png` (1.65x, the whole piece on the metal shot) |
| under the rail east of box S | the field at (4781-4811, 9672-9732) is green in the clean shot where the master's is pink: the same outlines in both (a colour drift, trap 15), metal whole over it in both chips | `opendiff.py 4540 9180 4990 9990`; `textmap.py 4730 9660 4830 9750 3 --acid` against `4730 8880 4830 8970`; `d_mS_c.png`, `d_mS_m.png` (4.5x, copy beside master) |

### Piece `x1`: the reset NOR's inputs, a clear, and `rcs_x1`'s driver (traced; wiring only)

```
rst = NOR(lpstb_b, res_b)          lc1's gate 3                         (firm)
rst_n = NOT rst                gate 4                               (firm)
rst_a = NOT rst_n                gate 5: rst_a   (firm)
rst_b = NOT rst_n                gate 6                               (firm)
rst_c = NOT rst_n                gate 7                               (firm)
rcs_x1    = NOT lc1_w7170                gate 2: rcs_x1           (firm)
```

Traced: the four joins (each pad, each column and each metal read as below), and with them the
equations, which are `lc1`'s with the new names.

- **`rst` is high while RES and LPSTB are both low** (`res_b` and `lpstb_b` are the two
  pins buffered in the pin's sense, `notes/blocks/trunks.md`). Believed: this is the reset
  condition of the datasheet (RES low resets the chip only while LPSTB is low; with LPSTB high
  it is a test mode). The datasheet's wording was not re-read in this run.
- Its three buffered copies are high during that reset: `rst_c` (the clear of latch D, which
  makes `lc_step`, and of `lc2`'s latch C), `rst_b` (north on V4, turning east at y 6720: not
  followed) and **`rst_a`, which is `rst_a`: the clear of `tl5`'s latches a
  and b, of `tl4`'s latch (whose inverse is the 4-bit counter's line `c4l_l3`) and of `tl4`'s
  cross-coupled pair**. So those four are cleared by the reset and by nothing else.
- **`rcs_x1` is not a copy of the reset.** It is the output of gate 2, the column's separate
  inverter: `rcs_x1` = NOT `lc1_w7170`, and `lc1_w7170` arrives from the south on the thin metal
  T1, which leaves `lc1`'s strip at (5030-5046,8067) into `lc2`'s (claimed; not followed here).
  What clears the five latches of the step logic is therefore decided in `lc2`'s west gate
  cluster or beyond.
- **The pads are not the ends of three of the lines** (found by the review, round 2): `res_b`,
  `lpstb_b` and the reset copy `rst_a` each go on in poly below their pad and turn
  south-east into the diagonal poly bundle of `lc1`'s strip (`lc1`'s Not done: "the diagonal
  bundle's other nine lines"). So the NOR and the four latch clears are not all that these
  three nets reach: **where the two pin lines and this copy of the reset go beyond the gate
  column is open** (three lines of that bundle). `rcs_x1`'s pad is an end (open field below it).

| Stretch | Drawn by | What | Evidence |
|---|---|---|---|
| the bus to y 6350 | `tl5` (the pins' lines: `trunks`) | ten vertical polys; by x at y 6350: 5063 `tl5_w5936`, 5107 `rcs_x1`, 5150 `rst_a`, 5192 `res_b`, 5237 `lpstb_b` | their notes; not re-read |
| **five columns, y 6350-6740** | `eof` | straight, under nine horizontal metals (`slbus`'s and others), no pad; no line steps a track | `x1_survey.png` (1.17x, metal and clean, all traces); `tl5_tracks.py rows row 5040 5262 3` at thirty heights (every 14 px, y 6340-6744): the columns stand at x 5061-5067, 5103-5115, 5148-5154, 5190-5199, 5235-5241 at every height; `tl5_tracks.py v X 6350 6900` per column: only 6-7 px dips at the gaps between metals (trap 2), the same heights on several columns |
| **four pads** | `eof` | (5105,6761), (5147,6803), (5190,6845), (5237,6803): each a ring with a bright centre in both metal shots and a green hole 16-17 px across in the clean shot | `x2_pads.png` (2.1x, metal and clean); `eof_cchk.py`; `textmap.py 5050 6728 5260 6906 3` |
| **four metals to y 6905** | `eof` | from pad 1 the metal's head stands 6-9 px (the ring) west of the centre and runs south at x 5077-5089 (M_a, shifting 6 px west at y 6890); from pad 2 the same, south at x 5116-5128 (M_b); V2 (x 5185-5194) and V3 (x 5230-5242) hang straight from pads 3 and 4 | the same text map: nothing above either head, bright in both chips to y 6905; the image |
| **the polys below pads 2, 3, 4** | `eof` | pad (5147,6803): open poly x 5141-5160 south to y 6900, bending south-east at about (5150,6910); pad (5190,6845): poly under V2, x 5188-5203 to y 6884, x 5197-5209 at y 6900; pad (5237,6803): poly under V3, x 5232-5250 to y 6872, then bending east (x 5247-5266 at y 6884, about (5266,6900)) | the reviewer's `review-2/k_pads234.png` (4.4x, four shots), `j_bundle.png`; `textmap.py 5128 6812 5275 6918 3 --acid`; `px.py col 5146 6776 6916 10 acid` against `col 5104` (field below pad 1); overlay `ov_x1fix.png` (4x, both stripped shots) |
| the gate column | `lc1` | M_a = gate 2's output; M_b = gate 5's output; V2, V3 = the NOR's inputs | its notes ("followed to y 6840 / 6800 / 6844 / 6800": the pads' heights) |

The fifth line, `tl5_w5936` (= `tl3_w3982`, the net that holds `rcs_cond` low), has no pad: its
poly runs on south in the open at x 5056-5072, beside M_a, and from y ~6890 shifts east under
it (`textmap.py 5050 6728 5260 6906 3`, the clean shot's column x 5059-5083). Drawn to y 6880.
`lc1` does not draw a poly there.

### Piece `r4lat`: the lower half of the latch on R4's match gets its load (traced; the tie uncertain)

```
bd1_n1 = NOT( bd1_n2  OR  inh_lat AND rc_eq_r4 )        upper half (bd1's)         depends (bd1's tie of N1's load)
bd1_n2 = NOT( bd1_an AND inh_lat  OR  bd1_n1 )          lower half; load: r4lat    depends (the tie drawn here; bd1's ?D, ?P)
bd1_an = NOT rc_eq_r4                                   bd1's inverter A           FIRM
```

(`tools/unsure.py --equations NAME`, full extraction. `bd1_q`, the gate of `bd1`'s pull-down G4, is an alias of
`bd1_n2` since this piece; `tools/unsure.py` lists `bd1_n2` as two pieces joined only through the tie.)

**Traced.** The load of the lower half: one transistor, 30/55, gate `bd1_n2` (the band), between the VCC land
and N2. With it the lower half is a complete gate, and with the tie the pair is cross-coupled: while
`inh_lat` is high `bd1_n1` = NOT `rc_eq_r4` and `bd1_n2` = `rc_eq_r4`; while it is low each holds the other.
So the pair is **a transparent latch of R4's match, open while `inh_lat` is high** (`inh_lat` is a copy of
`inh_src`), as `bd1`'s notes believed from the layout.

**Believed, not traced.** That the tie is what the box is (next table, last row; Ambiguity 23): the
equations are the extraction's with the tie drawn uncertain. What the latch is for: nothing traced says
where either output goes (Not done).

**How it was read.** East of the ground rail (x 13826-13870) the ground is open, but for `bd1_n1`'s metal
(x 13954-13970) and the VCC rail (from x 13997). There the clean shot shows edge lines light and plain
features dark (Ambiguity 24; trap 28), which is why `bd1` found that "the two chips do not line up within
10 px": they do (the contact (13957,15740) is at the same place in all four shots, and chip 1's *metal*
shot shows what chip 2's shots show). So the open part is read from the chip-2 metal and stripped shots
and chip 1's metal shot, and the clean shot is used where metal protected it.

| Part | What the photos show | Evidence |
|---|---|---|
| **the load block** | under `bd1_n1`'s metal the clean shot has, top to bottom: poly (salmon, y 15632-15648), a dark line (15656-15660), the bright channel (233-243/148-175, y 15664-15680), a dark line (15688), 10 px of poly (15692-15700), pink field (from 15704): **the profile of the upper half's load 97 px above** (poly 15524-15556, line 15560-15564, channel 15568-15584, line 15592-15596, poly 15600-15604, field from 15612). East of the metal the same bands in three shots. The two strip edges and the block's foot are 6-9 px dark bars across `bd1_n1`'s metal at y 15657-15663, 15687-15690 and 15705-15708 in both chips (edges underneath; no ring, no contact) | `px.py col 13962 15520 15720 4 acid1b,metal1`; `px.py col 13984 15616 15716 4 acid1b,acid,metal`; `textmap.py 13864 15618 14008 15722 3 --acid`; `e_a1.png`, `e_a2.png` (4.5x sharpened, four shots) |
| the block's sides | west edge x 13936 (a dark line between the strip's end, tan, and the poly, 172/114/54 in the chip-2 metal shot), east edge x 13992 (a dark line, then the land's tan from x 13996): the same junction with the land as the upper half's strip | `px.py row 15676 13872 14004 4 metal,acid,acid1b`; `px.py row 15674 13976 14024 4` against `row 15578` |
| the VCC land | tan under the rail to y 15684, a dark line at 15688, pink field from 15696: `bd1`'s `D 14000,15567:14048,15687`, with its contact (14022,15668) beside the strip | `px.py col 14012 15640 15720 4 acid1b,metal1` |
| **the strip west of the block and the arm** | plain tan, blue 77-91, red minus green 15-40 (diffusion; the band's poly beside it is 160/110/55) at x 13920-13932, y 15665-15686, then south without a break at x 13912-13926 to y 15728; in the clean shot this open strip is a dark red-brown bar (trap 28) | `px.py col 13926 15626 15716 3 all`, `col 13918 15650 15740 3 metal,acid,metal1`, `row 15696` and `row 15706 13872 14004 4` |
| **the arm to N2 under the rail** | along y 15720 the chip-2 shots are tan from x 13880 to 13928 with the rail's edge line at x 13872-13876, and the clean shot is protected tan (198/178/138: diffusion, not the pink of field) from x 13860 to 13880 with its own margin line at 13884: every x is tan in one chip or the other. `bd1` has this link as `?D 13870,15705:13936,15728`; its top edge is at about y 15712 | `px.py row 15720 13860 13944 4 all`; `px.py col 13900 15626 15716 3 all` (dark 15704-15710, tan from 15713) |
| the band is not on the strip west of the block | at x 13926 the band ends at y 15648 and the strip starts at 15662; between them the clean shot is bright green (field) | `px.py col 13926 15626 15716 3 all`; `e_box1.png` |
| **from G4's block to the band** | poly without a break at x 13900 from y 15626 to 15650 in three shots (chip-2 metal 150-170/97-130/42-72, chip-2 stripped orange, clean shot red-brown). `bd1` has it as `?P 13896,15618:13908,15642`; drawn here without `?` | `px.py col 13900 15626 15716 3 all` |
| **the tie** (uncertain) | a box with a light centre (13890-13906, 15661-15678) and a heavy outline, in both metal shots and the chip-2 stripped shot; its centre is tan with blue 75-95 (not the green of the field island below it, 139/152/88); no metal over it. Above it 10 px of dark, then the band's west end; east of it 8-10 px of dark, then the strip; west of it its outline, a field strip (green in the clean shot the whole way from y 15640 to 15685), then the rail. In the clean shot the box does not read (Ambiguity 24) | `e_box1.png`, `e_box2.png` (5.8x, five shots); `px.py row 15671 13872 14004 3 all`; `px.py col 13900 ...`; overlay `e_ov1.png` (4.2x, chip-2 metal and stripped) |

Also looked at (not drawn; for `bd1`): **the strip of `bd1_k`'s pull-down is not joined to N1 from above.**
Between N1's west box (to y 15600) and the strip's top segment (from y 15634) the clean shot, protected
there by `bd1_an`'s metal, is pink field (x 13770-13800, y 15602-15630; `e_k2.png`, 4.4x). So the transistor
under `inh_src`'s gate is not a pass transistor from the latch's node N1; whether its top segment reaches
the ground diffusion under the rail (`bd1`'s `?D`) was not settled (`e_k1.png`, `e_k2.png`).

## Ports

The net is driven outside the package (by `rdp2`'s NOR). `in` marks the port beyond which the
driver lies; the other three lead to the loads.

| Name | Layer | Where | Direction | What |
|---|---|---|---|---|
| `rc_eq_r4` | poly | (13420, 9654-9672) | in | from `mrach`'s poly row (its file ends it at x 13425) |
| `rc_eq_r4` | metal | (13641-13659, 10705) | to loads | track L7, on into `rdp3`'s piece (`rc_eq_r4`) |
| `rc_eq_r4` | metal | (13729-13747, 13475) | from `rdp3` | track L9, `rdp3`'s end |
| `rc_eq_r4` | metal | (13729-13747, 14695) | to loads | track L9, on into `bd1`'s track k15 (`rc_eq_r4`) |

| `sl_eq_r5` | poly | (8352, 4709-4729) | in | `cdp1`'s row y 4719 (its file ends it at x 8340) |
| `sl_eq_r5_n` | poly | (8348, 4840-4862) | out | the inverter's output, onto `tc2`'s poly from the pad (8290,4850) |
| `vss` | metal | (8399-8469, 4700) and (8399-8469, 4880) | - | slice 0's VSS rail, on north and south |
| `vcc` | metal | (8595-8645, 4700) and (8595-8645, 4880) | - | slice 0's VCC rail, on north and south |
| `sl_eq_r5_n` | poly | (5183, 2542-2560) | in | link C's east end on `r9m`'s corner (5175,2550); the net is `sl_eq_r5_n` |
| `sl_eq_r5_n` | poly | (4962, 2542-2560) | to loads | link C's west end on `tl4`'s row (4967,2551) |
| `sl_eq_r5_n` | metal | (4255, 2506-2518) | in | link D's east end on `tl4`'s bus line 1; the net is `sl_eq_r5_n` |
| `sl_eq_r5_n` | metal | (3528, 2505-2519) | to loads | link D's west end on `tl2`'s metal (3533,2509) |

| `inh_ck` | metal | (6098-6112, 6345) | to loads | link E's north end on `tl6`'s metal (6105,6350) |
| `inh_ck` | metal | (6422-6438, 8072) | in | link E's south end on `lc2`'s piece (`inh_ck`, M 6431,8067); the driver (`inh_ck`'s inverter) lies beyond |
| `inh_ck` | metal | (6445, 8165-8179) | to loads | link F's west end on `lc2`'s end (6450,8172) |
| `inh_ck` | metal | (6695, 8360-8374) | in | link F's east end on `trunks`' line S (its end x 6690): the net is `inh_ck` |
| `rcs_x1` | poly | (5097-5117, 6345) | to loads | from `tl5`'s bus line x 5107 |
| `rcs_x1` | metal | (5070-5090, 6905) | in | onto `lc1`'s M_a (`rcs_x1`, gate 2's output) |
| `rst_a` | poly | (5140-5160, 6345) | to loads | from `tl5`'s bus line x 5150 (the clear of four latches) |
| `rst_a` | metal | (5116-5130, 6905) | in | onto `lc1`'s M_b (`rst_a`, gate 5's output) |
| `res_b` | poly | (5182-5202, 6345) | in | from `tl5`'s bus line x 5192 (`trunks`' pad (5190,6065)) |
| `res_b` | metal | (5183-5197, 6905) | to loads | onto `lc1`'s V2 (`res_b`, the NOR's lower input) |
| `lpstb_b` | poly | (5227-5247, 6345) | in | from `tl5`'s bus line x 5237 (`trunks`' pad (5232,6105)) |
| `lpstb_b` | metal | (5229-5243, 6905) | to loads | onto `lc1`'s V3 (`lpstb_b`, the NOR's upper input) |
| `rst_a` | poly | (5141-5159, 6900) | to loads | the poly on south of the pad (5147,6803): into `lc1`'s diagonal bundle (bends south-east at about (5150,6910)) |
| `res_b` | poly | (5196-5210, 6900) | to loads | the poly on south of the pad (5190,6845), under V2, bending south-east: into `lc1`'s diagonal bundle |
| `lpstb_b` | poly | (5232-5248, 6872) | to loads | the poly on south of the pad (5237,6803), under V3; from here it bends south-east (about (5266,6900)): into `lc1`'s diagonal bundle |
| `tl5_w5936` | poly | (5053-5073, 6345) | ? | from `tl5`'s bus line x 5063 |
| `tl5_w5936` | poly | (5054-5072, 6880) | ? | on south beside M_a and under it (not followed) |

| `tl1_w5936` | poly | (2362-2386, 2506) | in | piece `r5nor`: from `tl1`'s row y 2498-2515; a gate of the NOR |
| `rcs_c1` | poly | (2405-2427, 2506) | in | from `tl1`'s poly (2405-2420,2500); a gate of the NOR |
| `sl_eq_r5_n` | poly | (2493-2515, 2506) | in | from `tl1`'s poly (2493-2508,2500); a gate of the NOR (the net's first load) |
| `tl1_w2637` | poly | (2452-2472, 2506) | out | the NOR's output, onto `tl1`'s poly (2448-2463,2500) |
| `vss` | metal | (2596, 2347-2404) | - | the arm, into the VSS plane (`tl1`'s, not drawn north of y 2500) |
| `vcc` | metal | (2250-2590, 1900) | - | the supply plane over the strap's head, on north, east and west (`padring`) |

| `inh_src` | poly | (10218-10234, 15912) | in or out | piece `isrc`, link G: the pad under the north end of `trunks`' metal x 10225 |
| `inh_src` | metal | (10390-10402, 15083) | to a load | onto `bc2`'s pad (10395,15087): the clear of latch unit a |
| `inh_src` | poly | (9770, 18072-18090) | in or out | link H: from `trunks`' pad (9770,18081) |
| `inh_src` | poly | (8930, 16728-16746) | ? | the row west of the tap pad (8966,16737): into the gate column |
| `inh_src` | poly | (8930, 16163-16181) | ? | the row west of the tap pad (8962,16172): into the gate column |
| `inh_src` | poly | (8930, 15248-15266) | ? | the row west of the end pad (8966,15260) |
| `inh_src` | poly | (8650, 17722-17742) | ? | the poly west of the pad (8688,17737) |

| `eof_w7777` | poly | (6450, 7812-7830) | in | row 3, on west into `lc1`'s strip (cluster E's undrawn west half) |
| `eof_w7718` | poly | (7400, 7203-7221) | ? | the poly row east of the pad (7313,7215) |
| `eof_w7718` | metal | (7262-7274, 7800) | ? | the metal south of the pad (7267,7736) |
| `eof_w7818` | poly | (7272-7285, 6875) | out | the poly north of the pad (7272,6912), towards a row y ~6862 |
| `vss` | metal | (7552-7598, 7585) and (7552-7598, 7860) | - | column 0's VSS rail, on north and south |
| `vcc` | metal | (7725-7775, 7720) and (7725-7775, 7860) | - | the wide metal east of the load, on north and south |

| `lc2_w8475` | metal | (4553-4575, 9190) | out | piece `ff3`: the copy's slave output on track C, onto `lc2`'s L-shaped metal (its port there, `in`): the clock of `lc2`'s first flip-flop |
| `eof_w9255` | metal | (4553-4575, 9990) | in | the copy's clock: the L-shaped metal from the END pad (4648,9904), on south (the next unit's track-C position; the follower: a contact near (4563,10080), on to y 10520) |
| `lc1_w7170` | metal | (4466-4484, 9060) | in | track A, on from `lc2`'s drawn end; it ends on the copy's pad (4473,9818) |
| `lc2_w8907` | metal | (4508-4526, 8700) | in | track B (the clear), on from `lc2`'s drawn end |
| `lc2_w8907` | metal | (4508-4526, 9420) | ? | track B runs on south past the copy's pad (the follower: to (4518,10170)) |
| `vss` | metal | (4757-4808, 9190) and (4757-4820, 9970) | - | the west rail, from `lc2`'s end and on south |
| `vcc` | metal | (4924-4980, 9190) and (4924-4980, 9970) | - | the middle rail, from `lc2`'s end and on south |

| `bd1_n2` | diffusion | (13868, 15712-15728) | out | piece `r4lat`: the load's node onto `bd1`'s N2 under the ground rail (inside `bd1`'s region; `bd1` has the link as `?D`) |
| `bd1_n2` | poly | (13895-13909, 15618) | in | the poly from `bd1`'s gate G4 block (the net it called `bd1_q`) down to the band and the load's gate |
| `vcc` | diffusion | (14004, 15659-15689) | - | the load's strip onto `bd1`'s VCC land (x 14000-14048, contact (14022,15668)) |

## Ambiguities

1. **`rdp3`'s contact (13736,12826)**, the top of L9 on the east pad of its poly link (not this
   package's geometry; the join rests on it). Both metal shots show a bright centre in a dark
   ring and the metal ends on the pad (`c_l9top.png`, 3.1x, four shots), which is what a contact
   at a line's end looks like (traps 12, 14). But the clean shot shows no green hole in the pad:
   its centre is orange-red (red minus green 80-100, text map `textmap.py 13540 12805 13765 12848
   3`), where the west pad of the same link (13565,12826) has the usual dull hole
   (`c_l5bot.png`). Readings: (a) a contact whose hole looks different in chip 1's stripped shot
   (residue); (b) no contact, which would leave L9's top and the poly link's east end as two free
   ends on one pad. Working assumption: (a), as `rdp3` drew it. What would settle it: the pad in
   `acid1` (chip 1's other stripped shot), or an independent reader.

2. **`cdp1`'s thin metal x 8501-8517 over the inverter's tie box** (8508-8538, 4783-4815). The
   metal (the data line of R8's slice 0, drawn by `cdp1` as one line from y 3382 to its contact
   (8509,4940)) is dark from y 4780 to 4815 in both metal shots, with a half-bright patch at
   y 4795-4798 on chip 2 only, and the clean shot is greenish under it there (a strip 9 px wide
   and 28 tall, not a round hole): `textmap.py 8484 4762 8600 4875 3 --acid`. That is the look of
   a thin metal over a box (traps 22, 26, 27): no widened pad, no full-bright centre in chip 1.
   Readings: (a) it passes over; (b) it makes a contact with the node, which would short a data
   bus line to this inverter's output. Working assumption: (a), nothing drawn. By trap 27 the
   photos cannot show the metal continuous over the box either; that is `cdp1`'s item (handoff).
   `tools/follow.py 8620 4720 N` joins this thin metal to the VCC rail at y 4078-4086: a false
   path along bare ground that is as bright as the follower's threshold in chip 2
   (`textmap.py 8494 4062 8640 4100 3`: 9-B, where metal is C-E).
3. **The two buried contacts of `r5inv`** are read from heavy-outlined boxes: the node's west end
   (8358-8392, 4836-4864), which `tc2` read the same way at 4.3x in four shots, and the load's tie
   (8508-8538, 4783-4815), which lies half under the thin metal. Inside each box the edges of the
   poly and of the diffusion cannot be seen, so the rectangles in the trace are placed to overlap
   within the box. Drawn without `?`: for the tie, the tan column from the box down into the
   strip (`px.py col 8521 4772 4852 3`) and the box at the load's corner; for the west box, the
   poly row ending on it and the strip leaving it. What would settle either: nothing more in
   these photos.
4. **A nub on link C's top edge** at (5044-5065, 2530-2542), in both chips (a small loop in the
   chip-2 stripped shot), over field between the two metals: not drawn, no connection possible.

5. **The staircase of `inh_ck` lies on other nets' poly for four of its stretches** (trap 13):
   on `lc1_w7040`'s row (y 7346, 190 px), on a second row (y 7432, 130 px), on `lc2`'s latch C
   data poly (x 6431, 64 px, `lc2`'s Ambiguity 3) and on the poly of the pad (6558,8127)
   (x 6559, 200 px). At none is there a pad, a ring or a hole in the clean shot (the scans named
   in Logic), and at each corner the metal's end is separate from the neighbouring pad
   ((6341,7345): 20 px of open poly; (6558,8127): 18 px). Each corner shows a dark bar 6-9 px
   long where the row's edge passes under it; a bar that short between two bright stretches is
   an edge underneath, as on every row the same metal crosses. Working assumption: no contact
   at any of them; a contact at the first would join `inh_ck` to latch D's output.
6. **The join rests on `trunks`' line S**, 12,000 px that its package read at 1x in the metal
   shot (re-read item R4). Re-read here by text only (Logic, the last row of the table): the
   contacts, the corners and the long metals agree with its drawing; taps in poly were not
   looked for.
7. **The heads of M_a and M_b at their pads** ((5105,6761), (5147,6803)): the metal does not
   leave the pad in line but stands beside it, 6-9 px of dark (the ring) between the centre and
   the head. Read as joined: there is no room for a gap between two metals in 9 px, each head
   starts at its pad's height with nothing above it, and a metal that ends does so on a contact
   (traps 12, 14). What would refute it: a second pad at either head.

8. **Which supply the plane north of y 1963 is** (piece `r5nor`). It is named `vcc` because the
   NOR's load hangs from it (the load's gate is tied to the output side, the other end goes to
   the strap) and the pull-downs go to an arm of the plane that `tl1` follows to its rail R1
   (`vss`). The plane itself is not followed to a pad. What would settle it: `padring`.
9. **The two buried contacts of `r5nor`** (the tie box x 2497-2530, y 2303-2330, and the box on
   the band x 2444-2475, y 2438-2465) are read from heavy-outlined boxes with a light centre, in
   both metal shots and both stripped shots; inside a box the poly's and the diffusion's edges
   cannot be seen, so the rectangles are placed to overlap within it. Drawn without `?`: each
   box is at the end of a poly, the first on a spur of the output strip that goes nowhere else,
   the second where the net `tl1_w2637` would otherwise have no driver and the NOR no exit.
10. **The load's gate as one block.** Three poly-coloured stripes (x 2436-2446, 2453-2475,
   2481-2526) with dark lines between them at x 2449 and 2478 are read as one poly over a strip
   whose edges are those lines (the strip comes out below the block at exactly x 2450-2478).
   The other reading, three polys side by side, has no poly leaving the west one or the middle
   one. Sizes only: the load is on the output strip either way.
11. **A pale half-dome** at (2250-2300, 2455-2495) in the clean shot only (`s6.png`): nothing in
   either chip-2 shot. Not drawn.

12. **The west metal at the pad (8967,17735)** (piece `isrc`). Two metals reach the pad's ring, from the
   north and from the west. Both are read as joined (tracing guide, trap 16): the dark stretch between
   each metal's end and the bright centre is the same 12 px (the trap's unjoined case measured 24
   against 10), and the west metal ends on the ring, not short of it. If the west one were separate,
   its pad (8688,17737) and poly would be another net.
13. **`inh_src`'s driver is not on what is drawn.** Three gates are on the net; the four stubs and the
   row of `trunks`' third end all lead into undrawn gate columns. Until those are traced, "every end
   is a gate" is known only for `bc2`'s clear and for the row at x 10540-10585 (seen, not drawn).

14. **Row 2's pad (7267,7736) has two metals** (piece `g7700`): one arrives from the east along the
   row, one from the south. Both are read as joined (trap 16): the dark ring between each metal's
   end and the pad's bright centre is 8-10 px on the east side and 10-12 px on the south side in
   both chips (`textmap.py 7222 7696 7336 7800 3`), each metal ends centred on the pad, and
   `follow.py 7270 7780 N --gap 16` ends on the pad's centre. If the south metal were separate it
   would be a net of its own that ends beside the pad.
15. **The wide metal x 7725-7775 is called VCC from the load's orientation only** (piece `g7700`):
   it was not followed to a labelled supply. `bw`'s notes describe the same metal (its line
   `rc_stepreq_n` runs under it north of y 7649).
16. **`cdp3`'s column-0 VSS rail is drawn where there is no metal** (not this package's geometry):
   `trace/cdp3.txt` has `M 7623,8450 y11200 w=46`, but from y 8450 to 8555 the ground at
   x 7600-7646 is bare; the rail there is the metal x 7552-7598 drawn here, which widens to
   x 7550-7645 at y 8555 (`t9.png`). Geometry only: both are `vss`.

17. **The three joins of the ring and the T's arm to the column at x 7600-7611** (piece `g7700`): the
   rail's east edge line lies over each junction in every shot, so that the top strip (y 7613-7628),
   the bottom strip (y 7745-7757) and the arm (y 7803-7817) are continuous with the column rests on
   their edge lines running through to it (tracer and reviewer). If one were cut the gate would have
   no path there; drawn without `?`.

18. **The copy carries the cell's four uncertain diffusions** (piece `ff3`): the column's run west of the
    rail at K1 and K2 (`?D`, three items; they only widen channels, and at K1 carry the clear's pull-down)
    and the 14 px strip beside K4's pad box (`?D`; K4's node to its load). They were not read again at the
    copy beyond the overlay (`d_ov2_1.png`, `d_ov2_3.png`: the copy shows what the master shows). So
    `eof_w9332`'s clear term and `eof_w9472`'s load rest on them, exactly as `lc2_w8552` and `lc2_w8692` do
    in the master (`notes/blocks/lc2.md`, Ambiguities). Settled when the master's are.
19. **The clear's identity at this copy rests on two long tracks read by text only.** Track A (760 px from
    `lc2`'s end to its END pad) and track B (680 px to its pad) were followed with `tl5_tracks.py` and
    `follow.py`, and seen at 1.7x from y 9100 south (`d_s1.png`); their stretch through `lc2`'s strip
    (y 8700-9100) lies beside `lc2`'s flip-flop, whose reviewers looked at that cluster but not at these
    two metals south of where `lc2` stops them. No hole and no ring on either between the pads.
20. **K1's VSS contact (4765,9211)** is read from a pit in the clean shot and a ring in both metal shots
    (`d_top.png`); the box around it is the only part of the copy that differs from the master. The
    finger of K1's third pull-down hangs from this box, so this one contact is what grounds K1's stack and
    its third pull-down.
21. **The cell's VCC contacts sit about 12-15 px north of where the cell draws them** (K1's: dimple at
    (4951,9349), drawn (4955,9360); the master's own is the same, (4953,8565) against (4955,8580)). Inside
    the box either way; geometry of `lc2`'s cell, not changed here.
22. **What lies in the copy's rectangle that the piece does not draw** (review round 7): (a) two stretches
    of diffusion under track A, x 4458-4495, y 9088-9250 and y 9570-9725, joined at y 9088-9118, 9215-9250,
    9570-9597 and 9700-9722 to the diffusion under the neighbouring metal x 4420-4440 (the reviewer: a
    diffusion wire of the west neighbour going round that metal's pads (4432,9183) and (4430,9655)); no
    contact to track A and no poly of this piece over it; its ends are not read (`urch`'s channel); (b) two
    VCC boxes under the middle rail, (4928-4985, 9195-9245) with a contact about (4950,9225) and
    (4932-4985, 9738-9800) with a contact (4955,9768): the turned flip-flop of column B's (`lc3`'s stage
    E4), drawn by `lc3`; (c) the green stripe at y 9730-9745, x 4800-4975 is in the chip-2 metal photograph
    only (an image artefact: not in chip 1's metal shot nor in either stripped shot).

23. **The tie of the lower half's load** (piece `r4lat`; box (13889-13913, 15660-15682)). Seen: a
    heavy-outlined box with a light centre at the west end of the band, in both metal shots and the chip-2
    stripped shot, with no metal over it: the look of a buried contact (`notes/layers.md`). Not seen:
    the poly from the band into the box (10 px of dark outline between, y 15650-15660) and the diffusion from
    the strip's end into it (8-10 px of dark, x 13908-13916); and the clean shot, which settles other boxes,
    does not show this one as a box (Ambiguity 24). Readings: (a) a buried contact of the band's poly onto
    the west end of the strip, the load's tie: `bd1_q` = `bd1_n2`, the latch closes; (b) the box's diffusion
    is not the strip's, which would leave the band (the gate of G4 and of this load) with no driver at all,
    and the box with a diffusion that goes nowhere (field west of it, the field island south). Working
    assumption: (a), drawn `?B` with `?P` and `?D` inside it, the names gathered by `@alias bd1_n2 bd1_q`
    (not renamed: trap 17). It is the mirror of the upper half's tie, which `bd1` drew uncertain for the
    same reason. What would settle it: a sharper photograph; nothing more in these.
24. **In the open ground east of `bd1`'s ground rail the clean shot is inverted against the other three
    shots** (x 13885-13950, y 15625-15700): where the chip-2 shots and chip 1's metal shot have a dark edge
    line (x 13908-13916, 13932-13936) it is light tan, and where they have the box's light centre and the
    plain strip it is near black or dark red-brown (`px.py row 15671 13872 14004 3 all`). It is not a
    registration error: the island below (y 15686-15701), the band's west end (x 13894) and the contact
    (13957,15740) are at the same place in all shots. Trap 28's case (a diffusion strip in an open gap reads
    as open poly in the clean shot), here for a whole group. Nothing in the piece rests on the clean shot in
    the open; under `bd1_n1`'s metal and beside the rails it is the main evidence.
25. **`bd1`'s uncertain items on this latch that the piece re-read**: `?P 13896,15618:13908,15642` (poly in
    three shots: drawn here without `?`, over it) and `?D 13870,15705:13936,15728` (diffusion in both chips:
    drawn here without `?`, over it). `bd1`'s other uncertain items there were not re-read: the upper
    half's tie, N2's third pull-down (`?D`, `?P` at x 13919-13986, y 15720-15833; its outlines are as `bd1`
    describes in `e_s2.png`, 3.8x chip-2 stripped), the source of `bd1_k`'s pull-down.

## Review

**Round 1: full review** (2026-11-19 00:05 +0000; one fresh reviewer agent on Claude Fable 5.2, read
from the photos alone; trace at commit 576ed4d; its images in `cache/scratch/eof/review-1/`, 22
used). Pieces: `r4`, `r5inv`, `r5w`.

Told to suspect: the pad at L2's top and the row under the metal x 13391; a contact from the bar
y 9925 onto any of the four metals over it (the ring-like spot at (13605,9924)); taps or track steps
on L2's piece, L7 and L9; `rdp3`'s contact (13736,12826) with no green hole; in `r5inv` the load's
tie and its tab, the thin metal over the tie box and the strip, the west box, the gate arm's east
end, a second pull-down or another poly on the node strip, which rail is which, the C's join to the
row y 4719; in `r5w` whether link C is one row, contacts under the wide metals, link D's pads and the
metal east of them.

Checked and found correct (4.8-6x in two or more shots, text maps, profiles, the follower):
- `r4` link A: the three pads (ring with bright centre in both metal shots, green hole in the clean
  shot); the row under x 13391 and the bar under its four metals plain poly with no hole; the spot at
  (13605,9924) on chip 2 only; L2's piece and L7 straight with no tap. Link B: straight, no pad or
  step; the row at y 13893 ends on a pad of the track x 13782, not on this metal; dark spots at
  y 13487 and 14222 on chip 2 only. `rdp3`'s stretch: the two jogs and the end as drawn, its contact
  candidates chip-2 blemishes. **`rdp3`'s contact (13736,12826)**: the metal ends on a rounded pad
  with a ring and bright centre in both metal shots and a pale patch in the chip-2 stripped shot; the
  clean shot has a mottled red centre and no green hole; read as a contact (Ambiguity 1 stays as an
  assumption with two readers agreeing).
- `r5inv`: the C continuous with the row y 4719; the arm ends at x 8473 with field at x 8482-8494;
  one pull-down only, no other poly on the strip; the west box and the tie box heavy-outlined in both
  chip-2 shots, the diffusion running into each in the clean shot (tab tan y 4790-4840 at x 8521);
  the thin metal with no pad, no bright centre in chip 1, no green hole, bright over the strip: no
  contact, within trap 27's limit; both rails continuous north to `shm`'s `vss` and `vcc` pieces.
- `r5w`: link C one row, no hole under either metal; link D's pads both contacts, the bar plain under
  the wide metal, the metals straight with no tap.
- Extraction: 0 errors, the claimed equations; `tools/unsure.py` lists none of these nets.

Findings, both geometry only, both confirmed by the tracer and fixed:
1. **The load's gate was drawn too long** (`P 8534,4783:8592,4872`, L 58). Over the strip the poly's
   west edge is x 8550: `px.py row 4836 8518 8600 3`: chip-2 metal blue 82-94 at x 8527-8545
   (diffusion) against 52-76 at x 8554-8587 (poly), dark edge at x 8548-8551 in the metal and stripped
   shots; `px.py row 4864`: field (green over red) at x 8532-8544, poly from x 8556; and at y 4807 the
   pocket x 8540-8548 is field. The arm to the tie box is only the block's top, y 4785-4801. Now
   `P 8550,4783:8590,4872` and `P 8508,4785:8554,4801`: W/L 38/40. Same transistor, same nets.
2. **The VSS rail was drawn too wide above the contact** (x 8399-8469 throughout). Its east edge is
   x 8444 at y 4721 and x 8466 from the contact's pad down (rows 4721, 4760, 4802, 4835, 4870 in both
   metal shots). Now a polygon, x 8399-8445 above y 4742. No contact involved.

Proof that the fixes changed no connection (commit before the fixes: 576ed4d):

```
tools/t.sh eof sameconn.py 576ed4d             ->  connections identical
.venv/bin/python tools/sameconn.py 576ed4d     ->  connections identical
```

Not checked by the reviewer: `cdp1`'s row y 4719 east of x 8660 (the tracer looked at it at 2x in the
clean shot, `t2_row.png`); other packages' geometry on `sl_eq_r5_n` between the inverter and
(5175,2550); `bd1` south of y 14700; `mrach` west of x 13340.

Round 1: no findings that change a connection.

**Round 2: full review of run 2's two pieces** (2026-11-19 00:44 to 01:04 +0000; one fresh reviewer agent on Claude
Fable 5.2, read from the photos alone; trace at commit 9f99dc2; its images in
`cache/scratch/eof/review-2/`, 17 used). Pieces: `tcwa`, `x1`.

Told to suspect: in `tcwa` the corner (6298,7346) and whether the metal reaches the pad
(6341,7345), the dark bar between the horizontal and the vertical there, the other four corners,
a contact where the metal lies lengthwise on a poly (y 7346, y 7432, x 6559), the junction
(6559,8172) with the pad (6558,8127) and the follower's three contact candidates on x 6559, the
tap (6427,7648) and other pads on x 6430 and x 6105, the row y 7648 (a break, a pad, a second
row), a one-track slip in the nest of staircase metals; in `x1` a column stepping a track or
tapped by one of the nine metals, the heads of M_a and M_b beside their pads and the pairing of
pads and metals, the meeting with `lc1`'s four metals, a pad on the fifth line.

Checked and found correct (5x views in two or more shots, text maps, profiles, the follower):
- `tcwa`: the corner (6298,7346) is an L (the metal ends at x 6305; the 9 px patch at x 6313-6322
  is open-poly colour in both chips, 143/114/51 and 140/78/38, not metal 222/177/97; the dark
  line x 6308 unbroken y 7335-7410); the pad (6558,8127) is another metal's (9 px of open poly at
  y 8150-8156 in both chips, the horizontal's north edge line unbroken across x 6500-6570); the
  corners (6105,7346), (6430,7432), (6559,8367) and `lc2`'s (6431,8172) without ring or hole; the
  tap a contact on this metal, which goes on through it; x 6105 and x 6430 with bars of 12 px or
  less and no hole (a bare strip x 6120-6126 separates x 6105 from every pad east of it); x 6559
  with one 10 px dim stretch at y 8318-8327 beside a neighbour's pad (6600,8323), bare strip
  between; the tap row one band to x 7530, then a gate under the wide metal; y 8367 one straight
  metal from x 6560 to `trunks`' corner (6757,8367), the follower agreeing both ways. Full
  extraction: `inh_ck` one net, `lc1_w7040` separate, 0 errors.
- `x1`: the five columns straight at 35 heights, no pad or ring under the nine metals; the heads
  of M_a and M_b over field, ending at their pads' height (follower ends (5081,6758),
  (5122,6800)), bare ground between pad 1's ring and M_b's head, so the pairing is as drawn; all
  four metals reach y 6905 on `lc1`'s tracks (each dims 6-16 px and shifts about 6 px where a
  diagonal poly passes under: no ring, no hole); no pad on the fifth line; both equations.

Finding (one; it changes where wires leave the package, so it counts as changing a connection):
1. **Three of the four pad polys do not end on their pads.** The trace ended each column at its
   pad. Below the pads (5147,6803), (5190,6845), (5237,6803) the poly goes on south (open poly
   x 5137-5155, y 6824-6912; salmon under V2; salmon under V3) and bends south-east into `lc1`'s
   undrawn diagonal bundle. **Confirmed** by the tracer: `textmap.py 5128 6812 5275 6918 3
   --acid` (chip-2 stripped F at x 5143-5155 from y 6824 to 6917; clean-shot poly 6-9 under V2 at
   x 5188-5203, shifting to x 5197-5209 at y 6902, and under V3 at x 5233-5245 to y 6875, shifting
   east below); `px.py col 5146 6776 6916 10 acid` (red over green by 40-80 below the pad) against
   `col 5104` (field below `rcs_x1`'s pad); the reviewer's `k_pads234.png`, `j_bundle.png`.
   **Fixed**: three poly pieces added (`P 5147,6815 y6900`, `P 5194,6858 5195,6884 5203,6900`,
   `P 5239,6815 y6878`), three ports added, and the notes and `notes/operation.md` now say that
   the three nets go on beyond the gate column. The four joins and the equations are unchanged (`tools/t.sh eof sameconn.py
   9f99dc2` and `.venv/bin/python tools/sameconn.py 9f99dc2` both end `connections identical`:
   the extraction cannot see a port), overlay `ov_x1fix.png`.
   The method that misled: a column was taken to end where its pad and metal were found; the
   pad of a poly under a metal that carries on (trap 29's "a wire is not finished where it goes
   under a thin metal") was not looked below. Handoff, Re-read.

Not checked by the reviewer: where the three diagonals end; `trunks`' line S beyond (6930,8536);
y 7346 at x 6150-6260 other than by scan; `tools/unsure.py` for `rst`.

Round 2: one finding, fixed.

**Round 3: fix check of round 2's fix** (2026-11-19 01:08 to 01:17 +0000; one fresh reviewer agent
on Claude Fable 5.2; trace at commit cd291ee, changes since 9f99dc2; its images in
`cache/scratch/eof/review-3/`, 7 used; 4.2-5.3x in four shots, text maps, profiles). Checked: each
of the three added polys is poly, continuous out of its pad and on the feature, with field on
both sides and no touch on a neighbour; `rcs_x1`'s pad (5105,6761) is an end (plain field at
x 5097-5113 down to y 6900 in all four shots, the pad's outline closed at y ~6780); the fifth
line (x 5063) stays separate from the other four (20 px of field to `rcs_x1`'s pad; it lies
against M_a's edge only as metal over it, no contact; it starts to bend at y ~6880); both
`sameconn` runs against 9f99dc2 end `connections identical`; 0 errors, 0 warnings.

Findings, both geometry only, both confirmed by the tracer and fixed:
1. `rst_a`'s added poly was drawn x 5139-5155; the feature's edges are x 5140 and 5161 in both
   metal shots (`px.py row 6860 5130 5170 3 metal,acid`: dark at 5139 and 5160-5163). Now
   `P 5150,6815 y6900 w=18`. Same ends.
2. `lpstb_b`'s added poly ran 6 px past where the bend starts (salmon x 5232-5250 to y 6872; at
   y 6884 it has moved east), and the port's note put the diagonal at about (5259,6900) where it
   is centred about x 5266. Now `P 5240,6815 y6872 w=16`, the port at (5232-5248,6872).

Proof that these fixes changed no connection (commit before them: cd291ee):

```
tools/t.sh eof sameconn.py cd291ee             ->  connections identical
.venv/bin/python tools/sameconn.py cd291ee     ->  connections identical
```

Round 3: no findings that change a connection.

**Round 4: full review of run 3's piece** (2026-11-19 12:10 to 12:16 +0100; one fresh reviewer agent on
Claude Fable 5.2, read from the photos alone; trace at commit dcd8d8d; its images in
`cache/scratch/eof/review-4/`, 14 used). Piece: `r5nor`.

Told to suspect: whether the strip round the west side is diffusion joined at both ends (or poly, or
stops short, or goes on elsewhere); the box at the top of `tl1_w2637`'s poly (a buried contact or a
rounded end on field); the load as one block or several polys, its foot and tie box, a poly leaving
the block or box; whether the three gate polys end at y ~2402 or go on under the wide metal, and
whether `rcs_c1`'s top touches the west pad; the pockets beside the poly tops; a contact of the arm
onto the output strip or the west strip, the two VSS contacts, a second contact on the island, contacts
of the two thin metals onto the strap; the arm's join to the plane and the island's separation; a
one-track slip among the four polys at y 2500; anything undrawn at x 2250-2330 and x 2550-2600.

Checked and found correct (5-5.5x in two to four shots, profiles, text maps, the extraction):
- the west strip is diffusion, unbroken, joined at both ends (`px.py row 2318`, `col 2341`: chip-2
  stripped red minus green 13-23, chip-2 metal blue 86-99; constant tan under the arm); nothing leaves
  it west of x 2331 or south of y 2465;
- the box on the band is a buried contact (its centre in the chip-2 stripped shot 142/155/89, the tie
  box's 137/156/91; the gate polys orange);
- the load is one poly block (all three stripes poly at y 2265, the middle one brighter in the clean
  shot); foot, tie box and spur join; no poly leaves the block or the box or goes north under the island;
- the gate poly tops end at y 2400-2405 with field above; `rcs_c1`'s top stops about 5 px short of the
  pad, no poly lies on either pad; the pockets are field and the band's top edge is continuous across
  each gate;
- no contact from the arm onto the output strip or the west strip (a dim patch at (2345,2390) on chip 2
  only); both VSS contacts real; the island has exactly one contact; none from the two thin metals;
- the arm joins the plane at x 2565-2590 with no edge line in either chip; the island is separate
  (bare ground x 2548-2580 east of it, y 2154-2184 north of it);
- the four polys at y 2500 are straight, in order, each on `tl1`'s matching poly;
- nothing undrawn at x 2250-2330 or x 2550-2600; the half-dome of Ambiguity 11 is absent in chip 2;
- 0 errors, four transistors, the equation FIRM.

Findings, all three geometry only, all confirmed by the tracer and fixed:
1. **The west VSS pad's east edge** is x ~2430, not 2416: `px.py row 2380 2404 2440 3 metal1,acid1b`
   has the clean shot's dark line at x 2428-2431; the dark line at x 2410-2413 that the tracer took for
   the edge is the contact's ring. Now `D 2383,2362:2430,2398`.
2. **The east VSS pad's east edge** is x ~2565, not 2548 (`px.py row 2395 2540 2575 3`: dark at
   x 2561-2564 in the clean shot). Now `D 2520,2364:2565,2412`.
3. **The head** runs to x ~2572, not 2562 (`px.py row 1938 2552 2584 3`: dark at x 2570-2573), and the
   seven rings sit about 7 px east of the drawn contacts (`px.py row 1940 2256 2300 3 metal,metal1`: the
   first ring's centre at x 2283). Contacts moved 7 px east, the head and the plane piece widened.

Proof that the fixes changed no connection (commit before the fixes: dcd8d8d):

```
tools/t.sh eof sameconn.py dcd8d8d             ->  connections identical
.venv/bin/python tools/sameconn.py dcd8d8d     ->  connections identical
```

Not checked by the reviewer: which supply the north plane is (Ambiguity 8); the field under the arm at
x 2355-2380 and 2480-2510, which reads grey-green in the clean shot instead of pink (taken as field:
no outline in any shot; the chip-2 stripped shot shows only fringes there); the edges inside the two
buried-contact boxes.

Round 4: no findings that change a connection.

**Round 5: full review of run 4's piece** (2026-11-19 12:41 to 12:47 +0100; one fresh reviewer agent on
Claude Fable 5.2, read from the photos alone; trace at commit 7fe8566; its images in
`cache/scratch/eof/review-5/`). Piece: `isrc` (links G and H).

Told to suspect: whether the west and the north metal are both on the pad (8967,17735); whether the
metal x 8968 is one metal through its two tap pads and whether those are contacts; other taps, side
arms or a track step on its 2,470 px, the tan stretch at y 16490-16600 and the chip-1 dim stretch at
y 17209-17234; link G's corners, its end on `bc2`'s pad, contacts of x 10312 onto the rows it crosses,
anything else leaving its two pads; the three poly hops (straight, one poly, no contact from above);
a second poly or a metal running on at the pads (9554,18081), (8964,18081), (8688,17737), (8966,15260);
the direction of the four stubs.

Checked and found correct (4.8x in four shots, text maps, the two-chip metal test, a flank scan):
- the pad (8967,17735): both metals joined (bright to the pad's own edge, 12-15 px of ring, against
  16 px of ring and then bare ground on the east side where nothing arrives); south of it open poly,
  no metal; the metal y 17781 crosses with no ring and no hole;
- x 8968 one straight metal y 15260-17735, no break over 16 px but the pad rings, no side arm at
  +-13 and +-16 px in either chip, clean-shot holes only at the three pads; both tap pads contacts
  with the metal joined on both sides, their rows leaving west only; nothing north of the end pad;
  y 16478-16606 a wide diffusion band passing under without a ring; the chip-1 dim patch, the bars at
  y 15507-15539 and a chip-2 dark spot (8972,16692) pass-overs or blemishes;
- the pads (8688,17737), (8964,18081), (9554,18081): each metal ends on its pad, nothing runs on west
  of x 8964, no poly south there, the poly at (8688,17737) leaves west only;
- the three hops straight, one poly each, no contact at any crossing;
- link G: corners as drawn, the spot (10258,15655) a blemish over field, x 10312 without contact onto
  `bc2`'s rows and clear of the pad (10352,15385), the end on `bc2`'s pad (10395,15087) with nothing
  north of it;
- extraction: three gates on `inh_src`, 0 errors, not listed by `tools/unsure.py`.

Findings, all geometry or comments only, all confirmed by the tracer and fixed:
1. **No metal at y 15835-15907 on x 10226.** The trace had `M 10225,15880 y15914`; the stretch is the
   hop's open poly (`px.py col 10226 15878 15962 4`: 164/116/60 to y 15894, ring y 15898-15902, centre
   y 15906-15914, ring to y 15930, metal from y 15934). The line is removed; `trunks`' own metal, which
   is drawn 48 px too far north (to y 15886), still covers the contact (handoff).
2. The stub at the tap pad (8962,16172) was y 16158-16176; the row is y 16163-16181 (`px.py col 8940
   16150 16190 3 acid1b`). Moved.
3. Comments: the hop north of (8964,18081) passes under four horizontal metals, not three; the two
   metals over the east hop are at x 9640-9684 and 9716-9732. Corrected.

Proof that the fixes changed no connection (commit before the fixes: 7fe8566):

```
tools/t.sh eof sameconn.py 7fe8566             ->  connections identical
.venv/bin/python tools/sameconn.py 7fe8566     ->  connections identical
```

Not checked by the reviewer: where the four stubs lead; `bc2`'s unit; the metal x 10225 south of
y 16000. The chip-2 stripped shot is fringed at several pads, so the holes rest on the clean shot and
the two metal shots.

Round 5: no findings that change a connection.

**Round 6: full review of run 5's piece, read twice** (2026-11-19 13:18 to 13:30 and 13:21 to 13:30
+0100; two fresh reviewer agents on Claude Fable 5.2, each alone and from the photos alone, with the
same brief; trace at commit 0002b90. The first was started before the session was cleared and taken
for lost, so a second was started for the round; both finished. Images: `cache/scratch/eof/review-6/`
(18) and `review-7/` (16)). Piece: `g7700`.

Told to suspect (both): whether rows 1 and 2 are apart east of the rail and whether the strap is
diffusion (trap 28); the ring's two corners, its joins to the column, and the bottom strip against row
3's cap; the join of the T's vertical arm to the strip under the load plate, and of the arm to the
column; the plate's tab and tie box, and the plate's upper part; both metals on row 2's pad
(7267,7736) and the corner (7315,7736); the two buried contacts and the pads of the output route, and
the hop along y 7604 under the metal x 7309-7322; row 3's corner at (6886,7777)-(6886,7821) (one poly
or two in line, trap 34) and pads on the row y 7821; contacts of the crossing field's vertical metals
onto the rows; a second contact on the rail or anything else on the column (the follower's candidate
(7571,7756)).

Checked and found correct by both (4-7x in two or more shots, profiles, text maps, the extraction):
- rows 1 and 2 apart: the patch between the caps is field in both metal shots (chip 2 160/143/84,
  blue 85 against 58-65 on the caps; chip 1 145/115/80), in the clean shot (153/151/90) and in the
  chip-2 stripped shot (154/147/93); no vertical poly east or west of the caps;
- the strap is diffusion (chip-2 metal blue 80-92), the ring continuous (`px.py col 7644`, `col 7646`:
  no dark line from y 7616 to 7752; rows 7620 and 7751 unbroken into the rail's edge) and separate
  from the T (field at y 7764-7772); the bottom strip and row 3's cap share one 10 px dark band
  (width only);
- the T and the load's strip join: the dark line at x 7660-7668 is 9 px wide at rows 7790 and 7800, as
  the plate's edge alone at row 7772 (15 px at row 7822): no second edge, in both metal shots; the arm
  and the west wire run into the column (at row 7810 the column's edge line is absent, against 16 px of
  dark at row 7756);
- the plate, its tab and the tie box are one poly (three orange bands split only by the strip's edges),
  no other poly reaches the box, field south of it; the VCC box closed, one contact;
- one contact on the column, (7572,7684); the candidate (7571,7756) has no ring in chip 1 and no hole;
- both buried contacts; the pads (7402,7822), (7401,7606), (7273,7606), (7272,6912), (7267,7736),
  (7313,7215) each with a ring and a clean-shot hole, no metal beyond the output's four; the hop along
  y 7604 continuous poly in all three gaps (blue 50-58), no ring under either metal (a dark ring at
  (7338,7605) in the clean shot only);
- row 2's pad: both metals on it (the south ring's 12 px includes the pad's edge, no bare ground; the
  second reviewer: consistent with Ambiguity 14, not proof); the corner (7315,7736) joined;
- row 3: one poly round the corner (`col 6886`: one poly from y 7773 to 7827, both metal shots); field
  x 6841-6877 between it and `lc1_w7780`'s pad; no pad or tap on row 3 or on the row y 7821 (the
  clean shot's rings in the gaps are absent from the chip-2 shots and the metal shots: traps 2, 15);
- the rail unbroken to the widening at y 8555, onto `cdp3`'s `vss`;
- full extraction: the four transistors and the equation, firm.

Findings: none by the second reviewer. The first reported "no findings" with two notes:
1. A comment (geometry only; confirmed from its `b2.png`, `b3.png`, fixed): the thin metal x 7272 was
   described as running "690 px over the crossing field's rows"; from y 6930 to about 7410 it lies over
   bare field, and four rows cross it at y 7420-7570. The trace comment and the wires table now say so.
2. Outside the piece (not a finding on it): an undrawn poly lies under row 2's metal x 7308-7327 from
   y ~7250 to ~7428, with field between its top and the pad (7313,7215), and no contact onto the metal
   (`textmap.py 7296 7236 7340 7430 4`: no hole, no ring). No package draws it: Not done, handoff.

Proof that the comment fix changed no connection (commit before it: 0002b90):

```
tools/t.sh eof sameconn.py 0002b90             ->  connections identical
.venv/bin/python tools/sameconn.py 0002b90     ->  connections identical
```

Not checked, or weak: where the top strip, the bottom strip and the T's arm enter the column
(x 7600-7611) the rail's edge line covers the junction (Ambiguity 17; the first reviewer measured the
edge line absent at row 7810); the chip-2 stripped shot is unreadable at row 3's corner; the clean shot
sits about 5 px east of the metal frame here (the trace follows the metal frame); the row y 7821 under
each metal only at 2.7x (first reviewer); the wide east metal's supply (Ambiguity 15); the south metal
beyond y 7800; the poly north of y 6875.

Round 6: no findings that change a connection.

### Round 7 (full review of piece `ff3`; 2026-11-19 13:27 to 13:44 +0000)

One fresh reviewer (general-purpose agent, Claude Fable 5.2), at commit 8d0843b (the piece as shipped in
88bafbc, with main merged in). A first reviewer, started at 13:04, was stopped with the session after ten
minutes and never reported; its images are in `cache/scratch/eof/review-7/` and were not used. The round
was run again with a new reviewer, whose images are in `cache/scratch/eof/review-8/`.

**Told to suspect**: the join of track C to `lc2`'s L-shaped metal and the contact (4561,9296); a copy that
differs from its master (all round the twelve pads and along the four edges; the top, where `lc2`'s K4
ends, and the bottom); the box y 9196-9242 and its contact (4765,9211); the seven buried-contact boxes,
accepted at 2.5x; the green patch under the rail east of (4752,9688); tracks A and B, followed by text only;
bare ground between the pads (4648,9124) and (4648,9254); the L-shaped feed; the rails' outlines.

**Checked and found correct** (4x or more in two or more shots, with text tools): claim 3 (track C
unbroken from y 9120 to the pad (4561,9296); the L's arm enters the pad (4648,9124); the contact real, poly
east only; the END pad (4560,9776) with poly east only and nothing south; `lc2_w8475` FIRM); claim 6 (bare
ground y 9140-9235 on x 4641-4655 in both chips; the feed one metal with the END pad (4648,9904)); claim 2
(the box separated from `lc2`'s column by field; (4765,9211) a contact, no second one); claims 4 and 5
(tracks A and B continuous, no side arm, no other contact; A ends at (4473,9818); the pad (4517,9384) real,
poly east only; dark spots on A at y 9066-9080 and on C at y 9395-9412 are chip-2 dirt); claim 1 (copy
against master block by block in all four shots: differences only at the top edge, dirt and the
neighbour's boxes; all seven buried-contact boxes match at 4.5x in three shots; the green patch has the
master's outlines and no ring); claims 7 and 8 (rail cuts at 13 heights; equations identical, 0 errors,
19 transistors). **Not checked**: the cell's thin metals over boxes and its four `?D` (the master's);
track B south of y 9840.

**Findings**, each checked by the tracer:

1. **Undrawn diffusion under track A** at x 4458-4495, y 9088-9250 and y 9570-9725, joined to the
   diffusion under the neighbouring metal x 4420-4440; no contact to track A, and no poly of the piece
   crosses it. Does not change a connection. **Confirmed** (`px.py col 4475 9070 9270 10 acid1b,metal`,
   `col 4475 9550 9740 10 acid1b`: flat tan 200/177/137 under the track from y 9100 to 9240 and from 9580
   to 9710, pink 186/127/127 elsewhere; `px.py row 9150 4410 4500 6`: tan only under track A's width). It
   is a wire of the west neighbour (`urch`'s channel), with ends nobody has read: **not drawn**; recorded in
   the Logic table, Ambiguity 22 and Not done. The notes' "two greenish stretches (y 9233, 9709)" are its
   south ends: the row in the Logic table is corrected.
2. **Two VCC boxes with contacts under the middle rail** are not drawn: x 4928-4985, y 9195-9245 with a
   contact about (4950,9225), and x 4932-4985, y 9738-9800 with a contact (4955,9768). Does not change a
   connection of this piece. **Confirmed** (`px.py pt 4955,9225 4955,9768`: protected diffusion colour,
   metal over both); they are the VCC boxes of the turned copy in column B (`lc3`'s stage E4,
   `@inst lc2_ff 260,716 rot=180 o=4826,8810` on its branch: the cell's contacts (4952,9108) and (4955,8580)
   land at (4960,9228) and (4957,9756)), which `lc3` draws. Not drawn here; Ambiguity 22's "nothing found"
   corrected.
3. **Geometry only**: K4's row from track A's END pad is drawn (by the cell) at y 9800-9818; west of the
   rail the poly lies at about y 9805-9826 and met the pad box by 2 px. **Confirmed** (`px.py col 4510 /
   4640 / 4700 9792 9838 3`: edges at y 9806-9808 and 9826-9830). **Fixed**: an own strip
   `P 4478,9808:4700,9827` on the row from the pad, stopped short of the column, so the channel stays the
   cell's.

Connections before and after the fix:

```
tools/t.sh eof sameconn.py 8d0843b              ->  connections identical
.venv/bin/python tools/sameconn.py 8d0843b      ->  connections identical
```

Round 7: no findings that change a connection.

### Round 9 (full review of piece `r4lat`; 2026-11-19 14:45 to 14:59 +0000)

One fresh reviewer (general-purpose agent, Claude Fable 5.2), at commit 3b08008. Its images are in
`cache/scratch/eof/review-9/`. (There is no round 8: the number follows the image folder, since
`review-8` held round 7's second run.)

**Told to suspect**: the tie box (whether it is a buried contact, whether the band's poly enters it and
the strip's diffusion is in it, or whether it joins the ground diffusion to the west); the link to N2
under the rail's east edge; the strip's edges and the block's foot, taken from two columns; whether the
band and the block are one poly, and how far down the block reaches; the block's west edge against the
arm (a wider gate, or an arm of poly); the poly link from G4's block, taken from one column; anything
leaving east under the VCC rail or south of the block.

**Checked and found correct** (ten images at 4x or more, the rest `px.py` and `textmap.py`): claim 1 (poly
over the strip: orange in the open at x 13941, bright salmon under the metal, east edge x 13992; band and
block one poly: the band's lower edge exists at x 13926 and is absent at x 13941); claim 2 (the strip runs
tan onto the land with no edge at x 13996-14044); claim 3 (N2, link and arm one diffusion: the clean shot
tan under the rail to x 13880, chip 2 tan from 13880; the clean shot's dark line at x 13884 is also on the
field row y 15696, so it is the margin line); claim 4 (field between band and strip at x 13926; the strip
west of x 13934 is bare diffusion, the arm is not poly); claim 5 (the box looks like `bd1`'s firm buried
contacts in the same column; field west and south of it, the ground diffusion's edge at x 13872 visible in
the clean shot; the dark towards the band and towards the strip is one 10-12 px line each, no room for a
field gap; "still not followable through the outline, so `?` is right"); claim 6 (poly unbroken at x 13898
from y 15606 to 15648 in three shots; G4 crosses the rail's east edge without a field stripe); claim 7 (no
ring, pad or hole on `bd1_n1`'s metal at y 15630-15705); claim 8 (0 errors, 0 warnings, both equations;
`unsure.py` shows `bd1_n2` joined only through the tie); claim 9 (nothing east under the VCC rail, nothing
south of the block; `opendiff.py` finds nothing). **Not checked**: the tie beyond its look (the clean shot
is unusable there); `bd1`'s other uncertain items (the upper tie, N2's third pull-down).

**Findings**, each checked by the tracer; none changes a connection:

1. **Geometry only**: the strip's edge lines are centred on y 15658-15660 and 15688-15689 (drawn 15661,
   15687), the foot's lower edge on 15703-15704 (drawn 15702). **Confirmed** (`px.py col 13941 15650 15710 2
   metal,acid`: minima at y 15660 and 15688-15690, the foot's at 15704-15706; `col 13982 15652 15708 2
   acid1b,metal`: 15658-15660 and 15688-15690). **Fixed**: `D 13916,15659:14004,15689`,
   `P 13937,15644:13992,15704`; the load is 30/55.
2. **Geometry only**: the arm is a dogleg: x 13908-13927 at y 15690-15710 (drawn 13913-13930), the
   strip's west part above it x 13919-13934. **Confirmed** (`px.py row 15700 13900 13936 2
   metal,acid,metal1`: edge lines at x 13906-13908 and 13930-13932, tan 13912-13924). **Fixed**:
   `D 13908,15684:13929,15728`.
3. **Geometry only, `bd1`'s**: its band is drawn to x 13996 and ends at x 13993, 7-8 px short of the land's
   edge at 14001. Not this package's item; not changed (handoff). No connection: field between.

Connections before and after the fixes:

```
tools/t.sh eof sameconn.py 3b08008              ->  connections identical
.venv/bin/python tools/sameconn.py 3b08008      ->  connections identical
```

Round 9: no findings that change a connection.

## Not done

- **Task 2, the loads of `sl_eq_r5_n` (= NOT `sl_eq_r5`)**: one load is drawn (piece `r5nor`,
  the NOR that makes `tl1_w2637`), and the net's poly ends there. Not checked: taps along
  `r9m`'s, `tc2`'s, `tl4`'s, `tl2`'s and `tl1`'s stretches of it (each was read by its own
  package). Next on this path: what `tl3`'s latch A does with it (`tl4_w4590`, its enable's
  source, is reached only by the row (4250,2810): queue row `tl3` (continue)).
- The supply plane north of y 1963 (only a piece over the strap's head is drawn; `padring`), and
  the VSS plane between the arm and `tl1`'s rail R1 (`tlb`).
- **The gate at the end of `inh_ck`'s tap row is traced** (piece `g7700`); its three wires go on:
  (1) the output `eof_w7818`: the poly north of the pad (7272,6912), towards a row y ~6862 in `bw`'s
  crossing field; (2) `eof_w7718`: the poly row east of (7400,7212) and the metal south of
  (7268,7800) (the follower runs it to (6514,8254): unchecked); (3) `eof_w7777`: the row y 7821 west
  of x 6450, into the undrawn west half of `lc1`'s cluster E. Also undrawn there: `lc1_w7780`'s row
  from x 6450 to its pad (6815,7778) and that pad's metal south.
- An undrawn poly under row 2's metal x 7308-7327, y ~7250-7428 (no contact onto the metal; field between
  its top and the pad (7313,7215)): `bw`'s crossing field / `busL`'s northern part.
- The units below the gate in the same column (x 7460-7800, y 7860-8440; `cdp3` (continue)): the
  rail and the wide metal are drawn to y 7860 only.
- **`inh_src`'s source** (what `inh_ck` is): still open after run 4 (piece `isrc`). Where to go on,
  each a poly entering undrawn logic: (1) the row y 16737 west of (8930,16737) and (2) the row y 16165
  west of (8930,16167), into repeated units of the gate column x 8650-8800 (`bc1` column B / `bc3`);
  (3) the row y 15258 west of (8930,15257) (`bc1`); (4) the poly west of (8650,17732) (`bc3`); (5)
  `trunks`' poly y 16950 east of x 10470, a gate row of the unit under the rail x 10540-10585 (`bc4`);
  (6) `trunks`' Not done item 1, the two contacts (13565,15275), (13565,15190) in `bd1`. Other taps of
  the long stretches that `trunks` drew were not looked for (R4).
- **The ripple chain below piece `ff3`: taken by `lc3`** (Matt Godbolt's claim of 2026-11-19 13:17 +0000,
  split with this package: `lc3` draws the turned copy in column B, its stage E4, and the unit below
  both columns, x 4440-5450, y 9960-10580, from this piece's ports at y 9970-9990, and uses this piece's
  names). Leave them to `lc3`. As this run left them (task (d), the rest; all in `lc3`'s ground, x 4440-5450,
  y 9900-10750): (1) the copy's clock `eof_w9255` south of (4553-4575,9990): the next unit's track-C
  position, a contact near (4563,10080), a corner (4568,10520) east to about (4674,10510) (the follower,
  unchecked); `findcell.py 4600 8350 4990 9190 --region 4400,9100:5400,10500` gives `@inst lc2_ff 0,1561`
  at only 0.52, so that unit is not a plain copy: overlay it first, then read what differs; (2) the turned
  copy in column B, `@inst lc2_ff 322,796 rot=180 o=4795,8770` (score 0.70, centre (5117,9566)): not looked
  at; `lc2`'s second flip-flop's output `lc2_w9034` and its stack (`lc2_w9171`) lead into that column; (3)
  track B south of y 9420 (to (4518,10170)); (4) both rails south of y 9970.
- **The diffusion under track A** (x 4458-4495, y 9088-9250 and y 9570-9725; Ambiguity 22a): a wire of
  the west neighbour's, not drawn by anyone (`urch` (continue): the metal x 4420-4442 with pads (4432,8708),
  (4432,9186), (4430,9655)).
- **`lc1_w7170`, the input of the inverter that drives `rcs_x1`**: the thin metal T1 leaves
  `lc1`'s strip south at (5030-5046,8067), into `lc2`'s (claimed).
- **`res_b`, `lpstb_b` and `rst_a` beyond the gate column**: three lines of the diagonal poly
  bundle of `lc1`'s strip, entering it at (5150,6900), (5203,6900) and about (5266,6900)
  (`lc1`'s Not done: the bundle's other nine lines).
- `tl5_w5936`'s poly south of (5063,6880): beside and under `lc1`'s M_a, into `lc1`'s strip.
- `rst_b` (a buffered copy of the reset) north of `lc1`'s strip: V4, x 5288-5310, "turns east
  at y 6720" (`lc1`); `rst_c`'s branch north at x 5713 (followed by `lc1` to y 6365).
- The other five polys of `tl5`'s south bus (x 5365, 5412, 5453 and two more) south of y 6350.
- **Where the outputs of the latch on R4's match go** (task (e), the rest; all in `bd1`'s region). The
  latch is complete since run 7 (piece `r4lat`), and no wire is known to leave it: `bd1_an` ends on gate
  G6's pad (13768,15806) (khaki field west of the pad, `e_s2.png`); `bd1_n1`'s metal x 13957 ends on the
  contact (13957,15740), whose poly is the gate of N2's third pull-down; `bd1_n2`'s poly (the band) ends at
  the load block's east edge x 13992 beside the VCC land; south of the lower half (y 15840-15880) is open
  field as far as the dense group. Where to look, in order: (1) **N1's west buried contact**
  (13766-13802, 15572-15600) and its "dead-end" poly pad (13749-13799, 15575-15597) under `bd1_an`'s
  metal (`bd1`'s Ambiguities): a poly leaving that pad under a metal is the likely exit of `bd1_n1`;
  under `inh_lat`'s metal x 13706-13726 the clean shot is field at y 15559-15616 (`textmap.py 13640 15556
  13812 15616 3 --acid`), so not west at that height; (2) the source of `bd1_k`'s pull-down (the strip's
  top segment, x 13773-13830, y 15634-15660): not from N1 (field between, piece `r4lat`'s last
  paragraph), so `bd1_k` is not the latch's output through that transistor; (3) `bd1_k` itself south of
  (13521,16273) and the dense group y 15880-16125, where `h_eq_r0`, `ck_out` and `inh_n` meet (`bd1`'s
  Not done). Read this group in the chip-2 shots and chip 1's metal shot, not in the clean shot
  (Ambiguity 24).
- The rest of the slice-0 logic of `cdp1`'s channel around the inverter was not traced; the
  inverter's own rectangle (x 8330-8650, y 4700-4880) has nothing else in it.
