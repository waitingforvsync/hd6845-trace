# tc1: top-centre logic, upper half (x 6400-8250, y 2500-4450)

Trace: `trace/tc1.txt`. Coordinates are metal-shot pixels. Local names start `tc1_`.

## Status

Runs 1 and 2 (2026-11-15). Traced, overlay-checked and extracting (26 transistors, no
errors, no open nets): the **island** (x 7330-7900, y 3050-4050: nine static gates), all
of its wiring, the **bus field below it** (y 4130-4450), the **six north-south metals**
east of it (x 8089-8321, each end to end) and the two top bus lines that feed them from
the west. **Every input of the island is now followed to the edge of the region; none is
driven inside this block**: `a` and `w1` come from the east (datapath side), `b`, `g`
and `i` from the south (tc2). See "Where the island's inputs come from".
Not traced: the gate columns at x 6400-7000 (about 40 loads) except the driver below, the
channel x 7000-7170 except the lines that concern the island and the driver, and most of
the top bus field.

Run 3 (2026-11-17, a collaborator's session; claim `tc1`, region x 6750-8250). Traced,
overlay-checked and extracting (36 transistors in all, no errors, no warnings): **the
driver gated by `tc1_g`** at x 6700-7160, y 3920-4225, with its load, its supply contacts
and its wiring into the channel: `tc1_o4020` = NOR(`tc1_g`, `tc1_x1`), and **the output's
route** up the channel and into the top bus field, where it becomes the bus line y 2641
and leaves east over the datapath. See "The driver gated by `tc1_g`".

Run 4 (same day, same claim). Traced and extracting (37 transistors in all): **the inverter
whose output is the strip on `tc1_x1`'s pad**: its load, supply contact and gate tie, added
to the pull-down that run 3's review found: the strip's node = NOT `tc1_p4308`. See "The
inverter of `tc1_p4308`". Run 3's work was not merged (its third review round had findings);
it goes in with this run's review. Runs 3 and 4 were merged at `3c0efe1`.

Run 6 (same day, same claim). **The second driver**, north of the first: `tc1_o3740` =
NOR(`tc1_p3698`, `tc1_x1_u`), five transistors. See "The second driver". Also a correction
of method: bright green in the open is diffusion here (top of these notes).

Run 7 (same day, same claim). **Cell B, the NOR north of the second driver**: `tc1_o3527` =
NOR(`tc1_o3353`, `tc1_o3095`), three transistors, with its output's route to the channel
metal x 7003-7023 that leaves south at y 4450, and **the source of `tc1_p3698`** (the thin
metal x 6765-6785 from the north). See "Cell B". 45 transistors in all, no errors, no
warnings.

Run 8 (same day, same claim). **Cell A, the NOR north of cell B**: `tc1_o3353` =
NOR(`tc1_m7100`, `tc1_l4_out`), three transistors, and **its upper input's route** from the
contact (7100,3180) on the upper piece of the channel metal x 7091-7110. See "Cell A". So
the island's `tc1_l4_out` goes through two NORs in a row: `tc1_o3527` =
NOR(NOR(`tc1_m7100`, `tc1_l4_out`), `tc1_o3095`). 48 transistors in all, no errors, no
warnings.

Run 9 (same day, same claim). **Cell C, the three-input NOR north of cell A**:
`tc1_o3095` = NOR(`tc1_p3051`, `tc1_x1`, `tc1_m7100`), four transistors. Its output is the
channel metal x 7003-7023 that ends on cell B's gate (until now named as that metal, renamed
`tc1_o3095`). `tc1_x1`'s channel metal and `tc1_o3740`'s thin metal are followed to their
north ends as far as they can be read. **Gate row 1's source is open** (`tc1_p3051`): its
poly ends in a box 10 px from a contact of `tc1_o3740`'s metal, and what is joined there is
not readable (Ambiguity 20). See "Cell C".
52 transistors in all, no errors, no warnings.

Run 5 (same day, same claim; wiring only, no new transistor). **Where the inverter's input
comes from and where the thin metal x 6968 goes in the south**: two poly rows running west
below the inverter, drawn to this package's west edge. See "The two rows below the
inverter".

## How this area reads in the photos (cost me a third of the run; read this first)

- A **diffusion wire in the open is a strip about 22 px wide between two dark edge
  lines**. Its interior is only slightly redder than the field (acid1b raw RGB about
  165/120/100 against field 150/158/96; in `acid` R>G inside, G>R outside). It is not
  green. Only *large* open diffusions (the drains of the big drivers) are green. At
  2x the two edge lines look like "thin dark wires"; they are the two sides of one
  strip. `tools/tc1_px.py col X Y0 Y1 2 acid1b,acid,metal` across a strip settles it.
- A weak load is a poly block about 60 x 65-90 px with the strip passing under it (two
  dark lines across the block, 22-28 px apart). The gate tie is a tab of diffusion
  ("bump") hanging from the strip beside the block, ending under a buried-contact box
  that the block's stem enters.
- In the stripped shots a dark line runs parallel to every rail edge 10-25 px outside
  it (the etch boundary of the metal's protection). It crosses poly bands and
  diffusion alike and is not layout. The metal shot does not have it: a line seen
  there is real.
- Under the rails, tan (raw 190/172/128) is diffusion, salmon (235/160/115) poly,
  and the field is 150/133/105 (shown pink by the viewer).
- Pull-downs sit *under the VSS rails*: a poly band crossing the rail's diffusion
  column. Outputs leave the column sideways into a buried-contact box.
- **Bright green in the open is a large diffusion, not field** (run 6, 2026-11-17). I read
  green areas beside the drivers as "open field" through runs 3-5, misled by
  `tools/classmap.py`, which paints them pale green, its colour for field in the open.
  Calibrated on known spots (7x7 means, R/G/B):

  | | clean shot | chip-2 stripped | chip-2 metal |
  |---|---|---|---|
  | large open diffusion (L2's and L3's drains, (7532,3420), (7532,3680)) | 118/155/90 | 160/147/89 | 166/130/82 |
  | open field, empty ((7110,4250), (7130,4300)) | 151/138/100 | 155/154/99 | 168/138/88 |
  | field between two poly rows (6922,4416) | 90/104/61 | 143/139/87 | 167/152/85 |

  The chip-2 stripped shot separates them: red minus green is 0-4 on field, 13-17 on
  diffusion. `tools/tc1_green.py X0 Y0 X1 Y1` (new) marks the pixels that are green in
  the clean shot and have red minus green of 8 or more in the chip-2 stripped shot, and
  lists every group with the share of it the trace draws as diffusion. **Re-check of the
  merged work with it** (x 6690-7060, y 3920-4460 and x 7110-7500, y 2600-2870): no large
  undrawn open diffusion; the four groups it lists are rims 8-11 px wide beside poly ends
  ((6765,3955), (6950,4424), (7120,2854)) or lie under the supply rail ((6722,3965)),
  where the rule does not apply. The gap at (7443-7446, 2640) that the notes below call
  "open field" is field by the chip-2 shots too (83/81/45, 123/118/66: red equal to
  green), though green in the clean shot.

## Inventory

Rails and channels (from two 0.7x views of the whole region):

| What | Where |
|---|---|
| Top bus field: seven horizontal metal lines at y 2554, 2598, 2641, 2684, 2727, 2771, 2814 (each 14 px wide), crossing the island's right VSS rail in poly | y 2500-2950, whole width; two lines traced |
| Gate columns, continuing the top-left logic | x 6400-7000, y 2650-4450; vertical rails at x 6507-6557, 6682-6757, 6857-6932 (widths near y 4000); not traced, rails not identified. Large devices under the rails, not island-style gates |
| Routing channel: verticals at x 7002-7022, 7048-7068, 7091-7110, 7133-7152 (west part, see Not done) and W1-W4 at x 7174-7325 (traced). South of y 4050 the west part is empty field except the polys of `g` | x 7000-7330, y 2950-4450 |
| **Island**: three vertical rails and nine gates | x 7330-7900, y 3050-4050 |
| Island left rail, VSS | x 7420-7470, y 2975-4335, where it becomes the VSS bus y 4288-4335 going east to x 7995 and then south (x 7943-7990) |
| Island centre rail, VCC | x 7597-7647, top end y 3105, down to the VCC bus y 4198-4250, which runs east to x 8166 and then south (x 8116-8165) |
| Island right rail, VSS | x 7770-7820, from above y 2500 (0.7x view) to its end at y 4000 |
| VSS strap joining the two outer rails | x 7420-7820, y 2975-3040 |
| Wiring between island and datapath: verticals V1 x 7914-7931, V2 x 7957-7977, V3 x 8002-8022, then x 8043-8063 | x 7900-8080 |
| Six north-south metal lines ns1..ns6, 44 px pitch (centres x 8096, 8140, 8184, 8227, 8270, 8314), traced end to end (table under Logic) | x 8089-8321, y 2720-4450 |
| Bus field below the island: tracks T1-T3, the `g` line, VCC and VSS buses, lines to tc2 and to the datapath; traced | y 4010-4450 |

VSS/VCC are assigned from the loads (all hang from the centre rail) and the pull-down
sources (all contact the outer rails); the rails have not been followed to the pads.
Both supplies leave this block southwards (ports).

**The datapath's regular slices start at x 8340** (cdp1's slice 0 rail is at x 8403),
not at 7600-7650. x 8090-8330 is a bundle of six north-south metal lines.

Island, right half (traced):

| Gate | Where | Kind |
|---|---|---|
| R1 | load 7655-7715 x 3138-3203; pull-down under right rail y 3193-3213 | inverter |
| R2 | load 7655-7715 x 3307-3397; pull-downs in the column 7826-7881 x 3256-3410 | 2-input NOR |
| R3 | load 7685-7730 x 3470-3544 (strong); pull-downs under/right of the rail y 3452-3556 | 2-input NOR |
| R4 | load 7653-7713 x 3615-3682; pull-down under the rail y 3667-3689 | inverter |
| R5 | load 7656-7698 x 3832-3884 (strong); ladder 7740-7873 x 3740-3972 | AND-OR-invert, 2+2 |

Island, left half (traced):

| Gate | Where | Kind |
|---|---|---|
| L1 | load 7532-7591 x 3160-3214; pull-down under the left rail y 3215-3235 | inverter (mirror image of R1) |
| L2 | drain = column y 3407-3471 plus the green region 7518-7547 x 3332-3513; gates = poly bands y 3388-3407 and y 3471-3492, each wrapping the drain as an L; strong load 7552-7588 x 3370-3460 | 2-input NOR, wide transistors |
| L3 | the same 258 px lower (bands y 3642-3663 and y 3729-3750, load 7552-7588 x 3630-3720) | 2-input NOR, wide transistors |
| L4 | pull-downs in the column 7368-7410 x 3828-3972 west of the rail; load 7541-7588 x 3874-3950 | 2-input NOR (mirror image of R2) |

The left rail's diffusion is a column x 7366-7482 (wider than the rail: x 7366-7410 is
in the open and green) from y 3290 to 3832, widened on the right to x 7547, with VSS
contacts at y 3258, 3335, 3527, 3597, 3803 and a pad at 7405-7468 x 3951-3998.

Channel west of the island, the four lines that serve it (all metal, about 20 wide):

| Line | x | y range | Net |
|---|---|---|---|
| W1 | 7174-7194 | 2976-3952 (ends on its lower contact; bare field below, measured) | `tc1_w1` |
| W2 upper | 7223-7240 | 2987-3128 (then east along y 2978-2995 to x 7350) | `ras_shift` |
| W2 lower | 7220-7240 | 3170 to beyond 4450 | `ras_straight` |
| W3 upper | 7265-7284 | 3032-3386 (from the east along y 3022-3042) | `tc1_a` |
| W3 lower | 7265-7284 | 3427-4070, then east along y 4060-4081 to contact (7336,4070) | `ras_o0_sel2` |
| W4 upper | 7307-7325 | 3062-3648 | `tc1_r1_out` |
| W4 lower | 7307-7325 | 3690-4026, then east along y 4014-4037 to a contact at (7379,4026) | `ras_o0_sel1` |

**Three of these verticals are cut where a gate is inserted in them**: W2 between
y 3130 and 3168, W3 between 3404 and 3422, W4 between 3664 and 3680. At 1x each looks
like one continuous line with two contacts. Each break was measured (`tc1_px.py col`:
bare field in the metal shot, unprotected colours in `acid1b`).

A wide metal strap, y 2975-3040, joins the two VSS rails (x 7420-7820; drawn). The
poly lines of `ras_shift` (y 2977-2994) and `tc1_a` (y 3020-3038) run west under it; their
edges print through the metal as dark lines and make the strap look like three metal
lines. The metal that brings each of them is separate from the strap: a 20 px gap at
x 7822-7842 (`ras_shift`, measured) and at x 7397-7420 (`tc1_a`, seen at 2x).

## Logic (traced; extraction: 26 transistors, 25 nets, no errors)

```
tc1_r1_out = NOT tc1_a
ras_straight = NOT ras_shift
ras_o0_sel2 = NOR(tc1_a, ras_straight)        = NOT a . b        (driver)
ras_o0_sel1 = NOR(tc1_r1_out, ras_straight)   = a . b            (driver)
tc1_l4_out = NOR(ras_o0_sel2, tc1_w1)
tc1_r2_out = NOR(tc1_a, ras_shift)
tc1_r5_out = NOT(tc1_g.ras_o0_sel2 + tc1_i.ras_o0_sel1)
tc1_r4_out = NOT tc1_r5_out                = b . (g.NOT a + i.a)
tc1_f      = NOR(tc1_r2_out, tc1_r4_out)   = (a + b) . NOT(b.(g.NOT a + i.a))   (driver)
           = a.NOT b  +  b.NOT a.NOT g  +  a.b.NOT i
```

In words: `f` is high when (a,b) = (1,0); when (a,b) = (0,1) unless `g`; when (a,b) =
(1,1) unless `i`; never when a = b = 0.

**No latch, no flip-flop, no clocked device and no pass transistor in the island or in
anything else traced in this block**: nine static gates and wiring. No named line
(`res_b`, `lpstb_b`, a clock) reaches anything traced here; `notes/blocks/trunks.md`
puts `res_b` and `lpstb_b` at x 5265-5330, west of this region.

### Where the island's inputs come from (all traced to the region edge)

