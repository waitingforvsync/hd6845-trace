# bd1: logic and routing channel left of the register-select gates (x 13000-14100, y 14700-17100)

Trace: `trace/bd1.txt` (`@requires sel`, `@requires bd3`). Coordinates are metal-shot pixels.

## Status

- Traced, extracted (0 errors, 0 warnings) and checked by overlay: the route of every write
  strobe that enters the region (R0 to R7 leave north on the track bundle, R8 west in poly);
  the two big inverters on line X; X's driver; and, new in the second run, **the gate column
  from y 15385 to 15850**: an inverter, the pull-down networks of both halves of a latch
  (one half complete with its load and output line), and the pull-down that `rst_a` gates.
- **The region is mostly a routing channel**: 18 vertical metal tracks (x 13088-13826) with
  poly cross-unders. The gates are a single column at x 13700-14080, y 15100-16900.
- NOT traced in runs 1 and 2: the second latch half's load east of the ground rail (y 15640-15705:
  since drawn by `eof`), the gate column at y 15850-16125 (run 5) and 16280-16900 (run 4), and the
  lower ends of several channel lines. See Not done.
- Tracks k7, k8, k9, k11, k15 are traced from the north edge to their first contact (k8: as
  far as it runs straight); `rst_lat` and `bd1_k` are followed through the channel.
- **Run 4 (2026-11-28): the gate column y 16340-16815 is traced** (11 transistors): a second copy of
  the latch on R4's match, 955 px south of it, on **R0-half's match** (`h_eq_r0half`), enabled by
  `ck_out` and cleared by `rst_a`; its upper node's wire is followed 4,900 px to `eof`'s wire
  `eof_w16432`, an input of the NOR `eof_w15955` in the bottom-centre logic. See "Run 4".
- **Run 5 (2026-11-28): the dense group y 15860-16135 is traced** (6 transistors): a latch on **R0's match**
  (`h_eq_r0`, passed while `ck_out` is high) whose inverted output is a second pull-down of line X's driver:
  **`rst_a_n` = NOR(`rst_a`, `h_eq_r0_q_n`)**, so `rst_rc`, `rst_lat` and `rst_ck` are not plain reset copies.
  See "Run 5". The gate column is now traced from y 15100 to y 16815; where this page still calls those lines
  copies of the reset, read it with that section.

How the gate column was read: plain views are not enough. `tools/rdp3_sharp.py` at 4.3-6.4x
with `acid1b` and a metal shot side by side, plus two text tools written for this block:
`tools/bd1_map.py` (ASCII map of colour classes of `acid1b`, which separates poly from
diffusion and field numerically) and `tools/bd1_prof.py` (colour profile along a line in
all shots). Colours here: under metal, field is pink (R high, B about G), diffusion bright
tan, poly salmon; in the open, poly is red-brown, field and diffusion both khaki (told apart
only by outlines). A narrow gap between two metals shows as a green strip with dark edges
over field, and as khaki with a dark blob over diffusion.

Boundary with `mra`: the mid-right array's own lines end with the `ck_a` rail at
x 13013-13037 (trunks). Everything from the track at x 13088 eastwards belongs to this
channel. There is no separate "bus at x 13000-13320": the lines there are tracks k0-k5
of the channel (k0-k3 are write strobes going north). Poly lines cross the boundary
westward under the `ck_a` rail at several y (ports table).

Reading coordinates off a view: a grid line is at the left edge of its label, and in a
two-panel image the right panel has its own origin (subtract the panel's offset before
dividing by the scale). `tools/sel_cut.py h Y x0 x1 --brief` gives track centres to 2 px
and is the quickest check.

## Inventory

| What | Where | Notes |
|---|---|---|
| Track bundle | x 13088 + 43.4 k, k = 0..17 (k17 = 13826), entering at y 14700 from the north | 18 metal lines, 20 wide. South of y 14850 they end, jog one or more tracks sideways (nested corners) or duck under each other in poly |
| Strobe polys from sel | y 14867, 14909, 14957, 15001, 15043, from x 14100 west | each ends on a contact under the track that takes it north |
| Wide rail from the north | x 13910-13958, y < 15246 | `vss`; ends in an arm (y 15215-15246) to the column's ground rail |
| Ground rail of the gate column | x 13826-13870, y 15100 to 16815 | one metal all the way (run 5: the "two narrow lines" at y 15833-15991 were the edges of what lies under it); 54 px wide through the group y 15860-16135 |
| Supply rail of the gate column | x 13997-14044, y < 16960 | `vcc`: every load of the column ends on it. By scan it is continuous from y 14600 to 16960, where bd3's wide rail (y 16907-16954) arrives |
| Inverter pair on X | x 13765-14050, y 15120-15350 | two inverters, one ground contact between them (13838,15237) |
| Inverter A | x 13860-14045, y 15385-15512 | `bd1_an` = NOT `rc_eq_r4`; pull-down east of the rail (gate P4), load block x 13936-13992 |
| Latch, upper half | x 13700-14050, y 15468-15690 | node `bd1_n1`; pull-downs under the rail (P2, P3, G4), load block x 13938-13992, y 15523-15608 |
| Pull-down of `bd1_k` | x 13773-13804, y 15634-15730 | strip under `bd1_an`'s metal, gate = `rst_a` |
| Latch, lower half | x 13797-13990, y 15705-15852 | node `bd1_n2`; pull-downs G5, G6 under the rail and a third (gate `bd1_n1`) east of it |
| (not traced) | x 13876-13995, y 15640-15705 | N2's load and the driver of `bd1_q` |
| Latch on R0's match (run 5) | x 13740-14055, y 15860-16135 | pass transistor on `ck_out` (pad (13713,15931), an L-shaped gate), storage node `h_eq_r0_q`, inverter (G1 under the rail, load at x 13954-13991), hold device (a plate tied to the rail by the contact (13870,15900)); the load's plate runs south as gate G2 of X's driver |
| X's driver | x 13760-14050, y 16100-16280 | a two-input NOR since run 5: the pull-down on `rst_a` (input poly along y 16231) and a second one, G2 (y 16107-16149), on the latch's `h_eq_r0_q_n` |
| Latch on R0-half's match (run 4) | x 13690-14050, y 16340-16815 | a copy of the latch at y 15385-15852, 955 px south: inverter B, upper half (node N1, the wire `eof_w16432`), lower half (node `h_eq_r0half_q`), a clear pull-down on `rst_a`; `ck_out`'s taps (13716,16495) and (13715,16711) are its two enable gates; (13716,16562) is the east end of `trunks`' wide poly row. y 16280-16340 is empty field; the ground rail ends at y 16815 |
| ck_out rail | x 13703-13727, y 15918-16724 | drawn in trunks.txt, not here; its north end is the pad of the pass transistor's gate (run 5) |
| Bottom bundle | y 16862-17128, x 13380-14100 | strobes from bd3 turning north or west; line X's corner |

## Logic

Traced (extracted by netlist.py) unless marked believed.

### Where the write strobes go

Every strobe that enters was followed to where it leaves. None of them feeds a gate
in this region.

