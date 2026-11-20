# tl6: top-left random logic, the sixth strip (x 5683-6400, y 2500-6350)

Package `tl6` (part 6 of 6 of the top-left logic, the eastmost strip). Trace: `trace/tl6.txt`.
Views: `cache/scratch/tl6/`. The strip is a **track field**: vertical metal tracks at a 43.5 px
pitch, poly rows under them, pads. No gate and no diffusion has been found in it. Its job is
to carry the signals of `tl5`'s gate column (and of the strips west of it) to the gate column
`tcw`, to the crossing field in front of the island `tc1`/`tc2`, and south.

## Status

2026-11-18 03:21 +0000. **Traced: the strip's wiring in three pieces; no transistor** (none
found: the strip is a track field). Piece 1: the rows of all fourteen of `tl5`'s east ports to
their ends, the tracks U0, U1, U2 and the north pieces of U4 and U5, the bus metals y 4482 and
y 4787, `ral_stb`. Piece 2: the tracks U8-U11, the five undrawn polys of the crossing field,
the six metals south of it with their nest of corners, `tcw`'s track x 6276 north of y 2700.
Piece 3: the row y 5045 / y 5173, the row y 6238, the wide ground metal. **Eleven joins between
named nets, all without a `?` item** (`tools/unsure.py`): the wire `tl5` called w4395 = `tcw_m6320`,
`c4l_gab`, the wire `tl5` called w4633 = `tcw_c`, `tl5_w4503` = the wire `tl5` called w4850, `ras_o0_alt2` =
`ras_o0_alt2`, the wire `tl5` called w5544 = `tc1_o3527`, `rst_ck`, `lc3_w9947` (`tcw`'s gate line and `tc2`'s metal x 6447),
`tc1_p4308` = the wire `tc2` called m6490, `tc2_o5175` = the wire `r9m` called l3, and U11 = `tc2_m6404`; `ral_stb` is taken
from `tc2`'s port to the south edge. Full extraction: 2299 nets, 4085 transistors (none
added), 0 errors, 0 warnings. Not traced: Not done (one pad 13 px beyond the east edge;
`tcw`'s own bus at x 6205-6400, y 2700-4420 was not re-read).

## Inventory

Survey (written first to `cache/scratch/tl6/survey.md`): `survey.png` (0.33x, every block's
geometry), `sv0_m.png`..`sv2_m.png`, `sv0_a.png`..`sv2_a.png` (0.95x, chip-2 metal and the clean
shot, three sections), `n_top.png` (1.8x, y 2490-2770), `a_w.png`, `a_e.png` (2.4x, the rows
y 3630-4160 at their west and east ends), `b_w1.png`, `b_w2.png` (1.9x, x 5675-6065,
y 4390-5100), `c_top.png`, `c_bot.png` (2.1x, the crossing field's top and foot), `d_sw.png`
(2.0x), `d_se.png` (1.75x) (y 5960-6360).

**Known cells first.** `tools/findcell.py` was not run: the cells of `tl1`, `tl5`, `tla`, `tc1`
and `tcw` are gates on a rail with a load under a second rail, and the strip has no rail, no
box and no diffusion (the six survey views at 0.95x and the eleven closer ones show only
tracks, rows, pads and bare ground; `tools/opendiff.py`: below, Self-check). A track field is
read track by track.

Tracks, by x (`segs.py 5683 6400` at 25 values of y, both metal shots; `tools/tl5_tracks.py v X
2500 6350` for every track: the stretches without metal and the clean shot's green holes):
U0 5712, U1 5755, U2 5799, U3 5843, U4 5886, U5 5930, U6 5973, U7 6016/6022, U8 6059, U9 6103,
U10 6146, U11 6190, then `tcw`'s 6233, 6276, 6320, 6363.

| Where | What | State |
|---|---|---|
| U0 x 5712, y 3722-6192 | one metal, pads at both ends | traced (piece 1) |
| U1 x 5755, y 4002-6065 | one metal from an arm at y 4002; pads (5800,4002), (5757,5632), (5755,6065) | traced (piece 1) |
| U2 x 5799 | three pieces: y 4135-4633, y 4698-4850, y 4980 to the south edge | traced (piece 1) |
| U3 x 5843 | `r9m`'s `tc2_o5175` north of its pad (5845,5045); `bw`'s `rc_stepreq_n` south of the pad (5838,5585) | theirs; the pad (5845,5045)'s poly east along y 5045: traced (piece 3) |
| U4 x 5886, U5 x 5930, north pieces | y 2722-4522 and y 2680-4437, pads at both ends, polys north out of the strip | traced (piece 1) |
| U4-U7 south of y 4565 | `amrw`'s and `bust`'s `c4l0`..`c4l3` | theirs |
| U6 x 5973, U7 x 6022 north | `r9m`'s `ra_eq_r9` and `sl_eq_r5_n` | theirs |
| U8 x 6059, U9 6103, U10 6146, U11 6190, north of the crossing field | U8 from a pad (6058,2592) (poly north), U9 from a pad (6102,2550) (poly east), U10 and U11 from corners at y 2572 and y 2620 (metals east out of the strip); south ends on the north pads of the crossing field's polys | traced (piece 2) |
| x 6040-6420, y 4390-4890 | **the crossing field**: eight vertical polys (x 6059 `r9m`'s, 6101, 6143, 6187, 6228, 6275, 6316 `fld`'s, 6405 `fld`'s) under eight bus metals (y 4482 `tc1_o3527`, 4528 `ra_eq_r9`, 4572 `c4l0`, 4613 `c4l1`, 4658 `c4l2`, 4701 `c4l3`, 4742 `r9m`'s, 4787 `ras_o0_alt2`) | the bus metals y 4482 and y 4787: traced (piece 1); the five polys x 6101-6275: traced (piece 2) |
| x 6090-6400, y 4830-6160 | five metals south from the field's south pads and one from a pad (6316,5003), a nest of corners at y 5568-5790 | traced (piece 2) |
| the rows y 3659, 3872, 4003, 4134 | from `tl5`'s ports and from the pads (5800,3658), (5800,4002), (5798,4135) east to pads of `tcw` and `fld` | traced (piece 1) |
| the rows y 4437-4979 | `tl5`'s nine ports there, to pads on U2, U4, U5, the pad (6010,4480) and the pad (6058,4872) | traced (piece 1) |
| the rows y 5632, 6065, 6151, 6195, 6325 | to pads on U1 and to four pads at x 5972-6145, whose metals leave south or east | traced (piece 1) |
| the row y 6238 (`rcs_mv`) | east to a corner at x 6236, where it goes south | traced (piece 3) |
| x 5890-6190, y 5985-6240 | a wide metal: a band y 5985-6025, a leg x 5890-5925 south, a leg x 6150-6190 south to a band y 6195-6240 east (`tc2`'s `vss` port at (6400, 6198-6243)) | traced (piece 3) |
| x 6230-6400, y 6100-6350 | three pads (6283,6150), (6323,6108), (6365,6150) with polys south, between them narrow outlined strips | traced (piece 2) |
| x 5683-6400, y 2500-2700 | the tracks' north ends, a poly along y 2535 east of the pad (6102,2550), the rim of the wide metal band at y 2500 | traced (piece 2) |

## Logic

No transistor. What the wiring joins (every join below is drawn without a `?` item;
`tools/unsure.py`):

### Piece 1 (traced 2026-11-18 03:14 +0000): the rows of `tl5`'s east ports and the tracks U0, U1, U2, U4, U5

| `tl5`'s port | Path (all read at 4x in the chip-2 metal shot and the clean shot unless noted) | Result |
|---|---|---|
| `tcw_m6320`, metal y 3659 (latch c's data) | the metal runs on 115 px to a pad (5800,3658); the pad's poly east along y 3650-3668 under U3-U11 and `tcw`'s track x 6233 onto `tcw`'s drawn poly (from x 6205) and its pad (6315,3655) | **the wire `tl5` called w4395 = `tcw_m6320`** |
| `tl5_w3505`, row y 3722 (latch a's enable) | ends on a pad (5712,3722), the north end of U0; U0 south to its pad (5712,6192); poly east along y 6195 to a pad (5972,6193); metal south across y 6350 | leaves south at (5972,6350) |
| `c4l_gab`, row y 3872 (latch c's clear) | east under U0 (no pad) and U3-U11 into `tcw`'s pad (6232,3870) | **`c4l_gab`** |
| `tl4_w5068`, row y 4437 | pad (5928,4437), U5's north piece north to its pad (5928,2680); poly north across y 2500 | leaves north at (5928,2500) |
| `tc1_o3527`, pad (5666,4480) | poly east to a pad (6010,4480), the west end of the bus metal y 4482, which crosses the field to `tc2`'s port | **the wire `tl5` called w5544 = `tc1_o3527`** |
| `c4l_l3`, row y 4521 | pad (5886,4522), U4's north piece north to its pad (5887,2722); poly north across y 2500 | leaves north at (5887,2500) |
| `tl5_w4503`, row y 4590 (latch c's inverse output) | east to a corner at x 5867 (in the open between U3 and U4), south, west along y 4699 to a pad (5797,4698); U2's middle piece south to a pad (5797,4850); the row y 4849 west | **`tl5_w4503` = the wire `tl5` called w4850**: inverter 1's input is latch c's inverse output |
| `tcw_c`, row y 4633 (latch c's output) | pad (5797,4633), U2's upper piece north to a pad (5798,4135); poly east along y 4134 into `fld`'s pad (6318,4135) | **the wire `tl5` called w4633 = `tcw_c`** |
| `ras_o0_alt2`, row y 4808 (inverter 1's output) | east under U0-U7, south at x 6058 to a pad (6058,4872); metal north to the west end of the bus metal y 4787, which crosses the field to `tc2`'s port | **the wire `tl5` called w4807 = `ras_o0_alt2`** |
| `tl5_w4503`, row y 4849 | the pad (5797,4850) above | |
| the wire `tl5` called w3982 (`tl4_w4068`), row y 4979 | pad (5798,4980), U2's south piece south across y 6350 | leaves south at (5799,6350) |
| `rst_ck`, pad (5666,5632) | poly east under U0 to a pad (5757,5632) **on U1** | **`rst_ck`** |
| `ck_out`, pad (5667,6150) | poly east along y 6151 to a pad (6016,6150); metal south across y 6350 | leaves south at (6016,6350) |

And from the east:

| Net | Path | Result |
|---|---|---|
| `rst_ck` (`fld`'s pad (6400,4005)) | poly west along y 4003 to a pad (5800,4002); metal west to a corner (5755,4002) and south as U1, pads (5757,5632) and (5755,6065); the south pad's poly east along y 6065 to a pad (6016,6066); metal east to a corner (6105,6066) and south across y 6350 | `rst_ck` is `rst_ck` and leaves south at (6105,6350) |
| `ral_stb` (`tc2`'s metal y 6328) | west to a pad (6145,6322); poly west along y 6325 to a pad (5755,6322); metal south across y 6350 | leaves south at (5755,6350). `tc2`'s notes give the follower's end (6012,6068) for this metal: the follower jumped from the pad to the metal x 6105 (which passes 40 px west of it without a contact: `t11.png` 4x, three shots) |

**What that says about the logic** (the equations are `tl5`'s, `tcw`'s and `fld`'s, with the
names joined here):

```
latch c (tl5):   tcw_c = NOT( c4l_gab  OR  tl3_e4243 AND NOT tcw_m6320  OR  tl5_w4503 )     = tcw_c
                 tl5_w4503 = NOT( tcw_m6320 AND tl3_e4243  OR  tcw_c )
inverter 1:      ras_o0_alt2 = NOT tl5_w4503
tcw / fld:       fld_y_b = NOT tcw_c ;  tcw_o3820 = NOT( fld_a_in OR (rst_ck AND tcw_c) ) ;  fld_a_in = NOT( (rst_ck AND tcw_b) OR tcw_o3820 )
```

- **`ras_o0_alt2`, the signal that drives row address bit 0 in interlace sync-and-video mode
  when R9's bit 0 is clear, is latch c of `tl5`'s column, buffered**: `ras_o0_alt2` = NOT
  `tl5_w4503`, and `tl5_w4503` is the latch's inverse output. Latch c is open while
  `tl3_e4243` is high, takes `tcw_m6320` (from `tcw`'s gate column) and is cleared by
  `c4l_gab`.
- **The same latch's output is `tcw_c`**: the data of `tcw`'s latch (the cross-coupled pair
  `fld_a_in` / `tcw_o3820`, gated by `rst_ck`) and, inverted, `fld_y_b`, the second input of the
  XOR that makes `ras_o0_alt1`. So both sources of row address bit 0 in that mode come from
  latch c: it is the best candidate for the **field (odd/even) flip-flop**; believed, not
  shown (what clocks and clears it is not identified).
- `tc1_o3527` (cell B's output of `tc1`) goes west to `tl5`'s track T10 and on into `tl4`'s
  strip on the row y 5544.

**Seen** (4x tiles: chip-2 metal over the clean shot, 104 x 100 px each):

| Item | Reading | Seen |
|---|---|---|
| pads (5800,3658), (5712,3722), (5800,4002) with its corner (5762,4003) | each a ring with a bright centre and a green hole on a salmon pad; T10's metal arrives from the west and ends on the first, bare ground east; the row y 3722 ends on the second (closed east end x 5733), U0 leaves south, bare ground north; the third's metal goes west and turns south | `t1.png` |
| pads (5798,4135), (5928,4437), (5886,4522) | U2 leaves the first south (closed west end); U5 arrives on the second from the north (closed east end x 5947, bare ground south); U4 arrives on the third from the north (closed east end x 5905, bare ground south to `amrw`'s corner at y 4565) | `t2.png` |
| pads (5797,4633), (5797,4698), the corner (5867,4590) | U2's upper piece ends on the first (bare ground, an hourglass of open field, between the two pads); the second's poly leaves east | `t3.png` |
| the L of `tl5_w4503`, x 5857-5877, y 4580-4708 | one poly in the open between U3 and U4: `px.py col 5866 4566 4722 6 metal,metal1,acid`: poly colour (146-170/112-135/46-61 in chip 2) without a dark line from y 4584 to y 4704, dark edges at y 4578 and y 4710, bare ground beyond; the row y 4590 has the same colour at the corner (x 5860-5868) as in the gap between U2 and U3 (x 5816-5824), where it surely runs on; `px.py row 4699 5810 5885 5` | `t4.png` (4x: chip-2 stripped, clean, chip-1 metal) |
| pads (5797,4850), (5798,4980), the corner (6058,4808) and pad (6058,4872) | U2's middle piece ends on the first (bare ground south); U2's south piece starts on the second (bare ground north); the row y 4808 turns south into a 30 px wide pad stem; the pad's metal goes north to the bus metal | `t5.png` |
| the pad (6010,4480) and `r9m`'s corner (6022,4442) / pad (6059,4440) beside it | the row y 4480 ends on the pad (6010,4480), whose metal runs east as the bus metal y 4482; `r9m`'s metal turns east 20 px north of it onto its own pad: 14 px of dark between the two metals in both chips | `q1.png` (4x, three shots) |
| joins to `tcw`'s poly at (6205-6215, 3655), to `tcw`'s pad (6232,3870), to `fld`'s pads (6318,4135) and (6400,4005) | each row runs into the other block's drawn pad or poly as one salmon band | `t6.png`, `t7.png` |
| pads (5887,2722), (5928,2680) | north ends of U4 and U5 (bare ground north of each metal); each pad's poly goes north | `t7.png`; the polys at y 2500-2560: `t12.png` (they run on under the band's rim) |
| pad (5757,5632) on U1 | ring with a bright centre in both metal shots, green hole; the row from `tl5`'s pad (5666,5632) passes under U0 (no widening) and ends on it (closed east end x 5775); U1 runs through | `t10.png` (4x, three shots); found by `tl5_tracks.py v 5755 4012 6052` (hole at y 5634) |
| pads (5712,6192), (5972,6193), (5755,6065) | U0 ends on the first; the row y 6195 ends on the second (closed east end x 5990), metal south; U1 ends on the third, poly east | `t8.png` |
| pads (6016,6066), (6016,6150), (5755,6322) | the row y 6065 ends on the first, metal east; the row y 6151 ends on the second, metal south; the third's poly goes east, its metal south | `t9.png` |
| the corner (6105,6066) of `rst_ck`'s metal | one plain L from the pad's metal to the metal x 6105, bare ground north and east of it, 30 px to the wide metal's band | `w3.png` |
| pad (6145,6322) and the metal x 6105 | the row y 6325 ends on the pad, whose metal goes east (`ral_stb`); the metal x 6105 crosses the row 40 px west of the pad at constant width without a ring | `t11.png` (4x, three shots) |
| the south edge at x 5725-6045, the north edge at x 5855-5960 | the metals x 5755, 5799, 5972, 6016 and the two polys run on across the edge | `t12.png` |
| the east edge at y 4482, 4787, 6328 | each metal runs on into `tc2`'s drawn piece (its `tc1_o3527`, `ras_o0_alt2`, `ral_stb`) | `t13.png` |

**The rows between their ends.** The clean shot along each row (a cream test, red > 195 and
red - green > 30, over 7 px): cream under every track the row crosses and nowhere widened; the
gaps between are the 25-30 px gaps between tracks (gap marks, tracing guide trap 2). Along
each track, `tools/tl5_tracks.py v`:

| Piece | Longest stretch without metal in both shots | Green holes |
|---|---|---|
| U0, x 5712, y 3735-6180 | 15 px (row edges) | none |
| U1, x 5755, y 4012-6052 | 18 px (y 5608-5626) and 16 px (y 5636-5652): the ring of the pad (5757,5632) | 5634 (the pad) |
| U2 upper, x 5799, y 4148-4622 | 9 px | none |
| U2 middle, x 5798, y 4712-4838 | 9 px | none |
| U2 south, x 5800, y 4992-6350 | 15 px (y 5570-5585) | none |
| U5 north, x 5930, y 2692-4425 | 11 px | none |
| U4 north, x 5886, y 2735-4510 | 12 px | none |
| bus metal y 4483, x 6025-6405 | 16 px (the pad's ring); 8-11 px at each poly's edges | none |
| bus metal y 4787, x 6062-6405 | 13 px | none |
| T10's piece y 3659, x 5683-5785 | none | none |
| x 6105, y 6075-6420; x 6016, y 6165-6360; x 5972, y 6208-6360; y 6328, x 6160-6420 | 12 px | none |

### Piece 2 (traced 2026-11-18 03:21 +0000): the tracks U8-U11, the crossing field, the metals south of it

**The crossing field** (x 6040-6420, y 4390-4890): eight vertical polys, each from a pad at
its north end to a pad at its south end, under eight horizontal bus metals. Nothing joins a
poly to a bus metal: no pad on any poly between its end pads, and `tools/tl5_tracks.py h` along
each of the eight metals (y 4483, 4528, 4572, 4613, 4658, 4701, 4742, 4787; x 6080-6300) finds
no green hole. The polys keep their order: `c_mid.png` (2.3x, clean shot and chip-2 stripped
shot, y 4455-4745) shows seven straight polys at the same x in every gap between metals
(orange in every gap in the chip-2 shot); `c_top.png`, `c_bot.png` (2.1x) their ends; overlay
`ov2.png` (1.9x).

| Poly | North pad and its metal | South pad and its metal | Net |
|---|---|---|---|
| x 6059 | `r9m`'s (6059,4440): `sl_eq_r5_n` (U7) | `r9m`'s (6058,4742): the bus metal y 4742 | theirs |
| x 6101 | (6101,4398): U8, by a foot east at y 4395 | (6101,4830): metal south, corner (6103,5790), east, corner (6233,5790), south, a foot east at y 6152 onto a pad (6275,6152); that pad's poly south along x 6282 across y 6350 | `tl6_p6101` |
| x 6143 | (6143,4437): U9, by a step east at y 4356 from x 6103 to x 6146 | (6144,4872): metal south, corner (6146,5746), east, corner (6276,5746), south, a foot east at y 6110 onto a pad (6318,6110); poly south along x 6322 across y 6350 | `tl6_p6143` |
| x 6187 | (6187,4397): U10, by a step east at y 4312 from x 6146 to x 6189 | (6187,4830): metal south, corner (6190,5702), east, corner (6320,5702), south, corner (6320,6074), east, corner (6363,6074), south to a pad (6360,6152); poly south along x 6365 across y 6350 | `tl6_p6187` |
| x 6229 | (6229,4437): U11, by a step east at y 4272 from x 6190 to x 6233 | (6229,4872): metal south, corner (6233,5659), east, corner (6363,5659), south, corner (6363,6032), east onto `tc2`'s metal of its pad (6404,6107) | **`tc2_m6404`** |
| x 6275 | `tcw`'s (6275,4405): `lc3_w9947` | (6274,4832): metal south, corner (6276,5612), east onto `tc2`'s metal (its `lc3_w9947`) | **`tcw`'s gate line = `tc2`'s metal x 6447: one net, `lc3_w9947`** |
| x 6316 | `fld`'s (6316,4437): `fld_a_in` | none: the poly turns east at y 4937 (`fld`'s) | theirs |
| x 6405 | `fld`'s (6405,4437) | `fld`'s (6400,4870) | theirs (`fld_y_b`) |

**North of the field.** U8 starts on a pad (6057,2595) whose poly goes north across y 2500
(and turns east under the rim of the wide metal band at y 2475-2500, outside the strip:
`w2.png`); U9 on a pad (6105,2552) whose poly runs 25 px north into a poly going east along
y 2518-2542 in the open, across x 6400; U10 comes from the east along y 2573 and turns south at
(6146,2573); U11 comes from the east along y 2619 and turns south at (6190,2619) (its metal
ends on a pad at about (6413,2617), 13 px beyond the strip's edge: seen on `w2.png`, not
drawn). `tcw`'s track x 6276 (`tcw_m6278`, drawn by `tcw` to y 2700) runs on north to a corner
(6276,2665) and east across x 6400: drawn here.

**South of the field**, one more metal of the nest: `tc2`'s row y 5003 (`tc1_p4308`) runs on
west to a pad (6317,5000); the pad's metal goes south along x 6320 to a corner (6320,5569) and
east onto `tc2`'s metal of its pad (6490,6108): **`tc1_p4308` = the wire `tc2` called m6490**. So three of
`tc2`'s nest metals are identified from here: `tc2_m6404` is U11, the metal x 6447 is `lc3_w9947` (`tcw`'s gate line)
(the common gate input of four pull-downs of `tcw`'s column), the wire `tc2` called m6490 is `tc1_p4308`.

**Seen** (4x tiles as in piece 1):

| Item | Reading | Seen |
|---|---|---|
| pads (6101,4398), (6143,4437), (6187,4397), (6229,4437) and the metals onto them | each a ring with a bright centre, green hole on a salmon pad whose poly leaves south; U8's foot arrives from the west, U9, U10, U11 from the north; 14-20 px of dark between each y 4437 pad and the bus metal y 4482 south of it (the follower jumps it: `follow.py 6103 4000 S` and `6190 4000 S` end on the pad (6010,4480)) | `u1.png`, `u2.png` |
| the steps of U9 (y 4356), U10 (y 4312), U11 (y 4272) | plain double corners over field, three separate pink bands in the clean shot; a speck on U10's step at (6162,4310) with nothing under it | `u1.png`, `u2.png`; `c_top.png` |
| pads (6101,4830), (6144,4872), (6187,4830), (6229,4872), (6274,4832) | poly from the north, metal leaving south, on each | `u3.png` |
| pad (6317,5000) | the row y 5003 from the east ends on it (bare ground north and west); metal south | `u4.png` |
| pads (6057,2595), (6105,2552) | north ends of U8 and U9 (bare ground north of each metal); U8's poly north in the open; U9's pad poly into the poly along y 2530: `px.py col 6104 2504 2548 4`: poly colour in the chip-2 metal shot (169/115/58) from y 2524 to the pad's ring, salmon in the clean shot from y 2528; `px.py row 2530`: poly from x 6100 east, bare ground west of x 6094 | `u4.png`, `w2.png` |
| the poly along y 2530, x 6100-6420 | poly colour (red - green > 30) at every sample in the chip-2 metal shot, at all but 3 in chip 1's; band y 2518-2542 at x 6150, 6250, 6350, 6398 | text; `n_top.png` 1.8x, `u5.png` |
| corners (6146,2573), (6190,2619), (6276,2665); the east edge at y 2520-2630 and at y 2665 | plain corners; each metal runs on across x 6400 | `u5.png`, `w2.png` |
| the nest of corners, x 6090-6400, y 5540-5820 | six nested L's, separate pink bands | `e_nest.png` 2x, two shots; `w3.png` 4x (four corners); overlay `ov3.png` 1.55x |
| pads (6275,6152), (6318,6110), (6360,6152) | V2's and V3's metals arrive by a foot from the west, V4's from the north; each pad's poly leaves south | `u6.png` |
| joins to `tc2`'s metals at (6400,6032), (6400,5612), (6400,5569) | each metal runs on into `tc2`'s drawn piece | `u7.png` |
| the polys x 6282, 6322, 6365 at y 6180-6350 | straight, under the wide metal band and `ral_stb`'s metal without a pad (`tl5_tracks.py v X 6170 6352 --half 4`: no hole), on across y 6350; narrow outlined ovals between them are open field | `v2.png`, `u7.png` |

Metal tests (`tools/tl5_tracks.py`, as in piece 1; none finds a stretch without metal in both
shots longer than 12 px or a green hole, except as noted): U8 x 6059 y 2608-4385; U9 x 6103
y 2565-4345, x 6146 y 4368-4425; U10 x 6146 y 2585-4300, x 6189 y 4325-4385; U11 x 6190
y 2632-4262, x 6233 y 4284-4425; the three steps; the metals y 2573, 2619, 2664 to x 6410; south
of the field x 6103 y 4845-5775 (a weak "hole" at y 5545, 38 px long, minimum 13: the black
blob of dirt on chip 1 at (6085,5540), plain metal in both metal shots), y 5790 x 6118-6230,
x 6235 y 5805-6140, x 6146 y 4888-5735, y 5746, x 6277 y 5760-6095, x 6190 y 4845-5690, y 5702,
x 6320 y 5716-6062, x 6363 y 6088-6135, x 6233 y 4888-5648, y 5659, x 6363 y 5672-6020, x 6276
y 4845-5600, y 5612, x 6320 y 5018-5556, y 5569. The stretches of 8-12 px at y 5030-5061 and
y 5157-5193 are the edges of the rows y 5045 and y 5173 under the metals.

### Piece 3 (traced 2026-11-18 03:21 +0000): the rows y 5045 / y 5173 and y 6238, the wide ground metal

| Item | Reading | Seen |
|---|---|---|
| **`tc2_o5175` = the wire `r9m` called l3** | `tc2`'s row y 5173 (the output of its NOR(`tc1_x1`, `fld_b_in`)) runs on west under the metals x 6363, 6320 and 6276 to a corner at x 6250-6268, in the open between the metals x 6233 and x 6276; north to y 5045; west along y 5035-5057 under seven metals to `r9m`'s pad (5845,5045), the south end of `tc2_o5175`'s metal x 5848 | `v1.png` (4x: the pad, both corners), `w2.png` (the row at x 6320-6420); `px.py col 6260 5022 5200 8 metal,metal1,acid`: one poly colour (124-153/84-119/38-59 in chip 2) from y 5038 to y 5182 with no dark line where the rows' edges would cross (y 5057, y 5163); `px.py row 5045 6226 6282 4`; the cream test along y 5045: cream under every metal from x 5851 to x 6247 |
| `rcs_mv` | `tl5`'s row y 6238 east under U0, U2, `bw`'s metal, the wide metal's west leg and the metals x 5972, 6016, 6105, along the south edge of the wide metal band from x 6141, to a corner at x 6226-6246; south in the open across y 6350 | `v2.png` 4x, `v3.png` 5x (chip-2 stripped, chip-1 metal, clean); `px.py col 6236 6222 6290 4`: the dark line at y 6246-6250 between the row and the poly below it is the band's rim (the through poly x 6282 has the same line, `col 6282`; where the row has only field below it, `col 6215`, the chip-2 stripped shot is green over red from y 6258); the clean shot is poly-coloured through the line (221/171/112, 191/162/105, then open poly) |
| the wide metal (`vss`) | `tc2`'s `vss` piece at (6400, 6198-6243) runs on west as a band y 6193-6245 to a leg x 6141-6195, north to a band y 5977-6029, west to a leg x 5882-5934, south across y 6350. No contact under it in the strip | `w1.png` (4x: the two north corners and the south-east junction), `d_se.png`, `d_sw.png`; runs of the metal test in both metal shots at six rows and six columns (the test reads each edge 5 px inside the outline seen at 4x). The clean shot under it is pink with an olive centre line (40-140 px long, minimum red - green 1 to -9: the halo under a wide metal, not a hole) |

### What the joins of pieces 2 and 3 say

- `tc2_o5175` = NOR(`tc1_x1`, `fld_b_in`) is the net `r9m` followed as "line 3" from `tla`'s
  track P (the middle cluster of the vertical control) round the top of `tl5`'s strip: so the
  NOR's output goes to the row counter's step logic area, 2,100 px west.
- `lc3_w9947`, the common gate input of four pull-downs of `tcw`'s column (a clock or enable by
  its use), comes up from the south: down the field's poly x 6275, the nest, `tc2`'s pad
  (6447,6150) and a poly south across y 6400.
- `tc1_p4308` (the input of an inverter in `tc1`'s west columns) likewise comes up from the
  south by `tc2`'s pad (6490,6108).
- U8, U9, U10 (`tl6_p6101`, `tl6_p6143`, `tl6_p6187`) only pass through: from the north or
  east edge, down the field, to three polys that leave south beside `tc2`'s three.

## Self-check (tracer, before any review)

**Piece 1 (2026-11-18 03:14 +0000).**
*Ends.* Every pad, corner and edge crossing drawn is in the "Seen" table: 21 pads and 4 corners
at 4x in the chip-2 metal shot and the clean shot (three shots where a neighbour's metal is
close), each with the ground about 50 px beyond; the edges on `t12.png` (south, north) and
`t13.png` (east); the west edge is `tl5`'s ports (its `pc3.png`, `pi1.png`, `g_n.png`,
`p2_c.png`; the rows at x 5676-5700 on `a_w.png` 2.4x and `ov1.png` 2x: **below 4x**; they are
straight bands onto `tl5`'s drawn rows, and the extraction joins each to `tl5`'s net).
The south edge at x 6105 and x 5972: `t12.png` shows x 5972 and x 6016; x 6105 at y 6350 only
by the metal test (`tl5_tracks.py v 6105 6075 6420`: metal to y 6420).
*Widths.* No transistor. No row or track drawn crosses a diffusion: `tools/opendiff.py 5683
2500 6400 6350` lists 22 green groups, all strips 8-12 px wide beside pads or between metals
(none wider than 12 px in its narrow direction).
*Weak spots.* (1) The rows between x 5830 and x 6200 (y 3659, 3872, 4003, 4134) rest on the
0.95x and 2.4x views and the cream test, not on a 4x view of every crossing; their ends are at
4x. (2) U0, U1, U2, U4, U5 between their pads rest on the metal test and the hole scan (which
found the pad (5757,5632)), and the 0.95x views. (3) The L of `tl5_w4503` is in the open with
a gap mark on each corner in the clean shot: decided by the colour profile in the chip-2 metal
shot (table). (4) The bus metals y 4482 and y 4787 over the field: the metal test and the hole
scan; the five polys under them are piece 2.
*Omissions* inside what is traced: rings in the metal shots without a drawn item: none on the
drawn tracks (specks only; no hole under them). Outlined boxes in the clean shot without a
drawn item: the khaki boxes between rows and tracks (open field between protected margins);
the hourglass (5775-5820, 4650-4685) between the pads (5797,4633) and (5797,4698): open
field, bare ground in the metal shot (`t3.png`).
*Track fields.* The table of metal tests above. Each pad's track: U0, U1, U2 are the three
westmost tracks and each of their pads has its metal seen leaving it at 4x; the pad
(5886,4522) is on U4 and (5928,4437) on U5 (`t2.png`: the metal over each pad, U3 `r9m`'s
drawn line beside the first).
*Joins to other blocks.* `tcw`'s poly `P 6315,3655 x6205` (its pad (6315,3655), net
`tcw_m6320`); `tcw`'s pad `P 6214,3853:6250,3888` (`c4l_gab`); `fld`'s pads
`P 6383,3988:6418,4022` (`rst_ck`) and `P 6300,4118:6336,4152` (`tcw_c`); `tc2`'s metals
`M 6400,4482...` (`tc1_o3527`), its `ras_o0_alt2` row metal and `M 7489,6274 y6328 x6400`
(`ral_stb`); `tl5`'s rows and pads at x 5683. `tools/amr_at.py` gives the joined name on every
piece.

**Pieces 2 and 3 (2026-11-18 03:21 +0000).**
*Ends.* Every pad and corner drawn is in the two "Seen" tables: 14 pads at 4x in two shots,
the three steps, the three north corners, the pads' feet; of the nest's twelve corners four at 4x (`w3.png`: (6103,5790), (6233,5790), (6146,5746),
(6276,5746)) and the rest at 2x in two shots (`e_nest.png`) and on the 1.55x overlay (**below
4x**: plain nested L's with pink between them in the clean shot, and each piece passes the
metal test from pad to pad). Edges:
north at x 6058 (`w2.png`: the poly runs on and turns east 12 px beyond the edge); east at
y 2530, 2573, 2619 (`u5.png`), y 2665 (`w2.png`), y 5003 (`u4.png`), y 5173 (`w2.png`), y 5569,
5612, 6032 (`u7.png`); south at x 6236, 6282 (`u7.png`), x 6322, 6365 (`v2.png`). The wide
metal's south end at (5908,6350): `d_sw.png` 2x and the metal test only (**below 4x**); its
east end is `tc2`'s drawn piece (`v2.png` shows the band at x 6400).
*Widths.* No transistor. The eight polys of the field lie on field between their pads (pink
on both sides of each in every gap, `c_mid.png`; no diffusion in the strip: `tools/opendiff.py`,
piece 1).
*Weak spots.* (1) The field's polys between y 4460 and y 4800: read at 2.3x in two stripped
shots, with the hole scan along each bus metal; not each of the 40 crossings at 4x. A contact
there would have a pad (tracing guide, trap 15) and none is widened. (2) The nest's corners
(above). (3) The two corners of `tc2_o5175`'s row and the corner of `rcs_mv` are in the open
or under a metal's rim: each decided by a colour profile in two or three shots (tables), not by
the view alone. (4) U9's pad poly into the poly along y 2530: the same. (5) The rows y 5045 and
y 6238 between their ends rest on the cream test under each metal and the 0.95x-2x views.
*Omissions* inside what is traced. Rings in the metal shots without a drawn item: a speck on
U10's step (6162,4310) and specks on the wide metal (`w1.png`, `d_se.png`): nothing under them
in the clean shot; the pad at about (6413,2617), beyond the edge (Not done). Outlined boxes in
the clean shot without a drawn item: khaki boxes of open field between metals (the largest:
x 6055-6090, y 4890-5980, with a black blob of dirt at (6085,5540); x 5990-6090, y 6090-6230
inside the wide metal's loop; x 6200-6260, y 2700-2860); the narrow ovals between the polys
x 6236-6405 at y 6250-6350 (field between polys in the open, `v2.png`).
*Track fields.* Each pad's track: the four north pads of the field alternate y 4398 / y 4437
and each metal is seen arriving on its own pad at 4x (`u1.png`, `u2.png`); the follower
(`follow.py X 4000 S` for X = 6059, 6103, 6146, 6190 and `X 5300 S` for the six south metals)
gives the same pairing. The three south pads (6275,6152), (6318,6110), (6360,6152) and
`tc2`'s three: `u6.png`, `u7.png`.
*Joins to other blocks.* `tc2`'s `M 6400,6026 x6406 y6112` (`tc2_m6404`), `M ... y5611 x6396`
(`lc3_w9947`), `M ... y5567 x6400` (`tc1_p4308`), `P 6610,5003 x6400` (`tc1_p4308`),
`P 6400,5161:6503,5185` (`tc2_o5175`), its `vss` metal at (6400, 6198-6243); `tcw`'s pad
`P 6258,4388:6292,4422` (`lc3_w9947`) and its metal `M 6276,... y2700` (`tcw_m6278`); `r9m`'s
pad and contact at (5845,5043) under the south end of `r9m`'s metal x 5848 (`tc2_o5175`); the pad and contact are drawn here (neither block had them: see Review round 1). `tools/amr_at.py` gives the joined name on every piece of ten of the joins at once and on this one after that contact was drawn. Note: an `@alias` does not connect anything: it only says which name a net keeps once the geometry makes it one net.
*Copies.* None: no cell is placed.

## Ports

The same ports are in `ports.d/tl6.txt`. West-side ports carry `tl5`'s names (aliases).

| Name | Layer | Where | Direction | What |
|---|---|---|---|---|
| `tcw_m6320` | metal | (5683, 3652-3666) | ? | = `tcw_m6320`; latch c's data |
| `tl5_w3505` | poly | (5683, 3712-3732) | ? | latch a's enable, to U0 |
| `c4l_gab` | poly | (5683, 3862-3882) | ? | = `c4l_gab`; latch c's clear |
| `tl4_w5068` | poly | (5683, 4427-4447) | ? | to U5's north piece |
| `tc1_o3527` | poly | (5683, 4470-4490) | ? | = `tc1_o3527` |
| `c4l_l3` | poly | (5683, 4511-4531) | ? | to U4's north piece |
| `tl5_w4503` | poly | (5683, 4580-4600) | in | latch c's inverse output |
| `tcw_c` | poly | (5683, 4623-4643) | in | = `tcw_c`; latch c's output |
| `ras_o0_alt2` | poly | (5683, 4798-4818) | in | = `ras_o0_alt2`; inverter 1's output |
| `tl5_w4503` | poly | (5683, 4840-4858) | ? | = `tl5_w4503`; inverter 1's gate |
| `tl4_w4068` | poly | (5683, 4970-4988) | ? | = `tl4_w4068`; to U2's south piece |
| `rst_ck` | poly | (5683, 5622-5642) | ? | = `rst_ck` |
| `ck_out` | poly | (5683, 6142-6160) | ? | to the pad (6016,6150) |
| `c4l_l3` | poly | (5877-5897, 2500) | ? | north from U4's north pad |
| `tl4_w5068` | poly | (5918-5938, 2500) | ? | north from U5's north pad |
| `tcw_m6320` | poly | (6212, 3649-3667) | ? | onto `tcw`'s poly |
| `c4l_gab` | poly | (6225, 3862-3882) | ? | into `tcw`'s pad (6232,3870) |
| `rst_ck` | poly | (6392, 3994-4012) | ? | into `fld`'s pad (6400,4005) |
| `tcw_c` | poly | (6310, 4125-4143) | ? | into `fld`'s pad (6318,4135) |
| `tc1_o3527` | metal | (6400, 4472-4492) | in | bus metal y 4482 |
| `ras_o0_alt2` | metal | (6400, 4777-4797) | ? | bus metal y 4787 |
| `ral_stb` | metal | (6400, 6318-6338) | ? | on east as `tc2`'s piece |
| `ral_stb` | metal | (5749-5761, 6350) | ? | from the pad (5755,6322) |
| `tl4_w4068` | metal | (5793-5805, 6350) | ? | U2's south piece |
| `tl5_w3505` | metal | (5966-5978, 6350) | ? | from the pad (5972,6193) |
| `ck_out` | metal | (6010-6022, 6350) | ? | from the pad (6016,6150) |
| `rst_ck` | metal | (6099-6111, 6350) | ? | from the corner (6105,6066) |
| `rcs_mv` | poly | (5683, 6228-6248) | ? | `tl5`'s row y 6238 |
| `tl6_p6101` | poly | (6052-6072, 2500) | ? | north from U8's pad (6057,2595); turns east under the band's rim at y 2475-2500 |
| `tl6_p6143` | poly | (6400, 2520-2540) | ? | the poly along y 2530 from U9's pad (6105,2552) |
| `tl6_p6187` | metal | (6400, 2567-2579) | ? | U10's north end, from the east |
| `tc2_m6404` | metal | (6400, 2613-2625) | ? | U11's north end; ends on a pad at about (6413,2617), not drawn |
| `tcw_m6278` | metal | (6400, 2659-2671) | ? | `tcw`'s track x 6276, from its corner (6276,2665) |
| `tc1_p4308` | poly | (6400, 4994-5012) | ? | onto `tc2`'s row y 5003 |
| `tc2_o5175` | poly | (6400, 5163-5183) | in | onto `tc2`'s row y 5173 (its NOR's output) |
| `tc2_o5175` | poly | (5843, 5035-5055) | ? | into `r9m`'s pad (5845,5045) (`tc2_o5175`) |
| `tc1_p4308` | metal | (6400, 5563-5575) | ? | = `tc1_p4308`; onto `tc2`'s metal |
| `lc3_w9947` | metal | (6400, 5606-5618) | ? | = `lc3_w9947`; onto `tc2`'s metal |
| `tc2_m6404` | metal | (6400, 6026-6038) | ? | onto `tc2`'s metal |
| `vss` | metal | (6400, 6193-6245) | - | the wide ground metal, on east as `tc2`'s piece |
| `vss` | metal | (5882-5934, 6350) | - | the wide ground metal's west leg |
| `rcs_mv` | poly | (6226-6246, 6350) | ? | from the row y 6238's corner |
| `tl6_p6101` | poly | (6273-6291, 6350) | ? | from the pad (6275,6152) |
| `tl6_p6143` | poly | (6313-6331, 6350) | ? | from the pad (6318,6110) |
| `tl6_p6187` | poly | (6356-6374, 6350) | ? | from the pad (6360,6152) |

## Ambiguities

1. **The supply of the wide metal** (x 5882-6195, y 5977-6245) is `vss` by `tc2`'s name for
   the piece it runs into at x 6400 ("the wide ground metal, from `fld`'s west ground rail"):
   one drawn metal from there on, no `?` item; nothing in this strip hangs on it (no contact).
2. **The pad (5757,5632) on U1** makes `rst_ck` the same net as `rst_ck`. It was found by the
   hole scan and read at 4x in three shots (`t10.png`): a full ring with a bright centre in both
   metal shots and a green hole. No other reading is offered; it is listed here because the
   join is far-reaching (it takes `rst_ck` into `tl4`'s strip on the row y 5631) and rests on
   one pad.
3. **`ral_stb`**: `tc2`'s notes give this metal's west end as (6012,6068) from the follower;
   here it ends on the pad (6145,6322) and the net goes on in poly to the pad (5755,6322). The
   metal x 6105 that the follower took is `rst_ck` (`t11.png`). A correction to `tc2`'s notes,
   for the coordinator.

## Not done

- The pad at about (6413,2617), the east end of U11's metal (`tc2_m6404`), 13 px beyond the
  strip's east edge: seen on `w2.png` (a ring at the metal's end), not drawn; its poly is not
  followed. It is in `tcw`'s region.
- U8's poly (`tl6_p6101`) north of y 2500: turns east under the rim of the wide metal band at
  y 2475-2500 (`w2.png`); the polys of U4 and U5 (`c4l_l3`, `tl4_w5068`) run on north under
  the band (`t12.png`). The band (y 2180-2500) is drawn by no block.
- `tcw`'s bus at x 6205-6400, y 2700-4420 (its tracks x 6233, 6276, 6320, 6363, their pads and
  rows) was not re-read: the 0.95x and 2.4x views show nothing there without an outline, and
  three open spots were looked at only through the hole scan ((6233,4244), (6276,3673),
  (6276,4201): open ground between metals).
- Everything that leaves the strip south (y 6350) or north is followed no further: Ports.

## Review

Round 1 (full review, 2026-11-18 03:39 +0000, a fresh agent on claude-fable-5-2, at commit e83f200). Told to
check each of the eleven joins at every step and that each end is the other block's net of
that name; to suspect U2's three pieces, the pad (5757,5632) on U1, the crossing field (a
step of one track), the three joins decided by colour profile, the nest's corners, and
missed taps. It read every join's pads, rows and corners at 4-7x in two to four shots,
confirmed U2's breaks in both metal shots (no metal at y 4641-4694 and y 4857-4976), U1 as
one piece with no other hole from y 4002 to 6065, the eight polys at the same x under every
bus metal with no hole on any, and scanned every drawn metal piece for undrawn contacts.
Joins 1-9 and 11: confirmed. One finding, which changes the netlist: join 10
(`tc2_o5175` = the wire `r9m` called l3) was claimed but not in the extraction: at (5845,5045) the poly and
the metal each just ended, with no pad and no contact drawn by either block, and the alias
line connects nothing by itself. The photos show the contact (ring with a bright centre in
both metal shots, green hole on a salmon pad in the clean shot): confirmed by the tracer at
6x (`chk_j10.png`) and drawn; the two are now one net (0 errors; `tc2_o5175 = NOR(fld_b_in,
tc1_x1)` is on r9m's line 3).
Not checked: tc2's rows east of its pads, `tc2_o5175` west of x 5683, tl5's side of its
ports, the undrawn pad at (6413,2617) on U11 (13 px outside the strip).

Round 2 (fix check, 2026-11-18 03:40 +0000, a fresh agent on claude-fable-5-2, against commit e83f200). The
contact is real (centre bright in both metal shots, green in the clean shot, pitted box in
the chip-2 stripped shot; profile along y 5046); the pad is the west end of row y 5045 and
of no other poly; only one metal lands on the ring, followed north to a corner at
(5842,2684) and west: r9m's line; U3 is empty from y 5066 to bw's pad near y 5585.
`tools/sameconn.py`: the only difference is the wire `r9m` called l3 and `tc2_o5175` becoming one net, with
one driver (tc2's NOR); `tc2_o5175` had none before.

Round 2: no findings.

## Corrections (coordinator, from the handoffs of 2026-11-19)

- `ports.d/tl6.txt`, `rst_ck M 6099-6111,6350 ?`: driven from the south (`rst_ck`, `eof` run 2): `in`.
  the wire `tl4` called w4590 (x 6016 at y 6350) is probably the wire `tc2` called sr_g (it is, and the net is `ck_out`: `tl4` runs 11-12) (`lc1`: "followed straight to y 6150"): not checked.
- The net that clears `tl5`'s latch c is also the 4-bit counter's pass-gate line `c4l_gab` (`tl3` run 11).

## Corrections (coordinator, from the handoffs of 2026-11-19, fourth batch)

- The ports `c4l_l3`, `tl4_w5068`, `tl6_p6101` ("on under the wide metal band") go to `tc1`'s `c4l_l3`, `tl4_w5068`, `tc1_bus2814` by three nested polys under the plane (`tlb` run 1).
- `lc3_w9947` (`tc2`'s metal x 6447 / `tcw`'s gate line; "not followed further"): followed south (`eof` run 13, piece `ck5`): it is the clock of the left-centre ripple counter; the net's canonical name is `lc3_w9947`, and `trace/tl6.txt`'s alias line was changed for that by `eof` (commit a9233e9, no geometry).
- The signal on track A / line X / the first through line of the left-centre strips, which these notes call a clock, a strobe "once per scan line" or leave without a source, **is the reset**: `rst_a`, the buffered copy of `rst` = NOR(`lpstb_b`, `res_b`) made by `lc1`'s gate 5 (`eof` run 10, piece `isrc5`, firm). `rst_ck`, `rst_rc` and `rst_lat` are further buffered copies of it: high while the RES and LPSTB pins are both low, and only then. The belief "a strobe once per scan line" is withdrawn.

## Corrections (coordinator, from the handoffs of 2026-11-20, third batch)

- Ports, `rcs_mv` poly (6226-6246, 6350), direction "?": it is an output. The net is driven in `tl3` (`rcs_mv` = NOR(`tl3_w4546`, `tl3_e4852`)) and runs on south to a pad (6232,6911) and down the whole left bus field to loads south of y 15000 (`busl`, piece `fc`; `bl0` run 9).
- The metal x 6016 that ends at (6016,6350) is one metal with the one `lc1` starts at (6016,6900) (`tl4` run 11: 550 px over nine poly rows, no pad): the net is the buffered clock `ck_out`.
