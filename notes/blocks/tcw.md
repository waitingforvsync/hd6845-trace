# tcw: the gate column west of the island (x 6380-6760, y 2500-4450)

## Status

Partial. 23 transistors in `trace/tcw.txt` (plus three pull-downs in `trace/fld.txt`).

- **South end, y 3660-4450: complete** (run 2, 2026-11-17): the latch `fld_a_in` / `tcw_o3820`
  with both loads, the inverter `fld_y_b`, and the last inverter, which drives the row
  `tc1_x1_u`. Sections "Run 2" and "AND-OR-invert" below.
- **Stretch B, y 3200-3620** (run 3, 2026-11-17): the big gate has its output and load,
  `tcw_o3240` = NOT(`tcw_m6320` AND `tcw_o3550` AND (`tcw_m6362a` OR `tcw_m6404`)), and the
  inverter `tcw_o3550` was complete already. Where `tcw_o3240` goes is not traced. Section "Run 3".
- **Stretch A, y 2690-3220**: the pull-downs under the ground rail and the bus metals of their
  inputs (serial work, 2026-11-16); the loads and outputs east of the rail are not traced. "Not
  done" says what was seen there.

Serial work of 2026-11-16 used views in `cache/scratch/rax/` (`tcw_s.png`, `t1a.png`, `t1m.png`,
`t1cm.png`, `t1load.png`, `t2cm.png`, `w3a.png`, `w3c.png`, `w3m.png`, `w4.png`, `w5cm.png`);
run 2's are in `cache/scratch/tcw/`.

## What the block is

One column of random logic, about twenty gates by the survey, built like the step-logic
clusters of the top-left block: pull-down stacks under a ground rail (x 6505-6560), each
with a load towards the supply rail x 6690-6740, inputs arriving from the west on pads
with thin vertical metals (x 6276, 6319, 6403, 6465, 6645 ...) and on horizontal polys.
`tools/findcell.py` with the cells traced so far finds no copy of any of them here
except three weak matches of the small inverter of `fld` (scores 0.68-0.74 at
(6572,3535), (6572,4143), (6572,4273)). So it has to be traced gate by gate.

Why it matters: the two sources of row address bit 0 in interlace sync and video, and
the R9 comparator's bit-0 inputs, come out of this column (`notes/blocks/fld.md`), and
the bundle that carries R9's match passes it (`notes/blocks/r9m.md`). The field
(odd/even) flip-flop is expected here.

## Traced

### AND-OR-invert at y 3690-3905 (extracted)

    tcw_o3820 = NOT( fld_a_in OR (tcw_a AND tcw_c) )      (third input identified in run 2)

Under the rail one diffusion column: rail contact (6512,3708) | gate `tcw_c` (y 3732-3750)
| node | gate `tcw_a` (y 3777-3795) | output | gate `fld_a_in` (y 3845-3863) | rail contact
(6535,3905). The output node has an arm east (y 3808-3836) to a load whose gate poly is
one piece with a pad (6648,3785) above it; the pad's tail goes west and down onto the arm
(buried contact, `?`). From the pad a thin metal runs south along x 6645 to a pad
(6646,3986): the output's way out. That pad's poly gates a pull-down of `fld_a_in` (run 2).

- `tcw_c` and `tcw_a` are the same nets as two of the three inputs of the group below:
  their thin metals (x 6319, x 6403) end on pads at (6318,3740) and (6400,3788), and from
  each pad the poly goes east as a gate of this stack. So neither net is driven here;
  their drivers are further on (each also has a poly going west from its lower pad, along
  y 4130 and y 4000).
- The third gate: a short poly that widens south-east of the rail at (6570-6625, 3850-3900).
  Run 2: it is `fld_a_in` (tied to that node at (6590,3912), and the gate of its load).

How sure: class map (poly over channel at the three gates, diffusion between, both
contacts), one 2.8x view in two shots, the load and its pad at 5.6x in both stripped
shots. The supply assignment of the two rails is the layout rule (AMB-014).

### The group at y 3940-4200 (in `trace/fld.txt`; pull-downs only)

`fld_a_in` low through `tcw_a` AND `tcw_b`; `fld_y_b` low through `tcw_c`. Their loads, and a
third pull-down of `fld_a_in`, were found in run 2 (below).

## Read, not drawn (2026-11-16)

