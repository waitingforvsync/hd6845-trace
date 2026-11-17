# Data bus interface column (`dbus`)

Region: x 17050-17700, y 5300-17000, and the D0-D7 pad cells to its right.
Trace: `trace/dbus.txt`. Scratch tools: `tools/dbus_mosaic.py` (the same rectangle at
several offsets side by side, for comparing repeats), `tools/dbus_autocorr.py`
(vertical pitch of a strip).

## Status

Traced, extracting (122 transistors, 0 errors, 0 warnings), overlay-checked:

- the input buffer chain (four inverters), cell `dbus_in`, six copies (D0-D5); D0's and
  D1's input lines (first session);
- **the input latch of D0-D3** (cell `dbus_lat`, ten transistors, master under chain 0,
  three more copies upside down under chains 1-3) and **the inverter that drives each
  data bus bit from it** (cell `dbus_drv`, two transistors, four copies at the chain
  pitch), with the lines between them, the lines from the chains (`d#_d`) and the ends of
  `dbl`'s four data lines: `db_b0`..`db_b3` are driven nets (2026-11-17 15:28 +0000);
- the latch enable `dbus_le` (metal M_b) from its top pad down the column and west to the
  region's edge;
- **run 3 (2026-11-17 17:53 +0000):**
  - **the input buffers of D6 and D7** (cell `dbus_in2`, nine transistors, two copies at
    y 15150-15770 and 15780-16400): four inverters like `dbus_in`, upside down, with wider
    pull-downs. D6's input line is drawn from the foot of D6's protection node to the
    chain; D7's is drawn to the region's south edge;
  - **the L arm of every first-stage gate is a second pull-down finger**, not a dead end
    (AMB-004 for this column): added to `dbus_in` (six transistors) and present in
    `dbus_in2`;
  - **where the four upper bits go**: `d4_d`, `d5_d`, `d6_d`, `d7_d` each leave the column
    west in poly (y 14000, 14696, 15173, 15650) and are drawn to the region's edge at
    x 16950. There is no latch for bits 4-7 in this column;
  - **the inverter at the foot of the column** (two transistors, y 16415-16590) and **the
    thin metal x 17438-17459, which is its output and is `d0_out_n`**: drawn end to end
    and joined to `dpad`'s contact, so D0's output data line has its driver.

Not traced: the latches of bits 4-7 (west of this region, see "Where bits 4-7 go"), the
logic above D0, the left-hand wiring of chains 1-5, the channel wiring to the pads for
D2-D5 and D7, the other seven `d#_out_n` lines. See "Not done".

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
| Input chain, D6 | 17262-17590 x 15150-15770 | cell `dbus_in2`, traced (run 3). `findcell` with `dbus_in`: 0.46 at best (upside down), so not a copy |
| Input chain, D7 | the same cell at (0,630) | placed: `tools/dbus_localmatch.py` 0.88 clean shot, 0.85 metal, 0.84 chip-2 stripped; overlay at 2x (`ovB.png`). Its wiring west of x 17265 differs and is drawn per copy |
| Inverter at the foot of the column | 17300-17590 x 16415-16590 | traced (run 3): drives the thin metal (`d0_out_n`) |
| Capacitor rectangle of D6's c tap | 17147-17257 x 16776-16905 | drawn (plain diffusion, one contact) |
| Capacitor rectangles of chains 4, 5 | 16880-16950 x 13820-13950; 17100-17210 x 14090-14210; 17130-17230 x 14820-14930 | seen, not drawn |
| No latch follows chains 4-7 | - | chain 5 starts 758 px below chain 4, chain 6 679 px below chain 5, chain 7 630 px below chain 6 |
| Logic above D0 | 17200-17700 x 5250-5900 | several gates, not looked at |

findcell (metal and clean shot, threshold 0.4) finds no seventh or eighth copy of
`dbus_in`: the buffers of D6 and D7 are a different cell (`dbus_in2`, below chain 5).

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
  into the latch, ending at the contact (17207,9248) on band E's pad.
