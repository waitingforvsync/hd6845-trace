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
  **`eof_w15127` = NOT(`eof_w15172` OR `eof_w15300`)** (unit V) and **`eof_w15300` = NOT((`eof_w15350`
  AND `eof_w15390`) OR `eof_w15127` OR `rst_a`)** (unit W). So the ripple counter's clock `lc3_w9947` =
  NOT `eof_w15127` is the inverse of one side of a set/reset latch: it goes low when `eof_w15350` and
  `eof_w15390` are both high (or at reset) and high again when `eof_w15172` is high. Each unit's third
  pull-down is gated by the other's load plate; V's single input lies on both rows of its stack (a
  hairpin), W's stack has two inputs. **Row C, the gate of the transistor that clears W, is `rst_a`'s row
  from the end pad (8966,15260)** of piece `isrc`: one of the undrawn gates of `rst_a` is now drawn.
- **Marked**: both equations rest on the plates' ties (uncertain as in every load of this build). The
  pull-downs are all drawn without `?`; the open gap east of the rail, through which both stacks'
  diffusions run, is read from edge lines against its colour (Ambiguity 53).
- The four inputs and outputs are drawn to ports: `eof_w15172` (the hairpin's row, on east at (9150,14653)),
  `eof_w15350` (a metal south, 1,346 px by the follower), `eof_w15390` (a metal north to the pad
  (9008,14828), whose poly goes on north) and W's output `eof_w15300` (a metal south to a pad (8836,15456)
  at the next unit of the column). None of the four is followed.

Full extraction with run 16: 2,378 nets, 4,362 transistors, 0 errors, 0 warnings.

