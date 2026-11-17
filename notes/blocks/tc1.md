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
overlay-checked and extracting (34 transistors in all, no errors, no warnings): **the
driver gated by `tc1_g`** at x 6700-7160, y 3920-4225, with its load, its supply contacts
and its wiring into the channel: `tc1_o4020` = NOR(`tc1_g`, `tc1_x1`), and **the output's
route** up the channel and into the top bus field, where it becomes the bus line y 2641
and leaves east over the datapath. See "The driver gated by `tc1_g`".

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
wraps the drain; load 60/37). Eight transistors. Views in `cache/scratch/tc1/`: `g1.png`
... `g11.png`, the class map `cm1.png`, overlays `ov1.png` ... `ov4.png`; text maps by
`tools/tc1_hex.py` (new: a rectangle as three character maps, the two metal shots and the
clean shot; its docstring gives what a real contact measures).

**What is there.** One diffusion lies under the rail x 6861-6932 and spills out on both
sides, under two thin metals that only pass over it (x 6817 and x 6968). Two polys cut it:

| Poly | Shape | Separates |
|---|---|---|
| `tc1_g` | the band y 3992-4014, which the earlier runs drew from the east as far as x 6960, runs on west under the thin metal x 6968 and under the rail; at x 6850-6862 it turns north to y 3943 and then west along y 3943-3961, across the diffusion column under the thin metal x 6817, ending at x 6772 | region A (x 6858-6936, y 3925-3992, **rail contact (6897,3958)**, with its strips under both thin metals) from the output node |
| `tc1_x1` | a ring round an island (x 6884-6936, y 4057-4178, **rail contact (6902,4136)**): an upper U (bar y 4035-4057, legs x 6862-6884 and x 6920-6934) and a lower U (leg x 6850-6884, bar y 4178-4202, east leg the block x 6950-6990, y 4123-4202), joined west of the rail by a vertical strip x 6820-6838, y 4083-4160 into which a foot of each U runs. The upper U's right foot runs east along y 4078-4100, over the diffusion column under the thin metal x 6968, to a pad with a **contact (7054,4092)** on the channel metal x 7053 | the island from the output node |

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

**Sizes** (W/L in px, from the drawn rectangles): `tc1_g` 104/18 under the rail (band
plus north arm), 37/18 at the west arm, 42/19 on the east column; `tc1_x1` 169/20 (upper
U), 102/31 (lower U under the rail), 95/27 (east leg and bar), 40/22 (the foot on the east
column); load 60/37. The lower U's left leg is drawn over the diffusion's west edge, so
its share of W is uncertain; the connections do not depend on it.

**How each join was decided.**

| Join | Evidence |
|---|---|
| Output strip (y 4014-4032) to the west column, across the gap between the thin metal x 6817 and the rail | the clean shot in the gap is red (90-136 / 65-75 / 62-78) where the same gap over field is khaki (86-137 / 85-141 / 46-93, y 4240); run 2 measured the same |
| Band y 4203-4222 to the west column, across the same gap | red in the gap at y 4212 (93-150 / 71-131); in the metal shot the band's two edges cross the gap |
| Band y 4203-4222 across the east gap | red in the gap at y 4212 (94-151 / 68-100) |
| Output strip to the east column (y 4014-4032), **`?D`** | the gap is a dark bar in the clean shot (trap 2) and measures neutral; in the metal shot the gap is plain there and an edge curves round below it (y 4032-4075). The east column's part between the two gates has no other neighbour that could supply its load |
| Island to the east column (y 4104-4120), **`?D`** | dark bar; in the metal shot an edge crosses the gap at y 4120 and none above it |
| Region A to the strip above `tc1_g`'s west arm and to the east column's top, both **`?D`** | dark bars; one outline in the metal shot |
| Buried contact of the output on the east column | a box with nested outlines at the poly's west end in both stripped shots, pale inside, no pits; the poly ends there (text map: no poly across the column at y 4036-4056) |
| Contacts (7054,4092), (7099,4047) | ring and bright centre in both metal shots, green hole inside the pad in the clean shot |

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
x 7370, in the open from there) and stops at x 7438. Between its end and the pad's ring
the clean shot is bright green (114/166/77 and 129/152/94 at x 7443-7446, y 2634-2646:
open field) for about 8 px, and the chip-2 stripped shot shows the poly's end edge at
x 7437-7440. Two nets. What that poly does at its end is not looked at (a tan band lies
under it at y 2652-2668).

