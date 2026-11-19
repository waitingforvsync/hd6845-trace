# bd1: logic and routing channel left of the register-select gates (x 13000-14100, y 14700-17100)

Trace: `trace/bd1.txt` (`@requires sel`, `@requires bd3`). Coordinates are metal-shot pixels.

## Status

- Traced, extracted (0 errors, 0 warnings) and checked by overlay: the route of every write
  strobe that enters the region (R0 to R7 leave north on the track bundle, R8 west in poly);
  the two big inverters on line X; X's driver; and, new in the second run, **the gate column
  from y 15385 to 15850**: an inverter, the pull-down networks of both halves of a latch
  (one half complete with its load and output line), and the pull-down that `inh_src` gates.
- **The region is mostly a routing channel**: 18 vertical metal tracks (x 13088-13826) with
  poly cross-unders. The gates are a single column at x 13700-14080, y 15100-16900.
- NOT traced: the second latch half's load east of the ground rail (y 15640-15705), the
  gate column at y 15850-16125 and 16280-16900 (everything
  `ck_out` feeds), and the lower ends of several channel lines. See Not done.
- Tracks k7, k8, k9, k11, k15 are traced from the north edge to their first contact (k8: as
  far as it runs straight); `inh_lat` and `bd1_k` are followed through the channel.

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
| Ground rail of the gate column | x 13826-13870, y 15100 to about 16760 | between y 15833 and 15991 it is replaced by two narrow lines (not traced), so the lower part is named `vss` from its pull-downs only |
| Supply rail of the gate column | x 13997-14044, y < 16960 | `vcc`: every load of the column ends on it. By scan it is continuous from y 14600 to 16960, where bd3's wide rail (y 16907-16954) arrives |
| Inverter pair on X | x 13765-14050, y 15120-15350 | two inverters, one ground contact between them (13838,15237) |
| Inverter A | x 13860-14045, y 15385-15512 | `bd1_an` = NOT `rc_eq_r4`; pull-down east of the rail (gate P4), load block x 13936-13992 |
| Latch, upper half | x 13700-14050, y 15468-15690 | node `bd1_n1`; pull-downs under the rail (P2, P3, G4), load block x 13938-13992, y 15523-15608 |
| Pull-down of `bd1_k` | x 13773-13804, y 15634-15730 | strip under `bd1_an`'s metal, gate = `inh_src` |
| Latch, lower half | x 13797-13990, y 15705-15852 | node `bd1_n2`; pull-downs G5, G6 under the rail and a third (gate `bd1_n1`) east of it |
| (not traced) | x 13876-13995, y 15640-15705 | N2's load and the driver of `bd1_q` |
| (not traced) dense group | x 13740-13960, y 15880-16125 | `ck_out`'s tap at (13716,15930) enters here; several gate bars 20 px apart under the rail; a metal from X's driver ends here at a contact near (13928,15916) |
| X's driver | x 13760-14050, y 16125-16280 | one inverter; input poly arrives along y 16231 |
| (not traced) | x 13700-14050, y 16280-16900 | gates; `ck_out` taps at (13716,16490), (13716,16565), (13715,16711) |
| ck_out rail | x 13703-13727, y 15930-16711 | drawn in trunks.txt, not here |
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
is distributed over the whole die). Here it is `inh_n`.

```
inh_n   = NOT inh_src       X's driver, y 16125-16280
inh_rc = NOT inh_n       upper inverter, gate bar y 15183-15203
inh_lat = NOT inh_n       lower inverter, gate bar y 15271-15291
```

