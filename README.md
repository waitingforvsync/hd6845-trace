# HD6845S die trace

Reverse engineering the Hitachi HD6845S CRT controller (the 6845 "type 0" of the Amstrad
CPC world) from die photographs, down to a complete transistor netlist, with the aim of
an exact model of its behaviour, including the undocumented edge cases, and a "visual
6845" that runs the netlist in a browser over the die layout.

- **Who is working on what**: the dashboard, https://waitingforvsync.github.io/hd6845-trace/dashboard/
  (rebuilt on every push by `.github/workflows/dashboard.yml` from `tools/dashboard.py`)
- What is established so far: `notes/operation.md`
- The plan and milestones: `PLAN.md`
- The trace (plain-text geometry): `trace/`; generated outputs (SVG, netlist, floor plan): `out/`

## Contributing

Read `notes/workflow.md` first: how a package of the die is claimed (`tools/claim.py`,
which needs write access: ask the owner), traced on its own branch, independently
reviewed and merged. Then `notes/tracing-guide.md` before tracing anything. The list of
tracing work is `notes/work-packages.md`; the active claims are in `claims/`.
