# rde: the data bus through the central datapath's rows D and E (y 5150-5700), and to R10's two west slices

## Status (2026-11-17 11:15 (UTC+1), contributor session; independently reviewed)

Wiring only (`trace/rde.txt`), no transistors. Drawn: the five slice bit lines of `cdp1`
(`db_b4`..`db_b0`, data bits 4..0) from `cdp1`'s drawn ends (y 5150) through
rows D and E to `cdp2`'s bus lines (`cdp2_a_s3_bus`..`cdp2_a_s7_bus`, y 5700); data bit 6
from (8075,5040) to `db_b6`; data bit 5 from `db_b5`'s tap (8727,5150) to
`db_b5`. **One 54 px stretch of each of the five lines (y 5542-5596) is drawn
`?M`: an assumption, see below.** Rows D and E themselves are still not traced.

Slices: `cdp1` c1..c5 = `cdp2` s3..s7, x = 8856 + 390 k (k = 0..4), data bits 4, 3, 2, 1, 0.

## Result

`tools/bust_fanout.py` on the full extraction:

| Data line | Write strobes |
|---|---|
| bits 0, 1, 4 | R0-R2, R4-R9, **R10, R11** (via the `?M` stretch) |
| bits 2, 3 | R0-R2, R4-R7, R9, **R10, R11** (via the `?M` stretch) |
| bit 5, bit 6 | R0-R2, R4, R6-R8, **R10** |
| bit 7 | R0-R2, R8 |

So `wr_r11` is on bits 0-4 and `wr_r10` on bits 0-6: the datasheet's R11 (cursor end
raster, 5 bits) and R10 (cursor start raster, 5 bits, plus bits 5-6, the blink mode).
`cdp2` row A is R11 with s3..s7 = bits 4..0; row C is R10 with s1 = bit 6, s2 = bit 5,
s3..s7 = bits 4..0. 3430 transistors before and after; 0 errors, 0 warnings.

What the check does and does not show: bits 5 and 6 arrive on firm geometry by routes
that have nothing to do with rows D/E, and they land on s2 and s1 in the order that
continues s3..s7 = bits 4..0. For the five lines the check is satisfied by any reading
in which the lines join at all; it does not test the `?M` stretch.

## The five lines through rows D and E

Method: `tools/rde_dim.py` (dark stretches along a thin line, per slice, both metal
shots), `tools/rde_edge.py` and `tools/rde_xs.py` (cross-profiles), sub-pixel medians of
the five slices (`tools/cdp1_sr.py`) at 4x-8x in four shots, and the five slices singly
at 5x. Images in `cache/scratch/rde/`.

- **y 5150-5542**: bright metal x (xc-7)..(xc+5), xc = 8856 + 390 k. Dark stretches of
  4-14 px in all five slices at y 5166, 5183-5196, 5385, 5403, 5413-5423, 5451-5460,
  5481, 5509-5517: edges of poly and diffusion underneath. The longest (y 5183-5196) is a
  thin poly; the metal's two edge lines run straight through it (`sr_5190.png`, 5x).
  No pad, ring or widening (`sv4.png`, `srm_5375.png`).
- **y 5596-5700**: bright metal x (xc-5)..(xc+11) (4 px east of the upper piece, and
  wider), crossings of 5-11 px at y 5601-5606, 5632-5639, 5670-5677, 5683-5690. No pad.
- **y 5542-5596, the stretch in question.** In both metal shots and all five slices the
  bright metal fades out at y 5540-5547 (tapering to its west side) and comes back at
  y 5593-5600 as a blob x (xc-7)..(xc+11). In between there is no bright metal on the
  line. What is there:
  - Underneath (`acid1b`): a diffusion column x (xc-18)..xc, y 5512-5590 (flat tan, the
    colour of the VSS diffusion under the rail beside it), a heavy dark line along its
    east side x (xc-2)..(xc+4) from y 5545 to 5588, and east of that the poly pad
    (xc+6)..(xc+60) x 5548-5588 of the next track's contact (xc+42,5562). A thin bar
    crosses the column at y 5557-5567: black in `metal`, `metal1` and `acid` from
    x (xc-25) to (xc+3) (the column only; review), two faint lines with a pale band between in `acid1b`. Below
    y 5590 the line is over bare field (pink).
  - Metal layer: `metal1` is dark over x (xc-8)..(xc+2) (44-59, against 82-99 on the open
    part of the column at xc-14) where `acid1b` is flat; `metal` is dim there (62-106).
    The dip of the line's west edge at xc-10 is present above, in and below the stretch.
    A strip x (xc+6)..(xc+10) is bright (95-150, the level of poly in the open, below
    metal's 165-190) at y 5548-5556 and 5566-5590, and one 6-8 px edge line (not a
    metal-to-metal gap) separates it from the pad's metal.
  - At y 5557-5567 everything is black; nothing can be seen across the bar.

  Readings considered:

  1. **Continuous (adopted, drawn `?M` w=10).** The metal's west edge is seen on both
     sides of the bar (y 5547-5556 and 5570-5586, all five slices, both metal shots), so
     only y 5557-5568 (about 12 px) is unseen. Read as the line narrowing to about 10 px,
     x (xc-8)..(xc+2), to clear the pad metal of the contact at (xc+42,5562), whose west
     edge is at about xc+16; a 10 px metal is all edge line and reads dark. The bright
     strip is the poly pad seen in the gap. For it: the metal-layer darkness with nothing
     underneath, the continuous west edge, the taper at the top and the wide blob at the
     bottom, and that neither end can be an end: there is no contact pad, no room for one
     (the smallest contact metal seen elsewhere is 14 x 40), no contact marks on the
     column in `acid1b` (the VSS contacts at (xc-63,5430) and (xc-63,5655) show theirs
     plainly in the same median), and the lower piece's top is over bare field.
  2. One long narrow contact from the line to the column (a tap into row E). Same net as
     reading 1. Against: the bar crossing the column inside it.
  3. Two pieces, each with a small contact onto the column on either side of the bar,
     the bar being a poly finger from the pad: a transistor in series with the line,
     gate on the pad's net. **This is the reading that would make the join wrong.**
     Against: two contacts of about 10 x 12 and 10 x 16 px, with no pad; no contact marks;
     a per-slice gate for a bus switch. Not excluded by sight.

  The two honest passes (medians, then profiles and single slices) do not show metal
  across the stretch directly, so the join of each of the five lines is an assumption and
  is listed by `tools/unsure.py`. Do not rename the `cdp2` bus names on its strength.
  What would settle it: tracing row E's cell (what the column, the bar and the heavy
  line at xc-2..xc+4 are), or a sharper photo of one slice.