- G1's gate poly continues into an L (17413-17503 x 8292-8318). The first notes said it
  crosses no diffusion (AMB-004). **It does** (run 3): see "The L arm" below. So
  `dN_a` has two pull-downs on `dN_in`: W 60 under the rail and W about 22 under the
  thin metal.

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
| Inverter N3 | band E turns south at x 17402-17424 (y 9255-9322) between the VSS land and the node x 17425-17476, y 9272-9310; load gate x 17475-17525, y 9252-9316 (chip-2 shot: orange block with the diffusion's edge across it at y 9270); VCC land x 17530-17586, y 9238-9300, contact (17555,9268). The node goes south under the thin metal to the buried contact (17450,9346) on the poly y 9336-9360 that joins the load gate's stem and runs west to M_c's bottom pad |
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
piece, 4630 px). From that pad a poly goes west along y 13602-13622, under three vertical
metals (x about 17036, 17080, 17122), to the pad (16990,13612), where a metal takes over and leaves the region west
(`mb_end.png`, `le_west.png`, overlay `le_ov.png`).

Followed beyond the region, **not drawn** (`follow.py` and one strip image,
`le_strip_m.png`): the metal goes west to x 16862, south to y 13810, west to x 16820 and
south along x 16818 to y 15800, then west, ending at about (16772,15800). On the run south
it carries **eight pads, each with a poly leaving west**, at about y 14040, 14260, 14435,
14650, 14900, 15120, 15385 and 15605. So `dbus_le` is not private to the four latches: it
also feeds eight things in the column x 16480-16800 (`areg`'s and `bd2`'s right-hand
columns, both untraced), and its driver is probably at its south-west end in `bd2`'s
right-hand column. Which way it is driven is not established (trap 20).

### The L arm of the first stage is a second pull-down (run 3, 2026-11-17)

In `dbus_in` (and in `dbus_in2`, mirrored top to bottom) the gate poly of the first
inverter runs past its diffusion, turns along the VSS land in the gap east of the rail,
and turns again to run east under the thin metal and on to beside the load. Under the
thin metal it crosses a diffusion (traced):

- North of the arm in `dbus_in` (south of it in `dbus_in2`) a tan strip lies under the
  rail, the gap and the thin metal: chain 0, y 8269-8292, x 17400 to about 17490. Under
  the rail it is one area with the VSS land down to the gate band, and in both chip-2
  shots one outline (bottom or top edge in one line from under the rail to x 17490,
  with a rounded corner there). Colour under the thin metal 180/150/130 against field
  184/122/125 further up (`c0_larm.png`, 4.3x, three shots).
- On the other side of the arm is the output node's column under the thin metal.
- The arm itself, under the thin metal, has the colour of poly over a channel:
  240/171/120 in chain 0, 236-242/169-175/120-125 in chains 1-5, 241/173/121 and
  237/172/121 in the two `dbus_in2` copies; the gate band under the rail measures
  241/175/122, poly over field under the same thin metal 196/144/100 (`patch.py`).

So the first stage has a second transistor, gate `d#_in`, between `vss` and `d#_a`, W
about 22-26, L 22-26. The logic is unchanged (`d#_a` = NOT `d#_in`); the pull-down is a
third wider than drawn before. Drawn in both cells; eight transistors added. **The same
L arm is on the input inverters of the bottom row (R/W, RS, CS: AMB-004) and probably on
RES and LPSTB**: those were not looked at (proposed as a re-read item in the handoff).

### The input chains of D6 and D7 (cell `dbus_in2`), traced 2026-11-17

Below chain 5 the column has eight more gates under the same two rails, in two groups of
four, 630 px apart. Each group is a four-inverter chain like `dbus_in` turned upside down
(input at the bottom, output at the top), but it is another layout: wider pull-downs,
other loads (`findcell`: 0.46). As extracted, for # = 6, 7:

    d#_a = NOT d#_in      stage 1, bottom gate (y 15616-15765 in chain 6)
    d#_b = NOT d#_a       stage 2 (y 15470-15605)
    d#_c = NOT d#_b       stage 3 (y 15314-15450)
    d#_d = NOT d#_c       stage 4, top gate (y 15160-15296)

