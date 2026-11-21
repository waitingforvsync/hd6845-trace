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

```
rc_stepreq_n = NOR(in1, in2, in3)        the row counter's step request (active low)   (2975,5035)
in2        = NOR(w2, e4)                 west column                                   (2571,5197)
in3        = NOR(e3, e4)                 east column                                   (3046,5197)
w2         = NOT c1                      pull-down under rail R1 itself                (2625,5066)
c1         = NOR(a2, b1)                 east column, top of the cluster               (3046,3115)
b1         = NOR(x1, a2, rcs_u3425)      east column; third pull-down west of the rail (3046,3590), (2920,3628)
rcs_u3425  = NOR(rcs_bc3460, rcs_iso2958) inverter; its output goes by a strap to b1's third gate. rcs_iso2958 is a
                                         gate poly with no connection found (2958,3481): see "The west column" below
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

- `rcs_e4`'s wire ("the gate of a pull-down under the rail x 7290-7345 of bc1's untraced left column ... the poly ends at x 7370 ... its driver is NOT found"; also the comment in `trace/tla.txt`, not edited): the poly ends at about x 7390 over a field island; the pull-down is gate 1 of the NOR `eof_w15523` = NOR(`rcs_e4`, `eof_w16040`, `bl0_w15566`) (`eof`, piece `u15500`); the driver has been found since (`rcs_e4` = NOR(`tl1_w4678`, `tl3_e3550`), `tl1`).
