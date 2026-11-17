# tl2: top-left random logic, the second strip (x 2817-3533, y 2500-6350)

Package `tl2` (part 2 of 6 of the top-left logic). Trace: `trace/tl2.txt`. Views:
`cache/scratch/tl2/`. Most of the strip is `tla`'s east gate column on rail R3 (VSS,
x 2950-3000; traced, `notes/blocks/tla.md`) and the bus field east of it. This package draws
what `tla`, `tl1`, `r9m` and `ur` did not. Nothing of theirs is redrawn.

## Status

2026-11-17 16:30 -0600. **Partial: one piece.** The east half of the small cluster below the
step logic (x 2817-3180, y 5900-6300) is traced: two inverters in series (4 transistors), which
buffer the third latch's output `tl1_w6022` onto `tl1_w5936`; rail R3 from y 5320 to its foot
and the VSS metal that leaves the foot; the two thin metals that pass over the units, each to
its south end in the strip. Full extraction: 0 errors, 0 warnings.

```
tl2_w6070 = NOT tl1_w6022     (2992,6109)   lower unit
tl1_w5936 = NOT tl2_w6070     (2992,5978)   upper unit
```

Not looked at: everything else in the strip (see Not done).

## Inventory

| Where | What |
|---|---|
| x 2860-3100, y 2940-5300 | `tla`'s east gate column on R3 (traced by `tla`) |
| x 3100-3533, y 2940-5700 | bus field: vertical metals, poly rows with pads; `tla` drew the tracks to about x 3340; x 3340-3533 not drawn |
| y 2500-2940 | horizontal metal tracks and rows north of the cluster, partly `r9m`'s and `tla`'s |
| x 2817-3180, y 5900-6300 | the small cluster's east half: **this piece** |
| x 2890-3533, y 6300-6350 | `rcs_thin_e`'s pad (2913,6327) and its poly row east (drawn); `lc_step`'s row y 6268-6290 is `ur`'s |

## Logic

### The small cluster's east half: two inverters (traced 2026-11-17)

Built like `tla`'s units on R3: the pull-down sits on a VSS box under the rail, its drain is a
strip that runs west under the rail to the node, and the load is a strip from a VCC box under
R2, under a poly plate between R2 and R3, with a tie box at the plate.

- **Lower unit, `tl2_w6070` = NOT `tl1_w6022`.** VSS box x 2968-3015, y 6095-6170, contact
  (2988,6144). Gate: `tl1`'s row y 6187-6203 (the third latch's output) runs on east under R2,
  the thin metals and R3, turns north at x 3101-3125 and west along y 6098-6120 across the top
  of the VSS box (W 47); its west end is at x 2953. Drain: tan under the rail, y 6064-6092. Node:
  a diffusion strip in the open gap between thin metal E and R3, x 2934-2947, y 6048-6120. Load:
  strip y 6093-6120 from a VCC box under R2 (x 2785-2833, y 6062-6122, contact (2803,6092):
  ring in both metal shots, specks in the clean shot, `c11.png`) under the plate x 2836-2925,
  y 6066-6122. Tie: box x 2895-2927, y 6042-6062 at the plate's top, reached by the node strip.
  Output: a strip east along y 6064-6084 to the buried contact B (box x 3038-3068, y 6050-6084).
- **Upper unit, `tl1_w5936` = NOT `tl2_w6070`.** VSS box x 2968-3015, y 5962-6040, contact
  (2986,6011). Gate: the poly from B east along y 6056-6076, north at x 3101-3125, west along
  y 5966-5990 across the top of the VSS box (W 47), west end x 2952. Drain: strip y 5942-5960
  north of the gate, west under the rail and through the gap to the node (x 2897-2930,
  y 5935-6005, under thin metal E), east to the buried contact A (box x 3038-3068, y 5924-5958).
  Load: strip y 5936-5962 from `tl1`'s VCC box under R2 (contact (2803,5935)) under the plate
  x 2842-2892, y 5915-5990. Tie: box x 2868-2897, y 5988-6008 below the plate.
  Output: poly from A east along y 5926-5947, south at x 3147-3170 round both loops, west along
  y 6228-6247, under R3, the thin metals and R2, to `tl1`'s row at x 2817.
