# tla: top-left logic, the gate cluster x 2450-3100, y 4600-5320 and its bus

Serial work, started 2026-11-15. Trace: `trace/tla.txt`. Views: `cache/scratch/tla/`.

## Names

In this note `in1`, `in2`, `in3`, `e3`, `e4`, `w2`, `c1`, `a2`, `b1`, `x1` are the signals
`rcs_in1` ... `rcs_x1` (`rcs_` = row counter step logic), `m2` is `rcs_cond_n`, and the
step signal is `rc_stepreq_n`. Bus line letters (A-G) and unit names are places, not signals.

## Status

Twenty-one gates and one latch traced and extracted (62 transistors, no errors) in the first and middle
clusters; the rest is surveyed only. The first cluster runs from y 2940 to y 5330. Added
2026-11-17: the west column y 3170-3590 (a selector and its inverter, below), the north end of
thin metal E, and a second transistor on `rcs_u3425` whose gate has no connection found.

**Run 2 (2026-11-28): the three units in the middle cluster's east column are re-read (R40)**: `rcs_mu` = NOT
`ra_eq_r9` has its load now and is firm, `rcs_in1` = NOT `rcs_mv` is firm, and three pull-downs drawn on field are
drawn where they are (units A and C are rail gates; unit B's column is x 4072-4108). See "Run 2" at the end; the
lines for `in1`, `rcs_mu` and `rcs_mn3852` in the table below are as first read and are superseded there.

**Run 3 (2026-11-28): the units on the columns beside R3 and R1 are re-read (R40's second half) and found as
drawn**: the fifteen pull-downs of the east column and the two of the west column are where this file has them, no
gate row runs on under a rail, and the one uncertain item among them, the VSS join at (3020,3500), is drawn firm
(`rcs_b1` is firm now). See "Run 3" at the end.

**Run 4 (2026-11-28): the cluster's rail gates are re-read (R23, R42)**: no connection changed; six pull-downs
changed width. The step gate's three are 69, 69 and 70 wide (were 52, 52, 38: the box under R3 runs on west to thin
metal E, and gate `in3`'s pull-down has a second part east of the rail); `rcs_w2` and `tla_w3505` under R1 are 44
(were 54, 57); the pull-down of `clk_tl`'s driver at (2626,7908) is 66 (was 52: a second part west of its rail). See
"Run 4" at the end.

**Run 5 (2026-11-28): the last rail-edge units are re-read (R23, R42, R32(b), R32(d)), and the gate called
`rcs_iso2958` has a feed.** Its stub turns west as a foot at the height of the arm of `rcs_b1`'s load plate and
reaches that arm's tie box: drawn joined through one uncertain piece, so **`rcs_u3425` = NOR(`rcs_bc3460`,
`rcs_b1`) (marked), a cross-coupled pair with `rcs_b1`** = NOR(`rcs_x1`, `rcs_a2`, `rcs_u3425`), as `tl3` reads
its mirror image of the pair (AMB-030). **The step formula below assumed that gate low and is superseded by the
one in "Run 5"** if the join is real. The transistor's diffusion link is firm now. The AND-OR-INVERT's stack under
gates g1 and g2 is one diffusion x 2971-3040 across the gap (69 wide; drawn 56), the two bands bent; same nets. See
"Run 5" at the end.

**Run 6 (2026-11-28): the six loads between R2 and R3 that were drawn as "the standard one" are read at their own
place (R32(c), R32(d), R30), and thin metal E is drawn in pieces (R41).** Five ties are as drawn (`rcs_c1`,
`rcs_u3288`, `rcs_cond`, `rcs_cond_n`, `rcs_in3`). **The sixth, `rcs_bc3460`'s, is built differently**: the tail, tab
and tie box drawn below its plate by analogy are not there (field), the plate is 33 px shorter, and the tie is a box
on the plate's top edge, on a tongue of the node strip that runs west under thin E. Same nets, same equation. Thin
metal E is uncertain (`?M`) at the ten places where neither metal shot shows it, so that the selector's gates are on
the wire from the far side of the die only through those. No connection changed. See "Run 6" at the end.

```
rc_stepreq_n = NOR(in1, in2, in3)        the row counter's step request (active low)   (2975,5035)
in2        = NOR(w2, e4)                 west column                                   (2571,5197)
in3        = NOR(e3, e4)                 east column                                   (3046,5197)
w2         = NOT c1                      pull-down under rail R1 itself                (2625,5066)
c1         = NOR(a2, b1)                 east column, top of the cluster               (3046,3115)
b1         = NOR(x1, a2, rcs_u3425)      east column; third pull-down west of the rail (3046,3590), (2920,3628)
rcs_u3425  = NOR(rcs_bc3460, rcs_iso2958) inverter; its output goes by a strap to b1's third gate. rcs_iso2958 is a
                                         gate poly with no connection found (2958,3481): see "The west column" below
                                         (run 5: its feed is believed to be rcs_b1's load plate: NOR(rcs_bc3460, rcs_b1))
tla_w3417  = NOT(rcs_thin_e AND tla_w3376 OR tla_w3505 AND amr_eq_r3)   west column, selector (2626,3418)
tla_w3505  = NOT rcs_thin_e              west column, rail gate under R1               (2626,3243)
rcs_u3288_n = NOT rcs_u3288              west column, top unit: rail gate with a strong load; drives thin metal W (2626,3112)
rcs_bc3460 = NOR(e3, e4)                 a second copy of in3's function               (3046,3892)
rcs_cond_n = NOR(in2, in3)               "m2": the step condition inverted              (3046,4765)
rcs_cond   = NOT rcs_cond_n              inverter on the column above; on bus piece A3   (3046,4636)
rcs_cond_lat <- rcs_cond while clk_tl  pass transistor latch (AMB-009)                (3046,4546)
rcs_u3288  = NOR(tl5_w2722, rcs_bd3330)                                                (3046,3288)
rcs_n4200  = NOT(rcs_cond AND clk_tl OR rcs_x1)   AND-OR-INVERT under the rail (3008,4200)
in1        = NOR(rcs_mu, rcs_mv)         middle cluster                                (4081,4072)
rcs_mu     = NOT ra_eq_r9              middle cluster, inverter                      (4050,3374)
rcs_mn3852 = NOR(?, in1)                 middle cluster; second gate not read
```

Put together, taking `rcs_iso2958` as low (b1 = NOT x1 AND NOT a2 AND NOT e3 AND NOT e4, so c1 = NOT a2 AND (x1 OR e3 OR e4)):

**step = in1 OR ( NOT e4 AND NOT (e3 AND a2) )**

and `m2` = e4 OR (e3 AND a2) is the complement of the bracket. `x1` cancels out of the step
(it still matters for `c1`, which also leaves the cluster westwards on the poly y 2985).
So: while `e4` is high only `in1` can step the row counter; while `e4` is low the counter
steps unless `e3` and `a2` are both high.

(Before the third pull-down of `b1` was found, on 2026-11-16, the formula read
`in1 OR (NOT e4 AND ((x1 AND NOT a2) OR NOT e3))`. That is superseded.)

What the inputs **are** is not known. None has reached a named signal yet:

| Signal | Followed to |
|---|---|
| `e4` | **17,000 px, all drawn, driver not found.** Bus line C middle piece (x 3196, y 3944-5677), east along y 5677, south at x 3527, contact (3565,5848), poly east along y 5847 to x 5285, south as line 5 of the poly bus x 5100-5290 to y 6850, diagonally to (5560,7122), east to a contact (6140,7124), metal east along y 7084, south at x 6769, contact (6730,8275), poly under six horizontal metals, contact (6730,8580), metal diagonally to x 6558, south down the left bus field (two steps west: x 6471 from y 9848, x 6300 from y 11880, x 6236 from y 12772), east at y 14528 to a contact (6411,14526), poly east to a contact (7012,14522), metal south to a contact (7055,15345), poly to the gate of a pull-down under the rail x 7290-7345 at (7317,15435) in bc1's untraced left column. **Five loads, all gates** (four in this cluster, one in bc1). See "The chase of e4" below |
| `e3` | bus line E, one piece y 2710-5166 with three contacts: (3283,5152) gate of in3; (3283,3852) a second gate (below); top (3283,2725), from which a poly runs east along y 2715-2735 to a pad (4270,2725) and a metal runs on **east along y 2718-2738** (pieces seen to x 5366; the three metals at y 2640, 2683 and 2728 run east in pieces, with cross-unders at the rails, as far as x 11700-12050, but tc1's notes show that pieces on one y are different nets) |
| `a2` | bus line A piece A2 (y 3166-3778): contacts (3108,3180) gate of c1, (3100,3632) gate of b1, (3103,3762) a poly that leaves **east along y 3752-3770** |
| `x1` | poly y 3538-3556 from the **east**, across the whole bus without a contact |
| `in1` | bus line G (x 3369, y 2754-4952), top contact (3368,2768), poly east along y 2768 to a contact (4225,2765), metal east and **south at x 4268-4290** (profile: unbroken to about y 4072; contact candidates at y 3898 and y 4090): into the middle or right gate column |

More of the east column (added 2026-11-16, extracted):

```
rcs_bc3460 = NOR(e3, e4)          unit at y 3892: a second copy of in3's function; its output
                                  goes up bus line C's upper piece to the unit at y 3425
rcs_u3425  = NOT rcs_bc3460       = e3 OR e4. An inverter: one pull-down, nothing above the node.
                                  Its load and its destination are in the dense part west of the rail
rcs_u3288  = NOR(tl5_w2722, rcs_bd3330)   unit at y 3288. Output up bus line C's top piece and west
                                  along y 2728 to about x 2822 (not looked at). tl5_w2722 comes from
                                  the east; rcs_bd3330 is a piece of bus line D (y 3330-4380)
```

Bus pieces now drawn: A1, A2, B (two pieces), C (top, upper, middle), D (y 3330-4380),
E (one piece y 2722-5158, three contacts), G upper.

**Where `in1` comes from (2026-11-16, extracted).** `in1`'s metal (bus line G of the first
field, the poly y 2768, then down the second bus field at x 4268-4290) ends on the output
of a unit of the **middle cluster** (x 3450-4110, the same construction 1042 px east: VCC
rail x 3824-3868, thin metal x 3948-3962, VSS rail x 3992-4041, units on a column east of
the VSS rail):

```
in1        = NOR(rcs_mu, rcs_mv)      unit at (4081,4072), with its load
rcs_mu     = NOT ra_eq_r9           inverter at (4050,3374): one gate, under the rail and on the column
rcs_mn3852 = NOR(?, in1)              the unit above in1's: in1 is one of its gates; output up x 4233 to y 2852
```

`rcs_mv` is a bus piece (x 4192, y 4112-4748) whose far end is a poly that leaves east and
south at (4283,4745); `ra_eq_r9` is a bus piece (x 4148, y 3320-3596). `e3`'s metal goes
east along y 2728 to x 4496, south to a contact (4490,3805), and on east in poly along
y 3805: towards the **right cluster** (x 4650-5050).

**What the step condition feeds (2026-11-16, extracted; one junction is AMB-009).**

```
rcs_cond     = NOT rcs_cond_n           = NOT e4 AND NOT (e3 AND a2): the bracket of the step formula
rcs_cond_lat <- rcs_cond while clk_tl is high      pass transistor: a dynamic latch
rcs_n4200    = NOT( rcs_cond AND clk_tl  OR  rcs_x1 )
```

`clk_tl` is **the clock**: NOT `ck_out`, i.e. CLK polarity (identified 2026-11-16 by
following it to its driver and the driver's input to the clock trunk; before that it was
the placeholder with the former name `rcs_bb3807`). Its route: bus line B (y 3807-4552; gate contacts at y 3810,
4160, 4410, 4548), a poly east onto a piece of bus line D down to (3240,5587), a poly west
along y 5587 under the cluster's foot to (2458,5587), a thin metal 2,240 px south at
x 2457 to (2456,7822), and a poly into the output node of an **inverter** at (2626,7908)
in the left column beside upper row 2 of the left array (traced: a "rail gate" like `w2`'s,
load to the VCC rail x 2780-2832). The inverter's input pad (2500,7907) is on the
left-edge trunk of `ck_out`: `tools/follow.py` from there south follows one metal 17,238 px
down the left edge and along the bottom to the clock block's branch contact (8567,18946).
The trunk also goes on from the pad, west and 2,050 px north at x 2370, to a contact
(2365,5847) and a poly that gates a unit of the small cluster below this one and ends on a
contact (2745,5842): more `ck_out` loads, not followed.

So:

- the step condition is sampled into `rcs_cond_lat` **while CLK is high**, and in that same
  phase it can pull `rcs_n4200` low;
- the row counter's step request itself (`rc_stepreq_n`) is combinational in `in1`, `e3`,
  `e4`, `a2`.

The column was read from the chip-2 shots at 7x: where no metal lies over it, they show
the poly bands and the diffusion edges (as lines across the bands) far more clearly than
the clean shot.

So the step logic is spread over all three clusters. They are one block of about 75 small
gates and three bus fields, and they are being traced unit by unit from here on (no more
chasing of single signals).

## How the row counter's step signal gets here

`rc_stepreq_n` (see `notes/blocks/wl.md`, `notes/blocks/bw.md`) was followed from the block west of
the counters: west along the central datapath's channel 3, north, west through the crossing
field x 6330-7700, up the metal x 5841 to a contact (5838,5585), west as poly along y 5585
through a second crossing field to a contact (3518,5587), by metal west and north to a
contact (3283,5238), by poly east, north (under a bus line) and west along y 5018 to a
buried contact at (3056,5030) on the output node of the gate below. About 9,000 px of wire.

## Layout of the cluster

Three vertical rails: R1 x 2590-2640, **R2 x 2775-2830 = VCC**, **R3 x 2950-3000 = VSS**
(R1 not yet read). Pull-downs sit on diffusion boxes under R3, each box tied to the rail by
a contact, with horizontal poly gates; a second column of pull-downs lies just east of R3
(x 3030-3063) between arms of those boxes. Loads lie between R2 and R3: a diffusion strip
from a VCC box under R2, under a poly plate in the open (bright orange-red, textured), to
the gate's node. East of the cluster a vertical bus of seven metal positions (x 3097-3375,
pitch 43) carries signals between this cluster, the ones above and below it, and the poly
lines that run east. **The bus lines are in pieces**: each piece joins two or three poly
lines by contacts and ends plainly; two pieces can share one x.

Under the wide rails the clean shot shows field as pink with an olive stripe down the
middle (the class map paints it olive): that stripe is not diffusion. Diffusion under a
rail is the tan boxes only.

## The step gate (traced)

- Output node: a U of diffusion round the VSS contact box of R3 at y 4950-4998: top part
  y 4903-4927, strip x 2888-2905 on the west, bottom part y 5022-5050. So the three
  pull-downs are: `in1` (gate y 4929-4947, above the box), `in2` (gate y 5001-5020, below
  the box), `in3` (gate y 5055-5075, onto the next box down, contact (2987,5108)).
- Load: strip y 5018-5047 from the VCC box under R2 (contact (2805,5030)), plate
  x 2845-2875. The plate's poly runs up to y 4962; its tie to the node (a dark box at
  (2885-2908, 4958-4996) on the strip) is drawn uncertain.
- The node goes east in the open to a buried contact (box x 3045-3068, y 5015-5047) with the
  poly that carries `rc_stepreq_n` away.

Inputs (pieces of the vertical bus):

| Input | Gate poly | Bus piece | Other contacts on the piece |
|---|---|---|---|
| `in1` | y 4929-4947, pad contact (3360,4937) | line G, upper piece, x 3352-3378, y 2754-4952 | top contact (3368,2768): poly east along y 2758-2778 to a contact (4225,2765) on a vertical metal of the next bus field (x 4140-4420). Not followed further |
| `in2` | y 4970-4992 then south at x 3000-3012 into the band y 5001-5020; pad contact (3148,4976) | line B, y 4705-5428 | (3150,4719): gate E1 of `m2`; (3150,5412): poly west along y 5400-5422, not followed: its driver |
| `in3` | y 5055-5075, pad contact (3108,5068) | line A, y 4790-5212 | (3108,4805): gate E2 of `m2`; (3108,5197): the output of the gate `in3 = NOR(e3, e4)` |
| `e3` | y 5147-5167, pad contact (3283,5152) | line E, upper piece, ends here; comes from the north (seen from y 5060) | not followed |
| `e4` | y 5230-5250, pad contact (3192,5237) | line C; another contact on it at (3192,5325), and it turns east at y 5665-5690 | extent not read |



