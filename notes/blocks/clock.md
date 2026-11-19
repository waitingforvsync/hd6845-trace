# Clock block (9450-13100 x 18550-19950)

Status: gate row, wiring region and output stage traced (trace/clock.txt). Driver
logic surveyed, not traced.

## Summary

Status: traced except for a few flagged joins (trace/clock.txt). 335 transistors in
the whole trace, no rule errors.

The block makes three clocks from the CLK pin:

| Net | What it is | Made by |
|---|---|---|
| `ck_out` | NOT CLK, heavily buffered | three-stage buffer in the two big arrays, fed straight from the pin node |
| `ck_a` | high only while CLK is low | left half of the driver logic: NOR(`ck_g2`, `clk_b`) |
| `ck_b` | high only while CLK is high | right half: NOR(`ck_g4`, `ck_clkn`) |

`ck_a` and `ck_b` are a two-phase non-overlapping pair: `ck_g2` is `ck_b` delayed by
two inverters and `ck_g4` is `ck_a` delayed by two inverters (gate row g1-g4), so
each phase waits for the other to have fallen. `ck_clkn` = NOT `clk_b` is made by an
inverter in the middle of the driver logic; `clk_b` is CLK through the two-stage
input buffer.

Two small inverters in the gate row also sit on the phase lines: g6 pulls line A
(`ck_a`) down when `ck_b` is high, and g5 pulls line B (`ck_b`) down when a third
signal, `inh_ck`, is high. Their depletion loads can pull a phase fully to VCC,
which a source-follower pull-up cannot.

**Correction (2026-11-15, from the trunks block, checked at 6x).** An earlier version
of this note said `inh_ck` was `ck_a` itself, joined by a link at y 18345. That link
does not exist: the line at y 18335-18358 is `ck_out` and neither contact is there.
`inh_ck` is the output of the lone inverter at the left end of the input buffer row
(`inh_ck`), whose input comes down from the core (followed back to about
(13565,15275); its source is not yet found). So `ck_b` is also held low whenever that
core signal is low, and the same inverted signal is distributed along the bottom
bus field and up the left bus field. What it is remains open; see
`notes/blocks/trunks.md`.

Where the clocks go (`notes/blocks/trunks.md` has the routes): `ck_a` and `ck_b` run
right along the gate row and turn up into the core at x 13090 and x 13010; `ck_a`
runs up the right edge of the mid-right array with a tap per row. `ck_out` leaves the
clock block four ways.

## Gate row (11150-12150 x 18600-19000): traced

Six inverters. Loads on the VCC band along the top, pull-downs under the VSS rail at
y 18795-18848. Two metal lines cross the loads: line A (y 18700-18722) and line B
(y 18745-18768).

| Gate | Input | Output | Notes |
|---|---|---|---|
| g5 | `inh_ck`: poly from a bus line at y 18455-18480 above the VCC band, which leaves left (not followed) | line B (`ck_b`) | tall weak load; output also tapped to a plain diffusion rectangle at 11728-11897 x 18975-19150 (added capacitance) |
| g6 | line B | line A (`ck_a`) | strong load (W/L about 68/26); output also goes up in poly at x 12098-12125 to a bus line at y 18455-18480 that leaves right (not followed) |
| g1, g2 | line B | `ck_g1`, `ck_g2` | so `ck_g2` = line B re-buffered |
| g3, g4 | line A | `ck_g3`, `ck_g4` | so `ck_g4` = line A re-buffered |

`inh_ck` is not `ck_a` (see the correction in the summary): g5's input is the output
of input-row gate 0. Lines A and B also continue right
along the row to x 13010 / 13090, where they turn up into the core (not followed).

## Wiring region (11950-12900 x 18850-19950): traced

Seven nets go down on vertical metals and enter the driver logic in metal at
x about 12000, each crossing the VCC metal at x 12088-12140 on a poly bar:

| Enters at y | Net | Via |
|---|---|---|
| 19254 | line B | V1 (x 12165-12190) |
| 19294 | line A | V2 (x 12208-12232) |
| 19490 | `clk_b` (CLK, buffered, same sense as the pin) | V5 (x 12557-12583) |
| 19532 | `ck_g4` (line A re-buffered) | V4 (x 12302-12318) |
| 19573 | `ck_g2` (line B re-buffered) | V3 (x 12255-12277) |
| 19900 | `clk_p` (the CLK pin node) | V6 (x 12600-12630), then along the bottom |

Six island devices to VCC hang on these nets (AMB-006, taken to be clamps). A plain
VCC diffusion block with nine contacts lies under the gate row's lines at
12385-12790 x 18600-18850.

## Driver logic (10900-12000 x 19140-19890): read from the clean shot, being traced

