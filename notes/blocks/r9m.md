# r9m: where R9's match goes (drawn; it is the input of `rcs_mu`'s inverter)

Serial work, 2026-11-16. No trace file. Views in `cache/scratch/rax/`: `eq1.png` ...
`eq9.png`. Every metal stretch from `tools/follow.py`.

## CORRECTION (2026-11-17 07:11): R9's match drives `rcs_mu`'s inverter; read this first

An independent review (Fable, 4-5x in both stripped shots; its images are in the reviewer
worktree under `cache/scratch/rv_r9m/`, `hop4.png`, `hop5.png`, `hop6.png`, re-checked
here by overlay, `fixhop.png`) found that the two poly hops under the metals
x 5078-5127 (between pads 4867/4912 and 5358/5400/5405) **do not run straight**: each
poly steps down one track going east. The trace was redrawn accordingly:

- R9's match (pad (5358,2641)) runs west, steps up at x 5120-5135, and arrives at pad
  (4867,2596), i.e. the metal that ends on the contact (4148,3335). So **the step logic's input
  there (then under a place name) is R9's match**, now one name, `ra_eq_r9`, and `rcs_mu = NOT ra_eq_r9`: the step
  logic's first term is "scan line equals R9 (as compared at the RA pins), and not
  `rcs_mv`". Firm geometry (no `?` on the path).
- Pad (4912,2641), with the metal down x 4194, the stub and track P's lower piece, belongs
  to the poly that steps down to a pad (5405,2681) and the metal along y 2685 to x 5848
  and south to (5845,5045): "bundle line 3", named `r9m_l3`. Track P's split (AMB-013)
  stands, confirmed by the review's measurements, but the two pieces carry the opposite
  nets to what the earlier text below says.
- Pad (5400,2596) does not join line 1's west part: its poly turns north at x 5175 and
  ends near y 2545 (not followed). The metal from it (y 2599, x 6022, the crossing field,
  pad (7855,4676)) is named `sl_eq_r5_n`. At `cdp1`'s west edge every row steps down one
  track (nested L's at x 8215-8345, `cache/scratch/bust/stair2.png`), so this row does
  **not** become `cdp1_l4676`: it turns south near x 8190. `cdp1_l4676` (the line from
  `amr` c3, east of `cdp1`) is fed instead by the west row y 4635.
- So: **`amr` c3's outer output is not `ra_eq_r9`**; that statement below is withdrawn,
  as is "the bundle's first line ... followed back 9,000 px".

A second, focused review (same day) confirmed both corrected hops and the staircase at
5.5x / 4.5x in both stripped shots, and found nothing else between the two legs. Not
drawn yet: the poly from pad (5400,2596) does not end at y 2550; it turns west along
y 2550 under the same metals to a pad with a contact at about (4905,2550). The
staircase's vertical legs are at about x 8360, 8318, 8275, 8232 (drawn 8337, 8297, 8262,
8230; no connection changes).

The sections below are kept as the record of how the earlier reading was made; where
they disagree with this one, this one holds.

## Route of `ra_eq_r9`, from the comparator west

| Stretch | Layer | Ends |
|---|---|---|
| from `cdp1`'s edge (8340,4459) west | poly | pad (7815,4460) |
| west along y 4462, south at x 7450, west along y 4527 (the top one of six bus metals that cross above the row address selector) | metal | pad (6920,4525) |
| west under three rails | poly | pad (6445,4520) |
| west over a field of eight vertical polys (x 6050-6400, no pads seen), north along x 5974 from y 4528 to y 2642, west along y 2640 | metal | pad (5358,2640) |
| west under the metals of `res_b` (x 5275) and `lpstb_b` (x 5335) | poly | pad at about (4912,2640) |
| west, shifting up 42 px on a diagonal at x 4580-4660, to x 4192 at y 2598, south along x 4192 | metal | y 3385, with a stub west to x 4168 |

