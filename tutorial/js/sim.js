// A switch-level simulation of the traced netlist, and the small logic-level latch.
// The transistor list is what the extraction tool recovered from the traced polygons
// (tutorial/data/example.json); nothing here is typed in by hand.

/**
 * Depletion-load NMOS, switch level. A node is low if a chain of conducting enhancement
 * transistors joins it to VSS; otherwise it is high if a depletion load joins it to VCC.
 * Transistors whose kind is 'load' are the always-on depletion devices (the weak pull-ups).
 */
export function simulate(ex, inputs) {
  const byName = {};
  for (const [id, n] of Object.entries(ex.nets)) for (const nm of n.names) byName[nm] = +id;
  const vss = byName.vss, vcc = byName.vcc;
  const val = {};                                   // node id -> 0 | 1
  val[vss] = 0; val[vcc] = 1;
  for (const [name, v] of Object.entries(inputs)) val[byName[name]] = v;
  const fixed = new Set([vss, vcc, ...Object.keys(inputs).map(n => byName[n])]);
  const nodes = Object.keys(ex.nets).map(Number).filter(n => !fixed.has(n));
  for (const n of nodes) val[n] = 1;
  const pulled = {};                                // node -> true if a load reaches VCC
  for (const t of ex.channels) if (t.kind === 'load') for (const [a, b] of [[t.a, t.b], [t.b, t.a]]) if (a === vcc) pulled[b] = true;
  const conducting = [];
  for (let iter = 0; iter < 12; iter++) {
    conducting.length = 0;
    for (const t of ex.channels) if (t.kind !== 'load' && val[t.gate] === 1) conducting.push(t);
    // flood from VSS through conducting transistors
    const low = new Set([vss]);
    let grew = true;
    while (grew) {
      grew = false;
      for (const t of conducting) {
        const inA = low.has(t.a), inB = low.has(t.b);
        if (inA !== inB) { low.add(inA ? t.b : t.a); grew = true; }
      }
    }
    let changed = false;
    for (const n of nodes) {
      const v = low.has(n) ? 0 : (pulled[n] ? 1 : val[n]);
      if (v !== val[n]) { val[n] = v; changed = true; }
    }
    if (!changed) break;
  }
  const on = new Set(ex.channels.filter(t => t.kind === 'load' || val[t.gate] === 1).map(t => t.id));
  return { val, byName, on };
}

/** The data-bus input latch: two cross-coupled AND-OR-invert gates, gated by `le`. */
export function latchStep(state, d, le) {
  let { q, qn } = state;
  const dn = d ? 0 : 1;
  for (let i = 0; i < 8; i++) {                        // relax: alternate so a holding pair settles
    const q2 = (dn && le) || qn ? 0 : 1;
    const qn2 = (d && le) || q2 ? 0 : 1;
    if (q2 === q && qn2 === qn) break;
    q = q2; qn = qn2;
  }
  return { q, qn, dn, out: qn ? 0 : 1 };
}
