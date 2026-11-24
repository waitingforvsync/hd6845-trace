# regs: which central-column row is which register (follow tasks from `sel` / `bd3`)

Trace: `trace/regs.txt`. Scratch: `cache/scratch/regs/` (`survey.md`). Started 2026-11-19 14:55 -0600.

## Status

- **Piece 1, the write strobes of R12-R15: traced** (2026-11-19 15:06 -0600). Four wires, no
  transistor, from where `bd3` leaves them (y 17300) to the write line of one register row each.
  Full extraction: 2378 nets (four joins), 4351 transistors, 0 errors, 0 warnings.
- `wr_r12`'s join rests on one uncertain item (a `?M`, Ambiguities 1); the other three joins have
  none (`tools/unsure.py` lists only `wr_r12`). `wr_r12` has a contact onto an undrawn structure in
  `bw`'s region, and `wr_r14` possibly one (Ambiguities 1).
- **Piece 2, the read selects of R14-R17: traced** (2026-11-19 15:29 -0600). Four wires, no
  transistor, from `bd3`'s lines (y 17300) to `cdp4`'s four selector lines as `busl` drew them
  (tracks x 6538-6668, to y 15000). Full extraction: 2374 nets (four more joins), 4351 transistors,
  0 errors, 0 warnings. No uncertain item on these joins.