**Class map check.** `tools/wl_px.py` at known spots of the traced gate gives, for the sum
of red minus green over the two chip-2 shots: load gate (poly) 79, diffusion arm 45,
field 11-36; at the spots south of it that looked unreadable: 94 and 77 on the blocks
(poly), 47-49 on two areas (diffusion), 11 on the large area (field). So the `--open`
thresholds hold here; the map of y 3940-4210 east of the rail (`t2cm.png`) is right as
far as it goes, it just does not show which poly ties to which node.

**Tile y 3420-3700** (`t3cm.png`):

- An inverter: rail contact (6527,3490), one gate at y 3515-3535 whose poly comes from
  the west along y 3525 (seen to x 6430), output node y 3540-3560 with an arm east along
  y 3555 to a poly block (6625-6680, 3540-3570) and the diffusion under the supply rail.
  This is the place of one of `findcell`'s inverter matches ((6572,3535)).
- **`tcw_b` passes through**: its thin metal x 6465 ends on a pad (6460,3650); from the
  pad a poly crosses under the ground rail along y 3640-3655 over field (no transistor)
  and goes on east from (6580,3647). So `tcw_b` comes from east of the rail, between
  the column and the island.
- Under the rail at y 3575-3635 a small island that the map gives as diffusion with a
  poly outline, inside field: not understood.

**East of the supply rail** (`tb1.png`, x 6560-7120, y 3590-3720): the logic does not
end at the rail x 6690-6740. A second gate column stands at x 6750-6960 (boxes with
contact pits at (6885,3640), a wide metal at x 6860-6890, gates and loads between), and
`tcw_b`'s poly heads into it. So the untraced logic between this column and the island's
channel W1 (x 7174) is two columns wide, not one; the queue entry is widened.

## The whole ground rail as text (2026-11-16)

`tools/railprof.py 6514 6546 Y0 Y1` (new): classifies the strip of the clean shot under
a rail and prints the runs along it. Under a rail the clean shot's colours are the
"protected" ones, so a gate (bright salmon: poly over a channel), diffusion (tan) and
field (pink) separate cleanly; checked on the six gates already traced (all six found,
within 6 px). It does **not** find contacts (pits are too small and edge lines look the
same; two attempts with blob detection in the clean shot and in the metal shots found
only some of the known ones), and it calls dull edge regions "poly over field" (one such
at y 3910-3934, checked by colour: not a gate).

Seventeen gates under the rail x 6505-6560, in five stretches of diffusion:

| Stretch | Runs (y) | Reading |
|---|---|---|
| A, y 2699-3215 | D 2699-2739, **G 2740-2765**, D, **G 2791-2812**, D 2813-2912, **G 2913-2934**, D, **G 2957-2978**, D 2979-3085, **G 3086-3109**, D, **G 3140-3164**, D 3165-3215 | six gates in three pairs; not looked at |
| B, y 3237-3616 | D 3237-3250, **G 3251-3274**, D, **G 3295-3317**, D 3318-3337, **G 3338-3361**, D 3362-3408 (rail contact, two pits), **G 3409-3433**, D 3434-3447; then D 3470-3512 (rail contact), **G 3519-3542**, D 3543-3560 | class map `t4cm.png`: the nodes at y 3240, 3326 and 3437 each have an arm east. Readings: an AND-OR-invert at 3237-3408 if the top node is on ground through its arm (not seen), output at y 3326; a single pull-down at 3409 (output y 3437); the inverter at 3519 (output y 3550). The four upper gates take four horizontal polys from the west (y 3260, 3305, 3347, 3392) |
| C, y 3695-3925 | traced: `tcw_o3820` | |
| D, y 3956-4195 | traced (pull-downs): `fld_a_in`, `fld_y_b` | |
| E, y 4200-4344 | D, **G 4257-4281**, D | one gate; not looked at (a `findcell` inverter match at (6572,4273)) |

West of the column a bus of thin vertical metals (x 6232, 6276, 6319, 6360, 6403, 6465)
brings the inputs: each gate's poly runs west to a pad on one of them. A net can have
pads at several rows (`tcw_a`, `tcw_c` do), so the bus metals have to be followed pad by
pad; a metal at one x is several nets along its length.

### Stretch B, y 3230-3620: three pull-down stacks with their inputs (drawn, partial)

