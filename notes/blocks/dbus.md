# Data bus interface column (`dbus`)

Region: x 17050-17700, y 5300-17000, and the D0-D7 pad cells to its right.
Trace: `trace/dbus.txt`. Scratch tools: `tools/dbus_mosaic.py` (the same rectangle at
several offsets side by side, for comparing repeats), `tools/dbus_autocorr.py`
(vertical pitch of a strip).

## Status

Traced, extracting (96 transistors, 0 errors), overlay-checked:

- the input buffer chain (four inverters), cell `dbus_in`, six copies (D0-D5); D0's and
  D1's input lines (first session);
- **the input latch of D0-D3** (cell `dbus_lat`, ten transistors, master under chain 0,
  three more copies upside down under chains 1-3) and **the inverter that drives each
  data bus bit from it** (cell `dbus_drv`, two transistors, four copies at the chain
  pitch), with the lines between them, the lines from the chains (`d#_d`) and the ends of
  `dbl`'s four data lines: `db_b0`..`db_b3` are now driven nets (2026-11-17 15:28 +0000);
- the latch enable `dbus_le` (metal M_b) from its top pad down the column and west to the
  region's edge.

Not traced: everything for bits 4-7 below chain 4, the logic at y 15100-16600, the logic
above D0, the channel wiring to the pads, the pad cells (those are `dpad`). See "Not done".

## Inventory

The column is not one unit per pad at the pad pitch. Logic occupies y 8030-16600
only; between y 5900 and 8030 there are just the rails and three metal lines coming
down from the D0 pad cell. Gates sit on a 152 px vertical pitch between two rails:

- VSS rail, metal, x 17355-17400 (pull-down diffusions under it; further up it joins
  a wide trunk at y 6620-6720).
- VCC rail, metal, x 17527-17585, top end at y 8287, bottom end about y 17000 where
  it joins a wide horizontal metal (y 16960-17010).
- Loads between the rails at x 17420-17520; gate outputs leave to the left in poly.
- Which rail is which comes from the orientation of the loads (every load's far end
  contacts the right-hand rail); neither rail was followed to a pad.
- Left of the VSS rail (x 17050-17300) is a wiring field. From unit 1 downward it
  carries five vertical metal lines (x about 17075, 17120, 17165, 17207, 17252).

