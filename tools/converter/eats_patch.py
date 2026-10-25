# "Eats" and "Eaten by" lines on every bestiary card
import os
GEN = os.path.dirname(os.path.abspath(__file__))
p = os.path.join(GEN, 'bestiary.twee'); s = open(p, encoding='utf8').read()

js = r"""/* who eats who: ids are creatures, anything else is plain food. Eaten by is worked out from this. */
setup.EATS = {
  virus2: ['bacteria'], concierge: ['bacteria', 'whisperer', 'smiler', 'crawler'], clown: ['humans', 'partygoers', 'smiler'],
  hound: ['humans', 'lizard', 'mice'], skinstealer: ['humans', 'skinstealer'], watcher: ['humans', 'mice'], chaser: ['humans'], giant: ['humans', 'poopers'],
  bacteria: ['hatchlings', 'humans'], virusyoung: ['moths', 'mice'], poopers: ['partygoers'], lizard: ['humans', 'mice'],
  whisperer: ['humans'], static: ['humans'], voice: ['humans'], smiler: ['humans'],
  partygoers: ['humans'], mannequins: ['humans'], crawler: ['humans', 'mice'], redeyes: ['humans', 'moths'],
  hatchlings: ['moths'], humans: ['almond water', 'canned food'], doll: ['nothing at all'], moths: ['almond water'],
  mice: ['crumbs'], glowbugs: ['light'], bellmouse: ['cheese from the ballroom']
};
setup.chainName = function (id, b) {
  var key = id === 'virus2' ? 'virus' : id, x = setup.BEASTS.find(function (y) { return y.id === key; });
  if (!x) { return id; }
  return b[key] && b[key].seen ? x.name : '???';
};
setup.chainTag = function (id, b) {
  var key = id === 'virus' ? 'virus2' : id, eats = setup.EATS[key] || [], by = [];
  Object.keys(setup.EATS).forEach(function (k) { if (k !== key && setup.EATS[k].indexOf(key) >= 0) { by.push(k); } });
  var ids = function (l) { return l.map(function (e) { return setup.EATS[e] ? setup.chainName(e, b) : e; }).join(', '); };
  var self = eats.indexOf(key) >= 0 ? ' (even its own kind)' : '';
  var byTxt = by.length ? ids(by) : self ? 'Only others of its own kind.' : (key === 'bellmouse' ? 'Nothing dares. The Concierge protects it.' : 'Nothing. No creature hunts it.');
  return '<div class="bchain"><b>\u{1F37D}️ Eats:</b> ' + (eats.length ? ids(eats.filter(function (e) { return e !== key; })) + self : 'nothing') + '</div>' +
         '<div class="bchain"><b>\u{26A0}️ Eaten by:</b> ' + byTxt + '</div>';
};
"""
if 'setup.EATS = ' not in s:
    a = "setup.openBestiary = function () {"
    assert a in s; s = s.replace(a, js + a, 1)

a = "+ setup.popTag(x.id) + '<p>' + x.desc + '</p>' +"
b = "+ setup.popTag(x.id) + '<p>' + x.desc + '</p>' + setup.chainTag(x.id, b) +"
if b not in s:
    assert a in s; s = s.replace(a, b, 1)

if '.bcard .bchain' not in s:
    s = s.replace("#bestiary .bcard .btip {",
                  "#bestiary .bcard .bchain { font-size: .85rem; margin: 2px 0; color: #e8dcc0; }\n#bestiary .bcard .btip {", 1)
assert '.bcard .bchain' in s and 'setup.chainTag(x.id, b)' in s
open(p, 'w', encoding='utf8').write(s)
print('eats')