Run 17 (Tom Seddon's session, Claude Fable 5.2; 2026-11-20 01:05 +0000 on). Two pieces, `in390` (wiring only)
and `in172` (3 transistors), no uncertain item: **two of the three inputs of the latch V/W are followed to
their sources**, both at the east gate column of the bottom-centre logic (`bc2`'s ground, free).

- **`eof_w15390`, the lower gate of W's stack, is `bc2_w15607`, the lower node of `bc2`'s latch unit b**
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
  node `bc2_w15000` is low, and set low by `eof_w15350` AND latch unit b's lower node (or the reset).
- **Not followed**: `eof_w15350` (the metal south of (8881,15465)): the follower ends on a pad at about
  (8882,16644), by position the output row of an undrawn latch copy in column B (Not done).

Full extraction with run 17: 2,377 nets, 4,365 transistors, 0 errors, 0 warnings.

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
| `in390` | x 9005-10275, y 14594-15520 | `eof_w15390`'s poly column x 9005-9023 north of the pad (9008,14828), under `eof_w15172`'s metal y 14785 and `bc1`'s bus metals y 14742, 14699, 14656; east at y 14600-14621 as a row (the bus metal y 14603-14618 on it to x 9190), 1,070 px under eleven vertical metals to a pad with a contact (10092,14609); a metal east along y 14611 to a corner (10268,14607) and south on x 10268 onto `bc2`'s metal end (10267,15515) of latch unit b's output pad |
| `in172`, the row | x 9140-10520, y 14644-14714 | `eof_w15172`'s poly row y 14644-14664 on east of x 9150 under the same vertical metals, a step south at x 10284-10302, the lower row y 14687-14704 under the metals x 10355 and x 10397 into the output box (10484-10520, 14681-14714) |
| `in172`, unit T | x 10335-10772, y 14590-15007 | a NOR at the top of `bc2`'s east column: a diffusion body west of the VSS rail (x 10495-10530, y 14622-14771) whose top and bottom bands run into two VSS boxes under the rail (contacts (10562,14613), (10562,14769)); gate row 1 (y 14643-14665) from pad A (10352,14654), gate row 3 (y 14728-14750) from pad B (10440,14738); the node between them with the output box; a node strip y 14690-14706 east under the rail to the load: a plate x 10660-10716, y 14668-14762 over a strip to the VCC box (contact (10742,14712)), a tail south into the tie box (10624-10652, 14738-14768); pad A's metal x 10355 south to a foot onto `bc2`'s pad (10395,15000), pad B's metal x 10441 south onto `bc2`'s metal at y 14940; the two rails over the unit |

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
eof_w15300 = NOT((eof_w15350 AND eof_w15390) OR eof_w15127 OR rst_a)    unit W, y 15285-15470
```

From the full extraction (which prints V's first term as `eof_w15172 & eof_w15172`: the hairpin gives two
gates in series on one net): V's load (8596,15133) 26/52; its stack 90/24 twice, both gated by
`eof_w15172`; (8645,15216) 34/23, gate `eof_w15300`, `eof_w15127` to `vss`. W's load (8595,15317) 30/54;
its stack 105/20 (gate `eof_w15350`) over 104/21 (gate `eof_w15390`); (8642,15384) 36/22, gate
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
which makes the clock `lc3_w9947` high; `eof_w15350` AND `eof_w15390` high, or `rst_a` high (the reset),
forces `eof_w15300` low, which lets `eof_w15127` rise, the clock low. So **the ripple counter's clock is
set high by `eof_w15172` and low by (`eof_w15350` AND `eof_w15390`) or the reset**; while both conditions
are low it holds. During reset the clock is `eof_w15172` itself. What the three signals are is open: none
of them is followed (Ports, Not done).

### Pieces `in390` and `in172`: two of the latch's inputs to their sources (traced; no uncertain item)

```
eof_w15390 = bc2_w15607                         one net: latch unit b's lower node (bc2), by a poly row and a metal
eof_w15172 = NOR(bc2_w14955, bc2_w15000)        unit T, the top unit of bc2's east gate column, y 14598-14790
```

From the full extraction: `t2121` at (10512,14654) 35/22, gate `bc2_w15000`, `vss` to `eof_w15172`; `t2122` at
(10512,14739) 35/22, gate `bc2_w14955`, `eof_w15172` to `vss`; the load `t2123` at (10688,14704) 27/56.
`tools/unsure.py --equations eof_w15172`: FIRM. W's equation now reads `eof_w15300` = NOT((`bc2_w15607` AND
`eof_w15350`) OR `eof_w15127` OR `rst_a`) (marked as before: W's tie). With `bc2`'s equations (marked there:
copies of `tl1`'s cells, reviewed on Opus only, R31): `bc2_w15000` = NOT((`bc2_w14912` AND `bc2_w14955`) OR
`bc2_w15029`), latch unit a's upper node, and `bc2_w15607` = NOT((`bc2_w15352` AND `bc2_w15432`) OR
`bc2_w15476` OR `bc2_w15565`), latch unit b's lower node.

What it does. `eof_w15172` is high only while latch unit a's enable `bc2_w14955` is low (the latch holds) and
its upper node `bc2_w15000` is low, i.e. while unit a holds a set bit (`bc2_w15029` high; believed, from
`bc2`'s equations); that sets `eof_w15127` low and the ripple counter's clock `lc3_w9947` high. The clock goes
low again when `eof_w15350` and latch unit b's lower node are both high, or at reset. What latch units a and b
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
| the row east of x 9150 | y 14644-14664 to x 10302; `bc1`'s bus metal y 14648-14664 lies on it from x 9044 to x 9141 and turns south there (run 16); under the same vertical metals as the row above, and under `eof_w15390`'s metal x 10268 | `eof_rows.py col`; `eof_cchk.py` at twelve crossings: 26-47 (26 under the wide metal x 9489; no ring, no pad); `px.py row 14652 10254 10310 3 acid1b,metal` against the same row under the metal x 10051 (`10036 10072`): the same dark bar at the metal's edge, salmon through it |
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
| `rst_a` | poly | (8930, 16728-16746) | ? | the row west of the tap pad (8966,16737): into the gate column |
| `rst_a` | poly | (8930, 16163-16181) | ? | the row west of the tap pad (8962,16172): into the gate column |
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
| `eof_w15350` | metal | (8873-8889, 15465) | in | piece `vw`: the upper gate of W's stack, from the south: the metal of the pad (8881,15351) runs on south (the follower: corners (8890,15699), (8926,15699), (8922,15913), (8882,15915), end (8882,16623); not checked) |
| `bc2_w15607` | metal | (10261-10275, 15520) | in | piece `in390`: `eof_w15390`'s metal x 10268 onto `bc2`'s metal x 10267 (its port (10267,15515)), from latch unit b's lower node. (The port `eof_w15390` (9002-9020,14790) of piece `vw` is gone) |
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
    metal and ends at x about 8666; row 2 (`eof_w15390`, from the pad (8922,15392)) ends at x about 8681;
    the 14 px between are not poly in the clean shot and both metal shots (the Logic table's row). Seen as a
    small outlined box at (8664-8680, 15370-15395) in all shots (`r16_wbox.png`, 6x, four shots: the two
    rounded ends and the edges of the diffusions above and below). If they were one poly, `eof_w15390`
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
    y 14785 crosses `eof_w15390`'s poly column x 9002-9020.
58. **`bc1`'s bus metals on and over `eof_w15390`'s poly** (piece `in390`; traps 13, 15). The bus metal
    y 14603-14618 lies on the row from its corner (x 9005) to x 9190, where the metal turns south (185 px),
    and the bus metals y 14656, 14699, 14742 and `eof_w15172`'s metal y 14785 cross the column x 9005-9023.
    Read as no contact at any: the poly keeps its width (18-21 px, no pad), neither metal shot has a ring,
    the clean shot has no hole on the row (`textmap.py 9020 14596 9200 14624 3`). Against, at the crossing
    (9014,14656) only: the clean shot's red minus green is 1 there on a 6 px streak (`eof_cchk.py 9011,14656`),
    and the column is dark orange-brown in the clean shot from the corner to y 14680 (137/66/32 under the
    metal y 14656, 134/82/27 at the corner) where the same poly is salmon (203-221/147-167/101-119) under the
    three metals south of it and `eof_w15172`'s row is salmon under the same metal (`px.py col 9014 14594
    14690 4 all`; `r17_a2.png`): read as a stain of that shot, since the chip-2 stripped shot has plain poly
    there and no pits. If the crossing were a contact, `eof_w15390` would also be `bc1`'s bus line y 14656.
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
hairpin's poly row, the hairpin's metal y 14785 over `eof_w15390`'s poly column.

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

## Not done

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
  `eof_w15390` = `bc2_w15607`, piece `in390`). **Left, and next: the third input, `eof_w15350`**, the metal
  south of (8881,15465): `follow.py 8880 15480 S --gap 16` gives corners (8889,15698) east, (8925,15702) south,
  (8922,15914) west, (8882,15915) south and an end (8882,16623), 1,238 px; `eof_cchk.py 8882,16640` finds a
  contact there (hole -8, centres 192/200): a pad at about (8882,16644). Not looked at on a view: the two
  "wide" stretches at the corners (trap 16), what the metal crosses, and the pad's poly. By position (my
  inference, not read) the pad is on the output row of the lower of the two undrawn latch copies under the
  rail x 8686-8731 (`@inst tl1_ua 5976,12146 mx=2685` with `tl1_ub 5973,12146 mx=2686.5`, the table at the end
  of piece `isrc4`: its clear row is y 16737, and in `bc2`'s unit a the output row lies 87 px above the clear
  row): so the next piece is that latch copy (`bc3`'s ground, free: place the two cells, overlay, look round
  every pad, R45), with the wire. **Then, to say what the clock's latch does**: `bc2`'s latch units a and b,
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