| Input | Used by | Route back from the island | Leaves the region at |
|---|---|---|---|
| `tc1_a` | R1, R2, L2 | metal V3, poly east | east: poly y 3387-3402 at x 8250, in the datapath channel between cdp1's rows A and B (cdp1's notes: that line runs the full width, contact at 10615,3385) |
| `ras_shift` | L1, R2 | metal V2/V3-lower, corner (8100,3725), metal south x 8088-8105, contact (8139,4090), poly east y 4079-4101, contact (8313,4090), metal south x 8307-8321 and west along y 4411-4426, contact (8247,4417), poly west y 4408-4427, contact (7859,4417), metal west y 4411-4426, contact (7511,4417), poly south | south: poly x 7503-7522 at y 4450 |
| `tc1_g` | R5 | metal x 8045-8063 south, west along y 4151-4167, contact (7685,4158), poly west y 4144-4167; contact (7317,4158) on the way, metal south to contact (7315,4395), poly west y 4385-4403, south at x 7134-7153 | south: poly x 7134-7153 at y 4450. The other end of the y 4144-4167 poly (north at x 7177-7202, west along y 3995-4014, under the channel metals without contact) is the **gate** of transistors in a big structure at x 6750-6940, y 3930-4200 (Not done), so `g` is not driven there |
| `tc1_i` | R5 | track T3, metal south x 7265-7284, contact (7270,4437), poly west y 4424-4443, south at x 7179-7196 | south: poly x 7179-7196 at y 4450 |
| `tc1_w1` | L4 | metal W1 up to contact (7186,2986), poly east and north (x 7290-7308) to contact (7362,2770), bus line y 2764-2778 east, cross-under at the right VSS rail (contacts 7663,2769 and 7858,2769), on east and south as **ns1** (x 8089-8104), jog east at y 3651-3667, contact (8139,3704), poly east | east: poly y 3691-3712 at x 8250 (seen to x 8350), into the random logic at the datapath's slice-0 position |

So `w1` and ns1 are one net (`@alias tc1_w1 tc1_ns1`): the line has exactly two ends, L4's
gate and the poly at (8350,3700). The bus line carries no other contact (its metal run
is unbroken in `sel_tracks.py h 2771` between the contacts named).

### Outputs and internal nets

- `tc1_r1_out` (NOT a): buried contact, poly, contact (7924,3159), metal V1 up to
  y 3071 and west to contact (7862,3072), poly west along y 3065-3079 across the top of
  the island (under both VSS rails, over field) to contact (7317,3072), metal W4 upper
  down to contact (7316,3638) = L3's band c. Goes nowhere else.
- `ras_straight` (NOT b): buried contact 7354-7396 x 3164-3199, poly west to contact
  (7228,3181), metal W2 lower: contacts (7230,3482) = L2's band b and (7230,3740) =
  L3's band d, and south past y 4450. No contact on it between y 3760 and 4450: the
  polys of `g` (y 4144-4167, 4385-4403), `x1` (4344-4362) and `i` (4424-4443) cross
  under it (the last checked by profile along x 7230).
- `ras_o0_sel2`: buried contact 7358-7396 x 3420-3452, poly west to contact (7279,3437),
  metal W3 lower: contact (7273,3852) = L4's band e, then to track T2. Tap at
  (7510,4069): metal south to contact (7511,4242), poly south under the VSS bus, west
  along y 4320-4337, south at x 7422-7438 past y 4450.
- `ras_o0_sel1`: buried contact 7356-7396 x 3684-3717, poly west to contact (7316,3700),
  metal W4 lower to track T1. Tap at (7554,4028): metal south to contact (7556,4206),
  poly south under both buses, west along y 4363-4382, south at x 7465-7481 past
  y 4450. From the pad under contact (7922,4027) a second poly goes south, east along
  y 4080-4097, diagonally (x - y = 3903) under the corner of `g`'s metal and under the
  VCC bus, and east along y 4212-4228 into the datapath (seen at 3.5x from the pad to
  the diagonal; the diagonal measured by profile at y 4170 and 4195).
- `tc1_l4_out`: buried contact 7364-7400 x 3878-3910, poly west along y 3885-3905 under
  W4, W3, W2, W1 (no contacts) to contact (7099,3897); metal north x 7091-7110 to
  contact (7100,3395); poly west along y 3388-3403 into the gate columns (seen to
  x 6930; **not drawn west of x 7150**).
- `tc1_r2_out`, `tc1_r4_out`, `tc1_r5_out`: as traced in run 1, each goes to one gate
  only (R3, R3, R4).
- `tc1_f`: R3's output; buried contact, poly band f, contact (7966,3506), metal east
  along y 3501-3519 and up x 8045-8064 to contact (8054,3354), poly east along
  y 3348-3362 into the datapath under ns1..ns6 without contact.
- R5's inputs h and j are `ras_o0_sel2` and `ras_o0_sel1` by tracks T2 and T1 (each:
  contact, poly east under the left and centre rails, contact, metal east).

### The six north-south metals (traced end to end; none has a transistor in this block)

| Line | x | North end | South end | Contacts |
|---|---|---|---|---|
| ns1 = `tc1_w1` | 8089-8104 | from the west on bus line y 2764-2778 | jogs east at y 3651-3667 to x 8132-8148, ends on contact (8139,3704): poly east y 3691-3712 | see `w1` above |
| ns2 | 8132-8148 | from the west on bus line y 2720-2734: cross-under at the VSS rail (contacts 7707,2725 and 7901,2724), metal west to contact (7403,2727), poly west y 2717-2737, south at x 7247-7267, west along y 2867-2883 (seen to x 7180) | ends on contact (8139,3567): poly east y 3556-3578 to x 8332, where it turns south | |
| ns3 | 8176-8191 | from the east on y 2720-2734 | jogs east at y 4151-4169 to x 8197-8213, ends on contact (8206,4329): poly west y 4320-4342 under the VCC and VSS verticals, south to contact (7905,4370), metal south x 7894-7909 past y 4450 | |
| ns4 | 8219-8234 | from the east on y 2764-2778 | jogs east at y 4112-4135 to x 8241-8257, west along y 4369-4383, south at x 8198-8212 past y 4450 | none in this block |
| ns5 | 8262-8278 | starts on contact (8271,2857): poly east y 2846-2868 | ends on contact (8270,3833) | (8270,3739) and (8270,3833), each to a poly going east |
| ns6 | 8307-8321 | from the east on y 2807-2821 | ends on contact (8313,3870) | (8313,3527) and (8313,3870), each to a poly going east; the metal is continuous across the upper one (profile along x 8314) |

Below ns1's and ns2's ends the same two tracks are reused: x 8088-8105 from y 3716 down
is `ras_shift` (field between y 3670 and 3710 at x 8096, measured), and x 8307-8321 from
y 4078 down is `ras_shift` again (ns6 ends at y 3883; a C-shaped poly lies between).

### Other lines through the bus field (routing only)

- `tc1_x1`: poly from the east at y 4255-4275 (datapath), south at x 7807-7831 under the
  VSS bus to contact (7815,4372), metal west along y 4369-4383 to contact (7359,4352),
  poly west along y 4344-4362 to contact (7056,4352), metal south x 7049-7068 past
  y 4450.
- `db_b6`: poly from the east at y 4365-4383 to contact (8075,4372), metal south
  x 8067-8082 past y 4450.
- VCC bus y 4198-4250 from the foot of the centre rail east to x 8166, then south at
  x 8116-8165. A plain rectangle: the diagonal lines on its east end are the edges of
  the `ras_o0_sel1` poly underneath. VSS bus y 4288-4335 from the foot of the left rail
  east to x 7995, then south at x 7943-7990.

Believed, not traced: L2, L3 and R3 have strong loads and wide pull-downs, so
`ras_o0_sel2` (NOT a AND b), `ras_o0_sel1` (a AND b) and `tc1_f` are lines with a heavy
load: strobes or enables. `a` and `b` together select which of them is active.

Sizes (W/L in px): weak loads 22/60 (R1, R2), 27/59 (L1), 28/59 (R4), 23/47 (L4);
strong loads 38/45 (R3), 40/42 (R5), about 65/36 (L2, L3; the strip's height under the
gate was not measured). Pull-downs 43/20 (R1, R4), 72/20 (L1), 55/18 (R2), 42/21 (L4),
67/18 (R3), 133/19 (R5, each of four), about 260/23 and 230/23 (L2, L3: each gate wraps
the drain region as an L). For L2 and L3 the W comes from rectangles drawn to the
visible edges; whether a source strip lies under the far end of each bottom arm
(x 7547-7591) was not settled, so their W is good to about 15 %.

## The driver gated by `tc1_g` (run 3, 2026-11-17; traced, extracted)

    tc1_o4020 = NOR(tc1_g, tc1_x1)

A wide two-input NOR with a strong load, built like L2 and L3 of the island (a gate that
wraps the drain; load 60/37). Nine transistors as drawn, and a tenth beside it (the pull-down on the strip, below). Views in `cache/scratch/tc1/`: `g1.png`
... `g11.png`, the class map `cm1.png`, overlays `ov1.png` ... `ov4.png`; text maps by
`tools/tc1_hex.py` (new: a rectangle as three character maps, the two metal shots and the
clean shot; its docstring gives what a real contact measures).

**What is there.** One diffusion lies under the rail x 6861-6932 and spills out on both
sides, under two thin metals that have no contact to it (x 6817 and x 6968). Two polys cut it:

| Poly | Shape | Separates |
|---|---|---|
| `tc1_g` | the band y 3992-4014, which the earlier runs drew from the east as far as x 6960, runs on west under the thin metal x 6968 and under the rail; at x 6836-6862 it turns north to y 3943 and then west along y 3943-3961, across the diffusion column under the thin metal x 6817, ending at x 6772 | region A (x 6858-6936, y 3925-3992, **rail contact (6897,3958)**, with its strips under both thin metals) from the output node |
| `tc1_x1` | a ring round an island (x 6884-6936, y 4057-4178, **rail contact (6902,4136)**): an upper U (bar y 4035-4057, legs x 6862-6884 and x 6920-6944) and a lower U (leg x 6862-6884, bar y 4178-4202, east leg the block x 6950-6990, y 4123-4202), joined west of the rail by a vertical strip x 6820-6838, y 4083-4160 into which a foot of each U runs. The upper U's right foot runs east along y 4078-4100, over the diffusion column under the thin metal x 6968, to a pad with a **contact (7054,4092)** on the channel metal x 7053 | the island from the output node |

**A branch of the ring** (found by review round 1, then drawn). The east leg's top does not
end at x 6990: the band y 4122-4146 runs on east under the channel metal x 7011 (no ring
on that metal: its dark bars at y 4120-4130 and 4144-4154 are the band's two edges), turns
south at x 7028-7046 and west again along y 4254-4272, to a pad (6940-6978, 4252-4284)
under the thin metal x 6968. **That pad has a contact to the thin metal** at about
(6962,4268): a dark ring with a bright centre in both metal shots (weaker than on the
`tcw` pads: red 150-200 against 180-220), a green hole inside the pad in the clean shot,
white in the chip-2 stripped shot. So the thin metal x 6968 is `tc1_x1` (it runs from
(6966,3806) to (6975,4402) by the follower; its other contacts are not looked at). The
branch crosses the gap between the metals x 6968 and x 7011 twice. That gap is a dark bar
in the clean shot (trap 2) and box means of the three shots in it do not tell poly from
field (tried on two known polys and two known fields there). At y 4122-4146 one band
continues at the same height on both sides of the bar: drawn certain. At y 4254-4272 the
band meets the pad: drawn `?P`, and the thin metal is therefore labelled `tc1_x1_u` and
aliased, as `trace/rad.txt` does for `ra4_drv_in_u`. Review round 2 measured the gap at
(6987-6995, 4260-4270) as orange in three shots and calls the join real; it stays `?P`
because of what follows.

**What else is on that pad** (found by review round 2, then drawn; views `h1.png` ...
`h5.png`, class map `h4.png`). A diffusion strip y 4270-4293 runs from the pad's west edge
west under the rail to the diffusion under the thin metal x 6817. Under the rail the strip
is one side of a pull-down: gate = a poly along y 4298-4320 (`tc1_p4308`; salmon under the
rail at x 6878-6912) that turns south at x 6988-7002 (seen to y 4382: not followed),
other side a diffusion (6877-6914, 4322-4368) with a **rail contact (6888,4338)** (a ring
6870-6915 x 4320-4365 in both metal shots, a pit in the clean shot). Run 4 found the
strip's load: it is the output of an inverter ("The inverter of `tc1_p4308`"). How the strip
meets the pad is not resolved (a dark line at x 6940-6957 between plain tan and the pad's
ring), and **that join is not drawn** (Ambiguity 17). The strip is `?D` where it crosses
the two gaps.

The output node is everything outside both: the strip y 4014-4035, the column under the
thin metal x 6817 (y 3961-4222, narrowed to x 6800-6816 beside the strip), the band
y 4203-4222 under the lower U, and the column under the thin metal x 6968 (y 4014-4078,
and east of the block). It leaves by a **buried contact (6966-6990, 4032-4062)** on the
east column: a poly runs east along y 4037-4057 to the **contact (7099,4047)**, whose metal
goes east and then north as the channel metal x 7133-7152.

**The ring's gate is `tc1_x1`.** The channel metal x 7053 is one piece from the contact
(7054,4092) down to `tc1_x1`'s contact (7056,4352), which run 2 drew (text map of
x 7030-7078, y 4060-4372 in both metal shots: bright metal all the way, a ring with a
bright centre at each contact and none between). `tc1_x1` = NOT `ras_o0_sel1`
(`notes/blocks/shm.md`), so, with `tc1_g` = NOT `fld_a_in` (`notes/blocks/fld.md`):

    tc1_o4020 = fld_a_in AND ras_o0_sel1        (believed: it rests on those two blocks)

**Load.** A diffusion under the west rail (x 6716-6752 from y 4036, widening to
x 6700-6756 at y 4120-4206, where the rail contacts it: a ring 6705-6750 x 4125-4195 in
both metal shots, pits in the clean shot) sends a strip east (y 4041-4100) to the west
column. The poly block x 6752-6790, y 4035-4105 lies across the strip (orange in the
chip-2 shots; between the block and the column the strip is in the open and red-brown).
The block's stem goes up x 6752-6764 to y 3992 and east into a buried-contact box
(6764-6796, 3988-4018; dark ring, pale centre, no pits, no metal) on a tab of the column.

**Supplies.** By the layout rule only: the load hangs from the rail x 6690-6748, so that
rail is taken as VCC and the rail x 6861-6932, which both pull-downs' sources contact, as
VSS. Neither is followed to a pad or to the island's rails (Ambiguity 11 stands; `tcw`
and `fld` make the same assumption for the same two rails, AMB-014).

**Sizes** (W/L in px, from the drawn rectangles): `tc1_g` 120/22 under the rail (band
plus north arm), 51/18 at the west arm, 42/19 on the east column; `tc1_x1` 148/24 (upper
U), 128/23 (lower U under the rail, the leg now a gate on its west side too), 96/27 (east
leg and bar), 40/22 (the foot on the east column), 22/18 (the strip over the island's neck,
`?D`); load 60/37; `tc1_p4308`'s pull-down 37/22. The north arm's and
the strip's shares rest on `?D` items; the connections do not depend on them.