Views `t4cm.png`, `t3cm.png`, `bus1.png`; overlay check `busB_chk.png`. Five more
transistors. From the extraction:

    tcw_o3326 : to the rail through tcw_m6362a; and through tcw_m6362b, then tcw_m6320, to
                the top node of the stack (y 3232-3250), whose connection is not found
    tcw_o3437 : to the rail through tcw_m6404
    tcw_o3550 : to the rail through tcw_m6232

Each gate poly runs west to a pad on one of the bus metals (pads at (6315,3263),
(6378,3355), (6408,3393), (6222,3526); the second gate's poly goes round by x 6289 to a
pad (6385,3440)). The overlay sits on every pad ring, both rail contacts and the four
bus metals of this stretch.

Read but not drawn as joins:

- `tcw_m6362b` has a lower pad (6385,3567) whose poly goes east to the foot of the third
  stack's output (`tcw_o3550`): probably that output's way out (then the second gate of
  the first stack is NOT `tcw_m6232`). The join itself is not read.
- `tcw_m6320` has a lower pad (6315,3655) with a poly going west along y 3655.
- If the first stack's top node is on ground, `tcw_o3326` = NOT(`tcw_m6362a` OR
  (`tcw_m6320` AND `tcw_m6362b`)), the same shape as `tcw_o3820`.
- **A ring in the metal shot at (6539,3266)**, on the rail over the first gate of the
  first stack, where the clean shot shows a gate and no pit. Not explained.

The bus metals' extents are from `tools/tla_tracks.py` (gaps under 34 px bridged) and
are marked uncertain: a gap of 46-48 px in two of them was read as the ring of a contact
in mid-run, which the overlay supports, but their far ends and other taps are not seen.

### Stretch B, east side (2026-11-16; drawn as uncertain items, AMB-015)

Tried with the two shots not used before here (`eastB_m.png`: both metal shots at 3.6x;
`strapB.png`: the chip-1 fringed and the chip-2 stripped shot at 5.4x). They added three
things; each is in the trace with a `?` and in AMB-015:

- The output arms of stacks 1 and 2 are joined by a diffusion strip along x 6588-6612, so
  the two stacks are one gate with the rail contact in its middle.
- Stack 3 is a complete inverter: `tcw_o3550` = NOT `tcw_m6232` (extracted), load under the
  block (6625-6680, 3540-3570), supply contact (6700,3545).
- Its output goes west through a buried contact onto the poly of the pad (6385,3567), up
  the bus metal `tcw_m6362b` and round to the middle gate of stack 1.

So, as extracted:

    tcw_o3550 = NOT tcw_m6232
    tcw_o3326 : low through tcw_m6362a, or through tcw_m6404, or through
                (tcw_o3550 AND tcw_m6320) to the top node of stack 1 (connection not found)

Also seen, not drawn: a supply contact ring at (6705,3375) (the box (6690-6730,
3345-3405)); a small contact with its own island of metal at (6612,3270), 30 px east of
stack 1's top node (it may be how that node is connected: not read); a vertical poly
x 6640-6665 from y 3220 to y 3375 and another x 6600-6625, y 3320-3400. The load of
`tcw_o3326` is among these and is not identified.

### Stretch A, y 2690-3220: six gates in three pairs (2026-11-16; drawn, partial)

Views `bus2.png` (clean), `bus2m.png` (both metal shots: the bus metals and their pad
rings), `railA.png`, `A_cm.png` (class maps at 4x); gate positions from
`tools/railprof.py`; overlay check `A_chk.png` (it sits on all eight pad rings, the five
bus metals and the three rail contacts). Six more transistors. From the extraction:

    pair 1:  tcw_m6362a  low through tcw_m6404 AND tcw_m6320
    pair 2:  tcw_o2993   low through tcw_m6404 AND tcw_m6278
    pair 3:  rail | gate tcw_o2993 | tcw_o3115 | gate tcw_m6404 | tcw_o3180

| Gate (y under the rail) | Pad | Bus metal |
|---|---|---|
| 2740-2760 | (6403,2745) | `tcw_m6404` (top end) |
| 2786-2806 | (6310,2787) | `tcw_m6320` (top end) |
| 2910-2930 | (6400,2915) | `tcw_m6404` |
| 2957-2975 | (6272,2958) | `tcw_m6278` |
| 3081-3099 | none: a C-shaped poly from pair 2's output arm | (`tcw_o2993`) |
| 3130-3150 | (6400,3135) | `tcw_m6404` |

