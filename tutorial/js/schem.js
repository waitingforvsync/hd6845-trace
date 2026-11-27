// Hand-laid schematics and the cross-section. Wires carry data-net so a simulation can colour them.
const NS = 'http://www.w3.org/2000/svg';

/** One transistor symbol with its channel at (cx, cy). Leads sit at cx+10 (cx-10 when flipped). */
function tr(cx, cy, { load = false, flip = false, id = '', gate = '', label = '' } = {}) {
  const s = flip ? -1 : 1;
  const lead = cx + 10 * s, plate = cx - 6 * s, gl = cx - 24 * s;
  return `<g data-t="${id}" class="tsym">
    <line class="sym" x1="${plate}" y1="${cy - 14}" x2="${plate}" y2="${cy + 14}"/>
    <line class="sym ch" x1="${cx}" y1="${cy - 18}" x2="${cx}" y2="${cy + 18}" ${load ? 'style="stroke-width:6px"' : ''}/>
    <line class="sym" x1="${cx}" y1="${cy - 18}" x2="${lead}" y2="${cy - 18}"/>
    <line class="sym" x1="${cx}" y1="${cy + 18}" x2="${lead}" y2="${cy + 18}"/>
    <line class="w" data-net="${gate}" x1="${plate}" y1="${cy}" x2="${gl}" y2="${cy}"/>
    <line class="w" data-net="${'ch:' + id}" x1="${lead}" y1="${cy - 18}" x2="${lead}" y2="${cy - 30}"/>
    <line class="w" data-net="${'ch2:' + id}" x1="${lead}" y1="${cy + 18}" x2="${lead}" y2="${cy + 30}"/>
    ${label ? `<text x="${cx + 20 * s + (flip ? -34 : 0)}" y="${cy + 4}">${label}</text>` : ''}
  </g>`;
}
const w = (net, d) => `<path class="w" data-net="${net}" d="${d}"/>`;
const dot = (x, y) => `<circle cx="${x}" cy="${y}" r="3.5" fill="var(--ink)"/>`;
const txt = (x, y, t, cls = '', anchor = 'start') => `<text class="${cls}" x="${x}" y="${y}" text-anchor="${anchor}">${t}</text>`;

/** Inverter with depletion load. Nets: vcc, out, in, vss. */
export function inverter(svg, p = 'inv') {
  svg.innerHTML = [
    w('vcc', 'M40 20H270'), txt(40, 14, 'VCC'),
    w('vss', 'M40 225H270'), txt(40, 240, 'VSS (ground)'),
    tr(140, 70, { load: true, id: p + 'L', gate: p + ':out', label: 'load' }),
    tr(140, 160, { id: p + 'P', gate: p + ':in', label: 'pull-down' }),
    w('vcc', 'M150 20V40'), w(p + ':out', 'M150 100V130'),
    w(p + ':out', 'M116 70H100V115H150'), w(p + ':out', 'M150 115H250'), dot(150, 115),
    txt(255, 119, 'out', 'lbl'),
    w('vss', 'M150 190V225'),
    w(p + ':in', 'M116 160H60'), txt(56, 164, 'in', 'lbl', 'end'),
  ].join('');
}

/** Two-input NOR. */
export function nor(svg, p = 'nor') {
  svg.innerHTML = [
    w('vcc', 'M40 20H270'), txt(40, 14, 'VCC'),
    w('vss', 'M40 225H270'), txt(40, 240, 'VSS (ground)'),
    tr(120, 70, { load: true, id: p + 'L', gate: p + ':out', label: 'load' }),
    tr(120, 160, { id: p + 'A', gate: p + ':a', label: '' }),
    tr(210, 160, { id: p + 'B', gate: p + ':b', flip: true }),
    w('vcc', 'M130 20V40'), w(p + ':out', 'M130 100V115'),
    w(p + ':out', 'M96 70H80V115H130'), w(p + ':out', 'M130 115H200'), dot(130, 115),
    w(p + ':out', 'M130 115V130'), w(p + ':out', 'M200 115V130'), dot(200, 115),
    w(p + ':out', 'M200 115H262'), txt(266, 119, 'out', 'lbl'),
    w('vss', 'M130 190V225'), w('vss', 'M200 190V225'), dot(130, 225), dot(200, 225),
    w(p + ':a', 'M96 160H60'), txt(56, 164, 'A', 'lbl', 'end'),
    w(p + ':b', 'M216 160H245'), txt(250, 164, 'B', 'lbl'),
  ].join('');
}

/** The worked example's circuit: the inverter feeds the NOR. Nets by the extraction's names. */
export function example(svg) {
  svg.innerHTML = [
    w('vcc', 'M30 20H420'), txt(30, 14, 'VCC'),
    w('vss', 'M30 270H420'), txt(30, 286, 'VSS'),
    tr(90, 70, { load: true, id: '0', gate: 'a_out_L', label: 't0 load' }),
    tr(90, 160, { id: '1', gate: 'in_a_L', label: 't1' }),
    tr(250, 70, { load: true, id: '3', gate: 'b_out_L', label: 't3 load' }),
    tr(250, 160, { id: '4', gate: 'a_out_L', label: 't4' }),
    tr(330, 160, { id: '2', gate: 'in_c_L', flip: true }),
    w('vcc', 'M100 20V40'), w('vcc', 'M260 20V40'),
    w('a_out_L', 'M100 100V115'), w('a_out_L', 'M66 70H50V115H100'), w('a_out_L', 'M100 115V130'), dot(100, 115),
    w('vss', 'M100 190V270'),
    w('in_a_L', 'M66 160H34'), txt(30, 164, 'in_a', 'lbl', 'end'),
    w('a_out_L', 'M100 115H170V160H226'),
    w('b_out_L', 'M260 100V115'), w('b_out_L', 'M226 70H210V115H260'), w('b_out_L', 'M260 115V130'), dot(260, 115),
    w('b_out_L', 'M260 115H320V130'), w('b_out_L', 'M320 115H400'), txt(404, 119, 'b_out', 'lbl'), dot(320, 115),
    w('vss', 'M260 190V270'), w('vss', 'M320 190V270'), dot(260, 270), dot(320, 270),
    w('in_c_L', 'M336 160H372'), txt(376, 164, 'in_c', 'lbl'),
    txt(36, 114, 'a_out', 'lbl'),
  ].join('');
}

