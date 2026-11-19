import { simulate, latchStep } from './sim.js';
import * as schem from './schem.js';
import { buildSteps } from './steps.js';

const $ = id => document.getElementById(id);
// three.js comes from a CDN. If it cannot load, the viewers say so and everything else still works.
let THREE, PhotoViewer, PhotoViewer2D, StackViewer, LAYER_COLOUR, pointInRing;
const LAYER_NAME = { M: 'Metal', P: 'Poly', D: 'Diffusion', C: 'Metal contact', B: 'Buried contact', T: 'Transistor channel' };
class Stub {
  constructor(el, why) {
    const d = document.createElement('div'); d.className = 'pv-fail';
    d.textContent = why ? `This view could not start: ${why}. The text, diagrams and simulations on this page still work.`
      : 'The 3D / photo viewer needs the three.js library, which could not be loaded (offline, or the CDN is blocked). The text and diagrams on this page still work.';
    el.appendChild(d);
    return new Proxy(this, { get: (t, k) => (k in t ? t[k] : (k === 'items' ? [] : () => {})), set: () => true });
  }
}
try {
  THREE = await import('three');
  ({ PhotoViewer, PhotoViewer2D, LAYER_COLOUR, pointInRing } = await import('./photo.js'));
  ({ StackViewer } = await import('./stack.js'));
} catch (err) {
  console.warn('three.js unavailable:', err);
  PhotoViewer = StackViewer = Stub;
  LAYER_COLOUR = { M: 0x4aa3ff, P: 0xff5a4d, D: 0x2fd36b, C: 0xffd23f, B: 0xd96bff, T: 0xffffff };
  pointInRing = () => false;
}
// A viewer that cannot start (no WebGL, say) must not take the rest of the page down with it.
const guard = C => C === Stub ? C : function (el, o) {
  try { return new C(el, o); } catch (err) { console.warn('viewer failed:', err); return new Stub(el, String(err && err.message || err).split('\n')[0]); }
};
// No WebGL: the photo views fall back to a 2D canvas; the 3D stacks say they cannot start.
const guardPhoto = C => C === Stub ? C : function (el, o) {
  try { if (/[?&]canvas2d\b/.test(location.search)) throw new Error('2D canvas requested'); return new C(el, o); } catch (err) {
    console.warn('WebGL unavailable, using a 2D canvas:', err);
    el.querySelectorAll(':scope > .pv-canvas').forEach(n => n.remove());
    try { return new PhotoViewer2D(el, o); } catch (e2) { return new Stub(el, String(e2.message).split('\n')[0]); }
  }
};
PhotoViewer = guardPhoto(PhotoViewer); StackViewer = guard(StackViewer);
const REDUCED = matchMedia('(prefers-reduced-motion: reduce)').matches;
// toggle buttons announce their state
const syncPressed = () => document.querySelectorAll('button.tgl').forEach(b => b.setAttribute('aria-pressed', b.classList.contains('on')));
new MutationObserver(syncPressed).observe(document.body, { subtree: true, attributes: true, attributeFilter: ['class'] });
const ex = await (await fetch('data/example.json')).json();
const EX = [ex.origin[0], ex.origin[1], ex.size[0], ex.size[1]];
const MID = [13300, 13900, 2400, 2400];     // the neighbourhood the "block of logic" button flies to
// The whole die at 1/4 and 1/2 of the photo's size, in tiles that load when they come into view.
function lazyTiles(step, size, fade) {
  const out = [];
  for (let r = 0, y = 0; y < 21025; r++, y += size) for (let c = 0, x = 0; x < 19838; c++, x += size) {
    out.push({ x, y, w: Math.min(size, 19838 - x), h: Math.min(size, 21025 - y), lazy: true, fade,
      urls: { metal: D(`L${step}_metal_${c}_${r}.jpg`), acid1b: D(`L${step}_acid1b_${c}_${r}.jpg`) } });
  }
  return out;
}
const DIE = [0, 0, 19838, 21025];
const D = f => 'data/' + f;
const SHOTS = ['metal', 'metal1', 'acid', 'acid1b'];
const SHOT_LABEL = { metal: 'Metal (chip 2)', metal1: 'Metal (chip 1)', acid: 'Etched (chip 2)', acid1b: 'Etched, clean (chip 1)' };
const exUrls = Object.fromEntries(SHOTS.map(s => [s, D(`ex_${s}.jpg`)]));
const netName = id => (ex.nets[id] && ex.nets[id].names[0]) ? ex.nets[id].names[0].replace(/_L$/, '') : 'unnamed wire';
const ORDER = { D: 0, P: 1, M: 2, B: 3, C: 4, T: 5 };
const HI = 0xf0834a, LO = 0x4aa3ff;

