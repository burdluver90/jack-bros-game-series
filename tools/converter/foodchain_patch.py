# a food chain inside the bestiary: apex predators at the top, the pre-mutation virus near the bottom
import os
GEN = os.path.dirname(os.path.abspath(__file__))
p = os.path.join(GEN, 'bestiary.twee'); s = open(p, encoding='utf8').read()

CSS = '''#bestiary .btabs { display: flex; gap: 8px; margin: 0 0 16px; clear: both; }
#bestiary .btab { padding: .35em 1em; border-radius: 99px; border: 1px solid #4a4528; background: #16140c; color: #c7c2a4; cursor: pointer; }
#bestiary .btab.on { border-color: #fde68a; color: #fde68a; background: #2a2610; }
#bestiary .fchain { display: flex; flex-direction: column; align-items: center; gap: 0; }
#bestiary .ftier { width: 100%; background: #16140c; border: 1px solid #4a4528; border-radius: 12px; padding: 10px 12px 12px; }
#bestiary .ftier.apex { border-color: #b91c1c; background: #1f0d0b; }
#bestiary .ftier h3 { margin: 0 0 8px; font: 900 .85rem "Arial Black", Arial; letter-spacing: .12em; text-transform: uppercase; color: #fde68a; }
#bestiary .ftier.apex h3 { color: #fca5a5; }
#bestiary .ftier .fnote { margin: -4px 0 8px; font-size: .8rem; color: #a8a38a; }
#bestiary .frow { display: flex; flex-wrap: wrap; gap: 8px; }
#bestiary .fmon { width: 96px; text-align: center; font-size: .75rem; color: #e7e4d4; }
#bestiary .fmon .fimg { width: 96px; height: 72px; background: #000; border-radius: 8px; overflow: hidden; display: flex; align-items: center; justify-content: center; font: 900 1.6rem "Arial Black", Arial; color: #3a3520; }
#bestiary .fmon .fimg img { width: 100%; height: 100%; object-fit: contain; }
#bestiary .farrow { font-size: 1.4rem; color: #8a845e; line-height: 1.6; }
'''
JS = r'''/* the food chain: who eats who in the Backrooms. Higher tiers hunt everything below them. */
setup.FOODCHAIN = [
  { name: 'Apex predators', apex: true, note: 'Nothing hunts these. Everything else runs.', list: ['virus2', 'concierge', 'clown'] },
  { name: 'Top hunters', note: 'They hunt almost anything that wanders alone.', list: ['hound', 'skinstealer', 'watcher', 'chaser', 'giant'] },
  { name: 'Hunters', note: 'Dangerous, but they stay out of the apex predators\' way.', list: ['bacteria', 'lizard', 'whisperer', 'static', 'voice', 'smiler'] },
  { name: 'Scavengers', note: 'They pick off the weak and the lost.', list: ['partygoers', 'mannequins', 'crawler', 'redeyes'] },
  { name: 'Prey', note: 'Small, weak, and hunted by nearly everything. A virus at this stage of life is almost the same as a bacteria.', list: ['virus1', 'doll'] }
];
setup.openFoodChain = function () {
  var b = setup.best(), tiers = '';
  setup.FOODCHAIN.forEach(function (t, i) {
    var row = '';
    t.list.forEach(function (id) {
      var real = id.replace(/[12]$/, ''), x = setup.BEASTS.filter(function (z) { return z.id === real; })[0], e = b[real] || {};
      var known = x && e.seen && (id !== 'virus2' || e.form2), name = '???', img = '';
      if (known) {
        name = id === 'virus1' ? 'The Virus (before mutation)' : id === 'virus2' ? 'The Virus (after mutation)' : x.name;
        img = '<img src="' + setup.bestImg(id === 'virus2' && x.img2 ? x.img2 : x.img) + '" alt="">';
      }
      row += '<div class="fmon"><div class="fimg">' + (img || '?') + '</div>' + name + '</div>';
    });
    tiers += (i ? '<div class="farrow">\u{25B2}</div>' : '') + '<div class="ftier' + (t.apex ? ' apex' : '') + '"><h3>' + t.name + '</h3><p class="fnote">' + t.note + '</p><div class="frow">' + row + '</div></div>';
  });
  $('#bestiary .bgrid, #bestiary .fchain').remove();
  $('#bestiary .bwrap').append('<div class="fchain">' + tiers + '</div>');
};
$(document).on('click', '#bestiary .btab', function () {
  $('#bestiary .btab').removeClass('on'); $(this).addClass('on');
  if ($(this).attr('data-t') === 'chain') { setup.openFoodChain(); } else { setup.openBestiary(); }
});
'''
pairs = [
    (".bestlink { text-align: center; margin: 6px 0 0; }", ".bestlink { text-align: center; margin: 6px 0 0; }\n" + CSS.rstrip('\n')),
    ("    '<div class=\"bgrid\">' + cards + '</div></div></div>').appendTo('body');",
     "    '<div class=\"btabs\"><button class=\"btab on\" data-t=\"cards\">Creatures</button><button class=\"btab\" data-t=\"chain\">\\u{1F356} Food chain</button></div>' +\n"
     "    '<div class=\"bgrid\">' + cards + '</div></div></div>').appendTo('body');"),
    ("$(document).on('click', '#bestiary .bclose',", JS + "$(document).on('click', '#bestiary .bclose',"),
]
for a, b2 in pairs:
    if b2 in s: continue
    assert a in s, a[:60]; s = s.replace(a, b2, 1)
open(p, 'w', encoding='utf8').write(s)
print('food chain')