## The small NOR `m2` (traced)

Column x 3030-3063 east of R3, between the east arms of two VSS boxes (y 4690-4707 and
y 4820-4842). Gates E1 (`in2`, y 4709-4734) and E2 (`in3`, y 4796-4817); the node between
them has a buried contact (box x 3045-3068, y 4750-4780) to a poly that runs east along
y 4753-4772, north under bus line C (x 3186-3206) and back west along y 4626-4645, where it
is gate E0 on the upper part of the same column (VSS below it; what is above: next piece).
No load has been found on `m2`.

## The gate that makes `in3` (traced)

Same construction as `m2`, one rail box further down (column x 3030-3063, y 5122-5266,
between the east arms of the VSS boxes at y 5080-5140 and y 5258-5297). Gates E3 (`e3`,
y 5147-5167) and E4 (`e4`, y 5230-5250). The node between them goes three ways: a buried
contact (box x 3042-3068, y 5181-5214) to the poly that runs east to bus line A's bottom
contact; a diffusion strip **west under the VSS rail** (y 5186-5208, tan between two thin
dark lines in the clean shot) to a box under the thin metal; and from that box, by a contact
(2915,5250), up the thin metal x 2903-2923. The load is on the far side of that box: a strip
y 5188-5216 under a poly plate x 2842-2897 to the VCC box under R2 (contact (2805,5212)).
The plate is one piece of poly from y 5168 to y 5265 (it looks like two plates in the clean
shot because the strip's edges show through it); its tie to the node is drawn uncertain.

## The gate that makes `in2` (traced)

The west side of the cluster is the mirror image of the east side: R1 (x 2600-2650) is a
second VSS rail, the small NORs sit on a column just **west** of it (x 2550-2592), and
their loads lie between R1 and the VCC rail R2 under a second thin metal (x 2688-2708).
`in2`'s gate: column y 5120-5282 between the rail boxes at y 5080-5142 and y 5258-5297;
gates `w2` (y 5142-5164) and `e4` (y 5230-5250, from a pad with a contact (2497,5238)
under a metal that comes round from bus line C by the poly y 5312-5332 and a contact
(2565,5321)); output by a buried contact (box x 2548-2578, y 5182-5214) and a poly west to
a contact (2412,5196), metal south and east along y 5411, contact (2565,5410), poly east
along y 5400-5422 under the whole cluster to bus line B's bottom contact (3150,5412).
Load: strip east under R1, box under thin metal W, plate x 2722-2775, VCC box under R2.

## The west column y 3170-3590: a selector and its inverter (traced 2026-11-17)

R1 (x 2600-2650) is one VSS rail from above y 3000 to the foot (0.7x overview). Under it and on
both sides of it, between two VSS boxes of the rail (contacts (2620,3277) and (2612,3550)), lies
one diffusion x 2558-2693, y 3300-3535. Four poly lines from the west cross all of it
(W/L 135/22 each); the part between the second and the third (y 3388-3449) is the node:

```
VSS (2620,3277) - gate rcs_thin_e (y 3319-3343) - gate tla_w3376 (y 3364-3387) - NODE
                - gate amr_eq_r3 (y 3451-3473) - gate tla_w3505 (y 3494-3515) - VSS (2612,3550)

tla_w3417 = NOT( rcs_thin_e AND tla_w3376  OR  tla_w3505 AND amr_eq_r3 )      firm
tla_w3505 = NOT rcs_thin_e                                                    marked (load tie)
```

So the unit is an inverting **two-way selector**: while `rcs_thin_e` is high the output is
NOT `tla_w3376`, while it is low NOT `amr_eq_r3`.

- Between the gates of each pair there is plain diffusion only (no contact, three shots).
  The dark ovals at x 2665-2680 between the polys are the 35 px gap between R1 and thin
  metal W showing through (layers.md), not layout.
- Node exit: a buried contact (concentric box x 2558-2594, y 3398-3438) with the poly
  y 3406-3430, west to a pad with a contact (2326,3418); metal x 2326 south 2,130 px (follow.py),
  east along y 5545 to a contact (2562,5545); poly east along y 5535-5550 at the cluster's
  foot, straight under R1, R2, R3 and the bus (read at 3x to 5.6x from x 2580 to x 3720: no pad,
  no step) and on through the second crossing field beside the step signal's poly (2.1x in
  three shots, x 3700-4400: at the same y under every metal) to a pad with a contact
  (4408,5545). There a metal on **track V of the second bus field** (x 4409) takes it north
  1,085 px (follow.py: no contact candidate) to a contact (4410,4460), whose pad's poly leaves
  **east along y 4452-4470 towards the right cluster** (drawn to x 4520; not followed).
  The poly that goes on east along y 5543 is another net: it starts on its own pad
  (4497,5545) with a metal going south, 45 px of bare ground from the first pad (4.2x).
- Load: the node bulges east under thin W (x 2693-2730) and runs on as a strip y 3400-3443
  under a plate x 2735-2777 (W/L 43/42) to the VCC box (contact (2805,3440)) that also feeds
  `rcs_u3425`'s load from its other side. A tail x 2714-2729 runs up to a box (2714-2757,
  3337-3360) where the plate's stem is tied to it (heavy box in four shots).
- A poly of **another net** lies under the output metal x 2326 from y 4540 to y 4985 (it comes
  from the west along y 4547 and leaves west along y 4980). No pad, no ring in the metal
  (5x): not joined (tracing guide, trap 13).

The four gate lines:

| Gate | Line | Followed to |
|---|---|---|
| 1, y 3331 | `rcs_thin_e` | pad contact (2326,3333) at the bottom of a metal x 2326 (y 2754-3347). The same metal has a contact (2326,3243) on the pad of the inverter's gate poly, and its top contact (2326,2768) is on a poly that runs east along y 2759-2777 to a pad with a contact (2695,2768). From there a thin metal goes south at x 2688-2705 and at y 2975-2997 turns east: **it is thin metal E** (one bright L at 4x; the earlier trace began E at x 2740 and said it came from the west). So thin E's north end is these two gates. Its driver is not found: thin E runs south over the east loads to about y 6036 (follow.py; contact candidate (2912,5983)), into the small cluster below |
| 2, y 3376 | `tla_w3376` | pad contact (2239,3376); metal west to x 2199 and south to a contact (2199,5502); poly east along y 5492-5508, straight under R1 and R2 (3.5x, 5.6x), to a pad with a contact (2870,5502); metal south at x 2865-2877 to about y 5977 (follow.py; that end not looked at): from the small cluster below |
| 3, y 3462 | `amr_eq_r3` | pad contact (2239,3463); metal x 2239 south to a contact (2239,5632) on the pad of a poly that leaves east along y 5622-5642 (seen to x 3450 at 1.45x, drawn only at the pad). **Believed** to be the vertical sync width match `amr_eq_r3`: an unmerged branch follows that line here from `amr`. Not joined on this branch, so the name is a place name |
| 4, y 3505 | `tla_w3505` | pad contact (2283,3506) at the bottom of a metal x 2283 (y 3188-3518); its top contact (2283,3202) is on the output poly of the inverter |

**The inverter** (y 3170-3255) is a "rail gate" like `rcs_w2`'s. Node: diffusion under R1 at
y 3207-3233 and a part west of the rail (x 2540-2602, one outline in both stripped shots) with
the buried contact (concentric box x 2548-2578, y 3195-3222) to the output poly y 3192-3212.
Gate: poly y 3234-3252 (W/L 57/18) from the pad (2326,3243); below it the VSS box it shares
with the selector. Load: strip east under thin W and under a plate (x 2722-2776; channel
y 3200-3228) to a VCC box of its own under R2 (contact (2805,3230)); tail x 2699-2719 down to
the tie box (2712-2752, 3248-3282). That the tie's tab is one poly with the plate is not
resolved (a dark line lies between them in both metal shots), so the tie is drawn `?`.

**The top unit of the west column (y 3010-3178): `rcs_u3288_n` = NOT `rcs_u3288`, driving thin
metal W.** (traced 2026-11-17)

- Input: `rcs_u3288`'s metal (bus line C's top piece, north to y 2728 and west) ends on a
  contact (2828,2726); a poly runs west along y 2717-2735 (3.9x: one straight line, pad to
  pad) to a contact (2562,2725); metal west along y 2727 to x 2292 and south at x 2283 to a
  contact (2283,3112) (follow.py; its one contact candidate (2286,2797) is fringe, no pad);
  poly east along y 3103-3122 to the gate under R1 (W/L 57/19).
- Node: diffusion under R1 at y 3080-3103 with a part west of the rail (x 2538-2602,
  y 3058-3098) carrying a concentric box (2545-2575, 3062-3092) to which **no poly comes**
  (4.6x and the 3.3x strip of the pads: nothing at y 3075 west of x 2535). The east column's
  inverter `rcs_u3425` has the same box without a poly at (3045-3070, 3415-3440): it seems
  to belong to this kind of unit. Below the gate: the rail's VSS box (contact (2620,3150)).