// every traced polygon as an overlay item
function overlayPolys() {
  const out = [];
  for (const L of ['D', 'P', 'M']) for (const p of ex.layers[L]) out.push({ pts: p.pts, meta: { layer: L, net: p.net, order: ORDER[L] } });
  for (const c of ex.contacts) out.push({ pts: c.pts, meta: { layer: 'C', net: -1, order: ORDER.C } });
  for (const b of ex.buried) out.push({ pts: b, meta: { layer: 'B', net: -1, order: ORDER.B } });
  for (const t of ex.channels) out.push({ pts: t.pts, meta: { layer: 'T', net: -1, tid: t.id, kind: t.kind, order: ORDER.T } });
  return out;
}
function tipAt(v, e, tip, html) {
  if (!html) { tip.style.display = 'none'; return; }
  const r = v.el.getBoundingClientRect();
  tip.innerHTML = html; tip.style.display = 'block';
  tip.style.left = Math.min(r.width - 170, e.clientX - r.left + 14) + 'px';
  tip.style.top = Math.max(4, e.clientY - r.top - 34) + 'px';
}
function segButtons(el, items, onPick, first = 0) {
  el.innerHTML = '';
  items.forEach(([v, label], i) => {
    const b = document.createElement('button'); b.textContent = label; b.dataset.v = v;
    b.onclick = () => { [...el.children].forEach(c => c.classList.toggle('on', c === b)); onPick(v); };
    if (i === first) b.className = 'on';
    el.appendChild(b);
  });
}
const NETCOL = { n0: 0x9aa0a6, vss: 0x3fa9f5, vcc: 0xff9f1c, in_c_L: 0xc77dff, in_a_L: 0xff595e, a_out_L: 0x2ec4b6, b_out_L: 0xffd23f };
const netColour = id => NETCOL[ex.nets[id].names[0] || 'n0'] ?? 0xaaaaaa;

/* theme ----------------------------------------------------------------------------------------*/
$('theme').onclick = () => {
  const r = document.documentElement, cur = r.dataset.theme || (matchMedia('(prefers-color-scheme:dark)').matches ? 'dark' : 'light');
  r.dataset.theme = cur === 'dark' ? 'light' : 'dark';
};
const links = [...document.querySelectorAll('nav.top a')];
document.querySelectorAll('section[id]').forEach(sec => {
  new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) links.forEach(a => a.classList.toggle('on', a.hash === '#' + sec.id)); }),
    { rootMargin: '-45% 0px -50% 0px' }).observe(sec);
});

/* 1. the journey -------------------------------------------------------------------------------*/
{
  const v = new PhotoViewer($('journey'), {
    bounds: DIE, minHalf: 50,
    tiles: [
      { x: 0, y: 0, w: 19838, h: 21025, urls: { metal: D('die_metal.jpg'), acid1b: D('die_acid1b.jpg') } },
      ...lazyTiles(4, 8192, [0.07, 0.14]),
      ...lazyTiles(2, 4096, [0.18, 0.3]),
      { x: EX[0], y: EX[1], w: EX[2], h: EX[3], urls: { metal: D('ex_metal.jpg'), acid1b: D('ex_acid1b.jpg') }, fade: [0.42, 0.8] },
    ],
  });
  v.setShots('metal'); v.reset();
  v.setNotes([{ x: EX[0], y: EX[1], html: 'the worked example is here' }, { x: 7200, y: 1180, html: 'a bond pad: a pin connects here' }, { x: 9300, y: 6400, html: 'a repeated array: the same cell many times' }]);
  v.onView = () => { const z = v.pxPerDie; $('j-info').textContent = `magnification ${z >= 1 ? z.toFixed(1) : z.toFixed(2)}x the photo's own pixels`; };
  segButtons($('j-shots'), [['metal', 'Metal intact'], ['acid1b', 'Metal etched away']], s => v.setShots(s));
  $('j-die').onclick = () => v.flyTo(...DIE, 900);
  $('j-mid').onclick = () => v.flyTo(...MID, 1200);
  $('j-ex').onclick = () => v.flyTo(EX[0] - 20, EX[1] - 20, EX[2] + 40, EX[3] + 40, 1600);
}