Where things are in chain 6 (overlay `ovA.png` 2.05x; views `g1.png`..`g4.png` at 2.8x in
three shots; chain 7 is 630 lower, overlay `ovB.png`):

| What | Where |
|---|---|
| Stage 4 | VSS land y 15250-15296 (contact 17386,15273), gate band y 15227-15250 from x 17270 to 17430, output node y 15187-15227. Node east through a neck (y 15188-15208) to a column under the thin metal (x 17446-17472, y 15173-15246); load gate x 17475-17524, y 15160-15221 over the strip y 15176-15210; VCC land x 17524-17588, contact (17552,15205); load gate tied to the node by the box (17464-17499, 15216-15249) at the foot of its stem |
| Stage 4 output | the node's west box (17310-17340, 15184-15213), a buried contact: poly west along y 15185-15199, a jog up at x 17225-17245, west along y 15165-15181: `d6_d` |
| Stages 3 and 2 | output node y 15334-15368 (x 17307-17421) above the gate band y 15377-15397 (x 17270-17391), VSS land below it west of the rail (x 17307-17371, y 15397-15447, contact (17348,15428), the rail widened over it). The node drops past the band's east end (x 17397-17421) to the tie box (17424-17453, 15375-15399); the load gate is x 17428-17527, y 15314-15347 with its open part down to y 15377 and a bar y 15363-15375 west to the box; load strip y 15338-15358; VCC land x 17530-17587, contact (17556,15367). Stage 2 is the same, 155 lower |
| Stage 1 | as stage 4, 455 lower, plus the L arm (x 17423-17437 down to y 15742, then east along y 15720-15742 to x 17506) with the second pull-down under the thin metal (the node's column x 17444-17470 down to the VSS land's east extension y 15747-15765) |
| Links | each stage's output leaves by a west box and runs west to x 17270, then **up** x 17270-17292 to the next stage's gate band. Stage 3's and stage 2's output lines also run on west to a pad each (the c and b taps) |
| Pull-down widths | the diffusion's west edge is at x 17314 (stages 1, 4) and 17307 (stages 2, 3), west of the rail: it shows as a dark line across the gate band in the metal shot and both stripped shots, and the band is brighter east of it (`g1w.png`, 4.3x; in stage 3 the band measures R-G 80-90 from x 17310 to 17368 and 20-40 west of it). W 107 (stages 1, 4), 64 (stages 2, 3) |

Per copy, west of x 17265 (overlays `ov67.png`, `ov9.png`):

| | Chain 6 (D6) | Chain 7 (D7) |
|---|---|---|
| Input | pad (17254,15695); metal south along x 17254 to y 15890, east to x 17298, south to the pad (17297,16662); poly east along y 16655-16672 under both rails and the `d_hiz` metal, north along x 17662-17678 (colour run y 16510-16676 in the metal shot), east along y 16509-16526 under `dpad`'s rail to the pad (17838,16519), which is on the metal that comes down from D6's protection node (`in6.png`, `in67.png`). **Joined: `d6_in` is pin D6's net** (`@alias d6 d6_in`) | pad (17254,16325); metal south to the pad (17253,16715); poly east along y 16705-16722 to under the VCC rail, then south under the rail's west half (x 17531-17548) past y 17000 (`in7.png`): drawn to the region's edge. Believed D7's (the only pad left); not joined |
| c tap | pad (17213,15347), metal south along x 17210 to a contact (17228,16843) on a diffusion rectangle 17147-17257 x 16776-16905 (a capacitor, as for `d0_c`) | pad (17082,15976), metal south along x 17080 to y 16758, west out of the region (`follow.py`: on to x 16837, south to y 17333); not followed further |
| b tap | pad (17170,15498), metal south along x 17165, **ends at y 16742 on nothing** (no pad): a stub, as `d0_b`'s cut strap | pad (17127,16127), metal south along x 17124, ends at y 16806 on nothing |
| `d#_d` | west along y 15165-15181 to the region's edge | west under chain 6's three metals to x 17184, **north** along x 17182-17197 in the gap between two of them (orange in the metal shot from y 15644 to 15830, field above and below: profile), west along y 15642-15657 to the region's edge |

