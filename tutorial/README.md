# From photo to netlist: the tutorial page

An interactive explanation of how the HD6845S's circuit is recovered from die photographs, with a
worked example (`trace/examples/pilot.txt`: an inverter feeding a NOR). Open `index.html` through any
static web server (`python3 -m http.server` in this folder); it fetches `data/` and loads three.js
from a CDN.

- `export.py` writes `data/`: photo crops and `example.json` (polygons, channels, nets, the extracted
  equations) from the repository's trace and the aligned photos in `cache/`. Run it from the
  repository root with the project's Python. Nothing else in the repository reads this folder.
- `js/photo.js` flat zoomable photo viewer, `js/stack.js` 3D layer view, `js/sim.js` switch-level
  simulation of the extracted netlist, `js/schem.js` diagrams, `js/steps.js` the worked example's
  steps, `js/main.js` the wiring.