/* 2. cross-section and the stack ---------------------------------------------------------------*/
{
  let on = false;
  const draw = () => {
    schem.crossSection($('xsec'), on);
    $('xs-btn').textContent = on ? 'Gate: high' : 'Gate: low'; $('xs-btn').classList.toggle('on', on);
    $('xs-cap').textContent = on ? 'Current can flow from the drain to the source: the switch is closed.' : 'Nothing joins the two islands: the switch is open.';
  };
  $('xs-btn').onclick = () => { on = !on; draw(); }; draw();

  const s = new StackViewer($('stack1'), ex, { photo: D('ex_acid1b.jpg') });
  const stages = [
    ['Substrate', { D: 0, P: 0, M: 0, C: 0, B: 0 }, 'The ground plane is the photograph itself. Everything built on it has been traced from it.'],
    ['+ Diffusion', { D: 1, P: 0, M: 0, C: 0, B: 0 }, 'Diffusion: n-type silicon, drawn as green slabs. These are wires, and the two ends of every transistor.'],
    ['+ Poly', { D: 1, P: 1, M: 0, C: 0, B: 1 }, 'Poly: wires and gates. White marks where poly crosses diffusion: five channels, the five transistors. Magenta: buried contacts, where poly dives straight into diffusion.'],
    ['+ Contacts', { D: 1, P: 1, M: 0, C: 1, B: 1 }, 'Contact cuts: yellow posts standing on the diffusion or poly they will connect to.'],
    ['+ Metal', { D: 1, P: 1, M: 1, C: 1, B: 1 }, 'Metal: the top layer, the wires you can see in an ordinary photo. The posts join it to what lies below, and only where a post stands.'],
    ['Etch the metal off', { D: 1, P: 1, M: 0, C: 0, B: 1 }, 'Remove the metal and what is left is what the etched photographs show: poly and diffusion, and the buried contacts.'],
  ];
  const apply = i => {
    s.setVisible(Object.fromEntries(Object.entries(stages[i][1]).map(([k, v]) => [k, !!v])));
    $('s1-caption').textContent = stages[i][2];
  };
  segButtons($('s1-build'), stages.map((st, i) => [i, st[0]]), v => apply(+v), 4);
  apply(4);
  $('s1-explode').oninput = e => s.setExplode(e.target.value / 100);
  segButtons($('s1-photo'), [['on', 'Photo under it'], ['off', 'No photo']], v => s.setVisible({ ground: v === 'on' }));
  s.onHover = (u, e, tip) => tipAt(s, e, tip, u && u.layer !== 'ground' ? (u.layer === 'T' ? `Transistor channel t${u.tid}` : `${LAYER_NAME[u.layer]}${u.net >= 0 ? ' · ' + netName(u.net) : ''}`) : null);
  s.onPick = u => {
    if (u && u.net >= 0) s.select({ nets: new Set([u.net]) });
    else if (u && u.tid != null) s.select({ tid: u.tid, nets: new Set([u.gate]) });
    else s.select(null);
  };
}

