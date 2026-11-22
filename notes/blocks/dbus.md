# Data bus interface column (`dbus`)

Region: x 17050-17700, y 5300-17000, and the D0-D7 pad cells to its right.
Trace: `trace/dbus.txt`. Scratch tools: `tools/dbus_mosaic.py` (the same rectangle at
several offsets side by side, for comparing repeats), `tools/dbus_autocorr.py`
(vertical pitch of a strip).

## Status

Traced, extracting (127 transistors, 85 nets, 0 errors, 0 warnings), overlay-checked:

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

- **run 4 (2026-11-17 18:55 +0000):**
  - **the "logic above D0" is the east half of `r9c`'s five units** (x 17500-17670,
    y 5260-5870): each unit's depletion load and its contact to the rail x 17616-17667,
    which is VCC (cell `dbus_r9l`, one transistor, five copies). With `r9c`'s pull-downs
    the full extraction now gives `ra#_cmp = NOT ra#_drv_in` for all five (AMB-012):
    firm for bits 0-3; bit 4's still depends on `r9c`'s `?P` on its gate line.
  - **the input lines of D2, D3, D4 and D5** (2026-11-17 19:10 +0000), each from the
    pin's protection node in `dpad` to the first gate of its buffer chain: `d2_in`..
    `d5_in` are now aliases of the pins `d2`..`d5` (wiring only, no transistors), so all
    of D0-D6 are joined to their buffers.
  - **`d1_out_n`, D1's output data line** (2026-11-17 19:15 +0000), from the D1 pad cell
    down the channel, west on chain 1's "line 2" and south on a 6,140 px metal to a poly
    that leaves the region west at (16950,16344): its driver is west of the column, not at
    the column's foot like D0's.
  - **correction to run 3**: `dbus_do0_in` does not come from the west edge. Its poly ends
    on a pad (16993,16451), and a metal from that pad runs south and then west out of the
    region at (16950,16712).

- **run 5 (2026-11-17 20:09 +0000):**
  - **`d2_out_n`, `d3_out_n`, `d4_out_n`, `d5_out_n`, the output data lines of D2-D5**
    (wiring only): each from the pad cell's strip 4 along the chain's "line 2" to a pad in
    the wiring field and by a long metal south to a pad in a staircase at the column's
    south-west corner (x 16860-17035, y 15830-16345), where a poly leaves west. Joined to
    `dpad`'s cells in the extraction. Their drivers are west of the column, like D1's.

- **run 6 (2026-11-17 20:52 +0000):**
  - **the capacitor taps of chains 1-5** (wiring and plain diffusion only, no transistor):
    each chain's `d#_b` in poly to a pad that has only a dot of metal, with an unstrapped
    plain diffusion rectangle nearby (`dbus_cap1b`..`dbus_cap5b`), and each `d#_c` in poly
    to a pad, a metal strap and a contact on a second rectangle: the pattern of chain 0,
    laid out differently in every chain. See "The capacitor taps of chains 1-5".

