# Partypoopers become hunters of the Partygoers (the Biggest Partygoer is their worst nightmare); IQ scores in the food chain
import os, re
GEN = os.path.dirname(os.path.abspath(__file__))
p = os.path.join(GEN, 'bestiary.twee'); s = open(p, encoding='utf8').read()

s = s.replace("{ id: 'poopers', name: 'The Partypoopers', tag: 'Prey',", "{ id: 'poopers', name: 'The Partypoopers', tag: 'Hunter',", 1)
s = re.sub(r"(  \{ id: 'poopers'.*?\n.*?\n)    desc: '[^\n]*\n",
           r"\1    desc: 'Very friendly grey party guests who hide behind fake smiling masks on sticks. The Partypoopers and the Partygoers have been at war for as long as anyone can remember, and the Partypoopers are the hunters: the disguise lets them sneak through Level Fun and pick off Partygoers one by one. Only one thing scares them. The Biggest Partygoer is their worst nightmare, and they never go near the door it guards. To a real person they are warm, chatty and always happy to help.',\n",
           s, count=1, flags=re.S)
assert 'worst nightmare' in s
# move them from Prey to Hunters in the food chain
s = s.replace("list: ['hatchlings', 'doll', 'poopers', 'moths',", "list: ['hatchlings', 'doll', 'moths',", 1)
s = s.replace("list: ['bacteria', 'virusyoung', 'lizard',", "list: ['bacteria', 'virusyoung', 'poopers', 'lizard',", 1)
assert "'virusyoung', 'poopers'" in s and "'doll', 'moths'" in s

# IQ for every creature, shown under its name in the food chain
iq = ("/* how smart each creature is */\n"
      "setup.IQ = { virus2: 170, concierge: 170, clown: 95, hound: 40, skinstealer: 110, watcher: 60, chaser: 20, giant: 55,\n"
      "  bacteria: 70, virusyoung: 150, poopers: 105, lizard: 30, whisperer: 90, static: 80, voice: 100, smiler: 50,\n"
      "  partygoers: 45, mannequins: 25, crawler: 15, redeyes: 10,\n"
      "  hatchlings: 60, doll: 75, moths: 5, mice: 20, glowbugs: 3, bellmouse: 85 };\n")
if 'setup.IQ =' not in s:
    s = s.replace("setup.openFoodChain = function () {", iq + "setup.openFoodChain = function () {", 1)
a = "      row += '<div class=\"fmon\"><div class=\"fimg\">' + (img || '?') + '</div>' + name + '</div>';"
b = "      row += '<div class=\"fmon\"><div class=\"fimg\">' + (img || '?') + '</div>' + name + (known && setup.IQ[id] !== undefined ? '<span class=\"fiq\">IQ ' + setup.IQ[id] + '</span>' : '') + '</div>';"
if b not in s:
    assert a in s; s = s.replace(a, b, 1)
css = "#bestiary .fmon .fiq { display: block; margin-top: 2px; font: 700 .7rem Arial, sans-serif; color: #9db8ff; letter-spacing: .05em; }"
if '.fiq' not in s:
    s = s.replace("#bestiary .farrow {", css + "\n#bestiary .farrow {", 1)
assert '.fiq' in s
open(p, 'w', encoding='utf8').write(s)

# the scene: they are hunters, and the Biggest Partygoer scares them
p = os.path.join(GEN, 'levels3.py'); s = open(p, encoding='utf8').read()
a = 'We are at WAR with the Partygoers. We have been for as long as anyone can remember."'
b = ('We are at WAR with the Partygoers. We have been for as long as anyone can remember. We hunt them, one by one." '
     'It shivers. "Except the big one by the door. Nobody hunts THAT one."')
if b not in s:
    assert a in s; s = s.replace(a, b, 1)
open(p, 'w', encoding='utf8').write(s)
print('iq')