| What | Where | State |
|---|---|---|
| Input chain, D0 | 17255-17590 x 8280-8880 | cell `dbus_in`, traced |
| Input chain, D1-D5 | same cell at (1,1365) (1,2732) (2,4098) (2,5465) (2,6223) | placed; findcell on the clean shot scores 0.81-0.83, each overlay checked at 1.25x. The four-gate core is the same in all six; the wiring left of x 17290 differs per copy and is drawn only for D0 (and D1's input) |
| Capacitor rectangles of chain 0 | 16960-17040 x 8445-8580 and x 8745-8880 | drawn |
| Input latch, D0 | 17230-17590 x 8885-9370 | cell `dbus_lat`, traced |
| Input latch, D1-D3 | **upside down**: `@inst dbus_lat` at (1,1266) (1,2631) (2,3998), mirrored about y 9195 (centres y 10461, 11826, 13193) | placed: findcell on the clean shot 0.76-0.77; `cellcheck.py` in both chip-2 shots: median correlation 0.92-0.94, the badly matching blocks are the VCC contact pits and the top edge. The first notes' "cluster 0 + 1366" was wrong |
| Bus inverter, D0 | 17290-17590 x 9373-9500 | cell `dbus_drv`, traced |
| Bus inverter, D1-D3 | the same cell at (0,1366) (0,2732) (0,4098), **not** upside down; its VSS land runs into the upside-down latch's land above it | placed; `cellcheck.py` metal: 0.95-0.96, bad blocks only along the top edge (the neighbour differs) |
| Cross-unders between units 0 and 1 | poly "line 1" y 9545-9566, "line 2" y 9590-9610, both under both rails | line 1 drawn (D1 input); line 2 is D1's P_y, not drawn. The same pair recurs below unit 1 (contact (17293,10920) seen) |
| Logic below chain 5 | 17150-17590 x 15100-16600 | single gates on the 152 pitch, not surveyed in detail. No cluster follows chains 4 and 5 (chain 5 starts 758 px below chain 4) |
| Logic above D0 | 17200-17700 x 5250-5900 | several gates, not looked at |

findcell (metal and clean shot, threshold 0.4) finds no seventh or eighth copy of
the chain. Where the input buffers of D6 and D7 are is not known; the lower part of
the column (y 15100-16600) is the first place to look, then the corner by the
bottom-right input pads.

## Logic

### Input chain `dbus_in` (traced)

Four inverters in series, the same arrangement as the R/W, RS and CS input buffers
in the bottom row (`rw_a`..`rw_d`). For chain n:

    dN_a = NOT dN_in      (G1, y 8287-8425 in chain 0)
    dN_b = NOT dN_a       (G2, y 8436-8568)
    dN_c = NOT dN_b       (G3, y 8588-8720)
    dN_d = NOT dN_c       (G4, y 8742-8870)

- `d0_in` is the line from the D0 pad cell (Ports). Traced into G1.
- `d1_in` is traced from the D1 pad cell's contact into chain 1's G1, so chain 1 is
  D1's. Chains 2-5 are tagged by position and *assumed* to follow the pad order.
- `d0_b` and `d0_c` each run left in poly to a metal contact next to a plain
  diffusion rectangle (the "added capacitance" rectangles of the bottom row). The
  strap from `d0_c`'s contact (17078,8795) to its rectangle (contact 16990,8787) is
  there. The strap for `d0_b` (contacts 17078,8490 and 16988,8468) is absent in both
  metal shots: each contact carries only a dot of metal. They are NOT bus lines.
- Only `dN_d`, the pad level delayed by four inverters, feeds logic. `d0_d` leaves G4
  in poly to a contact at 17205,8837 and goes down in metal (x 17198-17218, "M_a")
  into cluster 0, ending at a contact at 17207,9255.
- G1's gate poly continues into an L (17413-17503 x 8292-8318) that crosses no
  diffusion and ends beside the load, as on the bottom-row input inverters (AMB-004).

In chains 1-5 the b and c lines also run left (for chain 1: `d1_b` up at x 17225-17245
to y 9750 and left along y 9740-9760; `d1_c` left to x 17165 and down), presumably
to their capacitors; not followed.

### The input latch (cell `dbus_lat`; "cluster 0" of the first notes), traced 2026-11-17

Under chain 0, y 8885-9370: two cross-coupled AND-OR-invert gates and an inverter (ten
transistors); below it, y 9373-9500, an inverter with a strong load that drives the data
bus bit (two transistors, drawn outside the cell). As extracted:

    d0_d_n  = NOT d0_d                                  inverter N3
    dl0_q   = NOT( (d0_d_n AND dbus_le) OR dl0_q_n )    gate N0
    dl0_q_n = NOT( (d0_d   AND dbus_le) OR dl0_q   )    gate N1
    db_b0   = NOT dl0_q_n                               inverter N2

So it is a transparent latch: while `dbus_le` is high `dl0_q` follows the D0 pin (through
the four-inverter chain) and `db_b0` = D0; when `dbus_le` falls the pair holds. **The
internal data bus bit is driven all the time, by a static inverter, from this latch**:
there is no tri-state driver here. (Traced: the equations. Believed: that `dbus_le` is a
write-side enable; its source is not traced. It is the vertical metal M_b.)

Where things are (all coordinates checked by overlay at 2.85x, `ov_top.png`, `ov_bot.png`):

| What | Where |
|---|---|
| Diffusion column under the VSS rail, x 17330-17405 | VSS land 8888-8942 (contact 17364,8910); band A 8942-8966; mid node; band B 8986-9010; node N0 9012-9042 |
| N0 = `dl0_q` | from the column east (y 9015-9042) to under the thin metal, then south under it (x 17434-17470) to y 9095, and from y 9063 east under the load gate to the VCC land |
| Third pull-down of N0 (W 41 with the `?D` of Ambiguity 5, else 17) | a narrow diffusion x 17450-17467 runs from the VSS land's east strip (y 8920-8942, which goes on to x 17494) south to N0; the poly from M_d's top pad (17491,9010) runs up x 17498-17520 and west along y 8944-8966 over it and ends at x 17437. Gate = `dl0_q_n` |
| Load of N0 | poly x 17476-17518, y 9049-9121 under metal M_d; channel y 9063-9094. It is band C's east end. **Tied to N0 by the buried contact (17427,9085)**: a box 17414-17438 x 9072-9097 in the gap between the VSS rail and the thin metal, on a north tab of band C, with N0's west edge open into it (found by review round 2) |
| Column, middle part, x 17350-17400 for the land and band C, **x 17323-17400 from y 9153 down** (bands D and E are W 77 like A and B; review round 1) | VSS land 9063-9113 (contact 17362,9087); band C 9111-9133; node N1 9133-9198; band D 9196-9219; mid node; band E 9240-9262; VSS land 9268-9310 (contact 17368,9285) |
| N1 = `dl0_q_n` | east along y 9157-9190 under the thin metal and the load gate to the VCC land; load gate x 17478-17518, y 9142-9228 under M_d, tied to N1 by the buried contact (17446,9205); contact (17491,9213) to M_d |
| VCC land of both loads | x 17527-17585, y 9063-9188, long contact y 9082-9165; its west edge steps back to x 17536 between the two channels |
| Metal M_d, x 17480-17502 | (17491,9010) to (17491,9213): carries `dl0_q_n` up to the third pull-down of N0. `follow.py`: one piece, 9008-9216 |
| Metal M_c, x 17309-17327 | (17300,8944) to (17313,9345): carries `d0_d_n` up to band A. `follow.py`: one piece, 8940-9350 |
| Metal M_b, x 17243-17262 | starts at the pad (17252,8990) on band B; second pad (17252,9208) on band D; goes on south (`follow.py`: to y 13614, then west): `dbus_le` |
| Metal M_a, x 17198-17218 | `d0_d` from chain 0, ends on the pad (17207,9248) of band E |
| Inverter N3 | band E turns south at x 17402-17419 (y 9255-9322) between the VSS land and the node x 17420-17476, y 9272-9310; load gate x 17475-17525, y 9252-9316 (chip-2 shot: orange block with the diffusion's edge across it at y 9270); VCC land x 17530-17586, y 9238-9300, contact (17555,9268). The node goes south under the thin metal to the buried contact (17450,9346) on the poly y 9336-9360 that joins the load gate's stem and runs west to M_c's bottom pad |
| Inverter N2 | VSS land y 9373-9415, widened to x 17300-17431 below y 9395 (outline in both chip-2 shots, `n2w.png`); band F y 9415-9437 (W about 131); node N2 below it; east under the thin metal, buried contact (17448,9478) to the load gate's foot; a narrow diffusion x 17478-17497 north beside the load gate; load gate x 17497-17535, y 9390-9500 (W about 70); VCC land x 17535-17586, y 9400-9475, contact (17553,9440) |
| `db_b0` | N2's south-west tab, buried contact (17314,9466), poly west along y 9462-9479 to the pad under dbl's contact (17207,9467) |
| `dl0_q_n` to band F | N1's west tab and buried contact (17313,9166) under M_c; poly west along y 9155-9173, south down x 17157-17185, east along y 9415-9437: band F, which ends under the thin metal at x 17449 |

How the doubtful junctions were decided (colour maps of the clean shot, cells of 2-3 px,
`cache/scratch/dbus/map.py`; R-G about 80 is field under metal, 55 poly, 25 diffusion):

- **Band A does not go on east of the rail.** In the gap between the VSS rail and the thin
  metal (x 17416-17436) the rows of band A (y 8944-8965) are neutral (R-G 0-10) in the clean
  shot and not orange in the chip-2 stripped shot, where the rows of band C in the same gap
  are red-brown (R-G 60-70). The poly that continues at the same height east of the gap
  (x 17437-17520) is a different piece: it joins the poly that comes up from M_d's top pad.
  The first reading (one band from M_c's pad to M_d's pad) would short `d0_d_n` to `dl0_q_n`.
- **That piece crosses a channel under the thin metal.** At x 17452-17463 it is as red and
  bright (R-G 85-90) as the two load channels; its west end x 17437-17448 has the colour of
  poly over field. North of it the strip y 8920-8942 and south of it the strip x 17452-17466
  down to N0 are tan (diffusion); the strip in the open at (17470-17488, 8923-8935) is bright
  green (open diffusion).
- **Band D ends at x 17409**: green (field) in the gap at x 17410-17421 on its rows. The poly
  under the thin metal at y 9210-9225 comes from the load gate of N1 and ends at x 17431.
- **The boxes under the thin metal** at (17446,9200), (17450,9345), (17448,9475) are buried
  contacts, not metal contacts: tan inside like the diffusion beside them (179/170/128
  against 131/139/71 to 183/188/101 on the six known contact holes of M_a-M_d), and the
  thin metal has no pad anywhere in the cell. The same holds for the two boxes under M_c at
  (17313,9166) and (17315,9035): M_c is a straight line there, its two real contacts have pads.
- **The two load gates are separate** (not one comb): between them at y 9122-9141 the clean
  shot is field (pink under M_d, green in the gaps either side). A 9 px salmon strip at
  x 17524-17532 there is taken to be field between the gap and the land's outline.
- **The thin metal** x 17438-17459 runs through the whole cell and on south through unit 1
  (strip image `py_strip.png`): it starts at the corner (17448,8097). Its dark stretch at
  y 9308-9362 is the edges of the diffusion and poly under its west half; the east half is
  metal throughout (brightness map of both metal shots).

### Units 1-3, and what differs from copy to copy

Extracted for all four bits (# = 0..3):

    d#_d_n  = NOT d#_d
    dl#_q   = NOT( (d#_d_n AND dbus_le) OR dl#_q_n )
    dl#_q_n = NOT( (d#_d   AND dbus_le) OR dl#_q   )
    db_b#   = NOT dl#_q_n

The latch cell holds what is common (x >= 17237). Drawn per unit:

| | Unit 0 | Unit 1 | Units 2, 3 |
|---|---|---|---|
| `d#_d` to band E | poly west from G4 to the contact (17205,8837), metal M_a x 17208 down to the pad (17207,9248) on band E | **no metal**: poly west from G4 along y 10192-10212, south down x 17225-17241 (in the gap between the metal x 17210 and M_b) to band E's west end at y 10394-10416 (both stripped shots at 3.2x, `u1_dd2.png`) | the same, moved by 1366 and 2732 (metal shot at 1.85x, `u2_left.png`, `u3_left.png`) |
| `dl#_q_n` from the latch to band F of the bus inverter | west along y 9155-9173, south down x 17157-17185, east along y 9415-9437 | west along y 10483-10501, south down x 17202-17222 **under the metal x 17210** (no contact: no pad; `dbl`'s review saw the same U), east along y 10781-10803 | the vertical is at x 17181-17200, west of that metal (y 11849-12169 and 13215-13535) |
| `db_b#` | pad under `dbl`'s contact (17207,9467), poly east along y 9462-9479 to the buried contact at N2's south-west tab (17314,9466) | from (17077,10832) east along y 10828-10845 | from (17165,12200) along y 12194-12211; from (17208,13563) along y 13560-13577 |

The four data lines of `dbl` therefore each end on the **output** of an inverter (a buried
contact on its node), which answers `dbl`'s open question (gate or node): the unit drives
the line. With `dbl` loaded the extraction joins D0-D3's latches to `db_b0`..`db_b3`.

### The latch enable `dbus_le`

Metal M_b, x 17243-17262: starts on the pad (17252,8990) of unit 0's band B, has a pad on
bands B and D of every latch (unit 0: y 8990, 9208; units 1-3: 10448, 10666; 11813, 12031;
13180, 13398), runs on to y 13614 and turns west to the pad (17160,13612) (`follow.py`: one
piece, 4630 px). From that pad a poly goes west along y 13602-13622, under two vertical
metals, to the pad (16990,13612), where a metal takes over and leaves the region west
(`mb_end.png`, `le_west.png`, overlay `le_ov.png`).

Followed beyond the region, **not drawn** (`follow.py` and one strip image,
`le_strip_m.png`): the metal goes west to x 16862, south to y 13810, west to x 16820 and
south along x 16818 to y 15800, then west, ending at about (16772,15800). On the run south
it carries **eight pads, each with a poly leaving west**, at about y 14040, 14260, 14435,
14650, 14900, 15120, 15385 and 15605. So `dbus_le` is not private to the four latches: it
also feeds eight things in the column x 16480-16800 (`areg`'s and `bd2`'s right-hand
columns, both untraced), and its driver is probably at its south-west end in `bd2`'s
right-hand column. Which way it is driven is not established (trap 20).

### P_x and P_y (established about the two lines of AMB-003)

- **P_x is one line common to all eight pad cells**, not a per-bit line. A single
  vertical metal at x 17633-17650 starts at D0's contact (17625,7380), has a contact
  to each cell's P_x poly at that cell's P_x height (17640,9115 for D1; 10860,
  12440, 14030, 15630, 17235 for D2-D6) and ends on D7's contact (17625,18835).
  Continuity was seen at 1.3x from D0 to D1 and at the bottom end, and at 0.5x in
  between. Where it is driven was not found: no branch was seen at the top or bottom
  end, so the driver must tap it somewhere along the column.
- **P_y is per bit.** D0's comes up the column on the thin metal of unit 0; D1's
  comes from a metal line at x 17110-17130 that rises from below to a contact at
  17120,9620, then crosses in poly (line 2); D7's arrives in poly down x 17590-17605
  and along y 18905-18935.
- Consequence for the pad cell, using the facts in pads.md: rows G (VCC) and H with
  strip 1 (gate P_x, row H tied to P_x by the buried contact) form a depletion load
  *on P_x*, and row K (VCC) with P_y's buried contact a depletion load *on P_y*. So
  both lines are open-drain as far as the column is concerned, with a pull-up in
  every pad cell (eight in parallel on P_x). That would make P_x an enable shared by
  the cells and P_y the data, with the cell containing the gating (rows I, J and the
  S1/S2 nets). This is inference from the earlier notes, not a new reading of the
  pad cell.

## Ports

| Name | Layer | Where | Direction | What |
|---|---|---|---|---|
| `d0_in` | metal x 17548-17566 | comes down from the D0 pad cell: poly from a contact near 17818,6578 left along y 6578, down to a contact near 17546,6755, then metal down; turns left at y 8188 (cross-under 17300-17500) | in | D0 pad after its protection structure. Drawn from y 8050 down |
| `d1_in` | poly | from the D1 pad cell's contact at 17822,8400 (drawn up to x 17835) | in | D1 pad after its protection structure |
| `d2_in`..`d5_in` | poly | G1 gate band of each chain, at 17291,8340 + offset | in | not followed to the pads |
| `dN_d` | poly, then metal | G4 output, 17290-17345 x 8825-8847 + offset | out of the chain | pad level, buffered and delayed; into the latch (drawn for D0-D3; chains 4 and 5: not followed) |
| `db_b0`..`db_b3` | poly | pads under `dbl`'s contacts (17207,9467), (17077,10832), (17165,12200), (17208,13563) | out | the internal data bus bits, driven here by `dbus_drv` |
| `dbus_le` | metal | leaves west at (16950,13614) | believed in | latch enable; see above for where it goes |
| P_y of D0 | metal x 17590-17610 from the pad cell (contact near 17580,7495), contact 17597,8097, poly cross-under y 8090-8105, contact 17510,8097, metal left to x 17448 and down as the thin metal | - | to the pad | not drawn |
| P_y of D1 | poly y 9225-9240 from the pad cell to x 17650, down x 17640-17655 (under the P_x metal) to line 2 (y 9590-9610), left to a contact at 17120,9620, metal x 17110-17130 downward | - | to the pad | not drawn |
| P_x | metal x 17633-17650, y 7380-18835 | contacts listed above | to the pads | common enable-type line, not drawn |
| lines from the core | metal | two wide metals arrive from the left at y 9520-9545 and 9565-9585 and turn down at x 17195-17215 and 17155-17175: `dbl`'s `db_b3` and `db_b2`; the one at y 9460-9480 to the contact (17207,9467) is `db_b0` | - | drawn in `trace/dbl.txt` |

**Internal data bus**: bits 0-3 leave the bus inverters as above. The two poly lines
leaving each chain to the left (y 8532 and 8792 in chain 0) are the capacitor taps, not
bus lines.

## Ambiguities

1. **The tie of `dl#_q` to band C** (the gate of N0's load and of N1's single pull-down).
   I did not find it and first drew an assumed contact under the thin metal at (17450,9095).
   Review round 2 found the box: 17414-17438 x 9072-9097, in the open gap between the VSS
   rail and the thin metal, heavy outline, poly-coloured inside in both chip-2 shots (metal
   174/126/76, stripped 159/122/63, like the poly below it and unlike the field above), in
   all four units; in the clean shot N0's west edge (x 17438-17442) is there at y 9070 and
   gone at y 9084, where tan runs into the box (my own 2 px map shows the same: 6-7 against
   2-3). Drawn as a buried contact there (not `?`). Residual doubt: chip 1's metal shot does
   not read as poly at the box centre (145/128/73). Under the thin metal itself there is no
   contact (no dim line before the heavy line, unlike the three ties there).
2. **N0's west tab** (`?B`, `?P` at 17286-17328 x 9020-9048): a box like a buried contact
   under M_c (M_c has no pad there) with a short orange bar west of it (x 17289-17296 in the
   chip-2 shots), rounded end at x 17286. Drawn as a poly stub tied to N0. Nothing leaves
   it: the corridor between M_b and M_c is field from y 9058 to 9139 (measured), and under
   M_c it is field. It joins nothing either way; if it is not a contact the circuit does
   not change.
3. The strip under the west half of the thin metal, x 17434-17449, y 8968-9013, beside the
   narrow diffusion of the third pull-down: I first read it as poly by colour (R-G about
   55). Review round 1 measured it against poly under the same metal: 182/127/120 against
   215/163/116. It is field. Nothing is drawn there. Closed.
4. **The thin metal** x 17438-17459: taken to have no contact in the latch (no pad on it;
   the boxes under it measure as diffusion, not as contact holes). The first notes call it
   D0's P_y. It is not drawn, and it does not end in unit 0: it goes on south through unit 1
   at least to y 9900. If it is one line down the column it is not a per-bit line; where it
   ends was not looked for.
5. **The width of the third pull-down of N0** (`?D` at 17465-17491 x 8940-8986). A dark
   line crosses its gate poly at x 17488-17496, y 8944-8966, at full strength in all four
   units and all four shots, in one straight line with the east end of the VSS strip from
   y 8915 to 8988 (review rounds 1-3; my row profiles at y 8930, 8956, 8979: the dip is at
   x 17488-17494 in each). Round 3 measured it as a diffusion edge under the poly (6 px, like
   the edges under the small inverter's load gate), with the poly's own edge beside it at
   x 17498 south of the gate. So the diffusion under the gate reaches from x 17450 to 17491
   and the pocket south of the gate (17467-17491, 8968-8988) is drain: W about 41, not 17.
   Marked `?` because the pocket has no clear diffusion colour in any shot (clean shot
   116/99/77 against 115/158/76 for the open strip north of the gate and 141/137/74 for
   open field; it is 18 px tall between two poly outlines). Without the `?` item the
   transistor is W 17. No connection depends on it.
6. `d0_b` capacitor: contacts cut, strap absent in both metal shots. Looks like a
   metal-mask option. No effect on logic. (First session.)
7. Chains 2-5 are assigned to D2-D5 by position only. Chains 2 and 3 now drive `db_b2` and
   `db_b3` through their latches, which agrees with `dbl`'s bit numbers for those lines.
8. Device sizes: W/L of the cell's transistors as drawn are within about 5 px, except the
   third pull-down (Ambiguity 5).

## Review

**Round 1** (2026-11-17, a fresh agent; images and scripts `cache/scratch/dbus/review-1/`).
Told to suspect: where band A ends and whose the poly east of it is; the assumed tie of N0
to band C; each box under the thin metal and under M_c; band D's end; whether the two load
gates are separate; the upside-down copies and the per-unit joins; the bus inverters' land
width and south-west contacts; M_b's end. It read claims 1-4 and 6-10 at 4-6x in at least
two shots with row and column profiles, compared every copy with its master by block
difference maps, profiled the thin metal from y 8110 to 13700 in both metal shots (16 px
wide, continuous, no pad), and checked the per-unit wiring by overlay (unit 3's against
unit 2 by difference map only).

- Finding 1, **confirmed and fixed**: the diffusion under bands D and E is wider than drawn;
  its west edge is at x 17320-17324 from y 9150 to about 9285. My own map of the clean shot
  agrees (tan at x 17326-17334 against pink west of the line, at y 9185-9194, 9224-9236 and
  9263-9278; bands D and E as red there as over the rest of the channel). Drawn: W 77 for
  D and E. No connection changes. The reviewer's doubt whether the mid node between D and
  E is one piece (field tint at x 17338-17348 in the chip-2 shots) is in a gap between two
  metals; in the clean shot the node is tan out to x 17325. Left as one node.
- Finding 2, **no change, recorded** (Ambiguity 5): the line across the third pull-down's
  gate poly is not explained by the drawn geometry.
- Notes taken over: the VSS land above band C starts at y 9063, not 9051 (fixed);
  Ambiguity 3's strip is field (closed); M_b's end poly passes under three metals.
- Could not check: the assumed tie (Ambiguity 1): in all four units a 10-12 px dark band
  with no field colour between N0's end and band C, as at N1's certain tie, but no box and
  no contact patch.

**Round 2** (2026-11-17, a fresh agent, not shown round 1; `cache/scratch/dbus/review-2/`).
Told to suspect: the extent of every diffusion; unit 3's per-unit wiring and the joins of
units 2 and 3 (read at 1.85x before); the stretch between each upside-down latch and the
bus inverter below it; band A's end and the third pull-down; the boxes under the thin metal
and M_c; the assumed tie; anything left out. It read the junctions at 4-6x in two to four
shots, profiled each per-unit poly along its length in four shots, ran `follow.py` on
M_a-M_d and `cellcheck.py` on the copies (0.92-0.95).

- Finding 1, **confirmed and fixed**: the tie of N0 to band C is a real box about 20 px west
  of the assumed one (Ambiguity 1). Same net; the equations stand and no longer rest on a
  `?` item.
- Not decided, recorded (Ambiguity 5): the width of the third pull-down.
- Found correct: band A's end; the poly east of x 17437 to M_d's pad and its channel; bands
  B and D; the two load gates separate; all five boxes buried contacts; `dbus_drv`'s land
  and node both x 17300-17431; one VSS land at each latch/inverter junction; every per-unit
  poly reaches both its ends and touches no neighbour; M_b's end.
- Could not check: N0's west stub beyond its being a dead end in all four units; diffusion
  against field by colour in the chip-2 shots.

**Round 3** (2026-11-17, a fresh agent, not shown rounds 1-2; `cache/scratch/dbus/review-3/`).
Told to suspect: the tie box at (17427,9085) and anything else in the five gaps between the
vertical metals that could have been dismissed as a gap artefact; which polys under the
thin metal and M_d touch; the small inverter's gate; unit 1's join with its chain; the
transistor count. It scanned columns in each gap over y 8885-9505 against the trace, read
the junctions at 4-6x in two to four shots, compared the copies numerically and by montage.

- Finding 1, **taken over as `?D`**: the third pull-down of N0 is about 41 wide, not 17
  (Ambiguity 5). A size, not a connection.
- Minor geometry, fixed: the small inverter's gate is L 22 (east edge x 17424); band C in the
  gap reaches y 9130.
- Found correct: the tie box in all four units, separated by field from the VSS land and
  from the pocket north of it; nothing untraced in the gaps; bands A, B, D end before the
  field strip x 17420-17432; the polys under M_d and the thin metal separate where claimed;
  band E into the inverter's gate; all boxes buried contacts; M_a-M_d one piece each; twelve
  transistors in unit 0, none missing; unit 1's `d1_d` does not meet `d1_c`.
- Could not check: poly continuity through the contact (17450,9346) (only the common bottom
  edge supports it); the tie box's opening to N0 in chip 2; where the thin metal ends.

## Not done

- **Bits 4-7.** Chains 4 and 5 have no latch below them (chain 5 starts 758 px below
  chain 4); where `d4_d` and `d5_d` go is not followed. Where the input buffers and
  latches of D6 and D7 are is not known: the lower part of the column (y 15100-16600) is
  the first place to look. `db_b4`..`db_b7`'s routes to this column are not drawn (`dbl`
  did bits 0-3 only).
- Logic at y 15100-16600 (single gates on the 152 px pitch), logic above D0 at
  17200-17700 x 5250-5900.
- Left-hand wiring of chains 1-5: the capacitor taps (`d#_b`, `d#_c`; in unit 1 a poly
  comes down x 17181-17197 and turns west along y 10325-10345, probably `d1_c`'s), the
  input lines of D2-D5 (the contact (17293,10920) below unit 1 is on D2's cross-under).
- Channel wiring x 17590-17830: the P_x line, the P_y lines, input lines of D2-D7. The
  driver of P_x. The thin metal x 17438-17459 (Ambiguity 4): follow it to both ends.
- `dbus_le` west of x 16950: drawn to the region's edge only; its eight taps and its
  south-west end (16772,15800) belong to `areg`'s and `bd2`'s right-hand columns.
- Pad cell (AMB-003): `dpad`.