It is the second of four parallel lines over the last 1,200 px. The other three, by
their west ends: the first (y 2598 at x 4760) shifts to y 2555, turns south at x 4148 and
ends on the contact (4148,3335) of `ra_eq_r9`; the third ends on a pad (4270,2640) with
a poly west; the fourth on a pad (4232,2683) with a poly west. `rcs_e3`'s pad (4270,2725)
is the next position down; its metal goes east to x 4496 and south to y 3813 (followed,
not drawn), so `rcs_e3` is not one of the four.

## Where it ends

In the middle cluster of the row counter's step logic (`trace/tla.txt`), beside the
contact of `ra_eq_r9`, the input of the inverter that makes `rcs_mu`:

    rcs_mu  = NOT ra_eq_r9
    rcs_in1 = NOR(rcs_mu, rcs_mv)     = ra_eq_r9 AND NOT rcs_mv
    row counter step = rcs_in1 OR (NOT rcs_e4 AND NOT (rcs_e3 AND rcs_a2))

Whether the match line is on `ra_eq_r9` is AMB-013. If it is, the first term of the
row counter's step is "scan line equals R9 (as compared at the pins), and not
`rcs_mv`", which is what one expects of it; but that is the reason to be careful, not
evidence.

## Drawn (2026-11-17 04:33, contributor session)

`trace/r9m.txt`: the whole route above, from `cdp1`'s poly end (x 8340) to the stub at
the foot of x 4194, as one net `ra_eq_r9`. Every metal stretch re-run through
`tools/follow.py` (both chips' metal shots); the diagonal at x 4626-4668 placed by
sampling the follower with `--max` (it is at (4670,2639) after 180 px, (4660,2633) after
190, (4620,2598) after 230). Checked by overlay in `metal` and the stripped shots at
1-1.25x along the whole route and at 4x at the corner (4194,2599)
(`cache/scratch/r9m/pv1.png`, `pv2.png`, `pv3.png`, `cor.png`).

The follower's two contact candidates on the route are not contacts (four shots at 4x,
`cc1.png`, `cc2.png`): (7379,4527) and (5973,3398) are dark specks in the clean shot only,
with no ring in either metal shot. So the line has no taps between the comparator and
the step logic.

Extraction: no new transistors (the three poly hops cross no diffusion), no name clash;
`ra_eq_r9` is one net from the comparator's load to (4170,3376). The stub's last 12 px
to the metal x 4148 (`ra_eq_r9`) are **not drawn** (AMB-013 unchanged).

## The bundle's first line, followed back towards its driver (2026-11-17 04:41)

Drawn in `trace/r9m.txt` as one net with `ra_eq_r9` (the inverter input at the contact
(4148,3335) in `tla`), and with `cdp1_l4676` (alias), as far as the edge of an untraced
logic block. Route, from the step logic outwards:

| Stretch | Layer | Ends | How |
|---|---|---|---|
| north along x 4149 from the contact to y 2555, east, diagonal (4651,2555)-(4692,2597), east along y 2598 | metal | pad (4867,2596) | follow.py; diagonal sampled with `--max` |
| east under `res_b` / `lpstb_b` | poly | pad (5400,2596) | 1.8x view, both stripped shots |
| east along y 2599 to x 6022 (48 px east of R9's line), south to y 4442, east | metal | pad (6059,4440) | follow.py; 2.2x view |
| south along x 6058: one of the eight vertical polys R9's line crosses | poly | pad (6058,4742) | 2.2x, three shots (`l1h.png`) |
| the bus metal y 4742, east | metal | pad (6490,4740) | follow.py; 3.5x (`l1i.png`) |
| east along y 4740 under the rail x 6505-6560 and the crossing field | poly | pad (6965,4738) | 2.4x and 3x (`l1j.png`, `l1l.png`) |
| east along y 4744, north at x 7657 to y 4673, east | metal | pad (7855,4676) | follow.py; 2.8x (`l1m.png`) |
| east along y 4676: through `cdp1` as its through line `cdp1_l4676` (x 8340-10850, drawn there), on through the bus field, a diagonal (11465,4676)-(11530,4737) under the wide supply metal | poly | pad (11650,4740) | 0.95x strip, 2.9x at the diagonal (`l1o.png`, `l1q.png`) |
| east along y 4742 | metal | pad (12780,4738) | follow.py; 2.6x (`l1r.png`) |
| south along x 12782 under the wide supply metal y 5200-5550 | poly | a pad at about (12786,5570) | 0.48x only: drawn to y 5550 |

Contact candidates the follower reported on these stretches: (7178,4744) is `tc1`'s
diagonal poly passing under unbroken metal (four shots at 4x, `cc3.png`); the others lie
on the end pads. Extraction: no new transistors, 0 errors; the net gates only the
inverter that makes `rcs_mu`.

**Where it comes from**: a pad at about (12786,5570) into the logic block x 12600-12900,
y 5600-6400, between the counters and the upper right datapath, which no package covers
yet. So AMB-013's test ("if the first line is a second comparator's match, reading A is
the design") is one block away: the next step is that block, starting at the pad.

### A further observation on AMB-013 (not adopted, not drawn)

`tools/follow.py` going north from (4148,3450) turns **east** at y 3378 onto R9's stub
instead of reaching the contact (4148,3335); going south from y 3300 it ends at y 3338.
At 5x in four shots (`amb.png`): the contact's ring ends at about y 3345, and chip 1's
metal shot shows a dark band at y 3345-3360 across the track before bright metal resumes
at y 3362; chip 2's shows some speckle in the band.

**Measured (2026-11-17 04:42, `tools/r9m_bright.py` and the follower's own metal test, red > 177 and
green > 128, in both metal shots):**

| Where | Result | Reference |
|---|---|---|
| along x 4144-4154, y 3336-3376 (contact to lower piece) | **no pixel passes as metal in either shot from y 3341 to y 3371** (30 px); the brighter patch at y 3354-3362 is red 117-142 (max 162) in chip 2 and 104-131 in chip 1, the bare-ground range | R9's line over the poly x 6058 (y 4528): two dips about 5 px wide to 40-50, back to 150+ between; contact (6965,4740) into continuing metal: dips of 3-6 px |
| along y 3378, x 4140-4198 (R9's stub to the x 4148 metal) | metal 4144-4160 and from 4168 on in both shots; **5-6 px** without metal at x 4162-4166 (darkest 76-87) | the same 3-6 px dips; separate metal lines here are 20 px or more apart |

So the 30 px at y 3341-3371 is a break between two metal pieces, and the 5-6 px at
x 4162-4166 is the poly stem's edge (x 4166) printing through continuous metal.
**This supports reading C**: R9's match comes down x 4194, along the stub and onto the
lower piece of track P (x 4148, y 3372-3596, bottom end not looked at); the inverter that
makes `rcs_mu` has its input on the upper piece, which is the bundle's first line
(drawn above, followed to x 12782). Then `rcs_mu` = NOT (first line), and R9's match goes
on south: the lower piece ends on a contact at about (4148,3588) (ring in the metal shot,
pale centre on a poly pad in the clean shot, 4.5x, `pb.png`), whose poly runs **west**
along y about 3583 (salmon at x 4010-4140 in the clean shot, 2.2x, `pc.png`) into the
middle cluster's gate column, not traced. That gate is where R9's match is used, under
reading C.

**Applied as a separate commit** ("tla/r9m: reading C of AMB-013"), which also edits
`trace/tla.txt`: track P split into y 3320-3341 (the contact, label `ra_eq_r9` moved up)
and y 3371-3596, and R9's stub drawn onto the lower piece. Only the one contact (3335)
was on that metal, so nothing else changes. Extraction: `rcs_mu`'s inverter is gated by
the step logic's input (taken then for the bundle line from `amr` c3), and R9's match now runs on
down track P. Its lower end (contact (4148,3588)) has a poly west along y 3578-3598 to
x about 3995, where it turns south into the middle cluster's gate column (3.2x,
`cache/scratch/r9m/r9g.png`): the gate that uses R9's match is there, not traced. Between R9's stub and the x 4148
metal at y 3365-3390 there is a dark line only 4-12 px wide (at x about 4163, where
`tla`'s poly stem has its right edge, x 4166), narrower than the spacing between
separate metal lines elsewhere.

So a third reading exists. **Reading C**: the stub joins the x 4148 metal (the dark line
is the poly stem's edge printing through), but that metal is two pieces, broken at
y 3345-3360: the upper piece (the first line) ends on the contact and drives
`ra_eq_r9`, and the lower piece (y 3362-3596) carries R9's match on south. If so,
`trace/tla.txt`'s `M 4148,3320 y3596` joins two nets. A brightness profile along
x 4148 from y 3330 to 3370 in both metal shots, against a known crossing of poly under
unbroken metal, would decide the break.

## The bundle's lines 3 and 4, followed east from the step logic (observed, not drawn)

- **Line 3** (pad (4270,2640) in the middle cluster): metal east along y 2642 to a pad
  (4866,2681); beyond the `res_b`/`lpstb_b` metals a metal from x 5440 runs east along
  y 2685 to x 5848 and **south along x 5842 to a pad (5845,5045)** (tools/follow.py). The
  hop under the two metals is assumed from lines 1 and 2, not seen. Directly below, at
  (5845,5575), is the top pad of `bw`'s metal x 5841, which is `rc_stepreq_n` (the row
  counter's step request, made in the step logic). In the chip-2 stripped shot there is
  no poly between the two pads (1.6x, `cache/scratch/bust/sr.png`), so they are not shown
  to be one net. If they were, line 3 would be the step logic's output on its way to
  `wl`, not an input.
- **Line 4** (pad (4232,2683)): metal east along y 2685, then down to y 2728, to x 4868
  (pad, sampled with --max). The metal beyond the hop was not found from x 5420-5520 at
  y 2727.
- From the bus side (`notes/blocks/bust.md`): `amr`'s outer outputs c1 and c2 run west on
  `c4l1` and `cdp1_l4632`, along the bus metals above the row address selector to
  x 6913-6921. Whether those are lines 3 and 4 is not established; given line 3's route
  south at x 5842, probably not.

## Not done

The first line's source: the logic block x 12600-12900, y 5600-6400, from the pad at
about (12786,5570); the split of track P proposed above (for the coordinator); where R9's match goes south of y 3596;
the other two lines of the bundle; the pads (4270,2640) and (4232,2683) west into the cluster; `rcs_e3`'s metal
beyond (4494,3813).

## Note (coordinator, from the handoffs of 2026-11-17/18)

`sl_eq_r5_n`'s east end is drawn by `tc2` (not an open end). `r9m_l3` has a driver: `tc2_o5175`, joined
by `tl6` (join 10, contact (5845,5043)).

## Correction from `tl3` (coordinator, from the handoffs of 2026-11-18, second batch)

- "The lower piece ends on a contact at about (4148,3588), whose poly runs west along y about 3583 into
  the middle cluster's gate column, not traced": traced by `tl3` run 7: the pad (4148,3592) gates
  `tl3_e3550` = NOR(`rcs_mu`, `tc2_o5175`) and `tl3_e3712` = NOT `tc2_o5175`; both rest on this block's
  stub join at y 3376 (AMB-035).
- What R9's match does in the step logic: "`rcs_mu` = NOT R9's match" stands; "term 1 = R9's match AND
  NOT `rcs_mv`" does not. R9's match is an input of `rcs_mn3852`, and reaches the step request by
  `tl3_e3550` and `rcs_e4` (marked: AMB-013, AMB-032).

## Corrections (coordinator, from the handoffs of 2026-11-19)

- `sl_eq_r5_n` has a driver: NOT `sl_eq_r5` (`eof`). "Pad (5400,2596) ... its poly turns north at x 5175
  and ends near y 2545 (not followed)": it turns west there and is `tl4`'s row of the pad (4908,2551)
  (bus line 1), which `eof` joins on west through `tl3`'s strip to `sl_eq_r5_n` and north into `tlb`.
