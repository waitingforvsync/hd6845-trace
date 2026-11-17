# ral: the stage in front of the RA pad drivers (x 13960-16330, y 4220-4560)

## Status (2026-11-17 14:14 (UTC+1), contributor session; inverter 1 independently reviewed in three rounds, the last clean)

**The cell is traced in full** (`trace/ral.txt`, cell `ral_cell`, five copies s0-s4 west
to east; s0 is RA bit 0's cell, at x 13960-14460): 7 transistors per cell, 35 in the band
(and 98 in the fourteen MA copies, `notes/blocks/mal.md`). Inverter 1 is drawn: it is a
**two-input NOR of node a and `cnt_gab`**, so the cell is a static latch, transparent
while the strobe is high, **whose output `cnt_gab` forces high** (AMB-018 settled as its
second reading). Nothing in the cell drives `cnt_gab` (AMB-017 reading B: no). The device
sizes of re-read item R14 are corrected. Outputs: s0 and s1 join the RA0 and RA1 pad
drivers' input lines (`ra0_drv_in`, `ra1_drv_in`); s2-s4 join r9c's RA2-RA4 comparator-unit
lines and reach the pad drivers through `rad`'s lines: RA2 and RA3 renamed `ra2_drv_in`,
`ra3_drv_in`; RA4 joined only through r9c's `?P` (`ra4_drv_in_u`, aliased).
The hold device's two `?` items were re-read on the group medians and are now drawn firm
(below, "The hold device's two joins"). Left open: where `cnt_gab` and `ral_stb` come from.

### Logic (extracted)

```
ral_a_s#   <- rax_o#            pass transistor 68/25 at (14046,4468) + 434 per cell, gate ral_stb
ral_n1_s#  = NOR(ral_a_s#, cnt_gab)
                                 pull-down 94/22 at (14061,4333), gate ral_a_s#
                                 pull-down Tf 94/20 at (14160,4399), gate cnt_gab
                                 load 35/50 at (14054,4271), gate tied to ral_n1_s#
out_s#     = NOT ral_n1_s#      pull-down 199/22 at (14332,4410) (the extractor's figure for
                                 the Z-shaped gate; about 170 along its centre line),
                                 load 60/37 at (14330,4298)       (out_s0 = ra0_drv_in)
ral_a_s#   <-> out_s#           hold device 16/90 at (14245,4487), gate VSS
```

So, per cell: `out = ral_a OR cnt_gab`; while `ral_stb` is high `ral_a` follows the input
`rax_o#`; while it is low the hold device (believed depletion-mode, gate on VSS: a weak
always-on path, as in `cdp2_lat`) feeds the output back onto node a and the cell holds.
While `cnt_gab` is high the output is high whatever node a holds, and through the hold
device node a is pulled high too, so with the strobe low a high `cnt_gab` **sets** the
latch. `tools/unsure.py --equations`: both equations are FIRM for RA0-RA3 and for all
fourteen MA copies (RA4's output depends on r9c's `?P`). The feedback path is not an
equation; it is the hold device, whose two joins are below.

This does not sit easily with the name: `cnt_gab` is the counters' `_m` to `_mb` transfer
gate line (`mra`, `wl`), which would be expected to pulse every character. A line that
forces all five RA outputs high whenever it is high cannot do that in normal operation.
Either the net is not what its name says at this end (the join is drawn, firm: metal
y 4287, three poly hops), or it is low in normal operation. Not settled here; it bears on
AMB-017.

### Inverter 1: how it was read (2026-11-17 14:14)

Three earlier passes with single shots and the 19-copy median did not resolve it. What
did: **the medians of the two groups kept apart**, over a wider window
(`tools/ral_comp19.py --groups`: `ral_cr`, the five RA copies; `ral_cm`, the fourteen MA
copies turned back). The two groups lie under different metal and beside different
neighbours, so a feature both show is the cell's. The chip-1 metal shot (`metal1`) of
`ral_cm` is the clearest single view (`cache/scratch/ralinv/ev_cm_w.png`, with the trace
over it); poly not under metal is orange and grainy there, diffusion plain.
All views named in this file without a folder are in `cache/scratch/ralinv/`.
Diffusion against field in the open was decided by colour profiles of `ral_cr`
(calibrated on the input strip and on the field beside the hold block: diffusion reads
R-G about 40-46 in the metal shot and 30-35 in the chip-2 stripped shot, field about 20
and 0), under metal by the clean shot (diffusion 195/177/136, field 156-177/130-140/115,
poly over a channel 240/170/124, poly over field 213/168/118).

| Piece | Where (master) | Evidence |
|---|---|---|
| Pull-down on node a | poly bar y 4322-4344 over the diffusion 14014-14108 x 4301-4376 | the bar is orange and grainy in both metal shots; the diffusion's edges cross it as dark lines at x 14010 and x 14108; diffusion colour north (column profile x 14060: y 4301-4313) and south (clean shot under the line's metal, (14060,4360)) |
| Its source | the diffusion south of the bar runs east under the line's metal to Tf's source box and the VSS contact (14118,4423) | one outline: the lower edge y 4378 turns down at x 14105 into the box's west edge (`cache/scratch/ralinv/w5_metal.png`); clean shot at (14130,4362): diffusion |
| Its gate = node a | the bar goes on west over field to x 13984, turns south (x 13984-14006, under the line's metal, no ring), and ends in a buried contact (box 13982-14016 x 4390-4420, heavy outline, light centre) on a diffusion wire y 4395-4410 under the VSS rail, which runs east to x 14086 and south along x 14065-14086 into node a east of the pass gate | `ral_cm` metal1 (`kw1.png`); single shots of s1 in four layers (`b1.png`-`b4.png`); the wire's colour under the rail is uniform 196-204/167-177/134-140 over its whole length (row y 4402, column x 14074), with field (168-177/118-138/101-114) between its east end and Tf's box |
| Pull-down Tf on `cnt_gab` | as before, but the diffusion runs up to y 4352 (W 94, was 66) | channel colour under the line's metal at (14160,4360) |
| Its drain = `ral_n1` | the strip x 14172-14196 widens to x 14206 at y 4352-4368 (a diagonal edge from (14206,4368) to (14196,4386) in both metal shots) and goes north as a strip x 14192-14206 beside the pad's field island to a band y 4274-4292 | `zt1.png`, `nm.png`; clean shot at (14190,4360): diffusion; row y 4282 x 14196-14229: diffusion |
| The pad of `cnt_gab` sits on a field island | outline 14130-14192 x 4290-4350, the poly pad inside it | two nested outlines in every metal view; the ring between them is field. The bar's east end (x 14128) stops 12 px short of the pad on this island (`nk2.png`) |
| `ral_n1` onto inverter 2's gate | buried contact at the top of the Z poly: box 14240-14272 x 4270-4295 with a light centre, the band entering from the west | `zt1.png` (`ral_cm` metal1), `o_s1e_m.png` |
| `ral_n1` north of the bar | the band goes west above the pad's island to x 14128, down a neck x 14113-14128 round the load's corner, into the diffusion north of the bar | the chip-2 stripped shot of both medians shows one light path round the corner (`nk4.png`, `nk5.png`); no edge line across it in the row profile y 4310. The clean shot is murky here (dark red-brown at x 14086-14125) and the chip-2 shots read greener east of x 14086 with no edge between: taken as one region |
| Load | VCC contact (13980,4240) (ring in both metal shots of both medians, specks in the clean shot) on a land 13966-14072 x 4220-4268; strip x 14037-14072 south into `ral_n1`; poly block 14016-14110 x 4246-4296 over it (the strip's edges cross the block at x 14036 and x 14072); buried contact at the block's south-east corner (box 14088-14110 x 4276-4298, light centre) onto `ral_n1` | `top_m.png`, `top_b.png`, `ld1.png`, `ld2.png`, `nk2.png` |

Overlays checked at 3.3-3.8x: s1 west and east halves in the metal and clean shots
(`o_s1w_m.png`, `o_s1w_b.png`, `o_s1e_m.png`, `o_s1e_b.png`), s0's west half
(`o_s0w.png`), MA copies m4 (both halves, `o_m4a_m.png`, `o_m4b_m.png`) and m12
(`o_m12a_m.png`), and the two medians (`ev_cm_w.png`, `ev_cm_e.png`). Full extraction:
0 errors, 0 warnings, no net with several names; every copy gives the same two gates.

### Device sizes (re-read item R14, 2026-11-17 14:14)

| Device | Was | Now | How measured |
|---|---|---|---|
| Inverter 2's pull-down | 61/25 | 199/22 by the extractor (about 170 along the gate's centre line) | the diffusion is one piece 14229-14362 x 4322-4447 (stepping in to x 14252 below y 4391), and the whole Z-shaped poly is gate: west leg x 14247-14270 (source strip x 14229-14247 west of it, drain east of it above y 4353), middle leg y 4353-4374 (drain north, source south), east leg x 14321-14344 (source west, drain east). Row y 4335, column x 14295, row y 4410, column x 14333: channel colour under metal on the middle and east legs, diffusion colour both sides of each leg. South of the middle leg the chip-2 metal shot reads greener at x 14248-14281 than on the source strip, with no edge between and uniform in the chip-1 metal shot (`zg1.png`): taken as the same diffusion |
| Inverter 2's load | 61/32 | 60/37 | block 14283-14395 x 4279-4316 (it overhangs the strip's west edge by 15 px: column x 14289 is poly) |
| Pass transistor | 16/26 | 68/25 | gate poly x 14033-14058 (row y 4465: edges at x 14031 and 14059), top end y 4421; diffusion under it from y 4434 (edge under the poly in the clean shot, column x 14047) to y 4502 (edge across the poly in the metal shot), with no edge between; diffusion both sides (west: clean shot green at y 4455-4470 and tan under the rail at y 4437-4446; east: the wire x 14065-14086) |
| Tf | 66/20 | 94/20 | above |
| Hold device | 16/90 | unchanged | not re-read |