`tools/unsure.py`-style statement: with the four `?D` deleted, the NOR and its load still
extract on the west column and under the rail, but the output loses its way out (the
buried contact is on the east column). So **the equation is firm; that `tc1_o4020` is the
net on the channel metal x 7142 is marked**.

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
| `tc1_x1` | M | x 7047-7061, y 4060, going north | in | the channel metal x 7053 runs on north of the driver's contact; the follower gives its end at (7054,3134) (run 2 saw a contact (7056,3138) there) and candidates at (7058,3745), (7057,3717): not looked at |
| `tc1_m6817` | M | x 6811-6823, y 3905 and y 4228 | ? | thin metal over the driver's west column, no contact drawn (Ambiguity 12). Follower: from (6822,3496) to (6809,4379), candidates (6818,3883), (6813,3754), (6818,4309); the two at (6820,3977) and (6817,4211) are not contacts (text maps: unbroken metal, no ring) |
| `tc1_m6968` | M | x 6962-6974, y 3905 and y 4228 | ? | thin metal over the driver's east column (Ambiguity 13). Follower: from (6966,3806) to (6975,4402), candidates (6970,3947), (6972,4218): not looked at |
| `vss` | M | rail x 6861-6932 at y 3905 and y 4228 | | goes on both ways, not followed |
| `vcc` | M | rail x 6690-6748 at y 3990 and y 4228 | | the same; `tcw` draws it at y 3440-3900 |

South side, in the channel (tc2), west to east:

| Name | Layer | Where it crosses | Dir | What |
|---|---|---|---|---|
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
   from the east in any case. Would be settled by the thin metal's other ends (y 3496 and
   y 4379): if they are gates only, (a) costs nothing to add.
13. **Thin metal x 6968 over the output's buried-contact box** (y 4033-4068). Both metal
   shots are dark for 35 px with no ring and no bright centre; the clean shot under it is
   dull olive (148/142/104) where the same metal over the column further up leaves bright
   tan. Readings: (a) the metal is cut there and each piece ends on the output's diffusion
   (a contact at each end, or one hole over the box); (b) one metal passing over, darkened
   by the box's outlines. In (a) the thin metal is `tc1_o4020`. Working assumption: none
   adopted, **no contact drawn**, the metal drawn as one piece with a name of its own.
   Would be settled by a sharper look at (6968, 4020-4080) or by where its ends go.
14. **Lower U, west side.** The leg x 6850-6884 and its foot are drawn over the west edge
   of the diffusion under the rail (x 6858); whether any diffusion lies west of it
   (x 6838-6858, in the gap, a dark bar) is not seen. If it did, the strip x 6820-6838
   would be one more gate between the island's neck and the output. Same nets either way.
15. **One rail contact on the island** is drawn (pits at y 4118-4158 in the clean shot).
   Chip 1's metal shot also shows a dark dot at (6898,4088), where the clean shot is plain:
   not drawn.
16. **A poly or edge along y 3920-3930** above the strip over `tc1_g`'s west arm (text
   map: salmon/pink at x 6798-6831, y 3925-3928). Not identified; it bounds this piece on
   the north.

## Not done

- **Gate columns x 6400-7000, y 2650-4450**: nothing drawn. Dense random logic with large
  devices under wide rails (x 6510-6560, 6682-6757, 6857-6932 near y 4000) and thin
  verticals between (x 6745-6762, 6766-6785, 6808-6828, 6913-6932, 6938-6955, 6959-6977).
  It is not built like the island: budget for 3x views and profiles, not 2x.
- The driver gated by `tc1_g` is traced (run 3). Left there: Ambiguities 12 and 13 (the
  two thin metals over it), and the far ends of its ports: `tc1_o4020` east of x 8350 on
  the bus line y 2641 (follower: ends at (9098,2639)), `tc1_x1`'s metal north of y 4060
  (a ring at about (7055,3730): dark runs y 3713-3723 and 3736-3753 with bright between,
  a tap not looked at; and its top end at (7054,3134)), `tc1_m6817`, `tc1_m6968`, both
  rails. The poly along y 2628-2648 that stops at (7438,2640), and the vertical poly
  x 7160-7180 it comes from. Run 2's observation that `sel_tracks.py` reports false breaks
  on ns3 and ns5 (chip 2 has blemishes, chip 1 does not) still stands.
- **Channel x 7000-7170**: verticals at x 7002-7022 (from contact 7010,3092 down), x 7048-7068
  (from contact 7056,3138 down), x 7091-7110 (upper piece from the north to contact
  7098,3180; lower piece is `tc1_l4_out`), x 7133-7152 (from the north down to y 4050,
  west to contact 7099,4047, poly west y 4035-4055). Each contact's poly goes west into
  the gate columns. Two C-shaped polys lie under them (y 3345-3360 / x 7135-7154 /
  y 3476-3491, and y 3518-3534 / x 7050-7069 / y 3845-3865). None drawn.
- **Top bus field y 2500-2975**: seven bus lines (y 2554, 2598, 2641, 2684, 2727, 2771,
  2814), each crossing the right VSS rail in poly between contacts at x 7663 or 7707 and
  x 7858 or 7902 (alternating). Only the y 2727 (ns2) and y 2771 (`w1`) lines are drawn.
  The y 2814 line's poly runs on east from contact (7707,2811) without a second contact
  in view. The row A outputs of cdp1 fan out west into it (see Ports).
- Far ends of ns3..ns6 and of ns2's west poly; `tc1_x1`, `db_b6` (all in the Ports table).