Read from `acid1b` with `metal1` for contacts and `acid` for open areas (2026-11-14).
The earlier survey of this block from the chip-2 shots alone was wrong in several
places and is superseded.

**It is a two-phase non-overlapping clock generator.** Two cross-coupled NOR drivers
produce lines A and B from CLK:

```
A = NOR(ck_g2, clk_b)        ck_g2 = B through two inverters (gate row g1, g2)
B = NOR(ck_g4, N2)           ck_g4 = A through two inverters (gate row g3, g4)
N2 = NOT clk_b               inverter in the middle of the block
```

So A can only be high while CLK is low and B while CLK is high, and each waits for
the delayed copy of the other to fall. Lines A and B then go right along the gate
row into the core, and A (as the line first called `inh_ck`) is carried round the
bottom and left bus fields.

Left half (output A), with coordinates:
- Output pad: line A's metal contacts the output diffusion at (11030,19298).
  (Right half: line B contacts it at (11838,19250). Apart from that and the middle,
  the halves mirror each other about x = 11437.)
- Pull-up: long vertical poly, x 10980-11003 from y 19165, jogging at y 19545-19572
  to x 10966-10992, gate between the outer diffusion (x 10922-10978, contact to the
  top rail at 10937,19188) and the inner diffusion (x 11003-11033), which is the
  output. Width about 430. Its gate net is N1.
- N1 = NOR(b, c): load is the diffusion finger x 11258-11318 coming down from the
  VCC diffusion, gate y 19218-19270 (W/L about 60/50), tied to its output by a
  buried contact at 11228-11258 x 19278-19312; the same poly runs up the leg at
  x 11228-11250 to the bar under the top rail (y 19165-19191) and left to the long
  vertical poly. Below the load N1's diffusion necks down (x 11285-11300,
  y 19325-19365) to a column at x 11283-11308 that ends at y 19548. Pull-downs:
  b2 (x 11259-11282, to VSS column 11192-11251, W about 177) and c1
  (x 11314-11340, to VSS column 11343-11378, which ends at y 19505, W about 135).
- Output pull-downs: a (x 11109-11133) to VSS column 11058-11101, and b1
  (x 11160-11191) to VSS column 11192-11251; the output is the narrow column
  between them (x 11139-11159). All run down to y 19850: W about 480 each.
- Gate nets: b1 and b2 are joined above the rail by poly block B
  (11163-11272 x 19329-19365); b2 ends at a pad at 11259-11297 x 19551-19595 where
  the `ck_g2` metal line (y 19562-19585) ends. c1 and c2 (x 11388-11412) are joined
  by block C (11305-11410); c2 has a pad at 11382-11427 x 19470-19520 where the
  `clk_b` metal line (y 19479-19502) ends, and runs on down to a poly bar under the
  CLK metal line (11112-11412 x 19888-19906, no contact to that line) that also
  joins strip a. So a = c = `clk_b` and b = `ck_g2`.

Middle:
- Load 2: finger x 11401-11455, gate y 19218-19270, tied to its output N2 by a
  buried contact at 11366-11400 x 19275-19320. N2's column under the rail is
  x 11412-11450, pulled down through c2 to VSS column 11343-11378. So N2 = NOT clk_b.
- Load 2's gate poly continues right to x 11512, turns down at x 11490-11517
  (y 19270-19325), runs diagonally to (11525-11547, 19365) and becomes strip S
  (x 11523-11549), which runs the full height to a poly bar under the CLK line
  (11525-11763 x 19888-19907) and up strip a' (x 11742-11763). So N2 drives the
  right half's a' and c1'.

Right half (output B): mirror of the left. b' = `ck_g4`, by a pad at
11579-11619 x 19549-19588 where the `ck_g4` metal line turns down and ends. The
`ck_g2` line jogs down round that pad (y 19607-19640 for x 11540-11658).

Not settled (AMB-007):
- A box, 10938-11003 x 19632-19668, on the pull-up's gate where the poly widens to
  x 10950-10992 (and its mirror at 11870-11936). It looks like a buried contact
  window, but one there would short gate, VCC side and output together. Left out
  of the trace. Whether the pull-up is enhancement (output high = VCC - Vt, topped
  up by the small inverters g5/g6 in the gate row) or depletion is also open.
  Neither affects the logic above.
- The path of the output diffusion from the pad to the column between a and b1 was
  seen only at 3.3x (a narrow strip along y 19318-19332 and down x 11150-11165).

Things that looked like structure and are not: "R2" and the lines flanking the long
poly are rims that follow any poly edge in open areas; dark boxes at the ends of
gates in `acid1b` are the gate overhang (check such spots in `acid`).

## Output stage: the two big arrays (9500-10730 x 19180-19815): traced schematically

The two arrays are one circuit, a three-stage buffer ending in a push-pull pair:

