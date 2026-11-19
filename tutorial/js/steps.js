// The worked example, one entry per step. Coordinates are die-photo pixels.
// `ov` says which overlay layers are drawn (alpha), `net` colours by net, `hl` lights some nets.
const ALL = [14260, 14860, 390, 440];
const ROW_A = [14270, 14872, 370, 170];
const ROW_B = [14270, 15030, 370, 240];

export function buildSteps(ex) {
  const [ox, oy] = ex.origin;
  const tnote = (t, extra = '') => ({ x: t.at[0] + ox, y: t.at[1] + oy, html: `t${t.id}${t.kind === 'load' ? ' load' : ''} · W/L ${t.w}/${t.l}${extra}` });
  const T = Object.fromEntries(ex.channels.map(t => [t.id, t]));
  return [
    {
      title: 'Look first', shots: ['metal', 'metal', 0], fly: ALL, ov: {},
      body: `<p>This is the <b>metal shot</b> at the spot. Two things stand out: wide vertical bars of bright, speckled yellow (<b>metal</b> wires, the two widest about 50 pixels across; a wide wire like this that runs alongside a row of gates is a <b>rail</b>), and between them rows of shapes that repeat: the same pattern in each row, with small changes. Where the metal is absent you can make out outlines of what lies beneath (poly in orange-brown, diffusion as plain areas); under the metal, nothing shows.</p>
        <p>We do not know yet which rail is the supply and which is ground, or what the rows compute. The circuit has to be worked out from the shapes alone.</p>`,
      notes: [{ x: 14434, y: 14900, html: 'wide metal rail' }, { x: 14609, y: 14930, html: 'wide metal rail' }],
    },
    {
      title: 'Trace the metal', shots: ['metal', 'metal', 0], fly: ALL, ov: { M: 0.32 },
      body: `<p>Metal is the easiest layer: bright, grainy, with a dark edge line. We draw each wire as a shape (here, four of them): two wide rails at about 50 pixels, and two thin signal wires 16 to 20 pixels wide.</p>
        <div class="how">In the trace file a wire is one line: <code>M 14347,14825 y15240 w=16</code>. <code>M</code> is the layer (metal); <code>14347,14825</code> is the starting point, x then y in die pixels; <code>y15240</code> means run straight down to y = 15240; <code>w=16</code> is the width in pixels.</div>
        <p>Watch for a trap: dark lines <i>across</i> a metal wire are the edges of poly or diffusion running underneath. They are not breaks in the wire.</p>`,
      notes: [{ x: 14347, y: 14925, html: 'thin wire: only passes over (see step 11)' }],
    },
    {
      title: 'Etch the metal away', shots: ['metal', 'acid1b', 1], fly: ALL, ov: { M: 0.18 }, anim: true,
      body: `<p>Now the clean etched shot. The metal is gone, so we see what was hidden. Where metal used to cover things: <b>flat tan areas with dark outlines are diffusion</b> and <b>salmon strips with a sharp outline are poly</b>. In the open, away from where metal was, the colours change: poly is dark red-brown and diffusion can be bright green. The pink and khaki background is the thick oxide over bare silicon (the <i>field</i>); tan diffusion and khaki field are easy to confuse, so check where the metal was before deciding.</p>
        <p>The faint blue outline is where metal used to be. Use the buttons above the picture to flip between shots; each shows what the other hides.</p>
        <div class="how">The exact colours drift across the die, so we calibrate locally against something unmistakable. Metal also protects a margin of about 10 pixels beyond its own edge, so a gap between two wires shows a dark bar that is not a feature.</div>`,
      notes: [],
    },
    {
      title: 'Outline the diffusion', shots: ['acid1b', 'acid1b', 0], fly: ALL, ov: { D: 0.34 },
      body: `<p>We draw every diffusion region as a polygon: seven pieces here. Read them as wires made of silicon. Each row has a long horizontal band (the row's <b>output</b>) that runs east to the right-hand rail, plus a short vertical strip under the left rail that runs to the ground side.</p>
        <p>Diffusion carries current. But two diffusions are not joined just because they are close; <i>connections</i> need contacts, which come later.</p>`,
      notes: [{ x: 14420, y: 15000, html: 'row output band' }, { x: 14434, y: 15215, html: 'strip under the left rail' }],
    },
    {
      title: 'Outline the poly', shots: ['acid1b', 'acid1b', 0], fly: ALL, ov: { D: 0.18, P: 0.4 },
      body: `<p>Next the poly. It enters from the edges of the patch: <code>in_a</code> from the north into row A, and another wire runs up the left side (row B's output leaving the patch). Poly runs <b>over</b> diffusion at several places, and in each row it also forms a long wide block (a load's gate).</p>
        <p>Notice a poly wire that leaves the row A output and runs down to row B, where it crosses the diffusion. That is how one gate drives the next with no metal at all.</p>`,
      notes: [{ x: 14328, y: 14905, html: 'in_a enters here' }, { x: 14290, y: 15000, html: 'row B output leaves up the left' }],
    },
    {
      title: 'Find the transistors', shots: ['acid1b', 'acid1b', 0], fly: ALL, ov: { D: 0.18, P: 0.28, T: 0.9 },
      body: `<p><b>Wherever poly crosses diffusion, that is a transistor.</b> The software finds the overlap of the two layers and measures it: here five channels, with their width W and length L in pixels.</p>
        <p>Two are very different from the rest: <b>t0</b> and <b>t3</b> have <i>L larger than W</i> (a long, narrow channel, weak). Those are the <b>loads</b>. The others (t1, t2, t4) are wide and short: strong pull-downs.</p>`,
      notes: ex.channels.map(t => tnote(t)),
    },
    {
      title: 'Find the contacts', shots: ['metal', 'metal', 0], fly: ALL, ov: { M: 0.14, C: 0.9 },
      body: `<p>Metal reaches the layers below only through <b>contact cuts</b>: holes through the oxide, drawn here as small gold squares. In the metal shot each is a ring or oval in the metal; in the etched shot, a dark-specked box.</p>
        <p>There are six. Three tie the left rail to the rows' pull-down strips (it will turn out to be ground), two tie the right rail to the far end of each row's band, beyond its load, and one ties a metal wire to a poly wire (<code>in_c</code>).</p>
        <div class="how">A contact must have metal over it <i>and</i> something under it; the extraction tool reports a contact that lacks either. Every contact that decides a connection is checked in two photographs, because a contact read where there is none, or missed where there is one, changes the circuit.</div>`,
      notes: [{ x: 14423, y: 14920, html: 'rail to diffusion' }, { x: 14606, y: 14972, html: 'rail to diffusion' }, { x: 14305, y: 15176, html: 'metal to poly' }],
    },
    {
      title: 'Find the buried contacts', shots: ['acid1b', 'acid1b', 0], fly: ALL, ov: { D: 0.15, P: 0.2, T: 0.35, B: 0.95 },
      body: `<p>A <b>buried contact</b> joins poly straight to diffusion, with no metal. It shows as a small box with a heavy dark outline where a poly wire ends on diffusion. There are four.</p>
        <p>Two are the telltale of a <b>load</b>: the load's poly block is tied to its own output by one buried contact (the purple boxes beside the wide blocks). The other two carry a row's output off the diffusion and into poly, to be the next gate's input or to leave the patch.</p>
        <div class="try"><b>Check:</b> use the shot buttons. These boxes show in the etched shots; two of them lie partly under the thin metal at x 14347, which goes dark over them in the metal shot (a trap: that darkness is not a contact).</div>`,
      notes: [{ x: 14535, y: 14941, html: 'load tied to its output' }, { x: 14514, y: 15183, html: 'load tied to its output' }, { x: 14362, y: 14998, html: 'output into poly' }, { x: 14362, y: 15127, html: 'output into poly' }],
    },
    {
      title: 'Join the shapes into nets', shots: ['acid1b', 'acid1b', 0], fly: ALL, ov: { M: 0.5, D: 0.5, P: 0.5, B: 0.8, C: 0.9 }, net: true, hlName: 'a_out_L',
      body: `<p>Now the software merges: shapes that touch through a contact (metal to poly or diffusion) or a buried contact (poly to diffusion) belong to one <b>net</b>, an electrically single wire. Each colour is one net (the legend under the picture says which). Poly that merely crosses diffusion is <i>not</i> merged; that is a transistor.</p>
        <p>Two nets can be named from what we found: the rail whose contacts reach the <b>loads</b> is <b>VCC</b>; the rail on the pull-downs is <b>VSS</b>. The others are named for where they are: <code>in_a</code>, <code>in_c</code>, and the two row outputs <code>a_out</code> and <code>b_out</code>.</p>
        <p>The net <code>a_out</code> is already lit. Click any other shape to light its whole net. Notice that <code>a_out</code> includes row A's diffusion band, the poly that runs down the left, and the gate of a transistor in row B.</p>`,
      notes: [],
    },
    {
      title: 'Recover the logic', shots: ['acid1b', 'acid1b', 0], fly: ALL, ov: { D: 0.3, P: 0.35, T: 0.9 }, net: true,
      body: `<p>With transistors and nets in hand, the logic follows. For each output, find the load (the transistor between VCC and the node, whose gate is that node) and the pull-down paths to VSS:</p>
        <ul><li><b>Row A:</b> one pull-down (t1) with gate <code>in_a</code>. So <code>a_out = NOT in_a</code>.</li>
        <li><b>Row B:</b> two pull-downs in parallel, t4 with gate <code>a_out</code> and t2 with gate <code>in_c</code>. Either pulls the output low, so <code>b_out = NOR(a_out, in_c)</code>.</li></ul>
        <p>Chained: <code>b_out = in_a AND NOT in_c</code>. Below, the same circuit as a schematic; section 6 runs it.</p>
        <div class="card"><svg class="sch" id="sch-step" viewBox="0 0 440 300"></svg></div>`,
      notes: ex.channels.map(t => ({ x: t.at[0] + ox, y: t.at[1] + oy, html: `t${t.id} ${t.kind === 'load' ? 'load' : 'pull-down'} · gate ${(ex.nets[t.gate].names[0] || '').replace(/_L$/, '')}` })),
    },
    {
      title: 'A wire that is not a connection', shots: ['metal', 'metal', 0], fly: [14275, 14880, 170, 380], ov: { M: 0.14, P: 0.35 }, hl: [0],
      body: `<p>Last, the trap that costs the most. The thin metal at the left (highlighted) runs down across the poly wires of <b>four different nets</b>: <code>in_a</code> (y 14957), <code>a_out</code> (y 15000 and again at 15087), <code>b_out</code> (y 15131) and <code>in_c</code> (y 15172). It touches none of them: there is <i>no contact</i> where they cross, only the oxide between them.</p>
        <p>The extraction agrees: within this patch that metal is a net by itself, with no gates and no transistors on it (it carries on beyond the patch). A trace that joined it to any of those polys would invent a connection that is not there, which is exactly the error the independent reviewer is told to hunt for. "Metal lies over poly" is never evidence of a join by itself. A contact is.</p>
        <div class="how">To be sure, look at the crossing at four or more times magnification in two photographs, and measure the colours across it.</div>`,
      notes: [{ x: 14347, y: 14957, html: 'crosses in_a: no contact' }, { x: 14347, y: 15000, html: 'crosses a_out: no contact' }, { x: 14347, y: 15087, html: 'a_out again: no contact' }, { x: 14347, y: 15131, html: 'crosses b_out: no contact' }, { x: 14347, y: 15172, html: 'crosses in_c: no contact' }],
    },
  ];
}