Independent review (2026-11-17): leaning continuous, about 80%. "Neck" is an
interpretation; the dimness is also explained by the column's heavy east edge printing
through. The bar is probably a thin poly across the column (far blacker than the thin
poly under the same line at y 5190; pale double line in `acid1b`, as protected poly): a
probable gate, and if so the island below it (y 5567-5590) needs a contact, which only
the bit line can give (chip 2's metal shows an oval at xc-8..xc+2, y 5565-5588). So the
column is probably row E's tap on the bit line (same net), and "no tap on these lines"
is not firm at this spot. A series transistor in the bus (two pieces, contacts either
side of the bar) is not excluded. Settling it needs row E's cell traced.

## Bit 6 to R10's s1

`bust` drew the metal (data bit 6: `db_b6`'s metal, with the contact (8078,5020) onto
`db_b6`) to (8075,5040). It runs on south along x 8075 to y 5848, steps east to x 8118
along y 5840-5856 and runs south along x 8118 to `db_b6`'s drawn top (y 7395).
The step lies on one of channel 1's poly lines with no contact (uniform salmon under it;
`cdp2` found the same at the line's lower jog). Views: `b6a.png`, `s1a.png`, `s1b.png`,
`s1jog.png`. Firm.

Possible taps, not established and not drawn:
- (8116,6120): a similar heavy-outlined tan box under the line, 8105-8128 x 6100-6140
  (review, `rv_rde/b6C.png`).
- (8118,7088): a rounder, wider blob (about 18 px) on the line between two poly
  crossings; `acid1b` has a small heavy-outlined box there (`s1pad.png`, `tap.png`).
  The line carries on both sides (dark stretches of 9-13 px).
- y 5110-5440: the line lies over three diffusion regions (x 8062-8085, pitch 130) of
  the logic west of rows D/E; `tools/follow.py` lists contact candidates at y 5111, 5161,
  5295, 5360, 5407. No pad or ring seen at 2.9x.

## Bit 5 to R10's s2

`db_b5`'s tap metal at x 8727 runs from y 5150 straight down to a contact
(8728,6088) on a poly pad; the poly runs west along y 6079-6095, under the metals at
x 8687, 8620 (a VSS rail) and 8553 with no pad on any, to a pad with the contact
(8485,6087); that pad's metal has its line on the west side and goes south along x 8464
to y 6999, east to x 8532 and south to `db_b5`'s drawn top (y 7395). Views:
`s2top.png` (4x, three shots: both rings, both green patches, the poly end to end),
confirmed by the review. The poly under the x 8532 leg (y 6965-7135) is another net (from
a pad (8530,6950) on the x 8505 metal, turning west at y 7125), with no contact to this
line;
`s2c.png` (the pad and its line at 6x; the corner), `ov_s2.png` (overlay). Firm.
The follower's contact candidates on the x 8727 metal (y 5176, 5335, 5494): field or
poly under the line, no pad (`tap.png`).

## Ports

| Net | Layer | Where | Note |
|---|---|---|---|
| `db_b4`..`db_b0` | M | x 8856 + 390 k: joins `cdp1` at y 5140-5150 and `cdp2` at y 5700-5710 | data bits 4..0; `cdp2_a_sK_bus` / `cdp2_c_sK_bus` (K = 3..7) are aliases |
| `db_b6` | M | joins `bust` at (8075,5030-5040), `cdp2` at (8118,7395-7400) | data bit 6; `db_b6` is an alias |
| `db_b5` | M, P | joins `cdp1` at (8727,5140-5150), `cdp2` at (8532,7395-7400) | data bit 5; `db_b5` is an alias |

## Ambiguities

1. The stretch y 5542-5596 on the five lines (above): reading 1 adopted, reading 3 not
   excluded.
2. Taps on bit 6's line (above).
3. `cdp1`'s notes say of rows D/E "the column bit line x 9240-9256 straight through to
   y 5700": at 0.5-3x it looks so; at 5x and above the stretch is not plain metal.

## Not done

- Rows D and E (the cells): not traced. Seen while working on the lines, per slice: a
  poly block (xc-20)..(xc+16) x 5408-5455 under the line; the diffusion column and bar
  described above; a poly strip (xc+6)..(xc+16) x 5512-5540 between the column and a box
  under the next track; a poly block (xc-6)..(xc+16) x 5632-5680 under the line.
- `db_b7`'s metal (data bit 7) below y 5084 (jog to x 9335): not followed
  (`tools/follow.py` from (9335,5110) south stops at (9331,5516), unchecked).
- Where the s1 and s2 lines go below row C (x 8075, 8465 at y 7821), and the five bus
  lines below `cdp2` (they are `cdp3`'s bit lines by position: not joined here).