- **The loops.** Each gate poly goes round a rectangle of bare ground east of the rail
  (x 3020-3095, y 5995-6050 and y 6125-6182) before it reaches its box. The rectangles and the
  20 px gaps between the polys are field: chip-2 stripped shot 157/152/104 inside, 159/155/103
  on open field east of the cluster, 168/158/94 in the gap (`px.py pt`). No diffusion under the
  loops was found; they are drawn as poly wires. What they are for is not known.

Evidence (commands in `cache/scratch/tl2/survey.md`):
- Clean-shot colours under R3, measured here: diffusion 200/178/137 (the VSS box away from
  its contact, the two drain strips), field 208/130/116, gate band over the box 245/175/122.
- The drain strip east of the rail is diffusion in the open: chip-2 stripped 176/154/104 at
  (3030,5950) between edges at y 5938 and 5960; the lower one the same at (3030,6073).
- The node strip of the lower unit: `px.py col 2940 5976 6160 6`: chip-2 stripped 180/135/101
  from y 6054 to 6114 between dark lines at y 6042-6048 and y 6120-6126, and field
  (165/155/95) above and below.
- Overlays: `o1.png` (clean shot, 3.3x), `o2.png` (chip-2 stripped and metal, 4.6x),
  `o3.png` (metal, 2.4x).

### The thin metals over the units

- `tla_w3376`'s metal x 2865-2877: one line from `tla`'s pad (2870,5502) south through the
  cluster and out of the strip at y 6350 (`follow.py 2870 6100 N` runs to y 5498, `S` to
  y 6374). Dim over the upper tie box (y 5981-6010), no pad, no bright centre.
- `rcs_thin_e` (thin metal E, x 2906-2920): on south from `tla`'s piece (y 5400) to a pad with
  a contact (2913,6327): bright centre in a dark ring in both metal shots and a green hole in
  the clean shot (`textmap.py 2886 6296 2946 6350 3`). From the pad a poly row runs east along
  y 6316-6337, under the VSS metal x 3257-3305 and `ur`'s metal x 3347, out of the strip at
  x 3533 (`c14.png`; `px.py row 6326 2930 3540 12`: poly colour all the way). The metal is dark
  from y 6038 to 6068 in both metal shots, over the lower tie box: no bright centre, and the
  clean shot is protected tan inside the box (`c10.png`, `textmap.py 2884 6020 2944 6090 3`):
  read as one metal passing over a buried contact (tracing guide, trap 22), not a contact and
  not a break. The follower stops on both sides of it.

### R3 and the VSS metal at its foot