- **`tcw_m6404` is one metal** from its top pad (6403,2745) through the pads (6400,2915)
  and (6400,3135) to (6408,3393): seen continuous in both metal shots, a ring at each pad.
  It gates four pull-downs of the column: a common enable or clock.
- **Pair 1's output is `tcw_m6362a`**: the output node has an arm west (class map: open
  diffusion at (6445-6500, 2810-2845)) to the end of the poly from the pad (6355,2830),
  the top end of that bus metal, which runs unbroken (metal shots) down to the pad
  (6378,3355) and the third gate of stretch B's big gate. Buried contact `?`.
- **Pair 2's output feeds pair 3's first gate** through the C-shaped poly (arm west of the
  node at (6462-6510, 2983-3010), buried contact `?`).
- Rail contacts: (6522,2712) above pair 1; (6535,2872) and (6520,3052), each in a box cut
  off from the output above it by a line of field.

Corrections to what I wrote on 2026-11-16, when I held this stretch back:

- "One piece feeding four gates" was right; I doubted it for the wrong reason.
- The "two NANDs feeding each other" reading is **not** established and is not drawn.
  The class map shows the poly from the pad (6272,3178) (`tcw_m6278`, along y 3180)
  stopping at x 6460, 30 px of field short of pair 3's last node; and pair 3's middle node
  (`tcw_o3115`) has an arm east that goes on down the rail's east side. So pair 3 may be
  a two-input NOR with its output in the middle (if the last node is on the rail: pit
  marks at about (6520,3190), no clear ring) or a series pair with its output at the
  bottom. Both nodes are labelled; neither is called the output.
- The first track profile of the bus (2026-11-16) bridged gaps under 34 px. Unbridged, the
  x 6404 track shows only short bright runs, at the heights of the horizontal polys: the
  profile sees poly crossings as "metal" and misses the metal itself where a poly lies
  under it. The metal shots are the evidence for the bus metals, not that profile.

Not resolved in this stretch: where `tcw_m6278`'s poly along y 3180 ends; what the poly
from `tcw_m6232`'s top pad (6230,2875) does at the rail's west edge (it arrives at the
height of the first contact box); the loads; everything east of the rail.

### The bus metals south of the column, and the last gate (2026-11-16; drawn)

`tools/follow.py` and one view of both shots (`m6404s.png`).

- **`tcw_m6404`, the common enable, comes from the south**: from the column's foot it runs
  west along y 3708, south along x 6275, steps west round `fld_a_in`'s pad (y 3919,
  x 6233), back east at y 4231 and south along x 6282 to a pad (6275,4405) at the top of
  the vertical poly x 6275 of the field under the six bus metals. That poly goes on south
  to a pad (6275,4825) (`w1a.png`) and beyond: not drawn.
- **`tcw_m6232`** ends in the south on a pad (6232,3870); from it a poly runs east along
  y 3912 to the ground rail, which it reaches between the rail contact (6535,3905) and
  the node of `fld_a_in`. The rail profile reported a dull "poly over field" at exactly
  y 3910-3934. Whether the poly only crosses, or gates a third pull-down of `fld_a_in`'s
  node, was open; a colour check the same day shows it does not cross the rail (AMB-014): it
  ends at the rail's west edge, 30 px above the end of `fld_a_in`'s poly, possibly on the
  same node (then `tcw_m6232` would be `fld_a_in`). Drawn to the rail's west edge only.
- **A third metal on the x 6362 track**, `tcw_m6362c`, from a pad (6362,3832) to a pad
  (6362,4266). The upper pad's poly goes east towards the west side of `tcw_o3820`'s
  output node (drawn to x 6440; the join is not read). The lower pad's poly is the gate
  of the column's last pull-down (y 4257-4281). Run 2: the node above is the rail's contact,
  the node below is the output, and the gate is a complete inverter driving `tc1_x1_u`.

With this the first column's ground rail is complete in the trace as pull-downs: all
seventeen gates.

## Run 2 (2026-11-17, Matt Godbolt's session): the south end, y 3840-4450

Tools run as `tools/t.sh tcw ...`; views in `cache/scratch/tcw/`. The open areas between the two
rails were classed with `tools/tcw_cls.py` (new: the chip-2 stripped shot as a text class map;
thresholds measured on this run's first inverter: diffusion arm (6580,4295) 165/141/105, field
(6600,4350) 156/153/102, open poly (6650,4295) 191/157/76) and checked on views in both stripped
shots (R16, R19: nothing here is decided from `classmap.py` or `railprof.py` in the open).

