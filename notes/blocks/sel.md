# Register-select logic below the decode array (`sel`, x 14100-15850, y 14650-16550)

## Status

- Traced and extracted (trace/sel.txt, 0 errors, no open nets): how all 18 select
  columns leave the decode array; the gate column at x 14380-14850 (twelve identical
  inverter + NOR pairs, R0-R11); the right-hand gate column at x 15560-15890 (four
  select buffers for R16, R17, R15, R14 and two more inverter + NOR pairs for R15, R14);
  every input and output followed to the region boundary.
- Every pull-down, gate connection and output route was checked by overlay. The loads
  of the right-hand column are drawn schematically (marked `?`), see Ambiguities.
- rsel12 and rsel13 are not used inside the region: they pass through to the south.

## Inventory

| What | Where | Notes |
|---|---|---|
| VSS rail | y 14697-14747, x 14140-15720 | joins the decode array's VSS bus at the left; three ground rails hang from it (x 14434, 14789, 15690) |
| Top band | y 14636-14900 | each select column: contact at y ~14650 to poly, poly under the VSS rail, contact to a metal line (or straight on in poly) |
| Left bundle | x 14070-14320 | metal lines at x 14083 (rsel7), 14128 (rsel6), 14171 (rsel4), 14217 (rsel0), 14262 (wr_r6 going up), 14307 (strobe), 14347 (rsel2); poly lines in the gaps at x 14107, 14150, 14241, 14285 (outputs going up) |
| Gate column | x 14330-14890, y 14890-16720 | cell `sel_wr` x 12: left half at dy 0, 304, 608, 912, 1216, 1520; right half the same mirrored about x 14611.5. VCC rail x 14609 between the halves (top end y 14904), ground rails x 14434 and 14789 |
| Middle bundle | x 14900-15575 | 16 metal tracks on a 43.3 px grid, T0 14912 ... T15 15561 (list below) |
| Right gate column | x 15540-15890, y 14850-16550 | ground rail x 15663-15718, supply rail x 15795-15890. Cell `sel_rbuf` (two inverters) x 4 at y 14855 + 260k; cell `sel_rwr` (inverter + NOR) x 2 at y 15895 and 16195 |

Row k of the gate column (k = 0..5) has its inverter at y 14957 + 304k (gate A) and
its NOR at y 15087 / 15172 + 304k (gates B, C), output buried contact at y 15127 + 304k.
Row 5's NOR (y 16600-16720) lies below the region boundary but is traced here because
it is the same cell.

## Logic

All of this is traced (extracted by netlist.py), except where marked believed.

Each half-row of the gate column is

    rselN_n = NOT rselN
    wr_rN = NOR(rselN_n, strobe)        = rselN AND NOT strobe

| Row | Left half: register, select arrives by | Right half: register, select arrives by |
|---|---|---|
| 0 | R1: poly straight from the column (y 14865, x 14328) | R10: poly straight from the column (x 14797, y 14853, x 14886) |
| 1 | R2: metal x 14347, contact 14345,15240 | R5: T1, contact 14956,15259 |
| 2 | R0: metal x 14217, contact 14215,15566 | R3: T2, contact 14996,15564 |
| 3 | R4: metal x 14171, contact 14173,15869 | R8: T3, contact 15040,15866 |
| 4 | R6: metal x 14128, contact 14128,16171 | R9: T4, contact 15084,16170 |
| 5 | R7: metal x 14083, contact 14087,16476 | R11: T5, contact 15128,16475 |

Every select line of R0-R11 goes to exactly one gate, the inverter of its row, and
nowhere else (each metal line ends at its contact; checked with tools/sel_tracks.py
and by overlay).

The strobe input (gate C of each NOR):
- left half: metal x 14307 (`wr_stb_n`), contacts at 14305,15176 + 304k. It has no
  other connection inside the region and leaves it downwards.
- right half: metal T0 x 14912 (`wr_stb_n`), contacts at 14912,15174 + 304k. In row 0
  the gate C poly is a wide bar (y 15159-15197) that runs on east under the bundle to a
  contact at 15474,15172; metal from there joins T15 (x 15561), which comes down from
  a contact at 15622,14822 on a poly line arriving from the east along y 14825.
- Believed, not traced: `wr_stb_n` and `wr_stb_n` are one signal, an active-low write
  pulse, so that wr_rN is the write strobe of register N (high while the register is
  addressed and the pulse is low). Below the region (y 16715-17000) the left line has a
  metal branch to x 14240 and T0 turns west into a horizontal metal at y 16990; whether
  they meet is for package bd3 to trace.