```
ck_p --> [inverter: s3,s4,s5, W 3x480] --> ck_t --> [inverter: s1,s2, W 2x480] --> ck_n2
ck_n2 --> [F3, W 345] --> ck_ga   (pull-up gate of the output)
ck_out:  pull-up  = group A, W 2x483 + 145, gate ck_ga, from VCC
         pull-down = F1 + F2, W 2x345, gate ck_n2, to VSS
```

So `ck_out` = NOT `ck_n2` = NOT `ck_p`, delayed by three stages.

`ck_p` is the CLK pin node itself. The gates s3-s5 are joined along the bottom and
continue down in poly at x 10650-10695 to a wide poly bar (10650-11000 x
19892-19935) lying under the metal line at y 19892-19912; a contact at 10985,19901
joins the two (seen clearly at 2.9x). That metal line is the one that arrives from
the CLK protection cell via the vertical metal at x 12600-12630, and it carries on
to the left past x 9420 (not followed).

Supplies: VSS comes down from the core on the wide metal at x 10755-10815, branches
right at y 19335-19375 into the driver logic's middle rail, and turns left at
y 19765-19815 as the bus under both arrays. VCC arrives twice: on the wide metal at
x 10652-10722 from the core (it feeds only the load of `ck_t`), and on a wide metal
from the left at y 19095-19145 that spreads along the top of the left array
(y 19245-19300).

Loads: `ck_t` has a 154/27 load at x 10652-10680; `ck_n2` has a 174/34 load (group C,
x 10130-10165). Both are about 5.5 squares wide, which is what first suggested that
the wide metal over group C is VCC and not a signal.

`ck_out` leaves the block two ways. Up the left side on a metal at x 9515-9545 and
away to the left at y 19240-19262 (not followed; it seems to reach a contact at
9340,19240). And downward at x 9848-9870 from the bus along the bottom, right along
y 19848-19865 to x 10850, up at x 10840-10870 to a contact at 10852,19422, under the
VSS branch in poly to 10852,19292, and on up into the core in metal (seen at 0.85x;
not yet in the trace).

Established by close-up (6x): the gate bar of group A (9640-9830 x 19195-19240)
continues down its right-hand side at x 9797-9830 to the contact at 9810,19337 on
the `ck_ga` metal; the bar that joins F1-F3 (y 19357-19372) is a separate piece of
poly just below that contact. This fixes the polarity of the output.

Checked against the clean shot of chip 1 (2026-11-14):
- s1 and s2 hang from one poly pad (10283-10372 x 19180-19218, an inverted U) that
  carries two contacts to the `ck_t` bus. Confirmed.
- F1, F2 and F3 hang from one poly band (9850-10010 x 19325-19372) that lies under
  the `ck_ga` metal without contacting it and is fed by the poly coming down at
  x 9975-10010 from the `ck_n2` pad. Confirmed.
- Group A's gate bar runs down its right-hand side to a contact on the `ck_ga`
  metal at (9810,19337). Confirmed.
- Still inferred: the two load gates being tied to their output sides.

Not yet traced here: the load of `ck_ga` (the small device at 10030-10160 x
19430-19680 is the candidate), and whether `ck_ga` is bootstrapped.

## Route of `inh_ck` to the left of the die

From the bus piece at y 18458-18480 (which g5's gate also hangs on): left to a contact
at 10897,18468; a short poly link to a contact at 10808,18470 and, by a branch up at
x 10850-10870, to a contact at 10855,18385 on the bus line at y 18375-18400. From
10808,18470 a metal runs down to 10808,18600, crosses under the wide metal at
x 10720-10770 in poly to 10685,18600, runs left along y 18590-18612 to x 10255, up at
x 10250-10290 to y 18425, and left along y 18410-18440 as one of the lines of the
bottom bus field: poly links under vertical metals at x 9740-9840, 8440-8560 and
7470-7510, ending at a contact at 6800,18420. A poly line runs up from there to a
contact at 6800,17990 at the foot of the innermost vertical line (x about 6790) of
the bundle that climbs the left bus field. Seen at 1x; not in the trace.

## Corrections (coordinator, from the handoffs of 2026-11-19, fourth batch)

- The signal on track A / line X / the first through line of the left-centre strips, which these notes call a clock, a strobe "once per scan line" or leave without a source, **is the reset**: `rst_a`, the buffered copy of `rst` = NOR(`lpstb_b`, `res_b`) made by `lc1`'s gate 5 (`eof` run 10, piece `isrc5`, firm). `inh_ck`, `inh_rc` and `inh_lat` are further buffered copies of it: high while the RES and LPSTB pins are both low, and only then. The belief "a strobe once per scan line" is withdrawn. (`inh_ck`'s source was open here.)