- **X's driver** is one inverter. Pull-down: gate poly `inh_src` crossing the diffusion
  under the ground rail diagonally (x 13817-13888), ground contact at (13855,16250).
  Output diffusion above the gate; it reaches X three ways: a buried contact at
  (13762-13800, 16170-16210) to the tap poly that runs west to the contact (13672,16190)
  on X's metal; a metal contact at (13917,16155) to a line going north into the dense
  group (ends at a contact near (13928,15916), not traced); and a strip down the west
  side of the load. Load: poly block x 13953-13991, y 16140-16265, tied to the output by
  a buried contact at its top (13953-13985, 16142-16174), supply contact (14017,16228).
  W/L of the load 68/37; of the pull-down 90/24 as certain, up to 188/26 with the two
  uncertain pieces (Ambiguities).
- `inh_src` is on a metal line at x 13630 with a contact at each end. Top end,
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
- `inh_rc` leaves west in poly (buried contact 13766-13798, 15144-15173; poly along
  y 15151) to a contact at (13347,15150) where **track k6 ends: it goes north**.
- `inh_lat` leaves west in poly (buried contact 13766-13797, 15303-15333) to a contact
  at (13695,15325); metal south to (13700,15452), where one arm goes to a contact at
  (13655,15453) (poly west along y 15455 to a contact at (13520,15458), then metal south
  on x 13521 to a contact at (13520,15931) and on, see "Tracks") and the other runs south
  on x 13716 with contacts at (13717,15541) and (13716,15760): the gates P3 and G5 of the
  latch below (next section).

Believed: X, S (= NOT X, made by input-row gate 0), `inh_rc` and `inh_lat` are four
separately buffered copies of one clock-like signal `NOT inh_src` and its inverse; all
three inverters here are the same size.

### Gate column, y 15385-15850: an inverter and a latch gated by `inh_lat` (traced, second run)

```
bd1_an = NOT rc_eq_r4
bd1_n1 = NOT( rc_eq_r4 . inh_lat  +  bd1_q )                     upper half, complete
bd1_n2 : pull-downs  bd1_an . inh_lat  +  bd1_n1  to vss       lower half; its load is not traced
bd1_k  : pull-down  inh_src  to vss (source connection uncertain; its load is not in view)
```

Under the ground rail one diffusion column carries, top to bottom: vss contact (13832,15461),
gate P2 (y 15488-15508, `rc_eq_r4`), a strip 18 px tall with no contact, gate P3 (y 15530-15550,
`inh_lat`), node N1 (y 15552-15601), gate G4 (y 15602-15623, `bd1_q`), vss contact
(13845,15657); then field (y 15682-15706); then node N2 (y 15709-15745), gate G5
(y 15746-15766, `inh_lat`), a strip, gate G6 (y 15791-15810, `bd1_an`), vss contact
(13842,15832).

- **`rc_eq_r4`** enters from the north on track k15, jogs west at y 15087 to k13's position
  (x 13652), contact (13655,15391), poly east and south along x 13723 under
  `inh_lat`'s metal, east along y 15498 across the column (P2) and north again east of
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
- **`inh_lat` (NOT X) gates P3 and G5**: its metal on x 13716 has contacts at (13717,15541)
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
- **`inh_src`'s transistor.** The poly along y 15671 crosses a diffusion strip x 13773-13804
  that lies under `bd1_an`'s metal without touching it (31/20) and ends at x 13805. Below
  the gate the strip has a buried contact (13768-13792, 15699-15733) to a poly that goes west
  along y 15713 to a contact at (13674,15715): `bd1_k`, a metal line on x 13674 south to a
  contact at (13674,15973). Above the gate the strip is a closed box (y 15634-15660) with
  no contact; it is read as joined to the ground diffusion under the rail through the gap
  between the two metals (`?`, Ambiguities).

