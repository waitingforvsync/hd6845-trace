# busl: the left bus field

Queue row `busl` of `notes/work-packages.md` (written busL until 2026-11-19): the wiring between the
left array (`larr`, rows end at x 4780) and the central datapath (`cdp3`, `cdp4`, from x 7600).
Claimed region: x 4780-7550, y 10400-15000 (the main part; the northern part 6450-7600 x 6750-10400
is not started). Coordinates are metal-shot pixels; images are in `cache/scratch/busl/`. Wiring only:
no transistor has been found in the field so far. Twenty-two pieces are drawn: `h8`, `ch1`, `lc9`, `ctl`, `d6`, `sr`, `kb`, `n2`, `x68`, `x69`, `r12`, `r13`, `e6`, `p2`, `fb`, `fa`, `fc`, `fd`, `fe`, `ga`, `gb`, `gc`.
Pieces `d6`, `sr` and `kb` begin in the northern part (x 7180-7600, y 8795-10400), drawn there as far
as their pads or, for `sr`, the end of `eofw`'s metal; pieces `fb` and `fa` run through it from y 10400
to their end pads at (7120,7214), (7165,7170), and pieces `fc`, `fd`, `fe` (run 11) likewise, to `tl6`'s
port (6236,6350), `tc2`'s port (7533,6400) and the wide rail at (7592,8863), and pieces `ga`, `gb`, `gc` (run 12) to `lc1`'s port (6450,7780) and the end pads (6861,7257), (6904,7301); nothing else of the northern part is.

## Status