### Where bits 4-7 go (traced to the region's edge)

| Line | Route | Leaves at |
|---|---|---|
| `d4_d` | G4's output west to the pad (17255,14301); metal north along x 17253 to y 13998 and west to the pad (17205,13998) (`follow.py`: one piece); poly west along y 13993-14008 under the vertical metals | (16950,14000) |
| `d5_d` | G4's output west to the pad (17254,15064); metal north along x 17254 to y 14697, west to the pad (17167,14697) (`follow.py`: corner at (17245,14698), end (17163,14697)); poly west along y 14688-14704 | (16950,14696) |
| `d6_d` | above | (16950,15173) |
| `d7_d` | above | (16950,15650) |

`d4_b`'s poly ends at x 17257, 35 px east of `d4_d`'s upper pad: the clean shot is field
(pink under the metal's corner) between them (`d4d_b.png`, 2.4x).

**Believed, not traced**: the four lines go to four copies of the input latch in the gate
column at x 16480-16800 (`areg`'s and `bd2`'s right-hand columns, outside this region).
The eight tapped pads of `dbus_le` on its run down x 16818 are at about y 14040, 14260,
14435, 14650, 14900, 15120, 15385, 15605: four pairs 215-220 apart, which is the distance
between a latch's two `dbus_le` bands (218 in `dbus_lat`), and each of the four lines
arrives about 45 px outside one pair (above the first pair, below the other three), where
band E of the latch would be. A survey view at 0.42x (`s_wide.png`) shows four latch-like
units there at about y 13950-14300, 14400-14700, 14900-15200 and 15400-15700.

### The inverter at the foot of the column, and the thin metal (`d0_out_n`)

Traced (run 3; `g9.png`, `g9b.png` at 3-3.3x, overlay `ov9.png`):

    d0_out_n = NOT dbus_do0_in

- Pull-down under the end of the VSS rail (the rail ends at y 16552): gate band
  y 16444-16463, from the region's west edge (16950,16453) under the metals to x 17424;
  source the VSS land north of it, which is chain 7's stage-1 land (one diffusion under
  the rail from y 16335 to the band: `railprof.py`); output node south of it, x 17354-17419,
  y 16463-16497.
- The node runs east through the gap to a diffusion strip under the thin metal
  (x 17450-17474, y 16423-16560) that widens into a pad (17435-17474 x 16545-16590).
  **The thin metal x 17438-17459 ends on that pad** (a ring in the metal shot, a pit in
  the clean shot at (17452,16564)).
- Load: gate x 17475-17528, y 16455-16512 over the strip y 16465-16497; VCC land
  x 17541-17587, contact (17558,16478); tied to the node by a box at about
  (17462-17502, 16418-16452) (read at 3.3x only).
- The thin metal runs up the whole column to its corner at (17448,8103), east to the pad
  (17512,8103), in poly east along y 8095-8113 under the `d0_in` metal (no contact) to the
  pad (17600,8103), and in metal north up the channel to `dpad`'s contact (17597,7492) on
  D0's `out_n` poly (`follow.py`: one piece 7492-8134; `thin_top.png`, 4.4x, two shots).
  **Joined**: with `dpad` loaded the extraction has `d0_pu` = NOR(`d_hiz`, `d0_out_n`)
  with `d0_out_n` = NOT `dbus_do0_in`.
- Along the column the thin metal is 16 px wide and dim, and the follower's metal test
  does not see it (trap 19). A profile of its core (x 17444-17454) in both metal shots from
  y 8100 to 16570 is dim (R < 150 for more than 14 px) only where the trace has poly or a
  buried-contact box under it, repeating with the cells; review round 1 of run 2 found
  it continuous, 16 px wide, with no pad from y 8110 to 13700.

