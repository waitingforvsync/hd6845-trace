# bc4: bottom-centre random logic (x 9000-11000, y 16300-18550)

Trace: `trace/bc4.txt` (not yet started). Scratch: `cache/scratch/bc4/`. Coordinates are
metal-shot pixels.

## Status

Survey only, traced on claude-opus (Fable allowance exhausted). Nothing of this block is
drawn yet (`trace/bc4.txt` does not exist; no ports, no signals). Survey views: `cache/scratch/bc4/survey.png` (whole region, metal | acid1b,
0.57x, all blocks' geometry overlaid), `cache/scratch/bc4/left.png` (acid1b, 1x,
x 9050-10050, y 16350-17600).

## Inventory

Read at 0.57x and 1x only; every coordinate below is approximate (+-15 px) until read
at 4x.

**Supplies.** Wide speckled vertical metal rails (metal shot) at about x 9440-9480,
x 9625-9690, x 10530-10590 and x 10730-10760, running the height of the gate fields
(y 16300 to about 17550 for the left two, to about 18450 for the right two). Which is
VSS and which VCC is not yet read. A wide horizontal supply band along the bottom edge
from about y 18470 (whole width), joined by the left rails at about x 9300-9340 and
x 9640-9690 coming down through the track field. Not checked against `bc1`'s rails.

**Left gate field, x 9050-10000, y 16350-17550.** Dense random logic, columns of
gates either side of the rails:
- x 9050-9200, y 16400-17000: two or three large diffusion areas (wide transistors,
  probably drivers or loads), poly gates crossing them horizontally.
- x 9330-9560 and x 9690-9950: vertical stacks of small gates (pitch about 50 in y),
  many contacts; a dark (thin-oxide, likely depletion) diffusion stripe pattern at
  x 9530-9580 and x 9700-9760 suggests load transistors in columns beside the rails.
- Horizontal poly lines leave the field to the left at y about 16450, 16640, 16740,
  16790, 16850, 17110, 17150, 17210, 17510 (many with contacts at x 9120-9180).

**Right gate column, x 10280-10980, y 16350-17750.** A narrower column of gates beside
the rails x 10530-10590 / 10730-10760, poly inputs entering from the left in
horizontal pairs.

**Wiring field between, x 10000-10280, y 16300-17700.** Vertical metal tracks at
pitch about 22-25 (roughly ten tracks), some turning into the gate fields.

**Track field, y 17550-18450 (whole width).** Horizontal metal tracks, pitch about 22,
turning in nested L shapes (the tracks of the left gate field bending down and right),
and from y 18000 to 18350 a bus of about fifteen horizontal lines with contact columns
at x about 9290, 9330, 9380, 9410 (metal-to-poly ladders) running right; at
x 10200-10450 the bus bends diagonally down-right towards the bottom right corner.

**Already drawn by other blocks** (from the overlay with `TRACE=` empty):
- A metal track with label `inh_src` at x 10220, y 16390, running down x 10220 to
  y 16820, then a poly jog to (10305, 16945) and metal down x 10310 to about y 17560,
  then x 10270 down to y 18030.
- Metal x 10380 from y 16880 down to about y 18520 (with jogs at y 17680, 18320).
- Poly x 10140-10215 at y 17760 down to y 18070 and a metal line y 18070 from x 9770
  left to x 10150.
- Poly and metal y 17945 from x 10230 to about x 10950 and a diagonal leaving to the
  right at x 10930-11000, y 17600-17900.
- Short poly y 18420 between contacts at x 9555 and x 9775; contacts and metal at
  x 10290-10560, y 18440-18510 along the bottom.
These are other packages' routing ends; this block must join, not redraw, them.

**Cell hits** (`tools/t.sh bc4 findcell.py ... --region 9000,16300:11000,18550 --min 0.6`):

| cell | @inst | score | at |
|---|---|---|---|
| `tl1_ub` (2535,4347:2838,4797) | `@inst tl1_ub 6856,12101` | 0.79 | 9542,16673 |
| `tl1_ub` | `@inst tl1_ub 7096,12231 mx=2686.5` | 0.60 | 9782,16803 |
| `tl5_inv` (4951,4786:5213,4910) | `@inst tl5_inv 4430,12414 rot=180 o=5082,4848` | 0.64 | 9512,17262 |
| `bc1_drv` (7530,14978:7795,15163) | `@inst bc1_drv 2917,3383 mx=7662.5` | 0.65 | 10580,18454 |

Only the `tl1_ub` hit at 0.79 is worth checking first; the others are below 0.7 and the
`bc1_drv` hit lies on the bottom supply band, so it is probably not a real copy. None
has been checked against the photos.

## Checks after the survey

- **`tl1_ub` hit at (9542,16673) rejected** (`cache/scratch/bc4/ub.png` against the
  master `ubm.png`, 2x, acid1b and metal, cell overlaid): the master's thin vertical metal
  (x 2557-2573, copy x 9413-9429) and its top pad/contact have no counterpart, the poly
  and diffusion between copy x 9500 and 9560 differ, and the master's VCC box contact
  (2808,4600) falls on the copy's rail metal without a matching contact seen. Not a copy;
  the score 0.79 comes from the rail and column rhythm. The other hits (0.60-0.65) were
  not drawn either.
- **Right gate column, x 10460-10760, y 16480-16780** (`right.png` 1.3x,
  `r1.png` 2.2x, acid1b | metal): a unit repeated at about y +170 to +180
  (16500, 16680, 16850, ...): a wide diffusion area x 10600-10700 between the rails
  x 10565-10595 and x 10720-10760 (metal), with a dark (depletion) channel
  x 10655-10700 at y 16500-16570 and again at y 16680-16760, each under a poly plate
  that ends in a pad with a round contact at about (10740,16535) / (10740,16705), which
  lies at the west edge of the rail x 10720+. If that contact is to the rail, the load
  gate would be on a supply, not on its own node; this must be read at 5x in `acid`,
  `acid1b` and `metal` before anything is drawn (open question, not recorded as a fact).
  This repeated unit is the best first piece: once one copy is read, it can be a cell.

## Not done

Everything: rail identity (VSS/VCC), every gate, the track field, joins to the routes
already drawn listed above. Start with the `tl1_ub` hit at (9542,16673): crop
x 9380-9700, y 16440-16900 at `--scale 5` in acid1b and metal, compare with `tl1`'s
cell, and draw it as `@inst` only if every transistor and contact matches.

## Review