Ratios: inverter 1 (94/22) / (35/50) = 6; inverter 2 (199/22) / (60/37) = 5.6.

### The hold device's two joins (2026-11-17 14:14; were `?P` and `?B`)

- **Gate pad to gate block** (`P 14200,4440:14246,4452`): the dark line at y 4447 between
  them in the metal and chip-2 stripped shots is the VSS rail's edge. In the clean shot,
  which has no metal, the columns x 14210, 14225 and 14240 of both group medians pass
  from the pad's colour (about 215/165/113, poly under metal) to the block's (about
  140/80/50, poly in the open) with no edge line: the darkest point at x 14225 is
  128/79/52 (RA) and 133/72/51 (MA), where an edge reads 40-80/30-50/20-35 (columns
  x 14190 and x 14256 beside the pad, same rows). The west outline x 14200 runs unbroken
  from y 4400 to the block's foot in the chip-1 metal shot of both medians (`h1.png`,
  `h3.png`). Nothing else comes near the block, so its gate is the pad: VSS.
- **Strip to output poly** (`B 14315,4472:14347,4500`): a box 14320-14347 x 4474-4500
  with a heavy outline and a light centre, at the west end of the output poly's bend (the
  poly's orange starts at the box's east edge), with the strip entering from the west
  (diffusion colour at x 14298-14304 on the row y 4487). It looks like the cell's three
  other buried contacts in the chip-1 metal shot of both medians and the chip-2 stripped
  shot of the MA median (`h1.png`, `h2.png`, `h3.png`), and was already a heavy-outlined
  patch in the clean shot's single views.