R3 (x 2951-2999) runs on from `tla`'s end (y 5330) to y 6292 without a break (`px.py col 2962
5300 6310 10`: dark only at single samples where poly rows cross). At its foot a wide metal
runs east, y 6250-6292 to x 3160 and y 6238-6292 beyond, turns south at x 3257-3305 and leaves
the strip. `lc_step`'s row (`ur`) and the output row y 6228-6247 lie under or beside it without
a contact.

## Ports

| Name | Layer | Where | Dir | What |
|---|---|---|---|---|
| `tl1_w6022` | P | x 2817, y 6187-6203 | in | the third latch's output (`tl1`): the lower inverter's gate |
| `tl1_w5936` | P | x 2817, y 6228-6247 | out | the upper inverter's output, on to `tl1`'s row and the metal x 2500 |
| `tla_w3376` | M | x 2865-2877, y 6350 | ? | thin metal on south |
| `rcs_thin_e` | P | x 3533, y 6316-6337 | ? | row east from the pad (2913,6327) |
| `vss` | M | x 3257-3305, y 6350 | - | the metal from R3's foot, on south |

## Ambiguities

1. **The lower unit's tie box under thin metal E** (2895-2927, 6042-6062). Thin E is dark
   over it for 30 px. Read as a pass-over (see above). If it were a contact, `rcs_thin_e`
   would be `tl2_w6070`; if the metal were cut there, the pad (2913,6327) and its row would be
   on another net than `tla`'s `rcs_thin_e`. Working assumption: one metal, no contact.
2. **The upper unit's node lies under thin metal E** (x 2897-2930, y 5935-6005) and
   `follow.py` gives a contact candidate (2912,5983). The metal dims there only from C-D to
   9-A (chip 2) with no ring, and not at all in chip 1; the clean shot is protected tan with
   no green hole. No contact drawn.
3. **The loops** are drawn as poly on field. A diffusion narrower than the poly under them
   (which would make each a long transistor) cannot be excluded from colour alone; the field
   colour of the rectangles and gaps, and the two units being complete without it, speak
   against it.
4. The joins of the lower node strip and of the two strips east of the rail to the diffusion
   under the rail are hidden by a rail-edge line in every shot (review round 1); drawn joined on
   the continuity of their outlines.
5. Sizes: the pull-downs' W (47) is the VSS box's width; the lower load's strip is read from
   the brighter band of the plate (y 6093-6120). No connection depends on these.

## Review

Round 1 (full review, 2026-11-17 22:41 +0000, a fresh agent on claude-fable-5-2, at commit
7886411; 11 images in `cache/scratch/tl2/review-1/`). Piece: the small cluster's east half
with R3, the VSS metal and the two thin metals. Told to suspect: thin metal E dark over the
lower tie box (contact, break or pass-over), the follower's contact candidates (2912,5983) and
(2867,5980), diffusion under the loops and the boxes A and B, the lower node strip and its
joins, the upper drain strip under the rail, the lower load and its VCC box, the two rows
between x 2817 and x 3010, the pad (2913,6327) and its row.
It checked, at 3.3x and more in two or three shots and with text maps and profiles: thin E over
the tie box (pass-over: no bright centre, no pad, protected tan inside, green minus red at most
+1 against +44 and +52 at two real contacts); both candidates (not contacts); the lower node
strip (a feature in three shots; the gate's west end stays under the rail); both pull-downs;
the strips to A and B (diffusion, continuous) and the loops (plain poly on field, no edge
lines across them); the lower VCC box, contact and strip; both rows (continuous, no rings in
the chip-2 shots); R3 to its foot and the VSS metal (no contact to the rows); the pad
(2913,6327) (a contact) and its row to x 3530; the extraction, `opendiff.py`, `unsure.py`,
the ports at x 2817.
Findings, both geometry only, both checked by the tracer and fixed:
1. The upper load plate's west edge is at about x 2840, not 2848: confirmed (`px.py row 5950
   2834 2858 3`: chip-2 stripped 171/145/67 at x 2846, the edge at x 2840); drawn from x 2842.
2. The VSS contacts lie a few px east of where they were drawn: the clean shot's hole is at
   (2987,6011) for the upper one (94/127/84), and the metal shots' ring at about (2990,6146)
   for the lower; moved to (2986,6011) and (2988,6144).
Could not be checked: the joins of the lower node strip and of the two strips east of the rail
to the diffusion under the rail (a rail-edge line hides each in every shot; they rest on
outline continuity); the chip-2 stripped shot in the narrow gaps between the metals (fringes);
x 3200-3533 north of y 6215 was not surveyed.
`tools/t.sh tl2 sameconn.py 7886411`: `connections identical`.
`.venv/bin/python tools/sameconn.py 7886411`: `connections identical`.

Round 1: no findings that change a connection.

## Not done

- Everything in the strip outside x 2817-3180, y 5900-6300 that `tla`, `r9m`, `tl1` and `ur`
  have not drawn: the bus field's tracks x 3340-3533 and their rows (y 2940-5700), the tracks
  and rows north of y 2940, `tla`'s "bus pieces not yet drawn" (B2 from (3150,3810) south,
  C upper, D, F), the rows under the foot (y 5300-5700) east of x 2817.
- `rcs_thin_e`'s row east of x 3533 (towards its driver) and `tla_w3376`'s metal south of
  y 6350.
- The VSS metal south of (3281,6350).