- **run 7 (2026-11-17 16:40 -0600; Matt Godbolt's second session; no geometry changed):**
  - **`d_hiz` has no tap inside the region.** Its metal (x 17631-17651, drawn in `dpad`) was
    followed from D0's contact (y 7382) to the cross-under (y 18148): no corner, and one
    wide stretch only, y 17080-17090, the known west branch south of the region. See
    "A look along `d_hiz`".
  - **Ambiguity 9 (AMB-021) read again**, side by side with two buried boxes and a real pad
    on the same metal: it compares as a buried-contact box. Still assumed "no contact",
    still not provable from these photos. See Ambiguity 9.

Not traced: the latches of bits 4-7 (west of this region, see "Where bits 4-7 go"),
D7's input line south of y 17000, `d6_out_n` and `d7_out_n`. See "Not done".

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
| Input chain, D1-D5 | same cell at (1,1365) (1,2732) (2,4098) (2,5465) (2,6223) | placed; findcell on the clean shot scores 0.81-0.83, each overlay checked at 1.25x. The four-gate core is the same in all six; the wiring left of x 17290 differs per copy: the input lines are drawn for all six (run 4) and the capacitor taps for all six (chain 0 in the first session, chains 1-5 in run 6) |
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
| Capacitor rectangles of chains 1-5 | b (not strapped): 16990-17058 x 10030-10250; 16980-17090 x 11135-11270; 16953-17060 x 12066-12198; 17097-17212 x 14090-14215; 16846-16950 x 15215-15345. c (strapped): 16968-17045 x 10400-10615; 16975-17090 x 11575-11705; 16950-17060 x 12825-12965; 16885-16995 x 13825-13955; 17125-17235 x 14820-14950 | drawn (run 6), with the taps' polys, pads and straps |
| No latch follows chains 4-7 | - | chain 5 starts 758 px below chain 4, chain 6 679 px below chain 5, chain 7 630 px below chain 6 |
| Logic above D0 | 17200-17700 x 5250-5900 | `r9c`'s five compare units. Their east halves (the loads, x 17500-17670) traced here in run 4: cell `dbus_r9l`, master = unit 1 (y 5384-5478), copies at (0,130) (0,260) (0,390), unit 0 mirrored about y 5370. Nothing else is there: field between the units, and no structure east of the rail up to x 17700 |

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
south along x 16819 to y 15800, then west, and on south along x 16774 (not ending at about (16772,15800), where the follower stops on `d5_out_n`'s buried contact: `dlat`, 2026-11-17). On the run south
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
| Input | pad (17254,15695); metal south along x 17254 to y 15890, east to x 17298, south to the pad (17297,16662); poly east along y 16661-16677 under both rails and the `d_hiz` metal, north along x 17662-17678 (colour run y 16510-16676 in the metal shot), east along y 16509-16526 under `dpad`'s rail to the pad (17838,16519), which is on the metal that comes down from D6's protection node (`in6.png`, `in67.png`). **Joined: `d6_in` is pin D6's net** (`@alias d6 d6_in`) | pad (17254,16325); metal south to the pad (17253,16715); poly east along y 16705-16722 to under the VCC rail, then south under the rail's west half (x 17531-17548) past y 17000 (`in7.png`): drawn to the region's edge. Believed D7's (the only pad left); not joined |
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
The eight tapped pads of `dbus_le` on its run down x 16819 are at y 14046, 14264,
14436, 14654, 14913, 15131, 15390, 15608 (measured by `dlat`): four pairs 215-220 apart, which is the distance
between a latch's two `dbus_le` bands (218 in `dbus_lat`), and each of the four lines
arrives about 45 px outside one pair (above the first pair, below the other three), where
band E of the latch would be. A survey view at 0.42x (`s_wide.png`) shows four latch-like
units there at about y 13950-14300, 14400-14700, 14900-15200 and 15400-15700.

### The inverter at the foot of the column, and the thin metal (`d0_out_n`)

Traced (run 3; `g9.png`, `g9b.png` at 3-3.3x, overlay `ov9.png`):

    d0_out_n = NOT dbus_do0_in

- Pull-down under the end of the VSS rail (the rail ends at y 16552): gate band
  y 16444-16463, from the region's west edge (16950,16453) under the metals to x 17418;
  source the VSS land north of it, which is chain 7's stage-1 land (one diffusion under
  the rail from y 16335 to the band: `railprof.py`), with a second contact at (17372,16414);
  output node south of it, x 17354-17403, y 16463-16497.
- The node runs east in a neck 14 px tall (y 16476-16490) through the gap to a diffusion strip under the thin metal
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

What `dbus_do0_in` is: the data that the chip puts on D0, in true sense (the pad is NOT
`d0_out_n`). Its poly (y 16444-16463) starts on a pad (16993,16451), box 16977-17012 x
16435-16468, with a bright contact centre in the metal shot; the stripped shot has no edge
at x 16960 on that y, so nothing goes on west (run 3 drew the poly to the region's edge:
wrong, corrected in run 4). A metal x 16983-17002 leaves the pad south, turns west at
y 16702-16722 (a plain corner, no pad near it: `do0_pad.png`, 4x) and leaves the region at
(16950,16712). `tools/follow.py` takes it on west to x 16795 and south to (16797,17434),
with contact candidates at y 17259, 17295, 17324: outside this region, not looked at.

### `d1_out_n`: D1's output data line (traced 2026-11-17, run 4; wiring only)

One net, in this order:

1. `dpad`'s strip 4 of D1's cell (west end 17800, y 9201-9227) runs on west as a poly
   y 9219-9240 under the trunk (`d1o_top.png`: one orange shape with the cell's block);
2. south at x 17635-17657, directly under the `d_hiz` metal, 390 px. No contact: the clean
   shot under the metal is salmon to y 9606 and field pink from y 9612 (colours along
   x 17647), so the poly ends in the corner;
3. west along y 9589-9609, chain 1's "line 2", under the VCC rail, the thin metal, the VSS
   rail and D1's input jumper;
4. a step down of 22 px at x 17225-17243 to y 9612-9631. One poly: the clean shot at 6x
   shows the Z (`d1o_jog.png`). The chip-2 cuts alone were ambiguous here (at x 17270 they
   show three edges, the middle one being the top of D1's input pad);
5. a pad (17120,9620) and a metal x 17113-17132 south from it for 6,140 px
   (`tools/follow.py`: one piece). Its seven contact candidates were looked at in the
   metal and clean shots at 3x (`d1o_cand_metal.png`, `d1o_cand_acid1b.png`): at y 11021
   nothing; at y 12314-12384 chain 3's line 2 passes under (the clean shot is covered by
   residue there; no ring or pad in the metal shot); at y 14165 and y 14849-14911 the plain
   diffusion rectangles of chains 4 and 5 pass under it (tan, no specks, no ring). No tap;
6. a step west at y 15751-15770 to x 17026-17046 (`d1o_jogm.png`, both chips, 4x; the
   metal that turns the same way 25 px north-west of it is a separate line);
7. a pad (17034,16343) and a poly west along y 16334-16355, which passes under a vertical
   metal x 16940-16960 and leaves the region at x 16950.

Extraction (full): the net is `d1_out_n`, gate of D1's pad cell (`d1_pu` =
NOR(`d1_out_n`, `d_hiz`)). Its driver is not in this region.


### `d2_out_n`..`d5_out_n`: the output data lines of D2-D5 (traced 2026-11-17, run 5; wiring only)

Each is one net with the parts of D1's line. The poly of the pad cell's strip 4 comes west
out of the cell (a block at x 17790-17812, 15 px lower than the strip as `dpad` draws it,
the same in every cell) under `dpad`'s trunk and the `d_hiz` metal; for D3-D5 it then runs
north along the channel (x 17592-17614, in the 48 px gap between the VCC rail and the
`d_hiz` metal) to the height of the chain's "line 2"; line 2 runs west under the VCC rail,
the thin metal, the VSS rail and the vertical metals of the wiring field to a pad; a metal
runs south from the pad, turns west and south again, and ends on a pad from which a poly
leaves west.

| Pin | Out of the cell (y) | Channel run | Line 2 (y) | Pad in the field | Metal: x, turn (y), x | End pad | Poly west (y) |
|---|---|---|---|---|---|---|---|
| D2 | 10954-10976, no channel run: line 2 itself | - | 10954-10976 to x 17184; connector north x 17184-17199; upper row 10911-10933 | A (17078,10921) | 17080, 15718, 16993 | (16993,16217) | 16203-16225, drawn to x 16950 |
| D3 | 12538-12560 | y 12320-12560 | 12320-12343; corner south at x 17030-17050 | (17037,12376) | 17037, 15674, 16950 | (16950,16087) | 16073-16096 |
| D4 | 14121-14143 | y 13688-14143 | 13688-13710 | (16993,13698) | 16994, 15630, 16906 | (16907,15957) | 15943-15965 |
| D5 | 15726-15748 | y 14446-15748 (1,300 px) | 14446-14468 | (16949,14457) | 16950, 15588, 16862 | (16863,15827) | 15816-15835 |

The four end pads continue the staircase that D1's end pad (17034,16343) starts: 43 px
west and 130 px north per line. D3's lower run and its end pad lie on the region's west
edge (x 16950) and D4's and D5's ends 45 and 90 px outside it; the metals are drawn to
their end pads, with 30 px of the poly that leaves each.

Evidence (survey and commands: `cache/scratch/dbus/survey.md`):

- **Poly runs**: dark edge lines in the chip-2 stripped shot (`tools/dbus_dark.py`), two
  edges at constant position at every cut: D2's line at eleven columns x 17215-17790;
  D3's and D4's line 2 at eight columns each, D5's at nine; the channel runs at 5, 6 and
  13 rows (x 17590-17594 and 17613-17617 every time); the runs into the cells at five
  columns each. A cut along the centre of a run shows only the ghost edges of the metals
  above it (the stripped shots have a line beside every metal), so that cut cannot show
  continuity by itself; the views do.
- **Corners and joins at 2.7-4.5x**: the three top corners in three shots
  (`s5_topcorners.png`: one orange poly round each corner, a field gap of about 20 px to
  the input line's corner above); the four runs into the cells in both stripped shots
  (`s5_botcorners.png`: one shape with the block at the cell's edge); overlays
  `s5_ov_bot.png`, `s5_ov_top.png`, `s5_ov_west.png`, `s5_ov_stairs.png`.
- **D2's west end is two nets** (`s5_d2west.png` 3.6x, `s5_d2west_b.png` 4.5x in chip 1's
  metal shot and the clean shot). Line 2 does not go on to the pad B (17032,10965) that
  lies on its axis: at x 17184-17199 it turns north (a connector 16 px wide in the gap
  between two metals), joins an upper row y 10911-10933 and ends on pad A (17078,10921),
  where the metal starts. Pad B's row (y 10955-10975) comes east only to x 17155 and
  turns south at x 17135-17155. Between them, at y 10965, x 17162-17174, the clean shot is
  field pink under the metal there (199/118/124; the poly either side is salmon,
  215/160/113) and the chip-2 stripped shot is field (144-161/122-145/82-98 against
  155/120/57 on the poly): `tools/px.py row 10965 17126 17204 3`. Pad B carries only a
  dot of metal (like `d0_b`'s cut capacitor contacts): probably one of chain 2's
  capacitor taps. Not drawn.
- **D3's west end**: line 2 turns south at x 17030-17050 onto its pad. The pad 45 px
  north-west of it, (16990,12332), with a poly going south from it, is another net:
  field between them at y 12330, x 17017-17026, in both chip-2 shots (142/126/81 and
  133/131/77; `tools/px.py row 12330 16996 17044 3`). Not drawn.
- **The four metals**: `tools/follow.py` from each pad, one piece each (5,324, 3,780, 2,324
  and 1,432 px); the bright core measured every 300 px in both chips
  (`cache/scratch/dbus/s5_centres.py`): no drift and no step. Strip views of the whole
  length in the metal and clean shots (`s5_strip_m.png`, `s5_strip_c.png`, 1.2x): no pad
  or widening between the ends. The follower's ten contact candidates at 3x in the metal
  and clean shots (`s5_cands.png`): field specks, a residue blob in the clean shot at
  (17079,12374), and four places where a metal passes over the east part of a plain
  diffusion rectangle.
- **No tap on the rectangles** (`s5_rects.png`, 2.6x, metal and clean shot): D2's metal
  passes over the east edge of the rectangles 16977-17090 x 11140-11270 and x 11575-11705,
  D3's over 16955-17060 x 12830-12965, D4's over 16925-17000 x 13820-13965, D5's over the
  east edge of one at about x 16880-16958, y 15220-15345 (its own contact pad near
  (16885,15305); found by the review, `review-9/rect_d5.png`, three shots). Under each
  metal the rectangle is plain tan: no specks, no ring in the metal shot, no pad on the
  metal. Each rectangle has its own contact elsewhere (a dot at (17012,11205); straps
  ending at (17005,11650), (16972,12900), about (16935,13895)). They are the chains'
  capacitors (Not done) and are not drawn.
- **End pads** (`s5_endpads.png`, 3.5x, three shots): the same in all four: the metal
  comes down onto a pad 38 x 42 with a contact (a green hole in the clean shot), and a poly
  21 px tall leaves west and is still there 90 px west of the pad.

Extraction (full): the nets are `d2_out_n`..`d5_out_n`, the gates of the pad cells
(`d#_pu` = NOR(`d#_out_n`, `d_hiz`)); with my labels renamed as a test the extraction
reports each as one net with `dpad`'s. No transistor is added (127 in this file, 3,854 in
all). That chains 2-5 are the buffers of D2-D5 was an assignment by position (Ambiguity
7); these lines agree with it only in that chain k's line 2 belongs to pin k's cell.

### The capacitor taps of chains 1-5 (traced 2026-11-17, run 6; wiring only)

Chain 0's pattern (first session) holds for all six `dbus_in` chains, but the wiring is
drawn afresh in each: the second and third inverters' outputs (`d#_b`, true; `d#_c`,
inverted) each leave the chain west in poly and end on a pad in the wiring field.

- **`d#_b` ends on a pad whose contact carries only a dot of metal**: no metal leaves it
  (both metal shots), exactly as `d0_b`. Near each lies a plain diffusion rectangle with
  its own contact and dot of metal, joined to nothing: `dbus_cap1b`..`dbus_cap5b`. The
  strap that would join the two is absent: a metal option not taken, so `d#_b` carries no
  added capacitor in this chip.
- **`d#_c` ends on a pad from which a metal strap runs to a contact on a second plain
  diffusion rectangle**: that rectangle is on `d#_c` (junction capacitance to the
  substrate, as `d0_c`'s).
- No poly crosses any rectangle (no transistor: the extraction's count is unchanged at
  127), and the long metals of other nets that pass over the rectangles have no contact
  there (run 5's review, and round 1 of run 6 by text maps): `d1_out_n` over chain 4's b
  and chain 5's c rectangle, `d2_out_n` over chain 2's two, `d3_out_n` (x 17030-17042)
  over chain 3's c rectangle, `d4_out_n` (x 16984-16992) over chain 4's c rectangle,
  `d5_out_n` over the east edge of chain 5's b rectangle.

| Chain | `d#_b`: route from the cell (x 17257) | b pad (dot only) | b rectangle, its dot contact | `d#_c`: route | c pad | strap | c rectangle, contact |
|---|---|---|---|---|---|---|---|
| 1 | G2's output y 9885-9910 west to x 17220, north x 17220-17240 (in the gap between the metals x 17197-17217 and `dbus_le`'s x 17243-17262) to y 9750, west y 9740-9760 under four field metals (x 17068-17085, 17112-17130, 17155-17172, 17198-17215) | (17030,9751) | 16990-17058 x 10030-10250, (17014,10138) | G4's gate band (y 10156-10171 here) west to x 17190, south x 17180-17200 to y 10335, west y 10325-10345 | (17031,10336) | metal x 17022-17040 south to y 10596, west | 16968-17045 x 10400-10615, (17008,10595) |
| 2 | G2's output y 11252-11277 west to x 17140, north x 17130-17150 to y 10965, west y 10955-10975 | pad B (17030,10965) | 16980-17090 x 11135-11270, (17010,11205) | leaves at **G3's output** (y 11404-11429): a step (the west run y 11388-11408 ends at x about 17250; only its lower part, y 11410-11429, runs on east into the output band) | (17025,11395) | metal x 17026-17044 south to y 11643, west | 16975-17090 x 11575-11705, (17008,11640) |
| 3 | G2's output y 12620-12640 west under all the field metals to x 16992, north in the open x 16983-17002 | (16992,12331) | 16953-17060 x 12066-12198, (16990,12092) | leaves at **G3's output** (y 12772-12795): north x 17224-17247 to y 12743, west y 12733-12754 | (16992,12741) | metal x 16983-17001 south to y 12893, west | 16950-17060 x 12825-12965, (16972,12893) |
| 4 | leaves the **vertical poly between G2's output and G3's gate** (x 17264-17290) at y 14034-14053, west under `d4_d`'s metal | (17161,14043) | 17097-17212 x 14090-14215, (17180,14150) | G4's gate band y 14248-14269 west to x 17195, diagonally down-left (centre (17178,14275), (17157,14295), (17143,14315)) to y 14345, west y 14335-14355 | (16946,14345), on the region's edge | metal x 16938-16954 **north** 455 px to y 13890, west | 16885-16995 x 13825-13955, (16922,13890) |
| 5 | G2's output y 14748-14768 straight west under everything | (16898,14757), 50 px west of the region's edge | 16846-16950 x 15215-15345, (16881,15301) | G4's gate band y 15006-15027 west 60 px | (17201,15018) | metal x 17192-17210 **north** to y 14886, west | 17125-17235 x 14820-14950, (17178,14885) |

What was measured, and how (scratch: `cache/scratch/dbus/survey.md`, "run 6"; views
`s6_*.png`):

- Every run was classified sample by sample along its centre in the clean shot and the
  chip-2 stripped shot (`cache/scratch/dbus/s6_runs.py`, a 3 px step): poly (salmon under
  metal, dark red-brown in the open, orange in chip 2) at every sample, with no field
  (pink under metal, khaki in the open) inside any run; the only dark samples are the
  bars of the gaps between metals in the clean shot, where chip 2 is orange.
- **Chains 2 and 3: the c tap is not on G3's gate band (`d#_b`), which lies 15-20 px
  from it.** Chain 2: the tap's west run (y 11388-11408) passes directly below the west
  end of G3's gate band (y 11367-11387); `tools/px.py row 11377 17209 17281 3 acid1b` is
  field pink at x 17245-17263 and the band's poly begins at about x 17266, while row
  11416 is salmon from x 17227 to 17269 (the join to G3's output). Chain 3: the tap's
  west run (y 12733-12754) is level with G3's gate band; row 12743 is salmon to x 17224,
  field pink at x 17254-17266 (15 px), and row 12784 is salmon from x 17227 to 17266.
- **Chain 4's b tap joins the cell's vertical poly, not `d4_d`'s pad** 45 px above it:
  `tools/px.py row 14043 17176 17293 3 acid1b,acid,metal` is poly without a break from
  the pad to x 17284 (open, salmon under `d4_d`'s metal, open again), while the
  reference rows 14025 and 14070 are field pink at x 17251-17263 with the vertical's
  west edge at about x 17270; `col 17252 13975 14070` is field from y 13993 to 14032
  (between `d4_d`'s pad and the tap).
- Chain 1's b corner at the cell, at 5.5x in four shots (`s6_ch1b_end.png`): the two
  dark specks in the clean shot at (17232,9870) and (17232,9898) lie in the 26 px gap
  between two metals and have no ring in either metal shot (trap 2, checked in chip 2).
- Chain 4's diagonal: row profiles of the metal shot at y 14275, 14295, 14315, 14330
  place it; nine points along the drawn centre are poly in all three shots.
- The dots: each b pad and each b rectangle's contact has a bright centre in the metal
  shot and no line leaving (views at 1.3-3.2x; chain 1's and chain 5's pads at 3x in
  three shots).

### The loads of R9's compare units (cell `dbus_r9l`), traced 2026-11-17 (run 4)

`r9c` drew, for each RA bit, a pull-down under the rail x 17440-17495 (gate = the pad
driver's input line `ra#_drv_in`, output = `ra#_cmp`, the compare line of R9's comparator)
and left the east half, so that the unit being an inverter was an assumption (AMB-012).
The east half is the load, and nothing else:

- the output band under the rail runs on east as a diffusion strip 20 px wide, widens to
  30 px and passes under a poly block (x 17558-17611, 66 px tall): the load channel,
  W/L 30/53;
- east of the block the strip ends on a land (58 x 64) with a metal contact to the rail
  x 17616-17667;
- west of the block an arm of the strip (x 17532-17552) turns back beside the block to a
  heavy-outlined box (17557-17583, 22 px tall), where a tab of the block comes down onto
  it: the buried contact that ties the load's gate to the output side.

**Traced** (full extraction): `ra#_cmp = NOT ra#_drv_in`, # = 0-4. `tools/unsure.py
--equations` gives bits 0-3 as firm; bit 4's depends on `r9c`'s `?P`, the gate poly of its
unit (`trace/r9c.txt`, the open join `ra4_drv_in_u`). On its way to the comparator each
output also passes `r9c`'s `?B` at the unit's west end (the tie from the output band to the
poly that carries the output away): those are `r9c`'s items. One of them (unit 1, 17380-17410 x
5440-5470) was looked at here at 5x in three shots (`u1_west.png`): a heavy-outlined box
with a lighter centre between the poly from the pad and the diffusion from the band, i.e.
it looks like the buried contact `r9c` assumed. Not measured, the other four not looked at.

**The east rail is VCC** (traced, by metal continuity): `tools/follow.py` from (17632,5600)
north reaches y 4597 and turns east; cuts in both metal shots (`tools/larr_px.py`, along
x 17640 from y 4540 to 5300 and along y 4600 from x 17640 to 17920) show metal all the
way, the dark samples being pits (one at (17640,4656) is dark in chip 2 only). The rail
runs into a horizontal band y 4592-4635, which enters the wide metal x 17890-18190 that
`pads_out` has as `vcc` from y 4810 down (`rail_n.png`, 1.2x). The rail's south end is at
y 5902. That the *other* rail is VSS then also follows from the loads' orientation, which
is what AMB-012 asked for.

How it was measured: dark edge lines in the chip-2 stripped shot along five vertical cuts
(x 17515, 17541, 17568, 17592, 17640) and fourteen rows (`tools/dbus_dark.py`). Units 1-4
repeat at 130 px within 1 px on every edge; unit 0 is unit 1 mirrored about y 5370 within
2 px. At x 17541 the cut shows the strip's outer edge and the arm's end but no line where
the arm leaves the strip, so arm and strip are one layer. In the clean shot the arm is
green (open diffusion) and the land is tan with contact specks. Overlay: `ov_r9l.png`
(2x, metal and chip-2 stripped shot, all five).

Raw `cache/acid.npy` is **not** in the common frame (10 px off here); the aligned array is
`cache/acid_aligned.npy`, which `view.py` and `larr_px.py` use.

### The input lines of D2-D5 (traced 2026-11-17, run 4; wiring only)

Each is one net from the pin's protection node (`dpad`) to the first gate band of its
chain, and each has the parts of D1's line: node metal down to a contact on a poly pad,
poly west under `dpad`'s VSS trunk and the `d_hiz` metal, poly along the channel, "line 1"
west under the VCC rail, the thin metal and the VSS rail, a pad, a metal jumper over
"line 2", a second pad on the chain's first gate.

| Pin | Node contact | West run (y) | Channel run | Line 1 (y) | Pad 1 | Jumper | Pad 2 |
|---|---|---|---|---|---|---|---|
| D2 | (17837,10141) | 10131-10152 | x 17592-17613, down to y 10932 | 10912-10931 | (17295,10920) | straight, x 17285-17303 | (17295,11008), poly down to the band |
| D3 | (17838,11727) | 11714-11736 | x 17592-17614, down to y 12299 | 12278-12298 | (17295,12287) | straight | (17295,12376), poly down to the band |
| D4 | (17838,13329) | 13318-13340 | x 17592-17614, down to y 13666 | 13645-13666 | (17316,13655) | L: west to x 17266, south | (17275,13806), on the band's west end |
| D5 | (17835,14887) | 14878-14899, only to x 17631 | x 17631-17657, **up** to y 14403, directly under the `d_hiz` metal | 14403-14424 | (17316,14412) | L: west to x 17266, south | (17275,14500), poly down and east into the band |

Evidence:

- Every run: dark edge lines across it in the chip-2 stripped shot every 60-120 px, and
  one cut along its centre between the two corners (`tools/dbus_dark.py`): two edges at
  constant x all the way, and no line across the run, so no break and no branch. The
  poly is orange in both chip-2 shots (165/118/58 in the metal shot against 160/135/82
  for field).
- Corners and ends at 3-4x in two or three shots: `d2_top.png`, `d2_bot_acid.png`,
  `d2_bot_a1b.png`, `d2_jmp.png`, `d3_top.png`, `d3_bot.png`, `d4_bot.png`, `d4_jmp.png`,
  `d5_chan.png`, `d5_top.png`, `d5_cor.png`, `d5_west.png`.
- **D5's 480 px under the `d_hiz` metal is not a contact** (trap 13): no pad or ring on
  the metal in either chip, `tools/tla_contacts.py` finds no candidate, and the clean shot
  is salmon (poly under metal) throughout. A dark nick at (17650,14592) is in the edge of
  chip 2's metal only; chip 1 has a speckle 8 px lower; the clean shot is unchanged there
  (`d5_595.png`, 6x). In the clean shot the poly ends at both corners (pink beyond).
- Where a line passes under the rails, the thin metal, the trunk and the `d_hiz` metal,
  `tla_contacts.py` lists the same candidates in all four lines, at the open gaps between
  the metals (x 17344, 17424, 17495, 17594; 17671, 17788), 8 px off the poly: open field,
  not contacts. No ring on any of those metals in the views.
- **D4's jumper over line 2** (17266-17286 x 13690-13710) is dim in chip 2 (137/119/58;
  open poly beside it is 165/110/50, clear metal 215/180/95) and yellow in chip 1
  (191/177/85): metal, thinner over the poly step (trap 19). Read as continuous; if it
  were not, each half would be a metal with one end. D5's jumper is bright over its
  line 2 in both chips.
- A feature that crosses every chain's first gate band at x 17313 (an outline from above
  the band to below it) is the same in chains 1-4 (`g1w_a1b.png`, `g1w_acid.png`). It is
  not part of the input line: it is the west edge of the chain's own diffusion (review
  round 1 of run 4: the first pull-down is wider than drawn; see the Review section).
- Overlays: `ov_tops.png`, `ov_bots.png` (chip-2 stripped shot), `ov_jmps.png` (metal, 3x).

Extraction (full): `d2_a = NOT d2` .. `d5_a = NOT d5`, firm; transistor count unchanged.

What the lines "line 2" are: the `d#_out_n` lines of the same pin (drawn in run 5: see
"`d2_out_n`..`d5_out_n`").

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

The same ports with a definite place, one per line, are in `ports.d/dbus.txt` (run 4);
keep the two in step.

| Name | Layer | Where | Direction | What |
|---|---|---|---|---|
| `d0_in` | metal x 17548-17566 | comes down from the D0 pad cell: poly from a contact near 17818,6578 left along y 6578, down to a contact near 17546,6755, then metal down; turns left at y 8188 (cross-under 17300-17500) | in | D0 pad after its protection structure. Drawn from y 8050 down |
| `d1_in` | poly | from the D1 pad cell's contact at 17822,8400 (drawn up to x 17835) | in | D1 pad after its protection structure |
| `d2_in`..`d5_in` | metal, then poly | `dpad`'s node metals at (17836,10025), (17836,11674), (17836,13279), (17836,14862) | in | pins D2-D5 after their protection (aliases of `d2`..`d5`); drawn to the chains (run 4) |
| `dN_d` | poly, then metal | G4 output, 17290-17345 x 8825-8847 + offset | out of the chain | pad level, buffered and delayed; into the latch (D0-D3) |
| `d4_d`, `d5_d`, `d6_d`, `d7_d` | poly | leave west at (16950,14000), (16950,14696), (16950,15173), (16950,15650) | out | the buffered pins D4-D7, to the latch column at x 16480-16800 (believed) |
| `d6_in` | poly | pad (17838,16519) under the metal from D6's protection node | in | pin D6 (alias of `d6`) |
| `d7_in` | poly under the VCC rail, x 17531-17548 | leaves south at (17540,17000) | in | believed pin D7; not followed to the pad |
| `d7_c` | metal | leaves west at (16950,16758) | - | chain 7's c tap, probably to a capacitor; not followed |
| `dbus_do0_in` | metal | leaves west at (16950,16712), from the pad (16993,16451) at the west end of the poly y 16444-16463 | in | input of the inverter that drives `d0_out_n` |
| `d1_out_n` | poly y 16334-16355 | leaves west at (16950,16344) | in | D1's output data line; drawn from here to D1's pad cell |
| `d0_out_n` | metal x 17591-17609 | joins `dpad`'s metal at (17600,7565) | out | D0's output data line (the thin metal) |
| `d2_out_n` | poly y 16203-16225 | leaves west at (16950,16214); joins `dpad`'s strip 4 of D2's cell at (17801-17812, 10954-10962) | in | D2's output data line; drawn from here to D2's pad cell |
| `d3_out_n` | poly y 16073-16096 | drawn to (16905,16085), 30 px west of its end pad (16950,16087); goes on west | in | D3's output data line |
| `d4_out_n` | poly y 15943-15965 | drawn to (16860,15954), west of its end pad (16907,15957); goes on west | in | D4's output data line |
| `d5_out_n` | poly y 15816-15835 | drawn to (16817,15826), west of its end pad (16863,15827); goes on west | in | D5's output data line |
| `db_b0`..`db_b3` | poly | pads under `dbl`'s contacts (17207,9467), (17077,10832), (17165,12200), (17208,13563) | out | the internal data bus bits, driven here by `dbus_drv` |
| `dbus_le` | metal | leaves west at (16950,13614) | believed in | latch enable; see above for where it goes |
| P_y of D0 | now `d0_out_n` (row above): drawn | | | |
| P_y of D1 | now `d1_out_n` (row above): drawn | | | |
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
9. **The box under the `d6_in` metal at (17310,16488)** (`?D`): **open, undecided.** The
   output node of the foot inverter has a west tab that ends in a heavy-outlined box,
   17294-17328 x 16474-16502, whose west third lies under the metal x 17290-17306 that
   carries `d6_in` south. The metal is dim over y 16476-16512 in both chips (R at most
   160 in chip 2 and 141 in chip 1 over 36 px, with full-width dark bars at y 16481 and
   16508; 200-226 on the plain line), and `follow.py` reads an end from both sides.
   My first argument for "no contact" was wrong: the metal has **no** bright core there,
   and where the same metal passes chain 7's buried-contact boxes (y 15975, 16130) its west
   half stays at R 177-222 (review round 1 of run 3; my own profiles agree).
   - For a contact (which would tie pin D6 to `d0_out_n`): the dimming, deeper than over
     any buried box on the same line.
   - Against a contact: no pad (about 3 px of bulge on the west side), no bright centre,
     no specks; in the clean shot the box looks like chain 7's buried-contact boxes.
   - Against a break in the metal: the clean shot stays pink (field under metal) at
     x 17288-17292 all the way through.
   - Unexplained: the box's interior is black in the chip-2 stripped shot (G 16-57,
     against 72-110 for buried boxes and 110-168 for contact holes) and very dark in both
     metal shots (48/40/15, 56/46/21), pale in the clean shot (160/142/114).
   **Working assumption: no contact**, because a tie between an input pin and the output
   of a static gate makes no sense and because there is no pad. The trace joins nothing
   there: the tab and box are a `?D`, and `d6_in`'s metal is drawn through. To settle: the
   same spot at 6-8x in a better photo, or the logic (if D6 read back as D0's data ever
   shows in behaviour, the contact is real).
   **Run 7 (2026-11-17 16:40 -0600), a second reader, same conclusion.** The spot at 6x in
   all four shots (`c2_amb21.png`) and at 3x beside three references on the same metal
   (`c2_amb21_cmp.png`: `mosaic.py 17255 16445 100 90 --offsets "0,0 0,-513 0,-358 0,174"`,
   layers `acid1b`, `metal1`, `metal`, `acid`): chain 7's two buried boxes (y 15975, 16130)
   and the real pad (17297,16662).
   - The real pad has all three marks of a contact: the metal widened to a pad about 40 px
     across with a bright centre in both metal shots, a dark pit in the pale pad in the
     clean shot, a pitted box in the chip-2 stripped shot. The box here has none of them.
   - In the clean shot the box here is the same object as chain 7's two: a heavy outline
     with a clean pale square centre, no pit. It sits 6-8 px further west than they do
     relative to the metal (box x 17302-17317 inside its outline, against 17308-17323), so
     the metal lies over its west third where at chain 7 it passes beside the box. That
     is trap 22's pass-over (a thin metal dark for 35-80 px over a buried box, both metal
     shots, no pad, no hole), deeper here because the metal is on the box, not beside it.
   - `tools/textmap.py 17270 16455 17340 16525 3 --acid`: over y 16482-16509 the metal's
     columns read 2-6 in chip 2 and 2-8 in chip 1 (C-D on the plain line), no bright
     centre; the clean map has no `g` hole inside the box (0-6); the chip-2 stripped map
     is `-`/0-4 inside (dark), as the notes above say.
   Not explained, as before: why the interior is darker in the chip-2 stripped shot than
   chain 7's boxes. A dead-end buried box is not new in this column (Ambiguity 2).
   **AMB-021 stays as it is: assumed no contact, nothing drawn but the `?D`.**
10. **Load sizes in `dbus_in2`.** Stages 2 and 3: under the thin metal the load gate lies
   on the strip: 2 px rows of the clean shot there are poly over field y 15314-15322, an
   edge, the channel colour (R 220-242, R-G 70-106) y 15330-15349, 4 px of tan, an edge,
   and the bar y 15362-15365 (review round 1 of run 3; I had read a 12 px bare strip
   from a 5 px map). So the gate covers the strip from x 17428 to 17527: drawn so, W/L
   20/99, like `dbus_in`'s 27/96. Under the open part of the gate the metal shot has the
   strip's edges at y 15336 and 15360, 6-8 px lower: not reconciled (a size only). The
   stage-4/1 load (35/48) and the foot inverter's (32/53) are read at 2.8-3.3x. No
   connection depends on these.
11. **Chain 7 is D7's** by elimination only: its input line is drawn to y 17000 and goes on
   south under the VCC rail. Chains 2-5 are still assigned by position (Ambiguity 7).
12. **The tie box of the foot inverter's load** (17462-17502, 16418-16452) was read at 3.3x
   in the two stripped shots only; drawn as an ordinary buried contact because every load
   in the column is tied that way.
13. `dbus_in`'s pull-down widths (60 for G1/G4, 56 for G2/G3) were drawn in the first
   session from the land under the rail. In `dbus_in2` the diffusion reaches west of the
   rail (W 107 and 64). **G1 and G4: settled in run 4** (review round 1): the land has a
   tab west of the rail to x 17316 above the band and the channel runs on under the band
   to the output band, so W is about 94 (drawn). G2 and G3 (land drawn from x 17322) were
   not looked at again.

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

### Run 3 (2026-11-17)

**Round 1, full review of what run 3 added or changed** (2026-11-17 18:26 +0000, a fresh
agent; 22 images and its scripts' output in `cache/scratch/dbus/review-5/`). Told to
suspect: a contact between the `d6_in` metal and the box at the foot inverter's west tab;
whether the L arm has diffusion on both sides and whether the strip is one piece with the
VSS land; the second copy of `dbus_in2`; every poly under or beside other nets' metals
(`d7_d`'s vertical, chain 7's taps, `d4_d`..`d6_d` under the vertical metals); the `d6_in`
route; pull-down widths and the stage 2/3 load; the foot inverter's tie box, band end and
land; the thin metal from y 13700 to 16420; the capacitor contact and the b taps' ends. It
read the junctions at 3.4-7x in two to four shots with 3 px colour maps and profiles, ran
`railprof.py`, `follow.py` and `cellcheck.py` (second copy 0.93-0.94), and profiled the
thin metal from y 8125 to 16540 in both chips.

- Finding 1, **undecided, recorded** (Ambiguity 9): whether the `d6_in` metal has a
  contact to the box is not settled, and my evidence against one was wrong (no bright core;
  the box reaches under the metal to x 17292-17294). I checked: the same metal over chain
  7's boxes keeps R 177-222 on its west half, 121-168 at this box. The `?D` now reaches
  x 17294; the ambiguity is rewritten with both sides. No connection is drawn there.
- Finding 2, **confirmed and fixed**: a VSS contact at (17372,16414) on the land between
  chain 7's stage 1 and the foot inverter was not drawn (ring in both metal shots: my
  map). Same net.
- Finding 3, sizes, **confirmed and fixed**: the stage 2/3 load gate covers the strip
  under the thin metal (2 px rows: channel colour y 15330-15349), so L is about 100, not
  39 (Ambiguity 10); the foot inverter's gate band ends at x 17418; its node's neck through
  the gap is 14 px tall (tan y 16478-16488 between two edges, and the node does not reach
  east of x 17403 beside the band); `d6_in`'s poly under the VCC rail is at y 16663-16676,
  5 px south of where it was drawn.
- Found correct: diffusion on both sides of the L arm in all eight chains and the strip
  continuous through the gap (chain 1 and both `dbus_in2` copies on views, chain 0 by
  profile); the second copy of `dbus_in2` and the stage links in both; `d4_d`..`d7_d` and
  chain 7's taps continuous, each on one track, no pad on any metal they cross; `d7_d`'s
  vertical ends at y 15640 and 15834; `d4_b` not joined to `d4_d` (field x 17228-17264);
  the `d6_in` route and `d7_in`; the capacitor contact; both b-tap metals end on nothing;
  every new pad measures as a contact hole; the foot inverter's land, strip and VCC
  contact; the thin metal (no dim stretch over 23 px, no widening, no pad on `d0_in` at
  the top hop); both rail ends.
- Could not check: `dbus_in2`'s pull-down widths to better than about 10 px; poly
  continuity through the foot tie box's outline; whether the VCC rail joins the wide metal
  at y 16975.

**Round 2, fix check** (2026-11-17, a fresh agent, given only the diff since `b956b15` and
the six changes; ten images in `cache/scratch/dbus/review-6/`). It compared the extraction
before and after (70 nets, 122 transistors both; only the four `dbus_in2` loads differ,
W/L 40/39 to 20/99; no net joined or split) and read each change at 4x or more in two to
four shots with column profiles: the VSS contact (ring in both metal shots, pitted box in
the chip-2 stripped shot, specks in the clean shot); the load gates on their strips in
both copies (channel y 15330-15350 and 15483-15501, the gate clear of the node, the bar
and the tie box); the band end (salmon to x 17416); the neck (tan y 16477-16489, one piece
from the node to the strip and pad, 13 px of field between it and the band); the `d6_in`
poly (y 16662-16677 in three shots, meets its pad, 28 px clear of `d7_in`); the `?D` on
its box, touching only the west tab and lying under the `d6_in` metal.

Round 2: no findings.

Its one remark, not an error: the stage 2/3 load strip measures about 24 tall where it is
drawn 20 (a size; Ambiguity 10).

### Run 4 (2026-11-17)

**Round 1, full review of what run 4 added or changed** (reported 2026-11-17 19:31 +0000, a
fresh Fable 5.2 agent; 37 images in `cache/scratch/dbus/review-7/`). Told to suspect: the
east rail's join to VCC (read at 1.2x); whether the tab-on-arm box is a buried contact and
arm and strip one diffusion; each output strip's join to `r9c`'s band and its clearance
from the gate poly end; the cell copies; D4's jumper over line 2; a hidden contact under
the `d_hiz` metal on D5's poly and its corners; each node metal's reach to its pad; each
second pad's join to the gate band; branches or breaks along the channel runs;
`d1_out_n`'s join to the pad cell's strip, its corner, the Z-step (trap 10), the long
metal's candidate taps, a bridge at the metal's step, the end pad; whether anything goes on
west of `dbus_do0_in`'s pad. It read unit 1 at 4x in three shots and unit 0 at 4x, profiled
the rail-band-wide-metal joins in both metal shots, ran `cellcheck.py` on the loads (units
2-4: 0.96-0.98, unit 0: 0.92), viewed the tops of all four input lines at 3.6-4.6x and the
channel runs of D2-D4 end to end, the pads and jumpers at 3.6-4x, and every junction of
`d1_out_n` and `dbus_do0_in`.

No finding changes a connection. Two points:

- Finding 1, **confirmed and fixed (a size)**: the outline that crosses each chain's first
  gate band at x 17313 is diffusion, not wiring: G1's land reaches west of the rail. My
  check on the master (chain 0): a closed outline 17312-17350 x 8305-8328 above the band,
  green inside in the clean shot (105-130/131-152/85 against khaki 135-161/131-153/80
  outside: open diffusion), pinker than field in both chip-2 shots; its west edge is a
  dark line at x 17309-17316 at y 8316 and across the band at y 8340 (`g1_land.png`, 5x,
  three shots; `tools/dbus_dark.py`). Below the band the output band was already drawn
  from x 17305. G4 has the same tab (outline 17312-17350 x 8762-8781, green inside:
  `g4_land.png`). Drawn: both channels now run from x 17316, W 94 (was 60), in the cell,
  so in all six chains. No net changes (2176 nets, 3796 transistors before and after).
- Finding 2, **confirmed, notes corrected**: the notes said `ra#_cmp = NOT ra#_drv_in` for
  all five and named only `r9c`'s `?B`; `ra4_cmp`'s equation depends on `r9c`'s `?P` gate
  poly. The Status and the loads' section now say so (`operation.md` already did).
- Found correct: the rail to the band to the wide metal (both metal shots, 1.8x and
  profiles; dark samples alternate between the chips: pits); strip, arm, box, load and
  land of the units; the strip one diffusion with `r9c`'s band and 8 px clear of the gate
  poly end; D2's channel poly 6-9 px clear of a `d_hiz` contact pad at (17640,10855) (three
  shots); D4's jumper continuous (chip 2's stripped shot shows the metal's ghost over
  line 2); D4's pad 2 joined to the band and clear of the `d4_a` poly below; D5's poly
  salmon from y 14416 to 14896 with field beyond both corners, the nick dark in both chips
  (y 14587-14597 and 14596-14602) but both stripped shots uniform and no pad: no contact;
  `d1_out_n`'s join at x 17800, both corners, the Z-step one poly (poly colour down
  x 17230-17236 from y 9593 to 9628 in chip 2, field beyond both stubs in the clean shot),
  no tap at any candidate (chain 4's rectangle has its own contact at (17188,14155)), the
  metal's step clear of its neighbour, the end pad, no contact under the metal
  x 16940-16960; field west of `dbus_do0_in`'s pad in all shots.
- Not checked: the 6,140 px metal between its candidates (`follow.py` only); line 1 under
  the rails in chip 2 (fringes; read in the clean shot); `r9c`'s `?B` boxes; the VCC metal
  north of y 4520.

**Round 2: no findings.**

Round 2 was a fix check (reported 2026-11-17 19:38 +0000, a fresh Fable 5.2
agent; images in `cache/scratch/dbus/review-8/`) of the two rectangles added to `dbus_in`
since commit 0e53e80. It measured the outline at all twelve sites (G1 and G4, chains 0-5)
in all four shots (west edge x 17311-17316, top 19-23 px above the band; the drawn edges
sit 3-6 px inside, so W could be about 98), found the inside pinker than field in both
chip-2 shots at every site (in the clean shot green only in chain 0, mauve in chains 1-4),
the west edge crossing the gate band as a dark line at every site, the tab one colour with
the land up to the rail's edge, a 12-15 px field gap to the input line's poly in chains
1-3 and the pads of chains 4 and 5 ending at x 17298 and 17293, and the extraction
unchanged but for twelve widths. Viewed at 4x or more: the master's G1 and G4, G1 of
chains 1, 4 and 5, G4 of chain 3. Could not check directly: the tab's join to the land
under the rail's edge line (inferred from the absence of a second edge).

### Run 5 (2026-11-17)

**Round 1, full review of what run 5 added** (reported 2026-11-17 20:27 +0000, a fresh
Fable 5.2 agent; 29 images in `cache/scratch/dbus/review-9/`; the piece: `d2_out_n`..
`d5_out_n`, commit 0288b78). Told to suspect: D2's west end (the 16 px connector, and
whether line 2 is separate from pad B's row under the metal); D3's corner against the pad
10 px away; the joins into the four pad cells (an 8 px overlap with a strip `dpad` draws
15 px higher); the three top corners and the input lines' corners above them; a break,
branch or hidden contact along the channel runs, their clearance from the `d_hiz` pads and
the VCC lands, D5's input poly alongside; a contact wherever a metal crosses a line 2
(the earlier lines' metals cross the later lines' line 2); taps, track changes and
contacts onto the rectangles along the four long metals; bridges between the five nested
L's of the staircase and runs that share an x; whether each of the eight pads has a real
contact and each end pad's poly leaves from that pad.

What it checked: D2's west end at 4.5x in four shots with a column profile down the
connector (continuous poly from the upper row to line 2 in both chip-2 shots and the
clean shot; pad B's row ends at x about 17155; x 17162-17174 field pink under the bus
metal, which has no edge bars at line 2's height); D3's west end at 4.5x in four shots
(10-15 px of field to the neighbouring pad); the four joins into the cells at 4.5x in
both stripped shots (one stepped poly shape with strip 4 in each); the three top corners
with column profiles (one poly round each, about 9 px of field between dark edges to the
input line's corner); the channel runs by a row-by-row scan and views (poly unbroken at
every row in both chip-2 shots, no branch either way; 16-18 px between the interiors of
poly and VCC land at 6x; the `d_hiz` pads 8-10 px clear; D5's input poly 24 px away);
line 2 under the rails, the trunk and the field metals at 2x with text maps and
`railprof.py` (poly over field everywhere, no hole or ring at any crossing, including the
earlier lines' metals and the input jumpers); the long metals with `follow.py` and a scan
of both metal shots (one piece each, no widening, no ring; four dark patches are in one
chip only), the rectangles under them; the staircase corners at 4.2x in both metal shots
(five separate L's, no bridge; runs that share an x are separated by another line's
horizontal); the eight pads (real contacts; each end pad's poly leaves west from that
pad, clear of the second staircase's pads); the full extraction and `tools/unsure.py`
(none of these nets listed).

It reported no finding, and two remarks that change nothing in the trace:

- D5's metal also passes over the east edge of a plain diffusion rectangle (about
  y 15215-15350, its own contact pad near (16885,15305)) without contact; the notes named
  rectangles only under the other three. Checked (`review-9/rect_d5.png`: plain tan under
  the metal in the clean shot, no ring in either metal shot). Added to the notes.
- D2's line 2 is drawn at y 10954-10976 and `railprof.py` puts it at 10957-10977: within
  the 3 px tolerance; not changed.

Not checked by it: the long metals at 4x between their pads, corners and rectangles
(measured, not viewed); the crossing of D2's metal over D3's line 2 at (17080,12331) in
the clean shot (residue; both metal shots show no ring or pad); line 2 under the rails
above 2x.

Round 1: no findings.

### Run 6 (2026-11-17)

**Round 1, full review of what run 6 added** (reported 2026-11-17 21:14 +0000, a fresh Fable 5.2 agent; 33
images in `cache/scratch/dbus/review-10/`; the piece: the capacitor taps of chains 1-5,
commit ddebb74). Told to suspect: the three places where a tap passes within 20 px of
another net of its own chain (chain 2's c tap under G3's gate band, chain 3's c corner
beside it, chain 4's b tap against the vertical poly and `d4_d`'s pad), decided by the
tracer from clean-shot profiles; which cell poly each tap really joins; a thin metal
leaving a b pad or a b rectangle's dot; whether each c strap lands on its pad and on a
contact, and what else touches it (chain 4's 455 px strap beside `d4_out_n`'s and
`d5_out_n`'s metals, and `d5_out_n`'s pad on the same x); hidden contacts where a tap runs
under another net's metal; the gap specks read as artefacts; pad B and chain 3's b pad
against run 5's `d2_out_n` and `d3_out_n`; chain 4's diagonal (first drawn 15 px off); a
poly crossing a rectangle; anything undrawn in the field.

What it checked, at 4-5x in four shots at each junction, with profiles: chain 2's c tap
against G3's band (field pink at x 17254-17262 on every row y 11366-11404, chip 1's metal
bright with no edge bar over y 11356-11401; the join to G3's output continuous at x 17230,
y 11394-11427 in both chip-2 shots); chain 3's c corner (six rows y 12730-12756 pink at
x 17254-17266, both metal shots bright over y 12722-12770); chain 4's b tap (salmon to
x 17266 on row 14043, pink on rows 14022 and 14066; separate from `d4_d`'s pad; no contact
under `d4_d`'s metal); the diagonal (joins both horizontals, touches nothing else); chain
4's strap (ends at its pad; bare ground in both metal shots down to `d5_out_n`'s pad); all
b pads and b-rectangle dots (mosaics at 3x in both metal shots and ring samples at radius
36-38: nothing leaves); the five c straps (each lands on a pad and on a rectangle contact;
chain 1's is dim over its rectangle and `follow.py` misses it, but both stripped shots
show it continuous); every run on its centre line (continuous poly, no pad or contact hole
under any crossing metal; the gap specks absent in chip 2); pad B against `d2_out_n` (25 px
of field) and chain 3's b pad against `d3_out_n`'s corner (about 10 px of bare ground); the
ten rectangles (no poly crosses any; the metals over them have no contact); the field
x 16950-17290 for anything undrawn (nothing; a green patch at (17180-17260, 11190-11260)
is a stain on the clean shot only); the extraction (127 transistors, every piece on the
claimed net) and `tools/unsure.py` (none of these nets).

It reported four findings, all geometry or comment only; each checked by me and confirmed:

1. Chain 2's c step: the trace drew poly at (17246-17262, 11395-11410), which is field.
   Mine: `tools/px.py col 17256 11392 11432 3 acid1b` is pink to y 11407, edge at
   11410-11413, salmon 11416-11425; `row 11402 17240 17262` is salmon at x 17240, an edge
   at 17243-17246 and pink from 17255. Fixed: the step is now two rectangles
   (17225-17250 x 11395-11429 and 17245-17262 x 11410-11429). No connection changes: the
   drawn gap to G3's band was 8 px before and is 23 px now. Geometry only.
2. Chain 1's b west run crosses four field metals, not five (trace comment and the table
   above corrected). Comment only.
