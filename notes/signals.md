# Signal names

Every named net in the trace is listed here, by name or by pattern. `tools/build.py`
checks this: a net name that no row of these tables covers is reported as
"not in notes/signals.md" in the build output and in `out/report.txt`.

In a pattern, `#` stands for a number and `*` for any run of letters, digits and
underscores. The first column of every table is read by the build, so keep each pattern
in backticks in the first column.

## Rules

1. **A signal is named for what it is** as soon as tracing shows what it is: pin names
   as on the datasheet (`e`, `rw`, `ma5`), register numbers (`r1_b3_q`, `wr_r6`), counter
   bits (`hc0`, `rc3_q`), results (`h_eq_r0`).
2. **A signal that is not identified is named for where it is**: a block prefix and a
   local name (`cdp3_h_c5_q`, `rcs_e4`). The table says what is known about it. When it
   is identified it is renamed everywhere with `tools/rename.py` (trace files, notes,
   floor plan) and its old name goes into "Former names" at the end of this file.
3. Suffixes: `_n` inverse (active low), `_q` output of a latch or register bit, `_b#` bit
   number (bit 0 = least significant), `_s#` slice number where the bit order is not
   established, `_dly` a delayed copy, `_buf` a buffered copy.
4. **`_u` marks an open join**: a piece of wire believed to be the same net as the name
   without the suffix, whose connection has not been drawn (`ck_a_u`). Every
   `_u` name is a task; the build lists them.