### The last inverter, y 4200-4330: it drives the row `tc1_x1_u` (traced)

    tc1_x1_u = NOT tcw_m6362c

Rail contact (6521,4226) (ring in the metal shot, pits in both stripped shots) | gate y 4257-4281
| output node y 4282-4305. South of y 4305 the rail lies on field (pink in the clean shot): the
earlier node drawn below the output does not exist, and the node above the gate is ground.

- West: the output's arm (y 4287-4307) ends in a buried contact, a heavy box (6455-6478,
  4296-4320) in both stripped shots (`e3.png`, 5x); the poly from it runs south along
  x 6443-6466 and east as the row y 4383-4401, under both rails over field (salmon between
  pink), to x 6750: the row `tc1` drew from there to the pad (6947,4396) and labelled
  `tc1_x1_u`. The poly has no other branch west of x 6443.
- East: the arm (y 4284-4306) runs under the load's poly block (6622-6682, 4262-4322) to the
  supply pocket (6688-6735, 4245-4322, two pits). The load's gate tie is a tab of the block on a
  finger of the output's diffusion, buried contact box (6620-6650, 4236-4262).

**What this means for `tc1`'s Ambiguity 13 / AMB-020:** `tc1` aliases `tc1_x1_u` to `tc1_x1`
(assumed joins), and `tc1_x1` = NOT `ras_o0_sel1` has a driver of its own in `shm`. With this
inverter the row has a second driver. Two inverters on one net is not impossible but is unusual;
the joins at `tc1`'s pads (6962,4268) and (6968,3905) should be looked at again with this in
mind. Nothing in `tc1`'s trace is changed here.

### `tc1_p4308`'s row, y 4428-4448

Ends on a pad with a metal contact at (6622,4440) (text map: bright centre in a dark ring in
both metal shots, green hole in the clean shot); the thin metal leaves south at x 6621 into
`fld`'s region (port).

### The group at y 3900-4200, east of the rail: a cross-coupled pair (traced)

    fld_a_in  = NOT( (tcw_a AND tcw_b) OR tcw_o3820 )
    tcw_o3820 = NOT( fld_a_in OR (tcw_a AND tcw_c) )
    fld_y_b   = NOT tcw_c

A latch gated by `tcw_a`: with `tcw_a` low both keep their state; with it high `tcw_b` pulls
`fld_a_in` low and `tcw_c` pulls `tcw_o3820` low (traced; "a transparent latch with `tcw_a` as
its enable" is the reading, not a traced fact about what the signals are).

- **`fld_a_in`'s node** (the top node of `fld`'s stack, y 3956-3985 under the rail) has an arm
  east (y 3960-3974) to a vertical strip x 6603-6622 from y 3904 to y 4075 (class map: diffusion
  over its whole length; `px.py col 6612`: 141/117/84 in the chip-2 stripped shot).
- **Its load**: from the strip's head east (y 3906-3930) under a poly (6632-6670), which lies
  under the thin metal x 6645 (salmon in the clean shot, with the dark lines of the diffusion's
  edges at y 3900-3904 and y 3932), to the supply pocket (pale tan x 6686-6730, contact ring
  (6708,3917) in the metal shot).
- **The load's gate is the third gate of `tcw_o3820`** (formerly named by its place): that poly
  runs from the gate's east end south (x 6575-6600) and east (y 3872-3900) to the load, and
  comes down into a heavy box (6580-6600, 3903-3925) at the strip's head: a buried contact
  (`px.py row 3912`: interior 157/138/98 in the chip-2 stripped shot and dark in the clean shot,
  like the two known buried contacts of the last inverter). So that gate input is `fld_a_in`.
- **A third pull-down of `fld_a_in`**: the strip's south end passes under the poly block
  (6600-6680, 4028-4056) and ends on a diffusion strip y 4062-4080 that runs west to the rail's
  contact node. The block is one poly with the pad (6646,3986) (dark-brown open poly
  x 6650-6675, y 4005-4030 between them), where the thin metal x 6645 from `tcw_o3820`'s load
  pad lands.
- **`fld_y_b`'s load**: the bottom node's arm (y 4156-4178) runs on under the poly block
  (6626-6676, 4134-4184) to the supply pocket `tc1` drew (contact (6730,4158)); gate tie: a tab
  of the block on a finger of the node (x 6600-6620 north to y 4108), buried contact box
  (6625-6654, 4106-4132).

