# busc: the bus field between the strobe logic and the input buffer row

Region x 13200-17750, y 16900-18560 (master list). Trace: `trace/busc.txt`. Only the block below the data bus
column is traced here (run 1); the rest of the region is other packages' wiring (`cdp4`, `regs`, `bd2`) or
untraced.

## Run 1 (2026-11-27), piece `dhz`: the driver of `d_hiz`

Matt Godbolt, on Claude Fable 5.2, 2026-11-27 06:41 -0600. Region x 17040-17450, y 17070-17965, and the output's metal
north and east to (17641,17084). 10 transistors, 2 new nets (`rd_data_e_n`, `rd_data_e_b`; `d_hiz` gets its
driver), 0 errors, 0 warnings, no uncertain item. Views in `cache/scratch/busc/`: `s1_m`, `s2_*` (overviews),
`a_*`, `b_*`, `c_*`, `d_metal`, `k_*`, `p6`, `top_m` (photos at 3.3-6x), `o1_c`, `o2_c`, `o3_c`, `om1`, `om2`
(overlays). The clean shot is unusually readable here (wide transistors under contact straps: tan diffusion,
salmon poly, pits where contacts were), so diffusions and polys were taken from it by runs of colour classes
down columns and along rows, the straps and contact rings from the two metal shots (`tools/busc_rings.py`,
`tools/busc_pits.py`), and every junction from raw profiles (`tools/px.py`).

### What it establishes

    rd_data_e_n = NOT rd_data_e                 stage 1: pull-down G7, depletion load Gs                firm
    rd_data_e_b = NOT rd_data_e_n               stage 2: pull-down G6, depletion load under the E block firm
    d_hiz       : pulled to VCC through G1 (two parts), G3 and G4 while rd_data_e_n is high,
                  pulled to VSS through G2 and G5 while rd_data_e_b is high        (a push-pull output stage)

So **`d_hiz` = NOT `rd_data_e`**, buffered: the data pins are driven while `rd_data_e` is high, that is (`bd2`
run 3) while `e_b` is high in a read of the data register by the selected chip, and float otherwise. The high
level of `d_hiz` is made through enhancement pull-ups (one threshold below VCC, believed). The input
`rd_data_e` arrives on `bd2`'s thin metal (pad (17080,17949), metal east along y 17950); the output leaves on
a metal north along x 17363 and east along y 17084 into the data bus column's `d_hiz` metal (x 17631-17651,
`dpad`).

**Which rail is which.** The west supply is VCC by drawing: it is one metal with the data bus column's VCC
rail (`dbus`: `M 17527,8287:17585,17000`), through the wide metal y 16970-17020 that the rail turns west into
and that metal's turn south along x 16990-17060 to the strap over islands A1 and A2 (view `top_m`). The east
rail (x 17406-17452) is **taken as VSS and labelled so**: the pull-downs of both inverters and of the output
end on it, both loads have their gates tied to the node on their other side, and nothing else fits; where it
goes from its foot (east at y 17850-17906) is not drawn; review round 1 followed it east and south on a wide
metal x 17465-17520 to `inrow`'s `vss` rail (Ambiguity 1).

### Layout: one stack of strips

Horizontal poly gates over wide diffusions; every strip between two gates has a metal strap with a row of
contacts at a 40 px pitch. From the top (y of each strip from the clean shot down x 17190, 17290, 17330):