/* 3. schematics --------------------------------------------------------------------------------*/
{
  const inv = { a: 0 }, nr = { a: 0, b: 0 };
  const invS = $('sch-inv'), norS = $('sch-nor');
  schem.inverter(invS); schem.nor(norS);
  const draw = () => {
    const out = inv.a ? 0 : 1;
    schem.colour(invS, n => ({ vcc: 1, vss: 0, 'inv:out': out, 'inv:in': inv.a })[n] ?? (n.startsWith('ch:') || n.startsWith('ch2:') ? undefined : undefined), t => t === 'invL' || (t === 'invP' && inv.a));
    // lead wires of the transistors follow the nets they hang on
    const lv = { 'ch:invL': 1, 'ch2:invL': out, 'ch:invP': out, 'ch2:invP': 0 };
    for (const el of invS.querySelectorAll('.w')) if (lv[el.dataset.net] !== undefined) { el.classList.toggle('hi', lv[el.dataset.net] === 1); el.classList.toggle('lo', lv[el.dataset.net] === 0); }
    $('inv-out').textContent = out; $('inv-out').classList.toggle('h', !!out);
    const o2 = nr.a || nr.b ? 0 : 1;
    schem.colour(norS, n => ({ vcc: 1, vss: 0, 'nor:out': o2, 'nor:a': nr.a, 'nor:b': nr.b })[n], t => t === 'norL' || (t === 'norA' && nr.a) || (t === 'norB' && nr.b));
    const lv2 = { 'ch:norL': 1, 'ch2:norL': o2, 'ch:norA': o2, 'ch2:norA': 0, 'ch:norB': o2, 'ch2:norB': 0 };
    for (const el of norS.querySelectorAll('.w')) if (lv2[el.dataset.net] !== undefined) { el.classList.toggle('hi', lv2[el.dataset.net] === 1); el.classList.toggle('lo', lv2[el.dataset.net] === 0); }
    $('nor-out').textContent = o2; $('nor-out').classList.toggle('h', !!o2);
    for (const b of document.querySelectorAll('[data-in]')) {
      const [g, k] = b.dataset.in.split('-'), val = (g === 'inv' ? inv : nr)[k];
      b.textContent = `${g === 'inv' ? 'in' : k.toUpperCase()} = ${val}`; b.classList.toggle('on', !!val);
    }
  };
  for (const b of document.querySelectorAll('[data-in]')) b.onclick = () => { const [g, k] = b.dataset.in.split('-'); const o = g === 'inv' ? inv : nr; o[k] ^= 1; draw(); };
  draw();
}