Overlay: `d4.png` (3.4x, both stripped shots).

## Run 3 (2026-11-17, Matt Godbolt's session): stretch B's big gate, y 3140-3410 east of the rail

Views in `cache/scratch/tcw/` (`B_a.png`, `B_c.png`: both stripped shots at 3.4x; `B2.png` 5x;
`B_m.png` both metal shots; `B5.png`, `B6.png`; overlay `B_chk.png`). Open areas decided in the
chip-2 stripped shot with `tools/px.py` profiles (R16, R19). One thing to know when reading them:
the thin metal x 6612-6628 left an etch-boundary line on each side of itself in the chip-2
stripped shot (x about 6607 and 6635, on every row from y 3190 to y 3290), and the rail one at
x about 6585; they cross every feature and are not layout (trap 4).

    tcw_o3240 = NOT( tcw_m6320 AND tcw_o3550 AND (tcw_m6362a OR tcw_m6404) )

(as extracted; it rests on the strip of AMB-015, which is still drawn `?`).

- **The output is the top node of stack 1** (y 3232-3250 under the rail), the node whose
  connection the 2026-11-16 work did not find. Its arm runs east along y 3232-3246 to x 6656
  (`px.py row 3239`: 194/170/126 at x 6560-6581, 198/165/127 at x 6614-6629 in the chip-2 stripped
  shot, the boundary lines between; the clean shot is tan where the rail and the thin metal
  protected it and dark brown in the open, as on the strip) and turns south as a strip x 6640-6656
  (`px.py col 6648`: red minus green 20-28 from y 3256 to y 3296).
- **The node `tcw_o3326` (with `tcw_o3437`) is inside the gate, not an output**: it has no load.
  Field lies between its strip (x 6588-6612) and the load (`px.py row 3308`: 153/153/90 at
  x 6600-6620). The strip itself reads as diffusion again (`px.py row 3340`, `row 3390`: red minus
  green 19-33 at x 6596-6604 between two dark edges), which supports AMB-015's first item.
- **The load**: the strip widens under a poly block (6618-6680, 3314-3368) (the diffusion's edge
  lines at x 6630 and x 6660 run on through the poly; channel about 25 wide and 54 long) and comes
  out as a drain (6632-6672, 3376-3404), which runs east under the supply rail's edge line into
  the pocket `tc1` drew (contact (6708,3378); `px.py row 3396`: tan from x 6680 to x 6728 in the
  clean shot).
- **The load's gate tie**: the block has an arm north along x 6662-6680 (poly colour in the chip-2
  stripped shot from y 3364 up to y 3206: rows 3364, 3358, 3340, 3308, 3270, 3234, `col 6672`),
  beside the strip and 6 px from it. At y 3202-3220 its head turns west onto the strip's head: a
  box (6640-6660, 3200-3220) with a heavy frame, interior 144/128/88 in the chip-2 stripped shot
  and dark in the clean shot, the colours of the buried contacts of run 2 (157/138/98, dark).
- **Stack 1's first gate poly runs on east of the rail to a pad** with a metal contact
  (6616,3272) (`textmap.py 6596 3140 6664 3290 3`: bright centre in both metal shots, green hole
  in the clean shot). `px.py row 3258`, `row 3264`: poly colour at x 6589-6598 between the two
  boundary lines in the chip-2 stripped shot; salmon, dark red-brown, salmon in the clean shot, no
  field. So the pad is on `tcw_m6320`. From it a thin metal goes north along x 6620 (the clean shot
  is protected along it from y 3287 to y 3182) and north-east to a second contact (6637,3166)
  (text map: bright centre in both metal shots, green hole) on a pad (6623-6656, 3148-3180). It
  crosses the output's arm at y 3232-3246 without a contact (no green hole, no ring).

Read, not drawn:

- The pad (6623-6656, 3148-3180) seems to be one poly with a block east of it (6660-6678,
  3150-3178) and that with the large block (6628-6678, 3118-3142) north of it (a dark line at
  y 3144-3148 between them, which may be a diffusion edge under one poly). If so, `tcw_m6320` is
  on a load's gate, that is, it is the output of a gate of stretch A.
