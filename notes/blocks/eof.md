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
  the bottom-centre logic. **One end is the clear of `bc2`'s latch unit a** (`bc2_w15087`, joined:
  `bc2_w15029` = NOT((`bc2_w14876` AND `bc2_w14955`) OR `bc2_w15000` OR `inh_src`)). The bus line
  west of the pad (9770,18081) feeds a 2,470 px metal x 8968 with three pads and a west branch,
  each on a poly that goes on west into the gate column x 8650-8800 (repeated units; not followed).
  The third end (the poly y 16950 east of x 10470) is a gate row of the unit under the rail
  x 10540-10585 (looked at, not drawn). **Every end seen so far is a gate; the driver is still open.**

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

The bundle left of the right datapath has tracks L0..L11 at x 13348 + 43.4 k.

## Logic

Wiring only. What the join gives (traced; equations from the full extraction):

```
rc_eq_r4 = NOR(r4c_b0_x .. r4c_b6_x)                 rdp2: high when the row counter equals R4
bd1_an   = NOT rc_eq_r4                              bd1's inverter A            (firm)
bd1_n1   = NOT(bd1_q OR (inh_lat AND rc_eq_r4))      upper half of bd1's latch   (depends on bd1's ? items)
bd1_n2   : pull-downs (bd1_an AND inh_lat), bd1_n1   lower half; its load is not traced (bd1)
```

`tools/unsure.py --equations`: `rc_eq_r4` FIRM, `bd1_an` FIRM, `bd1_n1` DEPENDS (on `bd1`'s
uncertain items, none of them on this wire). `tools/unsure.py` does not list `rc_eq_r4`: no
uncertain item lies on the path from the comparator's NOR to the two gates.

Believed, not traced (from `notes/blocks/bd1.md`): the two halves are a transparent latch of this
signal, open while `inh_lat` is high; `inh_lat` is a copy of `inh_src`, the signal that also
stops `ck_b` (`inh_ck`) and the row counter's step (`inh_rc`). So **what R4's match does at the
end of the frame goes through this latch**; the latch's lower half (its load, the driver of
`bd1_q`) and where `bd1_n1`, `bd1_n2` and `bd1_an` go are `bd1`'s untraced part (the queue's
`bd1`-`bd3` row).

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

**The gate group at the tap row's end (not traced).** `k7_group.png` (1.95x, metal and clean),
`k3_rowend.png` (2.7x, four shots): a wide vertical metal x 7550-7600 over a diffusion column
(x 7545-7610, y 7610-7810) crossed by three poly rows, y 7640-7656 (this row, `inh_ck`), y 7705-7725
and y 7765-7785 (both from the west), with a metal contact (7575,7680) on the diffusion between
the first two; east of the metal an outline x 7610-7660, y 7610-7740 in which rows 1 and 2 appear
to meet (a U: if so both gates are `inh_ck`, two fingers round the contact), a strip east at
y ~7800 and what looks like a load with a contact (7745,7780) under a second wide metal
x 7722-7770. So `inh_ck` is a gate there. Nothing of it is drawn.

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
| `inh_ck` | poly | (7530, 7640-7656) | to loads | the tap's row: on east it is a gate of the undrawn group under the metal x 7550-7600 |
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
| `inh_src` | metal | (10390-10402, 15083) | to a load | onto `bc2`'s pad (10395,15087): `bc2_w15087`, the clear of latch unit a |
| `inh_src` | poly | (9770, 18072-18090) | in or out | link H: from `trunks`' pad (9770,18081) |
| `inh_src` | poly | (8930, 16728-16746) | ? | the row west of the tap pad (8966,16737): into the gate column |
| `inh_src` | poly | (8930, 16163-16181) | ? | the row west of the tap pad (8962,16172): into the gate column |
| `inh_src` | poly | (8930, 15248-15266) | ? | the row west of the end pad (8966,15260) |
| `inh_src` | poly | (8650, 17722-17742) | ? | the poly west of the pad (8688,17737) |

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

## Not done

- **Task 2, the loads of `sl_eq_r5_n` (= NOT `sl_eq_r5`)**: one load is drawn (piece `r5nor`,
  the NOR that makes `tl1_w2637`), and the net's poly ends there. Not checked: taps along
  `r9m`'s, `tc2`'s, `tl4`'s, `tl2`'s and `tl1`'s stretches of it (each was read by its own
  package). Next on this path: what `tl3`'s latch A does with it (`tl4_w4590`, its enable's
  source, is reached only by the row (4250,2810): queue row `tl3` (continue)).
- The supply plane north of y 1963 (only a piece over the strap's head is drawn; `padring`), and
  the VSS plane between the arm and `tl1`'s rail R1 (`tlb`).
- **The gate group at the end of `inh_ck`'s tap row**: x 7540-7780, y 7600-7820 (Logic, piece
  `tcwa`): three poly rows over a diffusion column under the wide metal x 7550-7600, a contact
  (7575,7680), a load-like block with a contact (7745,7780); rows 2 and 3 arrive from the west
  at (7500,7735) and (7500,7775). `trace/eof.txt` ends the row at x 7530.
- **`inh_src`'s source** (what `inh_ck` is): still open after run 4 (piece `isrc`). Where to go on,
  each a poly entering undrawn logic: (1) the row y 16737 west of (8930,16737) and (2) the row y 16165
  west of (8930,16167), into repeated units of the gate column x 8650-8800 (`bc1` column B / `bc3`);
  (3) the row y 15258 west of (8930,15257) (`bc1`); (4) the poly west of (8650,17732) (`bc3`); (5)
  `trunks`' poly y 16950 east of x 10470, a gate row of the unit under the rail x 10540-10585 (`bc4`);
  (6) `trunks`' Not done item 1, the two contacts (13565,15275), (13565,15190) in `bd1`. Other taps of
  the long stretches that `trunks` drew were not looked for (R4).
- **`lc1_w7170`, the input of the inverter that drives `rcs_x1`**: the thin metal T1 leaves
  `lc1`'s strip south at (5030-5046,8067), into `lc2`'s (claimed).
- **`res_b`, `lpstb_b` and `rst_a` beyond the gate column**: three lines of the diagonal poly
  bundle of `lc1`'s strip, entering it at (5150,6900), (5203,6900) and about (5266,6900)
  (`lc1`'s Not done: the bundle's other nine lines).
- `tl5_w5936`'s poly south of (5063,6880): beside and under `lc1`'s M_a, into `lc1`'s strip.
- `rst_b` (a buffered copy of the reset) north of `lc1`'s strip: V4, x 5288-5310, "turns east
  at y 6720" (`lc1`); `rst_c`'s branch north at x 5713 (followed by `lc1` to y 6365).
- The other five polys of `tl5`'s south bus (x 5365, 5412, 5453 and two more) south of y 6350.
- For `bd1` (queue row `bd1`-`bd3`): the latch's lower half and where `bd1_n1`, `bd1_n2`,
  `bd1_an` go now decide what R4's match does.
- The rest of the slice-0 logic of `cdp1`'s channel around the inverter was not traced; the
  inverter's own rectangle (x 8330-8650, y 4700-4880) has nothing else in it.
