// playthrough bot for Part 3.1: run in the game page. window.__bot keeps results across calls.
(async function (RUNS, START, INV) {
  const S = SugarCube, wait = ms => new Promise(q => setTimeout(q, ms));
  S.Config.passages.transitionOut = 0;
  const B = window.__bot = window.__bot || { runs: [], visited: {}, endings: {}, issues: [], linkSeen: {}, deadly: {} };
  const issue = (kind, msg) => { const k = kind + ': ' + msg; if (!B.issues.some(i => i.k === k)) B.issues.push({ k, n: 1 }); else B.issues.find(i => i.k === k).n++; };
  const passageEl = () => document.querySelector('#passages');
  const settle = async () => { for (let i = 0; i < 60; i++) { const el = document.querySelector('#passages .passage'); if (el && el.getAttribute('data-passage') === S.State.passage) return; await wait(10); } };
  const options = () => {
    const out = [];
    passageEl().querySelectorAll('a').forEach(a => { if (a.offsetParent !== null || a.closest('.choices,.find')) out.push({ el: a, label: (a.textContent || '').trim(), to: a.getAttribute('data-passage') }); });
    return out;
  };
  for (let run = 0; run < RUNS; run++) {
    S.setup.reset(); if (START) { (INV || []).forEach(i => S.setup.addItem(i)); if (START === 'Hotel Arrival' || START === 'Level 2 Pipe Dreams') S.State.variables.virusWith = Math.random() < .5; } S.Engine.play(START || 'Start'); await settle();
    const path = [], R = { path, ending: null, steps: 0, minSanity: 100, drank: 0, codesWrong: 0 };
    let sameClicks = 0, last = '';
    for (let step = 0; step < 400; step++) {
      const p = S.State.passage, P = S.Story.get(p), v = S.State.variables;
      if (p !== last) { path.push(p); sameClicks = 0; last = p; }
      B.visited[p] = (B.visited[p] || 0) + 1;
      R.minSanity = Math.min(R.minSanity, v.sanity);
      // like a real player: drink from the inventory when sanity gets low
      if (v.sanity < 35 && S.setup.has('almond')) { S.setup.drink(); R.drank++; }
      const root = passageEl(), txt = root.innerText;
      if (root.querySelector('.error-view')) issue('ERROR', p + ' :: ' + root.querySelector('.error-view').innerText.slice(0, 160));
      if (/undefined|NaN|\[object/.test(txt)) issue('BAD TEXT', p);
      root.querySelectorAll('img').forEach(im => { if (im.complete && im.naturalWidth === 0) issue('BROKEN IMG', p + ' ' + (im.src || '').slice(0, 40)); });
      if (typeof v.sanity !== 'number' || v.sanity > 100 + S.setup.DRAIN || v.sanity < 0) issue('SANITY RANGE', p + ' ' + v.sanity);
      if ((v.inv || []).length > S.setup.SLOTS) issue('INV OVERFLOW', p);
      if (P.tags.includes('ending')) { R.ending = p; break; }
      // code pads: usually right, sometimes wrong
      const pad = root.querySelector('.codepad');
      if (pad) {
        const right = Math.random() < .75; pad.querySelector('.cin').value = right ? pad.getAttribute('data-answer') : '999';
        if (!right) R.codesWrong++;
        pad.querySelector('.go').click(); await wait(right ? 700 : 60); await settle();
        if (S.State.passage === p) { sameClicks++; if (sameClicks > 6) { issue('STUCK PAD', p); break; } }
        continue;
      }
      let opts = options();
      // timed scenes: sometimes let the clock run out
      const tb = root.querySelector('.timerbar span');
      if (tb && Math.random() < .15) {
        await wait(parseFloat(tb.style.animationDuration) * 1000 + 150);
        opts = options();
      }
      opts = opts.filter(o => o.el.isConnected);
      if (!opts.length) { if (!pad) issue('DEAD END', p); break; }
      opts.forEach(o => { B.linkSeen[p + ' -> ' + o.label] = (B.linkSeen[p + ' -> ' + o.label] || 0) + 1; });
      if (opts.some(o => !o.label && !o.el.classList.contains('hotspot'))) issue('EMPTY LABEL', p);
      // learn: mostly skip choices that killed us before
      const sig = () => [...new Set(S.State.variables.inv || [])].sort().join(',') + (S.State.variables.virusWith ? '+v' : '') + (S.State.variables.power ? '+p' : '');
      const safe = opts.filter(o => !B.deadly[p + ' -> ' + o.label + ' @' + sig()]);
      if (safe.length && Math.random() < .92) opts = safe;
      // prefer links to places not seen much yet
      const fresh = opts.filter(o => o.to && !B.visited[o.to]);
      const rare = opts.slice().sort((a, b) => (B.linkSeen[p + ' -> ' + a.label] > B.linkSeen[p + ' -> ' + b.label] ? 1 : -1));
      let pick = fresh.length && Math.random() < .7 ? fresh[Math.floor(Math.random() * fresh.length)]
        : Math.random() < .5 ? rare[0] : opts[Math.floor(Math.random() * opts.length)];
      B.linkSeen[p + ' :: picked ' + pick.label] = (B.linkSeen[p + ' :: picked ' + pick.label] || 0) + 1;
      if (/drink/i.test(pick.label)) R.drank++;
      const key = p + ' -> ' + pick.label + ' @' + sig();
      pick.el.click(); await wait(5); await settle();
      if (S.Story.get(S.State.passage).tags.includes('ending') && S.State.passage !== 'Lost Your Mind') B.deadly[key] = S.State.passage;
      if (S.State.passage === p) { sameClicks++; if (sameClicks > 8) { issue('NO PROGRESS', p + ' (last click: ' + pick.label + ')'); break; } }
      R.steps++;
    }
    if (!R.ending) issue('NO ENDING', 'run ' + B.runs.length + ' stopped at ' + S.State.passage + ' after ' + R.steps + ' steps');
    B.endings[R.ending] = (B.endings[R.ending] || 0) + 1;
    R.inv = (S.State.variables.inv || []).slice(); R.start = START || 'Start';
    B.runs.push(R);
  }
  return { runs: B.runs.length, issues: B.issues.length };
})
