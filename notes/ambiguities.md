# Ambiguity register

Each entry: where, what is unclear, the candidate readings, the working assumption (if
any) and what would settle it. Status is open, assumed or resolved.

## AMB-001  Structure of the RES/LPSTB input buffers  (resolved)

Where: 6950-8000 x 1640-2060, two identical cells.

Each cell has a small inverter (driver gate fed from a pad through the vertical metal
at x 7380, load block at 7304-7370 x 1942-1996) followed by a large two-finger
transistor (diffusion 7080-7234 x 1790-1986) and a second wide poly block at
7025-7060 x 1897-1965. Both stages sit between two wide rails (y 1834-1886 and
y 2004-2052) and much of the detail is under the upper rail.

Unclear: how the second block and the two-finger transistor connect near
7025-7110 x 1830-2000, and therefore which rail is VCC and which VSS here. One reading
has the box at 7040-7070 x 1837-1867 as a buried contact tying the output diffusion to
the poly that leaves through the contact at 7076,1684; the other has it as a metal
contact to the upper rail.

Resolved: the large two-finger transistor with its load is the same cell as the
second stage of the CLK and E buffers, flipped top to bottom (found by template
matching, confirmed by overlay). That fixes the upper rail as ground and the lower
as supply. The first stage is a small inverter whose gate wraps round a pocket of
diffusion. Each cell is a non-inverting two-stage buffer. Traced in
trace/pads_in_top.txt; left cell is LPSTB, right cell is RES.

## AMB-002  Depletion implant visibility  (open)

Loads are identified by topology (gate tied to source through a buried contact, other
end on the supply). Whether the implant outline is visible in either shot is not yet
known. Matters for transistors that are depletion-mode without being wired as loads
(for example always-on pass devices), which topology alone would miss.

To settle: compare known loads against known pull-downs at 4-5x in both shots for any
consistent outline or tint.

2026-11-15: this now matters in a concrete place. The static register cell of the
central datapath (`cdp1_reg`, notes/blocks/cdp1.md) holds its value through a long
transistor whose gate is grounded; the cell only works if that device is
depletion-mode. So there are depletion devices that are not wired as loads, and
topology alone will not find them all. Any transistor whose gate is tied to VSS or to
its own source should be listed as a probable depletion device.

## AMB-003  Data pad cell  (resolved 2026-11-17)

Where: D0 master, 17780-18760 x 7150-7560 (and the same place in D1-D7).

The output fingers and their two gate nets are understood. The logic that makes
those gate nets from the two lines that arrive from the bus interface is not. The
clean shot of chip 1 settled which shapes under the VCC band are poly, and showed
that the cell contains more than two inverters: at least one transistor gated by the
second line sits in series with the pull-up gate net, the first line is tied to a
diffusion row deep in the cell, and two large closed shapes under the band are of
unknown kind. Everything established, with coordinates, is in
notes/blocks/pads.md.

To settle: trace the bus-interface logic that drives the two lines (M2), so that
their meaning and polarity are known; then finish the cell from 4x views of the
clean shot, starting with the buried contact at 17835-17858 x 7440-7460 and the left
end of row H's metal. A tri-state pair needs both output gates low when disabled,
which is a strong check on any reading.

Resolved 2026-11-17 by `dpad` (dp111, `notes/blocks/dpad.md`): the output cell is traced and
placed on D0-D7. `d#_pu` = NOR(`d_hiz`, `d#_out_n`) and `d#_pd` = NOR(`d_hiz`, `d#_pu`) drive 3
pull-up and 5 pull-down fingers; `d_hiz` (the "P_x" above) high floats the pin, `d#_out_n` (the
"P_y") low drives it high. Both outputs low when disabled, as the check above requires. The
readings of `notes/blocks/pads.md`'s data pad section that this entry rested on were wrong:
rows G and K are the pull-up gate node, not VCC; H and J are VSS; I is the pull-down node; the
"green shapes" are field islands; the boxes at 18597-18632 x 7250-7298, 17835-17858 x
7440-7460 and strip 4's end are not buried contacts; "gate 7170" is a field strip. The thin
metal that carries D0's "P_y" is one line down the whole data bus column, D0's alone
(`dbus`, run 3): `d0_out_n` = NOT `dbus_do0_in`.

## AMB-004  L-shaped poly on the input inverters  (changed 2026-11-17: wrong in the data bus column)

Where: 14626-14689 x 18286-18375 on the R/W group, and the same place in the RS and
CS groups (+628, +1256).

The input gate poly of the first inverter of each group continues past its diffusion
into an L that runs up beside the load and ends. It crosses no diffusion that I can
see, so it does nothing electrically as traced. It abuts the gate with no gap, so it
is drawn as part of the input net.

To settle: nothing needed unless a diffusion turns up under it. Worth a second look
if the input stage ever fails to simulate as a plain inverter.

