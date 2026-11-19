# busl: the left bus field

Queue row `busl` of `notes/work-packages.md` (written busL until 2026-11-19): the wiring between the
left array (`larr`, rows end at x 4780) and the central datapath (`cdp3`, `cdp4`, from x 7600).
Claimed region: x 4780-7550, y 10400-15000 (the main part; the northern part 6450-7600 x 6750-10400
is not started). Coordinates are metal-shot pixels; images are in `cache/scratch/busl/`. Wiring only:
no transistor has been found in the field so far.

## Status

Run 1 (richtw1's session, Claude Fable 5.2; 2026-11-19 13:50 to 14:00 +0100). Survey of the whole main
part, and one piece, `h8`, wiring only, no uncertain items:

- **The eight west outputs of the central datapath's register row H reach eight rows of the left
  array** (piece `h8`). Each `cdp3_hw_c#` (# = 7..0; `cdp3`: hw = NOT q1 of the 8-bit register row H)
  is drawn end to end across the field: a poly row west from `cdp3`'s piece at x 7600, a pad, a metal
  track south round one step of a staircase, a pad, and a diffusion row west to the array's edge at
  x 4780. The order is kept: c7 goes to the northernmost row (y 11338), c0 to the southernmost
  (y 14894); seven of the eight rows are 477 px apart, the array's row pitch.

Full extraction with run 1: 2,382 nets (unchanged: the eight wires lengthen `cdp3`'s nets), 4,290
transistors, 0 errors, 0 warnings. The package by itself: 8 nets, 0 errors, 0 warnings.

## Inventory

The field (survey: `cache/scratch/busl/survey.md`; views `s0_metal.png`, `s0_acid1b.png`):

- About 55 vertical metal tracks at a pitch of 43.4 px between x 4822 and x 7554, stepping sideways in
  staircases; most run on north of y 10400 and south of y 15000. A wide metal x 4960-5010 runs the
  whole height. Track centres at nine heights: `tools/sel_cut.py h Y 4780 7560 --brief`.
- Horizontal lines of two kinds (told apart in the open column x 5072, `tools/busl_rows.py`,
  `tools/px.py`): **diffusion rows** about 22 px wide (chip-2 metal shot blue 80-87; clean shot cream
  160/128/98 between two dark edge lines) and **poly rows** about 28 px wide (blue 52-57; clean shot
  154/90/61 in the open).
- Poly row bands under the tracks at y 10330-10700, 11850-12150, 12550-12900, 13300-13700, 14050-14300
  (`bc1`'s 13-line bus enters it from the east), 14450-14950.
- Drawn by others inside the region: `trunks` (two lines), `bc1` (the bus, lower right), `tla` (7 items).

Piece `h8` (all eight nets have the same build; `#` = the slice of `cdp3`'s row H):

| Net | Poly row y (x from the pad to 7600) | North pad, contact | Track: upper x, step y, lower x | South pad, contact | Diffusion row y (x 4780 to the pad) |
|---|---|---|---|---|---|
| `cdp3_hw_c7` | 10361 | (6039,10359) | 6039, 11272, 5690 | (5690,11335) | 11338 |
| `cdp3_hw_c6` | 10404 | (5996,10402) | 5996, 11230, 5626 | (5647,11812) | 11815 |
| `cdp3_hw_c5` | 10447 | (5953,10445) | 5953, 11186, 5583 | (5605,12290) | 12291 |
| `cdp3_hw_c4` | 10490 | (5909,10488) | 5909, 11142, 5540 | (5562,12766) | 12768 |
| `cdp3_hw_c3` | 10535 | (5866,10533) | 5866, 11100, 5496 | (5514,13222) | 13247; steps north at x 5432 to y 13220 |
| `cdp3_hw_c2` | 10577 | (5822,10575) | 5822, 11054, 5452 | (5474,13722) | 13725 |
| `cdp3_hw_c1` | 10621 | (5778,10619) | 5778, 11012, 5409 | (5427,14197) | 14202 |
| `cdp3_hw_c0` | 10664 | (5735,10662) | 5735, 10966, 5366 | (5385,14888) | 14894 |

- The poly rows run straight for 1,560-1,870 px under about forty tracks each; no track has a pad
  over them (views `b1_acid1b.png`, `b1_metal.png` at 1.3x).
- The north pads are a staircase of poly pads, each the west end of its row, each with the north end
  of its track on it (`t1.png`).
- Each track leans about 20 px east into its south pad (c7's comes straight down); the track ends
  there (`tools/follow.py --gap 16` from each track both ways; `e1.png`, `e2.png`, overlays `o1.png`,
  `o2.png`, `o3.png`).
- Seven of the tracks cross the diffusion rows of the nets north of their own pad, and the poly rows
  of other nets, without contact: `tools/tl5_tracks.py v X Y0 Y1` down each lower track shows only
  pairs of 8-17 px dark bars (the two edges of each row) and no stretch without metal in both chips;
  the clean shot's short greenish stretches (6-10 px) lie on the south edge of each diffusion row and
  nowhere else.

## Logic

Wiring only. Traced: the eight joins above (no uncertain item on any). From `cdp3`'s notes:
`cdp3_hw_c#` = NOT q1 of the row H register bit of slice c#, so **the left array's rows at y 11338 ..
14894 each take one bit of register row H, inverted**. Believed, not traced: these eight rows are
eight of the fourteen rows of the memory address counter, and row H is the low byte of a 14-bit
address register (R13, the display start, or R15, the cursor; `regs` is the queue row that decides).
What the rows do with the bit is `larr`'s untraced part (x 3900-4720).

## Ports

| Name | Layer | Where | Direction | What |
|---|---|---|---|---|
| `cdp3_hw_c7` .. `cdp3_hw_c0` | P | x 7600, y 10361, 10404, 10447, 10490, 10535, 10577, 10621, 10664 (18 px wide) | in | `cdp3`'s channel G west pieces, drawn there from x 7600 |
| `cdp3_hw_c7` .. `cdp3_hw_c0` | D | x 4780, y 11338, 11815, 12291, 12768, 13247, 13725, 14202, 14894 (20 px wide) | in (driven in `cdp3`) | on west into the left array's rows; `larr` draws nothing east of x 3900 |

## Ambiguities

1. **Red patches on the poly rows in the clean shot** (for instance (6340-6385,10353),
   (6095-6140,10530), (6160-6200,10660); each one track wide). Readings: a contact or a channel
   under that track; or a colour difference of chip 1's stripped shot only. Assumed the second:
   neither chip-2 shot shows anything there (the track keeps its width, no ring, no pad; `q1.png`
   at 3.2x, three shots), and a crossing field without pads carries no taps (guide, trap 15).
   Would settle it: nothing more in these photos; the patches' pattern over the whole band could be
   listed and compared with where the tracks' own contacts are.
2. **The rows' layer.** Taken as diffusion from the colours above; a poly row would make no
   difference to any connection here (nothing crosses the rows but metal).

3. **The poly L round c3's south pad** (the pad (5514,13222); a poly runs east along y 13258-13272
   and north along x 5545-5560, at minimum spacing from the pad's south and east edges). The round-1
   reviewer could not resolve the two outlines at 6x in the clean shot. Read by the tracer in the
   chip-2 shots at 5x (`c3s.png`): the pad's outline is closed and a pale strip 3-4 px wide lies
   between it and the poly's outline on both sides; `tools/px.py col 5515 13236 13276 2`: pad to
   y 13244, dark to 13258, poly (chip-2 stripped shot 157/116/63) from 13260. Taken as apart; there is
   no buried-contact box. The poly L itself is not drawn (not this piece's).

## Review

**Round 1: full review** (2026-11-19 14:05 +0100; a fresh Fable 5.2 reviewer agent; commit 59157c2; piece `h8`).
Told to suspect: the track staircase's order, the north pad staircase, the poly rows (a step, a
break, a tap, the red patches), each south pad (which track is on it, whether it ends), the lower
tracks' crossings, the diffusion rows (straight, their layer, c3's step), a shift by one row at x 7600.
Checked (25 images in `cache/scratch/busl/review-1/`): both pad staircases and the track staircase at
3.4x in the metal and clean shots, with `tools/follow.py --gap 16` on every track; the poly rows by an
edge-pair measurement every 7 px on the chip-2 metal shot to x 7618 (offset 0 to -2 px, width 23, no
step, no break) and views at 1.6x (no pad on any track); two red patches by `tools/textmap.py --acid`
(colour only); the nine rows at x 7600 (the ninth, y 10317, ends on its own pad near (6730,10315);
the eight drawn are the southern eight); each south pad at 4x in two shots; c3's step in three shots;
the lower tracks by `tools/tl5_tracks.py v`; a diagonal poly under c1 and c2 at (5400-5470,13395-13465)
and a pad (5408,14347) beside c0's track (neither touches); the diffusion rows in three shots (chip-2
metal blue 78-87: diffusion).
Findings: none. Could not check: (a) whether the poly L south and east of c3's pad touches the pad
(would change a connection): read afterwards by the tracer in the chip-2 shots, apart (Ambiguity 3);
(b) the diffusion rows and lower-track crossings were read at 1.4x and by text tools, not at 4x;
(c) `cdp3` has no `ports.d` file, so the join at x 7600 rests on the photos and the rows' y.
Nothing changed in the trace.

Round 1: no findings.

## Not done

- Everything else in the field: about 47 more tracks and all the other rows. Next pieces, in the
  order they join things: (1) the tracks that continue the eight lower track positions south of the
  pads (other metal pieces on x 5409-5626 start below each pad) and the poly rows y 11488, 11920,
  12441, 12980, 13397, 13875, 14350 that cross x 5072 (the second set of lines from the array, 477 px
  apart: 11488, 12441, 13397, 13875, 14350); (2) the top band's ninth row (y 10317, `cdp3_gate_f`) and
  the three poly rows at the top left (y 10560, 10686, 10736); (3) the staircases at x 5100-5700,
  y 10600-10960 west of piece `h8`'s; (4) the bands at y 11850-12150 and below.
- The diffusion rows west of x 4780 (`larr` (continue)).
- The northern part (6450-7600 x 6750-10400).
- `trunks`' two lines in the field: taps not checked (R4).
