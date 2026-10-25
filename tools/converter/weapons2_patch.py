# weapons get pros and cons
import os
GEN = os.path.dirname(os.path.abspath(__file__))
def patch(f, pairs):
    p = os.path.join(GEN, f); s = open(p, encoding='utf8').read()
    for a, b in pairs:
        if b in s:
            continue
        assert a in s, (f, a[:80]); s = s.replace(a, b, 1)
    open(p, 'w', encoding='utf8').write(s)

patch('hud.twee', [
    ("desc: 'Sharp. Might help in a fight.' }",
     "desc: 'PRO: wins every fight and never breaks. CON: heavy, you lose 1 extra sanity every scene while you carry it.' }"),
    ("desc: 'Heavy and red. Good for prying doors, or hitting things.' }",
     "desc: 'PRO: light, and it can pry open locked doors. CON: clumsy, you get hurt in fights (-15 sanity).' }"),
    ("desc: 'Wet from the poolrooms, but still solid. A weapon.' }",
     "desc: 'PRO: light, no downside while you carry it. CON: it snaps after one fight.' }"),
    ("desc: 'Heavy enough to dent metal. A weapon.' }",
     "desc: 'PRO: light, and it can turn big valves. CON: weak, you get hurt in fights (-10 sanity).' }"),
    ("desc: 'IN CASE OF EMERGENCY. The best weapon you have found. Hounds hate it.' }",
     "desc: 'PRO: wins every fight and hounds are scared of it. CON: heavy, you lose 1 extra sanity every scene while you carry it.' }"),
    # best weapon first; the bat last because it breaks
    ("setup.WEAPONS = ['sword', 'axe', 'bat', 'wrench', 'crowbar'];",
     "setup.WEAPONS = ['sword', 'axe', 'wrench', 'crowbar', 'bat'];\n"
     "setup.HEAVY = ['sword', 'axe'];\n"
     "/* call after a won fight: the weapon's downside kicks in */\n"
     "setup.useWeapon = function () {\n"
     "  var v = State.variables, w = setup.WEAPONS.filter(setup.has)[0];\n"
     "  if (w === 'bat') { v.inv.splice(v.inv.indexOf('bat'), 1); setup.toast('CRACK! Your baseball bat snapped in half.'); }\n"
     "  else if (w === 'crowbar') { v.sanity = Math.max(1, v.sanity - 15); setup.toast('The crowbar slipped. You got hurt (-15 sanity).'); }\n"
     "  else if (w === 'wrench') { v.sanity = Math.max(1, v.sanity - 10); setup.toast('The wrench is too weak. You got hurt (-10 sanity).'); }\n"
     "  setup.hud();\n"
     "};"),
    # heavy weapons drain a bit more
    ("setup.drainFor = function (p) { var d = setup.mode().drain; return p.tags.indexOf('fun') >= 0 ? d * 2 : d; };",
     "setup.drainFor = function (p) {\n"
     "  var d = setup.mode().drain; if (p.tags.indexOf('fun') >= 0) { d *= 2; }\n"
     "  return d + setup.HEAVY.filter(setup.has).length;   /* +1 for each heavy weapon you carry */\n"
     "};"),
])
# fights apply the downside
patch('drive31.py', [
    ("'on_enter':{1:'<<run setup.reset()>>',", "'on_enter':{1:'<<run setup.reset()>>',54:'<<run setup.useWeapon()>>',"),
])
patch('hotel.py', [
    ("'The exit door is clear.') + '\\n' +", "'The exit door is clear.<<run setup.useWeapon()>>') + '\\n' +"),
])
patch('levels3.py', [
    ("'The red eyes blink out one pair at a time. Under your feet you feel the floor slope toward a faint red glow.') +",
     "'The red eyes blink out one pair at a time. Under your feet you feel the floor slope toward a faint red glow.<<run setup.useWeapon()>>') +"),
    # the wrench can shut off the hot pipe: a new safe route
    ("'[[Follow the cold blue pipe|Level 4 Abandoned Office]][[Follow the hot red pipe|Steam Ending]]</div>\\n')",
     "'<<if setup.has(\"wrench\")>>[[Use the wrench to shut the hot pipe valve|Level 2 Valve]]<</if>>[[Follow the cold blue pipe|Level 4 Abandoned Office]][[Follow the hot red pipe|Steam Ending]]</div>\\n')\n"
     "P.append(':: Level 2 Valve\\n' + scene('art_level2') + '\\n' + story(\n"
     "    'You clamp the pipe wrench onto the big red valve and pull with everything you have.',\n"
     "    'SCREEEECH. The valve turns. The hissing stops. The red-hot pipe slowly fades to a dull grey.',\n"
     "    'Now you can follow it. It goes straight down, a shortcut.') +\n"
     "    '\\n<div class=\"choices\">[[Follow the cooled pipe down|Level 6 Lights Out]]</div>\\n')"),
])
print('weapon pros and cons patched')