- A poly foot leaves the tie's box west along y 3200-3216 to x 6592 (`px.py row 3208`), where a
  vertical poly x 6575-6600 runs north along the rail's east side (salmon-red in the clean shot at
  x 6574-6590 from y 3108 to y 3172, `px.py col 6578`, `col 6595`). That would be the output's way
  out, north into stretch A. Its north end is not read, nor whether it lies on diffusion there
  (the clean shot's red is that of poly over a channel: a pull-down east of the rail, R23).
- A narrow diffusion x 6604-6616, y 3104-3144 (`tcw_cls.py`).

## Ports

Also in `ports.d/tcw.txt`.

| Name | Layer | Where | Direction | What |
|---|---|---|---|---|
| `tc1_x1_u` | poly | x 6750, y 4383-4401 | out | output of the last inverter, east into `tc1` (its row to the pad (6947,4396)) |
| `tc1_p4308` | poly | x 6750, y 4428-4448 | in | from `tc1`; ends on the pad (6622,4440) |
| `tc1_p4308` | metal | x 6615-6627, y 4450 | ? | the thin metal from that pad, south into `fld` |
| `tcw_m6404` | poly | pad (6275,4405) | in | top of a vertical poly going south; gate input of four pull-downs |
| `tcw_m6320` | poly | x 6205, y 3646-3664 | ? | poly going west from the pad (6315,3655) |
| `tcw_m6278` | metal | x 6270-6282, y 2700 | ? | bus metal, drawn end |
| `vss`, `vcc` | metal | x 6507-6557 and x 6687-6737, y 4450 | - | the two rails |

`tcw_a`, `tcw_b`, `tcw_c`, `fld_a_in` and `fld_y_b` leave through `fld`'s geometry (pads west of
the rail), not through a boundary of this package.

## Ambiguities

1. **Supply assignment** of the two rails (x 6505-6560 ground, x 6690-6740 supply): the layout
   rule (loads towards the east rail), AMB-014. Run 2 adds four loads on the east rail and none
   on the west, which fits.
2. **The buried contact (6580-6600, 3903-3925)** decides that the third gate of `tcw_o3820` is
   `fld_a_in`, that is, that the pair is cross-coupled. Evidence: a heavy box in both stripped
   shots and an outline in both metal shots; interior colour like the two known buried contacts
   of the last inverter; the poly it ties is the gate of `fld_a_in`'s own load, which in this
   chip is tied to the load's source. The other reading (the box is only the strip's head and
   the poly passes beside it) would leave that load's gate untied. Drawn firm.
3. **Two drivers on `tc1_x1`** if `tc1`'s assumed joins (its Ambiguities 13 and 17, AMB-020) hold:
   see "The last inverter". Not resolved here; nothing of `tc1`'s is changed.
4. Stretch B's east side: AMB-015 (three `?` items, unchanged in the trace; run 3's profiles
   support the first, the strip, and its gate's equation rests on it). Seen in run 2 and not redrawn:
   the tie of `tcw_o3550`'s load looks like the other ties of this column (a tab of the block
   going up to a box at (6585-6650, 3495-3520)), not like the `?B` at the block's west end; the
   net is the same either way.

5. **The load block and its arm north are drawn as one poly** (run 3). Between the block's
   channel and the arm lies a dark line at x 6657-6663, read as the diffusion's east edge under
   the poly (the west edge shows the same way at x 6630). If they were two polys the load's gate
   would be untied and the arm a wire of `tcw_o3240` ending at y 3368. The net of the arm is the
   same either way.

## Review

### Run 2's review (2026-11-17 15:25 -0600)

Round 1, full review of run 2's two pieces (the last inverter with the two rows from `tc1`,
x 6430-6760, y 4190-4455; the loads and the third pull-down east of the rail, x 6545-6760,
y 3840-4200), by a fresh agent on Claude Fable 5.2, at commit `b197dbb`; 13 images in
`cache/scratch/tcw/review-1/`. The older geometry north of y 3660 was not under review.

Told to suspect: the buried contact (6576-6603, 3898-3926) that makes the pair cross-coupled;
whether the poly y 3872-3900 and the rectangle under the thin metal are one poly, and the
diffusion under it; whether the strip x 6603-6622 passes under the block (6600-6680, 4028-4056)
to the strip y 4062-4080; the block's link to the pad (6646,3986); the east end of the strip
y 4062-4080; the row y 4383-4401 under both rails; the buried contact (6455-6478, 4294-4320);
the thresholds of `tools/tcw_cls.py`.

