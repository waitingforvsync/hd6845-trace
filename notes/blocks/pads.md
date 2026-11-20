# Pad cells

## Output driver (`outdrv`, trace/pads_out.txt): done

23 instances: MA0-13, RA0-4, HSYNC, VSYNC, DISPTMG, CUDISP. Master is MA3.

- Pre-driver: two inverters in series under the inner VCC band. Input is a poly line
  from the core (`<pin>_drv_in`), first inverter output `<pin>_pu`, second `<pin>_pd`.
- Output pair: three pull-up fingers from VCC gated by `_pu`, three pull-down fingers
  to VSS gated by `_pd`. So the pad is the inverse of `_drv_in`.
- The pre-driver's ground reaches it through a wide diffusion tunnel under the pad
  neck (752-1027 x 3428-3568 on the master), because the VSS ring is on the far side
  of the pad from the core.
- The bond pads themselves are not in the cell: each pad sits differently relative to
  its driver. Only MA3's pad is drawn so far.

## Input pads

Bottom right (trace/inprot.txt, trace/inrow.txt):

| Pin | Path | Core-side nets |
|---|---|---|
| CLK | protection cell 1, then three-finger inverter, then two-finger inverter | `clk_n` = NOT clk, `clk_b` = clk buffered; `clk_b` leaves left along y 19070 |
| R/W | protection cell 2, then four inverters in a chain | `rw_a` = NOT rw, `rw_b` = rw, `rw_c` = NOT rw, `rw_d` = rw |
| E | protection cell 3, then three-finger and two-finger inverters | `e_n`, `e_b`; `e_b` goes up to the core in a wide poly line at x 16660-16705 |
| RS | protection cell 4, then four inverters | `rs_a` .. `rs_d` |
| CS | protection cell 5, then four inverters | `cs_a` .. `cs_d` |

In each four-inverter group the b and c outputs also connect to a large plain
diffusion rectangle (about 130 x 220 px), which looks like added capacitance.
One further inverter at the left end of the row (input from the core in poly,
output leaving left along y 18775) is not yet identified.

Top (trace/pads_in_top.txt):

| Pin | Path | Core-side net |
|---|---|---|
| LPSTB | left comb cell at 6380-6650 x 833-1280, then small inverter and two-finger inverter | `lpstb_b` = pin level, on the wire at y 1686 |
| RES | strip from the contact at 7880,1315, right comb cell, then the same two stages | `res_b` = pin level, on the wire at y 1730 |

Not yet drawn: the strips from the pads to the protection cells and from those to
the buffers, the two top comb cells, and the wiring below the buffer row.

## Data pad (D0-D7): in progress

**Superseded (coordinator, from the 2026-11-17 handoffs) by `notes/blocks/dpad.md`**, which traces the cell (AMB-003 closed). Several
readings below are wrong: rows G and K are the pull-up gate node, not VCC; H and J are VSS; I is
the pull-down node; the "green shapes" are field islands; the boxes at 18597-18632 x 7250-7298,
17835-17858 x 7440-7460 and strip 4's end are not buried contacts; "gate 7170" is a field strip
(items 3, 5 and 7 below). Kept as the record of the first reading.

Eight instances at dy = 0, 1735, 3470, 5054, 6637, 8242, 9847, 11452 from D0 (D0 at
the top, D7 at the bottom). Master rectangle 17600,5950:19200,7600. A median composite
of the eight (`tools/composite.py dpad ...`, view with `--comp dpad`) removes the etch
residue that hides the logic under the VCC band; raw metal of a clean instance
(`--shift 1,5054` for D3) shows where metal really is.

Read so far (D0 coordinates), all still to be confirmed by trace and extraction:

- Main fingers, top to bottom: A VCC (y 6757), B pad (6833), C VSS (6908), D pad
  (6983), E VCC (7058), F pad (7135). Gates between them at 6798, 6870, 6947, 7020,
  7097. A and E run on under the VCC band (x 17900-18200); C leaves to the right to
  the VSS ring.
- Right group below F (x 18740-19050): rows G' VSS (7215), H' pad (7290), I' VSS
  (7365), enclosed by one poly frame (strips at 7180, 7250, 7325). More pull-down
  fingers. The frame is fed from a poly bar at x 18684-18740 through three contacts
  on a metal column that comes from row I of the left group.
- Left group below F (x 18230-18660): rows G (7200), H (7275), I (7350), J (7425) and
  a three-contact row K (7517), with gate strips between them (T1 7237, 7312, 7386)
  joined into one spiral, and a separate strip P_y (7478) between J and K. Row G and
  row K are joined by a vertical metal at x 18228-18246.
