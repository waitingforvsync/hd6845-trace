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

- **Task 3, `rst_ck`'s source: found** (piece `tcwa`). `rst_ck`'s metal, which `tl6` drew to
  (6105,6350), is drawn on south and east down a staircase of five corners to the west end of
  `trunks`' line "S" at (6690,8366): **`rst_ck` is `rst_ck`**, the output of the lone inverter of
  the input buffer row (`rst_ck` = NOT `rst_a_n`, `rst_a_n` = NOT `rst_a`), the net that holds
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

- **Task (b), `rst_a`'s source: not found; two of its three open ends followed** (piece `isrc`).
  `rst_a` (the signal whose copies are `rst_ck`, `rst_rc`, `rst_lat`) is a widely fanned-out line of
  the bottom-centre logic. **One end is the clear of `bc2`'s latch unit a** (its own name for the pad is under Former names in the glossary; joined:
  `bc2_w15029` = NOT((`bc2_w14876` AND `bc2_w14955`) OR `bc2_w15000` OR `rst_a`)). The bus line
  west of the pad (9770,18081) feeds a 2,470 px metal x 8968 with three pads and a west branch,
  each on a poly that goes on west into the gate column x 8650-8800 (repeated units; not followed).
  The third end (the poly y 16950 east of x 10470) is a gate row of the unit under the rail
  x 10540-10585 (looked at, not drawn). **Every end seen so far is a gate; the driver is still open.**

Run 5 (richtw1's session, Claude Fable 5.2; 2026-11-19 13:05 +0100 on). One piece, 4 transistors,
no uncertain items.

- **Task (c), the gate group at the end of `rst_ck`'s tap row: traced** (piece `g7700`). It is one
  gate under the VSS rail of the central datapath's column 0: **`tc2_r5589` = NOT(`eof_w7777` AND
  (`rst_ck` OR `tc2_sr_g`))** (firm). Rows 1 and 2 are **not** two fingers of `rst_ck` (run 2's
  guess from a 2.7x view): their ends lie on a field island and are apart; row 2 is its own net.
  All three wires are followed to pads, none yet to a known net: the output goes west and north
  (two pads, a metal x 7272) to a pad (7272,6912) whose poly goes on north; `tc2_sr_g` has a pad
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
  is `bd1_n2`** and the two halves are a cross-coupled pair: **`bd1_n1` = NOT(`bd1_n2` OR (`rst_lat` AND
  `rc_eq_r4`)), `bd1_n2` = NOT((`bd1_an` AND `rst_lat`) OR `bd1_n1`)**: a transparent latch of R4's match,
  open while `rst_lat` is high, with `bd1_n2` the match as latched and `bd1_n1` its inverse (marked: both
  loads' ties are uncertain items). **Where the latch's outputs go is still open**: nothing leaves the
  lower half east or south (seen, `e_s2.png`); the one candidate is `bd1`'s old question at N1's west end
  (Not done).

Full extraction with run 7: 2,398 nets, 4,345 transistors, 0 errors, 0 warnings (the package by itself now
also loads `bd1`, with `sel` and `bd3`).

Run 8 (Tom Seddon's session, Claude Fable 5.2; 2026-11-19 15:25 +0000 on). Two pieces, no transistor of its
own (two diffusion links and a wire), no uncertain items.

- **Task (e), where the latch's outputs go: the latch has one exit, and it was already drawn** (piece
  `n2out`). The strip under `bd1_an`'s metal that `bd1` read as "the pull-down of `bd1_k`" (gate `rst_a`,
  a buried contact to a poly that leaves west) is not a unit of its own: in the open gap between that metal
  and the ground rail its lower segment is one diffusion with N2. So **`bd1_k` is `bd1_n2`**: the latch's
  true output leaves west on `bd1_k`'s poly and metals. The strip's top segment joins the ground diffusion
  through the same gap (`bd1`'s `?D`, firm here), so `rst_a` gates a third pull-down of N2:
  **`bd1_n2` = NOT((`bd1_an` AND `rst_lat`) OR `bd1_n1` OR `rst_a`)**: the latch takes R4's match while
  `rst_lat` is high, and its output can be high only while `rst_a` is low (marked: the load's tie).
- **The output followed 11,900 px** (piece `n2w`, wiring only): from `bd1`'s end (13521,16273) down the
  strobe channel, west through the bottom bus field beside `h_eq_r1`, `rst_lat` and `rst_a`, through
  `bc3`'s routing field without a tap, and north up the left bus field two tracks west of `rst_ck`, to
  `busl`'s south edge at (6711,15000): fourteen pads with contacts, seven poly links, **no gate and no tap
  on the way**. The follower takes the metal on north to (6948,8707), beside `cdp3`'s gate column (not
  read: it is in `busl`'s claimed region).

Full extraction with run 8: 2,398 nets (one fewer: `bd1_k` is an alias), 4,345 transistors, 0 errors,
0 warnings.

Run 9 (Tom Seddon's session, Claude Fable 5.2; 2026-11-19 16:17 +0000 on). One piece, wiring only, no
uncertain items.

- **Task (b), `rst_a`'s source: it is not in the bottom-centre logic. `rst_a` is `lc2`'s through line x 6299**, the first
  through line of the left-centre strips (piece `isrc4`). The fourth open end of piece `isrc`, the poly west
  of the pad (8688,17737), was followed 4,700 px: a poly row to a pad (8053,17735), a metal up the track
  bundle x 8057-8185 by two steps to a pad (8185,16303), a poly row west to a pad (7968,16303), `bc1`'s
  untraced "track 7969" 1,390 px north to a pad (7880,14914), and that pad's poly row west onto the east
  end of `busl`'s row y 14914 at x 7550, which `busl` and `lc3` bring down the left bus field from `lc2`'s
  through line (it enters `lc2` from the east at (6450,8630)). No uncertain item on the path; no transistor.
  So the signal whose copies stop `ck_b` (`rst_ck`), the row counter's step (`rst_rc`) and open the latch
  on R4's match (`rst_lat`) **arrives from the north-west**, from whatever drives `rst_a` east of
  (6450,8630): the strip between the left-centre logic and the central datapath (`busl`'s northern part,
  free), where the latch's output `bd1_n2` is also heading.
- **The other three open ends are gates, and so are two more on the new path** (looked at, not drawn): the
  tap rows y 16172 and y 16737 of the metal x 8968 are the clear rows of two mirrored copies of `tl1`'s latch
  cells under the rail x 8686-8731 (`findcell`, scores 0.67-0.73), the row y 15258 a pull-down of another unit
  under the same rail; on the new path the rows y 16303 and y 16909 are the clear rows of two more copies
  under the rail x 8336-8384. With `bc2`'s unit a, **`rst_a` is the clear of at least five latches of the
  bottom-centre logic** (believed for four: the cells are not placed).

Full extraction with run 9: 2,397 nets (one fewer: the through line's name became an alias of `rst_a`), 4,345 transistors,
0 errors, 0 warnings.

Run 10 (Tom Seddon's session, Claude Fable 5.2; 2026-11-19 16:56 +0000 on). One piece, wiring only, no
uncertain items.

- **Task (b), `rst_a`'s source: found. line X (the first through line of the left-centre strips) is `rst_a`**, the buffered reset of the left-centre gate
  column (piece `isrc5`). `lc2`'s through line was followed back from `lc2`'s east edge (6450,8630): the
  diagonal metal runs on 90 px to a pad (6513,8538); the pad's poly goes 450 px north (under `rst_ck`'s
  metal and, for 150 px, lengthwise under `eofw`'s metal of `tc2_sr_g`, with no contact) to a pad
  (6513,8087); a metal goes north by an L onto the track x 6558, 760 px up the crossing field, turns west
  at y 7258 and ends on a pad (6187,7257); that pad's poly row runs west through `lc1`'s crossing field,
  turns north-west as one line of `lc1`'s diagonal poly bundle and, under V5, V4, V3 and V2, comes up onto
  **the poly that piece `x1` (run 2) drew south of `rst_a`'s pad (5147,6803)**. Four pads with contacts,
  two polys, two metals, no transistor, no uncertain item (`tools/unsure.py` lists none of the names).
- So `rst_a_n` = NOT `rst_a`, and `rst_ck`, `rst_rc`, `rst_lat` = NOT `rst_a_n` are **three more buffered
  copies of `rst` = NOR(`lpstb_b`, `res_b`)** (firm in the extraction for the join and for `rst`, `rst_n`,
  `rst_a`, `rst_a_n`): the signal that holds `ck_b` low, stops the row counter's step, opens the latch on
  R4's match, holds that latch's output low, clears five latches of the bottom-centre logic and is the
  top-left logic's track A is high while the RES and LPSTB pins are both low. It is not a strobe (the
  belief written in `notes/operation.md` until this run).

Full extraction with run 10: 2,395 nets (one fewer than main's 2,396: `rst_a` is an alias
of `rst_a`; the through line's own name was renamed to `rst_a` by the refresh that main ran during this run), 4,345 transistors, 0 errors, 0 warnings. The package by itself: 1,031 nets, 1,764 transistors,
2 errors and 46 warnings, all of them `lc1`'s, `lc2`'s and `bd1`'s partial-load messages as before. After
merging main at the end of the run (`busl`'s runs 3-6 and the refresh): 2,389 nets, 0 errors, 0 warnings,
one net fewer than main; by itself 47 warnings (the new one: `rst_a` on two unconnected nets, because
`lc2`'s through line now carries that name and `lc3`'s and `busl`'s stretch of the line is not loaded).

Run 11 (Tom Seddon's session, Claude Fable 5.2; 2026-11-19 17:53 +0000 on). Two pieces, wiring only, no
transistor, no uncertain items.

- **The other lines of `lc1`'s diagonal bundle: `res_b` and `lpstb_b` go on to `lc2`'s second and third
  through lines** (piece `rl`). Each is built like `rst_a`'s line (piece `isrc5`), one and two lanes north of
  it: a poly diagonal under V2-V5, a row through the crossing field (y 7214, y 7170), a pad, a metal east,
  a track south (x 6602, x 6645), an L one track west, a pad, a poly column south, a pad, and a diagonal
  metal onto `lc2`'s metal end at x 6450. So **the second through line is `res_b` and the third through line is `lpstb_b`**: the
  buffered RES and LPSTB pins run down the left-centre strips and the left bus field (`lc3`, `busl`: no tap
  drawn on the way) and leave `busl` south at (6366,15000) and (6408,15000), into the bottom-left ground
  (`bl0`), where their loads must be. Six pads with contacts on each line, no transistor.
- **the wire `tl5` called w5936 (= `tl3_w3982`, the net that holds `rcs_cond` low) is the data of the left-centre latch C,
  and its driver is found as a place** (piece `w5936`). The bundle's lowest undrawn line runs by the row
  y 7300, a pad and the track x 6514 to a pad (6513,7889) **in the run of the metal** (trap 32): the metal
  goes on south, by an L, onto `lc2`'s metal x 6471 and its pad (6470,8127), **`tl3_w3982`, latch C's
  data**; and the pad's poly row runs 890 px east to a pad (7401,7888), whose metal goes south to a pad
  (7401,8425), whose poly ends on a heavy-outlined box (7490-7520, 8410-8442) at the foot of the gate
  column west of the central datapath (x 7460-7800; `cdp3` (continue), undrawn): a buried contact onto a
  strip that goes on east under the column's VSS rail. Believed: that is the output of the unit that
  drives the net (not traced: Not done).

Full extraction with run 11: 2,386 nets (three fewer than main's 2,389: the three joins), 4,345
transistors, 0 errors, 0 warnings. The package by itself: 1,028 nets, 1,764 transistors, 2 errors and 47
warnings, `lc1`'s, `lc2`'s and `bd1`'s partial-load messages as before.

Run 12 (Tom Seddon's session, Claude Fable 5.2; 2026-11-19 18:52 +0000 on). One piece, 6 transistors, no
uncertain items.

- **The driver of `tl3_w3982` is found and traced: three inverters in series from latch D's lower node**
  (piece `d3982`). The box at the foot of the gate column west of the central datapath, on which piece
  `w5936`'s poly ends, is the output of an inverter under the column's VSS rail (U4, a copy of `tl5`'s
  inverter turned 180 degrees); its gate row comes, by a C-shaped poly, from the output box of the unit
  above it (U3), and U3's from the unit above that (U2): two inverters of a larger build with a long load
  (plate 96 long against 56). U2's gate row is one poly with a band that turns west at y 8040 and runs
  1,010 px west under twenty-one tracks, with no pad and no contact, to a corner (6408,8040) and south
  onto **`lc2`'s poly `lc2_w8083`, the node of latch D's lower unit** (`lc1_w7928` through that cell's
  uncertain tie). So **`tl3_w3982` = NOT `eof_w8298`, `eof_w8298` = NOT `eof_w8168`, `eof_w8168` = NOT
  `lc1_w7928`** (the first two firm, the third firm as NOT `lc2_w8083`): the net that holds the row
  counter's step condition low and is latch C's data is **the inverse of latch D's second output, three
  gate delays later**. Latch D's first output is the inverse of `lc_step`, the step pulse of the scan line
  counter.
- The fourth unit of the column's foot (U1, y 7940-8060, another copy of U4's build) is **not** on this
  path and is not drawn (Not done: its input pad, its output's pads).

Full extraction with run 12: 2,388 nets, 4,351 transistors (six more than main's 4,345), 0 errors,
0 warnings. The package by itself: 1,030 nets, 1,770 transistors, 2 errors and 47 warnings, `lc1`'s, `lc2`'s
and `bd1`'s partial-load messages as before.

Run 13 (Tom Seddon's session, Claude Fable 5.2; 2026-11-19 19:50 +0000 on). Two pieces, wiring only, no
transistor, no uncertain items.

- **The clock of the left-centre ripple counter is `lc3_w9947`**, the gate line of the top-centre logic's
  west gate column (piece `ck5`). `lc2`'s fourth through line (the wire `lc2` called x6432 = `lc3_w9947`, the clock of
  stage B0) was followed back from `lc2`'s east edge (6450,9165): a metal north on x 6472 and a diagonal
  to a pad (6645,8580), a poly column to a pad (6645,8276), an L and the track x 6688, 1,030 px north, a
  metal west along y 7128 to a pad (6450,7127), and that pad's poly 725 px north under fourteen
  horizontal metals onto **the poly that `tc2` drew south of its pad (6447,6150): `lc3_w9947`, which
  `tl6` joined to `lc3_w9947`**. Three pads with contacts, no transistor. So the five-stage counter and
  the four pull-downs that `lc3_w9947` gates in `tcw`'s column have one clock; neither end is its driver
  (both are gates): the driver is still open, expected where `busl`'s row y 14784 takes the same net,
  toward the bottom-centre logic's 13-line bus.
- **the fifth corner-bundle line of `lc3` is `rst_c`** (piece `rc`): so `lc1_w7170` = NOT `rst_c` (firm), and **`rcs_x1` = NOT
  `lc1_w7170`, the clear of the step logic's five latches, is the reset, two inverters later**; the
  ripple counter's five stages are held clear while `lc1_w7170` is low, that is while the reset is on.
  Found by looking all round the corner where piece `ck5`'s metal turns onto `lc2`'s (trap 32): `rst_c`'s
  diagonal poly, which `lc2` drew out of its strip at (6450,8923), bends south and lies under `ck5`'s
  metal lengthwise for 225 px, with no contact, comes out below that metal's corner and ends on a pad
  with a contact (6469,9209), whose own metal runs south on x 6472 and turns west at y 9452 onto `lc3`'s
  fifth corner-bundle line.
- **The three undrawn rows of the diagonal bundle (y 6953, 6996, 7040) are not what feeds the tracks
  x 6688 and x 6730** (run 11's guess in Not done): each row's pad has a metal that runs on east past
  x 6830. The track x 6730 (line Q) is another net, followed part of the way and not drawn (Not done).
- One line of another package's trace file was changed, as a commit of its own: `trace/tl6.txt`'s
  the alias line of `trace/tl6.txt` was changed to name `lc3_w9947` (all four names are one since the rename of 2026-11-19) (piece `ck5`, "Names").

Full extraction with run 13: 2,382 nets (two fewer than main's 2,384: the two joins), 4,351 transistors,
0 errors, 0 warnings. The package by itself: 1,030 nets, 1,770 transistors, 2 errors and 47 warnings,
`lc1`'s, `lc2`'s and `bd1`'s partial-load messages as before.

Run 14 (Tom Seddon's session, Claude Fable 5.2; 2026-11-19 20:34 +0000 on). One piece, wiring only, no
transistor, no uncertain items.

- **The track that carries the latched R4 match north ends on the input of the inverter that makes
  `rcs_e3`** (piece `n2n`; task (e)). The metal that piece `n2w` left at `busl`'s south edge (6711,15000)
  was read through `busl`'s region by text (not drawn: the region is claimed) and drawn from `busl`'s north
  edge (6775,10400): north on x 6775, a diagonal to a pad (6947,8710), a poly column north to a pad
  (6988,8427), a metal 1,410 px north on x 6991 and 845 px west along y 7000 to a pad (6146,6997), and that
  pad's poly row west: **the middle one of the three undrawn rows of `lc1`'s diagonal bundle**, which runs up
  the diagonal onto `tl5`'s south bus poly x 5412, the bus line x 5412 of tl5 = `bd1_n2`. So the drawn wire is named
  `bd1_n2` (an open join: its 4,600 px in `busl`'s region are not drawn by anyone yet) and is one net with
  `bd1_n2` (firm): **`rcs_e3` = NOT `bd1_n2`, and `bd1_n2` is, believed, `bd1_n2`**, R4's match as
  the latch beside the strobe channel holds it. Three pads with contacts, no transistor, no tap.
- With it `bd1_n2` has its source as a place: every drawn end of the net is now this wire or the gate
  of `tl4`'s inverter.

Full extraction with run 14: 2,382 nets, 4,351 transistors, 0 errors, 0 warnings (the same counts as
before: the piece joins a named net). The package by itself: 1,030 nets, 1,770 transistors, 2 errors and
47 warnings, `lc1`'s, `lc2`'s and `bd1`'s partial-load messages as before.

Run 15 (Tom Seddon's session, Claude Fable 5.2; 2026-11-19 21:11 +0000 on). One piece, 2 transistors,
one uncertain item (the load's tie). A second piece was drawn, reviewed and withdrawn.

- **The driver of the ripple counter's clock is found** (piece `ck6`). `lc3_w9947` (the net of `tcw`'s gate line too: piece
  `ck5`) is followed from `busl`'s row end (7550,14784) east: the row's pad (7837,14784), the eleventh of
  `bc1`'s thirteen bus metals to a pad (8293,14785), a poly L and row along y 14825 under the
  bottom-centre logic's rails, a pad (8967,14870), a metal south to a pad (8962,15040) and a poly row west
  into **the output box of an inverter under the east VSS rail of the bottom-centre logic** (x 8508-8854,
  y 14942-15062; nobody had drawn it): **`lc3_w9947` = NOT `eof_w15127`** (marked: the load's tie). Five
  pads with contacts, no gate and no tap on the 1,900 px between.
- **The inverter's input `eof_w15127` is the output of the unit below it (unit V, y 15100-15285), which is
  read and not drawn.** It was drawn as piece `ck7`, an inverter of `eof_w15172` with two pull-downs in
  series on one hairpin poly; review round 17 found two diffusions under thin metals that the drawing
  stopped short of (a third pull-down on the node, and a strip on which the same gate rows and three more
  lie), both confirmed, so the unit is more than an inverter and cannot be finished without the unit below
  it (unit W). The piece is withdrawn from the trace (kept in `cache/scratch/eof/draft-ck7.txt`); what is
  established about V and W was under Logic and Not done until run 16 drew them (piece `vw`).
  Believed: V and W are a cross-coupled pair, so that the clock is the inverse of one side of a latch.

Full extraction with run 15: 2,383 nets, 4,353 transistors, 0 errors, 0 warnings (one net and two
transistors more than before the run). The package by itself: 1,032 nets, 1,772 transistors, 2 errors and
49 warnings: `lc1`'s, `lc2`'s and `bd1`'s partial-load messages as before, and `lc3_w9947` twice more on
"two unconnected nets" (the pieces `ck5` and `ck6` are joined by `busl`'s and `lc3`'s wires, which the
package does not load).

Run 16 (Tom Seddon's session, Claude Fable 5.2; 2026-11-19 23:32 +0000 on). One piece, 9 transistors,
five uncertain items (the two load ties). As first drawn it had 13 transistors (each stack in two fingers)
and an uncertain link; review round 19 showed the stacks are one diffusion each (below, Review).

- **The units V and W below the inverter are traced** (piece `vw`): a cross-coupled pair.
  **`eof_w15127` = NOT(`eof_w15172` OR `eof_w15300`)** (unit V) and **`eof_w15300` = NOT((`ck_out`
  AND `bc2_w15607`) OR `eof_w15127` OR `rst_a`)** (unit W). So the ripple counter's clock `lc3_w9947` =
  NOT `eof_w15127` is the inverse of one side of a set/reset latch: it goes low when `ck_out` and
  `bc2_w15607` are both high (or at reset) and high again when `eof_w15172` is high. Each unit's third
  pull-down is gated by the other's load plate; V's single input lies on both rows of its stack (a
  hairpin), W's stack has two inputs. **Row C, the gate of the transistor that clears W, is `rst_a`'s row
  from the end pad (8966,15260)** of piece `isrc`: one of the undrawn gates of `rst_a` is now drawn.
- **Marked**: both equations rest on the plates' ties (uncertain as in every load of this build). The
  pull-downs are all drawn without `?`; the open gap east of the rail, through which both stacks'
  diffusions run, is read from edge lines against its colour (Ambiguity 53).
- The four inputs and outputs are drawn to ports: `eof_w15172` (the hairpin's row, on east at (9150,14653)),
  `ck_out` (a metal south, 1,346 px by the follower), `bc2_w15607` (a metal north to the pad
  (9008,14828), whose poly goes on north) and W's output `eof_w15300` (a metal south to a pad (8836,15456)
  at the next unit of the column). None of the four is followed.

Full extraction with run 16: 2,378 nets, 4,362 transistors, 0 errors, 0 warnings.

Run 17 (Tom Seddon's session, Claude Fable 5.2; 2026-11-20 01:05 +0000 on). Two pieces, `in390` (wiring only)
and `in172` (3 transistors), no uncertain item: **two of the three inputs of the latch V/W are followed to
their sources**, both at the east gate column of the bottom-centre logic (`bc2`'s ground, free).

- **The lower gate of W's stack (the wire this package called w15390) is `bc2_w15607`, the lower node of `bc2`'s latch unit b**
  (piece `in390`; traced, wiring only): the poly column north of the pad (9008,14828) turns east at y 14610
  and runs 1,070 px as a row to a pad with a contact (10092,14609), whose metal goes east and 910 px south on
  x 10268 onto `bc2`'s metal of that net (its pad (10267,15607)). `bc1`'s bus metal y 14603-14618 lies on the
  row for 185 px and three more bus metals cross the column: no contact at any (Ambiguity 58).
- **`eof_w15172`, V's input, is the output of a NOR that nobody had drawn: `eof_w15172` = NOR(`bc2_w14955`,
  `bc2_w15000`)** (piece `in172`; traced, firm): the row y 14653 runs 1,150 px east, steps one track south at
  x 10284-10302 and ends in the output box of the top unit of `bc2`'s east column (unit T, x 10484-10770,
  y 14598-14790). T's two gate rows come from two pads whose metals go south onto `bc2`'s latch unit a: its
  output pad (10395,15000) (`bc2_w15000`) and its enable metal x 10441 (`bc2_w14955`).
- So the ripple counter's clock `lc3_w9947` is set high while latch unit a's enable is low and its upper
  node `bc2_w15000` is low, and set low by `ck_out` AND latch unit b's lower node (or the reset).
- **Not followed**: `ck_out` (the metal south of (8881,15465)): the follower ends on a pad at about
  (8882,16644), by position the output row of an undrawn latch copy in column B (Not done).

Full extraction with run 17: 2,377 nets, 4,365 transistors, 0 errors, 0 warnings.

Run 18 (Tom Seddon's session, Claude Fable 5.2; 2026-11-20 01:54 +0000 on). One piece, `in350` (wiring only),
no uncertain item: **the third input of the latch V/W is followed to its source, and it is `ck_out`**.

- **The upper gate of W's stack (the wire this package called w15350) is `ck_out`**, the main internal clock (NOT CLK) (piece
  `in350`; traced, firm for the join). The metal south of row 1's pad (8881,15351) does not end at
  (8882,16623), where the follower stopped and run 17 guessed a latch's output: it runs **through** two pads
  with contacts, (8882,16648) and (8882,16867), on south to a corner (8882,17649), west and south to a pad
  (8598,17908). From that pad a second metal runs 1,000 px east to a pad (9596,17909), whose poly crosses
  under two vertical metals to a pad (9769,17910), the west end of the metal that `trunks` draws as
  `ck_out #1` (`M 10320,17908 x10230`: "followed to x 10230 only"). Five pads with contacts, no gate on the way.
- So **W's equation is `eof_w15300` = NOT((`ck_out` AND `bc2_w15607`) OR `eof_w15127` OR `rst_a`)**: the ripple
  counter's clock `lc3_w9947` is set low while `ck_out` is high (CLK low) with latch unit b's lower node high,
  and high by `eof_w15172` (marked as before: W's tie).
- **The two pads in the metal's run are gate rows of the gate column under the rail x 8686-8731**: by their
  places the two enable rows of the lower of the two undrawn copies of `tl1`'s latch there (believed: the copy
  is not placed; the rows are drawn to x 8806). If so that latch is open while `ck_out` is high, like `tl1`'s
  third latch.
- **`ck_out` goes on from the pad (8598,17908)**: its poly runs west under the VSS rail to a pad with a
  contact (8424,17908), on which a metal from the north ends and from which the poly goes on west. Drawn to
  that pad; the two continuations are ports (Not done). As first drawn the piece also had a metal leaving that
  pad west; review round 22 showed that metal ends 34 px short of the pad's centre and is another net's.
- **Two more branches, found by review round 22**: the pads (9596,17909) and (9769,17910) of the hop each
  carry a second metal, from the north (tracks x 9596 and x 9770, each ending on its pad). Drawn as stubs
  (ports, not followed).

Full extraction with run 18: 2,378 nets, 4,372 transistors, 0 errors, 0 warnings (main has `cdp4`'s corner
group since run 17). The package by itself: 1,039 nets, 1,784 transistors, 0 errors, 65 warnings (the
partial-load messages of `lc1`, `lc2`, `bd1`, as before the piece).

Run 19 (Tom Seddon's session, Claude Fable 5.2; 2026-11-20 02:44 +0000 on). Two pieces, `lat16` (11 transistors: a
copy of `tl1`'s latch) and `inv16` (2 transistors, by hand): **the latch that `ck_out`'s two pads enable is
drawn, with the inverter that drives its data**.

- **The two pads in `ck_out`'s metal are the two enable rows of a latch** (piece `lat16`; traced, the cells'
  ties uncertain as in every copy): the lower of the two mirrored copies of `tl1`'s latch under column B's rail
  x 8686-8731 (x 8508-8815, y 16493-16975; `findcell` 0.72 and 0.67, every outline on its feature at 2.7x).
  `eof_w16693` = NOT((`eof_w16607` AND `ck_out`) OR `eof_w16823`), `eof_w16823` = NOT(`rst_a` OR (`ck_out` AND
  `eof_w16507`) OR `eof_w16693`), `eof_w16507` = NOT `eof_w16607`: **open while `ck_out` is high (CLK low), it
  takes `eof_w16607`, and the reset copy `rst_a` clears it** (its clear row is the row of `rst_a`'s tap pad
  (8966,16737), drawn to the pad). Run 18's belief about the two pads is now traced.
- **Its data does not come from the east like its other rows** (piece `inv16`; traced, the load's tie
  uncertain): the data row turns north under the track x 8838 (195 px of poly under another net's metal, no
  contact) and west into the output box of **an inverter that stands between the two latch copies**
  (x 8512-8800, y 16317-16465): `eof_w16607` = NOT `eof_w16388`. The inverter's gate row y 16380-16400 comes
  from a pad with a contact (9010,16388), on which a metal from the north ends (the follower: from
  (9010,16082); not followed). So **the latch stores NOT `eof_w16388`**: `eof_w16823` follows NOT `eof_w16388`
  and `eof_w16693` follows `eof_w16388` while `ck_out` is high.
- **Both outputs leave east** (drawn to ports; not followed): the upper node `eof_w16693` by a row to a pad
  with a contact (9012,16693) and a metal south (the follower: to (9011,17088)); the lower node `eof_w16823` by
  a row that turns north under that metal (100 px, no contact: Ambiguity 69) and east along y 16724-16745 into
  a structure at x 9058-9100, y 16665-16715 that is not read.
- **The lower node has a third exit, found by review round 24**: under the track x 8925 its row is one poly
  with a column x 8917-8935 south to y 17003, which turns west along y 16986-17003 to the rail and is there a
  gate of the unit south of the latch's foot box (not drawn; port at x 8760).

Full extraction with run 19: 2,385 nets, 4,385 transistors, 0 errors, 0 warnings. The package by itself:
1,046 nets, 1,797 transistors, 0 errors, 65 warnings (as before the pieces).

Run 20 (Tom Seddon's session, Claude Fable 5.2; 2026-11-20 03:55 +0000 on). Three pieces: `lat15` (11
transistors: the upper copy of `tl1`'s latch under the same rail) and two of wiring, `cap16` and `w16693`:
**the latch's three open wires are followed, and the latch has a second latch in front of it**.

- **`eof_w16388`, the input of the inverter on the latch's data, is the upper node of the other latch copy**
  (piece `lat15`; traced, the cells' ties uncertain as in every copy): the metal from the pad (9010,16388) runs
  300 px north and ends on a pad with a contact (9007,16082), the east end of the upper-node row of the upper
  of the two mirrored copies of `tl1`'s latch under column B's rail (x 8508-8815, y 15886-16368; `findcell`
  0.72 and 0.73). `eof_w16388` = NOT((`eof_w16000` AND `eof_w16040`) OR `eof_w16216`), `eof_w16216` =
  NOT((`eof_w15900` AND `eof_w16040`) OR `eof_w16388` OR `rst_a`), `eof_w15900` = NOT `eof_w16000`: **open
  while `eof_w16040` is high, it takes `eof_w16000`, and `rst_a` clears it too**. So the two copies are **two
  latches in series with the inverter between them**: while both are open `eof_w16823` = `eof_w16000`.
- **Its enable is not `ck_out`**: both enable rows end on pads of one metal x 8925, (8925,16040) and
  (8925,16262), which starts at the upper pad and runs on south through the lower one, over the lower latch
  (no contact), to (8925,17694) by the follower (not followed: port). **Its data** comes down the track
  x 8838 from a pad (8880,15738), whose poly row goes west into a box at column B's east edge at y 15740
  (not read: port); the track also runs on south of the data pad (port).
- **The lower latch's lower node `eof_w16823` ends on a large diffusion** (piece `cap16`; traced): the poly
  east of (9062,16735) turns north into a buried-contact box at (9080,16695), from whose pad a diffusion neck
  runs north into a rectangle of diffusion x 8908-9254, y 16477-16607 that lies under six tracks and has no
  gate and no contact. Believed: a capacitor on the node (a delay; `d3982`'s long loads are another).
- **The upper node `eof_w16693`** (piece `w16693`; traced, wiring): its metal ends on a pad with a contact
  (9011,17080), and the pad's poly runs west as a row y 17116-17135 into the unit south of the latch, the
  one whose first gate is the lower node's branch (y 16986-17003). That unit takes both outputs; it is not
  drawn (port at x 8800).

Full extraction with run 20: 2,403 nets, 4,461 transistors, 0 errors, 0 warnings. The package by itself:
1,052 nets, 1,808 transistors, 0 errors, 65 warnings (as before the pieces).

Run 21 (Tom Seddon's session, Claude Fable 5.2; 2026-11-20 04:49 +0000 on). Three pieces: `inv17` (2 transistors)
and `nor17` (3 transistors), by hand, and one of wiring, `in212`: **the unit south of the latch pair is two gates,
one on each output of the second latch**.

- **The lower node `eof_w16823` drives an inverter** (piece `inv17`; traced, the load's tie uncertain): the gate
  row y 16986-17003 that review round 24 found is the gate of a copy of the inverter `inv16`'s build, 607 px
  lower (x 8512-8814, y 16960-17072; `findcell` 0.83), whose source is the latch's own foot box:
  **`eof_w17040` = NOT `eof_w16823`**. Unlike `inv16`'s, its output leaves by a metal contact on a diffusion pad
  (8791,17040) and a thin metal that runs 520 px south down the column's east side to a pad (8792,17561), a
  poly row east and a pad (9008,17560), whose metal goes on south (port). The thin metal passes over three
  other units' boxes, where neither metal shot shows it: drawn uncertain there (Ambiguity 76).
- **The upper node `eof_w16693` is one input of a two-input NOR** (piece `nor17`; traced, the load's tie
  uncertain): **`eof_w17168` = NOR(`eof_w16693`, `eof_w17212`)**. Its two pull-downs are on one diffusion column
  east of the rail (x 8757-8785), between a VSS box at each end; the row between them, which run 20 took for
  a third input, is the **output**: it ends in a buried contact on the node and runs east to a pad
  (9007,17170), whose metal goes south and east (port).
- **The NOR's second input `eof_w17212` is followed to a pad 1,390 px north** (piece `in212`; traced, wiring;
  one stretch uncertain): the track x 9099 on which its row's pad lies is **not** the track x 9099 that comes
  down from the 13-line bus (a first reading by samples every 100 px had it run to the bus line y 14742,
  which would have made it `lc2_w8450`): at (9097,15870) it turns west and north to a pad with a contact
  (9053,15822), and the bus's track turns east 45 px above. The pad's poly row goes west (port; believed: to
  the pad (8838,15822) of the thin metal x 8792).
- So of the latch's two outputs one is buffered inverted (`eof_w17040` = the latch's value `eof_w16693`,
  one gate later) and one is gated: `eof_w17168` = `eof_w16823` AND NOT `eof_w17212`. **Where the two
  outputs go is not followed** (both metals run on south into the nest of Ls below column B).

Full extraction with run 21: 2,406 nets, 4,466 transistors, 0 errors, 0 warnings. The package by itself:
1,055 nets, 1,813 transistors, 0 errors, 65 warnings (as before the pieces).

Run 22 (Tom Seddon's session, Claude Fable 5.2; 2026-11-20 05:42 +0000 on). Two pieces of wiring, `o168` and
`o040`, no transistor, no uncertain item: **both outputs of the unit south of the latch pair are followed, one to
a wire that `bc1` drew and one to the edge of a gate nobody has drawn**.

- **The inverter's output `eof_w17040` is `bc1_g6_in`, the input of `bc1`'s inverter 6** (piece `o040`; traced):
  from the pad (9008,17560) the metal runs south and west to a pad (8733,17778), a poly row 390 px west under
  the rail and four tracks to a pad (8338,17777), and a metal west to the west track of the bundle x 8012-8229
  and 1,520 px north up it (a Z step at y 17259 onto x 8057, an L at y 16647 onto x 8143), onto `bc1`'s metal
  end (8143,16300). So **`bc1_g6_out` = NOT `eof_w17040`**: the second latch's lower node `eof_w16823`,
  inverted twice. `bc1_g6_out` goes on into the untraced gates of column A (`bc1`'s notes).
- **The NOR's output `eof_w17168` ends on a gate of a unit under column A's rail** (piece `o168`; traced to
  the unit's edge): from the pad (9055,17648) a poly row runs 480 px west, 300 px of it under `ck_out`'s metal
  of piece `in350` (the row of Ambiguity 63 is this net's), jogs south in the gap beside the rail, west under
  the rail (x 8500-8562) to x 8353 and north to a pad (8355,17649); a metal west and 220 px north up the
  track x 8186 to a pad (8185,17428), whose poly row runs east into a unit under the rail x 8315-8362
  (y 17300-17520), where it is a hairpin over a diffusion column: a gate. **The unit is not drawn** (port at
  x 8245; next run).

Full extraction with run 22: 2,447 nets, 4,557 transistors, 0 errors, 0 warnings (one net fewer: the join). The
package by itself: 1,055 nets, 1,813 transistors, 0 errors, 65 warnings (as before the pieces).

Run 23 (Tom Seddon's session, Claude Fable 5.2; 2026-11-20 06:29 +0000 on). One piece, `g174`, three
transistors, no uncertain item: **the unit that `eof_w17168` gates is a column of three wide pull-downs under
column A's VSS rail; its east side, with the load, is read and not drawn**.

- **Traced** (piece `g174`): one active area (x 8258-8368, y 17266-17560) under and west of the rail, with two
  contacts onto the rail, crossed by three polys. Row 1 (`eof_w17338`, from the west) and **the hairpin, which
  is `eof_w17168`** (piece `o168`'s row is one poly with its left leg), each lie between the rail's ground and
  one node, `eof_w17362`; a third poly (`eof_w17472`, a row from the west with a leg and a bar) lies between
  ground and a second node, the node below the lower bar (former name `eof_w17552`; it is `eof_w17362`, run 24). The three are wide: W/L 110/20, 156/21 and 167/22, against 28/19 for
  the NOR `nor17` that drives `eof_w17168`. The rail is `bc1`'s R1, followed 1,270 px south of where `bc1`
  ends it (one metal, a step west at y 17240-17270, an end at y 17568) and drawn.
- **Read, not drawn** (east of the rail; the Logic section's piece `g174` and Ambiguity 85): both nodes go on
  east by diffusion necks to one open diffusion strip (x 8400-8448, y 17315-17555), which has a load plate
  (x 8455-8500, y 17355-17445) toward the VCC rail: so the two nodes are believed one, the output of a strong
  NOR, `eof_w17362` = NOR(`eof_w17338`, `eof_w17168`, `eof_w17472`). **But the two gate polys `eof_w17168` and
  `eof_w17472` both run on east of the rail and end side by side in one heavy-outlined box on that same
  strip.** If the box is a buried contact, the gates are tied to their own drain, which makes no circuit; a
  second box of the same look, in the node's west part, has no poly at all. Nothing east of the rail is drawn.
  **Review round 29 changed the reading** (Ambiguity 85): the slot between the two arms is not field, as this
  run first had it, but has the necks' colour: the ground diffusion runs on east between the arms as a finger,
  the arms are gates along it, and the box is then the two arm ends over the field beyond the finger's end, no
  contact at all. That makes the ordinary NOR; it is believed, and is the next run's to draw and have reviewed.

Full extraction with run 23: 2,451 nets, 4,560 transistors, 0 errors, 0 warnings. The package by itself:
1,059 nets, 1,816 transistors, 0 errors, 65 warnings (as before the piece).

Run 24 (Tom Seddon's session, Claude Fable 5.2; 2026-11-20 11:13 +0000 on). One piece, `g174e`, one more
transistor (the load) and the east parts of the three gates; no uncertain item: **the unit that `eof_w17168`
gates is whole: a three-input NOR with large pull-downs, `eof_w17362` = NOR(`eof_w17338`, `eof_w17168`,
`eof_w17472`), and its output leaves south on a metal that the follower takes to the bottom bus field**.

- **Traced** (piece `g174e`): the active area runs on east of the rail (run 23's "east edge at x 8368" was
  inferred, and is not there). East of the rail it is the output node, a strip with a load on its east side;
  the ground diffusion goes on east in three places, as a band north and a sliver west of row 1's L and as a
  finger between the two arms. Each gate poly wraps its ground: row 1 runs round the strip's north end, the
  hairpin and the lower poly each turn down a right leg and along an arm; the two arms end on a small field
  island (the "box" of Ambiguity 85: no buried contact). The extraction gives W/L 258/21, 250/21 and 261/22
  for the three pull-downs and 67/37 for the load. The node below the lower poly's bar, which run 23 kept
  under a name of its own (former name `eof_w17552`), is `eof_w17362`.
- **How the narrow bands were classed**: over whole bands, against a control band of the same height that is
  certainly field (trap 38; `tools/eof_band.py`): the table in the Logic section.
- **The output**: the load's poly runs on south to a pad with a contact (8467,17603); the pad's metal goes
  south (port). `tools/follow.py` takes it 840 px south through the bottom bus field and 910 px west to
  (7552,18472): not checked, not drawn. `cudisp_drv_in`'s label is 450 px south of that end.

Full extraction with run 24: 2,450 nets, 4,561 transistors, 0 errors, 0 warnings. The package by itself:
1,058 nets, 1,817 transistors, 0 errors, 69 warnings (69 before the piece: other packages' names).

Run 25 (Tom Seddon's session, Claude Fable 5.2; 2026-11-20 12:20 +0000 on). One piece, `o362`, wiring only,
no transistor, no uncertain item: **the NOR's output `eof_w17362` is drawn on from its pad to the bottom
bus field: 840 px south, 910 px west, and through a poly hop under a rail to a second pad; it is the
third of the three bus lines y 18383 / 18428 / 18473 of which `trunks` draws the middle one**.

- **Traced** (piece `o362`): the thin metal from the pad (8467,17603) runs south over the bus field's poly
  rows with no tap (among them `ck_out`'s row y 17908), turns west at (8468,18474) and ends on a pad with
  a contact (7556,18473); that pad's poly runs west under the rail x 7468-7516 (no contact) to a pad with
  a contact (7384,18473), from which a metal goes on west (port at x 7340).
- **Not reached**: a load. `tools/follow.py` takes the metal on to (6318,18471): not checked.

Full extraction with run 25: 2,455 nets, 4,574 transistors, 0 errors, 0 warnings (the same connections as
before the piece: `tools/sameconn.py 7847ca9`, "connections identical"). The package by itself: 1,058 nets,
1,817 transistors, 0 errors, 69 warnings (other packages' names).

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

| `tcwa`, link E | x 6098-6438, y 6345-8072 | `rst_ck`'s metal on from `tl6`'s end (6105,6350): south to a corner (6105,7346), east (on `lc1_w7040`'s poly row, no contact) to a corner (6298,7346), south to a corner (6298,7432), east (on another row) to a corner (6430,7432), south through the tap's pad to y 8067, where `lc2`'s piece (`rst_ck`) takes over |
| `tcwa`, the tap | x 6412-7530, y 7632-7664 | a pad with a contact (6427,7648) on that metal; its poly row y 7640-7656 east across the crossing field to the gate group at x 7540 (drawn to x 7530) |
| `tcwa`, link F | x 6445-6695, y 8165-8374 | from `lc2`'s end (6450,8172): east to a corner (6559,8172), south (on the poly of another net's pad (6558,8127), no contact) to a corner (6559,8367), east to `trunks`' end (6690,8366) |
| `x1` | x 5053-5253, y 6345-6905 | five vertical polys of `tl5`'s bus on south from y 6350 (x 5063, 5107, 5150, 5192, 5237), straight under nine horizontal metals; four end on pads with contacts (5105,6761), (5147,6803), (5190,6845), (5237,6803), each with a metal on south to one of `lc1`'s wires at y 6900 (M_a, M_b, V2, V3); the fifth (x 5063) has no pad and runs on south. **Below three of the pads the poly goes on** (x 5150 in the open; x 5192 under V2; x 5237 under V3) and bends south-east into `lc1`'s diagonal poly bundle: drawn to y 6900 (the last to y 6872) |

| `r5nor` | x 2250-2600, y 1900-2506 | a three-input NOR in the band north of `tl1`'s strip: pull-down band y 2428-2465 under three polys (x 2362-2386, 2405-2427, 2493-2515), two VSS pads with contacts (2397,2376), (2532,2384) under an arm of the VSS plane (x 2270-2590, y 2347-2404), output strip x 2450-2478 north to a load (poly block x 2436-2526, y 2238-2292, tie box x 2499-2529, y 2304-2330), a branch of the output round the west side (y 2309-2328, x 2331-2351) to the first pull-down's drain, the output's buried contact to `tl1_w2637`'s poly (box x 2446-2474, y 2440-2466); VCC by a diffusion strap x 2288-2549 north to a head with seven contacts (y 1940) under the supply plane; a metal island (x 2272-2543, y 2184-2232) with one contact (2467,2205) on the strap |

| `isrc`, link G | x 10209-10405, y 15083-15929 | from `trunks`' metal x 10225 (y 15886): pad and contact (10226,15912), poly north to pad and contact (10226,15783), metal north / east y 15654 / north x 10312 / east y 15308 / north x 10396 to `bc2`'s pad (10395,15087) |
| `isrc`, link H | x 8650-9770, y 15244-18098 | from `trunks`' pad (9770,18081): poly west to pad and contact (9554,18081), metal y 18083 west to pad and contact (8964,18081), poly north to pad and contact (8967,17735); from there a metal north x 8968 through tap pads (8966,16737), (8962,16172) to an end pad (8966,15260), and a metal west y 17737 to a pad (8688,17737); each of the four pads' polys goes on west (stubs drawn) |

| `isrc4`, A | x 8036-8690, y 17718-17752 | the poly west of the pad (8688,17737): a row y 17728-17744 under five vertical metals and, from x 8388 to 8096, under another net's metal that lies on it, to a pad with a contact (8053,17735) |
| `isrc4`, B | x 8050-8326, y 16287-17752 | metal north on x 8057, a Z step at y 17301 onto x 8103, through a tap pad with a contact (8100,16910) (its poly row y 16900-16918 east under three tracks to a gate at x 8283-8311, ending at x 8326), a step at y 16697 onto x 8185, north to a pad with a contact (8185,16303) |
| `isrc4`, C | x 7950-8326, y 16286-16322 | the poly row y 16294-16312 of that pad: east under the track x 8229 to a second gate at x 8283-8311 (ending at x 8326), west under four tracks to a pad with a contact (7968,16303) |
| `isrc4`, D-E | x 7540-7974, y 14896-16322 | metal north on x 7967 (straight, 1,390 px), an L corner (7967,14914), west to a pad with a contact (7880,14914); the pad's poly row y 14904-14924 west under `bc1`'s metal x 7752-7795, RL3 and two more metals to `busl`'s row end at x 7550 |

| `isrc5`, A | x 6437-6536, y 8521-8643 | `lc2`'s diagonal metal on from its end (6450,8630) north-east to (6509,8571) and north to a pad with a contact (6513,8538) |
| `isrc5`, B | x 6496-6536, y 8066-8557 | the pad's poly x 6508-6528, 450 px north to a pad with a contact (6513,8087); under three metals on the way, one of them lengthwise (x 6508-6522, y 8259-8411: `tc2_sr_g`, `eofw`'s) |
| `isrc5`, C | x 6170-6565, y 7238-8094 | metal from that pad north over a poly row to a corner (6513,8018), east to a corner (6558,8018), north on x 6552-6565 to a corner (6558,7258), west along y 7252-7265 to a pad with a contact (6187,7257) |
| `isrc5`, D | x 5140-6210, y 6890-7278 | the pad's poly row y 7248-7266 west through `lc1`'s crossing field to x 5494, a 45-degree diagonal north-west (one line of `lc1`'s diagonal bundle) to (5149,6912), north onto piece `x1`'s poly of `rst_a` |

| `rl`, `res_b` | x 5190-6612, y 6890-8700 | poly diagonal (centre x = y - 1698) from piece `x1`'s end (5203,6900) to (5516,7214); row y 7205-7223 east to a pad with a contact (6146,7214); metal y 7216 east to a corner (6602,7216), south on x 6596-6608 to a corner (6602,8065), west to (6558,8065), south to a pad with a contact (6558,8125); poly column x 6549-6567 south (under `rst_ck`'s link F lengthwise, y 8166-8367, and two more metals) to a pad with a contact (6556,8493); metal south to (6557,8585) and at 45 degrees south-west onto `lc2`'s metal end (6450,8692) |
| `rl`, `lpstb_b` | x 5230-6655, y 6866-8765 | poly diagonal (centre x = y - 1632) from piece `x1`'s end (5240,6872) to (5538,7170); row y 7161-7179 east to a pad with a contact (6188,7170); metal y 7173 east to a corner (6645,7173), south on x 6639-6651 to a corner (6645,8108), west to (6601,8108), south to a pad with a contact (6602,8320); poly column x 6593-6611 south under three horizontal metals to a pad with a contact (6602,8536); metal south to (6601,8605) and at 45 degrees south-west onto `lc2`'s metal end (6450,8756) |
| `w5936`, to latch C | x 5054-6540, y 6876-8072 | poly from piece `x1`'s end (5063,6880): the bend at y 6892, a diagonal (centre x = y - 1829) to (5471,7300), row y 7291-7309 east to a pad with a contact (6146,7301); metal y 7303 east to a corner (6514,7303), south on x 6508-6520 **through** a pad with a contact (6513,7889) to a corner (6514,7978), west to (6471,7978), south onto `lc2`'s metal x 6471 at y 8067 (its pad (6470,8127): latch C's data) |
| `w5936`, to the box | x 6494-7522, y 7868-8444 | the pad's poly row y 7878-7898 east under seventeen tracks to a pad with a contact (7401,7888); metal south on x 7396-7408 to a pad with a contact (7401,8425); poly y 8417-8439 east to the west edge of a heavy-outlined box (7490-7520, 8410-8442), not drawn |
| `d3982`, U4 | x 7440-7778, y 8330-8448 | the inverter that drives `tl3_w3982` (cell `eof_dinv`, `tl5_inv` turned 180 degrees, drawn from this copy): VSS box y 8330-8373 with a contact (7568,8348) under the rail x 7552-7598, gate row y 8376-8396 directly below it (from the band x 7416-7440 to a rounded end at x 7614), node y 8398-8426; the node west on a strip y 8404-8428 to the output's buried contact (box 7490-7520, 8410-8442), on which piece `w5936`'s poly ends; east on a strip y 8405-8432 under the plate (x 7666-7722, y 8383-8448) to the VCC box (7728-7778, 8374-8432, contact (7750,8408)) under the wide metal x 7722-7776; a tail x 7640-7660 from the strip up to a hook under the tie box (7655-7697, 8352-8385), into which the plate's tab comes |
| `d3982`, U2 and U3 | x 7416-7778, y 8068-8196 and 130 px lower | two inverters of a larger build (cell `eof_dly`, master U2; U3 = `@inst eof_dly 0,130`, findcell 0.93): VSS box y 8068-8110, contact (7568,8086), gate row y 8114-8136 (to x 7606), node y 8137-8180; west on a strip y 8156-8176 to the output's buried contact (box 7487-7523, 8153-8187); east out from under the rail at y 8154-8174, a diffusion arm x 7612-7628 north to y 8118, the load's strip y 8118-8145 east under a long plate (x 7634-7730, y 8100-8166) to the VCC box (7736-7778, 8112-8175, contact (7748,8143)); the node also on east to the tie box (7645-7680, 8170-8195) under the plate's tab. The output's poly: from the box a row y 8158-8180 west to a band x 7416-7440, south, and east as the next unit's gate row (U3's y 8244-8266, U4's y 8376-8396) |
| `d3982`, the input | x 6401-7440, y 8030-8136 | from `lc2`'s poly (`P 6401,8067:6415,8092`, `lc2_w8083`) north on x 6401-6416 to a corner, the row y 8030-8050 east 1,010 px under twenty-one tracks (x 6430 `rst_ck`, 6471 `tl3_w3982`, 6514 `rst_a`, 6601 `res_b`, 6645 `lpstb_b`, 6688, 6731, 6775 `rcs_e4`, 6818, 6861, 6905, 6948, 6991, 7078, 7121, 7164, 7208, 7273, 7316, 7359, 7403 `tl3_w3982`), the band x 7416-7440 south from y 8030 into U2's gate row |
| `d3982`, the rails | x 7552-7598 and 7722-7776, y 7855-8460 | piece `g7700`'s VSS rail and wide VCC metal on south over the four units |

| `g7700`, the gate | x 7541-7775, y 7585-7860 | VSS rail x 7552-7598 over a diffusion column x 7541-7611, y 7613-7820, with one contact (7572,7684); three poly rows across it: row 1 y 7638-7656 (`rst_ck`), row 2 y 7708-7728 (`tc2_sr_g`), row 3 y 7767-7787 (`eof_w7777`); a diffusion ring east of the rail (top strip y 7613-7628, strap x 7637-7654, bottom strip y 7745-7757) round a field island x 7612-7636 on which rows 1 and 2 end; the output node south of row 3: east by a T-shaped diffusion wire (arm y 7803-7817, vertical x 7643-7658, y 7783-7854) to the load's strip (y 7783-7809) and the tie box (7664-7690, 7832-7854); load plate x 7666-7721, y 7761-7827; VCC box x 7726-7773, y 7759-7808 with contact (7748,7779) under the wide metal x 7725-7775 |
| `g7700`, the output | x 7254-7545, y 6875-7839 | diffusion wire west from the column (y 7803-7822) to a buried contact (7490-7518, 7805-7832); poly row y 7812-7831 west to a pad with contact (7402,7822); thin metal x 7401 north to a pad with contact (7401,7606); poly west along y 7604 under two metals to a pad with contact (7273,7606); thin metal x 7272 north to a pad with contact (7272,6912); the pad's poly on north (drawn to y 6875) |
| `g7700`, row 2 | x 7244-7632, y 7198-7800 | poly y 7726-7745 west (a widened step at x 7500-7527) to a pad with contact (7267,7736); from the pad a metal east and north (corner (7315,7736)) to a pad with contact (7313,7215), whose poly row leaves east (drawn to x 7400), and a metal south (x 7268, drawn to y 7800) |
| `g7700`, row 3 | x 6450-7634, y 7767-7831 | poly y 7767-7787 west from its end cap (x 7634) across the crossing field to a corner (6886,7777), south one track, west along y 7812-7830 to `lc1`'s east edge x 6450 |

| `ff3`, the flip-flop | x 4578-4985, y 9220-9955 | `@inst lc2_ff 0,780`: `lc2`'s cell (gates K1-K4, 19 transistors) 780 px lower, under the same west rail (x 4752-4820) and middle rail (x 4924-4980). Under the west rail (`railprof.py 4752 4798 9200 9860`): K1's rows y 9245-9271, 9296-9309; K2's 9418-9442, 9461-9485; K3's 9592-9616, 9647-9671; K4's 9758-9781, 9801-9824, 9844-9859 and one more (y 9913-9932) |
| `ff3`, the copy's own | x 4458-4980, y 8695-9990 | K1's VSS node, a short box y 9196-9242 under the west rail with one contact (4765,9211) (the master has a long contact column there); both rails y 9185-9970; track C (x 4553-4571) from `lc2`'s end (y 9190) to the copy's row-2 pad (4561,9296); track A (x 4466-4484) from `lc2`'s end (y 9060) to its END pad with a contact (4473,9818); track B (x 4508-4526) from `lc2`'s end (y 8700) through the pad with a contact (4517,9384) of the clear row, drawn to y 9420; the clock's L-shaped metal from the END pad (4648,9904) west along y 9897-9919 and south on x 4553-4575, drawn to y 9990 |

| `r4lat` | x 13868-14004, y 15618-15728 | the load of the lower half of `bd1`'s latch: a poly block x 13937-13992, y 15644-15704 below `bd1`'s band (y 15630-15650, the net `bd1_q`), over a diffusion strip y 15659-15689 from the VCC land (x 14000) west to x 13916; the strip's west end (x 13919-13934) south by a dogleg as an arm x 13908-13929 to y 15728 and west along y 15712-15728 to N2 under the ground rail; the tie, a heavy-outlined box (13889-13913, 15660-15682) below the band's west end (uncertain); the poly from gate G4's block to the band (x 13895-13909, y 15618-15640) |

| `n2out` | x 13795-13832, y 15638-15736 | two diffusion links in the open gap between `bd1_an`'s metal (east edge x 13793) and the ground rail (west edge x 13822): N2's west part (x 13795-13830, y 15712-15736) onto the lower segment of `bd1`'s strip, and the strip's top segment east (x 13795-13840, y 15638-15652) onto the ground diffusion (VSS contact (13845,15657)) |
| `n2w`, A-B | x 13331-13582, y 16250-16621 | `bd1`'s metal x 13521 turns east at y 16264 and south on x 13564 to a pad with a contact (13562,16604); a poly row y 16604 west under three tracks to a pad with a contact (13348,16604) |
| `n2w`, C-D | x 12831-13353, y 16600-17794 | metal south on x 13347, a 45-degree diagonal from (13347,16712) to (13220,16839) (over `wr_r7`'s poly diagonal, no contact), south on x 13218 to a pad with a contact (13217,17776); a poly row y 17776 west under the vertical trunks and the wide VCC rail x 12890-12985 to a pad with a contact (12848,17777) |
| `n2w`, E-F | x 10205-12850, y 17586-18010 | metal west along y 17779, the outer of three nested Z bends (north on x 11722 over four poly diagonals, west along y 17606) to a pad with a contact (11287,17603); a poly west to x 11137, a diagonal south-west to (10835,17905), west along y 17905 (its last 96 px under `ck_out`'s metal, no contact), south on x 10224 to a pad with a contact (10222,17993) |
| `n2w`, G-L | x 7405-10239, y 17990-18099 | metal south and west along y 18039 to a pad (9813,18037); poly under two metals to a pad (9594,18038); metal west (over `isrc`'s poly x 8964, no contact) to a pad (8643,18038); poly under two metals to a pad (8424,18039); metal west, a step south at x 8182 to y 18083, west to a pad (7600,18082); poly under `bc1`'s rail RL2 to a pad (7422,18081) |
| `n2w`, M-O | x 6692-7424, y 15000-18090 | metal west along y 18083 to a corner (6712,18083), north on x 6712 to a pad with a contact (6708,16519); a poly link x 6712 north under the supply buses to a pad with a contact (6710,16173); metal on north on x 6711, drawn to y 15000 |
| `ck5`, the poly from `tc2` | x 6442-6470, y 6390-7147 | `tc2`'s poly x 6443-6460 on south from y 6400 under fourteen horizontal metals to a pad with a contact (6450,7127) |
| `ck5`, the track | x 6444-6695, y 7121-8296 | metal east along y 7128 to a corner (6688,7128), the track x 6688 south over twelve poly rows to a corner (6688,8151), west to (6644,8151), south to a pad with a contact (6645,8276) |
| `ck5`, the column and the diagonal | x 6433-6665, y 8257-9174 | poly column x 6636-6654 under three horizontal metals to a pad with a contact (6645,8580); metal south to (6645,8628), a diagonal (x + y = 15272) to (6472,8801), south on x 6472 to y 9167, west onto `lc2`'s metal end at x 6450 |
| `rc` | x 6440-6489, y 8905-9459 | `rst_c`'s poly from `lc2`'s end (6450,8923) on at 45 degrees to (6472,8945), south under `ck5`'s metal to a pad with a contact (6469,9209); metal south on x 6472 to (6471,9452), west onto `lc3`'s metal end at x 6450 |
| `n2n`, the track | x 6768-6954, y 8703-10400 | metal north on x 6775 from `busl`'s north edge (the track is drawn by no one south of it), a 45-degree diagonal (x + y = 15727) from (6775,8952) to (6947,8780), north to a pad with a contact (6947,8710), the last of a staircase of four pads |
| `n2n`, the column | x 6934-7009, y 8409-8727 | the pad's poly x 6941-6961 north under three horizontal metals to y 8428, east along y 8416-8440 to a pad with a contact (6988,8427) |
| `n2n`, the metal | x 6139-6998, y 6993-8427 | north on x 6991 over ten poly rows to an L corner (6991,7000), the middle of three nested corners; west along y 7000 over five vertical polys to a pad with a contact (6146,6997) |
| `n2n`, the row and the diagonal | x 5403-6166, y 6345-7015 | the pad's poly row y 6988-7004 west under the crossing field's tracks to (5624,6996), a 45-degree diagonal (x - y = -1372) to a bend (5412,6784), north on x 5403-5421 under nine horizontal metals onto `tl5`'s poly end at y 6350 (`bd1_n2`) |
| `ck6`, the wire | x 7550-8986, y 14768-15058 | `busl`'s poly row y 14772-14796 on east to a pad with a contact (7837,14784); the bus metal y 14784 to a pad with a contact (8293,14785); a poly L south and east along y 14816-14834 (under R1, the VCC vertical and the VSS band; in the open from x 8735), south at x 8957-8980 to a pad with a contact (8967,14870); a metal south on x 8968 to a pad with a contact (8962,15040); a poly row y 15034-15050 west to the inverter's output box |
| `ck6`, the inverter U | x 8508-8854, y 14942-15062 | VSS box under the rail x 8687-8737 with a contact (8712,14965); gate row y 14990-15010 from a pad with a contact (8836,15000); the channel runs on east of the rail to x 8768; node south of the gate with its output box (8768-8797, 15030-15052) east of the rail; load west: strip under `bc1`'s thin metal x 8637-8650 and under a plate x 8568-8607 to the VCC box under R2 (contact (8534,15033)); tie box (8628-8648, 14977-15000) under the thin metal; the gate pad's metal x 8830-8848 south to a pad with a contact (8833,15127), the output of the unit below |
| `vw`, unit V | x 8508-8897, y 15100-15285 | under the rail x 8687-8737 a stack of two gates (rows A y 15163-15187 and B y 15204-15228, one hairpin poly with a pad (8880,15172) on its bend) between the node (y 15111-15164) and a VSS box (contact (8702,15260)); output box (8765-8800, 15116-15140) east of the rail; load plate x 8570-8622, y 15100-15148 with a pad (8592,15168) and a tie box (8627-8650, 15160-15187); under `bc1`'s thin metal x 8637-8650 a column of the node with a third gate (the arm y 15205-15228 of W's plate poly) and a pocket into the VSS box |
| `vw`, the stacks' east part | x 8738-8797, y 15118-15424 | both stacks' diffusions run on east of the rail through the open gap to under `bc1`'s thin metal x 8789-8801 (east edge x 8797), so that rows A, B, 1 and 2 are gates 90-105 wide; between V's ground and W's output pad the diffusion narrows to x 8754-8797 under row C (`rst_a`, y 15251-15270) |
| `vw`, unit W | x 8508-8940, y 15262-15472 | under the rail a stack of two gates (row 1 y 15329-15355 from a pad (8881,15351), row 2 y 15372-15398 from a pad (8922,15392)) between the node (y 15309-15330) and W's ground (contact (8722,15440)); output box (8762-8802, 15285-15320), its row to a pad (8835,15302); load plate x 8568-8622, y 15298-15335 (one poly with V's arm); under the thin metal x 8637-8650 a column of the node with a third gate (the row of the pad (8592,15383), V's output) and a foot into W's ground |
| `vw`, the wires | x 8580-9150, y 14645-15472 | V's plate pad to the pad (8592,15383) by a metal x 8580-8604; the hairpin's metal x 8882 north to (8882,14785), east to a pad (9054,14785), poly north and east along y 14653; row 2's metal x 8925 north to (8925,14828), east to a pad (9008,14828); W's output metal x 8838 south to a pad (8836,15456); row 1's metal x 8881 south (to y 15465) |
| `in390` | x 9005-10275, y 14594-15520 | `bc2_w15607`'s poly column x 9005-9023 north of the pad (9008,14828), under `eof_w15172`'s metal y 14785 and `bc1`'s bus metals y 14742, 14699, 14656; east at y 14600-14621 as a row (the bus metal y 14603-14618 on it to x 9190), 1,070 px under eleven vertical metals to a pad with a contact (10092,14609); a metal east along y 14611 to a corner (10268,14607) and south on x 10268 onto `bc2`'s metal end (10267,15515) of latch unit b's output pad |
| `in172`, the row | x 9140-10520, y 14644-14714 | `eof_w15172`'s poly row y 14644-14664 on east of x 9150 under the same vertical metals, a step south at x 10284-10302, the lower row y 14687-14704 under the metals x 10355 and x 10397 into the output box (10484-10520, 14681-14714) |
| `in172`, unit T | x 10335-10772, y 14590-15007 | a NOR at the top of `bc2`'s east column: a diffusion body west of the VSS rail (x 10495-10530, y 14622-14771) whose top and bottom bands run into two VSS boxes under the rail (contacts (10562,14613), (10562,14769)); gate row 1 (y 14643-14665) from pad A (10352,14654), gate row 3 (y 14728-14750) from pad B (10440,14738); the node between them with the output box; a node strip y 14690-14706 east under the rail to the load: a plate x 10660-10716, y 14668-14762 over a strip to the VCC box (contact (10742,14712)), a tail south into the tie box (10624-10652, 14738-14768); pad A's metal x 10355 south to a foot onto `bc2`'s pad (10395,15000), pad B's metal x 10441 south onto `bc2`'s metal at y 14940; the two rails over the unit |
| `in350`, the metal south | x 8866-8940, y 15455-17656 | `ck_out`'s metal from W's row-1 pad on south on x 8882; a step one track east (x 8925) from y 15698 to y 15915, round another net's pad (8882,15745) and its metal in the vacated position; through two pads with contacts, (8882,16648) and (8882,16867), each the east end of a poly row that runs west under the track x 8838 to the gate column (drawn to x 8806); on south to a corner (8882,17649) |
| `in350`, the L | x 8584-8890, y 17642-17922 | west along y 17649 (on another net's poly row for 300 px, no contact) to a corner (8600,17649), south on x 8600 over four poly rows to a pad with a contact (8598,17908) |
| `in350`, east to `ck_out` | x 8584-10245, y 17895-17922 | from that pad a metal east along y 17910, 1,000 px, to a pad with a contact (9596,17909); the pad's poly row y 17899-17914 east under a wide vertical metal (x 9641-9685) and a thin one (x 9723-9735) to a pad with a contact (9769,17910); a metal east onto `trunks`' end of `ck_out #1` at x 10230; on each of the two pads a second metal from the north (x 9589-9604, x 9762-9778), drawn as stubs to y 17866 |
| `in350`, west | x 8380-8588, y 17866-17925 | the poly of the pad (8598,17908) west along y 17899-17915 under the VSS rail and a thin metal to a pad with a contact (8424,17908); stubs of that pad's metal north (x 8418-8430) and of its poly on west |
| `lat16`, the latch | x 8508-8815, y 16493-16975 | a mirrored copy of `tl1`'s latch (`@inst tl1_ua 5976,12146 mx=2685`, `@inst tl1_ub 5973,12146 mx=2686.5`; x' = 11346 - x, y' = y + 12146) under column B's VSS rail x 8686-8731, loads under the VCC rail x 8510-8560; its own VSS box at the foot (8695-8745, 16922-16975; contact (8713,16950)), the long VCC contact (8537,16745), the thin metal x 8588-8600 between the upper plate (contact (8594,16648)) and the pad of the lower unit's third pull-down (contact (8594,16846)) |
| `lat16`, the rows | x 8800-9062, y 16598-16874 | from the cells' east edge (x 8806): data y 16598-16616 to the track x 8838; enable y 16640-16658 to `ck_out`'s pad (8882,16648); upper node y 16683-16702 to a pad with a contact (9012,16693) and a metal south (stub to y 16850); clear y 16771-16789, a step north at x 8893-8910, y 16728-16746 to `rst_a`'s tap pad (8966,16737); lower node y 16813-16832 to x 9022, north on x 9004-9022 to y 16724, east along y 16724-16745 to x 9062 (port), and a branch under the track x 8925: a column x 8917-8935 south to y 17003 and west along y 16986-17003 to x 8760 (port); enable y 16855-16874 to `ck_out`'s pad (8882,16867) |
| `inv16`, the inverter | x 8512-8800, y 16317-16465 | between the two latch copies, by hand: under the VSS rail the box (y 16317-16381, contact (8717,16349); also the foot of the upper copy's stack), the gate (y 16382-16403), the node (y 16404-16436); the node's strip east to a buried-contact box (8774-8800, 16417-16446); the load west of the rail: strip y 16381-16409 under a plate (8563-8655, 16372-16432) to a VCC box (8512-8560, 16380-16440; contact (8533,16412)), a tie box (8618-8660, 16433-16465) under the thin metal x 8637-8650 (uncertain) |
| `inv16`, its wires | x 8684-9027, y 16340-16616 | the gate row y 16380-16400 from a pad with a contact (9010,16388) (a metal from the north ends on it: stub to y 16340) west under four tracks to the rail; the output poly from the box east along y 16421-16443 and south under the track x 8838 (x 8826-8847, y 16421-16616) into the latch's data row |
| `lat15`, the latch | x 8508-8815, y 15886-16368 | the upper mirrored copy of `tl1`'s latch (`@inst tl1_ua 5976,11539 mx=2685`, `@inst tl1_ub 5973,11539 mx=2686.5`; x' = 11346 - x, y' = y + 11539: the lower copy moved 607 px north) under column B's VSS rail, loads under the VCC rail; the foot of its lower stack is the VSS box of the inverter `inv16`; long VCC contacts (8537,16138), (8535,16253) and one more (8532,15930); the thin metal x 8588-8600 between the upper plate (contact (8594,16041)) and the pad of the lower unit's third pull-down (contact (8594,16239)) |
| `lat15`, the rows | x 8800-9026, y 15984-16278 | from the cells' east edge: data y 15991-16009 to a pad with a contact (8838,16000) in the run of the track x 8838; enables y 16031-16049 and y 16248-16267 to pads with contacts (8925,16040), (8925,16262) on one metal x 8925; upper node y 16076-16095 to a pad with a contact (9007,16082) and the metal x 9011 south to the inverter's pad (9010,16388); clear y 16164-16182 to `rst_a`'s tap pad (8962,16172); the lower node's row ends at x 8812 |
| `lat15`, the data track | x 8800-8900, y 15722-16030 | from the data pad north on x 8838 to y 15868, east to x 8880, north over two poly rows to a pad with a contact (8880,15738); the pad's poly row y 15727-15745 west to x 8800 (port); the track south of the data pad to y 16030 (port) |
| `cap16`, the box and the diffusion | x 8908-9254, y 16434-16745 | the lower node's leg on east to x 9090, north on x 9068-9090 into a buried-contact box on a diffusion pad (9056-9102, 16672-16706); a neck x 9070-9088 north to a diffusion rectangle x 8908-9254, y 16477-16607 (with a step x 9167-9254 up to y 16434): no gate, no contact |
| `w16693`, the upper node's wire | x 8800-9028, y 16840-17135 | the metal x 9012 south to a pad with a contact (9011,17080); the pad's poly 35 px south and west as a row y 17116-17135 under four tracks to x 8800 (port: the unit south of the latch) |
| `inv17`, the inverter | x 8512-8814, y 16960-17072 | a copy of `inv16`'s build 607 px lower, by hand: under the VSS rail the latch `lat16`'s foot box as source, the gate (y 16986-17006: the west end of `eof_w16823`'s branch row), the node (y 17011-17043); the node's strip east (y 17024-17039) to a diffusion pad (8772-8814, 17021-17063) with a metal contact (8791,17040); the load west of the rail: strip y 16988-17016 under a plate (8563-8655, 16974-17039) to a VCC box (8512-8562, 16987-17047; contact (8533,17019)), a tie box (8618-8660, 17040-17072) under the thin metal x 8637-8650 (uncertain) |
| `inv17`, its output wire | x 8778-9030, y 17040-17610 | a thin metal (10 px) from the pad: a diagonal (8791,17062)-(8798,17095), south on x 8798, x 8796 from y 17272, over three boxes of other nodes (y 17144-17210, 17318-17368, 17454-17497: uncertain) to a pad with a contact (8792,17561); the pad's poly row y 17551-17569 east under four tracks to a pad with a contact (9008,17560); its metal south (stub to y 17610) |
| `nor17`, the gate | x 8700-8805, y 17074-17290 | VSS box under the rail (y 17074-17111, contact (8722,17092)); a band east (y 17097-17110) into the top of a diffusion column x 8757-8785 east of the rail; row 1 (y 17116-17135, `eof_w16693`) over it; the node (y 17135-17203) with a buried-contact box (8765-8802, 17151-17192) in which row 2, the output, ends; row 3 (y 17203-17222, `eof_w17212`) over it; a band west (y 17231-17245) into a second VSS box under the rail (y 17231-17290, long contact (8714,17258)) |
| `nor17`, the load | x 8508-8760, y 17148-17238 | the node's strip west under the rail (y 17163-17181), under the thin metal x 8637-8650 and a plate (8573-8623, 17148-17232; strip y 17166-17190) to a VCC box (8508-8565, 17162-17208; contact (8525,17183)); a tie box (8628-8662, 17196-17238) under the thin metal, with a tab of the plate and a tail of the strip (uncertain) |
| `nor17`, the output | x 8774-9064, y 17155-17600 | row 2 (y 17160-17178) east under the thin metal and four tracks to a pad with a contact (9007,17170); metal south on x 9011 over row 3 to a corner (9011,17518), east to (9057,17518), south (stub to y 17600) |
| `nor17`, rows 1 and 3 | x 8740-9114, y 17116-17226 | row 1 on west from x 8800 to its end at x 8741; row 3 from its end at x 8740 east under the thin metal and six tracks to a pad with a contact (9098,17210) |
| `in212` | x 8990-9106, y 15805-17210 | the track x 9099 from row 3's pad north, straight, to a corner (9099,15870), west to (9053,15870), north to a pad with a contact (9053,15822); the pad's poly row y 15812-15832 west (stub to x 8990); one stretch (y 16666-16718, over the edge of piece `cap16`'s pad) uncertain |
| `o168`, the first row | x 8573-9073, y 17600-17698 | `eof_w17168`'s metal x 9057 on to a pad with a contact (9055,17648); the pad's poly row y 17638-17656 west under the tracks x 9011, 8968, 8925 and under `ck_out`'s metal y 17649 (x 8600-8882), a leg south at x 8573-8588 in the open gap between the rail and the metal x 8600 |
| `o168`, the second row | x 8339-8588, y 17630-17698 | the row y 17682-17698 west under the rail x 8500-8562, the tracks x 8470 and x 8425 and `ck_out`'s second metal (which lies on it from x 8426 to x 8355), a leg north at x 8353-8371 to a pad with a contact (8355,17649) |
| `o168`, the metal and the last pad | x 8172-8361, y 17410-17656 | metal west along y 17650 to a corner (8186,17650), north on x 8186 to a pad with a contact (8185,17428), where it ends; the pad's poly row y 17419-17440 east, drawn to x 8245 (port) |
| `o040`, the metal and the row | x 8322-9017, y 17604-17796 | `eof_w17040`'s metal x 9010 south from the pad (9008,17560) to a corner (9010,17780), west along y 17780 over `rst_a`'s poly column x 8964 to a pad with a contact (8733,17778); the pad's poly row y 17768-17786 west under the thin metal x 8643, the metal x 8600, the rail x 8500-8562 and the tracks x 8470, 8425, 8382 to a pad with a contact (8338,17777) |
| `o040`, the track | x 8005-8345, y 16292-17784 | metal west along y 17777 to a corner (8012,17777); north on x 8012; a Z step at y 17259 onto x 8057; north to a corner (8057,16647); east along y 16647 to x 8143; north on x 8143 onto `bc1`'s metal end (8143,16300) of `bc1_g6_in` |
| `g174`, the rail | x 8316-8382, y 16300-17568 | column A's VSS rail south of `bc1`'s end: x 8338-8382 to y 17250, a step west at y 17240-17270, x 8316-8362 to its end at y 17568 |
| `g174`, the active area | x 8258-8411, y 17266-17560 | one diffusion under the rail and west of it in the open to a straight edge x 8254-8258; contacts onto the rail at (8335,17293) and (8335,17474). It runs on east of the rail (piece `g174e`) |
| `g174`, row 1 | x 8245-8413, y 17331-17351 | `eof_w17338`: a poly row right across the active area; a port at its west end; east of the rail: piece `g174e` |
| `g174`, the hairpin | x 8200-8372, y 17373-17441 | `eof_w17168`: piece `o168`'s row y 17419-17441 on to a left leg x 8305-8323 and a top bar y 17373-17395, which runs on east of the rail (piece `g174e`) |
| `g174e`, the active area east of the rail | x 8368-8467, y 17263-17560 | the output node's strip (x 8389-8452), the ground's band (y 17263-17282), sliver (x 8368-8388) and finger (y 17447-17468, to x 8411), and a field island x 8411-8434, y 17419-17498 |
| `g174e`, the gates' east parts | x 8370-8472, y 17282-17543 | row 1's L (to x 8472), the hairpin's and the lower poly's right legs (x 8370-8389) and arms (to x 8424, ending on the island) |
| `g174e`, the load | x 8446-8558, y 17326-17560 | a plate x 8461-8498, y 17360-17447 with a tie box (8458-8482, 17330-17354); the diffusion under the VCC rail with contacts (8528,17477), (8509,17513); the rail R2 on south, x 8488-8558 |
| `g174e`, the output | x 8455-8485, y 17445-17634 | the plate's tail south to a pad with a contact (8467,17603) and 30 px of its metal (port) |
| `g174`, the lower poly | x 8226-8372, y 17464-17560 | `eof_w17472`: a row y 17464-17486, an east leg x 8274-8296, a bottom bar y 17521-17543 under the rail (east of it: piece `g174e`); west of the active area the row turns south on x 8226-8242 (port at y 17560) |

The bundle left of the right datapath has tracks L0..L11 at x 13348 + 43.4 k.

## Logic

Wiring only. What the join gives (traced; equations from the full extraction):

```
rc_eq_r4 = NOR(r4c_b0_x .. r4c_b6_x)                 rdp2: high when the row counter equals R4
bd1_an   = NOT rc_eq_r4                              bd1's inverter A            (firm)
bd1_n1   = NOT(bd1_n2 OR (rst_lat AND rc_eq_r4))     upper half of bd1's latch   (depends on bd1's ? items)
bd1_n2   = NOT((bd1_an AND rst_lat) OR bd1_n1 OR rst_a)   lower half; load: piece r4lat (run 7); third term: piece n2out (run 8); depends: the tie
```

(Until run 7 the lower half had no load and the first equation read `bd1_q` for `bd1_n2`: piece `r4lat`,
below, shows they are one net.)

`tools/unsure.py --equations`: `rc_eq_r4` FIRM, `bd1_an` FIRM, `bd1_n1` DEPENDS (on `bd1`'s
uncertain items, none of them on this wire). `tools/unsure.py` does not list `rc_eq_r4`: no
uncertain item lies on the path from the comparator's NOR to the two gates.

Traced since run 7 (piece `r4lat`; marked, the two load ties): the two halves are a transparent latch
of this signal, open while `rst_lat` is high; `rst_lat` is a copy of `rst_a`, the signal that also
stops `ck_b` (`rst_ck`) and the row counter's step (`rst_rc`). So **what R4's match does at the
end of the frame goes through this latch**. Since run 8 (pieces `n2out`, `n2w`): the latch's exit is
`bd1_n2`, on the wire `bd1` called `bd1_k`, gated low while `rst_a` is high, and followed as far as
(6711,15000) in the left bus field; `bd1_n1` and `bd1_an` go nowhere else.

### The path, north to south

| Stretch | Drawn by | What | Evidence |
|---|---|---|---|
| comparator to the counter channel | `rdp2`, `mrach` | NOR at about (15000,8426); poly west and south to track T6 (= L0), contacts (13348,9360), (13349,9663); poly east along y 9663 to x 13425 | their notes; not re-read |
| **link A** | `eof` | the poly row runs on under L1 (`wr_r4`: no pad, no hole) to a pad with a contact (13433,9665), top of L2's upper piece; that metal ends on a pad with a contact (13432,9925); a poly bar goes east along y 9925 under L3 (`h_eq_r2`), L4, L5 (`rc1`), L6 with no contact, to a pad with a contact (13650,9925), top of L7 | `a_top.png` (2.8x, metal / chip-2 stripped / clean), `a_bar.png` (4x, three shots), overlay `ov_a.png`; text maps of both pads' rows and of the whole bar in both metal shots and the clean shot (each end pad: bright centre in a dark ring in both chips and a green hole in the clean shot; the bar plain between); `tools/follow.py` on both metals; `tools/tla_contacts.py` on both: no candidate |
| L7, L6, L5, link, L9 | `rdp3` | L7 from y 10700, jog west onto L6 at y 11507, onto L5 at y 12313, contact (13565,12826), poly link east under L6 and L7, contact (13736,12826), L9 south to y 13480 | read again here from text: `tools/follow.py 13651 10710 S` gives the two jogs and the end as drawn; its three contact candidates ((13651,11346), (13564,12585), (13563,12611)) are field under whole metal (text maps); the link's poly is continuous under L6 and L7 with no hole. The east contact: see Ambiguity 1 |
| **link B** | `eof` | L9, one straight metal y 13480-14690; crosses `hc5`'s poly (y 13880-13908) and `hc4`'s band (y 14010-14038) without a pad | `b_l9_m.png`, `b_l9_c.png` (2x strips, metal and clean shot, every package's trace outlined); follower positions every 200 px; text maps of the band crossing and of the one contact candidate (y 14222: field under whole metal) |
| k15 to the gates | `bd1` | k15 from y 14690, jog west at y 15087 to x 13652, contact (13655,15391), poly to gate P2 (in series with `rst_lat`'s P3 on node `bd1_n1`) and P4 (inverter A) | `tools/follow.py 13738 14700 S` gives the jog and the end as drawn; `d_bd1.png` (2.35x, all traces): the overlay sits on the features. The gate column itself was not re-read (`bd1`'s re-read item R1 stays) |

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
output of `tl1`'s third latch (open while `ck_out` is high, takes `tl4_w4068`); `rcs_c1` =
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

### Piece `isrc`: `rst_a` on from two of its open ends (traced; wiring only)

```
rst_a_n      = NOT rst_a                                              bd1 (X's driver)
bc2_w15029 = NOT((bc2_w14876 AND bc2_w14955) OR bc2_w15000 OR rst_a)   bc2's latch unit a: rst_a is its clear
```

The full extraction has one net `rst_a` with three gates on it: `bd1`'s two and now `bc2`'s
clear pull-down (10510,15088). `tools/unsure.py` does not list `rst_a`. `bc2`'s unit itself was
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

### Piece `isrc4`: `rst_a` is `lc2`'s through line x 6299 (traced; wiring only)

```
rst_a = lc2's line x 6299        one net: lc2's first through line, lc3's and busl's line 1, this piece, piece isrc, trunks
```

The full extraction has one net fewer (2,397) and no separate net for `lc2`'s through line x 6299; `rst_a` keeps its three gates
(`bd1`'s two, `bc2`'s clear). `tools/unsure.py` lists neither name: no uncertain item on the path. The
alias in `trace/eof.txt` was dropped by the rename of 2026-11-19.

The path, from the open end of piece `isrc` back to `busl`'s row:

| Stretch | Drawn by | What | Evidence |
|---|---|---|---|
| the pad (8688,17737) | `eof` (run 4) | the west end of the metal y 17737 | piece `isrc` |
| **A**, poly row y 17728-17744 | `eof` | west from the pad under five vertical metals (x 8418-8430, 8462-8474, the rail 8510-8558, 8590-8602, 8634-8646) with no contact, then under another net's metal from x 8388 to 8096 (Ambiguity 29), to a pad with a contact (8053,17735); the pad is the row's west end (field west of it) | `h_r4.png` (1.7x, three shots), `j_ov4.png`; `textmap.py 8370 17716 8660 17758 4` (the vertical metals bright through, no ring; the clean shot's dips are the bars of the gaps between metals, the same on the neighbouring rows); `px.py col 8300 17712 17760 3` and `col 8660` (the row's width); `textmap.py 8020 17702 8092 17762 3 --acid` (the pad: bright centre x 8050-8056 in a ring in both chips, hole in the clean shot) |
| **B**, metal x 8057 | `eof` | north from the pad, 420 px; chip 1's metal is blemished at y 17400-17435 and 17508-17527 (chip 2 whole, no ring: not contacts) | `follow.py 8050 17700 N`; `tl5_tracks.py v 8057 17314 17714`; `textmap.py 8027 17388 8090 17448 3`, `8027 17498 8090 17534 3` |
| **B**, the step at y 17301 | `eof` | a Z: east 46 px onto x 8103; the neighbouring tracks make the same step (the whole bundle moves one track east going north) | `i_c2.png` (3.9x, both metal shots); `tl5_tracks.py h 17301 8064 8094`: no break |
| **B**, metal x 8103 and the tap | `eof` | north 590 px; at (8100,16910) it runs **through a pad with a contact** (ring 46 px, bright centre in both chips, hole in the clean shot), whose poly row y 16900-16918 runs east under the tracks x 8143, 8186, 8229 (no contact) and in the open to a gate over the diffusion column under the thin metal x 8283-8307, ending at x ~8326 in the gap before the rail | `i_p1.png` (3.8x, three shots), `i_tap.png` (3.4x, three shots); `tl5_tracks.py v 8103 16712 17288`; `textmap.py 8076 16884 8250 16932 3 --acid`; `px.py row 16909 8236 8346 3` in four shots (channel colour 235-251/154-181/98-122 at x 8287-8311 in the clean shot; poly orange at x 8320-8326 in the chip-2 metal shot) |
| **B**, the step at y 16697 | `eof` | east 82 px (two tracks) onto x 8185, over a large diffusion-coloured area (Ambiguity 32) whose east edge is a 9 px bar across the metal at x 8164-8172 | `i_c1.png` (3.9x, both metal shots), `i_L.png`; `tl5_tracks.py h 16697 8112 8180`; `px.py row 16697 8150 8190 2 metal,metal1` |
| **B**, metal x 8185 | `eof` | north 380 px to a pad with a contact (8185,16303); `bc1`'s metal of `bc1_g6_in` jogs west 26 px above the pad and is not on it (Ambiguity 30) | `tl5_tracks.py v 8185 16320 16682`; `h_j4.png` (3x, three shots); `textmap.py 8155 16236 8215 16345 3` |
| **C**, poly row y 16294-16312 | `eof` | from the pad east under the track x 8229 and in the open to a gate at x 8283-8311 like the tap row's, ending at x ~8326; west under the tracks x 8143, 8098, 8056, 8012 (no pad, no ring, no hole) to a pad with a contact (7968,16303), the row's west end | `h_row4.png` (1.9x, three shots), `i_e4.png` (4.4x, three shots), `j_ov2.png`; `textmap.py 7990 16285 8215 16321 3`, `7926 16276 8000 16336 3 --acid`; `px.py row 16303 8236 8346 3` in four shots |
| **D**, metal x 7967 | `eof` | from the pad north, straight, 1,390 px (`bc1`'s "track 7969", which its notes list as not traced), an L corner (7967,14914), west to a pad with a contact (7880,14914) | `follow.py 7966 16270 N`; `tl5_tracks.py v 7967 14925 16290` (bars of 8-10 px at y 15854-15885, the edges of a poly row; no hole), `h 14913 7895 7960`; `textmap.py 7940 14894 7994 14942 3` (the corner: one metal), `7850 14885 7912 14942 3 --acid` (the pad) |
| **E**, poly row y 14904-14924 | `eof` | from the pad west: in the open, under `bc1`'s metal (`M 7838,15270 ... x7795 y14913 x7752`, which lies on the row for 43 px with no contact), in the open, under RL3 and two more metals, to x 7550 | `i_top.png` (2.6x, three shots), `j_ov1.png`; `tl5_tracks.py rows row 7540 7910 3 14896 ... 14932`; `px.py row 14914 7722 7748 2` in four shots (poly up to the metal's edge); `tl5_tracks.py h 14913 7745 7800` and `textmap.py 7736 14894 7812 14936 3` (no hole, no ring under `bc1`'s metal); `px.py col 7715 / 7622 / 7775 14892 14936 3` (the row is 18-20 px wide) |
| the row west of x 7550, the metal down the bus field | `busl` (piece `lc9`, line 1), `lc3`, `lc2` | pad and contact (6320,14914), metal x 5844 / 5908 / 6082 north to `lc3`'s x 6082 at y 10400, `lc3`'s line to (6299,9233), `lc2`'s through line to its east edge (6450,8630) | their notes; not re-read |

What the join says (believed, not traced): `rst_a` is made north-west of where it is used, and the three
copies of it that go to the clock block, the row counter's step and the latch on R4's match are made at
the far end of a line that crosses half the die. Its driver is whatever feeds `rst_a` east of
(6450,8630).

The gates it was seen to drive on the way (none drawn: the diffusion under each row belongs to units of
`bc1` (continue) and `bc3`; each row is drawn to its end):

| Row | Where its gate is | What the unit is |
|---|---|---|
| y 16303 (piece `isrc4`, C) | x 8283-8311, under the thin metal x 8283-8307, beside the VSS box of the rail x 8336-8384 (contact about (8350,16285)) | not placed; by its place 606 px above the next, the clear row of a copy of `tl1_ub` at about `@inst tl1_ub 5729,11668` (straddles y 16300, the edge of `bc3`'s findcell run) |
| y 16909 (piece `isrc4`, the tap) | x 8283-8311, the same column 606 px lower; VSS box with contact about (8355,16890) | the clear row (`tl1_ub`'s row of `rcs_x1`, y 4625-4643) of the copy `bc3`'s survey found: `tl1_ua` / `tl1_ub` at 5729,12275 (0.76 / 0.75) |
| y 16172 (piece `isrc`, tap pad (8962,16172)) | about x 8758-8793, beside the VSS box of the rail x 8686-8731 | the clear row of a mirrored copy, `@inst tl1_ub 5973,11539 mx=2686.5` (0.73), with `@inst tl1_ua 5976,11539 mx=2685` (0.72) |
| y 16737 (piece `isrc`, tap pad (8966,16737)) | the row steps south at x ~8905 to y 16770-16790; gate at about x 8760-8800, VSS contact about (8710,16763) | the clear row of the second mirrored copy, `@inst tl1_ub 5973,12146 mx=2686.5` (0.67), `@inst tl1_ua 5976,12146 mx=2685` (0.72) (`h_r1.png`, 3.3x, three shots) |
| y 15258 (piece `isrc`, end pad (8966,15260)) | bright channel at x 8745-8790 beside a VSS box with a contact about (8710,15262) under the rail x 8686-8731 | a pull-down of an unidentified unit of `bc1`'s column B (`h_r3.png`, 3.3x, three shots) |

`findcell` over x 8450-9050, y 15100-17800 (clean shot, min 0.6) also gives `@inst tl5_inv 3603,12459
mx=5082 rot=180 o=5082,4848` (0.77 at (8685,17307)). None of these was overlaid.

### Piece `isrc5`: line X (the first through line of the left-centre strips) is `rst_a`, the reset (traced; wiring only)

```
rst     = NOR(lpstb_b, res_b)      lc1's gate 3: high while the RES and LPSTB pins are both low
rst_n   = NOT rst                  lc1's gate 4
rst_a   = NOT rst_n                lc1's gate 5; the net now carries rst_a as an alias
rst_a_n   = NOT rst_a                bd1's driver of "line X"
rst_ck  = NOT rst_a_n,  rst_rc = NOT rst_a_n,  rst_lat = NOT rst_a_n
```

All from the full extraction (2,395 nets: one fewer than main's). `tools/unsure.py --equations`: `rst_n`,
`rst_a`, `rst_a_n` FIRM (`rst_ck` DEPENDS, as before: one uncertain item in its inverter). `tools/unsure.py`
lists not `rst_a`: no uncertain item on the path. The alias is
an alias (dropped at the rename) in `trace/eof.txt` (piece `isrc4`'s alias for the through line's old name went
when the refresh of 2026-11-19 renamed that line to `rst_a`); the new geometry is labelled `rst_a`. The
rename the rename of line X (the first through line of the left-centre strips) to `rst_a` (done) is the coordinator's refresh.

The path, from `lc2`'s metal end back to the driver:

| Stretch | Drawn by | What | Evidence |
|---|---|---|---|
| the through line | `lc2` (piece P) | `M 6450,8630 6342,8738 ...`: a diagonal that ends at the strip's east edge | its notes |
| **A**, the diagonal on, and its pad | `eof` | the metal runs on at 45 degrees to (6509,8571), then north to a pad with a contact (6513,8538): ring x 6495-6535, y 8523-8556, bright centre in both chips, the clean shot's hole at x 6519-6525. Nothing else on the pad: no metal north of it, field east and west | `j_s1.png` (1.85x, metal, every trace), `j_s2.png` (2.2x, both stripped shots), overlay `j_o4.png` (2.05x, three shots); `tl5_tracks.py h Y 6430 6560 --half 2` at y 8640, 8620, 8600, 8590, 8580, 8570, 8560 (the metal's centre at x 6440, 6459, 6478, 6488, 6498, 6508, 6513; no metal at y 8550, the ring); `textmap.py 6480 8505 6545 8575 3 --acid` |
| **B**, the poly x 6508-6528 | `eof` | from the pad 450 px north to a pad with a contact (6513,8087) (ring y 8063-8100, bright centre at y 8084-8090 in both chips, hole in the clean shot). In the open at y 8103-8157, 8187-8244 and 8469-8520; under metal between: `rst_ck`'s link F (y 8166-8178), the horizontal arm of `eofw`'s `tc2_sr_g` (y 8250-8266) and its vertical arm, which lies on the poly lengthwise from y 8259 to 8411 (Ambiguity 35), and an undrawn metal y 8448-8460. No contact with any: each metal is bright across the poly between the poly's two edge lines, with no ring and no widening | `j_s3.png` (2.3x, metal and chip-2 stripped), `j_o4.png`; `px.py col 6510 7900 8600 12 acid,acid1b,metal`; `textmap.py 6486 8085 6540 8530 3 --acid` (the whole run), `6486 8000 6580 8100 3` (the north pad); `tl5_tracks.py v 6515 8262 8408 --half 2` (the arm: no dark stretch in either chip) |
| **C**, the L and the track | `eof` | from the pad north over a poly row (y 8027-8054: two 9 px bars at its edges, metal bright between) to a corner (6513,8018), east 45 px to a corner (6558,8018), north on x 6552-6565 for 760 px. **The bundle steps here**: each track of the field ends in an L one track to the west (the track x 6513 north of y 7985 goes west at y 7982 to the pad (6470,8125); the track x 6600 goes west at y 8062 to x 6558 and the pad (6558,8127)); between the two Ls at x 6552-6564, y 8024-8054 there is no metal (open ground in both chips). On the 760 px: fourteen bars of 8-10 px, the edges of the rows it crosses (`rst`'s row y 7388, the tap row of `rst_ck` y 7648, `lc1_w7780`'s y 7778, `eofw`'s y 7822 among them), no break, one place where the clean shot is green under it (Ambiguity 33) | `j_s4.png` (1.9x), `j_s5.png` (3.2x, metal and chip-2 stripped: the nested Ls), overlay `j_o3.png` (1.45x, both metal shots and the clean shot); `follow.py 6558 7990 S --gap 16` (corners (6554,8016), (6516,8017), end at the pad's ring) and `N` (corner (6562,7256), end (6184,7258)); `tl5_tracks.py v 6513 8020 8062 --half 2`, `v 6559 7270 8010 --half 2`; `textmap.py 6486 8000 6580 8100 3` |
| **C**, the run west and its pad | `eof` | corner (6558,7258): an L (no metal north of y 7250 at x 6547-6565; the 9 px bar at y 7266-7272 just below the corner is the south edge of the poly row underneath). West along y 7252-7265, 370 px (chip 1's metal shot has a 13 px dark bar at x 6544-6556, chip 2 none: Ambiguity 36), to a pad with a contact (6187,7257): poly pad x 6172-6210, y 7238-7278, ring and bright centre in both chips, a green hole in the clean shot; the metal enters the ring from the east and ends there (no metal west, north or south of the pad). From x 6313 to the corner the metal lies on another net's poly row (Ambiguity 34) | `j_p6190.png` (5x, four shots), `j_c6313.png` (4.2x, four shots); `tl5_tracks.py h 7257 6200 6550 --half 2` (bars at x 6205-6215, the ring; 6261-6272, 6288-6295, vertical polys underneath; 6306-6320, the west edge of the poly underneath; no hole); `textmap.py 6160 7230 6345 7285 3`, `6490 7232 6640 7300 3 --acid` (the corner) |
| **D**, the row y 7248-7266 | `eof` | from the pad west: through `lc1`'s crossing field (x 5640-6130, under a dozen vertical metals, none with a pad or a ring on this row) and in the open to x 5494. It is the second lowest of the nine rows that end on the pads at x 6145-6190 (`lc1`'s Not done) and keeps its lane: at every cut a poly within 5 px of the line, its neighbours 46 px north and 40 px south | overlay `j_o2.png` (1.7x, three shots), `j_s6.png` (1.1x); `tools/eof_rows.py diag 5490 7258 6170 7257 --step 20 --reach 56`, `diag 5936 7257 6000 7257 --step 4 --reach 30` and `px.py row 7257 5936 6000 4 acid,acid1b,metal` (the two cuts with no run are poly in the open: 159/123/56 in the chip-2 metal shot) |
| **D**, the diagonal | `eof` | from (5494,7257) at 45 degrees north-west, 490 px, in the open as far as x 5360 and then under the metals V5, V4 (`rst_b`), V3 (`lpstb_b`) and V2 (`res_b`), which cross it without a pad, to a bend at (5149,6912) and north. The line stays within -5..+9 px of the straight 45-degree line at every cut, with its neighbours 43-47 px either side (the bundle's pitch): it does not change lane under the metals | `j_d1.png` (1.7x, both stripped shots), `j_d2.png` (3.5x, four shots: the bend), overlay `j_o1.png` (2.7x, metal and clean); `eof_rows.py diag 5497 7259 5140 6902 --step 14`; `eof_rows.py row Y 5120 5200` for y 6890-6930 (the poly at x 5148 down to y 6910, x 5155 at 6920, 5161 at 6930); `eof_rows.py col X 6920 7340` for x 5400-5600 (the rows' turning points: x 5560, 5540, 5518, 5497, 5471 for the rows y 7126, 7172, 7216, 7259, 7300) |
| `rst_a`'s poly and pad | `eof` (piece `x1`, run 2; reviewed, rounds 1-3) | `P 5150,6815 y6900`: the poly south of the pad (5147,6803), whose metal is `lc1`'s M_b, the output of gate 5 | piece `x1` |

**The other lanes** (drawn since run 11, pieces `rl` and `w5936`, each read on its own cuts): the bundle's
lines keep their order from the bend to the pads: the row y 7300 (pad (6146,7301)) comes from the poly
x 5063 (`tl3_w3982`), the row y 7214 (pad (6146,7214)) from `res_b`'s poly, the row y 7170 (pad
(6188,7170)) from `lpstb_b`'s, and the row y 7126 is `tla`'s drawn row (`rcs_e4`).

What the join says (traced, firm): the "inhibit" signal of the clock block, the row counter's step and
the strobe channel is the reset. `rst_a` leaves `lc1`'s gate 5 on a poly row east and a metal north (M_b)
to the pad (5147,6803); from the pad one poly goes north into `tl5`'s bus (the clear of four latches of
the top-left logic) and one goes south-east, this piece, to the left-centre through line, down the left
bus field (`lc3`, `busl`), east into the bottom-centre logic (piece `isrc4`: the clear of five latches
there, four of them believed) and along the bottom bus (`trunks`) to `bd1`'s inverter, which makes
`rst_a_n`; `rst_ck`, `rst_rc` and `rst_lat` are `rst_a_n` inverted again. Believed (function, not traced
further): while RES and LPSTB are both low `ck_b` is held low, the row counter's step is suppressed, the
latch on R4's match is open with its output forced low, and in the top-left logic each master/slave
latch pair "on `rst_ck`" has its `rst_ck`-high latch open only during reset and its `rst_ck`-low latch
open the rest of the time: those pairs are loaded at reset, not clocked once per scan line.

### Piece `rl`: `res_b` and `lpstb_b` are `lc2`'s through lines 2 and 3 (traced; wiring only)

```
res_b   = NOT res_n      the RES pin's buffer (trunks); now also carries res_b as an alias
lpstb_b = NOT lpstb_n    the LPSTB pin's buffer;        now also carries lpstb_b as an alias
```

From the full extraction (2,386 nets). `tools/unsure.py` lists neither name: no uncertain item on either
path. The aliases are an alias (dropped at the rename) and an alias (dropped at the rename) in `trace/eof.txt`; the
renames are the coordinator's refresh. No transistor is added: the two through lines have no drawn load
(`lc2`, `lc3` and `busl` pass them on to (6366,15000) and (6408,15000)).

The two paths, each from piece `x1`'s poly end to `lc2`'s metal end (`res_b` / `lpstb_b`):

| Stretch | What | Evidence |
|---|---|---|
| the diagonal | from the bend below the pad ((5203,6900) / (5240,6872)) at 45 degrees south-east under V2, V3 (`lpstb_b`'s own metal), V4 (`rst_b`), V5 and in the open from x 5380, to the turn ((5516,7214) / (5538,7170)). Each stays in its lane: a run within 8 px of the line at every cut, the neighbours 43-51 px either side | `tools/eof_rows.py diag 5196 6894 5518 7216 --step 14 --reach 56`, `diag 5238 6870 5540 7172 --step 14 --reach 30`; col cuts `eof_rows.py col X 7140 7330` for x 5450-5600 (the diagonals at x - y = -1698 and -1632 in the chip-2 stripped shot); row cuts at the bends; overlay `k_o1.png` (2.4x, clean shot: five bands between `lc1_w7040`'s line and `lpstb_b`'s at x 5300, each under its outline) |
| the row | y 7205-7223 / y 7161-7179, from the turn east through the crossing field (x 5640-6130, eight metals) to its pad. No pad on either row in the field, and no ring but one in chip 2 alone at (5665,7212) on `res_b`'s row (Ambiguity 40: a blemish) | `eof_rows.py diag 5522 7215 6140 7213 --step 20 --reach 30`, `diag 5545 7171 6180 7169 --step 20 --reach 30` (the cuts without a run are poly in the open: `px.py row 7213 5853 5869 4 metal,acid1b` and five more: 141-170/96-126/39-60 in the chip-2 metal shot); `tl5_tracks.py h 7214 5525 6128`, `h 7170 5545 6170` (clean-shot dips of 6-10 px, minimum 9-17: the gaps between the metals; `lpstb_b`'s 6127(15,14) is the gap beside the pad (6148,7213)); overlay `k_o2.png` (1.8x, metal and clean) |
| the first pad | (6146,7214) / (6188,7170): a poly pad about 38 px square, ring and bright centre in both metal shots, a green hole in the clean shot; the row arrives from the west, the metal leaves east, nothing else on it | `eof_cchk.py 6148,7213 6190,7169` (hole -36 / -22; centre 192 / 193 in chip 2, 208 / 221 in chip 1); `k_pads3.png` (3.4x, both metal shots and the clean shot) |
| the metal east and the track | y 7216 to the corner (6602,7216), south on x 6602 for 850 px / y 7173 to the corner (6645,7173), south on x 6645 for 935 px. Bars of 8-17 px where the tracks cross the rows of the field (the same heights on both, and on `rst_a`'s track x 6558); no break; no hole but one dull spot (Ambiguity 37) | `tl5_tracks.py h 7215 6170 6595`, `v 6600 7228 8056`, `h 7174 6212 6636`, `v 6645 7186 8098`; `follow.py 6230 7216 E --gap 16`, `6644 7300 S --gap 16`, `6644 7300 N --gap 16`; `eof_mrun.py col 6250 7150 7320 6400 6480`, `row 7350 6490 6670 7600 7950`; `textmap.py 6536 7626 6668 7670 3 --acid` (the three tracks over `rst_ck`'s tap row: alike), `6578 7806 6668 7842 3 --acid`; `k_s1.png` (1.3x, the nest) |
| the L and the second pad | each track ends in an L one track west: (6602,8065) to (6558,8065) and south to the pad (6558,8125) / (6645,8108) to (6601,8108) and south 210 px to the pad (6602,8320). 34 px of bare ground between `rst_a`'s corner (6558,8018) and `res_b`'s arm, 30 px between `res_b`'s corner and `lpstb_b`'s arm. Pads: ring and bright centre in both chips, pitted box in the chip-2 stripped shot | `eof_mrun.py row 8040 6490 6670 8090 8140 8200 8260`, `col 6535 7990 8130 6580 6620`; `tl5_tracks.py h 8068 6566 6594`, `v 6558 8076 8112`, `h 8110 6608 6634`, `v 6601 8124 8300`; `eof_cchk.py 6558,8127 6602,8320` (centre 222 / 209 in chip 2, 174 / 186 in chip 1; clean 12 / 4); `k_s2.png` (2.05x), `k_cols.png` (2.9x, four shots), overlay `k_o3.png` (2.2x, both metal shots) |
| the poly column | x 6549-6567, y 8127-8493 / x 6593-6611, y 8320-8536. `rst_ck`'s link F (piece `tcwa`) lies on `res_b`'s column from y 8166 to 8367 (Ambiguity 5: no contact), and both columns pass under the horizontal metals y 8362-8374 (link F's run east), 8405-8417 and 8448-8460 with no ring and no hole | `tl5_tracks.py v 6558 8140 8480`, `v 6602 8335 8520` (clean shot: no stretch under 24); `k_cols.png` (the columns salmon and whole in the clean shot from pad to pad); overlay `k_o4.png` (1.75x, metal and clean) |
| the third pad and the diagonal | (6556,8493) / (6602,8536): ring and bright centre in both chips, a dull hole in the clean shot. The metal leaves south, bends at (6557,8585) / (6601,8605) and runs at 45 degrees (x + y = 15142 / 15206) onto `lc2`'s metal ends (6450,8692) / (6450,8756). Between the ring of (6556,8493) and the horizontal metal y 8448-8460 north of it: 18 px of open poly in both chips (the follower jumps it in chip 2, trap 30) | `eof_mrun.py row 8510 6430 6640 8530 ... 8750` (every 20 px: the centres move 20 px per cut along both diagonals; `res_b` at (6452,8690), `lpstb_b` at (6457,8750)); `eof_cchk.py 6556,8493 6602,8535`; `textmap.py 6528 8438 6630 8524 3 --acid`; `follow.py 6557 8530 S --gap 16` and `6603 8580 S --gap 16` (they run on down `lc2`'s and `lc3`'s lines; the second to (6408,15150)); `k_s3.png` (3.2x, metal, every trace), overlay `k_o4.png` |

What the join says (traced, firm): the reset NOR of `lc1` is not the only place the two pin lines reach.
Both run on, unchanged, to the bottom-left of the chip. Believed (not traced): their loads there are the
light pen register's strobe logic and whatever else uses RES by itself.

### Piece `w5936`: `tl3_w3982` is latch C's data, and goes on to its driver's box (traced; wiring only)

```
tl3_w3982 (= the wire `tl5` called w5936 = tl3_w3982; now also tl3_w3982)
rcs_cond  = NOR(rcs_cond_n, tl3_w3982)                     tla / tl2 (firm, as before)
lc2_w8822 = NOT((lc2_w8646 & tl3_w3982) | lc2_w8688)       latch C, lc2 (marked, as before)
lc2_w9005 = NOT tl3_w3982                                  latch C's data inverter
```

From the full extraction. `tools/unsure.py` does not list the net. The alias is an alias (dropped at the rename of 2026-11-19) (with `tl3`'s own an alias (dropped at the rename of 2026-11-19) repeated so that the file extracts by itself).

| Stretch | What | Evidence |
|---|---|---|
| the diagonal | from the end of piece `x1`'s poly (5063,6880): the bend at y 6892, then 45 degrees south-east (centre x = y - 1829) under M_a, M_b, V2, V3, V4, V5 and in the open from x 5370 to the turn (5471,7300). In its lane at every cut (neighbours: `lc1_w7040`'s line 43 px south-west, `rst_a`'s 47 px north-east) | `eof_rows.py diag 5063 6892 5471 7300 --step 14 --reach 30` (two cuts under M_a and V2 give no run: the band is there on the overlay); `eof_rows.py row Y 5035 5130` for y 6870-6950; `col X 7140 7330`; overlay `k_o1.png` |
| the row and its pad | y 7291-7309 east through the crossing field to a pad with a contact (6146,7301); no pad on the row in the field | `eof_rows.py diag 5475 7300 6140 7300 --step 20 --reach 30`; `px.py row 7300 5867 5883 4 metal,acid1b` and two more (poly in the open at the cuts without a run); `tl5_tracks.py h 7300 5480 6128` (dips of 6-8 px); `eof_cchk.py 6148,7300` (hole -32; centre 191 / 210); `k_pads3.png`, overlay `k_o2.png` |
| the metal and the track | y 7303 east to a corner (6514,7303), south on x 6508-6520 | `follow.py 6230 7303 E --gap 16` (corner (6516,7303), end (6513,7865): the pad's ring); `tl5_tracks.py v 6514 7310 7990` (bars of 7-15 px, the ring 7867-7883 / 7895-7909); `eof_mrun.py` as above |
| **the pad (6513,7889), in the run of the metal** | ring y 7867-7906 with a bright centre (y 7885-7894) in both metal shots; the metal is whole north of y 7864 and **again south of y 7909**, in line, in both chips; a pitted box in the chip-2 stripped shot; in chip 1's clean shot the pad is vivid red-orange with no green hole (Ambiguity 38). The pad's poly leaves east; field west | `k_L6513.png` (2.75x, four shots), `j_c7886.png` (4.8x, four shots, run 10); `textmap.py 6484 7858 6546 7926 3 --acid`; `eof_cchk.py 6513,7888` |
| the L onto `lc2`'s metal | south of the pad to a corner (6514,7978), west along y 7972-7984 to (6471,7978), south on x 6465-6477 to `lc2`'s `M 6471,8067 y8142` (its pad (6470,8127), `tl3_w3982`). **`lc1_w7040`'s pad (6471,7930) stands 25 px north of the arm on the same x**: no metal at x 6471 from y 7938 to 7970 in either chip, and the pad's poly row (west along y 7944-7962) lies between. Two bars of 8 and 12 px at y 8024-8056 are the edges of the poly row that `rst_a`'s metal crosses beside it | `eof_mrun.py row 7920 6440 6540 7940 ... 8060`, `col 6471 7880 8140 6490 6514`; `k_L6513.png`; overlay `k_o3.png` |
| the row y 7878-7898 | from the pad east, 890 px, under seventeen tracks (x 6558 `rst_a`, 6601 `res_b`, 6644 `lpstb_b`, 6688, 6731, 6776 `rcs_e4`, 6818, 6861, 6905, 6948, 6991, 7078, 7121, 7165, 7208, 7273, 7360; the cut along y 7888 misses x 6905, where the metal is dim over the row in both chips: found by review round 13, `eof_mrun.py row 7860 6530 7440 7915`) to a pad with a contact (7401,7888). No pad or ring on any of them (x 6905: `textmap.py 6884 7866 6926 7910 3 --acid`, no ring, the clean shot salmon with no hole); one place where the clean shot has a hole-like patch (Ambiguity 33, under `rst_a`'s track) | `eof_rows.py diag 6540 7888 7560 7888 --step 30 --reach 30`, `diag 7380 7888 7450 7888 --step 6` (the row ends at x 7416); `tl5_tracks.py h 7888 6535 7380` (clean: 6558(32,-3), and seven dips of 6-8 px); `eof_mrun.py row 7888 6530 7390`; overlays `k_o5a.png`, `k_o5b.png` (2.7x, metal and clean) |
| the pad (7401,7888) and the metal south | ring, bright centre, green hole; the row arrives from the west, field east; the metal leaves south (66 px of bare ground between this pad and `g7700`'s output pad (7402,7822) north of it) and runs 535 px on x 7396-7408 to a pad with a contact (7401,8425) | `k_t4end.png` (2.1x), `k_p7400a.png` (3.5x, four shots); `eof_cchk.py 7400,7888 7400,8425` (hole -8 / -25); `follow.py 7403 7940 S --gap 16` and `N`; `tl5_tracks.py v 7402 7905 8405` (four bars of 8-10 px); `textmap.py 7380 7990 7425 8140 3` (the follower's candidate (7403,8066): field under whole metal) |
| the poly to the box | from the pad (7401,8425) east along y 8417-8439, in the open, 70 px, to a heavy-outlined box (7490-7520, 8410-8442), cream inside in the clean shot: a buried contact. A strip leaves the box's north-east corner east (y 8405-8425 at x 7520-7545) towards the VSS rail x 7552-7598. The poly is drawn to the box's west edge; the box and the strip are not drawn | `k_t5end.png` (2.1x, metal and chip-2 stripped), `k_p7400b.png` (3.6x, four shots) |

What the join says. Traced (firm): the net that `tl3` and `tl5` drew out of the top-left logic's south bus
(`tl3_w3982`: the second pull-down of `rcs_cond`, an input of `tl3`'s NOR `tl3_w3939` and of the pair's
`tl3_w4243`) is the data input of the left-centre latch C (`lc2`'s `tl3_w3982`; the latch is open while
`lc2_w8646` is high and is cleared by the reset copy `rst_c`), and the same net has a third branch east to
the foot of the gate column beside the central datapath. Believed (not traced): the box there is the
output of the unit that drives the net (every other end is a gate), so the step condition of the row
counter is held low, and latch C loaded, from a gate under that column's VSS rail: the next thing to
trace on this path (Not done). **Traced since run 12: piece `d3982`, next.**

### Piece `d3982`: the driver of `tl3_w3982`, three inverters from latch D's lower node (traced)

```
eof_w8168 = NOT lc1_w7928      U2  x 7416-7778, y 8068-8196   load 27/96   DEPENDS (lc2's tie); without it: NOT lc2_w8083
eof_w8298 = NOT eof_w8168      U3  the same 130 px lower      load 27/96   FIRM
tl3_w3982 = NOT eof_w8298      U4  x 7440-7778, y 8330-8448   load 27/56   FIRM
lc1_w7928 = NOT(lc1_w7040 | (lc1_w7780 & tc2_sr_g))          latch D's lower unit (lc2; marked, as before)
lc1_w7040 = NOT((lc1_w7862 & tc2_sr_g) | lc1_w7928 | rst_c)  latch D's upper unit (lc1); lc_step = NOT lc1_w7040
```

From the full extraction and `tools/unsure.py --equations` (run for each of the three). The pull-downs
are 57/22, 57/22 and 57/20. `lc2_w8083` is `lc2`'s label on the poly this piece joins: the node of latch
D's lower unit, which is `lc1_w7928` (the plate's metal north to the upper unit) only through that cell's
uncertain tie (`lc2`'s `@alias lc1_w7928 lc2_w8083`; `tools/unsure.py` lists the net on main already). The
piece's label is `lc2_w8083`.

The column (x 7460-7800) stands between the VSS rail x 7552-7598 (the central datapath's column-0 rail,
piece `g7700`'s) and the wide VCC metal x 7722-7776. South of `g7700` it holds four units at a pitch of 130:
U1 (y 7940-8060), U2, U3, U4. Each has its VSS box and contact under the rail, the gate row directly
below the box, the node below the gate; the node goes west on a strip to a heavy-outlined box at
x 7487-7523 (the output's buried contact) and east to the load. `tools/findcell.py` (clean shot): U4 is
`tl5_inv` turned 180 degrees (0.70), U1 the same (0.71; U1 against U4 0.89 at 0,-390), U2 only 0.46;
U3 against U2 0.93 at 0,130. `tl1`'s latch cells and `g7700`: no hit. U4 is drawn again from its own
measurements (cell `eof_dinv`), not placed as `tl5_inv`: the master's tie is uncertain because a thin
metal crosses it; here every tie box lies in the open.

| Item | What | Evidence (images in `cache/scratch/eof/`) |
|---|---|---|
| under the rail | clean shot, x 7552-7598: VSS boxes (dark outline, pits; a ring in both metal shots) at y 7940-7985, 8068-8110, 8200-8245, 8330-8375; a salmon gate band directly below each (7985-8002, 8112-8132, 8248-8265, 8378-8395); the node below each gate to a dark line (8040, 8182, 8305, 8438); **pink field between each node and the next box** (8045-8068, 8185-8198, 8310-8328), so no node is on the next unit's ground | `m_rail.png` (2.5x, both metal shots and the clean shot); `textmap.py 7534 8030 7612 8078 3`, `7534 8164 7612 8212 3`, `7534 8294 7612 8324 3`; `px.py col 7575 8322 8446 3 acid1b,metal1` (U4: box 8330-8373, gate 8376-8396, node 8398-8426). `railprof.py 7552 7598 7560 8600` gives the gates (7990-8009, 8119-8139, 8249-8262, 8380-8392) but calls y 8010-8118 one diffusion: wrong there |
| U4, the copy | every outline of the cell on its feature in three shots: box, gate row, node strips, output box, strip, plate, tail, tie box, VCC box and contact | `m_u4a.png` (3.3x, `tl5_inv` placed), `m_o3.png` (3.25x, metal and clean, the cell as drawn); `px.py col 7460 8368 8450 3 acid,metal` (gate row y 8376-8396, output row y 8418-8439), `col 7692 8344 8460 3` (plate y 8383-8448, strip y 8405-8432, tie box y 8353-8383), `row 8419 7598 7792 4` (plate x 7666-7722, VCC box x 7726-7778, ring x 7738-7758), `row 8388 7596 7640 3` (the gate ends at x 7613), `col 7768 8362 8450 3` (VCC box y 8373-8432) |
| U4's load strip is diffusion | in the open between the rail and the plate the strip reads orange in the chip-2 shots near its edges (trap 28); at its centre the chip-2 metal shot has blue 87-91 (diffusion and field; open poly 53-70) | `px.py col 7640 8006 8050 3` (U1's strip, the same build), `col 7625 8396 8440 4` |
| U2, the pull-down and the rows | gate row y 8114-8136 from the band to the rail and under it, ending at x 7605; green field y 8140-8152 between it and the output row y 8158-8180, **which reaches the band x 7416-7440 too: the field band between the two rows runs to the band's west edge, so the rows are apart** | `m_u2w.png` (4x, four shots); `px.py col 7480 8104 8182 3 acid,metal` (rows at 8113-8137 and 8157-8180) |
| U2, the output box | heavy-outlined box x 7487-7523, y 8153-8187 at the row's east end, on the node's strip (y 8156-8174, chip-2 blue 86-93) from the rail | `m_u2w.png`; `px.py col 7535 8146 8190 3` |
| **U2, the node east of the rail** | the node leaves from under the rail at y 8154-8174 (`px.py col 7606 8140 8194 3`, review round 14): the clean shot is protected-diffusion colour without a break from under the rail to x 7630 on the rows y 8155-8176 (the green rim stripe at x 7609-7612, which separates the gate's end from the arm, is there only for y up to 8143 and from 8191); a diffusion band (chip-2 metal 171/141/85, clean 160/100/93: not poly, which is 160/117/53) goes north as an arm x 7612-7633 to y 8116, where its top edge runs on east as the top edge of the strip under the plate, and on east to the tie box | `m_u2z.png` (5x, four shots), `m_u2e.png` (3.8x, three shots); `textmap.py 7576 8098 7660 8204 3 --acid`; `px.py pt 7620,8165 7618,8140 7670,8108 7670,8130 7640,8030 7625,8075 ...` |
| U2, the load | plate x 7633-7730 (the last 18 px salmon under the wide metal's margin), y 8100-8170; under it the strip y 8118-8145 (two dark lines through the plate in both chip-2 shots); VCC box x 7733-7778 with a ring (7747,8143) in both metal shots; the plate's tab down into a heavy-outlined box (7645-7680, 8170-8195) on the node: the tie | `m_u2e.png`, `m_u2z.png`; `px.py col 7665 8094 8202 3 acid1b,metal`, `row 8131 7604 7796 4` |
| U3 | U2's cell 130 px lower: every outline on its feature | `m_o1.png` (2.85x, chip-2 stripped and clean), `m_o2.png` (2.95x, metal and clean); `px.py col 7460 8236 8318 3` (rows y 8244-8267 and 8288-8310) |
| the chain | U2's output row, the band and U3's gate row are one poly (a C round a field island x 7443-7550, y 8182-8240); the same from U3's box to U4's gate row | `m_w1.png` (2.55x, three shots), `m_u2w.png`, `m_o1.png`, `m_o3.png` |
| **U2's input: not U1's output** | the band x 7416-7440 above U2's gate row ends at y 8030 by turning west; U1's output box (7480-7520, 8022-8055) stands 40 px east of it with field between (x 7442-7478) in all four shots, and no poly leaves that box | `m_u1w.png` (3.5x, four shots); `px.py row 8090 7406 7450 3` (band x 7416-7440) |
| the row y 8030-8050 | from the band west, under twenty-one tracks, to a corner at x 6401-6416. One poly at every cut; no pad, no widening, no ring on it in either metal shot. At x 6520-6590 it lies in the open, in the 30 px gap between the horizontal arms of two Ls (`rst_a`'s y 8012-8024, `res_b`'s y 8059-8071), not under them. Clean-shot stretches under 24 lie only in the open gaps between tracks (x 6574, 6619, 6751, 6794, 6837, 6879: trap 2) | `eof_rows.py diag 7436 8037 6480 8037 --step 40 --reach 30`; `m_in1.png` (2.8x, metal and chip-2 stripped, x 6990-7445), `m_row2.png` (2.2x, metal and clean, x 6425-7000); `eof_mrun.py row 8040 6410 7420 8012 8062` (the tracks); `tl5_tracks.py h 8040 6420 7414` |
| the crossings that matter | under `tl3_w3982`'s own thin metal x 7396-7408: two bars of 6-9 px (the row's edges), whole bright metal between, salmon with no hole in the clean shot; under the track x 7078 a dim spot in chip 2 only (chip 1 bright, no hole); under `rst_ck`'s metal x 6431 and the tracks x 6471 (`tl3_w3982`), 6514 (`rst_a`): bars and bright metal, no ring (Ambiguity 41) | `textmap.py 7380 8014 7428 8066 3`, `7052 8014 7100 8062 3`; `m_w8038.png` (4x, metal and chip-2 stripped), `m_o4.png` (5x, three shots) |
| the corner onto `lc2`'s poly | the row turns south at x 6401-6416 (chip-2 stripped orange at x 6406-6409, dark edges 6400 and 6415-6418) and is orange without a break from y 8032 to 8088, through `lc2`'s `P 6401,8067:6415,8092` | `px.py row 8060 6388 6430 3 acid,acid1b`, `col 6408 8020 8090 4`; `m_w8038.png`, `m_o4.png` |

What it says. Traced: the net `tl3_w3982` (the second pull-down of `rcs_cond`, an input of `tl3_w3939`
and of the pair's `tl3_w4243`, latch C's data) is driven by one inverter, and that inverter's input is
latch D's lower node through two more inverters, with nothing else on the two nets between. So
`tl3_w3982` = NOT `lc1_w7928` after three gate delays, and while latch D holds, `lc1_w7928` = NOT
`lc1_w7040` = `lc_step`: **`tl3_w3982` is the inverse of the scan line counter's step pulse `lc_step`,
late by three gates** (marked: latch D's two ties). With `rcs_cond` = NOR(`rcs_cond_n`, `tl3_w3982`): the
row counter's step condition can be high only while `lc1_w7928` is high. Believed: the two long loads
(27/96 against the column's 27/56 and 26/55) make U2 and U3 slow on purpose, a delay; nothing traced says
what the delay is for. `rst_ck` is `rst_ck` (traced; wiring only)

```
rst_a_n  = NOT rst_a                    the driver of "line X" (bd1, trunks)
rst_ck = NOT rst_a_n                      the lone inverter of the input buffer row (inrow)
rst_ck                                   one net: this piece, lc2's piece, trunks' line S
ck_b   = NOR(ck_clkn, ck_g4, rst_ck)    the clock block (firm)
```

The full extraction has one net carrying `rst_ck` (the clock block's and `inrow`'s label),
`rst_ck`, with thirteen gates on it: the clock block's (`ck_b`'s NOR), the
inverter's own load, and the eleven that were known as `rst_ck`'s (`tl1`'s two latches and the
NOR `tl1_w3636`, `rcs_a2`'s NOR, `tl3`'s latches B and C and the NOR `tl3_e4243`, `tl4`'s NOR
`tl4_w4545`, `tcw`'s pair `fld_a_in` / `tcw_o3820`). `tools/unsure.py`: the labelled pieces of
`rst_ck` (then under three names) in `clock`, `inrow`, `eof`, `fld`, `lc2`, `tl3`'s foot and
`tl4` stay one piece when every uncertain item is deleted (the second piece it lists is
`tl1_w3594`'s, across `tl3`'s `?M` thin metal: AMB-033, as before). `rst_ck` is kept as the name
the net is shown under (an alias in `trace/eof.txt`; the rename is proposed in the handoff).

Believed, not traced: what this says about the signal. The net that stops the horizontal
counter's master clock is the net on whose two levels the vertical control's master/slave latch
pairs work (`tl1`'s pair, `tl3`'s latches B and C) and that opens the field latch path of `tcw`.
That is the pattern of a strobe that marks one moment of every scan line (the vertical logic
steps once per line), not of a rarely used inhibit. What `rst_a` is remains open: its line is
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
| x 6431, y 8067-8172, corner, to x 6450 | `lc2` | its `rst_ck`: the metal lies on latch C's data poly for 64 px without a contact (its Ambiguity 3) and turns east | `textmap.py 6398 8090 6500 8200 3`: one 6 px bar at the poly's top edge, no ring, no hole; an L |
| **link F** | `eof` | east along y 8172 to a corner (6559,8172); south on the poly that leaves the pad (6558,8127) of another net (the pad's own metal arrives from the north; 18 px of open poly between its ring and this corner); corner (6559,8367); east over five poly columns to x 6690 | `textmap.py 6515 8060 6602 8200 3 --acid`, `6521 8322 6608 8400 3`; `tl5_tracks.py h 8172 6450 6545`, `v 6559 8190 8355`, `h 8367 6575 6760`: bars only, no hole; `k4_stair_m.png`, `k5_nestW.png`; overlay `ov_f.png` |
| the staircase to the contact (7034,8535) | `trunks` | corners (6757,8366), (6757,8452), (6930,8452), (6930,8536); the contact | `follow.py 6330 7432 E` gives every corner from (6430,7432) to the end (7038,8536) as drawn; `tl5_tracks.py` on each piece: bars only; `textmap.py 6950 8506 7070 8566 3 --acid`: ring, bright centre, hole |
| line S to the inverter | `trunks`, `clock`, `inrow` | poly (7034,8535)-(7034,8797), the metal down the left bus field (x 6862, step at y 13331, x 6798), poly under the supply buses, metal, poly under nine bus lines, the bottom bus line y 18428 (three poly hops), the turn at x 10268, the link to L4 and L6, L4 east, poly, metal to the inverter's output (13849,18590) | read by its package at 1x (re-read item R4). Here, by text only: `eof_cchk.py` on its nineteen contacts: seventeen have a hole in the clean shot (red minus green under 25), the other two, (7034,8797) and (8382,18428), a dull hole beside the centre on a text map; the centre is bright (over 150) in both metal shots at fifteen and in one shot at four ((9777,18425): chip 2 91; (6798,17990), (8602,18428), (12849,18384): chip 1 124-132), which were not looked at further; `follow.py 7032 8826 S` gives the diagonal, the step at y 13332 and the end (6797,16176) as drawn. The follower's contact candidates and the clean shot's dips on the two long metals are crossings without a pad (trap 15: `textmap.py 6826 9680 6900 9740 3 --acid`, `6762 14500 6836 14596 3`), and three long green stretches (y 16530-16690, 16822, 17483) are damage on chip 1 only (chip 2's metal is whole: `textmap.py 6768 16500 6834 16700 5 --acid`). **Taps of line S in poly under neighbouring lines were not looked for (R4 stays open).** |

**The gate group at the tap row's end** (run 2's look; **traced in run 5: piece `g7700`, which corrects this paragraph**: rows 1 and 2 do not meet). `k7_group.png` (1.95x, metal and clean),
`k3_rowend.png` (2.7x, four shots): a wide vertical metal x 7550-7600 over a diffusion column
(x 7545-7610, y 7610-7810) crossed by three poly rows, y 7640-7656 (this row, `rst_ck`), y 7705-7725
and y 7765-7785 (both from the west), with a metal contact (7575,7680) on the diffusion between
the first two; east of the metal an outline x 7610-7660, y 7610-7740 in which rows 1 and 2 appear
to meet (a U: if so both gates are `rst_ck`, two fingers round the contact), a strip east at
y ~7800 and what looks like a load with a contact (7745,7780) under a second wide metal
x 7722-7770. So `rst_ck` is a gate there. Nothing of it is drawn.

### Piece `g7700`: the gate on `rst_ck`'s tap row (traced)

```
tc2_r5589 = NOT( eof_w7777 AND (rst_ck OR tc2_sr_g) )        firm (tools/unsure.py --equations tc2_r5589)
```

Four transistors (full extraction): the load 26/55 (gate and source on `tc2_r5589`, drain VCC),
row 3's pull-down 70/19 between the output and the inner node, and two pull-downs 70/18 and 70/20
(gates `rst_ck`, `tc2_sr_g`) from the inner node to VSS, side by side with one source contact
between them. Traced: the equation, and that `rst_ck` is one of its inputs (the tap row of piece
`tcwa` is the gate's row 1: one poly from the pad (6427,7648)). Believed, not traced: nothing about
what the gate is for. With `rst_ck` high the output is NOT `eof_w7777`; with it low,
NAND(`eof_w7777`, `tc2_sr_g`).

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
| `tc2_r5589` (output) | pad (7402,7822); a thin metal x 7395-7407 north over rows 3, 2 and 1 (bars only) to a pad with a contact (7401,7606), no metal beyond; that pad's poly west along y 7596-7612 under the metals x 7309-7322 (row 2's) and x 7345-7362 without a contact, to a pad with a contact (7273,7606); a thin metal x 7266-7278 north for 690 px (over four rows of the crossing field at y 7420-7570, then over bare field from about y 7410) to a pad with a contact (7272,6912); **the pad's poly goes on north** towards a row y ~6862 (drawn to y 6875; `bw`'s crossing field, not followed) | `follow.py 7400 7818 N` (end 7403,7602), `7270 7560 N --gap 16` (end 7272,6910); `textmap.py 7372 7570 7436 7640 3`, `7228 7576 7300 7630 3`, `7243 7480 7300 7582 3`, `7237 6868 7309 6934 3`; `tl5_tracks.py v 7272 6930 7590` (bars of 8-13 px, no hole); `px.py row 7604 7285 7400 5`; `t18.png`, `t20.png` |
| `tc2_sr_g` (row 2) | west under the output's metal x 7401 and the metal x 7345-7362 (no ring) to a pad with a contact (7267,7736). **Two metals on the pad** (Ambiguity 14): one east along the row and north (corner (7315,7736)) to a pad with a contact (7313,7215), whose poly row leaves east along y 7203-7221 (drawn to x 7400); one south from the pad (x 7262-7274), which `follow.py` takes 2,160 px to (6514,8254) (not checked, drawn to y 7800) | `t14.png` (3.1x, four shots), `t19.png`; `textmap.py 7222 7696 7336 7800 3`, `7285 7180 7345 7240 3`; `follow.py 7290 7735 E --gap 16`, `7270 7780 N --gap 16`, `7270 7780 S --gap 16` |
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
  followed) and **line X (the first through line of the left-centre strips), which is `rst_a`: the clear of `tl5`'s latches a
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
| the bus to y 6350 | `tl5` (the pins' lines: `trunks`) | ten vertical polys; by x at y 6350: 5063 `tl3_w3982`, 5107 `rcs_x1`, 5150 `rst_a`, 5192 `res_b`, 5237 `lpstb_b` | their notes; not re-read |
| **five columns, y 6350-6740** | `eof` | straight, under nine horizontal metals (`slbus`'s and others), no pad; no line steps a track | `x1_survey.png` (1.17x, metal and clean, all traces); `tl5_tracks.py rows row 5040 5262 3` at thirty heights (every 14 px, y 6340-6744): the columns stand at x 5061-5067, 5103-5115, 5148-5154, 5190-5199, 5235-5241 at every height; `tl5_tracks.py v X 6350 6900` per column: only 6-7 px dips at the gaps between metals (trap 2), the same heights on several columns |
| **four pads** | `eof` | (5105,6761), (5147,6803), (5190,6845), (5237,6803): each a ring with a bright centre in both metal shots and a green hole 16-17 px across in the clean shot | `x2_pads.png` (2.1x, metal and clean); `eof_cchk.py`; `textmap.py 5050 6728 5260 6906 3` |
| **four metals to y 6905** | `eof` | from pad 1 the metal's head stands 6-9 px (the ring) west of the centre and runs south at x 5077-5089 (M_a, shifting 6 px west at y 6890); from pad 2 the same, south at x 5116-5128 (M_b); V2 (x 5185-5194) and V3 (x 5230-5242) hang straight from pads 3 and 4 | the same text map: nothing above either head, bright in both chips to y 6905; the image |
| **the polys below pads 2, 3, 4** | `eof` | pad (5147,6803): open poly x 5141-5160 south to y 6900, bending south-east at about (5150,6910); pad (5190,6845): poly under V2, x 5188-5203 to y 6884, x 5197-5209 at y 6900; pad (5237,6803): poly under V3, x 5232-5250 to y 6872, then bending east (x 5247-5266 at y 6884, about (5266,6900)) | the reviewer's `review-2/k_pads234.png` (4.4x, four shots), `j_bundle.png`; `textmap.py 5128 6812 5275 6918 3 --acid`; `px.py col 5146 6776 6916 10 acid` against `col 5104` (field below pad 1); overlay `ov_x1fix.png` (4x, both stripped shots) |
| the gate column | `lc1` | M_a = gate 2's output; M_b = gate 5's output; V2, V3 = the NOR's inputs | its notes ("followed to y 6840 / 6800 / 6844 / 6800": the pads' heights) |

The fifth line, the wire `tl5` called w5936 (= `tl3_w3982`, the net that holds `rcs_cond` low), has no pad: its
poly runs on south in the open at x 5056-5072, beside M_a, and from y ~6890 shifts east under
it (`textmap.py 5050 6728 5260 6906 3`, the clean shot's column x 5059-5083). Drawn to y 6880.
`lc1` does not draw a poly there.

### Piece `r4lat`: the lower half of the latch on R4's match gets its load (traced; the tie uncertain)

```
bd1_n1 = NOT( bd1_n2  OR  rst_lat AND rc_eq_r4 )        upper half (bd1's)         depends (bd1's tie of N1's load)
bd1_n2 = NOT( bd1_an AND rst_lat  OR  bd1_n1 )          lower half; load: r4lat    depends (the tie drawn here; bd1's ?D, ?P)
bd1_an = NOT rc_eq_r4                                   bd1's inverter A           FIRM
```

(`tools/unsure.py --equations NAME`, full extraction. `bd1_q`, the gate of `bd1`'s pull-down G4, is an alias of
`bd1_n2` since this piece; `tools/unsure.py` lists `bd1_n2` as two pieces joined only through the tie.)

**Traced.** The load of the lower half: one transistor, 30/55, gate `bd1_n2` (the band), between the VCC land
and N2. With it the lower half is a complete gate, and with the tie the pair is cross-coupled: while
`rst_lat` is high `bd1_n1` = NOT `rc_eq_r4` and `bd1_n2` = `rc_eq_r4`; while it is low each holds the other.
So the pair is **a transparent latch of R4's match, open while `rst_lat` is high** (`rst_lat` is a copy of
`rst_a`), as `bd1`'s notes believed from the layout.

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
under `rst_a`'s gate is not a pass transistor from the latch's node N1; whether its top segment reaches
the ground diffusion under the rail (`bd1`'s `?D`) was not settled (`e_k1.png`, `e_k2.png`).
(Settled in run 8, piece `n2out`: it does, and the lower segment is N2.)

### Piece `n2out`: the latch's output is `bd1_k`, and `rst_a` gates it (traced)

```
bd1_n2 = NOT( bd1_an AND rst_lat  OR  bd1_n1  OR  rst_a )      depends (the load's tie, piece r4lat)
bd1_n1 = NOT( bd1_n2  OR  rst_lat AND rc_eq_r4 )                 depends (bd1's tie of N1's load)
```

(`tools/unsure.py --equations bd1_n2`, full extraction. `bd1_k` is an alias of `bd1_n2` since this piece;
`tools/unsure.py` shows the labels `bd1_k`, the wire of piece `n2w` and N2's diffusion in one piece without
any uncertain item: the join does not rest on one.)

**Traced.** `bd1` drew a diffusion strip under `bd1_an`'s thin metal (x 13773-13804, y 15634-15730): a top
segment, the channel under `rst_a`'s gate (y 15661-15681), and a lower segment with a buried contact
(13768-13792, 15699-15733) to the poly that leaves west as `bd1_k`. It read it as a pull-down of a node
`bd1_k` whose load was "not in view", and drew N2 (under the ground rail, from x 13817) 13 px clear of it.
The two are one diffusion. Between `bd1_an`'s metal (east edge x 13793) and the rail (west edge x 13822)
the ground is open, 29 px wide, and both metal shots show it directly:

| Rows | What lies in the gap | Evidence |
|---|---|---|
| y 15638-15652 | **diffusion: the strip's top segment runs on east to the ground diffusion under the rail** (`bd1`'s `?D`) | the same four tests as the next row: `px.py row 15644 13786 13834 3 metal,metal1` (dark ends at x 13798, plain 13801-13816, the rail's edge line 13819-13822); `px.py row 15642 13786 13826 2 acid1b` (dark bar 87/69/68 .. 81/56/42, no green; tan 205/177/135 under the rail's margin, where field is pink 182/124/124); red minus green +20, +21 at x 13814. Its edges: y 15635 (top), 15653 (bottom) (`px.py col 13806 15620 15750 3 metal,metal1`) |
| y 15657-15703 | field: an island between the strip and the rail's diffusion | in both metal shots the dark at the metal's edge is 12-14 px wide (x 13795-13806: the metal's edge line and the strip's east edge line side by side); the clean shot has the green strip of a gap over field (x 13804-13820: 39/46/30 .. 131/140/84); in the chip-2 metal shot red minus green is -19 to -4 at x 13814 |
| y 15712-15736 | **diffusion: N2 runs on west from under the rail to the strip's lower segment** | (1) no edge: the dark at the metal's edge ends at x 13797 and the ground is plain from x 13799 to the rail's edge line at 13819, in both metal shots, exactly as on the row y 15519, where the column's diffusion is known to cross the gap between gates P2 and P3 (`px.py row Y 13786 13828 3 metal,metal1,acid` for Y = 15519, 15694, 15722, 15730); (2) the clean shot has no green strip there but the dark reddish bar of a gap over diffusion (x 13806-13814: 119-140/76-89/67-77), as on the known crossings y 15519 and y 15580 (N1) (`px.py row Y 13786 13826 2 acid1b`); (3) red minus green in the chip-2 metal shot at x 13814 is +17 to +23, as on N1's crossing (+4 to +20), against the island's -19 to -4 (`px.py col 13814 15500 15752 4 acid,metal`); (4) the plain area's top edge (y 15708) and bottom edge (y 15738-15742, slanting) are the lines of N2's top edge and of gate G5's upper edge under the rail, run on west (`px.py col 13806` and `col 13812 15620 15750 3 metal,metal1`; `f_j2.png`, 7x sharpened, both metal shots; `f_gap.png`, 4x, the whole column) |

So the unit is a third pull-down of N2 folded round a field island: ground diffusion, west through the gap,
the top segment, the channel under `rst_a`, the lower segment, east through the gap, N2; and N2's buried
contact under `bd1_an`'s metal puts the latch's true output on the poly that `bd1` called `bd1_k`.
`bd1_an`'s metal is dark at y 15720-15732 in both chips with the clean shot greenish beneath: the box under a
thin metal (traps 22, 26, 27), no pad and no ring, as `bd1` read it.

**What it does** (from the equations; marked like them). While `rst_a` is high the latch is open
(`rst_lat` is `rst_a` twice inverted) and N2 is held low, so `bd1_n1` = NOT `rc_eq_r4`; when `rst_a`
falls, `bd1_n2` rises if the match was there, and holds after `rst_lat` has fallen. **`bd1_n2` (`bd1_k`) =
R4's match as it was at the end of `rst_a`'s high phase, shown only while `rst_a` is low.**
Believed: this is why the lower half needs no clean hand-over; the term (`bd1_an` AND `rst_lat`) is then
redundant except during `rst_lat`'s two gate delays.

The chip-2 stripped shot is of no use in the gap (a red fringe column x 13800-13808 down its whole height:
`textmap.py 13740 15618 13884 15776 3 --acid`), and colour in the metal shots does not tell diffusion from
field at x 13801-13810 (150-180/130-145/80-90 on every row); the edge lines and the column x 13814 do.

### Piece `n2w`: the latch's output on from `bd1`'s end (traced; wiring only)

`bd1` followed `bd1_k` from the box west and south (contact (13674,15715), metal x 13674, contact
(13674,15975), a poly west, contact (13522,15999), metal south on x 13521 "to about y 16273"). From there,
all on one net, with no uncertain item (`tools/unsure.py`):

| Link | Path | Evidence |
|---|---|---|
| A | the metal turns east at y 16264 and south on x 13564 to a pad with a contact (13562,16604) | `follow.py 13521 16100 S` (corners (13526,16266), (13564,16262), end (13564,16608)); `f_k1.png` (1.8x), `f_k2.png` (3.8x); ring and bright centre in both chips (`textmap.py 13533 16576 13594 16631 3`) |
| B | a poly row y 16596-16612 west under the tracks x 13521, 13478, 13435 to a pad with a contact (13348,16604) | `px.py col 13450` and `col 13400 16585 16625 3 acid1b` (cream under metal, dark red-brown in the open: one band, centre y 16604); overlay `g_ov2.png` (4.4x, metal and clean); nothing leaves either pad on its far side |
| C | metal south on x 13347, a diagonal from (13347,16712) to (13220,16839), south on x 13218 to a pad with a contact (13217,17776) | the follower loses the diagonal where it crosses `wr_r7`'s poly diagonal ((13292,16780) from the north, (13258,16800) from the south); `follow.py ... --max` in 20 px stages from both ends gives (13334,16730), (13311,16750), (13294,16770) and (13258,16800), (13244,16820), (13222,16840): one 45-degree line; `textmap.py 13230 16740 13330 16850 4`: the bright band unbroken in both chips; `f_k4.png` (2.4x); candidates (13218,17634), (13218,17674) are the edges of `h_eq_r1`'s and `rst_lat`'s poly rows under it (two dark bars, no ring, no pad: trap 15) |
| D | a poly row y 17768-17784 west to a pad with a contact (12848,17777), under the trunks and under the wide VCC rail x 12890-12985 | overlay `g_ov3.png` (3x, metal and clean): one band; `px.py col 13100` (open: dark red-brown) and `col 12870 17755 17795 3 acid1b` (cream) |
| E | metal west along y 17779 to x 11722, north to y 17606, west to a pad with a contact (11287,17603): the outer of three nested Z bends (`rst_a`'s, drawn by `trunks`, is the middle one) | `follow.py 12700 17778 W` ends at (11718,17782) and `follow.py 11500 17603 E` at (11730,17612): the vertical piece is crossed by four poly diagonals and the follower finds no 35 px of metal on it; `textmap.py 11690 17590 11760 17795 3`: metal (C-F) at x 11714-11729 from y 17611 to 17785 in both chips, with four dark bars of 6-9 px (edges underneath); overlay `g_ov4.png` (2.4x). Candidates (12253,17780) and (11806,17781): plain metal, and a diagonal edge underneath |
| F | poly west from the pad to x 11137, a diagonal to (10835,17905), west along y 17897-17913 to x 10224, south to a pad with a contact (10222,17993) | `px.py col X ... 4 acid1b,acid` at X = 11200 (y 17602), 11100 (17640), 11000 (17740), 10900 (17842), 10860 (17880), 10830 (17904), 10600 and 10240 (17906): one line at 45 degrees and then flat; overlays `g_ov5.png` (2.4x, the diagonal beside `rst_a`'s), `g_ov6.png` (4.2x, the turn and the pad). **Its last 96 px (x 10224-10320) lie under `ck_out`'s metal** (`trunks`' `M 10320,17908 x10230`): no contact (`textmap.py 10190 17884 10340 17926 3`: the metal C-F with no ring, the clean shot poly-coloured with no hole; Ambiguity 27) |
| G, H | metal south 46 px and west along y 18039 to a pad with a contact (9813,18037); poly under the metals x 9650 and 9710 to a pad with a contact (9594,18038) | `follow.py 10222 18020 S`; `f_k14.png` (3x), overlay `g_ov7.png` (4.4x); candidate (10114,18040): plain metal in chip 2, a speck in chip 1 |
| I, J | metal west along y 18039 to a pad with a contact (8643,18038); poly under the metals x 8460 and 8510-8560 to a pad with a contact (8424,18039) | `follow.py 9500 18038 W`; it passes over `isrc`'s poly x 8964 (that piece's review: no hole); `f_k15.png`, overlay `g_ov8.png` (4.4x) |
| K, L | metal west, a step south at x 8182 from y 18039 to y 18083, west to a pad with a contact (7600,18082); poly under `bc1`'s rail RL2 to a pad with a contact (7422,18081) | `follow.py 8300 18037 W` (corners (8182,18051), (8178,18083)); `f_k16.png`, `f_k17.png`, overlay `g_ov9.png` (5x): one of four like cross-unders of the rail (rows y 18037, 18082, 18125, 18168) |
| M | metal west along y 18083 to a corner (6712,18083) and north on x 6712 to a pad with a contact (6708,16519) | `follow.py 7300 18083 W` (2,174 px; corner (6712,18075)); `f_k20.png` (2.6x: the corner, nested inside the next line's, which turns at (6755,18040)); candidates (6711,17641), (6712,17291), (6713,16792): plain metal in chip 2 (chip 1 is dim for 15 px at the last two: dirt, no ring) |
| N | poly x 6703-6721 north under the supply buses to a pad with a contact (6710,16173) | `px.py row 16300` and `row 16220 6688 6730 3 acid1b,metal` (cream under the bus, orange in the open: centre x 6713); overlay `g_ov10.png` (3.2x, three shots): one band; the pads of the neighbouring tracks x 6665 and 6752 are staggered 40 px lower |
| O | metal on north on x 6711, drawn to y 15000 | `follow.py 6711 16100 N --max 1150`; candidate (6712,15176): a poly row crossing (two dark bars with metal between, no ring) |

All fourteen pads: a dark ring about 40 px across with a bright centre in both metal shots
(`textmap.py`, 3 px, a 60 x 54 px window on each). No metal runs on beyond any pad and no second poly
leaves one (the views named above; trap 32).

**Where it goes** (not traced). `follow.py 6711 16100 N` takes the metal on: north on x 6711 to y 13242, a
step east to x 6781, north (candidates at y 12168, 9798, 9623, 9364: not looked at) and by a diagonal to
an end at (6948,8707), 7,476 px in all. That is the south end of the gate groups west of `cdp3`'s large
cells (`cdp3` (continue): "gates below it at y 8620-8800"; `eofw`'s corner pad (7446,8732) is 500 px east).
None of it is read: from y 15000 to 10400 it lies in `busl`'s claimed region.

### Piece `ck5`: the ripple counter's clock is `lc3_w9947` (traced; wiring only)

```
lc3_w9947 (= the wire `lc2` called x6432, the clock of stage B0; now one name, lc3_w9947)
eof_w9255  = NOT((lc3_w10201 & lc3_w10210) | (lc3_w10210 & lc3_w9947))     stage B0's slave output (lc3; firm)
lc3_w10123 = NOT((eof_w9255 & lc3_w9947) | lc2_w8450 | lc3_w10201)         stage B0's master
tcw_o3240  = NOT((lc3_w9947 & tcw_m6320 & tcw_o3550) | (tcw_m6320 & tcw_m6362a & tcw_o3550))   tcw (marked, as before)
```

From the full extraction (2,382 nets). In `tcw`'s column the net is the gate of four transistors
(at (6525,2750), (6524,2920), (6511,3140), (6530,3417)). `tools/unsure.py` lists none
of the four names: no uncertain item on the path.

**Names.** One net now carries four names. `lc3` had an alias (dropped at the rename of 2026-11-19) and `tl6` had `@alias
two names on one net`; the extractor wants one canonical name with every other name aliased to it
directly, and a later file's alias line replaces an earlier one's, so no line in `trace/eof.txt` alone
can make the full extraction clean. The canonical name is `lc3_w9947`: `trace/eof.txt` has an alias (dropped at the rename of 2026-11-19) (and repeats the other two), and **`trace/tl6.txt`'s line was changed to an alias (dropped at the rename of 2026-11-19)** as a commit of its own (no geometry; `tl6` by itself extracts as before: 966
nets, 2 errors, 56 warnings before and after). The renames are the coordinator's refresh.

The path, from `tc2`'s poly to `lc2`'s metal end:

| Stretch | What | Evidence |
|---|---|---|
| `tc2`'s poly | `P 6451,6160 y6400 w=17` from `tc2`'s pad (6447,6150), `lc3_w9947`; `tl6`: its metal is `lc3_w9947`'s | `notes/blocks/tc2.md` (piece 5), `notes/blocks/tl6.md` |
| the poly x 6443-6460 | on south from y 6400, 725 px, to a pad. It is the middle one of three vertical polys (x 6408, `tc2_m6404`'s, runs on south past the pad; x 6492, `tc1_p4308`'s, ends on a pad (6490,6755)) and keeps its lane: a run within 6 px of x 6452 at 41 of 49 cuts in the clean shot, the others in the open gaps between metals, where the chip-2 stripped shot has it. Fourteen horizontal metals cross it (y 6408-6422, 6453-6465, 6498-6507, 6539-6551, 6584-6596, 6625-6639, 6668-6682, 6799-6811, 6842-6855, 6908-6920, 6952-6964, 6994-7006, 7037-7049, 7080-7093: the last four are the three rows' metals and `rcs_e4`'s), none with a pad, a ring or a hole (Ambiguity 46) | `eof_rows.py diag 6452 7105 6452 6385 --step 15 --reach 28`; `tl5_tracks.py v 6452 6400 7105 --half 2` (clean-shot dips only in the open gaps between the metals: y 6519, 6822, 6974, 7017, 7060); `n_p1.png` (2.5x, metal and chip-2 stripped), overlay `n_o3.png` (1.6x, both stripped shots) |
| the pad (6450,7127) | a poly pad x 6432-6470, y 7107-7147: ring and bright centre in both metal shots, a pitted box in the chip-2 stripped shot, a green hole in the clean shot. The poly arrives from the north, the metal leaves east; field south and west (the poly x 6408 passes 15 px west of the pad) | `eof_cchk.py 6450,7125` (hole -28; centre 216 / 223; the east ring not dark); `n_pA.png` (5.6x, four shots) |
| the metal and the track | east along y 7122-7134 to a corner (6688,7128), south on x 6682-6694 for 1,030 px. Twelve pairs of 8-12 px bars, the edges of the poly rows it crosses (y 7158-7182, 7202-7226, 7246-7269, 7288-7313, 7375-7399, 7418-7443, 7505-7529, 7637-7660, 7768-7791, 7811-7835, 7879-7900, 8028-8052); no break, no hole. No poly under the metal y 7128 (the clean shot has none along it) | `follow.py 6690 7600 N --gap 16` (corner (6683,7130), end (6445,7128)) and `S` (corners (6686,8156), (6644,8153), end (6644,8253)); `tl5_tracks.py v 6687 7140 8150 --half 2`, `h 7128 6465 6680`; `eof_rows.py row 7128 6470 6700`; `n_s3.png` (1.7x), overlay `n_o2a.png` (3.6x, both metal shots) |
| the L and the second pad | corner (6688,8151), west to (6644,8151), south to a pad with a contact (6645,8276): pad x 6626-6664, y 8257-8296. 30 px of bare ground between this arm and line Q's (the track x 6730's L at y 8190) | `eof_mrun.py col 6666 8120 8190 6660 6672` (the arm's centre y 8151 in both chips); `eof_cchk.py 6645,8275` (hole 8; centre 235 / 170); overlay `n_o2b.png` (3.6x, both metal shots and the clean shot); `n_pB.png` (3.1x, four shots) |
| the poly column | x 6636-6654, y 8276-8580, salmon and whole in the clean shot from pad to pad, under the horizontal metals y 8362-8374, 8403-8416 and 8449-8460 with no ring and no hole. A metal of another net (x 6663-6678, y 8455-8545) runs beside it 9 px east | `tl5_tracks.py v 6645 8290 8565 --half 2` (no clean-shot dip); `n_pB.png` |
| the third pad, the diagonal and the run south | pad (6645,8580), x 6626-6665, y 8560-8600. The metal leaves south, bends at (6645,8628), runs at 45 degrees (x + y = 15272: 6632 at y 8640, 6593 at 8680, 6552 at 8720, 6511 at 8760, 6473 at 8800) between `lpstb_b`'s diagonal (x + y = 15206) and line Q's (15337), and south on x 6466-6478 from y 8800. From y 8945 it lies on `rst_c`'s poly (Ambiguities 43, 44) | `eof_cchk.py 6645,8580` (hole 0; centre 228 / 165); `eof_mrun.py row 8600 6430 6760 8620 ... 9180`; `tl5_tracks.py v 6472 8805 9175 --half 2` (one bar, y 8923-8936, where the poly's diagonal passes under); overlay `n_o1.png` (1.9x, metal) |
| the corner onto `lc2`'s metal | at y 9161-9174 the metal turns west: an arm x 6422-6458 onto `lc2`'s `M 6450,9165 x6432 y9233`. The vertical ends there; it is **not** on the pad (6469,9209) 35 px further south (Ambiguity 45) | `eof_mrun.py row 9140 6400 6570 9150 ... 9260`; `textmap.py 6416 9146 6500 9250 3 --acid`; `n_c9170.png` (3.6x, three shots, every trace) |

What the join says. Traced (firm for the join): the clock of the five-stage ripple counter of the
left-centre strips is the same net as the gate line `lc3_w9947` of the gate column west of the island,
which gates one pull-down in each of four units there (`notes/blocks/tcw.md`: "a common enable or
clock"). Not traced: its driver. Every end drawn so far is a gate; the net goes on down the left bus
field (`lc3`, `busl`: the row y 14784, drawn to x 7550) toward the bottom-centre logic's 13-line bus.

### Piece `rc`: the fifth corner-bundle line of `lc3` is `rst_c` (traced; wiring only)

```
rst_c     = NOT rst_n                      lc1's third buffer of the reset NOR; now also rst_c
lc1_w7170 = NOT rst_c                      lc3's lower inverter (firm)
rcs_x1    = NOT lc1_w7170                  lc1's gate 2: the clear of the step logic's five latches
lc2_w8450 = NOT lc1_w7170                  the ripple counter's clear
tc2_r5589 = NOT((rst_ck & lc1_w7170) | (lc1_w7170 & tc2_sr_g))      eof's gate g7700
```

From the full extraction; `tools/unsure.py --equations lc1_w7170`: FIRM. The alias is `@alias rst_c
rst_c`.

| Stretch | What | Evidence |
|---|---|---|
| `lc2`'s poly | `P 6258,8742 y8758 x6285 6450,8923 w=20`: from latch C's clear pad (6257,8731), at 45 degrees out of the strip (its port `rst_c P 6450,8911-8936`) | `notes/blocks/lc2.md` |
| the bend | the diagonal runs on under `lpstb_b`'s metal x 6432 and in the open to (6472,8945), where it turns south; no poly at x 6472 north of the bend (y 8880) and field east of it | `n_c8930.png` (5.5x, four shots); `eof_rows.py row Y 6410 6540` for y 8880, 8960 |
| the run under `ck5`'s metal | x 6462-6482, y 8945-9175, under the metal x 6466-6478 for its whole length: orange in the chip-2 stripped shot, salmon between two edge lines in the clean shot; the metal over it has no ring, no widening and no dark stretch in either chip (Ambiguities 43, 44) | `eof_rows.py row Y 6410 6540` for y 8960-9230 (a run at x 6467-6478 at every cut); `tl5_tracks.py v 6472 8945 9172 --half 2`; overlay `n_o4.png` (2.15x, three shots) |
| the pad (6469,9209) | x 6451-6489, y 9189-9227: ring and bright centre in both metal shots (centre 149 / 199), a pitted box in the chip-2 stripped shot, a green hole in the clean shot. The poly arrives from the north through 20 px of open ground below `ck5`'s corner; **the pad's own metal leaves south** (the ring is dark on the north, west and east and open on the south in both chips) | `eof_cchk.py 6469,9209` (hole -2; rings N 49 / 60, S 111 / 111); `textmap.py 6416 9146 6500 9250 3 --acid`; `n_c9170.png` |
| the metal south | x 6465-6478 from the pad to a corner (6471,9452), west along y 9445-9458 onto `lc3`'s `M 6450,9455 x6429 y9712 ...`, the fifth line of its corner bundle (`rst_c`). No bar and no hole on the 220 px | `follow.py 6470 9260 S --gap 16` (corner (6467,9456), then `lc3`'s line to (6293,9714)); `tl5_tracks.py v 6472 9232 9446 --half 2`; `eof_mrun.py row` cuts y 9240-9540; `textmap.py 6450 9436 6490 9470 3`; overlay `n_o4.png` |

What the join says. Traced (firm): the input of `lc3`'s lower inverter is the third buffered copy of
`rst` = NOR(`lpstb_b`, `res_b`), so `lc1_w7170` is low during reset and high otherwise, and

- `rcs_x1` = NOT `lc1_w7170` is the reset again (four gates after the NOR): the clear of `tl1`'s two
  latches and `tl3`'s latches A, B and C is the reset, not a signal of the frame;
- the ripple counter's five stages are cleared during reset (`lc2_w8450`) and count outside it;
- `eof`'s gate `g7700` is, outside reset, `tc2_r5589` = NOT(`rst_ck` OR `tc2_sr_g`) with `rst_ck` low:
  NOT `tc2_sr_g`.

`rst_c` also runs down the left bus field (`lc3`, `busl`: the row y 14697, drawn to x 7550).

### Piece `n2n`: the latched R4 match's track ends on `bd1_n2`, the input of `rcs_e3`'s inverter (traced; wiring only; the join to `bd1_n2` open)

```
rcs_e3    = NOT bd1_n2                  tl4's inverter at y 3781-3911 (its load tie uncertain, as before)
the bus line x 5412 of tl5 = `bd1_n2`                       this piece: one net (alias), no uncertain item
the track x 6775  ?= bd1_n2                        believed: the track through busl's region, read and not drawn
bd1_n2    = NOT((bd1_an & rst_lat) | bd1_n1 | rst_a)      the latch on R4's match (pieces r4lat, n2out)
```

From the full extraction (`rcs_e3 = NOT bd1_n2`; `t1068` at (4752,3850), 57/18, is the net's only gate).
The aliases are an alias (dropped at the rename) and `tl4`'s own an alias (dropped at the rename).

| Stretch | What | Evidence |
|---|---|---|
| **not drawn**: `busl`'s region, y 15000-10400 | from piece `n2w`'s end (6711,15000) the metal runs north on x 6711-6712 to a corner (6711,13249), east along y 13243-13255 to (6777,13249) and north on x 6775-6777 to y 10400. The step is one of three nested Ls (the line x 6754 turns at y 13285-13300 to x 6819; 30 px of ground between). No pad on it: the metal is 9-15 px wide at each of the follower's contact candidates (the crossing field's poly rows beneath: trap 15) | `follow.py 6711 16100 N` (corners (6715,13242), (6781,13243), end (6948,8707)); `eof_mrun.py row` cuts y 14950-10450; `o_step.png` (3.6x, metal and clean); widths from `eof_mrun.py row` cuts 6 px apart round each candidate. **Read, not reviewed and not drawn** |
| the track | x 6769-6782 from y 10400 north; 11-14 px wide, no dark stretch over 14 px (the rows of two crossing fields beneath, y 9560-9810 and y 10300-10400, and two single rows, y 9984-9998 and y 10048-10064, the rows of the neighbours' pads (6818,9988) and (6730,10050): round 16), no widening; the pad (6818,9988) has its ring 18 px east of this track, with open poly and no metal between (`px.py row 9988 6762 6840 4 metal,metal1,acid1b`: 113-161 red at x 6790-6798 in both chips, against 192-221 on the track); from (6775,8952) a diagonal to (6947,8780) and north to the pad | `eof_mrun.py col 6775 8940 10410`; `eof_mrun.py row` cuts y 8770-8970 (x + y = 15727); overlay `o_ov1.png` (2.2x, metal and clean) |
| the pad (6947,8710) | x 6934-6962, y 8690-8727: ring and bright centre in both metal shots (191 / 187), a green hole in the clean shot (red minus green -17); the last of four pads in a staircase ((6815,8670), (6858,8715), (6905,8670) are the tracks x 6645, 6689, 6733, by diagonals x + y = 15532, 15597, 15662: other nets; corrected in review round 16). South of the pad the clean shot is protected field (pink) under the metal: the poly ends on the pad | `eof_cchk.py 6947,8710`; `o_end1.png` (3x metal), `o_p1.png` (3.2x, three shots) |
| the poly column | x 6941-6961, y 8440-8690: salmon under three horizontal metals (y 8530-8547, 8575-8590, 8615-8632; no pad, no hole: `o_x1.png`, 4x, both metal shots and clean), dark red-brown in the open above them (orange in the chip-2 stripped shot), 5 px east of `trunks`' L metal x 6920-6940 (not under it); at y 8416-8440 east to the pad | `eof_rows.py row` cuts y 8440-8680 (a run at x 6947-6954 at every cut); `o_n1.png` (1.9x), `o_n2.png` (3x), three shots each |
| the pad (6988,8427) | x 6968-7009, y 8409-8446: ring and bright centre (206 / 199), a dull hole in the clean shot (-7); nothing leaves it but the row from the west and the metal north (x 6984-6997); the outline north of it at x 6965-6975 in the clean shot is the metal's protected margin | `eof_cchk.py 6987,8425`; `textmap.py 6930 8392 7022 8458 3 --acid`; `o_p2.png` (4.2x, three shots) |
| the metal north | x 6985-6997, y 7006-8408: over ten poly rows of the crossing field (y 7170, 7213, 7388, 7432, 7475, 7517, 7648 `rst_ck`'s tap, 7778 `g7700`'s row 3, 7887 `tl3_w3982`, 8037 `lc1_w7928`), bars of 8-14 px, no widening | `follow.py 6987 8395 N --gap 16`; `eof_mrun.py col 6991 6980 8420`; `eof_rows.py col 6975 7010 8420`; overlay `o_ov4.png` (0.9x, three shots) |
| the corner (6991,7000) | a plain L, the middle of three nested corners (row y 6957 turns south on x 7035, row y 7043 on x 6948), ground between them in both chips | `o_c1.png` (3.3x, both metal shots and clean); `eof_mrun.py row` cuts y 6960-7030 |
| the metal west | y 6994-7006, x 6172-6998: over five vertical polys (x 6280, 6323, 6366, 6409 `tc2_m6404`'s, 6451 `lc3_w9947`'s), ten edge bars of 9-12 px, no widening | `eof_mrun.py row 7000 6120 7010`; `eof_rows.py row 6979 6180 6990`, `row 7022`; overlay `o_ov2.png` (1.4x, metal and clean) |
| the pad (6146,6997) | x 6127-6166, y 6978-7015: ring and bright centre (198 / 212), green hole (-25). East of it under the metal the clean shot is protected field (190-197/117/125, the chip-2 stripped shot red minus green about 0): the poly ends on the pad | `eof_cchk.py 6145,6996`; `px.py row 6998 6100 6230 5 acid,acid1b,metal`; `o_r1.png` (2.15x, three shots) |
| the row | y 6988-7004 from the pad west to (5624,6996), salmon without a break in the clean shot, under about ten vertical metals (x 5668-6104, among them `rc_stepreq_n`'s x 5843 and `rst_ck`'s x 6105), field between it and the rows y 6953 and 7040 (`eof_rows.py row 6975 5600 6220`: nothing between the diagonal and the pads) | `o_r1.png`; `eof_rows.py row 6996 5600 6220`, `col` cuts x 5650-6120 |
| the diagonal | centre x - y = -1372 from (5624,6996) to the bend (5412,6784); the other two undrawn lines of the bundle run parallel at x - y = -1306 (from `tl5`'s poly x 5455 to the row y 6953) and -1439 (x 5368, row y 7040), 46 px away on either side, and none of the three crosses another; under one horizontal metal y 6830-6850 (no pad) | cuts in the chip-2 stripped shot, `eof_rows.py row` y 6790-6980 (three runs at each: 5460/5527/5593 at y 6900, 5491/5559/5627 at 6930, 5521/5590/5652 at 6960); `eof_rows.py diag 5412 6770 5640 6998 --step 20 --reach 110` (the line at offset 5-11 at every step); `o_b2.png` (2.1x), overlay `o_ov3.png` (1.85x), stripped and clean |
| the column | x 5403-5421 from the bend north to `tl5`'s poly end (`P 4967,5761 x5412 y6350 w=20`, its port `bd1_n2 P 5402-5422,6350`), under nine horizontal metals (y 6372, 6415, 6460, 6502, 6545, 6589, 6632, 6675, 6719): only the 3-6 px bars of the gaps between them, no hole | `px.py col 5412 6345 6790 3 acid1b,metal,metal1`; `eof_mrun.py col 5390 6340 6880 5434`; `o_b1.png` (1.45x clean) |

What the join says. Traced (firm, no uncertain item on the drawn wire): the net `bd1_n2`, whose one gate
is the pull-down of the inverter that makes `rcs_e3` (an input of `rcs_in3` = NOR(`rcs_e3`, `rcs_e4`) and of
`rcs_bc3460` in the row counter's step logic), comes from the south: out of `tl5`'s poly bus, through
`lc1`'s diagonal bundle and the crossing field, down the track x 6991 and the poly column to the track
x 6775, which leaves north of `busl`'s region at (6775,10400). Believed (the open join): that track is the
one piece `n2w` drew to (6711,15000), so the bus line x 5412 of tl5 is `bd1_n2` and **`rcs_e3` = NOT (R4's match as
latched)**. If so the latch on R4's match has one load, 23,000 px away, in the row counter's step logic,
and no gate on the way. What that does in the step logic is `tla`'s, `tl1`'s and `tl2`'s equations
(`notes/operation.md`); nothing new about them is traced here.

### Piece `ck6`: the ripple counter's clock is driven by an inverter in the bottom-centre logic (traced; the load's tie uncertain)

```
lc3_w9947  = NOT eof_w15127                the inverter U under the east VSS rail (x 8687-8737), y 14942-15062
```

From the full extraction: `t1878` at (8733,15000), 70/20, gate `eof_w15127`, between `vss` and `lc3_w9947`;
the load `t1877` at (8588,15029), 36/39. `tools/unsure.py --equations lc3_w9947`: depends on uncertain items
(the tie, Ambiguity 52). The net's other ends are all gates (the counter's stage B0, `tcw`'s four
transistors: piece `ck5`), so this is its driver. The gate's net `eof_w15127` is drawn from the gate
pad by its metal to the pad (8833,15127); beyond that it is the unit below (piece `vw`, next section).

| Stretch | What | Evidence |
|---|---|---|
| `busl`'s row on east | poly y 14772-14796 from x 7550 to the pad: salmon under the field's vertical metals, orange in the chip-2 metal shot in the gaps, no break | `px.py row 14784 7540 7830 14 acid1b,acid,metal` |
| the pad (7837,14784) | ring and bright centre in both metal shots (x 7833-7842, y 14778-14790), green hole in the clean shot; the bus metal leaves east | `textmap.py 7800 14760 7872 14810 3 --acid`; overlay `p_o4ab.png` (4.2x, metal and clean) |
| the bus metal y 14784 | y 14776-14792, x 7837-8293, the eleventh of `bc1`'s thirteen bus lines; it ends on the east pad (nothing east of it: R1's edge is 37 px on) | `follow.py 7900 14786 E --gap 16` (end (8296,14784)), `W` (end (7832,14784)); `p_s1.png` (0.8x) |
| the pad (8293,14785) | ring and centre in both chips (x 8289-8298, y 14781-14790), pit in the chip-2 stripped shot, green hole in the clean shot | `textmap.py 8262 14760 8330 14850 3 --acid`; `p_pad1.png` (4.8x, four shots); overlay `p_o4ab.png` |
| the poly L | from the pad south (x 8286-8310) to y 14836 and east along y 14816-14834: orange in the chip-2 metal shot | `p_pad1.png`; the same text map (the stripped shot's poly at x 8283-8310, y 14787-14832) |
| the row y 14825 | 680 px: under R1 (x 8330-8380), the VCC vertical (x 8415-8465) and the VSS band (x 8508-8735, the band's top edge lies along the row: Ambiguity 51), salmon; dark red-brown in the three gaps and in the open from x 8735 to 8860 (orange in the chip-2 metal shot, y 14817-14837); under a metal x 8872-8890 (the unit V's input, not drawn) and, from x 8915, lengthwise under the metal y 14820-14840 of the neighbouring pad (9008,14828) (Ambiguity 51); south at x 8957-8980 | `px.py row 14824 8296 8640 8 acid1b,acid,metal`; `p_pad2.png` (3.9x, four shots), `p_s3.png` (2x, metal and clean); `textmap.py 8898 14806 8994 14848 3`; overlay `p_o3.png` (2.9x, metal and clean) |
| the pad (8967,14870) | ring and centre in the metal shot, green hole in the clean shot; 20 px of field between the turn and the neighbouring pad (9008,14828) (another net) | `p_s3.png`, `p_o3.png` |
| the metal x 8968 | x 8958-8978, y 14866-15040, over open field, nothing crossing | `follow.py 8968 14910 S --gap 16` (end (8968,15020)), `N` (end (8967,14866)); `p_o3.png` |
| the pad (8962,15040) | ring and centre in both chips, pit, green hole; field east and south of it. (`rst_a`'s metal on the same x starts at its own pad (8966,15260), 220 px further south: piece `isrc`) | `p_e1.png` (3.1x, four shots) |
| the row y 15042 | y 15034-15050 from the pad west under the track x 8925 (the neighbouring pad (9008,14828)'s net), the metal x 8882 of the unit V's input and `eof_w15127`'s metal x 8838 (no pad on it under any of them) into the box | `p_r1.png` (2.9x, metal and clean); `textmap.py 8756 15006 8822 15072 3 --acid` |

The inverter U, by hand (`findcell.py 4951 4786 5213 4912 --region 8480,14880:8900,15400 --layer acid1b`
gives `tl5_inv` turned over, `@inst tl5_inv 3602,10158 mx=5082 rot=180 o=5082,4849`, at 0.62 only: the
plate is shorter and wider and the pull-down runs on east of the rail). `p_g1.png` (2.15x, four shots),
`p_g2.png` (clean, 4.1x), `p_g3.png` (chip-2 stripped, 4.1x); overlay `p_o1.png` (3.4x, metal and clean).

| Part | Where | Evidence |
|---|---|---|
| VSS box | x 8698-8742, y 14942-14993, under the rail x 8687-8737; contact (8712,14965): ring and centre in both chips, hole in the clean shot | `railprof.py 8692 8732 14880 15300` (diffusion 14952-14991, gate 14992-15016, diffusion 15017-15062); `textmap.py 8676 14936 8750 15070 3 --acid` |
| the box's tab east of the rail | x 8745-8770, y 14968-14990, in the open gap between the rail and `bc1_dec10_n`'s thin metal x 8789-8801: an outlined patch in all four shots, green in the clean shot (134/156/81 at (8757,14978)) | `px.py col 8757 14950 15072 4`; `px.py row 14980 8684 8800 4` |
| gate row | y 14990-15010, rounded west end x 8682, east across the rail and the gap, under the thin metal, to the pad with a contact (8836,15000) (centre in both chips, green hole) | `p_g2.png`; `textmap.py 8812 14976 8866 15030 3` |
| the channel | x 8698-8768: the diffusion's east edge is a dark line across the gate poly at x 8764-8768 in both metal shots (155-174 red on the poly west of it, 45-85 on the line) | `px.py row 15000 8736 8832 4` |
| node | under the rail y 15015-15040 and east of it to the box's pad (outline x 8745-8800, y 15018-15060); diffusion in the chip-2 shots (stripped: red minus green 21-25; metal shot 38-41, against 18-25 on the field south of it) | `px.py col 8757 14950 15072 4`; `px.py row 15028 8736 8832 4` |
| output box | buried contact x 8768-8797, y 15030-15052; the row y 15034-15050 ends in it. `bc1_dec10_n`'s thin metal passes over it (Ambiguity 49) | `p_b1.png` (4.8x, four shots); `textmap.py 8756 15006 8822 15072 3 --acid` |
| load | strip from the node west (y 15021-15043; from y 15012 under `bc1`'s thin metal x 8637-8650), under the plate (x 8568-8607, y 14978-15062; the strip's edges are the dark lines y 15008-15012 and y 15044-15048 across the plate) to the VCC box under R2 (x 8508-8562, y 15008-15056; contact (8534,15033): centre in both chips, hole) | `px.py row 15030 8540 8665 4`; `px.py col 8590 14960 15075 4`; `textmap.py 8500 14996 8572 15066 4` |
| tie | the plate's tab runs east along its top (poly to x 8619: `px.py row 14988 8596 8662 3`) to a heavy-outlined box (8628-8648, 14977-15000) on a tail of the strip, under `bc1`'s thin metal: drawn `?P`, `?B` (Ambiguities 50, 52) | `p_t12.png` (5.5x, clean and both metal shots) |
| the input's metal | x 8830-8848 from the gate pad (8836,15000) south over the row y 15042 of `lc3_w9947` (no pad) to a pad with a contact (8833,15127) (centre in both chips, pit, green hole); the pad's poly row y 15120-15138 goes west into the output box of the unit below | `follow.py 8838 15075 S --gap 16` (end (8838,15107)), `N` (end (8838,14997)); `p_in1.png` (3.1x, four shots), `p_o1.png`, `p_o2.png` |

### Piece `vw`: the units V and W, a cross-coupled pair that makes `eof_w15127` (traced; one link and the two ties uncertain)

```
eof_w15127 = NOT(eof_w15172 OR eof_w15300)                              unit V, y 15100-15285
eof_w15300 = NOT((ck_out AND bc2_w15607) OR eof_w15127 OR rst_a)    unit W, y 15285-15470
```

From the full extraction (which prints V's first term as `eof_w15172 & eof_w15172`: the hairpin gives two
gates in series on one net): V's load (8596,15133) 26/52; its stack 90/24 twice, both gated by
`eof_w15172`; (8645,15216) 34/23, gate `eof_w15300`, `eof_w15127` to `vss`. W's load (8595,15317) 30/54;
its stack 105/20 (gate `ck_out`) over 104/21 (gate `bc2_w15607`); (8642,15384) 36/22, gate
`eof_w15127`; (8776,15260) 43/19, gate `rst_a`, `eof_w15300` to `vss`. `tools/unsure.py --equations`: both
depend on uncertain items (the two ties).

The build is `tl1`'s latch units' (`tl1_ua`, `tl1_ub`), drawn by hand (`findcell.py` finds no copy at 0.5
over 8480,15040:8960,15700): a stack under the VSS rail, its node carried west under a thin metal and a
load plate to a VCC box, a tie box beside the plate, and a third pull-down under the thin metal whose gate
is the other unit's plate. New here: each stack's diffusion is **90 px wide**, from under the rail through
the open gap east of it to under the east thin metal. Views `r16_*.png` in `cache/scratch/eof/` (clean shot 4x:
`r16_v_clean.png`, `r16_w_clean.png`; both metal shots 3x: `r16_mw.png`, `r16_me.png`); overlays
`r16_o_w.png`, `r16_o_e.png` (2.85x, metal and clean) and `r16_o_n.png` (1.6x, the wires north). The colours
of the open gaps beside the rail were calibrated on V's node, which crosses both gaps (`tools/t.sh eof
eof_patch.py`): diffusion is 19-21 (chip-2 stripped shot, red minus green) and 31-33 (chip-2 metal shot),
about 115/80/65 in the clean shot; field is 2 and 20-23, about 105/100/65.

| Part | Where | Evidence |
|---|---|---|
| V's stack, hairpin, output box, load, plate pad, tie box, the metal south and the hairpin's wire | as in the withdrawn drawing (`cache/scratch/eof/draft-ck7.txt`), which review round 17 found right as far as it went | rows A and B one poly joined at x 8866-8897 with the pad (8880,15172), both ending free at x 8694 (`p_v5.png`); `railprof.py 8692 8732 15090 15470` (node 15111-15164, gate, 15189-15207, gate, diffusion from 15233); `eof_cchk.py` on the pads (8880,15172), (8592,15168), (8592,15383), (8702,15260): holes -22 to -33, centres 212-237 |
| V's column under the thin metal x 8637-8650 | x 8628-8662 from the node strip down to y 15256: the tie box, tan, the arm's gate y 15205-15228 (240-247 red), a pocket y 15232-15256 | `railprof.py 8632 8652 15090 15470` (diffusion 15124-15208, gate 15209-15233, diffusion); round 17's finding 1; `r16_v_clean.png` |
| the arm's poly | x 8597-8672, y 15205-15228; one poly with a column x 8597-8612 south, a widening y 15262-15298 and **W's plate**: salmon without a break from y 15208 to 15296, one edge line at y 15300 (the load strip's edge), the plate (244-248 red) below; field (pink 204/120) above y 15204, so it is not the plate pad's poly | `px.py col 8604 15196 15312 4 acid1b,acid`; `px.py row 15245 8562 8634 3` (salmon x 8598-8610); `px.py col 8668 15140 15440 4` (the arm reaches x 8668: orange 95-112/57-76 in the chip-2 metal shot) |
| the pocket into V's VSS box | through the 17 px open gap between the thin metal and the rail, y 15240-15257: chip-2 stripped 121-148/85-116 (red minus green 32-36) and both metal shots 149-174/111-133 (38-50) at x 8660-8668, tan on both sides (x 8640-8656 and from x 8672); the patch x 8663-8674, y 15242-15254: 22.8 in the stripped shot, 146/110/87 in the clean shot | `px.py row 15248 8640 8700 4`; `eof_patch.py 8663 8674 15242 15254`. VSS box x 8685-8730, y 15240-15284 |
| the stacks under the east thin metal | diffusion x 8777-8797 from V's box pad (y 15146) to y 15424: tan 188/178/140 between the rows, pink 196/120/132 north of y 15110 and south of y 15430, a dark line down its east side at x 8797. Rows A, B, C, 1, 2 are all at channel brightness on it (red 222-238; poly over field under the rail is 196-220) | `px.py col 8787 15060 15450 5 acid1b,acid,metal,metal1`; round 17's finding 2; `r16_east.png` (4x, three shots) |
| **the open gap east of the rail (x 8742-8777): the same diffusion runs through it** (review round 19; first drawn as field between the rows, with the part under the thin metal as a second finger) | no diffusion edge crosses rows A, B, 1 or 2 between the rail's edge and the thin metal's in either metal shot (red 152-186 in chip 2 from x 8742 to 8778 on each row; a real edge is 50-65: the inverter's at x 8766, row C's at x 8754); the nodes, which are diffusion in the gap by colour (21.2 and 33.0 at V's, 25.2 and 36.0 at W's), run up to the rows' edge lines with no line of their own, and every edge of rows A, B, 1, 2 in the gap is a single line as over plain field (minimum red 53-71 in chip 2, like the same rows at x 8850). The one doubled line (30-36 in chip 2, 33-43 in chip 1, 43-49 in the stripped shot, 9 px wide) is row C's top edge west of x 8757: the diffusion's boundary, which comes up x 8754 under row C and turns west along the row's top to the rail. So the band between B and C is V's ground, and row C's west end lies on field. Below row 2 the gap is diffusion by colour too (18.7 and 30.4). **Against**: the three bands between the rows have field colour in the chip-2 stripped shot (Ambiguity 53) | `px.py row Y 8730 8802 3 metal,metal1,acid1b` for Y = 15000, 15175, 15216, 15260, 15345, 15388 and the bands 15196, 15241, 15367, 15415; `px.py col X 15150 15282 2` and `15300 15432 2` for X = 8746-8772 and 8850/8858, in `metal`, `metal1`, `acid`; the reviewer's `e_gap_metal.png` (6x), `e_gap_v.png`, `e_gap_w.png`, `rowc.png` in `cache/scratch/eof/review-19/` |
| row C | poly y 15251-15270 from a rounded west end at x 8733-8738 east, in the open (orange in both metal shots), under the track x 8925 without contact (no hole, no ring: `eof_cchk.py 8920,15260`) onto the row of `rst_a`'s end pad (8966,15260). The diffusion under it is x 8754-8797 (its west edge a dark line across the poly in both metal shots) | `r16_me.png`, `r16_o_n.png`; round 17's `px.py row 15260 8736 8862 6` |
| W's stack | under the rail: node y 15309-15330, row 1, a closed diffusion y 15356-15374, row 2, diffusion from y 15406 with a contact (8722,15440) (hole -6, centres 211/228). Both rows end in the west at x 8681: poly over field x 8681-8692 (196-220 red), the diffusion's edge a dark line at x 8692-8696, channel (243-254) east of it; pink field between the two ends | `railprof.py 8706 8732 15090 15470`; `px.py row 15340 8650 8712 3`, `row 15386 8600 8716 4`, `col 8684 15296 15412 4` |
| W's node east, box and output | diffusion through the open gap from y 15309 (25.2 and 36.0: `eof_patch.py 8741 8750 15312 15328`; field north of it, 7.0 and 23.3 at y 15280-15296, green in the clean shot); the pad round the box x 8752-8800, y 15276-15328; row y 15292-15317 to the pad (8835,15302) (hole -35, centres 181/215); metal x 8830-8848 south over rows 1 and 2 (no hole: `eof_cchk.py 8838,15345 8838,15388`) to a pad (8836,15456) (hole -17) | `follow.py 8836 15330 S --gap 16` (end (8839,15434)); `r16_o_e.png` |
| rows 1 and 2 east | row 1 (6 px lower east of the rail) to the pad (8881,15351) (hole -38, centres 227/189), whose metal goes south: `follow.py 8880 15375 S --gap 16` runs 1,346 px (corners (8890,15699), (8926,15699), (8922,15913), (8882,15915), end (8882,16623)); row 2 to the pad (8922,15392) (hole -31, centres 229/210), whose metal runs north on x 8925 to a corner (8930,14830) and east to the pad (9008,14828) (hole -22): `follow.py 8920 15300 N --gap 16`. Row 1's metal crosses row 2 without contact (`eof_cchk.py 8881,15388`: no hole) | `r16_me.png`, `r16_o_n.png` |
| **the row of the pad (8592,15383) is not row 2** (trap 34) | from the pad east: channel x 8624-8652 under the thin metal (240-247 red), poly to x 8666 (orange 137/82-99 and 148/71-96 in the two metal shots at x 8660-8664), then 14 px that are not poly in three shots (x 8672-8676: clean 150-154/147-151, chip-2 metal 87-91/81-83, chip-1 metal 91-111/70-109), then row 2's end from x 8681 | `px.py row 15386 8600 8716 4 acid1b,acid,metal,metal1`; `textmap.py 8612 15358 8704 15434 2 --acid`; `r16_ww.png` (4x, stripped and clean): Ambiguity 54 |
| W's column, node strip and foot | the column x 8624-8660 under the thin metal from y 15302 to 15420 (`railprof.py 8632 8652`: diffusion to 15373, gate 15374-15397, diffusion to 15428), wider in the open gap at y 15316-15358 (22.9 and 27.7: `eof_patch.py 8663 8674 15322 15356`); the node strip y 15302-15316 between it and the rail (tan from x 8672 east at y 15310; its top edge one line at y 15300-15302 from the plate to the rail); the foot y 15402-15420, whose bottom edge runs in one line from x 8620 to the rail in the clean shot and both metal shots | `px.py row 15310 8640 8712 4`; `r16_foot.png` (4x, three shots); Ambiguity 55 |
| W's load and tie | plate x 8568-8622, y 15298-15335 over the strip y 15302-15332; VCC box `bc1`'s (8505-8562, 15250-15327; contact (8531,15290), centres 237/201). Tie: a tab of the plate's widening (bright patch x 8627-8635, y 15272-15292) into a heavy-outlined box (8645-8663, 15281-15298) on a tail of the strip, with a bar y 15302-15310 below it: drawn `?P`, `?D`, `?B` | `r16_wtie.png` (6x, four shots); `px.py row 15286 8604 8672 4`; `px.py col 8652 15262 15322 4`; Ambiguity 56 |

What it does (the equations are marked). V and W hold one bit. `eof_w15172` high forces `eof_w15127` low,
which makes the clock `lc3_w9947` high; `ck_out` AND `bc2_w15607` high, or `rst_a` high (the reset),
forces `eof_w15300` low, which lets `eof_w15127` rise, the clock low. So **the ripple counter's clock is
set high by `eof_w15172` and low by (`ck_out` AND `bc2_w15607`) or the reset**; while both conditions
are low it holds. During reset the clock is `eof_w15172` itself. What the three signals are is open: none
of them is followed (Ports, Not done).

### Pieces `in390` and `in172`: two of the latch's inputs to their sources (traced; no uncertain item)

```
W's lower stack gate = bc2_w15607               one net: latch unit b's lower node (bc2), by a poly row and a metal
eof_w15172 = NOR(bc2_w14955, bc2_w15000)        unit T, the top unit of bc2's east gate column, y 14598-14790
```

From the full extraction: `t2121` at (10512,14654) 35/22, gate `bc2_w15000`, `vss` to `eof_w15172`; `t2122` at
(10512,14739) 35/22, gate `bc2_w14955`, `eof_w15172` to `vss`; the load `t2123` at (10688,14704) 27/56.
`tools/unsure.py --equations eof_w15172`: FIRM. W's equation now reads `eof_w15300` = NOT((`bc2_w15607` AND
`ck_out`) OR `eof_w15127` OR `rst_a`) (marked as before: W's tie). With `bc2`'s equations (marked there:
copies of `tl1`'s cells, reviewed on Opus only, R31): `bc2_w15000` = NOT((`bc2_w14912` AND `bc2_w14955`) OR
`bc2_w15029`), latch unit a's upper node, and `bc2_w15607` = NOT((`bc2_w15352` AND `bc2_w15432`) OR
`bc2_w15476` OR `bc2_w15565`), latch unit b's lower node.

What it does. `eof_w15172` is high only while latch unit a's enable `bc2_w14955` is low (the latch holds) and
its upper node `bc2_w15000` is low, i.e. while unit a holds a set bit (`bc2_w15029` high; believed, from
`bc2`'s equations); that sets `eof_w15127` low and the ripple counter's clock `lc3_w9947` high. The clock goes
low again when `ck_out` and latch unit b's lower node are both high, or at reset. What latch units a and b
store is not traced (`bc2`: their data, enables and b's clear are not followed).

**Piece `in390`** (views `r17_*.png` in `cache/scratch/eof/`; survey at 1.15x `r17_s1.png`, `r17_s2.png`):

| Stretch | What | Evidence |
|---|---|---|
| the column | poly x 9005-9023 from the pad (9008,14828) north to y 14600: salmon in the clean shot under each metal that crosses it, orange in the chip-2 metal shot in the gaps (the older piece `P 9002,14790:9020,14815` was 3 px west) | `px.py row 14700 / 14740 / 14780 8994 9034 3 acid1b,metal,acid` (edges x 9003, 9024); `px.py col 9014 14676 14816 4 acid1b,metal,metal1`; `r17_a3.png` (3.7x, four shots) |
| what crosses the column | `eof_w15172`'s own metal y 14777-14794 and `bc1`'s bus metals y 14733-14752 (it turns south at x 9100), y 14690-14708 (it ends on the pad (9092,14697)) and y 14648-14664 (it turns south at x 9141): no pad, no ring, no hole at any | `eof_cchk.py 9014,14785 9014,14742 9014,14699`: red minus green 43, 40, 32 (a contact here is -15 to -28: `eof_cchk.py 9092,14697 9054,14785 9008,14828`); `9011,14656`: 1, with centres 231/217 and the ring open west and south (Ambiguity 58) |
| the corner | y 14600-14621 at x 9005-9025: no poly west of x 9003 (pink field in the clean shot); `bc1`'s bus metal y 14603-14618 comes from the west and lies on the row from here | `r17_a2.png` (6.4x, four shots); `textmap.py 8986 14590 9062 14672 2 --acid` |
| the row under the bus metal | x 9025-9190: the metal ends its run at x 9190 by turning south as the thin metal x 9184 (no metal at x 9184 north of y 14600); the poly goes on east. No contact on the 185 px: the clean shot's map is 4-7 with no hole, both metal shots are bright without a ring (one 8 px bar at x 9173-9176 in chip 2 only) | `textmap.py 9020 14596 9200 14624 3`; `textmap.py 9150 14584 9240 14634 2 --acid`; `eof_mrun.py row 14630 9000 10500 14608 14652 14674 14580`; `r17_a1.png` (3.6x, three shots) |
| the row east | y 14600-14621 to x 10078, the same y at every cut; under the thin metals x 9228, 9271, 9357, 10008, 10051 and the wide ones x 9467-9511, 9552-9597, 9814-9856 (rails: poly over field under each, no diffusion) | `eof_rows.py col X 14560 14760` at X = 9160 .. 10100; `railprof.py 9470 9508 14540 14900`, `9555 9597`, `9816 9856`; `eof_cchk.py` at the eight crossings: 35-47, no hole; `r17_s1.png` |
| the pad (10092,14609) | x 10074-10112, y 14594-14624: a bright centre 12 px across in a dark ring in both metal shots, pits in the chip-2 stripped shot; vivid red-orange with no green hole in the clean shot (Ambiguity 59). Field east of it under the metal | `textmap.py 10062 14584 10124 14630 2 --acid`; `r17_e1.png` (3x, three shots); overlay `r17_o4.png` (4x, both metal shots and the clean shot) |
| the metal | y 14604-14618 east to a corner (10268,14607), south on x 10261-10275 for 910 px: over `eof_w15172`'s row y 14653 (no hole: 42) and `bc2`'s clear row y 15565 (41; `bc2`'s own reading) to `bc2`'s metal `M 10267,15515 y15622`, which ends on its pad (10267,15607) | `follow.py 10269 14700 S --gap 16` (end (10265,15614), 930 px), `N` (corner (10261,14606), end (10117,14612)); `eof_mrun.py row 14800 10180 10420 14900 15000 15100 15200`; the follower's candidate (10268,14829) is nothing (`textmap.py 10236 14806 10300 14852 2 --acid`: the metal bright and unbroken, no ring); `r17_m1.png` (1.28x, metal and clean, `bc2`'s trace outlined) |

**Piece `in172`**:

| Part | Where | Evidence |
|---|---|---|
| the row east of x 9150 | y 14644-14664 to x 10302; `bc1`'s bus metal y 14648-14664 lies on it from x 9044 to x 9141 and turns south there (run 16); under the same vertical metals as the row above, and under `bc2_w15607`'s metal x 10268 | `eof_rows.py col`; `eof_cchk.py` at twelve crossings: 26-47 (26 under the wide metal x 9489; no ring, no pad); `px.py row 14652 10254 10310 3 acid1b,metal` against the same row under the metal x 10051 (`10036 10072`): the same dark bar at the metal's edge, salmon through it |
| the step | the row's east end x 10302; a vertical x 10284-10301 from y 14644 to 14704; the lower row y 14687-14704 east. 28 px of field between the step and pad A's outline (blue 79-88 in the chip-2 metal shot against 51-66 on the poly) | `px.py row 14652 10262 10346 4 metal,metal1,acid`; `row 14672 10266 10330 4`; `col 10294 14628 14716 4`; `col 10330 14664 14716 3`; `r17_e1.png`; overlay `r17_o2.png` (3.6x, metal and clean) |
| the lower row | under pad A's metal x 10355 and the metal x 10397 (`bc2`'s data line) without contact; the clean shot's ring at (10378,14695) is the gap between those two metals (not in the chip-2 shots) | `eof_cchk.py 10355,14695 10397,14695`: 47, 45; `r17_p1.png` (4x, four shots) |
| unit T, the body | diffusion x 10495-10530, y 14622-14771, west of the rail: outlined in both metal shots and the chip-2 stripped shot, red minus green 13-19 there inside against -3 to -8 outside. Chip 1's clean shot is covered by dark residue here (Ambiguity 60) | `eof_patch.py 10502 10535 14626 14634` (19.0), `10502 10514 14670 14678` (13.7), `10502 10535 14757 14767` (13.2), outside: `14600 14612` (-3.3), `14780 14790` (-4.3), `10470 10488 14668 14676` (-7.6); `px.py row 14631 / 14654 / 14674 / 14739 / 14762 10484 10552 4 metal,acid`; `r17_u2.png` (3.5x, four shots), `r17_u3.png` (6.5x, chip 2) |
| the two VSS boxes | the top band y 14622-14642 and the bottom band y 14752-14771 run on east of x 10530 (no edge there at y 14631 and y 14762) into boxes under the rail with contacts (10562,14613) and (10562,14769): ring and bright centre in both chips, pits | `eof_cchk.py 10562,14612 10562,14768` (0 and -9; centres 189-207); `px.py col 10570 14596 14790 4 all` |
| gate rows 1 and 3 | poly y 14643-14665 and y 14728-14750, orange from the pads to x 10541, 10 px past the body's east edge (the dark line x 10528-10532) and short of the rail; nothing of them under the rail (no edge between y 14648 and 14684 at x 10570) | `px.py row 14654` and `row 14739`; `px.py col 10520 14606 14790 4 metal,metal1,acid` |
| the output box | heavy-outlined box x 10484-10520, y 14681-14714 at the end of the lower row, on the node between the two gates: inside greenish-grey 143/145/78 in the chip-2 metal shot (poly is 160/116/56, diffusion 172/135/86) | `px.py row 14697 10464 10528 4`; `px.py col 10505 14664 14730 3`; `r17_u3.png` |
| the node strip | y 14690-14706 from the body (no edge at x 10530 at y 14697) east under the rail (bright between two dark lines y 14688 and y 14704-14708 in both metal shots) to x 10625; diffusion by the stripped shot (16.0 against -7.6 to 5.6 on the field beside it) | `px.py row 14697 10524 10664 4 metal,metal1,acid`; `eof_patch.py 10631 10643 14710 14734 14693 14702`; `r17_u4.png` (4.6x, chip 2), `r17_u5.png` (4.6x, chip 1) |
| the load | strip y 14690-14717 under the plate (poly x 10660-10716, y 14668-14762: 38-42) to the VCC box (x 10718-10770, y 14690-14736) with a contact (10742,14712) (ring and centre in both chips, speck in the clean shot); a tail x 10627-10647 from the strip south into a heavy-outlined box (10624-10652, 14738-14768) that the plate's tab (x 10648-10662, y 14742-14762) runs into: the tie, in the open, the same in three shots; drawn without `?` (Ambiguity 61) | `r17_u4.png`, `r17_u5.png`; `eof_patch.py 10664 10712 14694 14712 14672 14682 14726 14756`; `eof_cchk.py 10742,14712` (-19); overlay `r17_o1.png` (3.15x, chip-2 metal and stripped) |
| pad A and its metal | pad x 10335-10373, y 14636-14672, contact (10352,14654): ring in both chips, a dim centre, a green hole 12 px across in the clean shot, pits. Metal x 10348-10362 south, unbroken from y 14712 to 15008, with a foot east along y 14993-15007 into the ring of `bc2`'s pad (10395,15000): bright to x 10376, the ring's dark 10 px, the pad's centre x 10390-10400 (trap 16 (b): a passing metal leaves about 24 px) | `textmap.py 10326 14630 10380 14682 2 --acid`; `eof_mrun.py col 10355 14640 15030`; `textmap.py 10336 14972 10420 15022 2`; `eof_cchk.py 10395,15000` (-26; ring W 39 / 81) |
| pad B and its metal | pad x 10420-10458, y 14720-14756, contact (10440,14738): ring, bright centre, green hole, pits. Metal x 10434-10448 south: unbroken y 14761-14895, two bars at `bc2`'s data row y 14905-14922 (which it crosses, as `bc2` drew), onto `bc2`'s metal `M 10441,14940 y15188` and the pad (10441,14955) | `eof_cchk.py 10440,14738` (-16); `follow.py 10441 14800 S --gap 16` (end (10441,15150)), `N` (end (10439,14736)); `eof_mrun.py col 10441` |
| the rails | VSS x 10543-10597 and VCC x 10721-10771 over the unit, `bc2`'s rails going on north | `r17_u1.png` (3x, metal and clean), `r17_o1.png` |

### Piece `in350`: the third input of the latch is `ck_out` (traced; wiring only, no uncertain item)

```
W's upper stack gate = ck_out               one net, by 3,500 px of metal and one poly hop, on trunks' ck_out #1
eof_w15300 = NOT((ck_out AND bc2_w15607) OR eof_w15127 OR rst_a)        unit W, as the full extraction now prints it
```

From the full extraction: `t1895` at (8747,15343) 105/20, gate `ck_out`, `eof_w15300` to the stack's middle
node. `tools/unsure.py` does not list `ck_out` among the nets joined only through uncertain
items: no `?` on the path (W's equation stays marked: its tie). The gate's wire carried a placeholder name and
an alias until the refresh of 2026-11-20 renamed it.

What it says (traced for the join; the rest as marked before): the latch behind the ripple counter's clock is
clocked. `lc3_w9947` = NOT `eof_w15127` goes low when `ck_out` is high (CLK low) while latch unit b's lower
node `bc2_w15607` is high (W's stack pulls `eof_w15300` low, which lets `eof_w15127` rise), and high when
`eof_w15172` = NOR(`bc2_w14955`, `bc2_w15000`) is high. Believed, not traced: the two pads in the metal's run
are the enable rows of a latch copy of `tl1`'s build (below), so that latch would be open while `ck_out` is
high; `bc2`'s unit a has its enable on another net (`bc2_w14955`).

The path, from W's pad to `trunks`' metal (all `eof`'s; images in `cache/scratch/eof/`):

| Stretch | What | Evidence |
|---|---|---|
| metal x 8882, y 15455-15698 | on south from piece `vw`'s end; 14 px wide (edges x 8872 and x 8892) | `follow.py 8880 15480 S --gap 16`; `tl5_tracks.py v 8882 15470 15700` (two bars of 9 px, no hole); `px.py row 15600 8866 8900 2 metal` |
| the step east, y 15698 | a Z: east 43 px onto x 8925 (centre y 15698, edges y 15687 and 15708). It goes round **a pad with a contact (8882,15745) of another net** (hole -39, centres 238/221), whose metal lies in the vacated position x 8882 from y 15736 to y 15878 and leaves west and south on x 8838; 28 px of open ground (green in the clean shot) between the step and that pad's ring | `r18_j1.png` (2.6x, both metal shots and the clean shot); `tl5_tracks.py h 15700 8870 8935` (no break), `v 8882 15700 15915` (no metal y 15706-15734 and y 15878-15908, clean shot green at y 15716 and y 15891); `follow.py 8882 15800 N` and `S`; `eof_cchk.py 8882,15745` |
| metal x 8925, y 15698-15915 | 217 px over two poly rows (y 15765-15790, y 15810-15840: bars, no ring, red minus green 30 and 34); row 2's metal above it ends on its pad (8922,15392), with no metal from y 15398 to y 15691 | `tl5_tracks.py v 8925 15690 15925`, `v 8925 15380 15710`; `eof_cchk.py 8925,15777 8925,15825`; `px.py row 15800 8906 8944 2 metal` (edges x 8914 and x 8936) |
| the step back, y 15915 | west onto x 8882 (edges y 15904 and 15925); south of it on x 8925 no metal for 116 px, then another net's short metal between two pads (8925,16043) and (8925,16260) (the enable rows of the upper latch copy, by their places) | `r18_j1.png`; `tl5_tracks.py h 15915 8870 8935`, `v 8925 15915 16300` |
| metal x 8882, y 15915-16625 | 710 px, bars of 8-10 px at the poly rows it crosses, no hole | `tl5_tracks.py v 8882 15905 16640`; `px.py row 16300 8866 8900 2 metal` |
| **the pad (8882,16648)** | in the run of the metal: ring north (y 16625-16645) and south (y 16652-16669), bright centre x 8877-8886 in both chips, a green hole x 8874-8886, y 16646-16658 in the clean shot, pits; the pad's poly (x 8866-8898, y 16634-16665) is the east end of a row y 16640-16658 that runs west under the track x 8838 (no ring, red minus green 46) and in the open to the gate column; field east of the pad (green in the clean shot and the chip-2 stripped shot) | `r18_p1.png` (2.4x, three shots); `textmap.py 8850 16622 8930 16676 3 --acid`; `eof_cchk.py 8882,16648 8838,16648` (-8, centres 192/200); `px.py row 16648 8796 8866 5 acid1b,metal`; overlay `r18_ov2.png` |
| metal x 8882, y 16669-16844 | over three rows (y 16685-16700, the clear row's step y 16770-16790, y 16812-16830): bars, no ring, red minus green 47-50 | `tl5_tracks.py v 8882 16590 16920`; `eof_cchk.py 8882,16692 8882,16780 8882,16821` |
| **the pad (8882,16867)** | the same 219 px lower: ring y 16844-16861 and y 16871-16886, bright centre, hole x 8874-8889, y 16863-16872; the pad's poly (x 8866-8898, y 16851-16880) the east end of a row y 16855-16874 west under the track x 8838. Two things beside it are read as nothing (Ambiguities 64, 65): reddish patches east of the pad in chip 1's clean shot only, and chip 1's metal missing on the track x 8838 where it crosses this row | `r18_p1.png`, `r18_p2.png` (6x, chip-2 metal and stripped, clean); `textmap.py 8850 16836 8960 16898 3 --acid`; `eof_cchk.py 8882,16867 8838,16866` (-13, centres 182/204); `tl5_tracks.py v 8838 16600 16920` |
| metal x 8882, y 16886-17649 | 760 px, bars of 8-11 px only, no hole | `tl5_tracks.py v 8882 16860 17300`, `v 8882 17290 17665`; `follow.py 8882 16900 S --gap 16`; `px.py row 17300 8866 8900 2 metal` |
| the corner (8882,17649) | an L: west; no metal south of it for 19 px (then other features) and none east of x 8890 | `textmap.py 8860 17630 8905 17672 3`; `tl5_tracks.py v 8882 17650 17760` |
| metal y 17649, x 8600-8882 | 280 px, no break, no hole. **It lies on another net's poly row for its whole length** (Ambiguity 63) | `tl5_tracks.py h 17649 8585 8895`; `r18_c1.png` (3.6x, three shots); `px.py col 8750 17624 17672 3 acid1b,acid,metal` (bright y 17645-17654) |
| the corner (8600,17649) | an L: south. No ring and no hole at the corner; the poly beneath turns south 20 px further west (x 8572-8588, in the open between the rail and this metal) | `textmap.py 8578 17632 8622 17672 3`, `8545 17626 8632 17672 3 --acid`; `r18_c2.png` (5.5x, four shots); `tl5_tracks.py h 17649 8540 8600` |
| metal x 8600, y 17649-17890 | 16 px wide (edges x 8588 and x 8611), over four poly rows (y 17736 `rst_a`'s of piece `isrc4`, y 17780, 17822, 17862): bars, no ring; chip 1's metal is dim over the rows y 17736 and y 17822 (chip 2 whole) | `tl5_tracks.py v 8598 17640 17930`; `eof_cchk.py 8598,17736 8598,17780 8598,17822 8598,17862` (37, 42, 21, 34); `textmap.py 8574 17806 8626 17842 3` |
| **the pad (8598,17908)** | ring and bright centre in both chips, a green hole x 8589-8604, y 17903-17915, pits. Three things on it: the metal from the north (dark for 17 px, y 17887-17904, before the centre), a metal east (dark for 18 px, x 8605-8623), a poly west. Neither metal has another end here, and the two dark stretches are alike: both on the pad (trap 16 (b)) | `r18_p3.png` (5x, both metal shots and the clean shot); `r18_s4.png` (2x); `textmap.py 8568 17876 8640 17940 3 --acid`; `eof_cchk.py 8598,17908` (-18, centres 212/166); `tl5_tracks.py h 17908 8560 8700` |
| metal y 17910, x 8598-9596 | 1,000 px east, 16 px wide (edges y 17899 and y 17921), over field and over two vertical polys, x 8743-8766 and `rst_a`'s x 8961-8980 (piece `isrc`): edge bars only, no ring, no round hole (a 3 px green line along x 8759-8762 under the first, not a hole). The follower's two contact candidates (9472,17911), (9547,17910) are nothing: no ring, red minus green 27 and 10 at the metal's south edge | `follow.py 8650 17908 E --gap 16` (end (9600,17908)); `tl5_tracks.py h 17908 8620 9625`; `textmap.py 8728 17890 8786 17928 3`, `8948 17892 8996 17926 3`; `eof_cchk.py 8754,17908 8970,17908 9472,17911 9547,17910`; `px.py col 9000` / `col 9300 17892 17926 2 metal`; `r18_e1.png` |
| **the pad (9596,17909)** | the metal's east end: ring and bright centre x 9591-9600 in both chips, a hole in the clean shot (x 9591-9603, y 17911-17916), pits; pad x 9582-9616, y 17895-17922; no metal east of it for 40 px and none south. **A second metal ends on it from the north** (review round 22): the track x 9589-9604, metal from y 17602 down to the ring (dark y 17886-17903, 17 px, as on the pad (8598,17908)), row bars only on the way | `r18_e1.png` (3.4x, four shots); `textmap.py 9570 17884 9632 17934 3 --acid`; `eof_cchk.py 9595,17905` (-5, centres 215/152); `tl5_tracks.py h 17908 9590 10240`, `v 9596 17580 17935`, `v 9596 17910 17990`; `review-22/hop_pads5.png` (5x, both metal shots) |
| the poly hop, x 9612-9756 | row y 17899-17914: salmon (200-218 / 137-168) under the wide vertical metal x 9641-9685, dark red-brown in the clean shot and orange in the chip-2 metal shot (124-128 / 100 / 46-53) in the open gap at x 9712, with field either side (y 17897, y 17918). No hole and no ring under either vertical metal (red minus green 35 and 35). The dark specks on it at x 9620-9630 and x 9700 lie in the gaps between the metals, with a green ring in the same gap at the row above (trap 2); nothing there in the chip-2 shots | `r18_e1.png`; `px.py col 9663 17888 17930 3 acid1b,acid`, `col 9712 17888 17930 3 acid1b,acid,metal`; `eof_cchk.py 9663,17908 9729,17908`; overlay `r18_ov3.png` (4x) |
| **the pad (9769,17910)** and the metal east | ring and bright centre in both chips (x 9762-9771), hole x 9762-9777, y 17911-17916; pad x 9752-9790, y 17895-17921. **A second metal ends on it from the north** (review round 22): the track x 9762-9778, metal from y 17646 down to the ring (dark y 17886-17903), none south of the pad (`tl5_tracks.py v 9769 17620 17935`; `review-22/hop_pads5.png`). Its metal east: unbroken from x 9793 to x 10240 (bars of 8-10 px at x 10059-10090 and x 10210-10219, the polys beneath: the last is `bd1_n2`'s corner, piece `n2w`, no contact as read in run 8), onto `trunks`' `M 10320,17908 x10230 w=16` | `r18_e1.png`; `textmap.py 9738 17884 9806 17934 3 --acid`; `eof_cchk.py 9770,17910 10074,17910` (-2; 33); `tl5_tracks.py h 17908 9590 10240`; `px.py col 9820` / `col 10000 17892 17926 2 metal` |

The branch west of the pad (8598,17908), drawn as far as the next pad:

| Stretch | What | Evidence |
|---|---|---|
| poly row y 17899-17915, x 8438-8588 | from the pad west under the VSS rail (x 8505-8565; salmon, no ring, red minus green 39) and a thin metal (x 8455-8475; 38) to a pad; the dark specks at x 8480-8500 are the gap between those two metals (trap 2; orange poly with two edge lines there in chip 1's metal shot) | `r18_w2.png` (3.4x, four shots), `r18_p3.png` (5x); `px.py row 17906 8440 8600 6 acid1b,acid`; `eof_cchk.py 8534,17908 8468,17908` |
| **the pad (8424,17908)** | ring and bright centre (x 8420-8429) in both chips, a hole in the clean shot, pits; pad x 8405-8442, y 17893-17925. On it: (1) a metal from the north, x 8418-8430, which ends here (ring y 17886-17902; no metal south of the pad); (2) the poly goes on west. **The metal along y 17901-17915 west of the pad is not on it** (review round 22; Ambiguity 66): it ends at x 8390, and the 10 px between its end and the pad's ring (x 8398-8406) are open poly, not dim metal (151-152 / 104-122 / 51-54 in chip 2, 132-146 / 59-80 / 43-45 in chip 1; the metal beside it is 187-203 / 152-174 / 64-81), with the chip-2 stripped shot's pale ghost ending at x 8388; the metal's end turns north toward a pad with a contact at about (8382,17862) of the track x 8382 | `r18_p3.png`, `r18_w2.png`, `r18_w3.png` (4x, chip-1 metal, clean, chip-2 stripped); `textmap.py 8384 17884 8450 17932 3`; `eof_cchk.py 8424,17908` (-28, centres 196/181); `tl5_tracks.py v 8424 17700 17935`, `h 17908 8040 8440`; `px.py row 17908 8376 8424 3 metal,metal1,acid`, `col 8384 17850 17912 4 metal,metal1,acid`; `review-22/p8424_ctx.png` (both metal shots) |

Not followed (the follower's readings, unchecked). From the pad (8424,17908): the metal north runs to a corner
(8422,17690), west to (8142,17687), north to (8146,17383), east to (8230,17373) and north on the bundle's track
x 8229 to an end at (8227,17019); the poly west runs to x 8312, where it turns north into what looks like a pad
with a contact at about (8312,17862) (`r18_w3.png`); from x 8390 west it lies under the other net's metal
(which the follower takes west to (8056,17917), south and west to (7553,17950)): whether that metal makes
contact with it anywhere on those 80 px was not read (trap 13). From the pad (9596,17909): the metal north
runs to (9593,17608), west along y 17606 to (9315,17604) and north on x 9315 to an end (9315,16818). From the
pad (9769,17910): north to (9777,17650), east to (10053,17646), north to (10047,17346), west to (9965,17326)
and north on x 9965 to an end (9964,16950).

**The gate rows of the two pads** (believed, not traced). `tl1`'s cells `tl1_ua` and `tl1_ub` have their enable
on two rows, y 4492-4510 (gate 2 of the upper unit's stack) and y 4708-4728 (gate 1 of the lower unit's), and
`findcell` placed a mirrored copy of both cells at +12146 in y (the table at the end of piece `isrc4`: 0.72 and
0.67), which puts those rows at y 16647 and y 16864: the two pads' rows, at 16649 and 16865. In `bc2`'s two
copies the enable rows are joined by one vertical metal in the same way. The copy's clear row is `rst_a`'s row
of the tap pad (8966,16737). The copy is not placed or overlaid, so that these rows are gates, and of what,
is not in the trace.

### Pieces `lat16` and `inv16`: the latch that `ck_out` enables, and the inverter on its data (traced; the ties uncertain)

```
eof_w16607 = NOT eof_w16388                                        inv16: the inverter between the two latch copies
eof_w16507 = NOT eof_w16607                                        the cell's own inverter
eof_w16693 = NOT((ck_out AND eof_w16607) OR eof_w16823)            upper unit (tl1_ua)
eof_w16823 = NOT((ck_out AND eof_w16507) OR eof_w16693 OR rst_a)   lower unit (tl1_ub)
```

From the full extraction (thirteen transistors, `t369`-`t381` of the package's list). The inverter: load
(8609,16395) 28/92, gate and source on `eof_w16607`; pull-down (8721,16390) 48/20, gate `eof_w16388`. The cell's
inverter: load (8598,16572) 28/53; pull-down (8684,16568) 37/21, gate `eof_w16607`. Upper unit: stack 72/18
(gate `eof_w16607`) over 72/18 (gate `ck_out`); third pull-down (8715,16721) 42/20, gate `eof_w16823`; load
26/50. Lower unit: stack 83/19 (gate `ck_out`) over 81/21 (gate `eof_w16507`); third pull-down (8624,16901)
43/22, gate `eof_w16693`; clear (8776,16780) 35/18, gate `rst_a`; load 26/50. `tools/unsure.py --equations
eof_w16`: `eof_w16507` firm; the other three depend on uncertain items (the cells' two load ties and the
inverter's tie).

What it says (traced, but for the ties): **a transparent latch, open while `ck_out` is high (CLK low)**.
While open, `eof_w16693` = NOT `eof_w16607` = `eof_w16388` and `eof_w16823` = `eof_w16607` = NOT `eof_w16388`;
when `ck_out` falls both hold. `rst_a` high (the reset) forces `eof_w16823` low, and with it `eof_w16693`
high unless the latch is open with `eof_w16607` high. It is the fifth latch of `tl1`'s build that `rst_a` is
seen to clear and the first whose enable is `ck_out` (the top-left logic's third latch, `tl1_w6022`, is
enabled by `ck_out` too). Believed, not traced: what `eof_w16388` is and where the two outputs go; with the
clock latch V/W (which `ck_out` also gates) it belongs to a group clocked on CLK low.

**The latch** is the lower of the two mirrored copies of `tl1`'s units that `findcell` found under column
B's rail (run 9: the table at the end of piece `isrc4`). `findcell.py 2532 4350 2838 4600 --region
8450,16400:9050,17000 --layer acid1b --cell tl1_ua`: `@inst tl1_ua 5976,12146 mx=2685`, 0.72 (metal shot:
5972,12145, 0.67); `tl1_ub` (2535 4347 2838 4797): `@inst tl1_ub 5973,12146 mx=2686.5`, 0.67. Both give the
same mapping, x' = 11346 - x, y' = y + 12146. Overlays `s19_b.png`, `s19_c.png` (2.7x, clean and chip-2
metal), `s19_ov1.png`, `s19_ov2.png` (2.2x, clean), `s19_ov3.png` (1.9x, metal): every outline on its feature.
What the copy has of its own, and what was looked at round its pads (R45, trap 32):

| Item | What | Evidence |
|---|---|---|
| rails | VSS x 8686-8731 over the pull-downs' boxes, VCC x 8510-8560 over the loads' boxes. The VCC rail is `bc1`'s R2 (`M 8534,14990 y16300 w=48`) running on south; the VSS rail is the one drawn over V and W, continuous down to the latch (contacts and edge bars only) | `s19_rails.png` (0.75x), `s19_gap.png` (1.4x, both metal shots and the clean shot); `tl5_tracks.py v 8712 15460 17000 --half 12`, `v 8534 15330 17000 --half 12` (no stretch over 31 px without metal in both, each at a contact's ring) |
| VSS boxes | the cells' two (contacts (8726,16566), (8718,16756)) and the copy's own at the foot of the lower stack, x 8695-8745, y 16922-16975, contact (8713,16950); the lower unit's third pull-down's source strip y 16928-16942 runs into it from the west | `eof_cchk.py 8726,16566 8718,16756 8715,16950` (holes 5, 11, -8; centres 227/237, 236/208, 240/197); `s19_i.png` (3.2x, clean and metal) |
| VCC contacts | the cell's (8543,16593) and a long one on the two loads' box, (8537,16745). The diffusion under the rail is taller than the cells' boxes (y 16497-16622 and y 16656-16925), with a second long contact (8535,16860): drawn since review round 24 (no poly crosses it; the upper piece's top edge at y 16510 and a further contact (8532,16537): round 25) | `eof_cchk.py 8543,16593 8537,16745 8535,16860` (6, -9, 5; 208/223, 223/230, 224/217; the last two long north-south); `railprof.py 8514 8556 16480 16960` |
| thin metal x 8588-8600 | from the upper unit's plate (contact (8594,16648): hole 1, ring, bright centre) to the pad of the lower unit's third pull-down (contact (8594,16846): ring and bright centre in both chips, no green hole in the clean shot: Ambiguity 68); it ends on both | `tl5_tracks.py v 8594 16620 16880`; `textmap.py 8570 16826 8624 16874 3`; `px.py pt 8594,16846 8594,16648 acid,acid1b` |
| the top pad (the cell's inverter's output) | contact at (8776,16511) (bright centre x 8771-8780 in a dark ring in both chips, green hole in the clean shot), 8 px west of the instance's; its thin metal leaves south only (x 8765-8777, centre 8771 against the instance's 8781) and ends on the lower gate's pad (contact about (8785,16912)); open ground north and east of the pad, no poly leaving it | `textmap.py 8750 16478 8822 16540 3 --acid`; `eof_mrun.py row 16540 / 16720 / 16800` (8770-8772); `eof_rows.py col 8776 16440 16500`, `row 16507 8795 8830` (none); `eof_cchk.py 8791,16913` (-28, 186/192); `eof_rows.py col 8785 16925 17000`, `row 16912 8800 8850` (nothing leaves the lower pad) |

The rows east of the cells (the cells' rows end at x 8806; all `eof`'s):

| Row | What | Evidence |
|---|---|---|
| data, y 16598-16616 | east to the track x 8838, where it is one poly with a column under the track (piece `inv16`) | `s19_b.png`, `s19_d.png` (3x, four shots) |
| enable, y 16640-16658 and y 16855-16874 | onto `ck_out`'s pads (8882,16648), (8882,16867) (piece `in350`; the stubs drawn then to x 8806 now overlap the cells' rows) | `s19_b.png`, `s19_c.png`, `s19_ov2.png` |
| upper node `eof_w16693`, y 16683-16702 | from the cell's node box east under the tracks x 8838, 8882 (`ck_out`), 8925, 8968 (`rst_a`) with no contact, to **a pad with a contact (9012,16693)** (pad x 8975-9030, y 16675-16706; ring and bright centre in both chips, green hole); the pad's metal leaves south on x 9006-9018 (nothing north or east of the pad) and runs to (9011,17088) by the follower; drawn to y 16850 | `s19_g.png` (2.45x, four shots), `s19_h.png` (4x, four shots); `eof_cchk.py 8838,16693 8882,16693 8925,16693 8968,16693` (47-50: no hole); `eof_cchk.py 9008,16691` (-22, 221/208); `follow.py 9008 16730 S --gap 16`, `N`; `eof_rows.py col 9012 16640 16680`, `row 16690 9028 9060` (none) |
| clear, y 16771-16789 | east under the tracks x 8838, 8882 (no contact) to x 8910, north on x 8893-8910, east along y 16728-16746 onto piece `isrc`'s stub of the tap pad (8966,16737): **the clear is `rst_a`** | `s19_g.png`, `s19_ov2.png`; `eof_rows.py row 16758 8870 8940` (8896-8909); `eof_cchk.py 8838,16780 8882,16780` (45, 50) |
| lower node `eof_w16823`, y 16813-16832 | from the cell's node box east under the same four tracks to x 9022, north on x 9004-9022 **under the upper node's metal** for 100 px (Ambiguity 69: no contact), east along y 16724-16745; seen to x 9067, where it turns north into a structure at x 9058-9100, y 16665-16715 (a square ring with a dim centre at about (9080,16688) between the tracks x 9056 and x 9099: not read). Drawn to x 9062 (port). **A branch** (review round 24): under the track x 8925 the row is one poly with a column x 8917-8935 that runs south to y 17003 and west along y 16986-17003, under the tracks x 8882 (`ck_out`) and x 8838 with no contact, to the rail, where it is a gate (y 16988-17010 under the rail, between the latch's foot box and a diffusion y 17011-17043) of the unit south of the latch, which is not drawn; drawn to x 8760 (port) | `px.py col 8926 16800 17010 6 metal,acid1b,acid` (salmon without a break from y 16818 to y 16998, pink north of the row; the metal bright through y 16832, where the track x 8968 has the row's edge bar); `tl5_tracks.py v 8926 16790 17020` (no hole); `eof_rows.py col 8905 / 8860 / 8780 / 8760 16960 17030` (the leg at y 16988-17003); `railprof.py 8702 8738 16900 17060`; `eof_cchk.py 8882,16994 8838,16994` (47, 46); `s19_r1.png` (2.9x, clean and chip-2 stripped), `review-24/c1.png`. Also: `s19_g.png`, `s19_h.png`; `textmap.py 8988 16705 9040 16845 3`, `9040 16640 9112 16760 3 --acid`; `eof_rows.py row 16780 8990 9040` (9007-9019), `col 9045 16700 16770` (16730-16748); `eof_cchk.py 8838,16823 8882,16823 8925,16823 8968,16823` (7, 47, 45, 50: the first is chip 1's damaged track, Ambiguity 65) |

**The inverter** (piece `inv16`; x 8512-8800, y 16317-16465) stands between the two latch copies. It is the
build of U4 (`eof_dinv`, itself `tl5_inv`) mirrored left to right, with the load's tie below the strip
instead of above; `findcell` gives the cell only 0.55 (`tl5_inv`, 4951 4786 5213 4912) and no hit for
`eof_dinv`, so it is drawn by hand:

| Part | What | Evidence |
|---|---|---|
| under the rail | VSS box y 16317-16381 with a contact (8717,16349), the gate y 16382-16403, the node y 16404-16436 (x 8697-8745). The box is also the foot of the upper latch copy's stack (its lower gate is at y 16290-16316; that copy is not drawn) | `railprof.py 8692 8732 16290 16500`; `eof_cchk.py 8715,16345` (2; 159/198); `s19_e.png` (3x, clean and metal) |
| the gate row, y 16380-16400 | from **a pad with a contact (9010,16388)** (pad x 8995-9027, y 16372-16402; ring and bright centre in both chips, green hole, pits in the chip-2 stripped shot) west under the tracks x 8968 (`rst_a`), 8925, 8882 (`ck_out`), 8838 with no contact, in the open (orange in both chip-2 shots), under the rail, to its end at about x 8680 under the rail's west margin. The pad's metal comes from the north on x 9004-9018 and ends on the pad; nothing leaves the pad south or east | `s19_m.png` (4x, four shots), `s19_j.png` (5x, four shots); `eof_cchk.py 9012,16390 8968,16389 8925,16389 8882,16389 8838,16389` (-7; 50, 42, 43, 47); `follow.py 9011 16350 N --gap 16` (end (9010,16082)); `eof_rows.py col 9010 16400 16440`, `row 16388 9026 9060`; `px.py row 16389 8740 8830 9 metal,metal1,acid` |
| the output | the node's strip leaves the rail east at y 16422-16434 (x 8738-8768; `px.py col 8755 16412 16446 3 metal,acid`) to a buried-contact box (interior x 8779-8793, y 16421-16442, heavy outline all round), in which the output poly ends from the east; that poly runs east along y 16421-16443 to the track x 8838 and south under it on x 8826-8847 for 195 px (salmon under the metal in the clean shot, no ring and no hole on the track) into the latch's data row. The clean shot is unreadable in the gap east of the rail (trap 28); the strip, the box and the two polys are read in the chip-2 shots and chip 1's metal shot (Ambiguity 67) | `s19_j.png`, `s19_k.png` (7x, chip-2 metal and stripped), `s19_d.png`; `px.py row 16429 8736 8830 3 metal,metal1,acid`, `row 16410 8740 8830 6`; `textmap.py 8732 16366 8832 16500 3 --acid`; `tl5_tracks.py rows col 15700 16660 8 8832 8838 8844`, `v 8838 15700 16960` (no hole y 16000-16800); `eof_cchk.py 8838,16432 8838,16500 8838,16607` |
| the load | west of the rail: the node passes below the gate row's end (tan under the rail's margin, x 8676-8697, y 16412-16440), through the open gap between the rail and the thin metal x 8637-8650 (one diffusion 68 px tall there, y 16382-16450), and as a strip y 16381-16409 under the plate (x 8563-8655, y 16372-16432: three bars with two edge lines under the thin metal, at y 16378-16381 and y 16408-16411: `px.py col 8642 16366 16420 3 acid1b`; textured block in the open) to the VCC box (x 8512-8560, y 16380-16440, contact (8533,16412)). The tie is a heavy-outlined box under the thin metal below the plate's east end (x 8618-8660, y 16433-16465): drawn uncertain (Ambiguity 70) | `s19_l.png` (3.4x, clean and chip-2 stripped), `s19_e.png`; `px.py col 8668 16360 16470 4 metal,metal1,acid`, `row 16389 8646 8692 3`, `row 16420 8652 8686 4`; `eof_cchk.py 8537,16410` (4; 202/223); `tl5_tracks.py v 8643 16340 16500` |

### Pieces `lat15`, `cap16` and `w16693`: a second latch in front of the first, and the first latch's two outputs (traced; the ties uncertain)

```
eof_w15900 = NOT eof_w16000                                             the cell's own inverter
eof_w16388 = NOT((eof_w16000 AND eof_w16040) OR eof_w16216)             upper unit (tl1_ua)
eof_w16216 = NOT((eof_w15900 AND eof_w16040) OR eof_w16388 OR rst_a)    lower unit (tl1_ub)
```

From the full extraction (eleven transistors, `t369`-`t375` and `t378`-`t381` of the package's list). The
cell's inverter: load (8598,15965) 28/53; pull-down (8684,15960) 37/21, gate `eof_w16000`. Upper unit: stack
72/18 (gate `eof_w16000`) over 72/18 (gate `eof_w16040`); third pull-down (8715,16114) 42/20, gate
`eof_w16216`; load 26/50. Lower unit: stack 83/19 (gate `eof_w16040`) over 81/21 (gate `eof_w15900`); third
pull-down (8624,16294) 43/22, gate `eof_w16388`; clear (8776,16173) 35/18, gate `rst_a`; load 26/50.
`tools/unsure.py --equations eof_w16` / `eof_w15900`: `eof_w15900` firm; the two latch equations depend on
uncertain items (the cells' two load ties). Pieces `cap16` and `w16693` add no transistor.

What it says (traced, but for the ties): **a transparent latch, open while `eof_w16040` is high**: then
`eof_w16216` = `eof_w16000` and `eof_w16388` = NOT `eof_w16000`; both hold when `eof_w16040` falls; `rst_a`
high (the reset) forces `eof_w16216` low. Its upper node is the input of the inverter `inv16`, so
`eof_w16607` = `eof_w16000` as latched, and that is the data of the latch `lat16`, which is open while
`ck_out` is high: **two latches in series**, the first on `eof_w16040`, the second on `ck_out` (CLK low), with
one clear. The second latch's outputs: `eof_w16823` = the stored value, `eof_w16693` = its inverse.
Believed, not traced: `eof_w16040` is high only while `ck_out` is low, which would make the pair a
flip-flop clocked by CLK (its metal is not followed); the diffusion on `eof_w16823` is a capacitor that
slows that node.

**The latch** is the upper of the two mirrored copies that `findcell` found under column B's rail (run 9;
again in this run: `findcell.py 2532 4350 2838 4600 --min 0.55 --region 8450,15800:9050,16450 --layer acid1b
--cell tl1_ua`: `@inst tl1_ua 5976,11539 mx=2685`, 0.72; `tl1_ub` (2535 4347 2838 4797): `@inst tl1_ub
5973,11539 mx=2686.5`, 0.73): the lower copy moved 607 px north, x' = 11346 - x, y' = y + 11539. Overlays
`r20_u1.png`, `r20_u2.png` (2.7x, clean and chip-2 metal): every outline on its feature. `railprof.py 8692
8732 15860 16330` gives the cell's gates under the rail: y 15991-16003 and 16034-16047 (the upper stack),
16106-16127 (the third pull-down), 16244-16265 and 16288-16316 (the lower stack). What the copy has of its
own, and what was looked at round its pads (R45, trap 32):

| Item | What | Evidence |
|---|---|---|
| rails | VSS x 8686-8731 over the pull-downs' boxes, VCC x 8510-8560 (R2, `bc1`'s `M 8534,14990 y16300`, drawn again) over the loads' boxes, both drawn from y 15870 to y 16300, where run 19's pieces go on | `eof_mrun.py row 15880 / 16200 8480 8760` (8534(45), 8710(40-46) in both chips); `r20_u1.png`, `r20_u2.png`, `r20_u4.png` |
| VSS boxes | the cells' two (contacts (8713,15962), (8717,16150)); the foot of the lower stack is the inverter `inv16`'s box (contact (8717,16349)), drawn in run 19 | `eof_cchk.py 8713,15962 8717,16150` (-30, 0; centres 219/241, 202/175); `r20_u2.png` |
| VCC contacts | as at the lower copy the diffusion under the rail is taller than the cells' boxes (to y 16024, and y 16037-16318), with the cell's contact (8527,15967), one more above it (8532,15930), the long contact of the two loads' box (8537,16138) and a second long one (8535,16253) | `railprof.py 8514 8556 15860 16380`; `eof_cchk.py 8535,15975 8532,15930 8535,16140 8535,16250` (-21, -8, -8, 0; 177/161, 222/210, 221/199, 207/200; the last two long north-south); `r20_u4.png` (2.8x) |
| thin metal x 8588-8600 | from the upper unit's plate (contact (8594,16041)) to the pad of the lower unit's third pull-down (contact (8594,16239)): ring, bright centre and green hole at both | `eof_cchk.py 8594,16041 8594,16239` (-21, -26; 198/218, 171/203); `eof_mrun.py row 16120 / 16200` (8593-8594); `r20_u4.png` |
| the top pad (the cell's inverter's output) | contact (8776,15904); its thin metal leaves south only and ends on the lower gate's pad, whose contact is at (8787,16303), 10 px west of the instance's, as at the lower copy (Ambiguity 71a); open ground north and east of the top pad (the thin metal x 8792 of another net ends 80 px north of it, on the pad (8838,15822)) | `eof_cchk.py 8776,15904 8786,16300` (-47, -28; 209/193, 179/172); `textmap.py 8756 16270 8830 16340 3 --acid`; `r20_d1.png` (2.9x) |

The rows east of the cells (the cells' rows end at x 8806; all `eof`'s):

| Row | What | Evidence |
|---|---|---|
| data `eof_w16000`, y 15991-16009 | east 30 px to **a pad with a contact (8838,16000)** in the run of the track x 8838 (pad x 8820-8856, y 15984-16016); field east of the pad | `r20_u3.png`, `r20_u5.png` (2.5-2.6x, clean and metal); `eof_cchk.py 8838,16000` (-22, 214/202); `eof_mrun.py row 15970 / 16150` (8839 on both sides); `tl5_tracks.py v 8838 15860 16060` |
| enables `eof_w16040`, y 16031-16049 and y 16248-16267 | each east under the tracks x 8838 and x 8882 (`ck_out`) with no contact to **a pad with a contact, (8925,16040) and (8925,16262)**, on one metal x 8919-8931: its north end is the upper pad, and it runs through the lower pad and on south (the follower: to (8925,17694), then west along y 17700 to x 8643; candidates (8926,16552), (8926,16845), (8923,16963) are the bars of rows beneath, round 24 read the track over the lower latch as no contact). Drawn to y 16300 (port) | `r20_u5.png`; `eof_cchk.py 8925,16040 8925,16262` (-22, -27; 209/209, 179/192); `eof_cchk.py 8838,16040 8882,16040 8838,16257 8882,16257` (43, 39, 45, 47: no hole); `tl5_tracks.py v 8925 16020 16320` (no metal y 16020-16038, north of the upper pad; only rings and 8-10 px bars below); `eof_mrun.py row 16020` (no 8925), `row 16230 / 16290` (8925(13)); `follow.py 8925 16300 S --gap 16` |
| upper node `eof_w16388`, y 16076-16095 | east under the tracks x 8838, 8882 (`ck_out`), 8925 (the enable), 8968 (`rst_a`) with no contact to **a pad with a contact (9007,16082)** (pad x 8988-9026, y 16066-16100), the north end of the metal x 9004-9018 that runs south to the pad (9010,16388) of `inv16`'s gate row (nothing under it on the way) | `r20_u5.png`, `r20_s1.png`; `eof_cchk.py 9007,16082` (-34, 229/205); `eof_cchk.py 8838,16086 8882,16086 8925,16086 8968,16086` (43, 42, 35, 44); `tl5_tracks.py v 9011 16060 16400` (no metal y 16060-16081; then whole to the lower pad's ring) |
| clear, y 16164-16182 | east under the tracks x 8838, 8882, 8925 with no contact onto piece `isrc`'s stub of the tap pad (8962,16172): **the clear is `rst_a`** | `r20_u5.png`; `eof_cchk.py 8838,16173 8882,16173 8925,16173` (38, 39, 39) |
| lower node `eof_w16216` | **no row east of the cell**: its row ends at x 8812 with a rounded outline, field beyond (the gap between the tracks x 8838 and x 8882 has only the dark dots of every row gap there) | `r20_u3.png`; `px.py col 8815 / 8860 15980 16282 3 acid1b` (no red band at y 16205-16225) |

**The data track** (piece `lat15`). North of the data pad the track x 8831-8845 runs to y 15868, turns east
to x 8880 and north to **a pad with a contact (8880,15738)** (pad x 8862-8900, y 15722-15755; ring, bright
centre, green hole; `ck_out`'s metal steps round it to the east, piece `in350`). Between the corner and the
pad the metal, 14 px wide, crosses two poly rows of other nets (y 15772-15792 and y 15812-15832) and is dark
for 8-10 px over each of their four edges and nowhere longer (`tl3_thin.py 8874 8888 15745 15885 --thr 176
--min 5`: 9, 8, 8, 10 px, and 14 px at the pad's ring): no pad, no hole (`eof_cchk.py 8880,15782 8880,15822`:
36, 32). The pad's poly row y 15727-15745 runs west in the open (orange in both chip-2 shots, dark red in
the clean shot) to x 8800, where it enters a heavy-outlined box (8762-8795, 15722-15757) at column B's east
edge beside the thin metal x 8792: **not read** (port; by its place the output box of a unit of column B at
y about 15700-15760, which is not drawn). `r20_d1.png` (2.9x), `r20_d2.png` (3.6x, four shots), `r20_g4.png`
(3.3x, overlay). South of the data pad the track runs on (the follower in run 18: to (8838,17306)): port.

**The lower node's diffusion** (piece `cap16`). Run 19 left the lower node's east leg at x 9062, "into a
structure not read". It is this (`r20_a1.png`, 4.6x, four shots; `r20_g2.png`, 5x, overlay):

| Part | What | Evidence |
|---|---|---|
| the leg | the poly y 16724-16745 runs on east under the track x 9056 (no contact: `eof_cchk.py 9056,16735`: 50) into the gap between the tracks x 9056 and x 9099 and turns north, x 9068-9090 (orange in the chip-2 metal shot, blue 42-46) | `px.py row 16735 9024 9100 4 acid1b,acid,metal`; `textmap.py 9046 16596 9112 16750 3 --acid` |
| the box | a diffusion pad x 9056-9102, y 16672-16706 as drawn (in the clean shot green lobes either side of the poly, x 9058-9067 and x 9094-9100, to y 16713), with the box proper at y 16674-16704 (outline lines y 16672-16682 and y 16700-16704 in the chip-2 metal shot, a plain centre between; the poly's colour reaches north to y 16706: review round 26); heavy outline in all four shots, no metal over it (the two tracks pass either side): a buried contact | the same text map; `px.py row 16690 9040 9120 4`; `r20_a1.png` |
| the neck | from the pad north, x 9070-9088, y 16607-16672, to the rectangle. **It is the rectangle's material, not the poly's**: in the gap between two tracks the clean shot shows it dark (65-90/44-64/46-68) like the rectangle's inside in such a gap (83/55/47 at x 8950) and unlike the poly leg in the same gap (92-154/61-119/42-91); the chip-2 metal shot shows it plain (164-170/120/77) like the rectangle there (175/134/82) and unlike the leg (142/101/46, orange); and no edge line crosses it where it meets the rectangle (both metal shots bright at x 9073-9082, y 16605-16608, where the rectangle's bottom edge line is dark on either side). The chip-2 stripped shot does not separate the two (red minus green 27-33 for both) | `px.py col 9079 16590 16750 6 acid1b,acid,metal`, `row 16640 9040 9120 4`, `col 8950 16458 16494 3`, `col 8950 16588 16618 3`; the text map (rows 16605, 16608); Ambiguity 72 |
| the rectangle | diffusion x 8908-9254, y 16477-16607, with a step at its north-east corner (x 9167-9254 up to y 16434): flat tan under the tracks, grey-green in the wide open gaps (x 8985-9040, x 9160-9210), a heavy outline all round. **No gate** (no poly on it: the data poly of piece `inv16` passes 60 px west of it) **and no contact**: the six tracks over it (x 8925, 8968, 9056, 9099, 9142, 9225; `ck_out`'s x 8882 passes 20 px west of its edge) show only the 8-10 px bars of its top and bottom edges. Nothing else joins it: its bottom edge is whole but for the neck; south of its east part the pad (9180,16648) is a metal contact on a poly row of another net, with open field between; the olive block x 9255-9295, y 16430-16545 east of it is the open ground between the track x 9225 and an L of metal (trap 2), absent from the chip-2 shots | `r20_s2.png` (1.5x, clean and chip-2 stripped), `r20_b1.png` (3.1x), `r20_g1.png` (1.65x, overlay); `px.py row 16540 8886 8936 3`, `row 16540 9236 9270 3`, `col 9195 16418 16446 3`, `row 16455 9150 9186 3` (the edges); `tl5_tracks.py v X 16440 16640` for the six tracks; `opendiff.py 8880 16380 9320 17120` |

What it is: a diffusion of about 45,000 px2 on a latch node, with no transistor: **believed a capacitor**
(junction capacitance to the substrate), which slows `eof_w16823`. A second rectangle of the same size
(x 9042-9255, y 16778-16995) lies 170 px south; it is **not** on this latch: its one tie is a neck at its east
edge (y 16920-16936) into a box (9262-9290, 16910-16942) under the track x 9270, where a poly column from the
north ends (`r20_f1.png`, 3.6x, three shots): another net's, in `bc4`'s ground, not drawn.

**The upper node's wire** (piece `w16693`). The metal x 9006-9018 south of the pad (9012,16693) passes
nothing (the lower node's branch column is at x 8917-8935) and **ends on a pad with a contact (9011,17080)**
(pad x 8996-9027, y 17064-17100; ring and bright centre in both chips; the clean shot's hole is dull:
`eof_cchk.py 9012,17080`: -5, 241/206; `tl5_tracks.py v 9011 16840 17200`: no metal from y 17089 to the next
pad's ring at y 17164). The pad's poly goes south 35 px in the open (orange in both chip-2 shots, dark in the
clean shot) and west as a row y 17116-17135 (`px.py col 8926 / 8882 / 8838 / 8800 17100 17225 3 acid1b`:
salmon y 17119-17133) under the tracks x 8968 (`rst_a`), 8925 (`eof_w16040`), 8882 (`ck_out`) and 8838
(`eof_w16000`) with no contact (`eof_cchk.py 8968,17125 8925,17125 8882,17125 8838,17125`: 45, 39, 41, 36)
to x 8800, where it enters the unit south of the latch (port). `r20_c1.png` (3.6x, three shots), `r20_c2.png`
(2.4x), `r20_c3.png` (6x, four shots), `r20_g3.png` (4.2x, overlay). Two more rows enter that unit from the
east, other nets: y 17160-17178 from a pad (9005,17168) whose metal runs south on x 9010, and y 17203-17221
from a pad (9098,17208) on which the track x 9099 from the north ends.

### Pieces `inv17`, `nor17` and `in212`: the two gates on the second latch's outputs (traced; the ties and four metal stretches uncertain)

```
eof_w17040 = NOT eof_w16823                    inv17: an inverter on the lower node
eof_w17168 = NOR(eof_w16693, eof_w17212)       nor17: the upper node and one more input
```

From the full extraction (five transistors, `t389`, `t390` and `t395`-`t397` of the package's list). `inv17`:
pull-down (8721,16996) 48/20, gate `eof_w16823`; load (8609,17002) 28/91. `nor17`: pull-downs (8771,17126)
28/19, gate `eof_w16693`, and (8771,17212) 28/19, gate `eof_w17212`; load (8598,17178) 24/50.
`tools/unsure.py --equations eof_w17`: both equations depend on uncertain items (each unit's load tie).
Piece `in212` adds no transistor.

What it says (traced, but for the ties): with the latch `lat16` holding Q = `eof_w16823` (= `eof_w16000` as
passed through both latches) and its inverse `eof_w16693`, the unit makes **`eof_w17040` = NOT Q** on a thin
metal (a second copy of the inverse, one gate later, on a wire of its own) and **`eof_w17168` = Q AND NOT
`eof_w17212`**. What `eof_w17212` is and where the two outputs go is open, so nothing is said yet about
what the unit is for.

**The inverter** (piece `inv17`). `tools/findcell.py 8512 16317 8800 16465 --region 8450,16940:8900,17300
--layer acid1b` finds `inv16`'s rectangle again at +(0,607) with 0.83 (the other small cells of the
neighbourhood, `tl5_inv`, `eof_dinv`, `tl1_ua`, `tl1_ub`, the inverter U: no hit; `eof_dly` 0.52). `inv16` is
not a cell, so the copy is drawn by hand from its lines moved 607 px south and fitted (`r21_a1.png`, 3x, clean,
metal and stripped; `r21_o1.png`, 3.3x, overlay). As there, the VSS box above the gate is the foot box of
the latch copy north of it (here `lat16`'s, contact (8713,16950)).

| Part | What | Evidence |
|---|---|---|
| gate | y 16986-17006 under the rail: the west end of the lower node's branch row (piece `lat16`: `P 8760,16986:8935,17003`), to x 8684 | `railprof.py 8692 8732 16960 17300`: diffusion to y 16987, gate 16988-17010, diffusion 17011-17043; `px.py col 8712 16978 17050 4 acid1b`: bright salmon y 16988-17004 |
| node, east | a strip y 17024-17039 out of the rail to the pad. **Diffusion, and joined to the pad**: redder than the field south of it in three shots (stripped red minus green 25-28 against 2-14; chip-2 metal 41-44 against 24-28, blue 81-92; chip-1 metal 31-37 against 10-17), and the pad's dark west edge line (x 8765-8769 at y 17054) is absent where the strip arrives (y 17031: in the clean shot no sample under 137 from x 8750 to x 8780; the dark at x 8776-8783 there in the other three shots is the contact's ring: review round 27) | `px.py col 8758 16976 17078 3 acid1b,acid,metal`; `px.py row 17031 / 17054 8744 8800 3 acid1b,acid,metal,metal1` |
| output pad | a diffusion pad x 8772-8814, y 17021-17063, plain tan like the VCC box, with a metal contact: ring and bright centre (8792,17040) in both metal shots (chip-2 red 181-233 at y 17032-17047, a dark ring 40 px across), dark specks at (8785,17036) in the clean shot. `inv16` has a buried contact and a poly here; this pad has **no poly** | `px.py row 17036 8728 8826 3`, `px.py col 8792 17008 17076 3`; `r21_a1.png` |
| load | as `inv16`'s: the node west under the rail's margin, through the open gap (x 8658-8678), a strip y 16988-17016 under the plate (8563-8655, 16974-17039) to the VCC box (contact (8533,17019): `eof_cchk.py`: -13, 217/135) | `r21_a1.png`, `r21_o1.png` |
| tie | the heavy-outlined box (8618-8660, 17040-17072) under the thin metal x 8637-8650 below the plate's east end: uncertain, as `inv16`'s (Ambiguity 70) | `r21_o1.png` |

**The inverter's output wire.** A thin metal, about 10 px wide, leaves the pad south: a diagonal from
(8791,17062) to (8798,17095), then x 8798 to y 17250 and x 8796 below (`eof_mrun.py row ...`: 8799(5) at
y 17090, 17130, 17210; 8799(7) at 17250; 8796(11-12) at 17270, 17370, 17400; 8795(12) at 17430, 17450), to
**a pad with a contact (8792,17561)** (`eof_cchk.py`: -20, 201/222; ring and bright centre in both chips, a
greenish hole in the clean shot; `r21_h1.png`, 4x, three shots). North of the output pad there is no metal
at x 8790 (`r21_a1.png`): the pad is the wire's north end. `tools/follow.py` does not see this metal at all
("no metal at the start point"; trap 19). `tl3_thin.py 8794 8804 17070 17265`, `8790 8802 17260 17500` and
`8786 8800 17480 17560` (`--thr 176 --min 5`) sort its dark stretches:

| y | px | What lies under it |
|---|---|---|
| 17107-17118, 17136-17146, 17221-17232 | 11-12 | the edges of rows 1 and 3 of `nor17` |
| 17148-17205 | 58 | `nor17`'s output box (8765-8802, 17151-17192) and row 2 |
| 17284-17291 | 8 | the row y 17290-17305 of the pad (8838,17298) |
| 17322-17335 and 17347-17364, bright between | 14 + 18 | a heavy-outlined box (8770-8800, 17325-17352) with a pale square centre (`r21_i1.png`, 6x, four shots): the node box of the next unit down |
| 17414-17421, 17441-17447 | 7-8 | edges |
| 17457-17493 | 37 | a box at (8780-8800, 17460-17490), with a poly east to the pad (8838,17472) |
| 17499-17508, 17526-17533 | 8-10 | the edges of a poly end (8778-8805, 17503-17530; salmon in the clean shot, the metal bright over it in both chips: no contact) |
| 17540-17556 | 17 | the ring of the end pad |

Over the three boxes the metal is not shown by either metal shot and is drawn `?M` (trap 27; Ambiguity 76).
The end pad's poly row runs east along y 17551-17569 under the tracks x 8838, 8882 (`ck_out`), 8925
(`eof_w16040`), 8968 (`rst_a`) with no contact (`eof_cchk.py 8838,17560 8882,17560 8925,17560 8968,17560`:
clean red minus green 37-42, no ring) to **a pad with a contact (9008,17560)**: ring and bright centre in
both metal shots, the pad vivid red in the clean shot with no green hole (Ambiguity 77). Its metal runs
south (drawn to y 17610; `follow.py 9008 17600 S --gap 16`: to a corner (9003,17780), west to (8727,17779):
not checked). It is about 10 px wide to y 17250 and 13 below (x 8789-8802: `px.py row 17255 / 17265 / 17280`).

**The NOR** (piece `nor17`; by hand: `r21_b1.png` 3x, `r21_c1.png` 5x three shots, `r21_c2.png` 6x four shots,
`r21_g1.png` 4x three shots, `r21_j1.png` 5x three shots, `r21_e1.png` 3x; overlays `r21_o1.png`, `r21_o2.png`).

| Part | What | Evidence |
|---|---|---|
| VSS box 1 | under the rail, x 8700-8747, y 17074-17111, contact (8722,17092) (`eof_cchk.py`: -9, 195/235); field between it and `inv17`'s node (pink, y 17044-17070) and south of it (its foot edge y 17112-17118) | `px.py col 8722 17060 17300 4 acid1b`; `r21_b1.png` |
| band and column | a diffusion band y 17097-17110 east from the box, out from under the rail (tan up to the margin's edge at x 8738, plain in the chip-2 metal shot from x 8742), into the top of a column x 8757-8785 that runs south to y 17245. The column's edges are the dark lines across rows 1 and 3 at x 8752-8758 and x 8782-8785 in both metal shots; the band and column are diffusion by the same test as `inv17`'s strip (stripped red minus green 15-24, chip-2 metal blue 82-89) | `px.py row 17103 8690 8800 4`, `px.py row 17126 / 17212 8728 8812 3 acid1b,metal,metal1`, `px.py col 8772 17060 17300 4 acid1b,acid,metal` |
| row 1 | `eof_w16693`'s row y 17116-17135 on west of x 8800 over the column to its end at x 8741: a gate 28 wide | the same rows; `r21_c2.png` |
| node | the column between rows 1 and 3 (y 17135-17203): diffusion from y 17146 to y 17194 at x 8760 in the chip-2 stripped shot, with **no poly across it** | `px.py col 8760 17134 17208 3 acid1b,acid,metal,metal1` |
| row 2, the output | y 17160-17178, from the east: it **ends** in a heavy-outlined box (8765-8802, 17151-17192) with a lighter centre x 8776-8792 (outline x 8764-8772, poly from x 8798): a buried contact on the node | `px.py row 17172 8500 8800 4 acid1b,metal`; `r21_c1.png`, `r21_c2.png` |
| row 3 | y 17203-17222 from the east over the column to its end at x 8740: a gate 28 wide | as row 1 |
| VSS box 2 | below row 3 a band y 17231-17245 west into a box under the rail, x 8700-8747, y 17231-17290, with a long contact (8714,17258) (a long oval ring with a bright centre in both metal shots, several pits in the clean shot). The same box is the source of the unit below (gate y 17292-17306, not drawn) | `r21_j1.png`; `textmap.py 8694 17226 8752 17296 3`; `px.py row 17238 8690 8810 4` |
| load | the node's strip west from the column (no edge line at the column's west edge at y 17172), under the rail (y 17163-17181), across the gap and under the thin metal x 8637-8650 and the plate (8573-8623, 17148-17232; the strip y 17166-17190 under it) to the VCC box (8508-8565, 17162-17208; contact (8525,17183)) | `px.py row 17172`, `px.py col 8602 / 8672 17136 17240 4`; `r21_g1.png` |
| tie | a heavy-outlined box (8628-8662, 17196-17238) under the thin metal below the strip, a tab of the plate into it from the west and a tail of the strip from above: uncertain, like every tie of this build (Ambiguity 78) | `r21_g1.png` |

Run 20 saw "three rows over a column" and took all three for inputs. Row 2 is the output: its poly does not
cross the column. It runs east under the thin metal (`inv17`'s output wire, dark there: Ambiguity 76) and
the tracks x 8838, 8882, 8925, 8968 to **a pad with a contact (9007,17170)** (`eof_cchk.py`: -25, 198/183).
The pad's metal runs south on x 9011 over row 3 (no contact: `eof_cchk.py 9010,17212`: 46, no ring) to a
corner (9011,17518), east to (9057,17518) and south on x 9057 (drawn to y 17600; `r21_f1.png`, 2.2x). Beyond
the port the metal **ends on a pad with a contact at about (9055,17647)** (ring and bright centre in both
chips; `textmap.py 8990 17612 9082 17672 4`; found by review round 27), whose poly runs west along y 17636-17656
under `eof_w17040`'s metal x 9011 (bars of the row's edges only, no ring): not drawn. **The
corner passes 10 px north of the ring of `inv17`'s pad (9008,17560) and does not touch it** (trap 16):
between the arm's south edge (y 17527) and the ring (y 17542) both metal shots show bare ground (chip 2: 9,
chip 1: 7 on the text map's scale) and the clean shot open ground (`textmap.py 8984 17494 9040 17600 3
--acid`), and `follow.py 9008 17600 N --gap 16` from the pad's own metal stops on the pad. The x 9057
position is free below y 17265 because the track x 9056 from the north steps east there to x 9104.

The plain outlined "island" x 8575-8625, y 17050-17140 between the two plates is not layout: it is the open
part of the gap between the VCC rail and the thin metal x 8637-8650 (trap 2), and field in the chip-2 shots
(`px.py row 17095 8556 8644 4 acid1b,acid,metal`: stripped red minus green 3-9, chip-2 metal 22-25, as the
field east of the rail). The like island north of U's plate (Not done) is probably the same.

**The second input** (piece `in212`). Row 3's pad (9098,17210) (`eof_cchk.py`: -13, 229/193) is the south
end of the track x 9099 (nothing else leaves the pad: field east of it, the stepped track x 9104 passes
30 px south of its ring; `r21_e1.png`, `r21_o2.png`). The track is straight from there to y 15880
(`tl5_tracks.py v 9099 14700 17200`: between y 15880 and y 17195 the only stretches without metal in both
chips are the 8-11 px bars of the two large diffusions' edges at y 16474-16481, 16602-16610, 16777-16785,
16992-17002, and 47 px at y 16671-16717, where its west part lies over the east edge of the pad of
`eof_w16823`'s buried contact, piece `cap16`: Ambiguity 72, drawn `?M` now; in chip 2 the track keeps its
width there with a bright strip at x 9096 and the rest dim, and chip 1's darkness is a blemish over both
tracks and the box: review round 27). **At y 15870 it is not the
track x 9099 of further north**: sampled every 100 px (`eof_mrun.py row ...`) the line reads as one track
from y 17180 to the bus line y 14742, which turns south at (9097,14745) (`r21_k1.png`, 4.5x); but at
(9097,15870) the metal turns west along y 15858-15882 to (9053,15870) and north to **a pad with a contact
(9053,15822)** (`eof_cchk.py 9052,15822`: -16, 248/194), and the bus's track turns east at (9098,15827),
25 px east of that pad, with bare ground between (`r21_k2.png`, 3.6x; `r21_k3.png`, 5x, three shots;
`eof_mrun.py row 15845 / 15860`: no metal at x 9060-9140; trap 33). The pad's poly row runs west along
y 15812-15832 under the track x 9012 (drawn to x 8990: port). Believed, not read: it is the row that run 20
saw leaving the pad (8838,15822) east, the pad on which the thin metal x 8792 from the pad (8792,14870)
ends.

### Pieces `o168` and `o040`: the two gates' outputs followed (traced; wiring only, no uncertain item)

Traced. The unit south of the latch pair makes `eof_w17040` = NOT `eof_w16823` and `eof_w17168` =
NOR(`eof_w16693`, `eof_w17212`) (pieces `inv17`, `nor17`). Both wires were ports at y 17600.

**`o040`: `eof_w17040` is `bc1_g6_in`.** The stretches, each with what it was read from:

| Stretch | Reading | From |
|---|---|---|
| metal x 9010, y 17560-17780 | from the pad (9008,17560) south; bars of 8 px over the rows y 17636-17656 (`eof_w17168`'s) and y 17660; no hole | `tl5_tracks.py v 9010 17570 17800`; `eof_cchk.py 9010,17690 9010,17736` |
| the corner (9010,17780), metal y 17773-17787 | an L: west; over `rst_a`'s poly column x 8964 (piece `isrc`) with no contact | `follow.py 9008 17600 S --gap 16`; `eof_mrun.py col 8850 17750 17810 8950 8780`; `eof_cchk.py 8964,17780` (39); `r22_g1.png` (3.6x, three shots) |
| the pad (8733,17778) | a contact: ring and bright centre in both metal shots, a hole in the clean shot (-6; 201/205), a pitted box in the chip-2 stripped shot; the metal ends on it | `eof_cchk.py 8733,17778`; `tl5_tracks.py h 17779 8700 9020`; `r22_g1.png` |
| the row y 17768-17786, x 8345-8712 | one poly, under the thin metal x 8643 (another net's, drawn by no one: review round 28; `eof_mrun.py row 17758 8590 8700 17800`: 8643(13-14); `eof_cchk.py 8642,17777`: 44, no ring), the metal x 8600 (`ck_out`, piece `in350`), the rail x 8500-8562 and the tracks x 8470, 8425, 8382: no ring and no hole at any | `eof_rows.py col` at x 8700 ... 8360; `px.py col 8650 17760 17794 2 acid1b,acid`; `eof_cchk.py 8600,17778 8536,17778 8470,17778 8425,17778 8382,17778` (40-47); `tl5_tracks.py h 17778 8345 8730`; `r22_i2.png` (2.65x overlay) |
| the pad (8338,17777) | a contact (-13; 202/211; a pitted box in the chip-2 stripped shot); a metal from the west ends on it | `eof_cchk.py 8337,17776`; `r22_g2.png` (4.2x, three shots) |
| metal y 17777, x 8012-8338, and x 8012, y 17259-17777 | no stretch without metal; an L corner at (8012,17777) | `follow.py 8300 17778 W --gap 16`; `tl5_tracks.py h 17777 8000 8335`, `v 8012 17240 17790` |
| the step at y 17259 | a Z: east from x 8012 to x 8057, then north. `rst_a`'s metal of piece `isrc4` is on x 8057 south of its own step at y 17301: the two metals lie on one track position end to end with 25 px of bare ground between them | `r22_h1.png` (4.2x, four shots); `textmap.py 7994 17236 8080 17270 3` |
| metal x 8057, y 16647-17259 | bars of 9 px only; it crosses the diffusion-coloured area of Ambiguity 32 (y 16630-16780) with no ring. Chip 2's metal is dim at y 16883-16905 (the tool's "chip 2 fails"); chip 1's is whole there and the clean shot's protected strip unbroken (review round 28, `review-28/d16895.png`): continuity there rests on chip 1 | `tl5_tracks.py v 8057 16630 17270` |
| the corner (8057,16647), metal y 16647, the corner (8143,16647) | two Ls: east across the vacant position x 8100, then north; `rst_a`'s metal turns the same way 48 px lower (nested) | `r22_h2.png` (3.3x, four shots); `eof_mrun.py row` at y 16720, 16680, 16640, 16600 |
| metal x 8143, y 16300-16647 | bars of 8-12 px (the rows beneath, `rst_a`'s row y 16294-16312 of piece `isrc4` among them): no hole | `tl5_tracks.py v 8143 16240 16660` |
| `bc1`'s stretch (not drawn here) | `bc1`'s `M 8186,15900 y16260 x8143 y16300` fits: the jog at y 16254-16268 passes 26 px north of `rst_a`'s pad (8185,16303) (Ambiguity 30), and the metal x 8186 ends on a pad with a contact (8186,15910), the west end of the gate row of `bc1`'s inverter 6 | `r22_h3.png` (4.5x, four shots), `r22_h4.png` (3.1x, four shots, every package's trace); `tl5_tracks.py v 8186 15880 16270`; `eof_cchk.py 8186,15910` (-15; 192/168) |

So the extraction prints `bc1_g6_in` = NOT `eof_w16823` and `bc1_g6_out` = NOT `bc1_g6_in` (the second is firm;
the first depends on the load tie of `inv17` and on the three uncertain stretches of its thin metal, Ambiguity
76: the names `eof_w17040` and `bc1_g6_in` meet only through those, so the alias is kept and no rename is
proposed). **Believed**: `bc1_g6_out` is the second latch's lower node buffered by two inverters; where it goes
is `bc1`'s open end (a poly row east of the pad (8229,16107) into column A).

**`o168`: `eof_w17168` to the edge of a gate.**

| Stretch | Reading | From |
|---|---|---|
| the pad (9055,17648) | a contact: ring and bright centre in both metal shots, a pitted box in the chip-2 stripped shot (the clean shot has specks, no clear hole, like the pad (9008,17560): Ambiguity 77); the metal x 9057 ends on it; bare ground south of it | `eof_cchk.py 9055,17647` (1; 172/166); `tl5_tracks.py v 9057 17500 17700`; `textmap.py 9028 17624 9084 17672 3`; `r22_e1.png` (5.5x, four shots) |
| the row y 17638-17656, x 8573-9045 | one poly under the tracks x 9011, 8968, 8925 and, from x 8890 to x 8588, under `ck_out`'s metal y 17649: no ring, no hole (Ambiguity 63) | `eof_rows.py col` at x 9030 ... 8620; `px.py col 8950 17628 17664 2 acid1b`; `eof_cchk.py 9011,17647 8968,17647 8925,17647 8882,17649` (27-35); `r22_a1.png` (2.4x, three shots) |
| the leg x 8573-8588, y 17638-17698 | in the open gap between the rail and the metal x 8600: orange in both metal shots (chip 2: 160/123/57, blue under 75) from y 17640 to y 17696, dark red-brown in the clean shot; bare ground south of y 17700 | `px.py col 8580 17624 17920 4 metal,acid,acid1b`; `r22_a3.png` (5.5x, four shots) |
| the row y 17682-17698, x 8353-8588 | under the rail x 8500-8562 (field north and south of it, no ring: Ambiguity 79), the tracks x 8470, 8425 and `ck_out`'s second metal from x 8426 to x 8355 (Ambiguity 80) | `railprof.py 8508 8548 17300 17960`; `textmap.py 8486 17668 8600 17712 3 --acid`; `px.py row 17690 8440 8600 5 acid1b,acid,metal,metal1`; `eof_cchk.py 8470,17690 8425,17692 8390,17692` (40, 27, 44); `r22_b2.png` (4x, four shots), `r22_b3.png` (4.2x, three shots) |
| the leg x 8353-8371 and the pad (8355,17649) | a contact: a bright centre x 8349-8358 in a dark ring in both chips, a pitted box in the chip-2 stripped shot, a hole in the clean shot (3); a metal from the west ends on it | `textmap.py 8334 17622 8384 17708 3`; `eof_cchk.py 8357,17646`; `r22_b3.png` |
| metal y 17650, x 8186-8355, and x 8186, y 17428-17650 | no break; an L corner at (8186,17650) | `follow.py 8330 17649 W --gap 16`; `eof_mrun.py col 8270 17615 17680 8220`, `row 17600 8000 8260 ...`; `tl5_tracks.py h 17648 8175 8350`, `v 8184 17380 17650` |
| the pad (8185,17428) | a contact (-25; 171/193; a pitted box in the chip-2 stripped shot); the metal ends on it (the horizontal metal 35 px north is another net's, a step of the bundle) | `eof_cchk.py 8184,17428`; `r22_c1.png` (4.2x, three shots) |
| the row y 17419-17440 east of the pad | in the open: orange in chip 2's metal shot, dark red in the clean shot; drawn to x 8245 | `px.py col 8275 17408 17450 2 acid1b,acid,metal`; `eof_rows.py col` at x 8215 ... 8285; `r22_c2.png` (3x, three shots) |

**Seen beyond the port, not drawn** (`r22_c2.png`; `r22_d1.png`, 5.2x, clean; `r22_d2.png`, 2.65x, both metal
shots: chip 1's metal is destroyed over the rail there). The row crosses a dark line x 8254-8258 (Ambiguity 81)
and at x 8303 joins a hairpin under column A's rail x 8315-8362: a left leg x 8303-8322 up to y 17375, a top
bar y 17375-17393 east across a diffusion column (x 8305-8370, tan under the rail; `railprof.py 8340 8380 17300
17560`: gate y 17374-17389, a second gate y 17331-17352 above it, diffusion y 17397-17519 below), and on east
of the rail down x 8372-8395 and east along y 17425-17445 into a dark structure at x 8410-8440, y 17415-17510.
Contact specks at about (8338,17310) and (8340,17480). So **`eof_w17168` is the gate of a transistor of that
unit, in series or side by side with the row y 17331-17352's** (believed; the unit is not read). No known cell
matches (`findcell.py`, clean shot, region 8150,17280:8620,17620: `tl5_inv`, `tl1_ua`, `tl1_ub`, `eof_dinv`,
`eof_dly`, the rectangles of `inv16`, `nor17` and U: 0 hits).

### Piece `g174`: the pull-down column that `eof_w17168` gates (traced; the east side of the unit not drawn)

Run 23, 2026-11-20. The unit lies under column A's rail at x 8222-8500, y 17266-17568, in `bc3`'s ground (free).
No known cell matches it (`findcell`, run 22). It was read from eleven views (`r23_a1.png` to `r23_h2.png`:
1.35x to 7.5x, the four shots) and from text: `tools/railprof.py`, `tools/px.py`, `tools/textmap.py`,
`tools/opendiff.py`, `tools/eof_patch.py`, and three throwaway scripts kept in `cache/scratch/eof/`
(`r23_map.py`, `r23_prof.py`, `r23_rail.py`). Overlay `r23_o1.png` (3x, both stripped shots).

**What is drawn** (three transistors; no uncertain item):

| Item | Geometry | Evidence |
|---|---|---|
| The rail | `bc1`'s R1 (x 8336-8384, `vss`) on south of y 16300: x 8338-8382 to y 17250, x 8316-8362 from y 17240 to its end at y 17568 | `r23_rail.py 8338 8382 16290 17235`: no stretch of 20 px without metal in both chips (one of 12 px, y 16968-16979: an edge beneath). The step: `px.py row 17215` x 8338-8380, `row 17275` x 8318-8360; `px.py col 8350` and `col 8364`, y 17196-17276: dark bars of 6-15 px at different heights in the two columns, bright metal between, in both chips (`r23_f1.png`, 5x). The end: `px.py row 17566`, `row 17580`. `r23_c1.png` (1x, y 16280-17610, three shots). Chip 1's metal is destroyed over the unit (y 17320-17480): there the rail rests on chip 2 and on the clean shot's protected colours |
| The active area | x 8258-8368, y 17266-17560 | under the rail the clean shot shows it tan between the cream polys (`px.py col 8314 / 8340 17262 17566 2 acid1b`; `railprof.py 8318 8360 17240 17600`: gate 17331-17352, diffusion 17353-17373, gate 17374-17388, diffusion 17397-17519, gate 17520-17534, diffusion 17543-17559, field from 17575). West of the rail: the straight edge x 8254-8258 (the dark line of Ambiguity 81) and chip 2's colours (Ambiguity 83) |
| Contacts (8335,17293), (8335,17474) | onto the rail | a ring with a bright centre in chip 2's metal shot, a white pitted patch in the chip-2 stripped shot, specks in the clean shot, at each (`r23_d3.png`, 3.6x, three shots; chip 1's metal is destroyed there). A third contact of the same diffusion, (8348,17245), lies north of what is drawn |
| Row 1, `eof_w17338` | poly y 17331-17351, x 8245-8372 | cream under the rail (`px.py col 8340`: y 17332-17346), orange in chip 2 in the open (`r23_prof.py col 8280`: y 17335-17349; `row 17338`: x 8261-8302 and on west under the track x 8229) |
| The hairpin, `eof_w17168` | row y 17419-17441 to x 8306; left leg x 8305-8323, y 17373-17441; top bar y 17373-17395, x 8305-8372 | **the row and the leg are one poly**: `px.py row 17424 / 17430 / 17436 8286 8326 2 acid,metal,acid1b`: chip 2 has the poly's colour up to the rail's edge (x 8306), the clean shot is cream from x 8310, and no field colour lies between (`r23_h2.png`, 7.5x). The leg and the bar are cream in the clean shot (`px.py row 17384`: x 8306-8366; `row 17410`: x 8306-8318), the same colour over the leg as over the bar (240/170/120 and 237/170/114): the leg lies on the active area too |
| The lower poly, `eof_w17472` | row y 17464-17486, x 8226-8296; east leg x 8274-8296 to y 17543; bottom bar y 17521-17543, x 8274-8372; west leg x 8226-8242 south to y 17560 | chip 2's two shots and both of chip 1's (`r23_e1.png`, 4.8x, four shots): one orange poly, a hook; `r23_prof.py row 17472`: x 8227-8248 and x 8261-8288; `row 17500`: x 8226-8235 and x 8278-8292; `col 8233`: poly from y 17470 to y 17585. The bar under the rail: `px.py row 17531` cream x 8312-8366, `col 8340` y 17526-17540 |

**What the extraction gives** (firm: `tools/unsure.py` lists none of the four new nets):

    t  gate eof_w17338   vss <-> eof_w17362    W/L 110/20
    t  gate eof_w17168   eof_w17362 <-> vss    W/L 156/21
    t  gate eof_w17472   vss <-> eof_w17552 (former name; it is eof_w17362, run 24)    W/L 167/22

No load is drawn, so there is no equation. Each poly seals its node from the ground inside: row 1 crosses the
whole width; the hairpin's row runs west past the active area's edge and its bar east past the other edge, so
the part between row 1 and the hairpin (the band under the rail, y 17352-17372, and the area west of the leg
down to the row) is one node, `eof_w17362`; the lower poly's row likewise runs west past the edge and its bar
east past it, so the band below the bar (y 17544-17560) with the sliver west of the east leg is the other,
the node below the lower bar (former name `eof_w17552`; it is `eof_w17362`, run 24). The ground between the two polys (the inside of the hairpin, the area with the contact
(8335,17474), the band between the two rows) is `vss`. The widths count every stretch of a poly over the active
area and are rough (Ambiguities 83 and 86); the connections do not depend on them.

**What is read and not drawn, east of the rail** (run 23's reading, kept as written; **drawn since run 24, piece `g174e` below, which corrects four of these rows**):

| Feature | Where | Reading |
|---|---|---|
| The active area's east edge | x 8366-8370, y 17266-17560 | under the two right legs, field (the legs' row below). **Between the legs the ground diffusion goes on east** (review round 29; this run first read the slot as field from one row, `px.py row 17457`, which lies on the slot's north flank): the next row |
| The two necks and the slot | necks y 17358-17366 (north) and y 17548-17558 (south), slot y 17454-17464 between the two arms, each x 8370-8400 | three bands about 10 px high, each between two polys, and alike: in chip 2's two shots each has a greenish north flank and a reddish south flank (`px.py col 8380 / 8388 / 8396 17446 17470 1 acid,metal` for the slot; `eof_patch.py 8376 8394 17355 17358 17359 17364` for the north neck: -12.6 / -25.1 and 20.3 / 32.6), so one row or a few rows say nothing. Over the red flank (`eof_patch.py`, red minus green, stripped / metal): slot (8376-8400, 17458-17462) 16.0 / 34.6; north neck 20.3 / 32.6; south neck (8378-8392, 17549-17555) 24.9 / 42.2; the open strip 14.0 / 32.2. **The control**: a band of the same height that is certainly field, between the hairpin's row and the lower row west of the active area's edge (`eof_patch.py 8228 8250 17452 17458`), gives 0.5 / 24.2 on that flank. So all three are diffusion: the two nodes go on east by the necks, **and the ground between the two polys goes on east as a finger between the arms** (clean shot: the tan runs out under the rail's margin at y 17445-17462 with no closing edge, like the necks' mouths: the reviewer's `g1.png`, `e3.png`). Along y 17460 the finger's colour ends at about x 8404-8410, the box's west line. Not drawn: the two nodes and the ground are left at ports on the edge |
| The open diffusion strip | x 8400-8448, y 17315-17555 | bright green in the clean shot (`opendiff.py 8240 17200 8480 17600`: two groups), red minus green 14-17 / 32-33 in chip 2 (`eof_patch.py 8410 8440 17370 17410 17515 17545`), continuous east of the box (`px.py col 8442 17408 17508 3`: no edge line, 152-168/125-151/78-92). Both necks end on it: so **`eof_w17362` and the node below the lower bar (former name `eof_w17552`; it is `eof_w17362`, run 24) are believed one node** |
| The right legs and the arms | upper: x 8372-8398, y 17370-17440, arm y 17420-17448 east; lower: x 8372-8395, y 17462-17540, arm y 17462-17492 east | each bar turns down (up) east of the rail and runs to an arm. The legs lie over field (`eof_patch.py 8378 8390 17380 17412`: 159/138/72 in the chip-2 stripped shot and 125/78/52 in the clean shot, against 172-175 and 157-180 for the same polys over the active area west of the rail and 152-157 and 122-126 over field there); the arms west of the box are bright again (174/146/63; 176/111/73): over active area, **each between the ground finger and the strip: believed two more stretches of the two gates** |
| The box at the arms' ends | x 8410-8437, y 17418-17500 | one heavy outline round both arm ends, the ends dim and plain inside it (`eof_patch.py 8417 8429 17433 17444 17475 17488`: 125/106/57, dimmer than the arms west of it), a pale green spot between them that has the field's colour (`eof_patch.py 8416 8428 17454 17462`: -3.8 / 9.7; `px.py col 8422 17408 17508 3`; `r23_b1.png` 5.5x, `r23_h1.png` 7x). Believed since round 29: the two gates' ends over the field beyond the finger's end, no contact. Ambiguity 85 |
| The load | plate x 8455-8500, y 17355-17445; a hook at its top with a pale-centred box (8460-8478, 17330-17348); tan diffusion x 8500 and on east under the VCC rail, y 17372-17445 | by its place the strip's load: a poly plate between the strip and a diffusion under the VCC rail (`r23_g1.png` 3x, `r23_g2.png` 4.4x). Its length across the plate is about 45 and its width about 75, a strong load (about 1.6) beside pull-downs of 5 to 8. The VCC contact, the tie and the plate's south end are not read |
| Row 1 on east | north on x 8375-8410 to y 17282, east along y 17278-17305 to about x 8476 | the row wraps the strip's north end; its east stretch is bright like a poly over active area (`eof_patch.py 8420 8460 17284 17298`: 173/145/73): believed a second gate of `eof_w17338`, between the strip and what lies north of it (y 17256-17276, not read) |

**Believed, from the above**: the unit is a strong NOR on the strip, `eof_w17362` = NOR(`eof_w17338`, `eof_w17168`,
`eof_w17472`), with pull-downs four to five times its load's strength: a driver stage behind the NOR `nor17`.
The box stood against it (Ambiguity 85) until review round 29 showed the slot to be a ground finger: with the
finger the box is the gates' ends and ties nothing. Where the strip's node leaves the unit is not found.

### Piece `g174e`: the east side of the unit: the gates' east parts, the load, the output (traced)

Run 24, 2026-11-20. Region x 8368-8560, y 17263-17634 (`bc3`'s ground, free). Read from fourteen views
(`r24_a1.png` to `r24_g2.png`: 2.2x to 9x, the four shots), and mostly from text: `tools/px.py`,
`tools/eof_patch.py`, `tools/textmap.py`, `tools/follow.py`, `tools/tl5_tracks.py`, the new `tools/eof_band.py` (the mean colour of a narrow band over all its rows, or
columns, that are not dark: the whole-band test), and one script kept in `cache/scratch/eof/`: `r24_map.py` (a rectangle's red channel as numbers). Overlay `r24_o1.png` (3x,
both stripped shots).

**The narrow bands, classed over whole bands against a control** (trap 38; chip-2 metal shot / chip-2 stripped
shot, red minus green over the band's own rows or columns, the run that is not dark between its two edge lines):

| Band | Rectangle given to the script | Metal | Stripped | Class |
|---|---|---|---|---|
| **Control**: field between the hairpin's row and the lower row, west of the active area's edge | `tools/eof_band.py h c 8230 8250 17440 17466` | +14.0 | -3.4 | field (certain) |
| The slot between the two arms | `tools/eof_band.py h s 8378 8402 17448 17470` | +31.9 | +16.8 | diffusion |
| The north neck | `tools/eof_band.py h n 8374 8394 17350 17376` | +32.2 | +25.5 | diffusion |
| The south neck | `tools/eof_band.py h s 8376 8392 17540 17566` | +39.9 | +24.6 | diffusion |
| The band north of row 1's east stretch | `tools/eof_band.py h b 8396 8462 17258 17284` | +33.9 | +24.0 | diffusion |
| The band between the two rows over the active area west of the rail (Ambiguity 86) | `tools/eof_band.py h a 8264 8298 17440 17466` | +32.0 | +16.9 | diffusion |
| The sliver west of row 1's vertical part | `tools/eof_band.py v w 8368 8390 17288 17318` | +31.2 | +16.8 | diffusion |
| The bridge east of the box | `tools/eof_band.py v b 8434 8454 17425 17495` | +31.6 | +18.6 | diffusion |
| **The pocket between the two arm ends** | `tools/eof_band.py v p 8414 8432 17453 17463` | +3.8 | -7.7 | field |

A narrow band has a green flank on its north and a red one on its south (and, between two vertical lines, red
on the west and green on the east), so a few rows say nothing; the whole band does, and the seven diffusion
bands stand at least 17 units from the control in both shots (metal +31 to +40 against +14; stripped +17 to
+26 against -3), the pocket below it.

**What is drawn** (no uncertain item):

| Item | Geometry | Evidence |
|---|---|---|
| The active area east of the rail | one area with `g174`'s: west of the island to x 8411; north of it x 8376-8452, y 17263-17419; the bridge x 8434-8452; south of it to y 17560; the north-east corner to x 8467, and south of row 1 to a slanting edge from (8468,17306) to (8477,17322) | the table above. No edge closes the area at x 8368: the clean shot's protected tan under the rail runs to x 8370 with no dark line at the slot (`px.py row 17459 8344 8452 2 acid1b`), at the sliver (`row 17300`) and at the rail's step corner, where it runs on to x 8390 (`r24_map.py 8366 17260 8404 17290 2 acid1b`: 190-200 from the rail to x 8390 at y 17264-17274). Edges: north y 17263 (`px.py col 8425 17250 17275 2`), south y 17560 (`col 8425 17540 17580 2`), east x 8450-8452 south of the plate (`row 17520`), x 8467 at the north-east corner (`row 17270`, `row 17292`, `row 17314`) |
| **The field island** | x 8411-8434, y 17419-17498, left out of the diffusion | one dark line x 8408-8414 crosses the slot and both arms (`px.py row 17434`, `row 17459`, `row 17481`, metal and `metal1`: 72/56/5 on the arms, a real crossing); one line x 8430-8436 closes the pocket on the east; the pocket has the field's colour (the table). `r24_c1.png`, `r24_c2.png` (7x, four shots) |
| Row 1 (`eof_w17338`) east of the rail | a stub to x 8413; a vertical part x 8388-8413, y 17282-17351; an east stretch y 17282-17302 to x 8478 | the poly: `px.py row 17315 8380 8430 2` (edge lines x 8384-8388, 8412-8416), `col 8420 17250 17310 2` (y 17284-17300), `row 17292` (bright to x 8462; the active's edge line x 8464-8470 across it; the poly's colour again at x 8472-8476, its end at about x 8478: review round 31). `r24_b1.png`, `r24_b2.png` (4.5x, four shots). North and west of it the ground diffusion (the band and the sliver of the table), south and east the strip: three stretches of one gate |
| The hairpin (`eof_w17168`) east of the rail | the bar on to x 8389; a right leg x 8370-8389, y 17373-17447; an arm y 17425-17447 to x 8424 | `px.py row 17400 8362 8416 2` (poly x 8370-8388, its east edge line x 8388-8394, the strip plain from x 8396); `col 8400 17408 17502 2` (the arm between lines y 17422-17426 and 17450-17454); `row 17434 8396 8450 2` (bright to x 8404, the crossing line, the end to x 8422). No edge line crosses the poly from the bar's end to the arm (`px.py col 8381 17376 17446 2 metal`: lowest red 151; a real crossing of an active edge under this poly dips to 61, `px.py row 17430 8232 8290 2` at x 8254) |
| The lower poly (`eof_w17472`) east of the rail | the bar on to x 8389; a right leg x 8370-8389, y 17468-17543; an arm y 17468-17492 to x 8424 | the same: `px.py row 17515`, `row 17481`, `col 8381 17470 17530 2` (lowest red 162 in metal, 158 in the stripped shot) |
| The load | a poly plate x 8461-8498, y 17360-17447 over a diffusion x 8446-8504, y 17374-17441 | `px.py row 17405 8440 8548 2`, four shots: the strip plain to x 8452, the plate from its west edge line x 8456-8460, in the open (red, textured) to x 8480 and under the VCC rail's margin from there (clean shot 244/172/115: a poly over active area under metal, as 240/170/120 under the VSS rail); the plate's east edge prints through the rail at x 8496-8502; cream diffusion east of it. The active's north and south edge lines (y 17374, y 17442) cross the whole plate (`px.py col 8470`, `col 8492`; `r24_map.py 8476 17364 8502 17384 2`): the channel runs east-west. `r24_d1.png`, `r24_d2.png` (4.5x, four shots) |
| The plate's column and tab | column x 8462-8482 north to y 17334; tab x 8486-8498 north to y 17332 | the column: an orange bar y 17360-17368 between the plate and the box in both metal shots (`px.py col 8470 17318 17376 2`). The tab lies under the rail's west edge; clean shot 227/167/105, which is neither field under metal (203/117/126) nor diffusion under metal (202/179/139) (`px.py col 8491 17322 17462 3 acid1b`) |
| The tie | `B 8458,17330:8482,17354` on a diffusion x 8446-8482, y 17326-17354 | a box x 8456-8482, y 17326-17356 with a heavy frame and a pale centre (8462-8476, 17333-17350) in all four shots, at the column's north end, with the strip on its west and north (`r24_e1.png`, `r24_e2.png`, 9x) |
| The diffusion under the VCC rail | x 8500-8538, y 17375-17450; x 8510-8538 to y 17478; x 8493-8538, y 17476-17542 | the clean shot: cream, one area (`px.py col 8525 17360 17556 4`: no line from y 17376 to y 17540; `col 8508`: a notch y 17442-17474; `row 17410`, `row 17462`, `row 17510`). At y 17450-17475 it also runs on east past x 8558 (not followed) |
| Two contacts onto the rail | (8528,17477); (8509,17513), 18 x 34 | the first: a ring with a bright centre in both metal shots (`textmap.py 8486 17452 8554 17552 3 --acid`; `r24_d2.png`), specks in the clean shot. The second: a bright bar x 8504-8516, y 17494-17527 between dark sides in both metal shots, specks in the clean shot, a pitted white patch in the chip-2 stripped shot (Ambiguity 91) |
| The VCC rail R2 on south | x 8488-8558 from y 17236 to y 17560 (it runs on) | `r23_rail.py 8510 8556 17200 17600`: no stretch without metal in both chips. Its west edge is the dark line x 8484-8488 of both metal shots, which runs from y 17332 to y 17440, north of the active too; the strip x 8488-8497 has metal's colour north of the plate (`px.py col 8492 17322 17462 3 metal`: 199-208/167-174/81-97) and is dim over the plate (trap 30) |
| The output | the plate's tail x 8463-8480 south to a pad x 8455-8485, y 17583-17617; a contact (8467,17603); 30 px of the pad's metal south, 15 wide | the tail over field (clean shot 108/66/46 against 172/101/58 on the plate; `px.py row 17520 8436 8500 2`). The pad: a ring with a bright centre in both metal shots, a peach pad with a round green hole in the clean shot (`px.py col 8471 17540 17630 3`, metal and `acid1b`; `r24_g1.png`, `r24_g2.png`, 5x, four shots). South of the pad the clean shot's protected strip runs on (pink from y 17618) and chip 2's metal is bright again at y 17627 (trap 16: the dark stretch between is 14 px) |

**What the extraction gives** (firm: `tools/unsure.py --equations eof_w17362`):

    eof_w17362 = NOR(eof_w17168, eof_w17338, eof_w17472)
    t  gate eof_w17338   vss <-> eof_w17362    W/L 258/21
    t  gate eof_w17168   vss <-> eof_w17362    W/L 250/21
    t  gate eof_w17472   vss <-> eof_w17362    W/L 261/22
    t  gate eof_w17362   eof_w17362 <-> vcc    W/L  67/37   load

The pull-downs are six to seven times the load's strength, and four times the width of any gate of the latch
column behind them: a driver. **Believed, not traced**: it drives a long line. `tools/follow.py 8467 17640 S
--gap 16` takes the pad's metal 840 px south across the bottom bus field's rows to a corner (8466,18478) and
910 px west to an end at (7552,18472); the metal is thin (`tools/tl5_tracks.py v 8467 17600 17700`: four
stretches of 8-15 px without metal in both chips in the first 100 px, the bars of the rows beneath or breaks:
not read). `cudisp_drv_in`'s label (`pads_out`) is at (7729,18927), 450 px south of that stretch. Nothing of
this is drawn: the next piece.

**Seen in the region, not drawn** (other units'; also under Not done): a diffusion square x 8512-8566,
y 17284-17348 under the VCC rail with a contact at (8530,17312), north of this unit's load (it looks like the
east neighbour's); a pad with a contact at (8403,17603), 64 px west of the output's pad, with a metal from the
west and a poly south: no metal or poly joins it to the output's pad (review round 31, `review-31/h1.png`).

**What run 23 read differently** (its second table, "read and not drawn", above): (1) "the active area's east
edge x 8366-8370": there is none; (2) "the legs lie over field": its patches x 8378-8392 were half edge line
(the legs' east edge line is at x 8388-8394), and the legs' centre line has the arms' colour; the poly's colour
does not class it here at all (Ambiguity 88); (3) "the open strip x 8400-8448 ... continuous east of the box":
east of the box it is 14 px between two edge lines (the bridge of the table); (4) the load's plate is
x 8461-8498 by 87 high with a channel 37 long and 67 wide (W/L 1.8, where run 23 estimated 1.6).

### Piece `o362`: the NOR's output on to the bottom bus field (traced; wiring only, no uncertain item)

Run 25, 2026-11-20. Traced. `eof_w17362` = NOR(`eof_w17338`, `eof_w17168`, `eof_w17472`) (piece `g174e`) left
its unit at the port (8469,17634) on a thin metal. Read mostly from text and from five views (`r25_v1.png`,
`r25_v2.png`: 2.8x, three shots; `r25_end.png`: 3.7x, `r25_w2.png`: 5x, four shots; overlay `r25_w1.png`,
2.5x, four shots). The stretches, each with what it was read from:

| Stretch | Reading | From |
|---|---|---|
| metal x 8468, y 17630-18474 | one thin metal (12-15 px) over the bus field's poly rows; no stretch of 20 px without metal in both chips; stretches of 14-16 px at y 17781-17794, 17848-17861, 18106-18121, 18168-18183 are the edges of rows beneath (the clean shot's pink protected strip is unbroken beside each: trap 27); the rows are plain, about 20 px high, with no pad at the metal (trap 15). One of them is `ck_out`'s poly y 17908 between its pads (8598,17908) and (8424,17908) (piece `in350`) | `follow.py 8467 17640 S --gap 16`; `tl5_tracks.py v 8467 17600 18500 --half 2`; `eof_mrun.py row` at y 17940, 17975, 18060, 18300, 18450 (8468-8470, 12-15 wide); `r25_v1.png`, `r25_v2.png` |
| the crossing at y 17977 | the tool's dip in the clean shot (8 px, red minus green -3): a plain poly row y 17968-17984 through under the metal; the metal keeps its 12 px, no ring in either metal shot, the chip-2 stripped shot uniform poly across it: no contact | `textmap.py 8440 17946 8498 18000 3 --acid` |
| the corner (8468,18474) | an L: west. East of x 8476 and south of y 18485 open ground (green in the clean shot, no metal in either chip) | `tl5_tracks.py h 18473 7500 8490 --half 2` (no metal 8476-8489; clean shot 8486: -48); `r25_v2.png` |
| metal y 18474, x 7581-8455 | no stretch of 8 px without metal in both chips; 13-14 px wide | the same `tl5_tracks.py h`; `eof_mrun.py col 8300 18440 18510 7900 7650` |
| the pad (7556,18473) | a contact: ring (x 7538-7548, 7564-7580) and bright centre (225/203/112, 215/189/100) in both metal shots, a hole in the clean shot's peach pad, a pitted box in the chip-2 stripped shot; the metal ends on it | `px.py row 18473 7430 7600 6 metal,metal1,acid,acid1b`; `r25_end.png` |
| the poly row y 18462-18482, x 7400-7540 | one poly: open and orange in both metal shots at x 7522-7540 (172/109/61; 163/100/59) and x 7406-7460 (162-173/113-124/55-70), under the rail x 7468-7516 between (cream in the clean shot, 193-213/155-176/102-122, no hole; no ring in either metal shot: no contact; the rail joins the wide metal south of y 18515). `trunks` draws the next line north (y 18428) the same way under the same rail | the same `px.py row`; `px.py col 7500 18440 18520 5`; `r25_w1.png` |
| the pad (7384,18473) | a contact: in chip 1's metal shot a ring with a round bright centre (223/202/83); the chip-2 stripped shot a pitted box with a pale centre; the clean shot a pad with a green hole (`tl5_tracks.py`: 13 px, -17). Chip 2's metal shot shows the pad and its ring, with dirt over the centre (150/125/73 at most) | `tl5_tracks.py h 18473 7000 7480 --half 2`; `px.py col 7384 18446 18500 4`; `r25_w2.png` |
| metal west of the pad | 12-13 px wide, in both chips from x 7364 west (clean shot pink under it: no poly beneath); drawn to x 7340, a port | `px.py row 18473 7340 7430 6`; `follow.py 7350 18473 W --gap 16` (to (6318,18471), 1,048 px: not checked) |

**What the extraction gives**: no new join and no new transistor (`tools/sameconn.py 7847ca9` with every trace
file: connections identical). `eof_w17362` now has one open end, the port at (7340,18473).

**Believed, not traced**: by its place the line is the southernmost of the three bus lines that `trunks`'
comment names ("three bus lines (y 18383, 18426, 18470)"); where it goes west of x 7340 is not read.

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

| `rst_ck` | metal | (6098-6112, 6345) | to loads | link E's north end on `tl6`'s metal (6105,6350) |
| `rst_ck` | metal | (6422-6438, 8072) | in | link E's south end on `lc2`'s piece (`rst_ck`, M 6431,8067); the driver (`rst_ck`'s inverter) lies beyond |
| `rst_ck` | metal | (6445, 8165-8179) | to loads | link F's west end on `lc2`'s end (6450,8172) |
| `rst_ck` | metal | (6695, 8360-8374) | in | link F's east end on `trunks`' line S (its end x 6690): the net is `rst_ck` |
| `rcs_x1` | poly | (5097-5117, 6345) | to loads | from `tl5`'s bus line x 5107 |
| `rcs_x1` | metal | (5070-5090, 6905) | in | onto `lc1`'s M_a (`rcs_x1`, gate 2's output) |
| `rst_a` | poly | (5140-5160, 6345) | to loads | from `tl5`'s bus line x 5150 (the clear of four latches) |
| `rst_a` | metal | (5116-5130, 6905) | in | onto `lc1`'s M_b (`rst_a`, gate 5's output) |
| `res_b` | poly | (5182-5202, 6345) | in | from `tl5`'s bus line x 5192 (`trunks`' pad (5190,6065)) |
| `res_b` | metal | (5183-5197, 6905) | to loads | onto `lc1`'s V2 (`res_b`, the NOR's lower input) |
| `lpstb_b` | poly | (5227-5247, 6345) | in | from `tl5`'s bus line x 5237 (`trunks`' pad (5232,6105)) |
| `lpstb_b` | metal | (5229-5243, 6905) | to loads | onto `lc1`'s V3 (`lpstb_b`, the NOR's upper input) |
| `rst_a` | metal | (6450, 8623-8637) | to loads | piece `isrc5` (run 10): the poly south of the pad (5147,6803) is drawn on (it was a port at (5141-5159, 6900) until then) through `lc1`'s diagonal bundle and the crossing field to `lc2`'s metal end (its first through line, `rst_a`: its port (6450,8630)): one net |
| `res_b` | metal | (6450, 8685-8699) | to loads | piece `rl` (run 11): the poly south of the pad (5190,6845) is drawn on (a port at (5196-5210, 6900) until then) to `lc2`'s metal end, its second through line `res_b`: one net |
| `lpstb_b` | metal | (6450, 8749-8763) | to loads | piece `rl`: the same for the poly south of the pad (5237,6803) (a port at (5232-5248, 6872) until then), onto `lc2`'s third through line `lpstb_b`: one net |
| `tl3_w3982` | poly | (5053-5073, 6345) | ? | from `tl5`'s bus line x 5063 |
| `tl3_w3982` | metal | (6465-6477, 8067) | to loads | piece `w5936` (run 11): `tl3_w3982`'s poly is drawn on from (5063,6880) (a port until then); here the net's metal runs onto `lc2`'s metal x 6471 of `tl3_w3982`, latch C's data: one net |
| `lc1_w7928` | poly | (6401-6416, 8067) | in | piece `d3982` (run 12): from `lc2`'s poly `P 6401,8067:6415,8092` (its port `lc1_w7928 P 6408,8067 out`; the poly's label in both files is `lc2_w8083`, an alias of `lc1_w7928` through `lc2`'s uncertain tie): the node of latch D's lower unit, the input of the three inverters that drive `tl3_w3982`. (The port `tl3_w3982` poly (7492, 8417-8439) of run 11 is gone: the box it ended on is U4's output) |
| `vss` | metal | (7552-7598, 8460) | - | piece `d3982`: the gate column's VSS rail on south (it widens at y 8555 into the metal `cdp3` labels `vss`: piece `g7700`) |
| `vcc` | metal | (7722-7776, 8460) | - | piece `d3982`: the wide metal east of the column on south (VCC by the four loads' contacts; not followed to a supply) |

| `tl1_w5936` | poly | (2362-2386, 2506) | in | piece `r5nor`: from `tl1`'s row y 2498-2515; a gate of the NOR |
| `rcs_c1` | poly | (2405-2427, 2506) | in | from `tl1`'s poly (2405-2420,2500); a gate of the NOR |
| `sl_eq_r5_n` | poly | (2493-2515, 2506) | in | from `tl1`'s poly (2493-2508,2500); a gate of the NOR (the net's first load) |
| `tl1_w2637` | poly | (2452-2472, 2506) | out | the NOR's output, onto `tl1`'s poly (2448-2463,2500) |
| `vss` | metal | (2596, 2347-2404) | - | the arm, into the VSS plane (`tl1`'s, not drawn north of y 2500) |
| `vcc` | metal | (2250-2590, 1900) | - | the supply plane over the strap's head, on north, east and west (`padring`) |

| `rst_a` | poly | (10218-10234, 15912) | in or out | piece `isrc`, link G: the pad under the north end of `trunks`' metal x 10225 |
| `rst_a` | metal | (10390-10402, 15083) | to a load | onto `bc2`'s pad (10395,15087): the clear of latch unit a |
| `rst_a` | poly | (9770, 18072-18090) | in or out | link H: from `trunks`' pad (9770,18081) |
| `rst_a` | poly | (8930, 15248-15266) | out | the row west of the end pad (8966,15260): no longer a port, it is row C of piece `vw` (the gate of W's clear, at (8776,15260)) |
| `rst_a` | poly | (7550, 14904-14924) | in | piece `isrc4`: onto the east end of `busl`'s poly row of `rst_a` (its port (7550,14902-14926)); the driver lies beyond it: `lc1`'s gate 5, `rst_a` (piece `isrc5`) |
| `rst_a` | poly | (8326, 16294-16312) | to a load | piece `isrc4`: the row's east end, a gate at x 8283-8311 over an undrawn diffusion column (`bc1` (continue) / `bc3`) |
| `rst_a` | poly | (8326, 16900-16918) | to a load | piece `isrc4`: the tap row's east end, a gate at x 8283-8311 over an undrawn diffusion column (`bc3`) |

| `eof_w7777` | poly | (6450, 7812-7830) | in | row 3, on west into `lc1`'s strip (cluster E's undrawn west half) |
| `tc2_sr_g` | poly | (7400, 7203-7221) | ? | the poly row east of the pad (7313,7215) |
| `tc2_sr_g` | metal | (7262-7274, 7800) | ? | the metal south of the pad (7267,7736) |
| `tc2_r5589` | poly | (7272-7285, 6875) | out | the poly north of the pad (7272,6912), towards a row y ~6862 |
| `vss` | metal | (7552-7598, 7585) | - | column 0's VSS rail, on north (on south: piece `d3982`, to y 8460) |
| `vcc` | metal | (7725-7775, 7720) | - | the wide metal east of the load, on north (on south: piece `d3982`, to y 8460) |

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

| `bd1_n2` | diffusion | (13795, 15712-15736) | in | piece `n2out`: N2 in the gap onto the lower segment of `bd1`'s strip (the net it called `bd1_k`) |
| `vss` | diffusion | (13832, 15638-15652) | - | piece `n2out`: the strip's top segment onto `bd1`'s ground diffusion (`bd1` has the link as `?D`) |
| `bd1_n2` | metal | (13515-13527, 16260) | in | piece `n2w`: from `bd1`'s metal x 13521 (its `bd1_k`, drawn to y 16273) |
| `bd1_n2` | metal | (6705-6718, 15000) | out | piece `n2w`: on north up the left bus field into `busl`'s region; read there by text (piece `n2n`: x 6711 to a corner (6711,13249), east to (6777,13249), north), not drawn; it comes out at the next row's port |
| `lc3_w9947` | poly | (6443-6460, 6390) | ? | piece `ck5`: onto `tc2`'s poly of `lc3_w9947` (its port (6451,6400)), `lc3_w9947`'s line: gates in `tcw` |
| `lc3_w9947` | metal | (6440-6450, 9161-9174) | ? | piece `ck5`: onto `lc2`'s metal end (its fourth through line, `lc3_w9947`: its port (6450,9165)): the ripple counter's clock |
| `rst_c` | poly | (6450, 8911-8936) | in | piece `rc`: from `lc2`'s diagonal poly (its port there), from latch C's clear pad |
| `rst_c` | metal | (6440-6450, 9445-9459) | out | piece `rc`: onto `lc3`'s metal end (its fifth corner-bundle line, `rst_c`: its port (6450,9448-9462)) |
| `bd1_n2` | metal | (6769-6782, 10400) | in | piece `n2n`: the track x 6775 from `busl`'s region (believed `bd1_n2`, from the port (6711,15000): 4,600 px drawn by no one) |
| `bd1_n2` | poly | (5403-5421, 6345) | out | piece `n2n`: onto `tl5`'s poly end (its port `bd1_n2` (5402-5422,6350)): the input of `tl4`'s inverter that makes `rcs_e3` |
| `lc3_w9947` | poly | (7550, 14772-14796) | out | piece `ck6`: onto `busl`'s row end (its port there): the ripple counter's clock, driven by the inverter U at (8733,15000) |
| `bc2_w15000` | metal | (10392, 14993-15007) | in | piece `in172`: gate row 1 of the NOR T; pad A's metal x 10355, its foot onto `bc2`'s output pad (10395,15000) of latch unit a (its port (10385,15000)). (The port `eof_w15172` (9150,14645-14662) of piece `vw` is gone: the row is drawn on to its driver, T) |
| `bc2_w14955` | metal | (10434-10448, 14946) | in | piece `in172`: gate row 3 of the NOR T; pad B's metal x 10441 onto `bc2`'s enable metal of latch unit a (its port (10441,14940)); the net's driver is not found |
| `ck_out` | metal | (10245, 17902-17918) | in | piece `in350`: onto the west end of `trunks`' metal `ck_out #1` (`M 10320,17908 x10230 w=16`): the clock's driver is the clock block's buffer. (The port of piece `vw` at (8873-8889,15465), then under a placeholder name, is gone: the metal is drawn on) |
| `eof_w16000` | poly | (8800, 15727-15745) | in | piece `lat15`: the upper latch's data: the poly row west of the pad (8880,15738), where it enters a heavy-outlined box (8762-8795, 15722-15757) at column B's east edge (not read: by its place a unit's output) |
| `eof_w16000` | metal | (8831-8845, 16030) | ? | piece `lat15`: the track x 8838 on south of the data pad (8838,16000) (the follower: to (8838,17306); not checked) |
| `eof_w16040` | metal | (8919-8931, 16300) | in | piece `lat15`: the upper latch's enable: the metal x 8925 on south of its lower pad (8925,16262) (the follower: to (8925,17694), west along y 17700 to x 8643; not checked) |
| `bc1_g6_in` | metal | (8136-8150, 16292) | out | piece `o040`: `eof_w17040`'s metal x 8143 onto `bc1`'s metal end (8143,16300) of `bc1_g6_in` (`M 8186,15900 y16260 x8143 y16300`; `bc1` has no ports file): the input of `bc1`'s inverter 6. (The ports `eof_w17040` (9001-9015, 17610), `eof_w16823` (8760, 16986-17003) and `eof_w16693` (8800, 17116-17135) are gone: the wires are drawn on) |
| `eof_w17362` | metal | (7340, 18467-18480) | out | piece `o362` (run 25): **the NOR's output**, drawn from the pad (8467,17603) south, west along y 18474, through the pads (7556,18473) and (7384,18473) and the poly between them; the metal goes on west (`tools/follow.py`: to (6318,18471); not checked, not drawn). (The ports of piece `g174` at x 8368-8372 on the rail's east edge, `eof_w17168`, `eof_w17338`, `eof_w17472`, `eof_w17362`, `vss` and the node whose former name was `eof_w17552`, are gone: drawn on) |
| `eof_w17338` | poly | (8245, 17331-17351) | ? | piece `g174`: row 1 where it leaves the active area west, under the track x 8229 (in line with a pad at about (8188,17340): not read) |
| `vcc` | metal | (8488-8558, 17560) | - | piece `g174e`: the VCC rail R2 on south (drawn y 17236-17560, x 8488-8558; it runs on) |
| `eof_w17472` | poly | (8226-8242, 17560) | ? | piece `g174`: the lower poly's west leg on south (poly to y 17585 by `r23_prof.py col 8233`; not followed) |
| `vcc` | diffusion | (8538, 17450-17475) | - | piece `g174e`: the diffusion under the VCC rail runs on east past x 8558 at this height (not followed) |
| `vss` | metal | (8338-8382, 16300) | - | piece `g174`: column A's VSS rail, `bc1`'s R1 (`M 8360,14890 y16300 w=48`) drawn on south to its end at y 17568 |
| `eof_w17212` | poly | (8990, 15812-15832) | in | piece `in212`: the NOR's second input, the poly row west of the pad (9053,15822) (believed: to the pad (8838,15822) of the thin metal x 8792) |
| `vss` | metal | (8686-8732, 15870) and (8686-8732, 17300) | - | pieces `lat15`, `inv16`, `lat16`, `inv17`, `nor17`: column B's VSS rail, drawn over the two latch copies, the inverters and the NOR only; it runs on both ways (north to the piece over V and W) |
| `vcc` | metal | (8510-8560, 15870) and (8510-8560, 17240) | - | pieces `lat15`, `inv16`, `lat16`, `inv17`, `nor17`: R2 (`bc1`'s `M 8534,14990 y16300 w=48`, drawn again from y 15870) and on south of `bc1`'s end, over the VCC boxes of the two latch copies and the inverter |
| `ck_out` | metal | (8418-8430, 17866) | ? | piece `in350`: the metal that ends on the pad (8424,17908) from the north (the follower: to the bundle's track x 8229, end (8227,17019); not checked) |
| `ck_out` | poly | (8392, 17898-17916) | ? | piece `in350`: the poly west of the pad (8424,17908) (seen to x 8312, where it turns north; another net's metal lies on it from x 8390 west) |
| `ck_out` | metal | (9589-9604, 17866) | ? | piece `in350`: the metal that ends on the pad (9596,17909) from the north (the follower: west along y 17606, north on x 9315 to (9315,16818); not checked) |
| `ck_out` | metal | (9762-9778, 17866) | ? | piece `in350`: the metal that ends on the pad (9769,17910) from the north (the follower: east along y 17649, north on x 10050, west, north on x 9965 to (9964,16950); not checked) |
| `bc2_w15607` | metal | (10261-10275, 15520) | in | piece `in390`: `bc2_w15607`'s metal x 10268 onto `bc2`'s metal x 10267 (its port (10267,15515)), from latch unit b's lower node. (The port of piece `vw` at (9002-9020,14790), then under a placeholder name, is gone) |
| `eof_w15300` | poly | (8818-8854, 15440-15472) | out | piece `vw`: W's output at the pad (8836,15456), the south end of its metal x 8838; the pad's poly belongs to the next unit of the column (y 15440-15540: not drawn) |
| `vss` | metal | (8687-8737, 14900) and (8687-8737, 15465) | - | pieces `ck6`, `vw`: column B's VSS rail, drawn over U, V and W only; north it turns west as a band y 14816-14878 to the rail x 8510-8560, south it runs on down the column |
| `vcc` | metal | (8510-8558, 15340) | - | pieces `ck6`, `vw`: R2, `bc1`'s (`M 8534,14990 y16300 w=48`), drawn again over the three VCC boxes so that the package extracts by itself |
| `vss` | metal | (10543-10597, 14590) | - | piece `in172`: the east column's VSS rail, drawn over the NOR T only (y 14590-14790); `bc2`'s rail goes on south, north it runs on |
| `vcc` | metal | (10721-10771, 14590) | - | piece `in172`: the east column's VCC rail, likewise |

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

5. **The staircase of `rst_ck` lies on other nets' poly for four of its stretches** (trap 13):
   on `lc1_w7040`'s row (y 7346, 190 px), on a second row (y 7432, 130 px), on `lc2`'s latch C
   data poly (x 6431, 64 px, `lc2`'s Ambiguity 3) and on the poly of the pad (6558,8127)
   (x 6559, 200 px: since run 11 this poly is drawn, piece `rl`, and is `res_b`; a contact there
   would join `rst_ck` to the RES pin's buffer). At none is there a pad, a ring or a hole in the clean shot (the scans named
   in Logic), and at each corner the metal's end is separate from the neighbouring pad
   ((6341,7345): 20 px of open poly; (6558,8127): 18 px). Each corner shows a dark bar 6-9 px
   long where the row's edge passes under it; a bar that short between two bright stretches is
   an edge underneath, as on every row the same metal crosses. Working assumption: no contact
   at any of them; a contact at the first would join `rst_ck` to latch D's output.
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
13. **`rst_a`'s driver is not on what is drawn.** Three gates are on the net; the four stubs and the
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
26. **The two diffusion links of piece `n2out` cross an open gap 29 px wide between two metals**, where the
    clean shot shows only margin artefacts (trap 2) and the chip-2 stripped shot a fringe. They are drawn
    firm on what both metal shots show of the bare ground (no edge line between the strip and the rail on
    those rows, an extra one where the field island is), on the clean shot's bar-or-strip pattern checked
    against two known crossings and one known field stretch in the same gap, and on red minus green at
    x 13814. Other reading: the strip ends under `bd1_an`'s metal and N2 under the rail's edge line, with
    field between that happens to show no outline of its own; then the latch would have no output and
    `bd1_k` no source, and the plain area's top and bottom edges would not be N2's. Not adopted. The top
    link is the weaker of the two (15 px tall; `bd1` had it as `?D` from a colour map): if it were not
    there, `rst_a`'s transistor would be a stub and the term `rst_a` would drop out of `bd1_n2`.
27. **`bd1_n2`'s poly row y 17905 lies under `ck_out`'s metal for 96 px** (x 10224-10320; `trunks` draws
    the metal to x 10230, and it runs on west to a pad (9770,17910)). No contact: the metal has no ring,
    pad or widening there in either chip and the clean shot no hole (`textmap.py 10190 17884 10340 17926 3`);
    a contact would put the clock on a latch's output. Trap 13's case.
28. **The poly link N under the wide supply bus y 16345-16385** shows yellow and dark-brown patches in the
    clean shot (`g_ov10.png`); so do the two neighbouring tracks' polys under the same bus (`f_k19.png`),
    and both metal shots show the poly's two edge lines unbroken through the bus. Taken as the bus's
    residue, not a break.
29. **Another net's metal lies on `rst_a`'s poly row y 17736 for 290 px** (x 8096-8388; piece `isrc4`, A).
    It is the bundle's track x 8098, which comes down from the north, turns east along the row and turns
    south again at x 8372-8387 (a 6-9 px bar where it crosses the row's edges at each corner). No contact:
    the metal has no ring or widening in either chip and the clean shot no hole along it
    (`tl5_tracks.py h 17736 8062 8700`; `textmap.py 8062 17690 8134 17758 3 --acid`,
    `8336 17713 8426 17758 3 --acid`; `j_w.png`, `j_e.png`, 3.8x, three shots); its west end is 36 px
    from the pad's contact (8053,17735), with open poly between. Trap 13's case. That metal is not drawn
    (`bc3`); if it did make contact, `rst_a` would be on one more track of the bundle.
30. **`bc1`'s metal of `bc1_g6_in` passes 26 px north of the pad (8185,16303)**: it comes down x 8186 and jogs
    west to x 8143 at y 16250-16268. Between its lower edge and the pad's ring lie 8 px of bare ground
    (y 16276-16283: brightness 6-10 of 16 in both chips, metal is 12-14) and the clean shot is open-field green
    there, where it is protected pink under the jog (`textmap.py 8155 16236 8215 16345 3`; `h_j4.png`). The
    pad's only metal is the track from the south. If the jog were on the pad, `bc1_g6_in` would be `rst_a`.
31. **Dark bars across the row y 17736 at the gaps between metals** (x 8390-8400, 8445, 8490, 8570, 8615).
    Each is the clean shot's bar for a gap of about 30 px between two metals (trap 2), and the chip-2 metal
    shot shows open poly (135-160/83-112/38-56) for 12-14 px in each gap between the two metals' edge lines
    (`px.py row 17736 8382 8416 2` and `8432 8462 2` in four shots: the gap at the end of the metal of
    Ambiguity 29 reads like the gap between two of the vertical metals). The row is drawn as one poly.
    Other reading: a break under one of the edge lines (4-6 px that no shot shows); nothing suggests it.
32. **A large diffusion-coloured area under the track bundle, x 8000-8168, y 16600-16780**, where the tracks
    step. The clean shot is one flat tan there, under the tracks and between them (pink and green outside),
    the chip-2 stripped shot is redder than the field around (red minus green 24-38 inside against 4-12
    outside: `px.py pt 8075,16720 8140,16720 8075,16670 8030,16700 8120,16770 8200,16720 8075,16820`), and
    both metal shots show its east edge as a bar at x 8164-8172 across this piece's metal. Not drawn and
    not identified (`bc3`): no poly crosses it and this piece's metal has no contact on it (no ring; the
    track is whole in both chips). A small feature at about (8025,16632) at its north-west corner was not
    read.
33. **The clean shot is olive green under the track x 6558 where it crosses the poly row of the pad
    (6513,7888)** (piece `isrc5`, C; x 6546-6572, y 7884-7890: red minus green under 0, where the same row is
    salmon under the tracks x 6513, 6600 and 6645: `textmap.py 6490 7855 6660 7915 3 --acid`, `6534 7860 6584
    7912 2`; `j_c7886.png`, 4.8x, four shots). Candidate readings: a contact from this net onto that row; or
    no contact, the colour being the clean shot's (trap 15). **Assumed: no contact.** Both metal shots show
    the track there exactly as the neighbouring tracks over the same row (bright for 12 px between the two
    9 px bars of the row's edges, the same width as elsewhere, no ring, no widening), and the green band is
    26 px wide, wider than the 14 px metal: a contact of a thin metal has a pad about 35 px across and a
    round hole. What would settle it: that row's net (if it were `rst_a`, a contact would change nothing).
    **Since run 11 the row is drawn (piece `w5936`) and is not `rst_a`: it is `tl3_w3982`**, latch C's data,
    which has its own source (the box at (7505,8425)). A contact here would short the reset copy to that
    net, so the assumption now carries a connection. Read again for that: `tl5_tracks.py h 7888 6535 7380`
    gives 6558(32,-3) in the clean shot (as long and as low as a contact hole), the only such stretch on
    the row; both metal shots still show no ring, no bright centre and no pad (`j_c7886.png`), and the
    clean shot's colour of this one row drifts from the pad to x 6840 (vivid red at the pad and under the
    track x 6601, olive under x 6558, brown further east, plain salmon from x 6845 on: `k_o5a.png`), which
    the other three shots do not show. **Assumed, as before: no contact** (trap 15).
34. **The metal y 7252-7265 lies on another net's poly row from x 6313 to the corner (6558,7258)** (piece
    `isrc5`, C; trap 13). The poly comes from the north on x 6313-6333 (under the metal of the row y 7213)
    and turns east under this metal at x 6313 (its west edge is a 9-12 px bar across the metal in both
    chips; corrected by review round 12, which read it as a turn, not a square end: `textmap.py 6252 7196
    6350 7284 3`, `review-12/c8_rowend.png`), and runs on east of the corner under the next tracks
    (`j_c6313.png`; `textmap.py 6490 7232 6640 7300 3 --acid`). No contact: the metal
    keeps its width, no ring in either chip, no hole in the clean shot (`tl5_tracks.py h 7257 6200 6550
    --half 2`). The row is not drawn (the crossing field's: `busl`'s northern part).
35. **`eofw`'s metal of `tc2_sr_g` lies on the poly of piece `isrc5`, B, for 150 px** (the arm x 6508-6522,
    y 8259-8411; `eofw` noted the poly under it). No contact: `tl5_tracks.py v 6515 8262 8408 --half 2`
    finds no dark stretch in either chip, the metal keeps its 14 px width, and the clean shot is salmon
    under it throughout. Three specks about 6 px across in the chip-2 stripped shot only ((6516,8355),
    (6520,8382), (6523,8305): red minus green 6-20 on a poly that reads over 60) are taken as dirt or
    fringes under the metal's ghost. If there were a contact, latch D's enable `tc2_sr_g` would be the
    reset.
36. **Chip 1's metal shot has a dark bar across the metal y 7252-7265 at x 6544-6556**, 13 px, just west of
    the corner (6558,7258) (piece `isrc5`, C; found by review round 12). `px.py row 7258 6520 6580 3
    metal,metal1,acid1b`: chip 1 reads 135/87/23, 87/59/30, 69/33/20, 88/43/16, 143/90/35 there (as dark as
    an edge line), chip 2 reads 190-200/137-145/63-69 (whole metal, no edge line), and chip 1's clean shot
    is the same protected salmon through it (199-214/153-161/100-107): the metal was there when chip 1 was
    stripped. Candidate readings: a blemish of chip 1's metal photo; or two metals that meet at the corner.
    **Assumed: one metal** (the two chips are one layout, chip 2 shows no gap, 13 px is under any spacing
    between two metals here, no pad or hole; the sibling corners of the bundle are bright in both chips:
    `review-12/c2_corner.png`, 5.6x, four shots, looked at by the tracer too). If it were a break, `rst_a`
    would not reach the pad (6187,7257) and `rst_a` would have no driver.
37. **The clean shot is dull under `lpstb_b`'s track x 6645 where it crosses the poly row y 7812-7830**
    (piece `rl`; the row is `eofw`'s, `lc1_w7170`; the follower lists (6645,7822) as a contact candidate).
    `textmap.py 6578 7806 6668 7842 3 --acid`: red minus green 0-30 at x 6641-6659, y 7818-7827, where the
    same row reads 50-65 under `res_b`'s track x 6602 beside it; the chip-2 stripped shot is low at
    x 6647-6659 as well. Both metal shots show the track there as on every other row (bright for 12 px
    between the two bars of the row's edges, its width unchanged), `eof_cchk.py 6645,7822` finds no dark
    ring (71-117 round a centre of 218), and the row has no pad. Candidate readings: a contact of
    `lpstb_b` onto `lc1_w7170`'s row; or no contact. **Assumed: no contact** (no ring, no pad: traps 15,
    22). A contact would short the LPSTB pin's buffer to the output of `lc3`'s inverter.
38. **The pad (6513,7889) has no green hole in chip 1's clean shot** (piece `w5936`): it is vivid
    red-orange there (red minus green 100-120 at x 6514-6526, y 7879-7897; `eof_cchk.py`: 19 at its west
    rim), where every other pad of the two pieces has a green or dull hole. The other three shots show a
    contact: a ring with a bright centre in both metal shots (`textmap.py 6484 7858 6546 7926 3 --acid`:
    ring y 7867-7906, centre B-E at y 7885-7894 in chip 2 and chip 1) and a hole in the chip-2 stripped
    shot (red minus green 0-18 at x 6508-6523, y 7888-7894, on a poly that reads over 30; a pitted box in
    `k_L6513.png`). The pad (6558,8125) nearby has a small red spot (red minus green 56-80, about 8 px)
    inside its dull hole in the clean shot (`textmap.py 6543 8110 6575 8140 3`); (6513,8087) has a plain
    dull hole. **Assumed: a contact** (the pad is widened, 40 px, as only a contact pad is; three shots agree;
    the row's colours in the clean shot are abnormal as far as x 6840: Ambiguity 33). If there were none,
    the track x 6514 would pass over the row's end without touching it: the row and its two pads east
    would be a wire with no source, and latch C's data would have no driver either.
39. **Each of the three east-going metals lies on another net's poly** (pieces `rl`, `w5936`; found by
    review round 13; the same as Ambiguity 34 for `rst_a`'s metal y 7257). Four undrawn vertical polys come
    from the north at x 6270-6290, 6313-6333, 6360-6375 and about 6402, and each turns east under one metal
    and runs on east under the tracks: under `tl3_w3982`'s metal y 7303 from x about 6270, under `rst_a`'s
    y 7257 from x 6313, under `res_b`'s y 7216 from x about 6360, under `lpstb_b`'s y 7173 from x about 6402
    (`review-13/f3_under.png`, 3.9x, metal and clean, looked at by the tracer). No pad, ring or hole on any:
    `tl5_tracks.py h 7215 6170 6595`, `h 7174 6212 6636`, `h 7303 6170 6508` give no clean-shot stretch under
    24 and only bars of 8-10 px in both chips (chip 1 alone is dim for 20 px at x 6283-6303 on the metal
    y 7303, over the corner of the L beneath; chip 2 is whole there). **Assumed: no contact at any** (trap
    13). A contact would join the wire to an undrawn net of the crossing field.
40. **A ring-like dark circle in chip 2's metal shot at (5665,7212)**, on the vertical metal x 5660-5675
    where it crosses `res_b`'s row (piece `rl`; found by review round 13). Chip 1's metal shot is bright
    there, the row is unwidened and salmon with no hole in the clean shot (`review-13/b3_5665.png`, 5.8x,
    three shots, looked at by the tracer; `eof_cchk.py 5667,7212`: clean 30, chip 1 centre 207 with dark
    only north and south, the row's two edge bars). **Assumed: a blemish of chip 2's photo, no contact**
    (one chip only, no pad). A contact would tap `res_b` onto that metal (undrawn, `lc1`'s crossing field).
41. **The row y 8030-8050 crosses under twenty-one tracks, five of them on nets it must not touch** (piece
    `d3982`): `rst_ck`'s metal x 6431 (30 px east of the row's corner), `tl3_w3982`'s x 6471 and its thin
    metal x 7396-7408 (the chain's own output: a contact would close the three inverters into a ring),
    `rst_a`'s x 6514, `res_b`'s x 6601, `lpstb_b`'s x 6645. At each the metal shots show the row's two edge
    bars with whole bright metal between, the row keeps its width (no pad), and the clean shot is salmon
    with no hole (`textmap.py 7380 8014 7428 8066 3` for x 7402; `m_w8038.png` 4x and `m_o4.png` 5x for
    x 6431-6600; `tl5_tracks.py h 8040 6420 7414`: every clean-shot stretch under 24 lies in an open gap
    between two tracks, trap 2). Under the track x 7078 chip 2's metal is dim for 10 px (y 8032-8038) where
    chip 1's is bright (`textmap.py 7052 8014 7100 8062 3`): a blemish. **Assumed: no contact at any** (trap
    15: a tap in a crossing field has a widened pad). The other fifteen tracks are undrawn nets of the
    field (`busl`'s northern part), read the same way on `m_in1.png` and `m_row2.png` at 2.2-2.8x only.
42. **The three load ties are drawn without `?`** (piece `d3982`). U4 is a copy of `tl5_inv`, whose tie is
    uncertain in the master because a thin metal crosses its box; here the three tie boxes (U2 (7645-7680,
    8170-8195), U3 130 px lower, U4 (7655-7697, 8352-8385)) lie in the open: each is a heavy-outlined box at
    the end of the plate's tab, on a diffusion that comes from the node, in both chip-2 shots and the clean
    shot (`m_u2z.png` 5x, `m_u4a.png` 3.3x, `m_o2.png`, `m_o3.png`; the same build at U1 on `m_u1t.png`,
    5.5x). As in every load of this chip the box is taken to be a buried contact of plate to node (the
    guide's "how a load is recognised"); `g7700`'s tie in the same column is drawn the same way. If a tie
    were absent the plate would float (none of the three has any other connection: U2's and U3's plates
    end under the VCC metal's margin without a hole, U4's has no other poly).
43. **Piece `ck5`'s metal x 6466-6478 lies on `rst_c`'s poly for 225 px** (y 8945-9172; pieces `ck5`,
    `rc`). Read as no contact (trap 13): the metal has no ring, no widening and no dark stretch of 8 px
    or more in either chip along the whole overlap (`tl5_tracks.py v 6472 8945 9172 --half 2`), and the
    clean shot has no hole under it but the patch of the next item. A contact would make the ripple
    counter's clock the reset copy. What would settle it further: nothing in these photos.
44. **A dull patch at (6471,9045)** on the same overlap. The clean shot is dull (red minus green 0-40)
    over x 6456-6495, y 9038-9053: wider than the poly, and reaching 15 px onto the field east of the
    metal; chip 2's metal is dim on its west half for 9 px (y 9041-9050, 64-100) and chip 1's is whole
    (`textmap.py 6444 9020 6500 9075 3 --acid`; `tl5_tracks.py` gives 9048(7,17)). No pad (the poly is
    18-21 px wide there), no ring. Read as a stain, no contact.
45. **The knot at (6472,9161-9227): `ck5`'s corner and `rc`'s pad, 35 px apart on one x** (trap 16).
    The follower at `--gap 16` runs from (6470,9260) north straight through the pad to the pad
    (6645,8580). Read as two metals: (a) between the corner's lower edge (y 9174) and the pad's bright
    centre (y 9203-9215) neither chip has metal for 27 px, against a ring of 13 px on the south, where
    the pad's own metal starts at y 9230 (chip 2 has a half-bright patch at y 9185-9191, 144-176, where
    chip 1 is dark, 80-160: the open poly; trap 30); `eof_cchk.py`: the pad's ring is dark on the north
    (49 / 60) and open on the south (111 / 111) in both chips. (b) The west arm and the vertical are one
    metal: the 6-8 px dim line between them (x 6461-6464, 64-150 in chip 2) is the west edge of the poly
    underneath, which runs on up the vertical's west side; bare ground between two metals is 25 px or
    more everywhere in this bundle. If (a) were wrong the clock, the fifth corner-bundle line of `lc3` and `rst_c` would be one
    net; if (b) were wrong `lc2`'s through line would end on nothing.
46. **Crossings without pads** (piece `ck5`; trap 15): the poly x 6451 under fourteen horizontal metals,
    the track x 6688 over twelve poly rows (chip 1 dark for 20 px or more at four of them, y 7437-7461,
    7775-7797, 7820-7840, 7872-7904, where chip 2 is bright; chip 2 dark at y 7168-7187, where chip 1 is
    bright), the column x 6645 under three metals. No pad, no ring in both chips and no clean-shot hole
    at any of them: no contact. The seventh metal over the poly (y 6668-6682) was missed by the cut along
    x 6452 and found by review round 15: chip 2's metal is dim over the poly there (125-147 at x 6444-6460,
    against 210-240 at the other crossings) and chip 1's is bright through (183-211), the clean shot is
    salmon like the others (229/170/128), no ring, no hole (`eof_mrun.py col 6474 6390 7110 6430`;
    `px.py row 6675 6436 6468 4 metal,metal1,acid1b`).

47. **The join of piece `n2n`'s track to `bd1_n2` is not drawn** (the name `bd1_n2`). Between piece
    `n2w`'s end (6711,15000) and piece `n2n`'s start (6775,10400) the metal lies in `busl`'s claimed region.
    It was read by text and one view (the table of piece `n2n`, first row): one metal, one nested L step at
    y 13243-13255, no pad at any of the follower's sixteen contact candidates (9-15 px wide at each). Not
    reviewed. (a) One wire, as read: the bus line x 5412 of tl5 is `bd1_n2`. (b) A break or a tap in the 4,600 px that a
    text reading missed. Working assumption (a), carried by the name only: the two ends are separate nets in
    the extraction until someone draws the stretch (`busl`'s holder: the handoff of run 14 gives the
    coordinates). What would settle it: the stretch drawn and reviewed.
48. **Crossings without pads** (piece `n2n`; trap 15): the track x 6775 over the rows of two crossing
    fields and two single rows (y 9984-9998, y 10048-10064), the poly column x 6951 under three horizontal metals, the track x 6991 over ten poly rows
    (among them `rst_ck`'s tap row, `g7700`'s row 3, `tl3_w3982`'s row and `lc1_w7928`'s), the metal y 7000
    over five vertical polys (`tc2_m6404`'s and the ripple counter's clock among them), the row y 6996 under
    about ten vertical metals (`rc_stepreq_n`'s and `rst_ck`'s among them), the diagonal under the metal
    y 6830-6850 and the column x 5412 under nine horizontal metals. No pad, no widening and no ring at any
    of them: no contact. The clean shot is not clear of green everywhere (review round 16): under the track
    x 6775 it is greenish at (6775,9797) (126/145/74, red minus green -19 over about 10 px) and dull at
    (6775,9623) (148/143/69), where the metal is 13 px wide and bright through in both chips and the row is
    not widened; the same greenish patch lies under the neighbouring tracks on those rows (x 6689 on the row
    y 9797; x 6645, 6732, 6862 on the row y 9709): the drift of trap 15, not a hole in a pad. A contact at
    any of these crossings would join the latched R4 match to that net.
49. **A thin metal passes over the inverter's output box** (piece `ck6`). The metal that leaves the pad
    (8792,14870) runs south on x 8789-8801 (`bc1`'s ground, not drawn; the pad is the east end of the row
    y 14858-14880, which `bc1` draws as `bc1_dec10_n` to x 8500 and which is seen to run on to the pad at
    2x, `p_s3.png`: the name is believed) over U's box (8768-8797, 15030-15052): dark from y 15009 to
    15063 in both metal shots with a narrow bright spot (x 8789-8792, y 15036-15045, 7-B of 16, not full
    bright) in both; the clean shot has no green hole inside the box (green only on its outlines) and the
    metal is not widened (`textmap.py 8756 15006 8822 15072 3 --acid`; `p_b1.png`; the reviewer: blue
    131-140 on the bright centres against 96 at a known contact of a thin metal, (8642,14910)). Read: a
    pass-over (traps 22, 26). A contact would short that net to the counter's clock. (The same metal goes
    on over the box of the unit below and, from y 15116, over a diffusion strip: "The unit below the
    inverter".)
50. **`bc1`'s thin metal x 8637-8650 passes over the inverter's tie box and load strip** (`M 8642,14898
    y15060` in `trace/bc1.txt`, its `bc1_dec00_n`; it runs on south of y 15060, not drawn). Over the tie
    box both metal shots show a round bright centre about 12 px across in a dark ring, at (8637,14988);
    the clean shot shows the box as a heavy-outlined square with a pale centre and no green hole
    (`p_t12.png`, 5.5x, clean and both metal shots; the same at the tie box of the unit below,
    (8640,15172)). Read: the bright centre of trap 26, not a contact. A contact would put a decoder
    gate's output on the counter's clock.
51. **Two wide metals lie lengthwise on the row y 14825** (piece `ck6`; trap 13). (a) The VSS band
    y 14816-14878 (the rail x 8510-8560 turning east to column B's rail) lies over the row from x 8508 to
    8735, its top edge along the row's top edge; a second row, `bc1_dec10_n`'s, lies under its south edge.
    No ring and no hole on either row (`p_pad2.png`, 3.9x, four shots; `p_s3.png`; the reviewer's
    `r1.png`); a dark spot at (8570,14833) is in chip 2's metal shot only. (b) The metal of the
    neighbouring pad (9008,14828) (its track x 8915-8935 turns east along y 14820-14840) lies on the row's
    last 60 px and over its turn, and ends on its own pad 20 px east of the turn, on a poly column
    x 9002-9020 that goes north: `textmap.py 8898 14806 8994 14848 3` shows edge bars only (the track's
    edge, the turn's two edges) and salmon without a hole. Read: no contact at either; a contact at (a)
    would ground the clock.
52. **The inverter's load tie is drawn `?P`, `?B`** (piece `ck6`): the tie box lies under `bc1`'s thin
    metal (Ambiguity 50), so the chip-2 shots do not show the plate's poly entering it; the clean shot
    shows the box, and the plate's tab beside it (poly to x 8619, 5 px from the box's outline). As at
    `tl5_inv`, whose tie is under a thin metal too. The plate has no other connection, so without the tie
    it would float. Not looked at by the reviewer (whether poly enters the box).

53. **The open gap east of the rail is drawn as diffusion against its colour** (piece `vw`; x 8742-8777
    between the rail and the thin metal x 8789-8801). Edge lines say both stacks' diffusions run through it
    (the Logic table's row: no edge across rows A, B, 1, 2 in either metal shot; single edge lines on those
    rows; the doubled line along row C's top west of x 8757, in three shots). Colour says otherwise for the
    three bands between the rows: in the chip-2 stripped shot they read as field (`eof_patch.py 8752 8772
    15191 15200`: 1.7; `... 15235 15247`: 7.8; `... 15360 15373`: 11.3; field here is 2-6, the nodes and
    the foot in the same gap 19-25), and so in the clean shot (red minus green 11 against 36). The bands
    are 17-22 px high between two polys; a narrow diffusion in the open may show no colour (trap 4), but
    the foot (18 px) does show it. Drawn as diffusion on the edges, since the bands are alike in every
    shot and one of them, between B and C, is bounded by a diffusion edge that can be seen. If they were
    field after all: the stacks would each be two fingers (under the rail and under the thin metal), which
    changes no equation, **except** that the part between rows B and C under the thin metal would float,
    and the transistor under row C (`rst_a`) would lie between it and W's node, in series with the
    hairpin's gates to V's node: the reset would then clear the latch only while `eof_w15172` is high. As
    first drawn (run 16, before review round 19) the bands were field and that link an uncertain item.
    What would settle it: a sharper stripped shot of (8740-8780, 15185-15250).
54. **The row of the pad (8592,15383) and row 2 are in one line and are two polys** (piece `vw`; trap 34).
    The pad's row (V's output, by the metal x 8580-8604 from V's plate pad) crosses W's column under the thin
    metal and ends at x about 8666; row 2 (`bc2_w15607`, from the pad (8922,15392)) ends at x about 8681;
    the 14 px between are not poly in the clean shot and both metal shots (the Logic table's row). Seen as a
    small outlined box at (8664-8680, 15370-15395) in all shots (`r16_wbox.png`, 6x, four shots: the two
    rounded ends and the edges of the diffusions above and below). If they were one poly, `bc2_w15607`
    would be `eof_w15127` and W would be NOT(`eof_w15127`) with a redundant gate.
55. **Three links of V and W cross the 17 px open gap between the thin metal x 8637-8650 and the rail**
    (piece `vw`), where the clean shot shows a dark bar across anything (trap 2): V's pocket into its VSS
    box (y 15240-15257), W's node strip (y 15302-15316) and W's foot (y 15402-15420). The first is measured
    as diffusion in the chip-2 shots (Logic table). The other two are drawn plain on: tan on both sides of
    the bar at the same y, the foot's bottom edge in one line from x 8620 to the rail in three shots
    (`r16_foot.png`), the chip-2 shots dark over both (`eof_patch.py 8663 8676 15404 15414`: 90/91/51, no
    reading). Without the node strip W's stack would not be on its load; without the foot W's third
    pull-down would end nowhere.
56. **The two ties are drawn uncertain** (piece `vw`): V's `?P`, `?B` (box 8627-8650, 15160-15187, as in
    the withdrawn drawing) and W's `?P`, `?D`, `?B` (box 8645-8663, 15281-15298, read at 6x only, with its
    tail). Both lie under `bc1`'s thin metal x 8637-8650, like the inverter's (Ambiguity 52). Each plate
    has another connection that shows which net it is meant to be (V's plate pad feeds W's third gate, W's
    plate is V's arm), so the cross-coupling is drawn firm and only "plate = own output" is uncertain.
57. **Metals that lie on or cross polys of V and W without contact** (piece `vw`; traps 13, 22, 26). (a)
    `bc1`'s thin metal x 8637-8650 over V's tie box (bright centre 200/158, dull hole -8: Ambiguity 50), the
    arm (no hole), W's tie box (centres 92/103) and the row of the pad (8592,15383) (bright A-D through the
    row with two edge bars, no hole: `textmap.py 8612 15358 8704 15434 2 --acid`). (b) `bc1`'s thin metal
    x 8789-8801 over V's and W's output boxes and the five rows on the strip: dim throughout (centres
    95-136 against 181-237 on the contacts here); the clean shot's greenish line along the strip's edge
    gives `eof_cchk.py` a "hole" of -12 to -30 at every one of them, rows included, so that number means
    nothing on this metal. (c) The metal x 8580-8604 (V's output, dim) lies on W's plate and on the arm's
    column for 130 px: over the plate `eof_cchk.py 8592,15318` gives a bright centre with dark on all four
    sides (the plate's and the metal's edges, the strip's edge line) and no hole (+24; the two pads of the
    same metal -26 and -33); a contact there would short the latch's two sides. (d) W's output metal
    x 8838 over rows 1 and 2, row 1's metal over row 2, row 2's track x 8925 over row C and the row
    y 15042, the hairpin's metal x 8882 over the rows y 14825 and y 15042: no hole at any (`eof_cchk.py`:
    +33 to +40). (e) Seen by the reviewer of round 19, no contact: the bus metal y 14648-14660 lies on the
    hairpin's poly row from x 9060 to 9147 (where the metal turns south: run 15), and the hairpin's metal
    y 14785 crosses `bc2_w15607`'s poly column x 9002-9020.
58. **`bc1`'s bus metals on and over `bc2_w15607`'s poly** (piece `in390`; traps 13, 15). The bus metal
    y 14603-14618 lies on the row from its corner (x 9005) to x 9190, where the metal turns south (185 px),
    and the bus metals y 14656, 14699, 14742 and `eof_w15172`'s metal y 14785 cross the column x 9005-9023.
    Read as no contact at any: the poly keeps its width (18-21 px, no pad), neither metal shot has a ring,
    the clean shot has no hole on the row (`textmap.py 9020 14596 9200 14624 3`). Against, at the crossing
    (9014,14656) only: the clean shot's red minus green is 1 there on a 6 px streak (`eof_cchk.py 9011,14656`),
    and the column is dark orange-brown in the clean shot from the corner to y 14680 (137/66/32 under the
    metal y 14656, 134/82/27 at the corner) where the same poly is salmon (203-221/147-167/101-119) under the
    three metals south of it and `eof_w15172`'s row is salmon under the same metal (`px.py col 9014 14594
    14690 4 all`; `r17_a2.png`): read as a stain of that shot, since the chip-2 stripped shot has plain poly
    there and no pits. If the crossing were a contact, `bc2_w15607` would also be `bc1`'s bus line y 14656.
59. **The pad (10092,14609) has no green hole in the clean shot** (piece `in390`): vivid red-orange there,
    like the pad (6513,7889) of Ambiguity 38. Accepted as a contact from both metal shots (ring, bright centre
    12 px across) and the pits of the chip-2 stripped shot (trap 26, the converse). If it were none, the row
    would end on nothing and the metal start on nothing.
60. **Unit T is read without chip 1's clean shot** (piece `in172`): dark residue covers the stack west of the
    rail (x 10500-10620, y 14660-14740) and the plate in that shot. The body's diffusion, the gate rows' ends,
    the output box and the load are from both metal shots and the chip-2 stripped shot (`r17_u2.png` to
    `r17_u5.png`, the profiles in the piece's table). What only the clean shot would show (a buried contact's
    centre, protected colours under the rail) is not seen: the node strip under the rail is taken to be
    diffusion from its two edge lines in both metal shots and its colour either side of the rail.
61. **T's tie is drawn without `?`** (piece `in172`), unlike the ties of column B: the box (10624-10652,
    14738-14768) is in the open, heavy-outlined with a lighter centre in both metal shots and the chip-2
    stripped shot, the tail from the node strip runs into it from the north and the plate's tab from the east.
    Not seen: the box in the clean shot (residue). `eof_w15172`'s equation has the plate on its own node by
    this box alone.
62. **The foot of pad A's metal onto `bc2`'s pad (10395,15000)** (piece `in172`; trap 16): the metal x 10355
    turns east at y 14993-15007 and reaches the pad's ring from the west; the dark between its bright end
    (x 10376) and the pad's centre (x 10390) is 10 px in chip 2 and 8 px in chip 1, a ring's width. `bc2` read
    the same ("a metal from the north-west ends on it"). If the metal only passed the pad, T's row 1 would be
    an unknown net and not latch unit a's output.
63. **`ck_out`'s metal lies on another net's poly row for 300 px** (piece `in350`; trap 13). Under the
    stretch y 17649 from x 8588 to x 8893 the clean shot is salmon with a red outline (208/166/99 against
    pink field, 172/86/97, in the 8 px margin south of it; under the metals y 17606 and y 17690 of the same
    nest the field is pink): a poly row y 17640-17656. It is not this net's: at its west end it turns south
    20 px west of the metal's corner (x 8572-8588, in the open between the rail and the metal x 8600: orange
    in both metal shots, dark red-brown in the clean shot, to about y 17700), and east of the metal's other
    corner it goes on under the tracks x 8925 and x 8968 (salmon 210/168/101 under each at y 17648). Read as
    no contact: no ring and no widening anywhere along the 280 px in either metal shot, no hole in the clean
    shot (`tl5_tracks.py h 17649 8585 8895`), nothing at either corner (`textmap.py`), and the row keeps one
    width. Where the poly comes from and goes was not followed. If there were a contact, that net would be
    `ck_out` too.
    **Run 22: the row is `eof_w17168`'s** (piece `o168`: it comes from the NOR `nor17`'s output pad
    (9055,17648)); Ambiguity 80.
64. **Reddish patches east of the pad (8882,16867) in chip 1's clean shot** (piece `in350`; the poly column beside them, under the track x 8925, is the lower node's branch of piece `lat16`: review round 24): at x 8898-8915,
    y 16852-16872 the clean shot is not green as it is east of the pad (8882,16648) but blotched salmon
    (also at about (8945,16862)). Read as residue and not a poly leaving the pad east: irregular blobs, no edge
    lines; in chip 2's metal shot the 15 px of bare ground between the pad's ring and the track x 8925 are
    plain, with no poly crossing them, and the chip-2 stripped shot shows only that track's fringe
    (`r18_p2.png`, 6x; `textmap.py 8850 16836 8960 16898 3 --acid`). If it were a poly, the row would go on
    east under the track x 8925. Review round 22 adds: a real poly does lie under that track (x 8918-8935,
    y 16830-17000, turning west at y 16992), 18 px from the pad; the gap between them is bare ground in both
    metal shots (124/102/66 and 139/125/71, no edge bars along x 8908): no join (`review-22/pad2_ctx.png`).
65. **Chip 1's metal is missing on the track x 8838 where it crosses the row of the pad (8882,16867)** (piece
    `in350`): `tl5_tracks.py v 8838 16600 16920` fails chip 1 from y 16823 to 16885 and the clean shot is
    strongly green there (unprotected: -85, -66); chip 2's metal is whole, with only the row's two edge bars
    and no ring (`eof_cchk.py 8838,16866`: centre 186, ring open to the south). Read as damage to chip 1 (as
    on `trunks`' line S) and no contact between that track and `ck_out`'s row; the clean shot cannot confirm
    it at this spot.
66. **The metal that lies on `ck_out`'s poly west of the pad (8424,17908) is another net's** (piece `in350`;
    traps 13, 16, 30; settled by review round 22 against the first drawing). It was drawn as a metal leaving
    the pad west, its last 12 px before the ring taken for dim metal. They are open poly: 151-152 / 104-122 /
    51-54 in chip 2 and 132-146 / 59-80 / 43-45 in chip 1 at x 8400-8403 (metal 187-203 / 152-174 / 64-81 at
    x 8376-8385), the stripped shot's metal ghost ends at x 8388, and 33 px lie between the metal's end and the
    pad's centre against 17 px for the ring of the metal that does end on the pad. The metal's end turns north
    toward a pad with a contact at about (8382,17862) (bright in chip 1 at (8384,17886-17890), dim in chip 2:
    probable, not read further). Not read: whether that metal makes contact with the poly on the 80 px
    (x 8312-8390) where it lies on it; no ring or hole was seen there (`tl5_tracks.py h 17908 8040 8440`: no
    hole between x 8122 and x 8420). If it did, that net would be `ck_out`.

67. **The inverter's output east of the rail is read without chip 1's clean shot** (piece `inv16`; trap 28).
    In the open gap between the rail x 8686-8731 and the track x 8838 the clean shot shows a dark tangle at
    y 16400-16450 (`s19_j.png`, 5x): it does not show the box or the strip. In the other three shots
    (`s19_j.png`, `s19_k.png` at 7x) the row y 16421-16443 is three pieces between dark edges: x 8741-8766 plain
    and pinker than the field (chip-2 metal 172/128/82, chip-1 metal 156/121/77, chip-2 stripped 163/131/70),
    x 8779-8793 a box interior (168/130/76, 152/129/70, 150/131/66), x 8806-8824 poly (165/110/47, 152/88/48,
    158/113/45, like the gate row above: 160/114/59, 155/82/45, 155/115/52). The pale band between this row and
    the gate row (y 16403-16416) is field (165/146/83, 135/122/62, 143/137/64), closed at its east end by the
    track's edge. Read: the west piece is the node's diffusion strip from under the rail (where `railprof`
    gives diffusion at y 16404-16436), the box a buried contact, the east piece the output poly's end, which is
    U4's arrangement mirrored. The other reading, that the west piece is a poly stub ending at the rail (blue
    74-87 there is between poly's 41-68 and the 85-95 of trap 28's diffusion), leaves the output poly with no
    driver and the inverter with no output, and chip 1's metal shot separates the piece from poly clearly
    (red minus green 35 against 64-73). Drawn without `?`. What would settle it: another die's stripped shot.
68. **The lower contact of the latch's thin metal x 8588-8600 shows no green hole** (piece `lat16`; trap 26).
    At (8594,16846) both metal shots have a bright centre (x 8588-8600, y 16841-16850: 160-207 in chip 2,
    176-223 in chip 1) in a dark ring, and the metal ends there (`tl5_tracks.py v 8594 16620 16880`); the clean
    shot is dark red at the centre (109/55/34), the chip-2 stripped shot 135/116/69. The upper contact
    (8594,16648) has the hole (121/120/62). In the master and in `bc2`'s two copies the same pad carries a
    contact (the thin metal joins the upper unit's plate to the gate of the lower unit's third pull-down);
    drawn as one, without `?`. If it were none, `eof_w16823` would lose the term `eof_w16693` and the pair
    would not latch.
69. **The upper node's metal lies on the lower node's poly for 100 px** (piece `lat16`; trap 13). The metal
    x 9006-9018 south of the pad (9012,16693) runs over the poly column x 9004-9022 from y 16724 to y 16832.
    `textmap.py 8988 16705 9040 16845 3`: the metal is bright without a ring from y 16729 to y 16828 in both
    chips, the clean shot under it salmon (red minus green 48-72) with no hole; 15 px of field (y 16707-16722)
    between the pad and the poly's corner; the follower's candidates (9012,16798), (9011,16811) have no ring
    and no hole (`eof_cchk.py`: 27, 24, at the poly's east edge). Read as no contact: a contact would join the
    latch's two outputs.
70. **The inverter's tie, and the thin metal over it** (piece `inv16`). The tie box (8618-8660, 16433-16465)
    lies under the thin metal x 8637-8650 below the plate's east end; plate tab, hook and box are drawn `?`,
    as for every load of this build, and `eof_w16607`'s equation rests on them. The thin metal (another
    net's, not drawn here: it runs the length of column B) is dark over the box for 40 px in both chips
    (`tl5_tracks.py v 8643 16340 16500`: y 16426-16465) with no bright centre (`eof_cchk.py 8643,16450`:
    102/68): a pass-over (trap 22), read as no contact. Geometry not resolved and not affecting a connection:
    whether the gate row's west end (salmon x 8678-8697, y 16372-16412 under the rail's margin) lies partly on
    the node's diffusion, and where exactly the strip under the plate has its edges (y 16388-16410 from the two
    edge lines under the thin metal; the chip-2 stripped shot shows one line at y 16405).
71. **Two things at the latch that differ between the chips or from the master** (piece `lat16`; neither
    changes a connection). (a) The copy's thin metal from the top pad lies about 8 px west of the instance's
    (centre x 8771; the top pad's contact at (8776,16511), the lower pad's at about (8785,16912)): inside both
    pads either way; the cell is not changed. (b) Chip 1's metal on the track x 8838 is missing from about
    y 16793 to y 16910 (the clean shot is green there: `tl5_tracks.py v 8838 15700 16960`: -51, -85, -66),
    which is Ambiguity 65's damage and covers the lower node's row as well; chip 2's track is whole over the
    row with no ring (`eof_cchk.py 8838,16823`: 182, ring 78/79 north and south, as at the next track).
72. **The neck between the lower node's box and the large diffusion: diffusion or poly** (piece `cap16`;
    trap 28). In the 24 px gap between the tracks x 9056 and x 9099 the clean shot shows the neck
    (x 9070-9088, y 16607-16672) as a dark bar, which is what both a narrow diffusion and an open poly look
    like there. Read as diffusion, the rectangle's own neck, on three tests (the table of piece `cap16`): its
    colour in the clean shot and in the chip-2 metal shot is the rectangle's in a like gap and not the poly
    leg's in the same gap, and no edge line crosses it where it meets the rectangle. The other reading (the
    poly runs on north through the box and ends at the rectangle's edge) would leave the rectangle joined to
    nothing and the box without a purpose; it would not change any transistor or equation, only whether a
    gateless diffusion hangs on `eof_w16823`. Drawn without `?`. The box is read as a buried contact from its
    heavy outline in the two chip-2 shots and the poly's end inside it (`r20_a2.png`, 7.8x). **The two
    tracks beside it** (x 9056 and x 9099, other nets' through metals, drawn by no one) each lie with one edge
    over the pad, and there the photos have part of a contact's signature: both tracks fail the metal test
    for 40-46 px in both chips (`tl5_tracks.py v 9056 / 9099 16630 16760`: y 16673-16713, y 16671-16717), the
    clean shot is bright green under their edges (the two lobes, x 9058-9067 and x 9094-9100: 93/172/116,
    85/141/91), and on the track x 9056 a bright patch sits between two dark bars (`eof_cchk.py 9062,16692`:
    hole -75; 166 and 173 in a ring of 51-98). Read as **no contact from either track** (traps 22, 26, 27: a
    thin metal over a buried-contact box is dark for 35-80 px in both chips, and the clean shot is greenish
    under it): neither track is widened (a contact of these tracks has a pad 36 px wide, e.g. (8925,16262));
    the bright patch is 6 px wide and 20 long, the strip of the track between the pad's west edge line
    (x 9058, lengthwise under the track) and the track's own edge, with the pad's top and bottom edges as the
    two bars, while the track's other half runs past at full brightness (the text map's chip-2 column, x
    9049-9055); on the track x 9099 the same, mirrored (edge line x 9100), with no bar north or south
    (`eof_cchk.py 9099,16692`: ring 138 / 159). Chip 1's metal shot has a dark blemish over the box
    (x 9060-9140, y 16668-16715) and decides nothing. A contact here would join two through tracks to each
    other and to the latch's node. What would settle it: where the two tracks go (not followed).
    **Run 21: the track x 9099 here is `eof_w17212`**, the second input of the NOR `nor17` (piece `in212`:
    this stretch runs from the pad (9053,15822) to the NOR's row-3 pad (9098,17210)); it is drawn, with
    y 16666-16718 as `?M` (trap 27). A contact here would make that input the latch's own lower node, and
    the NOR, whose other input is the latch's upper node, a gate whose output is low whenever the latch
    is settled: one more reason to read none. The track x 9056 is still not followed.
73. **What the large diffusion is** (piece `cap16`). 350 x 130 px of diffusion with a step, no gate, no
    contact, under six tracks of other nets, tied only to the lower latch's lower node. Believed a capacitor
    that slows that node (the junction's capacitance; whether a depletion implant or thin oxide is involved is
    not visible). The upper node has no such diffusion (its metal and row are followed end to end). A twin
    170 px south is tied to another net at its east edge (not drawn). Nothing in the extraction depends on it.
74. **The data's poly at column B's edge** (piece `lat15`). The row of the pad (8880,15738) is drawn to x 8800,
    where it enters a heavy-outlined box (8762-8795, 15722-15757) beside the thin metal x 8792; the box is not
    a metal contact (`eof_cchk.py 8776,15737`: centre 101/104) and is not read: a buried contact onto a
    unit's node (then that unit drives the data) or a pad of something else. A port; the latch's equations
    do not depend on it.
75. **The thin metal x 8637-8650 over the upper latch copy** (piece `lat15`; review round 26; traps 22, 27).
    Column B's thin metal (another net's: `bc1` draws its top, `M 8642,14898 y15060`; nobody draws it here)
    runs over the copy's inverter node box and its two tie boxes and is dark there in both metal shots for
    12, 23 and 17 px (`tl3_thin.py 8636 8650 15860 16470 --thr 144 --min 8`), as over `inv16`'s tie (Ambiguity
    70: 35 px) and as the master's thin W over `tl1`'s cells. Read as a pass-over with no contact: no
    widening, no round bright centre, the clean shot tan under it. If it did make contact with a tie box it
    would join that net to a latch node. Its continuity over the boxes cannot be shown from these photos;
    whoever draws it draws those stretches `?M` (trap 27).

76. **`inv17`'s thin metal over three boxes** (piece `inv17`; traps 22, 26, 27). The output wire of the
    inverter, a metal about 10 px wide on x 8796-8798, passes over the output box of `nor17` (dark in both
    metal shots for 58 px, y 17148-17205), over the node box of the next unit down (8770-8800, 17325-17352:
    dark for 14 and 18 px with a bright stretch y 17336-17346 between, 10 px wide, not widened; the clean
    shot shows the box's pale square centre under it, no round green hole; `r21_i1.png`, 6x, four shots) and
    over a third box (8780-8800, 17460-17490: dark for 37 px). Read as pass-overs: at none is the metal
    widened into a pad, and a contact at any would tie the inverter's output to another gate's output.
    Its continuity over the boxes cannot be shown from these photos: the three stretches are `?M`, so
    that `eof_w17040`'s join from the inverter's pad to the pad (8792,17561) is marked. What would settle
    it: a shot with the metal intact at higher resolution, or the wire's use (its load is not found yet).
77. **The pad (9008,17560) shows no green hole** (piece `inv17`; trap 26's converse). Both metal shots show
    a ring and a bright centre there and the pad's own metal leaving south; chip 1's clean shot shows the
    pad vivid red with no hole (`eof_cchk.py 9007,17560`: 27), as at the pad (6513,7889) (Ambiguity 38,
    AMB-041). Drawn as a contact. Review round 27 looked at the chip-2 stripped shot at 6x: a pitted
    box, which is what a metal contact looks like there. If it were none, the poly row from the pad (8792,17561) would end on
    nothing and the metal south of the pad would have no source.
78. **`nor17`'s tie** (piece `nor17`). The heavy-outlined box (8628-8662, 17196-17238) below the load's
    strip lies under the thin metal x 8637-8650 (another net's, dark over it); the plate's tab enters it
    from the west and a tail of the strip from above. Drawn uncertain (`?P`, `?D`, `?B`), like `inv16`'s
    (Ambiguity 70) and every tie of this build; the NOR's equation rests on it. The same thin metal over
    this box and over `inv17`'s tie box is read as a pass-over, as in Ambiguity 75.
79. **`eof_w17168`'s row is vivid red-orange under the rail x 8500-8562 in chip 1's clean shot** (piece
    `o168`; row y 17682-17698). Under the rail the row reads 138/25/25 to 212/110/52 (`px.py row 17690 8440
    8600 5`), where the next row under the same rail (y 17733) is the usual cream (215/159/97), and chip 1's
    metal shot is reddish over the same 55 px. Read as a plain crossing: neither metal shot has a ring or a
    widening there (`textmap.py 8486 17668 8600 17712 3 --acid`: the rail is bright from edge to edge on the
    row, with only the two bars of the row's edges right across it, as on every row under this rail;
    `eof_cchk.py 8536,17690`: no hole, 54), there is field north and south of the row under the rail
    (`railprof.py 8508 8548 17300 17960`: poly over field), so it is no gate, and chip 2's two shots show an
    ordinary row. A blemish of chip 1 (the pad (6513,7889) has the same colour there: Ambiguity 38). If it
    were a contact, the NOR's output would be tied to this rail.
80. **`ck_out`'s metals lie on `eof_w17168`'s poly twice** (piece `o168`; trap 13). The row y 17638-17656 lies
    under the metal y 17649 of piece `in350` for 300 px (Ambiguity 63, written before the row had a net), and
    the row y 17682-17698 under `ck_out`'s other metal, the one that ends on the pad (8424,17908) from the north
    (not drawn; `follow.py 8390 17692 E --gap 16`: corner (8426,17693) south to (8424,17911); west to a corner
    (8142,17687)), from x 8426 to x 8355. Read as no contact both times: no ring, no widening, no hole
    (`eof_cchk.py 8425,17692 8390,17692`: 27, 44; `tl5_tracks.py h 17691 8362 8500`: none). The logic agrees
    here, which it could not for Ambiguity 63: the row is the output of the NOR `nor17`, and a NOR's output is
    not `ck_out`.
81. **A dark line x 8254-8258 across the row east of the pad (8185,17428)** (piece `o168`). A line 5-8 px wide
    in all four shots at y 17300-17500 (`px.py row 17429 8240 8266 2 metal,acid1b`: chip 2's metal 63-75
    there; absent at y 17100 and y 17800), which crosses the poly row y 17419-17440 58 px east of the pad. Not
    identified: it is no metal (dark in both metal shots), and `bc3`'s notes have "a big diffusion area
    x 8250-8400" here, whose west edge it may be. The row is drawn to x 8245, short of it, so that nothing
    drawn rests on what the line is; if the ground east of it were diffusion, the row would cross it as a gate
    before it reaches the hairpin. To settle with the unit (next run).
    **Run 23: it is the west edge of the unit's active area** (piece `g174`): one straight edge from y 17262 to
    y 17560, with ground of the open diffusion's colour east of it in chip 2 and field west of it
    (`eof_patch.py 8246 8253 17500 17540`: 1.7 / 11.2; `... 8266 8298 17275 17315`: 16.3 / 33.8), and the lower
    poly's block and the box of Ambiguity 84 against it. The row does cross active area before it reaches the
    leg: that stretch is part of the hairpin's gate. What is left of the doubt is Ambiguities 83 and 86.
82. **The join of `eof_w17040` to `bc1_g6_in` passes Ambiguity 76's three stretches** (piece `o040`; trap 17).
    Piece `o040` itself has no uncertain item, and `bc1`'s stretch was looked at again (`r22_h3.png`,
    `r22_h4.png`). But between the inverter `inv17` and the pad (8792,17561) the thin metal is drawn `?M` over
    three boxes, so `tools/unsure.py` lists `bc1_g6_in` and `eof_w17040` as two pieces without the uncertain
    items, and `bc1_g6_in` = NOT `eof_w16823` depends on them. The alias `@alias bc1_g6_in eof_w17040` records
    the join; no rename until Ambiguity 76 is settled. The join gives that ambiguity its first test from use:
    the thin metal's south end now has a load (`bc1`'s inverter 6) and no other driver was met on the 2,700 px
    from the pad (8792,17561) to that inverter, so the wire needs a source north of the pad.
83. **West of the rail the two chips disagree on the ground north of row 1** (piece `g174`; traps 21, 28). The
    rectangle x 8258-8306, y 17266-17322 has a dark outline on all sides and, in chip 2's two shots, the colour
    of the open diffusion strip east of the rail and not of field (`eof_patch.py 8266 8298 17275 17315`: red
    minus green 16.3 / 33.8; the strip 16.6 / 32.9; field at (8440-8460, 17240-17254) -8.8 / 11.8). In chip 1's
    clean shot it is khaki (148/137/105), which trap 21 gives as open field, where the strip is bright green
    (120/152/91). Drawn as active area on chip 2 and on the edge line x 8254-8258 that bounds it. If it were
    field, row 1's transistor would be 62 wide and not 110: a width, no connection (the node `eof_w17362` and
    the contact (8335,17293) lie under the rail either way). What would settle it: nothing more in these
    photos; a third chip.
84. **A heavy-outlined box with a pale centre and no poly, in `eof_w17362`'s west part** (piece `g174`;
    x 8242-8282, y 17372-17402, across the active area's west edge; `r23_b2.png`, 5x, four shots). Its outline
    is 6-8 px heavy, its centre (x 8262-8276, y 17378-17396) pale green in both chip-2 shots (138/161/89 in the
    stripped shot), bright yellow in a dark ring in chip 1's metal shot, blue-grey rings in the clean shot: the
    look of a buried-contact box, or of a contact's hole. No metal reaches it (`tl5_tracks.py h 17386 8120 8300`:
    none from x 8235 to x 8299 in either chip; `ck_out`'s second metal ends at x 8234, 8 px short of its outline),
    and no poly: chip 2 has no orange in or beside it, and the clean shot is pink under that metal at
    (8200-8236, 17386), where a poly would be cream. Nothing is drawn for it: as the photos show it, it joins
    the node to nothing. It is where a unit of this column would have its output box (`bc1`'s units have theirs
    at x 8271-8308, with a poly leaving west), so a wire may have been taken out of the layout here. Recorded
    because the box of Ambiguity 85 has the same look.
85. **The box where both gate polys end, east of the rail: a tie of the gates to their own drain, or not**
    (piece `g174`). **Resolved in run 24 (piece `g174e`): reading (4), drawn. The box is a field island; the
    pocket between the arm ends is field and the slot, the necks and the bridge east of the box are diffusion,
    each on a whole-band test against a control (the Logic section's table of piece `g174e`). A buried contact
    there would join the ground finger to the output node. What follows is the entry as run 23 left it.** **Since review round 29 the working belief is reading (4) at the end of this
    entry; fact (a)'s "a field slot" was wrong.** The facts, each measured (the Logic section's second table): (a) the hairpin
    `eof_w17168` and the lower poly `eof_w17472` each run on east of the rail, over field, and turn into an arm;
    the two arms run side by side, a slot between them (first read as field; diffusion: below), and end at x 8437 inside one heavy outline
    (x 8410-8437, y 17418-17500), 10 px short of the east edge of the open diffusion strip, which is continuous
    past them; (b) inside the outline the arm ends are dim and plain, not orange, and a pale green spot lies
    between them: what a poly's end on a buried contact looks like in the chip-2 shots; (c) the two necks make
    the strip one node with `eof_w17362` and the node below the lower bar (former name `eof_w17552`; it is `eof_w17362`, run 24); (d) the strip has a load toward the VCC rail.
    Readings: **(1) the box is a buried contact onto the strip**: then both polys, and with the first the NOR
    `nor17`'s output, are the strip's node, and the hairpin and the lower poly are transistors of W/L 7 and 8
    from that node to ground with their gates on it, against a load of about 1.6: the node could not rise.
    This is what the box looks like and it makes no circuit. **(2) the box joins nothing** (the ends lie in a
    window or a hole that does not tie them, as the box of Ambiguity 84 ties nothing): then the unit is the
    NOR of the Logic section, the ratio of pull-downs to load is the ordinary one, and the arms have no
    purpose that can be seen. **(3) the box joins the two polys to each other and not to the strip**: then
    `eof_w17472` is `eof_w17168`, the hairpin and the lower poly are two fingers of one pull-down, and the
    lower poly's west leg carries the NOR's output on south; but the strip passes the box with no field
    between. **(4) (review round 29) the slot is a finger of the ground diffusion**, which leaves the active
    area between the two right legs and runs east between the arms to the box's west line (about x 8408): the
    slot has the necks' colour and not that of a field band of the same height between two polys (the Logic
    table's row "The two necks and the slot", with its control). Then each arm is one more stretch of its gate,
    between the finger and the strip; the arms run 25 px on past the finger's end, as a gate must past the end
    of its diffusion; the pale spot between their ends is field (it has the field's colour), and the heavy
    outline is the two ends' outlines round that pocket. No contact, no tie: the unit is the NOR of the Logic
    section with ordinary ratios, and every fact above has its place ((b): a poly's end over field is dim here
    too, 125 against 152-157 west of the rail). This run's first reading missed it because its one row across
    the slot, y 17457, lay on the slot's greenish north flank, while its samples of the necks lay on their
    reddish south flanks: in chip 2's shots a 10 px band between two polys has both. Working assumption: (4),
    believed and not drawn: nothing east of the rail is in the trace, the two polys keep two names and the two
    nodes two names, so that no reading is built in. What would settle it: the next run's drawing of the east
    side and its review; from use, where `eof_w17472`'s west leg goes (a driver at its far end excludes (1)
    and (3)), and what the strip's node drives.
86. **The narrow bands of the active area west of the rail have no colour of their own** (piece `g174`; trap
    4). **Run 24: the band between the two rows (x 8264-8298, y 17443-17463) is diffusion on the whole-band test
    (+32.0 / +16.9 against +14.0 / -3.4 for the field band of the same height just west of the edge): as drawn.** Between row 1's bottom and the box of Ambiguity 84, between the two rows (y 17443-17463), west of the
    lower poly's east leg (x 8258-8273) and east of it (x 8297-8305) the ground is 8-15 px wide between two
    edges and reads between field and diffusion (`eof_patch.py 8266 8298 17446 17456`: 3.6 / 15.9;
    `... 8261 8268 17500 17540`: 16.2 / 30.8, but `r23_prof.py row 17500` gives the diffusion's colour only
    for the 4 px beside the edge line). Drawn as active area throughout on the one straight edge x 8254-8258,
    which runs the whole height. If any of them were field the widths of the hairpin's and the lower poly's
    transistors would be smaller (at least 63 and 62: the two bars under the rail); no connection changes,
    since each poly still seals its node under the rail.
87. **Chip 1's metal is destroyed over the unit** (piece `g174`; y 17320-17480, `r23_a3.png`). The rail between
    the two contacts, the contact (8335,17474) as a contact of this rail, and the absence of any other metal
    over the active area rest on chip 2's metal shot and on the clean shot's protected colours (cream polys,
    tan diffusion from x 8306 to x 8368 the whole height).

88. **The right legs and the arms are drawn as gate; the poly's colour does not show it** (piece `g174e`).
    Each leg (x 8370-8389) has diffusion against both its edges, the ground under the rail on the west and the
    strip on the east, and no edge line crosses the poly between the bar, the leg and the arm (`px.py col 8381`,
    2 px steps, both chip-2 shots: lowest red 151-162, where a real crossing dips to 61); the slot beside the
    arms is diffusion on the whole-band test. Against it: run 23 read the legs as lying over field from the
    poly's colour, and in the clean shot the east half of each leg (x 8382-8388) is dark (100-127) beside a
    bright west half (148-184) (`px.py row 17400 / 17515 8362 8416 2 acid1b`). Run 23's patches were half edge
    line; on the centre line the legs have the arms' colour in both chip-2 shots, and known field-poly and known
    active-poly of the same unit do not separate there (metal, red/green: 165-176/115-118 against
    170-185/121-135). If the legs lay over field after all, the hairpin's and the lower poly's widths would be
    about 50 less each; every connection and the equation would be the same. What would settle it: nothing more
    in these photos.
89. **Row 1's east end and the active area's east edge fall in one edge line** (piece `g174e`; x 8464-8470,
    y 17282-17302; `px.py row 17292 8440 8490 2`, metal and `acid1b`; `row 17270`, `row 17314`). Drawn at
    first: the active to x 8467, the poly 5 px past it, on the assumption that the gate closes the ground
    band off from the strip. **Closed by review round 31: the poly runs on past the edge line to about
    x 8478** (east of the line the strip x 8472-8476 has the poly's colour at y 17292-17296, metal
    139-157/80-110/43-65 and stripped 115-128/87-97/45-59, and is plain at y 17272, the band's height:
    161-165/122-133/77-81), so the gate overhangs the active's edge by 10 px. Drawn so since.
90. **The band and the sliver of ground diffusion beside row 1 join the ground under the rail's step corner,
    which only the clean shot shows** (piece `g174e`; x 8366-8392, y 17262-17282). In both metal shots the
    rail's corner lies over the place. The clean shot is protected tan (190-200) from under the rail right
    through to x 8390 at y 17264-17274, with no dark line, and the band (open, dull) and the sliver (open, dark
    red: trap 28) begin where the protection ends (`r24_map.py 8366 17260 8404 17290 2 acid1b,metal1`: red
    only, which does not tell tan from the pink of field under metal; in full colour the corner is tan,
    `px.py pt 8380,17268 8386,17270 acid1b`: 193/171/122, 195/176/126, the reviewer of round 31: 190-200/166-185/124-133;
    `r24_map.py 8364 17254 8404 17290 2 metal,acid`: in chip 2 a bright path from the sliver round the poly's
    corner to the band, lowest red 130-150 against 155-180 on either side). The dark dip of about 6 px where a
    diffusion passes from protected to open is there at the slot too, where chip 2 shows plain diffusion
    through it. If the band or the sliver were cut off, row 1's width would be less; no connection changes.
91. **The second contact of the diffusion under the VCC rail** (piece `g174e`; (8509,17513), 18 x 34) is read
    from a text map and one 4.5x view of the two metal shots (a bright bar between dark sides, not a round
    ring), with specks in the clean shot and a pitted patch in the chip-2 stripped shot. The first contact,
    (8528,17477), is a plain ring with a bright centre in both chips and joins the diffusion to the rail by
    itself.
92. **The dark line x 8484-8488 through the load's plate, and the tab** (piece `g174e`). Both metal shots show
    a dark line down the plate 12 px west of what looks like the rail's edge (x 8498-8502), and the chip-2
    stripped shot a red line there. Read as the rail's west edge: the line runs on north of the active area
    (so it is no active edge), the strip east of it has metal's colour where no poly lies under it, and the
    clean shot shows no line there, only the change from open to protected poly. The line x 8498-8502 is then
    the plate's east edge under the metal. Other reading: two polys side by side (a column and a strip), 4 px
    apart, which no process draws. The tab north of the plate under the rail's edge is poly by its colour in
    the clean shot; were it a diffusion from the tie box to the diffusion under the rail, the output would be
    tied to VCC. Working assumption: one poly, a plate with a column and a tab.
93. **The output pad's metal south** (piece `g174e`; (8467,17603)). Between the pad's bright centre and the
    metal south of it both metal shots are dark for 14 px (y 17611-17625; a ring is about 10, trap 16's false
    join had 24-33), and `tools/tl5_tracks.py v 8467 17600 17700` lists three more stretches of 8-13 px without
    metal in both chips further south (the thin metal over the bus rows: traps 19, 27). The clean shot's
    protected strip runs on south from the pad without a break (`px.py col 8471 17540 17630 3 acid1b`: pink
    from y 17618), and `tools/follow.py 8467 17640 N --gap 16` ends on the pad. Drawn: 30 px of metal and a
    port; the run beyond is the next piece's to read. (Run 25: read and drawn, piece `o362`; the ring's 15 px
    at y 17610-17624 is the only stretch of its kind next to the pad.)

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
  extraction: `rst_ck` one net, `lc1_w7040` separate, 0 errors.
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
- extraction: three gates on `rst_a`, 0 errors, not listed by `tools/unsure.py`.

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

### Round 10 (full review of pieces `n2out` and `n2w`; 2026-11-19 15:52 to 16:11 +0000)

One fresh reviewer (general-purpose agent, Claude Fable 5.2), at commit 278b6ae. Its images are in
`cache/scratch/eof/review-10/` (20 used).

**Told to suspect**: in `n2out`, both links across the open 29 px gap (whether the strip ends under
`bd1_an`'s metal and N2 under the rail's edge line with field between; whether the 15 px top link is
diffusion reaching the ground diffusion or a closed box; whether the lower segment is continuous under
the metal; a poly in the gap); in `n2w`, link F under `ck_out`'s metal and whether the diagonal keeps
its place beside `rst_a`'s; the braid of three Z bends (which line leaves on which); link C's
diagonal beside a second one; every pad for a metal running on or a second poly; the corner
(6712,18083), the step at x 8182, link N under the wide bus; the nine dismissed contact candidates.

**Checked and found correct**. `n2out` (6x in four shots, `px.py` rows on eleven rows, columns x 13782,
13796, 13800, 2 px brightness maps): claims 1 and 2 (on the link rows neither metal shot has an edge line
at x 13798-13806 and the rail's edge line is light, R about 105; on the island rows the dark band at
`bd1_an`'s edge is 10-12 px wide and the rail's edge is dark, R 47-64; the clean shot shows the diffusion
under the rail with no west edge on the link rows and one at x 13822-13826 on the island rows; the gap's
bar is red-brown as on N1's crossing, not green); claim 3 (the island is a closed outline in both metal
shots; field pink under the rail's margin at y 15685-15703); the lower segment continuous under the metal
from y 15686 to the box; claim 4 (extraction, the equation, `unsure.py`: `bd1_k`, N2 and the wire in one
piece without uncertain items); claim 5 (no contact over the box: no pad or widening, the same look as
N1's box under the same metal; the real contact (13768,15806) is a widened ringed pad). `n2w`: all
fourteen pads at 2.8-4x in three or four shots (one metal and one poly each, field beyond); all seven
poly links single unbroken bands; link F under `ck_out` (no ring in either chip, no hole; `ck_out`'s
metal turns a corner there and runs on west); the diagonal keeps its place (cuts every 20-30 px in the
clean and chip-2 metal shots); the braid's outer Z continuous; link C's diagonal, the step and the corner
as drawn; the pad (12848,17777) 25 px clear of the rail (`follow.py --gap 16` ends on it); every listed
candidate an edge underneath, a chip-1 speck or a clean-shot stain; every metal run profiled in both
chips: no break, no widening. **Not checked**: the chip-2 stripped shot in the gap (fringe: the reading
rests on both metal shots and the clean shot); links D and N under the wide rail and the buses in the
chip-2 stripped shot; the wire north of y 15000.

**Findings**, each checked by the tracer; none changes a connection:

1. **Geometry only, `bd1`'s**: the gate poly of `rst_a` (`P 13640,15671 x13805`) ends about 7 px short;
   its end cap lies on the island at x 13806-13812. **Confirmed** (`px.py col 13806 15620 15750 3
   metal,metal1`: 120-150/64-75/34-43, poly orange, at y 15665-15680; at x 13812 the same rows are not
   orange). Not this package's item and not changed (handoff): the gate crosses the whole strip either way.
2. **Geometry only**: the two links overlapped `bd1`'s diffusions under the rail by 5 px. **Fixed**:
   `D 13795,15712:13830,15736`, `D 13795,15638:13840,15652` (13 px each, inside `bd1`'s rectangles).

With them, **the geometry fixes that waited in `trace/eof.txt`** (master list, `eof` row: from `eofw`'s
handoff and three second-look reviews of `g7700`, `r5nor`, `isrc`), each measured first:

- `g7700`: the poly north of the pad (7272,6912) is x 7268-7286 (`px.py row 6890` and `row 6880 7256 7296 2
  acid1b,acid`): `P 7277,6875 y6912 w=18` (was x 7278, w 13). The metal south of the pad (7267,7736) is
  x 7266-7281 (`px.py row 7770 7254 7290 2 metal,metal1`): `M 7273,7736 y7800 w=12` (was x 7268). The row
  east of the pad (7313,7215) measures y 7205-7221 (`px.py col 7360 7196 7234 2 acid1b,acid`): as drawn
  (y 7203-7221), not changed.
- `r5nor`: the west VSS pad's top edge is at y 2354-2355 (`px.py col 2405 2340 2372 2 acid1b,metal`):
  `D 2383,2355:2430,2398` (was 2362). The metal island's east edge line is at x 2554-2556 in both chips
  (`px.py row 2208 2530 2570 2 metal,metal1`): `M 2272,2184:2554,2232` (was 2543).
- `isrc`: the poly north of the pad (8964,18081) is x 8962-8980 (`px.py row 17950`, `row 17850 8946 8990 2`
  and `row 17770 8950 8990 2 acid1b,acid`): `P 8970,18081 8970,17900 8970,17735 w=18` (was x 8964-8966), its
  pad `P 8950,18064:8988,18098`; the tap contact's centre is (8966,16172) (`textmap.py 8942 16152 8992 16194
  3`): `C 8966,16172` (was 8962). The pad (8688,17737) has its stub west (`P 8650,17722:8680,17742`):
  nothing to add.

Connections before and after all of these:

```
tools/t.sh eof sameconn.py 278b6ae              ->  connections identical
.venv/bin/python tools/sameconn.py 278b6ae      ->  connections identical
```

Round 10: no findings that change a connection.

### Round 11 (full review of piece `isrc4`; 2026-11-19 16:39 to 16:52 +0000)

A fresh Claude Fable 5.2 reviewer agent, briefed with the piece's seven claims and nothing of the tracer's
reasoning; the commit under review was b3a8392. Images in `cache/scratch/eof/review-11/` (17).

**Told to suspect**: the two steps of the metal inside the bundle (a neighbouring track taken; the 9 px bar
at x 8164-8172 on the step y 16697); whether the track runs on through the tap pad (8100,16910); the pad
(8185,16303) against `bc1_g6_in`'s jog; the pad (8053,17735) against the other net's metal on the row
y 17736, and that metal's ends; the dark bars across that row in the gaps between metals; the L corner
(7967,14914) and the pad (7880,14914); the row y 14914 as one poly to x 7550 and `bc1`'s metal on it; all
round each of the five new pads; the rows' east ends under the rail x 8336-8384; pads or contacts along
the 1,390 px of x 7967 and the chip-1 blemishes on x 8057.

**Checked** (4-4.4x in two to four shots, with text maps and the extraction):

- The extraction: 2,397 nets, 0 errors, 0 warnings; `unsure.py` lists neither name; `rst_a` keeps its
  three gates and `bc1_g6_in` is a separate net.
- The step y 17301 (`step1.png`): three tracks each step one position; this one goes x 8057 to x 8103 in
  one piece. The step y 16697 (`step2.png`, `diff32.png`): three tracks each step two positions; this one
  x 8103 to x 8185; the bar at x 8164-8172 is one vertical line that also crosses the neighbouring track
  and the bare ground between them, an edge underneath; no ring or hole on the metal over the tan area.
- The tap pad (`tap.png`, four shots): ring and bright centre in both chips, hole in the clean shot, the
  track bright above and below; the row ends on the pad to the west and at about x 8325 to the east
  (`tap_e.png`), with no poly band across the diffusion box under the rail.
- The pad (8185,16303) against the jog (`pad3.png`, text map): bare ground y 16275-16283 in both chips,
  open field in the clean shot: separate.
- Row C (`rowc_w.png`, `rowc_e.png`, `pad4ctx.png`): no ring or hole under the four tracks; field between
  the pad (7968,16303) and the poly under the track x 7925; the east end as the tap row's.
- The track x 7967 (`trk7967.png`): straight, bars only at the row y 15868; a dark spot at (7966,15057) is
  on chip 2 only. The L corner and the pad (7880,14914) (`Lcorner.png`, four shots): a plain L; the row ends
  on the pad (pink east of it).
- Row E (`rowE.png`, `rowE_ctx.png`): orange poly in both open stretches (chip 2: 155/111/58 against field
  162/139/87); no ring or hole under `bc1`'s metal, RL3 or the rail x 7552-7598; the same y either side of
  x 7550, no step or pad.
- Row A (`rowA.png`, `padA_w.png`, `cornerE.png`): orange poly at the centre of every gap in both chips; no
  ring under the five vertical metals or along the lying metal (the dark stretch x 8267-8293 is on chip 1
  only); that metal is a through line with a corner at each end. The chip-1 blemishes on x 8057: chip 2
  whole in both its shots.

**Findings**: none. **The reviewer's closest call** (no finding): the pad (8053,17735) against the lying
metal, about 18 px between their edge lines (x 8072-8090); both chips read non-metal there (chip 2 red
151-157 against metal above 200), the level of the bare gap further north, and the other metal's west
edge runs straight through its corner with no stub: separate, as drawn (Ambiguity 29).

**Could not check**: the 4-6 px under each metal edge line on the rows; the chip-2 stripped shot under the
rails (fringes: those stretches rest on the clean shot and the two metal shots); the feature at
(8025,16632), not on this net's metal; `busl`'s, `lc3`'s and `lc2`'s part of the net west of x 7540.

Round 11: no findings.

### Round 12 (full review of piece `isrc5`; 2026-11-19 17:21 to 17:38 +0000)

Commit before the round: 32744d6. One fresh reviewer (Claude Fable 5.2), briefed with the piece's five
claims (stretches A-D and the join) and told to suspect: the lane of the diagonal under the metals at
x 5180-5350 (which vertical poly the row y 7257 comes from); the row through the crossing field; the pad
(6187,7257) (its row, the metal on it, what else touches it); the nested Ls at y 7982-8105 and the corner
(6558,7258); the contact candidate (6558,7886); the metal on another net's poly at y 7257; `eofw`'s arm on
the poly of stretch B and the three specks; stretch B as one poly under three metals; stretch A onto the
pad (6513,8538); all four pads all round. Images in `cache/scratch/eof/review-12/` (18).

What it checked and found as claimed: the diagonal's lane (one straight poly from the bend (5149,6912) to
(5494,7257), from the vertical poly x 5141-5161, field 32 px either side throughout in the clean shot,
chip 2 within 1 px of the drawn centre at the open cuts, no pad under the four metals: `d1_clean.png`,
`d1_acid.png` 4.5x, `d2_bend.png` 5.4x, `d3_metal.png`); the row y 7257 (straight, no ring, pad or hole
under any metal: `r1_row.png`, text maps); the pad (6187,7257) (the row's own, the metal ends on it from
the east, field north and south, no poly east: `p1_pad6187.png`, 5x); the track x 6558 (every dark bar
paired in both chips, no break, no side arm: `c6_track_s.png`, `c7_track_n.png`); (6558,7886) (green in the
clean shot, no ring or widening in either metal shot, unlike the contact (6513,7888) beside it:
`c4_7886.png`, 5x); the nested Ls (no metal at x 6552-6564, y 8026-8050: `c5_nest.png`); stretch B (one
poly, no contact with link F, `eofw`'s arm or the metal y 8448-8460: `b1_poly.png`, `b2_arm.png`,
`b3_gap.png`); stretch A (continuous with `lc2`'s line and on the pad: `a1_diag.png`); the extraction (the
piece meets only `lc2.txt:715` and `eof.txt:298`; `rst_a_n` = NOT `rst_a` FIRM; `unsure.py` lists none of the
three names). Not checkable, it said: what causes the chip-1 bar and the green at (6558,7886); the chip-2
stripped shot under the metals (fringes); `lc2`'s line beyond (6450,8630) and piece `x1`'s pad.

Findings, each checked by the tracer:

1. **Not a connection change (nothing in the trace changes)**: chip 1's metal shot has a 13 px dark bar
   across the west run at x 6544-6556, which the notes did not mention; chip 2 reads metal there. The
   reviewer reads it as a chip-1 blemish and asks for an ambiguity. **Confirmed as described**
   (`px.py row 7258 6520 6580 3 metal,metal1,acid1b`; `review-12/c2_corner.png`): recorded as Ambiguity 36,
   the trace's comment says so. No geometry changed.
2. **Comment only**: the poly under the metal y 7257 does not start at x 6313 with a square end; it is a
   vertical poly x 6313-6333 from the north that turns east. **Confirmed** (`textmap.py 6290 7196 6350 7250
   3`: salmon at x 6314-6332 from y 7199 down to the row). Ambiguity 34 and the trace's comment corrected.
   No geometry changed; still no contact.

Both fixes are comments (two lines of `trace/eof.txt`, the notes). The proof that no connection changed:

```
tools/t.sh eof sameconn.py 32744d6               connections identical
.venv/bin/python tools/sameconn.py 32744d6       connections identical
```

Round 12: no findings that change a connection.

### Round 13 (full review of pieces `rl` and `w5936`; 2026-11-19 18:15 to 18:36 +0000)

Commit before the round: ba2a174. One fresh reviewer (Claude Fable 5.2), briefed with the two pieces'
eighteen claims (per wire: the diagonal, the row, each pad, each metal with its corners, each poly column,
the diagonal metal and the join; for `w5936` also the pad in the track's run, the L onto `lc2`'s metal, the
row y 7888, the metal x 7402 and the poly's end on the box) and told to suspect: a lane slip of the three
diagonals under the metals at x 5080-5350 and the three bends; the pad (6513,7889) (no green hole in
chip 1's clean shot) and whether the metal runs on through it; the L at (6514,7978)-(6471,7978) beside
`lc1_w7040`'s pad (6471,7930); the hole-like patch at (6558,7886); (6645,7822); the nested Ls and the bare
ground between them; taps on the four long rows; the poly columns and `rst_ck`'s metal on `res_b`'s; the
two diagonal metals and the gap north of the pad (6556,8493); the east end. Images in
`cache/scratch/eof/review-13/` (24).

What it checked and found as claimed: the lanes (the bends at 5x in both stripped shots with field beyond
each, `a2_bends.png`, `px.py col 5190 / 5240 / 5063`; clean-shot cuts at each metal: one band per lane,
counted from `lc1_w7040`'s line to each source, no salmon between lanes, `j1_lanes4x.png` 4.2x; the rows
keep their order, cuts x 5560-6120); the first pads (rings in both chips, pitted boxes in chip 2, field
east: `k1_pads1.png` 4.5x); the nest at 4.4x in three shots (`c_nest_*.png`: each L on its own track, bare
ground between each corner and the next arm in chip 1 and the clean shot, the pad (6471,7930) apart from
the arm, x 6471 whole to (6470,8127)); the pad (6513,7889) (ring and centre in both chips, a pitted box in
the chip-2 stripped shot, the metal on south in line: a contact; `g1_rows_acid.png` 5x); (6558,7886) and
(6645,7822) (both metal shots as the neighbouring crossings, no pad, no pitted box: no contact); the
columns (one poly from pad to pad, no ring or hole under `rst_ck`'s metal or its corner, open poly between
(6556,8493) and the metal north of it in both chips); the diagonals (x + y = 15142 and 15206 onto `lc2`'s
ends, `rst_a`'s at 15080: `e_diag_*.png` 3.6x); the east end (the row ends on (7401,7888), bare ground to
(7402,7822), the poly ends on the box, the band above the box apart from it: `i1`-`i4`); the extraction
(2,386 nets, 4,345 transistors, 0 errors, 0 warnings; `sameconn.py 4b7f4be`: only the three joins). Not
checkable, it said: the diagonals under the metals at x 5080-5350 in chip 2 (fringes: only the clean shot
shows them); the box's strip east (not followed); the pad (6602,8320) was read at 2.75x and by text map
only.

Findings, each checked by the tracer:

1. **Not a connection change (comments only)**: seventeen tracks cross the row y 7878-7898, not sixteen:
   the notes' list left out x 6905, where there is no contact. **Confirmed** (`eof_mrun.py row 7860 6530
   7440 7915`: seventeen runs at both heights; the tracer's cut along y 7888 itself misses that track,
   whose metal is dim over the row in both chips: `textmap.py 6884 7866 6926 7910 3 --acid`, 7-B between
   the two bars, no ring, the clean shot salmon, `eof_cchk.py 6905,7888`: clean 53). The Logic table, the
   inventory, the trace's comment and the floor-plan line corrected.
2. **Not a connection change (comments only)**: undrawn poly Ls lie lengthwise under three of the
   east-going metals (`res_b`'s y 7216 from x about 6360, `lpstb_b`'s y 7173 from about 6402, `tl3_w3982`'s
   y 7303 from about 6270), as Ambiguity 34 records for `rst_a`'s; no pad, ring or hole on any.
   **Confirmed** (`review-13/f3_under.png`; `tl5_tracks.py h 7303 6170 6508`: no hole, chip 1 dim for
   20 px over the L's corner, chip 2 whole). Recorded as Ambiguity 39 and in the trace's comments.
3. **Not a connection change (comments only)**: chip 2's metal shot has a ring-like dark circle at
   (5665,7212) on the vertical metal over `res_b`'s row; chip 1 is bright and the row has no pad and no
   hole: a blemish. **Confirmed** (`review-13/b3_5665.png`; `eof_cchk.py 5667,7212`). Recorded as
   Ambiguity 40; the Logic table's "no ring in the field" now names the exception.

All three fixes are comments (`trace/eof.txt`'s comment lines, the notes, one word of the floor-plan
fragment); no geometry changed. The proof that no connection changed:

```
tools/t.sh eof sameconn.py ba2a174               connections identical
.venv/bin/python tools/sameconn.py ba2a174       connections identical
```

Round 13: no findings that change a connection.

### Round 14 (full review of piece `d3982`; 2026-11-19 19:24 to 19:43 +0000)

One fresh reviewer agent (Claude Fable 5.2), at commit `33ff44e`, images in `cache/scratch/eof/review-14/`
(26). Told to suspect: U2's and U3's node east of the rail (that the diffusion under the rail joins the
arm and the strip); the top of the band x 7416-7440 (that it turns west and touches neither U1's output
box nor U1's gate row); that each unit's gate row and output row are two polys at the band; a contact of
the row y 8030-8050 to any of the tracks it crosses, above all x 6431, 6471, 7396-7408, 6514, 6601, 6645
and the dim spot at (7075,8035); the corner onto `lc2`'s poly; the three ties drawn without `?` and any
other connection of a plate; field under the rail between the units and south of U4; U3 as a copy of U2;
anything left out in x 7410-7790, y 8060-8460.

What it checked, and found correct: the node east of the rail (`b1_u2node.png` 4.8x, `k_u2u3_*.png`,
`textmap.py 7570 8094 7666 8206 3 --acid`: diffusion tan without a break from under the rail to x 7610,
where rows with field show a pink stripe and a green rim; the arm unbroken from the plate's west end to
the tie box in three shots; the clean shot alone changes colour along the arm at y 8150, olive above and
salmon below, taken as an artefact; the gate poly does not cross the arm); the band's top
(`d1_bandtop.png` 4.5x: it turns west, field to U1's box and to U1's gate row in all four shots); the field
stripes at the band, and between U4's gate row and the pad (7401,8425) (`i1_u4pad.png` 5x: field reaches
x 7420 in three shots; a reddish line at x 7416-7422 in the chip-2 stripped shot is the thin metal's ghost
boundary); the row (`e1`-`e3` 4x, `f_spots_*` 5.5x, `m2_x7359.png` 5x, text maps of all 1,010 px: one poly,
no pad, ring or hole at any of the 21 crossings; chip-2 dim spots at x 7078, 6645 and 6514 are bright in
chip 1 with no hole; a blob at (6925,8030-8058) is in the clean shot only); the corner (`g1_corner.png`
5.5x); field under the rail between the units and south of U4 (`c1`, `c2` 6x); the tie boxes, plates and
VCC boxes (`j1`, `j2` 3.55x, `m1_u4south.png`: no hole and no poly leaving any plate); U3 as a copy of U2
(overlay); nothing left out in the region but U1 (`opendiff.py`: only a sliver at x 7784-7790, a separate
poly east of the VCC metal). Not checked: the VCC metal and the rail to a supply; `lc2`'s uncertain tie
behind the alias; the `findcell` scores; U3's tie box was seen at 2.85x only.

Findings, each checked by the tracer:

1. **Not a connection change (geometry)**: the node's exit east of the rail is y 8154-8174 (U3:
   8284-8302), drawn 8152-8184. **Confirmed** (`px.py col 7606 8140 8194 3 acid1b,metal1`: tan y 8158-8170
   between edges at 8149-8152 and 8173-8176; `col 7606 8270 8324 3`: the same 130 px lower). Fixed:
   `D 7594,8154:7628,8174` in cell `eof_dly`.
2. **Not a connection change (geometry)**: U2's VCC contact centre is about (7747,8143), drawn
   (7751,8136). **Confirmed** (`textmap.py 7726 8116 7774 8170 3`: bright centre x 7741-7753, y 8134-8155
   in both chips; U3's the same 130 px lower, `textmap.py 7726 8246 7774 8300 3`). Fixed: `C 7748,8143`.
3. **Not a connection change (a comment)**: the trace's comment said "twenty tracks"; there are
   twenty-one. **Confirmed**; corrected.
4. **Not a connection change (a comment)**: at x 6520-6590 the row lies in the 30 px gap between two
   horizontal metals (edges y about 8025 and 8055: the arms of `rst_a`'s and `res_b`'s Ls), not under
   them. **Confirmed** (`eof_mrun.py row 8012 ... 8062`: 6556(17) at y 8012 and 6580(57) at y 8062, nothing
   at y 8040 between x 6521 and 6595). The Logic table's row says so now.

The proof that no connection changed:

```
tools/t.sh eof sameconn.py 33ff44e               connections identical
.venv/bin/python tools/sameconn.py 33ff44e       connections identical
```

Round 14: no findings that change a connection.

### Round 15 (full review of pieces `ck5` and `rc`; 2026-11-19 20:13 to 20:26 +0000)

One fresh reviewer (Claude Fable 5.2), started for this round, at commit a9233e9; 15 images in
`cache/scratch/eof/review-15/`. It was given the two pieces' claims (each route stretch by stretch, the
four pads, the two joins) and told to suspect: the knot at (6472,9150-9235) (whether `ck5`'s vertical is
joined to the west arm and separate from the pad (6469,9209), with the follower running straight
through); the 225 px where `ck5`'s metal lies on `rc`'s poly and the dull patch at (6471,9045); the bend
of `rc`'s poly at (6472,8945); the poly x 6451 between y 6400 and 7107 (a step to a neighbour, a contact
under a metal, which poly the pad (6450,7127) is on); all round each of the four pads; a one-track slip
in the nested Ls at y 8156 and in the diagonal bundle; the track x 6688 over its rows and the corner
(6688,7128); the corner (6471,9452).

What it checked: the knot at 6x in four shots with profiles (the dip at x 6463 between arm and vertical
is one edge line, `rc`'s poly edge; no metal from y 9176 to 9202, the patch at y 9184-9192 open poly:
chip 1 161/83/36 against 233/159/79 for metal; the pad's metal leaves south only); the overlap y 8945-9172
(no ring, widening or hole; the patch at (6471,9045) is dirt on chip 2, chip 1 bright there); the bend at
4.8x in four shots (one diagonal turning south, no branch, field beyond); the poly x 6451 at 2.6x in three
shots (one lane, no step); the pads (6450,7127), (6645,8276), (6645,8580) at 5x in four shots (one poly
and one metal each; the first 15 px clear of the poly x 6408); the nested Ls and the diagonal (`ck5` is
the middle line; no slip); the track x 6688 and the corners (6688,7128), (6471,9452) (plain Ls at 5x in
both chips); the full extraction and `tools/unsure.py`. Not checked: `tc2`'s poly north of y 6400; `lc2`'s
and `lc3`'s own lines beyond the joins; the twelve row crossings of the track x 6688 one by one at 4x
(text tools and a 1.2x view only); the diagonal above 2.1x.

Findings, each checked by the tracer:

1. **Fourteen metals cross the poly x 6451, not thirteen**: the notes and the trace comment left out the
   one at y 6668-6682, where chip 2's metal is dim over the poly. No contact (chip 1's metal bright
   through, no ring, the clean shot salmon like the other crossings, the poly unwidened). Notes and a
   comment only: does not change a connection. **Confirmed** (`eof_mrun.py col 6474 6390 7110 6430`: 14
   runs in both chips, the seventh at y 6675; `px.py row 6675 6436 6468 4 metal,metal1,acid1b`: chip 2
   125-147, chip 1 183-211, clean 229/170/128). Fixed: the comment, the path table, Ambiguity 46.
2. **The arm of the L was drawn 4-5 px south**: the metal is y 8144-8158 in both chips, the trace had
   y 8149.5-8162.5. Geometry only. **Confirmed** (`eof_mrun.py col 6666 8120 8190 6660 6672`: centre
   y 8150-8152, 9-14 px). Fixed: `M 6450,7128 x6688 y8151 x6644 y8276 w=13`.

The proof that no connection changed:

```
tools/t.sh eof sameconn.py a9233e9               connections identical
.venv/bin/python tools/sameconn.py a9233e9       connections identical
```

Round 15: no findings that change a connection.

### Round 16 (full review of piece `n2n`; 2026-11-19 20:51 to 21:03 +0000)

One fresh reviewer (Claude Fable 5.2), started for this round, at commit 94ea9b7; 23 images in
`cache/scratch/eof/review-16/`. It was given the piece's claims (the four stretches, the three pads with
contacts, the join from (6775,10400) to `tl5`'s poly end, no tap and no branch) and told to suspect: which
of the three diagonals joins which column and which row, and whether they run parallel without a crossing
or a step; the pad (6146,6997) (its own metal, the poly's end, the neighbouring pads (6188,6953),
(6188,7040)); the corner (6991,7000) of three nested Ls; pads or contacts in the run of the track x 6991
and of the metal y 7000 (text only by the tracer, one overlay at 0.9x); the pad (6988,8427) and the poly
corner (6951,8428) (read at 4.2x, blurred); the column x 6951 under its three metals and beside the L
metal x 6920-6940; the pad (6947,8710) (a swapped line among four diagonals; a poly leaving it south or
sideways); the track x 6775 from y 8952 to 10400 (text only); the column x 5412 under nine metals and its
meeting with `tl5`'s poly end. The stretch south of y 10400 (not drawn) was not part of the review.

What it checked: the diagonal metal by cuts from y 8930 to 8780 and a view in both chips (x + y = 15727
throughout, no swap); the pad (6947,8710) at 4.5x with a text map (ring and centre in both chips, green
hole, field south: clean 193/118/128, open ground east and west); the column x 6951 (one poly, no hole or
ring under the three metals, the L metal beside it edge to edge without contact); the corner (6951,8428)
at 4.5x in two views with profiles (the poly turns east only: open ground west, pink field north; the
track x 6948 ends on its own pad (6905,8405)); the pad (6988,8427) (only the metal north and the poly west
leave it); the track x 6991 and the metal y 7000 (bars of 8-13 px only, no holes, no pads; the corner the
middle of three nested Ls); the pad (6146,6997) at 4.2x (the y 7000 metal is its own, built like the pads
(6188,6953) and (6188,7040), which are separate; field east: clean 190-199/117/125; poly west); the row
y 6996 (continuous; the notch at x 5692 is a metal-gap artefact; no contact under the 43 px metal at
x 5907 nor under x 6016); the three diagonals at the bends and at the arrivals (parallel, no crossing, the
trace on the middle one; no contact under the thin metal y 6848); the column x 5412 (no hole on any of
the nine metals, continuous across y 6350 onto `tl5`'s middle poly end); the extraction (`rcs_e3` = NOT
`bd1_n2`) and `tools/unsure.py` (nothing for the net). Not checked: "field beyond the pad" rests on
the clean shot alone (the chip-2 stripped shot shows only fringes under the metal ghosts there);
`follow.py` was not run; south of y 10400; the two neighbouring lines of the diagonal bundle.

Findings, each checked by the tracer:

1. **Ambiguity 48 and the trace comment understated the crossings of the track x 6775**: two more poly
   rows cross under it, at y 9984-9998 and y 10048-10064 (the rows of the neighbours' pads (6818,9988) and
   (6730,10050)); the pad (6818,9988) has its ring 18 px from the track; and "no clean-shot hole at any of
   them" was not so: the clean shot is greenish under the track at (6775,9797) and dull at (6775,9623).
   The reviewer reads all of it as no contact (trap 15). Notes and a comment only: does not change a
   connection. **Confirmed** (`eof_rows.py col 6795 9960 10080`: rows at y 9986-9994 and 10056 in both
   stripped shots; `px.py row 9988 6762 6840 4 metal,metal1,acid1b`: the track 192-221, then 113-161 red at
   x 6790-6798 in both chips, which is not metal, then the pad's ring; `px.py col 6775 9785 9810 3`: clean
   126/145/74 at y 9797 with both chips' metal 187-222 through; `col 6775 9612 9634 3`: 148/143/69 at
   y 9624). No contact: the metal keeps its 13 px and its brightness in both chips, the rows are not
   widened, and the same patch lies under the neighbouring tracks. Fixed: the comment of stretch A in the
   trace, the path table's rows, Ambiguity 48.
2. **The other three pads of the staircase belong to the tracks x 6645, 6689, 6733**, not "x 6660, 6690,
   6732" as the path table said. Notes only. **Confirmed** (`eof_mrun.py row 9000 6620 6800 8950 8900 8850
   8800`: 6646, 6688, 6732, 6775 at y 9000 and three diagonals at x + y = 15532-15544, 15597, 15662).
   Fixed: the table.
3. **The package extracted by itself reports two "several names" errors**, at (4724,2813) and (4497,5634),
   neither on this net. Not a finding against the piece: the two errors were there before it (the Status
   section's counts since run 11: 2 errors and 47 warnings; `tools/t.sh eof sameconn.py 61d3be5` differs
   only by this piece's join), names of other packages' nets seen with only some trace files loaded; the
   full extraction has 0 errors and 0 warnings. Nothing changed.

The proof that no connection changed (the fixes are comments and notes; the geometry is as reviewed):

```
tools/t.sh eof sameconn.py 94ea9b7               connections identical
.venv/bin/python tools/sameconn.py 94ea9b7       connections identical
```

Round 16: no findings that change a connection.

### Round 17 (full review of pieces `ck6` and `ck7`; 2026-11-19 21:44 to 22:12 +0000)

A fresh reviewer (Claude Fable 5.2), briefed with the two pieces' claims as they stood at commit 05563d2
(`ck6`: the clock's wire from `busl`'s row end and the inverter U; `ck7`: the unit V drawn as an inverter of
`eof_w15172` with a hairpin pull-down, its wires and its metal south) and told to suspect: the hairpin's
join and its west ends, the diffusion between the two rows and the channels' east edge, the two tie boxes
and V's plate pad, the dim metal south of that pad, the two thin metals over the four boxes, the row
y 14825 under the VSS band (a step, a contact), its turn beside the neighbouring pad, the corner
(8882,14785), the bus metal's identity at the west end, the four supply contacts, and anything undrawn
inside the two units. It used 67 tool calls; images `cache/scratch/eof/review-17/`, read at 3.3-5x in
two to four shots, with `px.py`, `textmap.py` and `railprof.py`.

Findings:

1. **An undrawn transistor on V's tie tail** (piece `ck7`; changes a connection). The tail was drawn to end
   at the tie box; under the thin metal x 8637-8650 its diffusion runs on south to y about 15257, and a
   poly arm (y 15204-15228, one poly with the column x 8597-8620) crosses it. **Confirmed** (`px.py col
   8643 15100 15300 5 acid1b,acid`: tan 201-204/178-184/137-140 at y 15235-15250 like the strip's
   198/179/137, pink at y 15265, the arm 240-247 red; `textmap.py 8612 15184 8700 15292 4 --acid`;
   `q_f1.png`, 5.2x, four shots). Read further here: the pocket below the arm and the west part of V's VSS
   box are separated by one dark line only (the bar of the open gap), so the transistor is believed a
   pull-down of `eof_w15127` to VSS, and its gate's poly runs south to the plate of the unit below (seen
   at 2.9x): V would be one side of a cross-coupled pair. Not an inverter in any case.
2. **A second diffusion strip under the thin metal x 8789-8801** (piece `ck7`; changes connections). From
   V's box pad south to y about 15425, x about 8779-8795, crossed by rows A and B and by three more rows
   (y 15252, 15340, 15384); its lower end not established. **Confirmed as a diffusion** (`px.py col 8786
   15090 15450 8 acid1b,acid`: tan 191-202/178-185/136-142 between the rows from y 15194 to 15418, pink
   193-198/120-123/130 at y 15090-15106 and from y 15434; `q_f2.png`, 3.6x, three shots: a dark line down
   its east side at x 8797; `px.py row 15260 8736 8862 6`: the row y 15250-15270 has the diffusion's west
   edge as a dark line across it at x 8754). The open gap between the rows is field, as drawn
   (`tools/eof_patch.py 8750 8770 ...`: chip-2 stripped shot red minus green 3-5 on the two strips between
   the rows, 18-21 on the nodes), so what the strip's segments are joined to is not read; as it stands it
   would link V's node to the next unit's box pad through three gates.
3. **The pad (7837,14784)'s poly reaches x about 7863** (drawn to 7854; piece `ck6`; geometry only).
   **Confirmed** (`textmap.py 7842 14766 7884 14802 3`: salmon to x 7863, pink from x 7866). Fixed:
   `P 7820,14768:7864,14800`.
4. **The contact (8705,15262) centres nearer (8700,15260)** (piece `ck7`; geometry only). Not re-measured:
   the piece is withdrawn; the remark is in the table "The unit below the inverter".

Found correct by the reviewer: the hairpin joined at x 8872-8895 with both rows ending at x 8694; V's
plate and pad one poly, its contact, the metal south and its end on the pad (8592,15383); all four supply
contacts; no hole under the bright centres over the four boxes (blue 131-140 against 96 at the known
contact (8642,14910)); U's stack, tab, gate end and plate; the row y 14825 one poly without step or
contact (the dark spot (8570,14833) in chip 2 only); the turn and the pad (8967,14870) apart from the pad
(9008,14828); the metal x 8968, the row y 15042, the corner (8882,14785), the pad (9054,14785), the poly's
turn and the metal y 14656 without contact; the west end one bus line with both pads and no tap. Not
checked: whether poly enters either tie box; the row y 14825 at full length at 4x (text maps only); the
two new diffusions south of y 15285.

Outcome. Findings 1 and 2 are both in unit V and both mean the unit is not complete: finishing it needs
the unit below it read as well (the arm's poly and the strip both run into it), which is a piece of its own.
A half-drawn unit stays out of the trace: **piece `ck7` is withdrawn** (its drawing is
`cache/scratch/eof/draft-ck7.txt`; what is read is in the Logic section's table and in Not done). Piece
`ck6` stays as reviewed, with finding 3 fixed and three changes that the withdrawal made necessary: the
gate pad's metal x 8838 and its south pad (8833,15127) moved from `ck7`'s lines into `ck6`'s (the same
geometry), the two rail pieces shortened to the inverter (y 15070), and the label `eof_w15127` on that
metal. Against the reviewed commit:

```
tools/t.sh eof sameconn.py 05563d2               CONNECTIONS DIFFER (5 differences)
.venv/bin/python tools/sameconn.py 05563d2       CONNECTIONS DIFFER (5 differences)
```

The five are the withdrawal and nothing else: the name `eof_w15172` gone, V's three transistors gone (the
load and the two pull-downs), the equation of `eof_w15127` gone. `lc3_w9947` = NOT `eof_w15127` is as
reviewed.

Round 17: two findings that change a connection, both in piece `ck7`, which is withdrawn; one geometry-only finding in piece `ck6`, fixed.

### Round 18 (fix check of round 17's changes; 2026-11-19, after commit b7624fd)

A fresh reviewer (Claude Fable 5.2), briefed with the three findings of round 17 and with what changed
since commit 05563d2: the removal of piece `ck7`, the widened pad (7837,14784), and in `ck6`'s lines the
gate-pad metal x 8838 with its south pad (8833,15127), the two shortened rail pieces and the label. Five
images in `cache/scratch/eof/review-18/`, with column profiles and text maps.

- `tools/t.sh eof sameconn.py 05563d2` and `.venv/bin/python tools/sameconn.py 05563d2`: the same five
  differences, all intended (the name `eof_w15172`, unit V's three transistors, the equation of
  `eof_w15127`); `lc3_w9947` = NOT `eof_w15127` stays.
- Round 17's finding 1 confirmed again (`c_find1.png`, column x 8643: diffusion tan at y 15190-15203 and
  y 15232-15252 south of the tie box, a poly band y 15206-15228 across it at channel colour, field
  186/126/128 on the same column) and finding 2 (`d_find2.png`, column x 8788: a diffusion-coloured strip
  from the output box to about y 15420, crossed by five salmon bands and passing a second box at
  y 15290-15315): the removal was warranted.
- The inverter is not affected: field under both thin metals between it and unit V (x 8643, y 15048-15108;
  x 8793, y 15066-15110).
- The pad (7837,14784): salmon to x 7857, outline to x 7862, field from x 7864; nothing else near it.
- The gate-pad metal: one metal, x 8829-8846, bare ground both sides and beyond both pads; over the row
  y 15034-15050 two edge bars, bright between, no hole, no widening; the pad (8833,15127) is a contact
  (ring and bright centre in both chips, green hole in the clean shot).
- Both shortened rail pieces cover their contacts ((8712,14965), (8534,15033)); the label lies on the metal.

Round 18: no findings.

### Round 19 (full review of piece `vw`; 2026-11-20 00:05 to 00:36 +0000)

A fresh reviewer (Claude Fable 5.2), briefed with the piece's claims as they stood at commit 3d76317 (units V
and W as a cross-coupled pair of 13 transistors, each stack in two fingers, an uncertain link between the
segment between rows B and C and V's ground) and told to suspect: that link and the open gap's colour; the
row of the pad (8592,15383) against row 2; the rows' west ends; the three links across the west gap; the
strip's segments and the widening under row C; the arm's poly into W's plate; row C's west end and its run
to the pad (8966,15260); the dim metal x 8580-8604 over W's plate; every metal over a box or a row; the tie
boxes, W's output box, the supply contacts; the corner (8925,14828) and the pad (9008,14828); anything left
out. It used 79 tool calls and 17 images (`cache/scratch/eof/review-19/`, 4.1-6x in two to four shots), with
`px.py`, `textmap.py`, `railprof.py` and `follow.py`.

Findings:

1. **The stacks' diffusion runs through the open gap x 8742-8777 east of the rail; the "second finger" is
   not a separate strip** (changes a connection: four transistors fewer, two pairs of closed nodes become
   one each, the uncertain link becomes part of a plain diffusion; no equation changes). The trace had
   field in the gap under rows A, B, 1, 2 and between them. The reviewer: no diffusion edge crosses those
   rows or the bands between them in x 8738-8778 in either metal shot or the chip-2 stripped shot, though
   the same rail's diffusion edge is plain where it borders field (x 8744-8748 at y 15430-15445) and row C
   has its edge at x 8754; the nodes keep their colour down to the rows' edge lines, which are single; the
   one doubled line is row C's top edge west of x 8757, where the boundary that comes up x 8754 turns west
   to the rail. Against (the reviewer's own): the three bands have field colour in the stripped shot.
   **Confirmed**, by profiles of my own: `px.py row Y 8730 8802 3 metal,metal1,acid1b` on rows A, B, 1, 2
   (red 152-186 in chip 2 from x 8742 to 8778, no dip; the known edges dip to 50-65 at x 8766 on the
   inverter's gate and x 8754-8757 on row C); `px.py col X 15150 15282 2` in three shots for X = 8746,
   8750, 8764, 8770, 8850 (row C's top edge 30-36 / 33-43 / 43-49 and 9 px wide at x 8746-8750, against
   57-71 on every other poly edge and on the same edge at x 8764-8770) and `col X 15300 15432 2` (rows 1
   and 2: single lines; no line between W's node and row 1's edge). Fixed: both stacks' diffusions drawn
   through the gap (`D 8738,15118:8780,15246`, `D 8738,15309:8780,15424`), the `?D` link removed. The
   contrary colour is Ambiguity 53.
2. **W's node strip east of the west gap is y 15308-15316** (drawn from y 15302; pink above; geometry
   only). Confirmed (`px.py row 15310 8640 8712 4`: tan from x 8672; the text map of run 16 has pink at
   y 15305, x 8677-8731). Fixed: `D 8668,15308:8700,15316`.
3. **Row C's west end is x 8738** (drawn 8746; geometry only). Confirmed with finding 1 (the end lies on
   field west of x 8754). Fixed.

Also noted by the reviewer, no contact (added to Ambiguity 57): the bus metal y 14648-14660 on the
hairpin's poly row, the hairpin's metal y 14785 over `bc2_w15607`'s poly column.

Found correct by the reviewer: the row of the pad (8592,15383) and row 2 are two polys (clean shot and
both metal shots; the stripped shot undecided); rows A/B and 1/2 not joined at their west ends; the arm
apart from row B, one poly with W's plate, 18 px of field from V's plate pad; V's pocket and W's foot
across the west gap (W's node strip unreadable inside that gap, tan from x 8668 east); no contact under
either thin metal nor under the metal x 8580-8604 on W's plate; row C to the pad (8966,15260) under the
track x 8925 without contact; all pads and supply contacts; the pad (9008,14828) 15 px of field from the row
y 14825; the ports go on; nothing left out. Not checked: whether poly enters either tie box (W's tab ends
at x 8635 and the box starts at x 8646: the `?` stands); the colour question of finding 1.

Against the reviewed commit, after the fixes:

```
tools/t.sh eof sameconn.py 3d76317               connections identical
.venv/bin/python tools/sameconn.py 3d76317       connections identical
```

(both with the note "each [transistor] added or removed lies in parallel with one that is on the same
three nets on both sides": `sameconn` does not count the four transistors that went, nor the two pairs of
unnamed closed nodes that became one each). The finding is treated as one that changes a connection all
the same (a transistor's existence), so a fix check follows.

Round 19: one finding that changes a connection (the stacks' diffusion through the open gap), fixed, with two geometry-only findings.

### Round 20 (fix check of round 19's changes; 2026-11-20 00:40 to 00:58 +0000, after commit 873de81)

A fresh reviewer (Claude Fable 5.2), briefed with the three findings of round 19 and with what changed since
commit 3d76317 (both stacks' diffusions drawn through the open gap east of the rail, the uncertain link
removed, W's node strip, row C's west end). 35 tool calls, nine images in `cache/scratch/eof/review-20/`,
with profiles in three or four shots.

- `tools/t.sh eof sameconn.py 3d76317` and `.venv/bin/python tools/sameconn.py 3d76317`: connections
  identical; the four transistors fewer are the old finger pairs merged; no uncertain diffusion is left on
  the path.
- Finding 1, right. Under rows A, B, 1, 2 no dark line between x 8739 and 8779 in the chip-2 metal shot,
  the rail's and the thin metal's edge lines (centres x 8735, 8783) no wider than north of V, channel up to
  both protection boundaries in the clean shot; no vertical edge in the bands between the rows in three
  shots (their colour in the stripped shot is field-like, +5 to +10 against +20 for W's node and the foot:
  "the reading rests on edges, not colour": Ambiguity 53); under the rail the tan runs unbroken from the
  band between B and C into the VSS box (x 8716-8736, y 15234-15250, three shots); the edge at x 8755
  crosses row C in four shots with dimmer poly west of it; the transistor under row C is `rst_a`'s, between
  `vss` and `eof_w15300`, 43 wide. Nothing touched: row C 5 px clear of the new diffusion, the buried
  contacts cover both output rows.
- Finding 2, **geometry only**: the strip's top edge line is centred y 15300-15302 across x 8668-8730 with no
  step at x 8676 (clean shot and both metal shots); y 15308 is where the tan starts, not the edge.
  Confirmed (`px.py col 8690 15292 15326 2 acid1b,metal,metal1`: the line's minimum at y 15300, tan from
  y 15306; the same at x 8712). Fixed: the strip is one rectangle again (`D 8560,15302:8700,15316`) and
  W's stack starts at y 15303 under the rail.
- Finding 3, right; **geometry only**: the end may lie 5 px further west (a red outline at x 8732-8734 in
  the clean shot). Fixed: `P 8736,15251:8950,15270` (6 px clear of the VSS box).

Connections before and after these two geometry-only fixes (against commit 873de81):

```
tools/t.sh eof sameconn.py 873de81               connections identical
.venv/bin/python tools/sameconn.py 873de81       connections identical
```

Round 20: no findings that change a connection.

### Round 21 (full review of pieces `in390` and `in172`; 2026-11-20 01:30 to 01:49 +0000)

One fresh reviewer agent on Claude Fable 5.2, read from the photos alone; trace at commit befa9bc; its images
(16) and three scratch scripts in `cache/scratch/eof/review-21/`.

Told to suspect. `in390`: the crossing (9014,14656) of `bc1`'s bus metal over the poly column and the 185 px
where the bus metal y 14603-14618 lies on the row (contact or not; the column's odd colour in the clean
shot); the pad (10092,14609) without a green hole; whether the row keeps its track over 1,070 px and whether
a vertical metal taps it; the 910 px metal on x 10268 (its corner, taps, and that it is not the neighbour on
x 10225). `in172`: the step at x 10284-10302 (one poly; no continuation west of the lower row or east of the
upper one to pad A); unit T read without the clean shot (the body's extent, rows 1 and 3 crossing all of it
and stopping before the rail, the output box a buried contact on the node, the bands reaching VSS contacts);
the strip under the VSS rail (diffusion, continuous, no contact to the rail); the tie box drawn as certain;
the foot of the metal x 10355 onto `bc2`'s pad (trap 16) and pad B's metal onto `bc2`'s; anything left out
in x 10470-10780, y 14590-14790.

What it checked, and how: the column and its four crossings (4.2x in four shots, 7.5x): protected poly with
no hole at y 14699, 14742, 14785; at (9014,14656) no ring in either metal shot, the poly 20 px wide with no
pad, the clean shot dark olive (84/89/31) and not a hole, chip 2 ordinary poly (161/116/59): the tint is
chip 1's clean shot only (it agrees with Ambiguity 58 as written). The row under the bus metal (5x, four
shots): no ring in either chip, pink field west of x 9003. Both rows to x 10078 and x 10302: the same y
under all three wide metals (`railprof.py`; 3.9x), poly over field, red minus green 42-62 under every
crossing metal, no branch in the open stretches. The pad (10092,14609) at 6x: ring and bright centre in both
chips, a rounded box in the chip-2 stripped shot, nothing else leaving it. The metal to `bc2`'s pad (6x and
`follow.py`): a plain corner, 20 px of bare ground to the metal north of it, no hole beneath it, end at
(10265,15614); the neighbour on x 10225 ends separately at (10223,15570). The step (4.6x, four shots): one
L, no row west of the metal at y 14687-14704, field between the step and pad A. Unit T (5-5.4x): body edges
x 10490-10494 and 10530-10534; rows 1 and 3 poly to x 10536, stopping before the rail; the output box like
`bc2`'s box at (10506,15000), with node diffusion east of it; the strip under the rail two edge bars with
bright metal between in both chips, no ring; the tail diffusion, the tab poly, the tie box heavy-outlined
with a light centre in both chips; the plate not under the VCC rail. Pad A's foot (6x): it ends in the ring
of (10395,15000), 10 px dark either side of the centre. Pad B's metal (4.6x): dim in chip 2 at
y 14896-14936, clearly metal in chip 1, an unbroken protected strip in the clean shot to the pad
(10441,14955). The extraction: 0 errors, `eof_w15172` FIRM.

Findings: none ("nothing changes a connection, and no geometry error is worth a fix").

What it could not check: unit T in chip 1's clean shot (residue); a contact on the stained stretch
x 9005-9060 from the clean shot (both metal shots say none); `bc2`'s own readings and the rails' identity as
supplies.

Round 21: no findings.

### Round 22 (full review of piece `in350`; 2026-11-20 02:14 to 02:30 +0000)

One fresh reviewer agent on Claude Fable 5.2, read from the photos alone; trace at commit e2efee7; its images
(20) in `cache/scratch/eof/review-22/`.

Told to suspect: the pad (8598,17908) (whether both metals are on it, trap 16); the stretch y 17649 where the
metal lies 300 px on another net's poly (a contact, pad, ring or hole along it or at its corners; whether the
poly is another wire); the two through pads (8882,16648), (8882,16867) (the metal continuing through each; a
second poly east of the lower pad, where chip 1's clean shot has reddish patches; chip 1's metal missing on
the track x 8838 over that pad's row); the step at y 15698-15915 (separate from the pad (8882,15745), its
metal and the metals on x 8925 north and south); the poly hop between the pads (9596,17909) and (9769,17910)
(one poly, no contact to the two vertical metals, the metal east unbroken to `trunks`' `ck_out #1`, nothing
else on the pads); the pad (8424,17908) (the dim metal from the west, the metal from the north); pads, taps or
jogs hidden in the long follower-read stretches.

What it checked, and how: the extraction (the claimed equation, no `?` on the path); the step (4.2x): separate
from the pad (8882,15745), its metal and both metals on x 8925; both through pads: the metal continues, no
second poly, no contact of the track x 8838 at either row (chip 2 whole, no hole); the long runs: no pad, tap
or jog; the stretch y 17649 and both corners: no ring, no hole, the poly beneath turning south at x 8572-8588;
the pad (8598,17908) at 6x: both metals on it; the hop: one poly, no contact to the wide or the thin vertical
metal; the metal east of (9769,17910): one metal with `trunks`' `ck_out #1`, no contact at x 10216; the poly
west of (8598,17908): no contact under the rail or the thin metal; at the pad (8424,17908) the north metal
ends on the pad and the poly goes on west.

Findings:

1. **The metal west of the pad (8424,17908) is not on the pad** (changes a connection: a contact's metal and
   where a wire leaves the package). The trace had `M 8424,17908 x8380 w=14` and the port `ck_out` M
   (8380,17901-17915). `px.py row 17908`: the metal ends at x 8390, then 10 px of open-poly colour, then the
   ring; the chip-2 stripped shot's ghost ends at x 8390; 33 px without metal against 17 px for the north
   metal's ring; the metal probably turns north onto a pad (8382,17862) of the track x 8382
   (`review-22/p8424_m.png`, 6x, `p8424_ctx.png`, `p8424_ctx2.png`). **Checked by me** (`px.py row 17908 8376
   8424 3 metal,metal1,acid`: 151-152 / 104-122 / 51-54 and 132-146 / 59-80 / 43-45 at x 8400-8403, orange
   poly in both chips, against 187-203 / 152-174 / 64-81 on the metal; the stripped shot pale to x 8388 and
   dark beyond; `px.py col 8384 17850 17912 4`: bright in chip 1 at y 17886-17890; the reviewer's
   `p8424_ctx.png`: the metal's end bends north to the pad's ring at (8382,17862), and the pad (8424,17908)
   stands apart). **Confirmed.** I had read the 12 px as dim metal from brightness alone (Ambiguity 66 as
   first written); the colour says poly. Fixed: the stub and its port removed, the poly stub shortened to
   x 8392, Ambiguity 66 rewritten.
2. **The pads (9596,17909) and (9769,17910) each carry an undrawn metal from the north** (changes a
   connection: two branches of the net missing, two places where the wire leaves the package). Tracks
   x 9589-9604 and x 9762-9778 end on the pads with the same ring (y 17886-17903) as the piece's own north
   metal on the pad (8598,17908); no metal south of either; protected pink above both in the clean shot
   (`review-22/hop_n.png`, `hop_pads5.png`, 5x). **Checked by me** (`tl5_tracks.py v 9596 17580 17935`: metal
   from y 17602 to the ring y 17886-17903, bars of 8-11 px only; `v 9769 17620 17935`: from y 17646, the same;
   `v 9596 17910 17990` and `v 9769 17912 17990`: no metal south; the reviewer's `hop_pads5.png`: a bright
   track down to each ring in both chips). **Confirmed.** My view of the hop (`r18_e1.png`) began at y 17865
   and showed 20 px of each track above its pad, which I did not look at as metal on the pad: trap 32 (look
   all round every pad), not applied at these two. Fixed: both drawn as stubs to y 17866 with ports; the
   follower's readings of where they go are in Not done.
3. **A poly lies under the track x 8925 beside the pad (8882,16867)** (x 8918-8935, y 16830-17000, turning
   west at y 16992), 18 px from the pad, not mentioned in the notes; the gap between is bare ground in both
   metal shots, no join: the trace stands (`review-22/pad2_ctx.png`). Not a finding against the trace; added
   to Ambiguity 64.

After the fixes: `tools/t.sh eof sameconn.py e2efee7` ends `connections identical` and `.venv/bin/python
tools/sameconn.py e2efee7` ends `connections identical` (the tool compares nets and transistors: the removed
stub and the two new ones are all on `ck_out` and end on nothing drawn; what changed is where the net leaves
the package, which it does not see). Full extraction 2,378 nets, 4,372 transistors, 0 errors, 0 warnings.

What it could not check: where the two north tracks and the stubs at (8424,17908) go; the gates of the two
pad rows; chip 1 at (8838,16866), where its metal is missing.

Round 22: two findings that change a connection, fixed; a fix check follows.

### Round 23 (fix check of round 22's changes; 2026-11-20 02:34 to 02:39 +0000, after commit e2efee7)

One fresh reviewer agent on Claude Fable 5.2, briefed with the two findings and `git diff e2efee7 --
trace/eof.txt` only; trace at commit 86e3897; its images (7) in `cache/scratch/eof/review-23/`.

What it checked, and how. (1) The pad (8424,17908): the west metal ends at x 8388 (the follower at `--gap 16`,
both metal shots); `tl5_tracks.py h 17908`: no metal in either chip for x 8388-8420, 32 px, against the pad's
17 px ring on the north side; open poly at x 8396-8405, the same colour as the known poly east of the pad at
x 8447-8450; no hole in the clean shot along x 8300-8415, so that metal has no contact on the poly; its end
widens north at x 8370-8388, a corner toward the pad (8382,17862); the poly west is continuous into the pad
(red minus green 40-50 throughout); nothing else on the pad (field south; the north metal crosses the poly row
y 17853-17870 without ring or hole). (2) The pads (9596,17909) and (9769,17910): each north track is a single
track at y 17866 (x 9590-9604 and x 9763-9778, open poly either side) and ends at y 17886 with an 18 px ring
before the bright centre, the same as on the pads (8598,17908) and (8424,17908); each pad's own line has a
ring of the same class (13 px west at 9596, about 20 px east at 9769); no metal south of either pad; the clean
shot's protected strip runs into each pad; no contact where the stubs cross the poly row y 17853-17870.
(3) `tools/t.sh eof sameconn.py e2efee7` and `.venv/bin/python tools/sameconn.py e2efee7`: both `connections
identical`; the four changed port lines sit on the drawn stub ends, and `tools/ports.py` shows no lost partner.

Findings: none. An observation, not a finding: the other net's metal west of x 8390 is drawn by no package
(it is in Not done).

Round 23: no findings.

### Round 24 (full review of pieces `lat16` and `inv16`; 2026-11-20 03:08 to 03:35 +0000)

A fresh reviewer (Claude Fable 5.2), briefed with the two pieces' claims as they stood at commit 81f6ac5 (the
two cell copies, the rails, the foot box, the VCC contact, the thin metal x 8588-8600 with its two contacts,
the six rows east of the cells with their ends, the three equations; the inverter's diffusion under the
rail, its gate row and pad, the output strip, box and poly under the track x 8838, the load and its uncertain
tie, its equation). The two were reviewed together though the inverter is drawn by hand and the latch is a
cell copy: they are one group of 13 transistors in one 580 x 690 px region, and the latch's data is the
inverter's output. Told to suspect, for `lat16`: every pad and row end of the copy against the master; the
top pad and its thin metal; the contact (8594,16846); every crossing of the rows under the tracks x 8838,
8882, 8925, 8968; the pad (9012,16693) and the 100 px of its metal over the poly column; the column and the
port (9062,16735); the clear row's step and its join to `rst_a`'s pad; the foot box; the rails' names. For
`inv16`: which pieces east of the rail along y 16421-16443 are poly and which diffusion, the box, the pale
band; a contact between the poly and the track x 8838; whether gate row and plate are one poly; the gate
row's west end; the load's path; the diffusion under the rail; the pad (9010,16388). It used 97 tool calls and
25 images (`cache/scratch/eof/review-24/`, 2-5x in two to four shots, the copies side by side with the
master), with `px.py`, `textmap.py`, `railprof.py`, `tl5_tracks.py` and `follow.py`.

Findings:

1. **The lower node's row has a branch that was not drawn** (changes a connection: `eof_w16823` leaves the
   piece at a third place and gates a pull-down of an undrawn unit; no equation of the pieces changes). Under
   the track x 8925 the row y 16813-16832 is one poly with a column x 8917-8935 that runs south to y 17003 and
   west along y 16985-17003 to the rail, where `railprof` gives a gate at y 16988-16999 directly south of the
   foot box. **Confirmed by me**: `px.py col 8926 16800 17010 6 metal,acid1b,acid` (the clean shot salmon,
   212-232/135-175/84-127, without a break from y 16818 to y 16998 and pink, 187/120/126, north of the row; the
   chip-2 metal bright through y 16832 with no edge bar; the stripped shot red over green by 20-80);
   `tl5_tracks.py v 8926 16790 17020` (no hole, no ring); `eof_rows.py col 8905 / 8860 / 8780 / 8760 16960
   17030` (a poly at y 16988-17003 at each); `railprof.py 8702 8738 16900 17060` (gate 16988-17010);
   `s19_r1.png` (2.9x, clean and chip-2 stripped: the column and the leg plain). My view of the rows
   (`s19_g.png`) ended at y 16890 and I took the salmon under that track for the field's pink; Ambiguity 64's
   "reddish patches" lie beside this column. **Fixed**: `P 8917,16826:8935,17003`, `P 8760,16986:8935,17003`,
   a port at (8760,16986-17003).
2. **The strip under the inverter's plate is y 16380-16409 (drawn 16388-16410), and the output strip
   y 16422-16434 (drawn to 16437)** (geometry only). Confirmed: `px.py col 8642 16366 16420 3 acid1b` (edge
   lines y 16378-16381 and y 16408-16411), `px.py col 8755 16412 16446 3 metal,acid` (bright y 16424-16431).
   Fixed: `D 8556,16381:8664,16409`, `D 8738,16422:8782,16435` (the load is 28/92).
3. **The VCC diffusion under the west rail is taller than the cells' boxes** (y 16497-16622 and y 16656-16925),
   **with an undrawn long contact at about (8535,16860)** (geometry only: `vcc` onto `vcc`). Confirmed:
   `railprof.py 8514 8556 16480 16960`; `eof_cchk.py 8535,16860` (5; 224/217, long north-south). Fixed: two
   diffusion rectangles and the contact added; no poly crosses them.
4. Left out, no connection of the pieces (recorded under Not done): a large diffusion x 8900-9240,
   y 16478-16606 under the tracks, with no contact from the tracks x 8925, 8968, 9056; the through metals
   x 8838, 8925, 9056 and the thin metal x 8643, which no package draws.

Checked and found correct: both cell copies against the master (side by side at 2x, clean and metal), the top
pad and its thin metal; the contacts (8594,16648) and (8594,16846) (the lower has the same pit in the chip-2
stripped shot as the upper: Ambiguity 68); every crossing of the six rows and of the gate row under the four
tracks (no ring, no hole); the pad (9012,16693) (metal south only, 14 px of field to the column's corner, no
contact over the column); the column and the row y 16724-16745 as one poly, no contact under x 9056; the clear
row's step and its pad; the foot box; the rails by structure; of `inv16` the strip, the box and the output
poly east of the rail (strip blue 85 against poly 56; the pale band is field), no contact on the track x 8838
from y 16421 to y 16616, the plate and the gate row separate (plain diffusion in the gap), the pad
(9010,16388). Could not settle: the gate row's west end at x 8682-8696 (poly-coloured to y 16412 with a bar at
y 16402 in both metal shots; read as no tie to the node: Ambiguity 70); the three load ties; the continuity of
the thin metals over boxes (x 8771 at y 16806-16900, x 8643); what lies beyond the port (9062,16735).

After the fixes the extraction's connections are the same as at the reviewed commit (the branch is a wire
with no drawn load):

```
tools/t.sh eof sameconn.py 81f6ac5              connections identical
.venv/bin/python tools/sameconn.py 81f6ac5      connections identical
```

Round 24: one finding that changes a connection (a third exit of `eof_w16823`), fixed; two geometry-only, fixed.

### Round 25 (fix check of round 24's changes; 2026-11-20 03:38 to 03:48 +0000, after commit 81f6ac5)

A fresh reviewer (Claude Fable 5.2), briefed with `git diff 81f6ac5 -- trace/eof.txt` and round 24's three
findings in one line each (the branch of `eof_w16823` under the track x 8925; the two strips of the inverter;
the taller VCC diffusion with its contact), and asked whether each change is right, whether the column is one
poly with the row and with the leg, whether it touches a metal, the pad (8882,16867) or anything else,
whether x 8760 is on the leg, and whether any poly crosses the added diffusion. It used 29 tool calls and 9
images (`cache/scratch/eof/review-25/`), with `px.py`, `textmap.py` and `sameconn.py` (identical both ways
against 81f6ac5).

It found the three changes right: the branch one poly with the row (no edge bar at y 16832 under the track
in either metal shot, salmon unbroken y 16816-17000) and with the leg, which reaches x 8760 (poly colour
continuous x 8748-8933 in the clean and chip-2 stripped shots); no contact to the tracks x 8925, 8882, 8838
(a dark blob on x 8882 at y 16976-16990 is in chip 2 only); the pad (8882,16867) does not touch the column
(field colour at x 8904-8910 in both metal shots; the clean shot's salmon blob there is one of that shot's
ragged fringes beside the column); nothing branches off, and a field strip (y 17010-17016) separates the leg
from the diffusion south of it in the open; the plate's strip has its edge lines at y 16379-16380 and 16409,
the east strip at 16418 and 16436-16437; no poly crosses the added VCC diffusion and the contact (8535,16860)
is there. Two findings, both geometry only, both on the VCC diffusion added in round 24:

1. **`D 8510,16497:8560,16570` was about 11 px too tall** (geometry only): the top edge line is at
   y 16508-16510 in all four shots, field above. Confirmed (`px.py col 8535 16490 16522 3 metal,acid1b`: the
   edge at y 16508-16511). Fixed: `D 8510,16510:8560,16570`.
2. **An undrawn VCC contact at about (8532,16537)** on that piece (geometry only: `vcc` onto `vcc`). Confirmed
   (`eof_cchk.py 8532,16537`: hole -14, centres 219/150, ring west and east). Fixed: `C 8532,16537`.

After these two fixes (the commit before them is e994105):

```
tools/t.sh eof sameconn.py e994105              connections identical
.venv/bin/python tools/sameconn.py e994105      connections identical
```

Round 25: no findings that change a connection.

### Round 26 (full review of pieces `lat15`, `cap16` and `w16693`; 2026-11-20 04:21 to 04:41 +0000, at commit a8bd088)

A fresh reviewer (Claude Fable 5.2), briefed with the three pieces' claims (the two cell copies with their
equations and additions, every row east of the cells with its pad, the data track, the enable metal; the
lower node's leg, box, neck and rectangle; the upper node's metal, pad and row) and told to look hardest at:
whether the neck is diffusion joined to the rectangle or poly; whether the box is a buried contact and
whether either of the tracks x 9056 / x 9099 makes a contact there (dark for about 45 px in both metal shots,
green in the clean shot, a blemish in chip 1's metal shot); whether anything else touches the rectangle or
crosses it; each cell copy against the master and the lower copy; whether the metal x 8925 is one metal
through the pad (8925,16262) and ends at (8925,16040); the pad (8838,16000); the data track's corner and its
thin stretch over two poly rows; whether the lower-node row ends at x 8812; every crossing and every pad's
surroundings; whether the upper node's metal ends on the pad (9011,17080). It used 81 tool calls and 15
images (`cache/scratch/eof/review-26/`), with `px.py`, `textmap.py`, `tl5_tracks.py`, `tl3_thin.py`, the
follower, the extraction and `unsure.py --equations`.

It checked and found correct: the neck is the rectangle's material (chip-2 metal 162/118/74 against the
rectangle's 176/133/79, the poly leg's 158/110/47 and the field's 168/138/87; chip 1's metal shot blue 79-83
against poly 32-34; no edge line across at y 16602-16608, `c2.png`, 4.6x); no contact from the tracks beside
the box (the west half of x 9056 passes undisturbed in both chips, x 9099 has no ring north or south in chip 2
and no widening; the green lobes are in chip 1 only, the chip-2 stripped shot shows none and no pits:
`c3.png`, `c4.png`); the rectangle's perimeter whole on text maps of all four sides, the pad (9180,16648)
15 px of field away, the six tracks with 8-10 px edge bars only, no poly across; the upper node's metal ends
on the pad (9011,17080) with bare ground y 17107-17146 in both chips, the row ends at x 9026, its four
crossings without a hole (`w1.png`, 5x); both cell copies by overlay at 2.6x and 3.9x in the clean and metal
shots and by a mosaic against the lower copy (`l1`-`l3`, `l9`, `l10`); the lower-node row ends at x 8812
where the lower copy's runs on (`l4`, `l5`, 5x); bare ground north of (8925,16040) and symmetric rings at
(8925,16262); the data pad with the track through it, the row from the west and field east; the corner at
y 15868 whole and 30 px from `ck_out`'s corner in both chips (`l7.png`); the thin stretch x 8880 with 8-10 px
bars and no hole (`l8.png`); the metals x 9011 and x 8594 pad to pad; no row crossing with a hole; the
equations and their marks as claimed. Two notes, neither changing a connection:

1. **The box's extent** (geometry only): the box proper is y 16674-16704 and the poly's colour reaches north
   to about y 16706, where `B` was drawn to y 16716. Confirmed (`px.py col 9079 16664 16724 2 metal,acid1b`:
   outline lines y 16672-16682 and y 16700-16704 in the chip-2 metal shot, a plain centre 165/125/75 between,
   poly colour from y 16708; a further line at y 16714-16716 across the poly, read as the pad's foot under
   it). Fixed: `B 9066,16672:9092,16708`, `D 9056,16672:9102,16706` (the buried contact still covers all the
   poly on the pad, so no transistor appears).
2. **An undrawn thin metal over the cells** (coverage; another net's): the thin metal x 8637-8650 down
   column B (`bc1`'s `M 8642,14898 y15060`, which runs on) crosses the copy's inverter node box and both tie
   boxes, dark there for 12, 23 and 17 px in both chips (`tl3_thin.py 8636 8650 15860 16470 --thr 144 --min
   8`: y 15887-15898, 16044-16066, 16146-16162), with a 9 px bright patch at (8640,15904). The reviewer read
   it as no contact (the same at the lower copy and at the master's thin W; the clean shot 189/177/130; no
   widening; chip 1's metal is dark there, so chip 2 and the clean shot carry it). Confirmed as recorded:
   Ambiguity 75. Nothing drawn: the metal is not this package's, and no piece's net touches it.

It could not check: the track x 9099 at the box in chip 1's metal shot (the blemish); the unread box
(8762-8795, 15722-15757) beyond the data port (the thin metal x 8792 is dark for 36 px over it with no bright
centre); the cells' load ties and the continuity of the cell's thin metal over the node boxes (as at the
lower copy).

After the fix of note 1 (the commit before it is a8bd088):

```
tools/t.sh eof sameconn.py a8bd088              connections identical
.venv/bin/python tools/sameconn.py a8bd088      connections identical
```

Round 26: no findings that change a connection.

### Round 27 (full review of pieces `inv17`, `nor17` and `in212`; 2026-11-20 05:15 to 05:33 +0000, at commit 3ee5afd)

A fresh reviewer (Claude Fable 5.2), briefed with the three pieces' claims (the inverter with its source,
gate, node strip, output pad, load and tie, and its output wire pad to pad with the three `?M` stretches, the
row and the pad (9008,17560); the NOR with both VSS boxes, the bands and the column, rows 1 and 3 as gates,
row 2 ending in a buried contact, the strip to the load, the output metal with its corner, row 3 to its pad,
the rails, the undrawn plain area; the track x 9099 from the pad (9098,17210) to the pad (9053,15822) with
its corner, its `?M` stretch and the claim that it is not the track north of y 15830) and told to look hardest
at: whether the inverter's strip is diffusion and opens into the pad; metal contact or poly on that pad; the
thin metal (dim, unseen by the follower): one metal, a step or break, a contact at any of the three boxes,
where it begins; the pad (9008,17560) without a green hole; the load's shapes placed from another inverter;
whether both ends of the NOR's column reach VSS and the second box has a contact; whether row 2 ends in a
buried contact or is a third gate; whether rows 1 and 3 cross the column; where the node's strip goes west;
the output metal over row 3 and its corner beside the pad (trap 16); every track crossing; the corner
(9097,15870), the pad (9053,15822), any pad, tap or step in the track's run, the `?M` stretch. It used 76
tool calls and 23 images (`cache/scratch/eof/review-27/`), with `px.py`, `textmap.py`, the follower and the
extraction.

It checked and found correct. `inv17`: the strip is diffusion with edges at y 17019 and 17045 and opens into
the pad; the pad has a pitted contact and no poly, and nothing goes north from it; the gate row ends at
x 8684 and is not joined to the plate; the gap diffusion is bounded y 16990-17058; the thin metal runs from
pad to pad with no ring, widening or hole at the three boxes; the pad (9008,17560) is a pitted box in the
chip-2 stripped shot (`k1.png`, 6x): a contact (so Ambiguity 77 has its second look). `nor17`: both bands
are diffusion and reach tan under the rail's margin; both VSS contacts exist; the column is unbroken past
the box on its west side (`px.py col 8761`), so row 2 ends on it and is no gate; rows 1 and 3 cross fully;
the strip reaches the VCC box; the pads (9011,17080) and (9007,17170) are separate metals (`i1.png`); the
corner at y 17518 clears the pad's ring by bare ground; no hole under any track on the three rows.
`in212`: the corner and the pad (9053,15822) as drawn, with bare ground to the upper track and to the track
x 9012 (`l1.png`); the follower's run west there is a jump; no pad or tap in the run (its three contact
candidates are bright metal over flat tan). The overlay `q1.png` (3.9x, stripped shot): every outline on a
feature; the island is field. Four notes, none changing a connection:

1. **The `?M` stretch of `in212`, y 16671-16717** (a comment): the trace said the metal is "dark in both
   chips"; chip 1's darkness is an irregular blob about 60 x 50 px over both tracks and the box (absent in
   chip 2), and in chip 2 the track keeps its width and its centre stays bright. Confirmed (`px.py row 16690
   9084 9112 3 metal,metal1,acid1b`: chip 2 197/177/95 at x 9096, 126-148 at x 9099-9105; chip 1 33-101
   across). The `?M` stays; the comment and the notes are reworded.
2. **Beyond the port `eof_w17168`** (a note): the metal x 9057 ends 47 px south of the port on a pad with a
   contact at about (9055,17647) (ring and bright centre in both chips), whose poly runs west along
   y 17636-17656 under `eof_w17040`'s metal x 9011 with no ring there. Confirmed (`textmap.py 8990 17612 9082
   17672 4`). The port stays where it is; its note, the Ports table and Not done say so. Not drawn.
3. **A sentence of the notes** on the inverter's strip ("no sample under 141 from x 8750 to x 8780" at
   y 17031): true of the clean shot only (137 at step 2); the other shots are dark at x 8776-8783, the
   contact's ring. The conclusion holds (the pad's west edge line is absent where the strip arrives).
   Reworded.
4. **Two sizes** (geometry only): the inverter's plate has its top edge at about y 16972, drawn 16979; the
   thin metal at y 17250-17285 is x 8787-8802, drawn 10 px wide. Confirmed (`px.py col 8600 / 8640 16962
   16992 3`: edge line y 16965-16974; `px.py row 17255 / 17265 / 17280 8780 8808 3 metal,metal1`: bright
   x 8789-8801 in both chips). Fixed: `P 8563,16974:8655,17039`; the wire is 13 px wide from y 17244 to
   y 17460.

It could not check: the continuity of the thin metal over the three boxes and the absence of a contact
there (the photos cannot show it: Ambiguity 76); the load ties; the 6-8 px of each band's join hidden under
the rail's edge line; the track x 9099 at y 15880-16450, seen only at 1.85x and by the follower; the
identities of the rows `eof_w16823` and `eof_w16693` (earlier pieces) were not re-read.

After the fixes of notes 1-4 (the commit before them is 3ee5afd):

```
tools/t.sh eof sameconn.py 3ee5afd              connections identical
.venv/bin/python tools/sameconn.py 3ee5afd      connections identical
```

Round 27: no findings that change a connection.

### Round 28 (full review of pieces `o168` and `o040`; 2026-11-20 06:00 to 06:20 +0000, at commit cbf055e)

A fresh reviewer (Claude Fable 5.2), briefed with the two pieces' claims (`o168`: the pad (9055,17648), the row
y 17638-17656 under three tracks and under `ck_out`'s metal, the turn at x 8573-8588, the row y 17682-17698
under the wide metal, two tracks and `ck_out`'s second metal, the leg and the pad (8355,17649), the metal to
the corner (8186,17650) and the pad (8185,17428), the row east to the port x 8245; `o040`: the metal to the
corner (9010,17780) and the pad (8733,17778), the row to the pad (8338,17777), the metal to the corner
(8012,17777), the Z at y 17259, the corners at y 16647, the stretch onto `bc1`'s metal end (8143,16300) and
`bc1`'s jog to the contact (8186,15910); the alias) and told to look hardest at: the two steps of the track
bundle (a swap with a neighbour; the order and number of tracks entering and leaving; the bare ground between
this line and `rst_a`'s on x 8057); the join onto `bc1`'s metal and the jog beside the pad (8185,16303); the
long straights (a pad, a contact, two metals end to end); the row that is red-orange under the wide metal
(contact, gate or neither); the two stretches under `ck_out`'s metals and that metal's corners; whether the
turn at x 8573-8588 joins the two rows; all five pads (a contact, the metal ending, anything else leaving);
whether each row is one poly on both sides of the wide metal. It used 68 tool calls and 20 images
(`cache/scratch/eof/review-28/`), with `px.py`, `textmap.py`, `railprof.py`, `eof_mrun.py`, `eof_cchk.py`,
`tl5_tracks.py`, the follower and the extraction.

It checked and found correct. The five pads at 5-5.5x in four shots each, with text maps: each has a ring, a
bright centre and a pitted box, its metal ends on it and one poly leaves. The pad (8355,17649): the poly east
of it is the rounded end of another row that starts at x 8398, with bare field at x 8384-8392 between; no
metal bridges the leg to `ck_out`'s metal. The pad (8185,17428): 10 px of open ground to the metal north of
it. The turn at x 8573-8588: one poly from y 17642 to y 17694 in chip 2; the row y 17647 does not go on west
(the poly under the rail there ends at x 8543, field beyond). The row y 17690 under the rail: neither contact
nor gate (no ring in chip 2's metal, the row's edge bars cross the full width; the "diffusion" that
`railprof.py 8526 8545` reports between every row is the rail's centre strip: no outline, no edge line in
either metal shot, field in chip 2's stripped shot). `ck_out`'s overlaps and the corners (8600,17649),
(8882,17649): no ring, hole or widening. The row y 17777: one poly, orange in every open gap on both sides of
the rail. The Z at y 17259 (5x): continuous in both chips, 25 px of bare ground to `rst_a`'s step; a pad at
(8011,17215), 35 px north of it, is another net's (its poly tab passes under x 8057 as a plain crossing). The
corners at y 16647: three nested steps, order kept, 25 px of bare ground to the neighbour's Z at y 16611. The
join (8143,16300) and the jog (5x): one metal, bare ground between the jog and `rst_a`'s pad, a plain crossing
of `rst_a`'s row; plain crossings also at (8143,16515) and (8964,17780). The corner (9012,17518): 8 px of bare
ground to the pad (9008,17560). The extraction: 0 errors, `bc1_g6_out` = NOT `bc1_g6_in`, the alias listed by
`tools/unsure.py` as the notes say. One finding, which changes no connection:

1. **A sixth metal over the row y 17768-17786** (a comment): the trace's comment and the notes' table named
   five metals over the row; there is also a thin metal at x 8643 (`eof_mrun.py row 17758 / 17800`:
   8643(13-14)). A plain crossing (`eof_cchk.py 8642,17777`: 44, no ring; the row unbroken in the clean shot).
   Confirmed (`eof_mrun.py row 17758 8590 8700 17800`; `eof_cchk.py 8642,17777`: 44, centres 204/240;
   `tl5_tracks.py v 8643 17740 17815`: bars only, no hole). Fixed: the comment in the trace, the table of
   piece `o040` and the Inventory name it. No geometry changed.

It could not check, or found resting on one chip: chip 2's metal x 8057 is dim at y 16886-16902, so the
continuity there rests on chip 1 and the clean shot's unbroken protected strip (now in the table of piece
`o040`); the row y 17690 under the rail rests on chip 2 (chip 1's metal is damaged and its clean shot stained
there: Ambiguity 79); the long straights were read with `tl5_tracks.py` and a 0.85x overview, not at 4x
throughout; `bc1`'s stretch x 8186 north of the jog by the metal test only; nothing beyond the port x 8245.

After the fix of note 1 (the commit before it is cbf055e):

```
tools/t.sh eof sameconn.py cbf055e              connections identical
.venv/bin/python tools/sameconn.py cbf055e      connections identical
```

Round 28: no findings that change a connection.

### Round 29 (full review of piece `g174`; 2026-11-20 07:14 to 07:31 +0000, at commit 9789a76)

A fresh reviewer (Claude Fable 5.2), briefed with the piece's nine claims (the rail as one metal from `bc1`'s
end, with its step and its end; the active area; the two contacts; row 1; the hairpin's row, leg and bar as
one poly; the lower poly as a second one; the three transistors and their nets; the seven places where wires
leave the piece, with the claim that the ground diffusion between the two polys does not go on east; nothing
drawn for the box of Ambiguity 84) and told to suspect: the rail (its step read at 5x, 930 px of it at 1x and
by a script, chip 1's metal destroyed over the unit), the junction of the hairpin's row with its leg at the
rail's edge, whether the two rows are two polys, the active area west of the rail and whether each poly seals
its node on every side, the east edge, anything left out (a third contact, a poly or metal on the box), and the
two contacts. 17 images in `cache/scratch/eof/review-29/` (1x to 6.5x, the four shots), `tools/px.py`,
`tools/eof_patch.py`, `tools/textmap.py`.

One finding:

1. **The slot between the two arms east of the rail (x 8372-8407, y 17455-17464) reads as diffusion, not as
   field** (changes a connection: the ground diffusion leaves the piece east at (8368, 17452-17466), which the
   ports and the notes denied; no drawn net or transistor changes). The notes had the slot as field from
   `px.py row 17457`, a row on the slot's north flank (`px.py col 8388 17448 17470 1`: red 136 at y 17457
   against 180-184 on the centre line). Over (8376-8400, 17458-17462) `eof_patch.py` gives 16.0 / 34.6, with
   the necks (22.8 / 38.9, 28.0 / 45.5), the sliver and the open strip, and not with field (-0.6 / 9.1,
   -7.5 / 22.6); the clean shot's mouth at x 8366-8374 is like the necks' (`g1.png`, `e3.png`, `e2.png`);
   along y 17460 the colour turns to the field's at x 8404-8428, so the finger is not shown to reach the
   strip. **Confirmed** (1 px columns at x 8380, 8388, 8396, 8404: every one of the three bands has a
   greenish north flank and a reddish south flank; over the red flank the slot is 14.5-23.5 / 32-47, and a
   band of the same height that is certainly field, `eof_patch.py 8228 8250 17452 17458`, is 0.5 / 24.2).
   Fixed: a port `vss` D (8368, 17452-17466) in `ports.d/eof.txt` and the Ports table; the Logic section's
   second table (the rows on the east edge, the necks and the slot, the arms, the box); Ambiguity 85, which
   gains reading (4) as its working belief (the arms are gates along a ground finger, the box is their ends
   over field: no contact); Status, Not done, the glossary and `notes/operation.md`; a comment in the trace.
   No geometry changed. The method that misled (one row across a 10 px band between two polys) goes to the
   handoff as a proposed trap.

Checked and found correct: the rail as one metal from y 16290 to its end (the reviewer: y 17572; drawn to
y 17568), no dark bar over 11 px across its full width in both chips (`b1.png` 1x, `r1.png` / `r2.png` 3x,
`b2.png` 4.5x at `bc1`'s end, `c1.png` 5x at the step), 20 px of bare ground between its end and the metal
y 17599-17614; both contacts real and inside their regions, no third contact and none on either node
(`textmap.py 8300 17262 8376 17566 3 --acid`); the hairpin's row and leg one poly (`d1.png`, 6x: the outline
continuous round the corner), row 1 and the bottom bar continuous across the rail's edge; the two rows
separate at eight columns x 8216-8300 and under the rail, no poly joining row 1 to the top bar; the box of
Ambiguity 84 without metal (centre 162/127/78 and 136/117/60 against 225/200/120 and 204/198/107 for metal)
and without poly, pink field under the metal corner at x 8236 and west; the seals, the three transistors and
the ports listed (`f1.png`, `o1.png`); row 1's widened patch under the track x 8229 without ring or hole
(`h1.png`). Not checked: chip 1's metal over y 17340-17480 (destroyed); the active area's continuity across
the rail's west edge x 8305-8316 (an artefact line in both chips; widths only); Ambiguity 83; `bc1`'s reading
of the rail as VSS (taken as given); a closed bar at (8285-8332, 17245-17260) that enters the diffusion north
of the drawn rectangle (outside the piece: Not done).

Round 29: one finding, fixed (a port added: the ground diffusion leaves the piece east; no geometry changed).

### Round 30 (fix check of round 29's change; 2026-11-20, after commit 9949dbb, against 9789a76)

A fresh reviewer (Claude Fable 5.2), told the one finding and the fix (the port `vss` D (8368, 17452-17466);
only a comment changed in the trace) and to compare whole patches with a known field band and with open
diffusion. 6 images in `cache/scratch/eof/review-30/`. It found: the slot is diffusion (red minus green at
the band's brightest rows, x 8380-8400, y 17458-17460: 19 / 11 / 5 in the chip-2 stripped shot against -2 to
-11 for the field band and 21 for the north neck; 27-40 in the clean shot against -8 to 13 and 31-55; chip 1's
metal shot 26-42 against 18-26; `eof_patch.py`: slot 10.7 / 20.6, field -2.1 / 7.0, the open strip
14.0 / 32.2); the mouth at x 8368 is open (clean shot, row 17458: tan to x 8368 with no outline, like the
neck's row 17362; rows 17410, 17436 and 17484 have the poly's red outline at x 8364-8366); the port's place
is right (the band's dark lines at y 17450-17452 and y 17466-17468, its colour ending at x 8404-8408);
`tools/ports.py --near` shows the new port meeting no other. One remark, geometry only and outside what is
drawn: in the clean shot the poly at x 8382 is bright over y 17428-17440 and y 17476-17492 and dark on the
legs proper, so the diffusion probably also passes x 8368 under the two arm rows as gate area (one shot; it
would widen the same two transistors): added to Not done for the east side.

```
tools/t.sh eof sameconn.py 9789a76              connections identical
.venv/bin/python tools/sameconn.py 9789a76      connections identical
```

Round 30: no findings.

### Round 31 (full review of piece `g174e`; 2026-11-20 11:46 to 12:07 +0000, at commit 8e2cb12)

A fresh reviewer (Claude Fable 5.2), briefed with the piece's eight claims (the active area not closed at the
rail's east edge, with a field island; the output strip, its two necks and the bridge, and the ground's band,
sliver and finger; row 1's L; the hairpin's and the lower poly's right legs and arms, ending apart on the
island with no buried contact; the load, its tie, the diffusion under the VCC rail with two contacts, the
rail; the output's tail, pad, contact and metal; the equation and the sizes) and told to suspect: the box
where the arms end (island, buried contact or a U-turn of one poly), every narrow band classed as diffusion
(with the fairness of the control), anything closing the active area at the rail's east edge or at the step
corner, the legs as gate, row 1's east end, the load's plate and the dark line down it, the tie box and the
tab, the second contact, the output pad (traps 16, 22, 26, 32) and the tail. 13 images in
`cache/scratch/eof/review-31/` (the four shots), `tools/px.py`, `tools/eof_band.py`, `tools/follow.py`, a
per-channel peak measure of its own for the bands.

**No finding changes a connection.** Five notes, geometry only, each checked here and confirmed:

1. **Row 1's east end**: the poly runs to about x 8478 (drawn 8472). East of the active's edge line x 8466-8470
   the strip x 8472-8476 has the poly's colour at y 17292 (metal 139-157/80-110/43-65) and is plain at y 17272.
   Confirmed (`px.py row 17292 8440 8490 2 metal`; `row 17296 8462 8490 2 acid`: 115-128/87-97/45-59). Fixed:
   `P 8388,17282:8478,17302`. It closes Ambiguity 89: the gate overhangs the edge.
2. **The active's east edge south of row 1** slants from about (8470,17305) to (8480,17322); drawn straight at
   x 8467. Confirmed (`px.py row 17312 8454 8492 2 metal`: edge line x 8468-8476; `row 17320`: x 8476-8486).
   Fixed: the corner is a polygon, `D [ 8452,17263 x8467 y17304 8477,17322 y17328 x8452 ]`.
3. **Two things in the region that the piece's Logic section did not name** (both were under Not done): a
   diffusion square x 8512-8566, y 17284-17348 under the VCC rail with a contact at (8530,17312) (the east
   neighbour's by its look), and a pad at (8403,17603) with a metal from the west and a poly south, joined to
   the output's pad by nothing. Added to the Logic section and to Not done with the reviewer's coordinates.
4. **Ambiguity 90 cited a red-only map**, which cannot tell tan from pink. In full colour the step corner is
   tan (190-200/166-185/124-133; here `px.py pt 8380,17268 8386,17270 acid1b`: 193/171/122, 195/176/126):
   diffusion, as drawn. The entry now says so.
5. **The output's metal is 14-16 px wide** (drawn 12). Confirmed (`px.py row 17629 8448 8488 2`: metal
   x 8462-8476, `metal1` x 8464-8476). Fixed: `M 8469,17603 y17634 w=15`; the port is (8461-8477, 17634).

It checked and found correct: the box (the pocket has no poly: metal blue 85-90, clean green; it is field on
the same row on which the slot is diffusion, stripped red minus green -2 to -7 against +10 to +20; the arm
ends are ordinary orange poly, red minus green 40-49, unlike the tie box's pale centre, 12-23; the east line
is a single 7 px edge, so no U-turn; the arms end near x 8426); the bands (its own measure gives +12 to +28 in
the stripped shot for all seven and -14 to +1 for the pocket and three field controls of its own; the control
is fair: on row 17453 the active's west edge splits field, -6 to -11, from diffusion, +13 to +25); the bridge
(no line crosses column 8444 from y 17396 to y 17519 in three shots); the rail's east edge (chip 2 plain from
x 8372 into the strip at both necks and the slot; the clean shot's dip at x 8374-8378 is absent from chip 1's
metal shot; the bars and row 1 continuous across it); the load (the line x 8484-8488 is the rail's west edge,
at the same x at y 17320 and y 17462 in both chips; the tab is poly over field, clean 215-226 against 236-245
on the plate; the tie box adjoins the strip by a single line; the diffusion under the rail is unbroken on
column 8524; both contacts are real); the output (the pad's contact real; no edge crosses the tail; field
beside it; the metal leaves south, by the follower both ways and the pink strip; nothing else leaves the pad).

It could not check: whether the legs lie over active area or field (Ambiguity 88: widths only); chip 1's metal
near the VSS rail at y 17320-17480; the diffusion under the VCC rail east of x 8558; the output's metal beyond
y 17650; where `eof_w17472` comes from.

After the fixes of notes 1, 2 and 5 (the commit before them is 8e2cb12):

```
tools/t.sh eof sameconn.py 8e2cb12              connections identical
.venv/bin/python tools/sameconn.py 8e2cb12      connections identical
```

Round 31: no findings that change a connection.

### Round 32 (full review of piece `o362`; 2026-11-20 12:36 to 12:43 +0000, at commit 11dd9bb)

A fresh reviewer (Claude Fable 5.2), briefed with the piece's six claims (the thin metal x 8468 one metal
from y 17630 to y 18474 with no tap on any row it crosses, `ck_out`'s row y 17908 among them; the L corner
(8468,18474); the metal y 18474 unbroken to the pad (7556,18473) with no pad or branch in its run; the pad's
poly row under the rail x 7468-7516 without contact to the pad (7384,18473); the metal west of that pad and
the port; the trace lines) and told to suspect: two metals end to end on the track (the stretches of 14-16 px
without metal in both chips, and the longer ones in one chip alone); the crossing at y 17977, read from one
text map; the corner, read at 2.8x only; the horizontal metal, read by text only; whether the metal from the
east ends on the pad (7556,18473) and whether anything else leaves it; a contact from the rail to the poly
beneath; the pad (7384,18473), whose centre is dim in chip 2's metal shot, and whether the metal west of it
is joined; the neighbouring line y 18428.

What it checked (11 images in `cache/scratch/eof/review-32/`): the vertical metal on `v1.png`, `v2.png`
(2.9x; both metal shots and the clean shot) and by a width scan of both metal shots every 3 px (never over
15 px, chip 1 16: no pad, no T); the single-chip dim stretches at y 17742-17766 and y 18395-18419 (the other
chip bright, the clean shot pink); the crossing of `ck_out`'s row (`x17908.png`, 6x; `textmap.py --acid`;
`px.py row 17906`: chip 2 metal-yellow over the row, chip 1 dim there, the clean shot's row cream under the
metal with no hole, ring or pad); the crossing y 17977 (`x17977.png`, 6x: the greenish dip spans the row's
whole width, x 8444-8490, the metal keeps its width, no ring in either chip); the corner (`corner.png`, 5x;
text map: bare ground east, to the rail's edge at about x 8503, and south in both chips); the horizontal
metal over its full length (`h_east.png`, `h_west.png`, 2.75x, metal and clean: one line, no pad, no branch,
8-14 px wide with its top edge constant at y 18467-18470; the line y 18428 apart throughout, open field
between); the pad (7556,18473) (`padE.png`, 4.6x; 2 px profiles on three rows: ring, bright centre in both
chips, hole in the clean shot, the east metal on it, open orange poly west, nothing north or south); the
poly under the rail (`rail.png`, `west_acid.png`; text map: one poly, straight edges, no ring, no hole, no
poly along under the rail); the pad (7384,18473) (`padW.png`, `west_acid.png`: bright centre in chip 1, a
pitted box in the chip-2 stripped shot, a hole of -16 to -19 in the clean shot; rings of 12 px on both sides
in both chips, so the west metal is joined; pink under that metal: no poly west; open field to `trunks`' pad
(7420,18428)); the extraction alone and with every file (no join, nothing in `tools/unsure.py`; the port
agrees with `ports.d/eof.txt`).

Findings: none. Nothing changes a connection and no geometry was found worth correcting (edges within about
3 px).

What it could not check: anything west of x 7340; the centre of the pad (7384,18473) in chip 2's metal shot
(dim: the contact rests on the other three shots); the row crossings other than y 17908 and y 17977 at 4x or
more (read at 2.9x, with the width scan and the clean-shot scan); the chip-2 stripped shot along the vertical
run except by text map at y 17836-17932 and y 17950-18000.

Round 32: no findings.

## Not done

- **Ambiguity 53 to be measured again with a control** (from review round 29 of piece `g174`): a band about
  10-20 px high between two polys has a greenish north flank and a reddish south flank in chip 2's shots, so
  its colour says something only against a band of the same height that is certainly field, measured the same
  way. Piece `vw`'s three bands (x 8752-8772; y 15191-15200, 15235-15247, 15360-15373) were classed from
  patches without one. To do when next in column B: `tools/eof_band.py h` (run 24: the whole-band test) on each band and on a field
  band of the same height between two rows nearby.
- **Task 2, the loads of `sl_eq_r5_n` (= NOT `sl_eq_r5`)**: one load is drawn (piece `r5nor`,
  the NOR that makes `tl1_w2637`), and the net's poly ends there. Not checked: taps along
  `r9m`'s, `tc2`'s, `tl4`'s, `tl2`'s and `tl1`'s stretches of it (each was read by its own
  package). Next on this path: what `tl3`'s latch A does with it (`tl4_w4590`, its enable's
  source, is reached only by the row (4250,2810): queue row `tl3` (continue)).
- The supply plane north of y 1963 (only a piece over the strap's head is drawn; `padring`), and
  the VSS plane between the arm and `tl1`'s rail R1 (`tlb`).
- **The gate at the end of `rst_ck`'s tap row is traced** (piece `g7700`); its three wires go on:
  (1) the output `tc2_r5589`: the poly north of the pad (7272,6912), towards a row y ~6862 in `bw`'s
  crossing field; (2) `tc2_sr_g`: the poly row east of (7400,7212) and the metal south of
  (7268,7800) (the follower runs it to (6514,8254): unchecked); (3) `eof_w7777`: the row y 7821 west
  of x 6450, into the undrawn west half of `lc1`'s cluster E. Also undrawn there: `lc1_w7780`'s row
  from x 6450 to its pad (6815,7778) and that pad's metal south.
- An undrawn poly under row 2's metal x 7308-7327, y ~7250-7428 (no contact onto the metal; field between
  its top and the pad (7313,7215)): `bw`'s crossing field / `busl`'s northern part.
- The units below the gate in the same column (x 7460-7800, y 7860-8440): U2, U3, U4 are drawn (run 12,
  piece `d3982`, with the rail and the wide metal to y 8460); U1 and the diffusion under the rail at
  y 7849-7907 are not (the two items on U1 below; `cdp3` (continue)).
- **`rst_a`'s source (task (b)): found** (run 10, piece `isrc5`): it is `rst_a`. Nothing is left of the
  task but the renames (the rename of line X (the first through line of the left-centre strips) to `rst_a` (done); perhaps `rst_a_n`, `rst_ck`, `rst_rc`, `rst_lat`
  to names that say "reset": the coordinator's refresh).
- **The unit that drives `tl3_w3982`: traced** (run 12, piece `d3982`: three inverters from latch D's lower
  node). Left on that path: nothing of the wire; what latch D does is `lc1`'s and `lc2`'s (its enable
  `tc2_sr_g`'s driver is not found: `busl`'s piece `sr`).
- **U1, the fourth unit at the foot of the same gate column** (x 7313-7860, y 7940-8070; `cdp3` (continue),
  free; seen in run 12, not drawn): a copy of U4's build 390 px higher (`@inst eof_dinv 0,-390`; findcell
  0.89; every outline on its feature on `m_e1.png` and `m_u1t.png`, placed then as `tl5_inv`). Its wires
  differ from U4's: (1) the gate row y 7986-8006 runs west under the thin metal x 7396-7408 and the track
  x 7359 and **ends on a pad with a contact (7313,7995)** (`textmap.py 7290 7972 7340 8020 3`, `m_in1.png`),
  the north end of a metal x 7316 that runs 620 px south to **a pad with a contact (7316,8622)**
  (`follow.py 7316 8060 S --gap 16`; `textmap.py 7286 8570 7350 8640 3 --acid`; `m_p8625.png`, 3.5x, four
  shots); that pad's poly goes east along y 8612-8634 under the track x 7360 (which ends on its own pad
  (7358,8662)) and turns south at x 7385-7412, under `tc2_sr_g`'s metal y 8700-8715 (`eofw`'s, beside the
  corner pad (7446,8732)), to what looks like a pad with a contact at about (7402,8778) (`m_c8732.png`, 3x:
  not read). (2) **Its output box (7480-7520, 8022-8055) has no poly leaving it** (`m_u1w.png`); the output
  leaves by the load's plate, whose foot runs east as a poly row y 8051-8069 under the wide VCC metal to a
  pad with a contact (7838,8062) (`m_u1o.png`, 5x, three shots; `textmap.py 7814 8040 7862 8086 3`), from
  which a thin metal x 7831-7843 runs south **through** a pad with a contact (7836,8428) (ring and bright
  centre in both chips; the clean shot's hole is dull, not green: `textmap.py 7808 8386 7872 8452 3 --acid`)
  and on south (seen to y 8480: `m_p8430.png`, 3.5x, four shots; trap 32); that pad's poly row goes east
  along y 8418-8435 (seen to x 7960). To draw it: place the cell, read the three pads and the two ends.
- Under the same rail between `g7700` and U1 (y 7849-7907): `railprof.py 7552 7598 7560 8600` gives a
  diffusion with no gate; not looked at (`cdp3` (continue)).
- **The last two rows of `lc1`'s diagonal bundle** (y 6953 and 7040; the middle one, y 6996, is piece
  `n2n`'s: `bd1_n2`). They come from `tl5`'s south bus polys x 5455 (`tl5_w3461`, latch a's data) and
  x 5368 (`tl5_w2722`, the strong inverter's output), by diagonals at x - y = -1306 and -1439 (measured in
  run 14 with the middle one: the table of piece `n2n`; not drawn). Their pads (6188,6953), (6188,7040)
  each have a metal east along the row: the row y 6957 turns south at (7035,6957) on the track x 7035 and
  the row y 7043 at (6948,7043) on the track x 6948 (`o_c1.png`: the corners nested with piece `n2n`'s);
  both tracks run on south beside x 6991 (`eof_mrun.py row 8300 6930 7040`: 6947, 6990; x 7034 is `trunks`'
  staircase lower down: not followed, so which metal carries which south of y 7100 is not read). The top
  row jogs (y 6927 at x 5620, y 6953 at x 6100: run 11). To draw them: as piece `n2n`, one line each.
- **Line Q, the track x 6730** (seen in run 13, not drawn; `busl`'s northern part). It is not `rst_c`
  (run 13's first guess: that is `rst_c`, piece `rc`). From the south: a metal comes up x 6472 (seen from
  y 9540; the follower loops there), steps east at y 9490-9500 to x 6516 (`eof_mrun.py row 9490 6400 6570`:
  6476(20), 6507(30)), runs north on x 6516 beside `ck5`'s x 6472 to (6516,8821), by a diagonal (x + y =
  15337) to a pad with a contact (6690,8625) (`eof_cchk.py`: hole -10, centre 198 / 209); a poly column
  x 6690 north to a pad with a contact (6690,8320) (hole 3, 173 / 173); a metal north, an L east at y 8190
  onto the track x 6730 (`follow.py 6690 8290 N --gap 16`: corners (6692,8188), (6732,8191), end
  (6730,7469)), north to **a pad with a contact (6730,7473)** (hole -27, 218 / 186; `n_q1.png`, 3.4x); the
  pad's poly row y 7465-7485 runs east 630 px under the tracks to x 7372 (`n_q2.png`, 1.3x, three shots),
  north on x 7352-7372 to y 7295 and east along y 7290-7310 under `bw`'s metal x 7410-7432 and on (seen
  to x 7470: `n_q5.png`, 3.1x). **The track x 7359** (the one that ends south on its own pad (7358,8662),
  beside U1's wires) has its north end at y 7447, over this poly's corner (7362,7470): whether there is a
  contact was not read (`n_q4.png`, 5.5x, four shots: a bright patch x 7353-7372, y 7450-7490, no clear
  ring). South of y 9540 the line is one of `lc3`'s `lc3_e9756` / `lc3_e9798` (not checked).
- **The driver of the ripple counter's clock `lc3_w9947`: found** (run 15, piece `ck6`: the inverter U),
  **the latch behind it traced** (run 16, piece `vw`: the units V and W) **and two of the latch's three inputs
  followed to their sources** (run 17: `eof_w15172` = NOR(`bc2_w14955`, `bc2_w15000`), piece `in172`;
  the second is `bc2_w15607`, piece `in390`). **The third input is `ck_out`** (run 18, piece
  `in350`). **The latch whose two enable rows the wire's pads feed is drawn** (run 19, pieces `lat16`, `inv16`).
  **The latch's three open wires are followed** (run 20, pieces `lat15`, `cap16`, `w16693`): `eof_w16388` is
  the upper node of the upper latch copy, now drawn; `eof_w16823` ends on a large diffusion (and on the gate row
  y 16986-17003); `eof_w16693` runs to a row y 17116-17135 into the same unit.
  **The unit south of the latch is drawn** (run 21, pieces `inv17`, `nor17`, `in212`): an inverter on the lower
  node (`eof_w17040` = NOT `eof_w16823`) and a NOR on the upper (`eof_w17168` = NOR(`eof_w16693`, `eof_w17212`)).
  **Both outputs are followed** (run 22, pieces `o040`, `o168`): `eof_w17040` is `bc1_g6_in`, the input of
  `bc1`'s inverter 6; `eof_w17168` runs to the edge of a unit under column A's rail.
  **The unit that `eof_w17168` gates is drawn as far as the rail's east edge** (run 23, piece `g174`: three
  pull-downs).
  **The unit's east side is drawn** (run 24, piece `g174e`: the gates' east parts, the load, the output's pad; `eof_w17362` = NOR(`eof_w17338`, `eof_w17168`, `eof_w17472`), firm).
  **Left on that net, and next**: (1) (i) **the NOR's output `eof_w17362` west of the port (7340,18473)** (the next piece; wiring; drawn to there in run 25, piece `o362`: south from the pad (8467,17603), west along y 18474, a poly hop under the rail x 7468-7516 between the pads (7556,18473) and (7384,18473)): `follow.py 7350 18473 W --gap 16` takes the metal to an end (6318,18471), 1,048 px: not checked. To do: a continuous two-chip test along it (`tl5_tracks.py h 18473 6300 7370`), the end at 5x (trap 14), then what the end is on; `trunks`' middle line y 18428 runs beside it to a pad (6797,18428) and north up the left bus field. Not drawn beside the piece: the first of the three lines (y 18383); the rail x 7468-7516 and the wide metal south of y 18515 that it joins; the pads of the bus rows at x about 8424-8445 west of the thin metal (rows y 18115, 18205, 18290, 18380). `cudisp_drv_in`'s label is at (7729,18927) (`pads_out`), `disptmg_drv_in`'s at (5582,18927). Beside the pad, another net's pad with a contact at (8402,17603) (ring and bright centre in both metal shots; no poly from this unit reaches it: field at y 17565-17585), with a metal south: not followed. Also seen: the diffusion under the VCC rail runs on east past x 8558 at y 17450-17475; a second diffusion x 8512-8566, y 17284-17348 with a contact (8530,17312) under the same rail (another unit's; review round 31); the other pad (8403,17603) has a metal from the west and a poly south (review round 31). Then the unit's wires: `eof_w17338` west (a pad at about (8188,17340) on a track x 8186
  from the north) and `eof_w17472`'s west leg south of y 17560 (to y 17585 and on). Also not drawn: the
  contact (8348,17245) and the diffusion north of y 17266 under the rail (the next unit's, to y 17231); the
  poly that ends at about (8292-8328, 17250-17262) from the west. (ii) **`bc1_g6_out`**, the
  inverse of `eof_w17040`: `bc1` ends it on a poly east of the contact (8229,16107) "into the untraced gates
  below y 16000" (`bc1` (continue), free). (iii) `eof_w17212`, the poly row y 15812-15832 west of (8990,15822): by its
  place the row of the pad (8838,15822), on which the thin metal x 8792 ends by a diagonal; that metal's north
  end is the pad (8792,14870) by the VSS band y 14816-14878 (`bc1` (continue), free; run 20's view, not read;
  the thin metal runs down column B's east edge over the units' boxes: trap 27). (iv) **the unit below the NOR**
  (x 8500-8830, y 17229-17360; `bc3`'s ground, free; not drawn): the `tl5_inv` copy `findcell` gave at
  (8685,17307) (`bc3`'s notes: 0.79), which shares `nor17`'s second VSS box. Seen on `r21_d1.png` (1.6x),
  `r21_d2.png` (3x, three shots), `r21_i1.png` (6x): its gate row y 17290-17305 comes from a pad with a contact
  (8838,17298), **on which the track x 8838 from the north ends: by the follower of run 18 that track is
  `eof_w16000`, the first latch's data** (not checked; if so the unit inverts the latch's data and the data's
  driver is at the track's north end); its node box (8770-8800, 17325-17352) lies under `inv17`'s thin metal
  (Ambiguity 76), where its output goes is not read. Below it more units of the column (a box (8780-8800,
  17460-17490) with a poly east to a pad (8838,17472) whose track runs south; a poly end (8778-8805,
  17503-17530)). To draw: place `tl5_inv`, read its pads and the box. Also seen, other nets, not drawn: the
  track x 9056, which steps east at y 17240-17265 to x 9104 and runs on south beside `nor17`'s output; the
  track x 9012 north of y 15950 (it steps east there to x 9056); the 13-line bus's line y 14742, which turns
  south at (9097,14745) on x 9099 and east at (9098,15827) (`r21_k1.png`, `r21_k3.png`). (1a) **the upper latch's enable `eof_w16040`**: the metal x 8925 south of (8925,16300)
  (`follow.py 8925 16300 S --gap 16`: to (8925,17694), a corner west, (8643,17706), where the follower loops;
  candidates (8926,16552), (8926,16845), (8923,16963): bars of the rows beneath). If it is high only while
  `ck_out` is low the two latches are a flip-flop. (1b) **the upper latch's data `eof_w16000`**: the box
  (8762-8795, 15722-15757) at column B's east edge, where the poly row of the pad (8880,15738) ends (a unit of
  column B at y about 15700-15760, not drawn: `bc1` (continue), free; Ambiguity 74), and the track x 8838 south
  of (8838,16030) (the follower in run 18: to (8838,17306), by the `tl5_inv` copy). Seen beside them, other nets,
  not drawn: the pad (8838,15822) with the thin metal x 8792 (from the pad (8792,14870)) ending on it by a
  diagonal and its poly row east along y 15812-15832; a poly row y 15772-15792 through under the tracks; the
  second large diffusion x 9042-9255, y 16778-16995 with its tie box (9262-9290, 16910-16942) under the track
  x 9270 (`bc4`); the pad (9180,16648) with a poly row east and a metal south; the through metals x 9056, 9099,
  9142, 9225 and the thin metal x 8643, which no package draws. (2) **`ck_out`'s four open ends** (ports): at the pad (8424,17908) the metal north
  (`follow.py 8424 17870 N --gap 16`: corners (8422,17690) west, (8142,17687) north, (8146,17383) east,
  (8230,17373) north, end (8227,17019); candidates (8142,17540), (8144,17427); it crosses `rst_a`'s row y 17736
  at x 8418-8430 with no contact, as piece `isrc4` read it) and the poly west (to x 8312, north to a pad at
  about (8312,17862): `r18_w3.png`; another net's metal lies on it from x 8390 west, Ambiguity 66); at the pad
  (9596,17909) the metal north (`follow.py 9596 17860 N --gap 16`: corners (9593,17608) west, (9315,17604)
  north, end (9315,16818); candidates (9407,17607), (9316,17603), (9316,17028)); at the pad (9769,17910) the
  metal north (`follow.py 9769 17860 N --gap 16`: corners (9777,17650) east, (10053,17646) north, (10047,17346)
  west, (9965,17326) north, end (9964,16950); candidate (9966,17245)). The other net beside the first pad: the
  metal along y 17908 from x 8390 west (`follow.py 8380 17908 W`: (8056,17917) south, (8051,17953) west, end
  (7553,17950); a pad in its run at about (8108,17910)), whose east end turns north to a pad at about
  (8382,17862) on the track x 8382. (3) the poly row under the stretch y 17649 (Ambiguity 63), another net's, not
  followed either way. Also beside the wire, other nets, not drawn: the pad (8882,15745) with its metal south
  and west onto the track x 8838 (the follower: to (8838,17306)) and its poly west; pads at about (8838,15830),
  (8640,17862), (8690,17815), (8720,17778) of the nest of Ls south of column B; the rows the wire crosses.
  **Then, to say what the clock's latch does**: `bc2`'s latch units a and b,
  whose nodes are the other two inputs, have none of their own inputs followed (`bc2_w14912` data: its pad
  (10395,14912) is the south end of the thin metal x 10397 that comes from north of y 14570, seen in
  `r17_m1.png`, not as `bc2`'s notes say "goes west"; `bc2_w14955` enable, also T's gate row 3: its metal
  jogs west at y 15392 to x 10398 and runs on south; `bc2_w15388`, `bc2_w15432`; `bc2_w15565`, b's clear:
  its metal x 10226 comes down from a pad at about (10137,14695), the east end of the poly row y 14696 whose
  west end is the pad (9092,14697) of `bc1`'s bus line y 14699: seen in `r17_e1.png` and `r17_m1.png`, not
  drawn, not checked). Also: W's output
  `eof_w15300` goes on from the pad (8836,15456) into the next unit of column B (y 15440-15540: a pad row
  y about 15450-15470, a second pad (8833,15515); `r16_s2.png`, 1.6x), which is not drawn (`bc1` (continue),
  free): the column's units below W are of the same build (`railprof.py 8692 8732 15400 15700`: gate
  15469-15492, diffusion, field 15552-15591, diffusion, gate 15686). Ambiguity 53 (the open gap's colour) is
  piece `vw`'s open point. Another open end of `lc3_w9947` (not its driver): its bus metal in `tcw` north of
  its last pad (y 2745).
- Seen beside pieces `in390` and `in172`, not drawn (other nets; `bc2`, free): the poly rows y 14696, 14739,
  14782, 14826 of the same band (each from a pad at its west end to a pad at x 10085-10137, whose metal turns
  south in nested Ls at x 10140-10230); `bc1`'s bus metals y 14608 and y 14656 where they turn south at
  x 9184 and x 9141 (thin metals on south), and the thin metals x 9228, 9271, 9357, 10008, 10051 and the
  three rails over the band; the pad (10500,14565) north of T with a metal from the west along y 14565 and a
  poly east across the rails; the rails north of y 14590.
- Seen beside piece `ck6` and the units V and W, not drawn (other nets; `bc1` (continue) unless said): the other twelve
  bus metals of the 13-line bus and their pads (west ends x 7790 / 7835; east ends x 8250 / 8293, each
  with a poly under the rails to a pad at x 8580 / 8625 and a metal on east: the line y 14656 runs to
  x 9144 and turns south, the line y 14699 ends on a pad (9092,14697)); the VSS rail x 8510-8560 north of
  y 14816, its band y 14816-14878 and column B's rail x 8687-8737 outside y 14900-15070; the two thin
  metals down column B (x 8637-8650, `bc1_dec00_n`, south of y 15060; x 8789-8801 from the pad
  (8792,14870)); the pad (9008,14828) with its track x 8915-8935 (from the south) and its poly column
  x 9002-9020 north to y 14610 and east (drawn since run 17, piece `in390`; the crossing at (9011,14656)
  is Ambiguity 58); an outlined plain island
  x 8565-8625, y 14900-14968 north of U's plate (not identified); in `bc2`'s ground the vertical metals
  x 9130-9150, 9170-9195, 9215-9240.
- **`rst_c`'s other ends** (piece `rc`): `rst_c`'s lines in `lc3` and `busl` (the row y 14697 east of
  x 7550); `lc2`'s notes call the diagonal "a further branch", with no other open end known.
- **`res_b`'s and `lpstb_b`'s loads beyond `busl`'s south edge**: `res_b` leaves at (6366,15000) and
  `lpstb_b` at (6408,15000) into `bl0` (the follower takes the second to (6408,15150) and beyond). Taps on
  `lc2`'s, `lc3`'s and `busl`'s stretches were read by those packages (none drawn).
- Seen beside piece `isrc5`, not drawn (other nets): the poly row under its metal y 7257 east of x 6313
  (Ambiguity 34); the tracks x 6690, 6735 of the crossing field with their Ls; the metals y 8405-8417 and
  y 8448-8460 over the poly columns. All in `busl`'s northern part. (Drawn since run 11: the row of the pad
  (6513,7889) and the tracks x 6514, 6602, 6645 with their Ls, pads and poly columns: pieces `rl`, `w5936`.)
- **The gates of `rst_a` that are not drawn** (the pull-down on the row y 15258 is drawn since run 16: row C of piece `vw`, W's clear; the four latch copies' clear rows are left) (the table at the end of piece `isrc4`): the four latch
  copies' clear rows (y 16172, 16737 under the rail x 8686-8731: the rows are stubs of 20-25 px at
  x 8930; y 16303, 16909 under the rail x 8336-8384: the rows are drawn to their ends, x 8326) and the
  pull-down on the row y 15258. To draw them: place the copies (`findcell` lines in that table), look round
  every pad (R45), read the upper left copy by hand (it straddles y 16300). `bc1` (continue), `bc3`.
  Still not looked at: `trunks`' poly y 16950 east of x 10470, a gate row of the unit under the rail
  x 10540-10585 (`bc4`); `trunks`' two contacts (13565,15275), (13565,15190) and the contact (13627,16626)
  in `bd1`. Other taps of the long stretches that `trunks` drew were not looked for (R4).
- Seen beside piece `isrc4`, not drawn: the metal lying on its row y 17736 (Ambiguity 29: the bundle's
  track x 8098, east along the row, south at x 8380); the diffusion-coloured area x 8000-8168, y 16600-16780
  (Ambiguity 32); the other tracks of the bundle x 8012-8229 (they step with this one at y 17250-17350 and
  y 16640-16750); `bc1`'s tracks `bc1_dec01_n` (x 8056) and `bc1_g6_in` (x 8143) are drawn to y 16300 and run
  on south over the row y 16303 without contact.
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
- **`lc1_w7170`, the input of the inverter that drives `rcs_x1`: traced to its source** (`lc2`, `lc3`
  and piece `rc`, run 13): `lc1_w7170` = NOT `rst_c`.
- `res_b`, `lpstb_b`, `rst_a` and `tl3_w3982` beyond the gate column: drawn (pieces `isrc5`, `rl`, `w5936`).
- `rst_b` (a buffered copy of the reset) north of `lc1`'s strip: V4, x 5288-5310, "turns east
  at y 6720" (`lc1`); `rst_c`'s branch north at x 5713 (followed by `lc1` to y 6365).
- The other five polys of `tl5`'s south bus (x 5365, 5412, 5453 and two more) south of y 6350.
- **Where the latch's output `bd1_n2` goes north of (6711,15000)** (task (e)): **found, but for one
  stretch that is not drawn** (run 14, piece `n2n`): the track ends on `bd1_n2`, the input of the
  inverter that makes `rcs_e3`. **Left: the 4,600 px in `busl`'s region** (claimed: waitingforvsync,
  4780-7550 x 10400-15000), from (6711,15000) north on x 6711 to a corner (6711,13249), east to
  (6777,13249), north on x 6776 to (6775,10400); as a trace line, `M 6711,15000 y13249 x6776 y10400 w=13`.
  Read by text and one view (Ambiguity 47), not reviewed: the follower's candidates (6711,14686),
  (6711,14526), (6710,14429), (6712,14299), (6711,14222), (6711,14179), (6710,13996), (6710,13690),
  (6711,13635), (6712,13584), (6711,13541), (6711,13506), (6775,12168) are bars of the poly rows beneath
  (the metal 9-15 px wide at each). Whoever draws it (`busl`'s holder, or this package when `busl` is
  released) labels it `bd1_n2`, and `bd1_n2` in `trace/eof.txt` then becomes an alias to drop
  (`tools/rename.py`, the coordinator's refresh).
- `bd1_n1` and `bd1_an` have no other exit (run 7: `bd1_an` ends on G6's pad; `bd1_n1`'s metal ends on the
  pad of N2's third pull-down; N1's west buried contact (13766-13802, 15572-15600) carries a 24 x 27 px poly
  pad with nothing leaving it, field south of it under `bd1_an`'s metal). `bd1`'s own uncertain items on
  the latch (the upper tie, N2's third pull-down) are as they were.
- Seen beside the wire, not drawn (other nets): (1) **`rst_a`'s metal x 13630 has a contact that `bd1`
  does not draw**, a ring at about (13627,16625) on a pad whose poly runs east along y 16622 into the gate
  column's untraced part (y 16280-16900) (`f_k2.png`, 3.8x, metal and clean): another load of `rst_a`
  (`bd1`-`bd3`); (2) `ck_out`'s metal along y 17905, which `trunks` draws from x 10320 to 10230, runs on west
  to a pad at about (9770,17910), whose poly goes on west to a pad (9595,17905) (`f_k12.png`); (3) the
  third, inner Z bend of the braid at x 11640 (from y 17860 east of it to y 17690 west of it, pad about
  (11240,17725)) and the pads (11290,17775), (12850,17860): undrawn lines of the bottom bus (`busb`); (4)
  the diagonal `k4` (`rc_eq_r6`) from (13304,16690) south-west towards x 13175, parallel to this wire's
  (`bd1`'s Not done); (5) the tracks x 6665 and 6752 beside the wire in the left bus field, with pads
  (6665,16215), (6752,16212) and poly links like this one's; the line that turns at (6755,18040) is x 6752's.
- **The dense group y 15880-16125 of `bd1`'s gate column** (where `h_eq_r0`, `ck_out` and `rst_a_n` meet) is
  not on the latch's path after all: `bd1_k`'s pad (13674,15975) only passes it. It stays with `bd1`-`bd3`.
- The rest of the slice-0 logic of `cdp1`'s channel around the inverter was not traced; the
  inverter's own rectangle (x 8330-8650, y 4700-4880) has nothing else in it.

## Corrections (coordinator, from the handoffs of 2026-11-19, fourth batch)

- Piece `n2n`, Ambiguity 47 and Not done ("the 4,600 px ... read and not drawn", "believed"): the stretch is drawn and reviewed (`busl` run 7, piece `n2`: x 6711, an arm at y 13247, x 6776; no pad, no tap). `rcs_e3` = NOT `bd1_n2` is traced.