/* 4. reading the layers, with a quiz --------------------------------------------------------*/
{
  const v = new PhotoViewer($('read'), { bounds: [EX[0], EX[1], EX[2], EX[3] + 90], origin: ex.origin, minHalf: 20, tiles: [{ x: EX[0], y: EX[1], w: EX[2], h: EX[3], urls: exUrls }] });
  v.setShots('metal'); v.reset();
  let a = 'metal', b = 'acid1b', reveal = null;
  v.setOverlay(overlayPolys());
  v.overlayStyle = m => (reveal && reveal.has(m) ? { color: 0xffffff, opacity: 0.35, outline: 1 } : { color: 0, opacity: 0, outline: 0 });
  const upd = () => { v.setShots(a, b, $('r-mix').value / 100); };
  segButtons($('r-a'), SHOTS.map(s => [s, SHOT_LABEL[s]]), s => { a = s; upd(); });
  segButtons($('r-b'), SHOTS.map(s => [s, SHOT_LABEL[s]]), s => { b = s; upd(); }, 3);
  $('r-b').style.cssText = 'border:0;background:none';
  $('r-mix').oninput = upd; $('r-reset').onclick = () => v.reset();
  upd();

  const Q = [
    { q: 'Find a <b>metal contact</b>: a place where metal connects down to the silicon.', ok: m => m.layer === 'C', hint: 'Look in the metal shot for a ring or oval in the metal.', good: 'Yes: a contact cut. In the metal shot it is the ring; in the etched shot, the dark-specked box.' },
    { q: 'Find a <b>buried contact</b>: poly joined straight to diffusion.', ok: m => m.layer === 'B', hint: 'Use an etched shot: a small box with a heavy outline where a poly wire ends on diffusion.', good: 'Yes: a heavy-outlined box at the end of a poly wire.' },
    { q: 'Find a <b>transistor channel</b>: where poly crosses diffusion.', ok: m => m.layer === 'T', hint: 'Use the etched shot, and look for a poly stripe lying across a diffusion band.', good: 'Yes: a crossing of poly over diffusion is a transistor.' },
    { q: 'Find a <b>load transistor</b>: the fat poly block with a long channel, tied to its own output.', ok: m => m.layer === 'T' && m.kind === 'load', wrong: m => m.layer === 'T' ? 'That is a pull-down: a narrow poly wire across a wide band. A load is a fat block with a long channel.' : null, hint: 'There are two. In each row it is the block nearest the right-hand rail.', good: 'Yes. Its channel is longer than it is wide, so it is weak, and a buried contact ties it to its own output.' },
    { q: 'Find one of the two <b>wide power rails</b> (the wide vertical metal bars).', ok: m => m.layer === 'M' && (netName(m.net) === 'vss' || netName(m.net) === 'vcc'), hint: 'The two widest metal bars, about 50 pixels across.', good: 'Yes, a power rail: one carries VCC and the other VSS (which is which comes out in step 9 of the worked example).' },
  ];
  let qi = -1, score = 0, tries = 0, done = false; const answered_q = new Set();
  const nextQ = () => { qi = (qi + 1) % Q.length; reveal = null; v.restyle(); done = false; tries = 0; $('quiz-q').innerHTML = `Question ${qi + 1} of ${Q.length}: ` + Q[qi].q; $('quiz-res').textContent = ''; $('quiz-res').className = 'quiz-res'; v.setNotes([]); };
  let answered = 0;
  const check = (x, y) => {
    if (done) return;
    const q = Q[qi];
    const pts = [[0, 0], [8, 0], [-8, 0], [0, 8], [0, -8], [6, 6], [-6, -6], [6, -6], [-6, 6]];
    let hit = null, any = null;
    for (const [dx, dy] of pts) {
      const it = v.items.filter(i => pointInRing(x + dx, y + dy, i.abs)).sort((a, b) => (b.meta.order || 0) - (a.meta.order || 0));
      for (const i of it) { if (q.ok(i.meta)) { hit = i; break; } else if (!any && dx === 0 && dy === 0) any = i; }
      if (hit) break;
    }
    tries++;
    const res = $('quiz-res');
    if (hit) {
      done = true; if (tries === 1) score++;
      reveal = new Set([hit.meta]); v.restyle();
      res.className = 'quiz-res ok'; res.textContent = typeof q.good === 'function' ? q.good(hit.meta) : q.good;
    } else {
      res.className = 'quiz-res no';
      const m = any && q.wrong ? q.wrong(any.meta) : null;
      res.textContent = m || (any ? 'Not that one. Try another spot, or use the hint.' : 'Nothing traced there. Try another spot, or use the hint.');
    }
    if (hit && !answered_q.has(qi)) answered_q.add(qi);
    $('quiz-score').textContent = `Right first time: ${score} of ${answered_q.size} answered`;
  };
  v.onClick = (_, x, y) => check(x, y);
  $('quiz-hint').onclick = () => { if (done) return; $('quiz-res').className = 'quiz-res'; $('quiz-res').textContent = 'Hint: ' + Q[qi].hint; };
  $('quiz-next').onclick = nextQ;
  nextQ();
}