/** Colour every wire by its level and light the conducting transistors. level(net) -> 0|1|undefined. */
export function colour(svg, level, conducting = () => false) {
  for (const el of svg.querySelectorAll('.w')) {
    const v = level(el.dataset.net);
    el.classList.toggle('hi', v === 1); el.classList.toggle('lo', v === 0);
  }
  for (const g of svg.querySelectorAll('[data-t]')) g.querySelector('.ch').classList.toggle('on', conducting(g.dataset.t));
}

/** The data-bus latch as boxes and wires: each gate's output feeds the other gate. */
export function latch(svg) {
  const box = (x, y, wd, h, a, b) => `<rect x="${x}" y="${y}" width="${wd}" height="${h}" rx="8" fill="var(--surface)" stroke="var(--ink)" stroke-width="2"/>` +
    txt(x + wd / 2, y + h / 2 - 4, a, 'lbl', 'middle') + txt(x + wd / 2, y + h / 2 + 12, b, '', 'middle');
  svg.innerHTML = [
    box(140, 20, 150, 70, 'AND-OR-INVERT', 'q = NOT(d_n·le + q_n)'),
    box(140, 140, 150, 70, 'AND-OR-INVERT', 'q_n = NOT(d·le + q)'),
    w('d_n', 'M20 40H140'), txt(18, 34, 'd_n', 'lbl'),
    w('le', 'M20 65H140'), txt(18, 59, 'le', 'lbl'),
    w('d', 'M20 160H140'), txt(18, 154, 'd', 'lbl'),
    w('le', 'M20 185H140'), txt(18, 179, 'le', 'lbl'),
    // cross-coupling: q goes down into the lower gate, q_n goes up into the upper one (one crossing)
    w('q', 'M290 55H318V124H215V140'), txt(324, 90, 'q', 'lbl'),
    w('qn', 'M290 175H304V108H215V90'), txt(226, 99, 'q_n', 'lbl'),
    dot(304, 175),
    w('qn', 'M304 175H336'),
    `<polygon points="336,163 360,175 336,187" fill="var(--surface)" stroke="var(--ink)" stroke-width="2"/><circle cx="365" cy="175" r="4.5" fill="var(--surface)" stroke="var(--ink)" stroke-width="2"/>`,
    w('out', 'M370 175H412'), txt(412, 165, 'out', 'lbl', 'end'),
  ].join('');
}

/** Cross-section of an n-channel transistor; on = gate high. */
export function crossSection(svg, on) {
  const dots = on ? Array.from({ length: 9 }, (_, i) => `<circle cx="${186 + i * 11}" cy="${158}" r="3" fill="#ffd23f"/>`).join('') : '';
  svg.innerHTML = `
  <rect x="10" y="146" width="440" height="96" rx="6" fill="#8a8579" opacity=".55"/>
  <text x="225" y="234" text-anchor="middle" style="font-size:11px">p-type silicon (the wafer)</text>
  <rect x="40" y="146" width="130" height="46" rx="4" fill="var(--diff)" opacity=".85"/>
  <rect x="290" y="146" width="130" height="46" rx="4" fill="var(--diff)" opacity=".85"/>
  <text x="105" y="174" text-anchor="middle" style="fill:#052;font-weight:600">n+ diffusion</text>
  <text x="355" y="174" text-anchor="middle" style="fill:#052;font-weight:600">n+ diffusion</text>
  <rect x="170" y="140" width="120" height="6" fill="#cfd8dc"/>
  <text x="230" y="134" text-anchor="middle" style="font-size:10px">thin gate oxide</text>
  <rect x="165" y="100" width="130" height="38" rx="3" fill="${on ? '#ff6a5c' : '#c4463a'}"/>
  <text x="230" y="124" text-anchor="middle" style="fill:#fff;font-weight:600">poly gate ${on ? '(high)' : '(low)'}</text>
  ${on ? '<rect x="170" y="146" width="120" height="14" fill="#ffd23f" opacity=".35"/>' + dots : ''}
  <rect x="12" y="136" width="146" height="7" fill="#c9c6bb" opacity=".6"/><rect x="302" y="136" width="146" height="7" fill="#c9c6bb" opacity=".6"/>
  <rect x="88" y="76" width="34" height="62" fill="var(--metal)"/><rect x="338" y="76" width="34" height="62" fill="var(--metal)"/>
  <rect x="40" y="60" width="130" height="18" rx="3" fill="var(--metal)"/><rect x="290" y="60" width="130" height="18" rx="3" fill="var(--metal)"/>
  <text x="105" y="52" text-anchor="middle">source (metal contact)</text><text x="355" y="52" text-anchor="middle">drain (metal contact)</text>
  <text x="230" y="214" text-anchor="middle" style="font-weight:600">${on ? 'channel: electrons gathered under the gate' : 'no channel: the gap is plain p-type silicon'}</text>
  ${on ? '<path d="M355 100 Q230 40 105 100" fill="none" stroke="#ffd23f" stroke-width="2.5" stroke-dasharray="6 5" marker-end="url(#ar)"/>' : ''}
  <defs><marker id="ar" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0 0L8 4L0 8z" fill="#ffd23f"/></marker></defs>`;
}