3. `dbus_cap5b`'s west edge is at x about 16846, not 16838 (mine: `px.py row 15250 16826
   16866 3`: outline at x 16841-16850, green from 16853). Fixed. Geometry only.
4. The notes' list of metals over rectangles left out `d3_out_n` over chain 3's c
   rectangle and `d4_out_n` over chain 4's (no contact at either). Notes corrected.

Proof that the fixes change no connection (commit before the fixes: ddebb74):

    tools/t.sh dbus sameconn.py ddebb74             -> connections identical
    .venv/bin/python tools/sameconn.py ddebb74      -> connections identical

Not checked by it: the chip-2 stripped shot is fringed at the chain 2 and 3 gaps and at
the metal edge where chain 4's b tap meets the vertical poly, so those three rest on the
clean shot and the two metal shots; chain 2's b north run above y 11150, chain 1's c west
run and chain 2's two west runs were checked by survey and profile, not at 4x.

Round 1: no findings that change a connection.

### Run 7: review of its two readings

Run 7 changed no geometry, and was first merged (93cdc12) **without** a review, on the
tracer's reasoning that there was nothing drawn to check. That was wrong: its two readings
each decide a connection (whether `d_hiz` has a tap; whether pin D6 is tied to `d0_out_n`).
The user was told by a side note, and the review was run afterwards:

**Round 1, full review of run 7's two readings** (reported 2026-11-17 17:19 -0600, a fresh
Fable 5.2 agent, 31 tool uses, 8 images in `cache/scratch/dbus/review-11/`; told not to read
the tracer's two sections or AMB-021). Told to suspect: a contact with little or no pad
missed by the follower, a thin branch, the two long pass-overs; and, for Ambiguity 9, that
"no contact" was concluded from what makes sense electrically and not from the photos.

- **`d_hiz`, y 7374-17000: supported.** A 1 px scan of the whole length in `metal`,
  `metal1` and `acid1b` finds a green hole between two dark bars at exactly six places
  (y 7381-96, 9116-29, 10854-65, 12439-47, 14018-31, 15624-36): the cell contacts. The
  metal's own edge lines (x 17628-17636 and 17650-17658) are never interrupted in either
  chip: no branch. Every other dark feature present in both chips is a pair of bars
  22-25 px apart, a poly crossing (ten sampled: protected salmon poly, no green, no
  widening). Over y 9225-9605 and 14408-14895 the poly under the centre is uniform (red
  minus green 34-69, never green) and neither metal shot has a ring. Rejected one by one:
  (17640,9480), a debris ring on chip 1 only; y 11141-11194, a soft interference patch on
  chip 1; (17643,8713), a 10 px speck over plain field; (17647,14590), a 12 px notch in the
  east edge with intact poly beneath; y 16754 and 16827, fringes.
- **Ambiguity 9 (AMB-021): neither a contact nor a break, "about 85-90 % sure".** Not a
  break: the metal's west edge line at x 17285 is continuous through y 16480-16512 in both
  metal shots, the west flank at x 17290 is as bright there as above and below, and the
  protected/open boundary in the clean shot at x 17287 is unbroken. Not a contact: no
  widening (the real pad at (17297,16662) widens about 8 px west), no centred bright spot,
  no green pitted hole (the real contact reads 143/140/83 under a bright centre). What it
  is: two full-width dark bars (y 16479-85 and 16506-12, the box's top and bottom outlines)
  with a half-bright flank between, the same structure as the pass-overs at y 15958-91 and
  16110-43 (6.5x, four shots).
- Geometry only, not changed (weak evidence, the reviewer's words): under the metal at
  x 17288-17292, y 16485-16505, the clean shot's blue is 83-98 against 120-127 on field,
  which suggests the box or tab reaches west to about x 17287; the `?D` starts at 17294.
  No connection depends on it.

Not checked by it: the poly crossings' own routing, the contacts' targets inside the pad
cells, anything south of y 17000.

Round 1: no findings.

## A look along `d_hiz` (run 7, 2026-11-17 16:40 -0600)

The line is `dpad`'s (metal x 17631-17651, `M 17641,7374 y18155`). Looked at here because
its driver was listed under this region.

- `tools/t.sh dbus follow.py 17641 7420 S`: no corner; "wide from 17638,17080 to
  17638,17090" (the west branch `dpad`'s review found, south of this region); end at
  (17644,18148), the cross-under. `... N`: ends at (17642,7382), D0's contact.
- Its twenty contact candidates, each accounted for:

| y | What it is | How |
|---|---|---|
| 9139, 10873, 12456, 14039, 15645 (and 17249) | the cells' own contacts (17637,7385 + cell offset; the follower reports each about 18 px low) | `textmap.py 17612 9092 17675 9160 3 --acid`: ring, bright centre, `g` hole, poly pad `F` in the stripped map |
| 9290-9573 (eight) | `d1_out_n`'s poly directly under the metal, y 9219-9609 | text maps y 9275-9400, 9440-9590: metal C-E at one width throughout, clean map 5-9 (poly), no `g` hole |
| 14500, 14798 | `d5_out_n`'s poly under the metal, y 14403-14899 | the same, y 14480-14522 and 14776-14820 |
| 11168 | nothing: a soft green patch in the clean shot (no outline, shading off over 50 px), plain field in the chip-2 stripped shot, metal unwidened in both chips; the follower's candidate is a dark blob on the metal's west edge | `c2_hiz11168.png`, 5x, four shots |
| 16754, 16827 | nothing: the same kind of soft green patch at the metal's east edge (y 16817-16840), dark blobs on the west edge at y 16745, 16805, 16840; no pad, no poly under the line in the stripped shot | `c2_hiz16800.png`, 5x, four shots |

So between y 7374 and 17000 `d_hiz` touches nothing but the six pad cells (D0-D5; D6's and
D7's are south of the region). What this does not cover: a tap in poly or diffusion that
leaves one of the cell contacts' pads inside a pad cell (that is `dpad`'s cell, reviewed
there).

## Not done

- **The latches and bus inverters of bits 4-7**: not in this region. `d4_d`..`d7_d` leave
  west at x 16950 (y 14000, 14696, 15173, 15650) towards the gate column x 16480-16800,
  y 13950-15700, where `dbus_le` has its eight taps (see "Where bits 4-7 go"). That column
  is `areg`'s right-hand column down to y 14700 and `bd2`'s below; `db_b4`..`db_b7` are
  expected to be driven there. First thing to try: `findcell` with `dbus_lat`
  (17230 8885 17590 9370) and `dbus_drv` restricted to 16450,13900:16850,15750.
- `dbus_do0_in` west of (16950,16712) (metal; see its section) and `d1_out_n` west of
  (16950,16344) (poly): both drivers are outside the region.
- `d6_out_n`, `d7_out_n`: not drawn, and not in this region: both leave their pad cells
  south of y 17000 (`busc`'s area). Seen in run 5 (`s5_d67cell.png`, 2.6x, both stripped
  shots): D6's poly comes west out of its cell along y 17331-17353 to a pad (17600,17340)
  with a contact, and a metal runs SOUTH from the pad to (17600,18084)
  (`tools/follow.py 17601 17370 S`; nothing goes north); D7's comes west along
  y 18936-18958 and turns north up the channel at x 17592-17612 (edges at y 18400-18900).
  So these two are driven from below the column, not from the staircase.
  `d2_out_n`..`d5_out_n` are drawn to their end pads (run 5); the poly
  that leaves each end pad west (y 16214, 16085, 15954, 15826) goes into the column west
  of x 16950 (`bd2`'s right-hand column), where their drivers must be, with D1's
  (16950,16344) and `dbus_do0_in`'s metal.
- `d7_in` south of y 17000 to D7's protection; `d7_c`'s metal west of x 16950.
- Seen in run 5 and not looked at: a second staircase of pads with polys west lies
  between the end pads of `d2_out_n`..`d5_out_n` (about (16862,15990), (16905,16125),
  (16950,16255)), on or west of the region's edge.
- `d_hiz`'s driver: not in this region (run 7: no tap between y 7374 and 17000). The lead
  is the metal that leaves it west at (17630,17085), in `busc`'s area.
- `dbus_le` west of x 16950: drawn to the region's edge only; its eight taps and its
  south-west end (16772,15800).
- Ambiguity 9 (the box beside `d6_in`'s metal; AMB-021): read twice now (runs 3 and 7),
  assumed no contact. Nothing more can be had from these photos; it is settled by a better
  photo or by behaviour, not by another look.

**Inside the region nothing else is left** (run 7): every other item above leaves it, to
`dlat`, `busc` or `bd2` (rest).

## Note (coordinator, from the handoffs of 2026-11-17/18)

- The "open-drain ... with a pull-up" reading of the lines "P_x" / "P_y" in the early part of
  these notes is superseded by `dpad`: the pad cell has only gates on them; they are `d_hiz` and
  `d#_out_n`.