Changed 2026-11-17 by `dbus` (Tom Seddon, `notes/blocks/dbus.md`, "The L arm"): in the data bus
column the L arm of every first input inverter is a **second pull-down** (gate the pin, between
VSS and the stage's output, W about 22-26), traced in all eight chains: under the metal that
crosses it the arm lies on a diffusion (channel colour in the clean shot, tan on both sides,
one outline with the VSS land in the chip-2 shots). The logic is unchanged. For the bottom-row
input inverters the assumption "crosses no diffusion" is now doubtful and untested: re-read
item R25.

## AMB-005  Input protection cells: gate of the clamp, and the comb  (assumed)

Where: master 14667-15131 x 18943-19219 (R/W); also CLK, E, RS, CS cells.

The clamp is a 424/40 transistor from the input node to the rail at y 18950-18998.
Its gate poly forms a ring round the node and no contact or buried contact to it is
visible, so what it is tied to is unknown (ground is usual for such a clamp). The
rail itself is taken to be VSS but has not been followed to the ring. Under the VCC
band, below the node, there is a comb of ten small U-shaped features whose layer and
purpose are not worked out.

None of this affects logic: with any normal tie the clamp is off in operation.

Update, from 4x composite views of the comb and the right-hand end: the pad's strip
is poly and joins the frame at 15015-15035 x 19215-19262; the frame's right arm
feeds a thin spine at y 19128-19140, and the ten U shapes hang from that spine over
the lower edge of the node diffusion. Working assumption: the U shapes are buried
contacts, so pad poly, frame, gate band and node are one net, and the band over
y 19029-19070 is a thick-oxide clamp to the rail (gate on its own drain). This is
the textbook arrangement and it gives the pad net a junction to the substrate, which
a poly-only path would lack. Still to do: follow the rail to a supply.

Checked against the clean shot of chip 1: the frame is a poly plate
(14670-15130 x 19125-19215) with ten finger-shaped slots; ten fingers of the node
diffusion reach down into the slots. The band above the node is poly with no metal
over it. Nothing contradicts the working assumption; the trace still draws the comb
as a single strip.

Added 2026-11-17 by `dpad`: the data pads' protection is a thin-oxide grounded-gate clamp: the
poly frame is tied to VSS by an outer strip and a rail contact, and the pad reaches the
protected node through a diffused series strip.

## AMB-006  Island devices in the clock block wiring  (assumed: clamps)

Where: B1 12385-12447 x 18885-18975, B2 12563-12627 (same y), B3 12738-12802 (same y),
T1 12380-12456 x 19132-19202, T2 12380-12456 x 19302-19372, BI 12432-12497 x 19636-19726.

Each is a diffusion strip from VCC that passes under a poly gate and ends in a short
stub with one metal contact. A small metal pad, connected to nothing else, covers the
stub contact and the gate. The gate poly is on a signal net: B1 on `ck_n2`, B2 on
buffered CLK (`clk_b`), B3 on the CLK pin node (`clk_p`), T1 and T2 on line B, BI on
`ck_n1`. W/L is about 55/27 for T1/T2 and 52/22 for B1-B3.

Unclear:
1. How gate and stub are tied. An isolated pad is only useful if it joins them, but
   no separate poly contact is resolved; a buried contact at the poly edge would do
   the same job and then the pad would be redundant. Drawn as a buried contact,
   flagged.
2. What they are for. Gate tied to the stub with the far side on VCC is a pull-up if
   the device is depletion-mode, or a clamp to VCC + Vt if it is enhancement-mode.
   The implant is not visible (AMB-002). A pull-up on the CLK pin node would break
   the datasheet's input leakage figure, which argues for a clamp at least for B3.
   `ck_n1` and `ck_n2` so far have no other pull-up, which argues for pull-ups there.
3. Whether T2's gate line really joins line B's poly at 12288,19262. The strip is
   clearly poly from y 19285 down; its top end is not resolved. The alternative is a
   dead end, which makes no sense.

Effect on logic: none for `clk_p` and `clk_b` (both are driven anyway). For `ck_n1`,
`ck_n2` and line B it decides whether the nets have a static pull-up.

Update: `ck_n1` is the output of gate 2 and `ck_n2` the output of gate 4 in the gate
row, so every island sits on a net that already has an inverter's depletion load,
except B3, which sits on the CLK pin node (the pin, after its series resistor: see
AMB-005). A pull-up is therefore needed nowhere and is ruled out on the pin by the
leakage figure. Working assumption: all six are enhancement devices used as clamps
to VCC + Vt, on the nets that drive the bootstrapped driver logic. Marked
kind=clamp, which leaves them out of logic recovery.

Checked against the clean shot of chip 1: no buried contact at any of the six. Each
is a plain gate over the strip, with the stub's metal contact showing as a speck and
nothing visible on the gate. So if gate and stub are tied, it is by the metal pad
contacting both, and a contact onto poly leaves no speck to see. The tie is still
unproven. The nets involved are now known to be the clock phases, their delayed
copies and CLK, where overshoot above VCC from the wide drivers is plausible, which
suits a clamp.

## AMB-007  Clock driver logic  (mostly resolved)

Where: 10900-12000 x 19140-19890.

Resolved 2026-11-14 from the clean shot of chip 1: the block is the two-phase
non-overlapping clock generator (notes/blocks/clock.md). Its logic is traced and
extracts as two cross-coupled NORs.

Still open, neither affecting the logic:
1. A box at 10938-11003 x 19632-19668 on the left pull-up's gate, where the poly
   widens from x 10966-10992 to x 10950-10992 (mirror image at 11870-11936). It
   looks exactly like a buried-contact window in all five shots. A buried contact
   there would tie the gate to the diffusion on both sides, that is the VCC side and
   the output together, which cannot be. Candidate readings: (a) not a buried
   contact but some other mask feature; (b) a buried contact to the output side
   only, making the "pull-up" a large depletion load with its gate on its source
   and the whole half one ratioed NOR. Reading (b) gives the same logic. The trace
   leaves the box out and treats the gate as driven by the small NOR.
2. Whether the wide pull-ups are enhancement or depletion devices.

To settle: a delayered shot (poly removed), or measuring the phase lines' high level
on a real chip.

## AMB-008: the pull-down line L3 of counter rows r4-r10 seemed to have no feed (resolved 2026-11-15)

Where: mid-right array, thin metal line L3, piece y 9440-13018.

It looked cut at both ends with no contact. At 6.5x in all four shots its lower end widens
into a foot that turns west onto the contact (12567,13005), which had been given to the
neighbouring line L2. Feed: a metal line from the west along y 13005, contact
(11765,13005), poly east, that contact. Lesson: a line that ends in a widened foot ends on
something; look at the foot at 6x before calling it free.

For the 8-bit counter L3 is `ck_a` (poly followed in the clean shot to clock.txt's bus
line), so there it is a clock phase, not a clear. What the L3 lines of the row counter
(from the west along y 13005) and of the 4-bit counter (north) carry is open until their
sources are traced.

## AMB-009: the top of the column at (3045,4515) in the step logic cluster: buried contact or VSS? (2026-11-16)  (resolved 2026-11-18: VSS, the other reading)

**Where.** `trace/tla.txt`, the column x 3028-3063 above gate E0. A poly band (gate
`clk_tl`, y 4535-4558) crosses the column between the node `rcs_cond` and the column's
top end (y 4512-4532). Directly above that end sits the poly pad (3024-3066, 4455-4522) at
the bottom of the metal `rcs_cond_lat`.

**Reading adopted (drawn `?B`).** The pad overlaps the column top and is tied to it by a
buried contact: the band is a pass transistor, and `rcs_cond_lat` is a dynamic latch that
takes `rcs_cond` while `clk_tl` is high. Evidence: the pad's lower edge is a much
heavier dark band than its other edges (clean shot, 5.8x); the pad has no other poly
leaving it, so without the tie the metal would end on nothing; and the circuit makes
sense.

**Other reading.** The column top joins the VSS box under the rail to its west (the class
map shows diffusion on both sides of the rail's edge at y 4515-4530, with two dark lines at
x 2998 and x 3018 between them that could be the rail's etch boundary rather than edges),
and a 5 px strip between pad and column measures as field (green; it lies in the margin
of the metal's end, so it may be an artefact). Then the band would be a second pull-down:
`rcs_cond` = NOR(`clk_tl`, `rcs_cond_n`), and the unit above,
NOT(`rcs_cond` AND `clk_tl` OR `rcs_x1`), would reduce to NOT `rcs_x1`: a gate
with a term that can never be true. That is why this reading was not adopted.

**To settle it.** Simulation will not distinguish them easily; find where `rcs_cond_lat`'s
other end goes (poly west along y 4010-4030 from the pad at (3040,4028)): a latch node must
end on a gate.

**Correction 2026-11-18 (`tl2`, Tom Seddon).** The pass transistor's gate is not `clk_tl`: the gate row
y 4535-4558 ends at x 3122, and the gate is `tl3_w3982` (`trace/tla.txt` fixed, 1915f94, fa2a849).
So "`rcs_cond_lat` takes `rcs_cond` while `clk_tl` is high" above is not supported; it is
sampled while `tl3_w3982` is high. The ambiguity itself (the `?B` at the column's top) is
untouched. `rcs_n4200` keeps its `clk_tl` gate (contact (3150,4160)).

**Resolved 2026-11-18, the other way (`tl2` run 4, Tom Seddon; `notes/blocks/tl2.md`, "The top of
`tla`'s column").** The column's top is a diffusion band y 4514-4530 that runs west to R3 and the VSS
contact (2990,4513); a strip x 3009-3019 of the VSS box lies in the open east of R3 and runs into it
without an edge. Between the pad's lower outline (y 4496-4504) and the band (y 4512-4516) the strip
y 4505-4511 reads field (red equal to green) in both metal shots and the chip-2 stripped shot; an
independent review confirmed the field strip and the band. Two of the three reasons for the tie no
longer hold: the pad has other polys (its west arm gates `rcs_bd3330`'s unit; the metal's north end
is on an inverter's load), and the "degenerate unit" argument assumed the gate was `clk_tl`. So the
band of `tl3_w3982` is a second pull-down: **`rcs_cond` = NOR(`rcs_cond_n`, `tl3_w3982`)** (FIRM),
and `rcs_cond_lat` is not a latch node: it is driven by an inverter of `rcs_cond` (AMB-031).
`trace/tla.txt` fixed (d64bc8c: the `?B` removed, the pad's poly ended at y 4504, the column begun
at y 4514).

## AMB-010: is the strip S1 of the row address selector tied to the metal that crosses it at (7207,4955)? (2026-11-16)

`notes/blocks/ras.md`. The metal of `ras_o0_alt2` comes down x 7207 over the left end of
the poly strip S1 (gate `ras_o0_sel2`, y 4945-4970) and ends 45 px further on the contact
(7205,5000) of the diffusion below the strip.

- For a contact: a dark pit at (7207,4955) in the chip-2 stripped shot, and the strip's
  left end is wide enough for one.
- Against: no ring in either metal shot (the contact 45 px below has a plain one); the
  bright spots on the metal there are the stretches between the edge lines of the strip
  and of the diffusion finger above it.

**Adopted: no contact** (assumption). Then S1 is a third pass transistor into `ras_o0`,
gated by a poly that arrives from the north along x 7427. With a contact, gate and source
of S1 would be one net and the device a diode from `ras_o0_alt2` to `ras_o0`. Settle by
tracing `ras_o0_sel2` north and `ras_o0_alt2` north-west: if they turn out to be one net
anyway, the question is moot.

## AMB-011: the units east of the row address selector are taken to be inverters (2026-11-16)

`notes/blocks/rax.md`, "Assumptions". Drawn: one pull-down per unit, gate = selector
output, from VSS to the node that leaves on the unit's second pad (`rax_o#`). Not
traced: the load. Four readings carry the conclusion `rax_o#` = NOT `ras_o#`: one
diffusion under two metals with an unreadable gap between; no contact where the thin
metal x 7902 crosses the output's box; a buried contact at the pad poly's end; a load
somewhere east. **Adopted** because the result is the complement that the central
datapath's comparator needs, found independently. Settle by tracing the unit's east
half and the thin metal's two end pads.

## AMB-012: the units that make R9's compare value are taken to be inverters under a VSS rail (2026-11-16)  (resolved 2026-11-17 but for the `?B` ties)

`notes/blocks/r9c.md`, "Assumptions". Drawn: one pull-down per unit from the output to
the rail x 17440-17495, gate = an RA pad driver's input line. Not established: that the
rail is VSS (not followed to a labelled rail) and that the unit has a load. If the rail
were VCC the device would be a pull-up and `ra#_cmp` would follow `ra#_drv_in` instead of
inverting it. **Adopted: VSS and a load**, by the layout rule (gates under the ground
rail, load towards the other rail). Settle by tracing a unit's east half and following
either rail to a labelled one.

Resolved 2026-11-17 for the load and the rails by `dbus` (Tom Seddon, run 4, `notes/blocks/dbus.md`,
"The loads of R9's compare units"): each unit has a load to the rail x 17616-17667, which is
metal-continuous with `pads_out`'s `vcc`, with its gate tied to the output side (cell `dbus_r9l`).
So the units are inverters and the rail the pull-downs sit under is ground: `ra#_cmp` = NOT
`ra#_drv_in`. Left: `r9c`'s own `?B` at each unit's west end (the tie from the output band to the
poly that carries the output away): unit 1's (17380-17410 x 5440-5470) looks like a buried contact
at 5x in three shots, not measured; the other four not looked at.

## AMB-013: does R9's match line end on the step logic's input `ra_eq_r9`? (2026-11-16)  (resolved 2026-11-17)

`notes/blocks/r9m.md`. R9's match (`ra_eq_r9`) was followed 9,000 px from the comparator
to the middle cluster of the row counter's step logic. Its last metal comes down x 4192
from y 2598 and ends at y 3385 with a 25 px stub west (y 3368-3385, to x 4168). Twelve
pixels further west is the metal x 4148 that ends on the contact (4148,3335) of
`ra_eq_r9` (`trace/tla.txt`), and that metal is itself the end of **another** line of
the same four-line bundle (the one that is at y 2598 at x 4760).

- Reading A: the stub joins the metal x 4148 (the 12 px dark line between them is the
  edge of the poly pad underneath printing through). Then two lines of the bundle are one
  net, `ra_eq_r9`, which makes sense only if their two drivers are meant to be tied
  (a wired AND of two gate outputs), and `rcs_in1` = that AND, gated by `rcs_mv`.
- Reading B: the stub ends on a contact of its own that neither metal shot shows, and
  R9's match goes somewhere not found.

Both metal shots at 5x (`cache/scratch/rax/eq9.png`) and a profile (`--half 1`: metal at
x 4149-4157 and 4169-4196 on y 3376) do not decide it. **Not adopted either way; nothing
drawn.** Settle by tracing the other line (poly y 2595 at x 5400) to its driver: if that
is a second comparator's match, reading A is the design.

Resolved 2026-11-17 (contributor packages `r9m`, `bust`, merged; `notes/blocks/r9m.md`,
"CORRECTION"): neither A nor B. Track P (`trace/tla.txt`, x 4148) is two pieces, broken
at y 3341-3371 (a 30 px run with no metal in either metal shot; measured with the
follower's metal test against known poly crossings). The two poly hops under the metals
x 5078-5127 each step down one track, which an independent review found at 4-5x and the
coordinator saw in the chip-2 stripped shot. With both corrections, **R9's match
(`ra_eq_r9`) reaches the contact (4148,3335): `ra_eq_r9` is R9's match**, by firm
geometry, and `rcs_mu` = NOT R9's match. The stub and the lower piece of track P carry
another line of the bundle (`tc2_o5175`). The earlier statement that `amr` c3's outer output
drives `ra_eq_r9` is withdrawn.

**What follows from it, changed 2026-11-18 (`tl3` runs 8-9, Tom Seddon).** The join stands
(`rcs_mu` = NOT R9's match); what `rcs_mu` gates does not. The transistor under gate `rcs_mu` is a
pull-down of `rcs_mn3852`, not of `rcs_in1`: `trace/tla.txt`'s column `D 4052,3955:4090,4135` ran
through 70 px of field (split, e22fb03), and a diffusion branch of `rcs_mn3852`'s node runs under the
VSS rail onto that drain. So `rcs_in1` = NOT `rcs_mv` (was NOR(`rcs_mu`, `rcs_mv`)) and
`rcs_mn3852` = NOR(`tl3_e3712`, `rcs_in1`, `rcs_mu`). "The row counter steps when the scan line
equals R9, unless `rcs_mv`" is withdrawn. R9's match reaches the step request instead by
`tl3_e3550` = NOR(`rcs_mu`, `tc2_o5175`) and `rcs_e4` = NOR(`tl1_w4678`, `tl3_e3550`), marked on
AMB-032. `rcs_in1` = NOT `rcs_mv` rests on `tl3`'s split of `tla`'s column and on `tla`'s `?D` VSS
land below gate `rcs_mv`, which `tl3`'s reviewer doubts (re-read item R40).

## AMB-014: the gate group that makes `fld_a_in` and `fld_y_b` (2026-11-16)

`notes/blocks/fld.md`, last traced section. Three pull-downs under the rail x 6505-6560 are
drawn from a class map and 3.6-4.6x views in both stripped shots. Not established: that
the rail is VSS; the loads; the two buried contacts (`?B`) that put the two output lines
on their nodes; that the node above the series pair is separate from the rail contact
at y 3905; that the dark spot (6548,4188) is not a contact (if it were, `fld_y_b`'s node
would sit on the rail). **Adopted** as drawn: `fld_a_in` = NAND(`rst_ck`, `tcw_b`),
`fld_y_b` = NOT `tcw_c`. Settle when the region west of the island is traced as a block.

Added 2026-11-16: a poly from the lower pad (6232,3870) of the bus metal `c4l_gab` runs
east along y 3912 and reaches the rail at y 3910-3934, between the rail contact
(6535,3905) and the node of `fld_a_in` (which starts at y 3956 below a strip of field at
y 3948-3956; the clean shot is dull tan at y 3935-3947). If diffusion is continuous
under that poly, `fld_a_in` has a third pull-down gated by `c4l_gab`
(`fld_a_in` = NOT(`c4l_gab` OR (`rst_ck` AND `tcw_b`))); if the poly only passes over
field there, it goes on to the east side. Not decided; the trace stops the poly at the
rail's west edge.

Checked by colour the same day (clean shot, rows under the rail x 6514-6546, with the
known poly-over-field crossing of `tcw_b` at y 3641-3650 for comparison: salmon, about
(217,165,115)): at y 3911-3932 there is **no salmon row**; the middle of the rail is
tan-green there (the contact box reaches down to about y 3925). Across the rail at
y 3920 the bright salmon of the poly is at x 6480-6489 only, then dark, then the box. So
the poly **does not cross the rail and gates nothing under it**: the third pull-down is
out. It ends at the rail's west edge, 30 px above the end of `fld_a_in`'s poly. What it
ends on is open: if on the same node as `fld_a_in`'s poly, the bus net `c4l_gab` *is*
`fld_a_in` (and `tcw_o3550` its inverse). Not drawn; next thing to read there, at 5x in
the chip-2 stripped shot.

Updated 2026-11-17 by `tcw` (run 2): the loads of `fld_a_in` and `fld_y_b` are traced
(`trace/tcw.txt`, on the east rail, as the assumed supply assignment requires), and
`fld_a_in` has a third pull-down, gate `tcw_o3820` (a latch with `tcw_o3820`). Still open:
whether `c4l_gab`'s poly (ending at the rail's west edge at y 3912) is on `fld_a_in`'s node.

Updated 2026-11-18 by `tc2` (dp111): `fld`'s VCC rail is joined by drawn metal to `tcw`'s, and its VSS
rail to `tc1`'s east ground rail. The supply identity of both is still by the layout rule.

## AMB-015: three joins on the east side of the gate column's middle stretch (2026-11-16)

`notes/blocks/tcw.md`, "Stretch B, east side". All three are in the trace as `?` items:

1. **The two output nodes at y 3326 and y 3437 are one** (`tcw_o3326`, alias
   `tcw_o3437`): a 24 px strip x 6588-6612 between their arms. Evidence: an outlined band
   there in both metal shots; in the chip-2 stripped shot it is plain tan (that shot's
   diffusion colour) while the two gate-poly ends beside it are orange; in the chip-1
   fringed shot khaki. Against: the clean shot's class map gives the neighbouring strip
   (x 6582-6598) as field with a line of poly on its west side, which would instead join
   the two gates' east ends (and with them two bus metals); the two readings differ by
   one strip's width, at the resolution limit.
2. **The inverter at y 3519 has a load** whose gate (block (6625-6680, 3540-3570)) is tied
   to the output at its west end. The block and the arm under it are plain; the tie is
   placed by analogy with the gate above.
3. **Its output leaves on the bus metal `tcw_m6362b`**: the node's west end meets the end
   of the poly from the pad (6385,3567). Both ends are seen (class map); the buried
   contact is not.

**Adopted as drawn.** With them: `tcw_o3550` = NOT `c4l_gab`, and it is the middle gate
of the first stack. Settle 1 with a profile across the strip in the chip-2 shots at
several y, and by finding the load of `tcw_o3326` (one load or two decides it).

Profile done the same day (sum of red minus green over the two chip-2 shots, 4 px
steps, x 6556-6626, at y 3345, 3365, 3380, 3395, 3415, 3440): the strip x 6594-6602 reads
as diffusion at every height; the space between the two gates' east ends (x 6572-6576,
y 3365-3395) reads as **field**, so the gates are not joined to each other (the
alternative reading is out). Still open: at y 3440 a dark line (x 6580-6588) lies between
the lower arm and the strip, and a dark line cannot show whether two regions meet. So
item 1 stands as "a diffusion strip runs between the two arms; that it joins them is
assumed".

Note 2026-11-17 from `tcw` (run 2): the tie of `tcw_o3550`'s load is probably a tab up to a box
at (6585-6650, 3495-3520) rather than the `?B` at the block's west end; the same net either way.

Updated 2026-11-18 by `tcw` (run 3): the first item (the strip joining the output arms at y 3326 and
y 3437) is supported again (`px.py row 3340`, `row 3390`: red minus green 19-33 at x 6596-6604
between dark edges) and stays `?`; the gate's equation `tcw_o3240` now rests on it. "The top node,
whose connection is not found" is settled: it is the output `tcw_o3240`.

## AMB-016: two buried contacts in the gate column's top stretch (2026-11-16)

`notes/blocks/tcw.md`, "Stretch A". (1) Pair 1's output arm to the poly of the pad
(6355,2830): makes the output the bus net `tcw_m6362a`. (2) Pair 2's output arm to the
C-shaped poly: makes `tcw_o2993` the first gate of pair 3. In both the class map shows
an arm of open diffusion reaching west from the node to where a poly ends; the contact
itself is not resolved (`?B`). **Adopted.** `tools/unsure.py` lists the first (two
labels); the second has one label and is not seen by it.

## AMB-017: what drives `cnt_gab`, the counters' `_m`/`_mb` transfer gate line (2026-11-17)

`notes/blocks/ral.md`, "Where `cnt_gab` is driven". The net as drawn: `wl`'s band H4 (poly
y 7200-7225, x 11043-12910), the counters' line x 12902 (y 7200-16943), the metal from
`wl`'s contact (11392,7210) north to the cross-under, the metal y 4287, and the line
y 4354 through the five `ral` cells, where it gates one pull-down per cell. Every end was
looked at and every stretch scanned for contacts (G minus R in the clean shot, then 3.4-4x
views): no gate output drives it, and nothing ties it to a supply.

- Reading A: a contact the colour test misses, under wide metal (for instance where the
  north branch passes under the supply metal x 11280-11600).
- Reading B: it is driven inside the `ral` cells' untraced part (inverter 1's region).

No assumption adopted. Settle by tracing `ral`'s inverter 1 (B), then by single shots at
5x under the supply metal (A).

Updated 2026-11-17 by `ral` (dp111): **reading B is struck**: inverter 1 is traced and nothing in
the cell drives `cnt_gab` (`ral_n1` = NOR(`ral_a`, `cnt_gab`): `cnt_gab` is a force input).
A line that forces every RA output high cannot pulse each character, so either it is low in
normal use, or band H4 and the line x 12902 are not the counters' per-character transfer line
that `wl` and `mra` took them for. The routes from the cells to H4 were re-read and are right,
so the question is H4 and x 12902 themselves.

## AMB-018: the `ral` cell: latch, and its device sizes (2026-11-17)  (resolved 2026-11-17)

`notes/blocks/ral.md`; copies in `trace/ral.txt` (RA0-RA4) and `trace/mal.txt` (MA0-MA13).
Traced: a pass transistor from the input to node a on the strobe (`ral_stb` for RA,
`ck_out` for MA), a long hold device (gate VSS) from node a to the output, a pull-down
on `cnt_gab` (RA) or `mal_frc_m#` (MA), and inverter 2 (output = NOT `ral_n1`).
Inverter 1 (node a to `ral_n1`) is not drawn after three passes.

- Working belief (not extracted): `ral_n1` = NOT node a, so the cell is a static latch,
  transparent while the strobe is high; every MA output latched while CLK is low.
- Possibly `ral_n1` = NOR(node a, `cnt_gab`), making `cnt_gab` a force on the latch.

Device sizes: re-read item R14. Settle inverter 1 with single shots at 5-6x of
x 14195-14300, y 4280-4460 in copies s1 and m4.

Resolved 2026-11-17 by `ral` (dp111): inverter 1 traced, `ral_n1` = NOR(`ral_a`, `cnt_gab`) (MA
copies: NOR(`ral_a_m#`, `mal_frc_m#`)), so out = node a OR force line: a static latch,
transparent while the strobe is high, forced high (and set, through the hold device) by the
force line. FIRM for all 19 copies. Sizes corrected in the cell: inverter 2's pull-down 199/22
(the whole Z poly is gate), its load 60/37, the pass transistor 68/25, Tf 94/20 (R14 done).

## AMB-019: the data bit lines 0-4 through `cdp1`'s rows D/E, y 5542-5596 (2026-11-17)

`notes/blocks/rde.md`, "The five lines through rows D and E". On each of the five bit lines
(x 8856 + 390 k, k = 0..4) the bright metal fades out at y 5540-5547 and comes back at
y 5593-5600; about 12 px across a thin dark bar (y 5557-5567) cannot be seen in any shot.

- Reading 1 (adopted, drawn `?M`): the line narrows to about 10 px to clear the next
  track's contact pad, and is continuous. Then R11 is written from bits 0-4 and R10 from
  bits 0-6, as the datasheet says.
- Reading 2: a long contact from the line to the diffusion column below it (row E's tap).
  Same net.
- Reading 3: two pieces, each contacting the column either side of the bar, with the bar
  a gate: a transistor in series with each bit line. The joins would be wrong.

The contributor's review leaned to continuous (about 80 %); the coordinator's look at 4x
in two shots agrees that it cannot be seen. Settle by tracing row E's cell. The `cdp2`
bus names are aliases, not renamed.

## AMB-020: is the inverter `tc1_o4280` on the `tc1_x1` line? (2026-11-17)

Proposed by `tc1` (Matt Godbolt, `notes/blocks/tc1.md`). `shm` draws `tc1_x1` as NOT `ras_o0_sel1`
(inverter and load at x 8400-8650, y 4165-4280, joined to the `tc1_x1` poly through a `?B`).
1,500 px west, `tc1` finds the inverter `tc1_o4280` = NOT `tc1_p4308`, whose output strip runs up
to a pad at (6962,4268). A branch of the ring poly of the driver `tc1_o4020` (on the `tc1_x1`
line by firm geometry) ends on that pad, and the pad's contact puts the thin metal x 6968 on it.
Three joins: J1, **not drawn**, strip to pad (x 6934-6957); J2, drawn `?P`, branch poly to pad
(6972-7000, 4254-4272); J3, `shm`'s `?B` at about (8370-8410, 4240-4270), not looked at. All three
true would mean two complete inverters on one line. The thin metal x 6968 is also one input of
the second driver `tc1_o3740` (firm, contact (7009,3789)), whose output does not return to
`tc1_x1`; and the pad's net has a second destination west, the poly row y 4385-4405. **No reading
adopted**; J1 is left out so that `tc1_x1`'s equation does not change on a guess. To settle: J3
in the clean shot (a re-read under R12), the thin metal x 6968's other ends, `tc1_p4308`'s
source. Open join `tc1_x1_u`.

Updated 2026-11-17 (evening). `tc1` is done (runs 10-11): twice in its gate column a small gate's
output runs up to a contact of a line a larger gate already drives (`tc1_o4280` on `tc1_x1`;
`tc1_o2950` on `tc1_o3740`, the notes' J5), and both joins are left out; if one is ever shown,
the other becomes likely. J4 and J6 are drawn `?`. Then `tcw` (run 2) found that the row
`tc1_x1_u` (y 4383-4401) is the output of `tcw`'s last inverter, `tc1_x1_u` = NOT `tcw_m6362c`.
Because `trace/tc1.txt` aliases `tc1_x1_u` to `tc1_x1` (through J2, `?P`), the extraction now
gives **`tc1_x1` = NOR(`ras_o0_sel1`, `tcw_m6362c`)**: two inverters with their outputs on one
line, i.e. a wired NOR with two loads (DEPENDS: without the `?` items it falls apart). Either
that is the design, or J2 (or `shm`'s `?B`, J3) is wrong. First to re-read: the joins at `tc1`'s
pads (6962,4268) and (6968,3905).

Updated 2026-11-18: `tc1_x1` has a further gate, an input of `tc2_o5175` (`tc2`).

## AMB-021: a contact from pin D6's input line to the `d0_out_n` inverter? (2026-11-17)

Proposed by `dbus` (Tom Seddon, the notes' Ambiguity 9). A possible contact between `d6_in`'s
metal (x 17290-17306) and the box 17294-17328 x 16474-16502 at the west end of the output node
of the inverter that drives `d0_out_n`. For: the metal is dim over y 16476-16512 in both chips
(R at most 160 and 141 against 200-226), deeper than over any buried-contact box on the same
line. Against: no pad, no bright centre, no specks; the clean shot is field colour under the
metal's west edge all the way; a contact would tie pin D6 to `d0_out_n`. Unexplained: the box's
interior is black in the chip-2 stripped shot. **Assumed: no contact**; nothing drawn. To
settle: a better photo of the spot, or behaviour (D6 and D0 would interfere on reads).

Updated 2026-11-17 (evening) by `dbus` run 7 (Matt Godbolt) and an independent reviewer: read by
two more readers side by side with chain 7's buried boxes (y 15975, 16130) and the real pad
(17297,16662) on the same metal. The box has none of a contact's marks (no pad, no bright centre,
no pit in the clean shot), the metal's west edge line is continuous through y 16480-16512 in both
metal shots, and the structure matches the pass-overs at y 15958-91 and 16110-43. **Assumption
(no contact) kept, now three readers.** Another look at these photos will not settle it.

## AMB-022: the gate `rcs_iso2958` on `rcs_u3425` (2026-11-17)

Proposed by `tla` (dp111). A second transistor on `rcs_u3425` at (2959,3481): `rcs_u3425` =
NOR(`rcs_bc3460`, `rcs_iso2958`) as drawn. Its gate poly x 2950-2968, y 3449-3547 has no
connection found; its top end (2959,3447) abuts `rcs_u3425`'s diffusion with a single edge line
between. A tie there would make the gate `rcs_u3425` itself (a device that pulls its own gate
node, which does nothing useful). **No reading adopted.** To settle: the poly's other end, or a
profile across (2959,3447) against known buried contacts.

## AMB-023: buried or metal contact under `amr` c0's outer line (2026-11-17)

Proposed by `amr` (dp111). At (11601-11628, 6286-6307) a box under the outer line of column c0.
Measured against known buried and metal contacts, it is a **buried contact** on `amr_eq_r3`'s
diffusion line; a metal contact would make c0's compared bit (`c4l0`) the comparator's own output.
**Assumed: buried** (measured; `notes/blocks/amr.md`). It corrects #14's lead of a "third
connection" of c0's outer line.

## AMB-024: the wide NOR of `rcs_e4` across R1's west edge (2026-11-17)

Proposed by `tl1` (dp111, `notes/blocks/tl1.md`). The diffusion of the wide NOR that drives
`rcs_e4` crosses the west edge of rail R1 at x 2600, where an etch line sits on the rail's edge,
so its continuity is not seen directly. **Drawn firm.** A break would cut the output contact off
from the load. To settle: the spot in both chip-2 shots, or the load's other connections.

## AMB-025: the source of `tl1_w4678` (2026-11-17)

Proposed by `tl1` (dp111). A tan box (2553-2573, 4655-4690) under the metal x 2557-2573 is either
the end of a buried contact or a pass transistor gated by `rcs_x1`. In the second case
`rcs_e4`'s first input (`tl1_w4678`) is a latched value. Two passes, **not resolved; nothing
adopted**. Also open there: whether thin metal W contacts `tl1_w4678` near (2693,4688) (a widened
head, no ring in either metal shot; not drawn).

## AMB-026: the load-plate ties of `tl1`'s two latches (2026-11-17)

Proposed by `tl1` (dp111, third run). Four boxes, (2673-2697, 4622-4648), (2683-2708, 4500-4524)
and both 608 px higher, tie the load plates of the two cross-coupled pairs in the west column
(cells `tl1_ub`, `tl1_ua`). They have a buried-contact look (the same colour gradient as two
known buried contacts of the column; interiors 12-15 px) and are drawn `?`. The four latch
equations and the cross-coupling's last step rest on them (marked in `operation.md`); every
pull-down is firm, and the cross-coupling paths were seen in both copies independently. Thin
metal W lies over the lower ties, dark for 38 px, neither metal nor bare ground; W's pieces are
not drawn. To settle: profiles of the boxes against known buried and metal contacts.

Updated 2026-11-17/18. The same ties occur in every copy of the cells: `tl3`'s latch A at
(3715-3745, 3375-3400) and (3713-3737, 3492-3522), **in the open** (no thin metal over them), so
the chip-2 shots at 6x there may settle the tie for every copy (`tl3`'s reviewer's
`cache/scratch/tl3/review-1/mid3.png` shows heavy boxes at both, which fits the drawn reading);
`tl4`'s latch at (4801-4821, 4186-4216) and (4806-4834, 4065-4086), not readable there either;
`tl5`'s three latches and three inverters. In `tl1`, thin metal W over the three `tl1_ub` tie boxes:
the clean shot under W has contact-hole colour (red minus green -4 to +12, against about 30
where W surely passes over) and the metal is dark for 34 px with no bare ground; a contact would
join three latch outputs, a cut has no bare ground, a pass-over contradicts the clean shot.
Undrawn.

Updated 2026-11-18. More copies of the ties, all `?`: `tl4`'s second latch (y 3225-3765), where the
ties carry the cross-coupling and the inverter's output (each signal is taken from a load's plate);
`tl3`'s latch C ((3949-3977, 4673-4694), (3963-3987, 4794-4824)) and three more in `tl3`'s east
column; `tl2`'s inverter of `rcs_cond` (AMB-031); `lc1`'s latch D (the cell's tie, inherited). The
ties are not unreadable only because of the thin metals: `tl3`'s unit E1 has its tie in the open and
both chip-2 shots show a 7 px dark wall between the tab's box and the tail.

## AMB-027: the two `?P` joins of `tc2`'s set/reset latch `tc2_sr` (2026-11-18)

Proposed by `tc2` (dp111, `notes/blocks/tc2.md`). The latch at x 7760-8250, y 5960-6300 (reset
`cdp1_lw1`) is cross-coupled through two joins drawn `?P`, dark in every shot; the evidence is edge
lines and the opening of the buried contact's rings. The latch rests on them (marked, not firm).
`q_n`'s join to its pad poly is one of them. **Drawn `?P`.** Not resolvable in these photos.

## AMB-028: `tc1_ns3`'s metal over `rax`'s five boxes, and `cdp1_lw1` through `rax` (2026-11-18)

Proposed by `tc2` (dp111). (1) `tc1_ns3`'s metal crosses `rax`'s five unit boxes; drawn `?M` at the
five crossings, resting partly on the electrical argument (as AMB-011). (2) North of (8031,5468) the
follower takes `cdp1_lw1`'s thin metal 440 px through `rax`'s units 3-5 over six contact-like spots,
while `rax`'s own profile says short straps: nothing drawn there. (3) `tc2_rxl`'s load tie (box
x 8021-8048, y +38..+61 per unit) is under metal in units 2-4 and flush under the band in units 0
and 1 (consistent, not proven); it decides the load's gate, not the equation. Also seen once: the
box (8355-8385, 4835-4865) at the end of `sl_eq_r5_n`'s L, read as a buried contact onto diffusion at
`cdp1`'s west edge.

## AMB-029: the feedback of the pair `rcs_n4200` / `rcs_bd3330` through one load tie (2026-11-18)

Proposed by `tl2` (Tom Seddon, `notes/blocks/tl2.md`, Ambiguity 17). Firm: piece 2's node is
`rcs_bd3330` (buried contact (3048-3072, 4362-4390); two readers), and `tl2_w4260` is one poly, the
gate of piece 2's load and the west gate of `rcs_n4200`'s third pull-down. Assumed: the tie box
(2926-2950, 4298-4334; heavy outline, paler centre, four shots, not resolved at 10x) joins that poly
to the node, which makes the pair cross-coupled: `rcs_bd3330` = NOT(`rcs_n4200` OR (`clk_tl` AND
`rcs_cond_lat`)), `rcs_n4200` = NOT((`clk_tl` AND `rcs_cond`) OR `rcs_x1` OR `rcs_bd3330`). For: the
poly has no other end; without the tie two gates hang on an undriven net. Also in `tl2.md`: the
node crosses a 24 px gap between two metals at (3006-3032, 4390-4403), drawn firm (two readers);
`tla`'s VSS arm y 3818-3836 reads field-like in the chip-2 stripped shot, left as drawn (Ambiguity 18).
Updated 2026-11-18 (`tl2` run 4): with `rcs_cond_lat` = NOT `rcs_cond` (AMB-031) the pair reads as a D
latch for `rcs_cond` on `clk_tl`, with true and inverted data, open while `clk_tl` is high.

## AMB-030: `tl3`'s vertical gate under the rail joined to the lower unit's load-plate arm (2026-11-18)

Proposed by `tl3` (Matt Godbolt). A vertical poly x 3690-3712, y 4097-4196 (a second pull-down on the
upper node) and the buried-contact box of the lower unit's plate arm have only dark lines between
them for 10-12 px in all four shots at up to 6.6x. **Drawn joined, `?P 3704,4182:3728,4204`.** For: no
two polys lie that close elsewhere here; the poly runs 43 px past its channel with no other use;
without it the gate floats and the lower NOR drives nothing; with it the pair is a set/reset latch;
the poly's east edge steps east at the arm's level in three shots. Against: nobody has seen poly
continuous through the box's ring. `tl3_w3803` = NOR(`tl3_w3939`, `tl3_w4243`) rests on it. `tla` has
the mirror image of this pair east of R3 (`rcs_u3425` and `rcs_b1`); in `tl3`'s mirror the box that
`tla` could not place carries the poly to a metal pad, so these boxes are part of the unit's
pattern and are used or not per copy.

## AMB-031: `rcs_cond_lat` is `tl2_w4080` only through a load tie (2026-11-18)

Proposed by `tl2` (Tom Seddon, run 4; `notes/blocks/tl2.md`, Ambiguities 19 and 22). The inverter of
`rcs_cond` between R2 and R3 at y 4005-4145 has its node `tl2_w4080` under thin metal E; its load's
plate is one firm poly with `rcs_cond_lat`'s row, pad and metal. The two are joined only by a
heavy-outlined box below the plate (x 2872-2900, y 4113-4141), drawn `?P`, `?D`, `?B`: that the
plate's tab enters the box and that the diffusion under it joins the node's strip 7 px east are read
from shape and place. **Aliased (`@alias rcs_cond_lat tl2_w4080`), not renamed.** For: the node has no
other exit and `rcs_cond_lat` no other driver. If wrong, `rcs_cond_lat` is driven by nothing and
`tl2_w4080` drives nothing. Rests on it: `rcs_cond_lat` = NOT `rcs_cond`, and AMB-029's reading as a
D latch. The name `rcs_cond_lat` is kept until the tie is settled (it is no latch node; `tl2`
suggests `rcs_cond_inv`).

## AMB-032: is the middle cluster's thin metal x 3948-3962 one metal? (2026-11-18)

Proposed by `tl3` (Tom Seddon, runs 6-9; `notes/blocks/tl3.md`, Ambiguities 6 and 11). The thin metal
runs from a pad on the load plate of `tl3_e3550`'s unit (3930,3614) to a pad on `tl1_w4937`'s row
(3953,5458). **Assumed one metal, drawn with six stretches `?M`** (over load-tie boxes at y 3775-3826,
4272-4325, 4450-4497, 4668-4691, 4778-4810, 5098-5148), where neither metal shot shows metal for
14-38 px; names gathered by alias (`tl3_tm3955`, `tl3_tm3955_u`, `tl1_w4937`). For: two real end pads
and no pad or widening between; metal brightness everywhere else; the signature is trap 22's
pass-over; `tools/tl3_thin.py` separates these stretches (14-38 px, all over tie boxes) from the
8-13 px bars of plain edges. Against: at y 4455-4492 nothing at all for 38 px, and a greenish band
across in the clean shot; the spot (3955,4541) over latch C's inverter node is taken as a pass-over
(two reviewers). Also assumed: the plate's tie to `tl3_e3550`'s node (`?`, AMB-026's kind). **Rests on
it: `rcs_e4` = NOR(`tl1_w4678`, `tl3_e3550`), i.e. R9's match in the row counter's step request**
(AMB-013). Would settle it: a third chip's metal shot; the simulation.

## AMB-033: is the middle cluster's thin metal x 4099-4111 one metal, without a contact on the way? (2026-11-18)

Proposed by `tl3` (Matt Godbolt run 5, Tom Seddon runs 8 and 10; `notes/blocks/tl3.md`, Ambiguities 1,
12 and 13). The thin metal runs from a pad with a contact (4103,2899) on the row y 2899 to track A
(`rst_ck`). **Assumed one metal, no contact between its ends; six stretches drawn `?M`** (over node
boxes at y 2964-3021, 3381-3444, 3527-3574, 3686-3748, 3771-3969, 4051-4108), where neither metal shot
shows it for 40-55 px. For: two real end pads (full-bright centre 12 px across, green hole) and
nothing pad-like between; the row y 2899 has only gates on it, so its driver must arrive by this
metal; a contact on any box would short a unit's output to `rst_ck`; an unbroken pink protected strip
beside the line in the clean shot where one side lies over field. Against: small bright centres over
four boxes ((4104,2988), (4101,3719), (4102,4074), (4101,5202)). The most contact-like is (4102,4074),
on `rcs_in1`'s box (clean shot 186/182/139, neither a contact's green nor a pass-over's tan): a contact
there would make `tl3_e4243` constant; one at (4101,5202) would make latch C's data its own enable;
one at (4104,2988) would make the metal E1's second output. `rst_ck`'s source is not traced, so four
of the six have no electrical cross-check. **Rests on it: `tl1_w3594` = `rst_ck`** (`tl1`'s two latches
in series a master and a slave on `rst_ck`). Since `eof` run 2 (2026-11-19) `rst_ck` is `rst_ck` (firm), so `tl1_w3594` = `rst_ck` rests on this entry, and
`rst_ck`'s source is known: the cross-check this entry lacked is now possible from the driver's side. Would settle it: `rst_ck`'s source; a third chip's metal
shot; the simulation.

## AMB-034: three ring-like marks in `tl4` not drawn as contacts (2026-11-18)

Proposed by `tl4` (Matt Godbolt, runs 6-7; `notes/blocks/tl4.md`, Ambiguities 4-7 and 10). (1) The
heavy box at (4684,3420) under the metal of `tl4_w3245`: bright centre in a dark ring in both metal
shots, no hole in the clean shot, no pits in the chip-2 stripped shot; drawn as an uncertain lobe of
`tl4_w3390`'s diffusion, no contact. A contact would short `tl4_w3245` to `tl4_w3390`, which the rest
of the latch contradicts; what the box is for is not known. (2) A mark at (4683,5767) on RA's leg,
in both metal shots, right over the row of `bd1_n2`; no hole under it in either stripped shot, so
not drawn; a contact would tie `bd1_n2` (and `rcs_e3`'s input) to VSS. (3) The field box
(4722-4752, 3442-3488) under RA (an elongated ring in both metal shots): perhaps a substrate contact
of RA; not drawn (no poly, no diffusion). The lesson (a metal about 25 px wide over a box shows a
bright centre in a dark ring; the clean shot's hole decides) is trap 26.

## AMB-035: `tc2_o5175` reaches the gates of `tl3_e3550` and `tl3_e3712` only through `r9m`'s stub join (2026-11-18)

Proposed by `tl3` (Tom Seddon, run 7). The two gates are on the south end of `tla`'s lower piece of
track P (pad (4148,3592)). That piece is `tc2_o5175` (`r9m`'s line 3) only through `r9m`'s stub join at
y 3376: 5-6 px of dark, taken there as an edge under continuous metal (AMB-013's stub). If the join
is wrong the two gates are on an unnamed track piece with no driver. Rests on it: `tl3_e3550` =
NOR(`rcs_mu`, `tc2_o5175`), `tl3_e3712` = NOT `tc2_o5175`, and so `rcs_mn3852`'s first input.

## AMB-036: `rdp3`'s contact (13736,12826) on R4's match path (2026-11-19)

Proposed by `eof` (Tom Seddon, run 1). The top of track L9 on the east pad of the poly link y 12826:
ring and bright centre in both metal shots, the metal ends on the pad, a pale patch in the chip-2
stripped shot; but the clean shot shows a mottled red centre and no green hole (the link's west pad
has the usual hole). Tracer and reviewer both read a contact. **Drawn as a contact (as `rdp3` drew
it).** If it is not one, R4's match (`rc_eq_r4`) does not reach `bd1`'s latch and inverter A.

## AMB-037: `rst_ck`'s staircase over other nets without contact (2026-11-19)

Proposed from `eof` run 2 (`notes/blocks/eof.md`, Ambiguities 5-7) and `lc2` (its Ambiguity 3). The
metal that carries `rst_ck` from `trunks`' line S north to the top-left logic lies on other
nets' poly at four places, and `lc2`'s metal x 6422-6440 lies 64 px along latch C's data poly
(6431, 8117-8181); none is drawn as a contact (trap 13; read from text maps by two packages). A contact
at the first would join `rst_ck` to latch D's output `lc1_w7040`; the one in `lc2` would join it to
latch C's data `tl3_w3982`. The join to line S also rests on `trunks`' reading of that line (R4).

## AMB-038: the box at (7535-7580, 13903-13940) under `cdp4_ld`'s metal (2026-11-19)

Proposed by `busl` (richtw1, run 4; its Ambiguities 9 and 10). At the west edge of `cdp4`'s bottom-left
gate group. `cdp4_rst`'s poly ends on its west outline; the metal of `cdp4_ld` / `bc1_ld_a` (x 7556)
passes over its middle and is not seen in either metal shot for 51 px (y 13898-13949; drawn `?M`).
Readings: (a) a buried contact from `cdp4_rst`'s poly onto the group's node diffusion, the metal passing
over without contact; (b) a poly pad with a metal contact, making `cdp4_rst` and `cdp4_ld` one net;
(c) a metal contact onto the diffusion. **Assumed (a)**: heavy outline and plain inside, unlike the
contact pad at the other end of the same poly; no bright centre in chip 2 and no green hole in the
clean shot. Against: a 9 x 10 px spot at (7557,13929), at ground brightness in chip 1's metal shot and
greenish in the chip-2 stripped shot, without a ring. `cdp4_ld` = `bc1_ld_a` holds under every reading
(a metal does not end without a contact). Settled by tracing the gate group (`cdp4` (continue)): if the
node the box sits on is a gate output with the selects as inputs, (a) is right.
**Resolved 2026-11-20 as reading (a)** (`cdp4` run 2, Matt Godbolt): the group is one gate, `cdp4_rst` =
NOR of the six select rows with one load, and the box sits on its output diffusion (the column's west
edge line is absent at y 13912-13930 in three shots; tracer and reviewer); `cdp4_rst`'s poly ends in it
as a tongue, and the east box of the same gate, with no metal near it, has the same look. `cdp4_rst` had
no driver before; readings (b) and (c) would now put two drivers on one net. Drawn in `trace/cdp4.txt`.
Still uncertain: `busl`'s `?M 7556,13895 y13953` itself is not seen in either metal shot (the reviewer
could not check it either), so `cdp4_ld` = `bc1_ld_a` rests on it as before.

## AMB-039: `ck_out`'s track over the poly row y 13744, at (7145,13728-13749) (2026-11-19)

Proposed by `busl` (richtw1, run 6; its Ambiguity 13). Neither metal shot passes the metal test for
22 px along the track where it crosses this undrawn row (the other rows it crosses give 8-13 px edge
bars): chip 2 shows a dark patch with no bright centre, chip 1 a dim reddish stretch. Readings: (a) a
plain crossing with marks on the metal; (b) a contact, which would put `ck_out` (the enable of latch
D) on the row y 13744, which runs from west of x 6500 to a gate band of `cdp4`'s corner gate group.
**Assumed (a), drawn as a plain metal**: neither the metal nor the row is widened (every contact in the
field has a pad), the clean shot shows protected poly with no hole, the chip-2 stripped shot reads as at
the plain crossing 60 px north; tracer and reviewer agree. Against: both chips are dim at the same spot,
which dirt on one chip does not explain. Settled by the far ends of row y 13744 (`busl`) and the corner
gate group (`cdp4` (continue)).
**2026-11-19, later**: `regs` (run 3) reads row y 13744 as the read select of R13 (`rsel13_buf`), tapped at
(6492,13744) from the track x 6494 (read, not drawn). Under reading (b) latch D's enable would be on a
register read select: a further reason for (a). Still open until the row is drawn.
**2026-11-20, later**: the row has a second dim crossing, `busl_x7122`'s track 87 px west (AMB-045); the resolution below stands.
**2026-11-20**: `cdp4` (run 2) drew the row's east end: it is gate 2 of the NOR that makes `cdp4_rst`,
with no other contact (the open join `rsel13_buf`). Under reading (b) latch D's enable would also be an
input of `cdp4_rst`. Not settled: the row west of x 7550 is `busl`'s and is not drawn.
**Resolved 2026-11-20 as reading (a), a plain crossing** (`busl` run 8, richtw1; reviewed, no findings):
its "settled by" is met from the other direction. The row y 13744 is drawn end to end: it has a driver
of its own, `rsel13_buf`, through a pad with a contact at (6495,13744) on the track x 6494, and ends in
gate row 2 of `cdp4`'s NOR. A contact at (7145,13738) would short latch D's enable `ck_out` to R13's
read select, two driven nets. Nothing new was read at the crossing itself.

## AMB-040: the structure at x 10530-11400, y 11740-12350 on the write strobes of R12 and R14 (2026-11-19)

Proposed by `regs` (Matt Godbolt, run 1; its Ambiguities 1). In `bw`'s region, undrawn: a wide
diffusion-coloured rectangle x 10530-11400, y 11915-12185 with seven contacts at x 10540 and two
mirrored units at its east end (plates y 11838-11893 and 12205-12260, a strip from the top unit north to
y 11757 and east along y 11748, a U-shaped strip below the bottom unit). `wr_r12`'s metal has a contact
at (11378,12297) onto the bottom unit's box (drawn); whether `wr_r14` has the mirror contact at
(11331,11810) onto the top unit's is open (drawn `?C`; the photos lean against it); `wr_r12`'s metal over
the top unit is `?M` (x 11376, y 11757-11905), so `wr_r12` = row C's write line is marked. Readings and
what would settle them: `notes/blocks/regs.md`, Ambiguities 1. Settled by tracing the structure (`bw`
(continue)).

## AMB-041: the reset copy's track over latch C's data row, at (6558,7886) (2026-11-19)

Proposed by `eof` (Tom Seddon, runs 10-11; its Ambiguity 33). Where `rst_a`'s track x 6558 crosses the
poly row y 7878-7898 the clean shot has a hole-like olive patch (32 px, red minus green down to -3). The
row is `tl3_w3982` (latch C's data), so a contact there would short the reset copy to it. **Assumed: no
contact** (the tracer and two reviewers, rounds 12 and 13): no ring, bright centre or pad in either metal
shot, no pitted box in the chip-2 stripped shot, and the patch is wider than the metal. Against: on the
same row the pad (6513,7889), a real contact, shows no green hole in the clean shot either (the row's
colours there are abnormal from x 6500 to 6840), so the clean shot decides nothing on this row.

## AMB-042: the ripple counter's clock on `rst_c`'s poly, x 6466-6478, y 8945-9227 (2026-11-19)

Proposed by `eof` (Tom Seddon, run 13; its Ambiguities 43-45). Piece `ck5`'s metal (the clock of the
left-centre ripple counter, `lc3_w9947` = the wire `tcw` called m6404) lies on `rst_c`'s poly for 225 px (y 8945-9172),
and its corner stands 35 px north of the pad (6469,9209) of `rst_c`'s own metal on the same x. Readings:
(a) two nets, no contact along the overlap and two metals at the knot; (b) a contact or one metal, which
would make the ripple counter's clock the reset copy. **Assumed (a)**: no ring, widening or dark stretch
along the overlap in either chip; at the knot 27 px without metal in both chips north of the pad's
centre against a 13 px ring on the south, where the pad's own metal leaves. A dull patch at (6471,9045)
(clean shot dull over x 6456-6495, wider than the poly; chip 2's metal dim for 9 px, chip 1's whole) is
read as a stain. Three nets depend on it (`lc3_w9947`, `rst_c`, `lc1_w7170` = NOT `rst_c`). Settled by
the driver of the clock (`eof`: the row y 14784 east of x 7550), which must not be the reset.
**Resolved 2026-11-20 as reading (a)** (coordinator, from `eof` runs 15-18): the clock's driver is found
and is not the reset: `lc3_w9947` = NOT `eof_w15127`, an inverter on one side of a set/reset latch in the
bottom-centre logic (set by `eof_w15172`, cleared by `ck_out` AND `bc2_w15607`, or by `rst_a`). Every
other end of the net is a gate. Under reading (b) that inverter and `rst_c`'s driver would share a net.
The inverter's and the latch's equations are marked for load ties only.

## AMB-043: `eof`'s clock latch (units V, W): the stacks' diffusion in the open gap drawn against its colour (2026-11-20)

Proposed by `eof` (Tom Seddon, run 16; its Ambiguity 53). x 8742-8777, y 15160-15400, the 35 px open gap
between column B's rail and a thin metal in the bottom-centre logic. Edge lines in both metal shots and the
chip-2 stripped shot say both stacks' diffusions run through the gap (no edge across rows A, B, 1, 2;
single edge lines; a doubled line along row C's top west of x 8757, where the boundary turns west to the
rail). The colour of the three bands between the rows says field (stripped shot red minus green 2-11
against 19-25 for diffusion in the same gap; the clean shot likewise). **Assumed: diffusion** (drawn so;
two reviewers and the tracer on the edges). If field after all: each stack is two fingers (no equation
changes), except that the part between rows B and C under the thin metal would float and the `rst_a`
transistor would lie in series with V's input gates between the two nodes, so that the reset would clear
the latch only while `eof_w15172` is high. The equations at stake: `eof_w15127` = NOT(`eof_w15172` OR
`eof_w15300`), `eof_w15300` = NOT((`ck_out` AND `bc2_w15607`) OR `eof_w15127` OR `rst_a`), and through them
the ripple counter's clock `lc3_w9947`. **2026-11-20, later** (`eof` run 23): the bands were classed by
colour without a control band, and a like band elsewhere read both ways from single rows (trap 38): the
colour evidence is to be measured again with a control (Re-read item R49). What would settle it: that
measurement, or a sharper stripped shot of (8740-8780, 15185-15250).

## AMB-044: `rsel12_buf`'s track over the poly row y 13375, at (6452,13372-13389) (2026-11-20)

Proposed by `busl` (richtw1, run 8; its Ambiguity 15). The same kind as AMB-039. The row is
`cdp4_bus_s1`'s channel-2 row (a data line of latch row C). Neither metal shot passes the metal test for
18 px, the row's full height, where the track x 6452 crosses it; both chips are reddish and dim there
(chip 2 137/81/28, chip 1 130/54/27, against 206-212/159-171/79-89 on the track x 6494 over the same
row). Readings: (a) a plain crossing with a mark on the metal; (b) a contact onto the row, which would
put R12's read select on a data line of latch row C; (c) a break, which would leave row E's read gate
without a driver. **Assumed (a), drawn as a plain metal, no `?` item** (as AMB-039 was): the track's two
edge lines run unbroken through the patch in both chips (tracer and reviewer); no pad, no ring, no
widening of metal or row; no hole in the clean shot (222/165/121, as under x 6494); the track's real tap
480 px south has all of them; the row has its own pad at (5538,13375). The reviewer adds that the same
reddish patch occurs in one chip alone on unbroken crossings ((6452,14304) chip 1; (6494,13616) and
(7055,13852) chip 2). Against: both chips are dim at the same spot, as at AMB-039 (which the row's ends
settled as a plain crossing). Nothing in these photos can add to it. What would settle it: a sharper
metal shot of the spot, or simulation (reading (b) would drive a latch input whenever R12 is read).
**2026-11-20, later** (`busl` run 13, its Ambiguity 21): the next track west, x 6408 (`tl5_w2722`), has
a like mark over the same row at (6408,13357-13377): chip 2's metal is dim for the row's height with a
greenish patch of about 10 x 12 px in chip 2's stripped shot; chip 1's metal is bright between the
row's edge bars with no ring, the clean shot has no hole, the row is not widened. Read as a mark on
chip 2, a plain crossing, no `?` item. A one-chip mark, so weaker than this entry's two-chip one.

## AMB-045: `busl_x7122`'s track over the poly row y 13744, at (7058,13727-13761) (2026-11-20)

Proposed by `busl` (richtw1, run 11; its Ambiguity 16). The same kind as AMB-039 and AMB-044, and the
second dim crossing on AMB-039's row (`rsel13_buf`'s tap row; AMB-039 was 87 px east). Neither metal shot
passes the metal test for 18 px and again for 14 px where the track x 7058 crosses the row. Readings:
(a) a plain crossing with a dim surface in both chips; (b) a contact, which would put R13's read select
on `busl_x7122` (the row y 8863 under `cdp3`'s column 0 rail to the row y 14480 of the bottom-centre
bus); (c) a break. **Assumed (a), drawn as a plain metal, no `?` item**: the track's edge lines run
through unbroken, neither metal nor row is widened, the clean shot is protected cream without a hole,
and the row's real tap 560 px west has pad, ring, bright centre and hole. The reviewer found the same
dim centre on the same track over `rsel12_buf`'s row at (7058,13852): one wire cannot be on both
selects. Against: two dim crossings on one row. AMB-039's resolution stands (the row has its own
driver). What would settle it: the driver of the row y 14480 (`bc1`) or the far end of the row y 8863
(the pad (7835,8862)'s metal north, `cdp3` (continue)).

## AMB-046: the row y 8863 under `cdp3`'s column 0 rail, x 7550-7600 (2026-11-20)

Proposed by `busl` (richtw1, run 11; its Ambiguity 17), with the correction of `cdp3_k_a` it led to.
The poly row y 8863 from the pad (7423,8863) runs east under the wide rail. Its two edge lines run on
under the rail in all four shots, but the clean shot's colour between them is dark red, not the cream
of poly under metal, up to a slanted boundary at x 7600-7608 (the clean shot is anomalous over that
patch). **Assumed one poly row through, drawn `?P`** (42 px in `trace/busl.txt`; east of x 7592 the row
is `cdp3`'s `?P` to the contact pad (7835,8862), drawn by the first run of `cdp3` from a single
observation). If the row is broken under the rail, `busl_x7122` ends there on nothing and the pad
(7835,8862) with its metal north is a separate net. **`cdp3_k_a` is not on this row either way**
(coordinator, 2026-11-20, from `busl`'s handoff, both metal shots, `cache/scratch/refresh/h_k_a.png`):
`cdp3`'s first run had the pad's metal going south at x 7835 to the contact (7833,9165); there is no
metal at x 7835 between y 8880 and y 9160, the pad's metal goes north to a pad at about (7834,8645),
and `cdp3_k_a`'s metal starts at (7833,9165). `trace/cdp3.txt` corrected (`tools/sameconn.py`:
connections identical; no transistor is on either net there). What would settle the row: the pad's
metal north and what it reaches (`cdp3` (continue)).

## AMB-047: the gate cluster beside `cdp3`'s row A (2026-11-20)

Proposed by `cdp3` (Matt Godbolt, closing handoff 740bfe3). x 7780-8200, y 8260-8800: three gates on the
rail x 7986-8030 with three loads, about 14 transistors; inputs from U1 (`cdp3_w8063`, a buffered
`ck_out`, on two gate rows), from the end pad (7878,8385) of the x 7880 line (the output of the gate
beside row C) and from a pad (7878,8315) whose metal comes down from a pad (7987,6845). **Nothing of the
cluster is in the trace.** Five boundaries between diffusions lie in 20-25 px gaps between two metals; a
reviewer reads all five as joined (with controls in the same gap: field at y 8565-8628, the box
(7935,8648) against its neighbour); the row y 8502-8525 is two polys (firm; a break at x 7984-8005).
With that reading one transistor has its gate and its drain on one net, so a contact or a tie is still
misread. Candidates: the two boxes under the metal x 7927-7957 at (7937,8474) and (7935,8648), tan like
diffusion in the clean shot and orange like poly in the chip-2 stripped shot (contacts to diffusion, or
poly pads?). Two readings by the tracer and one by the reviewer give no consistent circuit. What is at
stake: where the cursor-match NAND's output goes, and the clocked logic it feeds. What would settle it:
those two boxes at 6x in all four shots, then the cluster redrawn from them (`cdp3` (continue); the
survey and the draft are in `notes/blocks/cdp3.md`, Not done). Trap 2's addition of the same date.

**Annotated 2026-11-21** (from `cdp2`'s handoff, piece `ga`): a third candidate reading of the two boxes. Small
heavy-outlined boxes under a thin metal were twice read as metal contacts in `cdp2` that day and are buried
contacts with the metal passing over (found by its reviewer). The two boxes at (7937,8474) and (7935,8648)
are very probably the same: no contact to the metal x 7927-7957. Re-read item R51 gives the test (pad or
land, hole or pits, widened ring; trap 27's addition). And the pad (7878,8315)'s metal from (7987,6845) is
`cdp2_w6845`, a through line from the west (a metal along y 6848), not the output of `cdp2`'s inverter.

**Annotated 2026-11-21 (evening)** (from `cdp3`'s handoff, merged 0d349fe): a poly row arrives at the box (7935,8648) from the west: the pad (7834,8647) at the end of `busl_x7122`'s metal x 7835 carries a row east (y 8637-8658) under the x 7880 metal to x 7918, 15 px short of the box. A row arriving there fits the box being a poly pad of this row with a contact from the metal x 7927-7957 rather than a diffusion: a lead, not a finding (views `cache/scratch/cdp3/x7835_a.png`, `ov_x7835.png`; `tools/px.py row 8647 7790 7960 6 metal,metal1,acid1b`).

## AMB-048: the tie of `cdp2_b_hl`'s load (2026-11-21)

Proposed by `cdp2` (Matt Godbolt, piece `gh`, merged 5d52ee6). The depletion load of the comparator's row line
`cdp2_b_hl` (x 8578-8745, y 7352-7432) has its gate plate tied to the line by a buried contact drawn `?B`.
The plate is one poly with row 2 of the lower series gate left of rows B, so the same tie decides two
equations: that `cdp2_b_hl` is a gate at all (NOT(OR over s3..s7 of (`cdp2_b_s#_p1` AND `cdp2_b_s#_y`))),
and that `cdp2_w7272` = NOT(`cdp2_b_hl` AND `cdp2_b_s7_x`). **Adopted: tied** (the tracer's reading; a depletion load's gate
is normally tied to its output node). What would settle it: the box at 6x in all four shots.

## AMB-049: the neck between the tracks x 8013 and x 8056 (2026-11-21)

Proposed by `eof` (Tom Seddon, run 29, piece `in207`; the block's Ambiguity 102). x 8025-8050, y 16609-16619.
Candidate readings: (a) one metal, the bundle's outermost L with a thin neck, so gate B of the NOR that
makes `eof_w17338` is `bc1_dec01_n`; (b) two metals ending 25 px apart, both without a contact. For (a): a
band 9-10 px tall in both metal shots with its own lower edge line, absent at a control column; chip 2
without a gap; the clean shot protected under it; the chip-2 stripped shot's ghost unbroken; the next two
lines of the bundle step by the same kind of L. Against: chip 1's dark notch 6 px wide at x 8046-8051; the
arm thinner than the tracks and dimmer than the ground in chip 2. **Adopted: (a)**, drawn `?M`, names held
by `@alias bc1_dec01_n eof_w17207`. Rests on it: which decode line of `bc1` selects DISPTMG's delayed term.
Would settle it: a sharper metal shot, or the logic (each of `bc1`'s decode lines reaching one gate of
this group). Looked at by the coordinator at 6x in both metal shots (`cache/scratch/refresh/h9_neck.png`):
the reading is as described; it does not decide it.

## AMB-050: the two ties of each unit of `bc1`'s west gate column (2026-11-21)

From `eof` runs 32-35 (Tom Seddon; the block's Ambiguities 120/121, 125/126, 131/132, 133/134). Four units
under the rail x 7294-7342 (`eof_w15523`, `eof_w15781`, `eof_w15262`, `eof_w15128`) are each drawn with two
uncertain items: the load's tie (`?B`, as every load of the build) and the tie at the node's exit (`?D` /
`?B`), where the node's diffusion band ends against the corner of a heavy-framed box with a pale centre from
which a poly row leaves west. Both metal shots show the box; the clean shot is inverted there (trap 28), so
how the active area gets under the poly is not seen. **Adopted: buried contacts** (the band has no other
end, the row no other driver; the reviewer of run 34 measured the pilot cell's accepted buried contact as a
control: the same 12 px dark line and plain centre). Rests on it: all four equations, and so the chain from
`rcs_e4`, `lc1_w7780`, `rcs_mv` and `rst_n` onward. Would settle it: a sharper shot, or the next units'
logic making sense with these inputs.

**Annotated 2026-11-21 (evening)** (from `eof` run 42, piece `selg`; the block's Ambiguity 172): two more units
of this build, `eof`'s cell `eof_sdrv` (x 7260-7325, y 16515-16570 and 325 px south), the select drivers
`eof_ga` = NOT `rcs_mv` and `eof_gb` = NOT `eof_ga`, are drawn with the same pair of ties (`?D` / `?B`). If the
west tie is not there the select line has no driver.

## AMB-051: the devices of `cap18`'s build (2026-11-21)

From `eof` runs 37-38 (Tom Seddon; the block's Ambiguities 116, 144, 150). Four devices of one build:
`cap18` on `eof_w16040`, its twin on `bl0_w15566` (drawn in run 49 as `cap18b`), `cap998` on `eof_w15998`
(tap pad (5627,16125)), `cap218` on `eof_w16218` (x 4850-5020, y 16700-16910). Each: a gate on the net, a
channel between VCC and a closed diffusion whose contact's metal island also covers the gate and has no wire.
Candidate readings: (a) a capacitor on the net; (b) a depletion load whose gate is tied to its source through
the island by a contact not seen in any of the four shots. For (a): no ring and no hole over any gate plate;
`cap998` sits on a net that has a driver with its own load. **Adopted: (a)**, drawn as transistors whose
island node has no other connection. Rests on it: whether `eof_w16040` (no driver found) has a pull-up. Would
settle it: the circuit (the driver of `eof_w16040` found), since no photo shows the cross-section.

## AMB-052: the arm of the track x 4780 onto the pad (4736,14155) (2026-11-21)

From `eof` run 38 (Tom Seddon; the block's Ambiguity 147). 6-8 px between the pad's metal frame and the arm
at y 14159 are dim in both chips (chip 2 80-144, chip 1 48-112). **Adopted: one metal**, the pad poly's east
edge under it (the bar is as narrow as a row's edge bar, the frame is bright on that side only, and the track
would otherwise end on nothing). Drawn as plain metal. Rests on it: the join of `eof_w15998`'s track from the
south to the seven northern rows of the left array (s0-s6); without it those rows' line has no driver. Would
settle it: a sharper metal shot, or the north track's other end (it is a free end pad (4736,11292)).

## AMB-053: the strap's north end on the VSS-tied poly band, left array rows s0-s13 (2026-11-21)

From `eof` runs 39-40 (Tom Seddon; the block's Ambiguity 156; master (4605,11536)). The thin metal x 4597-4613
of each row (y 11522-11898) carries the end of the transistor that the fourteen-row line gates (contacts
(4608,11757), (4607,11881)); its north end lies on a poly band y 11527-11545 that a pad with a contact
(4667,11540) ties to the VSS metal x 4647-4692. Candidate readings: (A) no contact: `eof_strap_s#` is a signal
node and the transistor a pass transistor; (B) a contact: `eof_strap_s#` is VSS and the transistor pulls
`eof_nbox_s#` low. For A: no hole in the clean shot (cream, uniform), the metal not widened (15 px), the band
18 px high where every contact of these thin metals stands on a 33-38 px pad, the two dark bars are the band's
edges. For B: the metal has no other connection north of the gate and ends exactly on the band; chip 2's
stripped shot is greenish there, but as greenish on the field south of the band (the metal's ghost). **Adopted:
A** (no `?` item drawn). Run 40 traced the group south of the metal: two pass transistors on the node with no
supply contact, so A is the reading that makes a circuit. Rests on it: the meaning of fourteen transistors.
Would settle it: what the box north of the gate (`eof_nbox_s#`) and its poly column drive.

## AMB-054: the selector's band meets the poly column inside rail G's margin (2026-11-21)

From `eof` run 44 (Tom Seddon; the block's Ambiguity 181). In each row of the left array the lower band from
the selector meets the poly column x 4152-4164 inside rail G's protected margin: read from the clean shot
(cream into the column's red-brown, no pink, no green rim; a 2-4 px dip at x 4160-4164 whose depth differs by
row, none in s8); chip 2's shots show only the rail's edge line there. Other reading: the band ends a few px
short of the column (no room for a poly gap; it would leave the band a dead end). **Adopted: one poly**
(the reviewer agrees and adds s9 from chip 2's stripped shot). Rests on it: the eleven joins of the compared
lines to `larr`'s lines H, and all fourteen bands' loads. Also rests on `larr`'s H3 being poly in the eleven
rows (R50).

## AMB-055: the greenish box under rail G beside each load's buried contact (2026-11-21)

From `eof` run 45 (Tom Seddon; the block's Ambiguity 185). Under rail G east of each buried contact of the two
loads lies a greenish box (x 4176-4197, y 11674-11714 and y 11820-11858 in row s1; clean shot 150/148/108; no
ring, specks or pits), between the buried contact (a dark bar 10-12 px) and the supply diffusion. Readings:
(a) field inside the buried contact's window; (b) bare diffusion of the buried contact's active area; (c) a
bump of the supply diffusion ending at the bar; (d) diffusion joining the buried contact to the supply
diffusion. (a)-(c) give the nets as drawn; (d) would put each compared line on `vcc`, so it is not believed.
**Adopted: (a)**; nothing is drawn of the boxes. Rests on it: all 28 loads. Settled by the pull-downs (run 46
drew them on one gate per row: the nodes are logic outputs, which (d) would contradict).

## AMB-056: `dbus_le`'s thin metal over the output boxes of the data output inverters (2026-11-21)

From `cdp4` run 8 (Matt Godbolt; the block's Ambiguity 15). The thin metal x 16768-16782 that `dlat` draws
south to (16774,15935) runs on south over five output boxes (buried contacts of `d5_out_n`..`d1_out_n`) and is
dark in both metal shots for 53-67 px over each (y 15802-15868, 15937-15990, 16067-16124, 16197-16255,
16323-16383), the clean shot greenish under it. **Adopted: one metal passing over the boxes with no contact**
(trap 27; the reviewer of round 7 checked each box against real pads: no pad, hole or pits). `dlat` draws the
stretch over the first box as plain metal; `cdp4` draws the other four `?M`, so `dbus_le` south of y 15990 is
joined only through uncertain items. Left as drawn: whether `dlat`'s stretch should be `?M` too is a question
of consistency only. Would settle it: the far end, traced by `cdp4` run 13 to the output box of a two-input
NOR under `bd2`'s VSS rail (PR #17 had a NOR as its driver); a NOR there makes one metal the reading.

## AMB-057: is the bottom bus line y 17860-17873 the east arm of `eof_w16040`'s pad (8643,17865)? (2026-11-21)

From `eof` run 49 (Tom Seddon; the block's Ambiguity 206; proposed there as AMB-051). One `?M`
(`trace/eof.txt`, `?M 8643,17866 x8708 w=12`). Reading B (drawn): one metal from the pad east over
`bl0_w15566`'s poly column x 8680-8698. For it: chip 2's metal shot (bright metal from x 8668, 26-27 px from
the pad's centre, as at the control pads (8685,17821) and (8598,17908)); the clean shot's protected strip and
the chip-2 stripped shot's ghost band at the line's height; the follower from the east runs to the pad; under
the other reading the line would end 6-8 px from the pad's metal. Reading A: the line ends on the column,
short of the pad. For it: chip 1's metal shot is dark from x 8646 to 8686, where both control pads show their
line bright right after the ring. **Adopted: B.** Rests on it: that the line `eof` runs 50-51 drew east
(`eof_w17866`, gate of `eof_w17345`'s second pull-down) is `eof_w16040`. Would settle it: the line's east end
logic; a sharper chip-1 view.

## AMB-058: is the cap of `rst_lat`'s north gate row tied to the box north of it? (2026-11-21)

From `eof` run 53 (Matt Godbolt; the block's Ambiguity 216; raised by review round 65, read again by round
66). The poly row y 16292-16314 from `rst_lat`'s end pad (10353,16345) ends in a cap x 10624-10640 east of
the diffusion it gates under the VSS rail x 10548-10598. Directly north, across a dark band y 16282-16290
(about 10 px), is a box (10622-10650, 16264-16282) that is dark in all four shots, on both chips, in a narrow
plain band that leaves the rail's north diffusion eastwards. **Assumed: no tie** (the cap is an end cap in
field): the box matches neither control (a buried contact's centre is light: 142-159 against about 100 here
in chip 2's metal shot), and the dark band is wider over the cap than east of it, so the cap has a north edge
of its own. Not strictly decidable: a dark line between poly and box is also what a buried contact shows.
Nothing is drawn for the box and the transistor is undrawn, so the extraction is the same either way. Would
settle it: tracing that unit (the band's ends; the poly that reads orange north of the box at y
16256-16259).

Updated 2026-11-23 (`eof` run 67, Kieran Connell): the "poly at y 16256" is the row of `eof_w16213`, from the
pad (10440,16215) south and east (y 16249-16267) toward `rst_lat`'s unit's west box (port at x 10481), with the
north end of the thin metal x 10476-10492 on the same net (AMB-060). Whether that poly joins the box is still
open; it is `eof`'s next work (`rst_lat`'s unit), whose output is probably `eof_w16213`.

## AMB-059: is the dark spot (10567,17178) on the VSS rail a contact onto the NOR `bc2_w14955`'s node? (2026-11-22)

From `eof` run 55 (Kieran Connell; the block's Ambiguity 217; the reviewer of round 68 measured the same and
agreed). Chip 2's metal shot has a dark spot about 10 px across (x 10564-10573, y 17173-17182) on the rail
x 10548-10598 over the node's diffusion y 17140-17199; run 51 had noted "a contact at about (10565,17175)" from
a low zoom. **Assumed: a blemish of chip 2, nothing drawn.** The spot has no ring; chip 1's metal shot is
uniformly bright over it and the clean shot uniformly tan (no greener patch, no specks), while both real rail
contacts 95 px north and 80 px south have the ring and the specks; a contact is a mask feature and would be on
both chips. A contact would put the node on `vss`: no gate, and `rst_lat`'s transistor between two grounded
diffusions; the node also has a load and an exit of its own, which a grounded diffusion would not. Rests on it:
`bc2_w14955` = NOR(`rst_lat`, `ck_out`). Would settle it: nothing more in these photos.

## AMB-060: is the box (10476-10518, 16980-17012) of the latch node `eof_w16996` contacted by the thin metal x 10476-10492? (2026-11-23)

From `eof` run 63 (Kieran Connell; the block's Ambiguity 219; review round 77). The latch `eof_w16889` /
`eof_w16996` in `bc2`'s rail column has no other visible exit for `eof_w16996`: no poly leaves the box (rows
north and south, field west), and the thin metal x 10476-10492 passes over it. Over the box the metal is dark
for 39 px in both chips, with no bright centre, no widening into a pad, and tan with no green hole in the clean
shot: trap 22's marks of a pass-over, none of a contact. Against a pass-over: a node needs an exit, and metal
is present up to the box's edge on both sides. The metal is on the track of `regs`' `lc2_w8450` (pad
(10484,17994), drawn north to y 17760), and its north end is `eof_w16213` at the pad (10440,16215) (`eof` run
67), with a poly toward `rst_lat`'s unit. Readings: (a) a contact: `eof_w16996` leaves on this metal, which
then is not `lc2_w8450` all the way (two metals end to end somewhere, trap 33; R53); (b) a pass-over: the
metal is another net and the latch's output leaves some other way not yet seen. **Drawn `?C`**: the metal
over the box only and unnamed, the name on the node's diffusion. Nothing rests on it: both latch equations
(`eof_w16889` = NOR(`bc2_w14955`, `eof_w16996`), `eof_w16996` = NOR(`rst_a`, `eof_w17345`, `eof_w16889`)) are
the same either way. Support for (b) (review round 79): the same metal is dark in the same way over the exit
box of `eof_w16560` (y 16500-16537), which has a poly exit of its own; the metal is dark over a box at each
unit along it (y 16240-16277, 16500-16537, 16977-17014, 17457-17492, 17716-17754). Would settle it: following
the thin metal both ways, stretch by stretch (a pink protected strip beside each dark stretch in the clean
shot, trap 27); finding `rst_lat`'s unit's output (probably `eof_w16213`), and what `eof_w16996` drives.