Outputs: see Ports. The left half's six outputs go west in poly (five of them as
bars at y 14867-15043 under the left bundle); the right half's go down the bundle on
the track their select line came down on (R10's on T6).

### Right-hand gate column (traced)

Each pull-down is a wide transistor (W about 130) under the ground rail: ground contact
above, horizontal poly gate, output band below; the band leaves west through a buried
contact into poly.

Upper part, y 14855-15895: four times two inverters in series, a non-inverting buffer.

    rselN_bn = NOT rselN          rselN_buf = NOT rselN_bn = rselN

| Buffer | Input arrives by | Gates at y | Output leaves by |
|---|---|---|---|
| R16 | poly from the column's contact 15755,14783: west along y 14783, down x 15552 (under T15) | 14910, 15037 | poly west y 15084, contact 15387,15086, T11 down |
| R17 | T14 to contact 15516,15130, poly east along y 15175 | 15170, 15297 | poly west y 15344, contact 15431,15349, T12 down |
| R15 | T10, contact 15340,15428, poly east | 15430, 15557 | poly west y 15604, contact 15471,15606, T13 down |
| R14 | T9, contact 15299,15692, poly east | 15690, 15817 | poly west y 15864, contact 15515,15866, T14 down |

Nothing else gates these: one transistor per output. Believed: the buffered selects
are the read enables of the four readable registers (R14-R17), to be combined with a
read pulse outside this region.

Lower part, y 15895-16530: twice the same logic as the gate column.

    rsel15_n = NOT rsel15     wr_r15 = NOR(rsel15_n, wr_stb_n)     gates at y 15956; 16082, 16172
    rsel14_n = NOT rsel14     wr_r14 = NOR(rsel14_n, wr_stb_n)     gates at y 16256; 16382, 16472

rsel15 reaches its second tap on T10 (contact 15340,15953, where T10's upper line
ends), rsel14 on T9 (contact 15299,16253, likewise). The strobe gates are fed from T15
through contacts at 15560,16172 and 15560,16472. Outputs: poly west along y 16127 to
a contact at 15344,16127 on T10, and along y 16427 to 15301,16428 on T9; both tracks
run on down from there.

### Summary: where each select line goes

| Select | Used for |
|---|---|
| rsel0-rsel11 | one gate pair each: wr_rN = rselN AND NOT strobe. Nothing else |
| rsel12, rsel13 | nothing here. T8 (x 15258) and T7 (x 15214) carry them through to y 16550 with no contact (track scan, and overlay on the metal shot). rsel12's first tap is exactly on the bottom edge: contact 15258,16560, poly east along y 16560 (seen to x 15600, not followed). rsel13 runs on south |
| rsel14, rsel15 | each: a buffer (rselN_buf) and a gate pair (wr_rN) |
| rsel16, rsel17 | a buffer each (rsel16_buf, rsel17_buf), nothing else: no write strobe |

## Middle bundle: what is on each track (from tools/sel_tracks.py, y ranges)

| Track | x | Segments |
|---|---|---|
| T0 | 14912 | 15161 - below region: wr_stb_n |
| T1 | 14954 | 14822-15272 rsel5; 15418 - below: wr_r5 |
| T2 | 14998 | 14783-15577 rsel3; 15724 - below: wr_r3 |
| T3 | 15041 | 14812-15880 rsel8; 16030 - below: wr_r8 |
| T4 | 15085 | 14770-16185 rsel9; 16334 - below: wr_r9 |
| T5 | 15128 | 14803-16490 rsel11; 16635 - below: wr_r11 |
| T6 | 15171 | 15115 - below: wr_r10 |
| T7 | 15214 | 14860 - below: rsel13 |
| T8 | 15258 | 14905 - below: rsel12 |
| T9 | 15301 | 15000-16266 rsel14 (taps at 15692 and 16253); 16415 - below: wr_r14 |
| T10 | 15344 | 15040-15966 rsel15 (taps at 15428 and 15953); 16114 - below: wr_r15 |
| T11 | 15388 | 14812-14905 rsel12 on its way to T8; 15073 - below: rsel16_buf |
| T12 | 15431 | 14770-15000 rsel14 on its way to T9; 15336 - below: rsel17_buf |
| T13 | 15474 | 14812-15040 rsel15 on its way to T10; 15098-15218 stub of wr_stb_n; 15593 - below: rsel15_buf |
| T14 | 15517 | 14770-15144 rsel17; 15853 - below: rsel14_buf |
| T15 | 15561 | 14822 - below: wr_stb_n |

## Ports

Local name, layer, where it crosses the boundary, direction.

| Name | Layer | Crossing | Direction | What |
|---|---|---|---|---|
| rsel0..rsel17 | metal | x of the column, y 14650 (top) | in | select columns of the decode array |
| vss | metal | 14140-14200, 14700 (top left) | - | decode array's VSS bus |
| vcc | metal | 14609, 16550 (bottom) | - | gate column supply rail, comes from below |
| rsel7 | metal | 14083, 14636-16490 | - | this line runs just outside the region's west edge (x < 14100) but belongs to it |
| wr_r6 | poly | 14100, 14867 (west) | out | rsel6 AND NOT strobe |
| wr_r1 | poly | 14100, 14909 (west) | out | rsel1 AND NOT strobe |
| wr_r2 | poly | 14100, 14957 (west) | out | rsel2 AND NOT strobe |
| wr_r0 | poly | 14100, 15001 (west) | out | rsel0 AND NOT strobe |
| wr_r4 | poly | 14100, 15043 (west) | out | rsel4 AND NOT strobe |
| wr_r7 | poly | 14135, 16550 (bottom; drawn to 16760) | out | rsel7 AND NOT strobe. Its NOR is at y 16600-16720 |
| wr_stb_n | metal | 14307, 16550 (bottom) | in | strobe of the left half |
| wr_stb_n | metal | 14912, 16550 (bottom) | - | strobe of the right half, continues down |
| wr_stb_n | metal | 15561, 16550 (bottom) | - | same net on T15, continues down |
| wr_stb_n | poly | 15850, 14825 (east) | in | where the strobe arrives |
| wr_r5 | metal | 14954, 16550 (bottom) | out | T1 |
| wr_r3 | metal | 14998, 16550 (bottom) | out | T2 |
| wr_r8 | metal | 15041, 16550 (bottom) | out | T3 |
| wr_r9 | metal | 15085, 16550 (bottom) | out | T4 |
| wr_r11 | metal | 15128, 16550 (bottom; starts at y 16635) | out | T5. At y 16550 T5 is still unconnected: rsel11's line ended at 16490 |
| wr_r10 | metal | 15171, 16550 (bottom) | out | T6 |
| rsel13 | metal | 15214, 16550 (bottom) | out | T7, not used inside the region |
| rsel12 | metal, poly | 15258, 16560 (bottom) | out | T8, not used inside the region; contact at 15258,16560 to a poly line going east along y 16560 |
| wr_r14 | metal | 15301, 16550 (bottom) | out | T9: rsel14 AND NOT strobe |
| wr_r15 | metal | 15344, 16550 (bottom) | out | T10: rsel15 AND NOT strobe |
| rsel16_buf | metal | 15388, 16550 (bottom) | out | T11: rsel16 buffered |
| rsel17_buf | metal | 15431, 16550 (bottom) | out | T12: rsel17 buffered |
| rsel15_buf | metal | 15474, 16550 (bottom) | out | T13: rsel15 buffered |
| rsel14_buf | metal | 15517, 16550 (bottom) | out | T14: rsel14 buffered |
| vss | metal | 14434, 14789, 15690 at 16550 (bottom) | - | the three ground rails run on down (the two of the gate column end near y 16870) |
| vcc | metal | 15795-15890, whole east edge | - | supply rail of the right-hand column; wider than the region, extent not traced |

The bars of the five west outputs run on west under two wide rails at x 13895-13935
and 13985-14030 to at least x 13880.

## Ambiguities

- `wr_stb_n` / `wr_stb_n`: see Logic. Working assumption: one net. Settled by
  tracing y 16700-17050, x 14200-14930 (package bd3).
- Loads of the right-hand column (all `?` shapes at x 15745-15880). What is established:
  each output band runs east from its pull-down, passes under a poly block near
  x 15770-15843 and ends on a contact land under the supply rail at x ~15862 (seen
  plainly for the R15 pair at 15862,15965 and 15862,16105, view x 15695-15895,
  y 15895-16235); a buried contact beside each block (for example 15760,14970 and
  15780,16180) ties the block to the output. So each output has one depletion load to
  the supply. Not established: the exact outlines, hence W/L. The trace places a block,
  a tie and a contact on the band where they give that circuit; the first inverter of
  the R16 buffer has a visibly larger block than those of the R17, R15, R14 buffers,
  which the trace does not show. To settle: 4x views of x 15730-15890 per gate.
- The supply rail x 14609 is called vcc from the orientation of the loads; its top end
  is at y 14904 and its source is below the region. The rail x 15795-15890 likewise.
- decode.txt draws the rsel16 column metal to y 14662 like the others. That column has
  no contact at y 14650: its metal continues (jogging right) to 15755,14783. Harmless;
  sel.txt adds the continuation.
- Metal stub on T13 from the strobe bar's contact 15474,15172 up to y 15098: it ends
  just below the poly bar of rsel16_buf (y 15084) with no contact (4x view). Purpose unknown.

## Not done

- Exact load outlines in the right-hand column (above).
- Outside the region, seen while following wires: the gate column has one more,
  different, row at y 16740-16870 (bd3); the west outputs' bars continue past x 13880
  (bd1); the strobe's poly continues east of x 15850 at y 14825.

## Re-read item R3 (2026-11-27): the track field T0-T17

Matt Godbolt, on Claude Fable 5.2, 2026-11-27 07:33 -0600. Region x 14100-15850, y 14650-16550. **Found as drawn but for the
place of two metal legs (geometry only).**

R3 asks for the track field between and below the gates checked like R1 and R2 (every track end, every
interruption, contacts, poly under tracks), "`rsel12`/`rsel13` carried through with no contact in particular".
Done with `tools/bd1_audit.py 14100 14650 15850 16550` (every trace file loaded; output kept in
`cache/scratch/sel/r3/audit.txt`) and `tools/bd1_sheet.py` for the flagged spots (sheets `sh1`..`sh4`, views
`v1`, `v2` in `cache/scratch/sel/r3/`):

1. **Breaks**: 8 candidates, 7 of them the rings of drawn contacts. The eighth, (15249,14847), is a real
   misplacement: the horizontal leg of `rsel13`'s metal from its contact (15300,14783) west to track T7 was
   drawn along y 14860 and lies at y 14864-14880; the same leg of `rsel12`'s metal (to T8) was drawn along
   y 14905 and lies at y 14907-14922 (down x 15250 and x 15320 in both metal shots). Redrawn along y 14872 and
   y 14914: same ends, same nets. No break.
2. **Undrawn metal**: none.
3. **Contact holes in the clean shot under drawn thin metal**: every drawn contact on the tracks has its hole
   (29 on T0-T17; (14128,16171) alone has a red-brown box instead, with ring and bright centre in both metal
   shots: real). Spots with no drawn contact, each looked at: (15258,14856), (15223,14857), (15343,14899),
   (15285,14900) were open ground under the two misplaced legs (gone after the fix); (15152,14807),
   (14947,14816), (14222,15544) are the rims of drawn contacts' pads; (15210,15267), (14124,15388),
   (14912,16238), (15090,16387) are specks beside plain tracks; (15085,15542) is a green interference patch
   under a plain track (bright and unringed in both chips); (14348,15000), (14341,15001), (14350,15015),
   (14350,15124), (14345,15132) are the cream centres of two framed boxes of the write-strobe gate column
   (drawn `B`) that the thin metal x 14338-14356 passes over: the class of re-read item R41 (a thin metal over
   node boxes), not a new finding and not settled here.
4. **`rsel12` and `rsel13` carried through with no contact**: along T7 (x 15214) and T8 (x 15258) from y 14890
   to y 16552 the clean shot is pink (field under metal) for 1,619 and 1,587 of 1,662 px and salmon (a poly
   row crossing, no hole) for 32 and 37; the only other stretches are one 6 px speck each ((15214,15266),
   (15258,15334)). Confirmed: no tap on either before the region's bottom edge.
5. **Poly gaps**: 7 candidates. Four at the top edge (y 14700-14738, x 14446-14794) are the pink field beside
   poly columns that are orange and unbroken (sheet `sh3`). (15552,14852): `rsel16`'s poly column is drawn at
   x 15541-15563 and lies under the track at x 15557-15569 (salmon there, pink at x 15552): 10 px west of its
   place, not a gap (left as drawn: the same ends). (15745,15170) and (15745,15430): the gate bar of the
   right-hand column's cell (`P 15600,14910 x15757` in the cell, drawn "schematically") is drawn to x 15757,
   and at x 15745 all four shots are plain field: the bar ends further west. Geometry of a cell master
   (a pull-down's width), left for whoever next opens the gate column; noted in the handoff.

Limits: the audit's (its docstring); the ring detector is useless here (a poly row under a track every 20 px
looks like a ring), so "no undrawn contact" rests on the clean shot, which is free of interference colours
along the tracks but for the one patch named.

Connections before and after the two legs' fix (commit aa6682c against the fixed tree):

    tools/t.sh sel sameconn.py aa6682c            ->  connections identical
    .venv/bin/python tools/sameconn.py aa6682c    ->  connections identical

## Review

