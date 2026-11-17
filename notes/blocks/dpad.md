# Data pad cells D0-D7 (`dpad`)

Region: x 17640-19150, y 5950-19150 (the eight pads down the right side, D0 at the top).
Trace: `trace/dpad.txt`. Scratch images: `cache/scratch/dpad/` (names in brackets below).

## Status

2026-11-17 14:59 +0000. Traced and extracting (full extraction 0 errors, 0 warnings):

- the output cell `dpad_cell` (output fingers, extra pull-down fingers, the two-NOR
  pre-driver under the VCC band, the two straps), master D0, placed on D1-D7, each copy
  checked on its own;
- `d_hiz` (the "P_x" of the first notes), drawn end to end through all eight cells;
- the input protection clamp `dpad_prot` on D0-D6, the VSS rail beside it, and the
  input lines of D0 and D1 joined to `dbus`'s `d0_in` and `d1_in`.

AMB-003 is settled (see Logic). Not traced: the inside of the protection (comb, strips,
the series resistor from the bond pad), D7's protection, the input lines of D2-D7, the
`d#_out_n` lines outside the cells (they are `dbus`'s channel wiring), the bond pads.

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

## Input protection (partly traced)

Traced (cell `dpad_prot`, D0 coordinates): one diffusion with the rail side (x
17685-17775, nine contacts at x 17705 to the rail metal), the clamp gate (the frame's
left arm, poly x 17778-17808) and the node (x 17810-17868, nine contacts at x 17830 to
a metal column that leaves south). The frame (the clamp's gate) is tied to VSS (below), so
the clamp is a grounded-gate transistor: vss, `d#_in`, W/L 397/30, gate vss.

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
- A poly strip along y 6530-6548 from x 17855 east under the band, ending at the node's
  neck.
- About 110 px above each cell a contact on the rail to a poly strip that runs east
  under the band (D0: contact 17727,6000, strip y 5975-5995; D1: contact 17725,7712,
  strip y 7700-7722) [rg].
- From the bond pad: a contact box 18265-18355 x 6475-6560, a narrow strip north along
  x 18295-18315 to y 6095, west along y 6085-6105 to x 18065, south along x 18062-18080
  to about y 6600 [p_m, p_b]. Not followed further.

**The frame is tied to VSS** (review round 2, confirmed in the photos by the tracer): its
right arm and the outer strip x 17978-17995 join in a U at the foot (y 6490-6512, acid1b
4.5x, `chk_foot.png`); the strip runs up to y 5985 and west along y 5975-5995 to a contact
on the rail at (17727,6000) (ring in metal, green patch in acid1b, `chk_prot0.png`; the
reviewer saw the same in all seven copies, D1 at 3.7-5x); in D0 a 20 px metal stub joins
it to the rail's top. Drawn in the cell. So the clamp is off in normal operation, as a
grounded-gate clamp. Still open: the series resistor from the pad (the comb and the pad's
strip): how the pad reaches the node.

## Ports

| Name | Layer | Where | Direction | What |
|---|---|---|---|---|
| `d#` | metal | neck 18850-19025 x 6650-6850 + cell offset, up to the bond pad | pad | bond pads not drawn |
| `d_hiz` | metal x 17631-17651 | y 7374-18850; contact 17637,7385 + cell offset in each cell; poly cross-under 17633-17655 x 18128-18304 between contacts 17643,18143 and 17643,18290 | into the cells | driver not found: `follow.py` reports contact candidates along it at y 9290-9573, 11168, 14500, 14798, 16754, 16827, none looked at |
| `d0_out_n` | poly, then metal | cell, west along y 7480-7505 to the contact 17597,7492, metal x 17589-17609 south (drawn to y 7570) | into the cell | `dbus` notes: continues to 17597,8097 |
| `d1_out_n` .. `d7_out_n` | poly | west end of strip 4 at 17800,7466-7492 + cell offset | into the cell | routes differ per pad (`dbus` notes list D1's and D7's); not drawn |
| `d0_in` | metal, poly, metal | node column, contact 17835,6585, poly west along y 6573-6597 and south along x 17550-17572, contact 17555,6755, metal x 17548-17566 to `dbus`'s piece at y 8050 | out | joined |
| `d1_in` | metal | node column to the contact 17836,8402, where `dbus`'s poly starts | out | joined |
| `d2_in_u` .. `d6_in_u` | metal | node column, drawn to y 6560 + protection offset; in the composite the contact is near 17825,6665 + offset with poly leaving west | out | not followed |

## Ambiguities

- The protection's comb and the pad's series strip (how the pad reaches the node): above.
  Related to AMB-005 (the frame is now known to be tied to VSS).
- D7's protection (x 17685-17960, y 17540-18030) is not the same layout: its frame is
  closed along the bottom and no neck leaves south [P_all, last tile]. Not traced.
- Whether the pull-up fingers are enhancement devices cannot be seen (AMB-002).

## Not done

- Protection: comb, strips, the series strip from each bond pad (lengths differ per
  pad), D7's variant; the bond pads.
- Input lines of D2-D7 from the protection nodes to the column (`d#_in_u`).
- `d#_out_n` outside the cells and the driver of `d_hiz`: `dbus`'s channel wiring. Lead (review round 1, confirmed): at (17630,17085) a metal leaves `d_hiz` west along y 17073-17095 to x 17355 and turns south along x 17350-17370 past y 17237 (`metal` at 2.4-3x): almost certainly its feed. It lies in `dbus`'s claimed region, so it is not drawn here.
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