/* 5. the worked example ------------------------------------------------------------------------*/
const steps = buildSteps(ex);
const exViewer = new PhotoViewer($('ex'), { bounds: EX, origin: ex.origin, minHalf: 20, tiles: [{ x: EX[0], y: EX[1], w: EX[2], h: EX[3], urls: exUrls }] });
{
  const v = exViewer;
  v.setOverlay(overlayPolys());
  const state = { ov: {}, net: false, hl: null };
  v.overlayStyle = m => {
    const a = state.ov[m.layer]; if (!a || state.off) return null;
    let color = LAYER_COLOUR[m.layer], op = a;
    if (state.net && m.net >= 0) color = netColour(m.net);
    if (state.hl) {
      const hit = state.hl.has(m.net);
      if (!hit && m.net >= 0) op = a * 0.35;
      if (hit) op = Math.min(0.85, a * 2.2);
    }
    return { color, opacity: op, outline: Math.min(1, op + 0.5) };
  };
  v.onHover = (it, x, y, e, tip) => tipAt(v, e, tip, it ? (it.meta.layer === 'T' ? `Transistor t${it.meta.tid}${it.meta.kind === 'load' ? ' (load)' : ''}` : `${LAYER_NAME[it.meta.layer]}${it.meta.net >= 0 ? ' · net ' + netName(it.meta.net) : ''}`) : null);
  v.onClick = it => {
    if (it && it.meta.net >= 0) state.hl = new Set([it.meta.net]);
    else if (it && it.meta.tid != null) state.hl = new Set([ex.channels[it.meta.tid].gate]);
    else state.hl = null;
    v.restyle();
  };
  segButtons($('e-shots'), SHOTS.map(s => [s, SHOT_LABEL[s]]), s => v.setShots(s, s, 0), 0);
  $('e-reset').onclick = () => v.flyTo(...EX);
  v.setShots('metal'); v.reset();

  const LAYER_LEGEND = $('e-legend').innerHTML;
  $('e-ovl').onclick = () => { state.off = !state.off; $('e-ovl').textContent = state.off ? 'Show the tracing' : 'Hide the tracing'; v.restyle(); };
  const host = $('steps');
  let cur = -1, mixAnim = null;
  steps.forEach((s, i) => {
    const d = document.createElement('div'); d.className = 'step'; d.id = 'step' + i;
    d.innerHTML = `<h3><span class="n">${i + 1}</span>${s.title}</h3>${s.body}`;
    host.appendChild(d);
  });
  const enter = i => {
    if (i === cur) return;
    cur = i; const s = steps[i];
    if (state.off) { state.off = false; $('e-ovl').textContent = 'Hide the tracing'; }
    document.querySelectorAll('.step').forEach((el, k) => el.classList.toggle('on', k === i));
    state.ov = s.ov; state.net = !!s.net; state.hl = s.hl ? new Set(s.hl) : (s.hlName ? new Set([Object.entries(ex.nets).find(([, n]) => n.names.includes(s.hlName))[0] | 0]) : null);
    $('e-legend').style.display = Object.keys(s.ov).length ? '' : 'none';
    $('e-legend').innerHTML = s.net ? Object.entries(NETCOL).map(([n, c]) => `<span><i style="background:#${c.toString(16).padStart(6, '0')}"></i>${n === 'n0' ? 'passing metal (no net)' : n.replace(/_L$/, '')}</span>`).join('') : LAYER_LEGEND;
    const [a, b, m] = s.shots;
    if (s.anim && !REDUCED) { v.setShots(a, b, 0); let t0 = performance.now(); cancelAnimationFrame(mixAnim); const tick = now => { const t = Math.min(1, (now - t0) / 1800); v.setMix(t); if (t < 1) mixAnim = requestAnimationFrame(tick); }; mixAnim = requestAnimationFrame(tick); }
    else { cancelAnimationFrame(mixAnim); v.setShots(a, b, m); }
    [...$('e-shots').children].forEach(c => c.classList.toggle('on', c.dataset.v === b && !s.anim ? true : (s.anim ? c.dataset.v === 'acid1b' : false)));
    v.restyle(); v.setNotes(s.notes || []);
    v.flyTo(...s.fly, REDUCED ? 0 : 900);
    $('e-info').textContent = `Step ${i + 1} of ${steps.length}`;
  };
  // the active step is the one whose middle is nearest a line 40% down the window
  let raf = 0;
  const pick = () => {
    raf = 0;
    const els = [...document.querySelectorAll('.step')], line = innerHeight * 0.5;
    const r0 = els[0].getBoundingClientRect(), rN = els[els.length - 1].getBoundingClientRect();
    if (r0.top > innerHeight * 0.9 || rN.bottom < innerHeight * 0.1) return;      // section off screen
    let best = 0, bd = 1e9;
    els.forEach((el, i) => { const r = el.getBoundingClientRect(), d = Math.abs((r.top + r.bottom) / 2 - line); if (d < bd) { bd = d; best = i; } });
    enter(best);
  };
  addEventListener('scroll', () => { if (!raf) raf = requestAnimationFrame(pick); }, { passive: true });
  addEventListener('resize', pick);
  document.querySelectorAll('.step').forEach((el, i) => el.addEventListener('click', () => enter(i)));
  schem.example($('sch-step'));
  enter(0);
}

