# Data bus interface column (`dbus`)

Region: x 17050-17700, y 5300-17000, and the D0-D7 pad cells to its right.
Trace: `trace/dbus.txt`. Scratch tools: `tools/dbus_mosaic.py` (the same rectangle at
several offsets side by side, for comparing repeats), `tools/dbus_autocorr.py`
(vertical pitch of a strip).

## Status

Traced, extracting, overlay-checked: the input buffer chain (four inverters) as cell
`dbus_in`, placed six times (D0-D5); the input line of D0 from where it enters the
column, and the whole input line of D1 from the pad cell's contact.

Surveyed, with coordinates below, but NOT traced: the gate group ("cluster") under
each of chains 0-3, all other logic in the column, the channel wiring to the pads.
The pad cell (AMB-003) was not attempted; what the column tells us about its two
lines is under "P_x and P_y" below.

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
| Cluster 0 | 17150-17590 x 8885-9520 | not traced, see below |
| Clusters 1-3 | cluster 0 + 1366, 2732, 4098 (by eye at 0.5x; not checked) | not traced |
| Cross-unders between units 0 and 1 | poly "line 1" y 9545-9566, "line 2" y 9590-9610, both under both rails | line 1 drawn (D1 input); line 2 is D1's P_y, not drawn |
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
    dl0_q   = NOT( (d0_d_n AND dbus_le) OR dl0_q_n )    gate N0   (marked: one assumed tie)
    dl0_q_n = NOT( (d0_d   AND dbus_le) OR dl0_q   )    gate N1   (marked: the same tie)
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
| Third pull-down of N0 | a narrow diffusion x 17450-17467 runs from the VSS land's east strip (y 8920-8942, which goes on to x 17494) south to N0; the poly from M_d's top pad (17491,9010) runs up x 17498-17520 and west along y 8944-8966 over it and ends at x 17437. Gate = `dl0_q_n` |
| Load of N0 | poly x 17476-17518, y 9049-9121 under metal M_d; channel y 9063-9094. It is band C's east end |
| Column, middle part, x 17350-17400 | VSS land 9051-9113 (contact 17362,9087); band C 9111-9133; node N1 9133-9198; band D 9196-9219; mid node; band E 9240-9262; VSS land 9268-9310 (contact 17368,9285) |
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
| `dN_d` | poly, then metal | G4 output, 17290-17345 x 8825-8847 + offset | out of the chain | pad level, buffered and delayed; into the cluster |
| P_y of D0 | metal x 17590-17610 from the pad cell (contact near 17580,7495), contact 17597,8097, poly cross-under y 8090-8105, contact 17510,8097, metal left to x 17448 and down as the thin metal | - | to the pad | not drawn |
| P_y of D1 | poly y 9225-9240 from the pad cell to x 17650, down x 17640-17655 (under the P_x metal) to line 2 (y 9590-9610), left to a contact at 17120,9620, metal x 17110-17130 downward | - | to the pad | not drawn |
| P_x | metal x 17633-17650, y 7380-18835 | contacts listed above | to the pads | common enable-type line, not drawn |
| M_b | metal x 17243-17262 | from 17252,8990 down through unit 1 | unknown | shared control line of the clusters, not drawn |
| lines from the core | metal | two wide metals arrive from the left at y 9520-9545 and 9565-9585 and turn down at x 17195-17215 and 17155-17175; another arrives at y 9460-9480 to a contact at 17207,9470 | unknown | not followed |

**Internal data bus: not identified.** The two poly lines leaving each chain to the
left (y 8532 and 8792 in chain 0) are the capacitor taps, not bus lines. The bus
lines must leave from the clusters or run in the left-hand wiring field.

## Ambiguities

- `d0_b` capacitor: contacts cut, strap absent in both metal shots. Looks like a
  metal-mask option. No effect on logic.
- Chains 2-5 are assigned to D2-D5 by position only.
- Whether clusters 1-3 are exact copies of cluster 0 has not been checked.

## Not done

- Clusters 0-3 (start with the diffusion-column table above; the open questions are
  the loads and the structures at x 17400-17525).
- Left-hand wiring of chains 1-5: capacitor taps, and where each `dN_d` goes
  (for chains 4 and 5 there is no cluster below).
- Logic at y 15100-16600 (and the D6, D7 input buffers), logic at y 5250-5900.
- Channel wiring x 17590-17830: P_x line, P_y lines, input lines of D2-D7.
- The driver of P_x.
- Pad cell (AMB-003): not attempted.
