# the Partypoopers wear disguise smiles, are very friendly, and hate the Partygoers
import os, re
GEN = os.path.dirname(os.path.abspath(__file__))
D = r'C:\Users\dahaw\OneDrive\Desktop\twine-games\part-3-1-backrooms\src\images'

# art: same three guests, but each holds a fake smiling mask on a stick in front of its face (one tilted so you see it is a disguise)
p = os.path.join(D, 'art_partypoopers.svg'); s = open(p, encoding='utf8').read()
def mask(x, y, k, tilt):
    return (f'<g transform="translate({x} {y + 20 * k}) scale({k}) rotate({tilt})">'
            f'<rect x="-3" y="40" width="6" height="110" fill="#a16207"/>'
            f'<ellipse rx="56" ry="50" fill="#fef3c7" stroke="#d6b45a" stroke-width="4"/>'
            f'<ellipse cx="-20" cy="-10" rx="8" ry="10" fill="#1f2937"/><ellipse cx="20" cy="-10" rx="8" ry="10" fill="#1f2937"/>'
            f'<path d="M-32 14 Q0 48 32 14" stroke="#b91c1c" stroke-width="7" fill="none" stroke-linecap="round"/>'
            f'<circle cx="-36" cy="12" r="8" fill="#fca5a5" opacity=".7"/><circle cx="36" cy="12" r="8" fill="#fca5a5" opacity=".7"/></g>')
masks = mask(560, 420, 1.1, -8) + mask(800, 400, 1.25, 0) + mask(1210, 430, 1.05, 24)
s = s.replace('NO PARTY  :(', 'PARTYGOERS NOT WELCOME')
if 'fef3c7' not in s:
    s = s.replace('<rect width="1600" height="900" fill="url(#v)"/></svg>', masks + '<rect width="1600" height="900" fill="url(#v)"/></svg>')
open(p, 'w', encoding='utf8').write(s)

p = os.path.join(GEN, 'levels3.py'); s = open(p, encoding='utf8').read()
start = s.index("P.append(':: Partypoopers\\n'")
end = s.index("P.append(':: Level 2 Valve\\n'")
new = ("P.append(':: Partypoopers\\n' + withVirus('art_partypoopers', (2, 14, .7)) + '\\n' + story(\n"
       "    'Behind the last door of Level Fun is a small grey room. A hand-painted sign on the wall says PARTYGOERS NOT WELCOME.',\n"
       "    'Three figures turn around. They are all smiling... but the smiles are painted on masks they hold up on sticks. One of them lowers its mask a little and waves at you.',\n"
       "    '\"Oh, a real person! Hi! Welcome!\" it says happily. \"We are the Partypoopers. We wear these smiles so the Partygoers think we are one of them. We cannot STAND the Partygoers.\" It holds up an old camera. \"Want a picture with us? We love pictures!\"') +\n"
       "    '\\n<div class=\"choices\"><span id=\"pp\"><<if !setup.has(\"photo\")>><<link \"Take a picture with the Partypoopers\">><<run setup.addItem(\"photo\")>><<replace \"#pp\">><p>FLASH. The photo slides out of the camera: you in the middle, three Partypoopers holding their fake smiles up and giving you a thumbs up. Looking at it makes you feel safe. It goes in your gear slot.</p><</replace>><</link>><</if>></span>'\n"
       "    '[[Wave goodbye and drop down the hatch|Level 2 Pipe Dreams]]</div>\\n')\n")
s = s[:start] + new + s[end:]
open(p, 'w', encoding='utf8').write(s)

p = os.path.join(GEN, 'bestiary.twee'); s = open(p, encoding='utf8').read()
s = re.sub(r"    desc: 'Grey, grumpy party guests[^\n]*\n",
           "    desc: 'Very friendly grey party guests who hide behind fake smiling masks on sticks. The disguise lets them sneak through Level Fun, because they HATE the Partygoers and want nothing to do with their party. To a real person they are warm, chatty and always happy to help.',\n", s, count=1)
s = s.replace("    tip: 'Take a picture with them. Their frowns are so calming that carrying the photo makes you lose 1 less sanity every scene.' },",
              "    tip: 'Say hi and take a picture with them. Carrying the photo makes you feel safe, so you lose 1 less sanity every scene.' },")
assert 'fake smiling masks' in s and 'Say hi and take a picture' in s
open(p, 'w', encoding='utf8').write(s)

p = os.path.join(GEN, 'hud.twee'); s = open(p, encoding='utf8').read()
s = s.replace("desc: 'You and three very grumpy Partypoopers. Looking at it keeps you calm: you lose 1 less sanity every scene.'",
              "desc: 'You and three friendly Partypoopers holding up their fake smiles. Looking at it makes you feel safe: you lose 1 less sanity every scene.'")
assert 'friendly Partypoopers' in s
open(p, 'w', encoding='utf8').write(s)
print('poopers v2')