**How each join was decided.**

| Join | Evidence |
|---|---|
| Output strip and its west side (y 4014-4083) to the west column, across the gap between the thin metal x 6817 and the rail | the clean shot in the gap is red (90-158 / 65-112 at y 4021, 4045, 4060, 4075) where the same gap over field is khaki (86-137 / 85-141 / 46-93, y 4240); run 2 measured the same at y 4021; review round 1 read the whole stretch as diffusion |
| Band y 4203-4222 to the west column, across the same gap | red in the gap at y 4212 (93-150 / 71-131); in the metal shot the band's two edges cross the gap |
| Band y 4203-4222 across the east gap | red in the gap at y 4212 (94-151 / 68-100) |
| Output strip to the east column (y 4014-4032), **`?D`** | the gap is a dark bar in the clean shot (trap 2) and measures neutral; in the metal shot the gap is plain there and an edge curves round below it (y 4032-4075). The east column's part between the two gates has no other neighbour that could supply its load |
| Island to the east column (y 4104-4120), **`?D`** | dark bar; in the metal shot an edge crosses the gap at y 4120 and none above it |
| Region A to the strip above `tc1_g`'s west arm and to the east column's top, both **`?D`** | dark bars; one outline in the metal shot |
| The column to region A under `tc1_g`'s north arm (y 3961-3992), **`?D`** | the arm covers it; it only adds width to the same gate |
| Output-side diffusion west of the lower U's leg (6838-6862, 4158-4222) | review round 2, re-measured: the clean shot is tan (protected diffusion, 201/187/131) at x 6854-6858 and red in the gap at rows y 4165 and 4190, the leg's poly starting at x 6862. The leg is one more gate segment |
| The column under `tc1_g`'s west arm wider by 14 px, **`?D`** | review round 2: red-brown to an edge line at x 6784 at y 3972; width only |
| The island's neck west under the strip to the column (y 4108-4130), **`?D`** | review round 1: diffusion colour in the gap at (6844,4122) in the chip-2 stripped shot, the strip paler at y 4112-4130 in both stripped shots. One more gate of `tc1_x1` between the same two nets |
| Buried contact of the output on the east column | a box with nested outlines at the poly's west end in both stripped shots, pale inside, no pits; the poly ends there (text map: no poly across the column at y 4036-4056) |
| Contacts (7054,4092), (7099,4047), (7140,2832), (7465,2640), (7706,2640), (7900,2640) | ring and bright centre in both metal shots, green hole inside the pad in the clean shot; each looked at again by review round 1 |

**Where the output goes** (traced to the region's east edge; views `n1.png` ... `n8.png`,
overlay `n6.png`):

1. Channel metal x 7133-7152 from the contact (7099,4047) north to a pad with the
   **contact (7140,2832)**. No tap on the way: along x 7142 both metal shots show only dark
   bars of 6-10 px (the edges of the polys it crosses: `tc1_g` at y 3995/4014, `tc1_l4_out`
   at y 3885/3905, two more at y 3342 and y 3495), no ring.
2. Poly from the pad east along y 2822-2845, north at x 7202-7222 to y 2676, east along
   y 2676-2694 to x 7482, north at x 7462-7482 to a pad with the **contact (7465,2640)**
   (ring and bright centre in both metal shots, green hole in the clean shot). Seen whole in
   one 3.2x view of the clean shot with the trace on it. From x 7350 to x 7480 this poly
   lies lengthwise under the bus metal y 2684 (trap 13): the text map shows no ring in the
   metal and no hole in the poly there, so no contact.