| Strobe | Enters | Route | Leaves |
|---|---|---|---|
| wr_r6 | poly, (14100,14867) | west to contact (13088,14867) | north, track k0 (13088,14700) |
| wr_r1 | poly, (14100,14909) | contact (13785,14913) | north, k16 (13782,14700) |
| wr_r2 | poly, (14100,14957) | contact (13609,14956) | north, k12 (13608,14700) |
| wr_r0 | poly, (14100,15001) | contact (13652,15000) | north, k13 (13652,14700) |
| wr_r4 | poly, (14100,15043) | contact (13521,15042) | north, k10 (13521,14700) |
| wr_r7 | poly, (14100,16864) | contact (13958,16861); metal west along y 16862; contact (13480,16864); poly west, diagonally up-left, north to contact (13218,16642); metal north on x 13218; jog west at y 15390 to x 13174 | north, k2 (13174,14700) |
| wr_r5 | metal, (14100,17041) | north at x 13915, west along y 16954, north at x 13435 to contact (13435,16908); poly west along y 16905, north at x 13164 to contact (13174,16730); metal north on x 13174 to contact (13175,15562); poly link to contact (13085,15563); metal north on x 13088; jog east at y 14912 to x 13131 | north, k1 (13131,14700) |
| wr_r3 | metal, (14100,17084) | step up at x 13832 to y 17041, west, north at x 13522 to contact (13522,16995); poly north at x 13518 (under wr_r7's metal) to contact (13522,16820); metal north on x 13521 to contact (13521,16455); poly west along y 16453 to contact (13262,16456); metal north on x 13261; jog west at y 15346 to x 13218 | north, k3 (13218,14700) |
| wr_r8 | metal, (14100,17128) | contact (13392,17126); poly west along y 17125 under every vertical line | west, (12985,17125), poly, still running |
| wr_r9 | metal, y 17172 | below the region; by scan the metal runs west to x 13471 | not followed |
| wr_r11 | metal, y 17215 | by scan to x 13414 | not followed |
| wr_r10 | metal, y 17258 | by scan to x 13471 | not followed |

So the strobes of R0 to R7 all go north in the bundle (towards the right datapath;
believed). The order on the tracks is k0 w6, k1 w5, k2 w7, k3 w3, k10 w4, k12 w2,
k13 w0, k16 w1. R8's goes west in poly; R9, R10, R11's were not followed.

The poly at y 14912 **west** of x 13712 is not wr_r1: wr_r1's poly ends at its
contact (13785,14913); a second poly starts 56 px further west on a contact under
track k14 and runs west, south (x 13133) and west again along y 15020 into the
mid-right array (`hc3`).

### Line X: its driver and the two inverters it feeds (traced)

X is the line of `notes/blocks/trunks.md` (input of input-row gate 0, whose output S
is distributed over the whole die). Here it is `rst_a_n`.

```
rst_a_n   = NOT rst_a       X's driver, y 16125-16280   (as read in run 1. Since run 5: rst_a_n = NOR(rst_a, h_eq_r0_q_n),
                            a second pull-down at y 16107-16149 gated by the latch on R0's match: section "Run 5")
rst_rc = NOT rst_a_n       upper inverter, gate bar y 15183-15203
rst_lat = NOT rst_a_n       lower inverter, gate bar y 15271-15291
```

- **X's driver** is one inverter (run 1; **a two-input NOR since run 5**, which found the second pull-down). Pull-down: gate poly `rst_a` crossing the diffusion
  under the ground rail diagonally (x 13817-13888), ground contact at (13855,16250).
  Output diffusion above the gate; it reaches X three ways: a buried contact at
  (13762-13800, 16170-16210) to the tap poly that runs west to the contact (13672,16190)
  on X's metal; a metal contact at (13917,16155) to a line going north into the dense
  group (it ends on the contact (13926,15917) of a diffusion box, the east end of the latch's hold device: run 5); and a strip down the west
  side of the load. Load: poly block x 13953-13991, y 16140-16265, tied to the output by
  a buried contact at its top (13953-13985, 16142-16174), supply contact (14017,16228).
  W/L of the load 68/37; of the pull-down 90/24 as certain, up to 188/26 with the two
  uncertain pieces (Ambiguities).
- `rst_a` is on a metal line at x 13630 with a contact at each end. Top end,
  (13629,15673): a poly goes east into the gate column along y 15671, crosses a 30 px
  wide diffusion strip (x 13772-13802, lying under the metal line on x 13782) and ends
  at x 13805 (5x view): so g is the **gate** of a small transistor there (the pull-down of
  `bd1_k`, next section), not an output.
  Bottom end, (13629,16150): the line ducks under X's horizontal metal in poly to a pad
  with a second contact, (13629,16235). From that pad the gate poly of X's driver runs
  east, and a metal runs south on x 13630 to a contact at (13631,16758); poly east
  under X's line and south along x 13699 to a contact at (13698,17080); metal west
  along y 17082 to a contact at (13480,17083); poly south, **leaving the region at
  (13480,17150)**. On the whole of g followed here no gate output was seen (its east end
  at y 15671 was looked at once, at 5x: a plain gate crossing, no buried contact), so
  **g is believed to come from the south** (bottom bus field): what drives it, and so
  what X is, lies outside this block.
- **X's metal** on track k11's position starts at the contact (13567,15193): that is
  its top end. A second contact 88 px lower, (13567,15281). Each goes to a poly bar
  running east, and each bar is the gate of one inverter: pull-down W/L 131/20, load
  70/38 (poly block next to the supply rail, tied to the output by a buried contact).
  The two share the ground contact (13838,15237) between the bars.
- `rst_rc` leaves west in poly (buried contact 13766-13798, 15144-15173; poly along
  y 15151) to a contact at (13347,15150) where **track k6 ends: it goes north**.
- `rst_lat` leaves west in poly (buried contact 13766-13797, 15303-15333) to a contact
  at (13695,15325); metal south to (13700,15452), where one arm goes to a contact at
  (13655,15453) (poly west along y 15455 to a contact at (13520,15458), then metal south
  on x 13521 to a contact at (13520,15931) and on, see "Tracks") and the other runs south
  on x 13716 with contacts at (13717,15541) and (13716,15760): the gates P3 and G5 of the
  latch below (next section).

Believed (run 1): X, S (= NOT X, made by input-row gate 0), `rst_rc` and `rst_lat` are four
separately buffered copies of one clock-like signal `NOT rst_a` and its inverse; all
three inverters here are the same size. **Run 5: the signal is `rst_a_n` = NOT `rst_a` AND `h_eq_r0_q`**,
the latched R0 match gated off by the reset: clock-like after all, once per scan line.

### Gate column, y 15385-15850: an inverter and a latch gated by `rst_lat` (traced, second run)

```
bd1_an = NOT rc_eq_r4
bd1_n1 = NOT( rc_eq_r4 . rst_lat  +  bd1_q )                     upper half, complete
bd1_n2 : pull-downs  bd1_an . rst_lat  +  bd1_n1  to vss       lower half; its load is not traced
bd1_k  : pull-down  rst_a  to vss (source connection uncertain; its load is not in view)
```

Under the ground rail one diffusion column carries, top to bottom: vss contact (13832,15461),
gate P2 (y 15488-15508, `rc_eq_r4`), a strip 18 px tall with no contact, gate P3 (y 15530-15550,
`rst_lat`), node N1 (y 15552-15601), gate G4 (y 15602-15623, `bd1_q`), vss contact
(13845,15657); then field (y 15682-15706); then node N2 (y 15709-15745), gate G5
(y 15746-15766, `rst_lat`), a strip, gate G6 (y 15791-15810, `bd1_an`), vss contact
(13842,15832).

- **`rc_eq_r4`** enters from the north on track k15, jogs west at y 15087 to k13's position
  (x 13652), contact (13655,15391), poly east and south along x 13723 under
  `rst_lat`'s metal, east along y 15498 across the column (P2) and north again east of
  the rail (P4, x 13868-13890, ending in a rounded cap at y 15427). P2 and P4 are one
  poly: an L round the ground diffusion (colour profile across the corner; the gap to P3
  below, y 15508-15518, is field).
- **Inverter A.** P4 between the ground diffusion and the node east of it (W/L 38/22);
  load block x 13936-13992, y 15432-15490 over a strip y 15447-15478 (31/56) from the supply
  contact (14019,15484). The output's buried contact (13910-13934, 15398-15424) joins the
  load's gate (a poly neck down the block's west side) and a poly bar going west under the
  rail over field to a pad with a contact at (13779,15405). From there **`bd1_an` runs
  south on a metal line on x 13783 to a contact at (13768,15806)**, with no contact on the
  way (checked at 5x and 6.4x in both metal shots: no pad, no ring, no specks below), and
  from that contact's poly pad the gate G6 runs east under the rail.
- **`rst_lat` (NOT X) gates P3 and G5**: its metal on x 13716 has contacts at (13717,15541)
  (pad of P3) and at its foot (13716,15760) (pad of G5). It goes nowhere else from this line.
- **Upper half, node `bd1_n1`.** Pull-downs: P2 and P3 in series (72/20 each), G4 alone
  (46/21). Load: poly block x 13938-13992, y 15523-15608 over a strip y 15565-15593 (28/54)
  from the supply land x 14000-14048, y 15567-15687. The block has a metal contact at
  (13956,15538): **`bd1_n1` leaves on a metal line on x 13957 south to a contact at
  (13957,15740)** on a poly pad (the poly goes on south-east and joins a poly block at
  x 13918-13954, y 15780-15798 by colour map; not traced). The tie of the load's gate to N1
  is a buried contact at (13894-13926, 15558-15576) with a poly arm from the block's top: `?`
  (Ambiguities). N1 also has a buried contact at its west end (13766-13802, 15572-15600) to
  a poly pad that ends 20 px further west under nothing: no function found.
- **`bd1_q`** is the poly of G4: a rounded end at x 13804 west of the rail, the gate, a block
  east of the rail (x 13877-13912), then (by colour profile) south at x 13896-13908 into a
  band y 15630-15650 that runs east to x 13996 beside the supply land. Its driver is not
  traced.
- **Lower half, node `bd1_n2`.** Traced: G5 and G6 in series (76/20 each) to the vss contact
  (13842,15832). Traced with less certainty (drawn `?`, see Ambiguities): a third
  pull-down east of the rail whose gate is `bd1_n1` (38/24). N2's diffusion goes east from
  the rail along y 15705-15728 and south along x 13919-13936 round an island of field; the
  poly from `bd1_n1`'s pad comes down x 13966-13986 and west as a block y 15782-15806
  across it; below the block a diffusion band y 15815-15833 runs back west to the vss
  contact's diffusion. Not traced: N2's load and its tie to `bd1_q` (north of the arm,
  x 13880-13995, y 15640-15705).
- **`rst_a`'s transistor.** The poly along y 15671 crosses a diffusion strip x 13773-13804
  that lies under `bd1_an`'s metal without touching it (31/20) and ends at x 13805. Below
  the gate the strip has a buried contact (13768-13792, 15699-15733) to a poly that goes west
  along y 15713 to a contact at (13674,15715): `bd1_k`, a metal line on x 13674 south to a
  contact at (13674,15973). Above the gate the strip is a closed box (y 15634-15660) with
  no contact; it is read as joined to the ground diffusion under the rail through the gap
  between the two metals (`?`, Ambiguities).

Believed (not traced): `bd1_q` = `bd1_n2` (so `bd1_n2` = NOT(`bd1_an` . `rst_lat` + `bd1_n1`)
with `bd1_q`'s band as its load gate).
That makes the pair a transparent latch of `rc_eq_r4`: while `rst_lat` is high (X low,
`rst_a` high) `bd1_n1` = NOT `rc_eq_r4` and `bd1_n2` = `rc_eq_r4`; while it is low both hold.
The layout supports it (the two halves mirror each other; `bd1_n1`'s line ends beside
N2; the band of `bd1_q` lies where N2's load would be), but the wiring that would prove
it (N2's load and the buried contact beside `bd1_q`'s band) is the untraced part. Neither `ck_out` nor any trunk clock reaches this latch: its
gate is `rst_lat`, the inverse of line X.

### Tracks traced so far

| Track at y 14700 | Net | What happens to it |
|---|---|---|
| k0 13088 | wr_r6 | ends at contact (13088,14867) |
| k1 13131 | wr_r5 | jogs to x 13088 at y 14912, down to contact (13085,15563) |
| k2 13174 | wr_r7 | jogs to x 13218 at y 15390, down to contact (13218,16642) |
| k3 13218 | wr_r3 | jogs to x 13261 at y 15346, down to contact (13262,16456) |
| k4 13261 | rc_eq_r6 | jogs to x 13304 at y 15308; runs on south to y 16690 and turns south-west along a diagonal into the field of diagonals (drawn to (13259,16738), run 3) |
| k5 13304 | h_eq_r0half | jogs to x 13348 at y 15262, down to contact (13348,16411); poly east along y 16410 towards the gate column (seen to x 13700 at 0.9x, not followed) |
| k6 13348 | rst_rc | ends at contact (13347,15150) |
| k7 13391 | h_eq_r0 | jogs to x 13435 at y 15176, down to contact (13432,15888); poly east along y 15889 under five lines into the gate column's dense group (seen to x 13695) |
| k8 13435 | h_eq_r1 | jogs to x 13478 at y 15130, runs south; one metal to y 16780 (the "23 px break" of the scan at y 16594 is the dark edges of two poly rows it crosses: run 3); `trunks` draws it on from there |
| k9 13478 | hc2 | jogs to x 13521 at y 15087, **ends at contact (13520,15390)**; poly west along y 15388 (under wr_r7's jog, no contact), corner at x 13108, south, west into the mid-right array at (13035,15497) (the poly's route is from the first run, `?`) |
| k10 13521 | wr_r4 | ends at contact (13521,15042) |
| k11 13565 | hc1 | jogs to x 13608 at y 15005, down to a contact at (13609,15608) (scan, 1.5x); poly west then diagonally down-left to counter row r17's n1 (drawn by `hcj`) |
| k12 13608 | wr_r2 | ends at contact (13609,14956) |
| k13 13652 | wr_r0 | ends at contact (13652,15000) |
| k14 13694 | hc3 | ends at contact (13692,14913); poly west into the mid-right array at y 15020 |
| k15 13738 | **rc_eq_r4** | jogs **west** to x 13652 at y 15087, down to contact (13655,15391): the latch's data input |
| k16 13782 | wr_r1 | ends at contact (13785,14913) |
| k17 13826 | hc0 | jogs to x 13782 at y 14975, down to y 15131, west to x 13696, contact (13697,15239); poly west along y 15238 to contact (13131,15235); metal south on x 13131 to contact (13131,16413); poly on into the mid-right array (trunks: along y 16440-16462) |

The jogs at y 15087-15176 are nested: k9, k8, k7 each step one track east once the track
east of them has ended (3.1x metal view, overlay checked). Below the jogs the track
positions therefore carry other nets than at the top edge:

| Position | Net below the jogs | Segments (contact to contact) |
|---|---|---|
| x 13435 | h_eq_r0, then **rst_lat** | k7 to (13432,15888). A new line starts at contact (13432,15955) and runs south (scan: to y 16769, lower end not traced): it is `rst_lat`, see below |
| x 13478 | h_eq_r1 | from the jog south |
| x 13521 | hc2, then **rst_lat**, then **bd1_k** | k9 to (13520,15390). Break. (13520,15458) to (13520,15931): `rst_lat`. Break. (13522,15999) south (scan: to y 16273, lower end not traced; a further piece y 16445-16805 is wr_r3's): `bd1_k` |
| x 13674 | bd1_k | (13674,15715) to (13674,15975) |

**Where `rst_lat` goes** (all traced except the last line's lower end): contact (13695,15325),
metal to (13700,15452); one arm south on x 13716 to the latch's gates P3 and G5; the other
arm contact (13655,15453), poly west, contact (13520,15458), metal south on x 13521,
contact (13520,15931), poly pad with a tail west along y 15959 under k8's line, contact
(13432,15955), metal south on x 13435 towards y 16769.

**Where `bd1_k` goes**: contact (13674,15975), poly west along y 15997 under `rst_a`'s and
X's lines, contact (13522,15999), metal south on x 13521 to about y 16273.

## Ports

| Name | Layer | Crossing | Direction | What |
|---|---|---|---|---|
| wr_r6, wr_r1, wr_r2, wr_r0, wr_r4 | poly | x 14100, y 14867 / 14909 / 14957 / 15001 / 15043 (east) | in | from sel |
| wr_r7 | poly | 14100,16864 (east) | in | from bd3 |
| wr_r5, wr_r3, wr_r8 | metal | x 14100, y 17041 / 17084 / 17128 (east) | in | from bd3 |
| wr_r6 | metal | 13088,14700 (north) | out | track k0 |
| wr_r5 | metal | 13131,14700 (north) | out | track k1 |
| wr_r7 | metal | 13174,14700 (north) | out | track k2 |
| wr_r3 | metal | 13218,14700 (north) | out | track k3 |
| rc_eq_r6 | metal | 13261,14700 (north) | ? | track k4 |
| h_eq_r0half | metal | 13304,14700 (north) | ? | track k5 |
| rst_rc | metal | 13348,14700 (north) | out | track k6: NOT X |
| h_eq_r0 | metal | 13391,14700 (north) | in | track k7; its poly along y 15889 ends on the buried contact of the pass transistor's land (run 5; inside the block) |
| h_eq_r1 | metal | 13435,14700 (north) | ? | track k8; runs south past y 16590 (lower end not traced) |
| hc2 | metal | 13478,14700 (north) | ? | track k9; ends at contact (13520,15390) |
| hc2 | poly | 13035,15497 (west) | ? | k9's poly, into the mid-right array (`?`: route from the first run) |
| rst_lat | metal | 13435,16769 (drawn to there) | out | NOT X going south on k8's position; lower end not traced |
| bd1_k | metal | 13521,16273 (drawn to there) | ? | going south on k10's position; lower end not traced |
| wr_r4 | metal | 13521,14700 (north) | out | track k10 |
| hc1 | metal | 13565,14700 (north) | ? | track k11; jogs to x 13608 at y 15005, ends at a contact at (13609,15608), poly west then diagonally down-left to counter row r17's n1 (drawn by `hcj`) |
| wr_r2 | metal | 13608,14700 (north) | out | track k12 |
| wr_r0 | metal | 13652,14700 (north) | out | track k13 |
| hc3 | metal | 13694,14700 (north) | ? | track k14 |
| hc3 | poly | 13000,15020 (west) | ? | into the mid-right array's routing channel, under the `ck_a` rail |
| rc_eq_r4 | metal | 13738,14700 (north) | in | track k15: data input of the latch and input of inverter A |
| wr_r1 | metal | 13782,14700 (north) | out | track k16 |
| hc0 | metal | 13826,14700 (north) | ? | track k17 |
| hc0 | poly | 12970,16451 (west) | ? | into the mid-right array (this last poly is `?`: from trunks' notes, not checked here) |
| wr_r8 | poly | 12985,17125 (west) | out | goes on west below the array's bottom row |
| rst_a_n | metal | 13672,16610 (drawn to there) | out | line X; trunks.txt draws it from y 16600 south. Not labelled in trunks.txt: it reaches inrow's `rst_a_n` |
| rst_a_n | metal | 13926,15917 | - | from the driver's node north to a contact on a diffusion box, the east end of the latch's hold device (run 5; inside the block) |
| rst_a | poly | 13805,15671 | - | ends as the gate of `bd1_k`'s pull-down (inside the block) |
| rst_a | poly | 13480,17150 (south) | in (believed) | X = NOT g; g has no driver in this region. Seen to y 17145, going south |
| bd1_q | poly | 13996,15640 | in (believed) | east end of the band y 15630-15650; driver not traced (believed `bd1_n2`) |
| bd1_n2 | diffusion | 13930,15705 | ? | N2's arm east of the rail, continuing north to its load (not traced) |
| vss | metal | 13910-13958, 14700 (north) | - | wide rail; named from the pull-downs it feeds |
| vcc | metal | 13997-14044, 14700 (north) | - | supply rail; joins bd3's wide rail at the bottom (by scan) |
| ck_out | metal | rail x 13703-13727, y 15930-16711 | in | trunks; the taps (13716,16495) and (13715,16711) are the lower latch's enable gates (run 4); its north end (13713,15931) is the pad of the pass transistor's gate in the latch on R0's match (run 5) |
| h_eq_r0half | poly | row y 16410 from k5's contact (13348,16411) | in | the data of the lower latch and the input of inverter B (run 4; inside the block) |
| rst_a | poly | row y 16628 from the tap (13628,16626) | in | ends as the gate of the lower latch's clear pull-down at x 13812 (run 4; inside the block) |
| eof_w16432 | metal | 10850, 18420-18440 | out | the lower latch's upper node N1, 4,900 px from the latch: the bus line y 18429 ends on the corner of `eof`'s metal x 10811 (run 4, piece `out2`) |
| vcc | metal | 13998-14044, 16900 (drawn to there) | - | the supply rail runs on south to `bd3`'s wide rail (by scan) |

## Ambiguities

- **Width of the pull-down of X's driver.** Certain: the gate poly crosses the
  diffusion under the rail (x 13817-13888). Uncertain, both drawn `?D`: (a) the poly
  ends east of the rail in a block (x 13886-13926, y 16183-16258) lying between the
  ground diffusion and the output strip, which would be a second channel (58 wide,
  38 long); (b) west of the rail the output diffusion (below the buried contact) and a
  heavy-outlined box (x 13759-13805, y 16247-16277) lie either side of the poly, as the
  source and drain strips do in the two inverters at the top, which would add 56 to the
  width. Neither changes the logic. To settle: a sharper photo; at 4.3x-5.6x the
  outlines are there but the continuity under the poly cannot be seen.
- **Is the ground rail one piece?** At y 15833-15991 the rail x 13826-13870 becomes two
  narrow lines. The lower part is labelled `vss` because pull-downs sit on it and the
  loads go to the other rail.
- The wide rail x 13910-13958 is called `vss` and the rail x 13997-14044 `vcc` from the
  orientation of the gates. The second is supported by bd3 (its wide rail y 16907-16954
  is traced to the input row's VCC band and turns north at x 13970-14030).
- The poly along y 15385 lies exactly under the 60 px metal jog of wr_r7 (x 13166-13225).
  No contact: both metal shots at 4x show plain metal there, and in `acid1b` the band
  shows no pad. That poly (from a corner at x 13108, where it goes south and then west
  into the mid-right array at y 15497, east to a contact near (13505,15385)) is not traced.
- X has **two** contacts at the top of its metal, 88 px apart, one per inverter gate
  bar, although the two bars could have been one poly. Both rings are plain in `metal`
  (2.9x) and the metal runs unbroken between them, so the two inverters do have the
  same input. They are separate gates with separate loads and outputs, not one
  double-width inverter: the outputs leave by different buried contacts to different
  wires and no diffusion or poly joins them.
- Contact pads look two ways in `acid1b` here: pale with a green centre, or a dark red
  box with a heavy outline (for example (13567,15281), (13522,16995), (13629,16235)).
  Both kinds have a plain contact ring in `metal`; both are treated as metal-to-poly
  contacts.

- **Load tie of `bd1_n1`** (13894-13926, 15558-15576). The load block's gate has a metal
  contact (13956,15538) to the line on x 13957, so that line is N1 only if the gate is tied
  to N1. Seen: a box with a bright centre and heavy outline on N1's diffusion east of the
  rail, and above it a dark complex (13897-13934, 15521-15556) reaching the block's top
  (4.3x, 4.85x; in `metal` two small squares at 13902-13918 and 13925-13941, y 15546-15562).
  The poly arm's shape is not resolved. Other reading: the block is a pull-up driven from
  the line's other end; nothing was seen that would drive it. Working assumption: tied
  (drawn `?`). To settle: follow the poly from the pad at (13957,15740).
- **Source of `bd1_k`'s pull-down** (13800-13830, 15634-15650). The strip segment above
  `rst_a`'s gate has no contact (metal 19 px wide there, no ring, `acid1b` smooth). In the
  28 px gap between `bd1_an`'s metal and the rail, at y 15634-15650 the colour map shows
  khaki with a dark blob and no green strip, as at the strip between P2 and P3 where
  diffusion certainly crosses the same gap; from y 15652 down the green strip of open field
  appears. So the segment is read as joined to the ground diffusion (drawn `?D`). If it is
  not, the device is only a capacitor between `rst_a` and `bd1_k`.
- **The dead-end poly on N1's west buried contact** (13749-13799, 15575-15597). Poly in
  the open, 24 x 27, with nothing leaving it (three shots at 6x). A C-shaped outline round
  it reaches up to P3's lower edge at (13768,15560); P3 is `rst_lat`, an inverter output,
  so a join there would short it to N1 and is not adopted.
- **N2's third pull-down** (13868-13986, 15705-15833). Evidence: in chip 2's stripped
  shot the block is orange (poly) and the arm above it and the band below it are tan like
  the diffusion under the rail, while the framed area west of the arm is greenish (field);
  `metal1` and `acid1b` show the same outlines; the poly is orange without a break from the
  block east and up to the pad of `bd1_n1`'s contact (13957,15740). Not seen directly:
  the diffusion under the block, and the join of the arm to N2 under the rail's edge
  (x 13873-13885, hidden by the rail's margin line). An earlier reading of the block as a
  load, and of the ring at its west end (13895-13917, 15777-15814) as a buried contact, is
  dropped: the ring is the block's rounded end over field.
- Whether P3's east end and P4's lower end touch (13864-13876, 15508-15520): measured pink
  (field under metal, B about G) for 10 px between them, so they are separate.
- `bd1_q`'s route from the block east of the rail to the band y 15630-15650 is from the
  colour map and one 4.85x view (drawn `?P`).

## Not done

Gate column (x 13700-14080). The photos are at their limit there: use
`tools/rdp3_sharp.py` at 2.9x for a group and 4.3-5.6x for junctions (plain view.py
was not readable).

- x 13876-13995, y 15640-15705, east of the rail: N2's load and the driver of `bd1_q`.
  Seen: a box with a bright centre and heavy outline at (13904-13924, 15654-15685) (a
  buried contact? there is no metal on it: metal brightness about 150 there); poly bands
  y 15657-15686 and y 15690-15700 at x 13944-13992 beside the supply land, separated from
  `bd1_q`'s band (y 15630-15650) by one dark line at y 15651-15657, as the two parts of a
  load block are; N2's diffusion arm continuing north at x 13922-13940 above y 15704; a
  second framed island at x 13878-13910, y 15679-15709. If the band is N2's load gate and
  the box its tie, `bd1_q` = `bd1_n2` and the latch closes. One 6x three-shot view
  (`acid1b`, `metal1`, `acid`) of x 13880-13995, y 15640-15710 should settle it.
  A two-shot 5.6x view (`acid`, `acid1b`) did not: chip 2's shot shows a tan strip
  x 13916-13937, y 15658-15697, continuous with N2's arm below and ending under an arch at
  y 15649-15658 right below `bd1_q`'s band (which is orange, poly, x 13891-13948), which
  fits the tie; but the features of the two chips do not line up within 10 px there, so
  nothing was drawn.
- y 15850-15880 under the rail: the ground diffusion ends at about y 15852.
- y 15880-16125 (dense group): **traced in run 5** (the section "Run 5" below).
- y 16280-16900: **traced in run 4** (the section "Run 4" below).

Channel:

- Lower ends, all in or near the diagonals at y 16560-16900: k4 (x 13304, past y 16700),
  k8 (x 13478; scan: metal to y 16594, break, to y 16797), `rst_lat` on x 13435 (to y 16769),
  `bd1_k` on x 13521 (to y 16273). Scan of x 13435 also shows metal at y 16812-16836 and
  16899-16964.
- k11's poly from (13609,15608). (k7's poly, `h_eq_r0`, ends on the buried contact of the pass transistor's
  land: run 5.) (k5's poly, `h_eq_r0half`, is the data of the lower latch: run 4.)
- Lines on x 13608 at y 16167-16224 and x 13565 at y 16251-16572 (scan only).
- The diagonals at x 13150-13450, y 16680-16890: three metal lines step two tracks east
  there (seen at 1.5x), wr_r7's poly passes under them.
- Bottom edge: a long vertical poly at x 13870-13885 passing under all the horizontal
  lines (y 16840-17150): it is the lower latch's output wire `eof_w16432` (run 4, piece `out2`).
- wr_r9, wr_r11, wr_r10 west of x 14100 (they lie below y 17100).

## Gate column y 15860-16125: what a look from the coordinating session added (2026-11-16)

**Superseded by "Run 5" (2026-11-28), which traced the group.** What stands: the rail runs straight through; the
contact on the bar x 13857-13878 lands on poly tied to VSS, the weak always-on device of a latch; `h_eq_r0` ends on a
buried contact; `ck_out`'s poly gates the pass transistor that takes R0's match onto the storage node. What does not:
the contact (13820,15887) is not one (it is the rail over the top end of `ck_out`'s own poly, which is the bar
x 13808-13828), and the "fingers" are one plate.

Not traced then; these were observations to start from (views `g1a/g1m/g1o/g1b`, `h1a/h1b/h1m/h1o`,
`t1ab/t1m/t1c` in the scratch folder).

- **The ground rail runs straight through**: `tools/follow.py` from (13830,15950) follows one
  metal from y 15156 to y 16807. In this stretch it is 70 px wide (x 13810-13880) with two
  contacts, (13820,15887) and (13868,15893). **Both land on poly**, not diffusion (12x: the
  first sits on the field end of a poly bar x 13808-13828 that is bright, i.e. over a
  channel, from y 15897 to 15945; the second on the top of a poly bar x 13857-13878 that
  runs down to y 15985). A poly tied to VSS over a channel is the weak always-on device of
  this chip's latches (rdp3, cdp2, larr). So this group is a latch of that family, built to
  order: `findcell.py` finds no copy of the register latch cell here.
- **`h_eq_r0`** (track k7's poly, y 15878-15898) ends in a heavy-outlined box at
  x 13755-13800, y 15868-15915: a buried contact onto a diffusion node.
- **`ck_out`**: the metal x 13704-13728 that trunks.txt draws from y 16724 up to y 15918 ends
  on a contact (13712,15928); its poly runs east along y 15920-15945 to x 13806, right
  beside that node. Read (not established): it is the gate of the pass transistor that
  takes the R0 match from the buried-contact node onto the latch's storage node (the tan
  strip x 13830-13855 and its foot y 15945-15962). **The R0 match is sampled on NOT CLK
  here.**
- **`rst_a_n`** (line X) comes up from its driver to the contact (13925,15918) on a box
  x 13905-13945, y 15895-15945.
- Below, y 15960-16050: a stack of three or four horizontal poly fingers across the rail's
  diffusion column (x 13790-13878): the latch's inverters. East of it a load block
  x 13945-13990 and the VCC land x 14000-14050 with a contact (14020,16025).
- `bd1_k` arrives at the contact (13674,15973) west of the group.

What to settle first when this is traced: whether `ck_out`'s poly and the VSS-tied bar are
two pieces (they must be: one is a clock, the other is at VSS, yet at 5.6x they touch at
x 13806), which means a gap of field or a diffusion edge is being misread there.

## Corrections (coordinator, from the handoffs of 2026-11-19)

- `rc_eq_r4` is `rc_eq_r4` (`eof` run 1, firm join): R4's match is the data of the latch gated by
  `rst_lat` (`bd1_n1` = NOT(`bd1_q` OR (`rst_lat` AND `rc_eq_r4`))) and the input of inverter A
  (`bd1_an` = NOT `rc_eq_r4`). The latch's lower half, `bd1_q`'s driver and where `bd1_n1`, `bd1_n2`,
  `bd1_an` go are in the end-of-frame lead group (`eof` (e)).

## Corrections (coordinator, from the handoffs of 2026-11-19, second batch)

- Status "NOT traced: the second latch half's load east of the ground rail", Inventory "(not traced)
  x 13876-13995, y 15640-15705: N2's load and the driver of `bd1_q`", Logic "Believed (not traced):
  `bd1_q` = `bd1_n2`", Not done (first item) and the port `bd1_q` (in, believed): **traced by `eof`**
  (run 7, piece `r4lat`). The band is N2's load gate (block x 13937-13992, y 15630-15702 over a strip
  y 15661-15687 from the VCC land), tied to N2 by a box at (13889-13913, 15660-15682), drawn uncertain.
  `bd1_q` is an alias of `bd1_n2`, and the pair is cross-coupled: `bd1_n1` = NOT(`bd1_n2` OR (`rst_lat`
  AND `rc_eq_r4`)), `bd1_n2` = NOT((`bd1_an` AND `rst_lat`) OR `bd1_n1`) (both depend on the two load
  ties): a transparent latch of R4's match, open while `rst_lat` is high.
- Not done, "the features of the two chips do not line up within 10 px there": they do. The clean shot
  is inverted as a whole in that open group (tracing guide, trap 28; R42).
- Ambiguities, "Source of `bd1_k`'s pull-down": one reading is excluded: the strip's top segment is not
  joined to N1 from above (pink field under `bd1_an`'s metal at x 13770-13800, y 15602-15630 in the
  clean shot). Whether it reaches the ground diffusion is as open as before.
- Trace: the band `P 13896,15630:13996,15650` ends at x 13993, not 13996 (`eof`'s review round 9; field
  between it and the land): corrected, `tools/sameconn.py`: connections identical. Its `?P
  13896,15618:13908,15642` and `?D 13870,15705:13936,15728` are left marked: `trace/eof.txt` draws firm
  items over both, so the extraction does not depend on them.

## Corrections (coordinator, from the handoffs of 2026-11-19, third batch)

- Logic ("`bd1_k` : pull-down `rst_a` to vss (source connection uncertain; its load is not in view)";
  "`rst_a`'s transistor ... `bd1_k`, a metal line on x 13674"), Inventory ("Pull-down of `bd1_k`") and
  Ambiguities ("Source of `bd1_k`'s pull-down ... If it is not, the device is only a capacitor"): the
  strip is **N2's third pull-down, and `bd1_k` is `bd1_n2`, the latch's output** (`eof` run 8, piece
  `n2out`). The strip's lower segment (with the buried contact) is one diffusion with N2 through the gap
  at y 15712-15736, and its top segment reaches the ground diffusion through the gap at y 15638-15652.
  `bd1_n2` = NOT((`bd1_an` AND `rst_lat`) OR `bd1_n1` OR `rst_a`).
- "Where `bd1_k` goes: ... metal south on x 13521 to about y 16273" and Not done ("`bd1_k` on x 13521 (to
  y 16273)", "Lines on ... x 13565 at y 16251-16572 (scan only)"): the metal turns east at y 16264 and
  runs south on x 13564 to a pad (13562,16604); the line on x 13565 is this net (`eof`, piece `n2w`, which
  follows it 11,900 px to (6711,15000)).
- "`rst_a` is on a metal line at x 13630 ... a metal runs south on x 13630 to a contact at
  (13631,16758)": on the way it has a contact at (13627,16626) (ring and bright centre in both metal
  shots; `tools/textmap.py 13600 16598 13660 16652 3`), whose pad's poly runs east along y 16622 into the
  gate column (not drawn by anyone): one more load of `rst_a`.
- `trace/bd1.txt`: the gate poly of `rst_a`, `P 13640,15671 x13805 w=20`, lengthened to x 13812 (poly
  orange at x 13806-13809 in the chip-2 metal shot; `eof`'s review round 10; geometry only,
  `tools/sameconn.py HEAD`: connections identical).

## Corrections (coordinator, from the handoffs of 2026-11-19, fourth batch)

- The latch's output `bd1_n2` is drawn to its load (`eof` runs 8 and 14, `busl` run 7): the inverter of `tl4`'s right cluster that makes `rcs_e3`, 23,000 px away, with no other gate on the wire. Line X is the reset copy `rst_a` (`eof` run 10).

## Run 3 (2026-11-27): re-read item R1, the channel's tracks

Matt Godbolt, on Claude Fable 5.2, 2026-11-27 07:27 -0600. Region x 13040-13700, y 14700-16740 (below y 16740 the field of
diagonals is `eof`'s claim). No transistor; two wires added; no uncertain item.

**Method.** R1 asks for all 18 tracks end to end in the clean shot: every end, every interruption, poly under
tracks. Done with a new tool, `tools/bd1_audit.py 13040 14700 13700 16740` (every trace file loaded), which
compares what is drawn with the photos and prints four lists, and a second, `tools/bd1_sheet.py`, which puts
the four shots of each listed spot side by side so that a list is looked at in one read:

1. **Breaks** (a drawn thin metal with no metal in either metal shot along 14 px or more, across its width):
   11 candidates, 9 of them the rings of drawn contacts. The other two, (13564,16421) and (13693,15185), are a
   poly row crossing under the track (clean shot: the row salmon and unbroken under the metal, pink field above
   and below; sheet `sh3`). **No break.**
2. **Undrawn metal**: one piece, (13290-13311, 16652-16709): track k4's continuation (below).
3. **Contact holes in the clean shot under drawn thin metal, against the drawn contacts.** Above y 16470: every
   hole of 100 px2 or more is a drawn contact. Eight smaller spots (30-103 px2) with no drawn contact were looked
   at (sheets `sh1`, `sh2`): (13127,14877), (13127,15398), (13520,15895), (13178,15918), (13589,16188),
   (13618,16182), (13215,16434) are a notch or speck on a poly band's edge, a gap ring between two metals, or
   dust, with the metal bright and unringed in both chips; (13630,15999), where `bd1_k`'s poly row passes under
   `rst_a`'s metal, has an olive-brown band in the clean shot (150/128/52), but the clean shot's colour does not discriminate on
   this row (plain crossings at (13630,16195) and (13716,16628) are olive too; the salmon 215/159/112 forty px
   east that this note first cited as the control is `bd1_k`'s own pad, not a crossing: corrected by review
   round 1). What decides it: the band is not widened into a pad in any of the four shots, chip 2's metal shot
   shows only the row's two edge bars (y 15985-15988, y 16009-16012) as at the next crossing west, and neither
   chip has a ring: **no contact**, as drawn. Four drawn contacts had no olive hole,
   (13567,15281), (13520,15455), (13629,15673), (13629,16235): each is a plain pad with ring and bright centre in
   both metal shots and a red-brown box in the clean shot (`sh2`): real. Below y 16470 the clean shot has
   interference colours under the tracks (green and pink bands: `sh4`), so its "holes" there mean nothing; the
   six largest and the six strongest ring candidates of both metal shots (`cache/scratch/busc/rings.py`, now
   `tools/busc_rings.py` on branch `busc`) were looked at (`sh4`, `sh5`): plain tracks and plain crossings of the
   poly rows, except one real pad, (13628,16626) (below).
4. **Poly gaps** (field colour inside a drawn thin poly): one candidate, (13687,14955) on `wr_r2`'s row: the row
   is orange and unbroken in both metal shots and chip 2's stripped shot (`sh7`). **No gap.**

**Found as drawn**: all 18 tracks, their jogs, ends and contacts, and the poly rows under them, within the
region. `k8`'s "23 px break" at y 16594 is the pair of dark edges where it crosses the wide poly row
y 16520-16560 and `eof`'s row y 16590-16612 (sheet `sh6`); the metal is one piece.

**Added:**

- **k4 (`rc_eq_r6`) south of y 16500**: the metal runs on down x 13304 (10-12 px of bright metal about x 13302)
  to y 16690 and turns south-west along a diagonal (x + y = 29997; `cdp4_track.py`), to (13259,16738) at this
  run's edge. Chip 1's metal shot has a dark blemish on it at y 16604-16634; chip 2's is metal throughout
  (view `k4`, four shots). No pad on it.
- **One more load of `rst_a`** (`eof` run 8's lead): a pad with a contact (13628,16626) on `rst_a`'s metal
  x 13630 (ring and bright centre in both chips, the pad's box 13611-13645 x 16610-16642 in the clean shot), and
  its poly east along y 16620-16636 under X's line (x 13672: salmon, not widened, no hole) and `ck_out`'s metal
  (x 13716: olive in the clean shot, as plain crossings on this row are; edges unchanged, no pad, 9-11 px edge
  bars only in both metal shots, no pit in chip 2's stripped shot) with no contact, into the gate column: drawn
  to x 13760. It runs on: at x 13776-13800, under the narrow metal x 13774-13790, the row is bright salmon
  (228-248/150-179) over tan: probably a gate there (review round 1's lead; not drawn).

**Not covered**: the tracks' lower ends in the field of diagonals below y 16740 (`eof`'s claim at the time); the
audit does not test a contact on open diffusion beside a metal, and "no hole" under a metal is from the clean
shot only above y 16470.

### Leads for the gate column's lower part (x 13690-14100, y 16280-16900), seen in this run, NOT drawn, NOT reviewed

Under the ground rail (`tools/bd2_umap.py 13790 16270 13900 16910 5 6`): land y 16402-16440 with the rail's
contact (13831,16415) | band y 16444-16460 | land | band y 16488-16502 | land y 16512-16552 | band
y 16558-16572 | land y 16582-16626 | ... | land | band y 16696-16710 | land | band y 16744-16762 | land.
The band y 16488-16502 starts west on the pad of `ck_out`'s tap (13716,16495). **The band y 16444-16460 is fed by
`h_eq_r0half`** (review round 1's lead, checked: the `?P` row y 16410 that k5's contact (13348,16411) feeds does not
end at x 13700; in the gap between X's and `ck_out`'s metals it turns south, orange poly in both metal shots down
x 13694 from y 16404 to y 16456 with no ground between, into the band's west end; not drawn, because the band
is not). It passes under `ck_out`'s metal with no contact. The two bands' east ends are separate (field between
them at x 13865-13880, y 16465-16485). A narrow metal x 13774-13790 runs from a pad (13777,16357) south to
y 16772 over both bands without contact; the pad's poly goes east along y 16350-16362 under the rail. `ck_out`'s
"tap" (13716,16562) is the east end of the wide poly row y 16520-16560 that `trunks` draws from the pad
(13131,16562). East of the rail (x 13860-14000) the photos are at their limit even sharpened
(`tools/rdp3_sharp.py`); nothing there was read.

## Run 4 (2026-11-28): the lower gate column is a second latch, on R0-half's match

Tom Seddon, on Claude Fable 5.2, 2026-11-28 09:00 +0000. Claimed region x 13690-14100, y 15850-16900; the
output's wire is followed out of it (a follow task: to a net another package has drawn). 11 transistors; full
extraction 2,545 nets (was 2,541), 4,924 transistors (was 4,913), 0 errors, 0 warnings.

### Piece `lat2`: the column y 16340-16815 (traced)

**It is a copy of the latch on R4's match** (y 15385-15852, this file and `eof`'s pieces `r4lat` and `n2out`),
955 px south. `tools/t.sh bd1 findcell.py 13790 15440 14050 15840 --min 0.3 --region 13700,16250:14100,16950
--orient 0 --layer acid1b --cell x` gives one hit, offset (0,955), score 0.90 (0.85 in the metal shot, offset
(0,954)). Master and copy side by side (`tools/mosaic.py 13735 15380 325 480 --offsets "0,0 0,955"`, in the
chip-2 stripped shot, the chip-2 metal shot and the clean shot) show the same polys, diffusions, metals and
contacts, and eight colour points read the same in the four shots (`tools/px.py pt`: the block of the third
pull-down is poly in both, chip-2 metal blue 55-69 and chip-1 metal green 82-87; the band below it is diffusion,
red minus green 21 in the chip-2 stripped shot; the island west of the arm is field, -5). The geometry is the
master's lines moved 955 px south and fitted on overlays (sharpened clean shot at 3.9x, both metal shots at 1.7x
and 2.1x); every contact sits on a ring in both metal shots (one metal's last 60 px are seen in chip 2 only: Ambiguity 8).

```
h_eq_r0half_n   = NOT h_eq_r0half                                                  inverter B (firm)
eof_w16432      = NOT( h_eq_r0half AND ck_out  OR  h_eq_r0half_q )                 upper node N1 (marked: its load's tie)
h_eq_r0half_q   = NOT( h_eq_r0half_n AND ck_out  OR  eof_w16432  OR  rst_a )       lower node N2 (marked: both ties, the third pull-down)
```

A transparent latch of R0-half's match: while `ck_out` is high (CLK low) N1 is the inverse of the match and N2
the match; while `ck_out` is low both hold. `rst_a` (the reset copy) holds N2 low. What leaves the cell is N1,
the **inverse** of the latched match (in the master it is N2 that leaves).

Under the ground rail (x 13826-13870; `tools/t.sh bd1 railprof.py 13826 13870 16270 16920`): ground land with
the rail's contact (13832,16416) | gate P2 y 16443-16463 (`h_eq_r0half`) | strip | gate P3 y 16485-16505
(`ck_out`) | node N1 y 16507-16556 | gate G4 y 16557-16578 (N2's poly) | ground land, contact (13842,16607) |
field y 16651-16671 | node N2 y 16664-16700 | gate G5 y 16701-16721 (`ck_out`) | strip | gate G6 y 16746-16765
(`h_eq_r0half_n`) | ground land, contact (13842,16790). The rail ends at y 16815. North of the cell, y 16280-16340
is empty field (nothing leaves north).

Where the copy differs from the master (each read in the photos, not copied):

- **(a) The data is `h_eq_r0half`, from the west.** The row y 16410 that track k5's contact (13348,16411) feeds
  (run 1 drew it uncertain "to about x 13700") is one poly to x 13695: in the clean shot salmon under each of the
  five tracks it passes (x 13435, 13478, 13564, 13630, 13672) and dark red-brown in the gaps, in chip 2's metal
  shot orange in the gaps (blue 58-69) (`tools/t.sh bd1 px.py row 16411 13352 13566 5 acid1b,metal`; `row 16410
  13560 13700 6 acid,acid1b`); no field colour on it anywhere. In the gap between X's metal and `ck_out`'s it
  turns south (x 13688-13702, y 16402-16462: orange in both metal shots with blue 49-70, no ground between;
  `px.py col 13695 16396 16466 4 metal,metal1,acid,acid1b`; view `a1`, four shots at 5x) into band A
  (y 16443-16463), which runs east under `ck_out`'s metal **with no contact** (`tools/t.sh bd1 textmap.py 13694
  16428 13738 16516 3`: over the band the clean shot is salmon with no hole and the metal shots have the two
  edge bars only, while the tap 40 px south has ring, bright centre and green hole), across the column as gate
  P2 and north again east of the rail as P4, the gate of inverter B (one poly: an L round the ground diffusion,
  as in the master). The row is now drawn firm.
- **(b) The two enable gates are on `ck_out`.** P3's pad (13717,16496) and G5's pad (13716,16715) lie under
  `ck_out`'s rail x 13703-13727 (`trunks`' metal; this file now requires `trunks`), each with ring and bright
  centre in both metal shots. `trunks`' contact (13715,16562) between them is the east end of its wide poly row.
- **(c) The clear is `rst_a`.** Run 3's tap row y 16620-16636 from the pad (13628,16626) runs on to x 13812 as
  the gate (bright salmon over tan under the metal x 13774-13792) of the pull-down on the strip under
  `h_eq_r0half_n`'s metal, as `rst_a`'s row y 15671 does in the master.
- **(d) N2 has no exit west.** The strip's lower segment has the master's buried contact (13768-13792,
  16654-16688), but the poly from it is a stub with a rounded west end at x 13749 (a closed box in both metal
  shots and the chip-2 stripped shot; in the clean shot pink field under `ck_out`'s metal at y 16668; no metal on
  it; views `w1a`, `w1b`, four shots at 3.3x; the mosaic shows the master's row running on west where the copy's
  box is closed).
- **(e) N1's poly runs on south**: piece `out2`.

### Piece `out2`: N1's wire to `eof_w16432` (traced; wiring only)

From the pad (13957,16695) at the foot of N1's metal the poly column x 13966-13986 passes the block (the gate
of N2's pull-down east of the rail) and, unlike the master's, goes on: south to y 16830, west along
y 16810-16830, south along x 13880-13900 under the metals of the bottom bundle (`wr_r7`'s, `wr_r5`'s, `wr_r3`'s,
`wr_r8`'s; salmon under each in the clean shot, orange between in both chip-2 shots, no pad: views `c1`, `c2`,
`o2`; `px.py col 13889 16830 17420 10`: red minus green 40-80 in the chip-2 stripped shot down to y 17150, field
after), west along y 17140-17156 between `wr_r8`'s and `wr_r9`'s metals (`px.py row 17148 13380 13900 10`: poly
from x 13890 to x 13715, bare ground west of it), south along x 13711-13729 down a channel of the bottom bus
field under about twenty bus metals with no pad (views `f1`, `f2`: clean shot and chip-2 metal at 1.9x) to **a
pad with a contact (13715,18078)** (ring and bright centre in both metal shots, a dark red box in the clean
shot: view `f3`, four shots at 3.4x). From the pad a thin metal runs south-west on a diagonal (x + y = 31777;
`textmap.py 13640 18090 13712 18150 3`) and west along y 18428 (`follow.py 13655 18120 S`: corner (13344,18430),
end (13148,18427); northwards it ends at the pad) to **a pad (13151,18427)** (ring, bright centre, green hole:
view `f4`). A poly row y 18420-18436 runs west under `ck_a`'s and `ck_b`'s metals and the wide supply metal
(`px.py row 18428 12780 13160 10`; view `hop`, four shots at 3x) to **a pad (12806,18428)**, the east end of a bus
metal y 18422-18436 that runs 2,000 px west to x 10806, where `eof`'s metal x 10811 turns into it (`eof`'s port
`eof_w16432` M (10850,18420-18440); `follow.py 12775 18428 W` runs through that corner and north to
(10808,16426)). The bus metal is one piece: `tools/tl5_tracks.py h 18429 10800 12815` finds no stretch of 25 px
without metal in both chips and no hole in the clean shot; its longest dark stretches (x 10840-10853 and
10856-10872, with two bright pixels between in chip 2) are the two edge bars of a 20 px poly column crossing
beneath; between them the metal is barely brighter than open poly (179-200/119-126/55-71 in chip 2 against 165-174/103-109
for the open poly just north; review round 2), and what shows it is that the metal's two edge lines (y 18416-18420 and
y 18438-18442) cross the column unbroken and dark in both chips, with the clean shot protected throughout (`textmap.py 10828
18414 10884 18446 2 --acid`; view `g1`, four shots at 4.1x); strips of the whole line in the chip-2 metal shot and
the clean shot at 2.4x (`tools/strips.py 10790 18395 2060 70 --n 4 --horizontal`) show five plain poly crossings
(x 10850, 10890, 11020, 11855, 12735), no pad and no branch.

So **`eof_w16432` is the upper node of this latch**: `eof_w15955` = NOR(`ck_out`, `eof_w16432`) (`eof`'s gate at
the head of the bottom-centre logic's east column; firm) is `h_eq_r0half_q` AND NOT `ck_out` while the latch
holds, i.e. the latched R0-half match passed while CLK is high, and `cdp4_w10808` = NOT `eof_w15955` carries it
12,000 px north to the top-right gate row (believed: where the half-line point is used, for the interlaced
field's vertical sync). `eof` found only gates on `eof_w16432`; this is its driver.

`tools/ports.py --prefix bd1`: the port `eof_w16432` M (10850,18420-18440) meets `eof`'s port of the same name at 0 px (the metals overlap; one net in the
full extraction). It is also listed against `eof`'s `eof_w17734` P (10897,18469), 33 px, names differ: **not a join**: that wire's poly column
(x 10885-10900) is one of the five plain crossings under the bus metal and ends on its own pad 35 px south of the line.

### Ambiguities of run 4

1. **N1's load tie** (13894-13940, 16478-16531) and 2. **N2's load tie** (13889-13922, 16599-16640): as in the
   master (this file's "Load tie of `bd1_n1`"; `eof`'s `r4lat`), a heavy-outlined box on the node joined to the
   load block's poly inside a dark complex whose shape is not resolved; drawn uncertain. On them rest: that the
   wire `eof_w16432` (firmly the gate of N1's load and of N2's east pull-down, by the metal contact (13956,16493))
   is the node N1, and that G4's poly (`bd1_q2`) is N2. `tools/unsure.py` lists both nets. The copy adds no
   evidence beyond the master's; a join the other way round is excluded only by the cell's sense.
3. **The diffusions of N2's pull-down east of the rail** (13868-13958, 16675-16788): uncertain as in the master.
   The arm and the band below the block read as diffusion and the island as field at the points measured.
4. **The dark line between the block and the column** (x 13952-13960, y 16737-16761): red 47-57 in both metal
   shots, as dark as the column's own west edge 25 px north (45-52), and red 93-100 in the chip-2 stripped shot,
   against 41-51 for that edge (`px.py row 16744 / 16748 / 16752 13944 13976 2 metal,metal1,acid`; control `row
   16722`). Read as the east edge of the diffusion under one poly (the diffusion column is x 13919-13957); the
   block has a rounded west end and closed long edges, so it has no other feed. The master has the same line and
   the same mark: the join is drawn `?P`.
5. **The wide supply metal over the poly row y 18428**: chip 2's metal shot has a dark spot at (12958,18426),
   about 15 x 12 px, chip 1's a dimmer one at (12947,18422); the two do not coincide, neither has a ring with a
   centre, and the clean shot shows the row salmon without a hole (`textmap.py 12880 18408 12998 18446 3 --acid`).
   Read as dirt: no contact. With a contact the wire would be tied to the supply.
6. **Crossings read as no contact** (none drawn uncertain): band A under `ck_out`'s metal (above); the row y 16410
   under five tracks (run 3's audit of the channel found no undrawn contact; not looked at again one by one);
   `out2`'s poly under the four strobe metals at x 13890 and under the bus metals down x 13720 (no pad on the
   poly, no widening of any metal: 1.9x and 2.5x views only); `ck_b`'s and `ck_a`'s metals over the row y 18428
   (3x); five poly columns under the bus metal.
8. **`h_eq_r0half_n`'s metal x 13773-13793 above its foot pad, y 16690-16750, is seen in chip 2 only** (review round 2).
   Chip 1's metal shot is dark there for 55 px (red 16-90) and its clean shot open green at y 16689-16701 and
   y 16725-16743; chip 2's metal shot has the metal to the pad (red 176-239, bars of 6-9 px where G5's band crosses)
   and its stripped shot the ghost (`textmap.py 13762 16680 13804 16770 3`). Read as damage on chip 1 (its two shots are
   of one die); the wire's last 60 px, and so G6's gate on the inverter's output, rest on chip 2. Drawn firm. In the
   master both chips show the metal.
7. `ck_out`'s metal between band A and the tap (y 16464-16490) is dark in chip 2 (red 64-130) and bright for
   10 px in chip 1; the clean shot is pink (protected) under it. One metal, as `trunks` draws it.

### Not done after run 4

- The dense group y 15850-16125 (`h_eq_r0`'s buried contact, `ck_out`'s tap (13716,15930), the VSS-tied bars):
  not looked at in this run.
- What `cdp4_w10808` does in the top-right gate row (`tr1`).
- The poly that the row y 18428 crosses was not searched for taps beyond the views named; the bus field's other
  lines beside it (y 18380-18470) are in no trace file.

## Run 5 (2026-11-28): the dense group is a latch on R0's match, and its output is a second input of X's driver

Tom Seddon, on Claude Fable 5.2, 2026-11-28 10:04 +0000. Piece `eol`, x 13740-14055, y 15860-16135 (the group that two
passes of run 2 and a look from the coordinating session left without a circuit) and what it joins in X's driver
below. 6 transistors in the extraction (four devices and the hold device; one pull-down counts twice because of an
uncertain strip); full extraction 2,547 nets (was 2,545), 4,930 transistors (was 4,924), 0 errors, 0 warnings.

### Piece `eol` (traced)

```
h_eq_r0_q    <- h_eq_r0  while ck_out is high         T1: pass transistor, 91/21 (35/21 if the land stops short of the bar)
h_eq_r0_q_n  =  NOT h_eq_r0_q                         G1 105/21 under the ground rail, load 34/37 (marked: the load's tie)
rst_a_n      =  NOR( rst_a, h_eq_r0_q_n )             G2 141/19, a second pull-down beside the existing one in X's driver
                                                      (marked: G2's gate is the load's plate, `bd1_q3`; the tie again)
h_eq_r0_q   <-> rst_a_n                               hold device 20/84, gate on vss (uncertain: the strip under the plate, and the
                                                      neck where its wire meets the contact box of X's metal)
```

**What it is.** A latch of the family of `rdp3_lat` (pass transistor, inverter, second inverter, weak hold device
whose gate is tied to VSS), built to order: `tools/findcell.py` finds no copy of that cell here (the coordinating
session's note of 2026-11-16, above), and the second inverter is not a gate of its own but **a second pull-down on line X's driver**.
So line X is not the plain inverse of `rst_a`: **`rst_a_n` = NOT `rst_a` AND `h_eq_r0_q`**, R0's match as passed
while `ck_out` is high (CLK low) and held while it is low, gated off by the reset. Its three inverters therefore give
`rst_ck` = `rst_rc` = `rst_lat` = `rst_a` OR NOT `h_eq_r0_q`: high during reset **and at every character except the one
for which the latched R0 match is high**, once per scan line, when they go low (if `h_eq_r0` is high on a match, as the
glossary has it: the comparator was not re-read here). This is the first traced use of R0's match. What it means for the lines named as reset copies
is in the handoff (their names, AMB-060, AMB-062, R56); nothing is renamed here.

**How it was read.** Sharpened views (`tools/rdp3_sharp.py`) at 3-7x of the four shots side by side, and every class
that decides a connection by colour profiles (`tools/px.py`) against controls read with the same command:
open poly (`h_eq_r0`'s row at (13740,15888)): chip-2 metal 178/119/59, chip-1 metal 130/74/35, chip-2 stripped
164/131/66; open field (13752,16010): 167/143/83, 141/119/74, 153/158/92; the narrow wire W (13775,16010):
169/130/82, 146/109/77, 165/140/86, a diffusion (the metal shot's blue and green are the field's, not poly's; the
stripped shot's red minus green is 25 against the field's -5). **East of the ground rail the clean shot's colours are
inverted** (trap 28, found in this very column): under X's metal it shows khaki where diffusion is expected and tan
beside the metal. There the classes come from the chip-2 pair and from the edge lines, and the clean shot is used for
edges only.

Under the ground rail, north to south (`tools/px.py col 13822 / 13843 / 13862 15944 16060 3 metal,metal1,acid1b`;
`tools/t.sh bd1 textmap.py 13740 15850 13900 16130 3 --acid`): field under the rail's first 30 px (pink) | bar L
x 13808-13830, y 15880-15944 (`ck_out`) and the strip of the storage node east of it | the node's foot
y 15946-15961 (tan 194/182/130 from x 13814 to x 13847, no hole) | the plate y 15967-16023 | field y 16024-16034
(pink) | D1 y 16040-16054 (the inverter's node) | gate G1 y 16056-16077 | ground land y 16079-16128 with the rail's
contact (13843,16108) | gate G2 y 16130-16149 | X's node (the existing diffusion).

- **The ground rail is one metal through the group** (x 13816-13870), not "two narrow lines": both metal shots are
  bright in every band between the edge bars of what lies beneath, and the clean shot is pink or protected under all of
  it. What looked like lines are the edges of bar L, of the strip and of bar R showing through. **It has two contacts
  here and no more**: (13870,15900) onto bar R (ring, 12 px centre in both chips, a green hole in the clean shot, a
  pitted patch in the chip-2 stripped shot) and (13843,16108) onto the ground land. **The bright spot (13821,15888) is
  not a contact**: the clean shot is salmon there with no hole (204/134/97; `px.py col 13819 15866 15900 2 all`), and
  it is the rail over the top end of bar L, which lies over field (traps 13 and 26). A contact there would tie `ck_out`
  to ground.
- **`ck_out`'s row and bar L are one poly.** `trunks`' metal x 13703-13727 ends on a pad with a contact (13713,15931);
  the row y 15923-15944 runs east and turns north under the rail's west edge. Along the row (`px.py row 15932 13786
  13836 2 all`) both metal shots are orange (chip-2 blue 57-68) without a dark line from x 13786 to the metal's own
  edge line x 13812-13816, where the control row above it (`row 15905`) has an edge at x 13800-13806; the clean
  shot's 6 px dip at x 13806-13810 is the edge of the rail's protected margin. This settles what the coordinating
  session asked first (its note of 2026-11-16, above): the row is not the neighbour of a VSS-tied bar, it is the bar.
- **T1.** `h_eq_r0`'s row (track k7's poly, y 15880-15898) ends on a pad in a nested, heavy-outlined box B1
  (13752-13796, 15872-15906): a buried contact onto a land that fills the inside of the L (plain to bar L's west edge
  line in both metal shots: view `t1m`). The L is the gate. Outside it lies the storage node `h_eq_r0_q`: the foot
  below the row, the strip x 13832-13852 east of bar L (closed by an arc at y 15895) and the wire W. Bar L's body is
  over diffusion (salmon 236-245 against 198-209 for its top end over field; the line across it at y 15890-15893).
- **The row from the track is now firm** (run 1 drew it uncertain "to about x 13700"): `px.py row 15889 13440 13762 6
  metal,acid,acid1b` has poly in every gap between the five tracks it passes (x 13476, 13520, 13562, 13630, 13672) (orange, chip-2 blue 48-68) and salmon
  under each; `tools/t.sh bd1 textmap.py 13460 15868 13690 15912 3` has each track bright across the row between the
  row's two edge bars, no ring and no hole; `tools/eof_tee.py h 15880 15898 13455 13750`: no branch.
- **W, B2, G1.** W runs south as a narrow diffusion wire x 13767-13785 (plain between two edge lines; classes above)
  to a second nested box B2 (13764-13802, 16040-16080), where the west end of a poly band lies on its land (the
  band's end orange at (13805,16066), the box's centre plain: view `b2`): the gate G1, y 16056-16077, east under the
  rail, through the gap and under X's metal to a rounded end at x 13934. In the gap x 13873-13900 between the rail and
  X's metal every band was measured (`px.py col 13889 15960 16062 3 all`, `col 13889 16062 16160 3`): D1 diffusion
  y 16041-16047, G1 poly, ground land diffusion y 16086-16098, G2 poly y 16110-16131, X's node below.
- **The inverter's node and its load.** D1 runs east under X's metal (tan in the clean shot, 193-198/151-184) and
  north-east into a narrow strip K2 (x 13937-13948) between X's metal and the load; the clean shot at y 16025 is one
  flat tan from x 13918 to x 13940 with no line (`px.py row 16025 13894 13962 2`), where both metal shots and the
  stripped shot have the line of the metal's own edge. D1's north-west edge is a diagonal line from (13905,16036) to
  (13930,16005). The load is a plate x 13954-13991, y 15994-16047 with the usual line across (y 16008-16012), a supply
  land east of it and a contact (14018,16025) on the column's VCC rail. K2 runs north beside the plate, unbroken, to a
  closed arc at y 15965 beside the plate's tie box. **K2 ends in the south at y 16046** (review round 3; the first
  drawing ran it on to a "small box" as a second tie): an edge line y 16044-16050 crosses it (`px.py col 13944 16034
  16060 2`), and between G1's end and the column, y 16053-16083, is field (`row 16066 13896 13972 2`: stripped shot red
  minus green -7 to -19 from x 13950; the reddish 6 px beside the line x 13934-13938 are its shading). The small
  ring-like box (13937-13953, 16087-16103) is the north-east tab of the ground land: the clean shot is one flat tan
  from under X's metal to x 13938 at y 16097 (`row 16097 13912 13964 2 all`: 190-192/178-183/133-138 with no line where
  both metal shots have the metal's own edge).
- **The plate's poly is G2.** It runs on south as a column x 13966-13990 and at y 16107-16129 turns west as a band:
  east of the rail at y 16107-16129, a step down in the gap, under the rail at y 16130-16149, and a west arm with a
  rounded end at x 13763 (views `x1b`, `q1`, `q2`; open poly in both metal shots, `px.py col 13797 16084 16162 3 all`).
  Under the rail and east of it the band lies between the ground land and X's node: a pull-down of X, as far east as
  the land's own edge, the dark line x 13950-13954 that crosses the band. **The column
  ends at y 16128**: below it are 12 px of field (`px.py col 13972 16040 16200 3 all`: chip-2 stripped 120-158/125-160,
  red minus green 0 or less, both metal shots plain, y 16136-16145) before the tie box of X's own load, so the plate
  is not on X's net. The block north of the west arm (13778-13825, 16101-16123) is plain, a diffusion (stripped shot
  16-23): the ground land's west end.
- **X's metal** (the `?M` of run 1, now firm): from the driver's contact (13917,16155) north on x 13905-13927 to a
  contact (13926,15917) on a diffusion box E (13907-13958, 15892-15945; pits in both stripped shots). Between its two
  contacts it shows edge bars only, in both chips (`textmap.py 13896 15948 13938 16150 3`).
- **The hold device.** Bar R runs from its contact down the rail's east side into a plate x 13791-13875,
  y 15967-16023 under the rail (its north edge west of the rail is at y 15977; one poly with the bar: salmon without
  a break at y 15976-15985). Two lines cross the plate, at
  y 15987-15990 and y 16010-16013, and the band between is brighter: the three "fingers" of the earlier passes. As in
  `rdp3_lat` (`notes/blocks/rdp3.md`, "Hold device": the same proportions, 22/82 there) this is one poly with the
  edges of a diffusion strip showing through; gaps of 3 px are far below any spacing rule. The strip is seen at both
  ends: against W in the west (one 6 px line between W's plain and the plate's orange, `px.py row 16000 13762 13826
  2 all`) and in the gap east of the rail, where y 15990-16005 is a diffusion (chip-2 metal 158-175/122-134/80-89,
  stripped 145-161/124-137) with field below (y 16017-16029, stripped red minus green 0). **From that block a narrow
  diffusion runs north in the gap between the rail and X's metal** (x 13889-13897; `px.py col 13893 15920 16000 3 all`:
  plain and unbroken from y 15932 to the block in both metal shots, 136-165/105-118/69-81 in chip 2, the stripped shot
  17-47 redder than green; `row 15970 13876 13912 2 all`) to the south-west corner of box E, where the box's outline
  is weak (`row 15934 13878 13920 2 all`: a dip to 72-86 at x 13908-13912 against 30-45 for the outline elsewhere).
  This is review round 3's finding: the first drawing had the wire as a column under X's metal, where there is no
  diffusion (box E is closed along its south side by an edge bar y 15943-15947).

### Ambiguities of run 5

1. **The hold device's strip under the plate, and the neck at box E** (two `?D` items: x 13780-13886, y 15990-16010
   under the plate; the neck (13894-13910, 15927-15939)). The strip is seen at both ends and not under the plate
   (edge lines and a brighter band only, as in `rdp3_lat`). East of the rail its wire is drawn firm: the block in the
   gap and the narrow diffusion north to box E's south-west corner (measured, above). At the corner one weak line
   (red 72-86 against 30-45 for the box's outline) lies between the wire and the box: read as the edge of the
   contact's pad showing through, with the diffusion going on. **Read: the hold device is between the storage node and
   `rst_a_n`**, the level the node itself produces (a positive loop: node high, `h_eq_r0_q_n` low, X high). If the
   neck were closed the wire from the strip would end nowhere and box E would have no way out. What would settle it:
   the simulation (does the latch hold while `ck_out` is low); these photos give no more. (The first drawing's column
   "K1" under X's metal is withdrawn: review round 3.)
2. **The plate's tie to its node** (`?B`, `?P`, `?D`): a box of the usual size (13952-13980, 15960-15989) at the
   plate's north end beside K2's arc; its centre is orange in chip 2 and plain in chip 1 (92/82/77, the reviewer's
   reading: a buried contact's centre, trap 24). Whether K2 enters the box is not seen. That `bd1_q3` (the plate, the
   column and G2) is the node `h_eq_r0_q_n` rests on it alone (`tools/unsure.py` lists the net); a depletion load's
   plate is on its own node by construction, and the plate has no other source: its column ends in field, and the
   small box at the foot of the column, first drawn as a second tie, is a tab of the ground land (above).
3. **Whether the land of B1 reaches bar L** (one edge line at x 13800-13806 against the bar, read as the bar's own
   edge with the diffusion going on beneath). If it stops short, only the row gates T1 (35/21 and not 91/21) and the
   bar lies on the storage node as a capacitor. The connections are the same.
4. **No poly between the plate and G1's west end.** The chip-2 stripped shot is strongly red on a line x 13794-13800
   from y 16027 to y 16048, between the plate's south-west corner and box B2, which would tie the VSS plate to the
   storage node. It is the shading of B2's outline: `px.py row 16033 13782 13826 2 all` has 4-6 px of dark red and then
   field from x 13802 (stripped 153-162/143-160), no orange 14 px wide.
5. **The ground land's west end and G2's west arm** (`?D` 13778-13820, 16118-16165): a channel under the arm west of
   the rail, between that block and X's diffusion there (the reviewer: the diffusion's edge line crosses the arm at
   x 13775); it changes G2's width only.
6. **A dark oval at (13833,15948) in chip 1's metal shot only**, over the storage node's foot: the bar of the foot's
   upper edge (`textmap.py 13812 15938 13856 15966 2`: no ring; the clean shot flat tan, no hole). No contact.
7. Crossings read as no contact, none drawn uncertain: the rail over bar L, the foot, the plate, G1 and G2; X's metal
   over the diagonal, G1, the ground land and G2; the five tracks over `h_eq_r0`'s row.

### Not done after run 5

- The gate column is traced from y 15100 to y 16815. Left in it: the load ties (uncertain in every unit), and the
  re-read of X's driver itself (y 16150-16280: run 1's geometry, with two `?D` items), which this run did not redraw.
- Whether `h_eq_r0` is high or low on a match (the comparator's cells: `rdp2`/`rdp3`), which decides whether the three
  lines are low or high in the character for which the match is latched.
- What `cdp4_w10808` does in the top-right gate row (`tr1`); the bus field's lines beside y 18428 (run 4's list).

## Review

### Round 1 (full review), 2026-11-27: run 3, the re-read of the channel (R1) and the two added wires

A fresh Claude Fable 5.2 agent, on commit 9611f93, 25 images in `cache/scratch/bd1/review-1/`. Told to suspect:
the lower zone y 16470-16740, where the clean shot has interference colours; (13630,15999); the tap
(13628,16626), its metal and its poly row; k4's continuation and the dark stretch in chip 1; the track ends;
the nested jogs. It took its own sample.

**No finding changes a connection.** Two findings on wording, both confirmed and fixed (a trace comment and the
notes; no geometry changed):

1. (13630,15999): the notes' control was mislabelled (the salmon patch cited is `bd1_k`'s own pad), and the clean
   shot's colour does not discriminate on that row. No contact stands on the other evidence (no widening in any
   shot, edge bars only). Notes corrected.
2. (13716,16628): the trace comment said "the same [salmon]" for the tap row under `ck_out`'s metal; the clean
   shot is olive there. Still no contact (edges unchanged, no pad, 9-11 px bars in both metal shots, no pit in
   chip 2's stripped shot). Comment and notes corrected.

Two leads outside the claims, both checked by me and written into the notes above, neither drawn: the tap row
runs on past x 13760 onto what is probably a gate under the narrow metal at about (13782,16628); the `?P` row
y 16410 (`h_eq_r0half`) turns south at x 13694 into the gate band y 16444-16460.

Checked and found correct by the reviewer: all 18 track positions by the two-chip test end to end
(`tools/tl5_tracks.py v`), every jog arm, and 1.9x surveys of the whole channel in three shots: no break, no
undrawn pad, no undrawn metal (19 cuts), no poly gap; the track ends k0, k6, k10, k12, k13, k14, k16, each on its
pad with bare ground beyond in both chips at 4x; the nested jogs (identities below them as drawn); every
crossing of the rows y 16520-16560, 16590-16612 and 16620-16636 at 4x in three shots (pads only where drawn);
the contact (13628,16626) (ring 12 / centre 14 / ring 12 px in both chips, pits in both stripped shots) on the
metal x 13630, which is continuous from the pad (13629,16235); the row past x 13672 without contact and without
a branch; k4 one metal to (13259,16738) with the turn at about y 16690, the dark stretch in chip 1 a blemish;
(13478,16594), (13564,16421), (13693,15185) plain crossings. Not checked by the reviewer: full-length 4x
strips of the tracks (text test and 1.9x surveys, 4x at flagged spots only); chip 1 is damaged over
x 13304-13521 below y 16520, so the evidence there is chip 2's two shots.

Connections before and after the wording fixes (commit 9611f93 against the fixed tree):

    tools/t.sh bd1 sameconn.py 9611f93            ->  connections identical
    .venv/bin/python tools/sameconn.py 9611f93    ->  connections identical

Recorded 2026-11-27 07:48 -0600.

Round 1: no findings that change a connection.

### Round 2 (full review), 2026-11-28: run 4, pieces `lat2` and `out2` and the row y 16410

A fresh Claude Fable 5.2 agent, on commit c22bbb7b, 17 images in `cache/scratch/bd1/review-2/`. Told to suspect:
any place where the copy differs from the master unnoticed; the row y 16410 (made firm from centre-line profiles);
the turn and band A under `ck_out`'s metal; the two stubs; the join of the block to the column; on `out2` every
corner, the leg x 13880-13900 at y 16900-17050, `rst_a`'s column against the corner (13720,17148), the channel
x 13710-13730 (read at 1.9x), the three pads, the diagonal, the row under the wide supply metal, the bus metal
(the dark stretch x 10840-10872, two metals end to end) and the join with `eof`'s metal.

**No finding changes a connection.** Three remarks, each checked by me:

1. (13773-13793, 16690-16750): `h_eq_r0half_n`'s metal above its foot pad is absent in chip 1 (metal shot dark,
   clean shot open green) and present in chip 2 (metal shot and the ghost in its stripped shot); the notes' "both
   metal shots" did not hold there. **Confirmed** (`textmap.py 13762 16680 13804 16770 3`: chip 1 red 16-90 for
   55 px, chip 2 red 176-239 between bars). Geometry unchanged (drawn firm on chip 2's two shots); recorded as
   Ambiguity 8 and in a trace comment. Not a connection change.
2. (10840-10872, 18429): over the poly column the bus metal is barely brighter than open poly, weaker than "dim
   but present"; what shows the metal is its two edge lines crossing the column unbroken in both chips.
   **Confirmed** (my own text map of the spot shows both lines); the notes' wording corrected. Not a connection change.
3. (13827-13873, 16635-16657): "the ground land under the rail has a narrow tail to y 16657 (drawn to 16635); one
   dark line (y 16660-16666) separates it from N2". **Not adopted**: `px.py col 13835 / 13848 / 13860 16626 16670 3
   acid1b,metal,metal1` has the land's tan (197-205/170-178/117-135) end at y 16631 on a dark line y 16635-16638 in
   all three shots at all three columns, and the band y 16641-16659 below it pink or olive (162-188/131-134/116-121;
   129-155/148-155/95-123), not tan: it is the field band the master has at y 15682-15706, between two dark lines.
   Either way geometry only: the band does not reach N2.

Checked and found correct by the reviewer (4x or more, or text maps, in two to four shots): the row y 16410 (poly
in every gap in four shots at 4 px steps; under each of the five tracks no pad, hole or ring; `tools/eof_tee.py`:
no branch); the turn (a corner, not a T) and band A under `ck_out`'s metal with no contact; both stubs dead ends
(pink field under `ck_out`'s metal at y 16670, bare ground west of the stub; N1's stub a closed box clear of band B
and of `trunks`' pad); both gap diffusions (`eof`'s tests, field control at y 16645); P4's cap clear of the output
bar, G5 and G6 clear of the block, G4 continuous into the band; `ck_out`'s metal one piece through its three
contacts; master and copy the same but for the known places (mosaics in three shots, a text difference map); the
block's join the same single 8 px line as the master's; on `out2` every corner a corner, the row y 16810-16830
clear of the pad (13957,16860), the leg x 13880-13900 continuous with three plain crossings, `rst_a`'s column
ending about 40 px short of the corner, the channel x 13710-13730 continuous with no pad and no widening (a 3 px
text map of all 940 px), the pad (13715,18078) not joined to the bus metal above it, the diagonal continuous in
chip 2 (dirt on chip 1 at x 13452-13476), both pads at y 18428 real, the spot on the supply metal dirt, the bus line
without hole or branch (both edge lines dark from x 10880 to x 12790). Not checked by the reviewer: the two load
ties (`?`); the N1 and N2 diffusions under the rail's east edge (cannot be seen there); the bus line beyond its west
end by text tests only.

Connections before and after the fixes (a trace comment and the notes; commit c22bbb7b against the fixed tree):

    tools/t.sh bd1 sameconn.py c22bbb7b            ->  connections identical
    .venv/bin/python tools/sameconn.py c22bbb7b    ->  connections identical

Recorded 2026-11-28 09:58 +0000.

Round 2: no findings that change a connection.

### Round 3 (full review), 2026-11-28: run 5, piece `eol`

A fresh Claude Fable 5.2 agent, on commit b624423a, 19 images in `cache/scratch/bd1/review-3/`. Told to suspect: the
spot (13821,15888); the junction of `ck_out`'s row with bar L; B1 and its land against the bar; W's layer; G1's east
end and its stretch in the gap; D1 into K2 and K2 against the column under X's metal; the column's south end, G2's
join to it, its step and its west arm; the two tie boxes; the hold device altogether (bar R and the plate, the three
bands, the strip, its east end, box E's exits); the red line beside B2; other contacts on the rail and on X's metal;
the tracer's distrust of the clean shot east of the rail; anything left out.

**No finding changes a net or an equation.** Two findings moved or removed uncertain items, each checked by me and
confirmed; because one removes a drawn (uncertain) buried contact and the other re-routes the hold device's wire, they
are treated as changing a connection and go to a fix check:

1. **The wire from the hold strip to box E is not under X's metal.** The trace had a column `?D` (13908-13927,
   15940-16012) south from box E. The reviewer: box E is closed along its south side (an edge bar y 15943-15947 in both
   metal shots), opens at its south-west corner (y 15929-15937, a dip to 72-76 against 30-45), and from there a plain
   strip x 13889-13897 runs south in the gap between the rail and X's metal into the strip's block (13882-13898,
   15992-16008); under X's metal there is no diffusion. **Confirmed** (`px.py col 13893 15920 16000 3 all`: plain and
   unbroken from y 15932 to the block, 136-165/105-118/69-81 in chip 2, 131-157/93-131 in chip 1; `row 15934 13878
   13920 2 all`; `row 15970 13876 13912 2 all`). Redrawn: the block and the wire firm, the neck at the corner `?D`,
   the strip under the plate `?D` as before. The device is between the same two nets.
2. **The south "tie box" is not a tie, and K2 ends at y 16046.** The trace had K2 running south to a `?B`
   (13935-13956, 16085-16104) under a `?P` tab. The reviewer: an edge line y 16044-16050 crosses K2; x 13938-13962,
   y 16053-16083 is field (stripped shot -7 to -19); the box is the ground land's north-east tab (the clean shot flat tan
   from under X's metal to x 13938, no west outline), and the line x 13950-13956 across G2's band is that land's east
   edge. **Confirmed** (`px.py row 16097 13912 13964 2 all`: 190-192/178-183/133-138 from x 13912 to x 13938 with no
   line; `col 13944 16034 16060 2`; my own `row 16066` had the field from x 13950 and I had taken the line's 6 px of
   red shading for the strip). Removed: K2's south part, the tab, the `?B`. Added: the land's tab and the channel under
   G2 to x 13950. `bd1_q3` is tied to `h_eq_r0_q_n` by the north box alone (uncertain, as before).
3. Geometry only, all taken: the plate's north edge west of the rail is y 15977 (drawn 15967 there); the uncertain
   diffusion under G2's west arm spans x 13778-13820 (drawn from 13797); K2's upper part is unbroken (now firm, with
   the tie box still uncertain); five tracks cross `h_eq_r0`'s row, not six (notes and comments).

Checked and found correct by the reviewer (4x or more, or text maps, in two to four shots): (13821,15888) no contact
(clean shot 204/155/108 with no hole, against 82/115/52 in bar R's hole); the rail one metal with two contacts;
`h_eq_r0`'s row without ring, hole or branch; B1 and B2 with plain centres; `ck_out`'s row into bar L (one edge line)
and the contact (13713,15931); W not poly; the storage strip and foot unbroken tan; the plate one poly with bar R; the
hold strip opening from W at y 15992-16008; D1 into K2 flat in the clean shot at y 16028; G1 poly in the gap and ending
at x 13936 or less; the column ending at y 16128 with field below; G2 continuous through the step; the red line beside
B2 an outline; the north box reading as a buried contact; no other contact on X's metal (`follow.py`, `textmap.py`);
the chip-1 oval a blemish; `tools/opendiff.py` finds nothing. Not checked by the reviewer: the diffusion under the plate
beneath the rail (edge lines and a redder band only); whether B1's land reaches the gate; whether K2 enters the north
box.

Connections before and after the fixes (commit b624423a against the fixed tree):

    tools/t.sh bd1 sameconn.py b624423a            ->  connections identical
    .venv/bin/python tools/sameconn.py b624423a    ->  connections identical

Recorded 2026-11-28 11:22 +0000.

Round 3: two findings, fixed.

### Round 4 (fix check), 2026-11-28: the corrections of round 3

A fresh Claude Fable 5.2 agent, on commit 87049ad1 against b624423a, 8 images in `cache/scratch/bd1/review-4/`. Told
what changed and why (the three findings of round 3), and to look at what the new firm diffusions touch: the wire in
the gap against bar R, its contact, the rail's bump and the plate's east edge; the tab and channel against G1's free
end, the column and G2's foot, the field south of the column and the lower load's tie box; the diffusion south of G2.

**No findings.** Checked and found right (profiles and views at 4x or more in two to four shots): box E's south
outline crosses under the vertical metal in all four shots (nothing leaves south); the strip x 13889-13897 plain and
unbroken from y 15933 to y 16005 in both metal shots, its blue too high for poly against G1 and G2 in the same gap, and
pinker than the field at y 16017-16030; the neck open, the dip at x 13908-13912 weak in both metal shots (75 against
28-36) and absent in the chip-2 stripped shot, `?D` appropriate; the new firm diffusion clear of bar R, its contact, the
bump and the plate; K2 ending on the line y 16044-16050; x 13940-13962 at y 16068 one plain region, greenish in the
stripped shot (field); the tab not poly, the clean shot flat tan from under the metal to x 13938; tab, the line across
G2 and the patch south of G2 (x 13938-13950, y 16135-16147) sharing one east edge at x 13952-13956; the new diffusion
clear of G1, the column and the lower tie box; the three geometry items. Both `tools/sameconn.py` runs against b624423a:
connections identical.

Recorded 2026-11-28 11:35 +0000.

Round 4: no findings.
