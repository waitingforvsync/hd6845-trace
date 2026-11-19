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
another line of the bundle (`r9m_l3`). The earlier statement that `amr` c3's outer output
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
would sit on the rail). **Adopted** as drawn: `fld_a_in` = NAND(`inh_ck`, `tcw_b`),
`fld_y_b` = NOT `tcw_c`. Settle when the region west of the island is traced as a block.

Added 2026-11-16: a poly from the lower pad (6232,3870) of the bus metal `c4l_gab` runs
east along y 3912 and reaches the rail at y 3910-3934, between the rail contact
(6535,3905) and the node of `fld_a_in` (which starts at y 3956 below a strip of field at
y 3948-3956; the clean shot is dull tan at y 3935-3947). If diffusion is continuous
under that poly, `fld_a_in` has a third pull-down gated by `c4l_gab`
(`fld_a_in` = NOT(`c4l_gab` OR (`inh_ck` AND `tcw_b`))); if the poly only passes over
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

## AMB-028: `tc1_ns3`'s metal over `rax`'s five boxes, and `tc2_sr_r` through `rax` (2026-11-18)

Proposed by `tc2` (dp111). (1) `tc1_ns3`'s metal crosses `rax`'s five unit boxes; drawn `?M` at the
five crossings, resting partly on the electrical argument (as AMB-011). (2) North of (8031,5468) the
follower takes `tc2_sr_r`'s thin metal 440 px through `rax`'s units 3-5 over six contact-like spots,
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
(`inh_ck`). **Assumed one metal, no contact between its ends; six stretches drawn `?M`** (over node
boxes at y 2964-3021, 3381-3444, 3527-3574, 3686-3748, 3771-3969, 4051-4108), where neither metal shot
shows it for 40-55 px. For: two real end pads (full-bright centre 12 px across, green hole) and
nothing pad-like between; the row y 2899 has only gates on it, so its driver must arrive by this
metal; a contact on any box would short a unit's output to `inh_ck`; an unbroken pink protected strip
beside the line in the clean shot where one side lies over field. Against: small bright centres over
four boxes ((4104,2988), (4101,3719), (4102,4074), (4101,5202)). The most contact-like is (4102,4074),
on `rcs_in1`'s box (clean shot 186/182/139, neither a contact's green nor a pass-over's tan): a contact
there would make `tl3_e4243` constant; one at (4101,5202) would make latch C's data its own enable;
one at (4104,2988) would make the metal E1's second output. `inh_ck`'s source is not traced, so four
of the six have no electrical cross-check. **Rests on it: `tl1_w3594` = `inh_ck`** (`tl1`'s two latches
in series a master and a slave on `inh_ck`). Since `eof` run 2 (2026-11-19) `inh_ck` is `inh_ck` (firm), so `tl1_w3594` = `inh_ck` rests on this entry, and
`inh_ck`'s source is known: the cross-check this entry lacked is now possible from the driver's side. Would settle it: `inh_ck`'s source; a third chip's metal
shot; the simulation.

## AMB-034: three ring-like marks in `tl4` not drawn as contacts (2026-11-18)

Proposed by `tl4` (Matt Godbolt, runs 6-7; `notes/blocks/tl4.md`, Ambiguities 4-7 and 10). (1) The
heavy box at (4684,3420) under the metal of `tl4_w3245`: bright centre in a dark ring in both metal
shots, no hole in the clean shot, no pits in the chip-2 stripped shot; drawn as an uncertain lobe of
`tl4_w3390`'s diffusion, no contact. A contact would short `tl4_w3245` to `tl4_w3390`, which the rest
of the latch contradicts; what the box is for is not known. (2) A mark at (4683,5767) on RA's leg,
in both metal shots, right over the row of `tl4_w3850`; no hole under it in either stripped shot, so
not drawn; a contact would tie `tl4_w3850` (and `rcs_e3`'s input) to VSS. (3) The field box
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

## AMB-037: `inh_ck`'s staircase over other nets without contact (2026-11-19)

Proposed from `eof` run 2 (`notes/blocks/eof.md`, Ambiguities 5-7) and `lc2` (its Ambiguity 3). The
metal that carries `inh_ck` from `trunks`' line S north to the top-left logic lies on other
nets' poly at four places, and `lc2`'s metal x 6422-6440 lies 64 px along latch C's data poly
(6431, 8117-8181); none is drawn as a contact (trap 13; read from text maps by two packages). A contact
at the first would join `inh_ck` to latch D's output `lc1_w7040`; the one in `lc2` would join it to
latch C's data `lc2_w8906`. The join to line S also rests on `trunks`' reading of that line (R4).
