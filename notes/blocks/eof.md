# eof: the end-of-frame lead group (follow tasks; spots across the die)

Queue row `eof` of `notes/work-packages.md`: wires whose ends decide the end-of-frame sequence,
followed to their gates. Only what no other package draws is in `trace/eof.txt`; the rest of each
path is other packages' geometry, named where it is used. Coordinates are metal-shot pixels;
images are in `cache/scratch/eof/`.

## Status

Run 1 (Tom Seddon's session, Claude Fable 5.2; 2026-11-18 23:30 to 23:50 +0000).
Three pieces, 2 transistors, no uncertain items.

- **Task 1, where R4's match goes: done** (piece `r4`, wiring only). `rc_eq_r4` is drawn end to
  end from R4's comparator to its loads: it is the net that `rdp3` called `rdp3_n7s9` and `bd1`
  called `bd1_a`, **the data input of the latch in the gate column beside the strobe channel
  and the input of inverter A there**.
- **Task 2, where R5's match goes: its first gate found and traced** (piece `r5inv`): at the
  west end of its row in the central datapath's channel `sl_eq_r5` is the only input of an
  inverter that nobody had drawn, **`r9m_l1w` = NOT `sl_eq_r5`**; the output is the line that
  `r9m` and `tc2` had drawn without a driver. Piece `r5w` (wiring only) carries that line on
  west: `r9m_l1w` is `tl4`'s bus line 1 (`tl4_w2512`) and `tl1`/`tl2`'s `tl1_w2592`, which
  leaves the top-left strips north at (2493-2508,2500) into the band y 2180-2500 (package
  `tlb`, not drawn by anyone). **No load of it is drawn yet.**
- Tasks 3 and 4 of the queue row (`tcw_a`'s source; `rcs_x1`'s driver): not started.

Full extraction with this file: 2,357 nets, 4,232 transistors, 0 errors, 0 warnings; the package
by itself (it loads `rdp3`): 0 errors, 0 warnings.

## Inventory

| Piece | Where | What |
|---|---|---|
| `r4`, link A | x 13416-13667, y 9647-10705 | from `mrach`'s poly end (13425,9663): pad and contact (13433,9665), the upper piece of bundle track L2 (y 9652-9938), pad and contact (13432,9925), poly bar y 9916-9934 east under L3-L6, pad and contact (13650,9925), track L7 south to `rdp3`'s piece at y 10700 |
| `r4`, link B | x 13729-13747, y 13475-14695 | bundle track L9, straight, from `rdp3`'s end (13738,13480) to `bd1`'s track k15 (13738,14690) |

| `r5inv` | x 8330-8650, y 4700-4880 | an inverter in the slice-0 position of `cdp1`'s channel: C-shaped input poly (the west end of the row y 4719), pull-down under slice 0's VSS rail (contact (8431,4770)), node strip y 4824-4848 with a buried contact to the output's poly at its west end (box x 8358-8392), load block x 8550-8590 (an arm from its top west to the tie box) with its tie box x 8508-8538, y 4783-4815, VCC contact (8615,4838) |
| `r5w`, link C | x 4962-5183, y 2542-2560 | the poly row from `r9m`'s corner (5175,2550) west under rail RC and the supply metal x 4948-4997 to `tl4`'s row end (4967,2551) |
| `r5w`, link D | x 3528-4255, y 2494-2526 | `tl2`'s metal on to a pad with a contact (3606,2510), a poly bar under the wide metal x 3648-3760, a pad with a contact (3800,2510), a straight metal east to `tl4`'s bus line 1 at (4250,2512) |

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
r9m_l1w  = NOT sl_eq_r5                      this piece (firm)
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
  there the net is `r9m_l1w` (`tc2`'s piece 13 and `r9m`).
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
| to the band | `tl2`, `tl1` | `tl1_w2592`: the metal x 3503 / y 2598, the pad (2868,2596), the row y 2591, a poly north out of the strips at (2493-2508,2500) | their notes |

The full extraction has one net with the three names and no gate on it but the inverter's own
load: **where NOT `sl_eq_r5` is used is north of y 2500** (or at a tap nobody has drawn).

## Ports

The net is driven outside the package (by `rdp2`'s NOR). `in` marks the port beyond which the
driver lies; the other three lead to the loads.

| Name | Layer | Where | Direction | What |
|---|---|---|---|---|
| `rc_eq_r4` | poly | (13420, 9654-9672) | in | from `mrach`'s poly row (its file ends it at x 13425) |
| `rc_eq_r4` | metal | (13641-13659, 10705) | to loads | track L7, on into `rdp3`'s piece (`rdp3_n7s9`) |
| `rc_eq_r4` | metal | (13729-13747, 13475) | from `rdp3` | track L9, `rdp3`'s end |
| `rc_eq_r4` | metal | (13729-13747, 14695) | to loads | track L9, on into `bd1`'s track k15 (`bd1_a`) |

| `sl_eq_r5` | poly | (8352, 4709-4729) | in | `cdp1`'s row y 4719 (its file ends it at x 8340) |
| `r9m_l1w` | poly | (8348, 4840-4862) | out | the inverter's output, onto `tc2`'s poly from the pad (8290,4850) |
| `vss` | metal | (8399-8469, 4700) and (8399-8469, 4880) | - | slice 0's VSS rail, on north and south |
| `vcc` | metal | (8595-8645, 4700) and (8595-8645, 4880) | - | slice 0's VCC rail, on north and south |
| `tl4_w2512` | poly | (5183, 2542-2560) | in | link C's east end on `r9m`'s corner (5175,2550); the net is `r9m_l1w` |
| `tl4_w2512` | poly | (4962, 2542-2560) | to loads | link C's west end on `tl4`'s row (4967,2551) |
| `tl1_w2592` | metal | (4255, 2506-2518) | in | link D's east end on `tl4`'s bus line 1; the net is `r9m_l1w` |
| `tl1_w2592` | metal | (3528, 2505-2519) | to loads | link D's west end on `tl2`'s metal (3533,2509) |

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
clean shot, `t2_row.png`); other packages' geometry on `r9m_l1w` between the inverter and
(5175,2550); `bd1` south of y 14700; `mrach` west of x 13340.

Round 1: no findings that change a connection.

## Not done

- **Task 2, the loads of `r9m_l1w` (= NOT `sl_eq_r5`)**: the net's only undrawn end is the poly
  that leaves `tl1`'s strip north at (2493-2508,2500) into the band y 2180-2500 (package `tlb`).
  Not checked here: taps along `r9m`'s, `tc2`'s, `tl4`'s, `tl2`'s and `tl1`'s stretches of it
  (each was read by its own package).
- Task 3: `tcw_a`'s source: its thin metal comes from the north to the pad (6400,4005) (`tcw`);
  its row y 5631 crosses `tl4`'s strip and goes on south across y 6350.
- Task 4: the driver of `rcs_x1`: beyond `tl5`'s bus line x 5107 (the row y 5890).
- For `bd1` (queue row `bd1`-`bd3`): the latch's lower half and where `bd1_n1`, `bd1_n2`,
  `bd1_an` go now decide what R4's match does.
- The rest of the slice-0 logic of `cdp1`'s channel around the inverter was not traced; the
  inverter's own rectangle (x 8330-8650, y 4700-4880) has nothing else in it.