Believed (not traced): `bd1_q` = `bd1_n2` (so `bd1_n2` = NOT(`bd1_an` . `inh_lat` + `bd1_n1`)
with `bd1_q`'s band as its load gate).
That makes the pair a transparent latch of `rc_eq_r4`: while `inh_lat` is high (X low,
`inh_src` high) `bd1_n1` = NOT `rc_eq_r4` and `bd1_n2` = `rc_eq_r4`; while it is low both hold.
The layout supports it (the two halves mirror each other; `bd1_n1`'s line ends beside
N2; the band of `bd1_q` lies where N2's load would be), but the wiring that would prove
it (N2's load and the buried contact beside `bd1_q`'s band) is the untraced part. Neither `ck_out` nor any trunk clock reaches this latch: its
gate is `inh_lat`, the inverse of line X.

### Tracks traced so far

| Track at y 14700 | Net | What happens to it |
|---|---|---|
| k0 13088 | wr_r6 | ends at contact (13088,14867) |
| k1 13131 | wr_r5 | jogs to x 13088 at y 14912, down to contact (13085,15563) |
| k2 13174 | wr_r7 | jogs to x 13218 at y 15390, down to contact (13218,16642) |
| k3 13218 | wr_r3 | jogs to x 13261 at y 15346, down to contact (13262,16456) |
| k4 13261 | rc_eq_r6 | jogs to x 13304 at y 15308; by scan runs on past y 16700 |
| k5 13304 | h_eq_r0half | jogs to x 13348 at y 15262, down to contact (13348,16411); poly east along y 16410 towards the gate column (seen to x 13700 at 0.9x, not followed) |
| k6 13348 | inh_rc | ends at contact (13347,15150) |
| k7 13391 | h_eq_r0 | jogs to x 13435 at y 15176, down to contact (13432,15888); poly east along y 15889 under five lines into the gate column's dense group (seen to x 13695) |
| k8 13435 | h_eq_r1 | jogs to x 13478 at y 15130, runs south; by scan metal to y 16594, a 23 px break, then to y 16797. Lower end not traced |
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
| x 13435 | h_eq_r0, then **inh_lat** | k7 to (13432,15888). A new line starts at contact (13432,15955) and runs south (scan: to y 16769, lower end not traced): it is `inh_lat`, see below |
| x 13478 | h_eq_r1 | from the jog south |
| x 13521 | hc2, then **inh_lat**, then **bd1_k** | k9 to (13520,15390). Break. (13520,15458) to (13520,15931): `inh_lat`. Break. (13522,15999) south (scan: to y 16273, lower end not traced; a further piece y 16445-16805 is wr_r3's): `bd1_k` |
| x 13674 | bd1_k | (13674,15715) to (13674,15975) |

**Where `inh_lat` goes** (all traced except the last line's lower end): contact (13695,15325),
metal to (13700,15452); one arm south on x 13716 to the latch's gates P3 and G5; the other
arm contact (13655,15453), poly west, contact (13520,15458), metal south on x 13521,
contact (13520,15931), poly pad with a tail west along y 15959 under k8's line, contact
(13432,15955), metal south on x 13435 towards y 16769.

**Where `bd1_k` goes**: contact (13674,15975), poly west along y 15997 under `inh_src`'s and
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
| inh_rc | metal | 13348,14700 (north) | out | track k6: NOT X |
| h_eq_r0 | metal | 13391,14700 (north) | ? | track k7; ends on a poly going east along y 15889 into the dense group of the gate column |
| h_eq_r1 | metal | 13435,14700 (north) | ? | track k8; runs south past y 16590 (lower end not traced) |
| hc2 | metal | 13478,14700 (north) | ? | track k9; ends at contact (13520,15390) |
| hc2 | poly | 13035,15497 (west) | ? | k9's poly, into the mid-right array (`?`: route from the first run) |
| inh_lat | metal | 13435,16769 (drawn to there) | out | NOT X going south on k8's position; lower end not traced |
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
| inh_n | metal | 13672,16610 (drawn to there) | out | line X; trunks.txt draws it from y 16600 south. Not labelled in trunks.txt: it reaches inrow's `inh_n` |
| inh_n | metal | 13922,15905 (`?`) | ? | from the driver's output north into the dense group |
| inh_src | poly | 13805,15671 | - | ends as the gate of `bd1_k`'s pull-down (inside the block) |
| inh_src | poly | 13480,17150 (south) | in (believed) | X = NOT g; g has no driver in this region. Seen to y 17145, going south |
| bd1_q | poly | 13996,15640 | in (believed) | east end of the band y 15630-15650; driver not traced (believed `bd1_n2`) |
| bd1_n2 | diffusion | 13930,15705 | ? | N2's arm east of the rail, continuing north to its load (not traced) |
| vss | metal | 13910-13958, 14700 (north) | - | wide rail; named from the pull-downs it feeds |
| vcc | metal | 13997-14044, 14700 (north) | - | supply rail; joins bd3's wide rail at the bottom (by scan) |
| ck_out | metal | rail x 13703-13727, y 15930-16711 | in | trunks; its taps are not traced here |

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
  `inh_src`'s gate has no contact (metal 19 px wide there, no ring, `acid1b` smooth). In the
  28 px gap between `bd1_an`'s metal and the rail, at y 15634-15650 the colour map shows
  khaki with a dark blob and no green strip, as at the strip between P2 and P3 where
  diffusion certainly crosses the same gap; from y 15652 down the green strip of open field
  appears. So the segment is read as joined to the ground diffusion (drawn `?D`). If it is
  not, the device is only a capacitor between `inh_src` and `bd1_k`.
- **The dead-end poly on N1's west buried contact** (13749-13799, 15575-15597). Poly in
  the open, 24 x 27, with nothing leaving it (three shots at 6x). A C-shaped outline round
  it reaches up to P3's lower edge at (13768,15560); P3 is `inh_lat`, an inverter output,
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
- y 15880-16125 (dense group): `ck_out` tap (13716,15930), poly east along y 15930 to
  x 13830; under the rail several poly bars about 20 px apart (y 15975-16050); a load
  at x 13955-13990, y 16005-16045 with supply contact (14018,16025); a contact near
  (13928,15916) where the metal from X's driver ends. Two passes at 2.6x and 4x gave no
  consistent circuit; one sharpened view (2.9x) is much better and is the way in.
- y 16280-16900: untraced. `ck_out` taps at (13716,16490), (13716,16565), (13715,16711).

Channel:

- Lower ends, all in or near the diagonals at y 16560-16900: k4 (x 13304, past y 16700),
  k8 (x 13478; scan: metal to y 16594, break, to y 16797), `inh_lat` on x 13435 (to y 16769),
  `bd1_k` on x 13521 (to y 16273). Scan of x 13435 also shows metal at y 16812-16836 and
  16899-16964.
- Where k5's poly (y 16410) and k7's poly (y 15889) go in the gate column, and k11's poly
  from (13609,15608).
- Lines on x 13608 at y 16167-16224 and x 13565 at y 16251-16572 (scan only).
- The diagonals at x 13150-13450, y 16680-16890: three metal lines step two tracks east
  there (seen at 1.5x), wr_r7's poly passes under them.
- Bottom edge: a long vertical poly at x 13870-13885 passing under all the horizontal
  lines (y 16840-17150).
- wr_r9, wr_r11, wr_r10 west of x 14100 (they lie below y 17100).

## Gate column y 15860-16125: what a look from the coordinating session added (2026-11-16)

Not traced; these are observations to start from (views `g1a/g1m/g1o/g1b`, `h1a/h1b/h1m/h1o`,
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
- **`inh_n`** (line X) comes up from its driver to the contact (13925,15918) on a box
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
  `inh_lat` (`bd1_n1` = NOT(`bd1_q` OR (`inh_lat` AND `rc_eq_r4`))) and the input of inverter A
  (`bd1_an` = NOT `rc_eq_r4`). The latch's lower half, `bd1_q`'s driver and where `bd1_n1`, `bd1_n2`,
  `bd1_an` go are in the end-of-frame lead group (`eof` (e)).
