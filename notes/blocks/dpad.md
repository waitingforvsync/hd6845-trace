# Data pad cells D0-D7 (`dpad`)

Region: x 17640-19150, y 5950-19150 (the eight pads down the right side, D0 at the top).
Trace: `trace/dpad.txt`. Scratch images: `cache/scratch/dpad/` (names in brackets below).

## Status

2026-11-17 16:10 +0000. The second review cycle's round 1 (after the series strip was drawn) is clean: no findings. Traced and extracting (full extraction 2143 nets, 3701 transistors, 0 errors, 0 warnings):

- the output cell `dpad_cell` (output fingers, extra pull-down fingers, the two-NOR
  pre-driver under the VCC band, the two straps), master D0, placed on D1-D7, each copy
  checked on its own;
- `d_hiz` (the "P_x" of the first notes), drawn end to end through all eight cells;
- the input protection clamp `dpad_prot` on D0-D6, the VSS rail beside it, and the
  input lines of D0 and D1 joined to `dbus`'s input buffers;
- the bond pad's metal, its contact box and **the pad's series strip** (a diffused
  resistor from the pad to the protection node), drawn per copy for D0-D6, so that the
  protection node and the input line are the pad's own net `d#` (`d0_in`, `d1_in` and
  the lines from the protection nodes to the input buffers are drawn in `trace/dbus.txt`, `d2_in`..`d6_in`); D7's strip as far as its
  untraced protection.