Run 1 (richtw1's session, Claude Fable 5.2; 2026-11-19 13:50 to 14:00 +0100). Survey of the whole main
part, and one piece, `h8`, wiring only, no uncertain items:

- **The eight west outputs of the central datapath's register row H reach eight rows of the left
  array** (piece `h8`). Each `cdp3_hw_c#` (# = 7..0; `cdp3`: hw = NOT q1 of the 8-bit register row H)
  is drawn end to end across the field: a poly row west from `cdp3`'s piece at x 7600, a pad, a metal
  track south round one step of a staircase, a pad, and a diffusion row west to the array's edge at
  x 4780. The order is kept: c7 goes to the northernmost row (y 11338), c0 to the southernmost
  (y 14894); seven of the eight rows are 477 px apart, the array's row pitch.

Run 2 (richtw1's session, Claude Fable 5.2; 2026-11-19 14:16 to 14:29 +0100). One piece, `ch1`, wiring
only, no uncertain items:

- **`cdp4`'s eight channel-1 lines are its row C latch inputs, and each reaches a row of the left
  array** (piece `ch1`). For every slice # the poly row `cdp4_bus_s#` (channel 1, x 7600, y 11878 ..
  12182) and the poly row `cdp4_in_s#` (channel 2, x 7600, y 13636 .. 13332: the data input of the
  8-bit latch row C, through the pass transistor gated by `cdp4_ld`) are one net, joined in the field
  by a metal track between poly pads; and the same track has a pad on the east end of one poly row of
  the left array (s7 y 11488, s6 11922, s5 12442, s4 12984, s3 13397, s2 13874, s1 14351). s0's track
  leaves the region south at (5451,15000) and ends 45 px on, on the pad of the next such row
  (y 15042, in `bl0`'s region, not drawn). The two names are gathered by `@alias` in `trace/busl.txt`
  (shown as `cdp4_bus_s#`); the rename is the coordinator's.

Run 3 (richtw1's session, Claude Fable 5.2; 2026-11-19 16:30 to 16:42 +0100). One piece, `lc9`, wiring
only, no uncertain items:

- **The nine metal lines that leave `lc3` south at y 10400 run down the whole field as one staircase
  bundle and end at its foot on the poly rows of the bottom-centre logic's 13-line bus** (piece `lc9`).
  With `tla`'s metal of `rcs_e4` (the tenth and easternmost line, drawn in `trace/tla.txt`) the lines
  keep their order through two staircases (y 11491-11880 and y 12380-12772) and turn east along
  y 14916-14528, the westernmost lowest. Seven end on a poly pad (x 6320-6409) whose poly row runs east
  under the next thirty tracks: `lc3_e9798` on the row y 14567, `lc2_w9079` on 14611, `lc3_e9756` on
  14654, **`rst_c` (the input of the inverter that drives `lc1_w7170`) on 14697**, `lc2_w8450`
  (the ripple counter's clear) on 14740, **`lc3_w9947` (the ripple counter's clock, `lc3_w9947`) on
  14784**, and `rst_a` on 14914. The rows are drawn to the region's edge at x 7550; they run on
  240-290 px to pads at x about 7790 and 7835, the west ends of `bc1`'s 13 bus metals (seen, not drawn:
  `bc1`'s region). `res_b` and `lpstb_b` turn south instead (x 6366, x 6408) and leave the
  region at y 15000. No line has a pad or contact between y 10400 and its end.

Run 4 (richtw1's session, Claude Fable 5.2; 2026-11-19 17:02 to 17:20 +0100). One piece, `ctl`, wiring
only, one uncertain item (a metal over a box):

- **`cdp4`'s six control rows are followed across the field** (piece `ctl`). Each of the poly rows
  `rsel14_buf`, `rsel15_buf`, `rsel17_buf`, `rsel16_buf` (`cdp4`'s selects 1-4) (the selector's four select lines), `cdp4_rst` (the gate line of the
  pull-downs on the selector nodes) and `cdp4_ld` (the strobe of the 8-bit latch row C) runs west from
  x 7600 to a pad with a metal track.
  - **The four selects come from the south.** Their tracks step west in one nested staircase
    (y 13073-13204) and run on south out of the region at (6538,15000), (6581,15000), (6624,15000),
    (6668,15000) (the follower runs each to y about 16150-16190, in `bl0`'s ground). On the way each
    runs through one more pad, the west end of a poly row that goes back east to the gate group at the
    bottom-left corner of `cdp4` (x 7560-7650, y 13650-14030, not drawn): `rsel14_buf` on the row
    y 13701, `rsel17_buf` on 13809, `rsel16_buf` on 13961, `rsel15_buf` on 14004. So each select is also
    an input of that group.
  - **`cdp4_rst` ends on that group.** Its track (x 7468) ends on a pad (7467,13897); a poly from the
    pad runs 70 px east, under one track, to a heavy-outlined box (7535-7580, 13903-13940) at the
    group's west edge, read as a buried contact onto the group's node diffusion (not drawn: Ambiguity 9).
    Believed: the group drives `cdp4_rst`, from the four selects among other inputs.
  - **`cdp4_ld` is `bc1_ld_a`**, the twin output of the bottom-centre strobe driver (`bc1`: `bc1_ld_a`
    = NOT `bc1_ld_n`, the same NAND as row D's strobe `cdp4_ld6`). Its track (x 7556) passes over the
    same box, where neither metal shot shows it for 51 px (drawn `?M`, guide trap 27), comes out
    south of it, turns west along y 13982 to x 7448 and runs south onto `bc1`'s metal at (7448,14050).
    The two names are gathered by `@alias bc1_ld_a cdp4_ld`; `tools/unsure.py` lists the net as two
    pieces without the uncertain item.

Run 5 (richtw1's session, Claude Fable 5.2; 2026-11-19, after the run-4 handoff of 17:42 +0100). One
piece, `d6`, wiring only, no uncertain items:

- **The six data lines of `cdp4`'s 6-bit latch row D are the six "line g" rows of `cdp3`'s row A
  cells** (piece `d6`). Each poly row `cdp3_g_c#` (# = 2..7; x 7600, y 9123 .. 8907: `cdp3` follows it
  east to a contact on line g, which comes down from the large cell of row A in column c#) ends west on
  a pad of a staircase (x 7336 .. 7553). The pad's metal track runs south, steps 86 px west
  (y 9190 .. 9407), runs 4,300 px down the east side of the field with no pad or contact, steps 65 px
  west in a second staircase (y 13722 .. 13938) and becomes the metal that `bc1` draws from y 14040
  onto the contact of one of its six poly lines (y 14089 .. 14304). The order is kept: c2 goes to line 1
  (the foot of `cdp3_g_c2`), c3 to line 2 (`cdp3_g_c3`), c4 .. c7 to lines 3 .. 6 (`cdp3_g_c4` ..
  `cdp3_g_c7`, which `bc1` follows east only to x 8040; believed `cdp4_in6_s3` .. `s6`). Line 6 (c7) is the
  long track that the earlier runs met at x 7468 / 7511. The names are gathered by `@alias`
  (`cdp3_g_c#` canonical).

Run 6 (richtw1's session, Claude Fable 5.2; 2026-11-19 18:06 to 18:30 +0100). Two pieces, `sr` and `kb`,
wiring only, no uncertain items:

- **`tc2_sr_g` runs down the whole field** (piece `sr`). The metal that `eofw` left as an open end south
  of its corner pad (7446,8732) (net `tc2_sr_g` = the wire `lc1` called w7908, the enable of latch D, = `tc2_sr_g`,
  row 2 of the gate on `rst_ck`'s tap row) is one metal from there to the south edge of the region:
  south to y 8910, a diagonal south-west (the south-east line of the diagonal bundle) to (7209,9168),
  4,500 px south at x 7209 (the track west of piece `d6`'s line 1), the seventh step of the lower
  staircase (west along y 13680 to x 7145), three more jogs (y 14176, 14285, 14588) and out at
  (7187,15000). No pad or contact on the way. It runs on in `bc1`'s ground (seen at 1x, not drawn):
  south to y 15482, west to x 7103, south; the follower ends at (7100,16279).
- **`bus_eq_r15` comes from a diffusion at the foot of `cdp3`'s column 0** (piece `kb`). The poly row
  y 9450 (`cdp3`: the input of gate 1 of the NAND beside its row C) ends west of x 7600 on a pad
  (7554,9450); the pad's metal track runs 1,670 px south at x 7555 with no pad or contact and ends on a
  contact (7555,11118) on a diffusion pad, from which a diffusion band (y 11095-11127) runs east under
  column 0's VSS rail into `cdp3`'s ground (drawn to x 7600).
- Looked at and not this package's: **`wr_r15`'s row y 11837 does not enter the field**: west of
  x 7598 there is bare field at that height in both metal shots and the clean shot (view `b_ends.png`,
  3x); the row's west end is at about x 7603-7640 under `cdp4`'s metal x 7600-7645 (`cdp4` (continue)).

Run 7 (richtw1's session, Claude Fable 5.2; 2026-11-19 22:30 to 22:56 +0100). Three pieces, `n2`,
`x68` and `x69`, wiring only, no uncertain items: three of the six nested Ls at the selects' staircase (`rsel17_buf`'s,
`rsel16_buf`'s, these three with corners at y 13247-13376, and `trunks`' line between the last two).

- **The latch on R4's match drives the row counter's step logic: `rcs_e3` = NOT `bd1_n2`** (piece
  `n2`). `eof` had drawn `bd1_n2` (the output of `bd1`'s latch on `rc_eq_r4`) from the latch to this
  region's south edge at (6711,15000), and the track that leaves the region north at (6775,10400) on
  to `tl5`'s bus poly x 5412, which is `bd1_n2`, the input of the inverter that makes `rcs_e3`
  (its pieces `n2w`, `n2n`; the join between them was the open `bd1_n2`). Between the two ports it
  is one thin metal: 1,753 px north at x 6711, east along y 13247, 2,847 px north at x 6776. No pad,
  no contact, no tap. The join holds without any uncertain item (`tools/unsure.py`, all files: the
  labels of `bd1_n2`, `bd1_k`, `bd1_n2`, `bd1_n2`, `bd1_n2` are on one piece; only `bd1_q`,
  the load's tie in `bd1`, is apart, as before). The names are gathered by an alias (dropped at the rename);
  the renames are the coordinator's.
- **Two through lines** (pieces `x68`, `x69`): the tracks next east, on either side of `trunks`' line,
  cross the whole region with one step each and no pad or contact in it: `busl_x6820` (x 6820 north
  of its arm y 13290, x 6754 south) and `busl_x6906` (x 6906 north of its arm y 13376, x 6841 south).
  Neither end is in the region (follower: `busl_x6820` from (6817,9988) to (6754,16220);
  `busl_x6906` from (7078,8778) to (6839,16219)). `busl_x6906`'s arm lies for 65 px on the poly row
  y 13375 (`cdp4_bus_s1`'s, piece `ch1`): no contact (below).

Run 8 (richtw1's session, Claude Fable 5.2; 2026-11-20 13:42 to 13:51 +0100). Two pieces, `r12` and
`r13`, wiring only, no uncertain items (registers lead group; item (2) of the Not done list):

- **The read selects of R12 and R13 cross the field, and each has one tap** (pieces `r12`, `r13`).
  `regs` had drawn `rsel12_buf` and `rsel13_buf` from `sel`'s buffers to this region's south edge
  at (6452,14990) and (6494,14990), and two tracks north of y 10400 onto the pads of `cdp3`'s
  read-gate rows `cdp3_gate_e` and `cdp3_gate_f`; the 4,600 px between were read by the follower and
  not drawn. Each is one thin metal, the two innermost Ls of the nest that the selects of piece `ctl`
  continue: `rsel12_buf` north on x 6452, east along y 12984, north on x 6516, east along y 12097,
  north on x 6690; `rsel13_buf` north on x 6494, east along y 13028, north on x 6560, east along
  y 12141, north on x 6733. So **`rsel12_buf` is `cdp3_gate_e`** (the gate of the pass transistors that
  read row C onto bus N) **and `rsel13_buf` is `cdp3_gate_f`** (row H onto bus N): R12 and R13 are read
  through `cdp3`'s rows E and F, now on drawn geometry with no uncertain item.
- **Each track has one pad in its lower run, the west end of a poly row into `cdp4`'s corner gate
  group**: `rsel12_buf` at (6452,13854) on the row y 13852, which runs east under thirty tracks and
  steps south at x 7528-7550 onto the group's gate row 4 (y 13873, `cdp4`'s `rsel12_buf_u`);
  `rsel13_buf` at (6495,13744) on the row y 13744, which runs straight into the block of gate row 2
  (`cdp4`'s `rsel13_buf_u`). With them the extraction gives, firm (`tools/unsure.py --equations`):
  **`cdp4_rst` = NOR(`rsel12_buf`, `rsel13_buf`, `rsel14_buf`, `rsel15_buf`, `rsel16_buf`,
  `rsel17_buf`)**: the selector's nodes are released only while one of R12-R17 is being read.
- The names are gathered by `@alias` (`rsel12_buf` with `rsel12_buf_u`, `cdp3_gate_e`; `rsel13_buf`
  with `rsel13_buf_u`, `cdp3_gate_f`); the renames are the coordinator's.
- One crossing is recorded as an ambiguity (15): the track x 6452 over `cdp4_bus_s1`'s row y 13375 is
  dim and reddish in both chips for 18 px, without pad or ring. And Ambiguity 13 (AMB-039) has its
  second direction: the row y 13744 has its own driver, by a pad.

Run 9 (richtw1's session, Claude Fable 5.2; 2026-11-20 14:09 to 14:20 +0100). Two pieces, `e6` and `p2`,
wiring only, no uncertain items: everything that arrives from `lc3` at y 10400 west of piece `lc9`
(item (3) of the Not done list) and the staircase at x 5100-5700 (item (5)).

- **`lc3`'s six diagonal metals run down the west side of the field and out of it** (piece `e6`).
  `lc3_e9577` .. `lc3_e9793` (each from the pad of its crossing row in `lc3`) keep their order: each
  diagonal turns south (x 5691 .. 5474), steps west along its own arm of a nest of Ls (y 10928 ..
  10752) and runs 4,200 px south on its own track (x 5322, 5279, 5235, 5192, 5148, 5105) to the region's
  edge at y 15000, with no pad, contact or tap. The sixth, `lc3_e9793`, has no arm: its metal ends on
  a pad (5473,10707), a poly goes on south and west along y 10750 **under the fifth line's arm** (no
  contact) to a pad (5102,10750), where its track starts. South of y 15000 the follower runs each to
  an end about 477 px (the left array's row pitch) below the last: (5326,15381), (5284,15859),
  (5239,16506), (5194,16981), (5151,17462), (5107,17938) (not read: `bl0`'s ground and below).
- **`rst_n` goes down the west edge of the field to `bl0`'s wide inverter: `bl0_w15412` = NOT
  `rst_n`** (piece `p2`). The poly that `lc3` leaves at (5475,10400) (from `rst_n`'s end pad
  (5473,10207)) turns west at y 10599, steps south-west along a diagonal and runs west as the row
  y 10663 to a pad (4907,10663); the pad's track (x 4909) runs 4,400 px south with no pad or contact
  and ends on a pad (4909,15087), the west end of the poly row y 15088 that `bl0` draws from x 5700
  east as `bl0_w15088`. The last 88 px of the track and the row from the pad to x 5700 lie south of
  this package's region (in `bl0`'s, where no one had drawn them) and are drawn here to close the join.
  Firm (`tools/unsure.py --equations`: `bl0_w15412` = NOT `rst_n`).
- **`lc2_w8450` has a second branch into the field** (piece `p2`): the poly that `lc3` leaves at
  (5541,10400) (from the end pad (5540,10165) of the metal that is also line 5 of piece `lc9`) turns
  west at y 10641, steps south-west and runs west as the row y 10706 to a pad (4822,10708); the pad's
  track (x 4822, the westernmost of the field) runs south out of the region at y 15000 (follower: to
  (4823,16690)), no pad or contact on the way.

Run 10 (richtw1's session, Claude Fable 5.2; 2026-11-20 15:33 to 15:45 +0100). Two pieces, `fb` and
`fa`, wiring only, no uncertain items: the two foot rows of item (7) of the Not done list and their
tracks, the next two Ls of the nest east of `busl_x6906`'s.

- **The foot rows y 14870 and y 14827 each lead 7,700 px north to a poly row at the top of the
  northern part** (pieces `fb`, `fa`). Each net is one wire with no tap between its ends: a poly row
  that comes in from the east at x 7550 (seen on east to a pad under `bc1`'s bus metals, (7836,14872)
  and (7794,14826), not drawn) and ends west on a pad ((6885,14871), (6927,14827)); the pad's metal
  track north (x 6885, x 6927); an arm 64 px east (y 13421, y 13463); 4,400 px north (x 6949, x 6992)
  out of the claimed region at y 10400 and on to a diagonal north-east in the bundle; a pad
  ((7121,8797), (7163,8842)); a **poly column** north under `eofw`'s staircase metals (no contact);
  a second pad ((7121,8627), (7164,8581)); a metal 1,400 px north (x 7121, x 7164) over six drawn
  rows of `bw` and `eof` (no pad on any); and an end pad ((7120,7214), (7165,7170)) on the east end of
  a poly row that runs on west into the crossing field (y 7214, y 7171; drawn 60 px, seen as poly to
  x 6720 and as a pale band under `eof`'s staircase arms west of that, not read).
- What they are is not known: neither end is drawn by any package. Named for their place, as the
  through lines of run 7: `busl_x6949` (row y 14870) and `busl_x6992` (row y 14827).

Run 11 (richtw1's session, Claude Fable 5.2; 2026-11-20 17:10 to 17:45 +0100). Three pieces, `fc`, `fd`
and `fe`, wiring only, one uncertain item (a poly row's last 42 px under a wide rail): the next three
Ls of the nest east of `busl_x6992`'s, which are also the next three diagonals of the bundle north of
y 10400. Two of the three have a named net at their north end.

- **`rcs_mv` runs from the top-left logic down the whole field and out of it south** (piece `fc`).
  `tl6` had drawn `rcs_mv` (= NOR(`tl3_w4546`, `tl3_e4852`), the net whose inverse is term 1 of the row
  counter's step request) to a poly that leaves its region south at (6236,6350). That poly column runs
  on 550 px south under ten horizontal metals (no contact) to a pad (6232,6911); the pad's metal runs
  980 px east along y 6913 and 1,700 px south on x 7208 to a pad (7207,8625); a poly column goes on
  under the two staircase metals to a pad (7206,8798); from there the metal is the diagonal
  (7208,8908)-(7035,9081), the track x 7036, an arm y 13507 and the track x 6971, which leaves the
  region at (6971,15000) (follower: on to (6970,15282), not read). No pad, contact or tap on the way:
  it is a through line, 9,700 px, and its loads south of y 15000 are open (`bl0`).
- **`tc2_r5718` runs from the top-centre logic to a poly row at the foot of the field** (piece `fd`).
  `tc2` had drawn the line of its pad (7530,6324) (from a poly row y 5718 that comes in from the east
  past x 8250) to a metal leaving south at (7533,6400). It is one metal on south: x 7533, a 22 px jog
  west at y 7279, x 7511, west along y 7453, south on x 7360 to a pad (7357,8667); a poly column
  under the staircase metals to a pad (7337,8798); the diagonal (7338,8844)-(7078,9104), the track
  x 7078, an arm y 13550, the track x 7014, a jog east at y 14308 to x 7058, a jog east at y 14438 to
  x 7100 and a pad (7098,14525), the west end of the poly row y 14524 (the row on which `rcs_e4` ends
  88 px further west, on its own pad (7012,14522): two nets on one row line). The row is drawn east to
  x 7550; it runs on toward `bc1`'s bus pads (not drawn). No tap on the way.
- **A third wire of the same build, from under `cdp3`'s column 0 rail to the row y 14480** (piece
  `fe`, `busl_x7122`): a poly row y 8863 that comes in from the east under the wide rail x 7550-7645
  (its last 42 px, under the rail, are drawn uncertain; it is **not** joined to `cdp3`'s uncertain row
  of `cdp3_k_a`, which starts 8 px further east: Ambiguities 17, 18) to a pad (7423,8863); a metal west
  to (7385,8862), the diagonal to (7122,9125), the track x 7122, an arm y 13594, the track x 7058, a jog
  east at y 14267 to x 7100, a jog east at y 14396 to x 7144 and a pad (7143,14481), the west end of
  the poly row y 14480, drawn east to x 7550. No tap on the way; one crossing is recorded as an
  ambiguity (16: the track over `rsel13_buf`'s row y 13744, dim in both chips, the same row as
  Ambiguity 13's).
- **Seen, for `cdp3`** (not drawn; Ambiguity 18): the row y 8863 runs on east of the rail as a poly to a
  contact pad (7835,8862), whose metal goes **north** to a pad at about (7834,8645); `cdp3`'s metal
  `M 7835,8850 y9414` south of that pad is not there between y 8880 and about y 9150, so the row's net is
  not `cdp3_k_a` (whose metal starts at the contact (7833,9165)).

Run 12 (richtw1's session, Claude Fable 5.2; 2026-11-20 20:02 to 20:20 +0100). Three pieces, `ga`, `gb`
and `gc`, wiring only, no uncertain items: the rows y 14480 (west part), y 14437 and y 14393 of the Not
done list with their lines, which are **three more lines of piece `lc9`'s staircase bundle** (lines 11,
12, 13, inside `tla`'s `rcs_e4`; a fourteenth, onto the row y 14350, is seen and not drawn).

- **Latch D's data `lc1_w7780` runs down the whole field to a pad south of it** (piece `ga`). `lc1` had
  drawn `lc1_w7780` (= NOT `lc1_w7733`, gate E1 of the left-centre cluster; the data of latch D, whose
  inverse is `lc_step`) on a poly row to its port (6450,7780), "seen to x 6710". The row runs on east
  under eight tracks (no contact) to an end pad (6819,7780); the pad's metal goes 500 px south on
  x 6819 and 46 px west along y 8282 to a pad (6773,8323); a poly column goes on south under the
  staircase metals to a pad (6774,8625); from there the metal is the diagonal (6775,8692)-(6602,8865),
  the track x 6602, an arm y 9886, the track x 6516 (through y 10400), an arm y 11923, the track
  x 6343, an arm y 12813, the track x 6278 and a run east along y 14483 to a pad (6364,14482), the
  west end of the poly row y 14480. The row runs 690 px east under thirteen tracks (no contact) to a
  pad (7057,14480) (the row's west part: its east part, from the pad (7143,14481) on, is
  `busl_x7122`'s, with field between); the pad's metal goes south on x 7058, jogs east at y 14588 and
  runs south on x 7100 out of the region at (7100,15000) to an end pad (7100,15175), from which a poly
  goes south and east as a row y 15218 (drawn 70 px; it runs on east under `ck_out`'s track toward
  `bc1`'s rail x 7292-7342, not read). No tap in 9,300 px. So **the output of gate E1 has a load in the
  bottom-centre logic** besides latch D and the inverter that makes `lc1_w7862`.
- **Two wires of the same build beside it** (pieces `gb`, `gc`), each from the east end pad of a poly
  row of the crossing field at the top of the northern part to a poly row at the foot of the field:
  `busl_x6559` from the pad (6861,7257) of the row y 7258 by the metal x 6861, an arm y 8320, a pad
  (6817,8408), a poly column, a pad (6818,8668), a diagonal, the tracks x 6646, x 6559, x 6386 and
  x 6322 (arms y 9928, 11967, 12857) and a run east along y 14440 to a pad (6407,14437) on the row
  y 14437, drawn east to x 7550; `busl_x6603` from the pad (6904,7301) of the row y 7300 by the metal
  x 6905, an arm y 8364, a pad (6861,8366), a poly column, a pad (6861,8710), a diagonal, the tracks
  x 6689, x 6602, x 6430 and x 6365 (arms y 9970, 12010, 12899) to a pad (6365,14394) on the row
  y 14393, drawn east to x 7550. No tap on either. Neither end is identified: the rows y 7258 and
  y 7300 run on west into the crossing field (drawn 60 px), the rows y 14437 and y 14393 east toward
  `bc1`'s bus pads.
- **Seen, not drawn**: the fourteenth line (pad (6406,14350) on the row y 14350; tracks x 6408, x 6473,
  x 6646, x 6732; pads (6904,8669), (6904,8408); a metal east and north on x 6948 to a corner
  (6940,7042) and west along y 7042, the follower's end (6186,7042), beside `bd1_n2`'s y 7000).

Full extraction with run 12: 2,460 nets (two more than without the three pieces, 2,458: `busl_x6559`,
`busl_x6603`; the third wire lengthens `lc1`'s net), 4,590 transistors, 0 errors, 0 warnings. The
package by itself: 60 nets, 0 errors, and the two warnings of run 9.

Full extraction with run 11: 2,455 nets (one more than main's 2,454: `busl_x7122`; the other two wires
lengthen `tl6`'s and `tc2`'s nets), 4,579 transistors, 0 errors, 0 warnings; 96 nets joined only through
uncertain items, as on main. The package by itself: 57 nets, 0 errors, and the two warnings of run 9.

Full extraction with run 10: 2,455 nets (two more than main's 2,453: the two new wires), 4,579
transistors, 0 errors, 0 warnings. The package by itself: 54 nets, 0 errors, and the two warnings of
run 9 (`lc2_w8450`'s two branches).

Full extraction with run 9: 2,453 nets (one fewer than main's 2,454: `bl0_w15088` is `rst_n`), 4,579
transistors, 0 errors, 0 warnings; 909 of 1,349 equations firm. The package by itself: 52 nets,
0 errors, and two warnings that `lc2_w8450` is on two unconnected nets (its two branches, piece `lc9`'s
line 5 and piece `p2`'s poly, meet in `lc3`'s file, which is not loaded then).

Full extraction with run 8: 2,451 nets (main had 2,455: four joins, each wire with its `_u` end and
its read-gate row), 4,574 transistors, 0 errors, 0 warnings; 907 of 1,347 equations firm. The package
by itself: 44 nets, 0 errors, 0 warnings.

Full extraction with run 7: 2,379 nets (main had 2,378: two new through lines, one join), 4,351
transistors, 0 errors, 0 warnings; 849 of 1,279 equations firm, as on main (`rcs_e3` = NOT `bd1_n2`
depends on uncertain items, as `rcs_e3` = NOT `bd1_n2` did). The package by itself: 42 nets,
0 errors, 0 warnings.

Full extraction with run 6: 2,390 nets (unchanged: the two wires lengthen `eofw`'s and `cdp3`'s nets),
4,345 transistors, 0 errors, 0 warnings. The package by itself: 39 nets, 0 errors, 0 warnings.

Full extraction with run 5: 2,391 nets (six fewer: the six joins), 4,345 transistors, 0 errors,
0 warnings. The package by itself: 37 nets, 0 errors, 0 warnings.

Full extraction with run 4: 2,398 nets (one fewer: `cdp4_ld` and `bc1_ld_a`), 4,345 transistors,
0 errors, 0 warnings; 847 of 1,276 equations firm, as before. The package by itself: 31 nets, 0 errors,
0 warnings.

Full extraction with run 3: 2,399 nets (unchanged: the nine lines lengthen `lc3`'s and `lc2`'s nets),
4,345 transistors, 0 errors, 0 warnings. The package by itself: 25 nets, 0 errors, 0 warnings.

Full extraction with run 2: 2,374 nets (eight fewer: the eight joins), 4,290 transistors, 0 errors,
0 warnings. The package by itself: 16 nets, 0 errors, 0 warnings.

Full extraction with run 1: 2,382 nets (unchanged: the eight wires lengthen `cdp3`'s nets), 4,290
transistors, 0 errors, 0 warnings. The package by itself: 8 nets, 0 errors, 0 warnings.

## Inventory

The field (survey: `cache/scratch/busl/survey.md`; views `s0_metal.png`, `s0_acid1b.png`):

- About 55 vertical metal tracks at a pitch of 43.4 px between x 4822 and x 7554, stepping sideways in
  staircases; most run on north of y 10400 and south of y 15000. A wide metal x 4960-5010 runs the
  whole height. Track centres at nine heights: `tools/sel_cut.py h Y 4780 7560 --brief`.
- Horizontal lines of two kinds (told apart in the open column x 5072, `tools/busl_rows.py`,
  `tools/px.py`): **diffusion rows** about 22 px wide (chip-2 metal shot blue 80-87; clean shot cream
  160/128/98 between two dark edge lines) and **poly rows** about 28 px wide (blue 52-57; clean shot
  154/90/61 in the open).
- Poly row bands under the tracks at y 10330-10700, 11850-12150, 12550-12900, 13300-13700, 14050-14300
  (`bc1`'s 13-line bus enters it from the east), 14450-14950.
- Drawn by others inside the region: `trunks` (two lines), `bc1` (the bus, lower right), `tla` (7 items).

Piece `h8` (all eight nets have the same build; `#` = the slice of `cdp3`'s row H):

| Net | Poly row y (x from the pad to 7600) | North pad, contact | Track: upper x, step y, lower x | South pad, contact | Diffusion row y (x 4780 to the pad) |
|---|---|---|---|---|---|
| `cdp3_hw_c7` | 10361 | (6039,10359) | 6039, 11272, 5690 | (5690,11335) | 11338 |
| `cdp3_hw_c6` | 10404 | (5996,10402) | 5996, 11230, 5626 | (5647,11812) | 11815 |
| `cdp3_hw_c5` | 10447 | (5953,10445) | 5953, 11186, 5583 | (5605,12290) | 12291 |
| `cdp3_hw_c4` | 10490 | (5909,10488) | 5909, 11142, 5540 | (5562,12766) | 12768 |
| `cdp3_hw_c3` | 10535 | (5866,10533) | 5866, 11100, 5496 | (5514,13222) | 13247; steps north at x 5432 to y 13220 |
| `cdp3_hw_c2` | 10577 | (5822,10575) | 5822, 11054, 5452 | (5474,13722) | 13725 |
| `cdp3_hw_c1` | 10621 | (5778,10619) | 5778, 11012, 5409 | (5427,14197) | 14202 |
| `cdp3_hw_c0` | 10664 | (5735,10662) | 5735, 10966, 5366 | (5385,14888) | 14894 |

- The poly rows run straight for 1,560-1,870 px under about forty tracks each; no track has a pad
  over them (views `b1_acid1b.png`, `b1_metal.png` at 1.3x).
- The north pads are a staircase of poly pads, each the west end of its row, each with the north end
  of its track on it (`t1.png`).
- Each track leans about 20 px east into its south pad (c7's comes straight down); the track ends
  there (`tools/follow.py --gap 16` from each track both ways; `e1.png`, `e2.png`, overlays `o1.png`,
  `o2.png`, `o3.png`).
- Seven of the tracks cross the diffusion rows of the nets north of their own pad, and the poly rows
  of other nets, without contact: `tools/tl5_tracks.py v X Y0 Y1` down each lower track shows only
  pairs of 8-17 px dark bars (the two edges of each row) and no stretch without metal in both chips;
  the clean shot's short greenish stretches (6-10 px) lie on the south edge of each diffusion row and
  nowhere else.

Piece `ch1` (pads are poly pads with a contact, given by the contact's centre, measured in both
metal shots with `tools/busl_padc.py`; row centres with `tools/busl_rowy.py` in open columns; tracks
with `tools/follow.py --gap 16`; every row is poly, 23-24 px between its edge lines):

| Net | Channel-1 row (to x 7600) | From its west end | Array row (x 4780 to its pad) | Channel-2 row (pad to x 7600) |
|---|---|---|---|---|
| `cdp4_bus_s7` | y 11878, pad (5857,11878) | metal arm west along y 11880 to the track x 5800: a T. The track runs north to the array row's pad and south to the channel-2 row's pad | y 11488, pad (5799,11488) | y 13636, pad (5800,13636) |
| `cdp4_bus_s6` | y 11922: the row itself runs on west to the array (one poly, x 4780 to 7600) | pad in the row at (5757,11922); track x 5757 south | the same row | y 13592, pad (5756,13592) |
| `cdp4_bus_s5` | y 11966, pad (5713,11966) | track x 5713 south, through the array row's pad, to the channel-2 pad | y 12442, pad (5713,12443) | y 13549, pad (5712,13550) |
| `cdp4_bus_s4` | y 12009, pad (5841,12010) | track x 5842 south to a pad (5843,12335); poly south along x 5846 and diagonally south-west to a pad (5668,12681); track x 5669 south through the array row's pad | y 12984, pad (5670,12984) | y 13506, pad (5668,13508) |
| `cdp4_bus_s3` | y 12052, pad (5668,12053) | track x 5668 south, west along y 12622 to x 5627, south, west along y 12860 to x 5540, south to a pad (5537,13157); poly from the pad's top east, south along x 5563, west along y 13266, south along x 5497 into the channel-2 row at (5497,13462) | y 13397; at x 5389 it runs diagonally south-east into the channel-2 row at x 5454 (one poly) | y 13462 |
| `cdp4_bus_s2` | y 12096, to x 6412 | the row turns into a diagonal poly, 770 px south-west under about eighteen tracks, to a pad (5624,12898); track x 5626 south through the channel-2 row's pad to the array row's pad | y 13874, pad (5625,13874) | y 13418, pad (5625,13419) |
| `cdp4_bus_s1` | y 12138, pad (7510,12138) at its west end | track x 7511 south to a pad (7511,12745); poly row y 12745 west to x 5945, diagonal south-west, row y 12941 to a pad (5582,12941); track x 5584 south, west along y 13286 to x 5540, south through the channel-2 row's pad, a diagonal step (y 13900-13944) to x 5496, south, west along y 14353 | y 14351, pad (5407,14351) | y 13375, pad (5538,13375) |
| `cdp4_bus_s0` | y 12182, pad (7554,12183) at its west end | track x 7555 south to a pad (7554,12919); poly west and south along x 7513 (410 px) into the channel-2 row at (7513,13332) | none in the region: from the channel-2 row's pad a track x 5582 south, a diagonal step (y 13916-13959) to x 5539, west along y 14398 to x 5451, south across y 15000; it ends on a pad (5365,15042) of a poly row from the west (view `j6.png`; not drawn, `bl0`'s region) | y 13332, pad (5582,13333) |

What was checked beyond the overlays (`o4.png` .. `o8.png`):

- The T of s7 at (5800,11880): `follow.py` from (5800,12050) north runs through to the pad at y 11484
  and south to y 13612; from the north it turns east into the pad (5857,11878); view `j1.png` (2.4x,
  three shots).
- Tracks that run on through a pad (s5 at (5713,12443), s4 at (5670,12984), s2 at (5625,13419), s1 at
  (5538,13375)): `follow.py` stops at each ring from both sides; views `e3.png`, `j3.png`, `c2w.png`
  show the track at full width on both sides of each pad.
- s3's track corner (5627,12860) is 38 px north of s2's pad (5624,12898) and not on it:
  `tools/textmap.py 5596 12840 5660 12916 3`: the arm's metal ends at y 12861, then a dark edge, then
  bare ground (R 144-160 in both chips) at y 12873-12879, then the pad's ring.
- s3's pad joins the poly that leaves it: `tools/textmap.py 5520 13130 5590 13200 3 --acid`: poly colour
  in the chip-2 stripped shot runs unbroken from the pad along its top (y 13148-13151) into the column
  x 5550-5568 (view `j7.png` at 4x). The poly column's junction with the row at (5497,13462):
  `tools/px.py col 5497 13426 13480 3`, no edge line between them.
- s0's poly column x 7513 lies for 410 px under a metal of another net (a track x 7511 that runs from
  y 8902 to 14284, not followed further): `tools/tl5_tracks.py v 7511 12820 13345` finds no hole and no
  stretch without metal: no contact. The column ends at the row's south edge
  (`tools/px.py col 7513 13290 13372 3`).
- No track has a pad on any of the rows or diagonals it crosses: views `c1a.png`, `c1b.png` (channel
  1), `c2a.png`, `k2.png` (channel 2), `k3.png` (row y 12745), `k5.png`, `k6.png` (the diagonals at
  1.5x), `k1.png`, `w1_*.png` (the array rows); `tools/tl5_tracks.py v` down the five long tracks
  finds green holes only at the pads named above.
- A metal staircase at x 6790-7140 has each step's horizontal run lying on one of channel 2's rows
  for 70-90 px (view `k4.png`). `tools/tl5_tracks.py h` along each run finds no green hole; the one
  low reading (y 13375, x 6853-6886, red minus green 15-25) is a yellowish patch of the clean shot,
  and the chip-2 stripped shot shows poly colour there with no hole
  (`tools/textmap.py 6820 13355 6915 13397 3 --acid`). No contact (Ambiguity 4).

Piece `lc9` (track centres with `tools/sel_cut.py h Y` at twelve heights and `sel_cut.py v` in the
middle of each horizontal run; every line with `tools/follow.py --gap 16`; pad contacts with
`tools/busl_padc.py` in both metal shots; row centres with `tools/busl_rowy.py`; all metals 12-15 px
wide, drawn 14; all rows poly, 23-24 px between their edge lines):

| Line | Net | x from y 10400 | Step west at y | x | Step west at y | x | East along y | End |
|---|---|---|---|---|---|---|---|---|
| 1 | `rst_a` | 6082 | 11491 | 5908 | 12380 | 5844 | 14916 | pad, contact (6320,14914); poly row y 14914 east |
| 2 | `res_b` | 6126 | 11534 | 5953 | 12424 | 5888 | 14874 | turns south at x 6366; leaves the region at (6366,15000) |
| 3 | `lpstb_b` | 6169 | 11577 | 5996 | 12466 | 5932 | 14830 | turns south at x 6408; leaves the region at (6408,15000) (the follower runs on to y 15150) |
| 4 | `lc3_w9947` | 6212 | 11622 | 6040 | 12506 | 5975 | 14787 | pad (6406,14784); row y 14784 |
| 5 | `lc2_w8450` | 6256 | 11664 | 6083 | 12553 | 6018 | 14744 | pad (6365,14741); row y 14740 |
| 6 | `rst_c` | 6299 | 11708 | 6126 | 12596 | 6061 | 14700 | pad (6408,14696); row y 14697 |
| 7 | `lc3_e9756` | 6342 | 11752 | 6169 | 12640 | 6105 | 14656 | pad (6365,14655); row y 14654 |
| 8 | `lc2_w9079` | 6386 | 11794 | 6212 | 12683 | 6148 | 14613 | pad (6409,14612); row y 14611 |
| 9 | `lc3_e9798` | 6429 | 11838 | 6256 | 12726 | 6191 | 14570 | pad (6363,14568); row y 14567 |
| 10 | `rcs_e4` (`trace/tla.txt`, not this piece) | 6472 | 11880 | 6300 | 12772 | 6235 | 14528 | contact (6407,14526); row y 14523 to the pad (7012,14522) |

- Names are `lc3`'s at its south edge (`ports.d/lc3.txt`); line 4's `lc3_w9947` gathers the wire `lc2` called x6432.
  **Line 5 is firmly `lc2_w8907`'s metal** (`lc3`'s name for it; the gates of the ripple counter's clear
  transistors are on that piece); it is `lc2_w8450`, the output of the inverter of `lc1_w7170`, only
  through `lc2`'s uncertain box (`?P 5598,8899:5612,8914`, `?B 5604,8897:5614,8916`, with its
  `@alias lc2_w8450 lc2_w8907`): `tools/unsure.py` lists `lc2_w8450` as two pieces without the uncertain
  items, line 5 on the piece of `lc2_w8907` (Ambiguity 8).
- The staircases are plain right-angle steps over field, nothing underneath (views `l9_s2.png`,
  `l9_s3.png`, overlays `l9_o1.png`, `l9_o2.png` at 1.5x). Two of `ch1`'s diagonal polys cross the second
  staircase.
- No break: `tools/tl5_tracks.py v` down all thirty vertical segments (`cache/scratch/busl/l9_scan.txt`)
  finds no stretch of 18 px or more without metal in both chips, only the 8-17 px edge bars of the rows
  crossed. No pad along any line: every "wide" stretch `tools/follow.py` reports is at a corner. The
  follower loses line 4 at its second step (the diagonal poly of `cdp4_bus_s2` crosses the corner) and
  line 9 at its first corner; each was picked up again beyond ((5975,12560), (6256,11900)) and followed
  both ways.
- The tracks cross, without contact, `cdp3_hw_c#`'s poly rows (y 10361-10664), `cdp4_bus_s#`'s rows
  and diagonals (y 11878-12182, 12290-12480, 12745, 13332-13636) and the undrawn rows of the bands at
  y 12550-12900, 14050-14300 and 14450-14570. Where a track crosses a poly the clean shot is greenish
  for 6-13 px under it at many crossings (red minus green down to -5: (6126,12387), (6342,10577),
  (6169,10446), (6212,10449), `rcs_e4`'s (6472,10490)): tiles at 4x in four shots beside the contact
  (6409,14697) (`l9_c1.png`) show the track at its own width with the row's two edge bars and no ring
  in either metal shot at all five (guide, trap 15).
- The end pads (view `l9_o3.png`, 3.2x, metal and clean shots with the trace): each has the metal
  arriving from the west and one poly leaving east; no metal beyond the ring (`follow.py`: none for
  16 px), field north and south. Lines 2 and 3 cross line 1's row y 14914 on their way south:
  `tools/tl5_tracks.py v 6365 14890 15060` and `v 6408 14845 15060`: two edge bars each, no hole.
- The rows (views `l9_e1.png` at 1.05x, `l9_e2.png`, `l9_e3.png` at 1.5x, clean and metal shots): ten
  poly rows at y 14523, 14567, 14611, 14654, 14697, 14740, 14784, 14827, 14870, 14914, the same y
  within 1 px at x 6450, 6583, 6710, 6884, 6972, 7080, 7146, 7300, 7390 (no step). Seven are this
  piece's. Row 14523 is `rcs_e4`'s as far as the pad (7012,14522), and another net starts on it at the
  pad (7100,14522) (`bc1`'s R10); rows 14827 and 14870 begin at pads (6915,14828) and (6872,14868) of
  two tracks that come from the north (x 6927 and x 6885; no metal south of either pad:
  `tools/tl5_tracks.py v 6915 14850 15000`, `v 6872 14885 15000`; other nets, not drawn). `tools/tl5_tracks.py h Y 6432 7552`
  along each of the seven lists greenish stretches in the clean shot; the eight strongest ((6665,14567),
  40 px long, (6846,14914), (6621,14567), (6715,14697), (6886,14740), (6804,14784), (7533,14784),
  (6502,14784)) as tiles at 3.5x in four shots (`l9_c2.png`): in both metal shots every track crosses
  at its own width, no pad, no ring; the chip-2 stripped shot shows plain poly: colour of chip 1's
  stripped shot only (Ambiguity 5).
- East of x 7550 (seen, `l9_e3.png`; not drawn): the ten rows run on under four more metals to pads
  with contacts in two columns, row 14523 to (7835,14520), 14567 to (7790,14567), 14611 to (7835,14610),
  14654 to (7790,14654), 14697 to (7835,14697), 14740 to (7790,14740), 14784 to (7835,14784), 14827 to
  (7790,14827), 14870 to (7835,14870); row 14914 goes on to a pad with a contact (7880,14914), from which
  `bc1`'s track x 7969 runs south: drawn by `eof` (piece `isrc4`, 2026-11-19), which finds that **line 1 is
  `rst_a`** (its name here until the refresh of 2026-11-19 is under Former names in the glossary). These are the west ends of
  `bc1`'s thirteen bus metals (`notes/blocks/bc1.md`: y 14354 .. 14873, x 7780-8280).

Piece `ctl` (pad contacts with `tools/busl_padc.py` in both metal shots; row centres with
`tools/busl_rowy.py` in open columns; tracks with `tools/follow.py --gap 16` and `tools/sel_cut.py`;
metals 13-16 px wide, drawn 14; every row is poly, 23-24 px between its edge lines):

| Net | Row at x 7600 (y) | Pad at its west end | Track | Second pad, and its row east to x 7550 | Leaves |
|---|---|---|---|---|---|
| `rsel14_buf` | 12225 | (6732,12226) | arm west along y 12228 to x 6602; south; west along y 13073 to x 6538; south | (6537,13701): row y 13701 | south, (6538,15000) |
| `rsel15_buf` | 12485 | (6732,12485) | arm west along y 12488 to x 6646; south; west along y 13116 to x 6581; south | (6580,14004): row y 14004 | south, (6581,15000) |
| `rsel17_buf` | 12528 | (6687,12528) | x 6689 south; west along y 13160 to x 6624; south | (6623,13809): row y 13809 | south, (6624,15000) |
| `rsel16_buf` | 12788 | (6731,12788) | x 6733 south; west along y 13204 to x 6668; south | (6666,13961): row y 13961 | south, (6668,15000) |
| `cdp4_rst` | 12874 | (7467,12875) | x 7468 south to a pad (7467,13897) | from that pad a poly 20 px wide east along y 13916 to x 7532 | on the box (7535-7580, 13903-13940) |
| `cdp4_ld` | 12962 | (7556,12983), below the row's end | x 7556 south; over the box y 13899-13949 (`?M`); south to y 13982; west to x 7448; south | none | onto `bc1`'s metal of `bc1_ld_a` at (7448,14050) |

- The six row-end pads (views `n8_selpads.png`, `n9_rstld.png`, 3.2-3.4x, three shots): each a widened
  poly pad with a green hole in the clean shot and a ring with a bright centre in the metal shot; the
  metal leaves west (sel1, sel2) or south (sel3, sel4, rst, ld), the poly east. `cdp4_ld`'s pad hangs
  below the row's west end (the row enters its top right corner); 15 px north of it is the pad
  (7554,12919) of `cdp4_bus_s0`, whose track ends there: `tools/follow.py 7556 13050 N` ends at y 12980.
- A long track of another net (not drawn; Not done) comes down x 7468 from the north, turns east at
  y 12835 just above `cdp4_rst`'s pad and goes on south along x 7511. It is not on the pad:
  `tools/textmap.py 7444 12816 7500 12884 3`: the corner's metal ends at y 12842, then open ground in
  the clean shot for 12 px (y 12849-12858, both metal shots at ground level), then the pad's ring.
- Another net's metal corner at about (7430,13897) (a step of the staircase of `cdp4`'s row D data
  lines) lies 10-16 px west of `cdp4_rst`'s south pad: separated by ground (round-4 reviewer, 4x).
- The nested staircase (view `n10_stair.png`, 2.4x, metal and clean shots; overlay `ct_o1.png`): six
  tracks step west one after another, the two westernmost of other nets (x 6516 at y about 12995,
  x 6559 at 13033), then sel1, sel2, sel3, sel4; plain right-angle steps over field, nothing beneath.
  Each track was followed through its step by itself (`tools/follow.py`); `tools/sel_cut.py h` gives
  6603/6646/6689 at y 12700 and 6538/6580/6624/6668 at y 13300.
- **Every select track runs on through its second pad** (view `n7_pads.png`, 4x, both metal shots and
  the clean shot: a ring with a bright centre on a widened row-end pad, the track at full width above
  and below). `tools/follow.py` stops at each ring; `tools/tl5_tracks.py v X 13230 14100` shows the
  ring's two dark stretches (14-17 px) and metal on both sides; `tools/follow.py 6580 14062 S` and
  `6538 13780 S` run to y 16192 and 16150. Guide, trap 32.
- No other pad on a track: `tools/tl5_tracks.py v` down each select track from y 13230 to 15000, down
  x 7468 (y 12890-13885) and x 7556 (y 12995-13900): only the 8-13 px bars of the rows crossed (channel
  2's eight rows, the rows y 13701-14004, `bc1`'s six lines y 14089-14304, the rows y 14354-14914).
  The south boundary: view `ct_o5.png` (3.2x): four plain tracks across y 15000.
- The four rows east of their pads (views `n6_rows.png`, overlay `ct_o2.png`, 1.14x; `ct_stair.png`,
  3.1x): straight, the same y within 1 px at x 6690, 7080, 7210 and 7534, under about twenty tracks
  each, no pad on any. Two more rows of other nets lie between them (y 13744 and y 13852, both from
  west of x 6500; not drawn). A metal staircase (the six data lines of `cdp4`'s row D on their way to
  `bc1`'s lines y 14089-14304; not drawn) crosses the band, and **one of its steps lies on
  `rsel17_buf`'s row y 13809 for 80 px** (x 7267-7347; the other steps lie between rows or on row
  y 13852): no pad, no ring, the clean shot's row unbroken under it (tile 5 of `ct_c1.png`, 3.6x, four
  shots): no contact (Ambiguity 4).
- `tools/tl5_tracks.py h` along the ten row stretches lists greenish stretches in the clean shot
  (thirty-odd; the longest (6669,13701), (6712,13701), (7061,13809), (6712,14004)): tiles at 3.6x in
  four shots (`ct_c1.png`): they are the row's open stretches between two tracks, olive in the clean
  shot; every track crosses at its own width in both metal shots (Ambiguity 5).
- At x 7550 (view `n11_east.png`, 4x): the four rows run on under the track x 7556 to the gate group's
  diffusion column under the wide metal x 7598-7650, where each is a gate band: sel1's row steps 12 px
  north at x 7548 (band y 13677-13698), sel3's continues (13792-13812), sel4's and sel2's continue
  (`n5_ldsouth.png`). The wide metal has contacts onto the column at (7607,13718) and (7607,13838).
  Rows y 13744 and y 13852 end there too (y 13852 steps south to a band y 13862-13882).
- **`cdp4_rst`'s south end** (views `n3_rstld.png` 3.6x, `ct_o4.png` 3.3x): the pad (7467,13897) has a
  ring with a bright centre in both metal shots and a green hole in the clean shot
  (`tools/textmap.py 7438 13860 7500 13930 3`); the poly leaves its lower edge east as a band
  y 13906-13927, passes under the track x 7511 (the metal bright throughout, one edge bar each side:
  no contact) and ends on the west outline of the box at x about 7532.
- **The box (7535-7580, 13903-13940) and `cdp4_ld`'s track over it** (`tools/textmap.py 7526 13890
  7590 13955 3`, against the known through pad (5713,12443) and `cdp4_rst`'s pad in the same form;
  `tools/tl5_tracks.py v 7556 13860 13990`): neither metal shot shows metal for 51 px (y 13898-13949);
  no bright centre in either (chip 2 reaches ground level at one spot west of the track's line, chip 1
  at one spot on it, (7557,13929): Ambiguity 9); the clean shot shows a heavy outline with a plain tan inside and no green hole, in
  protected colours (so metal was over it). The track is at full brightness to y 13897 and again from
  y 13949, where it runs on to the corner (7556,13982) (`tools/follow.py 7556 13960 S`: west to
  x 7442; `7452 14040 N`: the same piece from the other end). The arm y 13975-13989 lies over field
  between the rows y 13961 and y 14004; the track x 7448 crosses row y 14004 without a pad
  (`ct_o4.png`). `bc1` draws the same metal from (7448,14050) south (`trace/bc1.txt` line 214).

Piece `d6` (pad contacts with `tools/busl_padc.py` in both metal shots; row centres with
`tools/busl_rowy.py 7578 8880 9145` in the open column east of the last track; arm heights with
`tools/sel_cut.py v` between the tracks; track centres with `tools/sel_cut.py h` at fifteen heights;
metals 13-17 px wide, drawn 14; every row is poly, 22-25 px between its edge lines):

| Line | Net | Row at x 7600 (y) | Pad at its west end | Track from the pad | Step west at y | Long run x | Lower step west at y | Lower x, onto `bc1`'s metal at y 14040-14050 | `bc1`'s line and contact |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `cdp3_g_c2` | 9123 | (7336,9122) | 7338 | 9190 | 7252 | 13722 | 7189 | line 1, y 14089, (7188,14091): the foot of `cdp3_g_c2` |
| 2 | `cdp3_g_c3` | 9080 | (7380,9080) | 7382 | 9234 | 7296 | 13766 | 7231 | line 2, y 14132, (7230,14131): the foot of `cdp3_g_c3` |
| 3 | `cdp3_g_c4` | 9036 | (7423,9036) | 7426 | 9276 | 7339 | 13810 | 7274 | line 3, y 14175, (7274,14172): `cdp3_g_c4` |
| 4 | `cdp3_g_c5` | 8993 | (7467,8994) | 7468 | 9320 | 7382 | 13855 | 7317 | line 4, y 14218, (7317,14217): `cdp3_g_c5` |
| 5 | `cdp3_g_c6` | 8949 | (7510,8950) | 7512 | 9363 | 7426 | 13898 | 7360 | line 5, y 14261, (7361,14260): `cdp3_g_c6` |
| 6 | `cdp3_g_c7` | 8906 | (7553,8905) | 7556 | 9407 | 7468 to y 12835; east to 7512; south | 13938 | 7404 | line 6, y 14304, (7405,14304): `cdp3_g_c7` |

- The north end (view `d6_north_m.png`, 2.3x, chip-2 metal shot with every package's trace; overlay
  `d6_o1.png`, 1.65x, metal and clean shots): six pads in a staircase, 43 px apart both ways, each a
  ring with a bright centre on the widened west end of its row; one metal leaves each pad south; the
  rows run east under the tracks of the lines north of them (plain crossings: `tools/tl5_tracks.py v`
  down the six upper tracks shows only 8-13 px edge bars) to x 7600, where `trace/cdp3.txt` draws them
  on (lines 215-235; its y within 1 px of these). The six upper arms are plain right-angle steps over
  field. North-west of the pads lies the diagonal bundle (not this piece).
- The long runs: `tools/sel_cut.py h` gives 7252, 7296, 7339, 7382, 7426, 7468 at y 9450, 9800, 10400,
  11000, 11600, 12700 (no step). `tools/tl5_tracks.py v` down all nineteen vertical segments
  (`cache/scratch/busl/d6_scan.txt`): no stretch of 18 px or more without metal in both chips; only
  the 8-16 px edge bars of the rows crossed (`lc3`'s
  rows y 9561-9814, two rows y 10041-10072, the top band y 10300-10680, channel 1, the rows
  y 12210-12241, 12469-12543 and 12728-12804, channel 2, the rows y 13685-13870). `tools/tl5_tracks.py
  h` along all thirteen arms: no gap, no hole.
- No pad or contact on the way. `tools/follow.py`'s contact candidates and the scan's greenish
  stretches of the clean shot, as tiles at 3.4x in three or four shots (`d6_c1.png`, `d6_c3.png`):
  (7382,11275), (7252,12579), (7253,10992), (7295,10986), (7338,9382), (7427,11596) are spots at the
  edge of a plain track over field (nothing beneath to tap); (7296,10057), (7382,9666), (7426,9667),
  (7468,9709), (7467,9699), (7512,13600) are plain crossings of a poly row, the track at its own
  width, no ring. The six tracks cross `cdp4_bus_s1`'s poly row y 12745 without a pad (`d6_c2.png`,
  4x, both metal shots and the clean shot).
- Line 6's corner at y 12835 (x 7468 to 7512) ends 16 px above `cdp4_rst`'s north pad, with open
  ground between (piece `ctl`'s text map); from there the track lies over `cdp4_bus_s0`'s poly column
  (y 12920-13332) and crosses `cdp4_rst`'s poly (y 13906-13927), without a contact on either
  (`tools/tl5_tracks.py v 7512 12845 13930`: edge bars only).
- The lower staircase (view `d6_stair_m.png`, 3.6x, chip-2 metal shot; overlay `d6_o2.png`, 1.85x,
  metal and clean shots): six right-angle steps, each arm 65 px long; no track goes on south of its
  arm and no lower track north of it. A seventh track west of them (x 7210, stepping along y 13678 to
  x 7142; another net, not drawn) has the same shape. Line 3's arm lies on `rsel17_buf`'s row y 13809
  and line 4's on the undrawn row y 13852, each for 80 px (Ambiguity 4). Line 5's corner (7426,13898)
  is 20 px west of `cdp4_rst`'s south pad: `tools/px.py row 13898 7424 7470 3 metal,metal1,acid1b`:
  metal to x 7431, a dark edge, bare ground at x 7442-7449 (red 124-156 in both chips, the clean shot
  green 120/159/82), the pad's ring from x 7451.
- Chip 2 alone shows dark notches on the metal at (7366,13853), (7512,13066-13076) and
  (7512,13270-13282) (round-5 reviewer; `tools/px.py pt 7366,13853 7512,13071 7512,13276 7512,13150
  all`: chip-2 metal 116/76/22, 43/22/16, 72/40/29 against 164/115/62 on the plain track; chip-1 metal
  157/115/31, 211/148/97, 184/140/82; the clean shot protected, 216-218/160-166/112-121, no hole):
  marks on chip 2's metal, not contacts. In the clean shot the row-end pads of lines 1 and 2 are
  stained red (142/40/28, 139/40/27 at the contact) and show no green hole; their contacts rest on the
  ring and bright centre in both metal shots (`tools/busl_padc.py`: red 225/179 and 220/212) and, for
  pad 1, the hole in the chip-2 stripped shot.
- The south ends (view `d6_o3.png`, 3x, chip-2 metal shot with every package's trace): each track
  ends on the pad of its own line of `bc1`'s, in a staircase; `tools/tl5_tracks.py v` from each pad on
  south: no metal in either chip for 60 px or more beyond any of the six. Line 1's track is dark for
  20 px (y 14067-14087) just north of its contact, the others for 15-19 px: the pad's ring with the
  row's north edge. Another metal turns south at about (7187,14165), 70 px below line 1's pad
  (`tools/textmap.py 7160 14080 7216 14180 4`: no metal between them in either chip): not joined.

Piece `sr` (the line with `tools/follow.py --gap 16`, in stages (`--max 60` .. `900`) through the
diagonal; track centres with `tools/sel_cut.py h` at twenty heights and arm heights with `sel_cut.py v`;
one metal 13-18 px wide, drawn 14):

| Stretch | From | To | What it passes |
|---|---|---|---|
| `eofw`'s metal | the corner pad (7446,8732) | (7466,8800) | drawn in `trace/eofw.txt` (`M 7466,8745 y8800`) |
| south, x 7467 | y 8795 | y 8910 | the poly y 8850-8875 that leaves the pad (7425,8862) east (edge bars y 8846-8855, 8870-8878) |
| diagonal, x + y = 16377 | (7467,8910) | (7209,9168) | field; 57 px north-west of piece `d6`'s row-end pads |
| south, x 7209 | y 9168 | y 13680 | `lc3`'s rows y 9561-9814, the rows y 10041-10072, the top band, channel 1, the bands y 12210-12241, 12469-12543, 12728-12804, channel 2 |
| west, y 13680 | x 7209 | x 7145 | field (between channel 2's last row and row y 13701) |
| south, x 7145 | y 13680 | y 14176 | rows y 13701 (`rsel14_buf`), 13744, 13809 (`rsel17_buf`), 13852, 13961, 14004, `bc1`'s lines 1 and 2 (y 14089, 14132) |
| east, y 14176 | x 7145 | x 7187 | lies on `bc1`'s line 3 (the poly row y 14175, `cdp3_g_c4`) for 45 px |
| south, x 7187 | y 14176 | y 14285 | `bc1`'s lines 4 and 5 (y 14218, 14261) |
| east, y 14285 | x 7187 | x 7231 | between line 5 and line 6 (y 14304) |
| south, x 7231 | y 14285 | y 14588 | line 6 and the rows y 14354-14567 |
| west, y 14588 | x 7231 | x 7187 | between the rows y 14567 and 14611 |
| south, x 7187 | y 14588 | y 15000 | the rows y 14611-14914 (piece `lc9`'s) |

- The north end (view `sr_n1.png`, 2.5x, chip-2 metal shot with every package's trace; overlay
  `sr_o1.png`, 1.9x): the metal comes south from `eofw`'s corner pad at its own width, crosses the poly
  that runs east from another line's pad (7425,8862) (two edge bars, the metal bright between them; no
  ring) and turns into the diagonal at y 8910. Three more diagonals lie north-west of it (other nets;
  one ends on that pad). The diagonal is plain, over field, and turns south at (7209,9168), 45 px west
  of `d6`'s line 1 (x 7252).
- The long run: `tools/sel_cut.py h` gives 7208-7210 at y 9250, 9450, 9800, 10400, 11000, 11600, 12200,
  12700, 13300, 13600 (no step). `tools/tl5_tracks.py v` and `h` on all ten straight segments
  (`cache/scratch/busl/sr_scan.txt`): edge bars of 8-13 px at every row crossed, and four longer
  stretches, each looked at as a tile at 4x in both metal shots and the clean shot (`sr_c1.png`,
  `sr_c2.png`): (7209,9176-9243), chip 1 only, a dirt blob on chip 1's metal (chip 2 plain);
  (7231,14373-14394), chip 1 only, dirt rings wider than the track (chip 2 plain); (7187,14678-14694),
  17 px, the north edge of row y 14697 with a red spot on chip 1; and **(7145,13728-13749), 22 px
  without metal in both chips, on the poly row y 13744: Ambiguity 13**.
- The follower's contact candidates: (7207,9579), where the track crosses `lc3_e9577`'s poly row (the
  clean shot olive under the track for 7 px, gap rings at x 7232; the metal at its own width in both
  metal shots, no ring: guide, trap 15); (7208,12618), a green spot at the track's west edge over field
  (nothing beneath).
- The seventh step and the three jogs (views `sr_s1.png`, `sr_s2.png`, 2.9x, both metal shots and the
  clean shot; overlay `sr_o2.png`, 1.4x): right-angle corners, the metal continuous round each in both
  chips. `tools/follow.py 7188 14215 N` and `S` and `7186 14630 N` and `S` each run to the next corner
  both ways. The arm y 14176 lies on `bc1`'s line 3 between x 7145 and 7187: no pad, no ring, the clean
  shot's row plain under it (`tools/tl5_tracks.py h 14176 7150 7182`: no gap, no hole): no contact
  (Ambiguity 4). `d6`'s line 1 ends on its pad (7188,14091) 70 px north of the corner (7187,14176):
  bare ground between (piece `d6`'s text map). Another net's track at x 7143 (from an arm y 14390 to a
  pad (7143,14480)) begins 200 px south of the corner (7145,14176): rows only between them.
- South of y 15000 (view `sr_s3.png`, 1.03x, metal and clean shots; not drawn): the track runs on at
  x 7186 over `tla`'s poly (y 15334-15444) to a corner (7186,15482), west to x 7103 and south between
  the pads and gates of `bc1`'s group; `tools/follow.py 7186 14630 S` ends at (7100,16279) with contact
  candidates at (7100,15596-15660). None of it has been read.

Piece `kb` (pad contacts with `tools/busl_padc.py` in both metal shots; the row with
`tools/busl_rowy.py 7585 9410 9480`; the track with `tools/follow.py --gap 16` both ways and
`tools/sel_cut.py h` at six heights (7554-7556); metal 13 px wide, drawn 14):

| Net | Row at x 7600 (y) | Pad at its west end | Track | South end |
|---|---|---|---|---|
| `bus_eq_r15` | 9449 (poly, 24 px between its edge lines) | (7554,9450) | x 7555 south, 1,670 px | contact (7555,11118) on a diffusion pad (7538-7584, 11096-11144); a diffusion band y 11095-11127 east to x 7600 and on under the VSS rail |

- The north pad (view `b_ends.png`, tile 1, 3x, both metal shots and the clean shot): a ring with a
  bright centre on the widened west end of the row; field west of it; no metal north of it
  (`tools/follow.py 7555 9600 N` ends at y 9446; the upper arm of `d6`'s line 6 passes 25 px north, with
  open ground between: piece `d6`'s review). `trace/cdp3.txt` draws the row from x 7600 at y 9450.
- The track: `tools/tl5_tracks.py v 7555 9470 11095`: only the 8-12 px edge bars of the rows crossed
  (`lc3`'s rows y 9561-9814, y 10041-10072, the top band y 10298-10680); one stretch where chip 2 alone
  fails (y 10897-10916) and one greenish in the clean shot (y 10877): tiles at 4x (`b_c1.png`): dark
  specks on chip 2's metal over plain field, chip 1 plain; and the follower's candidate (7554,10070), a
  plain crossing of the poly row y 10056.
- The south end (views `b_s1.png` 3.2x, `kb_o1.png` 4x, chip-2 metal shot and clean shot): the track
  ends on a pad with a ring and a bright centre in both metal shots and a black pit in the clean shot
  at (7555,11113); no metal south of it (`tools/follow.py 7555 9600 S` ends at y 11126). The pad is
  plain tan inside a heavy outline in the clean shot (`tools/px.py row 11112 7520 7605 5`:
  193-197/164-176/115-126 under the pad's metal, red minus green 20-29, against 215/160/113 for poly
  under a track): **diffusion**, not poly. East of the pad a band between two edge lines (y 11095 and
  11128; `tools/busl_rowy.py 7590 11090 11170`) runs to the VSS rail and is the same tan under the
  rail's edge (194/176/122 at x 7595-7605). Nothing else leaves the pad: field west and south; the
  olive strip with dark outlines that runs north from the pad's north-east corner at x 7575-7592 (run 5
  noted it as "a thin line from the north") is in the clean shot only, all the way up the 38 px gap
  between the track and the rail (`tools/px.py row Y 7562 7602 4` at y 9900, 10950, 11060: both metal
  shots plain ground, 154-169/124-151/80-88 in chip 2, with no edge line between the track's and the
  rail's; the chip-2 stripped shot field, red minus green about 0; tiles `b_c1.png`): the gap's mark,
  not layout (guide, trap 2). The dark bar across the band at x 7585 in the clean shot is not
  in either chip-2 shot (metal 160-168, stripped 121-153 at x 7580-7585): the mark of the gap between
  the pad's metal and the rail (guide, trap 2). Ambiguity 14.

Piece `n2`, `x68`, `x69` (each line with `tools/follow.py --gap 16`, piece `n2` in stages `--max 300` ..
`4700`; track centres with `tools/sel_cut.py h Y` at seven heights north of the step and five south;
arm heights with `sel_cut.py v`; the two-chip metal test `tools/tl5_tracks.py v/h` on all nine
segments, kept in `cache/scratch/busl/n2_scan.txt`; views `n2_step.png` (3.4x metal), overlays
`n2_o1.png` (the step), `n2_o2.png`, `n2_o3.png` (both edges, 4x, every package's trace)):

| Piece | Net | South edge | South run x | Arm y | North run x | North edge |
|---|---|---|---|---|---|---|
| `n2` | `bd1_n2` | (6711,15000), onto `eof`'s `M 6711,15000 ..` (piece `n2w`) | 6711 | 13247 | 6776 | (6776,10400), onto `eof`'s `M .. 6775,10400` (piece `n2n`) |
| `x68` | `busl_x6820` | (6754,15000), on south | 6754 | 13290 | 6820 | (6820,10400), on north |
| `x69` | `busl_x6906` | (6841,15000), on south | 6841 | 13376 | 6906 | (6906,10400), on north |

All three are 14-16 px wide throughout (`sel_cut.py`). The nest, from the west: `rsel17_buf`'s L (arm
y 13160), `rsel16_buf`'s (13208), `n2`'s, `x68`'s, `trunks`' line (x 6862 north, arm y 13332, x 6798
south), `x69`'s. What the scan flagged, all looked at (tiles `n2_c2.png`, `n2_c3.png`, `n2_c4.png` at
3.2x in four shots):

- No stretch of 18 px or more without metal in both chips on any segment: the longest is 16 px
  ((6906,12034-12050)), the rest are the 8-13 px edge bars of the poly rows crossed (about 100 on
  each line).
- Stretches of 20-38 px where one chip alone fails the metal test, fourteen places: `n2` (6776,10553),
  (6776,11956), (6776,12101), (6776,12528), (6711,14256); `x68` (6754,13330), (6754,13461),
  (6754,13801), (6754,13960), (6754,14184), (6754,14560), (6754,14590), (6820,10469), (6820,12224),
  (6820,12655), (6820,12766); `x69` (6906,10619), (6906,11900), (6841,14566), (6841,14212). In each
  the other chip shows the metal bright and of the same width, with no ring; (6820,12655) is a speck
  on chip 2.
- The clean shot is greenish (red minus green under 24, down to -30) under a track at some row
  crossings: on x 6711 at y 13548, 13590, 13633, 13699, 14004, 14178, 14220, 14437, 14698; on x 6754 at
  y 13547, 14264; on x 6841 at y 13417, 13588, 14089, 14910. **The colour goes by crossing, not by row**
  (the reviewer's correction of this run's first wording, "greenish under every track"; `tools/px.py pt`
  in the clean shot: row y 13417 is 221/166/113 under x 6668 and 222/167/120 under x 6711, salmon, and
  126/158/99 under x 6841; row y 14089 is 183/111/74 under x 6711 and 142/161/102 under x 6841). None is
  read as a contact, on these grounds: neither metal shot shows a ring, a pad or a widening at any of
  them (the track is bright and 12-15 px wide across each; `tools/textmap.py 6690 13524 6780 13572 3
  --acid`, `6822 13400 6862 13434`, `6822 14074 6862 14104`; tiles and the reviewer's `green_rows.png`,
  `green_13417.png` at 4.5-5.8x); the green patch is the whole protected width (about 25 px) by the
  row's height, wider than the metal, where a contact's hole is about 12 px inside a pad; and `n2` is
  greenish over both `rsel14_buf`'s row (y 13701) and `rsel15_buf`'s (y 14004), where contacts would
  short the two selects (guide, trap 15). View `n2_c5.png`.
- `x69`'s arm lies on the poly row y 13375 (piece `ch1`: `cdp4_bus_s1`) from x 6841 to x 6906
  (`textmap.py 6824 13354 6924 13400 3 --acid`; view `n2_c6.png`, 5x, three shots): the metal is a
  plain bar 14 px tall in both chips with no ring and no pad (a notch at x 6882 in chip 2 only), and
  the clean shot under it has no hole (olive-yellow from x 6835 to 6890, red-orange under the
  corner). Two nets (guide, trap 13). `trunks`' arm lies the same way on the row y 13332.
- The four corners nearest to pads: `rsel14_buf`'s and `rsel15_buf`'s pads at x 6736 (y 12225, 12485)
  are 40 px west of `n2`'s north run; the metal test at both heights shows the gap
  (`sel_cut.py h 12300`: 6776 w15, no run between 6740 and 6769).

### Pieces `r12`, `r13` (run 8): the read selects of R12 and R13

Method as for `n2`: `tools/follow.py --gap 16` from both ends and from the middle of each run;
centres by `tools/sel_cut.py h` at fifteen heights and `v` on the four arms; the two-chip metal test
and the clean shot's hole test on all ten segments (`tools/tl5_tracks.py v/h`, kept in
`cache/scratch/busl/r8_scan.txt`); pads by `tools/busl_padc.py`; rows on views of both stripped shots.

| | lower run | arm 1 | middle run | arm 2 | upper run | tap (contact) | row |
|---|---|---|---|---|---|---|---|
| `r12` `rsel12_buf` | x 6452, y 15000-12984 | y 12984 | x 6516 | y 12097 | x 6690 to y 10400 | (6452,13854); chip 2 (6453,13855), chip 1 (6451,13853) | y 13852, 20 px, from the pad to x 7550; step south at x 7528-7550 to y 13873 |
| `r13` `rsel13_buf` | x 6494, y 15000-13028 | y 13028 | x 6560 | y 12141 | x 6733 to y 10400 | (6495,13744) in both chips | y 13744, 20 px, from the pad to `cdp4`'s block (7550-7578, 13732-13770) |

- **The two taps are contacts** (views `r8_taps_a.png`, `r8_taps_b.png`, 5x, four shots): each has the
  metal widened to a round pad with a dark ring and a bright centre in both metal shots, a poly pad
  about 45 x 34 px with a hole in the clean shot (`tl5_tracks`: red minus green down to 8 at
  (6452,13854), (6494,13750)) and a pitted box in the chip-2 stripped shot. The follower stops on
  `r12`'s pad from both sides (trap 32: the metal goes on through it; the two-chip test shows the two
  halves of the ring, y 13831-13849 and 13858-13873, and metal beyond) and runs through `r13`'s. Each
  pad's poly leaves east only: pink field west, north and south of both pads in the clean shot.
- **The rows are poly** (trap 39; `tools/px.py pt` in open gaps between tracks: chip-2 metal blue
  42-65, chip-1 green 71-113, at (6516,13744), (6730,13744), (7100,13744), (6473,13852), (6516,13852),
  (7100,13852), (7538,13852)) and continuous from pad to end in both stripped shots (views
  `r8_rows_w.png`, `r8_rows_e.png`, 2.1x, all traces outlined): no pad, no widening, no second end.
  The dark dots on them in the clean shot are at the gaps between tracks (trap 2).
- **Row y 13852's east end is a Z** (views `r8_east_a.png` 5x, `r8_step.png` 8x): the row (y 13842-
  13862) ends at x 7550 and the poly goes on south from x 7528-7550 into the row y 13862-13884 that
  `cdp4` draws from x 7545 east. In the open column x 7538 the chip-2 metal shot is poly colour
  without a break from y 13845 to 13881 (`tools/px.py col 7538 13836 13890 3`: 143-157/125-138/51-58,
  the dark edges at y 13839-13842 and 13884-13887). Row y 13744 meets `cdp4`'s block without a step.
- **Two arms**: y 12097 lies for 170 px on `cdp4_bus_s2`'s poly row (piece `ch1`, y 12095); no pad,
  no ring, no dark stretch in either chip and no hole in the clean shot along it (`tl5_tracks.py h
  12097 6530 6675`; views `r8_arms_m.png`, `r8_arms_c.png`, 4.6x; one dark dot at (6625,12086) on the
  row's north edge in the clean shot only): two nets (traps 13, 15). The arm y 12141 lies over field
  (pink in the clean shot); `cdp4_bus_s1`'s row ends at its pad (7510,12137), far east of it.
- **Metal test**: one stretch of 14 px or more without metal in both chips that is not a pad's ring:
  (6452,13372-13389), 18 px (Ambiguity 15); then (6494,13618-13633) 16 px and (6690,10622-10635)
  14 px. Stretches of 20 px or more where one chip alone fails: (6452,14140-14169), (6452,14289-14322),
  (6494,13614-13633), (6494,14550-14582), (6690,11861-11881), (6732,11078-11098), (6732,12035-12054),
  and (6652-6674,12097) on the arm. Clean-shot hole candidates besides the taps: (6494,14786) (the row
  y 14784 is dark red-brown there under every track). All looked at in four shots (tiles `r8_c1.png`,
  `r8_c2.png`, 3.6x): in each the other chip shows the metal bright and of the same width, no ring,
  no pad. The follower's candidates (6494,14914), (6497,14774) are the crossings of `rst_a`'s and
  `lc3_w9947`'s rows: plain.
- Overlays: `r8_o1.png` (taps, 4.3x, metal and clean), `r8_o2.png` (lower corners), `r8_o3.png`
  (arms), `r8_o4.png` (east ends, all traces).

### Pieces `e6`, `p2` (run 9): what arrives from `lc3` west of piece `lc9`

Method as for `lc9`: `tools/follow.py --gap 16` on each line (it loses the two western diagonals
where they cross the two polys, and is restarted from the tracks); centres by `tools/sel_cut.py h`
at six heights on the tracks and `v` at three cuts on the arms; diagonals from `lc3`'s end points
(each 45 degrees, checked by overlay `r9_o1.png`); the two-chip metal test and the clean shot's hole
test on all nineteen straight segments (`tools/tl5_tracks.py`, kept in `cache/scratch/busl/r9_scan.txt`);
pads by `tools/busl_padc.py`; rows by `tools/busl_rowy.py` in open columns; polys on views of both
stripped shots.

| Line | at y 10400 | turns south at | vertical x | arm y | track x | follower's end south of the region |
|---|---|---|---|---|---|---|
| `lc3_e9577` | 5915 | y 10624 | 5691 | 10928 | 5322 | (5326,15381) |
| `lc3_e9621` | 5851 | 10603 | 5648 | 10884 | 5279 | (5284,15859) |
| `lc3_e9665` | 5785 | 10581 | 5604 | 10840 | 5235 | (5239,16506) |
| `lc3_e9708` | 5722 | 10560 | 5562 | 10796 | 5192 | (5194,16981) |
| `lc3_e9750` | 5655 | 10537 | 5518 | 10752 | 5148 | (5151,17462) |
| `lc3_e9793` | 5588 | 10514 | 5474, to the pad (5473,10707) | poly row y 10750, from the pad to the pad (5102,10750) | 5105 | (5107,17938) |

- **The sixth line's hop** (views `r9_knot_c.png`, `r9_knot_m.png` 4.6x; `r9_row10750.png` 2.9x, four
  shots; overlay `r9_o2.png`): the pad (5473,10707) has a ring and a bright centre in both metal shots
  and a hole in the clean shot's poly pad; field (pink) lies north, east and west of the pad, so it is
  not on `rst_n`'s column above it or on `lc2_w8450`'s row; its poly leaves south into the row
  y 10750 (edges y 10740 and 10761), which is poly colour without a break in both stripped shots from
  x 5490 to the pad (5102,10750). The fifth line's arm lies on that row from x 5148 to x 5518: the
  dark line across the arm at x 5488 is the edge of the pad's poly underneath (trap 3), not a break
  (bright metal on both sides in both chips). **The pad (5102,10750) and the fifth line's corner are
  two metals** (trap 16): between the pad's ring (x 5112-5121) and the corner's west edge (x 5136)
  both metal shots show open poly (`tools/px.py row 10750 5088 5168 3`: chip 2 121-143/54-112/17-45,
  chip 1 151-167/75-100/42-48 at x 5124-5133; metal is 184-217/149-208/72-97 on the pad and
  192-226/135-174/59-103 on the corner).
- **Dim stretch on the fifth line's arm** at x 5158-5181, y 10752: chip 2 fails the metal test for
  20 px, chip 1 is bright there (176-207) but for a speck at x 5176-5182; the arm's two edge lines run
  through (`tools/textmap.py 5086 10728 5206 10782 3`).
- **Metal test on the tracks**: stretches of 14 px without metal in both chips at (5322,11906-11919),
  (5235,11491-11504), (5235,14898-14912), all row crossings; one chip alone for 20 px or more at
  (5322,13232-13262), (5322,12424-12456), (5192,14390-14409), (5192,13856-13888), (5192,14333-14366),
  (5148,13381-13414), (5148,14846-14871), (5106,13219-13242), (4909,11470-11490), (4822,13815-13868).
  The follower's contact candidates: (5320,12779), (5321,13699), (5321,13740), (5321,14137),
  (5321,14305), (5321,14579), (5278,12257), (5277,14287), (5235,13739), (5235,14076), (5235,14263),
  (5191,14883), (5148,14372), (5104,14178), (4909,11982). All looked at in three shots (tiles
  `r9_c1.png`, `r9_c2.png`, `r9_c3.png`, 2.9x): plain crossings or specks, no ring, no pad, no hole.
  The mark at (5225-5238,14265-14285) is a loop of debris on chip 1 (in its metal shot and its clean
  shot; chip 2's stripped shot has nothing there and its metal a smudge 10 px away; `r9_x14270.png`).
- **The clean shot is greenish under every one of these eight tracks on every one of the eight
  diffusion rows** of piece `h8` (y 11343, 11819, 12296, 12773, 13252, 13731, 14207, 14899; red minus
  green 17 down to -19, 6-11 px long, the same on all tracks): the rows' own colour under a track,
  sixty-four crossings alike, with no ring or pad at any (trap 15).
- **`rst_n`'s poly** (views `r9_knot_c.png`, `r9_knot_a.png` 4.6x in both stripped shots; overlay
  `r9_o3.png`): column x 5464-5486 from y 10400 to a foot at y 10590-10608, the foot west to x 5397, a
  diagonal to (5333,10663), the row y 10663 (edges y 10652 and 10675: `tools/busl_rowy.py` at x 5040,
  5100, 5200, 5300; poly, chip-2 blue 56-63) west under the wide VCC branch to the pad (4907,10663)
  (view `r9_p2_w.png` 2.1x, three shots; pads `r9_wpads_a.png`, `r9_wpads_b.png` 3.8x, four shots:
  ring, bright centre, hole; the poly leaves east only). The sixth line's metal x 5474 lies on the
  column from y 10514 to 10608 with no pad, ring or hole (traps 13, 15).
- **`lc2_w8450`'s poly**: column x 5530-5552 from y 10400 to y 10650, the row y 10641 west to x 5457
  (under the metals x 5518 and x 5474), a diagonal to (5394,10706), the row y 10706 (edges y 10695
  and 10718) west to the pad (4822,10708). Under the metal x 5474 at (5476,10643) the chip-2 stripped
  shot has a dark spot about 10 px across; both metal shots are bright there between the row's two
  edge bars and the clean shot has no hole (`tools/textmap.py 5452 10620 5500 10662 3 --acid`): no
  contact. The two rings on the row in the clean shot at (5492,10640), (5540,10635) are in the gaps
  between the metals (trap 2; not in the chip-2 shot). The track x 4909 crosses the row y 10706 30 px
  below its own pad: bright metal with the two edge bars in both chips, the row not widened; the clean
  shot is greenish under the track there (14 px, red minus green -4), as on other crossings.
- **The track x 4909's south end** (view `r9_pad15088.png` 4.4x; overlay `r9_o5.png`): the pad
  (4909,15087), ring and bright centre in both chips, a hole in the clean shot's poly pad; bare ground
  below the pad in both metal shots (`tools/tl5_tracks.py v 4909 15030 15440`: no metal from y 15093 to
  15409, where `bl0_w15412`'s track begins on the same position: trap 33); field west and south of
  the pad; the poly leaves east. **The row y 15088** (view `r9_row15088.png` 1.5x, three shots, all
  traces): poly from the pad to `bl0`'s piece at x 5700, with no pad on it; open stretches read poly in
  both metal shots (at x 5511-5526: chip 2 145-163/93-124/51-57, chip 1 146-152/65-90/45; the same gap
  is dark in both stripped shots, residue between two metals, trap 2). A metal jog of another net
  (from x 5495 north to x 5410 south) lies on the row from x 5400 to x 5500: a plain bright bar in both
  chips, no ring, no pad, no hole in the clean shot (views `r9_x15088_a.png`, `r9_x15088_b.png` 3.9x,
  four shots; `tools/textmap.py 5484 15066 5544 15108 3 --acid`).
- Overlays: `r9_o1.png` (the staircase, 1.5x), `r9_o2.png` (the hop), `r9_o3.png` (the polys' corners),
  `r9_o4.png` (the west pads), `r9_o5.png` (the south pad).

### Pieces `fb`, `fa` (run 10): the foot rows y 14870, y 14827 and their tracks

Method as for `n2` and `r12`: `tools/follow.py --gap 16` from the foot, from the middle and from the
upper pads (`fa`: (6927,14700) N: corners (6927,13466) E, (6991,13460) N, end (7162,8838) after
5,940 px; `fb`: (6949,12500) N: end (7121,8794), S: corners (6947,13422) W, (6885,13421) S, end
(6885,14847); north of the upper pads: (7122,8590) N ends (7120,7210), (7164,8545) N ends (7164,7169));
centres by `tools/sel_cut.py h` at 21 heights and, in both chips, every 10 px of all six straight runs
(1,422 samples: none more than 4 px off its track in both chips, median width 15 px); the diagonals by
`sel_cut.py h` every 20 px from y 9080 to y 8780 (x + y constant: 15986 for `fb`, 16052 for `fa`; the
bright runs between the diagonals in such a cut are bare ground, chip 2, trap 30); arms by `sel_cut.py
v`; pads by `tools/busl_padc.py`; rows by `tools/busl_rowy.py` (poly: blue 50-60); the two-chip metal
test and the clean shot's hole test on every straight segment (`tools/tl5_tracks.py v/h`, kept in
`cache/scratch/busl/f10_scan.txt`).

| | foot row (poly) | foot pad (contact) | lower run | arm | upper run | diagonal | pad | poly column | pad | metal north | end pad | row west |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `fb` `busl_x6949` | y 14870, 24 px, x 6885-7550 | (6885,14871) | x 6885 | y 13421 | x 6949, y 13421-9037 | (6949,9037)-(7122,8864) | (7121,8797) | x 7112-7136, y 8797-8627 | (7121,8627) | x 7121, y 8627-7214 | (7120,7214) | y 7214, 23 px |
| `fa` `busl_x6992` | y 14827, 24 px, x 6927-7550 | (6927,14827) | x 6927 | y 13463 | x 6992, y 13463-9060 | (6992,9060)-(7165,8888) | (7163,8842) | x 7155-7177, y 8842-8581 | (7164,8581) | x 7164, y 8581-7170 | (7165,7170) | y 7171, 24 px |

- **The pads are contacts**: each of the eight has a dark ring and a bright centre in both metal shots
  on a poly pad (views `f10_foot.png` 2.65x three shots, `f10_ncol.png` 3.2x three shots, `f10_nend.png`
  2.5x three shots; the two end pads and `fb`'s two upper pads show a green or pale hole in the clean shot; the two foot
  pads and `fa`'s diagonal pad are red there without a hole (red minus green 56-80 across the pad),
  with the ring and bright centre in both metal shots and a greenish patch inside the pad in the
  chip-2 stripped shot (`tools/textmap.py 6866 14852 6908 14892 3 --acid`, `6908 14808 6950 14848 3
  --acid`; `fa`'s diagonal pad is a pitted box there, `f10_ncol.png`): trap 26's converse).
- **The poly columns** between the diagonal pads and the second pads lie under one metal of `eofw` (y 8662-8680, both columns) and one staircase metal that no package
  draws (y 8704-8722 west of x 7135, over column B; a leg south at x 7140-7152 between the columns;
  y 8748-8765 going east, over column A: `tools/sel_cut.py v 7100`, `v 7146`, `v 7180 8640 8790`;
  corrected after the review): cream under the metals and dark in the gaps in the clean shot, poly orange in the open stretches of the chip-2 metal shot
  (`tools/busl_rowy.py 8712 7095 7190 --horizontal`: 143/111/49); no ring in any crossing metal and no
  hole on either column (`tools/tl5_tracks.py v 7122 8640 8780`, `v 7166 8595 8820`: two dark stretches
  on column B at y 8737 and y 8775, both in the open gaps between the metals).
- **The arms lie on poly rows of piece `ch1`** for 64 px each: `fb`'s on `cdp4_bus_s2`'s row y 13418,
  `fa`'s on `cdp4_bus_s3`'s row y 13461. No contact (traps 13, 15): the metal is of constant width and
  full brightness along both arms in both chips, without ring or widening (`tools/textmap.py 6864 13400
  6966 13440 3 --acid`; view `f10_arm5.png`, four shots at 2.85x). In the clean shot the row under
  `fb`'s arm is vivid red-orange (red minus green 80-120) where the row under `fa`'s is cream: colour,
  not a hole (a hole is green).
- **Crossings looked at** (tiles `f10_c1.png` .. `f10_c4.png`, 4x, four shots: every stretch the scan
  flagged, 23 places; `f10_c5.png`, 3.2x, three shots: the six rows the northern runs cross, y 7438 ..
  8040): all plain, metal of constant width, no ring, no pad. The longest stretch without metal in
  both chips is 17 px, on `fb`'s track where it crosses `rsel12_buf`'s row y 13852 ((6885,13835-13851)):
  a dark speck on the east half of the metal in chip 2 only, chip 1 bright from y 13844 on, the clean
  shot protected cream with red minus green 48-64 across the whole crossing, against the ring, bright
  centre and hole of that row's real tap 430 px west (`tools/textmap.py 6860 13826 6912 13878 3 --acid`
  against `tools/textmap.py 6427 13832 6479 13872 3`). The others: 15 px at (6927,13555-13569) and
  14 px at (6992,10388-10401) (row edge bars); one-chip stretches of 20-38 px at fourteen places, the
  other chip bright at each; a ring-like spot on chip 1 at (6883,13458) (absent from chip 2 and from
  both stripped shots: dirt); a dark blotch in the clean shot on `rst_ck`'s tap row under `fa`'s
  northern run at (7155-7185, 7640-7655) (both metal shots plain: dirt on chip 1). The greenish rows
  under the tracks (y 13376, 13503, 14219, 14266, 14483, 14742, 9796, 10057) are green under every
  track that crosses them (trap 15).
- **The foot rows between their pads and x 7550** (view `f10_rows.png`, 1.8x, with the trace;
  `f10_e7400.png`, 2.7x, four shots; `tools/busl_rowy.py` at x 6970 .. 7536: centres 14827 and 14870
  throughout): straight, no pad, no step. Row y 14827 lies in the open at x 7355-7445 (no track
  crosses it there: `bc1_ld_a`'s metal jogs east along y 14803 above it): orange-brown poly in both
  metal shots, dark in the clean shot (`tools/tl5_tracks.py h 14827 6950 7550` lists that stretch as
  low red minus green: open poly, not holes). **Over row y 14870 from x 7378 to x 7513 lies
  a wide metal** (about y 14840-14905, its west edge at x 7378; the row's two edges print through it
  as dark lines), **with a limb x 7469-7513 that runs north from it and also crosses row y 14827**
  (`tools/sel_cut.py h 14848 7350 7570`: 7463-7514; `h 14800`, `h 14760`: 7468-7515; corrected after
  the review, which found the limb and the plate's east end: the first reading had the plate run past
  x 7550): it is drawn by no package and is not followed here (believed supply). No contact onto
  either row: the clean shot is protected cream along row y 14870 with no hole (`tools/tl5_tracks.py h
  14870 6905 7550`: none; `h 14827`: nothing at x 7469-7513); the dark blob at (7470,14875) is on chip
  2 only. Under the limb, between the two rows, the clean shot has a grey band (x 7484-7504): read as
  field by the reviewer (no edge line prints through the metal in either chip and the rows are no
  brighter over it; no control under another wide metal).
- **The rows' ends outside the piece.** East of x 7550 (view `f10_east.png`, 1.6x): row y 14827 runs on
  to a pad at about (7794,14826) and row y 14870 to a pad at about (7836,14872), each with a contact
  ring, under `bc1`'s bus metals (not drawn, `bc1`'s region; which way each pad's metal leaves was not
  read). West of the end pads (view `f10_wrow.png`, 1.6x; `tools/busl_rowy.py X 7140 7245`): the rows
  y 7171 and y 7214 are poly at x 7040 .. 6720 and pale bands under `eof`'s two staircase arms
  (y 7166-7180, y 7210-7225) from x 6650 west to at least x 6400: not read.
- Overlays: `f10_o1.png` (the foot pads, 3.1x), `f10_o2.png` (the arms), `f10_o3.png` (the diagonals and
  their pads, 2.2x), `f10_o4.png` (the columns and second pads), `f10_o5.png` (the end pads).

### Pieces `fc`, `fd`, `fe` (run 11): three more Ls of the nest, to `rcs_mv`, `tc2_r5718` and `cdp3`'s rail

Method as for `fb`, `fa`: `tools/follow.py --gap 16` from the foot, from the middle and from the upper
pads (the calls and their ends are in `cache/scratch/busl/survey.md`, "Run 11"); centres by
`tools/sel_cut.py h` at 4 to 11 heights of each run (none more than 2 px off its track); arms and jogs
by `sel_cut.py v`; the diagonals and the northern runs by a two-chip cut, `tools/busl_both.py h/v` (new
this run: the follower's metal test in both metal shots, so that ground bright in chip 2 only does not
count: trap 30), every 20-40 px from y 9140 to y 8810; pads by `tools/busl_padc.py`; rows and poly
columns by `tools/busl_rowy.py` in their open stretches (poly: blue 54-62); the two-chip metal test and
the clean shot's hole test on all 26 straight segments (`tools/tl5_tracks.py v/h`, kept in
`cache/scratch/busl/g11_scan.txt`).

| | north end | northern run | pad | poly column | pad | diagonal (x + y) | upper run | arm | lower run | foot |
|---|---|---|---|---|---|---|---|---|---|---|
| `fc` `rcs_mv` | `tl6`'s poly (6236,6350); column x 6237 (24 px between edge lines) to a pad (6232,6911) | metal y 6913, x 6232-7208; x 7208, y 6913-8625 | (7207,8625) | x 7211, y 8625-8798 | (7206,8798) | (7208,8908)-(7035,9081) (16116) | x 7036 | y 13507 | x 6971 | out at (6971,15000) |
| `fd` `tc2_r5718` | `tc2`'s metal (7533,6400) | x 7533 to y 7279; x 7511 to y 7453; west to x 7360; x 7360 to y 8667 | (7357,8667) | x 7342, y 8667-8798 | (7337,8798) | (7338,8844)-(7078,9104) (16182) | x 7078 | y 13550 | x 7014 to y 14308; x 7058 to y 14438; x 7100 | pad (7098,14525); row y 14524 east |
| `fe` `busl_x7122` | poly row y 8863 from under the rail (x 7592) | - | - | - | (7423,8863) | metal y 8862 to x 7385; (7385,8862)-(7122,9125) (16247) | x 7122 | y 13594 | x 7058 to y 14267; x 7100 to y 14396; x 7144 | pad (7143,14481); row y 14480 east |

- **The pads are contacts**: each of the eight has a dark ring and a bright centre in both metal shots
  on a poly pad, and all but the two foot pads a green hole in the clean shot (views `g2_m.png`,
  `g2_c.png`, 3x, all traces; `g3_w.png`, `g9_o8.png` for (6232,6911); `g1_m.png`, `g1_c.png`,
  `g9_o1.png` for the foot pads, where the clean shot shows a pale centre in a cream pad).
  `tools/busl_padc.py` centres agree within 3 px between the chips.
- **`rcs_mv`'s poly column** (x 6227-6247, y 6350-6900; views `g5_col.png`, 2.25x, three shots, and
  `g9_o3.png` with `tl6`'s trace): one poly from `tl6`'s corner to the pad. Cream under each of the ten
  metals it passes under (at y about 6373, 6415, 6457, 6500, 6542, 6586, 6628, 6673, 6804, 6846: `amrw`'s
  one, `slbus`'s five and four that no package draws), dark red-brown in the open stretch y 6690-6790
  (`tools/px.py col 6236 6690 6830 10 acid,acid1b`: chip 2 stripped 167-181/123-144/62-76, the poly
  orange; `tools/busl_rowy.py 6740 6210 6262 --horizontal`: centre 6237, poly), of one width throughout
  (`tools/tl5_tracks.py rows col 6340 6920 6 6236 6226 6246`: poly at every sample of the centre line
  but single samples in the gaps between the metals). No contact from any of the ten: no pad, no ring,
  and the only low red-minus-green stretches on the column (y 6647, 6692, 6823; 6-9 px) lie in the gaps
  between the metals, not under one (trap 2). Those metals' own pads are at x 6190.
- **The two poly columns under the staircase metals** (x 7211 and x 7342; `g2_c.png`, `g9_o2.png`):
  cream under the two horizontal metals (y about 8705 and y 8757), dark red-brown in the gaps, poly
  orange in the open in the chip-2 metal shot (`tools/busl_rowy.py 8680 7185 7232 --horizontal`,
  `8735 7320 7372 --horizontal`: 153-162/119-127/60-62). `fd`'s upper pad (7357,8667) stands east of
  its column's axis (the column is x 7331-7353, the pad x 7334-7380). No ring in either crossing metal
  over either column.
- **The corner (7360,7453) of `tc2_r5718` lies over the corner of another poly**: a poly column
  x 7352-7372 comes down from the north in the open (red-brown, y 7380-7444), runs under the metal's
  corner and, about 25 px south of it under the track, turns west as a row y 7468-7490, seen to at
  least x 7285 (`tools/tl5_tracks.py rows col 7380 8660 8 7362`; views `g9_c1.png`, 5x, four shots,
  and the reviewer's `review-11/h3_corner7360.png`; the first reading had it end there: corrected
  after the review). No contact: no ring, the metal not widened, the clean shot cream with no hole
  (trap 13). The poly is drawn by no package (the northern part).
- **The jog at y 7279** (22 px: x 7511 south of it, x 7533 north; `tools/busl_both.py h` at y 7300,
  7280, 7274; view `g4_step.png`, 4.2x, both metal shots; overlay `g9_o4.png`) and **the plain corner
  (7208,6913)** of `rcs_mv` (`g9_c2.png`, 4x, three shots: nothing goes on east or north).
- **The arms lie on poly rows of piece `ch1`** for 64 px each (`fc`'s on `cdp4_bus_s4`'s row y 13506,
  `fd`'s on `cdp4_bus_s5`'s row y 13549, `fe`'s on `cdp4_bus_s6`'s row y 13592), as `fb`'s and `fa`'s
  do on the two rows above. No contact (traps 13, 15): no stretch without metal and no hole along any
  of the three (`tools/tl5_tracks.py h 13507 6984 7024`, `h 13550 7026 7066`, `h 13594 7070 7110`: none
  of either), metal of constant width without ring (overlay `g9_o5.png`, 4x).
- **The foot jogs** (views `g1_m.png`, `g1_c.png`, 2.1x; overlay `g9_o1.png`, 2.6x): the three lines
  step east one track at a time like `tc2_sr_g`'s further east. `rcs_e4`'s pad (7012,14522) has no
  metal north of it (`tools/follow.py 7014 14480 N`: no metal), so `tc2_r5718`'s track x 7014 ends at
  its jog y 14308 and does not reach that pad. **Each of the four jogs lies on a poly row for its full
  44 px** (added after the review): `fe`'s jog y 14267 on `bc1`'s line 5 (`cdp3_g_c6`, row y 14264),
  `fd`'s jog y 14308 on `bc1`'s line 6 (`cdp3_g_c7`, row y 14307), `fe`'s jog y 14396 on the undrawn
  row y 14394 and `fd`'s jog y 14438 on the undrawn row y 14437 (`tools/busl_rowy.py 7166 14240
  14460`), as `tc2_sr_g`'s jog lies on line 3. No contact (traps 13, 15): no stretch without metal and
  no hole along any of the four (`tools/tl5_tracks.py h 14267 7070 7090`, `h 14308 7026 7046`,
  `h 14396 7112 7132`, `h 14438 7070 7090`: none of either), no ring, the metal of constant width
  (`g9_o1.png`; the reviewer's `review-11/b3_jog14308_c1.png`). **A fourth net is seen there and not drawn**: a poly
  row y 14480 from the west ends on a pad (7057,14480), whose metal runs south on x 7058 (follower:
  a jog east at y 14588, lost at (7105,14587)).
- **The two foot rows between their pads and x 7550** (view `g9_rows.png`, 2.9x, two shots;
  `tools/busl_rowy.py` at x 7166 .. 7580: centres 14480 and 14524 throughout, poly): straight, in the
  open but under `tc2_sr_g`'s track, `bc1_ld_a`'s and a wide metal x 7483-7535 that no package draws
  (the same supply piece as beside rows y 14827, 14870: Not done); no pad, no hole
  (`tools/tl5_tracks.py h 14480 7165 7550`: one 6 px stretch at x 7405, in the open; `h 14524`: none).
- **Crossings looked at.** The scan's longest stretches without metal in both chips: 18 + 14 px on
  `fe`'s track over the row y 13744 (Ambiguity 16); 19 px at (7036,9802-9820) and 16 px at
  (7036,9711-9726) (tile `g7_t3.png`, 4.5x, four shots: row edge bars and a dark speck on chip 1; the
  three tracks' pink protected strips are of constant width in the clean shot, no pad); 16 px at
  (6971,14378-14393), (7036,13463-13478), (7078,13444-13459), 15 px at (7122,11863-11877),
  (7122,13420-13434), 14 px at (7078,12727-12740) (row edge bars: each is at a row's edge pair).
  One-chip stretches of 20-36 px at 32 places, the other chip passing at each, and one of 65 px on
  `tc2_r5718`'s track at (7533,6911-6975) in chip 1 only: a dark blot on that photo over track and
  ground alike (`tools/px.py row 6940 7515 7551 4 metal,metal1`), chip 2 bright (196-221) and the
  clean shot's protected strip unbroken. Low red-minus-green
  stretches in the clean shot under the tracks: y 9624, 9667, 9754, 9795, 10058 and (7058,13810): the
  rows y 9754, 9795, 10058 are greenish under all three tracks and under run 10's (trap 15), and
  (7058,13810) is `rsel17_buf`'s row y 13809, greenish under `fd`'s track too (tile `g7_t1.png`, 4.6x,
  four shots: metal of constant width, no ring, no pad on either).
- Overlays: `g9_o1.png` (foot), `g9_o2.png` (north pads and columns, clean shot), `g9_o3.png`
  (`rcs_mv`'s column), `g9_o4.png` (`tc2_r5718`'s corner and jog), `g9_o5.png` (arms), `g9_o6.png`
  (diagonals, 2.9x), `g9_o7.png` (the join to `tc2`'s metal), `g9_o8.png` (the pad (6232,6911)).

### Pieces `ga`, `gb`, `gc` (run 12): lines 11-13 of the staircase bundle, to the rows y 14480, 14437, 14393

Survey: `cache/scratch/busl/survey.md`, "Run 12". The bundle's tracks at fifteen heights by
`tools/busl_both.py h` (the two-chip metal test): between `rcs_e4` (line 10) and `rsel12_buf` there
are four more lines at every height (x 6516, 6559, 6602, 6646 from y 10040 to the upper staircase;
x 6343, 6386, 6430, 6473 between the staircases; x 6278, 6322, 6365, 6408 below the lower one). **The
follower misreads the upper staircase**: `tools/follow.py 6559 10426 S --gap 16` runs along line 12's arm
past its corner and comes back north on line 11, and from (6603,10426) it reports line 13's corner at
x 6385, line 12's track. The arms lie on `ch1`'s poly rows there, bright rows between dark edge lines;
the nest was read on a view (`h8_stair1.png`, 3.2x; overlay `h14_o345.png`) and from cuts across each
arm (`tools/sel_cut.py v`, both chips for the first): four plain nested Ls. Centres by
`busl_both.py h` at 7 to 8 heights of each run (none more than 3 px off), arms by `sel_cut.py v`, the
diagonals by `busl_both.py h` every 30 px from y 8930 to y 8660, pads by `tools/busl_padc.py` (the
two chips agree within 3 px but for (6407,14437): 6406,14434 against 6409,14439), rows by
`tools/busl_rowy.py` in open columns, the two-chip metal test and the clean shot's hole test on all 35
straight segments and the rows (`tools/tl5_tracks.py v/h`, kept in `cache/scratch/busl/h12_scan.txt`).

| | north end | northern run | pad | poly column | pad | diagonal (x + y) | tracks and arms | foot |
|---|---|---|---|---|---|---|---|---|
| `ga` `lc1_w7780` | `lc1`'s row y 7780 from its port (6450,7780) to its end pad (6819,7780) | x 6819, y 7780-8282; y 8282 west to x 6773 | (6773,8323) | x 6775, y 8323-8625 | (6774,8625) | (6775,8692)-(6602,8865) (15467) | x 6602; arm y 9886; x 6516; arm y 11923; x 6343; arm y 12813; x 6278; east along y 14483 | pad (6364,14482); row y 14480 to a pad (7057,14480); metal x 7058, jog y 14588, x 7100 to a pad (7100,15175); poly south and east, row y 15218 |
| `gb` `busl_x6559` | end pad (6861,7257) on the row y 7258 (from the west) | x 6861, y 7257-8320; y 8320 west to x 6818; x 6818 to y 8408 | (6817,8408) | x 6818, y 8408-8668 | (6818,8668) | (6818,8716)-(6646,8888) (15534) | x 6646; arm y 9928; x 6559; arm y 11967; x 6386; arm y 12857; x 6322; east along y 14440 | pad (6407,14437); row y 14437 east |
| `gc` `busl_x6603` | end pad (6904,7301) on the row y 7300 (from the west) | x 6905, y 7301-8364; y 8364 west to the pad | (6861,8366) | x 6861, y 8366-8710 | (6861,8710) | (6861,8737)-(6689,8909) (15598) | x 6689; arm y 9970; x 6602; arm y 12010; x 6430; arm y 12899; x 6365 | pad (6365,14394); row y 14393 east |

- **The pads are contacts**: each of the thirteen has a dark ring and a bright centre in both metal
  shots on a poly pad. The three north end pads and the six pads of the poly columns have a green or
  pale hole in the clean shot (views `h7_n1213.png`, 3.1x; `h5_npads.png`, 3x; overlays `h14_o1.png`,
  2.7x, and `h14_o8.png`, 3.4x, both metal shots and the clean shot); the three foot pads and the pad
  (7057,14480) show a pale or greenish centre in a cream pad there (`h3_west.png`, `h14_o6.png` 3.3x,
  `h14_o7a.png` 3.6x), as the foot pads of pieces `lc9`, `fb` .. `fe` do; the south end pad
  (7100,15175) has ring and bright centre in both chips, a pale centre in both stripped shots
  (`h14_o7b.png`, 4x, four shots).
- **`lc1_w7780`'s row between `lc1`'s port and its end pad** (x 6450-6800; view `h13_row7780.png`, 2.4x,
  three shots, all traces): one poly, cream in the clean shot under each of the eight tracks it passes
  under (x 6472, 6514, 6558, 6602, 6645, 6688, 6731, 6775: `eof`'s, `tla`'s and undrawn ones), orange
  in the chip-2 stripped shot, with no pad or ring on it (`tools/tl5_tracks.py rows row 6450 6840 6
  7780 7760 7800`: poly at every sample but single ones in the gaps, field on both sides; `h 7780 6455
  6795`: three stretches of 6-7 px in the gaps between tracks, trap 2). **The row ends on the pad**: east
  of it is field for about 33 px (pink under the track x 6861's strip), and the poly that carries on
  along the same line from x 6870 east is `eof`'s row of `lc1_w7170`, which comes up from y 7821 there
  (trap 34: two polys in line, not one). The pad has no metal north of it; the track x 6861 (piece
  `gb`) passes 42 px east of its centre, 16 px of bare ground between the pad's ring and the track.
- **The three poly columns** (x 6775, y 8323-8625; x 6818, y 8408-8668; x 6861, y 8366-8710; `h5_npads.png`,
  `h14_o1.png`): cream under the staircase metals they pass under (three at y about 8454, 8497, 8540:
  `trunks`' line, `eofw`'s and a third; column 3 also one at y about 8625), dark red-brown in the gaps and in their open
  stretches, poly orange there in chip 2 (`tools/px.py col 6776 8340 8450 8 metal,acid,acid1b`: metal
  158-180/104-131/48-67, stripped red over green by 30-50 at every sample from y 8348 to y 8436, where
  the clean shot is dark; `tools/tl5_tracks.py rows col 8300 8730 6 6775 6818 6861`). No ring in any
  crossing metal and no hole on a column (`tools/tl5_tracks.py v 6775 8345 8605`, `v 6818 8430 8648`:
  none; `v 6861 8388 8690`: one stretch of 11 px, minimum 19, at y 8523, in a gap between two metals).
- **Each line steps one track east north of its column** (`h6_ntop.png`, 2.5x; `h14_o1.png`): line 11
  from its pad north 40 px, east along y 8282 and north on x 6819; line 12 north on x 6818 to y 8320,
  east and north on x 6861; line 13 east from its pad along y 8364 and north on x 6905 (line 14 the
  same way onto x 6948). `tools/follow.py 6818 8370 N` follows line 12 round its arm correctly;
  started at (6905,8370) it starts on line 14's pad and goes up line 13's track.
- **The upper arms lie on poly rows of piece `ch1`** for 173 px each: line 11's on `cdp4_bus_s6`'s row
  y 11922, line 12's on `cdp4_bus_s5`'s row y 11964, line 13's on `cdp4_bus_s4`'s row y 12008. No
  contact (traps 13, 15): no stretch without metal in both chips along any (`tools/tl5_tracks.py h
  11923 6350 6510`, `h 11967 6393 6553`, `h 12010 6436 6596`), metal of constant width without ring
  (`h8_stair1.png`, `h14_o345.png`); one greenish speck of 6 x 9 px in the clean shot at (6440,12009),
  inside line 13's corner, where both metal shots are bright (`tools/textmap.py 6408 11988 6472 12032
  3 --acid`). The north arms (y 9886-9970) and the lower arms (y 12813-12899) lie on bare ground.
- **The foot** (`h3_west.png`, 2.1x; overlay `h14_o6.png`): four nested Ls inside `rcs_e4`'s (its bottom
  run is y 14528): lines 11 and 12 turn east (y 14483, y 14440) onto pads at x 6364 and x 6407, lines
  13 and 14 end on pads straight below their tracks (y 14394, y 14350). West of each pad the ground
  under the metal is field (pink protected strip): the rows start at the pads.
- **The rows y 14480, 14437, 14393 between their pads and x 7550** (views `h10_rows_w.png`,
  `h10_rows_e.png`, 2x, three shots; `tools/busl_rowy.py` at x 6430, 6990, 7170: centres 14480, 14437,
  14393/14394 throughout, poly; `tools/tl5_tracks.py rows row 6340 7600 6 ...` with the gaps between the
  rows: field between them everywhere): straight poly rows under the field's tracks with no pad on
  any. Row y 14480's west part ends on the pad (7057,14480); between it and `busl_x7122`'s pad
  (7143,14481) the row line is field for about 50 px under the track x 7100 (`pkkk` in that scan; run
  11 read the same). In the clean shot two stretches are residue-coloured and not cream: row y 14437
  at x 6640-6730 (dark, yellow-green and red blotches) and row y 14480 at x 6800-6950 (red and olive);
  the chip-2 stripped shot shows both rows orange and unbroken there and the metal shot their two
  edge lines in every gap between tracks.
- **Net C's metal** (pad (7057,14480) south; `h1_foot.png`, `h14_o7a.png`): x 7058 to y 14588, east
  to x 7100, south. `tla`'s metal of `rcs_e4` comes off its pad (7012,14522) south, east along y 14632
  and south on x 7057 (`trace/tla.txt`): the two share the track position x 7057, end to end, 44 px
  apart (trap 33), and each steps one track east like the jogs of pieces `fd`, `fe`. The track x 7100
  runs on south of y 15000 (`tools/sel_cut.py h` at y 14940 .. 15040 in both chips: 7099-7102;
  `tools/tl5_tracks.py v 7100 14590 15190`: bars of 8-12 px at each row, no more) to the end pad.
- **Crossings looked at** (tiles `h12_t1.png` .. `h12_t3.png`, 4x, four shots: 18 places). Stretches
  without metal in both chips of 14 px or more on the three wires: 15 + 15 px at (6343,12138-12186),
  where line 11's track crosses `cdp4_bus_s2`'s diagonal poly (its two edge bars; the track is of
  constant width and the clean shot's protected strip unbroken); 18 px at (6905,7872-7889), line 13's
  track over the row y 7888 of `tl3_w3982` (`eof`'s): the row's north edge bar and a dim stretch on the
  row in both chips, as on line 12's track over the same row 44 px west (`tools/textmap.py 6881 7860
  6929 7905 3 --acid` against `6837 7860 6885 7905`: no ring, no pad, the clean shot's protected cream
  the same); 16 px at (6602,10345-10360), line 13's track over `cdp3_hw_c7`'s row y 10361: a dark
  blotch on the east half of the metal in chip 2 only, chip 1 bright through it (`tools/textmap.py
  6578 10334 6626 10382 3 --acid`, against the same row under line 12's track and the row's real
  contact (6039,10356), which has ring and bright centre in both chips); 14-16 px at (6559,10406),
  (6322,13402), (6322,13576), (6430,12036) (row edge bars). One-chip stretches of 20-34 px at fifteen
  places, the other chip passing at each. Low red-minus-green stretches in the clean shot under the
  tracks: the rows y 9990, 10361, 9796 are greenish under every track that crosses them (trap 15);
  (6689,9393) is dirt on chip 1's clean shot (three dark blobs on the protected strip, both metal
  shots plain); (6689,9665) vivid red-orange, not a hole.
- **Other nets' tracks over the three rows**: none has a pad, a ring or a widening on any of them
  (`h10_rows_w.png`, `h10_rows_e.png`). The clean shot's low stretches along the rows
  (`tools/tl5_tracks.py h 14480 6385 7040`: x 6628, 6663, 6764, 6812, 6891, 6928; `h 14437 6428 7550`:
  x 6687, 6708 (21 px, minimum -32), 6734, 6895; `h 14393 ...`: x 6718, 6852) lie in the two residue
  stretches or at single tracks; three were looked at on tiles (`h12_t3.png`: (6708,14437) under
  `bd1_n2`'s track, (6928,14480) under `busl_x6992`'s, (6628,14480) under `rsel17_buf`'s): the metal
  bright and of constant width in both chips, no ring. `fd`'s jog y 14438 and `fe`'s jog y 14396 lie
  on the rows y 14437 and y 14393 for 44 px each (run 11: no contact).
- Overlays: `h14_o1.png` (north pads, columns and arms), `h14_o2.png` (diagonals, 3.3x), `h14_o345.png`
  (the three staircases), `h14_o6.png` (foot), `h14_o7a.png`, `h14_o7b.png` (the pad (7057,14480), the
  jog and the south end), `h14_o8.png` (north end pads).

## Logic

Wiring only. Traced: the eight joins above (no uncertain item on any). From `cdp3`'s notes:
`cdp3_hw_c#` = NOT q1 of the row H register bit of slice c#, so **the left array's rows at y 11338 ..
14894 each take one bit of register row H, inverted**. Believed, not traced: these eight rows are
eight of the fourteen rows of the memory address counter, and row H is the low byte of a 14-bit
address register (R13, the display start, or R15, the cursor; `regs` is the queue row that decides).
What the rows do with the bit is `larr`'s untraced part (x 3900-4720).

Piece `ch1`. Traced (no uncertain item on any of the eight nets): for each slice # of `cdp4`,
`cdp4_bus_s#` = `cdp4_in_s#`: the channel-1 line (which `cdp4` follows east to a contact under a track
that goes up into its row R1) is the data input of the row C latch bit of the same slice
(`cdp4_lc_s#_a` through the pass transistor gated by `cdp4_ld`), and the same net ends on a poly row
of the left array (s7..s1 at y 11488, 11922, 12442, 12984, 13397, 13874, 14351; s0 on the row at
y 15042 just south of the region, seen and not drawn). Nothing in the field drives these nets. Not
traced: which end drives (the array's rows, or `cdp4`'s row R1 upper, both untraced where these lines
arrive). Believed: the array's rows drive, i.e. eight bits of the memory address counter are what row C
latches on `cdp4_ld` and what row R1 takes from channel 1.

Piece `lc9`. Traced (no uncertain item of this package on any of the nine nets; line 5's name
`lc2_w8450` rests on an uncertain box of `lc2`'s, Ambiguity 8): each line is one metal from
`lc3`'s south edge to its end, with no contact on the way, so nothing in the field drives or loads
them. Seven go on as poly rows toward the bottom-centre logic's bus: **the ripple counter's clock
`lc3_w9947` (row y 14784), `rst_c`, whose inverse is `lc1_w7170` (row y 14697), the counter's
clear `lc2_w8450` = NOT `lc1_w7170` (row y 14740), `lc2_w9079` = NOT `lc3_w9299` (row y 14611),
`lc3_e9756` (14654), `lc3_e9798` (14567) and `rst_a` (14914)**; `rcs_e4` (the step logic's NOR,
`tla`) is the row above them (14523). Two (`res_b`, `lpstb_b`) go on south into `bl0`'s ground.
Not traced: what is at the far end of any of them (the rows' pads at x 7790/7835 and the bus metals are
`bc1`'s; `rst_c` and `lc3_e9756`, `lc3_e9798` also have ends east of `lc3` in the northern part).
Believed: the clock of the ripple counter and `rst_c` are driven in the bottom-centre logic, and
`lc2_w8450` and `lc2_w9079`, which have their drivers in the left-centre strips (`lc2_w8450`'s through
`lc2`'s uncertain box), are inputs there.

Piece `ctl`. Traced: `rsel14_buf`, `rsel15_buf`, `rsel17_buf`, `rsel16_buf` (`cdp4`'s selects 1-4) each reach, on one metal track from the south,
both the selector's gate row in `cdp4` and one poly row into the gate group at `cdp4`'s bottom-left
corner (no uncertain item on any of the four). `cdp4_rst` runs from its gate row to a poly that ends on
a box of that group (no uncertain item on what is drawn; the box itself is not drawn). **`cdp4_ld` =
`bc1_ld_a` = NOT `bc1_ld_n` = `bc1_ld_in1` AND `bc1_ld_in2`**: the 8-bit latch row C and the 6-bit
latch row D (`cdp4_ld6`, the same NAND through a second inverter) are loaded by the same event. That
join is **marked**: it rests on the `?M` over the box (51 px where the photos do not show the metal)
and on the reading that the box makes no contact with the metal (Ambiguity 9). Nothing in the field
drives or loads any of the six. Not traced: what drives the four selects (south of y 15000); the gate
group (`cdp4` (continue)). Believed: the group makes `cdp4_rst` from the selects (a gate band of each
select lies on its diffusion column, and `cdp4_rst`'s poly is tied to a node of that column), so that
the selector's nodes are pulled low when no select is high; and rows C and D together are one 14-bit
register loaded from the selector's bus lines.

Piece `d6`. Traced (no uncertain item on any of the six nets): `cdp3_g_c2` .. `cdp3_g_c7`, the lines
that `cdp3` follows from a contact on line g of each row A cell west to x 7600, are one metal each from
their row-end pads to `bc1`'s six row D data lines. So in the extraction **the data input of `cdp4`'s
row D latch bit under slice s1 (the pass transistor gated by `cdp4_ld6`) is `cdp3_g_c2`, and under s2
`cdp3_g_c3`**; `cdp3_g_c4` .. `c7` are `cdp3_g_c4` .. `cdp3_g_c7`, which `bc1` draws only as far as x 8040.
Believed: these run on to `cdp4_in6_s3` .. `s6` in the same order, so that the 6-bit latch row D takes
line g of the six large cells of `cdp3`'s row A, column c(k+1) into the bit under slice sk. Nothing in
the field drives or loads the six. Not traced: the row A cells (`cdp3` (continue), `cdp2` (continue)),
so what line g is; a latch's data input does not drive, so the cells must (believed).

Piece `sr`. Traced (no uncertain item of this package; the net's other joins are `eofw`'s): `tc2_sr_g`,
which is also `tc2_sr_g` (the enable of latch D, the latch that makes `lc_step`) and row 2 of the gate
`tc2_r5589` = NOT(`lc1_w7170` AND (`rst_ck` OR `tc2_sr_g`)), runs from `eofw`'s corner pad down the
field and out at (7187,15000), with no contact in the field. So the net has a third branch, into the
bottom-centre logic. Not traced: its end (in `bc1`'s group x 7000-7860, y 15000-16300). Believed: the
driver of `tc2_sr_g`, which no package has found, is there (the net's three drawn ends, `tc2`'s latch,
`eof`'s gate and latch D's enable, are all gates). The reading rests on Ambiguity 13 (no contact
where the track crosses row y 13744).

Piece `kb`. Traced (no uncertain item): `bus_eq_r15`, gate 1 of the NAND beside `cdp3`'s row C, is one
net with a diffusion pad at (7555,11118) and the band east of it. Not traced: what that diffusion is
(a source or drain under or east of column 0's VSS rail, `cdp3` (continue)); it is the only drawn end of
the net that can drive it.

Piece `n2`. Traced (no uncertain item of this package or on the join): `bd1_n2`, the output of
`bd1`'s latch on R4's match (`bd1_n2` = NOT((`bd1_an` AND `rst_lat`) OR `bd1_n1` OR `rst_a`):
`notes/blocks/eof.md`, pieces `r4lat`, `isrc5`), is one net with `tl5`'s bus line x 5412 (the row y 3850 of `tl4`; both renamed `bd1_n2` by the refresh of 2026-11-19), the input of
the inverter of `tl4`'s right cluster that makes `rcs_e3`. So **`rcs_e3` = NOT `bd1_n2`**: the step
logic's `rcs_cond_n` = `rcs_e4` OR (`rcs_e3` AND `rcs_a2`) takes R4's latched match inverted. Between
the latch and that inverter the net is wire only (about 23,000 px: the bottom bus field, this field,
`lc1`'s diagonal bundle, `tl5`'s bus); no other gate is on it in what is drawn. The equation is
marked, not firm, for reasons outside this package (the latch's load tie in `bd1`, an uncertain item
at `tl4`'s inverter).

Pieces `x68`, `x69`. Traced: two through lines with no connection in the region. What they are is
not known: named for their place (`busl_x6820`, `busl_x6906`).

Pieces `r12`, `r13`. Traced (no uncertain item of this package): `rsel12_buf` (`sel`'s buffered select
of R12, drawn by `regs` to the field's south edge) is one net with `cdp3_gate_e` and with gate row 4 of
`cdp4`'s corner NOR; `rsel13_buf` is one net with `cdp3_gate_f` and with gate row 2. So R12 is read
through `cdp3`'s row E (row C onto bus N) and R13 through row F (row H onto bus N), and **`cdp4_rst` =
NOR(`rsel12_buf`, `rsel13_buf`, `rsel14_buf`, `rsel15_buf`, `rsel16_buf`, `rsel17_buf`)** (firm).
Believed: `cdp4_rst` holds the nodes of `cdp4`'s selector low except during a read of one of the six
readable address registers.

Piece `e6`. Traced (no uncertain item): six through lines, no connection in the region; each is
`lc3`'s net of the same name (`lc3_e9577` .. `lc3_e9793`), whose other end is a poly row that leaves
`lc3` east at x 6450. What they are is not known. Believed from the follower's ends (about 477 px
apart): each ends at one row of the left array's lower part.

Piece `p2`. Traced (no uncertain item): `bl0_w15088` is `rst_n` = NOT `rst` (`lc1`'s gate 4; `rst` =
NOR(`lpstb_b`, `res_b`)), so **`bl0_w15412` = NOT `rst_n`**, firm: `bl0`'s wide inverter makes a
fourth copy in `rst`'s sense (after `rst_a`, `rst_b`, `rst_c`), high while both pins are low; `bl0`
follows its output to a pad (4909,15414) and a track south (loads not traced). `rst_n` also runs on
east from `bl0`'s pad (6320,15088) (its port (6450,15088), "seen to x 6790"). And `lc2_w8450` (the
ripple counter's clear, the data of latch B) has a branch to the track x 4822, end not read.

Pieces `fb`, `fa`. Traced (no uncertain item): two wires with no connection in the field, each from a
poly row at the foot of the field (y 14870, y 14827, entering from `bc1`'s bus in the east) to a poly
row at y 7214 / y 7171 at the top of the northern part. What they are is not known: named for their
place (`busl_x6949`, `busl_x6992`).

Pieces `fc`, `fd`, `fe`. Traced: `rcs_mv` (no uncertain item on the wire; `tl3`: `rcs_mv` =
NOR(`tl3_w4546`, `tl3_e4852`), marked there) leaves the top-left logic and crosses the whole field to
south of y 15000: **the net whose inverse is term 1 of the row counter's step request has loads in the
bottom-left of the chip**, not read. `tc2_r5718` (no uncertain item; neither end identified: a poly
row from east of x 8250 at y 5718 in the north, the row y 14524 toward `bc1`'s bus in the south).
`busl_x7122`: from the row y 8863 under `cdp3`'s column 0 rail to the row y 14480 toward `bc1`'s bus;
the 42 px under the rail are uncertain, and what the row is east of the rail is `cdp3`'s (Ambiguity
18). No transistor.

Pieces `ga`, `gb`, `gc`. Traced (no uncertain item on any of the three wires): `lc1_w7780` = NOT
`lc1_w7733` (`lc1`: gate E1, firm there; latch D's data) runs from the left-centre strip down the
field to a pad at (7100,15175) and a poly row toward the bottom-centre logic's west rail: **the signal
that latch D samples has a second destination in the bottom-centre logic**, not read. `busl_x6559`
and `busl_x6603`: from the rows y 7258 and y 7300 of the crossing field at the top of the northern
part to the rows y 14437 and y 14393 toward `bc1`'s bus; what they are is not known (the rows y 7257
and y 7300 further west, at x 6146-6187, are `rst_a`'s and `tl3_w3982`'s, which end there on pads with
metals east; whether these two rows are other polys on the same lines or something else is not read).
No transistor.

## Ports

| Name | Layer | Where | Direction | What |
|---|---|---|---|---|
| `cdp3_hw_c7` .. `cdp3_hw_c0` | P | x 7600, y 10361, 10404, 10447, 10490, 10535, 10577, 10621, 10664 (18 px wide) | in | `cdp3`'s channel G west pieces, drawn there from x 7600 |
| `cdp4_bus_s7` .. `cdp4_bus_s0` | P | x 7600, y 11878, 11922, 11966, 12009, 12052, 12096, 12138, 12182 (20 px wide) | not known | `cdp4`'s channel-1 lines, drawn there from x 7600 |
| `cdp4_bus_s7` .. `cdp4_bus_s0` (`cdp4`'s name: `cdp4_in_s#`) | P | x 7600, y 13636, 13592, 13549, 13506, 13462, 13418, 13375, 13332 | not known | `cdp4`'s channel-2 west pieces, the row C latch inputs |
| `cdp4_bus_s7` .. `cdp4_bus_s1` | P | x 4780, y 11488, 11922, 12442, 12984, 13397, 13874, 14351 | not known | poly rows on west into the left array (`larr` draws nothing east of x 3900) |
| `cdp4_bus_s0` | M | (5451,15000), 16 px wide | not known | the track goes on 45 px to a pad (5365,15042) on a poly row from the west (`bl0`) |
| `cdp3_hw_c7` .. `cdp3_hw_c0` | D | x 4780, y 11338, 11815, 12291, 12768, 13247, 13725, 14202, 14894 (20 px wide) | in (driven in `cdp3`) | on west into the left array's rows; `larr` draws nothing east of x 3900 |
| `rst_a`, `res_b`, `lpstb_b`, `lc3_w9947`, `lc2_w8450`, `rst_c`, `lc3_e9756`, `lc2_w9079`, `lc3_e9798` | M | y 10400, x 6082, 6126, 6169, 6212, 6256, 6299, 6342, 6386, 6429 (14 px wide) | `lc2_w8450`, `lc2_w9079`: in (driven in `lc2`, `lc3`; for `lc2_w8450` through `lc2`'s uncertain box, Ambiguity 8); the others not known | `lc3`'s nine metals at its south edge (its file ends them at y 10400; it calls the fifth `lc2_w8907`) |
| `lc3_e9798`, `lc2_w9079`, `lc3_e9756`, `rst_c`, `lc2_w8450`, `lc3_w9947`, `rst_a` | P | x 7550, y 14567, 14611, 14654, 14697, 14740, 14784, 14914 (24 px wide) | as above | poly rows on east 240-290 px to pads at x about 7790 / 7835 under `bc1`'s 13-line bus metals (not drawn) |
| `res_b`, `lpstb_b` | M | (6366,15000), (6408,15000), 14 px wide | not known | tracks on south into `bl0`'s ground (line 3 seen to y 15150) |
| `rsel14_buf`, `rsel15_buf`, `rsel17_buf`, `rsel16_buf` | P | x 7600, y 12225, 12485, 12528, 12788 (23 px wide) | in (driven from south of y 15000) | `cdp4`'s select rows, drawn there from x 7600 |
| `rsel14_buf`, `rsel17_buf`, `rsel16_buf`, `rsel15_buf` | P | x 7550, y 13701, 13809, 13961, 14004 (24 px wide) | in | poly rows on east 40-100 px to gate bands on the diffusion column of `cdp4`'s corner gate group (not drawn; sel1's steps 12 px north at x 7548) |
| `rsel14_buf`, `rsel15_buf`, `rsel17_buf`, `rsel16_buf` | M | y 15000, x 6538, 6581, 6624, 6668 (14 px wide) | in | tracks on south into `bl0`'s ground (followed to y about 16150-16190) |
| `cdp4_rst` | P | x 7600, y 12874 (22 px wide) | not known (believed in: driven by the corner gate group) | `cdp4`'s row, drawn there from x 7600 |
| `cdp4_rst` | P | (7532, 13906-13927) | not known | the poly ends on the west outline of the box (7535-7580, 13903-13940), not drawn (Ambiguity 9) |
| `bc1_ld_a` (`cdp4`'s name: `cdp4_ld`) | P | x 7600, y 12962 (22 px wide) | in (driven in `bc1`, through the `?M`) | `cdp4`'s strobe row of latch row C, drawn there from x 7600 |
| `bc1_ld_a` | M | (7448,14050), 14 px wide | in | joins `bc1`'s metal of the strobe driver's twin output |
| `cdp3_g_c2` .. `cdp3_g_c7` | P | x 7600, y 9123, 9080, 9036, 8993, 8949, 8906 (23 px wide) | not known (believed in: driven by `cdp3`'s row A cells) | `cdp3`'s channel B tracks onto line g, drawn there from x 7600 |
| `cdp3_g_c2` .. `cdp3_g_c7` | M | y 14050, x 7189, 7231, 7274, 7317, 7360, 7404 (14 px wide) | as above | each joins `bc1`'s metal (drawn there from y 14040) onto the contact of its line 1 .. 6 (`cdp3_g_c2`, `cdp3_g_c3`, `cdp3_g_c4` .. `cdp3_g_c7`) |
| `tc2_sr_g` | M | (7460-7474,8795), 14 px wide | not known | onto `eofw`'s metal south of the corner pad (7446,8732) (`M 7466,8745 y8800`; `eofw`'s port there is named `tc2_sr_g`, an alias) |
| `tc2_sr_g` | M | (7180-7194,15000), 14 px wide | not known (believed in: driven in `bc1`'s group) | the track goes on south in `bc1`'s ground: to y 15482, west to x 7103, south; the follower ends at (7100,16279) (not read) |
| `bus_eq_r15` | P | x 7600, y 9438-9460 (22 px wide) | out (driven from the diffusion at its south end; received by `cdp3`'s gate 1) | `cdp3`'s row y 9450, drawn there from x 7600 |
| `bus_eq_r15` | D | x 7600, y 11092-11127 | in | the diffusion band goes on east under column 0's VSS rail (x 7600-7646) into `cdp3`'s ground (not drawn) |
| `bd1_n2` | M | (6704-6718,15000), 14 px wide | in (driven by `bd1`'s latch) | onto `eof`'s metal from the bottom bus field (piece `n2w`, `M 6711,15000 ..`) |
| `bd1_n2` | M | (6769-6783,10400), 14 px wide | out | onto `eof`'s metal north (piece `n2n`, `M .. 6775,10400`, then labelled as an open join): to `tl5`'s bus line x 5412 and the inverter that makes `rcs_e3` |
| `busl_x6820` | M | (6813-6827,10400) | not known | the track goes on north; the follower ends at (6817,9988), not read |
| `busl_x6820` | M | (6747-6761,15000) | not known | on south into `bl0`'s ground; the follower ends at (6754,16220), not read |
| `busl_x6906` | M | (6899-6913,10400) | not known | on north; the follower ends at (7078,8778) (candidates (6905,10057), (6908,9798)), not read |
| `busl_x6906` | M | (6834-6848,15000) | not known | on south into `bl0`'s ground; the follower ends at (6839,16219), not read |
| `rsel12_buf`, `rsel13_buf` | M | (6445-6459,15000), (6487-6501,15000), 14 px wide | in (driven by `sel`'s buffers) | onto `regs`' metals from the bottom bus (`M 6452,16168 y14990`, `M 6494,16210 y14990`) |
| `rsel12_buf`, `rsel13_buf` | M | (6683-6697,10400), (6726-6740,10400), 14 px wide | out | onto `regs`' metals north to the pads of `cdp3_gate_e` (row y 10055) and `cdp3_gate_f` (row y 10316) |
| `rsel13_buf` | P | (7550, 13734-13754) | out | into the block of gate row 2 of `cdp4`'s NOR `cdp4_rst` (`cdp4`'s name there: `rsel13_buf_u`) |
| `rsel12_buf` | P | (7550, 13862-13884) | out | onto gate row 4 of the same NOR (`cdp4`'s name: `rsel12_buf_u`), after the step south at x 7528-7550 |
| `lc3_e9577`, `lc3_e9621`, `lc3_e9665`, `lc3_e9708`, `lc3_e9750`, `lc3_e9793` | M | y 10400, x 5915, 5851, 5785, 5722, 5655, 5588 (diagonals, 14 px wide) | in (from `lc3`'s crossing rows) | onto `lc3`'s diagonal metals, which its file ends at y 10400 |
| the same six | M | y 15000, x 5322, 5279, 5235, 5192, 5148, 5105 (14 px wide) | not known | tracks on south; the follower ends at (5326,15381), (5284,15859), (5239,16506), (5194,16981), (5151,17462), (5107,17938), not read |
| `rst_n` | P | (5464-5486, 10400) | in (driven in `lc1`) | onto `lc3`'s poly from the end pad (5473,10207) |
| `rst_n` | P | (5700, 15078-15098) | out | onto `bl0`'s row of `bl0_w15088` (`P 5700,15088 x5755`); the track crosses y 15000 at x 4909 inside this piece |
| `lc2_w8450` | P | (5530-5552, 10400) | in | onto `lc3`'s poly from the end pad (5540,10165) |
| `lc2_w8450` | M | (4815-4829, 15000) | not known | the track x 4822 on south; the follower ends at (4823,16690), candidates (4823,15199), (4823,15305), (4823,15548), (4823,15723), not read |
| `busl_x6949`, `busl_x6992` | P | (7550, 14859-14881), (7550, 14816-14838) | not known | poly rows on east to pads at about (7836,14872), (7794,14826) under `bc1`'s bus metals (not drawn) |
| `busl_x6949`, `busl_x6992` | P | (7060, 7203-7225), (7060, 7160-7182) | not known | poly rows on west into the crossing field of the northern part (seen as poly to x 6720; not read beyond) |
| `rcs_mv` | P | (6227-6247, 6350) | in (driven in `tl3`) | onto `tl6`'s poly column from the corner of the row y 6238 |
| `rcs_mv` | M | (6964-6978, 15000) | out | the track x 6971 on south into `bl0`'s ground; the follower ends at (6970,15282), candidate (6971,15098), not read |
| `tc2_r5718` | M | (7526-7540, 6400) | not known | onto `tc2`'s metal from its pad (7530,6324) |
| `tc2_r5718` | P | (7550, 14513-14535) | not known | the row y 14524 on east toward `bc1`'s bus pads (seen as poly to x 7580; not drawn) |
| `busl_x7122` | P | (7592, 8852-8874) | not known | the row y 8863 on east under the wide rail; ends 8 px short of `cdp3`'s `?P` (Ambiguities 17, 18) |
| `busl_x7122` | P | (7550, 14469-14491) | not known | the row y 14480 on east toward `bc1`'s bus pads (seen as poly to x 7580; not drawn) |
| `lc1_w7780` | P | (6450, 7770-7790) | in (driven in `lc1`) | onto `lc1`'s row of gate E1's output at its port |
| `lc1_w7780` | P | (7170, 15207-15229) | out | the row y 15218 from the end pad (7100,15175), on east under `ck_out`'s track toward `bc1`'s rail x 7292-7342 (seen to x 7260; not drawn) |
| `busl_x6559`, `busl_x6603` | P | (6800, 7247-7269), (6845, 7289-7311) | not known | poly rows on west into the crossing field of the northern part (not read) |
| `busl_x6559`, `busl_x6603` | P | (7550, 14426-14448), (7550, 14382-14404) | not known | the rows y 14437, y 14393 on east toward `bc1`'s bus pads (seen as poly to x 7600; not drawn) |

## Ambiguities

1. **Red patches on the poly rows in the clean shot** (for instance (6340-6385,10353),
   (6095-6140,10530), (6160-6200,10660); each one track wide). Readings: a contact or a channel
   under that track; or a colour difference of chip 1's stripped shot only. Assumed the second:
   neither chip-2 shot shows anything there (the track keeps its width, no ring, no pad; `q1.png`
   at 3.2x, three shots), and a crossing field without pads carries no taps (guide, trap 15).
   Would settle it: nothing more in these photos; the patches' pattern over the whole band could be
   listed and compared with where the tracks' own contacts are.
2. **The rows' layer.** Taken as diffusion from the colours above; a poly row would make no
   difference to any connection here (nothing crosses the rows but metal).

3. **The poly L round c3's south pad** (the pad (5514,13222); a poly runs east along y 13258-13272
   and north along x 5545-5560, at minimum spacing from the pad's south and east edges). The round-1
   reviewer could not resolve the two outlines at 6x in the clean shot. Read by the tracer in the
   chip-2 shots at 5x (`c3s.png`): the pad's outline is closed and a pale strip 3-4 px wide lies
   between it and the poly's outline on both sides; `tools/px.py col 5515 13236 13276 2`: pad to
   y 13244, dark to 13258, poly (chip-2 stripped shot 157/116/63) from 13260. Taken as apart; there is
   no buried-contact box. The poly L itself is not drawn (not this piece's).

4. **Metal lying on a poly row without a pad** (the steps of the staircase x 6790-7140 over channel 2's
   rows; the steps of a second staircase at x 6290-6740 over channel 1's rows, about 180 px each; the track x 7511 over s0's poly column, y 12920-13332; a track x 5843 that begins 35 px south
   of s4's pad (5843,12335) and lies on s4's poly for about 100 px: it is line 1 of piece `lc9`,
   `rst_a`, after its second step; one step of the staircase x 7130-7440, 80 px on `rsel17_buf`'s row y 13809 at x 7267-7347, piece `ctl`: it is line 3 of piece `d6`, `cdp3_g_c4`; line 4's arm, `cdp3_g_c5`, lies the same way on the undrawn row y 13852 at x 7310-7390). Readings: a contact somewhere
   along the overlap; or none. Assumed none: no pad, no ring, no green hole in the clean shot on any
   (measurements under piece `ch1` above; guide, trap 13). A contact would join one of these eight
   nets to another track's net.
5. **Red and yellowish patches on the poly rows and diagonals in the clean shot** (channel 2 at
   x 6600-6900, the diagonals at (5700,12610), (6250,12250)): as Ambiguity 1, colour only; the chip-2
   shots show nothing there. The same on piece `lc9`'s seven rows at x 6450-6900 (red, dark and
   green patches one track wide; the eight strongest are listed under the piece) and, greenish, where
   its tracks cross `cdp3_hw_c5`'s row y 10447 (five tracks in a row: a tap on each would short five
   nets to one register bit). A contact on any would join one of the nine nets to the net of the track
   above; none has a pad or a ring in either metal shot. The same on piece `ctl`'s rows (the open
   stretches between tracks are olive in the clean shot; the longest are listed under the piece).
7. **A ring on `cdp4_bus_s2`'s diagonal poly at (6012,12480)** (clean shot, in the gap between lines 3
   and 4 of piece `lc9`, just east of line 3's corner (5996,12466); view `l9_s3.png`). Readings: a
   buried contact or a contact; or the clean shot's mark where a gap between two metals crosses a poly
   (guide, trap 2). Assumed the second: no metal is over the spot (the metal shot shows the poly bare in
   the gap) and nothing but the poly is there for a contact to join; so no connection depends on it.
8. **Line 5's identity with `lc2_w8450`** (piece `lc9`). The line is one metal with `lc3`'s
   `lc2_w8907`, the net of the ripple counter's clear gates. That `lc2_w8907` is `lc2_w8450` = NOT
   `lc1_w7170` rests on `lc2`'s uncertain poly and buried contact at (5598-5614, 8897-8916)
   (`trace/lc2.txt`, with its alias). Readings: joined there (then row y 14740 carries the inverse of
   `lc1_w7170` to the bottom-centre logic, and the line is an output of the left-centre strips); or
   not (then the clear's net has no driver in the left-centre strips and may be driven from the
   bottom-centre logic through this line). Working assumption: `lc2`'s. Would settle it: `lc2`'s box
   read in a second shot, or the far end of row y 14740 (`bc1`).
9. **The box at (7535-7580, 13903-13940)** (piece `ctl`; at the west edge of `cdp4`'s corner gate
   group, half outside this package's region). `cdp4_rst`'s poly ends on its west outline and
   `cdp4_ld`'s metal passes over its middle. Readings: (a) a buried contact joining `cdp4_rst`'s poly
   to the group's node diffusion (the tan area east of it, between the gate bands y 13862-13882 and
   y 13949-13973), the metal passing over without contact; (b) a poly pad with a metal contact, which
   would make `cdp4_rst` and `cdp4_ld` one net (the poly then a cross-under beneath the track x 7511);
   (c) a metal contact onto that diffusion, which would put the strobe on the group's node. Working
   assumption: (a). For it: the box has a heavy outline and a plain inside, unlike the pad at the
   other end of the same poly 90 px west (widened, green hole, ring with a bright centre: a contact);
   no bright centre in either metal shot and no green hole in the clean shot (guide, traps 22, 26); a
   metal is dark for 35-80 px over such a box. Against: one spot of 9 x 10 px on the track's line at
   (7557,13929), found by the round-4 reviewer (`tools/px.py pt 7557,13929 all`: chip-1 metal
   140/122/62, the brightness of bare ground there and well under the track's 160-190; chip-2 metal
   97/89/51, dark; chip-2 stripped shot 136/154/83, greenish like the ghosts of this piece's real
   contacts; clean shot 196/169/118, not green). It has no ring of its own, is not bright in chip 2
   and sits off-centre in the dark stretch, so it is not a contact by the usual tests; `tl3`'s node
   boxes under its thin metal show brighter spots than this (guide, trap 26). A pass-over cannot be
   told from these photos with certainty, which is why the stretch is `?M`. The box and the diffusion are not
   drawn here: they are the gate group's (`cdp4` (continue)), whose tracing settles it (if the node is
   the output of a gate whose inputs are the selects, (a) is right).
10. **`cdp4_ld`'s metal over the box** (the `?M` at x 7556, y 13895-13953): no metal in either metal
   shot for 51 px. Readings: one metal, dark over the box (trap 27); or two metals that both end at the
   box, on a contact inside it or on nothing. Assumed one metal: the clean shot shows the box in
   protected colours, a metal line does not end without a contact, and under reading (b) or (c) of
   Ambiguity 9 the two pieces are joined through the contact all the same. So `cdp4_ld` = `bc1_ld_a`
   holds under every reading; what differs is whether `cdp4_rst` or the group's node is on it too.
11. **Which end drives `cdp3_g_c#`** (piece `d6`): the field holds no transistor. One end is the data
   input of `cdp4`'s row D latch (a pass transistor: it does not drive), the other `cdp3`'s row A cell,
   untraced. Settled by tracing that cell (`cdp3` (continue)).
12. **`cdp3_g_c4` .. `cdp3_g_c7` and `cdp4_in6_s3` .. `s6`** (piece `d6`): `bc1` draws lines 3-6 only to
   x 8040 ("continues right: staircase, then beyond x 8500"), so the extraction does not join
   `cdp3_g_c4` .. `c7` to row D's bits s3 .. s6. Working assumption: joined in order, as lines 1 and 2
   are. Settled by `bc1` (continue).
13. **The track of `tc2_sr_g` over the poly row y 13744, at (7145,13728-13749)** (piece `sr`). Neither
   metal shot passes the metal test for 22 px along the track there (the other rows it crosses give
   8-13 px edge bars). Chip 2 shows a dark disc about 12 px across at (7145,13738) between the row's two
   edge bars (`tools/px.py col 7145 13722 13764 3`: red 44-86 from y 13731 to 13746); chip 1 shows the
   north edge bar and then a dim reddish stretch (red 112-177, green 78-99 at x 7145; 148-174/121-150
   at x 7150), under the test's level. Readings: (a) a plain crossing with marks on the metal; (b) a
   contact from the track onto the row, which would put `tc2_sr_g` on the row y 13744 (an undrawn poly
   row from west of x 6500 to a gate band, y 13750-13768, of `cdp4`'s corner gate group). Working
   assumption: (a). For it: the metal is not widened (18 px above, at and below the crossing; every
   contact in this field has a pad of about 40 px) and neither is the row (edges y 13734 and 13752, as
   elsewhere); the clean shot shows the row in protected poly colour under the track (215/160/113 at
   (7145,13740-13746), no hole, the protected strip as wide as above and below the row); the chip-2
   stripped shot reads as at the plain crossing of row y 13701 60 px north
   (`tools/textmap.py 7118 13690 7172 13772 3 --acid`); no bright centre in chip 2; and chip 2's metal
   alone is dark the same way where this track crosses row y 13852 (y 13850-13872) and at three places
   the round-5 reviewer found on piece `d6`'s tracks. Against: both chips are dim at the same spot,
   which dirt on one chip does not explain. Views `sr_c1.png` (4x), `sr_c3.png` (7x), `sr_c4.png` (the
   two rows under thirty tracks, 1.5x). Would settle it: the far ends of row y 13744 (if `tc2_sr_g` were
   on it, the row would need no other driver) and the corner gate group (`cdp4` (continue)).
   Run 8 adds the second direction: the row y 13744 is `rsel13_buf`'s, driven through a pad of its own
   at (6495,13744) (piece `r13`), and ends in gate row 2 of `cdp4`'s NOR. A contact at (7145,13738)
   would short the enable of latch D to R13's read select; reading (a) stands, and nothing in these
   photos can add to it.
14. **The south end of `bus_eq_r15`'s track** (piece `kb`): the pad (7538-7584, 11096-11144) is read as
   diffusion from its plain tan colour under the pad's metal in the clean shot, and the band east of it
   as the same diffusion from its two edge lines and the tan under the rail's edge. In the open gap
   between the pad's metal and the rail (x 7585-7597) the band has no colour of its own (clean shot
   110/93/64, chip-2 stripped shot 97/95/79, red minus green 2, like field) and the clean shot has a
   dark bar across it at x 7585 that the chip-2 shots do not have. Readings: one diffusion from the pad
   to under the rail; or a pad that ends at x 7584 with something else east of it. Working assumption:
   one diffusion (the two edge lines run unbroken from the pad's corners to the rail in the chip-2
   metal shot). What is under the rail is `cdp3` (continue)'s; nothing drawn depends on it yet.
6. **Which end drives `cdp4_bus_s#`**: not decidable in the field (it holds no transistor). Settled by
   `larr`'s rows east of x 3900 and `cdp4`'s row R1 upper.
15. **The track of `rsel12_buf` over the poly row y 13375, at (6452,13372-13389)** (piece `r12`; the row
   is `cdp4_bus_s1`'s channel-2 piece, piece `ch1`). Of the same kind as 13: neither metal shot passes
   the metal test for 18 px along the track, the full height of the row. In both chips the track's
   surface there is reddish and dim (`tools/px.py col 6452 13356 13396 4`: chip 2 137/81/28 and
   133/85/38 at y 13376-13380, chip 1 130/54/27 and 133/108/54; the track x 6494 over the same row is
   206-212/159-171/79-89), which is the colour of the open row beside the track ((6468,13374):
   136/97/48). Readings: (a) a plain crossing with a mark on the metal in both chips; (b) a contact
   onto the row, which would put R12's read select on a data line of latch row C; (c) a break in the
   metal. Working assumption: (a). For it: the track's two edge lines run through the crossing
   unbroken in both metal shots (`tools/px.py row 13374 6438 6468 3`: dark at x 6441 and x 6462 at
   every height from 13370 to 13382), which a break would interrupt; neither the metal nor the row is
   widened, and this track's real tap 480 px south has a pad 45 px wide with a ring, a bright centre
   and a hole; the clean shot is plain protected poly under the track (222/165/121 against
   219/162/124 under x 6494), no hole; both stripped shots read like the neighbouring crossings; a
   break would leave `cdp3_gate_e` with no driver, and a contact would short a select to a data line.
   Against: both chips at the same spot. On chance (rough): one chip alone fails the test for 20 px or
   more at 8 places on these two tracks and at 20 on run 7's three, of about 500 row crossings (about
   3% a chip), so among the field's several thousand crossings a few where both chips happen to fail
   are to be expected; this is the second found. Views `r8_13380_a.png`, `r8_13380_b.png` (4.5x), `r8_x13375.png` (4.6x, four shots, beside
   `r8_x7145.png`, Ambiguity 13's spot).

16. **The track of `busl_x7122` over the poly row y 13744, at (7058,13727-13761)** (piece `fe`; the row
   is `rsel13_buf`'s, the one of Ambiguity 13, 87 px west of that spot). Neither metal shot passes the
   metal test for 18 px and again for 14 px with 3 px between (`g11_scan.txt`), the height of the row
   and its two edge lines. `tools/px.py col 7058 13718 13766 4 all`: over the row chip 2 reads
   47-187/45-136/13-59 (126/129/55 at y 13742) and chip 1 146-174/97-114/28-45, against
   184-217/150-189/68-88 and 196-209/140-179/68-84 on the track x 7014 over the same row. Readings:
   (a) a plain crossing where the metal's surface is dim in both chips; (b) a contact onto the row,
   which would put R13's read select on this wire; (c) a break in the metal. Working assumption: (a),
   drawn plain, no `?` item (as 13 and 15). For it: the track's two edge lines are there across the
   crossing at the same places as beside it (`tools/px.py row 13742 7040 7076 3`: dark at x 7046 and
   x 7067-7070; at y 13775: x 7046 and x 7070), so the metal is neither widened nor interrupted; the
   row is not widened; the clean shot is protected cream of the track's full width with no hole
   (221/169/119 under x 7058, 214/164/110 under x 7014); a real tap of this row, 560 px west, has a
   pad 45 px wide with ring, bright centre and hole; a contact would short a read select to a wire
   that the same row's other dim crossing (`tc2_sr_g`'s, Ambiguity 13) would then be shorted to as
   well. Against: both chips, and this is the second dim crossing on this one row (of about 30
   tracks that cross it), which chance alone does not make likely: something about this row's
   surface at some tracks is not understood. What would settle it: the driver of the row y 14480 or
   the far end of the row y 8863 (a net that cannot be a read select). View `g7_t1.png` (4.6x, four
   shots).
17. **The row y 8863 under the wide rail** (piece `fe`; the `?P` x 7550-7592). West of the rail's edge
   (x 7550) the row is open poly (chip-2 metal shot 160-166/110-115/54-63, clean shot red-brown;
   `tools/busl_rowy.py 7500 8835 8890`: centre 8863, 24 px). Under the rail the two edge lines of
   the row run on in all four shots (view `g6_j.png`, 5.5x, four shots), but the clean shot's colour
   between them is dark red (113-143/39-52/35-38: `tools/px.py row 8863 7430 7700 10`), not the cream
   of poly under metal, as far as a slanted boundary at x 7600-7608, east of which it is cream
   (216/171/108); the chip-2 stripped shot shows only fringes there. The clean shot is anomalous
   over this patch (the field above the row is grey-green under the rail's east half where metal
   protected it: trap 28's inversion), and a slanted boundary is not layout. Working assumption: one
   poly row through; drawn uncertain to x 7592. The alternative (the row ends at the rail's edge
   and something else begins) would need an end line across the band at x 7550, where both stripped
   shots show only the rail's etch-boundary line (trap 4).
18. **`cdp3`'s uncertain row and contact at y 8864 are this row's, and its metal x 7835 does not reach
   them** (seen, not drawn; for `cdp3` (continue)). `trace/cdp3.txt` has `?P 7600,8864 x7848`,
   `?C 7834,8862` and `M 7835,8850 y9414` as parts of `cdp3_k_a` ("seen by the first run only, not
   re-checked"). The row and the pad are there: one cream poly from x 7605 to a pad with a ring, a
   bright centre and a green hole at (7835,8862) (view `g8_k_a.png`, 4.3x, four shots). But the pad's
   metal goes **north**, to a second pad at about (7834,8645) (`tools/follow.py 7835 8830 N --gap 16`:
   end (7834,8642); view `g8_pad.png`, 3x), and south of the pad there is no metal at x 7835: plain
   ground over the rows y 8900-9050 in both metal shots (`g8_pad.png`; `tools/follow.py 7835 8900 S`:
   no metal; `tools/busl_both.py h` at y 8900, 8950, 9000, 9060, 9120, 9160: none at x 7835, the
   track x 7880 present; at y 9200 and y 9300: metal at x 7837). So `cdp3`'s metal of `cdp3_k_a`
   starts between y 9160 and y 9200 (its contact (7833,9165)), and the row y 8863 is another net,
   which goes on north from (7834,8645) (not read). Had this piece's row been drawn to x 7600, the
   extraction would have joined `busl_x7122` to `cdp3_k_a` through those items; it is drawn 8 px
   short for that reason. Proposed to the coordinator: correct `cdp3`'s three lines (handoff).
19. **Polys under these three wires without a contact** (drawn plain, traps 8, 13): `rcs_mv`'s poly
   column under ten metals and its metal y 6913 over `lc1`'s bus polys (x 6275-6451) and whatever else
   lies between x 6250 and x 7208 (`tools/tl5_tracks.py h 6913 6250 7195`: no stretch over 10 px
   without metal, no hole; the follower gives no contact candidate on the 2,700 px from (7208,8590)
   to the pad); the poly corner under `tc2_r5718`'s corner (7360,7453) (Inventory); the three arms on
   `ch1`'s rows; the four foot jogs on the rows y 14264, 14307, 14394, 14437 (two of them `bc1`'s
   lines 5 and 6); the wide metal x 7483-7535 over the two foot rows. None has a pad, a ring or a hole.
   Not looked at one by one: the poly rows of `bw` and `eof` that the northern runs x 7208, x 7360,
   x 7511 and x 7533 cross (the scan flags nothing on them: at most 13 px without metal in both chips,
   no hole).

20. **Polys under and over the three wires of run 12 without a contact** (drawn plain, traps 8, 13,
   15): the eight tracks over `lc1_w7780`'s row y 7780; the staircase metals over the three poly
   columns; the three upper arms on `ch1`'s rows y 11922, 11964, 12008 (173 px each); line 11's track
   over `cdp4_bus_s2`'s diagonal poly; the thirteen to eighteen tracks over each of the rows y 14480,
   14437, 14393 (among them `bd1_n2`'s, the read selects', `rcs_mv`'s, `tc2_r5718`'s and
   `busl_x7122`'s with their jogs, `ck_out`'s and `bc1_ld_a`'s) and the wide metal x 7483-7535 over
   the last two. None has a pad, a ring or a hole (Inventory). Not looked at one by one: the poly
   rows of `bw` and `eof` that the northern runs x 6819, x 6861 and x 6905 cross between y 7300 and
   y 8280 (the scan flags the one stretch at (6905,7872-7889), above, and one-chip stretches).
   Would settle any of them from another direction: the far ends of the rows.

## Review

**Round 1: full review** (2026-11-19 14:05 +0100; a fresh Fable 5.2 reviewer agent; commit 59157c2; piece `h8`).
Told to suspect: the track staircase's order, the north pad staircase, the poly rows (a step, a
break, a tap, the red patches), each south pad (which track is on it, whether it ends), the lower
tracks' crossings, the diffusion rows (straight, their layer, c3's step), a shift by one row at x 7600.
Checked (25 images in `cache/scratch/busl/review-1/`): both pad staircases and the track staircase at
3.4x in the metal and clean shots, with `tools/follow.py --gap 16` on every track; the poly rows by an
edge-pair measurement every 7 px on the chip-2 metal shot to x 7618 (offset 0 to -2 px, width 23, no
step, no break) and views at 1.6x (no pad on any track); two red patches by `tools/textmap.py --acid`
(colour only); the nine rows at x 7600 (the ninth, y 10317, ends on its own pad near (6730,10315);
the eight drawn are the southern eight); each south pad at 4x in two shots; c3's step in three shots;
the lower tracks by `tools/tl5_tracks.py v`; a diagonal poly under c1 and c2 at (5400-5470,13395-13465)
and a pad (5408,14347) beside c0's track (neither touches); the diffusion rows in three shots (chip-2
metal blue 78-87: diffusion).
Findings: none. Could not check: (a) whether the poly L south and east of c3's pad touches the pad
(would change a connection): read afterwards by the tracer in the chip-2 shots, apart (Ambiguity 3);
(b) the diffusion rows and lower-track crossings were read at 1.4x and by text tools, not at 4x;
(c) `cdp3` has no `ports.d` file, so the join at x 7600 rests on the photos and the rows' y.
Nothing changed in the trace.

Round 1: no findings.

**Run 2, piece `ch1`. Round 1: full review** (2026-11-19 14:39 +0100; a fresh Fable 5.2 reviewer agent;
commit 44a0f6d; images in `cache/scratch/busl/review-2/`, 22 used).
Told to suspect: tracks claimed to run through a pad or to end on one, the T at (5800,11880), the near
misses (s3's corners above s2's and s4's pads, the metal that begins south of s4's pad), track identity
through the bends and diagonal steps, s3's pad-to-poly joint and its L beside `cdp3_hw_c3`'s pad, the
three diagonals, s0's poly column under the track x 7511, the staircase steps lying on channel 2's
rows, the rows' identity at x 7600 and row 11922's continuity, the coloured patches.
Checked: every track piece with `tools/tl5_tracks.py` and `tools/follow.py --gap 16` from every pad;
the four through pads (rings symmetric, 15-18 px each side in both chips, metal beyond on both
sides); the T (view and text map: one metal in both chips); every end pad (no metal beyond; s4's pad
has 32 px without metal and open poly before the other metal starts, which has no contact down to
y 12500); the near misses (40, 52 and 30 px apart); s3's L (joined to its pad in both stripped shots,
joined to row 13462, about 12 px clear of `cdp3_hw_c3`'s pad on both sides); the three diagonals
(single, separate, no pads); s0's column (leaves the pad, joins row 13332, ends there, no hole under
the metal); the rows (eight and eight at x 7600 within 3 px of `cdp4`'s, no step; row 11922 continuous
through its pad; the seven array rows to x 4780 and row 12745 without another pad); six contact-hole
candidates from the text scans (none has a ring or pad in the metal shots); the extraction,
`tools/unsure.py`, `tools/padjoin.py` (nothing listed).
Findings, both geometry only, both confirmed:
1. s0's diagonal step was drawn 16 px too far north (y 13900-13943). Tracer's check, the metal test in
   both chips every 10 px (`tools/px.py row Y 5486 5600 6 metal,metal1`): the east track is at
   x 5582-5588 at y 13905, 5564-5576 at 13935, 5540-5552 at 13955; s1's step is as drawn. Redrawn
   y 13916-13959. The two tracks stay 33 px or more apart.
2. Channel 1 also has a metal staircase lying on its rows (x about 6290-6740, y 11878-12138, about
   180 px a step), which the notes named only for channel 2. No pad or ring on any step (reviewer's
   views `ch1w.png`, `ch1e.png`). Now covered by Ambiguity 4.
`tools/t.sh busl sameconn.py 44a0f6d`: `connections identical`.
`.venv/bin/python tools/sameconn.py 44a0f6d`: `connections identical`.
Could not check, or only weakly: the joint of s3's pad to its L is under the pad's metal and rests on
the two stripped shots; the row and staircase crossings were judged at 1.3x in the metal shots and
by text scans, not each at 4x; s0 south of y 15000 was not viewed by the reviewer (the tracer's view
`j6.png`).

Round 1: no findings that change a connection.

**Run 3, piece `lc9`. Round 1: full review** (2026-11-19 16:58 +0100; a fresh Fable 5.2 reviewer agent;
commit 25f8257; images in `cache/scratch/busl/review-3/`, 20 used).
Told to suspect: a swap or bridge in either staircase (read by the tracer at 1.5x; the follower lost
line 4 at its second corner), line 1 beside `cdp4_bus_s4`'s pad (5843,12335) and on its poly, the
greenish and coloured patches at the crossings on the lines and on the rows (twelve places named), the
seven rows from x 6430 to x 7550 (a break, an early end, a change of position, a tapped track; row
y 14914 and the last 150 px most), the end pads (a second poly, a metal running on, the two pad columns
assigned to the wrong lines, the track x 6452), lines 2 and 3 at their corners and past line 1's pad
and row, the ring at (6012,12480).
Checked: both staircases in both metal shots at 2.1-2.5x with the trace, the follower on every line
(ten in, ten out, same order, no bridge); line 4 over the diagonal at 5x in four shots (bars of 15 px
at most); line 1 against s4's pad (about 14 px without metal at y 12354-12368 in both chips, text map
and a 5x view; no ring or hole along the overlap to y 12483); the ring (clean shot only, no metal over
it); a scan of its own of both metal shots for widening on either side of every line (none; it finds
three known pads); the four named crossings on the lines by text map (plain crossings); the end pads at
3.2-3.4x in four shots (one metal from the west, one poly east, field north and south, nothing running
on); lines 2 and 3 (plain corners, clear of line 1's pad, bars only over row 14914); the track x 6452
(no pad); the rows to x 7550 (no field colour on any centre line in the clean shot, edges constant, no
pad on any crossing track, uniform under the wide metals; (6846,14914) at 6x in four shots and
(6665,14567): colour only; (7533,14784): a gap ring); the join with `lc3` at y 10400 (same x within
1 px, metal continuous); the extraction.
Findings, neither changes a connection, both confirmed by the tracer:
1. Line 5's name rests on an uncertain item of `lc2`'s: `tools/unsure.py` lists `lc2_w8450` as two
   pieces, the line on `lc2_w8907`'s (trap 17). Tracer: confirmed (`tools/unsure.py`, the box at
   `trace/lc2.txt` lines 385-387). The notes said "no uncertain item on any of the nine nets" and gave
   the port as driven in `lc2`: both now say what they rest on (Inventory, Logic, Ports, Ambiguity 8).
   Nothing drawn changes: the label stays the net's canonical name.
2. The pads of rows 14827 and 14870 are fed from the north (tracks x 6927, x 6885), not "from the
   south" as the notes said. Tracer: confirmed (`tools/tl5_tracks.py v 6915 14850 15000` and
   `v 6872 14885 15000`: no metal south of either pad; `v 6885 14600 14850`: metal with the rows' bars).
   Notes corrected; neither pad is drawn.
Also reported, outside the piece: `tools/follow.py` going north steps from line 9 onto `rcs_e4` at
(6522-6552,9798) and from line 2 onto line 3 at y 9775, both follower artefacts (25 px of bare ground;
ground bright in chip 2 only), and `lc3_e9798`'s metal arrives at y 9798 from a track x 6514 from the
north (Not done; handoff).
The trace is unchanged since the reviewed commit.
`tools/t.sh busl sameconn.py 25f8257`: `connections identical`.
`.venv/bin/python tools/sameconn.py 25f8257`: `connections identical`.
Could not check, or only weakly: anything east of x 7550; the rows at x 6985-7320 seen only in the
chip-2 metal shot at 2.2x (the other shots by text); the plain staircase and foot corners at 2.1-2.5x,
not 4x; of the eight named row patches three were viewed, the rest covered by the scans.

Round 1: no findings that change a connection.

**Run 4, piece `ctl`. Round 1: full review** (2026-11-19 17:39 +0100; a fresh Fable 5.2 reviewer agent;
commit 01aa682; images in `cache/scratch/busl/review-4/`, 33 used).
Told to suspect: the box (7535-7580, 13903-13940) and the metal x 7556 across it (a contact, two metals
or one, whether `cdp4_rst`'s poly reaches it); the four through pads (the right track, running on, the
right row); the nested staircase (read at 2.4x); the near misses (sel2's arm above sel3's pad, the
corner north of `cdp4_rst`'s pad, `cdp4_ld`'s pad below `cdp4_bus_s0`'s, the arms y 13938 and 13982
beside the rows); the staircase step on row y 13809 and the one north of row y 13701; the ten row
stretches (a break, a step, an early end, a tapped track, whether the four lower ones go on past
x 7550); the rows' identity at x 7600; taps on the six tracks; eight coloured stretches and the dot
(7558,13792).
Checked: the box at 4x and 7x in four shots (protected colours in the clean shot up to its north and
south outlines on the track's line, open ground beside; poly colour on both sides of its west outline
in the chip-2 stripped shot; the pad (7467,13897) and the band one poly; no metal between that pad and
the arm y 13938); the staircase at 4.4x in both metal shots (four right-angle steps, order kept, no
bridge; a green patch under sel2 at (6583,13120-13170) in chip 1 only); all eleven pads at 4.2-4.5x in
both chips (ring and bright centre, each on its claimed track; the four through tracks carry on south);
the near misses (ground or bare poly between, and one more: another net's corner (7430,13897) 10-16 px
west of `cdp4_rst`'s south pad); the rows (six at x 7600, matching `cdp4`; all ten stretches
continuous, poly colour in every open gap in chip 2; the four lower rows run on past x 7550); the
crossings on all six tracks (edge bars only); the step on row y 13809 at 5x and the greenish spots (no
ring, pad or widening); the join to `bc1` (the corner (7448,13982), the crossing of row y 14004, one
metal on to y 14636); the extraction and `tools/unsure.py`.
Findings: one, a comment only, confirmed by the tracer:
1. Ambiguity 9 said "Against: nothing" and the inventory "no bright centre in either": there is a
   9 x 10 px spot at (7557,13929) on the track's line inside the box, at ground brightness in chip 1's
   metal shot and greenish in the chip-2 stripped shot. Tracer: confirmed (`tools/px.py pt 7557,13929
   7557,13915 7556,13880 7535,13929 all`: 97/89/51, 140/122/62, 136/154/83, 196/169/118 at the spot;
   the track at (7556,13880) 205/134/59 and 199/159/98). Not a contact by the tests (no ring, dark in
   chip 2, off-centre); recorded in Ambiguity 9 and under the piece. Nothing drawn changes: the stretch
   stays `?M` and the box undrawn.
The trace is unchanged since the reviewed commit.
`tools/t.sh busl sameconn.py 01aa682`: `connections identical`.
`.venv/bin/python tools/sameconn.py 01aa682`: `connections identical`.
Could not check, or only weakly: whether the metal is continuous over the box and what the box is (the
corner gate group settles it); most row crossings by the two-chip metal test and text maps, not each
at 4x; the clean shot's hole test is weak in this field (sure contacts read red minus green from -12
to +61); anything south of y 15000, east of the drawn ends, or `bc1`'s metal beyond y 14060.

Round 1: no findings that change a connection.

**Run 5, piece `d6`. Round 1: full review** (2026-11-19 18:02 +0100; a fresh Fable 5.2 reviewer agent;
commit d9c6e0e; images in `cache/scratch/busl/review-5/`, 15 read).
Told to suspect: a swap or bridge in either staircase (the upper read at 2.3x, the lower at 3.6x, in
the chip-2 metal shot; the follower leaves lines 1, 2 and 4 at their lower arms), the long runs (a
step of one track, a pad, a contact or a break; line 6's detour at y 12835), a track running on
through either end, a second poly on a row-end pad, the rows from the pads to x 7600, each lower track
on the right line of `bc1`'s, the dismissed spots (six named, the crossings of row y 12745, the 20 px
dark stretch north of line 1's contact), the two near misses beside `cdp4_rst`'s pads, the arms lying
on the rows y 13809 and y 13852.
Checked: the six north pads at 4x in the chip-2 metal shot and both stripped shots (each on its own
row's west end, field west and north, no second poly, no metal for 55 px or more north of any in
either chip); the rows to x 7600 (unbroken, onto `cdp3`'s rows at the same y); the upper staircase at
3.6x in both metal shots (six nested right-angle steps over field, order kept; the pad (7554,9450) of
another net 8-10 px of open ground below line 6's arm); the long runs by a scan of its own of all
nineteen vertical segments in both metal shots (no widening to 21 px in both chips, no 14 px without
metal in both, a steady centre per 300 px) and strips at 1.12x in the metal and clean shots (no pad,
no poly under a track); line 6's detour at 4x in three shots with text maps (the track x 7512 from
the north ends on its own pad (7510,12742), no metal at y 12766-12820; open ground at y 12848-12854
between the arm and `cdp4_rst`'s north pad); the lower staircase at 3.2x in both metal shots and arms 3
and 4 at 4x in four shots (order kept; no ring or hole on either arm; open ground at x 7440-7448
between line 5's corner and `cdp4_rst`'s south pad; line 6's arm clear of the box at x 7535); the south
ends (each track on the claimed pad of `bc1`'s, no metal on south; line 1's dark stretch is ring plus
row edge); the seventh track where it crosses `bc1`'s rows (no ring, widening or hole); the dismissed
spots by text map and the y 12745 crossings at 4x; the extraction and `tools/unsure.py` (none of the
six nets listed).
Findings: none. Two comments for the notes, both checked by the tracer and added under the piece
(chip 2's dark notches on the metal at three places; the red stain on pads 1 and 2 in the clean shot).
The trace is unchanged since the reviewed commit.
Could not check, or only weakly: the long runs end to end at 2x or more (they rest on the 1.12x
strips and the two numeric scans); `bc1`'s rows east of the pads and `cdp3`'s rows east of x 7780.

Round 1: no findings.

**Run 6, pieces `sr` and `kb`. Round 1: full review** (2026-11-19 18:29 +0100; a fresh Fable 5.2 reviewer agent;
commit ebde718; images in `cache/scratch/busl/review-6/`, 15 used). The two pieces were reviewed together
(two single wires of the same build, no transistor).
Told to suspect, `sr`: the dark crossing of row y 13744 at (7145,13728-13749) (a contact, a break or a
plain crossing); the start south of `eofw`'s corner pad, the poly crossed at y 8850-8875 and which of
the four diagonals is drawn; the long run x 7209 (a step, a pad, a tap, a break; the two follower
candidates; chip 1's dark stretch); the step y 13680 and the jogs y 14176, 14285, 14588 (two metals
meeting end to end, the track going on south at x 7145, a join to `d6`'s line 1 pad, a contact on the
row under the arm y 14176); two flagged stretches; the crossing of y 15000. `kb`: the south pad's layer,
its contact, the band's join to the pad (the bar at x 7585) and whether it reaches x 7600, anything else
leaving the pad; the north pad (contact, anything west or north, the arm 25 px north, the row's
identity); two flagged places on the track.
Checked, `sr`: the start (one metal from `eofw`'s pad to the diagonal, a narrow neck at x 7470-7476 on
`eofw`'s stretch, the test passing at x 7473 with bars of 16 px or less; a plain crossing of the poly
y 8850-8875, no hole); the diagonal (the south-east one of four, the next one ends on the pad
(7425,8862); both corners plain; 2.9x, chip 2); the long run by a width scan of its own every 2 px in
both chips (12 px wide, centre 7208.5, no widening, step or tap, no break of 25 px), (7207,9579) at
4.5x (plain crossing), (7208,12618) (a spot beside the track), y 9176-9243 (a blob on chip 1 only);
**Ambiguity 13 at 4.4x and 7x: agrees it is a plain crossing** (at x 7148 chip 1 fails for only 14 px,
the edge bar; chip 2's dark patch is 27 px wide, wider than the track, with no bright centre; the clean
shot reads plain protected poly, 6-7 against 0-3 in the hole of the pad (7188,14091); the row is not
widened; no pits in the chip-2 stripped shot; why both chips are dim there stays unexplained); the step
and the three jogs at 4.1-4.4x in both chips (each a corner of one metal, no metal beyond any corner;
none from y 14100 to 14171 between line 1's pad and the corner (7187,14176); none at x 7145 from
y 14186 to 14390; no contact on the arm y 14176 or where the other arms pass rows); the two flagged
stretches (an edge bar and marks, no holes); the port (plain metal across y 15000, text map
y 14930-15075). `kb`: the north pad (a real contact: ring and bright centre in both chips, a pit in
the chip-2 stripped shot; 30 px without metal and open ground between it and line 6's arm; nothing west
or north; the row continuous into `cdp3`'s); the track (no widening; (7554,10070) a plain crossing;
y 10897-10916 dark in chip 2 only, over field); the south end (the pad diffusion: flat tan 195/166/124
with a contact speck, where the north pad is salmon; a real contact; the band one diffusion with the
pad: in the gap redder than field by 25-33 in both chip-2 shots at x 7584 and 7589, the bar at x 7585
in the clean shot only; nothing leaves north, south or west); the extraction and `tools/unsure.py`
(nothing listed for the two nets).
Findings: one, geometry only, confirmed by the tracer:
1. `kb`'s band at the port: drawn `D 7575,11100:7600,11127`; the band's north edge rises under the
   rail's west edge, so at x 7600 it is about y 11092-11126. Tracer's check (`tools/px.py col 7603 11078
   11136 3 acid1b,metal` and `col 7596 ...`): tan 195-203/149-175/112-140 from y 11096 to 11123, the edge
   lines centred on y 11088 and 11129 at x 7603 and on 11090 and 11128 at x 7596. Redrawn
   `D 7575,11095:7600,11127`; the port is y 11092-11127. Same net, same layer, same side.
`tools/t.sh busl sameconn.py ebde718`: `connections identical`.
`.venv/bin/python tools/sameconn.py ebde718`: `connections identical`.
Could not check, or only weakly: anything south of y 15075; under the rail east of x 7600 (no ring or
speck seen on the band as far as x 7650, not read); the far ends of row y 13744; the long run by view
apart from its ends and y 9545-9645 (text tools only).

Round 1: no findings that change a connection.

**Run 7, pieces `n2`, `x68`, `x69`. Round 1: full review** (2026-11-19 22:56 +0100; a fresh Fable 5.2 reviewer agent;
commit 85f1dfb; images in `cache/scratch/busl/review-7/`, 18 used). Told to suspect: the nest of
corners (each south run onto the right north run, no two Ls touching); a pad, contact or tap missed
along 4,600 px of each line, with the list of greenish crossings; the twenty places where one chip
shows no metal for 20-38 px; `x69`'s arm on the poly row y 13375; the two edges (that `n2` meets
`eof`'s metals and not a neighbour's, and no step of one pitch in between); pads of neighbouring nets
close to the tracks.
Checked: the nest at 4.4x in both metal shots and by `tools/textmap.py 6654 13140 6930 13402 3` (six
separate Ls, arms ending flush, 25-30 px of bare ground or open poly between neighbours in both chips);
`x69`'s arm at 6x in the metal shots and at 7x in both stripped shots against a real pad (a plain bar, no
hole, no ringed box: no contact); the arm's east end against the track x 6949 (`tools/follow.py 6841
15040 N --gap 16` runs on to x 6949: guide trap 30, the 28 px between are open poly, chip 1 red
123-145 against metal over 200); `tools/tl5_tracks.py` on all nine segments (longest stretch dark in
both chips 16 px) and a text map of each of the twenty one-chip stretches (row crossings dim in one
chip, or a speck); its own two-chip scans of the gaps beside the three lines over the full length, with
the arms as controls (no metal in any gap: no tap, no step), and 1x strips (rings only on the known
neighbour pads); the neighbour pads (6732,12226), (6732,12485), (6731,12788), (6666,13961),
(6884,14869): each at least 12 px of non-metal from the tracks; both edges at 5x (straight through
y 15000 and y 10400, coinciding with `eof`'s metals at x 6711 and x 6775); the extraction (2,379 nets,
0 errors, 0 warnings, `rcs_e3` = NOT `bd1_n2`) and `tools/unsure.py` (the join's labels on one piece).
Findings: two, both wording only (no geometry changed), both confirmed by the tracer:
1. "Greenish under every track" (the trace comment and three places in these notes) is wrong: the
   colour goes by crossing, not by row (row y 13417 is green only under x 6841 and salmon under x 6668
   and x 6711; rows y 14089 and 14910 green only under x 6841; row y 13590 under x 6711 and x 6841).
   Tracer's check: `tools/px.py pt 6668,13417 6711,13417 6841,13417 6711,14089 6841,14089 acid1b` gives
   221/166/113, 222/167/120, 126/158/99, 183/111/74, 142/161/102. The no-contact reading stands on the
   other grounds (no ring and no pad in either metal shot; the patch is the whole protected width; `n2`
   is greenish over both `rsel14_buf`'s and `rsel15_buf`'s rows). Reworded in the trace comment, the
   Inventory and Not done.
2. The trace comment said "the third of the five nested Ls" and listed six. Reworded.
`tools/t.sh busl sameconn.py 85f1dfb`: `connections identical`.
`.venv/bin/python tools/sameconn.py 85f1dfb`: `connections identical`.
Could not check, or only weakly: not every one of the roughly 300 crossings at 4x (about 30 at 4x or
more, the rest by text scans and the 1x strips); the chip-2 stripped shot under the tracks shows only
fringes and was not used for contacts on the runs; anything beyond the two edges.

Round 1: no findings that change a connection.

**Run 8, pieces `r12`, `r13`. Round 1: full review** (2026-11-20 14:06 +0100; a fresh Fable 5.2 reviewer agent;
commit 420283d; images in `cache/scratch/busl/review-8/`, 12 used). Told to suspect: the dim crossing
(6452,13372-13389) (a contact or a break?); the two nests of corners (each L onto the right upper
run, no step of a track); the arm y 12097 on `cdp4_bus_s2`'s poly row; the two taps (this track onto
this row, the metal on through the pad, a second poly on a pad); the rows' east ends (the step of
row y 13852, a swap with the rows y 13701 and y 13809); the rows' layer and any second pad on them;
the upper runs to y 10400 and the join onto `regs`' metals; the ten dim stretches of the scan.
Checked: the crossing at 6x in four shots, by colour profiles and a per-pixel class map (both chips
orange across the track for about 10 px: chip 2 133-150/81-96/31-38, chip 1 114-137/51-68/26-37; no
ring, no pad, the row 20 px as elsewhere, no hole in the clean shot, 216/165/112 as under x 6494; the
track's two edge lines unbroken through the patch in both chips, no end line across; the same reddish
patch occurs in one chip alone on unbroken crossings, chip 1 at (6452,14304), chip 2 at (6494,13616)
and (7055,13852); the chip-2 stripped shot is no evidence there, it reads red minus green 67 at
(6452,14304) where chip 2's metal is whole); the taps at 4.6x and by text maps with the stripped shot
(ring, bright centre and hole on each, the metal on both ways through each pad, neighbouring tracks
13-18 px clear, field north, south and west of both pads); both nests at 4.5x (order kept, no stub
beyond a corner; the arms y 12984, 13028, 12141 over field); the arm y 12097 (no pad, ring or hole; a
pale patch in the stripped shot at (6564,12097) is fringes, 7x); the rows in every gap between tracks
(chip-2 blue 46-65, chip-1 green 67-96, against 82-90 and 109-129 on a field control at y 13782:
poly, unbroken, straight, no other pad; the L of another net that lies on row y 13852 at x 7312-7388,
piece `d6`'s line 4, has no contact, 5.6x); the east ends by views and profiles (row y 13852 ends at
x 7548 and steps south through open poly at x 7530-7546, y 13845-13881, onto the row y 13873, which
starts at x 7528; row y 13744 runs into `cdp4`'s block; field between each and the rows y 13701 and
y 13809: no swap); the long runs by the two-chip test and the follower from both ends (one metal
each, no ring besides the taps; each listed dim stretch a one-chip blemish or a row edge; the clean
shot's green patch at (6494,14787) is damage to chip 1's row there); the north join at 4.6x (the same
tracks as `regs`' metals); the full extraction (0 errors, `cdp4_rst` = NOR of the six selects).
Findings: none.
Could not check, or only weakly: continuity at (6452,13372-13389) rests on the edge lines (Ambiguity
15 stays); that `cdp4`'s block (7550-7578, 13732-13770) is poly (golden-brown 173/128/56 in the clean
shot under the track x 7556: `cdp4`'s reading; only that nothing field-coloured separates the row, the
block and the gate row); the south join at y 15000 by tools only; not each of the roughly 100
crossings singly (the metal test and the clean-shot scan cover them).

Round 1: no findings.

**Run 9, pieces `e6`, `p2`. Round 1: full review** (2026-11-20 14:38 +0100; a fresh Fable 5.2 reviewer agent;
commit ea21812; images in `cache/scratch/busl/review-9/`, 20 used). Told to suspect: the order of the
six lines through the diagonals and the nest (the two western diagonals rested on a 1.5x overlay); the
knot at x 5440-5560 (the pad (5473,10707) joined only to the row y 10750; the metal x 5474 on
`rst_n`'s column and over `lc2_w8450`'s row at the dark spot (5476,10643); the arm y 10752 one metal
with x 5518 and without contact to the row under it); the pad (5102,10750) against the fifth line's
corner; the two diagonal polys (swapped, touching, a second poly on a pad, the rows' layer, under the
VCC metal); the track x 4909 over the row y 10706; the south end (the track's end on the pad, the row
y 15088 to x 5700, the jog lying on it, the dark gap at x 5511-5526); taps along the eight tracks with
the scan's list; two metals end to end on one track.
Checked: the six lines by `tools/tl5_tracks.py h` cuts at y 10400, 10450, 10500 and `tools/follow.py`
(four run unbroken from `lc3`'s pads to beyond y 15000), the two western diagonals at 4x in both metal
shots ((5655,10400) becomes x 5518, (5588,10400) becomes x 5474; no pad, ring or hole where they cross
the polys); the knot at 4x or more in four shots and by text map (the pad joins in poly only to the
row y 10750, pink field between it and the row y 10641; no ring, widening or hole on the metal x 5474
over `rst_n`'s column or at (5476,10643), where the chip-2 dark spot is in no other shot; the line at
x 5488 is the row's end edge); the arm (one metal; the dim stretch x 5158-5181 is chip 2 only, 7 px
dark in both; no pad or hole); the west end (open poly, orange in both metal shots, between the pad
(5102,10750) and the corner at x 5148; the follower from the track x 5105 stops on the pad); the two
diagonals (two polys with 40 px of field between, each column on the row claimed; both rows poly and
continuous to their pads, edge lines unbroken under VCC in both metal shots; no second poly on either
pad); (4909,10706) (no pad, ring or widening in either metal shot, no pits in chip 2); the south end
(the track ends on the pad (4909,15087), bare ground beyond; the row y 15088 one poly to `bl0`'s pad;
the gap x 5511-5526 orange open poly in both metal shots like its neighbours; the jog without hole or
pad: `bl0_w15088` = `rst_n` holds); the eight tracks by its own flank scans (no gap in both chips over
15 px, no ring or branch on any; the scans find the four end pads and the corners); the diffusion-row
crossings (alike, without pads).
Findings: none.
Could not check, or on weaker evidence: the row y 10750 lies under the arm for its whole length, so
its continuity rests on the two stripped shots (chip 1's clean shot is patchy dark red at x 5240-5360);
on `rst_n`'s row under VCC at x 4948-4978 chip 1's clean shot is green with a dark wedge in chip 1's
metal shot, read as a blemish of chip 1 because chip 2 is whole there; at (4909,10706) the clean shot's
patch is as green as a real hole, and "no contact" rests on the absence of a pad; south of y 15000
only the track x 4909 was read; `lc3` north of y 10400 not re-read.

Round 1: no findings.

**Run 10, pieces `fb`, `fa`. Round 1: full review** (2026-11-20 15:44 to 16:01 +0100; a fresh Fable 5.2
reviewer agent; commit faf7c54; images in `cache/scratch/busl/review-10/`, 12 used). Told to suspect:
the diagonal bundle (each drawn diagonal on the right track and the right pad; corners placed from
cuts every 20 px); the two arms lying on `cdp4_bus_s2`'s and `cdp4_bus_s3`'s rows (a contact; the
nested corners; the vivid red row under `fb`'s arm); the poly columns under the crossing metals
(poly, continuous, one per pad pair, a contact from a crossing metal, a second poly or metal on a
pad); the crossing (6885,13835-13851) on `rsel12_buf`'s row; the three pads without a green hole and
whether a foot row goes on west of its pad; the foot rows from x 6950 to x 7550 (the wide metal,
`bc1_ld_a`'s metal at x 7338, a dozen tracks); taps on the six long runs; the end pads (the metal
running on north, the row leaving west only).
Checked: the extraction (2,455 nets, 4,579 transistors, 0 errors, 0 warnings); the eight pads at
3.6-4x (ring and bright centre in both metal shots, a hole or pitted box in a stripped shot, field on
every other side; neither foot row goes west of its pad: clean shot green, chip-2 blue 73-81 against
56 for poly; both end metals stop at their pads, the rows leave west only, row y 7171 clears `fb`'s
end pad by about 13 px of field); the arms at 5x in four shots (corners as drawn, bare ground at every
other corner position in both chips, no ring or widening; under `fb`'s arm the row is olive at
x 6886-6914 and vivid red at x 6930-6954 in the clean shot, both metal shots fully bright: colour
only); the diagonals at 4x in both chips (each one continuous line onto the pad drawn; chip-1 cuts
every 20 px keep x + y at 15988 and 16054, no step); the columns (poly, continuous, straight: blue
46-65 in chip 2 along both; no ring where the metals cross; a dim blotch on chip 1 at (7166,8756) on
the crossing metal, chip 2 bright and the clean shot uniform cream at 5.5x: dirt); the crossing
(6885,13835-13851) (an edge bar and a chip-2 speck, no pad or widening, the neighbouring tracks alike
on that row); the long runs by its own two-chip scans (no stretch of 20 px without metal, no metal
wider than 16 px, no ring; the ring test finds the known pads in chip 2; the eight greenish row
crossings plain); the foot rows (poly in every open stretch, straight, no pad, no branch by cuts at
y 14806, 14848, 14892, no contact from any crossing metal, `bc1_ld_a`'s at x 7338 among them).
Findings: none in the trace. Three remarks on the notes' wording, each checked and the notes
corrected (no geometry changed): (1) the wide metal over row y 14870 ends at x 7513, not at the
region's edge, and has a limb x 7469-7513 north that also crosses row y 14827, without contact onto
either row (confirmed: `tools/sel_cut.py h 14848 7350 7570` gives 7463-7514, `h 14800` and `h 14760`
7468-7515); (2) the columns pass under one metal of `eofw` (y 8662-8680) and one staircase metal that
no package draws (y 8704-8722 west of x 7135, a leg x 7140-7152, y 8748-8765 east), not under two of
`eofw`'s (confirmed: `tools/sel_cut.py v 7100`, `v 7146`, `v 7180 8640 8790`; `eofw` draws one metal
there); (3) a grey band in the clean shot under the limb between the two rows (x 7484-7504), read as
field. The two undrawn metals are in Not done.
Could not check: the rows beyond x 7550 and west of x 7060; where the two undrawn metals go; most row
crossings were checked by text maps and scans, not by image; the grey band of remark (3) has no
control under another wide metal.

Round 1: no findings.

**Run 11, pieces `fc`, `fd`, `fe`. Round 1: full review** (2026-11-20 17:28 to 17:44 +0100; a fresh
Fable 5.2 reviewer agent; commit da3e566; images in `cache/scratch/busl/review-11/`, 28 used). Told to
suspect: the dim crossing of `fe`'s track over `rsel13_buf`'s row at (7058,13727-13761) (a contact or a
break); the follower's contact candidates at (7014,13810), (7058,13810), (6971,13702); track identity
at the three arms, at the foot jogs (which track reaches which pad; the track x 7014 against
`rcs_e4`'s pad (7012,14522); the fourth net's pad (7057,14480)) and in the diagonal bundle; the three
pads at the heads of the diagonals and the poly hops north of them, against the neighbouring net of
the pad (7317,8623); `rcs_mv`'s poly column (one poly, no contact from the metals over it, the join to
`tl6`'s poly); the join to `tc2`'s metal, the jog at y 7279 and the corners (7511,7453), (7360,7453);
the `?P` under the rail and the gap left to `cdp3`'s `?P`; a pad or tap along any long run.
Checked: the extraction (2,455 nets, 4,579 transistors, 0 errors); (7058,13744) against the row's
real tap (6495,13744) and the track x 7014 (no pad, ring or hole; the track's edge lines run through
at x 7046 and x 7068 in both chips and the centre is metal-hued; the same dim centre is at
(7058,13852) on `rsel12_buf`'s row, and one wire cannot be on both selects: a plain crossing); the
candidates and (6971,14390), (7036,9805-9826) (bright metal in at least one chip, no ring); the arms
(each upper track joins the lower track drawn); the foot (the track x 7014 ends at its jog, bare
ground down to the pad (7012,14522); 10 px of open ground between the jog y 14438 and the pad
(7057,14480); field between the pads on both row lines; gaps between `fd` and `fe` on the tracks
x 7058 and x 7100); the diagonals (two-chip cuts: x + y stays at 16116, 16182, 16247, ground
between); the heads (three contacts, both poly columns continuous, no contact from the two metals
over them, field between the pad (7357,8667) and the neighbouring net's poly); `rcs_mv`'s column (one
poly from `tl6`'s to the pad, ten metals, no contact; the pad (6189,6956) beside it separate); the
join to `tc2`, the jog y 7279 (a 5 px dim line in chip 2; chip 1 and the clean shot continuous), the
plain corners; the row y 8863 (no end line crosses the band under the rail in both chips, no contact
from the rail: the `?P` is right); the pad (7835,8862) (its metal goes north, none at x 7835 for
y 8900-9160: Ambiguity 18 and the gap are right); the long runs by its own width and ring scans,
validated on four known pads (no break of 20 px in both chips, no ring, no side arm).
Findings: none in the trace's geometry. Three remarks on wording, each checked and corrected:
(1) the trace's comment said `rcs_mv`'s column passes under eight metals; there are ten, as these
notes say (comment corrected in two places); (2) the poly under the corner (7360,7453) does not end
there but turns west as a row y 7468-7490 (confirmed on `review-11/h3_corner7360.png`: one cream band
from the column to at least x 7285 in the clean shot; the Inventory reworded; no contact either
way); (3) the foot jogs y 14267 and y 14308 lie on poly rows for their full 44 px, which the notes
did not say (confirmed, and the other two jogs do as well: `tools/busl_rowy.py 7166 14240 14460`
gives rows at y 14264, 14307, 14394, 14437; no hole and no stretch without metal on any of the four:
Inventory and Ambiguity 19). Only comment lines of the trace changed: `tools/t.sh busl sameconn.py
da3e566` ends `connections identical`, and `.venv/bin/python tools/sameconn.py da3e566` ends
`connections identical`.
Could not check: the poly rows crossed by the runs x 7208, 7360, 7511, 7533 and by the tracks x 7036,
7078, 7122 (y 9150-13480) one by one (text scans, four spot maps and two survey images); whether the
row y 8863 is broken exactly under the rail's edge line at x 7550; anything south of y 15000 or east
of x 7550 on the foot rows.

Round 1: no findings.

**Run 12, pieces `ga`, `gb`, `gc`. Round 1: full review** (2026-11-20 20:19 to 20:32 +0100; a fresh
Fable 5.2 reviewer agent; commit dc7a63f; images in `cache/scratch/busl/review-12/`, 27 used). Told to
suspect: the three staircases and the steps north of the poly columns (a line on the wrong track or
two lines swapped; `tools/follow.py` had misread the staircase y 11923-12054); the diagonals' pads and
tracks against their neighbours (`rcs_e4`, line 14, `bd1_n2`); each of the thirteen pads as a contact
(the four foot pads were accepted without a clear green hole); the three poly columns (one poly each,
no contact from a crossing metal); whether `lc1_w7780`'s row ends on the pad (6819,7780) apart from
the poly east of x 6870 on the same line, and whether the track x 6861 touches that pad (trap 16);
the row y 14480 (broken between the pads (7057,14480) and (7143,14481), continuous west of them
through the residue-coloured stretch; row y 14437 likewise); the track position x 7057/7058 between
this wire's jog y 14588 and `rcs_e4`'s arm y 14632; the dim crossings (6905,7872-7889),
(6602,10345-10360), (6343,12138-12186); the south end pad and its poly L.
Checked: the three staircases at 3.5-4x in both metal shots (each four plain nested Ls inside
`rcs_e4`'s, line 11 westmost throughout; the staircase the follower failed on also by cuts down every
track and along every arm with `tools/busl_both.py`; line 12's corner at (6386,11985) is dim in chip 2
only, chip 1 bright and the clean shot's protected strip unbroken); the steps north of the columns
and the diagonals (cuts at 13 heights: x + y = 15467 / 15534 / 15598 go to the pads and tracks
claimed, bare ground between each pad's ring and the neighbouring metal by `tools/textmap.py`); all
thirteen pads (ring and bright centre in both metal shots, a pitted box in the chip-2 stripped shot,
the four foot pads at 4.5x in four shots; field beyond each pad on the sides with no drawn poly); the
three poly columns (one poly each from pad to pad, only edge bars and no hole under the staircase
metals); the row y 7780 (one poly under eight tracks, ending on the pad; east of the pad open field,
then pink under the track x 6861, and `eof`'s poly starts at about x 6878; the track x 6861 is apart
from the pad's ring by ground and its own edge line in both chips); the row y 14480 (continuous from
(6364,14482) to (7057,14480): chip 1's metal shot shows orange poly in every gap of the residue
stretch and the open stretch x 6988-7040 is poly in three shots; field between (7057,14480) and
(7143,14481)); the rows y 14437 and y 14393 to x 7550 (no pad; the two jogs lying on them and the
wide metal x 7483-7535 show no ring or hole); the track position x 7057 at y 14597-14624 (no metal in
either chip, only the open orange poly of the row y 14610); the three dim crossings (4.2x, four
shots: plain); the south end (the metal ends on the pad (7100,15175), the poly L runs to the row
y 15218; a pad (7100,15262) below it is separate, ground between); every metal segment
(`tools/tl5_tracks.py`: no stretch of 20 px or more without metal in both chips; the clean shot's
lows on the tracks are greenish rows without rings); the full extraction (0 errors, no new
transistor), `tools/unsure.py` and `tools/padjoin.py` (nothing for these nets).
Findings: none.
Could not check: the stubs beyond their drawn ends (the rows y 7258 and y 7300 west, the rows y 14437
and y 14393 east of x 7550, the row y 15218 east of x 7170); `lc1`'s part of the row y 7780 west of
x 6440; the long straight runs between the staircases at 4x (read by the scans and by strip views at
1.4-2.1x in the chip-2 metal shot); the crossings of the northern runs over the rows between y 7370
and y 8060 one by one, other than (6905,7880).

Round 1: no findings.

## Not done

- Everything else in the field: about 20 more tracks and the other rows. Next pieces, in the
  order they join things: (1) done in run 6 (pieces `sr`, `kb`; `wr_r15`'s row does not enter the field); (2) done in run 8 (pieces `r12`, `r13`: the rows y 13744 and y 13852 and the two tracks); (3) done in run 9 (pieces `e6`, `p2`), but for the VCC metal
  x 5340-5390 and its branch west along y 10590-10650 (supply; not drawn); (4) the top band's ninth row (y 10317, `cdp3_gate_f`) and the three poly rows
  at the top left (y 10560, 10686, 10736); (5) done in run 9 (piece `e6`: the staircase at x 5100-5700 is its nest of Ls); (6) the bands at y 11850-12150 and below; (7) the foot of the field: rows y 14827 and
  14870 and their tracks: done in run 10 (pieces `fa`, `fb`); the
  net that starts on row y 14523 at the pad (7100,14522): done in run 11 (piece `fd`: it is `tc2_r5718`); the rows above
  y 14523 (`bc1`'s bus has four more, y 14354-14482): of row y 14480 the part east of the pad (7143,14481) is piece
  `fe` (run 11); the fourth net of the foot jogs (the row y 14480's west part, the pad (7057,14480) and its metal
  south) and the rows y 14437, y 14393 with their lines: done in run 12 (pieces `ga`, `gb`, `gc`: the first is
  `lc1_w7780`); left: **the row y 14350 and its line, the fourteenth of the staircase bundle** (pad (6406,14350);
  tracks x 6408, x 6473 (arms y 12942, y 12054), x 6646 through y 10400, arm y 10015, x 6732; diagonal x + y =
  15660 to a pad (6904,8669); a poly column to a pad (6904,8408); a metal east along y 8405 and north on x 6948
  to a corner (6940,7042), west along y 7042, the follower's end (6186,7042): the south-most of the three nested
  corners of which `eof`'s `bd1_n2` is the middle one, so probably onto the row of `lc1`'s diagonal bundle that
  comes from `tl5`'s bus poly x 5368, `tl5_w2722`; not read); (the track x 6452 beside piece `lc9`'s pads is `rsel12_buf`, run 8); the metal that turns south at
  about (7187,14165) below line 1's end pad.
- Piece `sr`'s south end: `tc2_sr_g`'s track from (7187,15000) on: x 7186 south over `tla`'s poly
  (y 15334-15444) to (7186,15482), west to x 7103, south; the follower ends at (7100,16279), contact
  candidates at (7100,15596-15660) (`bc1` (continue): the group x 7000-7860, y 15000-16300; seen at 1x
  in `sr_s3.png`, nothing read). The driver of `tc2_sr_g` is expected there. And the row y 13744, whose
  ends decide Ambiguity 13 (item (2) above).
- Piece `kb`'s south end: the diffusion band east of x 7600 at y 11095-11127, under column 0's VSS
  rail (`cdp3` (continue)); the three other diagonals of the bundle north-west of `sr`'s (one ends on
  the pad (7425,8862), whose poly runs east along y 8850-8875 under `sr`'s track; the northern part).
- `wr_r15`'s west end at about x 7603-7640, y 11825-11850, under the metal x 7600-7645 (`cdp4`
  (continue); view `b_ends.png`, tile 3).
- Piece `d6`'s ends: `bc1`'s lines 3-6 east of x 8040 to the feet of `cdp4_in6_s3` .. `s6` (`bc1`
  (continue); Ambiguity 12); the row A cells of `cdp3` on line g (`cdp3` (continue)).
- Piece `ctl`'s ends: the four select tracks south of y 15000 (x 6538, 6581, 6624, 6668; to y about
  16150-16190: `bl0`, `bl1`), where their drivers must be; **the gate group at `cdp4`'s bottom-left
  corner** (`cdp4` (continue), x 7550-7870, y 13640-14040): the box (7535-7580, 13903-13940) on which
  `cdp4_rst`'s poly ends (Ambiguity 9), the diffusion column under the wide metal x 7598-7650 with its
  contacts (7607,13718), (7607,13838) and the gate bands of sel1 (y 13677-13698), row y 13744
  (13750-13768), sel3 (13792-13812), row y 13852 (13862-13882), sel4 (13949-13973), sel2 (y 14004 on).
- Piece `lc9`'s rows east of x 7550: 240-290 px more of each to its pad at x about 7790 or 7835 (the
  pads are listed under the piece), and from there `bc1`'s 13 bus metals east (`bc1` (continue), or
  this package with its region extended to x 7860). Lines 2 and 3 south of y 15000 (`bl0`).
- Piece `e6`'s south ends: the six tracks from y 15000 on (x 5322 .. 5105; the follower's ends are in
  the Inventory): `bl0`'s ground and the left array's lower rows. Piece `p2`'s: `lc2_w8450`'s track
  x 4822 from y 15000 on (follower: to (4823,16690)); `rst_n` east of `bl0`'s port (6450,15088).
  The metal jog that lies on the row y 15088 at x 5400-5500 is another net's track (x 5495 north,
  x 5410 south), not followed. The tracks x 4867, x 5365 and the wide metal x 4960-5010 of the west
  side are `bl0`'s, piece `h8`'s and a supply.
- s0's last 45 px: the track from (5451,15000) to the pad (5365,15042) and the poly row west of it
  (`bl0`, or this package if its region is extended to y 15060).
- The diffusion rows and the poly rows west of x 4780 (`larr` (continue)).
- The northern part (6450-7600 x 6750-10400). Seen from this run: `lc3_e9798`'s metal along y 9798 turns north
  at x about 6515 (`tools/follow.py 6480 9798 E --gap 16`: north on x 6514, seen to y 9532; its end not
  read), 28 px short of `rcs_e4`'s metal x 6552-6564 (`tools/textmap.py 6420 9770 6600 9870 4`: a dark
  edge, bare ground with red 128-160, a dark edge, in both chips: not joined, and the round-3 reviewer's
  view at 5x agrees; `tools/follow.py` at `--gap 16` jumps it going north from (6429,10426), and going
  north from (6126,10426) it steps from line 2 onto line 3 at y 9775, in `lc3`: ground bright in chip 2
  only, guide trap 30).
- The wide metal over row y 14870 (x 7378-7513, y about 14840-14905) with its limb x 7469-7513 north
  across row y 14827 (views `f10_e7400.png`, `review-10/r12_widemetal.png`): drawn by no package, not
  followed (believed supply; `bc1` (continue) has "the VSS plate at the foot of the s0 rail" nearby).
- The staircase metal over the two poly columns of pieces `fb`, `fa` (y 8704-8722 west of x 7135, a
  leg x 7140-7152, y 8748-8765 east of it): drawn by no package (`eofw` draws the one above it,
  y 8662-8680); the northern part.
- Pieces `fb` and `fa`'s ends: east of x 7550 the rows y 14870 and y 14827 to their pads at about
  (7836,14872), (7794,14826) and the metals from those pads (`bc1` (continue), with piece `lc9`'s seven
  rows); west of x 7060 the rows y 7214 and y 7171 across the crossing field, under `eof`'s staircase
  arms from x 6650 on (the northern part; their west ends are beyond x 6400, in `lc1`'s strip).
- The other lines of the diagonal bundle north of y 10400: `busl_x6906` (pad (7078,8755), poly column
  to (7078,8490)) is left; the lines x 7035, x 7078 and x 7121 are pieces `fc`, `fd`, `fe` (run 11).
- Pieces `fc`, `fd`, `fe`'s ends: `rcs_mv`'s track x 6971 south of y 15000 (follower: to (6970,15282),
  candidate (6971,15098): `bl0`), where its loads must be; `tc2_r5718`'s row y 14524 and `busl_x7122`'s
  row y 14480 east of x 7550 (`bc1` (continue), with the nine rows of pieces `lc9`, `fb`, `fa`), and
  `tc2_r5718`'s north end (`tc2`: a poly row y 5718 east of x 8250); `busl_x7122`'s row y 8863 east of
  x 7592: under the rail, then a poly to a contact pad (7835,8862), a metal north to a pad at about
  (7834,8645) and on (`cdp3` (continue); Ambiguity 18, with the correction to `cdp3`'s `cdp3_k_a`).
- Seen beside those pieces and drawn by no package (the northern part): a net from a pad (7317,8623)
  (its metal north on x 7317; follower end (7316,7992)) by a poly east along y 8615-8637 and south on
  x 7400-7418 to a pad (7405,8777), on which the staircase metal y 8757 ends, and a poly east along
  y 8770-8783 under `tc2_sr_g`'s track to a heavy-outlined box (7490-7547, 8753-8793) (views `g2_m.png`,
  `g2_c.png`); two pads (7419,7384), (7463,7343) with tracks north beside `tc2_r5718`'s track x 7511
  (`g9_o4.png`); the open poly column x 7352-7372, y 7380-7490, whose south end lies under
  `tc2_r5718`'s corner; a pad (7270,6905) 60 px east of `rcs_mv`'s corner (7208,6913) (`g9_c2.png`);
  the pad (6188,6955) at the west end of the metal y 6955, 45 px south-west of `rcs_mv`'s pad
  (`g3_w.png`); the wide metal x 7483-7535 over the rows y 14480 and y 14524 (`g9_rows.png`).
- Pieces `ga`, `gb`, `gc`'s ends: `lc1_w7780`'s row y 15218 east of x 7170 (seen as open poly under `ck_out`'s
  track to x 7260, toward `bc1`'s rail x 7292-7342, where `bl0` found the gate bands of other rows: `bc1`
  (continue) / `bc3`); the rows y 7258 and y 7300 west of x 6800 / x 6845 (the crossing field of the northern
  part; `eof`'s metals y 7258 and y 7300 of `rst_a` and `tl3_w3982` lie on the same lines further west); the
  rows y 14437 and y 14393 east of x 7550 (`bc1` (continue), with the eleven rows of pieces `lc9`, `fb` .. `fe`).
- Seen by the reviewer of run 12, south of `lc1_w7780`'s end pad: a pad (7100,15262), separate from it (ground
  between), drawn by no package.
- Seen beside them and drawn by no package: a pad (6690,8621) between `eof`'s pad (6645,8580) and `tla`'s
  (6730,8580), with a poly column north and a metal about x 6679 south (`h4_north.png`, `h5_npads.png`). Of the
  staircase metals over the three poly columns, `trunks` draws the one at y 8452 and `eofw` the one at y 8498;
  whether any package draws the third (y about 8540 west of x 6880) and the one over column 3 at y about 8625
  was not checked.
- `trunks`' two lines in the field: taps not checked (R4).
- The ends of the two through lines of run 7: `busl_x6820` north of y 10400 (follower end (6817,9988),
  in the northern part) and south of y 15000 (end (6754,16220), `bl0`); `busl_x6906` north (end
  (7078,8778), the northern part) and south (end (6839,16219), `bl0`). (The tracks east of them, x 6949
  and x 6992, are pieces `fb` and `fa`, run 10.)
- The undrawn rows of the bands y 13300-13700 and 14050-14950 that these tracks cross (y 13417, 13548,
  13590, 13633, 13699, 14178, 14220, 14437, 14698 among them): their ends would confirm, from another
  direction, that none of the greenish crossings of run 7 is a tap.

## Corrections (coordinator, from the handoffs of 2026-11-19, fourth batch)

- The four select tracks of piece `ctl` are driven by `sel`'s buffers: they are the read selects of R14-R17 (`regs` run 2: the tracks hop in poly at y 16168-16558 and turn east along rows y 18168-18299).
- The "two undrawn rows of other nets" y 13744 and y 13852 are, as read by `regs` (run 3, not drawn), the read selects of R13 and R12, tapped at (6492,13744) and (6450,13852) from the tracks x 6494 and x 6452. For Ambiguity 13: a contact at (7145,13728-13749) would put latch D's enable `tc2_sr_g` on a register read select.
- Lines 1-3 of piece `lc9` are the reset copy `rst_a` and the buffered pins RES and LPSTB; line 6 is `rst_c` (`eof` runs 10, 11, 13).

## Corrections (coordinator, from the handoffs of 2026-11-20)

- Ambiguity 9 and the port of `cdp4_rst` ("read as a buried contact onto its node diffusion, not drawn"): drawn in `trace/cdp4.txt` (`cdp4` run 2) as that reading; AMB-038 is resolved as (a). The tongue, buried contact and diffusion (`D 7540,13905:7590,13940`) reach about 20 px into this region and overlap the end of the poly `P 7462,13906:7532,13927`. The `?M 7556,13895 y13953` is still not seen in either metal shot.
- The undrawn rows y 13744 and y 13852 end east of x 7550 as gates 2 and 4 of the NOR that makes `cdp4_rst` (ports `rsel13_buf_u` (7550,13751), `rsel12_buf_u` (7550,13873) in `ports.d/cdp4.txt`): draw the rows onto them.
- Piece `kb`: `bus_eq_r15`'s driver is `cdp4`'s comparator of the bus lines with R15 (`cdp4` run 3); the diffusion band east of (7600,11109) is its match line.
- Piece `lc9`, "row ... 14784 to (7835,14784)": the pad's contact is at (7837,14784) and the pad's poly reaches x 7863 (`eof`, piece `ck6`). The row is driven from the east: `lc3_w9947` = NOT `eof_w15127` (`eof` run 15), so the port at (7550,14784) is an input of this field.

## Corrections (coordinator, from the handoffs of 2026-11-20, `bl0`)

- "Where the buffered RES and LPSTB pins go" (the survey of run 7): the two metals from the pads
  (6363,15132) and (6408,15176) go to the gates G4 and G2 of `bl0`'s gate group as surveyed, and the third
  pad (6320,15088) is another net's (`bl0_w15088`). **The pins do not end there**: from each pad a poly row
  also runs east under the tracks to a pad ((6885,15130), (6929,15177)) and a track south to a pad
  ((6882,16170), (6928,16217)) (`notes/blocks/bl0.md`, piece `pe`).
- In the field's south-west corner two tracks are drawn by `bl0`, not by this package: x 4867 from a pad
  (4867,15675) north to a pad (4867,14436) (`lpstb_nres`, on west in poly along y 14436 into the left
  array), and nothing else. Seen there and not drawn: the track x 4909 from the pad (4909,15088) north
  (`bl0_w15088`; by the follower to about (4908,10660)).

## Corrections (coordinator, from the handoffs of 2026-11-20, third batch)

- The two corrections above that asked for work are done: the rows y 13744 and y 13852 are drawn onto `cdp4`'s ports (run 8), and the track x 4909 is drawn (run 9, piece `p2`: it is `rst_n`).
- The register: Ambiguity 13 is AMB-039, resolved as a plain crossing by run 8's rows; Ambiguity 15 is AMB-044 (new, assumed a plain crossing).
- The five `@alias` lines of runs 8 and 9 at the end of `trace/busl.txt` go at the next refresh, when the names they gather are renamed (the master list's `rename` row has the pairs).
