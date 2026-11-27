# bd2: bus control logic right of the register select gates

Region x 15850-17000, y 14700-17100. Trace: `trace/bd2.txt` (`@requires sel`, `areg`, `bd3`).
Extracts with 0 errors, 0 warnings. Three runs; this file was rewritten by the second, and the third
(2026-11-27: the column from group 4 down to `dbus_le`'s driver) has its own section, "Run 3", below.

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
- **Pull-downs traced, loads not**: the two gates of the gate group right of the bundle
  (`wr_data_e_n`, `ar_load_n`) and the `rs_d` inverter at the top of group 4 (`bd2_rs_n`).
- **Three results of the first run are corrected**: `ar_load` is not `NOT e_b` (G2's
  gate is a separate net, `ar_load_n`); row 1 has a third pull-down and a load; the metal
  at x 16210 is two wires (a second break, at y 15968-15988).
- **Not traced**: the source of `bd2_x`, the column below y 17110, the right-hand column. See Not done.
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
    ar_load = NOT ar_load_n                                 G2          traced
    ar_load_n  = NOT( bd2_x OR (e_b AND wr_addr_sel) )           gate group  pull-downs traced; load not, tie to G2 inferred
    wr_addr_sel  = NOR( rw_d, rs_d, cs_d )                      group 3     traced (by the pattern of group 2 west of the rail)
    wr_data_e_n    = NOT( wr_data_sel AND e_b )                         gate group  pull-downs traced; load and destination not

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
- `ar_load = bd2_x OR (e_b AND wr_addr_sel)`: the address register is loaded while E is
  high in a write to it, or when `bd2_x` (not traced) is high.

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
| Gate group right of the bundle | x 16240-16480, y 15400-15850 | pull-downs traced, loads not |
| Group 2 (`wr_data_sel`, NOR of R/W, NOT RS, CS) | 15890-16400 x 15985-16210 | traced |
| Group 3 (`wr_addr_sel`, NOR of R/W, RS, CS) | 15890-16400 x 16245-16470 | traced, west part by the pattern of group 2 |
| Group 4, first gate (`bd2_rs_n` = NOT `rs_d`) | 15850-16360 x 16529-16680 | traced (load: run 3) |
| `bd2_rw_n` = NOT `rw_d` | 15850-16312 x 16654-16765 | traced (run 3) |
| `dbus_le` = NOR(`cs_d`, `bd2_e_n`) | 15850-16400 x 16760-16965 | traced (run 3) |
| `bd2_e_n` = NOT `e_b` | 15850-16244 x 16962-17110 | traced (run 3) |
| Left column below y 17110 | x 15890-16260, y 17110 on (the rail runs on south past the region's edge) | not traced |
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

Diffusion column x 16312-16366 under the ground rail x 16312-16362
(`bd2_umap.py 16250 15404 16384 15850`).

- Upper gate, `wr_data_e_n = NOT( wr_data_sel AND e_b )`: ground land y 15422-15461 (contact
  16338,15432); band G_a y 15466-15488, gate `wr_data_sel` (pad and contact 16260,15473 at its
  west end); node; band G_b y 15509-15531, gate `e_b` (strip 2); `wr_data_e_n` y 15533-15565,
  widening east to x 16374. Boxed cell at its west end (16246-16296 x 15552-15572, three
  plain cells) with no poly leaving it. Load and destination not traced (east).
- Lower gate, `ar_load_n = NOT( bd2_x OR (e_b AND wr_addr_sel) )`: ground land y 15596-15635
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
| 16210 | 16723-17745 | `bd2_rw_n` (run 3): from the pad (16208,16733) of the `rw_d` inverter's output south; not followed below y 17100 |
| 16255 | 16118-17300+ | `bd2_rs_n`: contact 16252,16128 (band S of group 2), contact 16255,16562 (group 4's output band), on south |
| 16255 | 15947-15983 | this is the bar of `wr_addr_sel` crossing the track |
| 16277 | 15466-15872 | `wr_data_sel`: contact 16260,15473 (G_a) to contact 16274,15872 (row 3's lower band) |
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
| `bd2_rs_n` | metal | x 16255, y 17100 | driven here (group 4) | NOT `rs_d`; runs on south, destination unknown |
| `bd2_rw_n` | metal | x 16210, y 17100 | driven here (run 3) | NOT `rw_d`; runs on south (track scan: to y 17745), not followed |
| `dbus_le` | poly | x 16130, y 16865 (inside the region) | driven here (run 3) | the NOR's output cell; `cdp4`'s row leaves it east to the pad (16426,16864) |
| `bd2_e_n` | poly | x 16235, y 17110 (the region's south edge is y 17100) | driven here (run 3) | NOT `e_b`: the column x 16226-16244 goes on into the band y 17115-17130, a gate of the next unit south |
| `bd2_x` | poly | x 16376, y 15647 (inside the region) | from the untraced part | band arriving from the east; second term of `ar_load` |
| `wr_data_e_n` | diffusion | x 16374, y 15555 (inside the region) | driven here | goes east, not followed |
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
6. **Group 3 west of the rail** is drawn from group 2's shapes shifted by 261 px on the
   strength of the character maps and one overlay; its VCC land has no contact drawn
   (labelled `vcc`).
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

- **`bd2_x`** (second term of the address register strobe): band y 15638-15656 of the
  gate group, arriving from x 16376 east. Not followed.
- **Loads of `wr_data_e_n` and `ar_load_n`** and where `wr_data_e_n` goes (east of the gate
  group's rail, x 16370-16480; seen in one 3x view, `gg4.png`: a poly bar 16395-16483 x
  15475-15498 turning down at x 16465-16483, contact 16450,15539 with a thin metal
  x 16444-16459 down to contact 16450,15740, the wide vertical x 16489-16547).
- **The column below y 17110** (run 3 traced group 4 and the column down to there: see its Not done);
  `cs_d`'s tap at about y 17170; where `bd2_rs_n` and `bd2_rw_n` go south of y 17100.
- **Right-hand column** (x 16480-16800, y 14700-16450) and the routing east and south of
  it: not looked at. `dl7_q_n`, `dl6_q_n`, and probably `bd2_x`, `wr_data_e_n` go there.

## Where `wr_data_e_n` goes: looked at 2026-11-16, not resolved

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

Where `bd2_rw_n` goes is not followed: its metal x 16210 runs south from its pad (16208,16733) (run 1's track
scan: to y 17745). `bd2_e_n` has a second load: its poly column ends on the band y 17115-17130, a gate of the
next unit south under the rail (not drawn).

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

- The next unit south (band y 17115-17130, gate `bd2_e_n`; ground land shared with unit 3) and the rest of
  the column to the rail's end: bands at y 17175-17190, 17245-17260, 17335-17345 and on (`bd2_umap.py 15990
  17000 16150 17460 4 5`), with `cs_d`'s second tap (16385,17170), a pad (16210,17300), `bd2_rs_n`'s contact
  at about (16258,17340). Partly in `busc`'s region.
- `bd2_rw_n`'s metal x 16210 south of y 17100.
- The rail's south end; the supply rail's contacts west of x 15850.

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
