import os
GEN = os.path.dirname(os.path.abspath(__file__))
def patch(f, pairs):
    p = os.path.join(GEN, f); s = open(p, encoding='utf8').read()
    for a, b in pairs:
        if b in s:
            continue
        assert a in s, (f, a[:60]); s = s.replace(a, b, 1)
    open(p, 'w', encoding='utf8').write(s)

patch('hotel.py', [
    # any weapon works against the Concierge
    ("'<<if setup.has(\"sword\")>>You raise the sword.<<else>>You swing the crowbar.<</if>> The Concierge",
     "'You swing your <<print setup.weaponName()>>. The Concierge"),
    # a fire axe on the staircase
    ("'Up to FLOOR 2. Further up to FLOOR 3, where the sign has been crossed out with red paint. And a narrow service stair going down to the BASEMENT.') + '\\n' +\n    choices('[[Floor 2|Hotel Floor 2]]',",
     "'Up to FLOOR 2. Further up to FLOOR 3, where the sign has been crossed out with red paint. And a narrow service stair going down to the BASEMENT.',\n"
     "    '<<if !setup.isTaken(\"axe\")>>On the landing there is a red glass case: FIRE AXE. IN CASE OF EMERGENCY, BREAK GLASS.<<else>>The fire axe case is empty and broken.<</if>>') + '\\n' +\n"
     "    choices(pickup('axe', 'axe', 'Break the glass and take the fire axe'), '[[Floor 2|Hotel Floor 2]]',"),
    # the axe beats the hound
    ("timed(4, ['[[Hold your breath and tiptoe past it|Hotel Boiler Door]]',",
     "timed(4, ['<<if setup.has(\"axe\")>>[[Charge it with the fire axe|Hotel Hound Axe]]<</if>>', '[[Hold your breath and tiptoe past it|Hotel Boiler Door]]',"),
    ("add('Hotel Boiler Door',",
     "add('Hotel Hound Axe', scene('art_h_stairs') + '\\n' + story(\n"
     "    'You run down the stairs swinging the fire axe and yelling as loud as you can.',\n"
     "    'The hound\\'s white eyes go wide. It has never seen prey fight back. It scrambles away into the dark and does not come back.') + '\\n' +\n"
     "    choices('[[Keep going down|Hotel Boiler Door]]'), 'hotel')\n\nadd('Hotel Boiler Door',"),
])
patch('levels3.py', [
    # a pipe wrench in Level 2
    ("'\\n<div class=\"choices\"><<if !setup.isTaken(\"flashlight\")>>",
     "'\\n<div class=\"choices\"><<if !setup.isTaken(\"wrench\")>><span id=\"pkw\"><<link \"Take the pipe wrench off the valve\">><<if setup.take(\"wrench\",\"wrench\")>><<replace \"#pkw\">><</replace>><</if>><</link>></span><</if>><<if !setup.isTaken(\"flashlight\")>>"),
    ("'A flashlight hangs from a red valve wheel.')",
     "'A flashlight hangs from a red valve wheel. A rusty pipe wrench is stuck on the valve next to it.')"),
    # a weapon also scares off the red eyes in Level 6
    ("'[[Walk toward the whispering|Whispers Ending]]",
     "'<<if setup.hasWeapon()>>[[Swing your <<print setup.weaponName()>> at the red eyes|Lights Out Swing]]<</if>>[[Walk toward the whispering|Whispers Ending]]"),
    ("P.append(':: Lights Out Flashlight\\n'",
     "P.append(':: Lights Out Swing\\n' + scene('art_level6') + '\\n' + story(\n"
     "    'You swing blindly into the dark. CRACK. Something shrieks.',\n"
     "    'The red eyes blink out one pair at a time. Under your feet you feel the floor slope toward a faint red glow.') +\n"
     "    '\\n<div class=\"choices\">[[Follow the slope|Level Run For Your Life]]</div>\\n')\n"
     "P.append(':: Lights Out Flashlight\\n'"),
])
print('weapon patches applied')