5. Rows and slices are places and keep their numbers in the notes ("row r18", "slice
   s3"); the tables below say which bit each one is.

## Where the bits are

Counters (mid-right array, rows r0-r18 from the top, `notes/blocks/mra.md`):

| Rows | Counter | Bit of row |
|---|---|---|
| r18 ... r11 | horizontal character counter, `hc0` ... `hc7` | r18 = bit 0 (carry enters there), r11 = bit 7 |
| r10 ... r4 | character row counter, `rc0` ... `rc6` | r10 = bit 0, r4 = bit 6 |
| r3 ... r0 | horizontal sync width counter, `hsw0` ... `hsw3` (4 bits, on the character clock; compared bit for bit with R3's nibble in the upper right datapath) | r3 = bit 0, r0 = bit 3 |

Counters in the left array's upper rows (rows u0-u8 from the top, `notes/blocks/ur.md`; the
same bit cell as the mid-right array's):

| Rows | Counter | Bit of row |
|---|---|---|
| u8 ... u4 | scan line counter, `sl0` ... `sl4` (5 bits; stepped by `lc_step`; compared bit for bit with R5) | u8 = bit 0 (the carry enters there from the left column), u4 = bit 4 |
| u3 ... u0 | 4-bit counter, `c4l0` ... `c4l3` (compared with R3 bits 4-7 in `amr`: believed the vertical sync width counter; same clocks as the scan line counter) | u3 = bit 0, u0 = bit 3 |

Right datapath, lower array (R0, R1, R2 and their comparators): slice s1 = bit 0, s2 =
bit 1, ... s7 = bit 6, **s0 = bit 7** (from the counter lines: `hc0` arrives at s1, `hc7`
at s0). Upper array (R4, R6, R7, R5 and their comparators): the slices that the notes of
`rdp2` call sm1, s0, s1, ... s5 (left to right) are **bits 0 to 6** (from the scan line
counter's lines at R5's comparator, `notes/blocks/rdp1.md`). R3's four slices (t0-t3 in
the first notes) are bits 0-3 of that nibble.

Central datapath (registers identified by their write strobes, `notes/blocks/wrs.md`):

| Rows | Register | Slices |
|---|---|---|
| `cdp1` row A | R8 (6 bits) | columns c2-c7 (cells a0-a5). Bit order from the data bus (`notes/blocks/bust.md`): slices 5, 4, 1, 0, 3, 2 are bits 0, 1, 4, 5, 6, 7 (`r8_b#_*`); bits 0 and 1 are the two whose AND is `ras_shift` |
| `cdp1` row C, comparator row B | R9 (5 bits) | slices 1-5 = columns c3-c7; slice k = bit 5 - k, from the data bus (`r9_b#_*`) |
| `cdp2` row A | R11 (5 bits) | s3-s7 |
| `cdp2` row C, comparator rows B | R10 (7 bits) | s1-s7; s3-s7 compared, s7 = bit 0 ... s3 = bit 4 (from the `rax_o#` lines); s1, s2 the two mode bits |

## Supplies, pins and pad circuits

| Name | What it is |
|---|---|
| `vcc`, `vss` | supplies |
| `clk`, `e`, `rw`, `rs`, `cs`, `res`, `lpstb` | the pin itself (pad node) |
| `cs_p`, `e_p`, `rs_p`, `rw_p` | the pin's node behind its protection strip, at the input of its buffer |
| `clk_n`, `clk_b` | NOT CLK and CLK buffered (input row; `clk_b` feeds the phase generator) |
| `e_n`, `e_b` | NOT E and E buffered. `e_b` is the E that the bus control logic uses |
| `rw_a`, `rw_b`, `rw_c`, `rw_d`, `rs_a`, `rs_b`, `rs_c`, `rs_d`, `cs_a`, `cs_b`, `cs_c`, `cs_d` | the four inverters of each input chain: `_a` and `_c` inverted, `_b` and `_d` true. The core uses `_d` |
| `res_n`, `res_b` | NOT RES and RES buffered. `res_b` runs down the top-left logic to line 3 of the poly bus at x 5100-5290 |
| `lpstb_n`, `lpstb_b` | the same for LPSTB; `lpstb_b` ends on line 4 of that bus |
| `ma#`, `ra#`, `hsync`, `vsync`, `disptmg`, `cudisp` | output pins (pad node) |
| `*_drv_in` | the signal from the core that an output pad cell receives (the pad is its inverse) |
| `*_pu`, `*_pd` | inside an output pad cell: gate of the pull-up fingers (first inverter) and of the pull-down fingers (second inverter) |
| `d#_in` | data pin D# behind its protection, at its input buffer. With the pad's series strip drawn it is the pad's own net: an alias of `d#` (`trace/dpad.txt`) |
| `d#` | data pins D0-D7: the bond pad, the metal of the output fingers, and (D0-D6) the series strip, the protection node and the line to the input buffer. On the chip the strip is a diffused resistor between pad and node; the netlist has one net (`notes/blocks/dpad.md`) |
| `d_hiz` | output disable of the data pins, one line common to the eight pad cells (metal x 17631-17651, y 7374-18850, a contact in each cell): high turns off both output gates of every data pad. Driven from the bus-interface column; the driver is not traced. The "P_x" of the first notes |
| `d#_out_n` | the per-bit data line into data pad cell #, from the bus-interface column: while `d_hiz` is low the pin D# is its inverse. The "P_y" of the first notes. `d0_out_n` is the thin metal x 17438-17459 down the whole column, driven by an inverter at its foot (y 16415-16590); `d1_out_n` is drawn from D1's pad cell to the column's west edge at (16950,16344), driver not found |
| `d#_pu`, `d#_pd` | inside data pad cell #: gate of the pull-up fingers, NOR(`d_hiz`, `d#_out_n`), and gate of the pull-down fingers, NOR(`d_hiz`, `d#_pu`) |
| `d#_a`, `d#_b`, `d#_c`, `d#_d` | the four inverters of data input buffer #: `_a`, `_c` inverted, `_b`, `_d` true. Buffers 0-5 are cell `dbus_in`, 6 and 7 cell `dbus_in2` (`notes/blocks/dbus.md`). `d#_d` feeds the input latch: in the data bus column for bits 0-3; `d4_d`..`d7_d` leave it west at x 16950 and enter the latches of bits 4-7 in the column x 16466-16848 (`notes/blocks/dlat.md`) |
| `dbus_do0_in` | input of the inverter at the foot of the data bus column that drives `d0_out_n` (`d0_out_n` = NOT `dbus_do0_in`): a poly along y 16444-16463 from a pad (16993,16451), fed by a metal that leaves the column west at (16950,16712), not followed. The bit the chip puts on D0, in true sense |
| `dbus_cap#b` | # = 0-5: a plain diffusion rectangle beside data input buffer # with a contact that carries only a dot of metal, joined to nothing. The capacitor that a metal strap would have put on `d#_b` (whose pad nearby also has only a dot): a metal option not taken (`notes/blocks/dbus.md`, "The capacitor taps of chains 1-5") |
| `d#_d_n` | NOT `d#_d`: the inverter inside data input latch # (`notes/blocks/dbus.md`; bits 4-7: `notes/blocks/dlat.md`) |
| `dl#_q`, `dl#_q_n` | the data input latch of bit # in the data bus column: two cross-coupled AND-OR-invert gates, transparent while `dbus_le` is high. `dl#_q` follows pin D#; `db_b#` = NOT `dl#_q_n` (a static inverter drives the bus bit). Bits 4-7 are the same latch in the column west of it (cell `dlat_lat`), and their `dl#_q_n` run west and north to four inverters above the latches (cell `dlat_drv`) that drive `db_b4`..`db_b7` (`notes/blocks/dlat.md`); `areg_w6` and `areg_w7` are `dl7_q_n` and `dl6_q_n` (aliases in `trace/dlat.txt`) |
| `dbus_le` | enable of the data input latches: a vertical metal x 17243-17262 down the data bus column from y 8988 (to y 13614, then west); west of x 16950 it is the metal that runs south along x 16819 past the latches of bits 4-7 (a pad on each of their two gate bands) then turns west at y 15802 and runs on south along x 16774, out of that column, passing over the box ends of `d5_out_n`, `d4_out_n` and `d3_out_n` without contact (`notes/blocks/dlat.md`; followed to y 16104). Source not traced |

## Clocks

| Name | What it is |
|---|---|
| `ck_a` | phase high only while CLK is low (non-overlapping with `ck_b`). Slave clock of the horizontal and 4-bit counters |
| `ck_b` | phase high only while CLK is high. Master clock of the horizontal and 4-bit counters. Held low while `inh_ck` is high |
| `ck_a_u` | the line that gates the second pull-down of the horizontal counter's `_nx_g` nodes: followed in poly to the `ck_a` bus line of the clock block; join not drawn |
| `ck_out` | NOT CLK from the big three-stage buffer: the main internal clock, distributed along the bottom and left edges |
| `clk_tl` | NOT `ck_out`, i.e. CLK polarity, for the top-left logic: made by an inverter at (2626,7908) in the left column beside upper row 2 of the left array, where the left-edge trunk of `ck_out` arrives, and run back north (thin metal x 2457, poly y 5587, bus lines D and B). In the step logic it samples `rcs_cond` into `rcs_cond_lat`, enables the first term of `rcs_n4200`, and gates units at y 3765 and y 4410 |
| `ck_a_pu`, `ck_b_pu` | gates of the source-follower pull-ups of the two phase drivers |
| `ck_g#` | outputs of the clock gate row: `ck_g1`, `ck_g2` = `ck_b` delayed by one and two inverters, `ck_g3`, `ck_g4` = the same for `ck_a` |
| `ck_clkn` | NOT `clk_b` inside the phase generator |
| `ck_t`, `ck_n#`, `ck_ga` | internal nodes of the main clock buffer (first stage output, second stage output, gate of the output pull-up) |

## The inhibit signal

One core signal stops both the horizontal counter's master clock and the row counter's
step. Its source is not traced. It is a line of the bottom bus field with at least four
branches (followed 2026-11-16 from the strobe channel 3,700 px west, `notes/blocks/trunks.md`).
All five names below are copies of it.

| Name | What it is |
|---|---|
| `inh_src` | the signal itself: a bottom-bus line that reaches the gate of the driver of `inh_n`, a metal north along x 10225, a poly east into the bottom-centre logic at (10470,16950) and the bus further west than x 8978; source unknown |
| `inh_n` | NOT `inh_src`: "line X" of the notes. Input of the lone inverter in the input buffer row |
| `inh_ck` | NOT `inh_n` from that inverter: holds `ck_b` low in the clock block, and is distributed along the bottom bus field and up the left bus field ("S" in the notes) |
| `inh_rc` | NOT `inh_n` from the upper inverter in the strobe channel: runs up the wiring channel, over the top of the counters, to the row counter's step gate (`rc_step` = NOR(`inh_rc`, `rc_stepreq_n`)) |
| `inh_lat` | NOT `inh_n` from the lower inverter: gates the latch in the strobe channel's gate column |

## Counters

For `<bit>` read `hc#` (horizontal), `rc#` (character row), `hsw#` (horizontal sync
width), `sl#` (scan line) or `c4l#` (the left array's 4-bit counter, compared with R3 bits 4-7 in `amr`: believed the
vertical sync width counter). Each
bit is a master-slave pair (`notes/blocks/mra.md`; the node letters used there are given
in brackets).

| Name | What it is |
|---|---|
| `hc#`, `rc#`, `hsw#`, `sl#`, `c4l#` | the bit as the rest of the chip sees it: the buffered **master** (node n1). The comparators compare this, not the slave |
| `hc#_q`, `rc#_q`, `hsw#_q`, `sl#_q`, `c4l#_q` | slave latch (q): takes `_d` on the slave clock |
| `*_q_n` | NOT `_q` (g1) |
| `*_m` | master latch node (a): takes `_nx_g` on the master clock |
| `*_mb` | node b, joined to `_m` through a pass transistor gated by `cnt_gab`; gate of the feedback device from `_d` to `_m` |
| `*_m_n` | NOT `_m` (p3) |
| `*_d` | NOT `_m_n`: the copy of the master that the slave gate passes to `_q` (d) |
| `*_nx` | next-value node of the bit (m): pulled low through networks of the carry and `_q`; its pull-up and one branch are not resolved, so the next-state function is not extracted |
| `*_nx_n` | NOT `_nx` (nb) |
| `*_nx_g` | NOR(L3 line, `_nx_n`) (na): the next value, forced low while the counter's L3 line is high |
| `*_ci_n` | NOT carry-in of the bit (n2) |
| `*_co` | carry out of the bit = carry-in AND `_q` (x); carry-in of the next row up |
| `*_tab` | a diffusion tab pulled low by `_q_n` (spare finger); in rows r7-r10 and r15-r18 it is on the look-ahead line |
| `*_rb` | lower part of the diffusion R in the `_nx` network; its continuation is not resolved |
| `*_z` | far side of the weak always-on device from `_q`; ends as a free stub as traced (re-read item R9) |
| `*_md`, `*_mt` | metal straps between a row and its neighbour in the chain column (lower, upper); their joins are in `notes/blocks/mra.md` |
| `hc_ci`, `rc_ci`, `hsw_ci` | carry-in of each counter's bit 0. Sources not traced |
| `hc_lo4_set`, `rc_lo4_set` | look-ahead line: low while any of bits 0-3 is clear, i.e. high when `_q` of bits 0-3 are all 1 (group lines B and A) |
| `rc_ck_m`, `rc_ck_s` | master and slave clock of the row counter (bus lines E and D), made by the generator below |
| `rc_l3`, `hsw_l3` | the L3 line of the row counter (from the west along y 13005) and of the 4-bit counter (from the north). What they carry is not known; for the horizontal counter L3 is `ck_a` |
| `lc_ck_m`, `lc_ck_s` | master clock (line L1) and slave clock (rail x 4218) of both counters of the left array's upper rows: one line each through all nine rows. Made by a second copy of the row counter's clock generator, in the left column beside rows u0-u2: `lc_ck_s` = NOR(`lc_ck_m_dly`, `lc_step`), `lc_ck_m` = NOR(`lc_step_n`, `lc_ck_s_dly`) |
| `lc_step`, `lc_step_n` | the step pulse of those two counters and its inverse: both counters step once per pulse. `lc_step` comes from the left-centre logic (poly up x 5012, west along y 6368 over the counters, metal down x 2412); its gate is not traced |
| `lc_ck_m_n`, `lc_ck_m_dly`, `lc_ck_s_n`, `lc_ck_s_dly` | inverse and two-inverter delay of each of the two clocks, inside that generator |
| `c4l_l3`, `sl_l3` | the L3 lines of those two counters: the 4-bit one's comes from the north; the 5-bit one's from a poly along y 6410 (from the west, and from a metal from the north at x 3968) |
| `c4l_gab`, `sl_gab` | their pass-gate lines: the 4-bit one's comes from the north; the 5-bit one's from a poly from the east along y 6520, ending on a contact at (4087,11005) |
| `cnt_gab` | gate line of the `_m` to `_mb` pass transistors of all 19 bits (x 12902), fed from the top by band H4. **Also** the line y 4354 through the five `ral` cells, where it gates one of the two pull-downs of each cell's NOR (`ral_n1_s#` = NOR(`ral_a_s#`, `cnt_gab`)), so a high level sets that RA output high; the cells only read it: from `wl`'s contact (11392,7210) on H4 north along x 11396 / 11242, through the cross-under at x 11243-11694, east along y 4287 and a poly L into the band (`trace/ral.txt`, firm). Source not traced |
| `cnt_l2_a`, `cnt_l2_b`, `cnt_l2_c` | three pieces of the metal line L2 that passes through the rows without a contact |
| `cnt_la_a`, `cnt_la_b`, `cnt_la_c` | three pieces of the metal x 12285 through the rows; no contact found in the rows (re-read item R8). `cnt_la_a` feeds an inverter west of the counters |
| `cnt_la_a_n` | NOT `cnt_la_a`; leaves north |
| `cnt_bus_a`, `cnt_bus_b` | bus lines A and B of the channel between rows r3 and r4; not identified. B runs from the datapath channel 3 to the upper right datapath |

## Row address selector (`notes/blocks/ras.md`)

Eleven pass transistors between the scan line counter and five output nodes.

| Name | What it is |
|---|---|
| `ras_o#` | output bit # of the selector (# = 0-4). Expected to be the row address that goes to pin RA#; not yet followed to the pad |
| `ras_straight` | NOT `ras_shift` (made in the island `tc1`): gate line (left poly band) of the five pass transistors `sl`# to `ras_o`# |
| `ras_shift`, `ras_shift_n` | the mode line and its inverse: `ras_shift` = `r8_b1_q` AND `r8_b0_q`, R8's bits 1 and 0 (the interlace field: both set = interlace sync and video), made by a NAND and an inverter below R8's row (`notes/blocks/shm.md`). Gate line (right poly band) of the four pass transistors `sl`# to `ras_o`(#+1), and input of the island `tc1` |
| `ras_o0_alt1`, `ras_o0_alt2` | the two sources of `ras_o0` when `ras_shift` is high: `alt1` when R9's bit 0 is set, `alt2` when it is clear. `ras_o0_alt1` = `rc0_n` XOR `fld_y_b` (`notes/blocks/fld.md`). `alt2` runs from its pad (6928,4786) on a poly row west through the crossing field to a pad (6447,4786) and on west in metal past x 6400 (`notes/blocks/tc2.md`); not followed further (follower: end (6059,4876)) |
| `ras_o0_sel1`, `ras_o0_sel2` | made in the island `tc1`: `sel1` = `ras_shift` AND R9 bit 0, `sel2` = `ras_shift` AND NOT R9 bit 0. Gates of the pass transistors from `ras_o0_alt1` and `ras_o0_alt2` to `ras_o0`, and of the island's own AND-OR |
| `rax_o#` | output of the unit that takes selector output `ras_o`# (# = 0-4): pulled to VSS by a transistor gated by `ras_o`#; with the unit's load (`trace/tc2.txt`, piece 8: gate tied to the output, on the VCC rail x 8117-8163) NOT `ras_o`#, the complement of the row address (AMB-011). Each runs from its unit's pad at x 7836 through the nest of metals, along a line of the central datapath's channel 1 (the comparator's through track: `cdp2_trk_s7` is `rax_o0` ... `cdp2_trk_s4` is `rax_o3`), north along x 10981-11154, under the supply metal at y 4331-4500 and east to the logic in front of the RA pad drivers (`notes/blocks/rab.md`) |

## Row counter clock generator and step

| Name | What it is |
|---|---|
| `rc_stepreq_n` | request to step the row counter, active low. Made by a three-input NOR in the top-left logic |
| `rc_step` | NOR(`inh_rc`, `rc_stepreq_n`): the step pulse. The row counter's masters load while it is high |
| `rc_step_n` | NOT `rc_step` |
| `rc_ck_m_n`, `rc_ck_m_dly` | NOT `rc_ck_m`, and `rc_ck_m` delayed by two inverters; `rc_ck_s` = NOR(`rc_ck_m_dly`, `rc_step`) |
| `rc_ck_s_n`, `rc_ck_s_dly` | the same for `rc_ck_s`; `rc_ck_m` = NOR(`rc_step_n`, `rc_ck_s_dly`) |
| `rcs_in1`, `rcs_in2`, `rcs_in3` | the three inputs of the NOR that makes `rc_stepreq_n`. `rcs_in2` = NOR(`rcs_w2`, `rcs_e4`), `rcs_in3` = NOR(`rcs_e3`, `rcs_e4`). `rcs_in1` not identified: from the bus field at x 4279 |
| `rcs_w2`, `rcs_c1`, `rcs_b1` | `rcs_w2` = NOT `rcs_c1`; `rcs_c1` = NOR(`rcs_a2`, `rcs_b1`); `rcs_b1` = NOR(`rcs_x1`, `rcs_a2`, `rcs_u3425`) |
| `rcs_cond_n` | NOR(`rcs_in2`, `rcs_in3`) = `rcs_e4` OR (`rcs_e3` AND `rcs_a2`): the step condition inverted (called m2 in the block notes) |
| `rcs_cond` | NOT `rcs_cond_n`: the row counter's step condition apart from `rcs_in1`. On bus line A's piece A3; first gate of the series pair in `rcs_n4200` |
| `rcs_cond_lat` | `rcs_cond` sampled through a pass transistor while `clk_tl` is high (a dynamic latch on a metal and two poly pads); its poly goes west under the rail at y 4010-4030, not followed |
| `rcs_e3`, `rcs_e4`, `rcs_a2`, `rcs_x1` | inputs of the step logic, **not identified**. `rcs_e4` gates everything except `rcs_in1`; it is a long control line (17,000 px, five gate loads) that runs beside `res_b` and `lpstb_b`. Its driver is in the west column of the first cluster: `rcs_e4` = NOR(`tl1_w4678`, `tl1_w4937`), at (2607,4890) (`notes/blocks/tl1.md`); `tl1_w4678` is the output of two latches in series (open on `tl1_w3594` low-and-`tl1_w3678`-low, then on `tl1_w3594` high; data `tl1_w2857`; cleared by `tl1_w4025`) |
| `rcs_u#` | output of a unit of the step logic cluster that has no better name yet, by the y of its buried contact (`rcs_u3288` = NOR(`rcs_g3245`, `rcs_bd3330`); `rcs_u3425` = NOT `rcs_bc3460` = `rcs_e3` OR `rcs_e4`, third input of `rcs_b1`) |
| `rcs_n#` | output of an AND-OR-INVERT unit of the first cluster (`rcs_n4200` = NOT(`rcs_cond` AND `clk_tl` OR `rcs_g4240`)); leaves on a metal strap x 2845-2885 |
| `rcs_iso#` | a gate poly of the first cluster on which no connection has been found, by its x. `rcs_iso2958`: a vertical poly x 2950-2968, y 3447-3547, under the west edge of the VSS rail R3, gate of a second transistor from `rcs_u3425` to VSS (its diffusion link is drawn uncertain). If the rail contacts it, the transistor is always off |
| `rcs_g#` | an input of the cluster that arrives on a poly line from outside, by the y of that line |
| `rcs_ba#`, `rcs_bb#`, `rcs_bc#`, `rcs_bd#`, `rcs_be#`, `rcs_bf#`, `rcs_bg#` | a piece of bus line A-G beside the first cluster (x 3090-3380) whose driver is not yet known, by the y of its top end |
| `rcs_bp#`, `rcs_bq#`, `rcs_br#`, `rcs_bs#`, `rcs_bt#`, `rcs_bu#`, `rcs_bv#` | the same for the second bus field (x 4140-4420; tracks P-V at x 4148, 4192, 4235, 4279, 4322, 4365, 4409) |
| `amr_oa_c#`, `amr_ob_c#` | the two vertical metals of `amr`'s slice in column # (c1 x 11880, c2 12270, c3 12660; c0's two are drawn in `trace/bust.txt` and carry the bus names `db_b4` / `c4l0`), named before the slice was traced. Inner (`oa`, x 11916 + 390(#-1)): **a data bus bit** (bits 5, 6, 7), written into R3 bits 5-7 on `wr_r3`. Outer (`ob`, x 12001 + ...): **an input**, the bit that R3's bit is compared with (aliases of `c4l1`, `cdp1_l4632`; c3's is `cdp1_l4676`, which west of `cdp1` is fed from the row y 4635, not `ra_eq_r9`: `notes/blocks/r9m.md`, correction). To bus lines y 5047/5135/5177 and 4657/4696/4742 (`notes/blocks/amr.md`) |
| `r9m_l3` | the bundle's line 3: track P's lower piece (x 4148, y 3371-3596, contact (4148,3588) with a poly west into the middle cluster), the stub at y 3376, metal up x 4194, west along y 2641 / 2599, the pad (4912,2641), a poly stepping down to the pad (5405,2681), metal along y 2685 and down x 5848 to (5845,5045). Driver not found |
| `r9m_l1w` | the metal from the pad (5400,2596) (whose poly goes north at x 5175, not followed) east along y 2599, down x 6022, across the crossing field to the pad (7855,4676) and the row y 4676, which turns south near x 8190 at `cdp1`'s west edge |
| `rcs_mu`, `rcs_mv` | the two inputs of the NOR that makes `rcs_in1` (middle cluster): bus pieces of the second bus field (x 4192). `rcs_mu` = NOT `ra_eq_r9` (an inverter at y 3413); `rcs_mv` comes from a poly that leaves the bus field east and south at (4283,4745) |
| `rcs_mn#` | output of a unit of the middle cluster, by the y of its output (`rcs_mn3852` = NOR(?, `rcs_in1`)) |
| `rcs_thin_e` | thin metal E of the first cluster (x 2903-2923, y 2986-5400 and on south to about y 6036), over the east loads. Its north end is found: west along y 2986, north at x 2696 to a contact (2695,2768), poly west along y 2768, contact (2326,2768), metal x 2326 south to contacts (2326,3243) and (2326,3333). There it is the **select** of the mux unit `tla_w3417` and the input of the inverter `tla_w3505`. Its driver is not found (its south end, in the small cluster below, is not read) |
| `rcs_thin_w` | the piece of thin metal W (x 2688-2708) drawn at y 4940-5330, over the west loads of the first cluster; what it joins is not read, and it is not shown to be one metal with the upper piece (`rcs_u3288_n`, which follow.py ends at y 4002) |
| `rcs_u3288_n` | NOT `rcs_u3288`: output of the inverter at the top of the west column of the first cluster (rail gate under R1 at (2626,3112), strong load), carried by the upper piece of thin metal W (contact (2738,3027), x 2696, y 3026-4000). Its loads are not traced (contact candidates at y 3690-3949) |
| `tl1_w#` | a wire of the westmost strip of the top-left logic (`notes/blocks/tl1.md`), by the y of its defining contact or poly row. `tl1_w3636` = NOR(`tl1_w3594`, `tl1_w3678`) (unit at y 3558-3742, output on the metal x 2283 to gates of the two units below); `tl1_w4243` = NOT `tl1_w4287` (inverter at y 4215-4345; the first latch's output and the second latch's data); `tl1_w4678` (= NOT(`tl1_w4025` OR `tl1_w3594` AND `tl1_w4360` OR `tl1_w4703`), the unit at y 4590-4800; a buried contact puts it on a poly L to the NOR) and `tl1_w4937` (metal x 2370 from the row y 5460 under the foot, which comes from the east) are the two inputs of the NOR that drives `rcs_e4`; `tl1_w2857`, `tl1_w3678`, `tl1_w3594` enter on the poly rows y 2857, 2812, 2899 from the east; `tl1_w4025` is the metal x 2457 (y 4012-5372) with the row y 5372 under the foot, and the gate of one pull-down in each of the units at y 3982 and y 4590; `tl1_w4070` = NOT(`tl1_w4025` OR `tl1_w3636` AND `tl1_w3752` OR `tl1_w4287`) is the unit at y 3982-4215, a copy of the one at y 4590, and with `tl1_w4287` = NOT(`tl1_w2857` AND `tl1_w3636` OR `tl1_w4070`) (y 3732-3982) the first latch; `tl1_w4360` = NOT `tl1_w4243` and `tl1_w3752` = NOT `tl1_w2857` are the south and north pieces of the thin metal x 2557-2573 over the west column, each from the output of the inverter of the unit above (y 4345 and y 3737) to the second series gate of the unit below; `tl1_w4703` (= NOT(`tl1_w4243` AND `tl1_w3594` OR `tl1_w4678`), the other side of the second latch) and `tl1_w4095` are the two pieces of the thin metal x 2742, each from the load plate of the three-input gate of the unit above (y 4487 and y 3879) to the gate of the third pull-down of the unit below; `tl1_w4095` is an alias of `tl1_w4287` (one net through the `?` tie of that plate: an assumption); the west column of the small cluster (y 5690-6175) is a third latch of the same build (a second copy of the two units), open while `ck_out` is high: `tl1_w5706` = NOT `tl1_w3333` (the thin metal x 2557-2573, y 5697-6120), `tl1_w5841` = NOT(`tl1_w3333` AND `ck_out` OR `tl1_w6022`) (the thin metal x 2742, y 5829-6059), `tl1_w6022` = NOT(`tl1_w5978` OR `ck_out` AND `tl1_w5706` OR `tl1_w5841`) (the latch's output: metal x 2414 and the row y 6195 east out of the strip); `tl1_w5978` (pad (2326,5978), metal x 2326 on south) is its clear; `tl1_w3333`, its data, is a 4,700 px wire from a pad (2563,2550) at the top, by metal to (2197,3333) and by poly down the west side to the row y 5800; `tl1_w5936` only passes (a poly from the pad-ring side along y 5935, the metal x 2500, the row y 6237 east out of the strip); north of y 2790 only wiring: `tl1_w3333` leaves east by a metal from the pad (2826,2553), `tl1_w3678` by a metal from the pad (2830,2811); `tl1_w2637` and `tl1_w2592` are polys from the north (x 2455, x 2500) that turn into the rows y 2636 (to a pad (2827,2637) and a metal east) and y 2591 (east); `tl1_w2506` is a poly along the strip's north edge (y 2506) that turns north at x 2380, with no contact in the strip. None identified |
| `tl2_w#` | a wire of the second strip of the top-left logic (`notes/blocks/tl2.md`), by the y of its defining strip or row. `tl2_w6070` = NOT `tl1_w6022`: the node between the two inverters of the small cluster's east half (drain strip y 6064-6084, buried contact (3053,6067), and the poly loop that is the gate of the inverter driving `tl1_w5936`) |
| `tl3_w#` | a wire of the third strip of the top-left logic, the middle cluster's west column (`notes/blocks/tl3.md`), by the y of its row or contact. The latch at y 3212-3652 (copies of `tl1_ua`, `tl1_ub`): `tl3_w3233` = NOT `tl3_w3333`; `tl3_w3419` = NOT(`tl3_w3333` AND `tl3_w3373` OR `tl3_w3550`); `tl3_w3550` = NOT(`tl3_w3506` OR `tl3_w3373` AND `tl3_w3233` OR `tl3_w3419`): open while `tl3_w3373` is high, data `tl3_w3333`, cleared by `tl3_w3506`; `tl3_w3419` (the inverted output) leaves west. NOR units below it: `tl3_w3765` = NOR(`tl3_w3722`, `tl3_w3803`), `tl3_w3939` = NOR(`tl3_w3896`, `tl3_w3982`), `tl3_w4720` = NOR(`tl3_w3803`, `tl3_w4763`) (its output goes to the data row of the unit below). `tl3_w3368` is the thin metal x 3783 inside the latch, aliased to `tl3_w3419` across a `?` tie. None identified |
| `tl4_w#` | a wire of the fourth strip of the top-left logic, the vertical control's right cluster (`notes/blocks/tl4.md`), by the y of its defining row or pad. A latch at y 3906-4390, a copy of `tl1`'s: `tl4_w4025` data (row y 4025, metal x 4452), `tl4_w4068` enable (metal x 4625), `tl4_w4198` clear (metal x 4537), `tl4_w3928` = NOT `tl4_w4025`, `tl4_w4113` = NOT(`tl4_w4025` AND `tl4_w4068` OR `tl4_w4243`), `tl4_w4243` = NOT(`tl4_w4198` OR `tl4_w4068` AND `tl4_w3928` OR `tl4_w4113`): the output, on the metal x 4494 south. Above it `tl4_w3113` = NOR(`tl4_w3070`, `tl4_w3178`) (unit at y 3012-3222, output north on the metal x 4408) and `tl4_w3808` = NOT `tl4_w3850` (inverter at y 3781-3911, output north on the metal x 4496). Sources and destinations not followed |
| `tla_w#` | a line of the west column of the first cluster (under rail R1, x 2558-2693), by the y at which its poly crosses the rail. `tla_w3417` = NOT(`rcs_thin_e` AND `tla_w3376` OR `tla_w3505` AND `amr_eq_r3`): the output of a two-way selector (inverting), leaving by the metal x 2326, the poly y 5543 east along the cluster's foot to (4408,5545), track V of the second bus field north to (4410,4460) and a poly east along y 4461 towards the right cluster. `tla_w3505` = NOT `rcs_thin_e`. `tla_w3376`: input, from the small cluster below (metal x 2199, poly y 5500, metal x 2870 south from (2870,5502)). `amr_eq_r3`: input, from the metal x 2239 whose south end (2239,5632) is on a poly that leaves east along y 5632; believed to be the vertical sync width match `amr_eq_r3` (an unmerged branch follows that line from `amr`; not joined here) |
| `rc0_n` | NOT `rc0`: output of the inverter I2 west of the counters, whose input was traced to the row counter's bit 0 on 2026-11-16 (its two nets had place names until then: see Former names). One input of the XOR that makes `ras_o0_alt1` |
| `wl_h#` | horizontal poly bands H0 and H1 above the counters; not identified |

## Registers, comparators and their results

| Name | What it is |
|---|---|
| `rsel#` | select line of register # from the address decode (high when the address register holds #) |
| `rsel#_n` | NOT `rsel#` |
| `rsel#_bn`, `rsel#_buf`, `rsel#_bufn` | buffer of a select line: first inverter and output (`rsel12_bufn` is the first inverter of R12's separately built buffer) |
| `wr_stb_n` | common write strobe, active low |
| `wr_r#` | write strobe of register #: `rsel#` AND NOT `wr_stb_n` |
| `wr_r#_u` | the load strobe line at the register's latch row, where its join to `wr_r#` is not drawn |
| `r#_b#_a`, `r#_b#_n2`, `r#_b#_q` | register R#, bit #: storage node (loaded from the bus while the strobe is high), its inverse, and the output (= the stored bit) |
| `r#_b#_m#` | the metal straps of a register bit cell (in `cdp1`'s rows: `_m3`, `_m6`; `_m6` is also the output `_q` in row C) |
| `r#c_b#_nor`, `r#c_b#_x` | comparator of R#, bit #: NOR(counter bit, register bit), and x = counter bit XOR register bit |
| `r#hc_s#_nor`, `r#hc_s#_x` | comparator of the horizontal counter against R0 shifted one place (R0/2), by slice |
| `sl_eq_r#` | high when the scan line counter equals R5 (vertical total adjust). Leaves the comparator northwards; not followed |
| `amr_eq_r#` | high when the 4-bit counter `c4l0`..`c4l3` (on the lines `c4l0`..`cdp1_l4676`) equals R3 bits 4-7: the wired NOR of `r3c_b4_x` ... `r3c_b7_x` on a diffusion line y 6246-6272 through `amr`'s four slices, load in the first column. It leaves through a buried contact at c0 and runs west to a gate in `tla`'s first cluster (`notes/blocks/amr.md`). Named for the block until its use is traced |
| `hsw_eq_r#` | high when the horizontal sync width counter equals R3's nibble (the end of HSYNC). Not followed |
| `h_eq_r#` | high when the horizontal counter equals R# (R0: end of line; R1: displayed width; R2: sync position) |
| `h_eq_r#half` | high when the horizontal counter equals R0/2 |
| `h_eq_r#_u` | a piece believed to be `h_eq_r#` whose join is not drawn (tracks k7, k8 of the strobe channel) |
| `rc_eq_r#` | high when the row counter `rc` (its seven lines through the upper right array, joined by `ucz`) equals R4 (vertical total), R6 (vertical displayed) or R7 (vertical sync position). `rc_eq_r6` goes down the wiring channel to the strobe channel (its track k4); `rc_eq_r7` leaves west along y 6820 |
| `hc#_u` | the horizontal counter line at the comparators, where its join to `hc#` is not drawn |
| `db_b#` | **the internal data bus, bit #** (0-7). One net per bit across the chip: the right datapath's data lines (formerly `ubus_b#` in the upper array and `rbus_b#` in the lower one), the central datapath's bit lines (`notes/blocks/bust.md`), R3's data lines, `amr`'s inner lines. It writes R0-R11 by the register widths of the datasheet (`tools/bust_fanout.py`). The bit numbers rest on the counters' carry direction (the comparators) and on that fan-out; bits 0 and 1 also end in the D0 and D1 units of `dbus` (`notes/blocks/dbl.md`). Bits 0-3 are driven onto the bus by the input latches of pins D0-D3 in the data bus column (`dbus`: `db_b#` = NOT `dl#_q_n`), bits 4-7 the same way by the latches and inverters of `dlat` (`notes/blocks/dlat.md`). Bits 0-4 continue to R10 and R11 only through `?M` (AMB-019): the names `cdp2_a_s#_bus`, `cdp2_c_s#_bus` stay aliases there |
| `ar#`, `ar#_n` | address register bit # and its inverse (rows of the decode array) |
| `ar#_a`, `ar#_n2`, `ar#_q`, `ar#_trk` | nodes of address register bit #: storage node, its inverse, output, and the track that takes it to the decode |
| `ar_load`, `ar_load_n` | load strobe of the address register and its inverse |
| `areg_w#` | lines 6 and 7 of the bundle beside the address row inverters; not identified |

## Bus control

| Name | What it is |
|---|---|
| `wr_data_sel` | NOR(`rw_d`, `bd2_rs_n`, `cs_d`): a write to the data register is addressed |
| `wr_data_sel_n` | NOT `wr_data_sel` |
| `wr_data_lat`, `wr_data_lat_n` | transparent latch of `wr_data_sel`, open while `e_b` is high |
| `wr_data_e_n` | NOT(`wr_data_sel` AND `e_b`) |
| `wr_addr_sel` | NOR(`rw_d`, `rs_d`, `cs_d`): a write to the address register is addressed |
| `bd2_rs_n` | believed NOT `rs_d` (its gate is not fully traced) |
| `bd2_x` | second term of the address register load, from the untraced right-hand column |

## Strobe channel gate column (`notes/blocks/bd1.md`)

| Name | What it is |
|---|---|
| `bd1_k#` | tracks of the channel not yet identified (`rc_eq_r6`, `hc1`) |
| `bd1_a`, `bd1_an` | input and output of inverter A |
| `bd1_n#`, `bd1_q`, `bd1_k` | nodes of the latch gated by `inh_lat` (upper half node, lower half node, output, and the node pulled low by `inh_src`'s line) |

## Central datapath (`notes/blocks/cdp1.md` ... `cdp4.md`)

None of these rows has a register number yet, so all names are by place. Columns are
`c#`, slices `s#`, counted from the left.

| Name | What it is |
|---|---|
| `r8_b#_*`, `r9_b#_*` | R8 (cdp1 row A) and R9 (cdp1 row C), static register bit cell `cdp1_reg`: `_a` storage node (the bit line while the write line is high), `_n2` its inverse, `_q` output, `_m#` metal straps. Bit order from the data bus (`notes/blocks/bust.md`): R8 slices 5, 4, 1, 0, 3, 2 = bits 0, 1, 4, 5, 6, 7; R9 slice k = bit 5 - k. Renamed from `cdp1_a#_*`, `cdp1_c#_*` (former names) |
| `wr_r8`, `wr_r9` | the write strobes of R8 and R9, which are the write lines of rows A and C: **row A is R8, row C is R9** (`notes/blocks/wrs.md`) |
| `cdp1_b5_a` | the register-side input of R9's comparator in slice 5 (bit 0): not the register bit but the output of the island `tc1` |
| `ra#_cmp` | the row-address-side input of R9's comparator for bit # (# = 0-4): output of a unit near the right edge whose pull-down is gated by `ra#_drv_in`; with the unit's load (traced in `trace/dbus.txt`, cell `dbus_r9l`), NOT `ra#_drv_in`, the level of pin RA# (AMB-012, resolved but for `r9c`'s `?B` ties; `notes/blocks/r9c.md`). The comparator cell's own name for the same net, `cdp1_b#_b` with # = 5 minus the bit, is kept as an alias |
| `ra#_drv_in_u` | (# = 4) the input of r9c's RA4 unit, aliased to `ra4_drv_in` (`trace/rad.txt`) through r9c's `?P`. RA2's and RA3's were renamed when the joins through `ral` came out firm |
| `ral_stb` | the strobe of the `ral` cells' input pass transistors (metal y 4548 under the band). Followed back and drawn (`trace/ral.txt`): north along x 13862, west along y 4245 (the sixth line of rab's bundle), a cross-under at x 11150-11650, north along x 11068, west along y 2768 with three poly hops, to x 8350, where it is `tc1`'s nested bus metal ns4 (old name under former names). That metal goes south past y 4450 to its end pad (8204,5672) (`trace/tc2.txt`, piece 9), with one contact on the way, (8204,5371), onto a poly that runs east past x 8250 (seen to x 8425, not drawn). From the end pad the line goes on: a poly row west along y 5673, the pad (7748,5673), a metal south, the pad (7750,6065), a poly to the pad (7488,6282), and a metal west along y 6328 past x 6400 (follower: to (6012,6068)). Source: not found yet (west of x 6400) |
| `ral_a_s#` | `ral` cell s# (s0-s4 west to east; s0 is RA bit 0's cell), node a: the input pass transistor's far side (strobe `ral_stb`), the diffusion strip y 4479-4494 to the hold device (gate VSS), which joins it to the cell's output (`ra#_drv_in`; `ra4_drv_in_u` for 4), and the gate of one pull-down of the cell's NOR (a diffusion wire under the VSS rail, a buried contact, the poly bar y 4322-4344) |
| `ral_a_m#` | the same node in the fourteen copies of the `ral` cell in front of the MA pad drivers (`trace/mal.txt`, tags m0-m13 top to bottom; **copy m# drives MA#**: each output followed to its pad driver) |
| `mal_frc_m#` | the gate tab of the force pull-down in MA copy m# (`ral_n1_m#` = NOR(`ral_a_m#`, `mal_frc_m#`)): drawn as a pad of its own per copy; a thin vertical metal at x about 2700 runs past the pads and probably joins them all (seen, not drawn: `notes/blocks/mal.md`) |
| `ral_n1_s#`, `ral_n1_m#` | the output of the NOR of `ral` cell s# / MA copy m# (NOR of node a and `cnt_gab` / `mal_frc_m#`): its diffusion (north of the bar, the drain of the `cnt_gab` pull-down, the band above that line's pad) and, through a buried contact, the Z-shaped gate poly of the output inverter; the cell's output = NOT this |
| `cdp1_b#_n2`, `cdp1_b#_ne` | NOR(a, b) and a XOR b |
| `ra_eq_r9` | R9's match: NOR of the five `_ne` of the comparator in `cdp1` row B, high when R9 equals the 5-bit value on the `_b` lines, which are the row address as it goes to the RA pins (`ra#_cmp`; marked, AMB-012). In slice 5 the register bit is replaced by `cdp1_b5_a`, made by `tc1`. It runs to the row counter's step logic, where it is the input of the inverter that makes `rcs_mu` (contact (4148,3335); AMB-013, resolved; `notes/blocks/r9m.md`) |
| `cdp1_l#`, `cdp1_lw#` | horizontal lines of the data bus channel, named by their y; and two write-line links. East of the block they cross under the supply metal and go on east as the bus to the right datapath (`notes/blocks/bust.md`): `c4l0`, `c4l1`, `cdp1_l4632`, `cdp1_l4676` are the four inputs of `amr`'s comparator (the 4-bit counter `c4l0`..`c4l3`, compared with R3's high nibble; the last two keep their positional names until `bust`'s two `?P` rows are firm); `sl_eq_r5` is R5's match (`sl_eq_r5`, alias); `db_b6` is `amr` c2's inner line, an input there (the data written into the slice's latch); `cdp1_lw1` comes from the west: its west end is the pad (8353,4981), joined by a metal, a poly row and a thin metal to row B of the latch `tc2_sr` (its line `tc2_sr_r`, an alias; `notes/blocks/tc2.md`, piece 7) |
| `cdp2_a_s#_*` | cdp2 row A (5-bit latch), slice #: `_a` storage node, `_n2` inverse, `_q` output, `_bus` bit line |
| `cdp2_a_c_s#_*` | cdp2 row C (7-bit latch), the same nodes |
| `wr_r11`, `wr_r10` | the write strobes of R11 and R10, which are the load strobes of rows A and C: **row A is R11, row C is R10** (`notes/blocks/wrs.md`) |
| `cdp2_a_s#`, `cdp2_c_s#`, `cdp2_c_s#_bus` | per-slice lines and bit lines of those rows |
| `cdp2_b_s#`, `cdp2_b_s#_*` | cdp2 row B comparator with a ripple chain, slice #: `_y` = NOR(q, t), `_ne` = q XOR t, `_x` chain output of the slice, `_o2` inverse of the previous slice's chain output, `_p1` internal node |
| `cdp2_b_cin`, `cdp2_b_hl` | chain input of that comparator; and a row-long line pulled low per bit |
| `cdp2_trk_s#` | the value that row B compares row C against, per slice (through track). s7, s6, s5, s4 are aliases of `rax_o0`, `rax_o1`, `rax_o2`, `rax_o3`; `rax_o4`'s line (y 5826) has no through track tied to it as traced (slice s3 is wired differently) |
| `cdp2_ch#_#` | a line of channel 1, named by its y |
| `cdp3_c_c#_*`, `cdp3_h_c#_*` | cdp3 rows C (6 bit) and H (8 bit), static register bit in column #: `_x`, `_q1`, `_q` as in cdp1 |
| `cdp3_c_wr`, `cdp3_h_wr` | write lines of rows C and H |
| `cdp3_cw_c#`, `cdp3_hw_c#` | west outputs of those bits |
| `cdp3_cq_c#`, `cdp3_hq_c#` | read outputs of those bits, to the pass transistors onto bus N |
| `cdp3_n_c#` | bus N, column # |
| `cdp3_gate_e`, `cdp3_gate_f` | gates of the read pass transistors of rows E (row C onto bus N) and F (row H onto bus N) |
| `cdp3_bl_c#`, `cdp3_f_c#`, `cdp3_g_c#` | column lines e (bit line), f and g |
| `cdp3_k_a`, `cdp3_k_b`, `cdp3_k_c` | lines of the NAND beside row C |
| `cdp3_l#` | a line of channel B, named by its y |
| `cdp4_lc_s#_*`, `cdp4_lr_s#_*`, `cdp4_ldr_s#_*` | cdp4 latch rows C (8 bit), R1-lower (8 bit, upside down) and D (6 bit), slice #: `_a` storage node, `_n2` inverse, `_q` output, `_x2` internal strap |
| `cdp4_ld`, `cdp4_ld#b`, `cdp4_ld#` | load strobes of those rows (C, R1-lower, D) |
| `cdp4_in_s#`, `cdp4_in#b_s#`, `cdp4_in#_s#` | data inputs of those rows |
| `cdp4_n_s#` | output node of the 4-way selector, slice # |
| `cdp4_a_s#`, `cdp4_b_s#`, `cdp4_c_s#`, `cdp4_d_s#` | the selector's four sources per slice |
| `cdp4_sel#` | the four select lines of the selector |
| `cdp4_rst` | gate of the pull-down on the selector node |
| `cdp4_bus_s#` | the eight poly lines of channel 1 |

## Left array (`notes/blocks/larr.md`): the 14-bit memory address counter

Row tags `s0` ... `s13` are rows from the top; which MA bit each is has not been fixed.

| Name | What it is |
|---|---|
| `larr_n#_s#` | inverters of the row: `_n2` = the stored bit Q, `_n3` = NOT(carry-in XOR Q), `_n4`, `_n5` = the value sampled into the latch part |
| `larr_g#_s#` | storage node of the bit (`g6`) |
| `larr_x#_s#` | `_x1` dynamic node that takes the incremented or the loaded value; `_x2` = NOT `larr_ld` |
| `larr_ld_s#` | value offered for loading, from the right |
| `larr_y_s#`, `larr_z_s#` | new value leaving to the right; value written back to the bit |
| `larr_a_s#`, `larr_mid_s#` | internal nodes of the incrementer |
| `larr_cin_s#`, `larr_cout_s#` | carry in and out of a row |
| `larr_h_s#` | line H along a row boundary |
| `larr_l#_g#`, `larr_l#nc_s#` | group carry lines and their pieces |
| `larr_vm#` | vertical control lines Vm1-Vm6 of the latch part (clear, count, load, tied off, transfer, write) |

## Top-centre island and bottom-centre block

| Name | What it is |
|---|---|
| `tc1_l4_out`, `tc1_r#_out` | the island's remaining internal outputs: `tc1_r1_out` = NOT R9 bit 0; `tc1_r2_out` = NOR(R9 bit 0, `ras_shift`); `tc1_r5_out` = NOT((`tc1_i` AND `ras_o0_sel1`) OR (`tc1_g` AND `ras_o0_sel2`)), `tc1_r4_out` its inverse; `tc1_l4_out` = NOR(`ras_o0_sel2`, `tc1_w1`), leaves west |
| `tc1_g`, `tc1_i`, `tc1_w#`, `tc1_x#` | the island's other inputs and channel lines. `tc1_g` and `tc1_i` are used where the selector uses `ras_o0_alt2` and `ras_o0_alt1`; each is the output of a small inverter west of the selector (`notes/blocks/fld.md`), and they are **not** shown to be the selector's two nets |
| `tc1_x1` | NOT `ras_o0_sel1` (an inverter below R8's row, `notes/blocks/shm.md`); runs west past the island and into the logic west of the selector (`notes/blocks/fld.md`), from the contact (7055,4478) by poly and metal to a gate of the NOR `tc2_o5175` at (6500,5132) (`notes/blocks/tc2.md`). Its channel metal x 7053 also runs north: the ring gate of the driver `tc1_o4020`. A small inverter there, `tc1_o4280` = NOT `tc1_p4308`, may be on this line too; that join is not drawn (`notes/blocks/tc1.md`, Ambiguity 17; AMB-020; open join `tc1_x1_u`). The channel metal x 7053 runs north past the driver (contact (7054,4092)) to (7054,3134), with a tap at about (7055,3730) not looked at. The poly row y 4383-4401 that `tc1` labelled `tc1_x1_u` is the output of `tcw`'s last inverter, NOT `tcw_m6362c` (`notes/blocks/tcw.md`, run 2): if `tc1`'s assumed joins hold, `tc1_x1` has two drivers |
| `fld_a_in`, `fld_b_in` | gates of the two inverters whose outputs are `tc1_g` and `tc1_i` (`notes/blocks/fld.md`). `fld_a_in` = NOT((`tcw_a` AND `tcw_b`) OR `tcw_o3820`): pull-downs in the gate group west of the island, load and third pull-down east of the ground rail (`notes/blocks/tcw.md`, run 2); it is also the third gate input of `tcw_o3820` (supply assignment of the rails: AMB-014). `fld_b_in` = `cnt_la_a_n` XOR `tc1_g` (output of the first XOR cell) |
| `fld_y_b` | the metal input of the second XOR cell west of the selector: `ras_o0_alt1` = `rc0_n` XOR `fld_y_b`. Pulled low through `tcw_c` in the gate group west of the island (`fld_y_b` = NOT `tcw_c`; load traced in `tcw` run 2; AMB-014) |
| `tcw_a`, `tcw_b`, `tcw_c` | the three gate inputs of the group at x 6380-6700, y 3880-4220 (top-centre west), named by place: pads (6400,4005), (6455,4045), (6318,4135), each with a thin metal from the north. `tcw_a` and `tcw_c` are also gates of the AND-OR-invert above the group (pads (6400,3788), (6318,3740)). Sources not traced |
| `tcw_o#` | output node of a pull-down stack of the gate column west of the island, named by its y under the ground rail (`notes/blocks/tcw.md`). `tcw_o3820` = NOT(`fld_a_in` OR (`tcw_a` AND `tcw_c`)), leaving on a pad (6648,3785) and a thin metal to a pad (6646,3986), whose poly gates a third pull-down of `fld_a_in`: the two are a cross-coupled pair, a latch gated by `tcw_a`. `tcw_o3550` = NOT `tcw_m6232` (an inverter; alias of `tcw_m6362b`, the bus metal it leaves on, AMB-015). `tcw_o3326` (alias `tcw_o3437`: two stacks joined on their east side, AMB-015): low through `tcw_m6362a`, `tcw_m6404`, or `tcw_o3550` AND `tcw_m6320`; its load and destination not traced. `tcw_o2823` is an alias of `tcw_m6362a` (low through `tcw_m6404` AND `tcw_m6320`); `tcw_o2993` low through `tcw_m6404` AND `tcw_m6278`, gate of the next pair; `tcw_o3115`, `tcw_o3180` the middle and bottom nodes of that pair (which is its output is open) `tcw_o3240` = NOT(`tcw_m6320` AND `tcw_o3550` AND (`tcw_m6362a` OR `tcw_m6404`)) (run 3): the top node of the stack at y 3232-3410, with its load; `tcw_o3326` and `tcw_o3437` are one node inside that gate, not an output |
| `tcw_m#`, `tcw_m6362a`, `tcw_m6362b`, `tcw_m6362c` | a thin vertical metal of the bus west of the gate column, named by its x (and a letter where one x holds two nets). `tcw_m6404`: pads at y 2745, 2915, 3135, 3393: gates four pull-downs (a common enable or clock); comes from the south: its metal ends on a pad (6275,4405) at the top of a vertical poly under the six bus metals, not followed further. `tcw_m6320`: pads at y 2787, 3263, 3655. `tcw_m6232`: pads at y 2875 (a poly to the rail) and 3526. `tcw_m6278`: pads at y 2958 and 3178; runs on north and south. `tcw_m6362a`: from the pad (6355,2830) to (6378,3355); the output of the top pair of the column (AMB-016). `tcw_m6362b`: y 3437-3570; the output of the inverter `tcw_o3550` (AMB-015). `tcw_m6362c`: pads (6362,3832) and (6362,4266); gate of the column's last pull-down |
| `cdp1_fx_n2`, `cdp1_fy_n2`, `cdp1_fx_b`, `cdp1_fy_b` | names that the comparator cell's template gives the two copies west of the selector: `_n2` the cell's internal NOR of its inputs; `cdp1_fx_b` is an alias of `tc1_g`, `cdp1_fy_b` of `fld_y_b` |
| `tc1_ns#` | north-south lines ns1-ns6 east of the island. `tc1_ns2` (x 8132-8148, from a poly out of the logic at the datapath's slice-0 position) runs north to the bus line y 2727, west through the top bus field in poly to a pad (6773,2790), and south on the thin metal x 6765-6785 (`tc1_p3698`, aliased to it) to gate 1 of the second driver `tc1_o3740` |
| `tc1_bus#` | a through line of the top bus field north of the island that has no other name yet, named by the y of its metal track (`notes/blocks/tc1.md`, "The bus fan and the top bus field"). `tc1_bus2554` and `tc1_bus2684`: a poly from the north (x 7201-7218, x 7160-7176 at y 2500) to a metal track going east over the datapath. `tc1_bus2814`: a poly from the north (x 7117-7133) to the track y 2814 and on east as a poly (x 8350, y 2890-2907). `tc1_bus2858`: a poly row from the west (x 6750, y 2520-2540) to the track y 2858 and on east as a poly (x 8350, y 2933-2950). The two tracks below them are `r8_b4_q` (y 2899) and `r8_b5_q` (y 2943) |
| `tc1_o#` | output node of a gate in the columns west of the island's channel, named by its y (`notes/blocks/tc1.md`). `tc1_o4020` = NOR(`tc1_g`, `tc1_x1`): a wide driver at x 6800-6990, y 3925-4222 with a strong load; leaves on the channel metal x 7133-7152, a poly through the top bus field and the bus metal y 2641 going east over the datapath (drawn to x 8350; the follower gives its end at (9098,2639)). `tc1_o3740` = NOR(`tc1_ns2`, `tc1_x1`) (gate 1 arrives on the thin metal `tc1_p3698`, gate 2 on the thin metal `tc1_x1_u`): the second driver, north of the first (x 6690-7035, y 3600-3900); leaves on a metal that runs north, west along y 3653-3665 and north again at x 6941-6956 to a contact (6948,2977) and, across an uncertain metal (`notes/blocks/tc1.md`, Ambiguity 20, join J6), on into `tc1_m7056` (aliased to it) and east on the bus line y 2598. `tc1_o2950` = NOT `tc1_m6817`: cell D, a pull-down under the rail with a load of its own north of cell C (x 6690-6990, y 2800-2990); its output band ends in the box (6936-6974, 2944-2972), drawn as an uncertain buried contact onto `tc1_p3051` (aliased to it; join J4), which makes it gate row 1 of cell C. That the contact (6948,2977) of `tc1_o3740`'s thin metal is on the same band (J5) is not drawn. `tc1_o4280` = NOT `tc1_p4308`: the output node of a small inverter south of that driver (a strip under the rail, x 6803-6934, y 4270-4293). It runs up to `tc1_x1`'s pad (6962,4268); the join is not drawn (`notes/blocks/tc1.md`, Ambiguity 17), so it has no destination in the trace. `tc1_o3527` = NOR(`tc1_o3353`, `tc1_o3095`): cell B, the NOR north of the second driver (x 6690-7160, y 3405-3625); its poly runs south under the channel metal x 7048-7068 to the contact (7011,3852), and the channel metal x 7003-7023 takes it south out of the package at y 4450. `tc1_o3353` = NOR(`tc1_m7100`, `tc1_l4_out`): cell A, the next NOR north (x 6690-7160, y 3240-3420); its output is a C-shaped poly (y 3345-3362 / x 7137-7154 / y 3472-3492) that is cell B's gate row 1. `tc1_o3095` (formerly named as the channel metal x 7003-7023) = NOR(`tc1_p3051`, `tc1_x1`, `tc1_m7100`), with `tc1_p3051` = `tc1_o2950` if join J4 holds: cell C, the three-input NOR north of cell A (x 6690-7080, y 2940-3240); it leaves by the contact (7010,3093) on the channel metal x 7003-7023, which ends on cell B's gate row 2 |
| `tc1_m#` | a thin vertical metal of the gate columns west of the island's channel, named by its x. `tc1_m6817` passes over the driver `tc1_o4020`; no contact is drawn there (`notes/blocks/tc1.md`, Ambiguity 12), nor over cell B's buried contact (Ambiguity 18); its north end is a contact (6815,2833) on a pad whose C-shaped poly is the gate of cell D's pull-down (`tc1_o2950`); from its foot (6797,4372) it runs south to a pad (6796,4829), west on a poly row to a pad (6492,4828), by metal west, south along x 6364 and in three steps to a pad (6533,6152), and from there on a poly going south past y 6400 (`notes/blocks/tc2.md`): it is driven from the south, not followed further. `tc1_m7056`: the L-shaped metal y 2933-2948 / x 7049-7063 from the box of Ambiguity 20 to the contact (7054,2812), with the poly from there to the contact (7425,2596) and the bus metal y 2598 going east over the datapath (drawn to x 8350; the follower ends it at (9056,2595)); aliased to `tc1_o3740` across an uncertain metal. `tc1_m7100`: the upper piece of the channel metal x 7091-7110, ending south on the contact (7100,3180), whose poly is gate row 1 of cell A (`tc1_o3353`) and a gate of the next cell north; the metal goes north to y 2769, west along y 2762-2776 and north to a contact (6946,2680) on a pad of the poly row y 2652-2666, which comes from the west under the rail x 6858-6906 (its driver is west of x 6750) |
| `tc1_p#` | a poly of the gate columns west of the island's channel, named by its y. `tc1_p3698`: gate 1 of the second driver `tc1_o3740`; its vertical poly under the supply rail's east edge (x 6725-6740) ends at a pad with the contact (6772,3591), from which the thin metal x 6765-6785 goes north to a contact (6773,2790) on the west end of `tc1_ns2`'s poly: the two names are aliased. `tc1_p3051`: gate row 1 of cell C (`tc1_o3095`); its poly runs north to a box (6936-6974, 2944-2970) at the east end of a diffusion band, beside a contact (6948,2977) of `tc1_o3740`'s thin metal; the band is cell D's output, and the box is drawn as an uncertain buried contact, the name aliased to `tc1_o2950` (`notes/blocks/tc1.md`, Ambiguity 20). `tc1_p4308`: the input of the inverter `tc1_o4280` (gate of its pull-down under the rail x 6858-6908); its poly runs south and then west along y 4428-4448 (drawn to x 6750) to a pad with a contact at (6620,4436), whose metal goes south along x 6621 into the logic west of the selector (seen, not drawn) (`notes/blocks/tc1.md`, Ambiguity 17) |
| `tc1_x1_u` | the thin metal x 6968 over the same driver: an open join of `tc1_x1` (aliased in `trace/tc1.txt`): it has a contact on the pad (6962,4268) at the end of a branch of `tc1_x1`'s ring poly, and the branch meets the pad across a gap drawn `?P`. Its south end is a contact (6947,4396) on a pad whose poly runs west along y 4385-4405 (drawn to x 6750; seen to about x 6445). Its north end turns east into the contact (7009,3789) on gate 2 of the second driver `tc1_o3740` |
| `tc2_o#` | output node of a gate in the top-centre logic's lower half, named by its y (`notes/blocks/tc2.md`). `tc2_o5175` = NOR(`tc1_x1`, `fld_b_in`): two pull-downs west of the ground rail x 6537-6583 at y 5132 and 5219, load east of it; leaves west on a poly along y 5173 past x 6400, not followed |
| `tc2_sr_q`, `tc2_sr_q_n` | the two nodes of a latch of two cross-coupled gates at x 7977-8198, y 5990-6300 (`notes/blocks/tc2.md`, piece 4): `tc2_sr_q` = NOR(`tc2_sr_q_n`, `tc2_sr_c`, `tc2_sr_g` AND `tc2_sr_r`), `tc2_sr_q_n` = NOR(`tc2_sr_q`, `tc2_sr_g` AND `tc2_sr_s`); both depend on one `?` poly. `tc2_sr_q` leaves south on a metal x 7922 (past y 6400) and east on a poly y 6163-6180 (past x 8250); `tc2_sr_q_n` stays in the latch. Not identified |
| `tc2_sr_g` | the latch's common gate line: the gates in series with `tc2_sr_r` and with `tc2_sr_s`. Metal x 7837 going south past y 6400 (not followed) |
| `tc2_sr_r` | an alias of `cdp1_lw1` (`trace/tc2.txt`, piece 7): the latch's line that, with `tc2_sr_g` high, pulls `tc2_sr_q` low. From row B's pad by a metal x 7836 north, the pad (7836,5520), a poly east, the pad (8031,5520), a thin metal x 8031 north over `rax`'s units 2-4 without a contact, the pad (8031,5066), a poly row east along y 5066, the pad (8291,5066) and a metal to the pad (8353,4981), the west end of `cdp1_lw1` |
| `tc2_sr_s` | with `tc2_sr_g` high, pulls `tc2_sr_q_n` low. Metal x 7791 going south past y 6400 (not followed) |
| `tc2_sr_c` | pulls `tc2_sr_q` low by itself. It is the top line of `cdp2`'s channel 2 (poly y 6367, from the pad (7490,6367) east past x 8250), with a metal from that pad west along y 6370 past x 6400 (not followed either way) |
| `tc2_m#` | a metal of the nest west of the XOR cells (x 6400-6580, y 5350-6170), named by the x of its pad (`notes/blocks/tc2.md`, piece 5). `tc2_m6490`: from the west along y 5567 to the pad (6490,6108), poly south past y 6400. `tc2_m6447`: from the west along y 5611 to the pad (6447,6150), poly south past y 6400. Neither end is followed |
| `bc1_s#`, `bc1_s#_n` | the two bus lines the 2-bit decoder decodes, and their inverses |
| `bc1_dec#_n` | decoder outputs, active low (00, 10, 01) |
| `bc1_ld_in#`, `bc1_ld_n`, `bc1_ld_a` | inputs, NAND output and twin output of the driver of cdp4's row D strobe |
| `bc1_d#` | data lines 3-6 into cdp4's row D |
| `bc1_g#_in`, `bc1_g#_out` | input and output of inverter 6 |

## Odd ones

| Name | What it is |
|---|---|
| `rdp#_n#s#`, `rdp#_t#` | two short pieces of bundle wiring in the right datapath, named by track and position |

## Former names

Names used before 2026-11-16, for reading older commits; `tools/rename.py` adds a line for
every later rename. Row tags of the counter cells changed with the names: r18...r11 became
hc0...hc7, r10...r4 became rc0...rc6, r3...r0 became c4b0...c4b3; slice tags of the lower right
datapath s1...s7, s0 became b0...b6, b7.

| Old | New | Example |
|---|---|---|
| areg_load | ar_load | |
| bd2_a | wr_data_sel_n | |
| bd2_al_n | ar_load_n | |
| bd3_b12 | rsel12_buf | |
| bd2_c | wr_data_sel | |
| bd1_g | inh_src | |
| bd1_k7 | h_eq_r0_u | |
| bd1_k8 | h_eq_r1_u | |
| bd1_k5 | h_eq_r0half | |
| bd1_k14 | hc3 | |
| bd1_k17 | hc0 | |
| bd1_k9 | hc2 | |
| bd2_m255 | bd2_rs_n | |
| bd2_m210 | wr_addr_sel | |
| bd3_n12 | rsel12_bufn | |
| bd2_n1 | wr_data_lat | |
| bd2_nu | wr_data_e_n | |
| bd2_qb | wr_data_lat_n | |
| bd1_x | inh_n | |
| bd1_xn2 | inh_lat | |
| bd1_xn1 | inh_rc | |
| ck_src | inh_ck | |
| mra_a_r# | c#b#_m | mra_a_r0 -> c4b3_m |
| mra_a_r# | hc#_m | mra_a_r11 -> hc7_m |
| mra_a_r# | rc#_m | mra_a_r10 -> rc0_m |
| mra_b_r# | c#b#_mb | mra_b_r0 -> c4b3_mb |
| mra_b_r# | hc#_mb | mra_b_r11 -> hc7_mb |
| mra_b_r# | rc#_mb | mra_b_r10 -> rc0_mb |
| mra_busa | cnt_bus_a | |
| mra_busb | cnt_bus_b | |
| mra_busg | h_eq_r2 | |
| mra_cin_r3 | c4b_ci | |
| mra_cin_r18 | hc_ci | |
| mra_cin_r10 | rc_ci | |
| mra_cka2 | ck_a_u | |
| mra_ckb | ck_b | |
| mra_d_r# | c#b#_d | mra_d_r0 -> c4b3_d |
| mra_d_r# | hc#_d | mra_d_r11 -> hc7_d |
| mra_d_r# | rc#_d | mra_d_r10 -> rc0_d |
| mra_g#_r# | c#b#_q_n | mra_g1_r0 -> c4b3_q_n |
| mra_g#_r# | hc#_q_n | mra_g1_r11 -> hc7_q_n |
| mra_g#_r# | rc#_q_n | mra_g1_r10 -> rc0_q_n |
| mra_gab | cnt_gab | |
| mra_gla | rc_lo4_set | |
| mra_glb | hc_lo4_set | |
| mra_l2a | cnt_l2_a | |
| mra_l2b | cnt_l2_b | |
| mra_l2c | cnt_l2_c | |
| mra_l3m | rc_l3 | |
| mra_l3n | c4b_l3 | |
| mra_la | cnt_la_a | |
| mra_la2 | cnt_la_b | |
| mra_la3 | cnt_la_c | |
| mra_m7 | rc_ck_m | |
| mra_m_r# | c#b#_nx | mra_m_r0 -> c4b3_nx |
| mra_m_r# | hc#_nx | mra_m_r11 -> hc7_nx |
| mra_m_r# | rc#_nx | mra_m_r10 -> rc0_nx |
| mra_md_r# | c#b#_md | mra_md_r0 -> c4b3_md |
| mra_md_r# | hc#_md | mra_md_r11 -> hc7_md |
| mra_md_r# | rc#_md | mra_md_r10 -> rc0_md |
| mra_mt_r0 | c4b3_mt | |
| mra_mt_r# | hc#_mt | mra_mt_r11 -> hc7_mt |
| mra_n#_r# | c#b# | mra_n1_r0 -> c4b3 |
| mra_n#_r# | c#b#_ci_n | mra_n2_r0 -> c4b3_ci_n |
| mra_n#_r# | hc# | mra_n1_r11 -> hc7 |
| mra_n#_r# | hc#_ci_n | mra_n2_r11 -> hc7_ci_n |
| mra_n#_r# | rc# | mra_n1_r10 -> rc0 |
| mra_n#_r# | rc#_ci_n | mra_n2_r10 -> rc0_ci_n |
| mra_na_r# | c#b#_nx_g | mra_na_r0 -> c4b3_nx_g |
| mra_na_r# | hc#_nx_g | mra_na_r11 -> hc7_nx_g |
| mra_na_r# | rc#_nx_g | mra_na_r10 -> rc0_nx_g |
| mra_nb_r# | c#b#_nx_n | mra_nb_r0 -> c4b3_nx_n |
| mra_nb_r# | hc#_nx_n | mra_nb_r11 -> hc7_nx_n |
| mra_nb_r# | rc#_nx_n | mra_nb_r10 -> rc0_nx_n |
| mra_p#_r# | c#b#_m_n | mra_p3_r0 -> c4b3_m_n |
| mra_p#_r# | hc#_m_n | mra_p3_r11 -> hc7_m_n |
| mra_p#_r# | rc#_m_n | mra_p3_r10 -> rc0_m_n |
| mra_q_r# | c#b#_q | mra_q_r0 -> c4b3_q |
| mra_q_r# | hc#_q | mra_q_r11 -> hc7_q |
| mra_q_r# | rc#_q | mra_q_r10 -> rc0_q |
| mra_rb_r# | c#b#_rb | mra_rb_r0 -> c4b3_rb |
| mra_rb_r# | hc#_rb | mra_rb_r11 -> hc7_rb |
| mra_rb_r# | rc#_rb | mra_rb_r10 -> rc0_rb |
| mra_s7 | rc_ck_s | |
| mra_tab_r# | c#b#_tab | mra_tab_r0 -> c4b3_tab |
| mra_tab_r# | hc#_tab | mra_tab_r11 -> hc7_tab |
| mra_tab_r# | rc#_tab | mra_tab_r10 -> rc0_tab |
| mra_x_r# | c#b#_co | mra_x_r0 -> c4b3_co |
| mra_x_r# | hc#_co | mra_x_r11 -> hc7_co |
| mra_x_r# | rc#_co | mra_x_r10 -> rc0_co |
| mra_z_r# | c#b#_z | mra_z_r0 -> c4b3_z |
| mra_z_r# | hc#_z | mra_z_r11 -> hc7_z |
| mra_z_r# | rc#_z | mra_z_r10 -> rc0_z |
| rdp3_ar_ld | ar_load | |
| rdp#_ar_s#_a | ar#_a | rdp3_ar_s1_a -> ar0_a |
| rdp#_ar_s#_n# | ar#_n# | rdp3_ar_s1_n2 -> ar0_n2 |
| rdp#_ar_s#_q | ar#_q | rdp3_ar_s1_q -> ar0_q |
| rdp#_ar_s#_trk | ar#_trk | rdp3_ar_s1_trk -> ar0_trk |
| rdp#_bus_s# | rbus_b# | rdp3_bus_s0 -> rbus_b7 |
| rdp#_c_s# | hc# | rdp3_c_s0 -> hc7 |
| rdp#_c_s# | hc#_u | rdp3_c_s1 -> hc0_u |
| rdp3_ca_eq | h_eq_r1 | |
| rdp#_ca_s#_nor | r#c_b#_nor | rdp3_ca_s0_nor -> r1c_b7_nor |
| rdp#_ca_s#_x | r#c_b#_x | rdp3_ca_s0_x -> r1c_b7_x |
| rdp3_cb_eq | h_eq_r2 | |
| rdp#_cb_s#_nor | r#c_b#_nor | rdp3_cb_s0_nor -> r2c_b7_nor |
| rdp#_cb_s#_x | r#c_b#_x | rdp3_cb_s0_x -> r2c_b7_x |
| rdp2_cc_eq | h_eq_r0 | |
| rdp#_cc_s#_nor | r#c_b#_nor | rdp2_cc_s0_nor -> r0c_b7_nor |
| rdp#_cc_s#_x | r#c_b#_x | rdp2_cc_s0_x -> r0c_b7_x |
| rdp2_cd_eq | h_eq_r0half | |
| rdp#_cd_s#_nor | r#hc_s#_nor | rdp2_cd_s1_nor -> r0hc_s1_nor |
| rdp#_cd_s#_x | r#hc_s#_x | rdp2_cd_s1_x -> r0hc_s1_x |
| rdp2_ce_eq | uc_eq_r4 | |
| rdp#_ce_s#_nor | r#c_s#_nor | rdp2_ce_s0_nor -> r4c_s0_nor |
| rdp#_ce_s#_x | r#c_s#_x | rdp2_ce_s0_x -> r4c_s0_x |
| rdp2_ce_sm1_nor | r4c_sm1_nor | |
| rdp2_ce_sm1_x | r4c_sm1_x | |
| rdp3_n4 | rc0 | |
| rdp3_n5 | rc1 | |
| rdp3_n6 | rc2 | |
| rdp3_n8 | rc3 | |
| rdp3_ra_ld | wr_r1_u | |
| rdp#_ra_s#_a | r#_b#_a | rdp3_ra_s0_a -> r1_b7_a |
| rdp#_ra_s#_n# | r#_b#_n# | rdp3_ra_s0_n2 -> r1_b7_n2 |
| rdp#_ra_s#_q | r#_b#_q | rdp3_ra_s0_q -> r1_b7_q |
| rdp3_rb_ld | wr_r2_u | |
| rdp#_rb_s#_a | r#_b#_a | rdp3_rb_s0_a -> r2_b7_a |
| rdp#_rb_s#_n# | r#_b#_n# | rdp3_rb_s0_n2 -> r2_b7_n2 |
| rdp#_rb_s#_q | r#_b#_q | rdp3_rb_s0_q -> r2_b7_q |
| rdp3_rc_ld | wr_r0_u | |
| rdp#_rc_s#_a | r#_b#_a | rdp3_rc_s0_a -> r0_b7_a |
| rdp#_rc_s#_n# | r#_b#_n# | rdp3_rc_s0_n2 -> r0_b7_n2 |
| rdp#_rc_s#_q | r#_b#_q | rdp3_rc_s0_q -> r0_b7_q |
| rdp2_re_ld | wr_r4_u | |
| rdp#_re_s#_a | r#_s#_a | rdp3_re_s0_a -> r4_s0_a |
| rdp#_re_s#_n# | r#_s#_n# | rdp3_re_s0_n2 -> r4_s0_n2 |
| rdp#_re_s#_q | r#_s#_q | rdp3_re_s0_q -> r4_s0_q |
| rdp3_re_sm1_a | r4_sm1_a | |
| rdp3_re_sm1_n2 | r4_sm1_n2 | |
| rdp3_re_sm1_q | r4_sm1_q | |
| rdp2_rf_ld | wr_r6 | |
| rdp#_rf_s#_a | r#_s#_a | rdp3_rf_s0_a -> r6_s0_a |
| rdp#_rf_s#_n# | r#_s#_n# | rdp3_rf_s0_n2 -> r6_s0_n2 |
| rdp#_rf_s#_q | r#_s#_q | rdp3_rf_s0_q -> r6_s0_q |
| rdp3_rf_sm1_a | r6_sm1_a | |
| rdp3_rf_sm1_n2 | r6_sm1_n2 | |
| rdp3_rf_sm1_q | r6_sm1_q | |
| rdp3_s0 | inh_rc | |
| rdp#_ubus_s# | ubus_s# | rdp2_ubus_s0 -> ubus_s0 |
| rdp2_ubus_sm1 | ubus_sm1 | |
| rdp#_uc_s# | uc_s# | rdp2_uc_s0 -> uc_s0 |
| rdp2_uc_sm1 | uc_sm1 | |
| sel_b# | rsel#_buf | sel_b13 -> rsel13_buf |
| sel_bn# | rsel#_bn | sel_bn13 -> rsel13_bn |
| sel_n# | rsel#_n | sel_n0 -> rsel0_n |
| sel_stb_l | wr_stb_n | |
| sel_stb_r | wr_stb_n | |
| sel_w# | wr_r# | sel_w0 -> wr_r0 |
| t_g0_in | inh_n | |
| t_g0_out | inh_ck | |
| tla_a2 | rcs_a2 | |
| tla_b1 | rcs_b1 | |
| tla_c1 | rcs_c1 | |
| tla_e# | rcs_e# | tla_e3 -> rcs_e3 |
| tla_in# | rcs_in# | tla_in1 -> rcs_in1 |
| tla_m2 | rcs_m2 | |
| tla_thin | rcs_thin_e | |
| tla_thinw | rcs_thin_w | |
| tla_w2 | rcs_w2 | |
| tla_x1 | rcs_x1 | |
| wl_b | rc_stepreq_n | |
| wl_d_buf | rc_ck_s_dly | |
| wl_d_n | rc_ck_s_n | |
| wl_e_buf | rc_ck_m_dly | |
| wl_e_n | rc_ck_m_n | |
| wl_la_n | cnt_la_a_n | |
| wl_p | rc_step | |
| wl_pb | rc_step_n | |
| h_eq_r0_u | h_eq_r0 | |
| h_eq_r1_u | h_eq_r1 | |
| rcs_ba4100 | rcs_cond | |
| rcs_cm4028 | rcs_cond_lat | |
| rcs_m2 | rcs_cond_n | |
| rcs_bb3807 | rcs_stb | |
| rcs_stb_n | ck_out | |
| rcs_stb | clk_tl | |
| bd1_k4 | uc_eq_r6 | |
| c4b0 | hsw0 | |
| c4b0_ci_n | hsw0_ci_n | |
| c4b0_co | hsw0_co | |
| c4b0_d | hsw0_d | |
| c4b0_m | hsw0_m | |
| c4b0_m_n | hsw0_m_n | |
| c4b0_mb | hsw0_mb | |
| c4b0_nx | hsw0_nx | |
| c4b0_nx_g | hsw0_nx_g | |
| c4b0_nx_n | hsw0_nx_n | |
| c4b0_q | hsw0_q | |
| c4b0_q_n | hsw0_q_n | |
| c4b0_rb | hsw0_rb | |
| c4b0_tab | hsw0_tab | |
| c4b0_z | hsw0_z | |
| c4b1 | hsw1 | |
| c4b1_ci_n | hsw1_ci_n | |
| c4b1_co | hsw1_co | |
| c4b1_d | hsw1_d | |
| c4b1_m | hsw1_m | |
| c4b1_m_n | hsw1_m_n | |
| c4b1_mb | hsw1_mb | |
| c4b1_md | hsw1_md | |
| c4b1_nx | hsw1_nx | |
| c4b1_nx_g | hsw1_nx_g | |
| c4b1_nx_n | hsw1_nx_n | |
| c4b1_q | hsw1_q | |
| c4b1_q_n | hsw1_q_n | |
| c4b1_rb | hsw1_rb | |
| c4b1_tab | hsw1_tab | |
| c4b1_z | hsw1_z | |
| c4b2 | hsw2 | |
| c4b2_ci_n | hsw2_ci_n | |
| c4b2_co | hsw2_co | |
| c4b2_d | hsw2_d | |
| c4b2_m | hsw2_m | |
| c4b2_m_n | hsw2_m_n | |
| c4b2_mb | hsw2_mb | |
| c4b2_md | hsw2_md | |
| c4b2_nx | hsw2_nx | |
| c4b2_nx_g | hsw2_nx_g | |
| c4b2_nx_n | hsw2_nx_n | |
| c4b2_q | hsw2_q | |
| c4b2_q_n | hsw2_q_n | |
| c4b2_rb | hsw2_rb | |
| c4b2_tab | hsw2_tab | |
| c4b2_z | hsw2_z | |
| c4b3 | hsw3 | |
| c4b3_ci_n | hsw3_ci_n | |
| c4b3_co | hsw3_co | |
| c4b3_d | hsw3_d | |
| c4b3_m | hsw3_m | |
| c4b3_m_n | hsw3_m_n | |
| c4b3_mb | hsw3_mb | |
| c4b3_md | hsw3_md | |
| c4b3_mt | hsw3_mt | |
| c4b3_nx | hsw3_nx | |
| c4b3_nx_g | hsw3_nx_g | |
| c4b3_nx_n | hsw3_nx_n | |
| c4b3_q | hsw3_q | |
| c4b3_q_n | hsw3_q_n | |
| c4b3_rb | hsw3_rb | |
| c4b3_tab | hsw3_tab | |
| c4b3_z | hsw3_z | |
| c4b_ci | hsw_ci | |
| c4b_l3 | hsw_l3 | |
| c5l0 | sl0 | |
| c5l0_ci_n | sl0_ci_n | |
| c5l0_co | sl0_co | |
| c5l0_d | sl0_d | |
| c5l0_m | sl0_m | |
| c5l0_m_n | sl0_m_n | |
| c5l0_mb | sl0_mb | |
| c5l0_nx | sl0_nx | |
| c5l0_nx_g | sl0_nx_g | |
| c5l0_nx_n | sl0_nx_n | |
| c5l0_q | sl0_q | |
| c5l0_q_n | sl0_q_n | |
| c5l0_rb | sl0_rb | |
| c5l0_tab | sl0_tab | |
| c5l0_z | sl0_z | |
| c5l1 | sl1 | |
| c5l1_ci_n | sl1_ci_n | |
| c5l1_co | sl1_co | |
| c5l1_d | sl1_d | |
| c5l1_m | sl1_m | |
| c5l1_m_n | sl1_m_n | |
| c5l1_mb | sl1_mb | |
| c5l1_md | sl1_md | |
| c5l1_nx | sl1_nx | |
| c5l1_nx_g | sl1_nx_g | |
| c5l1_nx_n | sl1_nx_n | |
| c5l1_q | sl1_q | |
| c5l1_q_n | sl1_q_n | |
| c5l1_rb | sl1_rb | |
| c5l1_tab | sl1_tab | |
| c5l1_z | sl1_z | |
| c5l2 | sl2 | |
| c5l2_ci_n | sl2_ci_n | |
| c5l2_co | sl2_co | |
| c5l2_d | sl2_d | |
| c5l2_m | sl2_m | |
| c5l2_m_n | sl2_m_n | |
| c5l2_mb | sl2_mb | |
| c5l2_md | sl2_md | |
| c5l2_nx | sl2_nx | |
| c5l2_nx_g | sl2_nx_g | |
| c5l2_nx_n | sl2_nx_n | |
| c5l2_q | sl2_q | |
| c5l2_q_n | sl2_q_n | |
| c5l2_rb | sl2_rb | |
| c5l2_tab | sl2_tab | |
| c5l2_z | sl2_z | |
| c5l3 | sl3 | |
| c5l3_ci_n | sl3_ci_n | |
| c5l3_co | sl3_co | |
| c5l3_d | sl3_d | |
| c5l3_m | sl3_m | |
| c5l3_m_n | sl3_m_n | |
| c5l3_mb | sl3_mb | |
| c5l3_md | sl3_md | |
| c5l3_nx | sl3_nx | |
| c5l3_nx_g | sl3_nx_g | |
| c5l3_nx_n | sl3_nx_n | |
| c5l3_q | sl3_q | |
| c5l3_q_n | sl3_q_n | |
| c5l3_rb | sl3_rb | |
| c5l3_tab | sl3_tab | |
| c5l3_z | sl3_z | |
| c5l4 | sl4 | |
| c5l4_ci_n | sl4_ci_n | |
| c5l4_co | sl4_co | |
| c5l4_d | sl4_d | |
| c5l4_m | sl4_m | |
| c5l4_m_n | sl4_m_n | |
| c5l4_mb | sl4_mb | |
| c5l4_md | sl4_md | |
| c5l4_nx | sl4_nx | |
| c5l4_nx_g | sl4_nx_g | |
| c5l4_nx_n | sl4_nx_n | |
| c5l4_q | sl4_q | |
| c5l4_q_n | sl4_q_n | |
| c5l4_rb | sl4_rb | |
| c5l4_tab | sl4_tab | |
| c5l4_z | sl4_z | |
| c5l_gab | sl_gab | |
| c5l_l3 | sl_l3 | |
| hsw_eq_r3_x | hsw_eq_r3 | |
| r3_t0_a | r3_b0_a | |
| r3_t0_d | r3_b0_d | |
| r3_t0_n2 | r3_b0_n2 | |
| r3_t0_q | r3_b0_q | |
| r3_t1_a | r3_b1_a | |
| r3_t1_d | r3_b1_d | |
| r3_t1_n2 | r3_b1_n2 | |
| r3_t1_q | r3_b1_q | |
| r3_t2_a | r3_b2_a | |
| r3_t2_d | r3_b2_d | |
| r3_t2_n2 | r3_b2_n2 | |
| r3_t2_q | r3_b2_q | |
| r3_t3_a | r3_b3_a | |
| r3_t3_d | r3_b3_d | |
| r3_t3_n2 | r3_b3_n2 | |
| r3_t3_q | r3_b3_q | |
| r3c_t0_nor | r3c_b0_nor | |
| r3c_t0_x | r3c_b0_x | |
| r3c_t1_nor | r3c_b1_nor | |
| r3c_t1_x | r3c_b1_x | |
| r3c_t2_nor | r3c_b2_nor | |
| r3c_t2_x | r3c_b2_x | |
| r3c_t3_nor | r3c_b3_nor | |
| r3c_t3_x | r3c_b3_x | |
| r4_s0_a | r4_b1_a | |
| r4_s0_n2 | r4_b1_n2 | |
| r4_s0_q | r4_b1_q | |
| r4_s1_a | r4_b2_a | |
| r4_s1_n2 | r4_b2_n2 | |
| r4_s1_q | r4_b2_q | |
| r4_s2_a | r4_b3_a | |
| r4_s2_n2 | r4_b3_n2 | |
| r4_s2_q | r4_b3_q | |
| r4_s3_a | r4_b4_a | |
| r4_s3_n2 | r4_b4_n2 | |
| r4_s3_q | r4_b4_q | |
| r4_s4_a | r4_b5_a | |
| r4_s4_n2 | r4_b5_n2 | |
| r4_s4_q | r4_b5_q | |
| r4_s5_a | r4_b6_a | |
| r4_s5_n2 | r4_b6_n2 | |
| r4_s5_q | r4_b6_q | |
| r4_sm1_a | r4_b0_a | |
| r4_sm1_n2 | r4_b0_n2 | |
| r4_sm1_q | r4_b0_q | |
| r4c_s0_nor | r4c_b1_nor | |
| r4c_s0_x | r4c_b1_x | |
| r4c_s1_nor | r4c_b2_nor | |
| r4c_s1_x | r4c_b2_x | |
| r4c_s2_nor | r4c_b3_nor | |
| r4c_s2_x | r4c_b3_x | |
| r4c_s3_nor | r4c_b4_nor | |
| r4c_s3_x | r4c_b4_x | |
| r4c_s4_nor | r4c_b5_nor | |
| r4c_s4_x | r4c_b5_x | |
| r4c_s5_nor | r4c_b6_nor | |
| r4c_s5_x | r4c_b6_x | |
| r4c_sm1_nor | r4c_b0_nor | |
| r4c_sm1_x | r4c_b0_x | |
| r5_s0_a | r5_b1_a | |
| r5_s0_n2 | r5_b1_n2 | |
| r5_s0_q | r5_b1_q | |
| r5_s1_a | r5_b2_a | |
| r5_s1_n2 | r5_b2_n2 | |
| r5_s1_q | r5_b2_q | |
| r5_s2_a | r5_b3_a | |
| r5_s2_n2 | r5_b3_n2 | |
| r5_s2_q | r5_b3_q | |
| r5_s3_a | r5_b4_a | |
| r5_s3_n2 | r5_b4_n2 | |
| r5_s3_q | r5_b4_q | |
| r5_sm1_a | r5_b0_a | |
| r5_sm1_n2 | r5_b0_n2 | |
| r5_sm1_q | r5_b0_q | |
| r5c_s0_nor | r5c_b1_nor | |
| r5c_s0_x | r5c_b1_x | |
| r5c_s1_nor | r5c_b2_nor | |
| r5c_s1_x | r5c_b2_x | |
| r5c_s2_nor | r5c_b3_nor | |
| r5c_s2_x | r5c_b3_x | |
| r5c_s3_nor | r5c_b4_nor | |
| r5c_s3_x | r5c_b4_x | |
| r5c_sm1_nor | r5c_b0_nor | |
| r5c_sm1_x | r5c_b0_x | |
| r6_s0_a | r6_b1_a | |
| r6_s0_n2 | r6_b1_n2 | |
| r6_s0_q | r6_b1_q | |
| r6_s1_a | r6_b2_a | |
| r6_s1_n2 | r6_b2_n2 | |
| r6_s1_q | r6_b2_q | |
| r6_s2_a | r6_b3_a | |
| r6_s2_n2 | r6_b3_n2 | |
| r6_s2_q | r6_b3_q | |
| r6_s3_a | r6_b4_a | |
| r6_s3_n2 | r6_b4_n2 | |
| r6_s3_q | r6_b4_q | |
| r6_s4_a | r6_b5_a | |
| r6_s4_n2 | r6_b5_n2 | |
| r6_s4_q | r6_b5_q | |
| r6_s5_a | r6_b6_a | |
| r6_s5_n2 | r6_b6_n2 | |
| r6_s5_q | r6_b6_q | |
| r6_sm1_a | r6_b0_a | |
| r6_sm1_n2 | r6_b0_n2 | |
| r6_sm1_q | r6_b0_q | |
| r6c_s0_nor | r6c_b1_nor | |
| r6c_s0_x | r6c_b1_x | |
| r6c_s1_nor | r6c_b2_nor | |
| r6c_s1_x | r6c_b2_x | |
| r6c_s2_nor | r6c_b3_nor | |
| r6c_s2_x | r6c_b3_x | |
| r6c_s3_nor | r6c_b4_nor | |
| r6c_s3_x | r6c_b4_x | |
| r6c_s4_nor | r6c_b5_nor | |
| r6c_s4_x | r6c_b5_x | |
| r6c_s5_nor | r6c_b6_nor | |
| r6c_s5_x | r6c_b6_x | |
| r6c_sm1_nor | r6c_b0_nor | |
| r6c_sm1_x | r6c_b0_x | |
| r7_s0_a | r7_b1_a | |
| r7_s0_n2 | r7_b1_n2 | |
| r7_s0_q | r7_b1_q | |
| r7_s1_a | r7_b2_a | |
| r7_s1_n2 | r7_b2_n2 | |
| r7_s1_q | r7_b2_q | |
| r7_s2_a | r7_b3_a | |
| r7_s2_n2 | r7_b3_n2 | |
| r7_s2_q | r7_b3_q | |
| r7_s3_a | r7_b4_a | |
| r7_s3_n2 | r7_b4_n2 | |
| r7_s3_q | r7_b4_q | |
| r7_s4_a | r7_b5_a | |
| r7_s4_n2 | r7_b5_n2 | |
| r7_s4_q | r7_b5_q | |
| r7_s5_a | r7_b6_a | |
| r7_s5_n2 | r7_b6_n2 | |
| r7_s5_q | r7_b6_q | |
| r7_sm1_a | r7_b0_a | |
| r7_sm1_n2 | r7_b0_n2 | |
| r7_sm1_q | r7_b0_q | |
| r7c_s0_nor | r7c_b1_nor | |
| r7c_s0_x | r7c_b1_x | |
| r7c_s1_nor | r7c_b2_nor | |
| r7c_s1_x | r7c_b2_x | |
| r7c_s2_nor | r7c_b3_nor | |
| r7c_s2_x | r7c_b3_x | |
| r7c_s3_nor | r7c_b4_nor | |
| r7c_s3_x | r7c_b4_x | |
| r7c_s4_nor | r7c_b5_nor | |
| r7c_s4_x | r7c_b5_x | |
| r7c_s5_nor | r7c_b6_nor | |
| r7c_s5_x | r7c_b6_x | |
| r7c_sm1_nor | r7c_b0_nor | |
| r7c_sm1_x | r7c_b0_x | |
| sl_eq_r5_x | sl_eq_r5 | |
| ubus_s0 | ubus_b1 | |
| ubus_s1 | ubus_b2 | |
| ubus_s2 | ubus_b3 | |
| ubus_s3 | ubus_b4 | |
| ubus_s4 | ubus_b5 | |
| ubus_s5 | ubus_b6 | |
| ubus_sm1 | ubus_b0 | |
| uc_s0 | uc_b1 | |
| uc_s1 | uc_b2 | |
| uc_s2 | uc_b3 | |
| uc_s3 | uc_b4 | |
| uc_s4 | uc_b5 | |
| uc_s5 | uc_b6 | |
| uc_sm1 | uc_b0 | |
| cdp2_ch1_5826 | ch1w_5758 | |
| ch1w_5890 | cdp2_trk_s6 | |
| ch1w_5848 | cdp2_trk_s5 | |
| ch1w_5800 | cdp2_trk_s4 | |
| ch1w_5758 | rax_o4 | |
| cdp1_a_wr | wr_r8 | |
| cdp1_c_wr | wr_r9 | |
| cdp2_a_ld | wr_r11 | |
| cdp2_c_ld | wr_r10 | |
| tc1_b | ras_shift | |
| tc1_l2_out | ras_o0_sel2 | |
| tc1_l1_out | ras_straight | |
| tc1_l3_out | ras_o0_sel1 | |
| tc1_ns6 | cdp1_a5_q | |
| tc1_ns5 | cdp1_a4_q | |
| fld_x_a | cnt_la_a_n | |
| fld_y_a | rc0_n | via wl_i2_out |
| wl_i2_in | rc0 | |
| wl_i2_out | rc0_n | |
| h_eq_r2_u | h_eq_r2 | |
| wr_r0_u | wr_r0 | |
| wr_r1_u | wr_r1 | |
| wr_r2_u | wr_r2 | |
| wr_r4_u | wr_r4 | |
| rdp3_n1s4 | wr_r4 | |
| hc0_u | hc0 | |
| hc1_u | hc1 | |
| hc2_u | hc2 | |
| hc3_u | hc3 | |
| hc4_u | hc4 | |
| hc5_u | hc5 | |
| bd1_k11 | hc1 | |
| ra3_drv_in_u | ra3_drv_in | |
| ral_frc | cnt_gab | |
| ral_tf_s# | ral_n1_s# | |
| ral_tf_m# | ral_n1_m# | |
| tc1_ns4 | ral_stb | |
| ra2_drv_in_u | ra2_drv_in | |
| uc_b0 | rc0 | |
| uc_b1 | rc1 | |
| uc_b2 | rc2 | |
| uc_b3 | rc3 | |
| uc_b4 | rc4 | |
| uc_b5 | rc5 | |
| uc_b6 | rc6 | |
| uc_eq_r4 | rc_eq_r4 | |
| uc_eq_r6 | rc_eq_r6 | |
| uc_eq_r7 | rc_eq_r7 | |
| cdp1_l4719 | sl_eq_r5 | |
| rdp3_n2s1 | h_eq_r0 | |
| rdp3_n0 | h_eq_r0half | |
| cdp1_b_eq | ra_eq_r9 | |
| rcs_bq3335 | ra_eq_r9 | |
| cdp1_a0_x | r8_b5_a | |
| cdp1_a0_q1 | r8_b5_n2 | |
| cdp1_a0_q | r8_b5_q | |
| cdp1_a0_m3 | r8_b5_m3 | |
| cdp1_a0_m6 | r8_b5_m6 | |
| cdp1_a0_bl | db_b5 | |
| cdp1_a1_x | r8_b4_a | |
| cdp1_a1_q1 | r8_b4_n2 | |
| cdp1_a1_q | r8_b4_q | |
| cdp1_a1_m3 | r8_b4_m3 | |
| cdp1_a1_m6 | r8_b4_m6 | |
| cdp1_a1_bl | db_b4 | |
| cdp1_a2_x | r8_b7_a | |
| cdp1_a2_q1 | r8_b7_n2 | |
| cdp1_a2_q | r8_b7_q | |
| cdp1_a2_m3 | r8_b7_m3 | |
| cdp1_a2_m6 | r8_b7_m6 | |
| cdp1_a2_bl | db_b7 | |
| cdp1_a3_x | r8_b6_a | |
| cdp1_a3_q1 | r8_b6_n2 | |
| cdp1_a3_q | r8_b6_q | |
| cdp1_a3_m3 | r8_b6_m3 | |
| cdp1_a3_m6 | r8_b6_m6 | |
| cdp1_a3_bl | db_b6 | |
| cdp1_a4_x | r8_b1_a | |
| cdp1_a4_q1 | r8_b1_n2 | |
| cdp1_a4_q | r8_b1_q | |
| cdp1_a4_m3 | r8_b1_m3 | |
| cdp1_a4_m6 | r8_b1_m6 | |
| cdp1_a4_bl | db_b1 | |
| cdp1_a5_x | r8_b0_a | |
| cdp1_a5_q1 | r8_b0_n2 | |
| cdp1_a5_q | r8_b0_q | |
| cdp1_a5_m3 | r8_b0_m3 | |
| cdp1_a5_m6 | r8_b0_m6 | |
| cdp1_a5_bl | db_b0 | |
| cdp1_c1_x | r9_b4_a | |
| cdp1_c1_q1 | r9_b4_n2 | |
| cdp1_c1_q | r9_b4_q | |
| cdp1_c1_m3 | r9_b4_m3 | |
| cdp1_c1_m6 | r9_b4_m6 | |
| cdp1_c1_bl | db_b4 | |
| cdp1_c2_x | r9_b3_a | |
| cdp1_c2_q1 | r9_b3_n2 | |
| cdp1_c2_q | r9_b3_q | |
| cdp1_c2_m3 | r9_b3_m3 | |
| cdp1_c2_m6 | r9_b3_m6 | |
| cdp1_c2_bl | db_b3 | |
| cdp1_c3_x | r9_b2_a | |
| cdp1_c3_q1 | r9_b2_n2 | |
| cdp1_c3_q | r9_b2_q | |
| cdp1_c3_m3 | r9_b2_m3 | |
| cdp1_c3_m6 | r9_b2_m6 | |
| cdp1_c3_bl | db_b2 | |
| cdp1_c4_x | r9_b1_a | |
| cdp1_c4_q1 | r9_b1_n2 | |
| cdp1_c4_q | r9_b1_q | |
| cdp1_c4_m3 | r9_b1_m3 | |
| cdp1_c4_m6 | r9_b1_m6 | |
| cdp1_c4_bl | db_b1 | |
| cdp1_c5_x | r9_b0_a | |
| cdp1_c5_q1 | r9_b0_n2 | |
| cdp1_c5_q | r9_b0_q | |
| cdp1_c5_m3 | r9_b0_m3 | |
| cdp1_c5_m6 | r9_b0_m6 | |
| cdp1_c5_bl | db_b0 | |
| ubus_b0 | db_b0 | |
| rbus_b0 | db_b0 | |
| ubus_b1 | db_b1 | |
| rbus_b1 | db_b1 | |
| ubus_b2 | db_b2 | |
| rbus_b2 | db_b2 | |
| ubus_b3 | db_b3 | |
| rbus_b3 | db_b3 | |
| ubus_b4 | db_b4 | |
| rbus_b4 | db_b4 | |
| ubus_b5 | db_b5 | |
| rbus_b5 | db_b5 | |
| ubus_b6 | db_b6 | |
| rbus_b6 | db_b6 | |
| rbus_b7 | db_b7 | |
| r3_b0_d | db_b0 | |
| r3_b1_d | db_b1 | |
| r3_b2_d | db_b2 | |
| r3_b3_d | db_b3 | |
| amr_oa_c1 | db_b5 | |
| amr_oa_c2 | db_b6 | |
| amr_oa_c3 | db_b7 | |
| cdp1_lw2 | db_b6 | |
| tc1_x2 | db_b6 | |
| tc1_m7013 | tc1_o3095 | |
| tc1_o3740_u | tc1_p3051 | |
| tc1_b2554 | tc1_bus2554 | |
| tc1_b2684 | tc1_bus2684 | |
| tc1_b2814 | tc1_bus2814 | |
| tc1_b2858 | tc1_bus2858 | |
| cdp1_l4544 | c4l0 | |
| cdp1_l4588 | c4l1 | |
| amr_ob_c1 | c4l1 | |
| tla_w3461 | amr_eq_r3 | |