3. The contact is the west end of **the bus metal y 2641** (the third of the top bus
   field's seven lines). It runs east to the contact (7706,2640), crosses the island's
   right VSS rail in poly (salmon under the rail, x 7740-7822; open poly east of it) to
   the contact (7900,2640), and goes on east as metal. `tools/follow.py` gives its end at
   (9098,2639), 1,180 px on, over the top of the datapath: drawn to x 8350, not looked at
   beyond.

**Not joined, measured:** a second poly lies on the same y just west of the pad at
(7465,2640): it comes from a vertical poly x 7160-7180 along y 2628-2648 (under metal to
x 7370, in the open from there) to x 7438, where review round 2 saw it turn north
(x 7415-7438) rather than stop. Between its end and the pad's ring
the clean shot is bright green (114/166/77 and 129/152/94 at x 7443-7446, y 2634-2646) and
the chip-2 shots show red equal to green (83/81/45, 123/118/66: field, not poly, not
diffusion) for about 8 px, and the chip-2 stripped shot shows the poly's end edge at
x 7437-7440. Two nets. What that poly does at its end is not looked at (a tan band lies
under it at y 2652-2668).

**What `tools/unsure.py` says.** `--equations tc1_o4020`: FIRM (the NOR and its load
extract with every `?` item deleted). `tc1_x1` is listed as two pieces: the net as it was,
and the thin metal x 6968 (`tc1_x1_u`), joined only through the `?P` at the pad (above).
`tc1_o4020` is listed as "2 pieces without the
uncertain items": the node as labelled on the west column, and the output poly with the
channel metal and the bus line y 2641. They are joined only through the `?D` at
(6930-6952, 4014-4032), the strip of the output node across the gap between the rail and
the thin metal x 6968 (table above). So **the equation is firm; that the net on the
channel metal x 7142 and the bus line y 2641 is this NOR's output is an assumption**
(trap 17), resting on that one strip.

## The inverter of `tc1_p4308` (run 4, 2026-11-17; traced, extracted)

    tc1_o4280 = NOT tc1_p4308          (`tc1_o4280` is the strip's node: a net of its own in the trace)

Two transistors, at x 6688-7002, y 4243-4384, south of the driver. Views `k1.png` ...
`k5.png` (overlay `k5.png`), `h1.png` ... `h6.png`.

| Part | Where | Evidence |
|---|---|---|
| Pull-down | under the rail x 6858-6908: the strip y 4270-4297 / gate `tc1_p4308` y 4298-4320 / a diffusion (6877-6914, 4322-4368) with the rail contact (6888,4338) | class map `h4.png` (diffusion, poly over channel, diffusion); ring in both metal shots, pit in the clean shot; review rounds 2 and 3 of run 3 |
| Output node | the strip y 4270-4293 from x 6934, just short of the pad (6962,4268), west under the rail (`?D` in the two gaps) to the diffusion under the thin metal x 6817 (6803-6835, 4270-4337) | as above; the thin metal has no contact on it (text map: unbroken bright metal at y 4290-4329, the only dark bar the diffusion's south edge at y 4335) |
| Load | the supply rail (x 6688-6736 here) contacts a diffusion pad (6690-6742, 4250-4322); a strip y 4268-4292 runs east from it under a poly block (6746-6798, 4246-4310) to the output node | pad: ring in both metal shots, pits at (6705,4283) and (6712,4300) in the clean shot. Block: orange in both chip-2 shots at y 4250-4258, 4270-4290 and 4298-4306 with the strip's two edge lines across it at y 4264 and y 4294 (column profile at x 6770); in the clean shot the middle band is the brighter (poly over a channel) |
| Gate tie | the block's foot enters a buried-contact box (6774-6802, 4312-4342) on a tab of the output node's diffusion | box: dark ring and pale centre in both chip-2 shots (row y 4332, column x 6788), no pits, no metal |

Sizes: pull-down 37/22, load 24/52 (a weak load, like the island's 22/60).

**The strip's join to the pad is not drawn, on purpose.** East of x 6934 the strip runs up
to the pad (6962,4268), on which `tc1_x1`'s branch poly ends (`?P`) and which has the metal
contact of the thin metal x 6968. If the strip joins the pad, this inverter drives the ring
gate of `tc1_o4020` and the whole `tc1_x1` line, on which `shm` already draws an inverter of
`ras_o0_sel1`: two complete inverters on one line. I think at least one of the joins
involved is wrong and do not know which, so the one that would change an existing equation
is left out: in the extraction `tc1_x1` = NOT `ras_o0_sel1` as before, and `tc1_o4280` is a
net with no destination drawn. Ambiguity 17 has the evidence, which got stronger *for* this
join in the review of run 4 (a butting contact is the likeliest reading of the pad).
`tools/unsure.py`: `tc1_o4280`'s equation DEPENDS (its load reaches it across the west gap's
`?D`); `tc1_x1` is two pieces without the uncertain items (the line, and the thin metal
x 6968 with the pad).

## The two rows below the inverter (run 5, 2026-11-17; wiring, traced to x 6750)

Views `m1.png` ... `m5.png` in `cache/scratch/tc1/`; text maps and strips.

| Row | Route | Evidence |
|---|---|---|
| `tc1_p4308` (y 4428-4448) | the inverter's gate poly goes on south at x 6988-7006 to y 4448 and turns west along y 4428-4448, under the rail x 6858-6908, the metal of `tc1_m6817` (x 6788-6806) and the supply rail x 6688-6736, to x 6750 (drawn). **Seen further, outside this package:** it ends on a pad with a contact at (6620,4436) (dark ring 6600-6640 x 4415-4455 with a bright centre in both metal shots, green hole in the clean shot); the pad's metal goes south along x 6621 to (6622,5006) by the follower, into `fld`'s upper group | clean shot: salmon all along under the metals, over pink (field: no transistor under either rail; `tools/railprof.py` says the same under the rail); chip-2 stripped shot: orange in the open stretches (x 6910-6990, x 6610-6724). No ring on any metal that crosses it (the metal of `tc1_m6817` is bright over it at y 4434-4446) |
| `tc1_x1_u` (y 4385-4405) | the thin metal x 6968 runs on south from the pad (6962,4268) to y 4404 (x 6964-6980 there), where a foot spreads west over a poly pad (6928-6966, 4380-4412) onto the **contact (6947,4396)**; the pad's poly runs west along y 4385-4405 under the same three metals to x 6750 (drawn). **Seen further:** west under the ground rail x 6505-6560 (salmon there: not checked for a channel) to about x 6445, where a strip of the chip-2 stripped shot loses it | contact: ring with a bright centre in both metal shots (text map), green hole inside the salmon pad. The 20 px gap at x 6914-6930 between the row and the pad is orange in both metal shots (158/120/53 and 158/76/39) where the row between the two polys is bare ground (172/151/87, 157/125/68). The metal of `tc1_m6817` is bright over the row at y 4392-4401: no contact |

So the input of the inverter comes from the south, from the logic west of the selector
(`fld`); and the net of the thin metal x 6968, which is `tc1_x1` if the `?P` holds, goes
west into the first gate column. Neither end is in this package. For Ambiguity 17 this
adds: the net on the pad (6962,4268) has at least one more destination, which fits a
distributed signal; it does not decide any of the three joins.

**The thin metal x 6968's north end** (one view, `m4.png`; not drawn): above a dark bar at
y 3798-3805 the metal widens to a pad (6958-6998, 3778-3797) lying on a horizontal poly
y 3775-3795; whether that is a contact is not decided. South of the bar the metal runs
over a diffusion-coloured column (x 6952-6975).

## The second driver (run 6, 2026-11-17; traced, extracted)

    tc1_o3740 = NOR(tc1_p3698, tc1_x1_u)        (tc1_x1_u: the thin metal x 6968, alias of tc1_x1)

Five transistors as extracted (gate 1 and its arm's crossing, gate 2 and its arm's crossing, the load) at x 6690-7035,
y 3600-3900, directly north of the driver `tc1_o4020` and of the same build. Views in
`cache/scratch/tc1/`: `p1.png` ... `p7.png`, `q1.png` ... `q7.png` (`q7.png` is the overlay),
the class map `p2.png`; row and column profiles; `tools/tc1_green.py`.

| Part | Where | Evidence |
|---|---|---|
| Rail-contact region, top | under the rail x 6858-6906, y 3627-3688, **and on east of the rail to an edge at x 6969-6978**; contact (6880,3658) | diffusion in the class map; two pits in the clean shot, a ring 6870-6895 x 3652-3670 in the metal shot. East part (review of run 6): no edge at x 6914-6930 or at y 3675-3683 in either metal shot, red minus green 17-27 in the chip-2 stripped shot. I had taken it for a closed box: its "outline" is the protection boundary of the metal that passes over it (trap 2) |
| Gate 1, `tc1_p3698` | band y 3688-3708 under the rail and on east, still over diffusion, ending at x 6986 just past the diffusion's edge; at x 6824-6849 it turns north to y 3645 and west along y 3645-3668 across the column under the thin metal x 6817, on in the open to a vertical poly under the supply rail's east edge (x 6725-6740), which comes from the north | band: poly over channel in the class map; the band crossing the gap to the leg and the leg itself: row profile at y 3690 (salmon at x 6826-6832, orange-brown in the metal shot at x 6835-6847). **Arm to the vertical poly**: row profile at y 3656: orange in three shots at x 6746-6752, where 26 px north (y 3630) there is no poly; the two dark lines across the arm at x 6741 and x 6757 are the rail's edge and its etch line |
| Output node | under the rail y 3708-3776; the column under the thin metal x 6817 (y 3668-3852, west of the two legs); its open part east of the rail (6914-6952, 3718-3766) and the box region on the column under the thin metal x 6968 | west join across the gap between the metals: redder than the field of the same gap in three shots (row y 3740 against row y 3915). East part: bright green in the clean shot with red minus green of 17 in the chip-2 stripped shot: large open diffusion by the calibration at the top of these notes (I first read it as field) |
| Gate 2 | band y 3776-3798 under the rail, on east over the open diffusion and over the column under the thin metal x 6968, to a pad with the **contact (7009,3789)**; at x 6824-6849 it turns south to y 3852 and west along y 3852-3878 across the column, ending at x 6778 | class map; row profile at y 3820 (leg at x 6826-6832); `q1.png`, `p7.png` |
| Gate 2's source | **the thin metal x 6968**: its north end turns east along y 3783-3797 and enters the contact's ring from the west | `q6.png` (5.6x, both metal shots and the clean shot): ring 6998-7030 x 3768-3808 with a bright centre in both chips, the bright metal arm west of it, green hole under the centre; 2 px text map: the dark line at x 6970-6974 between the arm and the line from the south is the edge of the column's diffusion underneath |
| Rail-contact region, bottom | under the rail y 3798-3897, contact (6880,3845); its foot under the widened rail (to x 6936); its open part east of the rail (6914-6952, 3803-3866) and the column under the thin metal x 6968 below gate 2 | pits at y 3825, 3860, 3875 and a ring 6868-6885 x 3835-3855; the open part bright green and diffusion by the chip-2 stripped shot (164/147/96) |
| Output's way out | buried-contact box (6943-6980, 3724-3764) on the column under the thin metal x 6968 (that metal ends south of it, so the box is in the open); poly east along y 3728-3750 to a pad with the **contact (7010,3722)**; metal north to y 3659, **west along y 3653-3665, north along x 6941-6956** past y 3600 | nested outlines, no pits, in both stripped shots; contact: ring and bright centre in both metal shots, green hole. The route is the follower's (corners (7004,3660) and (6946,3651), end (6947,3547), a contact candidate at (6948,3595)) and the review's: I had drawn it straight north along x 7010, where both metal shots are bare from y 3644 up. It passes over the top contact region's east part without contact. Not followed north of y 3600; it is **not** run 2's metal from the contact (7010,3092) |
| Load | the supply rail's diffusion (contact (6715,3768): pits all along it) sends a strip east to the column under a poly block (6746-6782, 3736-3800); the block's top enters a buried-contact box (6757-6795, 3686-3722) on a tab of the column | row y 3760: protected diffusion to x 6742, orange poly x 6748-6780, a red-brown open strip x 6792-6796, the column from x 6803; column x 6770: orange y 3740-3796 with no edge line across it (the strip is as tall as the block, as at the first driver's load) |

Sizes (drawn, after the review): gate 1 153/19 (band from the leg to x 6972) and 20/23 where
its arm crosses the column; gate 2 one channel from the leg to the east column, and 20/26
where its arm crosses the column; load 60/36. Under the legs the diffusion is not visible
(`?D`): width only.

**What it means.** One input is the net of the thin metal x 6968 (Ambiguity 17: `tc1_x1` if
the pad's `?P` holds, the inverter `tc1_o4280` if the undrawn join J1 holds, both if both).
The output goes north on the metal x 7010, **not** to `tc1_x1`'s channel metal x 7053: the
"ring at about (7055,3730)" on that metal, listed under Not done since run 3, is not a
contact (no hole in the clean shot; a poly lies lengthwise under the metal there and makes
the two dark bars).

**Three contacts stand in a column at x 7010** (`q6.png`), each with its own metal, and
between them the ground is bare: (7010,3722) with metal to the north (this output);
(7009,3789) with metal to the west (gate 2, from the thin metal x 6968); (7010,3855) with
metal to the south (the channel metal that the follower takes down to (7006,4484): its pad's
poly is not followed). Run 2's "vertical at x 7002-7022" is therefore three pieces.

**Uncertain (`?D`), all width only:** the diffusion under each leg (under poly, not
visible); the diffusion west of the column that gate 1's arm crosses (x 6758-6802, y 3627-3690: its west edge at x 6755-6758 runs the whole height in both metal shots, so the arm's channel is about 62 wide; the part under the arm is not visible).

**Not drawn, inside the region** (the pad at (7010,3855) and its poly are drawn in run 7: cell B's output). The slot at y 3606-3626,
x 6920-6968, is **field, not a poly row** (round 1 took it for poly from a text map; round 2
and my own profile: 170/145/124 under the output's metal against 244/180/128 on the gate
rows 50 px either side, and the same slot one cell north, y 3432-3450, reads 175/133/116,
which is the field under the rail). It is a notch in the rail-contact region between its two
fingers. The
structure at (6745-6800, 3810-3900) west of the column's foot.

## Cell B: the NOR north of the second driver (run 7, 2026-11-17; traced, extracted)

    tc1_o3527 = NOR(tc1_o3353, tc1_o3095)

Three transistors (two pull-downs 40/20 and 40/21, load 32/50) at x 6690-7160, y 3405-3625.
The column under the rail x 6858-6906 goes on north of the second driver as two smaller
NOR cells of one build: cell B (y 3410-3625, this run) and cell A (y 3240-3410, **not
drawn**). Their transistors are not under the rail but east of it, on a diffusion column
x 6928-6968 under the thin metal x 6941-6956. Views in `cache/scratch/tc1/run7/`:
`s_*.png` (survey, 3x), `b_*.png` (4x, three shots), `w1.png`/`w1b.png` (west side, 5x, four
shots), `box.png`, `lad.png`/`ladb.png` (9x), `j1.png`/`j1b.png` (7x), `op.png`, `chs.png`,
`sth.png`, overlays `ov1.png` ... `ov3.png`; `survey.md` there is the survey as written.

| Part | Where | Evidence |
|---|---|---|
| Rail-contact region | under the rail, (6872-6920, 3412-3471), contact (6885,3440); two fingers east to x 6968 at y 3412-3430 and y 3454-3471, a **field slot** (6920-6968, 3432-3452) between them | ring in both metal shots, pits in the clean shot; slot 175/133/116 in the clean shot (field under metal 173/134/120; the gate rows 244/180/128) |
| Column | diffusion x 6928-6968 from the lower finger (y 3454) to the next finger (y 3585-3606), which belongs to the second driver's rail-contact region. That region's top edge is at y 3583 (run 6 drew it from y 3627) and it has a third contact at (6887,3606) | tan under the thin metal in the clean shot (201/182/135), bright salmon where the gate rows cross; `b_acid1b.png` |
| Gate row 1, `tc1_o3353` | poly y 3472-3492 from x 6920 east. It is the lower row of a **C-shaped poly**: east to x 7137-7154, north under the channel metal x 7133-7152 to y 3345, west along y 3345-3362 to cell A's middle node | salmon all the way in the clean shot (`ch_clean.png`), dark outline with rounded corners in the metal shot; no ring on the three channel metals it passes under |
| Middle node (output) | (6928-6968, 3497-3556); on it a buried-contact box, outer outline (6940-6970, 3510-3546), poly end (6950-6968, 3518-3538) | `box.png` (7x): nested outlines at a poly end, tan inside, no pits, no hole |
| Output's way out | poly east along y 3517-3536 to x 7050-7067, **south lengthwise under the channel metal x 7048-7068** (`tc1_x1`'s) to y 3845-3865, west to a pad (6998-7032, 3838-3870) with the **contact (7011,3852)**; from it the channel metal x 7003-7023 south, leaving at y 4450 | `op.png` (3.5x, four shots): salmon x 7050-7068 unbroken from y 3520 to y 3860, the metal over it unbroken in both metal shots; `chs.png`, `sth.png`: no ring on the metal x 7003-7023 between the pad and y 4450, no hole in the clean shot |
| Gate row 2, `tc1_o3095` (cell C's output, run 9) | poly y 3558-3579, x 6912-7030, with a pad (6995-7032, 3553-3590) and the **contact (7011,3571)**: the channel metal x 7003-7023 comes to it from the north and ends there | heavy ring with a bright centre in both metal shots, green hole in the clean shot; bare ground south of the ring down to the contact (7010,3722) |
| Output node, west | a band y 3520-3536 from the middle node west under the rail to a region (6800-6836, 3497-3540) under the thin metal x 6817 | tan with dark (not red) outlines in the clean shot (R 204: field 173, poly 244); in the metal shot its edge lines run unbroken from the column to the region, the upper one turning north into the region's east edge |
| Load | band y 3508-3540 from that region west, under a poly block (6748-6798, 3460-3554), to the supply rail's contact region (6694-6742, 3496-3572; contact (6710,3530)). The block's arm (y 3462-3480) runs east onto a stub of the region (6816-6834, 3464-3500): buried contact (the "ladder") | block: salmon under the thin metal x 6775 with the band's edges as dark lines at y 3503-3509 and y 3537-3543; arm: orange in the gap x 6800-6812 at y 3466-3476 and not at y 3486-3495; ladder: two pale cells in the clean shot divided by a line at y 3480 (`lad.png`) |

**`tc1_p3698` comes from the thin metal x 6765-6785.** That metal comes from the north and
ends on a poly pad (6755-6795, 3578-3605) with a contact at (6772,3591) (ring with a bright
centre in both metal shots, green hole in the clean shot). The pad joins west to the top of
the vertical poly x 6725-6740 that run 6 followed up from the second driver's gate 1. The
join crosses the gap between the rail's edge and the thin metal, which is a dark bar in the
clean shot (trap); measured in the chip-1 metal shot the gap is orange at the pad's rows
(x 6743-6752, y 3588-3594: red minus green 40-70, green 72-94) and bare ground above and
below (red minus green 12-17, green 120-140): poly.

**What it means.** Cell B's output is the NOR of cell A's output and of whatever drives the
channel metal x 7003-7023 from the north (run 2 saw its north end as a contact at
(7010,3092): not checked). It leaves the package south on the lower piece of that channel
metal, which turns west at y 4465-4495 to a contact at about (6965,4480), outside the
package. With run 6: "the vertical at x 7002-7022" is four pieces, the top one cell B's
input, the bottom one cell B's output.

**The two thin metals over the buried contacts.** `tc1_m6817` is dark over the ladder
(y 3458-3500: 29-96 in both metal shots, where the metal reads 180-230) and the thin metal
x 6948 (`tc1_o3740`) is as dark over the middle node's box (y 3510-3546: 38-85). The box is
plainly a buried contact with no hole, so a buried contact under a 12 px metal darkens it
this much without a metal contact. No contact is drawn at either (Ambiguity 18).

**Not drawn, seen:** cell A (y 3240-3410): its east side is cell B's shifted by -172 (the
C-shaped poly is its output; its lower gate row y 3385-3408 is the poly of `tc1_l4_out`'s
contact (7100,3395), drawn in run 1; its upper gate row at about y 3300-3320 not looked
at); its load side is not a copy (block y 3332-3415, ladder (6800-6835, 3377-3428)). A dark
loop at (7150-7165, 3495-3510) in the clean shot only, just outside the C-shaped poly's
corner: nothing there in either metal shot (taken as a blemish of chip 1).

## Cell A: the NOR north of cell B (run 8, 2026-11-17; traced, extracted)

    tc1_o3353 = NOR(tc1_m7100, tc1_l4_out)

Three transistors (pull-downs 40/18 and 40/15, load 31/50) at x 6690-7160, y 3240-3420,
with the upper input's poly up to the contact (7100,3180). The east side is cell B's,
172 px north on the same column; the load is cell B's mirrored top to bottom.
`tools/unsure.py --equations tc1_o3353`: FIRM (no `?` item in the piece). Views in
`cache/scratch/tc1/run8/`: `a_*.png` (2.6x, three shots), `e1.png`/`e2.png` (east side, 4.5x,
four shots), `f1.png`/`f2.png` (the finger, 6.3x), `g1.png` ... `g5.png` (the poly north to
the contact), `w1.png`/`w2.png` (load side, 3.8x), overlays `ov1.png`, `ov2.png`.

| Part | Where | Evidence |
|---|---|---|
| Rail-contact region | under the rail x 6858-6906, (6872-6920, 3254-3296), contact (6890,3276); one finger east onto the column, y 3280-3296 | tan box with pits in the clean shot, ring 6872-6910 x 3260-3288 in the metal shot; the finger's edge lines (y 3276, y 3297) cross the gap x 6906-6930 unbroken in both metal shots |
| Column | diffusion x 6928-6968 from the finger down to cell B's upper finger (y 3412-3430). It starts at y 3285: field above it to y 3232 (`tools/railprof.py`), so it is not joined to the next cell's column | tan under the thin metal x 6941-6956, bright salmon where the two gate rows cross |
| Gate row 1, `tc1_m7100` | poly y 3301-3319 from x 6915 (pink field under the rail west of it) across the column to x 7004, where it **turns north as a poly in the open, x 6986-7006**, up to a row y 3170-3190; that row runs east under the channel metals x 7013 and x 7058 to a pad (7082-7118, 3162-3200) with the **contact (7100,3180)** | row profile y 3310: salmon 245/172/120 over the column, orange in the open x 6971-6998 in three shots. Column profile x 6992, y 3172-3316: orange in both metal shots (red minus green 46-86 in chip 1) and red-brown in the clean shot all the way, bare ground at y 3160; one dull sample in the clean shot at y 3244. Its east edge lies under the west margin of the channel metal x 7003-7023 (salmon at x 6999-7005): that metal has no ring anywhere along it and the clean shot no hole (text map). Contact: bright centre in a dark ring in both metal shots, green hole in the pad |
| The contact's metal | the upper piece of the channel metal x 7091-7110: `tools/follow.py` takes it north to y 2766, west along y 2766 to x 6947 and north to an end at (6949,2677), in the top bus field. Bare ground between its south end (y 3190) and the lower piece (`tc1_l4_out`, from y 3384) | follower; `a_metal.png` |
| Middle node (output) | (6928-6968, 3319-3388), with a buried-contact box (6940-6970, 3338-3374) into which the C-shaped poly `tc1_o3353` (run 7) ends from the east | nested outlines at a poly end, as cell B's box (`e1.png`) |
| Gate row 2, `tc1_l4_out` | poly y 3388-3403 from the contact (7100,3395) (run 1) west across the column to x 6916 | salmon over the column; in the gap x 6914-6928 orange in both metal shots at y 3390-3398 (column profile x 6921); pink field under the rail |
| Output node, west | band y 3348-3363 from the middle node west under the rail to a region (6800-6836, 3347-3386) under `tc1_m6817` | tan under the rail (207/172/137). In both gaps (x 6843 and x 6921) the chip-2 stripped shot has red minus green 24-36 between edge lines at y 3345 and y 3364 and 2-7 outside them (the calibration at the top of these notes: diffusion 13-17, field 0-4) |
| Load | band y 3347-3378 from the region west under a poly block (6748-6798, 3328-3416) to the supply rail's contact region (6694-6742, 3347-3408), contact (6708,3378). The block's bottom runs east as an arm (y 3398-3416) onto a stub of the region (6816-6834, 3380-3416): buried contact (6808-6838, 3394-3420) | block: orange in both metal shots in the open at x 6750 from y 3330 to y 3414, the band's edges as dark lines at y 3346 and y 3374; arm: orange in the gap x 6792-6800 at y 3407 (chip 1: red minus green 67-85); stub: diffusion-coloured from the region down to the arm (text map); supply contact: ring 6695-6722 x 3355-3400, pits |

**The row y 3170-3190 goes on west of the corner** (not drawn west of x 6975): it crosses
the column under the thin metal x 6941-6956 at y 3173-3187 as a gate (salmon 245/172/124;
`tools/railprof.py`: gate) of the next cell north, whose column runs y 3100-3231 with a
second gate row at y 3129-3144. So `tc1_m7100` has two gates: cell A's row 1 and that one.

**What it means.** With cell B: `tc1_o3527` = NOR(NOR(`tc1_m7100`, `tc1_l4_out`),
`tc1_o3095`) = (`tc1_m7100` OR `tc1_l4_out`) AND NOT `tc1_o3095`. `tc1_l4_out` is the
island's NOR(`ras_o0_sel2`, `tc1_w1`). The other two inputs come from the north and are not
followed.

**The thin metals over cell A** (all drawn through to y 3250-3300; text maps of each strip
in both metal shots and the clean shot). `tc1_m6817` over the stub and the arm: dim from
y 3374 to y 3422, bright only at x 6818-6824, y 3404-3414 (B-D of 16 in chip 2, B in chip 1;
cell B's ladder reads 8-A at the same place), no green hole in the clean shot: no contact
drawn (Ambiguity 18). The thin metal x 6948 (`tc1_o3740`): bright over the finger between
the finger's two edge bars, which run on to both sides of the metal (not a ring), diffusion
colour with no hole under it; dim over the box as over cell B's: no contact drawn. The thin
metal x 6775 (`tc1_p3698`): edge bars of the block and the band only. Its west edge is dim
at y 3257-3263 in both chips, north of this cell: not looked at (drawn to y 3300 only).

**Not drawn, seen:** the row y 3170-3190 west of x 6975 and the cell it belongs to; a
diffusion band at about y 3202-3227 from x 6815 to x 6970 north of this cell's rail-contact
region (`ov1.png`: the next cell's). The khaki box (7078-7126, 3233-3337) and the green
ovals at (6972-7000, 3325-3340) and (6972-7000, 3368-3382) are open ground between metals
(artefacts).

## Cell C: the three-input NOR north of cell A (run 9, 2026-11-17; traced, extracted)

    tc1_o3095 = NOR(tc1_p3051, tc1_x1, tc1_m7100)        (tc1_p3051: gate row 1's poly; its source is open)

Four transistors (pull-downs 40/18, 40/19, 40/20; load 25/50) at x 6690-7080, y 2940-3240, on
the same column x 6928-6968 under the thin metal x 6941-6956. `tools/unsure.py --equations
tc1_o3095`: FIRM. Views in `cache/scratch/tc1/run9/`: `r9a_*.png` (2.6x, three shots),
`w1.png`/`w2.png` (west, 3.9x), `e1.png`/`e2.png` (east, 3.5x), `c1.png`/`c2.png` (the bottom
band, 4.6x), `n1.png` ... `n5.png` (the north end), overlays `ov1.png`, `ov2.png`.

| Part | Where | Evidence |
|---|---|---|
| Rail-contact region 1 | (6870-6918, 2990-3038), contact (6887,3015); finger east y 3018-3038 onto the column's top | tan box with pits in the clean shot, ring 6872-6903 x 2998-3032 in the metal shot |
| Gate row 1, `tc1_p3051` | poly y 3042-3060 from x 6914 across the column to x 7003; north in the open along x 6988-7003 to y 2950; west along y 2950-2962 into a box (6936-6974, 2944-2970) | rows y 2985, 3015, 3050 and column x 6997: orange in the chip-1 metal shot (red minus green 48-84) from y 2965 to y 3050, salmon over the column and under the margin of the metal y 2933-2948 |
| Middle node (output) | column y 3060-3127, with a buried-contact box (6940-6970, 3077-3113); poly east y 3085-3103 to a pad (6995-7032, 3075-3112) with the **contact (7010,3093)**, the north end of the channel metal x 7003-7023 | box: nested outlines at a poly end like cells A and B; contact: bright centre in a 36 px dark ring in both metal shots, green hole (text map); bare ground north of the pad |
| Gate row 2, `tc1_x1` | poly y 3127-3146 from x 6909 across the column, under the channel metal x 7003-7023 (edge bars only) to a pad (7042-7074, 3120-3156) with the **contact (7056,3138)**, the north end of `tc1_x1`'s channel metal x 7048-7068 | contact: bright centre in a dark ring in both chips, green hole; the follower from (7055,3330) north ends at (7054,3134); bare ground north of the pad in both chips. West end: orange to x 6911, the tan of region 2 from x 6902 west (row y 3136) |
| Rail-contact region 2 | (6859-6902, 3127-3176), contact (6877,3146); finger east y 3152-3166 onto the column between gate rows 2 and 3 | tan box with pits, ring 6861-6892 x 3128-3163 |
| Gate row 3, `tc1_m7100` | the row y 3170-3190 from the contact (7100,3180) (run 8), now drawn across the column to its end at x 6914 | salmon 245/172/124 over the column (row y 3178) |
| Bottom region | column y 3190-3231; from it a band y 3206-3222 west under the rail, a strip x 6818-6836 north under `tc1_m6817` to a region (6804-6836, 3080-3106), and a band y 3085-3103 east under the rail back to the middle node | the outline of strip and bottom band is one line round the corner in both metal shots (`c1.png`); row y 3092: tan 206/169/141 from x 6846 to x 6911; strip at y 3160: 206/169/141; bottom band under the rail 205/155/137 (Ambiguity 19) |
| Load | band y 3078-3103 from the region west under a poly block (6748-6798, 3028-3120) to the supply rail's contact region (6692-6742, 3058-3160), contacts (6705,3078) and (6705,3136). The block's top runs east as an arm (y 3028-3048) onto a stub (6818-6836, 3034-3084) north of the region: buried contact (6804-6834, 3024-3052) | block: orange in the open at x 6750 from y 3031 to y 3116, edge lines at y 3076 and y 3104; arm: orange in the gap x 6792-6801 at y 3038; stub: tan from y 3036 to the region (column x 6828), with two duller patches at y 3044-3048 and y 3056-3060 |

**The output node wraps rail-contact region 2**: gate row 2 pulls the middle node down to
finger 2 from the north and gate row 3 pulls the bottom region down to it from the south;
the two are one node through the strip under `tc1_m6817`.

**The north end of gate row 1 (open; Ambiguity 20).** Established: gate row 1's poly is
one piece from the gate row north to y 2950 and west to about x 6980, with nothing joining it
on the way; it ends on the east outline of a box of pale cells with nested outlines
(6936-6974, 2944-2970), which looks like a buried contact. The thin metal x 6941-6956
(`tc1_o3740`, from the second driver) has a **contact (6948,2977)** directly south of the box
(the box's bottom outline is at y 2970-2974, the contact's centre at y 2977):
bright centre in a dark ring in both metal shots, a green hole in the clean shot. Not
established: what the contact lands on, whether box and contact are one node, and whether the
thin metal ends at the contact (the review: north of it the metal shots are as dim as over
the output box, where the metal certainly continues, so brightness does not say; the
follower's stop at (6947,2978) is not evidence). A metal y 2933-2948 comes from (7055,2806)
south along x 7056 and west to at least x 6974, and a dim strip carries it to about x 6940,
directly above the thin metal: one L-shaped metal or two is not readable. (My note that this
metal runs from about x 6820 came from one 3x overlay and is withdrawn: it would cross the
rail.) The box is the east end of a tan band y 2940-2961 that runs west, across the gap
x 6906-6935 (unconfirmed there: a plain strip between two edge lines in the metal shots, but
dark in the clean shot, neither tan nor green), under the rail to a region (6800-6835, 2940-2970) and, in one low-zoom
view, on under a poly block (6755-6797, 2940-2980) to a supply region: the shape of a load.
`tc1_o3740` already has its load. **Nothing is joined in the trace**, and the poly is named
by place. The equations below wait on this.

**What it would mean if gate row 1 were `tc1_o3740`** (not claimed): `tc1_o3740` =
NOR(`tc1_p3698`, `tc1_x1`), so `tc1_o3095` would be `tc1_p3698` AND NOT `tc1_x1` AND NOT
`tc1_m7100`. In any case cell B gives `tc1_o3527` = (`tc1_m7100` OR `tc1_l4_out`) AND NOT
`tc1_o3095`.

**The metals over the cell.** `tc1_o3740`'s thin metal: bright over the bottom region
between the region's two edge bars (y 3200-3216; no ring, no hole: the follower's candidate
(6948,3210) is not a contact), dim over the box y 3077-3113 as over the other two boxes.
`tc1_m6817`: over the stub and arm as at cells A and B (Ambiguity 18). The channel metal
x 7003-7023: dim for 12 px below its contact's ring, then only edge bars where gate row 2
passes under it. The thin metal x 6765-6785 (`tc1_p3698`): its west edge is dim at
y 3257-3263 in both chips, over plain field in the clean shot: nothing there to contact.

**Not drawn, seen:** the next cell north (a salmon load block at about (6750-6800,
2945-2970), a supply contact region at (6680-6742, 2970-3025)); the tan band y 2943-2962.

## Ports

Region edges: x 8250 on the east (drawn to x 8350, where the datapath's first slice
starts), y 4450 on the south (tc2), y 2500 on the north, x 6400 on the west. "In/out"
is as seen from this block; where no driver has been found the direction is "?".

East side (into the datapath, or the random logic at its slice-0 position x 8290-8750):

| Name | Layer | Where it crosses | Dir | What |
|---|---|---|---|---|
| `r8_b1_q` | P | x 8350, y 2846-2868 | ? | north end of ns5, from contact (8271,2857) |
| `tc1_ns3` | M | x 8350, y 2720-2734 | ? | ns3 arrives from the east over the top of the datapath |
| `ral_stb` | M | x 8350, y 2764-2778 | ? | ns4, the same |
| `r8_b0_q` | M | x 8350, y 2807-2821 | ? | ns6, the same |
| `tc1_f` | P | x 8250, y 3348-3362 | out | R3 output; runs on under ns1..ns6 without contact, in the channel between cdp1's rows A and B |
| `tc1_a` | P | x 8250, y 3387-3402 | in (believed) | same channel, 40 px below `tc1_f` |
| `r8_b0_q` | P | x 8350, y 3516-3539 | ? | from contact (8313,3527) |
| `tc1_ns2` | P | x 8250, y 3556-3578; reaches x 8332 and turns south there | ? | from contact (8139,3567) |
| `tc1_w1` (= ns1) | P | x 8250, y 3691-3712 (seen to x 8350) | **in** (its only other end is L4's gate) | from contact (8139,3704) |
| `r8_b1_q` | P | x 8350, y 3728-3751 | ? | from contact (8270,3739) |
| `r8_b1_q` | P | x 8350, y 3822-3844 | ? | from contact (8270,3833) |
| `r8_b0_q` | P | x 8350, y 3859-3881 | ? | from contact (8313,3870), the south end of ns6 |
| `ras_o0_sel1` | P | x 8250, y 4212-4228 (drawn to x 8350) | out | a AND b, to the datapath just above cdp1's row C |
| `tc1_x1` | P | x 8250, y 4255-4275 (drawn to x 8350) | ? | passes through: see the west side, y 4344-4362 |
| `db_b6` | P | x 8250, y 4365-4383 (drawn to x 8350) | ? | passes through: see the south side, x 8075 |

South side (tc2), west to east:

| Name | Layer | Where it crosses | Dir | What |
|---|---|---|---|---|
| `ras_straight` | M | 7230, 4450 (W2 lower, x 7220-7240) | out | NOT b |
| `ras_o0_sel2` | P | x 7422-7438, y 4450 | out | NOT a AND b; from the tap on track T2 |
| `ras_o0_sel1` | P | x 7465-7481, y 4450 | out | a AND b; from the tap on track T1 |
| `ras_shift` | P | x 7503-7522, y 4450 | in (believed: its only other end) | from contact (7511,4417) |
| `tc1_ns3` | M | x 7894-7909, y 4450 | ? | from contact (7905,4370) |
| `vss` | M | x 7943-7990, y 4450 | | the VSS bus (y 4288-4335, from the foot of the left rail) turns south |
| `db_b6` | M | x 8067-8082, y 4450 | ? | to contact (8075,4372) |
| `vcc` | M | x 8116-8165, y 4450 | | the VCC bus (y 4198-4250, from the foot of the centre rail) turns south |
| `ral_stb` | M | x 8198-8212, y 4450 | ? | ns4 has no contact in this block |

West side (drawn to x 6960, the east edge of the gate columns, which are not traced):

| Name | Layer | Where it crosses | Dir | What |
|---|---|---|---|---|
| `tc1_l4_out` | P | x 6960, y 3388-3403, going west; ends at x 6931 | out | NOR(l2_out, w1); arrives by contact (7099,3897), metal x 7091-7110, contact (7100,3395). West of x 6968 the band has diffusion-coloured (tan) areas above (y 3360-3386) and below (y 3405-3423) it: believed the gate of one transistor at x 6931-6968 (one 4x view, not drawn) |
| `tc1_g` | P | x 6960, y 3995-4014, going west | out of this wire (it is a gate there) | to the big structure at x 6750-6940, y 3930-4200, see Not done |
| `tc1_ns2` | P | x 7180, y 2867-2883, going west | ? | far end of ns2 (1.5x view) |

Run 3's ports (the driver; region edges as drawn):

| Name | Layer | Where it crosses | Dir | What |
|---|---|---|---|---|
| `tc1_o4020` | M | x 8350, y 2634-2648 (the bus line y 2641), going east | out | NOR(`tc1_g`, `tc1_x1`). The follower gives the metal's end at (9098,2639): not looked at. East of x 8250 it is outside this package
| `tc1_x1` (run 3's port; closed in run 9: the metal ends on the contact (7056,3138), cell C's gate row 2) | M | x 7048-7068, y 3405, going north | in | the channel metal x 7053 runs on north of the driver's contact; drawn to y 3405 (run 7: no ring on it over y 3405-4060; the candidates (7058,3745), (7057,3717) are a notch with no hole under it). The follower gives its end at (7054,3134) (run 2 saw a contact (7056,3138) there) |
| `tc1_m6817` | M | x 6811-6823 at y 3905; x 6788-6806 at y 4380, going south | ? | thin metal over the driver's west column, no contact drawn (Ambiguity 12). Follower (started either side of the strip, where it stops): from (6822,3496) south; it does not end at (6809,4379) as the follower says: there it has a foot (6788-6828, 4362-4380), a jog 20 px west, and goes on south at x 6788-6806 (bright again from y 4392 to at least y 4530, with the dark bars of poly rows across it: not followed, contacts not checked); candidates (6818,3883), (6813,3754), (6818,4309); the two at (6820,3977) and (6817,4211) are not contacts (text maps: unbroken metal, no ring) |
| `tc1_x1_u` (alias of `tc1_x1`) | M | x 6962-6974, y 3905 and y 4300 | ? | the thin metal x 6968: contact on the pad (6962,4268) at the end of `tc1_x1`'s branch; no contact to the driver's diffusion (Ambiguity 13). Follower: from (6966,3806) to (6975,4402) when started either side of the box at y 4033-4068, where it stops; candidates (6970,3947), (6972,4218) are not contacts (review round 1)
| `tc1_p4308` | P | x 6750, y 4428-4448, going west | in | input of the inverter; ends on the pad (6620,4436), whose metal goes south along x 6621 to (6622,5006) (seen, not drawn) |
| `tc1_x1_u` | P | x 6750, y 4385-4405, going west | ? | the poly row from the thin metal x 6968's south pad (6947,4396); seen to about x 6445 |
| `vcc` | M | rail x 6688-6736 at y 4330 | | the supply rail, narrower here than at the driver; goes on south |
| `tc1_p3698` | M | x 6765-6785, y 3405, going north | in | gate 1 of the second driver: the vertical poly under the supply rail's east edge ends at a pad with the contact (6772,3591), and the thin metal x 6765-6785 goes north from it (run 7); drawn to y 3000 (runs 8, 9: no contact over the loads of cells A and C; the dim west edge at y 3257-3263 is over plain field) |
| `tc1_p3051` | P | ends at about (6980,2956) on the box (6936-6974, 2944-2970) | in | gate row 1 of cell C; source open (Ambiguity 20) |
| horizontal metal y 2933-2948 | M | from (7055,2806) south along x 7056, west along y 2933-2948 to x 6974, dim to about x 6940 (follower, review of run 9) | ? | not drawn, not named; may be one piece with `tc1_o3740`'s thin metal |
| `tc1_m7100` | M | x 7091-7110, y 3140, going north | in | the upper piece of the channel metal x 7091-7110, from the contact (7100,3180): gate row 1 of cell A and a gate of the next cell north. Follower: north to y 2766, west along y 2766 to x 6947, north to an end at (6949,2677) (not looked at) |
| `tc1_m7100` | P | x 6975, y 3170-3190, going west | out of this wire | the row from the contact (7100,3180) goes on west across the column under the thin metal x 6941-6956 (a gate of the next cell north, not drawn) |
| `tc1_o3740` | M | x 6941-6956, y 3405, going north | out | NOR(`tc1_p3698`, `tc1_x1_u`); it passes over the columns, boxes and fingers of cells B, A and C without contact (Ambiguity 18) and has a contact at (6948,2977) (run 9); drawn to there. What the contact joins, and whether the metal goes on north, is open (Ambiguity 20) |
| `vss` | M | rail x 6858-6906 at y 2985 (run 9); x 6861-6932 at y 3905; x 6858-6908 at y 4380 (it narrows at y 4238) | | goes on both ways, not followed |
| `vcc` | M | rail x 6690-6748 at y 3990 and y 4228 | | the same; `tcw` draws it at y 3440-3900 |

South side, in the channel (tc2), west to east:

| Name | Layer | Where it crosses | Dir | What |
|---|---|---|---|---|
| `tc1_o3527` | M | x 7003-7023, y 4450 | out | NOR(`tc1_o3353`, `tc1_o3095`), cell B's output, from the contact (7011,3852); south of y 4450 it turns west along y 4465-4495 to a contact at about (6965,4480) (seen, not drawn) |
| `tc1_x1` | M | x 7049-7068, y 4450 | ? | from contact (7056,4352) |
| `tc1_g` | P | x 7134-7153, y 4450 | **in** (believed: every other end of `g` is a gate) | from contact (7315,4395) |
| `tc1_i` | P | x 7179-7196, y 4450 | **in** (its only other end) | from contact (7270,4437) |

North side:

| Name | Layer | Where it crosses | Dir | What |
|---|---|---|---|---|
| `vss` | M | right rail x 7771-7819, drawn y 3000-4000; it continues north through the top bus field (the bus lines cross it in poly) | | |

Seen while following these, **not mine and not drawn**: `r8_b5_q` (poly from the
datapath at y 3017-3040) turns north at x 8047-8072 and west again along y 2930-2950; it
passes 15 px from the `tc1_a` contact pad at (8010,3028) **without touching it** (field
gap at x 8030-8046, measured with `tc1_px.py row 3029`). `r8_b4_q` (poly, y 2978-2993)
turns north at x 8094-8112 up to y 2893 and west along y 2893-2907; two more polys of
the same kind (y 2850-2864 down x 8134-8152 to y 2935-2950; y 2805-2821 down
x 8181-8202 to y 2893-2908) nest round it: they are the row A outputs fanning out west
into the top bus field, all under ns1..ns6 without contact (1.4x view only).
A large C-shaped **poly** at x 8307-8360, y 3907-4062 (orange in the metal shot; at 1x
it looks like metal) lies between ns6's south end and `ras_shift`'s contact (8313,4090)
and touches neither (field at y 3896-3908 and 4056-4070, measured).

## Ambiguities

1. **Rails.** VSS/VCC of the island assigned from load orientation only (see
   Inventory). Would be settled by following the centre rail's bus (y 4193-4257) east.
2. **Diffusion column right of the right rail joins the pads under it** (R1's source
   pad to R2's column at 7826-7832 x 3256-3280; R2's lower source at 7826-7832 x
   3390-3410). The joins lie under the rail's edge line, so they cannot be seen
   directly; no gap shows in `tc1_px.py row 3270` / `row 3400` and the circuit needs
   them. Working assumption: joined.
3. **R5's gate tie.** The load's stem goes up to a buried-contact box (7673-7702 x
   3767-3802); a 10 px light strip between two dark lines runs from the box down
   x 7705-7719 to the output region. Read as a narrow diffusion wire (its colour in
   `acid` is diffusion-like). If it were field the load gate would float, so the
   reading is safe, but the strip is at the limit of the photos.
4. **Strips between the series gates of R5** (y 3779-3794 and y 3907-3921): in the open
   they look like thin outlined bands, which could be taken for two more poly lines.
   Under the rail the same y is plain diffusion (tan), so they are the series nodes.

5. **L2/L3 diffusion right of the left rail** is drawn as one rectangle 7478-7547 x
   3290-3830 that the L-shaped gates cut into drains and source strips. The strips
   between one gate's arm and the next (y 3290-3306, 3539-3562, 3801-3830) are 16-29 px
   tall and were seen at 2x only. They are all VSS either way; only W is affected.
6. **Poly under metal W1** (x 7183-7200, y 3104-3235, part of `ras_shift`) runs lengthwise
   under W1 for 130 px. No contact ring is visible on W1 there at 2.4x; assumed none.
7. Crossings of the west-going poly bands under W1-W4 were judged at 2.25-2.4x: a
   contact shows there as a 30 px dark ring and a pad with a green dot in `acid1b`;
   every band has exactly one, at its end.

8. **Bump on `g`'s poly** at x 7007-7031, y 3976-4000, directly under the channel metal
   x 7001-7023. It looks like half a contact pad. Profiles along x 7012 show unbroken
   bright metal in both metal shots and plain salmon poly in `acid1b`, where a real
   contact 90 px away (7099,3897) shows a 12 px bright dot inside a thick dark ring and a
   green-tan patch. Working assumption: no contact.
9. **Direction of `b`, `g`, `i`.** "In" for these rests on every other end being a gate
   or (for `g`) a gate in the untraced structure at x 6750-6940. If tc2 finds no driver
   on the polys at (7512,4450), (7143,4450), (7187,4450), look again at that structure.
10. **ns lines' polys east of x 8250** were drawn from 1.4-1.9x views only as far as
   x 8350; what they meet there is outside this block.
11. The supplies of the gate columns (rails x 6682-6757 and x 6857-6932 near y 4000) are
   **not identified**: nothing traced ties them to the island's rails. Run 3 labels them
   `vcc` and `vss` from the driver's load (see "The driver gated by `tc1_g`").

12. **Thin metal x 6817 over the strip that joins the ring's two U's** (x 6804-6840,
   y 4082-4164). Both metal shots are dark there for 80 px, with one small bright spot at
   (6816-6819, 4118-4127); run 2 read it as the ring's contact. Readings: (a) a contact of
   the thin metal on the poly strip, so the thin metal is `tc1_x1`; (b) a contact on the
   narrow diffusion column beside the strip, so it is the output; (c) no contact: the
   strip's west edge line lies lengthwise under a 12 px metal and darkens it (trap 3).
   Measured (`tools/tc1_hex.py 6795 4070 6858 4172`): the clean shot is protected tan at
   x 6801-6812 all along (so the metal is continuous above); the strip is salmon with a
   green rim on all four sides and **no green hole inside it**, where the two known pad
   contacts of `tcw` ((6318,3740), (6400,3788)) each show a 12 px green hole inside the
   salmon and a 40 px dark ring with a 12 px bright centre in both metal shots; the narrow
   column shows no pits. Working assumption: (c), **no contact drawn**; the ring is fed
   from the east in any case. Review round 1 agrees (the strip reads red over green,
   200/135/122, where the pads of real contacts read green over red) and explains the
   bright spot: the island's neck passes under the strip there (now a `?D`). Would be
   settled for good by the thin metal's other ends (y 3496 and y 4379).
13. **Thin metal x 6968 over the output's buried-contact box** (y 4033-4068). Both metal
   shots are dark for 35 px with no ring and no bright centre; the clean shot under it is
   dull olive (148/142/104) where the same metal over the column further up leaves bright
   tan. Readings: (a) the metal is cut there and each piece ends on the output's diffusion
   (a contact at each end, or one hole over the box); (b) one metal passing over, darkened
   by the box's outlines. In (a) the thin metal is `tc1_o4020`. **No contact drawn**, the metal drawn as one piece.
   After review round 1 this metal is `tc1_x1` (its contact on the pad (6962,4268)), which
   is an input of the gate whose output node lies under the box: a contact here would
   short the gate's input to its output, so reading (a) is out unless the pad's join is
   wrong. The reviewer could not prove either reading from the photos (no bright centre,
   no pad, the hue of the dark stretch metal-like).
14. **The strip as a gate.** Review round 1 reads the island's neck as running west across
   the gap and under the strip x 6820-6838 (y 4108-4130) to the column: drawn `?D`. One
   more gate of `tc1_x1` between island and output; same nets either way.
15. **One rail contact on the island** is drawn (pits at y 4118-4158 in the clean shot).
   Chip 1's metal shot also shows a dark dot at (6898,4088), where the clean shot is plain:
   not drawn. Review round 1: a blemish of chip 1.
16. **A poly or edge along y 3920-3930** above the strip over `tc1_g`'s west arm (text
   map: salmon/pink at x 6798-6831, y 3925-3928). Not identified; it bounds this piece on
   the north.
17. **Is the inverter `tc1_o4280` on the `tc1_x1` line?** (Open; one join deliberately not
   drawn.) Three joins are involved:
   - J1, **not drawn**: the inverter's output strip to the pad (6962,4268), at x 6934-6957.
     For: the strip runs straight at the pad and has no other destination; the review of
     run 4 saw the pad's contact ring (6957-6976, 4258-4290) hold two pale patches split by
     a dark line at y 4276-4278, the lower with the strip's colour in the chip-2 stripped
     shot (171/140/87 against 171/133/88 on the strip), i.e. poly ending at y 4277 and the
     strip's diffusion under the same contact: a butting contact. Against: an etch line at
     x 6951-6957 hides the strip between its open stretch and the ring; not proven.
   - J2, drawn `?P`: `tc1_x1`'s branch poly into the pad at (6972-7000, 4254-4272). For: the
     branch runs 300 px to end exactly there; two reviewers measured the gap as poly
     (orange in three shots). Against: the gap is a dark bar in the clean shot.
   - J3, `shm`'s `?B`: its inverter of `ras_o0_sel1` onto the `tc1_x1` poly at about
     (8370-8410, 4240-4270). Not looked at here.
   If all three hold, the line has two complete inverters on it (low if either input is
   high): possible, but nothing else traced is built so. If J3 is the wrong one, `tc1_x1` =
   NOT `tc1_p4308` and `shm`'s inverter drives something else. If J1 or J2 is wrong, the
   inverter here (with the thin metal x 6968, if J2 is the wrong one) is another net.
   **No reading adopted. J1 is left out of the trace so that no existing equation changes
   on a guess.** Would be settled by: a look at J3 in the clean shot; the thin metal
   x 6968's other ends (y 3806, y 4402); `tc1_p4308`'s source.

18. **The thin metals over cell B's two buried contacts** (run 7). `tc1_m6817` over the
   ladder (6808-6838, 3458-3500) and the thin metal x 6948 (`tc1_o3740`) over the middle
   node's box (6940-6970, 3510-3546) are both dark for about 40 px in both metal shots, as
   in Ambiguities 12 and 13. Readings: (a) no metal contact, the metal passes over a buried
   contact (drawn); (b) a metal contact, which would put the metal on cell B's output.
   For (a): the clean shot is protected tan under both (metal present), with no green hole
   and no pits; neither has the single 12 px bright centre in a 40 px ring that the pad
   contacts 100 px away show; the box under x 6948 is a textbook buried contact; cell A has
   the same two dark stretches over its own ladder and box, so (b) at all four would short
   cell A's output to cell B's, and cell B's gate row 1 is cell A's output; (b) on the
   x 6948 metal would also short `tc1_o3740` to both. For (b): nothing but the darkness; the
   follower stops at each. **(a) adopted.** Would be settled by either metal's far end
   (`tc1_m6817` north of y 3300; south of y 4530).
   Run 8: cell A has the same two stretches (`tc1_m6817` over its stub and arm, y 3374-3422;
   the thin metal x 6948 over its box, y 3338-3371) and is drawn the same way. Over cell A's
   arm `tc1_m6817` is brighter at its east edge than over cell B's (B-D against 8-A of 16, in
   both chips), still without a green hole in the clean shot. If (b) held at cell A's stub,
   `tc1_m6817` would be `tc1_o3353`.
   Run 9: cell C has the same pair (`tc1_m6817` over its stub and arm, y 3024-3084; the thin
   metal over its box, y 3077-3113), drawn the same way. Three cells with a dark stretch of
   `tc1_m6817` over each gate tie: if they were contacts, three outputs would be one net.
19. **Cell C's strip and bottom band: diffusion or poly?** (run 9). The strip x 6818-6836,
   y 3100-3224 and the band y 3206-3222 under the rail read 203/158/119 and 205/155/137 in
   the clean shot at some samples (red minus green 45-50), between protected diffusion
   (18-35) and poly over field (50-70); `tools/railprof.py` calls the strip "poly over
   field" and the band "diffusion". Drawn as diffusion: the centre of the strip at y 3160
   reads 206/169/141, exactly as the band y 3085-3103; the outline of strip, band and the
   column's bottom region is one line with no box at either end in both metal shots; and a
   poly could not join the column's diffusion without a buried contact. If it were poly from
   the load's gate tie with a hidden buried contact at the column, the bottom region would
   still be the output node (the load's gate is the output): the equation does not change.
   The review of run 9 measured strip and both bands as diffusion (203/165/139, 209/166/138
   against poly over field 225/165/118) and the corner as one shape.
20. **What drives cell C's gate row 1, and where `tc1_o3740`'s thin metal ends** (run 9;
   open, nothing joined). At (6925-7010, 2935-2990): the poly `tc1_p3051` ends on a box
   (6936-6974, 2944-2970) that looks like a buried contact onto the east end of a diffusion
   band y 2940-2961 with what looks like a load at its west end; the thin metal has a contact
   (6948,2977) adjoining the box's bottom outline; a metal y 2933-2948 arrives from the east directly
   above. Readings: (a) box and contact are on one diffusion, so `tc1_p3051`, `tc1_o3740` and
   the band are one net (then `tc1_o3740` has two loads, or the "load" is something else);
   (b) the contact is on a separate patch and the thin metal carries `tc1_o3740` on north
   and east along the metal y 2933-2948 to (7055,2806), while `tc1_p3051` is the output of
   the cell whose load the band belongs to; (c) other. Not readable at 9x in four shots.
   Would be settled by tracing the next piece north (the band's west end and its pull-downs)
   and by a profile of the metals between y 2940 and y 2975 against a known stretch.

## Review

Independent review of run 3 (workflow step 6): one fresh agent per round, briefed with the
claims and the places most likely to be wrong, told to find errors from the photos.

**Round 1** (2026-11-17 09:19 -0600). Told to suspect: the two dark stretches on the thin metals x 6817 and
x 6968; the buried contact of the output and its node across the east gap; the rail
contacts and a possible second one on the island; the ring's closure; the poly route in the
top bus field with its "no contact under the bus metal y 2684" and the 10 px gap at
(7438-7449, 2640); the cross-under at the VSS rail and the two long channel metals, which had
been read from text only. It looked at 30-odd views at 3.4-7x in two to four shots
(`cache/scratch/tc1/review-1/`), ran row profiles, text maps and the follower.

| Finding | Outcome |
|---|---|
| 1. An undrawn branch of the ring poly at (6990-7046, 4122-4270): the block's top runs on east, south and west | **Confirmed** (my views `f1.png`, `f2.png`, `f3.png`, overlay `f4.png`). Drawn; followed to its end, a pad under the thin metal x 6968 with a contact, which makes that metal `tc1_x1` (through one `?P`: `tc1_x1_u`) |
| 2. No contact of the thin metal x 6817 on the strip; the island's neck probably passes under the strip (an undrawn gate segment) | No-contact reading **agrees** with the trace. The neck **adopted as `?D`** (same nets, more width) |
| 3. Geometry: `tc1_g`'s north arm is x 6834-6862, the upper U's right leg reaches x 6950, the load block reaches y 4118, the west gap at y 4032-4078 is diffusion | **Confirmed** by row profiles (arm orange in the gap at x 6842-6850; gap red at y 4045-4075; block's edge at y 4105-4115) and drawn: arm 6836-6862, leg to 6944 (kept 4 px clear of the east column), block to y 4110, gap diffusion y 4014-4083 |

Checked and found correct by the reviewer: the NOR's topology and the ring's closure; the
lower bar continuous into the block; the east-gap join at y 4014-4032 (both metal shots
flat across it); both rail contacts and the rail being one piece; the load, stem and tie
box; the six contacts of the output route; both poly corners; no contact under the bus
metal y 2684; the gap at (7438-7449, 2640) being field (7x); the cross-under at the VSS
rail; the metals x 7053 (y 4092-4352) and x 7142 (y 2832-4047) unbroken and untapped.
Could not check: the thin metal x 6968 over the box (Ambiguity 13); the output poly across
the 6 px open gap at (6984-6990, 4047), which rests on the box's nested outlines. Tool
note from the reviewer: `follow.py` at its default gap stops on both thin metals at the
dark stretches, so their end-to-end figures in the Ports table are two runs each.

**Round 2** (2026-11-17 09:43 -0600; started before the workflow changed to "one full review, then fix
checks": it was briefed with the whole piece again, pointed hardest at the branch added
after round 1, the redrawn widths and anything left out, and told not to read this
section). About 30 views at 3-7x in two to four shots (`cache/scratch/tc1/review-2/`), row
profiles, text maps, the follower.

| Finding | Outcome |
|---|---|
| 1. The pad (6962,4268) is joined from the west by a diffusion strip y 4270-4292 that runs under the rail, where it is one side of a transistor (gate poly y 4297-4318, a rail contact at about (6885,4340) on the other side) | **Confirmed** (my views `h1.png`-`h4.png`, a row profile at y 4280, overlay `h5.png`). Drawn: strip, pull-down, rail contact, the gate poly `tc1_p4308`; the strip's join to the pad `?B`. It makes the extraction's `tc1_x1` a NOR: Ambiguity 17 |
| 2. The lower U's left leg starts at x 6862, not 6850, and the diffusion west of it is real | **Confirmed** by row profiles at y 4165 and 4190; redrawn, diffusion added (width only) |
| 3. The diffusion under `tc1_g`'s west arm reaches x 6786 | **Adopted as `?D`** (a row profile at y 3972 agrees; width only) |
| 4. The channel metal x 7003-7023 is not drawn | True; it has no contact here. Left in Not done with the reviewer's check |
| 5. The second poly on y 2628-2648 turns north at x 7415-7438 instead of stopping; still not joined to the pad (7465,2640) | Notes corrected; nothing drawn changes |

Checked and found correct: the `?P` into the pad (orange in the gap in three shots); the
branch across its first gap and round both corners, unbroken and unbranched; `tc1_g`'s
band, the north arm, the foot and the lower bar across the gaps; all six contacts of the
output route; the metal x 7142 untapped from y 2850 to y 4045; no contact under the bus
metal y 2684; the cross-under at the VSS rail; the load. Could not check: either thin
metal over its dark stretch (Ambiguities 12, 13 stay open); whether the pad's interior is
poly or diffusion.

**Round 3** (2026-11-17 09:56 -0600; a fix check of the changes since commit `18544c5`, 15-odd views in
`cache/scratch/tc1/review-3/`, row profiles, the extraction before and after). **No finding
changes a connection**, and the netlist differs from the earlier one only as intended. But
the round is not clean: three findings, all confirmed by my own row profiles and text map,
all fixed.

| Finding | Outcome |
|---|---|
| 1. The rail is drawn 72 px wide to y 4380; south of y 4238 it is x 6858-6908 | **Confirmed** (bare ground from x 6916 at y 4250, 4309, 4345 in both metal shots). Redrawn as two pieces; the contact (6888,4338) is inside the narrow one |
| 2. The pull-down's gate and source diffusion are x 6876-6914, not 6862-6918 (W about 40, not 56) | **Confirmed** (edge at x 6874, field at x 6858-6866 at y 4345). Redrawn: W 37 |
| 3. `tc1_p4308` does not come from the east: it turns south at x 6985-7000 | **Confirmed** (clean shot: salmon at x 6988-7000 from y 4322 to y 4382). Drawn to y 4384; notes and port corrected |

Checked and found correct by the reviewer: the ring's closure round the redrawn leg (the
lower foot's poly continuous over x 6842-6884); the gate crossing its whole diffusion; no
contact of the rail on the strip; the strip separate from the band above it; the source
contact; both gap `?D` diffusion-coloured in the chip-2 shots; the `?B` and the west-arm `?D`
rightly uncertain.

**The review is not closed.** Three rounds are the workflow's limit and the third had
confirmed findings, so run 3 was **not merged**. The three fixes above have not been seen by
a reviewer. The next run's full review must cover them together with whatever it adds.

### Run 4's review (a new cycle: full review, then fix checks)

**Round 1** (2026-11-17 10:19 -0600; full review of the inverter at x 6688-7002, y 4225-4384, which includes
the three fixes of run 3's round 3; 12 views at 4-7x in up to four shots in
`cache/scratch/tc1/review-4/`, text maps, profiles; told to suspect the load block being
three polys, the gate tie, the supply contact, the diffusion under the thin metal x 6817,
and the recent fixes).

| Finding | Outcome |
|---|---|
| 1. The pad's contact ring is larger than drawn (6957-6976, 4258-4290) and holds two patches; the lower has the strip's colour: probably a butting contact joining metal, poly and strip. Not proven | **Undecidable**; it is evidence for the join J1 of Ambiguity 17, recorded there. The join was `?B` when reviewed; **it has since been removed from the trace** (not because of this finding: because, with `shm`'s inverter on the same line, I think one of three joins is wrong and will not let a guess change `tc1_x1`'s equation) |
| 2. The thin metal x 6817 is not drawn south of y 4228 and does not end at (6809,4379): it turns west at y 4366-4380 | **Confirmed** (my text map of y 4290-4400 shows the same). Drawn to (6790,4373); the notes' port corrected. (The "turn west" is a jog: see round 2) |
| 3. The supply rail is drawn only to y 4330 and runs on | Not an error: drawn as far as traced, a port in the table |

Checked and found correct: the rail's narrowing and its contact; no ring or pit on the
strip; the channel x 6875-6914; the gate poly's west end at x 6855 over field, its turn
south, and its being separate from the branch poly; the west gap diffusion-coloured at
y 4280 and field at y 4255 and 4304; the column ending at y 4337 with nothing on it; the
load block being one block with the strip under it from pad to column (matched against the
pilot load); the supply contact; the gate-tie box (matched against the pilot buried
contact) with the foot reaching it; the strip separate from the driver's band. Could not
check: the thin metal x 6968 across y 4277-4297; `tc1_p4308` south of y 4390.

**Round 2** (2026-11-17 10:26 -0600; a fix check of the changes since commit `0833b4a`: the thin metal x 6817
drawn on south, the `?B` and its alias removed; views `turn.png`, `south.png` in
`cache/scratch/tc1/review-5/`, text maps, the extraction before and after).

| Finding | Outcome |
|---|---|
| 1. The thin metal x 6817 does not turn west at y 4366-4380: that is a foot, a 20 px jog, and the line goes on south at x 6788-6806. The drawn stub lies inside the foot, so no connection is wrong, but the description is | **Confirmed** (my text map of y 4290-4400: bare ground at x 6790-6808, y 4380-4389, bright metal again at x 6790-6799 from y 4392 in both chips). Redrawn as the line to y 4372 and the foot as a rectangle; comment, port and notes corrected |

Otherwise no findings: y 4228-4366 of that metal is one piece with no ring and no hole; the
new metal touches no other; with the `?B` gone the strip's `?D` clears the pad's poly by
6 px and the gate poly by 5 px and overlaps no poly; the netlist differs only as intended.

**Round 3** (2026-11-17 10:29 -0600; a fix check of the one change since commit `9eaf935`, the thin metal
x 6817's foot: a text map at 2 px, one view `cache/scratch/tc1/review-6/foot.png`, the
extraction before and after, alone and with every file loaded). It checked that the foot
(6788-6826, 4366-4380) is right in both metal shots and joined to the line from the north,
that nothing drawn comes within 24 px of it and no contact lies under it, that the metal does
go on south from it at x 6790-6802, and that no net or transistor changed.

Round 3: no findings.

### Run 5's review

**Round 1** (2026-11-17 10:52 -0600; full review of the piece at x 6750-7008, y 4298-4450: eight views at
4-6.5x in two to four shots in `cache/scratch/tc1/review-7/`, text maps, the follower,
`tools/railprof.py`, the extraction alone and with every file; told to suspect the vertical
poly's continuity and its turn, the row-to-pad gap, the contact (6947,4396), contacts and
channels under each of the three metals, and a third row).

| Finding | Outcome |
|---|---|
| 1. The thin metal x 6968's south end is not a diagonal: the line runs straight on to y 4404 at x 6964-6980 and a foot spreads west over the pad | **Confirmed** (my text map: chip 1 bright at x 6974-6978 at y 4392-4400). Redrawn as the line to y 4404 and the foot (6938-6980, 4386-4406). Same connection |
| 2. The rail x 6858-6908 widens west to about x 6836 from y 4438 south, over the lower row, with no contact | Not an error of the trace: the rail is drawn to y 4380 only and is listed as going on. Noted here for whoever draws it further |

Checked and found correct: the vertical poly x 6988-7006 continuous from y 4320 to y 4448
(orange in both metal shots) and turning west only; the contact (6947,4396) (ring and
bright centre in both chips, green hole); the row-to-pad gap being poly in three shots; the
pad's poly going nowhere else; no contact of either row to any of the three metals, none of
the thin metal on the gate poly; no diffusion under or between the rows; no third row; the
two nets separate in the extraction. Could not check: the thin metal x 6968 across
y 4276-4298 (dark in both chips; unbroken is inferred); the supply-rail crossing other than
by text map; anything west of x 6750.

**Round 2** (2026-11-17 10:58 -0600; a fix check of the one change since commit `b44998b`, the thin metal
x 6968's south end: per-pixel profiles of both metal shots, an 8x view and a text map in
`cache/scratch/tc1/review-8/`, the extraction before and after, alone and with every file).
It checked the line's last stretch (lit at x 6970-6979, ending at y 4404-4405 in both
chips), the foot (a metal stripe at x 6957-6965, y 4382-4409, and the contact's centre at
(6940-6952, 4390-4402), one piece with the line: the dark line between them is the pad's
east edge), that no other drawn metal is within 30 px, and that no net or transistor
changed.

Round 2: no findings.

### Run 6's review

**Round 1** (2026-11-17 11:32 -0600; full review of the second driver, x 6690-7035, y 3600-3900: about 25
views at 4-7x in `cache/scratch/tc1/review-9/`, the follower, text maps, `tools/railprof.py`,
row and column profiles; told to suspect the owner of the contact (7009,3789) and the three
contacts at x 7010, gate 1's far end, the open diffusions east of the rail, the legs, the
load). **The NOR holds; one routing error, three width errors, one omission**, all confirmed
by my own profiles and the follower, all fixed.

| Finding | Outcome |
|---|---|
| 1. The output's metal does not go straight north along x 7010: from the contact it goes north to y 3650, west along y 3653-3665, north along x 6941-6956 | **Confirmed** (follower: corners (7004,3660), (6946,3651)). Redrawn. It changes the output's port, and removes the supposed link to run 2's metal from (7010,3092) |
| 2. The undrawn "closed box" is the top contact region continuing east; gate 1's band is over diffusion there. Gate 2 likewise is one channel from the leg to the east column | **Confirmed** (row y 3645: no edge at x 6914-6930 in the metal shot, diffusion colour in the chip-2 stripped shot; band's end at x 6986). Drawn: width only |
| 3. Both arms are channels where they cross the column under the thin metal x 6817, and no diffusion was drawn under them | **Confirmed** (`tools/railprof.py` had said GATE at y 3649-3665 and 3857-3882 in my own survey). The column drawn end to end: two more channel segments on the same nets |
| 4. The legs are x 6824-6849, not 6823-6836 | **Confirmed** (rows y 3680 and y 3830: orange to x 6845-6848 in three shots). Redrawn |
| 5. A poly row at y 3606-3626, x 6915-6968, not drawn and not listed | Confirmed at the time from a text map, **withdrawn in round 2**: it is a field slot (see round 2). Nothing was drawn for it |

Checked and found correct: the contact (7009,3789) on gate 2's pad, fed from the west by
the thin metal x 6968's arm; the three contacts at x 7010 separate, bare ground between;
both open diffusions being diffusion and separated by gate 2's band; the output's gap
diffusion, buried contact and poly; the vertical poly going on north (to y 3584); the arm's
join to it (the line across the arm at x 6754-6760 is a diffusion edge); no contact on
either thin metal; the load. Not checked: diffusion under the legs and under the load
block; the output's metal north of y 3600; the supply contact (6715,3768) beyond 4.5x.

**Round 2** (2026-11-17 11:50 -0600; fix check of the changes since `a624b5e` only: 9 views in
`cache/scratch/tc1/review-10/`, the follower, extraction before and after, profiles in four
shots). **No connection is wrong**: nets and gates identical before and after the fixes.

| Finding | Outcome |
|---|---|
| 1. Gate 1's arm is wider than drawn: the diffusion west of the column has its edge at x 6755-6758 over y 3627-3686, across the arm, and the ground south of the arm has no edge to the column | **Confirmed** (rows y 3636, 3656, 3678 in both metal shots: dark at x 6756, and red minus green 40 east of it against 18 west). Drawn: the channel is 62 wide, not 20; same nets |
| 2. The "poly row" y 3606-3626 of round 1 is a field slot | **Confirmed** (profile down x 6948). The notes corrected; nothing had been drawn |
| 3. Three lines of the trace file's header comment still gave the old legs and the old route | **Confirmed**; corrected |

Checked and found correct: the output metal's route and corners, with no ring or hole
anywhere on it; the diffusion's east edge at x 6970-6972 crossing gate 1's band; both arms
over diffusion under the thin metal x 6817; the legs continuous into the bands.

**Round 3** (2026-11-17 11:55 -0600; fix check of the one geometry change since `6b214a1`, the diffusion
west of the column at x 6758-6802, y 3627-3690: 7x views in four shots and an overlay in
`cache/scratch/tc1/review-11/`, colour profiles on rows y 3635, 3656, 3679 and 3830, the
chip-1 stripped shot read directly, extraction before and after, `tools/unsure.py`). Checked
and found correct: the west edge at x 6756-6759 over the full height; both bands diffusion
and not poly; no edge between them and the column; the south band, the load's box, the tab
and the column one piece, the neck 6 px clear of the band; the netlist differing only in
that channel's width (20 to 62) on the same nets.

Round 3: no findings.

### Run 7's review

**Round 1** (2026-11-17 12:47 -0600; full review of cell B, x 6690-7160, y 3405-3625, and of its output's
route south to y 4450, by a fresh agent: views at 4-8.5x in two to four shots in
`cache/scratch/tc1/review-12/`, colour profiles, text maps, the extraction and
`tools/unsure.py`). Told to suspect: `tc1_m6817` over the ladder and the thin metal x 6948
over the box (contact, break or neither); the ladder's build; the band under the rail and its
joins across the two gaps; the pad's join to `tc1_p3698`'s vertical poly; the field slot and
the fingers' joins; the column's width; the C-shaped poly and the metal x 7133-7152 over it;
the output poly's run under the metal x 7048-7068 and into its pad; the two pieces of the
channel metal x 7003-7023; the contacts (6887,3606) and (6710,3530); anything left out.

Checked and found correct: no metal contact and no break at either buried contact (the clean
shot is protected tan under both, ladder cells 204/168/130 and box 196/167/122, where the pad
contacts 100 px away read green, 152/173/98; neither metal widens; the darkness is a
lengthwise edge under the metal's centre with half-bright flanks, in both chips). The arm is
y 3462-3480 only and the stub joins the region below it. The band is diffusion under the rail
and in both gaps, with no edge across it at x 6838 or x 6929. The pad's join is poly in the
gap at y 3586-3598 in three shots, field above and below. All three fingers cross the gap
x 6914-6930; both slots are field. The column is x 6928-6968 and both rows cross it. The
C-shaped poly is continuous, with no hole or ring under any of the four channel metals (the
loop at (7150-7165, 3495-3510) is in the chip-1 clean shot only). The output poly has no hole
along its run; the notch at (7048-7056, 3710-3724) is in both metal shots but the poly under
it is uniform and there is no pad. The channel metal's north piece ends at (7011,3571) and its
south piece has no ring or hole from y 3870 to y 4450. All six contacts are real and placed
within 4 px.

Three remarks that change no connection, **not applied to the trace** (so that what is merged
is what was reviewed): the stub's east edge is at about x 6838 (drawn 6834); the south
channel metal steps about 4 px east and narrows to about 14 px near y 4300 (drawn straight,
20 wide); cell A's load block reaches about y 3415 (these notes said 3400: corrected).
Not checked by the reviewer: cell A's end of `tc1_o3353`, the metals north of y 3405, the
contact near (6965,4480).

Round 1: no findings.

### Run 8's review

**Round 1** (2026-11-17 13:08 -0600; full review of cell A and its input route, x 6690-7160, y 3140-3420, by a
fresh agent: twelve views at 4-9x in up to four shots in `cache/scratch/tc1/review-13/`,
colour profiles, text maps, the follower, `tools/railprof.py`, the extraction and
`tools/unsure.py`). Told to suspect: `tc1_m6817` over the stub and arm (contact, break or
neither); the thin metal x 6948 over the finger and over the box; the vertical poly
x 6986-7006 (one piece, its two joins, a contact to the channel metal beside it); the west
ends of both gate rows; the band across the two gaps and the load band at the supply
region; the arm's join to the stub; the finger's join and the column's top; the contact
(7100,3180) and the bare stretch of the metal x 7091-7110; the two rail contacts; anything
left out.

Checked and found correct: the vertical poly is one piece (orange in chip 1 down x 6992
from y 3174 to y 3312, including y 3244; bare ground at y 3156 and y 3330), joins the row
and gate row 1 and ends at both; the channel metal x 7013 beside it is unbroken with no ring
from y 3150 to y 3420 in both chips. The contact (7100,3180) is real, the follower stops at
y 3184 from the north and at y 3392 from the south with bare ground between, and neither
channel metal taps the row. Both gate rows end at about x 6914, with field under the rail;
no third gate. The column starts at y 3285; the finger and the band cross both gaps as
diffusion and the band joins the region under `tc1_m6817`. The thin metal x 6948 has no ring
or hole at the finger or the box (one dark speck at (6947,3288), chip-2 stripped shot only).
`tc1_m6817` over the ladder is neither a contact nor a break (clean shot 209/173/126 there
against 143-180/152-164 at four real contacts, no pits); Ambiguity 18 stands, since only the
green test separates the readings. The stub is continuous with the region and the arm is
orange in the gap at y 3407; the contacts (6890,3276) and (6708,3378) are real and on the
metals claimed.

Two remarks that change no connection, **not applied to the trace** (so that what is merged
is what was reviewed): the supply rail's east edge measures about x 6732-6734 over
y 3336-3402 (drawn 6742; the band still reaches the block); gate row 2 reads y 3386-3406 in
the clean shot (drawn 3388-3403: L nearer 20 than 15).
Not checked by the reviewer: which supply each rail is; anything north of y 3140 (the route
of `tc1_m7100`, the cell north, a follower candidate at (6948,3210)); the contact
(7100,3395) and the C-shaped poly (earlier runs); the exact shape of the arm, stub and
buried contact at (6800-6812, 3378-3400), too blurred at 9x: only the arm-to-stub tie is
supported.

Round 1: no findings.

### Run 9's review

**Round 1** (2026-11-17 13:32 -0600; full review of cell C, x 6690-7080, y 2940-3240, by a fresh agent: ten
views at 3-5x in three shots in `cache/scratch/tc1/review-14/`, profiles, text maps, the
follower, the extraction). Told to suspect: the strip and bottom band (diffusion or poly, one
shape or not); a contact on the bottom region; rail-contact region 2 touching the column
beside gate row 2; the column's continuity and its separation from cell A; the three
contacts and whether each metal ends there; gate row 1's poly and the area
(6925-7010, 2935-2990); `tc1_m6817` over the gate tie; the bands across the gaps, the arm
and the stub; the supply and rail contacts; anything left out.

**No finding changes a drawn connection.** Two findings about what the notes claimed at the
north end, both accepted (I had no measurement that contradicts either):

| Finding | Outcome |
|---|---|
| 1. That the thin metal x 6941-6956 ends at the contact (6948,2977) is not established: north of it both metal shots read as dim as over the output box, where the metal continues; the follower's stop is not evidence. The metal y 2933-2948 does not start at x 6820 (it would cross the rail): the follower takes it from (7056,2850) to an end at (6974,2939), and a dim strip carries it to about x 6940, above the thin metal | **Accepted.** Notes and comments corrected; the metal stays drawn up to the contact only. Ambiguity 20 |
| 2. The "believed" join of gate row 1 to `tc1_o3740` is weaker than the notes said: the poly ends on the box's east outline; the box is the east end of a band that runs west under the rail to what looks like a load of its own. Leaving it unjoined is right, but it should be called open | **Accepted.** The poly renamed from its open-join name (the `_u` form of the second driver's output) to the place name `tc1_p3051`; notes, glossary and comments say "open". No geometry changed |

Checked and found correct: strip and both bands are diffusion and one shape round the corner,
continuous in both gaps; the column is one piece y 3021-3219, all three gates cross it, field
separates it from cell A; no contact at (6948,3210); region 2 touches the column only through
its finger; the contacts (7010,3093) and (7056,3138) are real with bare ground north of each;
both rail contacts and both supply contacts are real; no contact where gate row 2 passes under
the metal x 7003-7023; `tc1_m6817` over the gate tie is neither a contact nor a break; the
stub is continuous and the arm crosses its gap; nothing undrawn in the cell. Not checked:
the rails' supplies; the diffusion under the north cell's poly block; the load band's 4 px
junction at x 6742-6746 (edge line only).

**Round 2** (2026-11-17 13:35 -0600; fix check of the changes since `4738538`, by a fresh agent: views at 4-9x in
four shots and profiles in `cache/scratch/tc1/review-15/`, the diff, the extraction before and
after). Both fixes right: the diff changes only comments and the label's name; the two
extractions are identical apart from that name; the gate of the transistor at (6948,3051) is
a net with no driver and nothing else on it; nothing drawn joins the poly, the box, the
contact's patch and the metal. The poly, its outline at x 6974-6978, the contact and the dim
strip are as described. Three points about wording, none changing geometry or a connection,
all corrected: a garbled comment line in the trace file; the band's continuity across the gap
x 6906-6935 was stated as fact and rests on the metal shots only (the clean shot is dark
there); the contact is not 10 px south of the box but adjoins its bottom outline.

**Round 3** (2026-11-17 13:36 -0600; fix check of the wording changes since `a1848f0`, by a fresh agent: the
diff, the extraction before and after, profiles and views in `cache/scratch/tc1/review-16/`).
The diff touches comments only and the extraction is byte-identical. The three corrected
statements hold: the box at the east end of the tan band with its east outline at
x 6972-6976; the gap dark in the clean shot (at x 6914-6932) with a plain strip between two
edge lines in both metal shots; the contact's hole and bright centre at y 2976-2980 against
the box's outline at y 2970-2974.

Round 3: no findings.

## Not done

- **Gate columns x 6400-7000, y 2650-4450**: nothing drawn. Dense random logic with large
  devices under wide rails (x 6510-6560, 6682-6757, 6857-6932 near y 4000) and thin
  verticals between (x 6745-6762, 6766-6785, 6808-6828, 6913-6932, 6938-6955, 6959-6977).
  It is not built like the island: budget for 3x views and profiles, not 2x.
- The second driver is traced (run 6). Left there: the structure at (6745-6800, 3810-3900).
- Cells B, A and C are traced (runs 7-9). Left there: Ambiguities 18 and 19, and the north
  ends of the thin metal x 6765-6785 = `tc1_p3698` and of `tc1_m6817` (both drawn to
  y 3000), and of `tc1_m7100` (to y 3140; the follower ends it at (6949,2677) in the top bus
  field). **First for the next run: Ambiguity 20**, the source of `tc1_p3051`: the box
  (6936-6974, 2944-2970) beside the contact (6948,2977), the tan band west of it along
  y 2940-2961 (to a region (6800-6835, 2940-2970) and a poly block (6755-6797, 2940-2980))
  and the metal y 2933-2948 over it. It belongs to **the next piece north, y 2850-2990** on
  the same rail (a supply contact region (6680-6742, 2970-3025), a rail contact at about
  (6885,2880)): not surveyed.
- The driver gated by `tc1_g` is traced (run 3). Left there: Ambiguities 12 and 13 (the
  two thin metals over it), and the far ends of its ports: `tc1_o4020` east of x 8350 on
  the bus line y 2641 (follower: ends at (9098,2639)), `tc1_x1`'s metal north of y 4060
  (its top end at (7054,3134); the "ring" at about (7055,3730) is not a contact: see the
  section "The second driver"), `tc1_m6817`, the thin metal x 6968
  (`tc1_x1_u`: its ends at y 3806 and y 4402 and any other contact; the pad (6962,4268)'s
  west side, now drawn as the strip), both rails. **First for the next run**: the strip's
  node is done (run 4: an inverter); its input and the thin metal x 6968's south end are
  followed to this package's west edge (run 5). Left: the thin metal x 6968's north end
  (a pad at (6958-6998, 3778-3797) on a poly y 3775-3795: contact not decided); the pad at
  about (6972,4482); Ambiguity 17 from `shm`'s side (its `?B` at about (8370-8410,
  4240-4270)). West of x 6750 both rows belong to `tcw`'s region. The poly along y 2628-2648 that stops at (7438,2640), and the vertical poly
  x 7160-7180 it comes from. Run 2's observation that `sel_tracks.py` reports false breaks
  on ns3 and ns5 (chip 2 has blemishes, chip 1 does not) still stands.
- **Channel x 7000-7170**: all four verticals are drawn to their ends south of y 3085
  (run 9: x 7003-7023 = `tc1_o3095` from the contact (7010,3093); x 7048-7068 = `tc1_x1`
  from the contact (7056,3138)), except `tc1_m7100` (x 7091-7110), which goes on north of
  y 3140 into the top bus field, and `tc1_o4020` (drawn). North of y 3085 the channel is
  bare ground as far as y 3070 (text map); above that not looked at.
- **Top bus field y 2500-2975**: seven bus lines (y 2554, 2598, 2641, 2684, 2727, 2771,
  2814), each crossing the right VSS rail in poly between contacts at x 7663 or 7707 and
  x 7858 or 7902 (alternating). Only the y 2727 (ns2) and y 2771 (`w1`) lines are drawn.
  The y 2814 line's poly runs on east from contact (7707,2811) without a second contact
  in view. The row A outputs of cdp1 fan out west into it (see Ports).
- Far ends of ns3..ns6 and of ns2's west poly; `tc1_x1`, `db_b6` (all in the Ports table).