| y | Strip or gate | On |
|---|---|---|
| 17128-17188 | islands A1 (x 17118-17220) and A2 (x 17250-17324), field between them | VCC |
| 17189-17211 (17173-17211 over A2) | gate G1 | `rd_data_e_n` |
| 17213-17256 | strip A3 (x 17118-17336; a field notch 17225-17245 down to y 17222 between the islands) | `d_hiz` |
| 17284-17327 | strip B1 (x 17160-17369) | VSS |
| 17329-17347 | gate G2 | `rd_data_e_b` |
| 17352-17398 | strip B2 | `d_hiz` |
| 17400-17418 | gate G3 | `rd_data_e_n` |
| 17423-17468 | strip B3 (x 17119-17369) | VCC |
| 17471-17489 | gate G4 | `rd_data_e_n` |
| 17494-17539 | strip B4 | `d_hiz` |
| 17542-17558 | gate G5 | `rd_data_e_b` |
| 17565-17610 | strip B5 | VSS |
| 17612-17634 | gate G6 | `rd_data_e_n` |
| 17636-17680 | strip B6 (x 17181-17362) | `rd_data_e_b` |
| 17690-17727 | the E block: poly over the column x 17305-17362 | `rd_data_e_b` (stage 2's load) |
| 17730-17778 | the load's box, contact (17335,17753) | VCC |
| 17706-17748 | Ds1 (x 17119-17196), contact (17158,17726) | VCC |
| 17750-17788 | gate Gs (x 17088-17226) | `rd_data_e_n` (stage 1's load) |
| 17799-17842 | strip D1 (x 17118-17362) | `rd_data_e_n` |
| 17845-17867 | gate G7 | `rd_data_e` |
| 17869-17908 | strip D2 | VSS |

Transistors as extracted: G1 102/22 and 74/38 (the poly is 38 long over A2), G2 199/18, G3 and G4 250/18,
G5 250/16, G6 188/22, G7 244/22, loads 59/37 (stage 2) and 77/38 (stage 1).

### The polys

- **`rd_data_e_n`**: G1's west end runs on west to x 17083 and south as a column x 17083-17099 under the VCC
  metal (salmon, no hole) to the pad P3 (17084,17404); G3 starts from that pad. G4 and G6 have pads of their
  own, P4 (17083,17492) and P6 (17082,17620). One thin metal x 17074-17092 joins the three pads and runs on
  south to the strap over D1 (`tools/follow.py 17085 17550 N`: end (17083,17402); `S`: corner (17093,17822),
  east to (17351,17817)). Each pad has a ring in both metal shots and a hole in the clean shot
  (`busc_rings.py`: 112, 147, 112). A small dark ring at (17100-17115, 17610-17630) beside P6 is G6's poly in
  the gap between that thin metal and the VCC inner rail, not a contact (view `p6`).
- **`rd_data_e_b`**: G2 and G5 both run east into a column x 17406-17424 along the block's east side, under
  the VSS rail (salmon, no hole). The column's foot turns west along y 17686-17704 into the E block, and an arm
  of it ends in a framed box (17250-17280, 17686-17724) on a tongue of strip B6 (down x 17265: tan from B6
  through the box, with two thin bars where metal edges cross). So the strip B6 is this net.
- **Gs** ends east in a framed box (17222-17252, 17756-17792) on a tab of strip D1: stage 1's load is tied to
  its output.
- **G7** runs east past the stack and south (x 17420-17440, past the VSS rail's foot) to the pad
  (17428,17949), the east end of `rd_data_e`'s thin metal y 17950.

### The loads

- Stage 1: the diffusion x 17119-17196 runs from Ds1 (VCC: contact (17158,17726) on the strap of the inner
  rail) south under Gs into D1.
- Stage 2: the column x 17305-17362 runs from B6 south under the E block to the box (17305-17362,
  17730-17778) with its contact (17335,17753; ring 135). The column's west edge is one dark line x 17300-17304
  from y 17685 to y 17785 in the clean shot, across block and box alike. The box's metal is the VCC arm: row
  y 17738 is metal in both chips from x 17268 across a single 8 px line (the box's west edge under the metal)
  to x 17324; at y 17752 there is no metal west of the box. The arm also covers the E block's lower part
  (y 17706-17727: chip 1's metal shot is metal there, and the clean shot is salmon with no hole, 228-241 /
  151-180: no contact; chip 2's metal shot is dark there, which is not explained).

### The metals, and the gaps between them

- **VCC**: the wide metal's foot (x 17040-17112), its strap over A1 and A2, south along x 17078-17112 to
  y 17366 (x 17080-17100 down to y 17262, to x 17121 below), an inner rail x 17124-17156 from y 17320 to
  y 17748 with straps over B3 and Ds1, and an arm east along y 17706-17746 (y 17727-17746 where it passes
  stage 2's tie box) to the load's box.
- **VSS**: the east rail x 17406-17452 from y 17286 to its foot at y 17906, with straps over B1, B5 and D2.
- **`d_hiz`**: the strap over A3; a link x 17176-17206 south (over B1's west end and G2: no pit, salmon) to the
  strap over B2; from that strap's east end a link x 17338-17372 south (over the east ends of G3 and G4 and
  the east end of B3: no pit) to the strap over B4; and from A3's strap the output north along x 17353-17373
  to y 17077 and east along y 17078-17090 to the column's metal (`tools/follow.py 17354 17200 N --gap 30`:
  corners (17366,17084) and (17646,17085), then south on the column's metal). No pad on the run east
  (`cdp4_candh.py h` every 6 px, x 17380-17630: none).
- **`rd_data_e_n`**: the strap over D1 and the thin metal x 17074-17092 north over P6, P4 and P3.
- **`rd_data_e_b`**: the strap over B6 alone.
- Gaps measured as bare ground between two edge lines in both metal shots (`tools/px.py`): the `d_hiz` link
  against B1's strap (row y 17300, x 17218-17226), B3's strap against the east link (row y 17445,
  x 17334-17346), the east link against the VSS rail (x 17386-17396), the VCC inner rail against B5's and B4's
  straps (rows y 17585 and y 17515, x 17166-17174), the VCC metal's south end against the thin metal (down
  x 17085: metal to y 17366, orange poly y 17374-17388, metal from y 17398), the thin metal against the inner
  rail (rows y 17450 and y 17580: ground x 17102-17108, olive in the clean shot).
- Hidden branches: `tools/eof_tee.py` on every gate and both columns: none.

### Field, not layout

Plain areas inside the block that are field (chip 2's stripped shot R-G 0-8 against +14..+26 on diffusion):
the rectangle (17255-17300, 17755-17790); the outlined strip round the block's foot (17060-17100, 17845-17935
and y 17915-17935); the area east of the top group (17385-17460, 17105-17260).

### Ambiguities

1. **The east rail is VSS by reasoning, not by drawing.** If it were not, nothing here would work as a
   circuit. Review round 1 followed its foot to `inrow`'s `vss` rail by a wide metal (x 17465-17520) that no
   package draws yet.
2. **The two framed boxes** (the ties of the two loads) are drawn `B`: heavy outline, lighter centre, each at
   the end of a load's gate poly that has no other driver.
3. **Stage 2's load diffusion under the E block** is not seen (poly and metal lie over it); it is drawn
   because B6 and the box line up in x, their common west edge prints as one line, and the stage has no other
   load.
4. **The contact rows** are drawn where `busc_rings.py` finds a ring in both metal shots and the clean
   shot's pits agree; a contact more or less in a row changes nothing.
5. **G1's two parts**: over A2 the poly is 38 long against 22 over A1 (down x 17290 and x 17170 in both metal
   shots). Both islands are on VCC; why the right part is longer is not known.

### Ports

| Name | Layer | Where | Direction | What |
|---|---|---|---|---|
| `rd_data_e` | metal | (17100,17950) | in | `bd2`'s thin metal from its pad (17080,17949) |
| `d_hiz` | metal | (17641,17084) | out | joins the data bus column's `d_hiz` metal x 17631-17651 (`dpad`) |
| `vcc` | metal | x 17040, y 17130-17270 (west) | supply | the wide metal from the column's VCC rail |
| `vss` | metal | (17442,17880) (east) | supply | the east rail's foot; goes on east, not followed |

### Not done

- Where the east rail goes from its foot.
- The rest of `busc`'s region.

## Review

### Round 1 (full review), 2026-11-27, piece `dhz`

A fresh Claude Fable 5.2 agent, on commit 8826117, 20 images in `cache/scratch/busc/review-1/` (4.3-6x in two
or more shots, with `tools/px.py`, `tools/textmap.py`, `tools/follow.py`, `tools/busl_mdrawn.py`). Told to
suspect: which strap is on which metal (the two `d_hiz` links past B1's and B3's straps, the east link against
the VSS rail, the thin metal against the inner rail and the VCC metal's south end, the straps over B4, B5 and
B6 against the inner rail, B1's and B5's straps into the east rail, B3's and Ds1's into the inner rail); the
strap over A1 and A2 and whether the wide metal is the VCC rail's; the poly joins and any contact on either
poly column; the two buried contacts and whether the loads' diffusions exist; a contact from the VCC arm to
the E block; G1's two parts and the loop between the islands; the output's metal; anything not drawn.

Findings, none of which changes a connection (all confirmed by me and fixed):

1. **Inner VCC rail** is x 17124-17156, not x 17106-17140 (row y 17515: metal x 17126-17154 in both chips,
   bare ground x 17105-17117). Moved, with the straps that start on it.
2. **East rail** is x 17406-17452 (row y 17505), drawn x 17400-17442. Moved.
3. **The VCC arm** was drawn over the lower half of stage 2's tie box; at x 17250-17280 it is y 17727-17746 and
   clears the box. Narrowed there. No contact either way.
4. **The west VCC metal** is x 17080-17100 for y 17180-17258 and widens to x 17121 only below y 17262. Redrawn.
5. **Gs** runs west to x 17088 (drawn 17100), **G7** to x 17096 (17110), **B1**'s west edge is x 17160 (17170).
6. **The loop between the islands** is a field notch in A3 (17225-17245, down to y 17222); G1 is one poly, 36-38
   long over A2 and 20 over A1. Notch drawn (Ambiguity 5 stands: the reason for the longer part is not known).

Checked and found as drawn by the reviewer: every gap between metals of different nets is bare ground between
two edge lines in both chips, with no pit or hole under either link or under the inner rail over B2, B4 and
B5; the strap over A1 and A2 is one metal with the wide VCC metal, which runs to `dbus`' rail; B1, B5 and D2
join the east rail, B3 and Ds1 the inner rail; the poly joins (G1, the west column and P3, with open poly
y 17372-17388; G3, G4 and G6 from their pads, stopping at x 17386 with field before the rail; G2 and G5 into
the east column; the foot into the E block; G7 to its pad); no contact on either poly column, on G7's column
or on the E block (chip 2's dark patch is absent in chip 1); stage 2's channel exists (diffusion edge lines
cross the open poly at x 17300-17306 and x 17369-17375), Ds1 runs under Gs into D1, both tie boxes read as
buried contacts; the output is one metal to (17641,17084), joined to the column, crossing a poly column at
x 17528-17548 without contact; the three outlined areas and the strip x 17045-17068 are field.
**The east rail** (the reviewer's own following, not drawn here): from its foot east, then south on a wide
metal x 17465-17520 to `inrow`'s `vss` rail (y 18381-18431), clear of `inrow`'s VCC band. So Ambiguity 1 has
a second leg to stand on; the wide metal is no package's yet.
Could not be settled from the photos (reviewer): the thin metal through the rims of P4 and P6 (6 px bands
that read orange in chip 2 and yellow in chip 1; read as metal over poly, and nothing else could feed G4 and
G6); B5's strap into the rail (a 9-12 px dark line that coincides with the poly column's west edge beneath);
a greenish patch at (17265,17710) in stage 2's tie box in the clean shot, like a contact hole, with no bright
centre in either metal shot (stage 1's box, with no metal near, shows the same green).

Connections before and after the fixes (commit 8826117 against the fixed tree):

    tools/t.sh busc sameconn.py 8826117            ->  connections identical
    .venv/bin/python tools/sameconn.py 8826117    ->  connections identical

Recorded 2026-11-27 07:06 -0600.

Round 1: no findings that change a connection.