/* 6. running the traced netlist ----------------------------------------------------------------*/
{
  const inputs = { in_a_L: 0, in_c_L: 0 };
  const photo = new PhotoViewer($('sim-photo'), { bounds: EX, origin: ex.origin, minHalf: 20, tiles: [{ x: EX[0], y: EX[1], w: EX[2], h: EX[3], urls: exUrls }] });
  photo.setShots('acid1b'); photo.reset(); photo.setOverlay(overlayPolys());
  const stack = new StackViewer($('stack2'), ex, { photo: D('ex_acid1b.jpg') });
  stack.setExplode(0.6);
  const sch = $('sch-ex'); schem.example(sch);
  let sim = null, picked = null;
  const info = document.createElement('p'); info.className = 'hint'; info.id = 'sim-info'; info.setAttribute('aria-live', 'polite'); $('stack2').parentElement.after(info);
  const lvl = id => sim.val[id];
  photo.overlayStyle = m => {
    if (m.layer === 'C') return { color: LAYER_COLOUR.C, opacity: 0.5, outline: 1 };
    if (m.layer === 'B') return { color: LAYER_COLOUR.B, opacity: 0.5, outline: 1 };
    if (m.layer === 'T') return { color: sim.on.has(m.tid) ? 0xffffff : 0x222222, opacity: sim.on.has(m.tid) ? 0.8 : 0.55, outline: 1, outlineColor: picked === m.tid ? 0xffff00 : 0xffffff };
    const v = lvl(m.net);
    return { color: v === 1 ? HI : LO, opacity: m.layer === 'M' ? 0.36 : 0.45, outline: 0.8 };
  };
  photo.onHover = (it, x, y, e, tip) => tipAt(photo, e, tip, it ? (it.meta.layer === 'T' ? `t${it.meta.tid}: ${sim.on.has(it.meta.tid) ? 'conducting' : 'off'}` : it.meta.net >= 0 ? `${LAYER_NAME[it.meta.layer]} · ${netName(it.meta.net)} = ${lvl(it.meta.net)}` : null) : null);
  const describe = tid => {
    const t = ex.channels[tid], n = id => netName(id);
    return `t${tid}${t.kind === 'load' ? ' (load: always conducting)' : ''}: gate ${n(t.gate)} = ${lvl(t.gate)}, channel between ${n(t.a)} and ${n(t.b)}, W/L ${t.w}/${t.l}. It is ${sim.on.has(tid) ? 'conducting' : 'off'}.`;
  };
  photo.onClick = it => { picked = it && it.meta.tid != null ? it.meta.tid : null; info.textContent = picked != null ? describe(picked) : ''; photo.restyle(); stack.select(picked != null ? { tid: picked } : null); };
  stack.onPick = u => { picked = u && u.tid != null ? u.tid : null; info.textContent = picked != null ? describe(picked) : ''; photo.restyle(); stack.select(picked != null ? { tid: picked } : null); };
  stack.onHover = (u, e, tip) => tipAt(stack, e, tip, u && u.layer !== 'ground' ? (u.layer === 'T' ? `t${u.tid}: ${sim.on.has(u.tid) ? 'conducting' : 'off'}` : u.net >= 0 ? `${LAYER_NAME[u.layer]} · ${netName(u.net)} = ${lvl(u.net)}` : LAYER_NAME[u.layer]) : null);
  const tt = $('tt');
  const nm = s => s.replace(/_L\b/g, '');
  const render = () => {
    sim = simulate(ex, inputs);
    photo.restyle();
    stack.paint(u => u.layer === 'T' ? new THREE.Color(sim.on.has(u.tid) ? 0xffffff : 0x3a3a38) : u.net >= 0 ? new THREE.Color(lvl(u.net) === 1 ? HI : LO) : null);
    const a = sim.val[sim.byName.a_out_L], b = sim.val[sim.byName.b_out_L];
    $('v-a').textContent = a; $('v-a').classList.toggle('h', !!a); $('v-b').textContent = b; $('v-b').classList.toggle('h', !!b);
    schem.colour(sch, n => { const id = sim.byName[n]; return id !== undefined ? sim.val[id] : undefined; }, t => sim.on.has(+t));
    const chv = { '0': [sim.byName.vcc, sim.byName.a_out_L], '1': [sim.byName.a_out_L, sim.byName.vss], '3': [sim.byName.vcc, sim.byName.b_out_L], '4': [sim.byName.b_out_L, sim.byName.vss], '2': [sim.byName.b_out_L, sim.byName.vss] };
    for (const el of sch.querySelectorAll('.w')) { const m = /^ch(2?):(\d)$/.exec(el.dataset.net || ''); if (m) { const v = sim.val[chv[m[2]][m[1] ? 1 : 0]]; el.classList.toggle('hi', v === 1); el.classList.toggle('lo', v === 0); } }
    for (const bt of document.querySelectorAll('[data-sim]')) { const k = bt.dataset.sim; bt.textContent = `${nm(k)} = ${inputs[k]}`; bt.classList.toggle('on', !!inputs[k]); }
    // table
    const rows = [];
    for (const A of [0, 1]) for (const C of [0, 1]) { const s = simulate(ex, { in_a_L: A, in_c_L: C }); rows.push([A, C, s.val[s.byName.a_out_L], s.val[s.byName.b_out_L]]); }
    tt.innerHTML = `<tr><th>in_a</th><th>in_c</th><th>a_out</th><th>b_out</th></tr>` + rows.map(r => `<tr class="${r[0] === inputs.in_a_L && r[1] === inputs.in_c_L ? 'cur' : ''}">${r.map(x => `<td>${x}</td>`).join('')}</tr>`).join('') +
      `<tr><td colspan="4" style="font-size:13px;color:var(--ink2)">Equations the tool recovered from the transistor list: ${ex.logic.map(g => `<code>${nm(ex.nets[g.out].name)} = ${nm(g.expr)}</code>`).join(', ')}</td></tr>`;
    if (picked != null) info.textContent = describe(picked);
  };
  for (const bt of document.querySelectorAll('[data-sim]')) bt.onclick = () => { inputs[bt.dataset.sim] ^= 1; render(); };
  $('s2-explode').oninput = e => stack.setExplode(e.target.value / 100);
  render();
}

