# a population for every creature, on its bestiary card and in the food chain
import os
GEN = os.path.dirname(os.path.abspath(__file__))
p = os.path.join(GEN, 'bestiary.twee'); s = open(p, encoding='utf8').read()

pop = ("/* how many of each creature live in the Backrooms */\n"
       "setup.POP = { virus2: 25, concierge: 1, clown: 1, hound: 340, skinstealer: 10, watcher: 75, chaser: 1, giant: 1,\n"
       "  bacteria: 40000, virusyoung: 33000, poopers: 500, lizard: 8000, whisperer: 300, static: 1200, voice: 1, smiler: 5000,\n"
       "  partygoers: 12000, mannequins: 2500, crawler: 15000, redeyes: 30000,\n"
       "  hatchlings: 100000, doll: 1, moths: 1000000, mice: 250000, glowbugs: 5000000, bellmouse: 1 };\n"
       "setup.popNum = function (id) { var n = setup.POP[id === 'virus' ? 'virus2' : id]; return n === undefined ? '' : n.toLocaleString('en-US'); };\n"
       "setup.popTag = function (id) { var n = setup.popNum(id); return n === '' ? '' : '<div class=\"bpop\">\\u{1F465} Population ' + n + (n === '1' ? ' (the only one)' : '') + '</div>'; };\n")
if 'setup.POP = ' not in s:
    a = "setup.iqTag = function (id) {"
    assert a in s; s = s.replace(a, pop + a, 1)

a = "+ setup.iqTag(x.id) + '<p>'"
b = "+ setup.iqTag(x.id) + setup.popTag(x.id) + '<p>'"
if b not in s:
    assert a in s; s = s.replace(a, b, 1)

a = "'<span class=\"fiq\">IQ ' + setup.IQ[id] + '</span>' : '')"
b = a + " + (known && setup.popNum(id) !== '' ? '<span class=\"fpop\">Pop ' + setup.popNum(id) + '</span>' : '')"
if 'class=\"fpop\"' not in s:
    assert a in s; s = s.replace(a, b, 1)

if '.bcard .bpop' not in s:
    s = s.replace("#bestiary .bcard .btip {",
                  "#bestiary .bcard .bpop { font: 700 .8rem Arial, sans-serif; color: #8fe3b0; letter-spacing: .04em; }\n#bestiary .bcard .btip {", 1)
if '.fmon .fpop' not in s:
    s = s.replace("#bestiary .farrow {",
                  "#bestiary .fmon .fpop { display: block; font: 700 .7rem Arial, sans-serif; color: #8fe3b0; letter-spacing: .05em; }\n#bestiary .farrow {", 1)
assert '.bcard .bpop' in s and '.fmon .fpop' in s and 'setup.popTag(x.id)' in s
open(p, 'w', encoding='utf8').write(s)
print('pop')