What `dbus_do0_in` is: a poly from the west along y 16444-16463, not followed. It is the
data that the chip puts on D0, in true sense (the pad is NOT `d0_out_n`).

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
| `dN_d` | poly, then metal | G4 output, 17290-17345 x 8825-8847 + offset | out of the chain | pad level, buffered and delayed; into the latch (D0-D3) |
| `d4_d`, `d5_d`, `d6_d`, `d7_d` | poly | leave west at (16950,14000), (16950,14696), (16950,15173), (16950,15650) | out | the buffered pins D4-D7, to the latch column at x 16480-16800 (believed) |
| `d6_in` | poly | pad (17838,16519) under the metal from D6's protection node | in | pin D6 (alias of `d6`) |
| `d7_in` | poly under the VCC rail, x 17531-17548 | leaves south at (17540,17000) | in | believed pin D7; not followed to the pad |
| `d7_c` | metal | leaves west at (16950,16758) | - | chain 7's c tap, probably to a capacitor; not followed |
| `dbus_do0_in` | poly y 16444-16463 | enters at (16950,16453) | in | input of the inverter that drives `d0_out_n` |
| `d0_out_n` | metal x 17591-17609 | joins `dpad`'s metal at (17600,7565) | out | D0's output data line (the thin metal) |
| `db_b0`..`db_b3` | poly | pads under `dbl`'s contacts (17207,9467), (17077,10832), (17165,12200), (17208,13563) | out | the internal data bus bits, driven here by `dbus_drv` |
| `dbus_le` | metal | leaves west at (16950,13614) | believed in | latch enable; see above for where it goes |
| P_y of D0 | now `d0_out_n` (row above): drawn | | | |
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
4. **The thin metal** x 17438-17459. Closed in run 3: it is `d0_out_n`, one line from the
   pad (17512,8103) at the top to the pad (17452,16564) on the output of the inverter at
   the foot of the column, with no contact between (no pad on it; where it is dim, poly or
   a buried-contact box lies under it). What rests on a profile and not on a view: its
   continuity between y 13700 and 16420 (trap 19).
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
9. **The box beside the `d6_in` metal at (17314,16488)** (`?D`). The output node of the foot
   inverter has a west tab that ends in a heavy-outlined box, 17301-17328 x 16474-16502,
   right beside the metal x 17290-17306 that carries `d6_in` south. The metal is dim over
   y 16476-16512 in both chips with a dark-bright-dark pattern (R 40-60, 100-150, 50,
   against 200-226 on the plain line), which `follow.py` reads as an end from both sides.
   Readings: (a) the box's outline printing through the metal's east edge, no contact: the
   metal is not widened there (bright core 12-14 px, as on the plain line), the thin metal
   shows the same dimming over every buried-contact box it crosses, and a contact would
   tie pin D6 to the output of a static gate, which makes no sense; (b) a contact joining
   `d6_in` to that node. The box's centre is very dark in the three shots with metal or
   oxide on (metal 48/40/15, chip-2 stripped 56/49/33, chip-1 metal 56/46/21) and pale in
   the clean shot (160/142/114), unlike the pads (bright centre) and unlike the buried
   contacts nearby (metal 118-141): it may be a contact cut that no metal covers, as the
   cut straps of the b taps suggest. **Working assumption: (a)**; the tab and box are
   drawn as diffusion (`?D`), joined to nothing else. To settle: a 6x view of the box in
   chip 1's metal shot, and whether the same box exists where nothing passes.
10. **Load sizes in `dbus_in2`.** Stages 2 and 3: under the thin metal the load gate is seen
   as a block y 15314-15347 and a bar y 15363-15375 with a 12 px tan strip between
   (178/162/102, diffusion), while under the open part of the gate the strip's edges are
   at y 15336 and 15360 (metal shot). Drawn as a strip y 15338-15358 under a gate
   x 17428-17527: W/L extracts as 40/39; the channel may be as short as 55 (only the open
   part) or as long as 100. The stage-4/1 load (35/48) and the foot inverter's (32/53) are
   read at 2.8-3.3x. No connection depends on these.