AMB-003 is settled (see Logic). Not traced: the comb inside the protection, D7's
protection, the input lines of D2-D7, the `d#_out_n` lines outside the cells (they are
`dbus`'s channel wiring).

Instance offsets from D0 (tag = pin):

| | D0 | D1 | D2 | D3 | D4 | D5 | D6 | D7 |
|---|---|---|---|---|---|---|---|---|
| `dpad_cell` | 0,0 | 0,1735 | 1,3470 | 1,5054 | 2,6637 | 2,8242 | 2,9847 | 3,11452 |
| `dpad_prot` | 0,0 | 0,1736 | 1,3469 | 1,5118 | 2,6723 | 2,8306 | 3,9911 | not placed |

The protection sits 0-86 px lower relative to the output cell from D3 on, which is why
it is a cell of its own (and why a composite made with the output cell's offsets is
doubled there).

## Inventory (D0 coordinates)

| What | Where |
|---|---|
| VCC band (metal) | x 17900-18200, the whole height |
| Finger stack: rows A vcc 6733-6787, B pad 6808-6862, C vss 6883-6937, D pad 6958-7012, E vcc 7033-7087, F pad 7108-7155 | diffusion 17897-19040 x 6733-7155, one block; gates g1 6787-6808, g2 6862-6883, g3 6937-6958, g4 7012-7033, g5 7087-7108 |
| Extra pull-down fingers: G' vss 7185-7242, H' pad 7262-7318, I' vss 7340-7390 | diffusion 18742-19037 x 7155-7390, continuous with row F; gates gr1 7165-7185, gr2 7242-7262, gr3 7318-7340 joined by the poly bar 18690-18732 x 7168-7340 |
| Field strip between row F and the pre-driver | y 7155-7175, x 17897-18740 (green in acid1b under the band and in the gap between the F and G metals; no poly) |
| Pre-driver, under the band | loads U' 17957-18085 x 7225-7262 and L' 17957-18085 x 7318-7355 with the VCC pocket between them (three contacts, y 7292); field bars 17937-17957 x 7215-7368 and 18085-18107 x 7255-7368, field box 18085-18195 x 7215-7258 |
| Pre-driver, right of the band | rows G 7175-7228 (11 contacts), H 7250-7302 (8), I 7322-7378 (3), J 7400-7452 (5), K 7492-7540 (3), x 18195-18665 at most |
| Pull-up strap (metal) | x 17861-17881, y 6790-7522; contacts 17860,6797 (g1), 17860,7040 and 7080 (g4, g5), 17862,7208 (pu tab), 17857,7514 (pu tab) |
| Pull-down strap (metal) | x 17804-17822, y 6925-7350; contacts 17818,6937 (g2, g3), 17815,7335 (pd tab) |
| `d_hiz` contact | 17637,7385 in every cell; poly east along y 7375-7398 |
| Input protection | 17685-17960 x 6060-6550 (D0); rail x 17690-17765 |
| Bond pad (metal), the same in every cell | square 18515-19024 x 6049-6558; west tab 18363-18515 x 6374-6558 running on over the contact box; neck 18840-19024 down to row B |
| Series strip's contact box | diffusion 18272-18360 x 6478-6565, contact 18307,6523 (in the cell) |
| Series strip (diffusion, about 22 px between its edge lines) | per pad, see the table under Input protection |

## Logic

### The cell's gates (traced; all sixteen equations are FIRM in `tools/unsure.py --equations`)

    d#_pu = NOR(d_hiz, d#_out_n)        gate of the pull-up fingers
    d#_pd = NOR(d_hiz, d#_pu)           gate of the pull-down fingers

    pin D# = high through the pull-ups when d#_pu is high, low through the pull-downs
             when d#_pd is high, floating when both are low.

So: `d_hiz` high gives `d#_pu` = `d#_pd` = 0, the pin floats (the tri-state check of
AMB-003 holds); `d_hiz` low gives `d#_pu` = NOT `d#_out_n`, `d#_pd` = `d#_out_n`, and
the pin is the inverse of `d#_out_n`.

Transistors of one cell (14), as extracted for D0:

| Transistor | Gate | Between | Where | W/L |
|---|---|---|---|---|
| load U' | `d0_pu` (buried contact 17905-17939 x 7222-7253 at its left end) | vcc pocket, `d0_pu` | 17957-18085 x 7225-7262 | 128/37 |
| load L' | `d0_pd` (buried contact 17905-17939 x 7315-7358) | vcc pocket, `d0_pd` | 17957-18085 x 7318-7355 | 128/37 |
| strip 1 | `d_hiz` | `d0_pu` (row G), vss (row H) | y 7228-7250, x 18195-18630 | 435/22 |
| strip 4 | `d0_out_n` | `d0_pu` (row K, under the band y 7492-7540, tab 17840-17900), vss (row J, under the band y 7430-7466) | y 7466-7492, x 17840-18365 | 525/26 |
| strip 2 | `d0_pu` (the poly of U' continued: down x 18143-18163, east along y 7302-7322) | `d0_pd` (row I and the region west of the vertical piece), vss (row H) | to x 18597 | 494/20 |
| strip 3 and its piece under the band | `d_hiz` | `d0_pd` (row I, under the band y 7368-7405), vss (row J, under the band y 7430-7466) | y 7378-7400 east of x 18200, y 7405-7430 under the band | 581/23 |
| g1, g4, g5 | `d0_pu` | vcc (rows A, E), `d0` (rows B, D, F) | three fingers | 1143/21 each |
| g2, g3 | `d0_pd` | `d0` (rows B, D), vss (row C) | two fingers | 1143/21 each |
| gr1, gr2, gr3 | `d0_pd` | `d0` (rows F, H'), vss (rows G', I') | three fingers | 295/20 each |

How the nodes are made up:

- **`d#_pu`** = the diffusion under the band at y 7175-7215 (it runs east into row G
  without a break) + row K and the diffusion under the band at y 7492-7540 (joined to
  row G by the metal x 18225-18250) + the two tabs west of the band that the pull-up
  strap contacts + the poly of U' and strip 2.
- **`d#_pd`** = the diffusion under the band at y 7368-7405 + the region between the
  right field bar and strip 2's vertical piece + row I + the tab 17800-17900 x
  7310-7360 that the pull-down strap contacts + the poly of L'. Row I's metal goes
  east and up the column x 18685-18722 to three contacts on the poly bar of the extra
  fingers.
- **vss** = rows H and J (their metals are joined at x 18270-18300; J's metal leaves
  east as a wide line to the ring) + the diffusion under the band at y 7430-7466 and
  its tab 17840-17900 x 7445-7466.
- `d_hiz` poly: in from the contact along y 7375-7398, a wider piece under the pull-up
  strap (no contact: the strap is plain 18 px metal over it in the metal shot), under
  the band along y 7405-7430, up a diagonal at x 18160-18200 to strip 3, round the east
  end of row H (x 18635-18655) and back west as strip 1 to x 18183.

### What the earlier readings got wrong (AMB-003)

- Rows G and K were taken for VCC. No metal joins them to the band (a 20 px gap at x
  18205-18225 from y 7160 to 7545 in the eight-copy metal composite and in each copy
  [c2m, Rm_all, RR7]); the diffusion of the pull-up node runs into row G; and the load
  U' has its buried contact on that node. They are the pull-up gate node.
- Row H was read as tied to `d_hiz` by a buried contact at 18597-18632 x 7250-7298.
  That box is the end of row H's diffusion showing bright green where no metal covers it
  (H's metal ends at x 18592); the `d_hiz` poly passes east of it (x 18635-18655) and
  in the chip-2 shot the box is plain diffusion with no poly on it [z_b1]. Row H's metal
  joins row J's at x 18270-18300: VSS.
- The two "closed green shapes" under the band are field: they end the channels of the
  two loads on both sides, and the box is where U' and strip 1 end. With them as field,
  U' and L' are two separate loads sharing the VCC pocket.
- "Gate 7170" below row F does not exist: y 7155-7175 is a field strip (green, not
  salmon, in acid1b; plain, not granular orange, in the chip-2 shot) [z_c, z_d, z_e].
- The "small buried contact at 17835-17858 x 7440-7460" is the corner of the vss tab
  showing through where the strap's metal does not cover it: a green dot with a dark rim
  in acid1b in every copy, nothing but the box corner in the chip-2 shot [m_small].
- The end of strip 4 (18355-18387 x 7455-7500) is not a buried contact either: the
  poly simply ends 17 px past the diffusion edge at x 18365 [z_a].

### Traced and believed

Traced: everything in the table above, in the composite and in each copy.

Not seen directly, but drawn firm (so `tools/unsure.py --equations` reports FIRM for them):
the evidence below was re-checked by review round 1 at 4.5x in three shots, which found the
bars sit exactly in the metal gaps, vanish over poly, and are absent in rows A and E where
the metal is continuous: the signature of a metal-gap artefact (guide trap 2), not of a
diffusion break. If a later reading disproves one of them, the item becomes `?D`:

- That the diffusion is continuous where a metal gap leaves a dark bar across it in
  acid1b (trap 2): at the band's west edge x 17890-17900 (the three tabs) and at x
  18205-18222 and 18250-18262 (rows G to K). At x 18232, under the G-K metal, the
  colour is the diffusion's tan without a step from y 7404 to 7464, so row J and the
  vss strip under the band are one region; the tabs' top and bottom edges run straight
  on into the band in the chip-2 composite [z_f, z_g]. The pull-down strap reaches its
  node only through the tab 17800-17900 x 7310-7360, so that one matters; the pull-up
  strap has two tabs and the G-K metal.
- Between row J's metal and row K's (y 7452-7462, x 18262-18365) the dark bar hides
  whether the diffusion is continuous there. It changes only the width of strip 4's
  channel.
- Which rail is VCC and which VSS comes from the loads and pull-downs, as elsewhere.

## Input protection (traced except the comb and D7)

Traced (cell `dpad_prot`, D0 coordinates): one diffusion with the rail side (x
17685-17775, nine contacts at x 17705 to the rail metal), the clamp gate (the frame's
left arm, poly x 17778-17808) and the node (x 17810-17868, nine contacts at x 17830 to
a metal column that leaves south). The frame (the clamp's gate) is tied to VSS (below), so
the clamp is a thin-oxide grounded-gate transistor between vss and the pad net `d#`, W/L
397/30, gate vss (annotated `kind=clamp`: off in normal operation).

The rail x 17690-17765 is VSS: it is metal-continuous with `dbus`'s VSS rail (x
17355-17400) through the trunk at y 6625-6708 [rail, o3], and a metal test along it
finds no gap from y 6068 to 18080 other than contact rings.

Seen and NOT drawn (composite with the protection's own offsets, `--comp dpadp`
[pr1, pt]):

- The frame: left arm, top arm y 6058-6098, right arm x 17920-17955 down to y 6515
  (drawn as plain poly). The big diffusion's outline runs to x 17938 and up to y 6080,
  under the arms.
- A comb at x 17868-17920, y 6105-6500: about ten poly fingers alternating with
  U-shaped outlined bars, over the node's east part. In `inprot` the same shape was
  taken for buried contacts tying the frame to the node (AMB-005).
- A poly strip x 17978-17995 from above y 6040 down to y 6500, joined to the foot of the
  right arm at y 6495-6515; field (green) between it and the arm.

(The two strips first listed here as "a poly strip along y 6530-6548" and "from the bond
pad ... not followed further" are one diffusion strip, the pad's series strip: below.)

**The frame is tied to VSS** (review round 2, confirmed in the photos by the tracer): its
right arm and the outer strip x 17978-17995 join in a U at the foot (y 6490-6512, acid1b
4.5x, `chk_foot.png`); the strip runs up to y 5985 and west along y 5975-5995 to a contact
on the rail at (17727,6000) (ring in metal, green patch in acid1b, `chk_prot0.png`; the
reviewer saw the same in all seven copies, D1 at 3.7-5x); in D0 a 20 px metal stub joins
it to the rail's top. Drawn in the cell. So the clamp is off in normal operation, as a
grounded-gate clamp. The rail contact and its poly pad are drawn per copy: in D0 the pad
hangs below the top run (contact 17727,6002, with the metal stub); in D1-D6 the pad is in
line with the run and the contact is at y 5978 in cell coordinates, under the rail's own
metal (metal and acid1b at 3.2x, all seven, `s_rc.png`).

### The pad's series strip (drawn)

How the pad reaches the node: the bond pad's metal has a tab west to a contact box
(the same place in every output cell), and from the box one narrow diffusion strip runs
round a loop, east of the VCC band and under it, to the neck of the protection node. It
is the input's series resistor; the output fingers are on the pad's metal directly. The
route differs from pad to pad, so the strips are drawn outside the cells (absolute
coordinates of the strip's centre line; width 20 drawn, about 22 between the edge lines):

| Pad | From the box, north along x | West along y | South along x | West along y, to the neck | Bottom run relative to D0's |
|---|---|---|---|---|---|
| D0 | 18318 | 6065 | 18080 | 6541 | 0 |
| D1 | 18318 | 7801 | 18080 | 8278 | 0 |
| D2 | 18319 | 9578 | 18081 | 10055 | 44 lower; neck drawn longer |
| D3 | 18320 | 11140 | 18081 | 11660 | 0 |
| D4 | 18321 | 12744 | 18082 | 13266 | 0 |
| D5 | 18321 | 14350 | 18082 | 14848 | 0 |
| D6 | 18322 | 15955 | 18082 | 16476 | 23 lower; neck drawn longer |
| D7 | box, west along y 17971 to x 18084, north to y 17776, east to x 18322, north to y 17538, west | | | drawn to x 17920; it goes on to about x 17850 and into the top of D7's protection, which is not traced | |

The loop's height differs (the top run is 476-522 px above the bottom run), so the
resistors are not all the same length.

Evidence (images in `cache/scratch/dpad/`):

- **It is diffusion, not poly.** In the open its middle is green in `acid1b`
  (115/154/90 at 17885,6541) where open poly beside it (the D0 input line at 17795,6586) is
  red-brown (136/106/74); in both chip-2 shots it is brighter and pinker than field where
  poly is darker and orange (`metal` 182/130/84 against 162/112/55, `acid` 190/150/96
  against 166/124/66). Under the band its colour is the node diffusion's tan
  (174/149/119 against 182/165/120 for the node under its metal column), not the salmon of
  the frame's outer poly strip beside it (209/147/102). The outline is unbroken where it
  passes under the band's edges [s_d0_b 1.8x, s_d0_sw 4x in three shots, s_foot_b 3x all
  seven].
- **Position.** Both edge lines of every leg were found in `acid1b` at six points per leg
  (`strip_meas.py` in the scratch folder); the centres agree within 2 px along a leg.
  Overlays of all eight at 0.93x [ov_01, ov_23, ov_45, ov_67].
- **It crosses no poly and touches nothing else.** The nearest poly is the foot of the
  frame's U, 12-19 px of field north of the bottom run in every copy [s_foot_b]; the
  rest of the strip lies east of x 18069, 74 px or more from the frame's outer strip.
  No transistor appears in the extraction (3701 before and after), and the only nets
  that changed are the seven protection nodes, now `d0`..`d6`.
- **The pad end.** The box is tan in `acid1b` with one pitted contact, and a ring in both
  metal shots, in all eight cells [s_box_b, s_box_m]. The pad's tab runs on over it: the
  8 px dark line at x 18356-18364 is the box's edge printing through, with bright metal
  on both sides in both metal shots (profiles in D1 and D4). The pad's outline was
  measured with a metal test along six columns and five rows in every copy and both metal
  shots; the bond ball hides the middle [ovp_04].
- **The node end** (the one inferred join). Along the east edge of the node's metal column
  there is a dark line 5-8 px wide between the neck (tan, under the metal) and the strip
  (green, in the open) in every copy. Read as the metal-edge artefact (guide trap 2), not
  a break, because: the strip's lower edge line runs straight on as the neck's bottom
  edge in all seven copies; in D2 and D6, where the strip arrives 44 and 23 px lower, the
  neck is longer by exactly as much; 5-8 px is too narrow for two diffusion edges with
  field between them; and the same line runs on along the whole metal edge above and
  below the strip [s_neck_b 4x acid1b, s_neck_ma 6x metal and acid]. Drawn firm.

## Ports

| Name | Layer | Where | Direction | What |
|---|---|---|---|---|
| `d#` | metal | the bond pad 18515-19024 x 6049-6558 + cell offset | pad | pad metal, contact box and series strip drawn; D0-D6: the same net as the protection node and the input line |
| `d_hiz` | metal x 17631-17651 | y 7374-18850; contact 17637,7385 + cell offset in each cell; poly cross-under 17633-17655 x 18128-18304 between contacts 17643,18143 and 17643,18290 | into the cells | driver not found: `follow.py` reports contact candidates along it at y 9290-9573, 11168, 14500, 14798, 16754, 16827, none looked at |
| `d0_out_n` | poly, then metal | cell, west along y 7480-7505 to the contact 17597,7492, metal x 17589-17609 south (drawn to y 7570) | into the cell | `dbus` notes: continues to 17597,8097 |
| `d1_out_n` .. `d7_out_n` | poly | west end of strip 4 at 17800,7466-7492 + cell offset | into the cell | routes differ per pad; D0-D5's are drawn in `trace/dbus.txt` (D1-D5's to end pads at the column's west edge); D6's goes west to a pad (17600,17340) and south by metal, D7's north up the channel (`busC`). In every cell the poly at strip 4's west end is a block about 15 px lower than the cell draws it (geometry only) |
| `d0` (alias `d0_in`) | metal, poly, metal | node column, contact 17835,6585, poly west along y 6573-6597 and south along x 17550-17572, contact 17555,6755, metal x 17548-17566 to `dbus`'s piece at y 8050 | out | joined: `dbus`'s input buffer reads `d0_a = NOT d0` |
| `d1` (alias `d1_in`) | metal | node column to the contact 17836,8402, where `dbus`'s poly starts | out | joined: `d1_a = NOT d1` |
| `d2` .. `d6` (the lines on to the input buffers drawn by `dbus` as `d2_in`..`d6_in`; node contacts (17837,10141), (17838,11727), (17838,13329), (17835,14887), (17838,16519)) | metal | node column, drawn to y 6560 + protection offset; in the composite the contact is near 17825,6665 + offset with poly leaving west | out | the line to `dbus`'s input buffer is not followed: that is what the `_u` aliases stand for |
| `d7` | diffusion | the series strip's end at 17920,17538 | out | goes on into D7's untraced protection |

## Ambiguities

- The protection's comb (poly fingers hanging from the frame's right arm over the node's
  east part): not drawn. Related to AMB-005 (the frame is now known to be tied to VSS).
- The series strip's join to the node's neck is hidden by a 5-8 px dark line along the
  metal column's edge in every copy; drawn firm on the evidence listed under "The pad's
  series strip". If it were a break, the pad would not reach the input at all.
- Pad and node are one net in the netlist; on the chip a diffused resistor (about 60
  squares: some 1,400 px of a 22 px strip) lies between them. The extraction has no
  resistors.
- D7's protection (x 17685-17960, y 17540-18030) is not the same layout: its frame is
  closed along the bottom and no neck leaves south [P_all, last tile]. Not traced.
- Whether the pull-up fingers are enhancement devices cannot be seen (AMB-002).

## Not done

- The pad's series strip is drawn (D0-D6 to the node, D7 to its protection's edge) and
  reviewed (second cycle, round 1).
- D7's strip west of x 17920: it continues west to a neck at x ~17838-17858 that runs
  south into D7's protection node (seen by the second cycle's reviewer); not drawn.
- Protection: the comb; D7's variant (its strip enters from the top near 17850,17538).
- Input line of D7 from its protection to the column (D2-D6's are drawn by `dbus`, 2026-11-17).
- `d#_out_n` outside the cells (D0's is drawn: `dbus`, from the contact (17597,7492) down the channel to the inverter `d0_out_n` = NOT `dbus_do0_in`) and the driver of `d_hiz`: `dbus`'s channel wiring. Lead (review round 1, confirmed): at (17630,17085) a metal leaves `d_hiz` west along y 17073-17095 to x 17355 and turns south along x 17350-17370 past y 17237 (`metal` at 2.4-3x): almost certainly its feed. It lies in `dbus`'s claimed region, so it is not drawn here.
- The straps' metal was checked per copy only at 0.42x [U_a, U_b]; the rows' metal of
  D1-D6 at 1.05x [Rm_all], D7 at 1.5x.

## Review

Round 1 (2026-11-17 15:18 +0000, a fresh agent briefed with `/trace6845`'s reviewer text; told to suspect
the diffusion continuity across the dark gap bars, row F to gr1 to G', each copy's strap and
row metal, the `d_hiz` cross-under ends and D0's exit contacts; checked those at 4-5x in
three shots, the pre-driver, the extra fingers, the straps and contacts in all eight
copies, the joins and the `d_hiz` line). No wrong connection. Findings, each checked by the
tracer in the photos: (1) an undrawn metal branch of `d_hiz` at (17630,17085) going west
and south: confirmed; it is in `dbus`'s claimed region, so it is recorded under Not done
as a lead, not drawn; (2) the VSS rail x 17690-17765 runs on past D7: confirmed, drawn to
y 18850; (3) row J's metal runs on to x ~18812 and merges north into I': confirmed for
the extension (drawn), the merge left undrawn (both are `vss`); (4) believed continuities
drawn firm: the notes now say why.

Round 2 (2026-11-17 15:32 +0000, a fresh agent briefed with the skill's text; told to suspect the copies D1-D7
in the clean shot at 3x, the protection copies' placement, the pre-driver in two copies
other than D0, L' and its tie, the cross-under and the rail around y 18100-18350; checked
each copy's pre-driver at 3x with overlay, the metal gaps in all eight copies in both metal
shots, straps and finger stacks, the pd tab, row H's end, the protection copies, the joins
and the follower's candidates on `d_hiz`). One finding, which changes a connection: the
clamp gate (the frame) is tied to VSS by an outer strip and a rail contact in all seven
copies. Confirmed by the tracer at 1.9x and 4.5x (`chk_prot0.png`, `chk_foot.png`): drawn
in the cell; `d#_prot_g` is gone (merged into `vss`, 7 nets fewer). Could not be checked:
whether the two load-gate boxes are buried contacts (accepted from acid1b), D0's metal under
the bond-wire shadow, D7's protection.

Round 3 (2026-11-17 15:41 +0000, a fresh agent; told to suspect the new frame-to-VSS path in each copy, the
load-gate boxes, D0's metal under the bond-wire shadow and the protection's inside). No
wrong connection in the drawn geometry (frame-to-VSS confirmed in all seven copies at
3-4.5x; U' and L' gate boxes read as buried contacts; extraction unchanged). Findings,
checked by the tracer:
- **The pad's series strip is diffusion and runs to the node: confirmed** (`acid1b` 2.1x,
  `review-3/series0.png`: one outlined strip from the pad box 18265-18355 x 6475-6560 north
  along x ~18300-18315, west along y ~6060-6075, south along x ~18065-18085, west along
  y 6530-6548 to the node's neck at x ~17850; colour in the open diffusion-green, not poly).
  The notes had it as a poly ending at the neck and as "not followed". It is the pad-to-node
  path and is **not drawn**: see Not done 1.
- The rail contact in copies D1-D6 sits at about y 5978 (master coordinates), drawn at 6000
  as in D0: it still overlaps; not changed.
- The clamp is a thin-oxide grounded-gate device (the diffusion's top edge shows under the
  top arm at y 6080-6086; no internal edge in the left arm): the `kind=field` annotation
  in the cell is wrong in name only.

Round 3 is the last round the project allows; it had a confirmed finding (the omission
above), so this package is not ready to merge: it waits for the series strip to be drawn
and reviewed.

Second cycle, round 1 (full review, 2026-11-17 16:10 +0000, a fresh agent on claude-fable-5-2, before commit 1741a5d): told to
suspect the strip-to-neck join in every copy, the strip's corners and top run under the VCC
band, the pad metal across the contact box's east edge, D7's strip, and the frame's rail
contacts. It checked those at 2.2-4.6x in acid1b, acid, metal and metal1 with row profiles
in all seven copies (the neck's east side has no diffusion edge; the strip under the band
matches the neck's colour, not the poly's), the corners and legs, the pad metal in all
eight copies, D7's strip (it continues west to a neck at x ~17838-17858 that runs south
into the node), the frame rail contacts in all seven copies, `d_hiz` (follower unbroken;
cross-under symmetric), the VSS rail and VCC band (metal test), D0's input line, the cell
copies by overlay, and the extraction (2143 nets, 3701 transistors, 0 errors; no net joined
only through uncertain items). Two cosmetic offsets, no connection change, left as drawn:
the frame's top run is about 8 px lower in the photo (y 5967-5989 in D0) than drawn
(5975-5995), still overlapping by about 14 px; the VCC band's west edge is at about
x 17925, drawn at 17900, with no contact in the extra 25 px. Not checked: the pre-driver
above 0.76x (covered by the first cycle), D1's input join, D0's pad metal under the
bond-ball shadow, the undrawn comb and D7's protection (in Not done).

Round 1: no findings.