Both were promoted in this pass on that evidence; a reviewer should look at them once
more, because the latch's feedback rests on them and on nothing else.

### What the cell does with `cnt_gab` (AMB-017, reading B: no)

The line y 4346-4362 crosses each cell over, from west to east: the bar's southward poly,
the VSS diffusion, Tf's gate, `ral_n1`'s strip, a field island, inverter 2's source strip,
the Z poly's middle leg (which lies under the metal for 100 px: trap 13), the output strip
and the output poly. Its only connection is the tab to Tf's poly pad (contact
(14157,4318)). No ring anywhere else along it in either metal shot of the five-copy
median at 5x (`ln1.png`, `ln2.png`), no contact patch in the clean shot under it (green
minus red along y 4350-4358 is positive only at two 3 px edge crossings, x 14204 and
x 14362), and the pad's poly leaves only southwards, as Tf's gate. **So the cell only
reads `cnt_gab`.**

### Where `cnt_gab` is driven: every end looked at, none found (2026-11-17 05:08)

The net as now drawn: band H4 (poly y 7200-7225, x 11043-12910), the counters' line
x 12902 (y 7200-16943), the metal from `wl`'s contact (11392,7210) north to the
cross-under, the metal y 4287 and the line through the five cells. Ends and taps
looked at:

| Place | Result |
|---|---|
| H4's west end | ends at x 11043-11055 in a closed outline, with nothing leaving it north or west (four shots at 3.5x and 5x, `cache/scratch/gab/h4c.png`, `cache/scratch/ral/h4w.png`, `h4n.png`); the metal x 11025 beside it is `rc0_n`, no ring. **`wl`'s notes say H4 "runs on west into the bus field": it does not** |
| H4 itself, x 11060-12900 | a colour scan of the clean shot along the band (G minus R, which picks out a contact's green centre) finds only the two known contacts (11392,7210) and (12889,7214), plus three spots at x 12121, 12299, 12467, which are not contacts (4x mosaics in both shots, `h4c1.png`, `h4c2.png`: no ring, only the band crossing under a metal) |
| H4's east end | the contact (12889,7210) onto x 12902; no poly beyond (`h4e.png`) |
| x 12902's bottom | ends free 55 px above `ck_b`'s contact (`mra`'s notes) |
| the north metal's contact candidate (11393,6965) | not a contact: polys crossing under (four shots at 4x, `g2.png`) |
| its corners (11249,5612), (11396,5615) | plain corners (3.4x, `co.png`) |
| the pad (11243,4284) | poly east only (`pd.png`) |
| the line's east end | stops at x 16255 over cell s4's output poly, with no contact, as in the other cells (4.5x, `be2.png`). The first draft ran it to x 16330, onto the wide metal there: corrected |

| the counters' line x 12902, y 7240-16930 | the same colour scan finds only `mra`'s per-row gate contacts of the pass transistors (y 10515, 13161, 15134, 15610, 16088 ..., checked at 4x, `g12m.png`, `g12a.png`) and a spot at y 7299 with no ring in either metal shot (`g7299.png`) |
| its bottom end | free, 30 px above the metal at y 16975 (four shots at 4x, `gbot.png`), as `mra` found |

So no gate output drives `cnt_gab` anywhere along the drawn net, and nothing in the
trace connects it to a supply. H4 and x 12902 are now both ruled out (above), and so is the north branch:
the same colour scan along x 11242 (y 4300-5612), y 5614, x 11396 (y 5614-7200) and
y 4287 (x 11700-13820) finds only the known pads at the ends, plus six spots (x 11242 at
y 4508, 4638, 4726, 5100; x 11396 at y 6352, 6940) which at 3.4x in both shots are polys
crossing under continuous metal, with no ring (`nb1.png`, `nb2.png`).

**So the whole drawn net of `cnt_gab` has no driver.** Two possibilities were left. (a) A
contact where the colour test fails, under a wide metal, for instance where the north branch
passes under the supply metal x 11280-11600. (b) The net is driven inside the RA band
cells. **(b) is now ruled out** (2026-11-17 14:14, "What the cell does with `cnt_gab`"
above): with the cell traced in full, the line's only connection in each cell is the gate
of the pull-down Tf. (a) is what is left, together with (c): the line through the fourteen
MA copies (below, "Not done" 3), which has not been followed and may be the same net.

### Inverter 2, from the median of all nineteen copies (2026-11-17 06:23)

`tools/ral_comp19.py` builds the median of the five RA copies and the fourteen MA copies
(turned back into the master's frame) as composite `ral_c19`. At 4.2x in the clean shot
it shows what single shots and the five-copy composite did not
(`cache/scratch/ral/c19l.png`, `c19r.png`, `c19t.png`; overlay `c19ov.png`):

- load: VCC contact (14330,4252) (ring in the metal shot) onto a land, gate block
  14295-14395 x 4280-4312 tied to the output poly x 14372-14395;
- output node: diffusion under the load and down x 14345-14370; buried contact
  14365-14410 x 4418-4450 onto the output poly;
- pull-down: the L-shaped poly (x 14320-14345 down to y 4452; west along y 4350-4372;
  up x 14255-14280 to y 4320) between the VSS-contacted box 14255-14330 x 4385-4445
  and the drain strip.

Extracted: `ra#_drv_in = NOT ral_n1_s#` (`_u` for RA4) for all five RA
copies (and for the fourteen MA copies in `trace/mal.txt`). The pull-down's size was
re-read on 2026-11-17 14:14 (the whole Z is gate: "Device sizes" above). Three passes at
inverter 1 with this composite did not resolve it; the fourth, with the two groups' medians
kept apart, did ("Inverter 1: how it was read" above).

### Ports

| Name | Layer | Where (s0; +434, +868, +1431, +1865 for s1-s4) | Direction | What |
|---|---|---|---|---|
| `vcc` | metal | top rail y 4220-4268 (drawn from x 13960: its west end in s0 is at x 13955) | supply | by device orientation, not followed to a labelled rail |
| `vss` | metal | middle rail y 4397-4446 | supply | same |
| `cnt_gab` | metal | y 4346-4362, x 13895-16258 | in | the counters' `_m`/`_mb` gate line: drawn back to `wl`'s band H4 (glossary); this block's first name for it is in the glossary's former names |
| `ral_stb` | metal | y 4540-4556, x 13990-15910 (ends on s4's pad) | in | the sixth line of rab's bundle; drawn back 9,000 px to x 8350, where it is `tc1`'s nested metal ns4 (renamed; the old name is in the glossary's former names) |
| `rax_o0` | poly | (14000,4500), from rab | in | s0's input, onto the strip by a buried contact (the same heavy-outlined square in all five copies and both stripped shots, 4x mosaics `bin.png`, `bin2.png`) |
| `rax_o1` ... `rax_o4` | poly | up x 13995 + dx from pads at (14430,4590), (14863,4635), (15425,4675), (15860,4632) to the buried contact on each strip | in | s1-s4's inputs; s2's and s4's pads at the ends of rab's metals (s4's goes on east along y 4722 to x 15862 and north) |
| `ra0_drv_in` | poly | x 14331-14349 at y 4480-4525, joins r9c's poly from the pad (14340,4764) | out | s0's output |
| `ra1_drv_in` | poly | s1's output poly down to a pad (14774,4592) on RA1's line y 4592 | out | |
| `ra2_drv_in` | poly | s2's output poly down to a pad (15208,4805), where r9c's RA2 unit line starts | out | |
| `ra3_drv_in` | poly, metal, poly | s3's output poly to a pad (15771,4593), metal east along y 4590 and south along x 16297, poly to a pad (16297,5108), where r9c's RA3 unit line starts | out | |
| `ra4_drv_in_u` | poly, metal, poly | s4's output poly to a pad (16205,4640), metal south along x 16207, poly to a pad (16205,5153), where r9c's RA4 unit line starts | out | |
| `ral_a_s#` | diffusion, poly | inside the cell | internal | node a: east of the pass gate, the strip to the hold device, the wire under the VSS rail and the bar (gate of inverter 1's pull-down) |
| `ral_n1_s#` | diffusion, poly | inside the cell | internal | inverter 1's output: north of the bar, Tf's drain, the band above the pad, the Z poly |

### How sure

- Inverter 1, the sizes and the line: the three sections above.
- Rails, line taps, contacts: metal composite and single shots at 2.6-4x; overlay
  `cache/scratch/ral/ov1.png`.
- The input strip: colour profile along y 4486 in both stripped shots
  (`tools/ral_prof.py row 4486 13985 14460 5`): not field from x 14015 to 14315, field
  at 14320-14340, again not field 14345-14390 (the output poly's horizontal piece).
  Down x 14120: diffusion at y 4479-4491, field at 4458-4467 (a field moat between Tf's
  box and the strip; Tf's poly runs on 16 px over it and makes no second device).
- Copies: `cellcheck.py ral_cell --layer acid` (before this pass): s1 0.6 %, s2 4.2 %,
  s3 1.2 % bad blocks; s4 15 %, all of it the strobe line ending at s4's pad and a wide
  rail at the band's east edge, outside the drawn devices.

### Ambiguities

1. The hold device's two joins are drawn firm on the evidence above; they are the only
   support of the latch's feedback and deserve an independent look. That the device is
   depletion-mode (conducting with its gate on VSS) is believed, from `cdp2_lat`, not seen.
2. The west end of the load's poly block (x 14016-14036) is drawn over field: the land's
   outline turns up round it in the clean shot (`top_b.png`), and under the rail it reads
   210/141/100 against 231/156/119 on the channel. If the land runs under it the load is
   wider; no net changes.
3. Two places where diffusion changes shade with no edge line (east end of `ral_n1`
   north of the bar; south of the Z's middle leg) are drawn as one region each.
4. The input buried contact at the strip's west end (`?` in the trace's comment, drawn
   `B`) was not re-read.

## Review

Round 1 (2026-11-17, an independent agent, single copies s0-s3, m4, m9, m12 and both group
medians at 5x+): see below; its findings (notes nits, a diffusion item overhanging Tf's
gate by 2 px) were fixed.

Round 2 (2026-11-17, an independent agent, single copies s3, m7 and m0 at 5-7x): one
finding: the Round 1 fix (diffusion item trimmed to x 14150) had removed the diffusion under
Tf's gate at y 4352-4370, so Tf extracted as 77/20; the photo shows diffusion on both sides
there (gate poly continuous from y 4338 to 4455). Restored to x 14172: Tf 94/20 again in all
19 copies. Everything else re-checked right (load, bar pull-down and its gate wire, pass
gate 68/25, the `ral_n1` band by colour against known diffusion, inverter 2, the hold
device in four layers).

Round 3 (2026-11-17, an independent agent; the Tf fix against an extraction of the previous
commit: only the 19 Tf lines changed, 77/20 to 94/20, same nets; fresh copies s4 and m11 at
5x in four layers, judged without the trace first; the notes' sizes, counts and equations
against the extraction).

Re-read of the force line and the strobe (2026-11-17, an independent agent, every hop at
4.4-6x in both stripped shots and both metal shots), because a force line that is the
counters' transfer line does not fit: the cross-under at x 11150-11720 (three polys, none
steps), the metal y 4287, the hop at (13822-13905, 4285-4350), the metal x 11242 and
x 11396 down to band H4 at (11392,7212), and the strobe's route back to `tc1`'s ns4 with
its three poly hops on y 2768: no swap and no wrong join. The contradiction is therefore
not in these routes: it is in what band H4 / the line x 12902 does (`wl`'s and `mra`'s
reading) or in an undiscovered driver (AMB-017).

### Round 1 details: inverter 1

Independently reviewed on single copies s0-s3, m4, m9, m12 and both group medians at 5x+:
inverter 1 = NOR(node a, `cnt_gab`) confirmed device by device (the bar's gate wire to
node a, its VSS source, the drain and load on one net, both buried contacts on `ral_n1`);
nothing in the cell drives `cnt_gab` (AMB-017 reading B: no); the R14 sizes confirmed
within edge width (inverter 2's load measured about 64/40 against the drawn 60/37); the
hold device's poly join and buried contact read firm in all 19 copies (the latch's
feedback rests on these two); overlays on s0, s1, m4, m12; extraction against the
previous cell: only the cell's own devices changed, nets fell by exactly 19.

Round 3: no findings.

## Not done (next)

1. `cnt_gab`'s driver (AMB-017, reading A), and whether a line that sets the RA outputs
   can be the counters' transfer gate line (above).
2. The hold device's size (drawn 16/90; the block's foot is at about y 4508, not 4500,
   which changes nothing electrically) was not re-read.
3. **The fourteen MA copies have a common line too**: a thin vertical metal at x about
   2700 runs through the column past the copies' pads (seen from y 10250 to 11350 in both
   metal shots, with tabs to the pads of m4 and m5, `cache/scratch/ralinv/frc.png`; it is
   the image of this band's line y 4354, and the MA median shows it right across the
   cell). `mal` names each pad `mal_frc_m#` as a port of its own; the line is not drawn
   and its ends are not looked at. If it joins `cnt_gab`, one line sets all nineteen
   address outputs.
4. `ral_stb`'s source.
5. The twentieth copy, at (8449,5562), is not placed (`notes/blocks/mal.md`).

## History: earlier passes (superseded by the Status above where they differ)

## First survey

Serial work, 2026-11-16. Survey only. Views in
`cache/scratch/rax/`: `ral1.png`, `ral2.png` (the band at 1.55x), `ralA.png`, `ralM.png`,
`ralC.png` (the master cell at 2.8x in the clean, metal and chip-2 stripped shots),
`ralq1.png` ... `ralq4.png` (its four quadrants at 3.6x), `ram1.png` ... `ram3.png`.

## What it is

A band of five copies of one cell, about 430 x 260 px. `tools/findcell.py` with the cell
at x 14020-14450, y 4265-4525 as master (clean shot):

| Copy | dx | Score |
|---|---|---|
| master | 0 | 1 |
| 2 | 434 | 0.93 |
| 3 | 868 | 0.89 |
| 4 | 1431 | 0.94 |
| 5 | 1865 | 0.84 |

and **fifteen more hits elsewhere, turned 90 degrees** (scores 0.78-0.82): fourteen in
the left array's untraced left column at x 2660 (y 8155, 8761, 9368, 9976, 10627, 11234,
12036, 12730, 13382, 15506, 16201, 17275, 17925, 18576; some mirrored), which is where
the `maN_drv_in` lines start, and one at (8449,5562), in the untraced corner below the
central datapath's top block. So this cell is the common stage in front of every memory
address and row address output: nineteen or twenty copies. Trace it once, check each
copy's ports.

## Ports of the master, as far as read

- **Rails**: a wide metal along the top (y up to 4270), a wide metal y 4395-4442 with
  contacts to two diffusion boxes (pits at (14117,4423) and (14262,4422)) and to a poly
  pad (14210,4420). Pull-down gates cross the diffusion beside both boxes, so the
  middle rail is taken to be VSS and the top one VCC (not followed to a labelled rail).
- **A thin metal along y 4350** through all five cells, with a tap up to a poly pad at
  (14156,4318) in each. Its poly (x 14148-14170) comes down across the diffusion under
  the middle rail, between the contact box at x 14100-14145 and a node at
  x 14172-14192: a pull-down gated by this line. Where the line comes from: not followed.
- **The sixth line of the row address bundle** (`notes/blocks/rab.md`): metal along
  y 4548 under the band, with a pad per cell ((14040,4548) for the master) and a poly up
  x 14035-14055 to y 4420. On the way it crosses a horizontal diffusion band
  (y 4478-4500): read as a pass transistor. So this line is the cell's strobe; the same
  cell in the left column sits beside the `ck_out` trunk, whose taps come every 608 px.
- **The poly pad on the middle rail** (14210,4420) goes down to two wide poly bars
  (x 14200-14292, y 4452-4472 and 4478-4502) over the diffusion bands there: the shape of
  the long weak device with its gate on VSS that the register latches use (`hold`).
- **Output**: an S-shaped poly, vertical at x 14372-14395 from y 4320 through the middle
  rail to y 4500, west to x 14345, south along x 14340-14362 to the pad (14340,4764),
  whence metal to the RA0 driver's poly at (15305,4762).
- **Input**: not placed. `rax_o0`'s poly arrives along y 4500 at x 14000 and `rax_o1`'s
  comes up x 14430 from the pad (14430,4590), i.e. at the left edge of the next cell.

A pass transistor on a strobe, two inverters and a weak feedback device is the static
latch of the register rows (`cdp2_lat`), so the working guess is: **each RA and MA
output is latched, transparent on the line y 4548 (RA) or `ck_out`'s trunk (MA)**, and
can be forced by the line y 4350. A guess until the cell is traced.

## Not done

The cell itself, device by device (start from the chip-2 stripped shot: most of the cell
has no metal over it); the two rails and the lines y 4350 and y 4548 to their sources;
the other four copies' inputs and outputs; the fifteen copies elsewhere.

## 2026-11-16 23:07  Second look (contributor session): readings before drawing

Median composite of the five RA copies: `composite.py ral_c 13990,4240:14460,4600
--offsets "0,0 434,0 868,0 1431,0 1865,0"`. In this band the chip-2 stripped shot (`acid`)
of the composite is the clearest view of poly; `classmap.py --comp ral_c --open` helps
with open diffusion. At 4x the composite is too blurred for junctions: use single shots
there.

Read (one or two views each; to be confirmed by overlay before drawing):

| Feature | Where | Reading |
|---|---|---|
| Top rail | metal y 4220-4270, whole band | joins a wide vertical metal at x 14950-15100 going north (survey at 0.4x). Load-shaped poly blocks hang below it (e.g. 14300-14360 x 4275-4305 over a diffusion strip): taken as VCC |
| Middle rail | metal y 4395-4447, whole band | contacts to diffusion at (14117,4423) and (14265,4415), and a contact to the poly pad 14200-14246 x 4398-4446 (green centre in the clean shot) at about (14222,4422): taken as VSS |
| Line y 4350 | metal y 4343-4359 | metal tab up to the poly pad 14142-14176 x 4303-4346, contact (14157,4318) |
| Pull-down Tf | poly x 14150-14170, y 4346-4466, over diffusion 14102-14196 x 4378-4448 | source on the VSS contact (14117,4423); drain the strip x 14172-14196. Gate = line y 4350. The poly runs on 20 px below the diffusion box (to y 4466) over a strip y 4450-4470: possibly a second device, not settled |
| L-shaped poly | 14245-14345 x 4325-4370, then down x 14325-14345 to y 4448 | crosses the diffusion box 14252-14365 x 4378-4448 (contact at about (14265,4415)) as a pull-down gate; drain x 14348-14365 |
| Output poly | vertical x 14375-14395, y 4300-4500 | as in the first survey |
| Two poly bars | 14200-14290 x 4455-4473 and 4480-4500, inside an outlined box 14195-14300 x 4450-4505 | joined to the VSS pad above? Not settled (the dark line at y 4447-4452 is not resolved at any zoom tried) |
| Strobe pass device | poly x 14028-14053, y 4440-4535, contact pad 14025-14058 x 4530-4562 on the metal y 4548 | crosses a horizontal strip y 4478-4500 (seen in both stripped shots) |

Open: whether the drain of Tf joins the VSS-poly pad side (x 14196/14200), how node a
reaches the gates, and where the diffusion strips y 4450-4470 and y 4478-4500 end on the
right (one turns up at x 14390-14420).