11. **Chain 7 is D7's** by elimination only: its input line is drawn to y 17000 and goes on
   south under the VCC rail. Chains 2-5 are still assigned by position (Ambiguity 7).
12. **The tie box of the foot inverter's load** (17462-17502, 16418-16452) was read at 3.3x
   in the two stripped shots only; drawn as an ordinary buried contact because every load
   in the column is tied that way.
13. `dbus_in`'s pull-down widths (60 for G1/G4, 56 for G2/G3) were drawn in the first
   session from the land under the rail. In `dbus_in2` the diffusion reaches west of the
   rail (W 107 and 64). Whether `dbus_in`'s does too was not looked at (a size only).

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

**Round 4** (2026-11-17, a fresh agent, not shown rounds 1-3; `cache/scratch/dbus/review-4/`).
Told to suspect: every place where one named net could be two or two one (the three long
polys of each unit against each other and the chains' other outputs; the poly through the
contact (17450,9346); what M_b touches on its 4600 px; M_a's pad; the data bus poly against
band F and the loop); the tie box and the `?D` pocket; each N2's south-west contact; unit
3; anything left out. It read the junctions at 4-5x in three shots with 1-2 px colour
profiles, ran `follow.py` on M_a-M_d, a strip of M_b end to end, `cellcheck.py` on the
copies (0.92-0.95) and overlays of units 1-3 at 2.7x.

Round 4: no findings.

Its observations, not errors: three of `follow.py`'s contact candidates on M_b ((17252,9141),
(17252,11232), (17255,11289)) are dark blotches in chip 1's metal shot only, with no pad and
continuous metal in chip 2: taken as damage on chip 1. Three wording slips in these notes,
corrected. It could not check: whether N2's south-west box takes its diffusion from above or
from the neck at x 17328-17350 (the same net either way), the `?D` pocket's width, `dbl`'s
bit order, the thin metal's ends.

## Not done

- **The latches and bus inverters of bits 4-7**: not in this region. `d4_d`..`d7_d` leave
  west at x 16950 (y 14000, 14696, 15173, 15650) towards the gate column x 16480-16800,
  y 13950-15700, where `dbus_le` has its eight taps (see "Where bits 4-7 go"). That column
  is `areg`'s right-hand column down to y 14700 and `bd2`'s below; `db_b4`..`db_b7` are
  expected to be driven there. First thing to try: `findcell` with `dbus_lat`
  (17230 8885 17590 9370) and `dbus_drv` restricted to 16450,13900:16850,15750.
- `dbus_do0_in` west of x 16950 (poly along y 16453), and the drivers of `d1_out_n`..
  `d7_out_n` (D1's rises on a metal x 17110-17130 to a contact (17120,9620)): the five to
  seven vertical metals at x 16945-17130 left of chains 4-7 are probably these lines and
  `dbl`-like bus lines; none is drawn.
- `d7_in` south of y 17000 to D7's protection; `d7_c`'s metal west of x 16950.
- Logic above D0 at 17200-17700 x 5250-5900.
- Left-hand wiring of chains 1-5: the capacitor taps (`d#_b`, `d#_c`; in unit 1 a poly
  comes down x 17181-17197 and turns west along y 10325-10345, probably `d1_c`'s; chain 4:
  `d4_c` runs west and diagonally to a pad (16945,14345), `d4_b` to a pad (17158,14045)
  with only a dot of metal beside a rectangle 17100-17210 x 14090-14210; chain 5: `d5_c`
  to a pad (17210,15020) and by metal north to a rectangle 17130-17230 x 14820-14930), the
  input lines of D2-D5 (the contact (17293,10920) below unit 1 is on D2's cross-under; a
  poly along y 14440-14460 from a pad (16945,14450) reaches chain 5's input pad at about
  (17278,14420)).
- Channel wiring x 17590-17830: `d_hiz`'s driver, the input lines of D2-D5.
- `dbus_le` west of x 16950: drawn to the region's edge only; its eight taps and its
  south-west end (16772,15800).
- Ambiguity 9 (the box beside `d6_in`'s metal).
