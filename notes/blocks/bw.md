# bw: bus field between the central datapath and the counters, and the lines that cross it

Serial work, started 2026-11-15. Trace: `trace/bw.txt`. Views: `cache/scratch/bw/`.

## Status

Drawn and extracted: the routes of the five poly lines that leave block `wl` westwards,
as far as each was followed (table below). Wiring only, no transistors.
Not drawn: the bus field's own vertical lines (surveyed only, see the last section).

## The five lines from `wl`

They do **not** stop in the bus field. Each crosses it without a contact (clean shot: the
salmon band is unbroken under every vertical metal; the dark rings at the crossings are
the metal's margins), runs west as one of the lines of the central datapath's "channel 3"
(y 7830-8030, cdp2's notes), and four of them turn **north** at the channel's west end as
a nested bundle (x 7790-7930), bend twice (y 7560-7700 and y 7250-7480) and run west into
a crossing field of horizontal poly lines and vertical metals (x 6330-7700, y 7150-7700).
There each ends on a pad with a contact to one vertical metal.

| Line (name in `wl`) | Channel y | Turns north at x | Ends on | Then |
|---|---|---|---|---|
| bus line B's line (`cnt_bus_b`) | 7831-7849 | 7925, then 7832 | pad, contact (7466,7343) | metal x 7455-7478 **north** (seen to y 7150) |
| `ck_a` | 7873-7891 | 7880, then 7787 | pad, contact (7419,7387) | metal x 7410-7432 **north** (seen to y 7150) |
| `rc_stepreq_n` (row counter step, active low) | 7917-7935 | 7839, then under the wide metal at x 7753 | after y 7436 west, x 7407 south, y 7519 west through the whole crossing field, x 6300 north, y 7471 west: pad, contact (5838,7470) | metal x 5830-5852 north to a contact (5838,5585); poly west along y 5585 through a second crossing field to a contact (3518,5587); metal west and north to a contact (3283,5238); poly east, north and west along y 5018 to the output node of the step gate at (2975,5035): block `tla` |
| `wl_h1` (band H1's line) | 7962-7980 | 7792, then x 7709 | after y 7477 west, x 7450 south, y 7562 west: pad, contact (7031,7560) | metal x 7025-7048, direction not followed |
| R2 match (`h_eq_r2`) | 8006-8024 | does not turn | pad, contact (8340,8010) | metal x 8330-8352, not followed |

So the row counter's step signal is made in the **top-left logic**, by a three-input NOR
at (2975,5035) (`notes/blocks/tla.md`). `ck_a` and bus line B's signal go north on two metals at x 7421
and x 7467 (west edge of the central datapath, towards the top-centre logic).

Two corrections to cdp2's notes on channel 3: the four lines turn **north** at its west
end, not down; and the whole channel has now been read in the clean shot from x 7950 to
x 11040: there is no contact on any of the five lines on the way (cdp2 had looked at two
slices only).

Stretches that lie under metal and cannot be seen in the metal shots: `rc_stepreq_n` and `wl_h1`
under the wide vertical metal x 7725-7775 (y 7430-7700), all crossings in the crossing
field, and the piece of the first line of the bundle (not one of ours) that runs down
under the metal x 7300-7322. Read with `tools/classmap.py --open`.

## Other things seen at the bus field's top (not drawn)

- `rc0_n` (poly y 7441-7462) ends at a contact (11022,7432) under a metal x 11010-11035
  that goes north; `rc0` (poly y 7486-7508) ends at a contact (11022,7503) under a
  metal x 11010-11032 that goes **south**, stepping one pitch east at y 7600-7650, at
  y 8580-8640 and again at y 9280-9320, and on down the bus field.
- The load strobe of cdp2's row C (`wr_r10`, poly y 7790-7808) ends at a contact
  (10893,7797) under the top of a metal x 10880-10905 that goes south.
- Band H4 (`cnt_gab`) runs on west of x 11040 along y 7200-7222: not followed.

## Survey of the bus field itself (y 9400-17200)

About twenty vertical metal lines, x 10760-11480 at their widest. Where a line leaves the
field to the east the ones to its west step one pitch (43-44 px) east by a diagonal, so a
line's x changes along its length. Two staircases of contacts tie eight of the lines to
eight horizontal poly lines of the central datapath: at y 10345-10650 (contacts from
(10890,10355) to about (11200,10630)) and at y 13300-13620 (from (11070,13450) to
(10890,13610)): an eight-line bus between cdp3's rows and cdp4's rows. The field's lines
must be read in the clean shot end to end (tracing guide, trap 10); a 1x metal view shows
only the staircases.

## Not done

Everything in the survey; the far ends of the five lines (table); H4 west of x 11040.

## Corrections (coordinator, from the handoffs of `busl` run 16, 2026-11-21)

- The table's row `wl_h1` ("metal x 7025-7048, direction not followed") and the comment in `trace/bw.txt`: the metal goes north on x 7034 to a corner (7034,6957), west along y 6957 to a pad (6188,6956), and by a poly row, a diagonal and the poly column x 5454 onto `tl5`'s poly end (5453,6350): it is `wl_h1`, the data of `tl5`'s latch a (`busl`, piece `ha`).

## Corrections (coordinator, from the handoffs of `cdp3`, `cdp4` runs 4-15, `eof` runs 36-51 and `regs` runs 5-6, 2026-11-21)

- Survey of the bus field: "an eight-line bus between cdp3's rows and cdp4's rows" is the read bus of R12-R17
  (`cdp3_n_c#` = `cdp4_n_s#`, firm; `regs` run 6, `cdp4` run 4) and runs on south of `cdp4`'s staircase to the
  bottom bus. The lower staircase of contacts begins at (11200,13330) (column 0), its second pad at about
  (11157,13375), not at (11070,13450); the upper one ends at (11200,10664), not about (11200,10630).
- The field's westmost two lines are other nets: x 10852 is `rst_lat` (a reset copy, from `trunks`' diagonal
  up to y 3592), x 10808 is `cdp4_w10808` (the output of an undrawn unit of `bc2` at about (10620-10780,
  15750-15860)); both drawn by `cdp4` run 12.

## Corrections (coordinator, from the handoffs of `busl` runs 17-18, 2026-11-24)

- The metals north of the pads (7419,7387) (`ck_a`) and (7466,7343) (`cnt_bus_b`), "seen to y 7150", are followed
  (`busl` run 18, pieces `ya`, `yb`): north to corners (7424,6762), (7468,6718), west to end pads (6491,6759),
  (6538,6717), and by poly columns north to `tc2`'s pads: `tc1_p4308` and `tc1_m6817`. The two metals lie on
  `fld`'s poly rows y 6756 / y 6712 for 380 / 420 px without a contact (`busl`'s Ambiguity 23).