Checked and found correct (views at 3-5x in two or more shots, `tools/px.py` profiles, the
follower): every item above. The buried contact: row y 3915 of the chip-2 stripped shot reads
box interior x 6583-6596, a 12 px dark line, the strip x 6613-6620, the same form as the two
load ties (rows y 4120 and y 4250); field west and south of the box; the poly continuous down
x 6590 into it. The poly and the rectangle are one (the lines at y 3902 and y 3933 are the
diffusion's edges and continue at x 6674). Pad, link and block are one poly. The strip
y 4062-4080 has no top edge of its own at x 6612-6638 (the diffusion comes out from under the
block) and a closed east end. Row y 4392 continuous from x 6443 to x 6764 over field under
both rails. The thin metal x 6645 runs pad to pad (214 px).

Findings, all geometry only, all confirmed by me (`px.py row 4042`, `col 6650`, `row 4420`,
`row 3917`) and fixed:

1. The pull-down of `fld_a_in` under the block is about 40 wide, not 25 (diffusion edges cross
   the block at x 6601-6604 and x 6643-6646).
2. `fld_a_in`'s load poly reaches x 6677, not 6670.
3. `fld_y_b`'s load block reaches y 4198, not 4184.
4. The strip is x 6600-6614 at y 3933-3958 (drawn from x 6600 now).
5. The ground rail widens east to x 6586 south of y 4388 (drawn).

Not checked by the reviewer: the arms where they cross the rails' edge lines (x 6556-6572,
x 6676-6686: hidden by the edge line in every shot, inferred from matching edges on both
sides); `tc1`'s rail and contact (6730,4158); a patch `tools/opendiff.py` reports at
(6711-6732, 3943-3987) under `tc1`'s rail; `tc1_x1_u` being `tc1_x1` (that is `tc1`'s alias).
The reviewer also notes that `tools/tcw_cls.py` misreads poly under the thin metal's ghost and
strip edges; `tools/px.py` profiles decide.

    tools/t.sh tcw sameconn.py b197dbb          -> connections identical
    .venv/bin/python tools/sameconn.py b197dbb  -> connections identical

Round 1: no findings that change a connection.

## Not done

North of y 3660 the loads and outputs. What run 2 saw there, not drawn (views `b1.png`, `b2.png`,
`b3.png`, `a1.png`, `a2.png`; class maps from `tools/tcw_cls.py`):

- **Where `tcw_o3240` goes**, and what the pad (6623-6656, 3148-3180) at the north end of
  `tcw_m6320`'s thin metal is on: "Run 3", Read, not drawn. Both lead into stretch A's east side
  (y 3060-3220), which is the next piece.
- **Stretch A, y 2690-3220, east of the rail.** A metal about 25 px wide along x 6630-6655 from
  a pad with a contact at (6642,2755) to a pad with a contact at (6642,2965); poly blocks at
  (6600-6628, 2742-2766), (6590-6660, 2840-2870), (6600-6660, 2900-2925), (6600-6680,
  2995-3015), (6620-6680, 3060-3140); a diffusion strip y 2724-2736 from the rail's contact node
  east to x 6625; a diffusion (6565-6610, 2780-2830) east of the rail beside pair 1's second
  gate and output.
- y 2500-2690: not looked at.
- `tcw_b`'s metal (x 6465) north of y 3990 and its poly east from (6580,3647); the polys of
  `tcw_a` and `tcw_c` going west along y 4000 and y 4130 (west of this package's region).
- Re-read items R16, R19, R20, R23 for the 2026-11-16 work north of y 3660 are still open; the
  south end was read in the chip-2 stripped shot in run 2.

Method that worked in run 2: `tools/tcw_cls.py X0 Y0 X1 Y1 4` first (it shows the diffusion
strips between the rails as runs of `d`), then one view of both stripped shots at about 3.4x
(sharper than 6x) with the draft overlaid.

## Notes from `tc1` (coordinator, from the 2026-11-17 handoffs)

Two poly rows enter this region from `tc1` at x 6750: y 4385-4405 (`tc1_x1_u`, seen to about
x 6445, passing under the ground rail x 6505-6560, not checked for a channel there) and
y 4428-4448 (`tc1_p4308`, ending on a pad with a contact at (6620,4436); metal south along
x 6621). `tc1_p3698` comes down a poly under the supply rail's edge at x 6725-6740. These are
this block's to follow.