- Left of the VCC band two metal straps collect the gate ends: S1 (x 17862-17883)
  takes the gates at 6798, 7020, 7097 and 7170, and S2 (x 17804-17825) the gates at
  6870 and 6947. So S1 is the pull-up gate net and S2 the pull-down gate net.
- Under the VCC band: three VCC contacts at (17977-18057, 7292) with a load block
  above (U', y 7225-7266) and below (L', y 7316-7359). Two poly lines enter from the
  bus-interface side: P_x (y 7399-7422, turning up at x 18170) and P_y (y 7465-7492).

Re-read from the clean shot of chip 1 with the eight-cell metal composite
(2026-11-14). Much more is now established, but the cell has more logic than the
"two lines in, two gates out" picture assumed, and it is still not traced. Parked
again (AMB-003); the facts below are the starting point for finishing it.

Established (D0 coordinates):

1. Straps. S1 (metal, x 17857-17882) collects the pull-up gates; S2 (x 17797-17822)
   the pull-down gates 6870 and 6947. Each also contacts a diffusion:
   - S1 at (17862,7208), box 17845-17887 x 7180-7247, and again at its lower end at
     (17855,7512), box 17840-17885 x 7495-7545.
   - S2 at (17815,7335), box 17800-17845 x 7310-7360, which extends right to x 17895.
   S1 crosses the line P_x at y 7365-7430 without a contact.
2. Line P_x. Arrives from the bus-interface side as poly along y 7378-7398, widens to
   a vertical piece at x 17855-17885 (y 7365-7430), runs right under the band along
   y 7405-7430, steps up at x 18160-18200 and becomes strip 3 (y 7380-7400, between
   rows I and J). At x 18635-18658 it turns up, runs to y 7228 and comes back left as
   strip 1 (y 7228-7250, between rows G and H), ending at x 18183. On the way it is
   tied to the right-hand end of row H by a buried contact (window 18597-18632 x
   7250-7298). Row H's metal (eight contacts) ends at x 18592 and does not reach the
   contact column.
3. Line P_y. Arrives along y 7460-7500, crosses the lower S1 diffusion box as a gate
   (y 7470-7492), runs right under the band and ends over row K with a buried contact
   at 18355-18387 x 7455-7500. So there is a transistor, gate P_y, between the
   S1-contacted diffusion below it and a diffusion above it (17840-17885 x
   7440-7468), which has a small buried contact at 17835-17858 x 7440-7460 to poly.
   Which poly is not resolved; if it is P_x this is a pass transistor from P_x onto
   the pull-up gate net.
4. Under the band. Poly bar U' (17920-18160 x 7227-7266) turns down at x 18140-18160
   and becomes strip 2 (y 7302-7322, between rows H and I, ending at x 18595). Bar L'
   is 17940-18112 x 7318-7355. A diffusion with three VCC contacts lies between the
   bars (17958-18092 x 7266-7318).
5. Two closed shapes with heavy outlines and green interiors, each crossing both
   bars: 17917-17945 x 7218-7368 on the left, and on the right 18097-18116 x
   7252-7368 joined to a box 18095-18200 x 7218-7258. In that box the end of U'
   (x 18160) and the end of strip 1 (x 18183) face each other across a 20 px green
   gap. The metal composite shows no gap in the VCC band here.
6. Row I's metal (three contacts) runs right along y 7335-7375 and up a column at
   x 18678-18722 whose three contacts land on the poly bar that feeds the frame gates
   of the right-hand group.
7. Rows: G VCC, J VSS, K VCC (three contacts). Row K with strip 4 over its top edge
   reads as a depletion load on P_y.

Not established: what the two green shapes are (item 5). Read as buried-contact
windows they tie U', L', strip 1 and strip 2 into one net, and then no assignment of
the rows gives a working circuit; so that reading, or one of items 2-4, is wrong
somewhere. Also open: where row H's metal goes at its left end, and what the frame
group does if row I is not simply the pull-down gate net.

## Corrections (coordinator, from the handoffs of 2026-11-20, third batch)

- The DISPTMG driver's input `disptmg_drv_in` has its driver traced (`eof` run 27, 2026-11-20, firm): `disptmg_drv_in` = NOR(`eof_w17338`, `eof_w17168`, `eof_w17472`), a driver in the bottom-centre logic, by a wire with no tap. Geometry only, not changed: the input poly is drawn at x 5570-5595 from y 18912; the stripe in the clean shot is x 5578-5596 there (about 5 px east).