/* 8. the latch ---------------------------------------------------------------------------------*/
{
  const svg = $('sch-latch'); schem.latch(svg);
  let d = 0, le = 0, st = { q: 0, qn: 1 }, known = false;
  const hist = [];
  const draw = () => {
    const r = latchStep(st, d, le); if (le) known = true; st = { q: r.q, qn: r.qn };
    const lv = { d, d_n: d ? 0 : 1, le, q: st.q, qn: st.qn, out: r.out };
    schem.colour(svg, n => (known || n === 'd' || n === 'd_n' || n === 'le') ? lv[n] : undefined);
    $('l-d').textContent = `d = ${d}`; $('l-d').classList.toggle('on', !!d);
    $('l-le').textContent = `le = ${le}`; $('l-le').classList.toggle('on', !!le);
    for (const [id, val] of [['l-q', st.q], ['l-qn', st.qn], ['l-out', r.out]]) { $(id).textContent = known ? val : '?'; $(id).classList.toggle('h', known && !!val); $(id).classList.toggle('u', !known); }
    hist.push({ d, le, out: known ? r.out : null }); if (hist.length > 14) hist.shift();
    const W = 420, H = 220, step = (W - 60) / 13;
    const track = (y, key, name, col) => {
      let p = '', prev = null;
      hist.forEach((h, i) => { const x = 50 + i * step, v = h[key]; if (v === null) return; const yy = y + (v ? 0 : 34); p += prev === null ? `M${x} ${yy}` : `H${x}V${yy}`; prev = v; });
      p += prev === null ? '' : `H${50 + (hist.length) * step}`;
      return `<text x="6" y="${y + 22}" style="font:600 12px system-ui;fill:var(--ink)">${name}</text><path class="s" d="${p}" stroke="${col}"/><line class="g" x1="46" x2="${W - 8}" y1="${y + 40}" y2="${y + 40}"/>`;
    };
    $('timing').innerHTML = track(14, 'd', 'd', 'var(--metal)') + track(84, 'le', 'le', 'var(--accent)') + track(154, 'out', 'out', 'var(--diff)');
  };
  $('l-d').onclick = () => { d ^= 1; draw(); };
  $('l-le').onclick = () => { le ^= 1; draw(); };
  draw();
}
