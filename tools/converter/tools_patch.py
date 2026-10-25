# crowbar and wrench get utility uses around the game
import os
GEN = os.path.dirname(os.path.abspath(__file__))
def patch(f, pairs):
    p = os.path.join(GEN, f); s = open(p, encoding='utf8').read()
    for a, b in pairs:
        if b in s:
            continue
        assert a in s, (f, a[:80]); s = s.replace(a, b, 1)
    open(p, 'w', encoding='utf8').write(s)

CROW = '<<if setup.has("crowbar")>>'
WR = '<<if setup.has("wrench")>>'
END = '<</if>>'

patch('hud.twee', [
    ("desc: 'PRO: light, and it can pry open locked doors. CON: clumsy, you get hurt in fights (-15 sanity).' }",
     "desc: 'PRO: light, and it pries open doors, hatches and stuck elevators. CON: clumsy, you get hurt in fights (-15 sanity).' }"),
    ("desc: 'PRO: light, and it can turn big valves. CON: weak, you get hurt in fights (-10 sanity).' }",
     "desc: 'PRO: light, and it turns valves, fixes squeaky hinges and opens taps. CON: weak, you get hurt in fights (-10 sanity).' }"),
])

# Level 1: the crowbar pries a floor hatch while the skin stealer is coming
patch('levels.twee', [
    ('<div id="opts" class="choices">[[Hide behind a pillar|Level 1 Hidden]]</div>',
     '<div id="opts" class="choices">[[Hide behind a pillar|Level 1 Hidden]]' + CROW + '[[Pry open the floor hatch with the crowbar|Level 1 Hatch]]' + END + '</div>'),
    # Level Fun: the wrench quiets the squeaky grey door
    ('[[Ease the grey door open slowly|Level 1 Stairwell]]',
     '[[Ease the grey door open slowly|Level 1 Stairwell]]' + WR + '[[Tighten the squeaky hinges with the wrench first|Level Fun Hinges]]' + END),
])
p = os.path.join(GEN, 'levels.twee'); s = open(p, encoding='utf8').read()
if ':: Level 1 Hatch' not in s:
    s += '''
:: Level 1 Hatch [flicker]
<div class="scene"><div class="pos bg">[img[art_level1]]</div></div>
<div class="story-text"><p>You jam the crowbar into the edge of a metal hatch in the floor and heave. It pops open with a clang.</p><p>You drop down and pull it shut just as long grey fingers slide across the floor above you.</p><p>A ladder leads down to a stairwell.</p></div>
<div class="choices">[[Climb down to the stairwell|Level 1 Stairwell]]</div>

:: Level Fun Hinges [fun]
<div class="scene"><div class="pos bg">[img[art_funexits]]</div></div>
<div class="story-text"><p>You tighten the rusty hinges of the grey door one careful turn at a time.</p><p>The door swings open without a single squeak. Behind you, the party keeps going. Nobody noticed.</p></div>
<div class="choices">[[Slip through the grey door|Level 1 Stairwell]]</div>
'''
    open(p, 'w', encoding='utf8').write(s)

# Level 4: the wrench opens the water cooler tap so you can fill a bottle to keep
patch('levels3.py', [
    ("'\\n<div class=\"choices\"><span id=\"cool\"><<link \"Drink from the water cooler\">>",
     "'\\n<div class=\"choices\">' + '" + WR + "<<if !setup.isTaken(\"coolerbottle\")>><span id=\"pkcb\"><<link \"Unscrew the cooler tap with the wrench and fill a bottle\">><<if setup.take(\"coolerbottle\",\"almond\")>><<replace \"#pkcb\">><</replace>><</if>><</link>></span><</if>>" + END + "' + '<span id=\"cool\"><<link \"Drink from the water cooler\">>"),
])

# Hotel: crowbar opens Room 215 (maid's closet) and the dead elevator; wrench bleeds the boiler pressure
patch('hotel.py', [
    ("            '[[Room 217|Hotel Room 217]]', '[[Back to the stairs|Hotel Staircase]]'), 'hotel')",
     "            '" + CROW + "[[Pry open Room 215 with the crowbar|Hotel Room 215]]" + END + "', '[[Room 217|Hotel Room 217]]', '[[Back to the stairs|Hotel Staircase]]'), 'hotel')\n\n"
     "add('Hotel Room 215', scene('art_h_room') + '\\n' + story(\n"
     "    'Room 215 has no handle because it is not a guest room. It is the maid\\'s closet.',\n"
     "    'Shelves of towels, tiny soaps, and a cleaning cart. Pinned to the wall is a staff notice:',\n"
     "    '\"STAFF REMINDER: the boiler code is the same as the band\\'s song. Do NOT tell the guests.\"') + '\\n' +\n"
     "    choices(pickup('w215', 'almond', 'Take a bottle of almond water from the cart'), '[[Back to the hallway|Hotel Floor 2]]'), 'hotel')"),
    ("    'A sticker on the panel says: POWER CONTROLS - FLOOR 3.') + '\\n' +\n    choices('[[Back to the lobby|Hotel Lobby]]'), 'hotel')",
     "    'A sticker on the panel says: POWER CONTROLS - FLOOR 3.') + '\\n' +\n"
     "    choices('" + CROW + "[[Pry the elevator doors open with the crowbar|Hotel Elevator Shaft]]" + END + "', '[[Back to the lobby|Hotel Lobby]]'), 'hotel')\n\n"
     "add('Hotel Elevator Shaft', scene('art_h_stairs') + '\\n' + story(\n"
     "    'You force the crowbar between the doors and lean on it until they grind open.',\n"
     "    'No elevator. Just a dark shaft and thick greasy cables going all the way down.',\n"
     "    'At the very bottom you can see a faint light and the word BASEMENT.') + '\\n' +\n"
     "    choices('[[Climb down the cables|Hotel Boiler Door]]', '[[Back to the lobby|Hotel Lobby]]'), 'hotel')"),
    ("    choices('[[Try again, carefully|Hotel Keypad]]',",
     "    choices('" + WR + "<<link \"Bleed the pressure valve with the wrench\" \"Hotel Keypad\">><<set $codeTries to 0>><<run setup.toast(\"Hissss. The pressure drops back to safe.\")>><</link>>" + END + "', '[[Try again, carefully|Hotel Keypad]]',"),
])
print('tool uses patched')