- `dbus_le`'s eight taps and the latches of bits 4-7 are traced in `dlat` (`notes/blocks/dlat.md`).

## Corrections (coordinator, from the handoffs of `cdp3`, `cdp4` runs 4-15, `eof` runs 36-51 and `regs` runs 5-6, 2026-11-21)

- `dbus_do0_in`'s metal ("west at y 16702-16722 out of the region (follow.py: on west to x 16795, then south
  to (16797,17434))", here and in `trace/dbus.txt`'s comment): drawn by `cdp4` run 7: it is the read bus's
  column 7 (`cdp3_n_c7`), from the read multiplexers of R12-R17; `@alias cdp3_n_c7 dbus_do0_in`, so `d0_out_n`
  = NOT `cdp3_n_c7`.
- "The driver is west of the column" for `d1_out_n`..`d5_out_n`: the drivers are the five inverters of
  `cdp4`'s cell `cdp4_ro` (run 8); each row is drawn on from this block's end to its buried contact.
- Not done, "`d6_out_n`, `d7_out_n`: not drawn, and not in this region": both are drawn (`cdp4` runs 9-11):
  `d6_out_n` from an inverter of the read bus's column 1 into D6's pad cell; `d7_out_n` (`regs`' inverter of
  column 0) ends as a poly column x 17595-17613 from a pad (17558,18146) south to y 18957 and a row east into
  the pad cell.
- `d7_c` ("metal west of x 16950"): the reviewer of `cdp4` run 7 followed it west along y 16758 to a corner
  near (16838,16758) and south on x ~16840 to about y 17306; undrawn (a lead in `busc`'s row).