- Load: **strong** (W/L about 47/33; the standard load is about 28/55). The node's strip runs
  east at y 3080-3097 and turns down as the west side of a diffusion x 2728-2790, y 3092-3138;
  the plate (x 2745-2778) crosses it north-south (no diffusion edge crosses the plate in the
  metal shots, unlike the standard loads) to the VCC box under R2 (contact (2805,3110), shared
  with `rcs_c1`'s load). The plate continues at its top as a band going west (y 3040-3068) with
  a pad above it, and the pad has a **metal contact (2738,3027) to thin metal W**, which goes
  west 40 px and south at x 2689-2703 over the west loads (follow.py: to y 4002; contact
  candidates at y 3690, 3786, 3825, 3925, 3949, in units not traced). The band's west end is
  tied to a tail of the node by a buried contact (box 2690-2712, 3056-3080) right under thin
  W's metal: drawn `?`, so "thin W is this inverter's output" is **marked**. The piece of thin
  W drawn earlier (y 4940-5330, `rcs_thin_w`) is not shown to be the same metal.
- Not resolved: a heavy-outlined box west of the rail below the gate (2545-2598, 3128-3150).
  If it is diffusion joined to the VSS box, the gate is twice as wide; the logic is the same.

**If `amr_eq_r3` is the vertical sync width match**, this unit chooses between it and a signal
from the small cluster below, under control of the net on thin metal E, which runs the length
of the cluster. Nothing more is claimed.

**A second transistor on `rcs_u3425` (dense part west of R3).** A vertical poly x 2950-2968,
y 3447-3547, under the west edge of R3, crosses a diffusion (y 3462-3500) between the column
under thin E (`rcs_u3425`'s node) and the rail's VSS box (contact (2990,3500)). Measured in the
clean shot: 245/178/128 on the poly over y 3466-3496 (a gate over its channel under this rail
measures 238/176/128) and 221/167/118 over y 3508-3540 (poly over field: 214-220/165/117); dark
lines cross it at y 3462 and y 3502. West of the poly the link runs through the 27 px gap
between thin E and the rail: a dark bar in the clean shot, plain tan in the chip-2 shot (the
field just below is green there). Drawn `?D`. The poly has a rounded cap at the top (15 px
above the diffusion) and a 45 px stub over field at the bottom. **No connection to it was
found** in two passes (four shots at 5-6x; no pad, no paler patch, no arm, no ring that can be
told from the poly's own edges under the rail). It is named `rcs_iso2958`. If the rail above
contacts the stub, the gate is on VSS and the transistor is always off (an unused input tied
off), and `rcs_u3425` = NOT `rcs_bc3460` as before; the step formula above assumes that.

## The chase of `e4` (2026-11-16)

`e4` gates the whole step logic, so naming it was the first aim. Result: its route is
drawn end to end and it is **not identified**. What was learnt on the way:

- **It is not RES**, though it looked like it for an hour. The RES line (`res_b`, metal
  x 5266-5290 from the pad buffers at the top) comes down the whole top-left logic without
  a tap and from y 5857 to y 6075 lies exactly on top of `e4`'s poly (bus line 5). Five
  shots at 5-9x and a colour profile every 6 px show no contact; the metal's last 20 px
  turn **west** along y 6055-6080 to a contact (5190,6065) on the pad of bus line 3. The
  overlap is routing (tracing guide, trap 8). `lpstb_b` ends the same way one line over:
  contact (5232,6105), bus line 4. Both are now drawn in `trace/trunks.txt`.
- So the poly bus x 5100-5290 (y 6060-6850) carries, west to east: two unidentified
  lines, `res_b`, `lpstb_b`, `e4`. All five fan out diagonally at y 6850-7350 to
  horizontal metals going east (pads at x 6130-6165). `e4` travels with the two input
  pins' signals from the top-left to the centre, which suggests (no more) that it is a
  signal of the same standing: a chip-wide control line.
- It is not the neighbouring gate's output either: `m2`'s poly runs under bus line C for
  120 px (y 4636-4762) with no contact (6.4x, three shots).
- The two crossing fields it passes in the left bus field (y 9560-9780 and
  y 10340-10660) give it no tap. In those fields the clean shot's colour under a metal
  varies from salmon to yellow-green from crossing to crossing, on whole rows at a time,
  so the contact-colour test (`tools/xfield.py`) is not usable there; a real tap has a pad.
- The 13-line bus of bc1 (y 14354-14873): its line y 14526 is **two nets**. The poly from
  the west ends on the pad (7012,14522) and goes south (`e4`); the line's continuation
  east starts on a separate pad (7100,14522) fed by a metal from the north. (I followed
  the eastern piece to a gate at (9480,15560) before noticing: not `e4`.)

Where its driver can still be: on one of the poly stretches as a branch I did not see
(the diagonal fan and y 7122, x 5560-6128, were only read at 1.1x), or at a contact with
a pad on the 4,000 px of metal in the left bus field that the profile tools did not flag.

## The thin metals and the dense part (open, 2026-11-16)

- **Thin metal E: north end found 2026-11-17** (see "The west column"): it is the net of the
  selector's first gate and of the inverter's gate, by the metal x 2696 (y 2754-2986), the
  poly y 2768 and the metal x 2326. Thin metal W's top end is a contact (2738,3027) on the
  load gate of the top unit of the west column: W carries that inverter's output
  (`rcs_u3288_n`, marked).
- **Thin metal E (x 2903-2923)** shows dark stretches of 40-60 px wherever it passes a
  load's tie (the buried contact between the load plate's tab and the tail of the node's
  box), at y 3164, 3337, 3530, 3620, 3820, 4202, 4313, 4640, 4813, 4935, 5011, 5246. Neither
  metal shot shows bright metal there. Read as: the metal is continuous and dips over the
  buried contacts (if those were metal contacts, the outputs of several different gates
  would be shorted together). So where thin E really makes contact is still not found;
  `tools/tla_contacts.py` is no help on it (it passes over tan diffusion boxes all the way).
- **The dense part west of the rail, x 2835-2975, y 3395-3665: resolved 2026-11-16.** It is
  two loads and a strap. The inverter `rcs_u3425`'s node strip runs west under the rail to a
  diffusion column under thin E (x 2900-2940, ending at y 3500); its load plate
  (x 2845-2895) continues downwards as a pad with a metal contact (2865,3488) and a
  buried-contact tie to that column. A **metal strap** (x 2850-2886) takes the node from
  that contact down, over `b1`'s load plate, to a second pad (contact (2865,3640)) whose
  poly arm crosses `b1`'s box under thin E at y 3617-3638 **as a gate** (9x: bright over a
  channel, diffusion on both sides, and the part below links east to the VSS box). So
  `b1` has three pull-downs. How the two crossings were told apart: class runs down
  x 2912-2928 show plain diffusion with a box at its edge at the top crossing (a tie) and
  a bright band right across the diffusion at the bottom one (a gate).
- **Two kinds of non-standard unit** in this cluster, both now traced once: the strap
  (an output carried over a neighbouring load to a gate), and the AND-OR-INVERT unit
  whose diffusion is one wide area under the VSS rail and under a signal metal beside it
  (`rcs_n4200`, y 4045-4320), with series gates.

## Reading aids for this region

- **The loads' ties.** Each load plate has a tab at its lower corner that is tied by a
  buried contact to a tail of the node's box, right under the thin metal. In the metal
  shot the tie looks like a metal contact (a round blob). It is not one: all the loads of
  a column have it and the thin metal runs on past them. So the thin metals (x 2903-2923
  and x 2688-2708) do not join the loads' nodes; what they do connect is not read yet.
- **Under a wide rail** the clean shot shows field as pink with an olive stripe down the
  middle; the class map paints the stripe as open diffusion. Diffusion under a rail is the
  tan boxes only.
- **The bus as a class map** (`strips.py --layer class`): metal shows as white bands (field
  that was under metal), gaps between pieces as olive blocks, poly crossings as red bars,
  contacts as yellow-green blobs in a red pad. One image shows 3,000 px of the bus.
- `tools/follow.py` follows one metal line from a point through corners, jogs and
  diagonals, using both chips' metal shots, and prints it as a trace line. It turned a
  4,000 px bus-field run from an afternoon into a minute. Its ends and its staircases must
  still be looked at: see its docstring for the two mistakes it made here.
- `tools/tla_tracks.py` (where a track has metal; splits at gaps) and
  `tools/tla_contacts.py` (contact candidates on a track from the clean shot's colour).
  Both are for knowing where to look. A dark band across one chip's metal with nothing
  under it in the clean shot is dirt: check the other chip's metal shot (`metal1`).
- Not every part of the column is the simple NOR unit: y 4235-4620 on the east side has
  diffusion strips under the thin metal with gates across them (pass transistors or a
  latch). Not traced.

## What the chase showed about this part of the die

The top-left "logic" is gate clusters joined by bus fields: the vertical bus x 3090-3380
beside this cluster, seven horizontal poly lines along its top (y 2630-2900), another
vertical bus field at x 4140-4420, the poly bus x 5100-5300 / y 5840-6850 with its
diagonal fan, and the left bus field x 6300-6900 that runs the height of the die. Signals
such as `e4` are global: they have a dozen taps. Following one at a time costs a handful
of views per hop. The region has to be traced whole, cluster by cluster and bus by bus.

My guess, **not shown by anything yet**: this is the vertical control. In a 6845 the
character row counter steps at the end of a scan line when the scan line counter has
reached R9. The formula has that shape if `e4` is an end-of-line timing strobe (active
low), `e3` or `x1`/`a2` are scan-line comparisons, and `in1` is a separate cause. The way
to prove or refute it is to reach a named signal: the R0 match line from the right
datapath (bd1's tracks k7/k8, not followed past their first jog) is the best candidate
for `e4`, and it would arrive up the left bus field, which is where `e4` comes from.

## Not done

- `rcs_iso2958`'s top end (2959,3447): its cap abuts `rcs_u3425`'s diffusion with a single
  edge line between (acid1b column profile; review round 1, 6x); a tie there is not
  excluded, and would make the gate `rcs_u3425` itself. "No connection found" is not
  "no connection".
- The poly y 2977-2996 on `rcs_c1`'s line does not start at x 2330: it runs on west to
  x 2262, north along x 2258-2272, east along y 2712-2725 beside the y 2727 metal to about
  x 2415 and north out of the region (review round 1; no contact to the x 2283 / y 2727
  metal). A port not drawn.

- The inputs' sources (table in Status). Next: `e4` south down the left bus field, and
  from the other side the R0 match line from bd1's k7/k8.
- West column (R1's columns) y 3590-4940: not traced. Polys from west pads cross R1 at about
  y 3600, 3690, 3810-3900 and on down (0.7x overview only). Thin W (`rcs_u3288_n`) has
  contact candidates there at y 3690, 3786, 3825, 3925, 3949; where it ends (y 4002?) and
  whether the piece at y 4940-5330 is the same metal.
- The top unit's box west of the rail (2545-2598, 3128-3150), and the boxes without a poly at
  (2545-2575, 3062-3092) and (3045-3070, 3415-3440).
- `tla_w3417`'s poly east of (4520,4461), into the right cluster; `tla_w3376`'s metal south of (2871,5975);
  `amr_eq_r3`'s poly east of (2300,5632) (to be joined to `amr_eq_r3` when that branch is
  merged); thin E south of y 5400 (to about y 6036). All lead into the small cluster below
  (y 5450-6330), which is not traced, or east along the foot.
- `rcs_iso2958`'s connection (see "The west column"): look for a rail contact on the stub
  (2950-2968, 3505-3545), e.g. by comparing the rail's metal there with a known rail-to-poly
  contact.
- The inverter `tla_w3505`'s load tie (2712-2752, 3248-3282): tab and plate one poly?
- y 3700-4590 on the east side (the units at y 3420 and y 3895 and the dense part west of the
  rail at y 3395-3665 are traced: `rcs_u3425`, `rcs_bc3460`, `rcs_b1`'s load and third gate).
- How rail R2 (VCC, top end y 3018) is fed.
- Bus pieces not yet drawn: B2 (from (3150,3810) south), C upper, D, F, and everything
  north of y 2940.

## Review

Round 1 (full review, 2026-11-17 19:00 +0000, a fresh agent on claude-fable-5-2, at commit fff417a). Told to
suspect the poly row y 5543 (read at 2.1x), the corner (2696,2986), a swap or tap among the
four parallel metals x 2199-2326, the two contacts on x 2326, the AOI's series order and
node box, the inverter ties, the joins across R1's edge and the `?D` link. It read the row
y 5543 over its whole length at 3.3x (constant y, no pad or step), the metals and their
contacts in both chips, the AOI's four gates with a rail profile and views, the corner and
both routes at y 2726 / y 2768, and the foreign poly under x 2326. No wrong connection.
Findings, each checked by the tracer:
1. The pull-down of `rcs_u3288_n` also runs west of the rail (closed outline 2550-2600 x
   3098-3148 with the gate across it): confirmed on `review-1/j1.png`; drawn, W 57 -> 105,
   same nets.
2. `rcs_iso2958`'s top end may be tied to `rcs_u3425`'s diffusion: undecidable at 6x;
   recorded under Not done.
3. An untraced poly continuing `rcs_c1`'s line west and north: recorded under Not done.
Could not be checked: the joins across R1's edge at x 2600 (the etch line sits on the rail
edge; supported by outlines continuing across), the `?D` link, the top unit's pad-to-plate
join, the row y 5543 in a second shot.

Round 2 (fix check, 2026-11-17 19:04 +0000, a fresh agent on claude-fable-5-2, against commit fff417a). The
added west patch is right (diffusion on both sides of the gate, joined to the rail's VSS
box; the netlist differs only in that one transistor). One finding: the same pull-down
also runs east of the rail, a mirror-image closed patch at (2655-2683, 3125-3147):
confirmed by the tracer at 6x (`chk_east.png`) and drawn; W 105 -> about 133, same nets.

Round 3 (fix check, 2026-11-17 19:07 +0000, a fresh agent on claude-fable-5-2, against commit 90ea353). The east
patch is diffusion below the gate, joined to the VSS box, ends at x 2681-2684 short of thin
W, and is 44 px clear of the load; the overlap above the gate is the same node. The full
extraction of both versions differs only in that transistor (105/19 -> 134/19); the node
and `vss` stay separate.

Round 3: no findings.

**Note from `tl1` (coordinator, 2026-11-17).** Thin metal W's "end at y 4002" is probably a
follower stop: `tl1` found no stretch of it fully dark for more than 20 px from y 3030 to y 5952.
`rcs_e4`'s driver is the wide NOR in `tl1` (`notes/blocks/tl1.md`). Two VCC boxes here need
correcting (master list, `tla` row; R29).

Round 4 (full review, 2026-11-28 14:20 +0000, a fresh agent on claude-fable-5-2, at commit 072f3ba5; images in
`cache/scratch/tla/review-4/`, 11 used). Piece `r40` of run 2 only: the three units of this file in the middle
cluster's east column (x 3820-4300, y 3300-4170). Told to suspect: "field east of the rail" at units A and C;
unit B's column edges and its continuity; the arm and the two bands against the gate rows (an extra channel at
x 4050-4072); the two ties drawn firm and a contact of the thin metal x 3948-3962 on unit C's tail; the joins
under the rail's east edge line; the channel under the rail at unit C; the pad (4192,3413) against the diagonal
metal north of it and the pad (4148,3335); anything undrawn. It read the junctions at 4.5-5x in two to four shots
and measured with `tools/px.py` rows and columns, `tools/tl3_thin.py` and the extraction with every file.
Found correct: the field pockets east of the rail at A and C (they match certain field in all four shots; chip-2
stripped red minus green 0-11 against 29-41 on the strips in the same gap); unit B's column (an edge line across
both gate rows at x 4068-4074, absent at y 3917 where the arm passes; continuous to y ~3980; field west of it
between the three bands); all five joins under the rail's edge; both ties (box and tail share one outline, the
tail runs into the strip with no edge, the plates have no other exit); no contact of the thin metal x 3948-3962
on unit C's tail (edge bars of 8-9 px only, no ring, hole or widening); the pads (4192,3413) fed from the south
only and (4148,3335) from the north only; no undrawn tap on the three metals inside the region; nothing undrawn
with every package outlined; the extraction and `tools/unsure.py` as claimed. Three findings, each checked by
the tracer, **all geometry only**:
1. The rail gates of units A and C are about 44 wide, not 38: the box's and the channel's east edge is a second
   dark line at x ~4056 in both metal shots, east of the rail's own edge line at x 4046. Confirmed (`px.py row
   3340 / 3374 / 4113 / 4136 4038 4066 2 all`: minima at x 4046 and x 4056 with a hump between in both chips, and
   the chip-2 stripped shot dark at x 4050-4058; the node rows 3407 and 4088 have the one line). Fixed: both
   diffusions drawn to x 4056. Same nets.
2. Unit B's VSS box was drawn 10 px too far east (to x 4050, touching gate `rcs_in1`'s poly): outside the arm's
   height its east edge is x ~4040. Confirmed (`px.py col 4036 / 4043 / 4047 3878 3936 3 acid1b,acid`). Fixed:
   box to x 4040, the arm from x 4034. No transistor had been extracted there. Same nets.
3. The contact (4270,3893) on `rcs_in1`'s metal is at about (4277,3898). Confirmed (`tools/textmap.py 4248 3872
   4296 3918 3`: bright centre x 4272-4281, y 3893-3902 in both chips, hole x 4272-4284). Moved; same pad and metal.
Connections before and after the fixes (against 072f3ba5):
`tools/t.sh tla sameconn.py 072f3ba5`: `connections identical`;
`.venv/bin/python tools/sameconn.py 072f3ba5`: `connections identical`.
Could not be checked: the inside of the buried-contact boxes; the thin metal x 4099-4111 over the three output
boxes (`tl3`'s `?M`: at `rcs_in1`'s box it reads as a pass-over, at `rcs_mu`'s only one row was read, `rcs_mn3852`'s
was not examined; Ambiguities 3 and 4 of run 2); the three metals beyond the region.

Round 4: no findings that change a connection.

Round 5 (full review, 2026-11-28 15:07 +0000, a fresh agent on claude-fable-5-2, at commit 556b4842; images in
`cache/scratch/tla/review-5/`, 21 used). Piece `r40b` of run 3 only: the nine units on the columns beside R3 and R1
(x 2940-3090, y 3000-5310; x 2520-2660, y 5095-5310). Told to suspect: the join at (3010-3026, 3478-3530), made
firm in this run (one diffusion, or two facing each other across the rail's edge; whether the open area east of it
is diffusion at all); the same at the fourteen arms; a gate row running on under the rail, or a tap or second
transistor between the rail's edge and the column or between the column and bus line A; the column's edges, a side
branch, a column continuing through a field pocket; "nothing above the node" of `rcs_u3425`; the top of
`rcs_cond`'s unit. It read the join at 5.5x in four shots and rows y 3486-3522, each arm at 4.2x in three shots
with a row across it, all seventeen gate rows under the rails, column profiles down x 3078, x 3018 and x 2535 for
undrawn rows, the field pockets, the node strips, `rcs_u3425`'s node and `rcs_cond`'s top at 5.5x, the extraction,
`tools/unsure.py` and `tools/sameconn.py f5adf76a`.
Found correct: the join (clean shot tan to x 3018, chip-2 metal plain from x 3021, both stripped shots one box
colour up to the line; the open area is diffusion, chip-2 stripped red minus green 22-28 against 2-8 on the field
east of the column); all fourteen arm joins (one edge line; where a box ends against field the line is double, 14
px); no gate row under R3 or R1 (pink and olive at all seventeen rows, control rail gates 240/175; no lines across
the rail in chip 2's metal shot); exactly two edge dips on every row, no undrawn poly row; every field pocket
field; the band y 3824-3838 between `tl2`'s gate and gate `rcs_e3` diffusion; the node strips diffusion with no
contact on `rcs_u3425`'s; field above `rcs_u3425`'s node (its box's poly is a closed cap ending at x ~3084, short
of bus line A: still AMB-030); `rcs_cond`'s top; the nine equations.
Findings, each checked by the tracer, **all geometry only**:
1. Two node strips were drawn about 8 px north of where they are: `rcs_b1`'s (`D 2935,3575:3048,3600`) and
   `rcs_bc3460`'s (`D 2925,3882:3048,3901`). Confirmed (`px.py col 3018 3566 3620 2 metal,metal1`: edge lines at
   y 3582-3584 and y 3606-3608; `col 2980 3566 3620 2 acid1b`: tan y 3586-3604 under the rail; `col 3018 3872 3920
   2`: lines at y 3890 and y 3908-3910; control `rcs_c1`'s strip, lines at y 3107 and y 3126 against 3105-3124
   drawn). Fixed: y 3583-3607 and y 3890-3909. Same ends.
2. Several arms were drawn 5-8 px off in y. Each arm measured (`px.py col 3018 Y0 Y1 2 metal,metal1` at the eleven
   east arms, `col 2575` at the two west ones). Off by 7-12 px and fixed, with the column's end: `rcs_c1`'s lower
   arm (lower edge line y 3194-3196, drawn to 3183), `rcs_u3288`'s upper (y 3208-3210, drawn from 3218), `rcs_b1`'s
   lower (y 3670-3672, drawn to 3662), `rcs_cond`'s lower (y 4670-4672, drawn to 4663), `rcs_in3`'s lower (y 5276,
   drawn to 5266), `rcs_in2`'s lower (y 5274-5276 with field from y 5280, drawn to 5282). Within 4 px and left: the
   other seven. Left on purpose: `rcs_bc3460`'s upper arm (upper edge line y 3824, drawn from 3818): its top is
   where `tl2`'s column meets it. Same ends.
3. An observation, no change: at the join the rail's metal bulges east round its contact (chip 1's metal bright to
   x 3012 at y 3488-3497), so every shot's edge line lies about 10 px east of its place at the arms; R3 is drawn
   straight. This is why the line at the join is at x 3016-3026 (run 3's text above) and supports reading it as the
   rail's edge line.
Connections before and after the fixes (against 556b4842):
`tools/t.sh tla sameconn.py 556b4842`: `connections identical`;
`.venv/bin/python tools/sameconn.py 556b4842`: `connections identical`.
Could not be checked: the 2-4 px directly under each edge line (the joins rest on diffusion seen on both sides:
Ambiguity 1 of run 3); chip 2 under the rail by colour (fringes), only its metal shot's absence of lines; the
loads west of R3, the rows east of x 3090 and the column outside the units' y ranges, which are outside the piece.

Round 5: no findings that change a connection.

Round 6 (full review, 2026-11-28 15:30-15:45 +0000, a fresh agent on Claude Fable 5.2, at commit b218b14e; images in
`cache/scratch/tla/review-6/`). Piece `rg` of run 4: the six rail-gate pull-downs (the step gate's three under R3,
`rcs_w2` and `tla_w3505` under R1, `clk_tl`'s driver at (2615,7908)). Told to suspect: whether the gap stretch
(2932-2948, 4955-4992) is diffusion or field and whether the U's inner field is under thin metal E; whether the two
gate rows reach the box's west edge; whether the line at x 3038-3040 crosses `rcs_in3`'s row and whether the patch
below the gate is diffusion on `vss`; the east edge at x 2648 of the R1 gates and whether they have a part west of
the rail after all; the line and patch of `clk_tl`'s driver; any gate that fits its old drawing better. It looked at
each unit at 4.5-5x in four shots with profiles (`tools/px.py row / col`, `tools/textmap.py`).

- Finding 1, **geometry only, confirmed**: the step gate's two rows end further west than drawn (2924), under thin
  metal E: `rcs_in1`'s at x ~2913 and `rcs_in2`'s at x ~2919 (tracer: `px.py row 4938 / 4972 / 5010 2906 2930 2
  acid,acid1b`: chip-2 stripped red over green by 16-42 on row 4938 over x 2912-2924 and by 13-21 on row 5010 over
  x 2920-2924, green over red by 5-12 between the rows; clean shot salmon 201-220/141-147/88-109 on the rows at
  x 2920 against 179/140/118 between). Both rows pass the box's edge (x ~2927-2930) by 8-14 px: run 4's Ambiguity 2
  is settled. Drawn to x 2913 and x 2918.
- Finding 2, **geometry only, confirmed**: `rcs_w2`'s rail box `D 2598,5080:2652,5142` was still drawn to x 2652; its
  east edge is the line at x 2647-2650 (pink field at x 2656 down to y 5130: `px.py col 2656 4980 5130 6`). Drawn to
  x 2648, and the box shared by `tla_w3505` and the selector (`D 2600,3254:2652,3305`) likewise.
- Found correct: the gap stretch is diffusion (like the bands, unlike the field in the same gap, in four shots;
  tan unbroken from x 2948 under the rail), the inner strip is field under E, and no poly crosses the U's west
  strip; the box's east edge at x 2998 and no part east of it; `rcs_in3`'s line across the row in all four shots,
  the patch like the node strip and with only `vss` neighbours (the rail box and the arm at y 5122); the R1 gates'
  line at x 2647-2650 at gate and VSS rows only, no line across either row west of the rail; `clk_tl`'s driver as
  drawn; four marks on the rails ((2982,5066), (2972,4904), (2623,5068), (2623,7858)) are blemishes of one chip, not
  contacts.
- Could not check: the joins across a rail's own edge line (the second parts of `rcs_in3` and of `clk_tl`'s driver,
  the step gate's box): one line either way, same nets (run 4, Ambiguity 1); the gap east of R1 at `rcs_w2` in the
  chip-2 stripped shot (murky; "no part there" rests on both metal shots); and, outside this piece, the 6-9 px
  between the node's buried-contact box (3042-3071, 5012-5049) and `rcs_in3`'s row, dark throughout in both metal
  shots (noted under "Not done after run 4").
- After the fixes: `tools/t.sh tla sameconn.py b218b14e`: `connections identical`; `.venv/bin/python
  tools/sameconn.py b218b14e`: `connections identical` (2,547 nets, 4,931 transistors, 0 errors, 0 warnings before
  and after).

Round 6: no findings that change a connection.

Round 7 (full review, 2026-11-28 16:15-16:37 +0000, a fresh agent on Claude Fable 5.2, at commit 26f28ec5; nine images
in `cache/scratch/tla/review-7/`). Pieces `iso` and `aoi` of run 5 (eleven claims: the transistor under R3's west
edge, its diffusion link, its free top end, the foot, the join to `rcs_b1`'s plate arm through the `?P`, no contact
on the poly; the stack as one diffusion across the gap, its two edges, each gate band one poly across it, the series
order, no contact of the thin metal). Told to suspect: the join of the foot to the tie box (poly, field, or two
polys' ends), whether the foot exists and is one poly with the stub, the box's east outline and the arm's entry,
anything else at the stub's bottom end (`rcs_x1`'s row); the link in the gap between thin metal E and R3; the cap
against the strip above; the gap between R3 and the thin metal x 3026-3062 between the gate rows and above g1; the
stack's edges; the bands through their bends and whether they touch; g2's west end; a contact of the thin metal. It
looked at both pieces at 5-8x in four shots with profiles and text maps (`tools/px.py`, `tools/textmap.py`) and the
extraction.

- Finding 1, **geometry only, confirmed**: the VSS box `D 2968,3470:3035,3528` (a line from before run 5): below
  the channel its west edge is at x ~2979, not 2968 (tracer: `px.py row 3516 2964 2990 2 acid1b,metal`: dark
  x 2968-2978, tan from x 2982), so the drawn box lay against the stub's east edge where the photo has field; and
  its top is y 3482 east of x ~2997 (`px.py col 3010 3462 3492 3 acid1b`: pink to y 3471, line y 3480-3483, tan
  from y 3489; drawn 3470). Redrawn as the box `D 2979,3482:3035,3528` and its part beside the channel `D
  2968,3464:2996,3502`. The transistor is 39/18 before and after.
- Found correct. `iso`: the channel y 3466-3499 with edge lines in all four shots, cap and lower stub poly over
  field; the link's bottom edge one line from under E through the gap to the poly, the gap's interior red over green
  by 31-47 in the chip-2 stripped shot against 7-23 on field, no vertical line between column and link, tan east of
  the poly from x 2974 into the box; the cap ends flush on the strip's edge line with no box and no poly over the
  strip, field west of it; **the foot is orange at x 2942-2950, y 3531-3546 in both metal shots** (chip 2
  151/113/58, chip 1 173/90/54), the stub's west edge line (red 61-80 at y 3522-3528) is absent there and only R3's
  edge line remains, the clean shot salmon from x 2948 with no pink; **the join, against a control**: at g2's west
  end (y 4167), where a poly certainly ends, there are a bare strip x 2944-2948 and pink field x 2952-2958, and the
  foot has neither; the box's interior ends x ~2930, outline x 2932-2937, red from x 2938; the arm enters from the
  west; no ring in chip 1 and no green hole on the poly (a dark blob at (2962-2974, 3536-3550) is in chip 2 only);
  `rcs_x1`'s row ends at x ~3010 with pink field under R3. `aoi`: against a real edge in the same gap (row 4070: a
  dark line x 3016-3020 in both metal shots) the rows 4094 and 4135 read like node N's row 4200, no line in either
  metal shot, tan to x 3010 and from x 3022; edges x 2968-2972 and ~3041; both bands continuous orange through the
  gap in both metal shots, never touching; g2 ends at x ~2960; both pads real contacts; no ring or hole on the thin
  metal; pink field east of x 3046.
- Could not check: poly through the box's east outline (x 2931-2938), invisible in every shot ("`?P` is right to
  stay"); the chip-2 stripped shot does not resolve the foot; a faint tan streak under R3 at x 2976-2988
  (y 3448-3458, 3546-3576) without outline or ring in any shot, read as tint.
- After the fix: `tools/t.sh tla sameconn.py 26f28ec5`: `connections identical`; `.venv/bin/python tools/sameconn.py
  26f28ec5`: `connections identical` (2,546 nets, 4,931 transistors, 0 errors, 0 warnings before and after).

Round 7: no findings that change a connection.

## Corrections from `tl1`-`tl4` (coordinator, from the handoffs of 2026-11-17/18)

Each is in the named block's notes in full; the trace fixes are on main.
- `rcs_c1`'s poly is drawn (by `tl1`). `ck_out`'s row y 5849 ends at R1's east edge (x ~2658), not on
  the pad (2745,5842), which is the top of thin metal x 2742 (fixed, ee9c0d0).
- The middle cluster's east VSS rail runs up to y 2595 and joins the west rail there (`tl3` draws
  y 2622-3060).
- The pass transistor of `rcs_cond_lat` is gated by `tl3_w3982`, not `clk_tl` (fixed, 1915f94,
  fa2a849; AMB-009). So "`rcs_cond_lat` <- `rcs_cond` while `clk_tl`" and "the step condition is
  sampled while CLK is high" are not supported. `clk_tl`'s gate contacts: (3150,3812) and
  (3150,4418) are pads with rows west into what `tl2` traced; (3152,4548) gates nothing.
- `x1`'s row ends at x 3470 on the pad (3454,3504) of the bus metal x 3456 (which also carries
  `rcs_x1`); the poly that leaves east along y 3752-3770 (`a2`) is the
  output of `tl3`'s NOR 1.
- Bus pieces: D upper and F are drawn by `tl2`, as is D middle's bottom contact (3237,4376).
- `rcs_bc3460` = NOR(`rcs_e3`, `rcs_e4`, `tl5_w4937`, `clk_tl`): two inputs more than this file says
  (so `rcs_u3425` is not simply `rcs_e3` OR `rcs_e4`); the step formula stands. `rcs_bd3330` has its
  driver (`tl2`'s piece 2, AMB-029). `rcs_n4200` has a third input, `rcs_bd3330` (marked), on the west
  part of g3, which is two polys (fixed, 0239da7).
- `tla_w3376`'s metal does not end in the small cluster: it passes over it and leaves the strip at
  y 6350. Thin E south of y 5400 is drawn by `tl2` (to a pad (2913,6327), row east along y 6316-6337).
- `tla_w3417`'s poly along y 4461 ends on gate 1 of `tl4_w4545` (`tl4`).
- The right cluster (x 4650-5050) is the same column build as the first cluster's west column,
  2125 px east and 434 px north; there is no thin metal at the place of thin metal W (`tl4`).
- The buried-contact box at (3045-3070, 3415-3440): in `tl3`'s mirror of that unit it carries the poly
  to a metal pad; part of the unit's pattern, used or not per copy (AMB-030).
- Re-read items R29, R30, R32, R33 apply here.

## Corrections from `tl2`-`tl4` (coordinator, from the handoffs of 2026-11-18, second batch)

- **`rcs_cond` and `rcs_cond_lat`** (`tl2` run 4, Tom Seddon; AMB-009 resolved the other way): wherever
  this file gives `rcs_cond` = NOT `rcs_cond_n` and `rcs_cond_lat` <- `rcs_cond` through a pass
  transistor (AMB-009), "the step condition is sampled into `rcs_cond_lat` while CLK is high", and the
  correction above that the pass transistor is gated by `tl3_w3982`: the band of `tl3_w3982` at
  (3046,4546) is a pull-down to VSS, so **`rcs_cond` = NOR(`rcs_cond_n`, `tl3_w3982`)**, and
  `rcs_cond_lat` = NOT `rcs_cond` by an inverter in `tl2`'s strip at y 4005-4145 (through its load's
  tie, AMB-031). `trace/tla.txt` was fixed in `tl2`'s commits d64bc8c and d362cb4. The statement that
  `rcs_cond` = NOT `e4` AND NOT (`e3` AND `a2`) gains the factor NOT `tl3_w3982`; the step formula does
  not use `rcs_cond` and stands.
- The unit of `rcs_n4200`: the diffusion under the g1 band is drawn from x 2990; its west edge is at
  x 2968-2971, and g1's poly runs on west over field to the gap and north (drawn in `trace/tl2.txt`).
  A width only.
- **`rcs_in1` and `rcs_mn3852`** (`tl3` runs 7-8, Tom Seddon; AMB-013): `rcs_in1` = NOT `rcs_mv`, not
  NOR(`rcs_mu`, `rcs_mv`); its node is the load strip y 4070-4096 and the box, its only pull-down under
  gate `rcs_mv`. The transistor under gate `rcs_mu` belongs to `rcs_mn3852` = NOR(`tl3_e3712`,
  `rcs_in1`, `rcs_mu`), by a diffusion branch under the thin metal x 3948-3962 and the VSS rail.
  `D 4052,3955:4090,4135` ran through 70 px of field and was split (e22fb03). `rcs_mn3852`'s upper gate
  (the bottom band of `tl3_e3712`'s poly), its VSS box, arm, column and load are drawn in
  `trace/tl3.txt`; "its other gate (above the node) is not read yet" in this file and in
  `trace/tla.txt` is out of date. Not checked, from `tl3`'s reviewer (R40): gate `rcs_mu`'s channel is
  x ~4072-4108, not 4052-4110, and the piece below it an L; east of the rail below gate `rcs_mv` reads
  field, so `D 4052,4066:4090,4135` may stop at y ~4096 and the `?D` VSS land may not exist.
- **`rcs_mv`**: its track ends on a pad with a contact (4192,4743), whose poly leaves east (`tl3`), and
  it is driven at (4193,4420) by `tl3`'s NOR `rcs_mv` = NOR(`tl3_e4852`, `tl3_w4546`) at y 4345-4514.
  It has a second gate: `tl3`'s unit e3, pad (4190,4288).
- `rcs_in1`'s unit: the VSS land below gate `rcs_mv`, drawn `?D 4005,4130:4092,4165` with
  `?C 4018,4148`, is the rail's VSS box above `tl3`'s unit e3, which `tl3` draws firm (Matt Godbolt).
- The bus piece `M 4148,3371 y3596`: its south end is a pad with a contact (4148,3592) (in
  `trace/tl3.txt`), gate of `tl3_e3550`'s NOR and of `tl3_e3712`'s inverter.
- **Bus line E is driven from `tl4`**: its top pad's poly to the pad (4270,2725) is under the sixth bus
  line, which comes down the track x 4496 from `tl4`'s inverter: `rcs_e3` = NOT `bd1_n2`. The pad
  rectangle `P 4250,2708:4290,2742` is about 8 px west of the pad (x 4258-4298): geometry only.
- The VCC rail `M 3846,3040 y5497` goes on north to y ~2922 (drawn in `trace/tl3.txt`, with E1's VCC
  contact); the VSS rail `M 4017,3050 y5300`'s south end is at y ~5296, as drawn.
- Re-read items R38 (the follower's ends here), R39, R40, R41 (thin metal E), R42 apply here.

## Corrections (coordinator, from the handoffs of 2026-11-19)

- `rcs_thin_e`'s south end: its row y 6327 ends on the pad (3973,6329), whose metal goes south to `ur`'s
  pad (3968,6410) and a poly east along y 6402-6422 (`tl3` run 11; not `sl_l3`).

## Corrections (coordinator, from the handoffs of 2026-11-19, fourth batch)

- `tl3_w3982`'s driver is `eof`'s inverter U4 at (7575,8386) (run 12). For the reader of `rcs_e4`'s line through the nest at y 7888-8275: the tracks west of it are named (x 6645 `lpstb_b`, 6602 `res_b`, 6558 `rst_a`, 6514 `tl3_w3982`; `eof` runs 10-11).

## Corrections (coordinator, from the handoffs of 2026-11-20)

- The input of `rcs_u3288` that this file called g3245 ("comes from ..."): it is `tl5_w2722` = NOT `tl4_w3113` (`tl3` run 12: its row y 2683 is drawn through strip 3 onto `tl4`'s bus line 5; renamed at the refresh of 2026-11-20).
- The third input of `rcs_bc3460` (`tl2`'s w3722): it is `tl5_w4937` = NOT `tl4_w4068` (`tl3` run 12: the row y 2639 onto `tl4`'s bus line 4; renamed).
- The data of `tl1`'s first latch (`tl1`'s w2857) is `rcs_mn3852` (the row y 2857 is one poly from `rcs_mn3852`'s unit to the latch; renamed).

## Corrections (coordinator, from the handoffs of `eof` runs 28-35, 2026-11-21)

- `rcs_e4`'s wire ("the gate of a pull-down under the rail x 7290-7345 of bc1's untraced left column ... the poly ends at x 7370 ... its driver is NOT found"; also the comment in `trace/tla.txt`, not edited): the poly ends at about x 7390 over a field island; the pull-down is gate 1 of the NOR `eof_w15523` = NOR(`rcs_e4`, `eof_w16040`, `h_eq_r1_n`) (`eof`, piece `u15500`); the driver has been found since (`rcs_e4` = NOR(`tl1_w4678`, `tl3_e3550`), `tl1`).

## Corrections (coordinator, from the handoffs of `busl` runs 17-18, 2026-11-24)

- Geometry only, same ends: the diagonal of `rcs_e4` south of its pad (6730,8580), drawn `6732,8655 6560,8828`,
  lies 16 px west of its metal (x + y = 15403; `tools/busl_mdrawn.py h 8700`, `h 8760`; `busl` run 17).

## Run 2 (2026-11-28): re-read item R40, the three units in the middle cluster's east column

Tom Seddon's session, on Claude Fable 5.2, from 2026-11-28 13:40 +0000. Piece `r40`: this file's three units
east of the middle cluster's VSS rail (x 3992-4041), re-read at their own place as R40 asks: unit A, the inverter
that makes `rcs_mu` (y 3300-3450); unit B, `rcs_mn3852`'s two lower pull-downs (y 3836-3990; its top gate, load
and the branch under the rail are `tl3`'s); unit C, `rcs_in1` (y 4040-4170). Region x 3820-4300, y 3300-4170.
Scratch: `cache/scratch/tla/survey.md`, `draft-r40.txt`, images `s1`-`s8`, overlays `o1`-`o3`.

**Result: no connection of the netlist changed except that `rcs_mu`'s load is now drawn** (it was "not drawn": the
net had a pull-down and no load, so the extraction printed no equation for it). Two pull-downs were drawn where
there is field and are now drawn where they are, on the same nets; three widths changed.

```
rcs_mu     = NOT ra_eq_r9                       unit A: pull-down 44/21 under the rail, load 24/56     firm
rcs_mn3852 = NOR(tl3_e3712, rcs_in1, rcs_mu)    unit B: the two lower pull-downs are 36/20 (were 58)    marked (tl3's load tie)
rcs_in1    = NOT rcs_mv                         unit C: pull-down 44/22 under the rail, load 25/56     firm
```

(`tools/unsure.py --equations NAME`: `rcs_mu` and `rcs_in1` FIRM; `rcs_mn3852` DEPENDS, on `tl3`'s uncertain tie
of its load.) Full extraction: 2,547 nets, 4,931 transistors (one more: the load), 0 errors, 0 warnings.

### What was wrong: the "diffusion column just east of the rail"

This file drew every unit of the column on a diffusion column x 4052-4110 directly east of the rail, "as in the
first cluster". `tl3` run 8 found 70 px of it to be field. The rest, read here:

- **East of the rail the open gap x 4050-4070 is field everywhere in this piece.** The gap between the rail (east
  edge x 4047) and the thin metal x 4099-4111 shows the clean shot's open colours between two protected margins,
  which at 2.5x looks like an outlined box. It is not one: `tools/px.py col 4070 3200 3316 8 acid1b,acid` reads
  the same khaki (152-156/133-142/93-102; chip-2 stripped 151-155/142-152/89-100) for 150 px north of unit A's
  gate without a line across, and the gap's values are those of the field below each unit, not of the diffusion
  strips in the same gap (chip-2 stripped red minus green 3-11 against 14-15 on unit A's node strip; clean shot
  8-16 against 22-36).
- **The column exists only at unit B, and is x 4072-4108**, its east third under the thin metal (R40's guess
  "an edge at x ~4072" is right). Rows through it (`px.py row 3875 / 3895 / 3917 / 3941 / 3960 / 3976 4042 4126 3
  all`): a diffusion edge crosses both gate rows at x 4069-4075 (chip-2 metal 59/26/5 and 59/21/5 on a poly that
  reads 150-180 either side); west of it the rows lie on field (row 3875, x 4054-4066: 158-165/146-163/78-80,
  chip-2 stripped green over red; row 3960 likewise); under the thin metal the clean shot is tan between the
  rows (167-204/153-184) and bright salmon under them (219-249/146-188, a gate over its channel), and the
  column's east edge is a dark line at x 4108-4111 at every height. Down it (`px.py col 4082 3838 3998 3
  metal,acid`, `col 4101 ... acid1b,metal1`): node, gate `rcs_in1` y 3886-3906, the VSS arm y 3909-3926, gate
  `rcs_mu` y 3929-3950, the branch's end y 3952-3981, pink field from y 3988.
- **Units A and C are rail gates** (the build of `tl3`'s units 3 and of the inverter at the rail's south end):
  the pull-down is under the rail only, between the rail's VSS box and the node, which is the load's strip
  passing under the rail on its way to the output box east of it.

### Unit A: `rcs_mu` = NOT `ra_eq_r9` (traced; firm)

- Under the rail (`px.py col 4028 3306 3440 4 acid1b,metal1`; `row 3340 / 3374 / 3400 3980 4062 3
  acid1b,metal1`): the VSS box x 4012-4056, y 3322-3348 with its contact (4030,3348); the gate y 3364-3385,
  bright salmon 229-244/156-181 over x 4013-4051 with an edge line across the poly at x 4007-4010 and paler
  salmon (poly over field, 211-229/152-169) west of it; the node, tan, y 3388-3412. The box and the channel end in the east at a second dark line at x ~4056 in both metal
  shots, 9 px beyond the rail's own edge line (review round 4; `px.py row 3340 / 3374 4038 4066 2 all`; the node's
  row 3407 has the rail's line only). **Pull-down 44/21** (was 84/22, half of it on the field east of the rail).
- East of the rail the node is a narrow strip (light interior y 3402-3412 between two edge lines; `px.py col 4070
  3316 3452 4 all`) from under the rail, with no edge line at the rail's edge, to the output box
  (4078-4116, 3398-3432). The gate poly runs on east over field to its stem and pad (4148,3335).
- **The load, new** (`s3_mu_load.png`, 4.6x, four shots; `px.py row 3404 3856 4056 4 acid1b,acid`, `col 3928 3336
  3450 3 all`): the strip runs west from under the rail through the open gap (x 3944-3984, chip-2 stripped red
  minus green 18-24) and under a plate x 3882-3938, y 3378-3440 onto the VCC box that `tl3` draws under the VCC
  rail (x 3819-3879, y 3363-3572). The strip's edges cross the plate at y 3390-3396 and y 3420-3426: **load
  24/56**.
- **The tie is read in the open** (nothing lies over it): a heavy-outlined box (3914-3946, 3345-3378; plain
  centre x 3923-3932, y 3357-3363: chip-2 metal 147-160/120-141/72-77, chip 1 red equal to green) sits on the
  plate's upper edge at its east end, with one 12 px dark band (y 3366-3378) between its centre and the plate's
  upper bar, so there is no room for field between them; east of the box the tail, a diffusion x 3945-3962
  (chip-2 metal plain, blue 80-92; `px.py row 3358 3896 3980 3 all`), runs from y 3354 down into the strip with
  no edge line across (`px.py col 3951 3336 3430 4 all`: light from y 3356 to y 3416). The plate's outline is
  closed on its other three sides. Drawn firm (Ambiguity 1 below).
- The output pad (4192,3416), R38's "top end not looked at": `tools/tl5_tracks.py v 4192 3300 3470` and
  `tools/textmap.py 4160 3330 4222 3440 3`: ring y 3402-3411, bright centre y 3414-3423 in both metal shots, a
  green hole in the clean shot; north of the ring 9 px of bare open ground (y 3393-3399: 8-9 and 6-7 in the two
  metal maps, green in the clean shot). The metal arrives from the south only; the diagonal metal that passes at
  y 3366-3386 (from the track x 4192 north of here to the lower piece of the track x 4148) is another net, 16 px
  from the ring. As drawn.

### Unit B: the two lower pull-downs of `rcs_mn3852` (traced; widths only)

- The column as above; both pull-downs **36 wide** (were 58): gate `rcs_in1` 36/19, gate `rcs_mu` 36/20.
- The node's band y 3847-3862 comes from under the rail (`tl3`'s strip) to the column; between it and gate
  `rcs_in1`'s row west of the column is field (`px.py col 4063 3830 3996 3 all`, y 3872-3878 green over red in
  the chip-2 stripped shot), and under the rail there too (pink, 188/127/118 at (4042,3875)).
- The rail's VSS box x 4002-4040, y 3888-3928 (`px.py row 3895 3984 4056 4`, `col 4020 3830 4000 4`; its east
  edge from review round 4: `px.py col 4043` and `col 4047 3878 3936 3` are tan only at the arm's height), contact
  (4018,3910) as before; its arm east, interior y 3912-3924, joins the column between the two gate rows with no
  edge line from the box to x 4090 (`px.py row 3917`).
- Below gate `rcs_mu` the column ends at y ~3982 and a band y 3968-3982 leaves it west onto `tl3`'s band under
  the rail (`px.py row 3976`: plain from x 4051 to x 4090 without an edge), the branch that makes this the third
  pull-down of `rcs_mn3852` (`tl3` run 8, unchanged). West of the column between the band and the gate row:
  field. "The piece below it an L" (R40): yes.
- Gate `rcs_in1`'s row lies at y 3886-3905 along its length (`px.py col 4135` and `col 4215 3872 3916 2`); it was
  drawn 3 px north. Its west end is at the rail's edge (x ~4050); the VSS box under the rail has no poly across
  it (`px.py row 3895`: tan x 4004-4036).

### Unit C: `rcs_in1` = NOT `rcs_mv` (traced; firm)

- **The pull-down is under the rail** (`px.py col 4026 4050 4182 4 acid1b,metal1`): node (the load's strip) tan
  y 4082-4098, gate `rcs_mv` y 4103-4122 bright salmon 235-240/149-171 (a gate over its channel), tan again from
  y 4130: the rail's VSS box, which `tl3`'s cell `tl3_enor` draws with its contact (4027,4162). The channel is
  x 4013-4051 (`px.py row 4112 3980 4062 3 acid1b,acid,metal1`: an edge line across the poly at x 4007-4010,
  poly over field west of it; `row 4136`: the box x 4013-4051, pink field west of it), and its east edge, like unit A's, is the second dark line
  at x ~4056 (review round 4; `px.py row 4113 / 4136 4038 4066 2 all`). **44/22.** This is what
  this file's old comment meant by "the poly runs on west under the rail and is bright there: it also gates
  something under the rail (not read)".
- **East of the rail below gate `rcs_mv` is field** (`px.py col 4068 4046 4180 3 all`: y 4133-4160 reads as the
  open field at y 4046-4058 in all four shots; `s7_c_east.png`, 4.5x: the "box" there is bounded by the rail's
  edge, the thin metal's edge, the gate row and the next unit's arm). The transistor drawn there (38/22, on a
  `?D` land with a `?C`) did not exist; the land's part under the rail is `tl3`'s VSS box. Same nets, and the
  equation no longer rests on an uncertain item.
- East of the rail the node's strip (y 4079-4095) runs from under the rail to the output box (4076-4114,
  4056-4094), as before.
- The load (`s8_c_load.png`, 4.4x, four shots; `px.py row 4084 3820 3996 4 all`, `col 3927 4040 4160 3 all`):
  VCC box x 3824-3878, y 4071-4130 with one contact (`tools/textmap.py 3818 4040 3884 4180 3`: ring, bright
  centre x 3839-3851, y 4088-4112; R29's question about VCC boxes: one box, one contact here); plate x 3882-3938,
  y 4048-4118 with the strip's edges across it at y 4067-4073 and y 4094-4100: **load 25/56**.
- **The tie, re-read** (it was drawn `?P`/`?B` "as in the first cluster", 12 px east of where it is): the same
  form as unit A's, turned over. A heavy box (3912-3944, 4120-4150; plain centre x 3920-3932, y 4130-4136) hangs
  on the plate's lower edge at its east end (one 10 px dark band, y 4118-4127, between the plate's lower bar and
  the centre); east of it the tail lies under the thin metal x 3948-3962, where the clean shot is tan without a
  break from the strip down to y 4134 (`px.py col 3956 4050 4166 4 acid1b,acid`: 195-202/147-180/133-143, no
  edge at the strip's lower side; pink above y 4062 and below y 4150), x 3943-3963 (`px.py row 4133 3890 3984 3
  all`). Drawn firm (Ambiguity 1).

### Ports of run 2 (`ports.d/tla.txt`, started with this run)

| Name | Layer | Place | Direction | What |
|---|---|---|---|---|
| `ra_eq_r9` | M | (4148,3320) | in | north end of the bus piece x 4138-4160 above unit A's gate pad (4148,3335); R9's match, from `r9m` |
| `rcs_mn3852` | M | (4233,2852) | out | top of the bus piece x 4222-4245 from unit B's output pad (4225,3852); `tl3`'s row y 2857 lands on its top pad |
| `rcs_mv` | M | (4192,4748) | in | south end of the bus piece x 4183-4205 from unit C's gate pad (4195,4112); `tl3` draws its pad (4192,4743) and its driver's contact (4193,4420) |

`tools/ports.py --prefix tla`: 2 meetings, both the same place and **not a join**: `rcs_mn3852` M (4233,2852) against
`tl3`'s and `tl4`'s `ck_out` P (4250,2810), 36 px, names differ. The bus piece ends on its pad (ring y 2841-2850,
bright centre y 2853-2859, hole in the clean shot) and there is no metal north of it (`tools/tl5_tracks.py v 4233
2780 2900`: no metal in either chip y 2780-2851); `ck_out`'s row y 2808-2817 passes 25 px north of the ring with
open ground between (`tools/textmap.py 4206 2796 4262 2880 3`). Two ports without a partner (`ra_eq_r9`: `r9m` has no
ports file; `rcs_mv`: `tl3` lists the pad's poly at x 4250, not the pad).

### Ambiguities of run 2

1. **The two ties are drawn firm**, unlike most load ties of these clusters. What is seen: the box directly on
   the plate's edge (one outline band between the plate's bar and the box's centre, 10-12 px, the width of the
   box's other sides), the tail beside the box (one band between), the tail running into the strip without an
   edge, the plate closed on its other sides. What is not seen, as for every buried contact: the poly and the
   diffusion inside the box's outline. Unit A's is in the open in all four shots; unit C's tail is under the thin
   metal x 3948-3962 (read from the clean shot's protected colours). If either were not a tie, the plate would
   float; no other reading was found. The thin metal over unit C's tail is `tl3`'s item (`?M` there, AMB-032).
2. **The joins under the rail's east edge line** (x 4045-4051): unit A's and unit C's node from under the rail
   to the strip east of it, unit B's arm and band. Each is read from diffusion colour within 3 px either side and
   no line across in the chip-2 stripped shot (the rail's own edge line lies there in the metal shots). If unit
   A's or C's were cut, the unit's output box would be on nothing.
3. **Unit A's output box under the thin metal x 4099-4111** ((4101,3413): a bright spot in a dark stretch, in
   both metal shots): `tl3` draws the metal `?M` there and reads no contact (trap 26). Not re-read here; a
   contact there would put `rst_ck` on `rcs_mu`.
4. `rcs_in1`'s box under the same thin metal ((4102,4074)): `tl3`'s `?M`, "not decided" in its comment. Not
   re-read here.

### Not done after run 2

- R40 for the middle cluster is done with this run. **R40's second half, "the same check in `tla`'s first
  cluster"** (every unit drawn on "a column just east of R3", x 3030-3063, and its mirror west of R1), is not
  done: that is the next piece. Start with `px.py col` down x 3046 and x 2571 (the gaps beside R3 and R1) from
  y 3000 to y 5330 against this run's field values, then each unit as here.
- The rest of this file's Not done list above is unchanged (R29, R30, R32, R38's other ends, R39, R41, R42;
  `rcs_iso2958`; the west column y 3590-4940; thin metal W).
- `ports.d/tla.txt` holds only this piece's three wire ends; the file's other ports are still only in the tables
  of "Status" and "The west column".

## Run 3 (2026-11-28): re-read item R40's second half, the columns beside R3 and R1

Tom Seddon's session, on Claude Fable 5.2, from 2026-11-28 14:28 +0000. Piece `r40b`: "the same check in `tla`'s
first cluster" (R40): every unit drawn on the column just east of R3 (x 3030-3063) and on its mirror west of R1
(x 2550-2592). Regions x 2940-3090, y 3000-5310 and x 2520-2660, y 5095-5310. Scratch: `cache/scratch/tla/survey.md`
("run 3"), images `r40b_s1`-`r40b_s8` (`s3`-`s7` with every package's trace outlined).

| Unit | y | Pull-downs (gate, y) |
|---|---|---|
| `rcs_c1` | 3039-3183 | `rcs_b1` 3074, `rcs_a2` 3157 |
| `rcs_u3288` | 3218-3372 | `tl5_w2722` 3246, `rcs_bd3330` 3330 |
| `rcs_u3425` | 3402-3482 | `rcs_bc3460` 3461 (its second transistor, `rcs_iso2958`'s, is under the rail: not this piece) |
| `rcs_b1` | 3478-3662 | `rcs_x1` 3547, `rcs_a2` 3638 (its third, under thin metal E: not this piece) |
| `rcs_bc3460` | 3818-3972 | `rcs_e3` 3852, `rcs_e4` 3940 (`tl2` draws the two above, y 3722 and 3808) |
| `rcs_cond` | 4514-4663 | `tl3_w3982` 4546, `rcs_cond_n` 4636 |
| `rcs_cond_n` | 4690-4842 | `rcs_in2` 4722, `rcs_in3` 4806 |
| `rcs_in3` | 5122-5266 | `rcs_e3` 5157, `rcs_e4` 5240 |
| `rcs_in2` (west) | 5120-5282 | `rcs_w2` 5153, `rcs_e4` 5240 |

**Result: found as drawn. No connection changed; one item lost its `?`; review round 5 moved two node strips and six arm ends by 7-12 px (geometry only).** `rcs_b1` =
NOR(`rcs_a2`, `rcs_u3425`, `rcs_x1`) is firm now (`tools/unsure.py --equations rcs_b1`; 1,002 of 1,464 equations
firm, was 1,001; uncertain items 1,235, was 1,236). Full extraction 2,547 nets, 4,931 transistors, 0 errors, 0
warnings; `tools/t.sh tla sameconn.py f5adf76a` and `.venv/bin/python tools/sameconn.py f5adf76a`: connections
identical.

### Why the middle cluster's mistake is not repeated here

In the middle cluster (run 2) the "column just east of the rail" lay in a 50 px gap between the rail and a thin
metal, where the clean shot's open colours between two protected margins pass for an outlined box. **Here nothing
lies east of R3 before bus line A (x 3097): the column is in the open**, and both chip-2 shots show it plainly
(outline, gate rows, node boxes: `r40b_s2.png` at 4x, `s3`-`s6` at 2.7-3x). Measured all the same, as R40 asks:

- **Every column end to end** (`tools/px.py col 3046 3000 3700 6 acid1b,acid,metal`; `col 3036 3784 4004 4`,
  `col 3036 4496 4860 4`, `col 3036 5104 5304 4`, `col 2571 5104 5304 4 metal,acid,acid1b`). In the chip-2
  stripped shot red minus green is -9 to +6 on the field between the units (y 3198-3204, 3378-3396, 3678-3684,
  3976-4000, 4672-4680, 4848-4860, 5284-5304), 15-30 on the column's diffusion and 30-45 on the gate rows. Each
  unit reads arm, gate, node, gate, arm, as drawn. The VSS section between `rcs_u3425`'s gate and `rcs_b1`'s gate
  `rcs_x1` (y 3478-3530) is a large open diffusion (clean shot green, 133-143/140-164/84-104; chip-2 stripped
  165/141/99: trap 21).
- **Each gate's channel** (`px.py row Y 2952 3084 3 metal,metal1,acid,acid1b` at the fifteen gate rows; `row 3074 /
  3246 / 3547 / 4722 3016 3074 1 metal`): a diffusion edge line crosses every gate row on each side of the column,
  at x 3027-3028 and x 3064-3065, and at x 3031-3032 and x 3068-3069 for the four rows of `rcs_b1` and `rcs_bc3460`
  (those two units lie 4 px east, in both chips). 37 px centre to centre; drawn x 3030-3063 (33). Each edge is
  within 2-5 px of its line: **not redrawn**. The west unit (`row 5153 / 5240 2528 2612 3`): lines at x 2549-2552
  and x 2588-2591, about 39; drawn 42. Gate lengths (`px.py col 3052 Y-22 Y+22 1 metal`): the two edge lines are 28
  px apart centre to centre at every gate (a bright band of about 20); drawn 16 to 25, not redrawn.
- **What the gate rows do under the rail: nothing.** Each row comes from the east, crosses the column, lies on
  field for x 3009-3021 and ends at the rail's edge line (x 3004-3009). Under R3 at every one of the fifteen rows
  the clean shot is the rail's field (pink 184-205/115-128 with the olive stripe 152-170/139-157 down the middle),
  never the salmon of a poly: no rail gate like units A and C of the middle cluster. The west unit's two rows end
  at R1's west edge likewise (`px.py row 5153 / 5240 2594 2662 3 acid1b,metal1`: pink and olive under R1; the rail
  gate of `rcs_w2` at y 5066, for comparison, 238-250/168-183).
- **The nodes' strips west under the rail** are the pale bands of the chip-2 stripped shot at y 3105-3124,
  3278-3297, 3412-3445, 3882-3901, 4578-4600, 4755-4772 and 5186-5208 (east) and y 5193-5207 (west, eastwards), as
  drawn. Their loads west of R3 are not part of this piece (R30, R32(c)-(e), R41).
- Nothing is undrawn inside the units' own rectangles (x 2940-3080 at y 3000-3195 on `r40b_s1.png` with this
  file's trace; y 3195-3675, 3770-4015, 4490-4870 and 5095-5310 on `s3`-`s6`, and x 2520-2660, y 5095-5310 on
  `s7`, with every package's trace outlined), except the node box without a poly at (3045-3070, 3415-3440), which
  is AMB-030. The stretches of the column between those cuts (y 3675-3770, 4015-4490, 4870-5095) hold other units
  (`tl2`'s, the AND-OR-INVERT, the step gate) and were not looked at in this piece.

### The VSS join at (3020,3500): `?D` made firm

`?D 2968,3470:3035,3528` was the box under R3 with the contact (2990,3500) and "its join to the column's top (join
seen only as a heavy line at the rail's edge: assumed, as in the other units)". Read (`r40b_s8.png`, 4.2x, three
shots; `px.py row 3490 / 3500 / 3515 2986 3040 2 all`; `px.py col 3008 / 3014 / 3040 3462 3544 2 acid,acid1b`):

- under the rail the clean shot is tan (195-204/150-183) without a break from x 2986 to x 3018; then one line (red
  83-94 at x 3024, 3-5 px under 110); then the open diffusion. In the chip-2 stripped shot the line is at
  x 3016-3022 (red 60, 7-9 px under 100), with red minus green 16-25 west of it and 23-46 east of it;
- the box's upper and lower edges under the rail are at y 3482 and y 3532, the open part's at y 3477 and y 3535
  (the two gate rows);
- one line of 6-9 px cannot be two diffusion edges with field between.

So it is one diffusion with the rail's edge line across it, and it is drawn `D`. **The same is true of every arm of
these columns** (fourteen joins of an arm to its box under the rail, drawn firm from the start). The line's depth
does not tell a join from a gap: across x 3000-3030 the chip-2 stripped shot's darkest red is 39-84 at the arms,
60 at this join, and 31 and 83 at two places with field on both sides (y 3390, y 3290); 42 over 14 px where a box
under the rail ends against field (y 3200). What is read is what lies either side of the line.

### Ambiguities of run 3

1. **The joins under R3's east edge line and R1's west edge line**: every arm of the columns to its VSS box under
   the rail, and the join at (3020,3500). Each is read from diffusion on both sides up to one line of 6-9 px at the
   rail's edge, and edges that agree within 5 px; under the line itself nothing is seen in any shot (the rail's
   edge in the metal shots, the etch line in the stripped ones). If one were cut, that unit's column would have no
   VSS at that end. This is Ambiguity 2 of run 2 for this cluster.
2. `rcs_u3425` = NOR(`rcs_bc3460`, `rcs_iso2958`) stays marked: `rcs_iso2958`'s transistor rests on the link
   `?D 2936,3462:2972,3500` in the gap between thin metal E and the rail, and its gate has no connection found
   (Not done, above). Not re-read here.

### Not done after run 3

- R40 is done for `tla` with this run (both halves).
- Next for this file, in the order of the re-read list: **R23 and R42 for the first cluster's rail gates** (the
  step gate's three pull-downs at y 4938, 5010, 5065 under R3; `rcs_w2` at (2625,5066) and `tla_w3505` at
  (2626,3243) under R1): a second patch of the same device beyond the rail, and the box's edge at the second dark
  line about 9 px beyond the rail's own (run 2, review round 4). Then **the loads west of R3 and east of R1 of the
  units of this piece** (R30; R32(c)-(e): the ties at y 3134, 3307, 4615, 4790, 5216 drawn by analogy, each
  load's gate poly beyond its tie box; R41: thin metal E over the tie boxes), R32(a) (the gate rows' ends on the
  bus pads), R29, R38's other ends, R39.
- The rest of this file's Not done list is unchanged (`rcs_iso2958`; the west column y 3590-4940; thin metal W;
  the boxes without a poly; bus pieces; `ports.d/tla.txt` for the file's older wires).

## Run 4 (2026-11-28): re-read items R23 and R42, the first cluster's rail gates

Tom Seddon's session, on Claude Fable 5.2, from 2026-11-28 15:14 +0000. Piece `rg`: the pull-downs of this file that
sit under a rail ("rail gates"), re-read for R23 (a second closed patch of the same device beyond the rail) and R42
(the box's edges against the rail's own edge lines; poly against diffusion in the gap between a rail and a thin
metal): the step gate's three under R3 (x 2880-3080, y 4890-5150), `rcs_w2` (x 2530-2700, y 5000-5110) and
`tla_w3505` (x 2560-2700, y 3190-3300) under R1, and, of the same build in this file though outside the package's
region, the pull-down of `clk_tl`'s driver (x 2525-2700, y 7845-7970). Not in this piece: the top unit
`rcs_u3288_n` (found on both sides of R1 in 2026-11-17's review rounds 1 and 2), the selector (drawn across R1 from
the start), the AND-OR-INVERT's gates under R3 (R32(b); `tl2` re-read its g3) and `rcs_iso2958`'s transistor.
Scratch: `cache/scratch/tla/survey.md` ("run 4"), images `rg_s1`-`rg_s5`, overlays `rg_o1`, `rg_o2`;
`cache/scratch/tla/mat.py` prints a matrix of `tools/px.py`'s numbers (the commands below give the same numbers row
by row).

**Result: no connection changed; six widths.** `tools/t.sh tla sameconn.py 73f39883` and `.venv/bin/python
tools/sameconn.py 73f39883`: connections identical. Review round 6 (full): no finding that changes a connection; two
geometry-only fixes (the two gate rows' west ends, two rail boxes' east edges). Full extraction 2,547 nets, 4,931 transistors, 0 errors, 0
warnings.

| Pull-down | Gate | Was | Is | What was found |
|---|---|---|---|---|
| step gate, (2964,4938) | `rcs_in1` | 52/18 | 69/18 | the box runs on west of R3 to thin metal E |
| step gate, (2964,5010) | `rcs_in2` | 52/19 | 69/19 | the same box |
| step gate, (3004,5065) | `rcs_in3` | 38/20 | 70/20 | a second part east of R3 (R23) |
| `rcs_w2`, (2626,5066) | `rcs_c1` | 54/18 | 44/18 | the box's east edge is 12 px inside R1's edge line |
| `tla_w3505`, (2626,3243) | `rcs_thin_e` | 57/18 | 44/18 | the same |
| `clk_tl`'s driver, (2615,7908) | `ck_out` | 52/24 | 66/24 | a second part west of its rail (R23); east edge as `rcs_w2`'s |

### The rails' own edge lines

Under a rail a diffusion's edge and the rail's edge are two lines, and which is which is read from a row where the
rail lies on field. R3's east edge line is at x 3006 (`px.py row 4882 2984 3030 2 metal`: bright to x 3000, 62-70 at
x 3006, 143 at x 3012; the same at y 4876-4894, above the step gate); its west edge line at x 2950-2954, thin metal
E's east edge line at x 2926-2928, and the open gap between them x 2930-2948. R1's metal at these units is bright
x 2608-2650 with edge lines at x 2601 and x 2659.

### The step gate's box under R3: gates `in1` and `in2` (traced; 69 wide)

- **East edge, as drawn** (x 2998): a second line 8 px inside the rail's own (`px.py row 4912 / 4936 / 5008 2984
  3030 2 metal`: red 83-92, 65-75 and 72-119 at x 2998, a bump at x 3000-3002, the rail's line at x 3006; clean shot
  dark at x 2996-2999, then the margin's pink or salmon). It is absent at y 5038-5044, where the node's strip goes
  on east, and at gate `in3`'s rows. East of the rail above `in1`'s row and between the two rows is field (chip-2
  stripped red minus green -4 to +8 at y 4915 and y 4960), and no edge line crosses `in1`'s row there (`px.py row
  4936 2984 3030 2 metal`: 145-178 over x 3012-3030). No second part in the east.
- **West: the box runs on out of the rail through the gap to thin metal E** (`rg_s4.png`, 5.5x, three shots). The
  trace had its west edge at x 2947, the rail's. Read:
  - in the gap (x 2932-2948) the two gate rows are poly (chip-2 metal blue 35-61) and the stretches above, between
    and below them are plain (blue 78-92): the U's top band (y 4904-4916), **the stretch between the rows
    (y 4955-4992)** and the U's bottom band (y 5030-5042). The three read alike and unlike the field in the same
    gap above and below the gate, in all four shots (`px.py pt 2940,4860 2940,4884 2940,4910 2940,4972 2940,4982
    2940,5036 2940,5092 2940,5112 2940,5180 2940,5300 all --r 3`): chip-2 stripped red minus green 28-47 against
    4-13; clean shot red over green by 30-40 against green at or above red; chip-2 metal 170-172/133-136 against
    162-164/139-145;
  - no edge line crosses either gate row between E's edge line and the rail's (`px.py row 4934 / 5006 2922 2962 2
    metal,metal1`: chip-2 red 154-168 flat over x 2934-2946) (trap 38's test);
  - the U's inner field is the strip x 2906-2926, y 4920-5027 **under thin metal E**: a closed rounded outline,
    green inside in the chip-2 stripped shot, pink in the clean shot (193/140/112 at (2918,4972), against
    158/164/101 on the top band under E at (2914,4915)). The gap's stretches lie outside that outline.
- So the VSS box and both channels are x 2930-2998. The gate rows go on under E past the box's edge, to x ~2913
  and x ~2919 (review round 6).
- Gate lengths in the open gap (`px.py col 2940 4898 5054 6 metal`): edge lines at y 4922 and y 4952, y 4994 and
  y 5024 (30 centre to centre, poly about 22); drawn 18 and 19, not redrawn.

### Gate `in3` (traced; 70 wide): a second part east of the rail

`rg_s2.png` (5.5x, four shots); `px.py row 5066 / 5090 3004 3064 2 metal,metal1`.

- **One heavy line, in both metal shots and the chip-2 stripped shot**, comes down x 3038-3040 from the node's
  buried-contact box, **crosses the gate row** (chip-2 metal red 47-62, chip 1 35-45, on a poly that reads 150-188
  either side, blue 47-71), goes on to y 5096, west along y 5098-5100 to x 3018, south along x 3017 to y 5120 and
  east along y 5121 as the upper edge of the unit's arm. East of it and in the pocket x 3020-3060, y 5104-5118 is
  field (chip-2 stripped red minus green -8 to +6; clean shot khaki, green 131-143).
- Inside it, below the gate, is a plain patch x 3012-3036, y 5084-5096: not poly (chip-2 metal blue 74-88); chip-2
  stripped red minus green 13-28 at y 5092 and 7-16 at y 5086 (a 12 px band between two edges: trap 38's flanks);
  in the clean shot red-brown like the arm at y 5128-5134 (green 66-100, red over green by 23-54).
- Above the gate the node's strip (y 5030-5048) lies against the row from the rail to the same line.
- Between the patch and the box under the rail lies the rail's own edge line (x 3006; clean shot tan to x 3008,
  dark x 3011-3017): one line, the standing of every arm of this column (run 3, Ambiguity 1).
- The box's west edge under the rail is the dark line x 2966-2968 of the clean shot (`px.py row 5088 / 5064 2944
  2990 2 acid1b`: tan, and at the gate rows bright salmon 213-252, from x 2972; pink field west of it); the poly
  runs on over field to x ~2956 (paler salmon x 2956-2962).
- So the channel is x 2969-3039: the pull-down drawn 38 wide under the rail is 70.

### `rcs_w2` and `tla_w3505` under R1 (traced; 44 wide each)

`rg_s3.png` (4x, four shots; `rcs_w2`); `px.py row 5040 / 5064 / 5096 2584 2692 3 metal,acid1b` and `row 3216 / 3244
/ 3264 2581 2692 3 metal,acid1b`.

- **East edge**: a line at x 2647 in the chip-2 metal shot, 12 px inside the rail's edge line, and dark x 2647-2650
  in the clean shot, **at the gate rows and the VSS rows and not at the node rows** (y 5036-5044; y 3212-3220: tan
  through to x 2662, the node's strip going east to the load). East of it under the rail's margin the gate rows are
  salmon (poly over field, 215-240/135-176 at x 2656-2662) and the VSS rows pink (`px.py col 2656 4980 5130 6
  acid1b,metal,acid,metal1`: 186-197/105-131/100-128 beside the VSS box as above the unit, where the rail lies on
  field; at 4x the pink strip beside the salmon looks like more of the gate). The poly ends at x ~2672, as drawn.
- **West edge**: one line at x 2599-2602, bright salmon from x 2605.
- **No second part** (R23). West of R1 below each gate is field (chip-2 stripped red minus green -18 to +7 at
  y 5084-5108 and -22 to +7 at y 3264-3294; chip-2 metal plain from the row's lower edge down, with no line), and no
  edge line crosses either row west of the rail (`px.py row 5066 / 3244 2560 2612 3 metal,metal1`: chip 2 151-169
  flat). In the gap east of R1 (x 2662-2680) below each gate the chip-2 stripped shot reads about 0-20 (a streak of
  12-29 at x 2668 at both units), against 22-52 on the node strips (y 5042, y 3220) and on the selector's diffusion
  in the same gap (y 3308-3340).
- So each channel is x 2604-2648, 44 wide, like units A and C of the middle cluster (run 2). The node above each
  gate is drawn across the rail as before (it joins the part west of the rail to the strip east of it).

### The pull-down of `clk_tl`'s driver (traced; 66 wide): a second part west of its rail

In this file since 2026-11-16 ("a rail gate like `rcs_w2`'s"), at (2626,7908), outside the package's region.
`rg_s5.png` (4x, four shots); `px.py row 7908 2562 2612 2 metal,metal1`; `px.py col 2590 7890 7952 2 all`.

- **West**: the same figure as gate `in3`'s east part. One heavy line comes down x 2576-2580 from the node's
  buried-contact box, crosses the gate row (60-66 in chip 2, 42-60 in chip 1, on a poly reading 155-173 either
  side), goes on to y 7940 and east along y 7940-7944 to the rail. Inside it below the gate a plain patch
  x 2584-2599, y 7926-7938 (chip-2 metal 136-178/112-144/62-96; chip-2 stripped red minus green -9 on its north
  flank and +35 on its south, against -34 to -11 on the field below the line). The rail's edge line (x 2604-2606)
  lies between the patch and the box under the rail.
- **East**: as `rcs_w2`'s: dark x 2650 in the clean shot at the gate rows and the VSS rows, pink field at x 2656
  below the gate, tan through at the node rows (y 7880-7884).
- So the channel is x 2582-2648, 66 wide (was 52).

### Ambiguities of run 4

1. **The second parts join the boxes under their rails across the rail's own edge line** (gate `in3` at x 3006,
   `clk_tl`'s driver at x 2604-2606), and the step gate's box crosses R3's west edge line (x 2950-2954) into the
   gap. Each is read from diffusion on both sides of one line, as every arm of the columns is (run 3, Ambiguity 1).
   If `in3`'s or the driver's were cut, the patch below the gate would be a diffusion on nothing and the device
   would be the width it was drawn before; the gate, the node and the supply are the same either way.
2. **Where the step gate's two gate rows end in the west**: settled by review round 6. They end under thin metal
   E, at x ~2913 (`rcs_in1`) and x ~2919 (`rcs_in2`), 8-14 px past the box's edge (chip-2 stripped shot: red over
   green on the rows, green between them). Drawn so.
3. **The patches below the gates are 12 px bands between two edge lines**, classed by the heavy line that bounds
   them and crosses the gate row in three shots, by the chip-2 metal shot's blue (not poly) and by the chip-2
   stripped shot against the field beyond the line; the two flanks of such a band read differently there (trap 38).

### Not done after run 4

- R23 and R42 are done for the rail gates named above. **Left of R23 / R42 / R32(b) in this file**: the
  AND-OR-INVERT's gates under R3 (g1, g2 at y 4116, 4162, with the metal of `rcs_cond_lat` beside the rail) and
  `rcs_iso2958`'s transistor under R3's west edge (y 3462-3500).
- Next, in the order of the re-read list: **the loads west of R3 and east of R1 of the first cluster's units**
  (R30; R32(c)-(e): the ties at y 3134, 3307, 4615, 4790, 5216 drawn by analogy, each load's gate poly beyond its
  tie box; R41: thin metal E over the tie boxes), the step gate's load and its uncertain tie at (2885-2908,
  4958-4996), R32(a) (the gate rows' ends on the bus pads), R29, R38's other ends, R39.
- From review round 6, not looked at further: the 6-9 px between the node's buried-contact box (3042-3071,
  5012-5049) and `rcs_in3`'s row (y 5055) are dark throughout in both metal shots, so their separation is not
  resolved there (the box is the step request's exit to `bw`'s poly; a join would tie `rcs_in3` to the node). Read
  it in the stripped shots with the step gate's load.
- Seen in passing, not drawn: gate `in2`'s poly east of the rail is a curved band from the row y 4970-4992 down to
  the gate band (x ~3005-3035 on `rg_o1.png`), drawn as a straight stub x 3000-3012; same ends.
- The rest of this file's Not done list is unchanged (`rcs_iso2958`; the west column y 3590-4940; thin metal W;
  the boxes without a poly; bus pieces; `ports.d/tla.txt` for the file's older wires).

## Run 5 (2026-11-28): the AND-OR-INVERT's gates under R3, and the gate called `rcs_iso2958`

Tom Seddon's session, on Claude Fable 5.2, from 2026-11-28 15:54 +0000. Two pieces, what run 4 left of R23 / R42 /
R32(b): piece `aoi`, gates g1 and g2 of `rcs_n4200`'s unit and the stack under them (x 2930-3140, y 4080-4190),
and piece `iso`, the second transistor on `rcs_u3425` (x 2890-3010, y 3440-3560), which also falls under R32(d)
(a load's gate poly beyond its tie box). Scratch: `cache/scratch/tla/survey.md` ("run 5"), `draft-aoi.txt`,
`draft-iso.txt`, images `aoi_s1.png` (3x, four shots), `iso_s1.png` (5x), `iso_s2.png` (7x), overlays `aoi_o1.png`,
`iso_o1.png`; `cache/scratch/tla/mat.py` prints the matrices cited as "mat.py" (the same numbers as
`tools/px.py`).

**Result.** One connection changed, through an uncertain piece: the gate of the second transistor on `rcs_u3425`
is drawn onto `rcs_b1`'s load plate. One `?D` became firm. Two pull-downs changed width. Full extraction 2,546
nets (one fewer: the gate's net is `rcs_b1`'s), 4,931 transistors, 0 errors, 0 warnings; `tools/unsure.py
--equations`: 1,002 of 1,464 firm (was 1,002: `rcs_u3425`'s equation DEPENDS before and after, on a different
item), 1,235 uncertain items (one `?D` fewer, one `?P` more).
Review round 7 (full): no finding that changes a connection; one geometry-only fix (the VSS box's outline beside
the channel; `tools/sameconn.py 26f28ec5`: connections identical, package alone and every trace file).

```
rcs_u3425 = NOR(rcs_bc3460, rcs_b1)                  marked: the ?P through the tie box's east outline (was NOR(rcs_bc3460, rcs_iso2958), a gate with no feed)
rcs_b1    = NOR(rcs_x1, rcs_a2, rcs_u3425)           firm, as before
rcs_n4200 = NOT((clk_tl AND rcs_cond) OR rcs_bd3330 OR rcs_x1)   as before (marked through tl2's item); g1, g2 80/20 along the bent bands (69 across; were 60/23, 56/25)
```

### Piece `iso`: the gate has a feed (believed), and the pair is a latch

What was drawn: a vertical poly x 2950-2968, y 3449-3547 under R3's west edge, "rounded cap at the top, a 45 px
stub over field at the bottom, no connection found" (AMB-022), over a diffusion link drawn `?D`.

- **The poly, end to end** (`tools/px.py col 2958 3436 3680 4 all`, clean shot): cap y 3448-3458 (poly over
  field, 198-223/112-174/90-120), edge line y 3460-3464, channel y 3468-3496 (245-253/164-184/125-130), edge
  line y 3500-3504, poly over field y 3508-3544 (210-228/124-174/108-124), end at y ~3547, pink field
  y 3552-3576 (195-201/110-128/120-132), `rcs_b1`'s strip from y 3588. The cap ends 15 px above the channel
  and 2-4 px below the lower edge line of `rcs_u3425`'s strip: an ordinary overhang.
- **The bottom end turns west as a foot** (`iso_s2.png`, 7x, four shots; `px.py row 3518 / 3534 / 3540 / 3546 /
  3552 2900 2982 3 all`; `col 2940 / 2945 3504 3562 3 all`). At y 3531-3546, x 2942-2950, in the gap just west
  of R3's edge line, **both metal shots show open poly**: chip 2 128-146/98-116/44-63, chip 1 145-178/75-95/43-56
  (control, the row of `rcs_cond_lat` crossing the same gap over field at y 4020, `px.py row 4020 2915 2960 3
  all`: chip 2 163-170/125-132/60-65, chip 1 134-149/67-82/34-48). Above the foot, y 3507-3528, the same x is a
  dark line (59-67/50-68/25-36), the stub's west edge; below it, y 3549-3552, the gap is green in the clean shot
  (113/112/55, 111/124/67).
- **Foot and stub are one poly**: in the clean shot row 3540 is salmon without a line from x 2948 to x 2963
  (194-228/126-183); the dip at x 2951-2954 in the metal shots (85-93) is R3's own edge line, the same as at
  y 4020 (91-97), where a poly certainly runs on under the rail.
- **West of the foot lies one dark band, then the tie box of `rcs_b1`'s load** (`px.py row 3540 2876 2932 3 all`
  with the row above; `col 2925 3512 3572 3 all`). From the plate eastwards along y 3540, clean shot: the arm
  (salmon to x 2903, dark red in the open sliver between the strap and thin metal E, x 2891-2897), the box's
  west outline x 2906-2917, its interior x 2919-2929 (tan 192-205/162-172/115-141; y 3533-3546), **its east
  outline x 2931-2938 (62-65/63-91/45-69)**, the foot (dark red x 2939-2946 in the open sliver, salmon from
  x 2948). The east side reads as the west side does: outline band, then poly. The foot's height (y 3530-3547)
  is the height of the arm inside the box (y 3533-3546).
- **No field between the foot and the box**: in the gap at y 3534-3546, x 2930-2939 is dark in both metal shots
  (35-88) where the field of the same gap, 20 px north (`col 2940`, y 3510-3519), is plain and bright
  (133-138/127-134/72-78).
- **What is not seen**: poly through the 7-10 px of the box's east outline, as at every buried contact (run 2,
  Ambiguity 1). So the arm is drawn firm into the box (`P 2888,3531:2930,3553`), the foot firm from x 2942
  (`P 2942,3531:2968,3547`), and the stretch through the outline uncertain (`?P 2928,3531:2944,3547`). The tie
  box was drawn to x 2946, over the foot; it is drawn to its outline (x 2938) with its diffusion (x 2936), so
  that without the `?P` the stub is an unnamed gate again and `tools/unsure.py --equations rcs_u3425` says
  DEPENDS (`without ?: NOR(n…, rcs_bc3460)`). The poly's old name `rcs_iso2958` is kept as an alias of
  `rcs_b1`, with its label on the uncertain piece.
- **For the join**, beside the photos: the stub runs 45 px past its channel to exactly the arm's height and
  ends there; the same unit mirrored in the middle cluster has the same vertical poly ending at its lower
  unit's plate arm (`tl3`, AMB-030: drawn joined, `?`); and the unit below this one in the same column has the
  build once more, a load plate's poly that runs on past its tie box to a gate under R3 (`tl2_w4260`, the west
  gate of `rcs_n4200`'s third pull-down: firm poly, uncertain tie). **Against**: nothing but the unseen 7-10 px.
  Without the join the gate has no feed at all, in a unit with no other spare device.
- **The diffusion link is firm** (was `?D 2936,3462:2972,3500`; `px.py row 3470 / 3488 / 3516 2924 2974 2 all`;
  mat.py over x 2898-3010, y 3436-3536). In the 24 px gap between thin metal E and R3, x 2934-2940: the chip-2
  stripped shot reads red over green by 34-45 at y 3470 and y 3488 against 8-10 on the field of the same gap at
  y 3516; the clean shot a dark bar (54-61) against an olive strip (91-110/103-118/52-67) (trap 2's pair); the
  metal shots are plain in both places and decide nothing. The diffusion's top edge is one line y 3460-3464
  from x 2938 across the poly to x ~2994, its bottom edge one line y 3500-3504 from under thin E to x 2974, and
  no line lies between the column under thin E and the gap at y 3464-3472. East of the poly the VSS box has a
  part x 2972-2994 that reaches up to the top line (under the rail's middle the box's top is y 3482; tan from
  y ~3476, the clean shot's green minus blue 33-61 against -9 to +14 on the pink field above the line). Channel
  y 3464-3500: 36-38 wide, as drawn (39/18). The box itself is drawn to its outline since review round 7: west edge
  x ~2979 below the channel, top y 3482.

**What the pair does (traced equations; the reading is a consequence, marked like them).** With S = `rcs_bc3460`
= NOR(`rcs_e3`, `rcs_e4`, `tl5_w4937`, `clk_tl`) and R = `rcs_x1` OR `rcs_a2`:

```
rcs_u3425 = NOT S AND NOT rcs_b1
rcs_b1    = NOT R AND NOT rcs_u3425 = NOT R AND (S OR rcs_b1)
```

`rcs_b1` is a latch: cleared while `rcs_x1` or `rcs_a2` is high, set while `rcs_bc3460` is high with both low
(that needs `clk_tl` low: CLK low), holding otherwise. The step request, with `rcs_c1` = NOT `rcs_a2` AND NOT
`rcs_b1` (unchanged):

**step = in1 OR ( NOT e4 AND ( NOT e3 OR ( NOT a2 AND NOT rcs_b1 ) ) )**

Without the join (the gate taken as low, as "Status" did) `rcs_b1` is combinational, NOT `rcs_x1` AND NOT
`rcs_a2` AND `rcs_bc3460`, and the bracket reduces to NOT (e3 AND a2): the old formula. The two differ while
`e3` is high, `e4` and `a2` low: the old formula steps; the new one steps only if the latch has been cleared
(by `rcs_x1` or `rcs_a2`) since it was last set. `rcs_cond_n` = NOR(in2, in3) follows the same bracket.

### Piece `aoi`: the stack under g1 and g2 (traced; one diffusion 69 wide, bands bent)

`aoi_s1.png` (3x, four shots). The metals here: R3 with edge lines at x 2950-2954 and x 3006; the thin metal of
`rcs_cond_lat` with edge lines at x 3026 and x 3062; the gap between them x 3008-3024.

- **West edge x 2968-2972**: one dark line in the clean shot and both metal shots at y 4122, 4144 and 4167
  (`px.py row 4122 / 4144 / 4167 2946 2980 2 acid1b,metal,metal1`), from the VSS box down to y 4194 (mat.py
  `acid1b r 2942 3078 4 4086 4194 6`). West of it the rail lies on field (pink, 195-203/117-134/122-129 at
  y 4144), except `tl2`'s poly (g1's west end) and g2's own end: salmon x 2960-2966 at y 4167, pink west of
  x 2958. The stack was drawn from x 2990 ("the bands' west ends bend"); `tl2` run 4 had the edge at
  x 2968-2971.
- **East edge x 3038-3044**: one dark line in all three shots at the same rows (`px.py row … 3030 3050 2`),
  under the middle of the thin metal, from y 4086 to y 4182; east of it the gate rows are poly over field
  (217-234 against 240-254 over the channel) and pink between and above. Drawn to x 3046 before.
- **The gap is diffusion from above g1 to node N** (R32(b); `px.py col 3012 / 3016 / 3020 4080 4272 4 all`).
  Both gate rows cross it as poly (chip-2 metal blue 46-72 between edge lines at y 4100 and y 4126-4128, y 4146-
  4148 and y 4180-4182). Between the rows (y 4132-4140): chip-2 metal 163-173/129-153/75-91, the chip-2 stripped
  shot bright (105-141) with red over green by 9-46, the clean shot a dark bar without green: **like node N in
  the same gap** (y 4188-4212: 175-182/138-144/85-91; stripped 140-154/107-114; clean 49-59) **and unlike the
  field island under g3** (y 4232-4252: metal dim 75-100/68-89/31-38, stripped green over red, clean green
  100-131/153-166/85-96). No vertical line between the two metals' edge lines at y 4092, 4134 or 4194.
- **The bands are bent** (edge line to edge line, `px.py col 2982 / 3000 / 3030 / 3054 4096 4184 2 acid1b`):
  g1 lies at y 4113-4135 under R3 west of x ~2995 and at y 4101-4123 from there east; g2 at y 4157-4178 under R3
  and at y 4145-4167 from the gap east (in the gap the chip-2 metal shot shows poly y 4147-4181). Both were
  drawn straight (y 4103-4128, y 4150-4175). g2's west end is at x ~2960; it was drawn from x 2985, which only
  worked because the stack was drawn from x 2990.
- **R23**: nothing of the stack beyond the two edges (field west of x 2968 and east of x 3044 at every row).
- Node N's rectangle now starts at y 4182 (was 4176: g2's west part reaches y 4178). Its own outline was not
  re-read (Not done).

### Ambiguities of run 5

1. **The join of `rcs_iso2958`'s poly to `rcs_b1`'s plate arm** (`?P 2928,3531:2944,3547`): believed, not seen;
   the evidence is above. This is AMB-022, with a reading adopted. What would settle it: nothing more in these
   photos that the tracer can think of (the stretch is a buried-contact box's outline in a 24 px gap between
   two metals); a delayered or sharper shot of (2935,3540), or the behaviour of the row counter's step.
2. **The stack's part east of R3 reaches VSS only through the gap stretch above g1** (x 3008-3024, y 4088-4098,
   10-12 px between the east column's top edge line at y ~4086 and g1's top edge): read as diffusion (both metal
   shots plain and bright, 162-178/142-144/84-92, with no vertical line; the clean shot red-brown at x 3020, not
   olive). If it were field, g1 would be 37 wide and not 69, g2 unchanged; same nets, same equation.
3. In the full extraction g1's channel is 84/20 and not 80/20, because `tl2`'s piece of the same band (`P
   2938,4107:2990,4130` in `trace/tl2.txt`) is drawn 5 px north of where the band lies west of x 2990. Not
   edited (another package's file); geometry only.

### Not done after run 5

- **R23, R42 and R32(b) are done for this file** (runs 3-5). R32(d) is done for `rcs_b1`'s load (this run) and
  open for the other loads.
- Next, in the order of the re-read list: **the loads west of R3 and east of R1 of the first cluster's units**
  (R30; R32(c)-(e): the ties at y 3134, 3307, 4615, 4790, 5216 drawn by analogy, each load's gate poly beyond
  its tie box; R41: thin metal E over the tie boxes), the step gate's load and its uncertain tie at (2885-2908,
  4958-4996) with the 6-9 px between the step request's buried-contact box and `rcs_in3`'s row (run 4), R32(a),
  R29, R38's other ends, R39.
- Seen in passing, not drawn: the arm of `rcs_b1`'s plate is drawn y 3531-3553 and lies at y ~3531-3547; node
  N's outline (its east part's top edge is a line at y ~4186, drawn 4182; whether it reaches x 2950 in the west
  above y 4226 was not read: the clean shot is pink at x 2954-2958, y 4176-4194).
- The rest of this file's Not done list is unchanged (the west column y 3590-4940; thin metal W; the boxes
  without a poly; bus pieces; `ports.d/tla.txt` for the file's older wires). **`rcs_iso2958`'s two entries in
  the old "Not done" list above are answered by this run** (the cap is an overhang; the feed is the foot).

## Run 6 (2026-11-28): the "standard" loads between R2 and R3, and thin metal E over their boxes

Tom Seddon's session, on Claude Fable 5.2, from 2026-11-28 16:46 +0000. Two pieces, the next of the re-read list
after run 5: piece `lt`, the six loads west of R3 that this file drew as "the standard one" (R32(c): four of their
ties were drawn by analogy with `rcs_c1`'s; R32(d): each load's gate poly beyond its tie box; R30: each load's far
side), and piece `te`, thin metal E where it passes over the boxes (R41). Scratch: `cache/scratch/tla/survey.md`
("run 6"), `draft-lt.txt`, `draft-te.txt`; `cache/scratch/tla/ld.py YT` prints the profiles of one tie (YT = the
tab's top as drawn: 3158, 3331, 4631, 4806, 5240) and `mat.py` the matrices, both the same numbers as
`tools/px.py`. Images `ld_s1_c1.png` (5x, four shots), `ld_s2_bc.png`, `ld_s3_bc_n.png` (4x), `ld_s4_bc_tie.png`
(8x), `ld_s5_bc_tie3.png` (5.9x), `ld_m1_metal.png`, `ld_m2_acid.png` (the four other standard loads side by side,
2.6x), overlay `ld_o1_bc.png` (5x).

**Result.** No connection changed (`tools/sameconn.py b2b4a85b`: connections identical, package alone and every
trace file). One load redrawn: `rcs_bc3460`'s (27/50, was 27/55). Ten stretches of thin metal E are `?M`. Full
extraction 2,546 nets, 4,931 transistors, 0 errors, 0 warnings; `tools/unsure.py --equations`: 1,002 of 1,464 firm,
as before; 1,245 uncertain items (ten more, the `?M`); `tools/unsure.py` lists `rcs_thin_e` as joined only
through uncertain items (Ambiguity 2).

### Piece `lt`: five standard ties, read at their own place (as drawn)

The loads of `rcs_c1` (tab top y 3158), `rcs_u3288` (3331), `rcs_cond` (4631), `rcs_cond_n` (4806) and `rcs_in3`
(5240) are one build, and each reads the same way (`ld.py YT`; `mat.py LAYER CH 2884 2950 3 YT-22 YT+38 3`; the
two mosaics):

- **The tail** under thin metal E, x 2913-2927 between edge lines at x 2910 and x 2931-2937: in the clean shot tan
  (190-205/156-175) from the node box down with no dark line across (`col x 2918`: only dips to 135-160 where the
  tab's top edge crosses, at YT-6 and YT+3; an edge there reads 40-90), a bright centre at YT+8 to YT+18
  (199-213/150-179), a heavy line at YT+20 to YT+26 (43-86), and below it pink field (188-195/125-128/126), green
  in the chip-2 stripped shot (red minus green -20 to -50).
- **The tab** runs east from the plate's lower corner at about YT+5 to YT+20. Both metal shots show poly colour to
  x ~2899 (chip-2 blue 48-58, like the plate's 43-66); then come E's own edge line and the box's west outline
  (dark x 2901-2913). The chip-2 stripped shot stays red over green from the plate into the box (`rcs_c1`: 29, 17,
  12, 8, 18, 22 at x 2895-2910; `rcs_u3288` 15-20; `rcs_cond` 3-10; `rcs_cond_n` 8-26; `rcs_in3` 15-25) where 12 px
  above the tab the same stretch is green field (-6 to -30, -8 to -30, -5 to -19, -1 to -17; not at `rcs_cond_n`'s,
  where it reads 0-11 there too: Ambiguity 3). In the clean shot the stretch x 2898-2907 at the tab is salmon or
  tan (162-193/106-147/69-110), not pink.
- **East of the box** (R32(d)): its outline x 2931-2937, then the open gap to R3, x 2940-2948, is field at every
  one of the five (clean shot olive 82-101/67-103, chip-2 stripped red minus green -3 to +10, both metal shots
  plain with blue 72-84). No foot like `rcs_b1`'s: the plate's poly ends in the box. Below the box: the heavy
  line, then field.
- **The far side** (R30; `ld.py YT d`, the gap's column x 2941): only the node strip crosses the gap (y 3108-3124,
  3281-3297, 4585-4597, 4760-4772, 5190-5206: red minus green 20-52 between two lines), field above and below it.
  No load of the five reaches a VSS box.
- **The plates** are closed on the west, north and south (mosaics; `rcs_c1`'s down x 2870: edge lines at y 3086-3089,
  3107-3110, 3134-3137, 3179-3185, so plate y 3088-3182 and a channel 28 wide, as drawn).

What is not seen, at any of the five: poly through the 6 px of the box's west outline, which lies under E's edge
line. That is the standing of every buried contact (run 2, Ambiguity 1); the ties stay drawn firm.

### Piece `lt`: `rcs_bc3460`'s load is not the standard one (traced; same nets)

This file drew it as the others, "the standard one": plate y 3867-3960, a tail down from the node box, a tab at
the plate's lower corner and a tie box at (2908-2932, 3932-3959). `tl2` (run 3) had met "an oval at (2909,3868)
that this run read as the load's tie box and the reviewer as an island of field" and left it `?D`.

- **Nothing is below the node box** (`tools/px.py col 2918 3896 3976 4 all`): the box's bottom line at y 3908-3912,
  then from y 3916 to y 3976 the clean shot is pink (181-200/108-129/112-131: field under metal), the chip-2
  stripped shot green from y 3932 (red minus green down to -53), and E is bright throughout in both metal shots.
  No tail, no box, no tab.
- **The plate ends at y 3928** (`px.py col 2870 3826 3990 4 all`): top bar y 3866-3876, the strip's edge lines at
  y 3878-3882 and y 3906-3910 (channel 28 wide, as drawn), bottom bar y 3914-3922, the plate's edge y 3926-3930,
  then open field to y 3990 (chip-2 metal 160/137/87, chip-2 stripped 151/148/96, clean shot khaki 155/140/100).
  North of the unit, x 2840-2895, y 3700-3830: field, no poly (`ld_s3_bc_n.png`).
- **The tie is a box on the plate's top edge**: a heavy rounded outline x 2868-2900, y 3835-3860 over the east part
  of the plate, with one dark band of 10-12 px (y 3855-3866) between its centre and the plate's top bar. Its
  centre (x 2878-2892, y 3845-3852) reads as the centres of the middle cluster's tie boxes do, in all four shots,
  and not as poly (`px.py pt 2884,3848 3927,3360 3926,4133 2870,3871 2880,3872 2868,3166 all --r 2`):

  | | chip-2 metal | chip-1 metal | chip-2 stripped | clean |
  |---|---|---|---|---|
  | this box's centre (2884,3848) | 153/118/78 | 120/110/56 | 163/139/91 | 89/71/59 |
  | run 2's tie boxes (3927,3360), (3926,4133) | 155/134/71, 169/134/83 | 130/130/73, 135/122/58 | 159/144/83, 166/148/102 | 100/79/61, 89/79/59 |
  | plate poly (2870,3871), (2880,3872), (2868,3166) | 156/115/58, 141/97/44, 158/107/60 | 145/81/42, 139/76/39, 138/77/45 | 137/114/58, 146/100/47, 169/126/72 | 114/73/49, 139/95/48, 187/96/63 |

- **The box is open to the east: a tongue of the node strip.** Along y 3845-3848 the clean shot has no dark line
  from the centre to the node strip under E's east half (`mat.py acid1b r 2869 2938 3 3827 3893 3`: 74-105 on the
  centre, 135-142 at x 2890-2896, 182-187 at x 2899, a dip to 145-163 at x 2902-2905, 188-208 from x 2908 to
  x 2926). The tongue is y 3841-3855 (its edges at x 2899-2914: dark at y 3836-3839 and y 3857-3860); the chip-2
  stripped shot is red over green along it (12-42). The strip it leaves is the one `tl2` draws down from the unit
  above (`D 2915,3757:2935,3890` there). In the metal shots only E's own edge line (x 2896-2905) lies between
  box and strip.
- **Thin E passes over the tongue**: bright in both metal shots at y 3842-3854, x 2908-2920, the width it has
  everywhere (`tools/textmap.py 2884 3824 2938 3892 3 --acid`), tan under it in the clean shot, no hole.
- **The oval is an island of field**, as `tl2`'s reviewer read it: x 2899-2916, y 3858-3878, between the tongue
  (north), the strip (east), the node box (south) and the plate's top bar (west), with a line on each side. Its
  interior (x 2905-2911, y 3863-3873) is green in the chip-2 stripped shot (98-147/106-162), like the field under
  E below the node box, and bright under E in both metal shots. Not a tie, not a contact.

Drawn: the plate to y 3928, the plate's poly up into the box, the box, the tongue and, so that the file extracts
by itself, the strip from the tongue down to the node box (the same strip as `tl2`'s). Removed: the tail, the tab
and the box below. `rcs_bc3460` = NOR(`rcs_e3`, `rcs_e4`, `tl5_w4937`, `clk_tl`) as before (firm), load 27/50.

"Reading aids" above says every load plate of a column has its tab at the lower corner: five of the six between
R2 and R3 do.

### Piece `te`: thin metal E over the boxes (R41)

`tools/tl3_thin.py 2903 2925 2996 5400 --thr 176 --min 8` lists 43 stretches where neither metal shot shows
metal anywhere across E's width. Bars of 8-10 px lie over single edges. Stretches of 14 px or more, or pairs of
bars round a half-bright centre, lie at ten places, now drawn `?M` (the metal between them is firm):

| `?M` | dark in both metal shots | what lies under E |
|---|---|---|
| y 3146-3193 | y 3148-3191 (44 px; half-bright centre y 3163-3178) | `rcs_c1`'s tie box |
| y 3321-3366 | y 3323-3338, y 3349-3364 | `rcs_u3288`'s tie box |
| y 3473-3565 | y 3475-3483, y 3499-3512, y 3522-3563 (42 px) | `rcs_u3425`'s pad tie and `rcs_b1`'s tie box |
| y 4165-4208 | y 4167-4178, y 4189-4206 | `rcs_n4200`'s tie box |
| y 4291-4313 | y 4293-4311 (chip 1 to y 4333) | the tie box of `rcs_bd3330`'s load (`tl2`) |
| y 4623-4669 | y 4625-4640, y 4653-4667 | `rcs_cond`'s tie box |
| y 4797-4842 | y 4799-4811, y 4827-4840 (full-bright between) | `rcs_cond_n`'s tie box |
| y 4914-4956 | y 4916-4931, y 4935-4954 | the step gate's top band and the west end of gate `in1`'s row |
| y 4989-5035 | y 4991-5004, y 5016-5033 | the west end of gate `in2`'s row and the bottom band |
| y 5231-5275 | y 5233-5245, y 5259-5273 (chip 1: y 5233-5273) | `rcs_in3`'s tie box |

At none of them is there a pad, a widening of the metal or a green hole in the clean shot (the box centres are
tan: 199-213/150-179), and a contact on any tie box would short that gate's output to the select line. The reading
stays "one metal that passes over"; the photos do not show it there. Over `rcs_bc3460`'s tongue and island E is
not dark (8 px at y 3835-3842 only). The label `rcs_thin_e` moved from y 5000 (now inside a `?M`) to y 5100, and
the north piece carries the name too (`N M 2800,2986`), so that `tools/unsure.py` lists the join and the
selector's equation keeps its form without the uncertain items.

### Ambiguities of run 6

1. **`rcs_bc3460`'s tie**: the plate's poly through the 10-12 px band between the plate's top bar and the box's
   centre is not seen (as at every tie box: run 2, Ambiguity 1), nor is the tongue under E's own edge line
   (x 2896-2905) in the metal shots; the clean shot shows the tongue there. Drawn firm. If the box were not the
   plate's, the load would have no tie at all (the plate has no other exit: field north, west and south, the
   strip's VCC box and node box at its ends).
2. **Thin metal E at ten places** (`?M`; AMB-032 and AMB-033 are the same question on `tl3`'s two thin metals):
   that it is one metal without a contact from its north end (the selector's gates, by the metal x 2696, the poly
   y 2768 and the metal x 2326) to `tl2`'s piece south of y 5400 is believed, not seen. `tools/unsure.py` lists
   `rcs_thin_e` as three pieces joined only through uncertain items (the north piece; the piece y 5033-5231; and the
   south end with `tl2`'s, `tl3`'s and `busl`'s stretches of the wire). What rests on it: that the selector
   `tla_w3417`'s select and the gate of `tla_w3505` are the wire `busl` followed to the far side of the die
   (`notes/operation.md`). What would settle it: nothing more in these photos; a contact would show a pad.
3. At `rcs_cond_n`'s tie the stretch between plate and tail 12 px above the tab is not green in the chip-2
   stripped shot (red minus green 0-11 at x 2899-2911, y 4794) as it is at the four others: the tab may be taller
   there (its top nearer y 4795 than y 4806). Geometry only; not redrawn.
4. `tl2`'s `?D 2903,3845:2917,3890` (in `trace/tl2.txt`) covers the island of field and the tongue's east end. It
   joins nothing that is not joined anyway. Not edited (another package's file); in the handoff.

### Not done after run 6

- **R32(c) is done for this file** (the five ties drawn by analogy, and `rcs_bc3460`'s), **R41 for thin metal E**,
  and R30 and R32(d) for these six loads.
- Next, in the order of the re-read list: the loads that are not of the standard build, each with its tie:
  the step gate's load and its uncertain tie at (2885-2908, 4958-4996), with the 6-9 px between the step request's
  buried-contact box and `rcs_in3`'s row (run 4); `rcs_n4200`'s load and its pad's arm (B 2896,4158:2940,4200);
  `rcs_u3425`'s pad tie (B 2893,3474:2928,3501); then the loads east of R1 (R30, R32(c)-(e) for the west column:
  `rcs_in2`'s, `rcs_w2`'s, the selector's, `tla_w3505`'s uncertain tie, the top unit's) with thin metal W over
  them (R41: W is drawn in two pieces, y 3027-4002? and y 4940-5330, not shown to be one metal); R32(a), R29,
  R38's other ends, R39.
- Seen in passing, not drawn: thin metal E is drawn 20 wide and is about 14 (bright x 2908-2920 in both metal
  shots; `tl2` draws its south part 14 wide); the standard tabs are drawn y YT to YT+22 and lie at about YT+5 to
  YT+20.
- The rest of this file's Not done list is unchanged.

