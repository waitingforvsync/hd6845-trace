# bd2: bus control logic right of the register select gates

Region x 15850-17000, y 14700-17100. Trace: `trace/bd2.txt` (`@requires sel`, `areg`, `bd3`).
Extracts with 0 errors, 0 warnings. Seven runs; this file was rewritten by the second, the third
(2026-11-27: the column from group 4 down to `dbus_le`'s driver) has its own section, "Run 3", below, the
fourth (2026-11-28: the gate group east of its rail) the section "Run 4", the fifth (2026-11-28: the
inverter of `wr_addr_sel` south of the group, which corrects what gates the upper gate) the section "Run 5",
the sixth (2026-11-28: a re-read of runs 1-2's wiring between the bundle and the gate group, found as
drawn) the section "Run 6", and the seventh (2026-11-28: a re-read of groups 2 and 3, the two NORs of R/W, RS
and CS; connections as drawn, widths and two cells' places corrected, group 3's VCC contact found) the section
"Run 7".

## Status

- **Traced and extracted**
  - G1, the driver of `wr_stb_n`, and G2, the driver of `ar_load` (first run).
  - The **strobe latch** behind G1: rows 1-3 of the left gate column and the inverter
    G4 west of the rail. A D latch, open while `e_b` is high.
  - **Where R/W, CS and RS act**: groups 2 and 3 of the left column, two three-input
    NORs of `rw_d`, `cs_d` and RS (one takes `rs_d`, the other its inverse). Group 2's
    output is the latch's data input, group 3's gates the address register strobe.
  - The wiring of `e_b`, `wr_data_lat`, `ar_load_n`, `wr_data_sel_n`, `wr_data_sel`, `wr_addr_sel`, `bd2_rs_n`
    and the top ends of `rw_d`, `rs_d`, `cs_d` in the bundle.
- **The gate group right of the bundle is a cross-coupled pair as drawn** (run 4, 2026-11-28): both loads and a
  third pull-down of the upper gate are traced; `bd2_x` is the upper node's own load poly, and the lower
  node's load poly comes back as the gate of the upper gate's third pull-down. Both ties are uncertain items.
- **The pair is a D latch of `wr_addr_sel`, open while E is high** (run 5, 2026-11-28): south of the group a
  third unit, an inverter, makes `wr_addr_sel_n` = NOT `wr_addr_sel`, and its output is what gates the upper
  gate's stack (band G_a), by the pad (16274,15873) and the thin metal x 16270-16284. Runs 1-4 had `wr_data_sel`
  there: run 2 drew the band of row 3 on east to that pad, across 26 px of field. So `ar_load` is `wr_addr_sel`
  as it was while E was last high, the same circuit as the strobe latch beside it. Marked: three uncertain ties.
- **The wiring between the bundle and the gate group is re-read and reviewed** (run 6, 2026-11-28): the break
  in the metal x 16169 (G1's gate is `wr_data_lat`, not `e_b`), `e_b`'s feeds of bands G_b and G_d, G2's gate
  on the metal from the pad (16205,15690), `wr_addr_sel`'s feed of G_e, and every crossing without a contact.
  Found as runs 1-2 drew it; nothing redrawn.
- **Groups 2 and 3 are re-read** (run 7, 2026-11-28): both NORs as run 2 drew them, group 3 now from its own
  photographs and not from group 2's pattern; its VCC contact is drawn. All three pull-downs of each are
  64-70 wide (run 2 had 28 and 52): the stack runs west of the rail to x 15990 and, at the R/W input, east of
  it to x 16096. Each output's boxed cell is drawn where its box is (30 px east of run 2's).
- **Three results of the first run are corrected**: `ar_load` is not `NOT e_b` (G2's
  gate is a separate net, `ar_load_n`); row 1 has a third pull-down and a load; the metal
  at x 16210 is two wires (a second break, at y 15968-15988).
- **Not traced**: the column below y 17400, the `?B` cells of runs 1-2. See Not done.
  (The rest of group 4 and the column to y 17110 are run 3's.)
- Images used: about 44 (first run) + 46 (second). What worked in the second run was
  **numbers instead of pictures**: character maps of small areas by colour class
  (`tools/bd2_umap.py` for what lies under metal in the clean shot, `tools/bd2_cmap.py`
  for poly against plain areas in the open, `tools/bd2_patch.py` / `bd2_prof.py` for
  single patches and profiles), and **contact footprints**: under a metal the clean shot
  is olive green (G >= R, B about 100) where the metal had a contact, salmon where it
  only crosses a poly, pink over field. At 5-6x the pictures of this area are too
  blurred to decide a junction; the maps decided them, and the pictures were then used
  to check the trace by overlay.

## Verdict on the disagreement with bd3: the input of the `wr_stb_n` driver is NOT `e_b`

bd3 reads the metal at x 16169 as one line from G1's gate down to `e_b`; the first run
here read a break at y 15443-15470. **The break is real: `trace/bd3.txt`'s `bd3_stb`
section is wrong in its last two `M` lines and its `N M 16167,15500 e_b` label** (the
inverter itself, its load, output route and the gap to the pad at 16255,15085 are
right and duplicate G1 here). Evidence, all from numbers (`tools/bd2_prof.py`):

1. Colour and grain of both metal shots down x 16162-16177 (`bd2_prof.py col 16169
   15405 15500 7 3`): metal (R about 180-200, G/R 0.8-0.9, grain 21-39) down to y 15411;
   the ring of contact 16167,15432 (dark 15414-15426, bright centre 15429-15438, dark
   15441-15453); then y 15455-15464 is **orange and smooth in both chips**: chip 2
   165/114/58, G/R 0.69, grain 11.5; chip 1 150/97/51, G/R 0.65, grain 6.7. Bare poly
   beside it measures G/R 0.58-0.75; twelve other 8 px pieces of the same trunk between
   dark crossings (y 16080-17325) measure R 158-212, G/R 0.78-0.90 (one shot at most
   down to 0.68, never both), grain 13-30. Then a dark line y 15465-15471, then metal.
2. That dark line at y 15465-15471 runs straight across from x 16136 to 16184
   (`bd2_prof.py map 16100 15396 16235 15504`): it is the top edge of the metal that
   arrives from contact 16122,15388 and turns down. Nothing underneath has an edge there:
   in the clean shot the poly under the line is uniform (221-231/158-179/118-133) from
   y 15442 to 15500.
3. Chip 2's stripped shot has a very dark bar across that poly at y 15451-15467
   (R 51-74; everywhere else from y 15380 to 15720 along x 16169 it is 96 or more,
   including under the three tap contacts further down): the uncovered piece of poly.
4. The thin dark line at x 16154-16160 between the horizontal metal y 15470-15490 and
   the lower trunk (`bd2_prof.py row 15479 16104 16192 4 2`) is 6 px wide and sits on
   the left edge of the poly underneath (red outline at x 16158-16163 in the clean
   shot): an edge printing through, not a gap. So the metal from 16122,15388 does join
   the lower trunk.
5. Gate polys followed at 3x (view k3): G1's band y 15078-15100 -> pad/contact
   16255,15086 -> metal x 16255, y 15222 west, x 16168 down -> ends on contact
   16167,15432 (poly "strip 1" goes on south from the pad).

So `wr_stb_n = NOT wr_data_lat`, and `wr_data_lat` is the Q of the latch below.

## Equations (the answer in one place)

    wr_stb_n = NOT wr_data_lat                                   G1          traced
    wr_data_lat    = NOT( wr_data_lat_n OR (e_b AND wr_data_sel_n) )             row 1       traced
    wr_data_lat_n    = NOT( wr_data_lat OR (e_b AND wr_data_sel) )             rows 2-3    traced
    wr_data_sel_n     = NOT wr_data_sel                                    G4          traced (the tie of its output to the bar is inferred)
    wr_data_sel     = NOR( rw_d, bd2_rs_n, cs_d )                  group 2     traced
    bd2_rs_n  = NOT rs_d                                     group 4     traced (load: run 3)
    bd2_rw_n  = NOT rw_d                                     run 3       traced
    dbus_le   = NOR( cs_d, bd2_e_n )                         run 3       traced
    bd2_e_n   = NOT e_b                                      run 3       traced
    rd_data_e = NOR( bd2_e_n, cs_d, bd2_rw_n, bd2_rs_n )     run 3       traced
    ar_load = NOT ar_load_n                                 G2          traced
    ar_load_n  = NOT( wr_data_e_n OR (e_b AND wr_addr_sel) )     gate group  traced (run 4); marked: `bd2_x` is `wr_data_e_n` through an uncertain tie; tie to G2 inferred
    wr_addr_sel  = NOR( rw_d, rs_d, cs_d )                      group 3     traced (by the pattern of group 2 west of the rail)
    wr_addr_sel_n = NOT wr_addr_sel                             run 5       traced; marked: its way out to G_a is through an uncertain tie
    wr_data_e_n    = NOT( ar_load_n OR (wr_addr_sel_n AND e_b) )        gate group  traced (runs 4, 5); marked: the third pull-down's gate is `ar_load_n` through an uncertain tie, G_a is `wr_addr_sel_n` through another

Read as logic (believed; `rw_d`, `rs_d`, `cs_d` have the sense of their pins):

- `wr_data_sel` = write AND chip selected AND RS high: a write to the data register.
- `wr_addr_sel` = write AND chip selected AND RS low: a write to the address register.
- Rows 1-3 with G4 are a transparent latch: while `e_b` is high `wr_data_lat = wr_data_sel`
  (and `wr_data_lat_n = NOT wr_data_sel`); while `e_b` is low both hold. Hence

      wr_stb_n = NOT wr_data_sel   while E is high;  held at its last value while E is low
      wr_rN    = rselN AND wr_data_sel(latched)      (the NOR in sel)

  - **Set** (strobes on, `wr_data_lat` high): `e_b AND wr_data_sel` pulls `wr_data_lat_n` low.
  - **Cleared** (strobes off): `e_b AND wr_data_sel_n`, i.e. `e_b AND NOT wr_data_sel`, pulls `wr_data_lat` low.
  - **Held**: the cross-coupling `wr_data_lat` -> row 2's gate, `wr_data_lat_n` -> row 1's third
    pull-down, whenever `e_b` is low.
- `ar_load = wr_data_e_n OR (e_b AND wr_addr_sel)` with `wr_data_e_n = NOT(ar_load_n OR (wr_addr_sel_n AND e_b))`
  (runs 4 and 5): the two gates and the inverter are a second transparent latch, the mirror of rows 1-3 with
  G4: while `e_b` is high `ar_load = wr_addr_sel`; while it is low both nodes hold. So the address register's
  load strobe goes high when E rises in a write to the address register and stays high until E next rises
  with `wr_addr_sel` low (any other cycle, or a deselected one), exactly as the write strobe does for the data
  registers. (Run 4's reading, a set/reset pair cleared only by a data write, came from run 2's wrong join of
  G_a to `wr_data_sel`: "Run 5".)

Nothing in the traced part turns the write strobe off when E falls: as traced, the
selected register's strobe stays on from E rising in a data write until E next rises
with `wr_data_sel` low. Whether that is the whole story depends on what `sel` does with it
and on the data path; it is what the silicon here says.

## Inventory

| What | Where | State |
|---|---|---|
| VCC rail | x 15795-15890, whole height (shared with `sel`'s right-hand column); band y 14745-14805 to areg's inverter rail x 16142-16194 | drawn |
| VCC land under that rail | x 15850-15898, continuous from y 15682 down at least to y 16120 | drawn in pieces where a load uses it |
| Ground rail of the left column | x 16008-16058, y 14908 to about 17050; joined by the band y 14908-14960 to `areg_rail_r` | drawn; lower end not looked at |
| `areg_rail_r` | x 16401-16450 above y 14908; jogs to x 16355-16405 (y 14908-15330), then to x 16312-16362 (y 15400 on), the ground rail of the gate group, which **ends at y 15922** | drawn to y 15330 and y 15400-15850; the jog between is the first run's observation, not drawn |
| G1, driver of `wr_stb_n` | 15900-16272 x 15030-15160 | traced |
| G2, driver of `ar_load` | 15895-16272 x 15225-15360 | traced |
| Row 1 (latch, Q side) | 15900-16150 x 15500-15715 | traced |
| Rows 2-3 (latch, Q bar side) | 15900-16150 x 15655-15915 | traced |
| G4 (`wr_data_sel_n = NOT wr_data_sel`) | 15900-16125 x 15857-15985 | traced |
| Gate group right of the bundle | x 16240-16500, y 15400-15760 | traced (pull-downs run 2; loads, third pull-down and ties run 4, the ties uncertain; G_a's gate corrected by run 5) |
| Inverter `wr_addr_sel_n` = NOT `wr_addr_sel` | x 16286-16545, y 15770-15900 | traced (run 5): pull-down beside the ground land, load on the VCC rail x 16491-16538, output row west under the rail's end to the pad (16274,15873) |
| Group 2 (`wr_data_sel`, NOR of R/W, NOT RS, CS) | 15890-16400 x 15985-16210 | traced (run 2; re-read by run 7) |
| Group 3 (`wr_addr_sel`, NOR of R/W, RS, CS) | 15890-16400 x 16245-16470 | traced (run 2, west part by the pattern of group 2; read from its own photographs by run 7) |
| Group 4, first gate (`bd2_rs_n` = NOT `rs_d`) | 15850-16360 x 16529-16680 | traced (load: run 3) |
| `bd2_rw_n` = NOT `rw_d` | 15850-16312 x 16654-16765 | traced (run 3) |
| `dbus_le` = NOR(`cs_d`, `bd2_e_n`) | 15850-16400 x 16760-16965 | traced (run 3) |
| `bd2_e_n` = NOT `e_b` | 15850-16244 x 16962-17110 | traced (run 3) |
| `rd_data_e` = NOR(`bd2_e_n`, `cs_d`, `bd2_rw_n`, `bd2_rs_n`) | 15850-16400 x 17108-17400, and its route to (17112,17950) | traced (run 3, piece `rdg`) |
| Left column below y 17400 | under the rail (a land from y 17435 on) | not traced |
| Right-hand column | x 16480-16800, y 14700-16450; routing east and south of it | not looked at; the metal ending at about (16772,15800) and running north along x 16818 with eight tapped pads is `dbus_le`, the data input latches' enable (`dbus`, 2026-11-17); the column is the bits 4-7 latch column, package `dlat` |

## Logic

### G1: `wr_stb_n` driver (traced, first run)

One inverter, `wr_stb_n = NOT wr_data_lat`.

- Load: VCC land under the rail (contacts 15862,15048 and 15862,15108), strip
  y 15075-15145 east under the poly block 15903-15942 x 15030-15160 (W/L about 70/39).
  The block's top end is tied to the output by a buried contact at 15912-15948 x 15028-15062.
- Pull-down: poly band y 15078-15100 from x 15978 to the contact 16255,15086, with a leg
  down at x 15978-16000 to y 15160. Output above the band and left of the leg, ground
  below the band and right of the leg (contact 16032,15122 on the rail). W about 280.
- Output: strip y 15050-15078, buried contact 16185-16218 x 15030-15058 at its east
  end, poly north at x 16256 under the ground band to contact 16255,14868, metal west along
  y 14868 to contact 15928,14868, poly west along y 14825 into `sel` (15850,14825).
- The poly from the north ends on that buried contact; it does not reach the contact
  at 16255,15086 (10 px of bare field between them at y 15058-15068).
- Input: contact 16255,15086, metal down x 16255 to y 15222, west, down x 16158-16178
  (the "upper trunk") to its **end** at contact 16167,15432. From that pad the poly
  "strip 1" runs down x 16157-16180, diagonally, down x 16208-16218 to y 15612 and steps
  right into a block (16224-16248 x 15600-15660). From the block's foot a band goes
  west: y 15643-15657 under the `ar_load_n` metal, slanting down under the `e_b` trunk to
  y 15664-15680, to the buried contact at the east end of row 1's output strip.
  Checked in the second run: salmon unbroken under both metals, the block orange in
  the open (`bd2_umap.py 16140 15580 16260 15700`, `bd2_cmap.py 16180 15590 16262 15700`).

### G2: `ar_load` driver (traced; its input corrected in the second run)

One inverter, `ar_load = NOT ar_load_n`.

- Load: VCC land (contact 15863,15300), strip y 15258-15332 under the block
  15898-15940 x 15232-15335 (W/L about 75/42); the block has an arm along y 15228-15250 to
  a buried contact at 15963-15995 x 15243-15272 on the output.
- Pull-down: band y 15290-15312, x 15978-16195, ending in the pad of contact 16210,15300.
  Output above (y 15262-15290), ground below (contact 16040,15338). W about 128.
- Output: buried contact 16098-16132 x 15243-15277, poly east along y 15257 to contact
  16255,15258, metal east and up x 16297 to contact 16296,15003, poly under the ground
  band, contact 16296,14822, metal x 16299 up into `areg`.
- **Input.** From the pad of contact 16210,15300 only a metal leaves: x 16200-16222 down
  to its end at contact 16205,15690. The first run had a poly ("strip 2") under that
  metal all the way from the pad and so joined G2's gate to `e_b`. It is not there:
  - under the metal the clean shot is pink field from y 15313 to 15355, between the
    olive contact footprint (y 15298-15310) and the poly that starts at y 15358
    (`larr_px.py - col 16211 15286 15400 3`; `bd2_umap.py 16100 15286 16246 15500`);
  - that poly is the branch from the `e_b` pad 16122,15388, which arrives along
    y 15358-15378 and turns down as strip 2 (x 16208-16218) to the gate band G_b;
  - where the metal crosses it there is no contact: metal bright and unbroken from
    y 15364 to 15400 in both shots, salmon unbroken under it, no olive patch.
- From the pad of contact 16205,15690 a poly bar (x 16228-16250, y 15688-15702, over
  field: the plain areas above and below it measure as field) runs east to the boxed
  cell at the west end of `ar_load_n`'s diffusion (16266-16296 x 15684-15704).

(Run 4, 2026-11-28: `bd2_x` is `wr_data_e_n` as drawn; see "Run 4".)
So the address register's load strobe is `bd2_x OR (e_b AND wr_addr_sel)`, with
`wr_addr_sel = NOR(rw_d, rs_d, cs_d)` (group 3): E high in a write to the address
register, not simply NOT E. **This changes what areg.md should assume.**

### The strobe latch (traced, second run)

Left gate column, rows 1-3, plus G4. All three AND-OR-invert / inverter gates have the
same build: pull-downs in a diffusion column under the ground rail, the output running
west under the rail's edge to a load whose strip comes from the VCC land under a poly
block. The block, a thin bar above it and a bar or pad below it are **one poly** (the
6-9 px dark lines between them are the strip's two edges under the poly; two polys could
not be that close), and that poly is tied to the output at a boxed cell.

**Row 1: `wr_data_lat = NOT( wr_data_lat_n OR (e_b AND wr_data_sel_n) )`**

- Ground land 16028-16075 x 15505-15545, contact 16047,15522. Column x 16018-16100.
- Upper band y 15555-15578, gate `wr_data_sel_n` (pad and contact 16114,15560). Lower band
  y 15603-15625, gate `e_b` (east to the tap 16167,15605). Output strip y 15628-15657.
- Third pull-down, gate `wr_data_lat_n`: the ground land has an arm west along y 15537-15552
  (tan and unbroken under the rail from x 16010 to the land: no edge between), which
  turns down at x 15942-15978, passes under the bar of the L-shaped poly
  (15908-15992 x 15558-15587) and returns east along y 15638-15657 into the output
  strip (tan and unbroken under the rail from x 16011 to 16059 at y 15640-15652).
  Evidence that this loop is diffusion and the pocket inside it (15978-16020 x
  15590-15637) field: in chip 2's stripped shot R-G is +13 to +21 on the loop and -5 in
  the pocket (field reference +1); the same order in both metal shots
  (`bd2_patch.py`, patches T4-T8 in the second run). The loop's left edge (x 15937)
  crosses the bar, and the bar is brighter over the loop than over field in three shots.
  This is the first run's reading (E); reading (A), the bar as the load, is out.
- Load: the output diffusion continues south (x 15962-15981 to y 15708); the strip from
  the VCC land joins it along y 15682-15704 under the poly block 15902-15952. That poly
  (y 15664-15735) runs on east as the band y 15712-15747, the gate of row 2. A finger of
  the band (15986-16008 x 15658-15712) ends in a boxed cell with a light centre
  (15988-16006 x 15660-15680) on the output diffusion: the tie, and the cross-coupling
  of `wr_data_lat` into row 2.
- Output to G1: buried contact at the strip's east end (box 16102-16118 x 15644-15654,
  bar x 16130-16134 down into the band): see G1.

**Rows 2-3: `wr_data_lat_n = NOT( wr_data_lat OR (e_b AND wr_data_sel) )`**

- Ground land with contact 16047,15700; band y 15722-15747 (gate `wr_data_lat`); output
  y 15750-15808; band y 15811-15831 (gate `e_b`, from the tap 16166,15822, rounded west
  end at x 16020); node y 15837-15853; band y 15857-15877 (gate `wr_data_sel`); ground land
  with contact 16047,15898. Read under the rail with `bd2_umap.py 15996 15660 16070 15912`.
- The output has an arm west under the rail (y 15778-15798) to the load: strip from the
  VCC land under the block 15902-15952 x 15778-15797; that poly (y 15757-15847) ends
  in the pad of contact 15925,15825, from which the metal x 15912-15935 goes up to the
  pad of the L-shaped poly of row 1 (contact 15925,15625). The pad's poly wraps a boxed
  cell (15956-15996 x 15800-15842) on the output's arm: the tie. Either way round (the
  cell as tie of the load, or the pad as part of the load gate) this metal is `wr_data_lat_n`.

**G4: `wr_data_sel_n = NOT wr_data_sel`**

- The west end of the `wr_data_sel` band widens and turns down under the rail's edge
  (x 16004-16022, salmon from y 15858 to 15917 with one dark edge line at y 15882-15890)
  and crosses a strip that runs from row 3's ground land (x 16026 on) west to an output
  land 15958-15996 x 15890-15920.
- Load: block 15900-15956 x 15890-15909 over the strip from the VCC land, one poly with
  the bars above (y 15868-15884) and below (y 15918-15929); the lower bar turns down
  (x 15933-15952) to y 15975.
- The output diffusion goes south from the land (x 15966-15980) and ends in a boxed
  cell at 15966-15978 x 15956-15970, between the load gate's down-turn and the west end
  (x 15988) of a poly bar y 15955-15973. That bar runs east under the rail (field above
  and below it: a wire) to the pad of contact 16105,15962.
- `wr_data_sel_n`: thin metal from that contact up x 16093-16112 to the pad of row 1's upper
  band (contact 16114,15560). About 13 px wide where it crosses rows 1 and 3, 16 px
  between y 15668 and 15768 and below y 15900.
- **Inferred, not seen**: that the cell ties both the load gate and the bar to the
  output (drawn as one poly through a `?B`). The bar has no other driver and row 1's
  upper band no other source, and the alternative driver would short the latch
  (Ambiguity 2).

### Gate group right of the bundle (pull-downs traced, second run)

**Corrected by run 5** (its section below): band G_a is not gated by `wr_data_sel`. The pad (16274,15872) is
not on row 3's lower band (26 px of field between them); it is the west end of the output row of the inverter
of `wr_addr_sel`. Where this section writes `wr_data_sel` for G_a, its pad and the thin metal x 16270-16284,
read `bd2_w15872` = `wr_addr_sel_n`. The rest stands.

Diffusion column x 16312-16366 under the ground rail x 16312-16362
(`bd2_umap.py 16250 15404 16384 15850`).

- Upper gate, `wr_data_e_n = NOT( wr_data_sel AND e_b )`: ground land y 15422-15461 (contact
  16338,15432); band G_a y 15466-15488, gate `wr_data_sel` (pad and contact 16260,15473 at its
  west end); node; band G_b y 15509-15531, gate `e_b` (strip 2); `wr_data_e_n` y 15533-15565,
  widening east to x 16374. Boxed cell at its west end (16246-16296 x 15552-15572, three
  plain cells) with no poly leaving it. Load and destination not traced (east).
- Lower gate, `ar_load_n = NOT( bd2_x OR (e_b AND wr_addr_sel) )` (`bd2_x` is `wr_data_e_n` as drawn: run 4): ground land y 15596-15635
  (contact 16327,15612); band y 15638-15656, gate `bd2_x`, arriving from the east; the
  node `ar_load_n` y 15663-15720 (arm east at y 15687-15708 to x 16374, arm west to the
  boxed cell); band G_d y 15726-15744, gate `e_b` (tap 16167,15735); node; band G_e
  y 15770-15788, gate `wr_addr_sel` (contact 16207,15778, from group 3; the band's poly
  also extends east of the column to about x 16372); ground land y 15795-15831 (contact
  16330,15812). Load not traced.
- `wr_data_sel` here: metal pad on contact 16260,15473 and thin metal x 16270-16284 down to
  contact 16274,15872 on the east end of row 3's lower band (its driver is group 2,
  below). It crosses both boxed cells.
  No contact there: the cell centres are cream in the clean shot (193-201/170-183/126-138)
  like diffusion under metal, not olive green like the footprints of the known contacts
  of these metals (154-165/167-183/96-103), although in the metal shots the centres are
  as bright as contact centres.
- East of the rail (seen in one 3x view, not traced): a poly bar 16395-16483 x
  15475-15498 in line with G_a, turning down at x 16465-16483 to y 15558; contact
  16450,15539 with a thin metal x 16444-16459 going down to contact 16450,15740; the
  wide vertical metal x 16489-16547 with a long contact strip.

### Groups 2, 3 and 4 of the left column: where R/W, CS and RS act (traced, second run)

**Group 2: `wr_data_sel = NOR( rw_d, bd2_rs_n, cs_d )`** (y 15985-16210)

- Under the rail (`bd2_umap.py 15996 15876 16072 16070` and `15996 16056 16112 16236`):
  ground land y 15987-16026 (contact 16044,16008); band R y 16032-16047; output
  y 16056-16083; band S y 16090-16108; ground land y 16113-16155 (contact 16025,16132);
  band T y 16160-16178; output again y 16185-16203.
- The two output pieces are **one node**. The upper has an arm west under the rail
  (y 16064-16080) to the load (block 15898-15938 x 16068-16096 over the strip from the VCC
  land, one poly with the bars above and below, tie at the boxed cell 15915-15940 x
  16121-16141). From the load's east end a diffusion wire (x 15944-15964) goes down to
  y 16208 and back east under the rail into the lower piece. The wire is pink in the
  metal shots, green in the clean shot, and measures R-G +24/+25 in chip 2's stripped
  shot against +3 for field and -3 for the field pocket it encloses.
- Band R: east under the `e_b` trunk and the `wr_data_sel` metal (salmon, no contact) to the
  contact 16297,16040 = **top end of `rw_d`** (olive footprint).
- Band S (x 15970-16076): its east end is joined by a poly link (x 16064-16073,
  y 16093-16120, orange in all three shots) to a band y 16120-16136 that runs east to the
  contact 16252,16128 (olive footprint) on the metal x 16255 = `bd2_rs_n`.
- Band T: from x 15970 east across the whole bundle (salmon under `e_b`, `bd2_rs_n`,
  `rw_d` and `wr_addr_sel`: no contact) to the contact 16386,16171 = **top end of `cs_d`**.
- Output: boxed cell 16075-16102 x 16058-16081 at the east end of the upper output
  piece; poly band y 16078-16092 east under the `e_b` trunk to the contact 16210,16086 at
  the lower end of the `wr_data_sel` metal.

**The metal at x 16210 is two wires** (measured like the first break):

- y 15972-15981, x 16204-16219: chip 2 144/96/47 (G/R 0.67), chip 1 141/90/45 (0.63), in
  both orange like the proven gap of the x 16169 metal (155/107/55, 143/94/50), against
  195-204/164-169 and 182-189/142-145 on the metal either side; chip 2's stripped shot
  has a dark bar at y 15968-15980 (R 55-118, elsewhere 127-205)
  (`bd2_prof.py stat 16204,15972:16219,15981 ...`).
- **Upper piece = `wr_addr_sel`**: from contact 16207,15778 (band G_e) down to y 15967, east
  as a bar y 15947-15967 (the 6 px dark line at x 16221-16226 between them lies on the
  edge of the poly underneath: an edge printing through) to x 16349, down x 16329-16349
  (pink field under it all the way, salmon where it crosses band T) to the contact
  16343,16344 on group 3's output band. The first run took this vertical for the gate
  group's ground rail running on; that rail ends at y 15922 (view q1).
- **Lower piece = `wr_data_sel`**: contact 16211,15997 (olive) down to contact 16210,16086.
  The pad of the upper contact is the foot of a poly that runs up under the upper
  piece (x 16206-16216, salmon and unbroken from y 15982 to 15877) into row 3's lower
  band. So group 2's output reaches the latch (rows 2-3, G4) and, by the thin metal
  x 16277, the gate band G_a.

**Group 3: `wr_addr_sel = NOR( rw_d, rs_d, cs_d )`** (y 16245-16470)

- The same gate 261 px lower: under the rail ground land y 16250-16287, band R'
  y 16293-16308, output y 16317-16347, band S' y 16353-16367, ground land y 16374-16416,
  band T' y 16422-16438, output y 16446-16467 (`bd2_umap.py 15996 16236 16080 16490`);
  west of the rail the character map shows group 2's load, wire and tie cell shifted
  by 261 (`bd2_cmap.py 15892 16296 16012 16476`). Drawn from group 2's shapes; checked
  by one overlay (view ov6).
- Band R' ends on `rw_d`'s tap 16298,16302; band T' on `cs_d`'s tap 16386,16430 (olive
  footprints both). Band S' is linked (x 16064-16073, y 16354-16381) to a band
  y 16381-16397 that ends on the contact 16211,16388, the top end of a metal that goes
  south to the contact 16211,16606 on `rs_d`'s band in group 4.
- Output: boxed cell at the east end of the upper output piece, band y 16339-16353 east
  across the bundle (salmon under `e_b`, `bd2_rs_n`, `rw_d`) to the contact 16343,16344.

**Group 4, first gate: `bd2_rs_n` pulled low by `rs_d`** (y 16545-16680)

- Under the rail: field down to y 16563; land y 16575-16590 (the output); band
  y 16594-16612; ground land y 16620-16677 (contact about 16041,16663); band
  y 16681-16699; land y 16707-16725 (`bd2_umap.py 15996 16476 16080 16730`).
- The band y 16594-16612 runs east across the bundle to the contact 16343,16603 =
  **top end of `rs_d`**, and on the way has the contact 16211,16606 of the metal that
  feeds band S' of group 3. Salmon, no contact, under `e_b`, `bd2_rs_n` and `rw_d`.
- Output: a boxed cell (16090-16130 x 16545-16578) on the north side of the land's east
  end; poly band y 16552-16568 east to the contact 16255,16562 on the `bd2_rs_n` metal
  (view g4z). That metal runs up to band S of group 2 (contact 16252,16128) and on
  south (track scan: to y 17300 at least, not followed).
- Its load, and the band y 16681-16699 that `rw_d` taps (a second inverter), are traced by run 3: no
  other pull-down west of the rail, so `bd2_rs_n` = NOT `rs_d` is no longer a belief.

## Bundle x 16100-16400: what is on each track

| x | Segment | Net |
|---|---|---|
| 16104 | 15560-15962 | `wr_data_sel_n`: contact 16114,15560 (row 1 upper band) to contact 16105,15962 (G4's bar) |
| 16122 | 15384-15490 | `e_b`: contact 16122,15388 down to the corner into the lower trunk |
| 16169 | 15211-15443 | `wr_data_lat` (upper trunk), contact 16167,15432 at its lower end |
| 16169 | 15470-17702 | `e_b` (lower trunk); taps 16167,15605 (row 1), 16167,15735 (G_d), 16166,15822 (row 3), **16166,17037 (run 3: the gate of the inverter `bd2_e_n`; the "scan gap" of run 1)**. No contact where it crosses the bands of groups 2-4 and of run 3's gates (salmon in the clean shot) |
| 16210 | 15296-15690 | `ar_load_n`: contact 16210,15300 (G2's gate) to contact 16205,15690 |
| 16210 | 15771-15967 | `wr_addr_sel`: contact 16207,15778 (band G_e), then east along y 15957 and down x 16339 |
| 16210 | 15990-16096 | `wr_data_sel`: contact 16211,15997 (poly up to row 3's lower band) to contact 16210,16086 (group 2's output) |
| 16210 | 16378-16616 | `rs_d`: contact 16211,16388 (band S' of group 3) to contact 16211,16606 (group 4's band) |
| 16210 | 16723-17222 | `bd2_rw_n` (run 3): from the pad (16208,16733) of the `rw_d` inverter's output south to the pad (16209,17212) of the read gate's band C. Bare from there to y 17290, where `rd_data_e`'s metal starts at its pad (16210,17300) (run 1's scan took the two for one track to y 17745) |
| 16255 | 16118-17348 | `bd2_rs_n`: contact 16252,16128 (band S of group 2), contact 16255,16562 (group 4's output band), south to its end on the pad (16253,17342) of the read gate's band D (run 3) |
| 16255 | 15947-15983 | this is the bar of `wr_addr_sel` crossing the track |
| 16277 | 15466-15872 | `bd2_w15872` (= `wr_addr_sel_n` through its tie; run 5): contact 16260,15473 (G_a) to contact 16274,15873, the pad of the inverter's output row. Runs 1-4 had `wr_data_sel` here: row 3's lower band does not reach that pad |
| 16299 | 16030-17569 | `rw_d`: top end at contact 16297,16040 (group 2); taps 16298,16302 (group 3), 16298,16690 (group 4, not traced) |
| 16339 | 15957-16354 | `wr_addr_sel`: down to contact 16343,16344 (group 3's output band) |
| 16342 | 16593-17515 | `rs_d`: top end at contact 16343,16603 (group 4's band) |
| 16385 | 16161-17569 | `cs_d`: top end at contact 16386,16171 (group 2); tap 16386,16430 (group 3); tap 16384,16821 (run 3: band 1 of `dbus_le`'s NOR); the tap at 17170 per trunks.md not looked at |

## Ports

| Name | Layer | Crosses at | Direction | What |
|---|---|---|---|---|
| `wr_stb_n` | poly | x 15850, y 14825 (west) | driven here | write strobe gate of `sel` (G1 output) |
| `ar_load` | metal | x 16299, y 14700 (top) | driven here | address register load strobe (G2 output) = NOT `ar_load_n` |
| `vcc` | metal | x 15795-15890, y 14700 and y 17100 | supply | rail shared with `sel` |
| `vcc` | metal | x 16142-16194, y 14700 (top) | supply | areg's inverter rail |
| `vss` (`areg_rail_r`) | metal | x 16401-16450, y 14700 (top) | supply | ground |
| `dl7_q_n` | metal | x 16341, y 14700 (top) | unknown | contact 16337,14866, poly down x 16330-16345 to y 15240, then diagonally south-east to the bit-7 latch's output (16466,15389): `dl7_q_n` (`dlat`); `dl6_q_n` likewise from the bit-6 latch |
| `dl6_q_n` | poly | x 16364, y 14700 (top) | unknown | to the right-hand column. Not drawn |
| `e_b` | metal | x 16169, y 17100 (bottom) | from outside | E buffered; lower trunk |
| `rw_d` | metal | x 16298, y 17100 | from outside | per trunks.md; ends at 16297,16040 |
| `rs_d` | metal | x 16342, y 17100 | from outside | per trunks.md; ends at 16343,16603 |
| `cs_d` | metal | x 16385, y 17100 | from outside | per trunks.md; ends at 16386,16171 |
| `dbus_le` | poly | x 16130, y 16865 (inside the region) | driven here (run 3) | the NOR's output cell; `cdp4`'s row leaves it east to the pad (16426,16864) |
| `rd_data_e` | metal | x 17112, y 17950 (far outside the region: the end of its route) | driven here (run 3, piece `rdg`) | the read gate's output; a thin metal goes on east into the block below the data bus column |
| (`bd2_x`, `wr_data_e_n`) | | | | no longer ports (run 4): the band of `bd2_x` is the load poly of `wr_data_e_n` and ends under the strap at x 16482; the node's arm ends on its own load and pull-down |
| ? | metal | x 16016-16026, y 17100 | ? | thin line where the ground rail was; not looked at |
| ? | metal, 49 wide | x 16492-16540, y 17100; x 16505-16540 at y 14700 | supply? | wide vertical of the right-hand column, whole height |
| ? x 6 | metal | x 16580, 16624, 16668, 16711, 16755, 16799 at y 17100 | ? | six lines on a 43.5 px pitch leaving south |
| ? | metal | x 16837 (faint), 17001 at y 17100 | ? | |
| ? | metal | x 16586, 16621, 16732, 16816, 16950, 16992 at y 14720 (top) | ? | lines of the right-hand column continuing into areg's untraced part |
| ? | metal | x 17000 (east), y about 14694, 14728, 14761, 14798, 14834, 14916, 14992, 15022, 15096, 15175, 15199, 15323, 15532, 15674, 15741, 15796, 15844, 15936, 16106, 16215, 16508, 16580, 16632, 16685, 16759, 16984, 17010, 17048, 17085 | ? | raw output of `sel_cut.py v 16995`; not checked by eye |

The lists marked ? at the south, east and top edges come from `tools/sel_cut.py` only.

## Ambiguities

1. **The boxed cells.** Every tie of an output to poly in this block is a "boxed cell":
   one to three small plain patches inside a heavy outline, at the end of a diffusion,
   with a poly ending at or wrapping it. At 6x the buried-contact window itself cannot
   be told from its outlines, so each is a `?B` in the trace (row 1's output to the band
   for G1, the ties of the loads of row 1, rows 2-3, G4, groups 2 and 3, the output
   cells of groups 2, 3 and 4, `ar_load_n`'s west end). Each is taken as a
   poly-to-diffusion contact because the poly that ends there has no other driver or
   is a load gate. G1's and G2's own output contacts look the same and are certain.
2. **Two boxed cells with no poly leaving them**: at the east end of `wr_data_lat_n`
   (16088-16142 x 15764-15798, three plain cells; the mirror image of row 1's output
   contact about y 15716) and at the west end of `wr_data_e_n` (16246-16296 x 15552-15572).
   Not drawn. The thin metals `wr_data_sel_n` and `wr_data_sel` pass over them. A contact from
   `wr_data_sel_n` to the first would short G4's output to `wr_data_lat_n` and leave the latch unable
   to clear; a contact from `wr_data_sel` to the second would short group 2's output to
   `wr_data_e_n`. The clean shot shows no contact footprint on either (cream / tan, not
   olive). Working assumption: unused cells, no contact.
3. **`wr_data_sel_n` across rows 1 and 3** is only a 3-6 px bright core in the metal shots
   between y 15566-15668 and 15800-15898, dark where it crosses the two boxed cells.
   Taken as one metal from 16114,15560 to 16105,15962 because the clean shot has a
   protected (pink) strip under it all the way and the core is metal-yellow over the
   orange band at y 15606 in both chips. No contact on rows 1 or 3's bands.
4. **G4's output cell** (15966-15978 x 15956-15970): that it ties both the load gate and
   the bar (and so the thin metal `wr_data_sel_n`) to G4's output is inferred: the bar has no
   other driver and row 1's upper band no other source.
5. **`ar_load_n`'s west cell** (16262-16292 x 15682-15706): that it joins the node to the
   bar from the pad 16205,15690 is inferred the same way (G2's gate has no other driver).
6. **Group 3 west of the rail** was drawn from group 2's shapes shifted by 261 px on the
   strength of the character maps and one overlay; its VCC land had no contact drawn
   (labelled `vcc`). **Settled by run 7**: read row by row and column by column against group 2, the
   same in every feature; the contact is at (15864,16352).
7. **`bd2_rs_n`**: settled by run 3 (the load is west of the rail and there is no second pull-down):
   `NOT rs_d`.
8. **Loads of G1 and G2**: the VCC lands under the rail are shared with the loads of
   `sel`'s right-hand column on the other side of the rail (`sel.txt` draws those
   schematically). The strips from the lands to the load blocks are drawn from edge
   lines seen in the metal shot.
9. **Other blocks' notes that this trace contradicts** (not edited): `trace/bd3.txt`
   block `bd3_stb` (its `e_b` label on G1's gate, and the metal it draws through the
   break); areg.md "seen below the region" (the poly from contact 16252,14862 does not
   reach 16255,15085; the strobe is not NOT E); trunks.md, which has `rs_d` on the
   metal x 16333-16352 "above 15900" with a tap at y 16335: `rs_d` ends at 16343,16603,
   and the metal above is `wr_addr_sel` ending on the contact 16343,16344.
   **With all files loaded the extraction reports two errors that come from these, not
   from bd2**: "net carries several names: wr_data_lat, e_b" (bd3_stb's metal drawn through
   the break at 16169,15443-15470) and "wr_addr_sel, rs_d" (`trace/trunks.txt`,
   `M 16342,17528 y16200`: `rs_d`'s metal should stop at y 16593; between y 16354 and
   16593 the track is empty, open colours in the clean shot).
10. **Ground rail x 16008-16058 below y 16600**: the scans show several short gaps
   (16655-16679, 16797-16815, 16921-16975, 17053-17112 in chip 2, none of them in chip 1
   above 17049). Drawn continuous to y 17050. Under it the clean shot shows only
   pink field from y 16479 to 16563.

## Not done

- **`bd2_x`, the loads of `wr_data_e_n` and `ar_load_n`, where `wr_data_e_n` goes**: done by run 4 (its
  section below), with both ties uncertain; the group's south part by run 5 (the inverter of `wr_addr_sel`),
  which also answers Ambiguity 16. Runs 1-2's joins between the bundle and the group are re-read by run 6
  (found as drawn). Left there: the three ties (Ambiguities 17 and 21) and the tie of `ar_load_n`'s west cell
  (Ambiguity 5); the strobe latch's own wiring west of the `e_b` trunk is still unreviewed (run 6's Not
  done). Groups 2 and 3 are re-read by run 7.
- **The column below y 17400** (run 3 traced group 4 and the column down to there: see its two sections).
- **Right-hand column** (x 16480-16800, y 14700-16450) and the routing east and south of
  it: not looked at. `dl7_q_n`, `dl6_q_n`, and probably `bd2_x`, `wr_data_e_n` go there.

## Where `wr_data_e_n` goes: looked at 2026-11-16, not resolved

**Superseded by run 4 (2026-11-28, section "Run 4")**: the band read here as the node's wire north to a long
load is field, the block at y 15472-15498 is the gate of a third pull-down, and the loads are under the strap.
Kept as the record of what was seen then.

This is the node that would answer "what closes the write strobe when E falls" (jsbeeb
issue 1866): NOT(`wr_data_sel` AND `e_b`) is the only traced signal that is a write to
the data register gated by E, and nothing traced uses it. Views
`cache/scratch/rax/bd2g_m.png`, `bd2g_a1.png`, `bd2g_a2.png`, `bd2q.png` (the last, a
four-shot view at 3.8x, shows nothing the 3.4x clean view does not).

Seen east of the ground rail (x 16370-16490), none of it drawn:

- **Its load**: a diffusion band leaves the node's east end, runs north along
  x 16372-16402 to y 15462 and east under a poly block (x 16405-16475, y 15468-15497)
  to the VCC land under the wide metal x 16490-16545 (contact pits at x 16510). The
  block's west end has the loop of a buried contact on the band. An ordinary depletion
  load, gate tied to the node.
- **A pad at (16452,15535)** just below the block (green centre in the clean shot, ring in
  both metal shots), from which a metal strap runs south along x 16454 to a second pad
  at (16452,15735). Under the strap: poly blocks at y 15585-15615 and 15625-15645 (the
  second is the east end of the gate band `bd2_x`, which therefore does not "arrive from
  the east" as the trace's comment says but ends here), field, poly at y 15675-15712.
- Not established: whether the pad (16452,15535) is on `wr_data_e_n` (through the load
  gate's poly) or on something else; what the pad (16452,15735) is on. If the first, the
  node goes to whatever the second pad feeds, in the lower part of this gate group
  (y 15700-15860: a loop at (16395-16420,15700-15740), a band along y 15750-15775).

Class maps at 4x (`bd2cm1.png`, `bd2cm2.png`, same day): both pads are **poly** pads.
The upper one is the south end of a poly that comes down x 16452-16470 from the east
part of the block at y 15475-15495; a dark line crosses the block at x 16447 (a
diffusion edge under it: where its channel begins). So the block with its tail is one
poly: the load's gate. By the rule that a load's gate is tied to its own node, the strap
carries `wr_data_e_n` to the lower pad; the tie itself (the buried contact at the block's
west end) was not resolved. From the lower pad the poly goes west along y 15742-15755 to
about x 16395 and turns; where it ends is not read. An orange block (poly over a channel)
lies under the strap at x 16445-16482, y 15690-15710.

Next step: the lower half of this group (x 16370-16490, y 15650-15860) at 3x, clean
shot and chip-2 stripped shot side by side, following the poly from the lower pad; then
the right-hand column x 16480-16800.

## Note (coordinator, from the handoffs of 2026-11-17/18)

The right-hand column x 16480-16800, y 14700-15770 is traced in `dlat` (the latches of data bits
4-7). `dbus_le` does not end at about (16772,15800): it runs on south along x 16774 (seen to
y 16104) over the west ends of `d5_out_n` (box 16756-16790 x 15807-15841), `d4_out_n` (y ~15957) and
`d3_out_n` (y ~16087), buried contacts onto diffusions that leave west: the outputs of those lines'
drivers, still to trace here. The enable's driver is further south.

## Run 3 (2026-11-27): the column from group 4 to the data latch enable's gate

Matt Godbolt, on Claude Fable 5.2, 2026-11-27 from 05:25 -0600. Piece `g4n`: the left column's four gates
below group 3, x 15850-16420, y 16530-17110. 8 transistors and 2 nets more in the full extraction (4,846 and 2,517),
0 errors, 0 warnings, no uncertain item added. What was read from pictures was read at 4.2-5x in three shots
and then from numbers: `tools/bd2_umap.py` (what lies under the rail), `tools/bd2_cmap.py`, a new
`tools/bd2_prof4.py` (a row or column as classes in all four shots), `tools/px.py` (raw colours),
`tools/cdp4_candh.py` / `tools/cdp4_cand.py` (is a crossing a contact) and `tools/eof_tee.py` (hidden
branches). Views in `cache/scratch/bd2/`: `a1_*`, `a2_*`, `a3_ld`, `a4_x`, `a5_*` (the photos), `o1_acid`,
`o2_acid`, `o3_c`, `o5_acid`, `o6_c` (overlays).

### What it establishes

    bd2_rs_n = NOT rs_d                       unit 1   load now traced (was: pull-down and output only)
    bd2_rw_n = NOT rw_d                       unit 2   new
    dbus_le  = NOR( cs_d, bd2_e_n )           the NOR  new: the driver of the data input latches' enable
    bd2_e_n  = NOT e_b                        unit 3   new

All four firm in `tools/unsure.py --equations`. So `dbus_le` = `e_b` AND NOT `cs_d`. Read as logic (believed:
`cs_d` has the sense of the CS pin, which selects when low): **the data input latches are open while E is high
and the chip is selected, in reads as well as writes** (R/W does not enter), and they hold from the moment E
falls or CS rises. The join of this gate's output to the eight latches' gate bands is `cdp4`'s (runs 7-13):
it rests on the metal x 16762-16780 over five output boxes, four `?M` (AMB-056); the equation here does not.

`bd2_rw_n`, `bd2_rs_n` and `bd2_e_n` (its poly column ends on band A) all go on to the read gate south of
unit 3: piece `rdg`, below.

### The column under the rail (x 16008-16058), y 16540-17110

`tools/bd2_umap.py 15990 16540 16150 17110 4 5`, from the top: output land y 16575-16590 | band y 16594-16612
(`rs_d`) | ground land y 16620-16677 (contact 16044,16652, a tall oval) | band y 16681-16699 (`rw_d`) | output land
y 16705-16722 | field y 16735-16760 | ground land y 16765-16805 (contact 16042,16782) | band y 16812-16828
(`cs_d`) | output land y 16835-16895 | band y 16898-16915 (`bd2_e_n`) | ground land y 16920-16960 (contact
16042,16945) | field y 16965-16995 | output land y 17005-17020 | band y 17030-17045 (`e_b`) | ground land
y 17050-17110 (contact 16040,17086) | band y 17115-17130 (next piece). The rail's metal is drawn on to y 17112
(run 2 stopped it at y 17050; the contact at y 17086 is on it); its south end is still not looked at.

### Units 1, 2 and 3: one inverter three times

Unit 1 (`rs_d`, y 16529-16642) and unit 3 (`e_b`, 434 px lower) are the same layout; unit 2 (`rw_d`) is unit 1
turned over about y 16647 and shares its ground land. The gate-level cell, on unit 1:

- **Pull-down.** The diffusion under the rail goes on east of it to x 16121 on both sides of the band (the
  ground land's east arm y 16620-16636; a field pocket y 16642-16660, east of x 16082, separates it from unit 2's arm), so the
  transistor is about 113 wide and 18 long. Run 2 had drawn it 58 wide (the part under the rail). The band's
  poly ends west of the rail at x 15976.
- **Output cell** (run 2): a framed box on the output land's east end with the poly that leaves east.
- **Load**, west of the rail. A poly block x 15894-15932, y 16529-16642 lies over a diffusion that runs from
  the VCC land under the supply rail (east edge x 15893) to a drain strip x 15934-15948 on the block's east
  side: channel 69 wide (y 16560-16629), 38 long. The diffusion's top and bottom edges print through the
  block as one dark line each (y 16557-16563 and y 16626-16632 down x 15912, 7-9 px: one edge line, not a gap
  between two polys, which needs two lines and field between them); the 12 px plain strip y 16644-16656
  between unit 1's and unit 2's blocks is the gap between the two polys (green in the clean shot: the two rims).
  The strip is green in the clean shot (diffusion in the open), pinker than field in the metal shots.
- **Tie.** The strip's top joins east along y 16562-16584 through a framed box (15958-15996, 16542-16582:
  heavy outline, tan centre in the clean shot) into the output land's north-west corner under the rail's
  edge; the block's north arm (y 16529-16552) ends in the box. Row y 16574 across the junction: after the
  box's east edge (x 15996) the metal shots are plain and pinker than field (158-174 / 105-135 / 72-91) to
  the rail's edge line at x 16010, with no second edge line: one diffusion.
- **VCC.** Each of the four VCC lands has a contact to the supply rail at x 15863: ring and bright core in
  both metal shots, hole in the clean shot ((15863,16587), (15863,16725), (15863,16885), (15863,17023);
  `cdp4_padc.py`). The rail is `bd3`'s (`@requires bd3`), whose `sel_rwr` copies have the same four as `?C`:
  the lands are shared with `sel`'s loads on the rail's other side. (Before the review the notes had two
  contacts on clean-shot specks 12-20 px off the rings and none for unit 3 and the NOR: corrected.)

Unit 2's own things: band y 16681-16699 east across the bundle to `rw_d`'s tap pad (centre 16296,16690; hole
in the clean shot); output cell (16088-16132, 16712-16750) on the output land's south side; its poly east along
y 16722-16740 to a pad (16208,16733) whose contact (hole in the clean shot y 16732-16740, pink again from
y 16748) is the north end of the metal x 16210: at y 16800 that track is metal in both chips (220-245 /
146-207 / 88-126 at x 16207-16216) over pink field. This is run 1's unidentified track "16210, 16754-17745".

Unit 3's own things: band y 17028-17046 east to a pad under the `e_b` trunk, centre (16166,17037). The
contact: hole in the clean shot x 16160-16172 (86-112 / 59-120 / 40-61) inside a salmon ring, bright centre
between dark rings in both metal shots, and a wider dark ring across the track than a plain crossing has
(`cdp4_cand.py`: across `AA84236BCB9522235` against `9A9646ACDB8448AA9` at (16169,16819)). This is the
trunk's "scan gap at about 17018-17044" of run 1. The output cell (16088-16132, 16978-17018) sends a poly
east along y 16987-17003 under the trunk and the track x 16210 into the NOR's input column (below).

### The NOR that drives `dbus_le` (y 16760-16965)

- Two pull-downs between two ground lands and the output land in the middle. Under the rail the diffusion is
  x 16030-16066; east of the rail a column x 16066-16096 runs through all five zones from y 16788 to y 16943
  (down x 16082: arm, edge, band, land, edge, band, arm; its east edge prints through both bands at x 16098).
  Each pull-down is 66 wide.
- **Band 1** (y 16810-16828): from x 16014 east under the whole bundle to `cs_d`'s tap pad (16384,16821)
  (hole; `trunks`' "tap at about y 16815").
- **Band 2** (y 16898-16918): from x 16012 east to x 16244, where it turns south as a **poly column
  x 16226-16244 in the gap between the track x 16210 and `bd2_rs_n`'s metal**: orange in both metal shots and
  in chip 2's stripped shot from y 16900 to y 17134 without a break (`bd2_prof4.py col 16234 16850 17150 3`);
  in the clean shot dark red-brown (poly in the open). Unit 3's row y 16987-17003 joins it from the west: at
  y 16995 the clean shot is salmon from under the track x 16210 to x 16226 and dark red from x 16230, with no
  pink between; at y 16960, where there is no row, the same stretch is pink (field) up to the column. East of
  the column at y 16995 the clean shot is pink under `bd2_rs_n`'s metal: the row ends on the column.
- **Output cell** (16096-16128, 16849-16882) at the land's east end; `cdp4`'s row `P 16130,16865 x16426`
  leaves it east (its port (16130,16865) is met).
- **Load**, west of the rail: the output land runs west as a band y 16847-16881 to the VCC land under the
  supply rail (tan under the rail's edge, x 15864-15893); a poly block x 15932-15970, y 16830-16932 crosses
  it: channel 34 wide, 38 long. **Tie**: a diffusion wire x 15988-16000 leaves the band's bottom edge (the
  edge line y 16880-16886 is open at x 15986-15998) south to y 16930 and turns west along y 16912-16930 into
  a framed box (15944-15978, 16903-16927; bright centre in the chip-1 metal shot) under the block's lower
  part. The wire is green in the clean shot and pinker than field in chip 2's metal shot (163 / 106-128 /
  74-84). A plain 8 px patch between the block and the wire (x 15976-15983, y 16885-16907; outlined, like a
  tongue) is field: R-G 16-23 in chip 2's metal shot against 35-40 on the band.

### Crossings with no contact

`cdp4_candh.py v` at every place a new poly passes under a vertical track: `rw_d`'s band under `e_b` (16169)
and `bd2_rs_n` (16255); unit 2's output row under `e_b`; `cs_d`'s band under 16169, 16211, 16255, 16298,
16342; band 2 under 16169, 16211; unit 3's row under 16211: all plain crossings (clean shot salmon, minimum
R-G 44-56). Unit 3's row under `e_b` at (16169,16995) is flagged by the metal shots' pattern (the row's two
edges print through the trunk 18 px apart) but the clean shot is salmon throughout (206-221 / 146-170 /
110-118, no hole) and the profile across the track is a plain crossing's: no contact. The three tap pads and
unit 3's pad test as pads. `eof_tee.py` on the five new rows and the column: no branch but the row itself.

### Ambiguities (run 3)

11. **The framed boxes** of this run (three output cells, four ties) are drawn `B`, not `?B`: each has the
    heavy outline and the lighter centre, the poly that ends in it has no other driver or is a load's gate,
    and the diffusion on the other side leads nowhere else. Run 2's `?B` on unit 1's output cell is left as it
    is (same look). If a box were not a contact, its net would have no driver.
12. **Under-band diffusion west of x 16008**: in units 1-3 the diffusion's west edge under the band may lie at
    about x 15997 rather than at the rail's edge (a dark line x 15995-16000 beside the rail in the metal
    shots); the bands are drawn over diffusion from x 16008. Width only (113 against perhaps 124).
13. **A dark patch in the clean shot under the rail**, x 16005-16030, y 16918-16940, below the west stub of
    the NOR's band 2 (57 / 39 / 29 against pink field 188 / 129 / 126 at y 16950; green in chip 2's stripped
    shot, which has fringes under metal). Both metal shots are bright there with no edge line, and band 1 has
    no counterpart. Not drawn: taken as residue on chip 1 (review round 1 took it so too).

### Not done (run 3)

- The next gate south: done as piece `rdg`, below.
- The rail's south end.

## Run 3, piece `rdg` (2026-11-27): the read gate and its output's route

Same run, after piece `g4n`'s review. Region x 15850-16420, y 17108-17400 for the gate; its output's route
to (17112,17950). 5 transistors and 1 net more in the full extraction (4,851 and 2,518), 0 errors, 0
warnings, no uncertain item. Views in `cache/scratch/bd2/p2/`: `b1_*`, `b2_*`, `b3_ld`, `b3_ldm`, `b4_wq`
(photos), `o_r1`, `o_r2`, `o_r3`, `o_route`, `o_rt1`, `o_end`, `o_end2` (overlays).

### What it establishes

    rd_data_e = NOR( bd2_e_n, cs_d, bd2_rw_n, bd2_rs_n )        one gate, four pull-downs, one load

Firm in `tools/unsure.py --equations`. With piece `g4n`'s three inverters: `rd_data_e` = `e_b` AND NOT `cs_d`
AND `rw_d` AND `rs_d`. Read as logic (believed, from the pins' senses): **high while E is high in a read of
the data register by the selected chip**. It is the mirror of the write decode above it (`wr_data_sel` has
`rw_d` where this has `bd2_rw_n`, and is latched by E where this is gated by E). Its output leaves the
block east and south to a pad (17080,17949) at the west edge of the untraced block below the data bus column
(x 17100-17700, y 17000-18400), where a thin metal goes on east. Believed, not traced: that block makes the
data pins' output enable from it (`tools/follow.py 17110 17947 E` runs along a metal with a contact
candidate every 30-40 px and comes out, after many corners, on the metal x 17645 that `dbus` knows as
`d_hiz`'s; the follower can merge metals at wide places, so this is a lead, not a reading).

### The gate

Under the rail (`tools/bd2_umap.py 15990 17000 16150 17460 4 5`): unit 3's ground land | band A y 17114-17134
| land L1 y 17138-17170 | band B y 17173-17193 | ground land y 17197-17242 (contact 16035,17217: pits in
the clean shot, ring in the metal shot) | band C y 17245-17265 | land L2 y 17269-17330 | band D
y 17333-17351 | ground land y 17355-17398 (contact 16045,17378) | field. East of the rail every land goes on
to x 16076-16097 (down x 16078 all nine zones show), and the bands cross the diffusion's east edge as one
edge line (x 16095-16101 under band A, x 16086-16092 under bands B and C; rows y 17122, 17183, 17255).

- **Band A, gate `bd2_e_n`**: from x 16003 east to the column x 16226-16244 of piece `g4n`, which ends on it
  (orange to y 17134; the gap x 16225-16243 is plain below y 17136).
- **Band B, gate `cs_d`**: the band's poly goes on east of the rail into an L: south along x 16093-16111 to
  y 17221, east along y 17203-17221 to under the `e_b` trunk, north under the trunk (x 16163-16180, salmon in
  the clean shot, no hole: `cdp4_candh.py v 16169,17190 16169,17205`) to y 17160, and east along y 17160-17180
  under the whole bundle to `cs_d`'s second tap pad (16384,17169) (`trunks`' "tap at 17170"). East of the rail
  the plain areas the L encloses are field (chip 2's stripped shot R-G -10..+3 there against +14..+26 on
  diffusion): the L is wiring, not a gate.
- **Band C, gate `bd2_rw_n`**: east under the `e_b` trunk to x 16222, north along x 16202-16222 to the pad
  (16209,17212), the south end of `bd2_rw_n`'s metal x 16210 (`tools/follow.py 16210 16760 S`: end
  (16210,17216), no contact candidate on the way). Below the pad the track is bare to y 17290 (orange poly
  to y 17265, then field: `tools/px.py col 16210 17212 17300 6`), so this metal and the output's are apart.
- **Band D, gate `bd2_rs_n`**: east to the pad (16253,17342), the south end of `bd2_rs_n`'s metal x 16255
  (`tools/follow.py 16255 17110 S`: end (16251,17348)).
- **L1 and L2 are one node.** A diffusion wire W, x 15974-15988, runs west of the rail from L1's west end
  (it turns east into L1 along y 17148-17164) south to the load's band: bright green in the clean shot at
  x 15978-15988 from y 17150 to y 17290 without a break (108-127 / 132-152 / 87-95 down x 15984), pink-tan
  in chip 2's stripped and metal shots (view `b4_wq`, 6x, three shots). Between W and the rail lies a field
  pocket (x 15990-16006, y 17165-17285: olive, 113 / 117 / 57) that holds the west end caps of bands B and C;
  it cannot be poly (it would join band B to band C, each driven from the east).
- **Load**: the `dbus_le` NOR's load upside down. L2 runs west as a band y 17284-17320 to the VCC land under
  the supply rail (land y 17260-17322, contact (15865,17302)); a poly block x 15908-15950, y 17236-17338 crosses it (channel 36 wide, 42 long; the band's
  edges print through the block at y 17280-17284 and y 17320-17325). **Tie**: W sends a branch west along
  y 17238-17256 into a framed box (15918-15952, 17236-17264; bright centre (15935,17250) in both metal shots)
  under the block's top. A small outlined patch (15955-15970, 17262-17280) between the block and W is field,
  like the tongue in the `dbus_le` NOR's load.
- **Output cell** (16092-16130, 17286-17314) on L2's east end; its poly east along y 17293-17307 under the
  `e_b` trunk to the pad (16210,17300).

### The output's route

`tools/follow.py 16210 17296 S`: a thin metal from the pad south along x 16210-16217 to a corner
(16217,17648), east along y 17648 (between `d6_out_n`'s line y 17603 and `e_b`'s y 17691; `busl_mdrawn.py`
listed it undrawn at three cuts) to a corner (16863,17655), south along x 16862 to a pad (16862,17948) with a
hole in the clean shot. No contact on the way: `cdp4_candh.py` every 6-8 px along all three legs finds no pad
but the end one; the follower's candidate (16711,17646) is a grey smear in the clean shot (151-162 / 128-131 /
107-113, 30 px, no edge) under bright metal with no ring in either chip. From the pad a poly row y 17938-17956
runs east under the metal x 16906 and the wide rail x 16940-17030 (salmon 205-225 / 151-176 throughout, dark
red in the gap x 16924-16942) to a second pad (17080,17949) (hole; ring in both metal shots), from which a
thin metal leaves east along y 17950: drawn 30 px, port.

### Crossings with no contact (piece `rdg`)

`cdp4_candh.py v`: the row y 17170 under 16342, 16298, 16255, 16211, 16169; the route under the `e_b` trunk
at y 17190 and 17205; band A under 16169, 16211; band C under 16169; the output row under 16169; band D
under 16169, 16211; the far row under 16906: all plain (clean shot salmon, minimum R-G 35-52). The four pads
test as pads. `tools/eof_tee.py` on every leg of the four gate polys, the output row and the far row: no
branch.

### Ambiguities (piece `rdg`)

14. **The link W** is read from colour over 140 px of a 14 px strip between two edge lines; in chip 2's
    metal and stripped shots its west half is redder and its east half plain, as on the `dbus_le` NOR's tie
    wire. If W were not diffusion north of the branch (y 17256), L1 would have neither load nor output.
15. (Closed by review round 2: the load's VCC land runs from y 17260 and has its contact at (15865,17302).)

### Not done (piece `rdg`)

- The block below the data bus column that `rd_data_e` enters at (17112,17950) (`busc`'s region).
- The ground rail south of y 17400 (`cdp4` draws it from y 17285 to y 17535); the column under it below
  y 17400 (a land from y 17435 on).

## Run 4 (2026-11-28): the gate group east of its rail

Tom Seddon, on Claude Fable 5.2, 2026-11-28 from 03:06 +0000. Piece `gge`: x 16366-16500, y 15440-15760, the part
of the gate group east of its ground rail x 16312-16362, as far as the VCC rail x 16491-16538 (`dlat`'s).
3 transistors more in the full extraction (4,911; 2,538 nets), 0 errors, 0 warnings; two uncertain ties.
Views in `cache/scratch/bd2/`: `s1`, `s2u`, `s2l`, `u1`, `u2`, `u3a` (7x, chip 2 stripped), `m1`, `m2`, `l1`,
`j1`, `j2`, `j3` (9-10x, four shots), overlays `o1`, `o2`. Pictures of this spot are too blurred to decide a
junction (as run 2 found); what is drawn rests on numbers: `tools/px.py` rows, columns and points in all four
shots, `tools/bd2_umap.py` (the clean shot under metal), `tools/bd2_prof4.py`, `tools/cdp4_candh.py`.

### What it establishes

    wr_data_e_n = NOT( ar_load_n OR (wr_data_sel AND e_b) )
    ar_load_n   = NOT( wr_data_e_n OR (e_b AND wr_addr_sel) )

**Marked, both**: each cross term enters through a tie drawn `?B` (Ambiguity 17). Without the two ties the
extraction has three firm transistors and two polys with no driver:

| Transistor | W/L | Gate | Between | State |
|---|---|---|---|---|
| third pull-down of the upper gate, (16430,15485) | 39/26 | the poly of pad U, the strap and pad L (`bd2_w15540`) | `vss` and `wr_data_e_n` | firm |
| load of the upper gate, (16457,15608) | 22/50 | the poly of the band `bd2_x` | `wr_data_e_n` and `vcc` | firm |
| load of the lower gate, (16457,15702) | 23/50 | the poly of pad L (`bd2_w15540`) | `ar_load_n` and `vcc` | firm |

So `bd2_x`, run 2's "second term of the address register strobe, arriving from the east", does not arrive
from anywhere: its band is the west arm of the upper load's poly and ends under the strap at x 16482. And the
"strap" that run 2's last look could not place (pad (16452,15535) to pad (16452,15735)) joins the gate of the
upper gate's third pull-down to the lower load's poly. Each of the two polys has a load's channel under it and
one other gate, no metal contact but the strap's two, and one framed box at a node's arm: read as each load's
gate tied to its own node, which is what makes the pair cross-coupled. The 2026-11-16 reading of this spot (a
band north along x 16372-16402 and a long load east-west under the block at y 15472-15498) is withdrawn: that
"band" and the gap to the VCC land are field.

### Calibration (all `tools/px.py pt`, layers `acid1b,acid,metal,metal1`)

Open diffusion known from runs 2-3: (15954,16150) chip 2 stripped R-G +33, chip 2 metal 168/113/76;
(15981,17220) stripped +16. Field pocket (15998,17220): stripped +3. Field here (16440,15420): stripped
150/155 (-5), metal 165/138/89. In the clean shot open diffusion is pink to red here (166/107/95), not green.

### The upper part, y 15440-15575

- **T**, the top strip x 16377-16453, y 15449-15462: diffusion (stripped R-G +17..+28 down x 16383, 16398,
  16425; metal 166-178/133-136/88-91). Its east end is closed (outline x 16450-16455); east of it
  (16465,15452), (16475,15458), (16470,15445) are field (stripped -3..-8), so the VCC land does not come west
  here. **Its west end is a tongue of the rail's ground land**: under the rail's protected margin the clean
  shot is tan to x 16371 at y 15448-15458 and only there; at y 15424-15444 the land ends at x 16359
  (`tools/bd2_umap.py 16344 15412 16388 15580 3 4`). The 6 px between x 16371 and T's first diffusion sample
  (x 16377) are the margin's boundary line and are not read (Ambiguity 18).
- **The block**, poly, x 16394-16480, y 15472-15498 (orange in both chip-2 shots and in chip 1's metal shot).
  Two dark lines cross it north-south, at x 16408-16411 and x 16450-16455, each running on as an outline of
  the plain area above and below: the diffusion under the block runs north-south between them, from T to the
  area south of the block (stripped +18 at (16440,15510)). Between the lines the poly is bright, outside them
  duller. The block's top and bottom lines are thin (about 4 px): single edges. Channel 39 wide, 26 long.
- West of x 16408 the block ends in a cap x 16394-16410 with a heavy outline (interior olive in chip 2:
  stripped 134/130/65, metal 125/114/61): read as the gate's end over field, not a buried contact
  (Ambiguity 19). The area west and south-west of it (x 16380-16407, y 15470-15546) is a field pocket:
  stripped -10, clean 150/153/99.
- East of x 16455 the poly goes on to x 16480 and turns south (x 16455-16478) to **pad U**
  (16436-16476, 15522-15560), contact (16453,15539): green hole in the clean shot (`cdp4_candh.py`: clean
  minimum R-G -32..-40), yellow centre in chip 2's stripped shot, ring and bright centre in both metal shots.
- South of the block the diffusion narrows to a wire x 16409-16425 (stripped +33..+42 down x 16416,
  y 15518-15548; metal 172-179/115-119/80-85; chip 1's metal shot 137-143/94-98/78-85) which runs south to
  y 15621. The strip beside it, x 16423-16432, reads dark olive in both chip-2 shots and is taken as the pad's
  broad outline, not a second wire.
- **The node's arm**: the band y 15553-15568 from the rail column (the clean shot under the margin is tan to
  x 16371 at y 15548-15564, the node's rows) east to the wire: row y 15562 is diffusion without an edge line
  from x 16380 to x 16422 in three shots (stripped R-G +14..+39 at every sample; metal 164-179/127-138;
  chip 1's metal 132-153/107-116). So the wire is `wr_data_e_n`.

### The strap

`tools/follow.py 16452 15570 S`: a thin metal x 16446-16466 from pad U to its end (16449,15746) on **pad L**
(16434-16482, 15719-15757), contact (16452,15740) (clean minimum R-G -12..-15, a large bright centre in both
metal shots). Between the pads it crosses three poly blocks; `tools/cdp4_candh.py -v v` every 8-14 px along
it gives clean minima of 0..+78 there (edge lines; no green hole): no contact.

### The two loads, y 15575-15725

Under and beside the strap the clean shot (protected by the strap and the rail's margin from x 16436 on)
shows, north to south (`tools/bd2_umap.py 16424 15500 16500 15772 4 4`; `tools/px.py col 16437 15572 15764 3`
in four shots, in the open stretch west of the strap):

    bar A        y 15580-15590   poly (metal 169/111/60, chip 1 162/77/38)
    line         y 15591-15597   dark, 6-9 px
    block 1      y 15598-15618   poly, bright (metal 177-189/137-148/70-75, chip 1 146-170/99-110/46-61)
    line         y 15619-15626   dark, 9 px, no plain colour in it
    block 2      y 15627-15648   poly (metal 146-158/100-120/45-59)
    field        y 15655-15666   (metal 156-161/149-154/83-93)
    bar C        y 15674-15684   poly
    line         y 15685-15692   dark, 9 px
    block 3      y 15694-15712   poly, bright
    line         y 15714-15719   dark, 6 px, no plain colour in it
    pad L        y 15720-15757

- **A, block 1 and block 2 are one poly, and so are C, block 3 and pad L.** The lines between them are the
  edges of a diffusion strip under the poly (run 2's rule for this block's loads: two polys cannot lie 6-9 px
  apart, and the line under each bar, where the poly must overhang its strip, looks the same as the line under
  the block's other side). The bright part of each is the channel. Where two polys really are apart (block 2
  to bar C) the same column shows 12 px of field colour between two dark lines.
- **The strips reach the VCC land.** Under the rail the land is one tan area x 16500-16540 from y 15572 to
  y 15706 with contact pits (`tools/bd2_umap.py 16480 15572 16552 15730 4 6`), and it comes west to x 16488
  only at y 15596-15608 and y 15692-15704, the two strips' rows; beside block 2 the same column is field.
- **West ends.** Row y 15605: plain without an edge from the node's wire (x 16408) to the poly's edge line at
  x 16429: the upper strip leaves `wr_data_e_n`'s wire. Row y 15695: plain without an edge from x 16375 to
  x 16426, then the edge line and the poly: the lower strip is `ar_load_n`'s east arm (run 2 had it to
  x 16374).
- **Block 2 is the east end of the band of `bd2_x`**: at y 15642 the band is orange in both chip-2 shots from
  the rail (x 16372) to x 16435 and salmon under the strap from there to x 16482; field beyond (x 16488).
- Two green rings in the clean shot at (16470-16488, 15650-15668) and about (16478,15562) are not layout:
  both metal shots are plain there (153/153/88, 139/132/66); they lie in the 10 px between the strap's and the
  rail's protected margins.

### The two ties (drawn uncertain)

- **Lower.** From pad L a poly row y 15745-15757 runs west to x 16391 (orange in both metal shots, red-brown
  in the clean shot) and meets a framed structure under the arm of `ar_load_n`: a box (16393-16409,
  15719-15735) with a light centre in both chip-2 shots and chip 1's metal shot, a lens-shaped plain area
  between it and the arm's heavy bottom line (y 15708-15718), and a smaller cell east of it (16418-16427,
  15720-15733) (view `j3`). It is the "boxed cell" of this block (Ambiguity 1): drawn as a diffusion tab from
  the arm, the row's poly turned north over it, and a `?B`.
- **Upper** (moved by review round 3). The framed box is at x 16368-16404, y 15596-15629: a dark frame 8-10 px
  thick on all four sides round a plain centre x 16383-16392, y 15611-15617 (`tools/px.py col 16388 15566 15640 3`
  and `row 15614 16362 16416 3`: centre metal 166/137/88, chip 1 155/129/69, stripped R-G +22..+37; the clean
  shot is dark there). Its south frame lies on the top of `bd2_x`'s band and its east frame against the west
  side of the node's wire (diffusion from x 16407 on row y 15614). Drawn as the band's poly taken north into
  it, the wire's west side taken into it, and a `?B`. Run 4 first drew this tie 30 px further north, on the
  plain area under the arm's arch (16376-16399, 15574-15595): that area is field (stripped R-G -9..-22 down
  x 16388, y 15578-15590; like the pocket at (16395,15530)), and the box here was the "poly piece" left out.
- **The band's path**: at the rail's height (y 15638-15657) from its west end at x 16290 (orange in the 10 px
  between the thin metal x 16270-16284 and the rail; pink field under that metal) as far as x 16392, then
  y 15633-15651 on east to the block (review round 3; `tools/px.py col 16380` and `col 16410`).

### Ambiguities (run 4)

16. **The function as drawn is not believable as it stands.** (**Answered by run 5**: the wrong join was run
    2's, G_a on `wr_data_sel`; with G_a on the inverter of `wr_addr_sel` the pair is a D latch. Kept as
    written.) With both ties the two gates are a set/reset
    pair: `ar_load` goes high in a write to the address register (E high) and stays high until E is high in a
    write to a data register. `ar_load` is the gate of the address register's five write transistors (`areg`),
    and the data input latches follow the pins in every selected cycle, reads included (`dbus_le`, run 3), so
    a read after an address write would let the address register follow the pins the chip itself drives. No
    such behaviour is known. Candidates, none checked: one of the two ties is not what it is drawn as; a join
    of runs 1-2 (unreviewed) is wrong, e.g. G2's gate on `ar_load_n` through its `?B` (Ambiguity 5), group 3's
    identity (Ambiguity 6), or which signals gate the two stacks; or `areg`'s use of `ar_load`. The three
    transistors and the two polys do not depend on this.
17. **The two ties** are read from the look of a framed box at the end of a poly that has no other driver
    (each poly was followed to all its ends: a load's channel, one other gate, the strap's pads). Neither
    window is resolved at 9x in four shots. If the upper tie is not there, `bd2_x`'s band has no driver at
    all: its west end (x 16290, re-read by review round 3) has none.
18. **T's join to the ground land** rests on the tongue of tan in the clean shot under the rail's margin; the
    last 6 px are not seen. If T were not on the land the third pull-down would have no source.
19. **The block's west cap** (16394-16410, 15472-15499) has the heavy outline of a framed box. It lies over
    the field pocket, with T 6 px north of it and the strip's edge at its east side: read as a gate's end, with
    no diffusion under it.
20. **The wire's width** below the block (x 16409-16425 drawn; the east edge may be at x 16422 or x 16432):
    width only.

### Not done (run 4)

- The group's south part east of the rail: done by run 5.
- The ties (Ambiguity 17). The function (Ambiguity 16) is answered by run 5.

## Run 5 (2026-11-28): the inverter of `wr_addr_sel`, and what gates the upper gate

Tom Seddon, on Claude Fable 5.2, 2026-11-28 from 04:02 +0000. Piece `ggs`: the gate group's south part east
of its rail (x 16366-16545, y 15757-15900), the rail's south end (x 16312-16362, y 15832-15922) and the pad
(16274,15873) with what reaches it. 2 transistors and 1 net more in the full extraction (4,913; 2,539), 0
errors, 0 warnings; one uncertain tie added, and **one join of run 2 removed**. Views in `cache/scratch/bd2/`:
`r5_s1` (4x, four shots), `r5_s2` (2.4x), `r5_u1` (5.8x), `r5_u2` (5x, under the rail's end), `r5_j1` (4.9x,
the pad and the ground west of it), overlay `r5_o1`. As in runs 2-4 the pictures place things and the numbers
decide: `tools/px.py`, `tools/bd2_cmap.py`, `tools/bd2_umap.py`, `tools/bd2_prof4.py`, `tools/textmap.py`,
`tools/cdp4_candh.py`, `tools/cdp4_padc.py`, `tools/follow.py`.

### What it establishes

    wr_addr_sel_n = NOT wr_addr_sel                                  (new: 38/20 against a load of 24/50)
    wr_data_e_n   = NOT( ar_load_n OR (wr_addr_sel_n AND e_b) )      (G_a's gate corrected)
    ar_load_n     = NOT( wr_data_e_n OR (e_b AND wr_addr_sel) )      (as run 4)

**The address register's strobe is a transparent latch of `wr_addr_sel`, open while `e_b` is high**: the same
circuit as the write strobe latch (rows 1-3 with G4), with the inverter here in G4's place. Marked: the
inverter's output reaches G_a through a tie drawn `?B` (Ambiguity 21), and the two cross terms through run 4's
(Ambiguity 17).

**Run 2's join of G_a to `wr_data_sel` is withdrawn.** Run 2 drew the lower band of row 3 (`wr_data_sel`,
y 15857-15877) on east to the pad (16274,15872), the foot of the thin metal that goes up to G_a's pad. Between
the metal x 16200-16222, under which that band ends and its poly turns south to the pad (16211,15997), and the
pad's outline at x 16253 there is open field in all four shots:

- `tools/px.py row 15868 16216 16264 3`: x 16237-16249 chip 2 stripped 154-156/156-162/88-95 (red minus green
  -1 to -13), chip 2 metal 167-170/138-143/80-88, chip 1 metal 137-142/112-115/75-82, clean 152-158/130-150/89-101
  (khaki). Poly here is 165-180/107-128/56-66 in chip 2's metal shot and red over green by 40-70 in its stripped
  shot.
- `tools/bd2_prof4.py row 15862 / 15868 / 15874 16150 16440 3`: plain in all four shots from x 16231 to x 16252
  on all three rows; `tools/textmap.py 16244 15846 16312 15900 3 --acid`: the stripped shot is greener than red
  at x 16244-16256 on every row from y 15846 to y 15897. View `r5_j1`.

So nothing of row 3's reaches the pad. What does reach it is a poly row from the east.

### The inverter

- **Gate.** Band G_e (`wr_addr_sel`, y 15770-15788) turns south at the rail's east edge: a poly column
  x 16364-16384 from the band to a cap at y 15852 (`tools/bd2_prof4.py col 16376 15756 15900 2`: orange in
  both chip-2 shots and chip 1's metal shot y 15782-15798, 15808-15836, 15846-15850; salmon in the clean shot
  under the rail's margin, x 16364-16371, `tools/bd2_umap.py 16336 15740 16392 15846 2 2`). Two dark lines cross
  it, at y 15800-15806 and y 15838-15844: a diffusion's edges.
- **Source.** West of the column the ground land under the rail (contact (16330,15812)) runs to the column's
  edge with no edge line: `tools/px.py row 15812 16346 16376 2 acid1b` gives tan 195/181/139, then 164/113/105
  and 209/103/87 (the poly's red outline), then salmon 246/146/99; row y 15822 the same. Controls with the same
  command: row y 15752 (the node above G_e, where the land ends in field) is dark, 84/80/64 and 93/47/41, for
  6 px and then pink; row y 15778 (G_e over the column's edge) dark 75/66/58, 93/45/39.
- **Drain, the node.** East of the column a diffusion x 16392-16424, y 15806-15836 (`tools/px.py row 15812`,
  `row 15822`, `col 16400`: stripped red minus green +14 to +39, metal 173-179/132-138/85-92; field 20 px north,
  (16405,15788), stripped 0). The dark line x 16382-16390 between column and node is the column's own outline:
  it runs the column's whole length, also where field is east of it (`tools/bd2_prof4.py col 16386`).
- **Load.** East of the node a poly x 16432-16482: bar y 15784-15797, block y 15804-15826, south bar
  y 15834-15843, with single dark lines of 6-8 px between and orange on both sides of each
  (`tools/px.py col 16455` and `col 16474 15780 15846 2`; the same look as the two loads north of it, control
  `col 16474 15578 15630 2`): one poly over a strip. The strip leaves the node without an edge line (rows
  y 15812, 15822: plain from x 16392 to the poly's outline at x 16428) and reaches the VCC land under the rail
  x 16491-16538: the land is tan x 16500-16540 from y 15772 to y 15872 and comes west to x 16484 only at
  y 15804-15820 (`tools/bd2_umap.py 16340 15744 16560 15876 4 4`). Contacts (16513,15799) and (16514,15844)
  (`tools/cdp4_padc.py`: bright centre in both metal shots, a hole of 420 px in the clean shot at each). The
  rail's metal is drawn on to y 15900; it runs further.
- **The load poly's arm.** From the south bar a poly column x 16432-16452 runs south to y 15886
  (`tools/bd2_prof4.py col 16441 15826 15902 2`: orange without a break y 15834-15884 in three shots, field from
  y 15892). The area inside the L (x 16456-16484, y 15848-15912) is field, open to the south
  (`col 16468`; (16470,15860) stripped +1).
- **The node's wire.** From the node's south-east corner a diffusion x 16406-16421 runs south
  (`tools/bd2_prof4.py col 16412 15790 15900 2`: diffusion colours y 15806-15858 with no line across, a dark
  line y 15860-15868, a plain patch y 15870-15886).
- **The box** (Ambiguity 21). The patch is x 16410-16418, between two dark bands of 10-12 px (x 16396-16408
  and x 16420-16429; `tools/px.py row 15878 16366 16462 3`), inside a heavy outline about x 16400-16426,
  y 15860-15892. West of it a poly row ends, east of it the arm. It is the boxed cell of this block
  (Ambiguity 1) and what a poly through a buried contact looks like from above (tracing guide, trap 24). Drawn
  as the row's poly taken through to the arm over the wire's end, with a `?B`.
- **The output row.** Poly y 15868-15887 from the box west: open x 16372-16396 (orange in three shots), under
  the rail's south end (salmon y 15869-15884 across x 16314-16370 with no line along it or across it:
  `tools/px.py col 16322`, `col 16344`, `col 16364 15830 15912 3`), x 16294-16310, into the pad (16253-16292,
  15852-15892). The pad's contact (16274,15873): `tools/cdp4_candh.py -v v 16276,15872`: PAD, clean minimum red
  minus green -25 (view `r5_j1`: green hole, bright centre in chip 1). The thin metal: `tools/follow.py 16277
  15700 N` and `S` end at (16277,15468) and (16273,15880), G_a's pad and this one.
- The rail x 16312-16362 is drawn on to its south end (y 15920). Under it south of the land the clean shot is
  pink field but for a grey-olive smear x 16334-16352 north and south of the row (145/151/111, no outline, both
  metal shots plain apart from the row's two edge lines): residue, not drawn (view `r5_u2`).
- Field, checked: x 16385-16485, y 15758-15778 and x 16388-16428, y 15778-15798 (stripped red minus green 0 to
  -16 at five points; the clean shot's green double lines there are rims); the pocket x 16378-16400,
  y 15843-15858 (stripped 130/149/92). `tools/opendiff.py 16366 15757 16490 15940`: no large open diffusion
  undrawn.

### The thin metal over the two boxed cells (run 2's Ambiguity 2, re-read)

The net of G_a now being this inverter's output, a contact from the thin metal x 16270-16284 to either boxed
cell it crosses (the west ends of `wr_data_e_n`, y 15548-15578, and of `ar_load_n`, y 15680-15713) would short
that output to a latch node. `tools/cdp4_candh.py -v v` calls both pad-like (a bright centre between two dark
bars in both metal shots, clean minimum -20 and -33). Read as no contact, as run 2 did, on three counts
(`tools/px.py row 15563`, `15697` against `15600`, `15650` on the same metal over field and `15875`, `15473`
at its two real contacts; `tools/textmap.py 16244 15538 16312 15584 3 --acid`, `16244 15668 16312 15720 3 --acid`):

- the clean shot under the centre is cream, 187/185/129 and 182/185/130, with a greenish spot 3-6 px wide
  beside it (153/172/132, 144/173/136): blue 129-136. The holes of the two real contacts are 9-12 px wide,
  150-175/184-193/103-109 (trap 26's two classes: 186-203/176-182/131-139 for a pass-over, blue 85-108 for a
  hole);
- the metal is not widened: its bright part is 8 px wide over each box against 15 px over field;
- the dark bars are 9-10 px (edges underneath), not a ring.

It stays a reading (Ambiguity 22), and since review round 4 the two stretches (y 15546-15580, y 15678-15716)
are drawn `?M`, as trap 27 asks, with the label `bd2_w15872` on G_a's pad: `tools/unsure.py` lists
`wr_addr_sel_n` as joined to it only through uncertain items (the two stretches and the tie box).

### The stacks are wider than runs 2-4 drew them (review round 4)

The diffusion under bands G_a and G_b runs west to x 16288, not x 16314: between the bands the clean shot is tan
at x 16290-16296 and pink field at x 16276-16282 (`tools/bd2_umap.py 16276 15416 16330 15580 2 4`; row y 15504
is tan without a break from x 16290 to the rail), and both metal shots have an edge line at x 16284-16292
across each band (`tools/px.py row 15478`, `15520 16272 16300 3`). The same for G_d and G_e, the foot of
`ar_load_n` (y 15710-15724) and a tab of the south ground land (x 16286-16302, y 15794-15806)
(`tools/bd2_umap.py 16276 15590 16330 15840 2 4`); the north ground land and band x's channel do not run west
(field at x 16276-16290, y 15594-15662). Drawn: the upper stack's pull-downs are 78/22 (were 52/22), the lower
stack's 62/18 (were 38/18). Widths only.

### Ambiguities (run 5)

21. **The inverter's tie box** (16400-16426, 15860-15892): that the row, the load poly's arm and the node's
    wire are joined there is read from the box's look and from what ends at it; the window is not resolved.
    Without it the row (and so G_a) has no driver and the load's gate is tied to nothing.
22. **The thin metal x 16270-16284 over the two boxed cells**: no contact, by the clean shot's colour and the
    metal's width (above); drawn `?M` there. A contact at either would short the inverter's output to a node of
    the latch. The cell at the west end of `wr_data_e_n` still has no poly leaving it (run 2's Ambiguity 2): a
    small poly island lies at its west end (x 16244-16256, y 15550-15574), closed, with field for 8 px or more
    between it and the feed of band G_b north of it (`tools/bd2_cmap.py 16226 15500 16268 15584 3`; review
    round 4). Not drawn: it joins nothing.
23. **The gate's west side** is under the rail's margin: that the ground land reaches the column rests on the
    clean shot's missing edge line there (two rows, two controls). If the land ended short of it the
    pull-down would have no source.
24. **The poly column's south end**: drawn to y 15852 (orange y 15846-15850 at x 16376, salmon at y 15844 under
    the margin); the cap itself is not resolved. Length only.

### Not done (run 5)

- Runs 1-2's other joins round the group, still unreviewed: G2's gate on `ar_load_n` through the `?B` at
  (16262-16292, 15682-15706); group 3 west of the rail (drawn "by the pattern of group 2"); the taps of
  `e_b` on bands G_b and G_d. Run 5 re-read only G_a's net. (**Run 6** re-read the first and the third, with
  the rest of the wiring between the bundle and the group; group 3 is left.)
- The column under the left rail below y 17400; the `?B` cells of runs 1-2.
- East of the VCC rail x 16491-16538 south of y 15770 (the right-hand column's lower part): not looked at.

## Run 6 (2026-11-28): the wiring between the bundle and the gate group, re-read

Tom Seddon, on Claude Fable 5.2, 2026-11-28 from 04:52 +0000. Piece `ggw`: x 16095-16312, y 15280-15800, the
polys and metals that runs 1 and 2 drew between the bundle's tracks (x 16104-16284) and the gate group's two
stacks, none of which a review had read (run 5's Not done; round 4's "not checked"). **A re-read: everything
was found as drawn, and no geometry changed** (4,913 transistors, 2,539 nets, 0 errors, 0 warnings, as before).
Views in `cache/scratch/bd2/`: `r6_s1`, `r6_s2` (2.8x, metal and clean shot with the trace), `r6_j1` (5x, four
shots, the break), `r6_j2` (2.75x, four shots, the pad of `ar_load_n`). As in runs 2-5 the numbers decide:
`tools/tl5_tracks.py` (the two-chip metal test along each metal), `tools/bd2_umap.py`, `tools/bd2_cmap.py`,
`tools/px.py`, `tools/textmap.py`, `tools/cdp4_candh.py`, `tools/cdp4_padc.py`, `tools/opendiff.py`.

### What it confirms

Each of these is a join or a separation that the equations of the two latches rest on:

| Net | What is drawn | Read again by |
|---|---|---|
| `wr_data_lat` | the metal x 16158-16178 from G1 **ends** on the contact (16167,15432); 10 px of bare poly between its pad's ring and the top edge of `e_b`'s metal | `tools/px.py col 16169 15402 15530 3 all --r 2`: ring y 15414-15426, centre, ring y 15441-15453, then y 15456-15465 orange in both chips (chip 2 173/119/58, 169/102/43; chip 1 158/96/49, 156/86/56), dark y 15468-15471, metal from y 15474 (218/174/88, chip 1 218/181/86). `row 15460 16143 16195 3`: orange x 16164-16173 in both chips; control `row 15490` (the lower trunk over the same poly): chip 1 193-229/169-183. Chip 2's stripped shot: 50-79 red at y 15450-15468, 175-212 elsewhere. `tools/tl5_tracks.py v 16169 15380 15860`: no metal in both chips for 34 px below the centre, against 16-19 px at the trunk's other three contacts. View `r6_j1` |
| `wr_data_lat` | the pad's poly ("strip 1") south under `e_b`'s trunk, diagonally to under the metal x 16200-16222, into the block (16226-16248, 15598-15662), and from the block's foot west as the band y 15643-15657 under that metal and the trunk | `tools/bd2_umap.py 16100 15340 16304 15540 4 4` and `16148 15540 16304 15800 4 4`: salmon without a break x 16164-16172 from the pad to y 15520, stepping east from y 15524, under the metal x 16196-16219 from y 15544 to y 15612, the band y 15644-15656 under the metal (`px.py col 16212 15628 15672 3`: 223/159/121, 214/164/119) and slanting under the trunk to x 16152-16164 at y 15672; in the 20 px between the two metals orange in three shots (`tools/bd2_cmap.py`, rows y 15528-15552 and y 15644-15656) |
| `e_b` | the lower trunk starts at the corner (16169,15480): west along y 15470-15490, north along x 16112-16135 to the contact (16122,15388) | `tools/tl5_tracks.py v 16122 15370 15500`, `h 15480 16110 16180`: metal throughout but for an 8 px bar x 16154-16162, the west edge of strip 1 underneath; the clean shot's protected pink is unbroken under both arms |
| `e_b` | from that contact's pad a poly east along y 15358-15378 under the upper trunk, then south under the metal x 16200-16222 ("strip 2") to y 15488, diagonally into the open and east as band G_b | `bd2_umap.py`: salmon y 15360-15372 under the trunk and under the metal, pink field above; x 16208-16216 from y 15376 to y 15500 without a break, x 16220 at y 15512, x 16224 at y 15516; `bd2_cmap.py`: orange x 16228-16262, y 15512-15528 in three shots; `px.py row 15520 16238 16312 3 all` |
| `e_b` | taps (16167,15605) (pad, row west to row 1's lower band) and (16167,15735) (pad, row east y 15728-15746 = band G_d) | `tools/cdp4_padc.py`: holes of 284 and 245 px; `bd2_cmap.py`: G_d's row orange x 16184-16262 in three shots; `px.py row 15737 16238 16312 3 all` |
| `ar_load_n` | G2's gate band on the pad of the contact (16210,15300); one metal x 16200-16222 from there to the contact (16205,15690); its pad's poly bar east to the boxed cell (16262-16292, 15682-15706) | `px.py row 15301 16150 16236 4 all`: salmon without a break x 16158-16198, hole x 16206-16218; `tl5_tracks.py v 16211 15285 15800`: metal from the hole at y 15303 to the hole at y 15694, dark bars of 8-18 px only; `px.py row 15695 16186 16318 3 all`: poly x 16228-16250 (chip 2 160-179/78-143/42-70, chip 1 135-163/63-90), the cell's outline x 16255-16267, the thin metal, then diffusion x 16294-16306 (151-178/86-145/70-91) into the stack. The tie itself stays `?B` (Ambiguity 5) |
| `wr_addr_sel` | the contact (16207,15778) is the north end of another metal on the same track; its pad's poly east = band G_e | `tl5_tracks.py v 16211`: no metal in either chip y 15700-15775, open ground at y 15722 and y 15747 (clean red minus green -44) on both sides of G_d's row, which passes between the two pads; `px.py row 15779 16238 16312 3 all` |

**No contact at any crossing.** `tools/cdp4_candh.py -v v` on the metal x 16200-16222 over strip 2, strip 1 and
the band (y 15368, 15420, 15470, 15515, 15548, 15590, 15650) and on the trunk over the branch, strip 1 and the
band (y 15368, 15490, 15660): none pad-like, clean minima of red minus green 36 to 82 (a hole is under 24);
`tl5_tracks.py` finds holes on those two metals only at their seven contacts. G2's band and `ar_load`'s row
under the upper trunk (y 15290-15312, 15246-15268): two edge bars each, no hole.

**Nothing joins that is drawn apart.** Field under the metal x 16200-16222 between the band and the pad
(pink, y 15660-15676); no poly column in the gap between the trunk and that metal (`px.py row 15400`,
`row 15580 16176 16204 2 all`: plain 158-174/129-153/84-90, clean green); the upper trunk's pad has field
north of it (pink y 15376-15416) and `e_b`'s pad only the one branch; G_b's feed is 17 px of plain ground from
G_a's pad and G_d's row 14-17 px of open ground from each pad on the track x 16210. `tools/opendiff.py 16095
15280 16312 15800`: one green group, the field strip in the gap between the two metals (235 px2 at
x 16186-16195, y 15412-15448; stripped red minus green about 0).

### Ambiguities (run 6)

25. **The thin metal x 16270-16284 over bands G_d and G_e**: `tools/cdp4_candh.py -v v 16277,15735
    16277,15779` calls both pad-like (clean minima 11 and 33); over G_b (`16277,15520`) not. Read as pass-overs
    (`tools/textmap.py 16246 15496 16312 15545 3 --acid`, `16246 15712 16312 15806 3 --acid`, against the
    metal's two contacts, `16240 15452 16300 15496` and `16246 15850 16312 15896`): the dark bars above and
    below the bright stretch are the rows' own edge lines and run on past the metal on both sides (a ring does
    not); the metal is not widened (bright part 9 px, as between the rows); the clean shot under the metal's
    centre is salmon, 211-231/154-173 (`px.py row 15520`, `15737`, `15779 16238 16312 3 all`: the three bands
    alike), and its low value is a sliver 5 px wide on the metal's east edge, the edge line of the stack's
    diffusion under the band, present at all three bands; the two real holes are 9-12 px wide and centred. A
    contact at G_d would short this inverter's output to `e_b`, one at G_e to its own input.
26. **The block's foot and the pad of `ar_load_n`** (strip 1's block ends at y 15657-15662, the pad and its bar
    begin at y 15675-15684): 12 px between the two edge lines, the narrowest gap of the piece; a join would put
    G1's gate and G2's on one net. Read as apart: pink field under the metal's margin to x 16227 at
    y 15660-15676; at x 16240 field in three shots (stripped red minus green -20 to +12); at x 16234 the stripped
    shot reddens toward the south line (+15 to +42: the south flank of a narrow band, tracing guide trap 38)
    while the clean shot is green and dark with no red-brown (`tools/px.py col 16228`, `16234`, `16240 15636
    15700 3 all`).

### Not done (run 6)

- **Group 3 west of the rail** (x 15890-16060, y 16245-16470), drawn "by the pattern of group 2", its VCC
  contact not looked for; with it group 2 (y 15985-16210), which no review has read either. Next.
- The strobe latch's own wiring west of the `e_b` trunk (x 16088-16150, y 15540-15990): the thin metal
  `wr_data_sel_n`, the hook cell on row 1's output, the undrawn boxed structure at (16088-16142, 15764-15798)
  (Ambiguities 2-4): unreviewed.
- The column under the left rail below y 17400; the `?B` cells of runs 1-2; east of the VCC rail
  x 16491-16538 south of y 15770.

## Run 7 (2026-11-28): groups 2 and 3, re-read

Tom Seddon, on Claude Fable 5.2, 2026-11-28 from 05:25 +0000. Piece `g23`: x 15850-16400, y 15980-16475, the two
three-input NORs that run 2 drew and no review had read (run 6's Not done): group 2 (`wr_data_sel`) and group 3
(`wr_addr_sel`), the second drawn west of the rail "by the pattern of group 2". **A re-read: every connection is
as drawn** (`tools/sameconn.py` against the last merge, 84a0fe3b: connections identical, the package alone and
with every trace file; 4,913 transistors, 2,539 nets, 0 errors, 0 warnings). What changed is geometry: three
widths, the place of two boxed cells, one contact. Views in `cache/scratch/bd2/`: `r7_g2w`, `r7_g3w` (2.1-2.2x,
the west parts, three shots), `r7_g2e`, `r7_g3e` (1.75x, the bundle crossing with the trace), `r7_g2cell`,
`r7_g2R` (7x, four shots), overlays `r7_o1`, `r7_o2`, `r7_o3`. The numbers decide, as before:
`tools/bd2_prof4.py` (rows and columns in four shots), `tools/bd2_umap.py`, `tools/bd2_cmap.py`, `tools/px.py`,
`tools/textmap.py`, `tools/tl5_tracks.py`, `tools/opendiff.py`.

### What it confirms

    wr_data_sel = NOR( rw_d, bd2_rs_n, cs_d )        group 2
    wr_addr_sel = NOR( rw_d, rs_d, cs_d )            group 3

Marked, both, as before: each output reaches its poly band through a boxed cell drawn `?B`, and each load's
gate is tied through another (Ambiguity 1).

**Group 3 is group 2 again, feature for feature, 261 px south.** The same eleven rows and five columns were
read in both (`tools/bd2_prof4.py row Y 15880 16066 2` at y 16020, 16056, 16072, 16084, 16100, 16132, 16150,
16168, 16188, 16202, 16216 and the same plus 261; `col X` at x 15908, 15922, 15954, 15979, 15998 over
y 15980-16224 and y 16241-16485). In both:

- **The load.** Upper bar, a dark line of 6-8 px, the block, a line, the lower bar, down x 15908 and x 15922
  (group 2: bar y 16048-16058, block y 16068-16096, bar y 16106-16118): one poly over a strip, the look of
  run 4's loads. The strip leaves the VCC land without an edge line: on the strip's rows the clean shot is tan
  and plain from under the rail to the block's outline (`row 16072`, `16084`; `16333`, `16345`), and pink field
  with a dark line on the rows above and below (`row 16056`, `16168`; `16317`). Below the lower bar the framed
  cell (centre x 15924-15936, y 16132-16138 in group 2), 12-14 px of frame between it and the bar and between
  it and the wire: the tie, `?B` as before.
- **The arm, the wire and the way back.** Row y 16072 is diffusion without an edge line from the wire
  (x 15944) to the rail (both metal shots; green in the clean shot, tan under the rail); column x 15954 is
  diffusion without a line across from y 16068 to y 16204; row y 16202 is diffusion from x 15950 into the rail.
  So the node's two pieces under the rail are one net round the west side. Group 3: rows y 16333 and y 16463,
  the same. No poly lies on the wire at the height of bands S and T: the bands end in the pocket east of it
  (`tools/px.py row 16431 15940 15992 3`: the wire x 15952-15960 is 141-168/78-128/56-76, the band's end
  x 15975-15981 orange with blue under 50, dark between).
- **The pocket.** Between the wire and the stack (x 15968-15986) bands S and T end over field (column x 15979:
  orange y 16092-16110 and y 16162-16180, plain field y 16118-16154 between). The heavy closed outline seen
  there at low zoom is the wire's east edge, the bands' ends and the stack's west edge.
- **The contacts on poly.** `tools/tl5_tracks.py v` down each track of the bundle from y 15975 to y 16480
  (x 16169, 16210, 16255, 16298, 16340, 16385): a hole in the clean shot at each of the nine drawn contacts
  (15997 and 16086 on x 16210; 16128 on x 16255; 16042 and 16301 on x 16298; 16347 on x 16340; 16171 and 16432
  on x 16385; 16389 on x 16210) and nowhere else under metal; the `e_b` trunk has only edge bars of 8-14 px
  over the eight bands; no metal on x 16210 from y 16100 to y 16378 and on x 16340 below y 16354 in either
  chip, none on x 16255 above y 16126, on x 16298 above y 16036, on x 16385 above y 16166. The feed of group
  3's middle input is `rs_d`: one metal x 16211 from the hole at y 16389 to the hole at y 16606 on group 4's
  band (`v 16211 16370 16640`).
- **The link from band S to band U** (x 16066-16078): one poly from the band under the rail's edge down into
  the band that runs to the pad (salmon without a break under the rail's margin, `tools/bd2_umap.py`; orange in
  three shots x 16067-16076 from y 16094 to y 16121, `tools/bd2_cmap.py 16052 16046 16150 16146 3`; group 3 the
  same from y 16355 to y 16382).

### What it corrects (geometry; no connection)

- **The stack is wider on the west.** Its diffusion runs to an edge line at x 15984-15990, not to the rail's
  edge at x 16008: column x 15998 has the whole stack (output, S, ground, T, output, each line between them a
  single one of 4-5 px), rows y 16100 and y 16168 have the bands orange from x 15990 with the edge line across
  them, row y 16132 the ground land green in the clean shot at x 15996-16002. Bands S and T are 70 wide (were
  52). Group 3 the same.
- **The R/W input's pull-down is 64 wide, not 28: the stack's top runs east of the rail.** A heavy outline comes
  down x 16074-16080 from y 15980, steps east along y 16008-16012 and runs down x 16095-16100, across band R and
  on down the east end of the output's tab (view `r7_g2R`, the same in all four shots). Inside it band R is
  bright (`tools/px.py row 16040 16062 16112 3 all`: chip 2 174-182/131-140/55-64 at x 16074-16089, chip 1
  146-177/75-107) and east of the line across it ordinary open poly (159-163/87-109/51-58; 112-146/50-77): a
  channel, as run 4 read the bright part of its loads. Group 3 the same (`row 16301`; `tools/bd2_cmap.py 16056
  16241 16116 16293 2`). Run 3's units below have the same lobe, drawn (113/18).
- **Each output's boxed cell is 30 px east of where run 2 drew it.** The plain patch x 16068-16098,
  y 16058-16078 that run 2 took for the cell is the output diffusion's east end (the lobe's foot: chip 2's
  metal shot 175-180/128-142/82-94 on `row 16066`, blue over 80, where open poly has blue under 66); run 2's
  "poly round the foot of the cell" is that patch's pink and is withdrawn. The cell is the framed box east of
  it: a plain centre x 16107-16118, y 16076-16093 (158-172/102-144/76-86, the look of poly on bare silicon,
  trap 24) inside a dark frame of 8-10 px (x 16096-16130, y 16060-16099), with the band orange from x 16129
  (`row 16082`, `col 16111 16056 16104 3 all`; view `r7_g2cell`). Group 3: centre x 16108-16117, y 16338-16350
  (`row 16343`, `col 16111 16317 16365`). Drawn as the tab taken into the box, the band's end in it, and the
  `?B` on the box. The window is not resolved, as before.
- **Group 3's VCC contact** (15864,16352): a tall oval, bright centre x 15857-15869, y 16339-16369 in both
  metal shots, greenish in the clean shot, pitted in chip 2's stripped shot, the same as group 2's at
  y 16078-16102 (`tools/textmap.py 15842 16318 15896 16380 3 --acid` against `15842 16057 15896 16119`; view
  `r7_g3w`). Under the VCC rail the two groups differ only in the neighbours' lands (`sel`'s loads on the
  rail's other side: tan at y 16245-16297 and y 16409-16445 beside group 3, at y 16108-16140 beside group 2,
  where the land is one piece with group 2's and shares its oval).

### Ambiguities (run 7)

27. **A green patch between the pad (16210,16086) and band U** (x 16203-16224, y 16108-16119; the one group
    `tools/opendiff.py 15890 15980 16400 16475` lists as undrawn): 11 px between two poly edges, dim in both
    metal shots (120/112/66), red over green by 34 in chip 2's stripped shot, green in the clean shot; nothing
    reaches it. Read as the gap between two polys (tracing guide, trap 38), not a diffusion. Not drawn.
28. **The lobes east of the rail** are joined to the land under the rail on the clean shot's evidence
    (`tools/px.py row 16020 16044 16104 3 all`: tan 183-191/160-187/129-135 without a line from x 16050 to
    x 16068, then 6 px of the margin's boundary, not read, then the lobe in the open, dark red
    111-119/80-106/70-85 against khaki-green field east of the outline); in chip 2 the rail's own edge line
    lies across the join. That the lobe is diffusion rests on its outline, on band R's bright stretch inside it
    and on its colour against the field east of it (chip 2's metal shot 178-182/133-140 against 166/139; its
    stripped shot red over green by 8-34 against 2-4: the east half is at the low end of diffusion). If a lobe
    were not part of the land, R's pull-down under the rail (28 wide) would remain, and the equation with it.

### Not done (run 7)

- The strobe latch's own wiring west of the `e_b` trunk (x 16088-16150, y 15540-15990): the thin metal
  `wr_data_sel_n`, the hook cell on row 1's output, the undrawn boxed structure at (16088-16142, 15764-15798)
  (Ambiguities 2-4): unreviewed. Next.
- The boxed cells' windows (Ambiguity 1), here four: two load ties, two output cells.
- The column under the left rail below y 17400; east of the VCC rail x 16491-16538 south of y 15770.

## Review

Run 3 is the first piece of this block traced under the review rule (runs 1-2 predate it).

### Round 1 (full review), 2026-11-27, piece `g4n`

A fresh Claude Fable 5.2 agent, on commit 955655c, images in `cache/scratch/bd2/review-1/` (4.3-8.5x in four
shots, with profiles: `tools/px.py`, `tools/textmap.py`, `tools/bd2_umap.py`, `tools/follow.py`,
`tools/eof_tee.py`). Told to suspect: the loads west of the rail (one poly over one diffusion, or separate
polys; the strip between unit 1's and unit 2's blocks), each drain strip's way through its tie box into the
output land, the NOR's tie wire and the patch beside it, the contact on the `e_b` trunk, the tee and the
column in the gap between two metals, every crossing claimed to have no contact, the pad (16208,16733) and
the track x 16210 north of it, the NOR's east column, the VCC lands and their contacts.

Findings, none of which changes a connection (all confirmed by me and fixed):

1. **VCC contacts.** All four lands have a contact ring at x 15855-15870 in both metal shots, which the notes
   denied for unit 3 and the NOR, and the two contacts drawn were on clean-shot specks 12-20 px away.
   Confirmed (`cdp4_padc.py 15862,16586 15862,16724 15862,16886 15862,17024`: a hole of 356-516 px and both
   metal centres at each). Now four contacts at the rings. The lands were on `vcc` before and after.
2. **Ground contact of units 1-2** (run 2's `C 16041,16663`) reached to within 1 px of the new band y 16681;
   it is a tall oval about (16044,16652). Moved, 24 x 34.
3. **Ground lands.** Units 1-2: the land reaches x 16082 between the two arms (drawn to 16066): added. Unit 3:
   it narrows to x 16030-16066 below y 17070 (drawn full width): narrowed.
4. **The NOR cell's poly** ended 2 px into `cdp4`'s row: extended to x 16136.

Unexplained by the reviewer and by me: the dark patch under the rail (Ambiguity 13, not drawn).

Checked and found correct by the reviewer: the three load blocks are one poly each (single 8 px edge lines;
chip 2's stripped shot shows the poly unbroken down x 15912); the strip between the blocks is field; the
corridors into the output lands are diffusion to x 16004 with edge lines in line with the lands' edges; the
NOR's tie (the band's bottom edge open at x 15993, closed at x 15980; the patch field; the arm diffusion);
the four contacts (16166,17037), (16208,16733), (16296,16690), (16384,16821), and the `e_b` trunk one metal
through its pad; the track x 16210 bare ground at y 16632-16672 (the metal runs from the pad south only); the
tee and the column (unbroken y 16900-17131, field north of band 2, pink under x 16255 throughout); all listed
crossings; the NOR's east column one diffusion; nothing undrawn in the gaps between the tracks x 16190-16407.
Could not check: that the seven boxes are buried contacts beyond their look (Ambiguity 11); the 6 px under
the rail's edge line at each corridor-to-land join.

Connections before and after the fixes (commit 955655c against the fixed tree):

    tools/t.sh bd2 sameconn.py 955655c            ->  connections identical
    .venv/bin/python tools/sameconn.py 955655c    ->  connections identical

Recorded 2026-11-27 06:05 -0600.

Round 1: no findings that change a connection.

### Round 2 (full review), 2026-11-27, piece `rdg`

A fresh Claude Fable 5.2 agent, on commit 421ad7f, 19 images in `cache/scratch/bd2/review-2/` (to 6.4x, three
and four shots, with `tools/px.py`, `tools/textmap.py`, `tools/tl5_tracks.py`, `tools/eof_tee.py`). Told to
suspect: the wire W (diffusion along its whole length, joined at both ends) and the pocket beside it; whether
the middle and south lands are ground, so that the gate is a NOR; band B's route (one poly with the L, the L on
field, no contact to the `e_b` trunk, the pad on `cs_d`); band C's reach to the pad (16209,17212) and that pad
apart from the pad (16210,17300); the load's tie box, the branch into it and the patch; the output's route (one
metal, no contact, the grey spot at (16700-16712,17648), the two pads and the row between); how far east each
land goes.

Findings, neither of which changes a connection (both confirmed by me and fixed):

1. **Band D's channel, east end**: the south ground land has a lip east of the rail to x 16095 (y 17358-17372),
   so the diffusion's edge crosses band D at x 16096-16100, not x 16076. Confirmed (row y 17365 in chip 2's
   stripped shot: R-G +11..+32 at x 16072-16088, edge at x 16096-16100). Drawn to x 16095.
2. **The load's VCC land** runs north to about y 17255 and has a contact near (15868,17302). Confirmed (tan
   down x 15874 from y 17264; `cdp4_padc.py`: hole (15866,17300), ring in chip 2's metal shot). Land from
   y 17260, contact drawn at (15865,17302) under `bd3`'s rail; Ambiguity 15 closed.

Checked and found as drawn by the reviewer: W is diffusion along its whole length (chip 2's metal R-G 35-38
and stripped +14..+16 down x 15981 from y 17154 to y 17310, equal to the load band, against 20 and -3 for
field), with no edge line across it at either end; the pocket is field, with no poly between the caps of bands
B and C; both ground contacts have ring and bright centre in both metal shots, and L2 has none; band B is one
poly across a single 8 px edge line at x 16088, the L lies on field, the `e_b` trunk has no ring and no hole
over it, the pad (16384,17169) is on `cs_d`'s metal; band C's poly is continuous into the pad (16209,17212),
with bare ground in both chips between that pad and (16210,17300); bands A and D continuous to the column and
to the pad, the metal x 16255 ending on its pad; the tie box and the output cell have the buried contact's
look, the patch is field; the route is one metal with no break of 20 px in either chip and neither corner a
T, the smear at (16700-16712,17648) lies over field under bright metal with no ring, the far row and both pads
are as drawn and the metal runs on east past x 17145; no branch on any poly, no contact at any crossing.
Not checked by the reviewer: that the rail x 15795-15890 is VCC; where the port's metal goes; the clean shot's
green under the middle of the wide rail x 16940-17030 (read as field).

Connections before and after the fixes (commit 421ad7f against the fixed tree):

    tools/t.sh bd2 sameconn.py 421ad7f            ->  connections identical
    .venv/bin/python tools/sameconn.py 421ad7f    ->  connections identical

Recorded 2026-11-27 06:26 -0600.

Round 2: no findings that change a connection.

### Round 3 (full review), 2026-11-28, piece `gge`

One fresh reviewer (Claude Fable 5.2), on commit 3d7ebc37, images in `cache/scratch/bd2/review-3/` (14 views,
2.5x to 8x, four shots; mostly `tools/px.py`, `tools/textmap.py`, `tools/railprof.py`, `tools/follow.py`).
It was given the piece's nine claims and told to suspect: which way the diffusion runs under the block at
y 15472-15498 and whether T is on the ground land; the block's west cap; whether each load's bar, block and
band or pad are one poly; the two ties and any other driver of the two polys (the strap's crossings, the
band's west end, the pads' other sides); whether the strips reach the VCC land and their nodes; the arm's join
to the wire; the items left out (two green rings, a small cell, an olive strip, a poly piece); and, because
of Ambiguity 16, any wrong connection in the piece or where it joins the two stacks under the rail.

Findings, each checked by the tracer in the photos:

1. **The upper tie was drawn on a field pocket; the framed box is 30 px south**, at (16370-16404, 15598-15628).
   Confirmed (`tools/px.py pt 16388,15585`: stripped R-G -9, metal 175/157/83; `col 16388` and `row 15614`:
   the frame and its plain centre). The three `?` items redrawn there. Geometry only: the tie still joins
   `bd2_x` to `wr_data_e_n`, and stays uncertain.
2. **The band of `bd2_x`** steps 6 px north at x 16392 and ends in the west at x 16290, not x 16306.
   Confirmed (`tools/px.py col 16380`, `col 16410`, `row 15647 16282 16318 3`: orange at x 16294-16300).
   Redrawn. Geometry only; no driver at the west end.

Checked and found correct: T on the ground land (the land's east edge line at x 16357 is present at
y 15430/15440 and absent at y 15452/15456 in both metal shots; clean tan to x 16372), field east of T; the two
edge lines across the block, the cap as poly over field with 8 px of field to G_a's end; wire and arm one
plain area with no line across; the strap (constant width at the three crossings, no hole, `follow.py` ends
on both pads, nothing else leaves either pad); each line between a load's poly parts a single 6-8 px edge
with poly colour on both sides at x 16474; the land's west edge line (x 16495) absent only at the strips'
rows; the row from pad L ending at x 16392; the lower tie rightly uncertain; the left-out items field or
outline; the stacks under the rail as the trace has them. Not checked: the diffusion side of either tie
window; the identities of the stacks' inputs (earlier runs); anything south of y 15757. It found no wrong
connection behind Ambiguity 16 in this piece.

After the fixes (commit before them 3d7ebc37):

    tools/t.sh bd2 sameconn.py 3d7ebc37              connections identical
    .venv/bin/python tools/sameconn.py 3d7ebc37      connections identical

Round 3: no findings that change a connection.

### Round 4 (full review), 2026-11-28, piece `ggs`

One fresh reviewer (Claude Fable 5.2), on commit f15d5ae5, 15 images in `cache/scratch/bd2/review-4/` (to about
5x, four shots; mostly `tools/px.py`, `tools/textmap.py`, `tools/bd2_prof4.py`, `tools/tl5_tracks.py`,
`tools/cdp4_candh.py`, the extraction). It was given the piece's ten claims and told to suspect: the gap between
row 3's band and the pad (16274,15873), and anything else reaching that pad; the thin metal over the two boxed
cells (contact or pass-over) and its two ends; the output row under the rail (one poly, no contact, the smear);
whether the column is G_e's poly, where it ends, and whether it is a gate (the land against its west edge, the
edge lines across it, diffusion or field east of it); the load (one poly, the strip's two ends, the contacts,
the rail); the arm, the wire and what the box joins; anything undrawn in x 16366-16490, y 15757-15925 and under
the rail's south end.

Findings, each checked by the tracer in the photos; none changes a connection:

1. **The thin metal was drawn plain over both boxed cells.** The reviewer agrees there is no contact, but it
   is a reading, and trap 27 asks for `?M`. Confirmed; the two stretches are `?M` and the label is on G_a's
   pad. Marking only.
2. **The stacks' diffusion is wider than drawn** (runs 2-4's geometry): to x 16288 under G_a, G_b, G_d, G_e,
   with a tab of the south ground land. Confirmed (the section above). Two rectangles added. Widths only.
3. **A poly island at the west end of the cell at `wr_data_e_n`'s west arm** is not drawn. Confirmed as an
   island (Ambiguity 22); left undrawn. No connection.

Checked and found as drawn: x 16235-16252 bare field in all four shots on every row y 15836-15905, the band's
poly turning south under the metal x 16200-16222 with no contact, only the thin metal and the east row on the
pad; the boxes' centres 182-187/185/129-130 in the clean shot against holes of 160-181/176-195/101-109 at the
metal's two real contacts, and a pale pitted patch in chip 2's stripped shot at both contacts and at neither
box; the metal one piece (no gap of 25 px, `tools/tl5_tracks.py v 16274` / `16277`), ending on both pads, G_a's
pad on its band; the row one poly from pad to box with unbroken edge lines under the rail and no contact, the
smear without edge lines in either metal shot (the same grey lies under the VCC rail at (16506-16526, 15896));
the column continuous with G_e, its cap near y 15850 with pink field at (16370, 15852-15864) before the row,
the diffusion's edge lines (y 15802, 15841) across it in both metal shots and the land against it with no
edge line; the node diffusion and the area north of it field (stripped red minus green 14-23 against 1-5);
the load one poly, its strip reaching node and land, both contacts and the rail; the arm unbroken to y 15884,
the wire unbroken to the box with field south of it, the box plain between dark bands of 12 and 10 px; the
equations; the rail's end at y 15919. Not checked: the box's window (`?B` is the right marking, it said); the
cap's exact y; runs 1-2's other joins (box 2's `?B`, the `e_b` taps); east of the VCC rail.

After the fixes (commit before them f15d5ae5):

    tools/t.sh bd2 sameconn.py f15d5ae5              connections identical
    .venv/bin/python tools/sameconn.py f15d5ae5      connections identical

Recorded 2026-11-28 04:44 +0000.

Round 4: no findings that change a connection.

### Round 5 (full review), 2026-11-28, piece `ggw`

One fresh reviewer (Claude Fable 5.2), on commit 118fd0c0, images in `cache/scratch/bd2/review-5/` (views to
about 4x in three and four shots; mostly `tools/px.py`, `tools/textmap.py`, `tools/tl5_tracks.py`,
`tools/follow.py`, `tools/bd2_umap.py`, `tools/eof_tee.py`, the extraction). It was given the piece's nine
claims (the two metals on the track x 16169 and the break between them; `e_b`'s corner, pad and taps; strip 1
with its block and band; `e_b`'s branch, strip 2 and G_b; `ar_load_n`'s metal from G2's pad to the pad
(16205,15690), the bar and the cell; the other metal from (16207,15778) and G_e; G_d's row between the two
pads; the thin metal's three crossings; field between all of these) and told to suspect: the break (bare in
both chips, or a dim stretch of one metal); the join of the horizontal metal to the lower trunk; the metal
x 16200-16222 (one piece, a contact on any of the three polys under it, where it stops); the 12 px between the
block's foot and the pad and bar, and G_d's row against the two pads; each long poly end to end, strips 1 and 2
where both lie under one metal, a poly column in the gap between the metals, anything else leaving a pad; the
thin metal over G_d and G_e, which an automatic pad test calls pad-like; the bar, and the undrawn cell 135 px
north of it.

It reported **no findings**, and three remarks it called geometry only, each checked by the tracer:

1. **Strip 1's diagonal lies about 6 px south of where it was drawn in the gap between the two metals.**
   Confirmed: `tools/px.py col 16190 15514 15566 3 metal,metal1,acid` has the poly at y 15529-15551 between
   its two edge lines (centre y 15540; drawn centre y 15536, in a diagonal drawn steeper than it is), and
   `tools/bd2_umap.py 16156 15500 16228 15580 4 4` has it leave the trunk at y 15520-15532 and reach the metal
   x 16200-16222 at y 15540-15556. Redrawn (`P 16168,15440 y15518 16210,15560 y15612`). Geometry only: a path
   between the same two ends.
2. **The upper boxed cell (16243-16292, 15548-15576) is undrawn**, with a closed west end and an orange patch
   at x 16247-16254. Known (Ambiguity 22); the reviewer found field west, north and south of it in both chips
   and pink under the thin metal above and below it: no poly reaches it, and it is not joined to the block
   below. Left undrawn. No connection.
3. **The upper trunk is dark for 13 px (chip 2) over G2's band**, with no hole and no pad: an edge underneath.
   Nothing to change.

Checked and found as drawn: the break (y 15456-15465 orange in both chips like five open-poly controls nearby,
35 px without metal against 13-20 px at the other taps, `tools/follow.py --gap 16` from the north ending at
(16165,15438)); `e_b`'s corner (the dark line x 16154-16162 is 9 px and as deep as a known poly edge under the
same trunk, the clean shot's pink unbroken to strip 1's edge, a field pocket between the arm and the pad
above, the follower turning west and north to (16123,15388)); strip 1, the block and the band (salmon under
both metals, orange in the gap, the block one poly, the band orange to x 16126, no holes); the branch, strip 2
and G_b, with pink field between strips 1 and 2 under the metal at y 15512-15536 and no poly column in the gap
x 16182-16198 over its whole length; field all round every pad; the metal x 16200-16222 one piece from y 15300
to y 15690 (longest dark stretch 16 px, holes only at the two contacts), the bar reaching the cell and the arm
the rail; no metal y 15700-15775 in either chip and a new metal from (16207,15778); G_d's row continuous
x 16185-16260 with field on both sides; the thin metal over G_b, G_d and G_e (clean shot salmon, red minus
green 29-77, no ring, no widening, against the contact at (16274,15873)); the block's foot against the pad and
bar (field at x 16228-16252, y 15664-15676, pink under the metal) and against `bd2_x`'s band (field
x 16252-16288); `tools/eof_tee.py` on eleven poly stretches: no branches. Not checked: the `?B` window of the
lower cell and the `?M` stretches (excluded by the brief; it notes that `tools/tl5_tracks.py` reads the clean
shot green over both cells, -16 and -17, as over the real contact, -11: Ambiguity 22 stands as a reading);
poly continuity across the 6-8 px edge lines at metal edges, which is inferred; anything west of x 16118 or
east of x 16312.

After the fix (commit before it 118fd0c0):

    tools/t.sh bd2 sameconn.py 118fd0c0              connections identical
    .venv/bin/python tools/sameconn.py 118fd0c0      connections identical

Recorded 2026-11-28 05:17 +0000.

Round 5: no findings that change a connection.
