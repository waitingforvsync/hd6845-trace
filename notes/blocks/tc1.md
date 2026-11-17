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
6870-6915 x 4320-4365 in both metal shots, a pit in the clean shot). So, as extracted:

    tc1_x1 = NOR(ras_o0_sel1, tc1_p4308)        (through ?P, ?B, ?D: see Ambiguity 17)

How the strip meets the pad is not resolved (a dark line 6 px wide at x 6940-6946 between
plain tan and the pad): `?B`. The strip is `?D` where it crosses the two gaps. South of
y 4293 the diffusion under the thin metal x 6817 goes on (tan to about y 4345, pits at
y 4312-4341, a poly beside it): **not traced**, so the strip's node may have more on it,
the thin metal x 6817 included.

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
the clean shot is bright green (114/166/77 and 129/152/94 at x 7443-7446, y 2634-2646:
open field) for about 8 px, and the chip-2 stripped shot shows the poly's end edge at
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
| `tc1_m6817` | M | x 6811-6823, y 3905 and y 4228 | ? | thin metal over the driver's west column, no contact drawn (Ambiguity 12). Follower (started either side of the strip, where it stops): from (6822,3496) to (6809,4379), candidates (6818,3883), (6813,3754), (6818,4309); the two at (6820,3977) and (6817,4211) are not contacts (text maps: unbroken metal, no ring) |
| `tc1_x1_u` (alias of `tc1_x1`) | M | x 6962-6974, y 3905 and y 4300 | ? | the thin metal x 6968: contact on the pad (6962,4268) at the end of `tc1_x1`'s branch; no contact to the driver's diffusion (Ambiguity 13). Follower: from (6966,3806) to (6975,4402) when started either side of the box at y 4033-4068, where it stops; candidates (6970,3947), (6972,4218) are not contacts (review round 1)
| `tc1_p4308` | P | x 6988-7002, y 4384, going south | in (a gate here) | gate of the pull-down on the strip; where it comes from is not followed |
| `vss` | M | rail x 6861-6932 at y 3905; x 6858-6908 at y 4380 (it narrows at y 4238) | | goes on both ways, not followed |
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
17. **`tc1_x1` has a second pull-down, 1,500 px from its first.** `shm` draws `tc1_x1` as the
   output of an inverter of `ras_o0_sel1` with its load at (8564,4254) (through a `?B`
   there). Here the same net, by the ring's branch, the pad (6962,4268) and the strip, is
   pulled to the rail through `tc1_p4308`. Readings: (a) both are right: a NOR with its two
   pull-downs far apart; (b) the branch does not join the pad (the `?P`) or the strip does
   not join the pad (the `?B`): then the strip, the thin metal x 6968 and this pull-down are
   another net, whose load is not found; (c) `shm`'s `?B` is wrong and the net's only
   driver is here. Working assumption: (a), as extracted, **every link of it marked**.
   Would be settled by tracing the strip's node to its load or its other ends (the
   diffusion under the thin metal x 6817 south of y 4293, the thin metal x 6968's ends at
   y 3806 and y 4402) and by a sharper look at the pad.

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

## Not done

- **Gate columns x 6400-7000, y 2650-4450**: nothing drawn. Dense random logic with large
  devices under wide rails (x 6510-6560, 6682-6757, 6857-6932 near y 4000) and thin
  verticals between (x 6745-6762, 6766-6785, 6808-6828, 6913-6932, 6938-6955, 6959-6977).
  It is not built like the island: budget for 3x views and profiles, not 2x.
- The driver gated by `tc1_g` is traced (run 3). Left there: Ambiguities 12 and 13 (the
  two thin metals over it), and the far ends of its ports: `tc1_o4020` east of x 8350 on
  the bus line y 2641 (follower: ends at (9098,2639)), `tc1_x1`'s metal north of y 4060
  (a ring at about (7055,3730): dark runs y 3713-3723 and 3736-3753 with bright between,
  a tap not looked at; and its top end at (7054,3134)), `tc1_m6817`, the thin metal x 6968
  (`tc1_x1_u`: its ends at y 3806 and y 4402 and any other contact; the pad (6962,4268)'s
  west side, now drawn as the strip), both rails. **First for the next run**: the strip's
  node (Ambiguity 17): the diffusion under the thin metal x 6817 south of y 4293, and
  `tc1_p4308` south of y 4384. The channel metal x 7003-7023 (no ring on it over
  y 3972-4296; follower: from (7011,3850) south to a corner at (7006,4484)) is not drawn. The poly along y 2628-2648 that stops at (7438,2640), and the vertical poly
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