- **Piece 3, the buffered selects of R12 and R13: traced in two parts** (2026-11-19 15:44 -0600). South: from
  `bd3`'s poly ends along the bottom bus to the tracks x 6452 and x 6494 at y 14990, the south edge
  of the left bus field (`busl`'s claimed region). North: the same two wires from y 10400 to the
  west ends of `cdp3`'s read-gate rows `rsel12_buf` and `rsel13_buf`. **The 4,600 px between
  (y 10400-15000) are read with the follower and not drawn** (they are `busl`'s): two open joins.
  Full extraction: 2374 nets, 4351 transistors, 0 errors, 0 warnings (no new net: each part lies on
  a net that exists).
- **Piece `w8450`, "the wire of the seventh row": traced** (run 4, 2026-11-20 23:20 +0100; richtw1's
  session, on Fable). It is not a register wire: it is **`lc2_w8450`**, the reset copy that `bl0` left
  at a port in the bottom-left logic (4930,16713). One wire, no transistor drawn, thirteen pads with
  contacts and six poly links, from that port to a thin metal track x 10485 that goes north into the
  bottom-centre logic's east gate column (drawn to y 17760). No uncertain item on it. Full extraction:
  2462 nets (no new net: the wire lies on a net that exists), 4594 transistors, 0 errors, 0 warnings.
- **Piece `r9`, the ninth row y 17648: traced** (run 5, 2026-11-21 19:26 +0000; Kieran Connell's session,
  on Fable). It is not a register's select either: it is a bottom-bus line, **`rd_b7`**, that ends as
  the gate of an undrawn inverter under the south end of `bd3`'s ground rail (x 15560-15900,
  y 17370-17530): **`d7_out_n` = NOT `rd_b7`** (two transistors: pull-down 46/20, depletion load
  24/54; no uncertain item). The wire is drawn from the bus pad (12806,17907) to the gate (two hops, four
  pads with contacts), and the output from the inverter to a pad (16773,18012) at the foot of the track
  x 16776 (two pads with contacts); both go on (ports): the bus metal y 17907 west of x 12770, the output's
  poly row y 18012 east of x 16800. Full extraction: 2525 nets, 4754 transistors, 0 errors, 0 warnings
  (two new nets, two new transistors; no join to a named net).
- **Piece `n0`, the source of `rd_b7`: traced** (run 6, 2026-11-21 19:54 +0000; Kieran Connell's
  session, on Fable). **`rd_b7` is bus N, column 0** (`rd_b7` = `cdp4_n_s0`): the bus metal runs
  west from (12770,17907) to a corner (11200,17911) and north on the track x 11200 of the bus field east of
  the central datapath, 7,245 px, through a pad (11200,13330) that ends `cdp4`'s row y 13333 (`cdp4_n_s0`,
  the R14-R17 selector's node of slice 0) to its end on a pad (11200,10664) that ends `cdp3`'s row y 10664
  (`rd_b7`, the read bus of rows C and H, R12 and R13). So the inverter of run 5 is **`d7_out_n` =
  NOT `rd_b7`: the first stage of the read path of R12-R17, column 0**, firm (`tools/unsure.py
  --equations d7_out_n`: no uncertain item). Wiring only: two pads with contacts, two poly rows, no
  transistor. Full extraction: 2523 nets (two joins), 4782 transistors, 0 errors, 0 warnings.

## Inventory

| What | Where | Notes |
|---|---|---|
| Eight rows west from `bd3`'s tracks | y 17302, 17345, 17388, 17432 (strobes); 17475, 17519, 17562, 17604 (read selects, not drawn) | each track of x 15214-15517 turns west at its row; pitch 43.3 |
| Hop under trunks' X and the VCC rail | x 14456-14714 | poly between pads: east pad x 14714 (rows 17302, 17388) or 14672 (17345, 17432), west pad 14497 or 14456. Straight: eight rows in, eight out, same y (3x, `metal` and `acid1b`) |
| Hop under the vertical trunks | x 12805-13430 | poly between pads 13386 / 13430 and 12805 / 12850, straight (1.85x, both shots); the same cross-under as `wrs`'s four rows above |
| `wr_r13`'s hop | x 11375, y 17340-17428 | poly between two pads under `wr_r15`'s row (4.5x, both shots) |
| Nest west and north | x 11245-11463 | the four lines turn north at x 11463 / 11418 / 11375 / 11331, step 88 px west at y 14785 / 14824 / 14868 / 14915, and run north inside `wrs`'s four |
| Diagonals | (11331,10709)-(10895,10273) `wr_r14`; (11375,10688)-(10938,10251) `wr_r12` | parallel to `wrs`'s; placed by `follow.py --max` in stages, overlay at 1.85x |
| Ends | pads (10935,9532), (11243,10705), (10893,8819), (11243,11830) | each a metal contact on the east end of a poly row |
| Read selects: first diagonals | pads (11942,17470), (11984,17514), (12027,17558), (12068,17602) to pads (11592,17730), (11555,17773), (11592,17818), (11552,17862) | four parallel poly diagonals south-west under the clock lines, x + y = 29368, 29434, 29503, 29565 (measured on cuts of the clean shot); order kept (4x, both stripped shots) |
| Second diagonals | pads (11238,17732), (11282,17776), (11324,17819), (11365,17863) to poly rows y 18036, 18080, 18122, 18166 | x + y = 28956, 29023, 29088, 29153. Six diagonals run here; ours are the upper four (the other two start on pads (11350,17945), (11305,17990)) |
| Third diagonals | rows y 18036-18166 at x 10333-10400 to pads (10182,18165), (10138,18210), (10182,18252), (10225,18297) | x + y = 28369, 28438, 28501, 28566. **Seven** rows arrive at x 10450: the top one (y 17990, from a pad (10470,17985)) is another wire and takes the pad (10138,18120) and the metal row y 18124; each of ours lands three rows further down than it arrived (3.2x clean, 5x chip-2 stripped) |
| Straight hops on the rows y 18168, 18212, 18255, 18299 | x 9550-9808; 8382-8638; 7385-7600 | poly between pads under one or two vertical metals; rows straight (1.8x, 3.4x, 2.9x in `metal` and `acid1b`) |
| Corners and tracks | x 6668, 6626, 6582, 6538, y 16515-18299 | each row turns north (nested: the northernmost row takes the easternmost track) |
| Vertical hop | y 16168-16558 | poly between pads under the horizontal metal rows y 16260-16480: pads (6668,16210)/(6668,16558), (6624,16168)/(6626,16515), (6581,16210)/(6582,16558), (6538,16168)/(6538,16515); five columns hop here (the fifth, x 6711, is `eof`'s `bd1_n2` track), all straight (2.7x, both shots) |
| Tracks north | y 15000-16168 | metal to `busl`'s south edge, where `rsel14_buf`, `rsel15_buf`, `rsel17_buf`, `rsel16_buf` (`cdp4`'s selects 1-4) are drawn; six poly rows cross at y 15070-15190 without a contact |
| `lc2_w8450`: poly row from `bl0`'s port | x 4930-5853, y 16703-16723 | straight; under a wide metal x 4950-5020, `bl0`'s six tracks and their neighbours (x 5100-5360), in the 25 px gap between two horizontal metals at x 5420-5540, open at x 5550-5720, under three tracks to a corner (2.5x in `metal`, `acid1b`, `acid`: `a1.png`, `a2.png`; the gap stretch at 3x in four shots, `a4.png`) |
| Corner and second row | column x 5837-5853, y 16703-16810; row y 16791-16810, x 5837-6065 | open poly between the metals x 5815 and x 5865 (orange in both metal shots: `px.py row 16760 5822 5868 2 all`, `px.py col 5845 16700 16830 4 metal,acid`); the row passes under the track x 5855-5875 without a ring, through the pad (5909,16800), and ends under the rail x 6008-6055 as a band between two diffusions (not drawn) |
| Metal x 5910, poly row y 17018 | y 16800-17019; x 5907-6408 | thin metal (22 px wide) between pads (5909,16800) and (5907,17019), over two poly rows of other nets (y 16870-16890, 16920-16940: edge bars only); poly row straight under the rails x 6015-6065 and x 6190-6238 and the tracks x 6280, 6320 (2.2x, three shots, `o2.png`) |
| Track x 6408 | y 17017-18126 | thin metal between pads (6408,17017) and (6408,18126); `tl5_tracks.py v 6408 17035 18108`: no stretch without metal in both chips (Ambiguities 3) |
| Poly row under the six tracks | x 6408-6712, y 18117-18133 | under the tracks of `rsel12_buf` .. `rsel16_buf` (x 6452-6668), no pad, no ring (3.3x, three shots, `o3.png`) |
| The seventh row | y 18125, x 6712-10137 | metal with the bus's three straight hops, pads 7382/7555, 8424/8641, 9596/9811 (each hop at 4-4.4x in both stripped shots: `h1.png`, `h2.png`, `h3.png`); `tl5_tracks.py h 18123 6600 10200`: metal at x 6740-7364, 7581-8405, 8669-9571, 9837-10117 |
| First of the third diagonals | pad (10137,18124) to pad (10484,17994) | poly east to x 10184, diagonal x + y = 28308, row y 17995 east (3x in both stripped shots, `o4.png`): the band above `rsel16_buf`'s |
| Track x 10485 | y 17994 north | thin metal from the pad (10484,17994), drawn to y 17760; north of that it passes over the boxes and rows of the gate column (Not done) |
| `rd_b7`: bus metal and its pad | metal y 17907 west of the pad (12806,17907) | `follow.py 12770 17907 W` runs it 1,594 px to (11200,17913): not followed. Pad: bright centre in both metal shots, greenish centre in the clean shot (`px.py row 17907 12780 12830 5 metal,metal1,acid1b`) |
| Hop under the vertical trunks, and up to the second pad | poly row y 17897-17917, x 12806-13224; poly north x 13206-13224 to the pad (13240,17862) | straight (2.6x in three shots, `w6.png`); the row above (y 17862, pads (12845,17862) and (13172,17862)) is another net, undrawn; the corner and both pads at 4x in four shots (`w4.png`) |
| Diagonal and row y 17648 | thin metal from the pad's east ring (13262,17857) on x + y = 31119 to the corner (13470,17649), east to the pad (14497,17648) | the diagonal lies beside and partly on `trunks`' poly diagonal of `rst_a` for 200 px, crosses that poly's row y 17815 (the follower's stop (13316,17803)) and its column x 13480: no pad, no ring (4x in four shots, `w2.png`, `w7.png`); the row passes over poly columns at x 13700 and 14195 (`r2.png`) |
| Hop under `trunks`' X and the VCC rail | pads (14497,17648), (14714,17648) | straight, between `rsel14_buf`'s row y 17604 and `rsel13_buf`'s y 17691, whose pads sit one position west (2x in four shots, `h1.png`; `tl5_tracks.py h 17648 14380 15600`) |
| Row east, corner, pad | metal y 17648 to x 15560, north to the pad (15558,17428) | no pad between (strip in three shots, `r1.png`); the pad: `px.py col 15560 17395 17460 5`, green hole at y 17429 (`tl5_tracks.py v 15560 17390 17670`) |
| The inverter | x 15577-15895, y 17372-17491 | pull-down: diffusion column x 15662-15708 under the ground rail's end (the rail's metal runs to y 17525; `bd3` drew it to y 17380), ground contact (15679,17391), gate band y 17418-17438, drain below; a tab west to a buried-contact box (15602-15640, 17449-17479); a neck east y 17452-17474 to the node land x 15752-15776; load plate x 15781-15835, y 17432-17491 over the strip y 17449-17473, tie box (15772-15804, 17400-17428), supply land x 15838-15895 with a contact (15864,17450) under the VCC rail (3.2x in four shots: `e3.png`, `e4.png`, `e6.png`; overlays `ov1.png`, `ov2.png`) |
| The output `d7_out_n` | poly x 15587 south, y 17646 east, x 15932 south to the pad (15971,17733); metal y 17735 east, corner x 16776, south to the pad (16773,18012) | the row passes under the VCC rail x 15795-15890 without a channel (`px.py row 17644 15770 15930 10`: 211-222/164-176 throughout); the metal passes over twelve poly columns, bars of 8-10 px only, no pad (`tl5_tracks.py h 17736 15990 16790`, `o5.png`); `tl5_tracks.py v 16776 17730 18030`: metal to the ring, green hole at y 18014 |
| Bus N column 0: the bus row west of x 12770 | metal y 17907-17911, x 11200-12770 | `tl5_tracks.py h 17909 11150 12790`: metal throughout, bars of 8-12 px where three poly lines cross (x 11222-11267, two of `regs`' own diagonals; x 12728-12760, a poly column), no hole in the clean shot; strip in three shots (`x2.png`) |
| Corner and the track x 11200 | corner (11200,17911); thin metal x 11194-11206, y 10664-17911 | the corner at 3.5x in four shots (`x3.png`); `tl5_tracks.py v 11201 10600 17900`: no stretch of 20 px without metal in both chips (bars of 8-17 px at poly rows and at the pad); centre x 11199-11201 at nine cuts (`px.py row`); six strips of 1,210 px in three shots at 1x (`t1.png`-`t6.png`): straight, the lines beside it step (y 14920) and it does not; it passes over the wide diffusion of Ambiguities 1 (y 11905-12185, no pad) |
| The pad in the run | (11200,13330), poly row y 13323-13343 west to `cdp4`'s row end at x 10850 | 3.5x in four shots (`c2.png`): metal on both sides of the ring in both chips (`px.py col 11200 13300 13360 4`), pad at the row's end, field east of it; the row at 3x (`p2.png`) and by text (`tl5_tracks.py rows row 10830 11230 5 13311 13322 13333 13344 13355`) |
| The end pad | (11200,10664), poly row y 10654-10674 west to `cdp3`'s row end at x 10850 | 3.5x in four shots (`c3.png`): the metal arrives from the south, bare ground north of the ring (`px.py col 11198 10640 10700 4`); the row at 3x (`p1.png`) and by text |
| Not drawn: a structure on `wr_r12`'s line | x 11320-11400, y 11740-12350 | Ambiguities 1 |

## Logic

No transistor. Four joins (extraction; names gathered by `@alias`, the renames are the refresh's):

| Strobe | Ends on | Row | Bits |
|---|---|---|---|
| `wr_r12` | `cdp3_c_wr`, pad (10935,9532) | `cdp3` row C, register cell x 6 (c2..c7) | 6 |
| `wr_r13` | row H's write line, pad (11243,10705) | `cdp3` row H, register cell x 8 (c0..c7) | 8 |
| `wr_r14` | the line drawn by `cdp3` at y 8819, pad (10893,8819) | the line into `cdp3`'s row A (six large cells c2..c7; its branches into the cells are not traced) | 6 (believed, from the row) |
| `wr_r15` | the strobe row y 11837 of `cdp4`, pad (11243,11830) | `cdp4` row R1, lower half: eight latches | 8 |

So, by their strobes: **R12 is `cdp3`'s row C, R13 its row H, R15 `cdp4`'s 8-bit latch row R1
(lower half); R14's strobe is the line into `cdp3`'s row A.** The widths agree with the data sheet
in all four (R12 and R14 six bits, R13 and R15 eight). Traced for R13, R14, R15; marked for R12
(Ambiguities 1). All of it rests on `sel`'s assignment of select lines to register numbers, as in
`wrs`.

### The buffered selects of R12 and R13 (piece 3)

| Select | Row after the third diagonals | Track at y 15000 | North end (by the follower through `busl`'s region) |
|---|---|---|---|
| `rsel13_buf` | y 18343 | x 6494 | `rsel13_buf`, pad (6730,10317): the gates of row F, which pass row H onto bus N |
| `rsel12_buf` | y 18387 | x 6452 | `rsel12_buf`, pad (6730,10055): the gates of row E, which pass row C onto bus N |

Route. `rsel12_buf`: `bd3`'s poly x 14199 ends on a pad (14195,17730); metal row y 17736 west, a
metal diagonal (13520,17736)-(13262,17994), pad (13212,17993); poly under the vertical trunks to
pad (12805,17995); metal to the sixth pad of the second diagonals (11305,17990); poly diagonal
(x + y = 29284) to the poly row y 18250; third diagonal (28698) to pad (10225,18385); metal row
y 18386 with the three straight hops (pads 9808/9592, 8638/8425, 7558/7385); north on x 6452; the
vertical hop (pads y 16515 / 16168); north to y 14990. `rsel13_buf`: `bd3`'s poly x 15512 ends on a
pad (15512,17688); metal row y 17691 west through the rail hop (pads 14672/14456), a metal diagonal
(13501,17692)-(13241,17952), pad (13168,17950); poly to pad (12850,17950); metal to the fifth pad
(11350,17946); poly west to x 11271 and diagonal (29219) to the row y 18208; third diagonal (28632)
to pad (10267,18340); metal row y 18342 (pads 9764/9550, 8597/8382, 7600/7428); north on x 6494;
vertical hop (y 16558 / 16210); north to y 14990.

The stretch not drawn, as the follower gives it (`follow.py X 15500 N`, both chips; one 4x view of
the corners at y 12050-12170, `q5.png`): x 6452 north to (6454,12986), east to (6516,12979), north
to (6521,12099), east along y 12095 **on top of `busl`'s poly row `cdp4_bus_s2`** (no pad, no
contact seen: trap 13), a corner north at x 6690, and north to y 10400. x 6494 north to
(6501,13024), east to (6565,13023), north to (6562,12141), east along y 12140, north at x 6735 to
y 10400. **Each track has one tap on the way** (found by review round 4, confirmed by `textmap.py`:
a bright centre, red 176-220, in a dark ring about 34 px across in both metal shots, on a widened
poly pad): track x 6494 (`rsel13_buf`) at (6492,13744), the west end of the poly row y 13744, and
track x 6452 (`rsel12_buf`) at (6450,13852), the west end of the poly row y 13852. Both rows run
east to about x 7545 beside the four select rows of `cdp4` and, by `busl`'s notes, end as gate bands in
the gate group at `cdp4`'s bottom-left corner (not read here). So that group takes six select
rows (R12-R17's), not four. North of y 10400 (drawn): x 6690 steps east at y 10270 to x 6733 and ends on the pad
(6730,10055); x 6733 ends on the pad (6730,10317); each pad's poly row runs east to `cdp3`'s edge
(x 7600) under about twenty vertical metals without a pad (1.36x, both stripped shots).

So, **if the middle stretch is as the follower gives it: R12's buffered select reads row C and
R13's reads row H onto bus N**, the same rows their write strobes end on (piece 1): R12 = row C
and R13 = row H from two independent directions, which also supports the marked `wr_r12` join.
Marked, not firm: the two joins are open until the middle is drawn.

### The read selects (piece 2)

| Select | Row after the third diagonals | Track | Joins | Selector source (`cdp4`) |
|---|---|---|---|---|
| `rsel16_buf` | y 18168 | x 6668 | `rsel16_buf` | c: the 6-bit latch row D (s2..s7) |
| `rsel17_buf` | y 18212 | x 6626 | `rsel17_buf` | d: the 8-bit latch row C |
| `rsel15_buf` | y 18255 | x 6582 | `rsel15_buf` | b: the 8-bit latch row R1, lower half |
| `rsel14_buf` | y 18299 | x 6538 | `rsel14_buf` | a: the 6-bit source from above row R1 (s2..s7) |

So **`cdp4`'s four-way selector is the read multiplexer of R14-R17** (traced: the four joins).
Two things agree with it that were found separately: the widths (R14 and R16 six bits, R15 and R17
eight), and R15, whose write strobe `wr_r15` ends on the same latch row (R1, lower half) that
`rsel15_buf` selects for reading. Rows C and D, loaded together by `bc1_ld_n` (`busl`), are then
R17 and R16, the light pen register (believed, from the data sheet: read only, 14 bits latched by
one event). The 6-bit source a is R14 as read; that it is `cdp3`'s row A, which `wr_r14` strobes,
is not traced (`cdp4` row R1's upper half).

`cdp3`'s notes had `wr_r13` running "on east past x 10990 without a contact": it ends on the
pad (11243,10705). `cdp4`'s strobe row (`wr_r15`, drawn there to x 10600, "ends not examined")
is one poly row y 11824-11844 east to the pad (11243,11830) (`tl5_tracks.py rows` in the clean
shot: poly all the way, field on both sides).

### `lc2_w8450` to the bottom bus (piece `w8450`, run 4)

No transistor. One join, by geometry: the wire starts on `bl0`'s poly row (its port (4930,16713),
the row of the pad (4823,16713) at the foot of the left bus field's track x 4822), so the whole wire
is **`lc2_w8450`** = NOT `lc1_w7170` (`lc2`'s equation, marked there for its own uncertain box): the
data of the left-centre latch B and the clear of the ripple counter's stages, a copy of the reset in
`rst`'s sense. `tools/unsure.py`: nothing new joined through an uncertain item (the wire has none).

Route, west to east: poly row y 16713 east to a corner (5845,16713); poly column south; poly row
y 16800 east through the pad (5909,16800) to its end under the rail x 6008-6055 (below); from the
pad a thin metal south to the pad (5907,17019); poly row y 17018 east to the pad (6408,17017); the
track x 6408 south to the pad (6408,18126); poly row east under the six select tracks to the pad
(6712,18124); the metal row y 18125 east with three hops to the pad (10137,18124); poly east and
north-east (the first of the third diagonals) and along y 17995 to the pad (10484,17994); the thin
metal x 10485 north.

**Two ends, both gates, both in logic nobody has traced (seen, not drawn):**

- West: the row y 16791-16810 ends as a band under the supply rail x 6008-6055 of the bottom-left
  logic, between a diffusion with the rail's contact (6030,16845) below it (y 16815-16870) and a
  diffusion above it (y 16755-16790) that goes west, by a patch (5990-6005,16758-16772), to a
  heavy-outlined box (5953-5990,16748-16785) (clean shot at 5.6x, `b2.png`; four shots at 2.8x,
  `b1.png`). So it looks like the gate of one pull-down of a unit of `bl1`/`bl2`. `railprof.py 6008
  6048 16500 17100` calls the band "poly over field" between two diffusions (its colour test; the
  band has a dark diagonal mark on it in the clean shot). Believed a gate, not drawn: the unit is
  the bottom-left logic's. The poly's tip is an orange nub to x 6065 beyond the rail's east edge. The
  diffusion above the band also leaves the rail east, as a strip x 6072-6092, y 16745-16812 (beside
  the tip x 6080-6092: chip-2 metal 155-168/112-128/78-85, plain, and the chip-2 stripped shot red
  over green by 15-19, `px.py row 16796 6044 6100 2 all`); between the tip and the strip are 12-14 px
  of dark in both metal shots, read as two edge lines with no buried contact (no box, no lighter
  centre, and the poly does not cross the strip): found by review round 5, for whoever draws the
  pull-down.
- East: the track x 10485 runs north beside the gate column of the bottom-centre logic's east part
  (rail x 10550-10600). `tl5_tracks.py v 10486 16300 17990`: stretches without metal in both chips at
  y 17716-17755, 17457-17549, 17326-17363, 17152-17188, 16914-17074, 16805-16840, 16673-16710,
  16500-16553 and none at all north of y 16300. The first two were looked at (4.8x and 7.5x, four
  shots: `s12.png`, `c4.png`, `c4b.png`; `textmap.py 10456 17696 10516 17768 3 --acid`): the metal
  goes dark over a heavy-outlined box at the west end of a unit (y 17715-17750, y 17455-17495), with
  no bright centre, no green hole and no widening, and is seen again beyond: pass-overs (traps 22,
  27), so the track goes on north past at least two units. Its loads are not found.

So what this piece establishes: **the reset copy `lc2_w8450` is taken from the left bus field across
the bottom of the chip into the bottom-centre logic's east gate column, with one gate load in the
bottom-left logic on the way** (traced: the wire; believed: that the west end is a gate; open: every
load at the east end).

### The ninth row and its inverter (piece `r9`, run 5)

Traced: `d7_out_n` = NOT `rd_b7`.

- **`rd_b7`** arrives on the bottom bus (metal y 17907; its source is west of x 12770, not followed),
  hops east under the vertical trunks in poly, climbs to the row y 17648 on a thin diagonal metal, hops
  under `trunks`' X and the VCC rail like the eight rows above it, turns north at x 15560 and ends on a
  pad (15558,17428), whose poly runs east as the gate band y 17418-17438 of one pull-down. No tap, no
  other transistor on the way.
- **The inverter** stands south of `bd3`'s R13 select buffer, on the same two rails. Pull-down 46/20 under
  the south end of the ground rail; depletion load 24/54 at the west edge of the VCC rail, its plate tied
  to the node land by a buried contact at the plate's top-left corner. The drain reaches the load by a
  diffusion neck east and the output poly by a tab west and a buried contact.
- **`d7_out_n`** leaves on poly (south, east under the VCC rail, south) to a pad (15971,17733), runs
  east on the top line of a bus of thin metals (y 17735) to a corner at x 16776, south to a pad
  (16773,18012), and on east as a poly row y 18012 under `e_b`'s track and a wide rail to a pad seen at
  (17065,18010) with a metal on east (1.28x, `o4.png`): not followed.

Believed, not traced: nothing about what the signal is. It is one more line of the bottom bus that passes
the strobe logic; its row lies directly below the eight rows of the register strobes and read selects only
because they share the hop.

### Bus N, column 0, to the inverter (piece `n0`, run 6)

Traced, firm: **`d7_out_n` = NOT `rd_b7`.**

`rd_b7` of run 5 is one net with `rd_b7` and `cdp4_n_s0` (aliases in `trace/regs.txt`; the rename is
the coordinator's refresh). The net now reads, in the full extraction: six read transistors (gates
`rsel12_buf` .. `rsel17_buf`: rows C and H of `cdp3`, the four ways of `cdp4`'s selector), the pull-down
gated by `cdp4_rst` = NOR of the six selects, and one load: the gate of this inverter. So bus N's column 0 is
precharged or held low (by `cdp4_rst`) while no register of R12-R17 is selected, takes the selected
register's bit, and leaves the datapath by the track x 11200 and the bottom bus to an inverter beside the
R13 select buffer, whose output `d7_out_n` goes east toward the data bus column (not followed).

Believed, not traced: the other seven columns do the same. The upper staircase of pads (y 10361-10664, the
east ends of `cdp3`'s rows `rd_b7` .. `c7`) and the lower one (from (11200,13330), `cdp4_n_s0` .. `s7`)
put the eight columns on eight tracks of this bus field (`bw`'s survey says so); the rows through the hop
x 14456-14714 below `rsel12_buf`'s (y about 17777, 17823, 17865, 17905) and the unit east of the VCC rail
beside this inverter are probably theirs. Which data bit column 0 is, is not established here.

## Ports

| Name | Layer | Where | Direction | What |
|---|---|---|---|---|
| `wr_r12` | metal | 15214,17290 | in | from `bd3`'s line on T7's position |
| `wr_r14` | metal | 15258,17290 | in | from `bd3` |
| `wr_r15` | metal | 15301,17290 | in | from `bd3` |
| `wr_r13` | metal | 15344,17290 | in | from `bd3` |
| `wr_r12` | poly | 10835,9533 | out | onto `cdp3_c_wr` |
| `wr_r14` | poly | 10835,8818 | out | onto `wr_r14` |
| `wr_r13` | poly | 10835,10709 | out | onto `wr_r13` |
| `wr_r15` | poly | 10590,11835 | out | onto `wr_r15` |
| `rsel16_buf`, `rsel17_buf`, `rsel15_buf`, `rsel14_buf` | metal | (15388 / 15431 / 15474 / 15517, 17290) | in | from `bd3`'s lines |
| `rsel16_buf` | metal | 6668,14990 | out | onto `busl`'s `rsel16_buf` |
| `rsel17_buf` | metal | 6624,14990 | out | onto `rsel17_buf` |
| `rsel15_buf` | metal | 6581,14990 | out | onto `rsel15_buf` |
| `rsel14_buf` | metal | 6538,14990 | out | onto `rsel14_buf` |
| `rsel12_buf` | poly | 14199,17290 | in | from `bd3`'s poly |
| `rsel13_buf` | poly | 15512,17490 | in | from `bd3`'s poly |
| `rsel12_buf` | metal | 6452,14990 | out | into `busl`'s region: track x 6452, undrawn there |
| `rsel13_buf` | metal | 6494,14990 | out | into `busl`'s region: track x 6494, undrawn there |
| `rsel12_buf` | metal | 6690,10400 | in | from `busl`'s region: believed `rsel12_buf` |
| `rsel13_buf` | metal | 6733,10400 | in | from `busl`'s region: believed `rsel13_buf` |
| `lc2_w8450` | poly | (4920-4930, 16703-16723) | in | from `bl0`'s poly row (its port (4930,16713)) |
| `lc2_w8450` | poly | (6008, 16791-16810) | out | the band under the rail x 6008-6055: believed the gate of a pull-down of the bottom-left logic (undrawn); the poly is drawn to its end, x 6065 |
| `lc2_w8450` | metal | (10479-10491, 17760) | out | the track x 10485 on north beside the bottom-centre logic's east gate column: not followed (Not done) |
| `rd_b7` | poly | (10840, 10654-10674) | in | `cdp3`'s row y 10664 (its east piece of s0, drawn there to x 10850): bus N column 0 (run 6; replaces run 5's port of `rd_b7` at (12770,17907)) |
| `rd_b7` | poly | (10840, 13323-13343) | in | `cdp4`'s row y 13333 ("s0: n out to the right", drawn there to x 10850): `cdp4_n_s0`, the same net |
| `d7_out_n` | poly | (16800, 18003-18021) | out | the poly row y 18012 on east under `e_b`'s track and a wide rail to a pad seen at (17065,18010): not followed |

## Ambiguities

1. **The structure at x 11320-11400, y 11740-12350 on `wr_r12`'s and `wr_r14`'s lines** (in `bw`'s
   region; nobody has drawn it). A wide diffusion-coloured rectangle x 10530-11400, y 11915-12185
   with seven contacts in a column at x 10540 (west end, beside `cdp4`'s s7 supply rail) has two
   mirrored units at its east end (sharpened clean shot, `g4.png`, `g6.png`). Top unit: a poly
   plate x 11325-11393, y 11838-11893 over the rectangle's neck; a strip of the rectangle's colour
   x 11358-11375 from the plate north to y 11757, turning east along y 11742-11756 (seen to
   x 11480, not followed); a heavy-outlined box (11325-11343, 11798-11820) joined to the plate's
   west part, under `wr_r14`'s metal. Bottom unit: plate y 12205-12260, a U-shaped strip down to
   y 12342, box (11373-11392, 12283-12300) joined to the plate's east part, under `wr_r12`'s metal.
   - **`wr_r12` contacts the bottom box at (11378,12297): drawn** (found by review round 1). Both
     metal shots have a bright centre 12 px across (red 220) in a dark ring; the clean shot has a
     green hole (154/168/117; `textmap.py 11356 12274 11404 12320`). So the bottom unit's plate is
     on `wr_r12`. The plate itself is not drawn.
   - **`wr_r14` may contact the top box at (11331,11810): drawn `?C` on a `?P` box.** The same ring
     and bright centre in both metal shots; the clean shot reads 152-178 / 146-160 / 95-103 (red
     minus green 6-18, never greener than red; +6 to +30 by the fix check), and the chip-2 stripped
     shot is red over green by 35-50 at the centre, where the real contact on `wr_r12` is
     grey-green: it leans toward a pass-over (trap 26), not a contact.
   - **`wr_r12` at y 11757-11905: drawn `?M`.** The line's two edge lines (x 11364, 11386) run
     through in both chips, the interior is dim (red 100-160 against 215-240 north and south of
     it), and the clean shot east of the centre line is protected without a break (`px.py col
     11383`). So the metal is there, and one net is the better reading (reviewer and tracer); it
     cannot be shown unbroken from these photos (traps 22, 27). No contact is seen at the north
     end (11376,11750): bright metal between the two edge bars of the strip's east arm, no hole.
   What the units are is not read. With the plate on the strobe that passes over its box, each
   looks like an extra pull-up on one long strobe line (a depletion load whose plate is its
   output, fed from the rectangle as a supply cross-under): believed only. If instead they are
   transistors gated by the strobes, the strips are two more nets (the top one leaves east along
   y 11748). Either way `wr_r12` reaches row C's write line by its own metal; what would settle
   the rest is tracing the two units, the strip east along y 11748 and the contact column at
   x 10540 (`bw`).
2. **Green stretches under the read selects' tracks** (`tl5_tracks.py v`): (6538, 16115-16150),
   35 px, just north of the hop's pad, where the clean shot has interference colours over an area
   wider than the track; (6626, 17203-17436) and (6626, 17456-17528), (6668, 17446-17496), far too
   long for contacts. Read as not contacts; no pad or ring in the metal shot at 2.7x for the first.
   The same value at x 6917 on all four rows (8-9 px) is one vertical feature beneath, not four
   contacts.
3. **The track x 6408 at y 17580-17625** (piece `w8450`). Chip 1's metal shot has two dark blobs on
   the track (y 17580-17595, 17605-17622: `tl5_tracks.py v 6408 17035 18108` gives "chip 1 fails
   17604-17623"), and chip 1's clean shot interference colours and two blue-green specks there. Chip
   2's metal shot has full-bright metal with straight edges through both (`textmap.py 6388 17585
   6430 17640 3`; four shots at 3x, `f1.png`), and its stripped shot is plain. Read as damage on
   chip 1's surface: no ring, no pad; the metal is one piece. The follower's contact candidate
   (6409,17603) is the same place.
4. **The pad (5907,17019)'s centre in chip 2** (piece `w8450`). Dark ring about 40 px across in both
   metal shots and a pad box in both stripped shots, but the centre is bright only in chip 1 (red
   160-235; chip 2 96-150: `textmap.py 5880 16992 5936 17046 3 --acid`). Read as a contact with dirt
   on it in chip 2: the thin metal from the north ends squarely on the ring and the poly row leaves
   east.
5. **Crossings read as no contact** (piece `w8450`): the track x 5855-5875 over the row y 16800 at
   (5865,16800) (bright across, edge bars only: `s19b.png`, `s20b.png`); the wide metal x 4950-5020
   over the row y 16713 (a dark mark at (4990,16712) is in chip 2's metal shot only: `a3.png`); the
   dark dots on the poly rows at x 6248 (row y 17018) and at x 6470, 6515, 6560, 6603, 6647 (row
   y 18125) and 10330, 10375, 10420 (row y 17995) lie in the gaps between two metals (trap 2), with
   no metal above; two clean-shot specks on the metal row at (6808,18123) (the edge of a poly column
   beneath) and (8912,18126) (chip 1's clean shot only; metal D-E across in both chips:
   `textmap.py 8894 18108 8932 18144 3`); the metals x 10255-10270 and x 10300-10400 over the
   diagonal and the row y 17995 (no pad on the poly, trap 15).
6. **Crossings and strips of piece `r9`** (run 5).
   - `rd_b7`'s thin metal lies beside and partly on `trunks`' poly diagonal (`rst_a`) from about
     (13465,17655) to (13330,17790), crosses that poly's row y 17815 at (13316,17803) and its column at
     (13480,17648). Read as no contact: no pad, no ring, the metal keeps its width (4x in four shots,
     `w2.png`, `w7.png`; traps 13, 15). The metal is dim where it lies on the poly (it fails the metal test at
     x 13470-13440 and x 13350: `px.py col`), bright between; one metal from corner to pad.
   - The two narrow strips of the drain (tab x 15640-15662 and neck x 15712-15752, y 17452-17474; 14 px
     between their edge lines) are read as diffusion: blue 83-91 in chip 2's metal shot and 77-80 in chip
     1's against 58-70 and 39-54 for the open poly beside them, and darker and redder than the field
     control (15630,17510) in all four shots (`px.py pt`; survey). `textmap.py 15565 17440 15650 17500 3
     --acid` reads the west tab strongly red over green in the chip-2 stripped shot, like poly. If the tab
     were poly the box would still join it to the drain or not at all; the reading "drain - box - output
     poly" is the ordinary one (a box with a heavy outline between a diffusion and a poly).
   - The dark dot on the ground rail's metal at (15688,17497) is in chip 2 only; the clean shot is plain
     field there (147/140/112 from y 17480 to 17525, `px.py col 15685`). No contact.
7. **Crossings of piece `n0`** (run 6), all read as no contact. The two poly rows (y 10664 and y 13333)
   each pass under eight vertical metals of the bus field between x 10850 and the pad: the dark dots on the
   rows lie in the gaps between the metals (trap 2), no metal has a widened pad there (3x, `p1.png`,
   `p2.png`; trap 15). The track x 11200 passes over poly rows at y 10700-10722 (`cdp3`'s row H write line),
   11819-11850 (`wr_r15`'s row to its pad (11243,11830)), 14551-14583, 16373-16406 (a row ending on a pad
   (11240,16388) of the next line east: 3.5x in four shots, `c1.png`; the track keeps its width, the clean
   shot is uniform salmon under it) and the rows and diagonals of the bottom bus at y 17458-17877, and over
   the wide diffusion of Ambiguities 1 at y 11905-12185: bars of 8-14 px only, no widening, no hole
   (`tl5_tracks.py v 11201 10600 17900`). Chip 1's metal shot has blemishes on the track at y 15230 and
   y 15650-15760 (chip 2 is plain there; the clean shot, chip 1's, has interference colours at the same
   places: `t4.png`, `t5.png`).

## Review

**Round 1, full review, 2026-11-19 15:16 -0600** (fresh Fable reviewer; piece 1, at commit 8e1aa03; 24
images in `cache/scratch/regs/review-1/`). Told to suspect: `wr_r12` across the structure and
over its mirrored unit, `wr_r14`'s metal there, the order of the nests at the corners y 14785-14915
and the turns, the two diagonals, both poly hops, the four end pads and their rows, `wr_r13`'s hop.
Checked at 3.2-5x in `metal`, `metal1`, `acid1b` (hops not in `acid`), with `px.py`, `textmap.py`,
`tl5_tracks.py` and 0.9x views of the long runs: corners, turns, diagonals, the 44 px step, both
hops (eight rows straight), the end pads (a hole each, no metal beyond), the rows y 10709 and
y 11835 (continuous, no pads under the crossing metals), no contact where `wr_r14` crosses row C or
at a poly end beside `wr_r12` at y 12905; a ring at (13218,17425) is in chip 2 only, not a contact.
Could not check: what the two units are; `bd3`'s names; the rows west of x 10570 / 10825.
Findings:
1. Undrawn contact on `wr_r12` at (11378,12297). **Changes a connection** (a contact exists).
   Confirmed by the tracer (`px.py pt`, `textmap.py`): drawn, with the box.
2. Probable contact on `wr_r14` at (11331,11810), borderline in the clean shot. Would change a
   connection. Undecidable: drawn `?C` on a `?P` box, Ambiguities 1.
3. `wr_r12` at y 11757-11905: the metal is there (edge lines through, interior dim); the notes'
   "no metal" was wrong and the `?M` too narrow. Geometry only: `?M` widened to 14 px, notes
   corrected.
`tools/t.sh regs sameconn.py 8e1aa03`: `connections identical`. `.venv/bin/python tools/sameconn.py
8e1aa03`: `connections identical` (the plate the new contact lands on is not drawn, so the
extraction does not change; the finding still counts, because a contact was added).
Round 1: three findings, fixed (one contact added, one marked uncertain, one geometry).

**Round 2, fix check, 2026-11-19 15:20 -0600** (fresh Fable reviewer; the changes since 8e1aa03, at
commit 81387d1; three images in `cache/scratch/regs/review-2/`). Change 1 (contact on `wr_r12`):
right; bright centre red 214-229 in both metal shots, green hole red minus green -9 to -18 (the
pad (11243,11830) reads -8 to -25), box is poly as drawn. Change 2 (`?C` on `wr_r14`): uncertain is
the right call, and the photos lean against a contact (no green hole; poly-red in the chip-2
stripped shot); the trace's comment and Ambiguities 1 now say so. Geometry only (a comment).
Change 3 (`?M` 14 px): right, inside the two edge lines, 25 px clear of the `?P` box and of the
metal on x 11331. `tools/t.sh regs sameconn.py 8e1aa03`: `connections identical`.
`.venv/bin/python tools/sameconn.py 8e1aa03`: `connections identical`. After the comment fix,
against 81387d1: both `connections identical` again.
Round 2: no findings that change a connection.

**Round 3, full review of piece 2, 2026-11-19 15:35 -0600** (fresh Fable reviewer; the four read selects, at
commit 1c5b259; 28 images in `cache/scratch/regs/review-3/`). Told to suspect: the third diagonals
(seven rows, an off-by-one), the second and first diagonals, every straight hop, the vertical hop,
the corners, the tracks to y 14990 and the green stretches of Ambiguities 2, the ends on `bd3`'s and
`busl`'s metals, missed taps. Checked: the third diagonals at 4x in `acid1b` and `acid` (five
separate bands to five pads, ours bands 2-5, no off-by-one); the poly rows x 10440-10920 on 13
cuts; the second diagonals at 2.8-4x (six from six pads, ours the upper four); the first diagonals
at 2.4x in three shots (separate in the chip-2 stripped shot, where the debris is absent); all hops
at 2-4x with text rows; the vertical hop at 2.8x; the corners; `tl5_tracks.py` on every straight
metal piece (no stretch over 18 px without metal in both chips); the green stretches (interference
colour, unbroken metal, no ring); no taps (about 1x metal); both ends. Not checked: the second
diagonals under metal at 4x except one passage; the long runs at high zoom; `metal1` as an image.
Round 3: no findings.

**Round 4, full review of piece 3, 2026-11-19 15:53 -0600** (fresh Fable reviewer; at commit 49ae634; images
in `cache/scratch/regs/review-4/`). Told to suspect: which wire is which through the second and
third diagonals, the two metal diagonals, every hop, the two poly columns from `bd3`, the undrawn
middle stretch, the north ends, missed taps and the green stretches. Checked at 4-4.6x in two or
three shots: the poly columns (contacts only at the end pads), the rail hop, the second and third
diagonals (no band swapped or shared), the three row hops and the vertical hop, the north ends
(both pads are contacts; the step at y 10270 is 10 px clear of the lower pad; rows continuous to
x 7615, no pad); at 2.8-3.1x the trunk cross-under and the metal diagonals; the green stretches (no
ring). Not checked: the north rows above 2.8x; the long runs except by `tl5_tracks.py`.
Drawn geometry: no findings. The undrawn middle stretch (notes only): the route holds, and
1. two taps were missing from the notes: (6492,13744) on `rsel13_buf`'s track and (6450,13852) on
   `rsel12_buf`'s, each the west end pad of a poly row toward `cdp4`'s corner gate group. A
   connection, in geometry this package does not draw (`busl`'s region). Confirmed by the tracer
   (`textmap.py 6470 13724 6518 13766`, `6428 13832 6476 13872`); the notes' Logic now has them and
   the handoff carries them to `busl`. No trace line changed:
   `tools/t.sh regs sameconn.py 49ae634`: `connections identical`;
   `.venv/bin/python tools/sameconn.py 49ae634`: `connections identical`.
Round 4: no findings that change a connection.

**Round 5, full review of piece `w8450`, 2026-11-20 23:42 +0100** (fresh Fable reviewer; at commit
c55d30d; 26 images by its count, 23 files in `cache/scratch/regs/review-5/`). Told to suspect: the
920 px poly row from `bl0`'s end (a hidden tap, a branch, the gap stretch x 5420-5540, the mark
(4990,16712)); the corner (5845,16713) and whether either row runs on past it; the crossing
(5865,16800); the row's east end under the rail; the pad (5907,17019), dull in chip 2; the track
x 6408 at y 17580-17625; the three hops and a swap with a neighbouring row; the west end pad
(6712,18124) against `bd1_n2`'s corner; which diagonal band lands on the pad (10137,18124); the pad
(10484,17994), the track x 10485 and the stretch y 17716-17755; missed taps on the metal row and
the two tracks; all round every pad. Checked (text maps of both chips at every crossing, `px.py`,
`busl_both.py`, `tl5_tracks.py`, views at 2.3-7.5x): the row is one straight poly with no ring or
hole at any crossing, open poly in the gaps x 5375-5398 and 5425-5530, the mark in chip 2 only; no
edge line across either junction of the column, field north of y 16700, south of y 16815, east of
x 5858 and west under the track x 5815; no contact at (5865,16800); the pad (5909,16800) a contact
with field north of it; the vertical poly x 5925-5945 ends 10 px of field short of the row and the
box (5953-5990,16748-16785) is separate; no contact where the metal x 5910 crosses the two rows
(the metal y 16885-16895 ends at x 5873); the pad (5907,17019) a contact (ring in both chips, centre
red 220 / 145, green hole); the track x 6408 one metal, the patches in chip 1 only; no pad under the
six tracks; 8-10 px of bare ground between `bd1_n2`'s corner and the pad (6712,18124); no contact at
x 6808, 6917, 8262, 8912 and no branch outside the hops; the three hops straight; the first band
lands on (10137,18124) and goes to the row y 17995, `rsel16_buf`'s is the next, no touching and no
pad under the crossing metals; no contact on the three rows the track x 10485 crosses; the stretch
y 17716-17755 has no bright centre, no hole and no widening, and the metal is bright again at
y 17685-17715; every poly link is orange in an open stretch (trap 39); the ports as stated. Could
not check: whether the metal is continuous through y 17716-17755 (undrawn; trap 27); the gap
between the poly's tip and the strip of finding 2 more finely; the hops in images above 2.6x (their
straightness rests on the text cuts; the tracer's own `h1.png`-`h3.png` are at 4-4.4x in both
stripped shots).
Findings, all geometry or notes, each checked by the tracer:
1. The east end of the row y 16800 is at about x 6066, not x 6060. Geometry only (a length).
   Confirmed (`px.py row 16796 6044 6100 2 all`: orange, 157/94/54 and 149/93/48 in chip 2, at
   x 6060-6062, dark from x 6066): the poly now ends at x 6065.
2. The notes left out that the diffusion above the band leaves the rail east as a strip x 6072-6092
   beside the poly's tip, with 12-14 px of dark between, read as no buried contact. Notes only (in
   undrawn geometry). Confirmed for the strip (the same profile: plain, blue 78-85, chip-2 stripped
   red over green 15-19 at x 6082-6088); the gap is as the reviewer read it and is left to whoever
   draws the pull-down: Logic, "Two ends".
3. The rail the row y 17018 passes under is x 6015-6065, not x 6010-6050. A comment. Confirmed
   (`busl_both.py h 17040 5990 6090`: metal x 6019-6061 by the two-chip test): notes and trace
   comment corrected.
`tools/t.sh regs sameconn.py c55d30d`: `connections identical`. `.venv/bin/python tools/sameconn.py
c55d30d`: `connections identical`.
Round 5: no findings that change a connection.

**Round 6, full review of piece `r9`, 2026-11-21 19:35 +0000** (fresh Fable reviewer; at commit ac77193; 21
images in `cache/scratch/regs/review-6/`). Told to suspect: the diagonal metal x 13262-13470 on and across
`rst_a`'s poly and its end on the pad (13240,17862); both hops keeping their rows; the drain's two narrow
strips and the west box; the load (plate, strip, tie box, supply contact); the ground contact, the ground
rail's metal to y 17527 and the dot (15688,17497); the gate poly's end and the pad (15558,17428); the
output poly under the VCC rail; the metal y 17735 over the poly columns, its corner and the pad
(16773,18012); anything undrawn at x 15560-15900, y 17370-17530 that touches these nets.

Checked and found correct: the west pad (metal from the west only) and the rows y 17815 / 17862 / 17907
on their tracks at seven cuts (`tl5_tracks.py rows`; 2.4x in three shots); the poly column x 13206-13224
apart from the pad (13172,17862); the diagonal as one metal from pad to corner, bright in both chips, the
pad's ring equal on both sides, no pad, widening or hole at (13316,17803) or at the column crossing
(`textmap.py`; 4-5x); the row y 17648 continuous in chip 2 (chip 1's failure at x 13924-13998 is a blemish
on that die) and the second hop straight (3.9x, two shots); the gate pad (metal from the south only, poly
east only, the gate's cap at about x 15728 with field beyond); both contacts of the inverter (ring in the
metal shots, pits in the stripped ones), the tab as diffusion (chip-2 stripped 172/160/94 at x 15652), the
west box, the tie box and the node land, field north of the tie box; the ground rail's metal to about
y 17527 with field under it from y 17476 (`railprof.py` calls y 17490-17513 diffusion: not tan, trap 18);
the dot (15688,17497) in chip 2 only; the output poly under the VCC rail uniform, no transistor; the metal
y 17735 without a pad (the pads at y 17775 are the next row's), the inner corner at x 16776, the pad
(16773,18012) and its poly on east; the extraction and `unsure.py` (0 nets).

One finding, geometry only, confirmed and fixed: **the load plate's west edge is at x 15781, not 15790**
(`px.py row 17483 15765 15805 3 metal,metal1,acid`: the edge line at x 15777-15780, orange poly at
x 15783-15789, the VCC rail's own edge at x 15792-15795). The load is 24/54, not 24/45. Proof that no
connection changed, against ac77193:

    tools/t.sh regs sameconn.py ac77193             ->  connections identical
    .venv/bin/python tools/sameconn.py ac77193      ->  connections identical

Not checked by the reviewer: the bus metal west of x 12770 (a poly column crosses under it at about
x 12738-12750, outside what is drawn) and the output poly east of x 16830 (both are ports); the west hop's
rows at 4x (2.4x and seven text cuts; the tracer's `w6.png` is 2.6x in three shots, `w4.png` 4x at its east
end); the neck from views and single points only; what the two rails join north of y 17370 (`bd3`'s).

Round 6: no findings that change a connection.

**Round 7, full review of piece `n0`, 2026-11-21 20:05 +0000** (fresh Fable reviewer; at commit 6cdd5db; 21
images in `cache/scratch/regs/review-7/`). Told to suspect: whether the 7,245 px track is one metal on one
position all the way (two metals end to end, or a step where a neighbour steps: traps 10, 33); both pads
(contact real, the metal through the one at (11200,13330) and ending on the one at (11200,10664), a second
poly); each poly row from x 10850 to its pad (the right row, straight, no tap onto the metals above); the
corner (11200,17911); the bus row to run 5's pad; the crossing (11201,16390); anything the track touches
that the trace leaves out.

Checked and found correct: the track by `tl5_tracks.py v 11201 10600 17900` (the longest stretch without
metal in both chips is 18 px, each accounted for: the pad's rings, poly rows at y 10708, 11830, 14567,
16390 and the bottom bus rows, a diffusion edge at y 12179-12186, a 10 px blemish at y 15238-15247 that is
dark across chip 1 and only a notch in chip 2, with nothing under it in the chip-2 stripped shot; chip 1's
failure at y 15712-15761 is dirt), by two-chip cuts of its own every 60 px (centre x 11197-11204 at every
cut, the neighbours at x 11113 and x 11157 not moving either) and on six 1x strips in three shots (the
nested corners at y 14880-14920 are lines further east); the end pad (ring and bright centre in both
metal shots, green hole in the clean shot, pitted box in the chip-2 stripped shot, metal from the south,
bare ground north, no second poly; the rows y 10621 and y 10708 end on their own pads at x 11157 and
x 11243); the pad (11200,13330) in all four shots, metal within 5 px of its ring on both sides in both
chips, field east and south, the row y 13376 on its own pad at x 11157; both poly rows straight with no
widened metal over them, the clean shot's dots in the gaps between metals and absent from the chip-2
shots; the crossings (11200,11835) and (11201,16390) (text map with `--acid`: the track keeps its width,
plain salmon under it, 14 px of open poly to the neighbour's pad ring); the bottom bus crossings
y 17458-17877; the corner (no metal south of y 17915 or west of x 11196); the bus row continuous to the
ring of the pad (12806,17907), bars of 8-12 px at the poly diagonal and the poly column only (ragged
material in the clean shot at x 12690-12745 is residue on chip 1, absent from chip 2); the full
extraction and `unsure.py`.

Not checked by the reviewer: `cdp3`'s and `cdp4`'s rows west of x 10830 (theirs); run 5's pad beyond the
metal reaching its ring (round 6); whether the crossing polys are drawn by anyone; the crossings at
y 10708 and y 14567 and the wide diffusion at 4x (1x, the metal test and a text map only).

Round 7: no findings.

## Not done

- The two open joins of piece 3 are closed (`busl` run 8: Corrections, second batch, below).
- **`lc2_w8450`'s track x 10485 north of y 17760** (the east end of piece `w8450`; in `bc4`'s
  region). Thin metal beside the gate column on the rail x 10550-10600. Stretches without metal in
  both chips (`tl5_tracks.py v 10486 16300 17990`): y 17716-17755 and 17457-17549 (looked at: over a
  box each, pass-overs; the second also over a poly row y 17500-17525, where the metal shows 10 px
  wide), 17326-17363, 17152-17188, 16914-17074 (160 px: not read), 16805-16840, 16673-16710,
  16500-16553; no metal north of y 16300, so the track ends at about y 16340. To do: read each
  stretch at 5x in four shots (a tap has a widened pad, a bright centre and a green hole), draw the
  pass-overs `?M` (trap 27), find the end and every load. Views: `c2.png`, `c3.png` (2.8x, four
  shots, y 16880-17780).
- **The pull-down on `lc2_w8450` under the rail x 6008-6055 at y 16791-16810** (the west end; in
  `bl1`/`bl2`'s region): gate band drawn as poly only; its two diffusions, the rail and the box
  (5953-5990,16748-16785) are not drawn (Logic, "Two ends").
- The ninth row y 17648 is drawn (run 5, piece `r9`) and its source found (run 6, piece `n0`: bus N,
  column 0). **Left of it**: the inverter's output `d7_out_n` east of (16800,18012) (a poly row
  under `e_b`'s track x 16810 and a wide rail x 16940-17030 to a pad seen at (17065,18010), metal on
  east; `busc`'s region): believed toward the data bus column.
- **The other seven columns of bus N** (believed, run 6): seven more tracks of the bus field from the
  staircases of pads at y 10361-10621 (`rd_b6` .. `c7`; the next pad is at about (11155,10621)) and
  y 13376-13633 (`cdp4_n_s1` .. `s7`; the next pad at about (11157,13375)), to wherever each goes; the
  same reading as piece `n0`, one line at a time (the lines step where a neighbour leaves: `bw`'s survey).
- More undrawn metal rows go through the same hop below `rsel12_buf`'s: y about 17777 (pads at about
  (14450,17777), (14673,17777)), y about 17823 (pads (14497,17823), (14714,17823)), y about 17865 and
  17905 (`s1.png`, 0.55x, every trace outlined); and at the trunk hop the row y 17862 between pads
  (12845,17862) and (13172,17862), whose east pad takes a thin metal from the north (`w4.png`, `w6.png`).
- The unit east of the VCC rail beside the new inverter (a poly block at x 15890-15935, y 17410-17470 and a
  poly row y 17405-17420, x 15880-15940: `e5.png`), undrawn.
- The structure of Ambiguities 1.
- `wr_r14`'s branches into the row A cells (`cdp3` (continue)); the source of `cdp4`'s 6-bit
  input a (`cdp4` (continue)).

## Corrections (coordinator, from the handoffs of 2026-11-20)

- "`wr_r14` ... its branches into the cells are not traced" and "6 (believed, from the row)": the branches are the strobe loops of R14's six latch cells; row A is R14, firm (`cdp3` row A, 2026-11-20).
- The two undrawn rows y 13744 and y 13852 end as gates 2 and 4 of the NOR that makes `cdp4_rst` (`cdp4` run 2); their east parts step south to y 13759 and y 13873 at x 7550 and are drawn there as the open joins `rsel13_buf`, `rsel12_buf`.

## Corrections (coordinator, from the handoffs of 2026-11-20, second batch)

- Piece 3, "The 4,600 px between are read (notes), not drawn", and the two joins "believed": drawn by `busl` run 8 (pieces `r12`, `r13`) and reviewed, no uncertain item: `rsel12_buf` and `rsel13_buf` run from this package's ports at the south edge of the left bus field to its tracks at y 10400 on one thin metal each, and they are the read gates of `cdp3`'s rows E and F. The path is as read here; the tap contacts are at (6452,13854) and (6495,13744) (here: (6450,13852), (6492,13744)).

## Corrections (coordinator, from the handoffs of `cdp3`, `cdp4` runs 4-15, `eof` runs 36-51 and `regs` runs 5-6, 2026-11-21)

- "Believed, not traced: the other seven columns do the same": traced by `cdp4` runs 4-11. The "more undrawn
  metal rows through the same hop below `rsel12_buf`'s, y about 17777 ..." are the read bus's columns 1-7 (y
  17777, 17821, 17864, 17908, 17951, 17994, 18037).
- "The unit east of the VCC rail beside this inverter" is the sixth data output inverter, on column 1 (`cdp4`
  run 9); columns 2-7 go north to the data output units instead.
- `d7_out_n` "to a pad seen at (17065,18010) with a metal on east: not followed": followed (`cdp4` run 11):
  it is `d7_out_n`, into D7's pad cell; the pad's contact is at (17080,18013).

## Corrections (coordinator, from the handoffs of `eof` runs 63-68, 2026-11-23)

- Track x 10485 ("north of that it passes over the boxes and rows of the gate column"; Not done, "`lc2_w8450`'s
  track x 10485 north of y 17760", "no metal north of y 16300, so the track ends at about y 16340"): the thin
  metal x 10476-10492 runs north to (10484,16240) and turns west to a pad (10440,16215); that north end is drawn
  by `eof` (run 67, piece `p16215`) as `eof_w16213`, on a net with a poly toward `rst_lat`'s unit. Whether it is
  one metal with `lc2_w8450` is not shown: it is dark over a box at each unit between (y 16240-16277,
  16500-16537, 16977-17014, 17457-17492, 17716-17754). At y 16996 the box is the node of the NOR `eof_w16996`,
  with no other exit; `eof` draws a `?C` there (AMB-060). If that contact is real, the track is two metals end
  to end somewhere between y 17024 and y 17760 (trap 33; R53). `regs`' drawn stretch (to y 17760) is not
  affected.

## Corrections (coordinator, from the handoff of `eof` run 69, 2026-11-24)

- Piece J (the thin metal x 10485 north of the pad (10484,17994), `lc2_w8450`): the same track's north end is
  `eof_w16213` = NOT `rst_lat`, the output of `rst_lat`'s inverter in `bc2`'s rail column (`eof` piece
  `u16303`, firm). `lc2_w8450` is the reset in the other sense, so the track is not one metal on one net: the
  break or the wrong reading lies at one of the box stretches y 16500-16537, 16977-17014 (AMB-060),
  17457-17492, 17716-17754. Neither package joins them.
