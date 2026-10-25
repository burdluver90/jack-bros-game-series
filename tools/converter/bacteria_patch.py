# a bacteria attacks you; the mutated virus absorbs it and grows extra tendrils
import os
GEN = os.path.dirname(os.path.abspath(__file__))
D = r'C:\Users\dahaw\OneDrive\Desktop\twine-games\part-3-1-backrooms\src\images'
def patch(f, pairs):
    p = os.path.join(GEN, f); s = open(p, encoding='utf8').read()
    for a, b in pairs:
        if b in s:
            continue
        assert a in s, (f, a[:80]); s = s.replace(a, b, 1)
    open(p, 'w', encoding='utf8').write(s)

# ---------- art ----------
cilia = ''.join(f'<line x1="{800 + 230 * __import__("math").cos(a / 20 * 6.283):.0f}" y1="{470 + 170 * __import__("math").sin(a / 20 * 6.283):.0f}" '
                f'x2="{800 + 290 * __import__("math").cos(a / 20 * 6.283):.0f}" y2="{470 + 220 * __import__("math").sin(a / 20 * 6.283):.0f}"/>' for a in range(20))
bact = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 900">
  <defs>
    <radialGradient id="slime" cx=".45" cy=".4" r=".7"><stop offset="0" stop-color="#b6f06a"/><stop offset=".6" stop-color="#5a9a2a"/><stop offset="1" stop-color="#1f3d0e"/></radialGradient>
    <radialGradient id="vign" cx=".5" cy=".5" r=".75"><stop offset=".5" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".8"/></radialGradient>
    <filter id="blur"><feGaussianBlur stdDeviation="14"/></filter>
  </defs>
  <rect width="1600" height="900" fill="#14180c"/>
  <!-- carpet and damp walls, like Level 4 gone wrong -->
  <polygon points="0,620 1600,620 1600,900 0,900" fill="#3a3a22"/>
  <g fill="#6b8f2a" opacity=".35" filter="url(#blur)"><ellipse cx="300" cy="300" rx="200" ry="120"/><ellipse cx="1300" cy="250" rx="220" ry="140"/><ellipse cx="800" cy="760" rx="500" ry="80"/></g>
  <!-- the bacteria: a huge pill-shaped cell with whip-like flagella -->
  <g stroke="#86c43a" stroke-width="8" stroke-linecap="round" fill="none" opacity=".9">{cilia}
    <path d="M1080 470 C1250 380 1300 560 1480 470"/><path d="M1060 560 C1220 660 1320 520 1560 640"/><path d="M540 520 C380 640 260 500 60 600"/></g>
  <ellipse cx="800" cy="470" rx="240" ry="175" fill="url(#slime)"/>
  <g fill="#2d5410" opacity=".7"><ellipse cx="720" cy="420" rx="50" ry="34"/><ellipse cx="880" cy="520" rx="70" ry="40"/><circle cx="860" cy="390" r="18"/><circle cx="690" cy="530" r="14"/></g>
  <!-- a mouth-like opening -->
  <path d="M700 480 Q800 560 900 480 Q800 520 700 480 Z" fill="#0d1a05"/>
  <rect width="1600" height="900" fill="url(#vign)"/>
</svg>
'''
absorb = bact.replace('<ellipse cx="800" cy="470" rx="240" ry="175" fill="url(#slime)"/>',
    '<ellipse cx="1100" cy="500" rx="150" ry="110" fill="url(#slime)" opacity=".75"/>'
    '<!-- the virus tendrils pierce the bacteria and drain it -->'
    '<g stroke="#7c2d92" stroke-width="16" stroke-linecap="round" fill="none"><path d="M560 300 C760 260 900 420 1060 470"/><path d="M560 420 C760 520 900 560 1080 540"/><path d="M560 560 C740 700 960 640 1120 580"/></g>'
    '<g fill="#b6f06a" opacity=".9"><circle cx="760" cy="290" r="10"/><circle cx="880" cy="380" r="8"/><circle cx="780" cy="500" r="9"/><circle cx="900" cy="620" r="10"/></g>') \
    .replace('<path d="M700 480 Q800 560 900 480 Q800 520 700 480 Z" fill="#0d1a05"/>', '')
for n, s in (('art_bacteria', bact), ('art_absorb', absorb)):
    open(os.path.join(D, n + '.svg'), 'w', encoding='utf8').write(s)

# ---------- passages, between Level ! and the hotel ----------
patch('levels3.py', [
    ("'<<set $virusWith to true>>\"We are deeper than anyone has ever gone,\" it says. \"And I think I know where the real exit is.\"') +\n    f'\\n<div class=\"choices\">[[Next|{END}]]</div>\\n')",
     "'<<set $virusWith to true>>\"We are deeper than anyone has ever gone,\" it says. \"And I think I know where the real exit is.\"') +\n    '\\n<div class=\"choices\">[[Next|Bacteria Attack]]</div>\\n')\n"
     "P.append(':: Bacteria Attack\\n' + scene('art_bacteria', (4, 14, .75)) + '\\n' + story(\n"
     "    'Something wet slaps against the carpet behind you.',\n"
     "    'A giant green bacteria oozes out of the vent, whipping its long tails. It lunges and wraps one around your leg.',\n"
     "    'The virus goes very still. \"That,\" it says, \"is a bacteria. I am basically one too. But it is not like me.\"') +\n"
     "    '\\n<div id=\"opts\" class=\"choices\">[[Tell the virus to get it|Bacteria Absorb]]'\n"
     "    '<<if setup.hasWeapon()>><<link `\"Hit the tail with your \" + setup.weaponName()` \"Bacteria Hit\">><</link>><</if>></div>\\n'\n"
     "    '<div class=\"timerbar\"><span style=\"animation-duration:3s\"></span></div>\\n'\n"
     "    '<<timed 3s>><<replace \"#opts\">><div class=\"caught\">[[It drags you into the vent|Bacteria Ending]]</div><</replace>><<run $(\".timerbar\").remove()>><</timed>>\\n')\n"
     "P.append(':: Bacteria Hit\\n' + scene('art_bacteria', (4, 14, .75)) + '\\n' + story(\n"
     "    'You smash the tail. It lets go of your leg, but it splits into two new tails. Hitting it just makes more of it.<<run setup.useWeapon()>>',\n"
     "    'The virus pushes you behind it. \"My turn.\"') +\n"
     "    '\\n<div class=\"choices\">[[Let the virus handle it|Bacteria Absorb]]</div>\\n')\n"
     "P.append(':: Bacteria Absorb\\n' + scene('art_absorb', (4, 14, .75)) + '\\n' + story(\n"
     "    'The virus shoots its tendrils straight into the bacteria. The green slime starts flowing up them, into the virus.',\n"
     "    'The bacteria shrinks... and shrinks... until it is nothing but a puddle on the carpet.',\n"
     "    '<<set $virusStrong to true>>The virus shudders. Three brand-new tendrils burst out of its back, thicker and longer than the others. \"Much better,\" it says. \"Now I can fight with you.\"') +\n"
     "    f'\\n<div class=\"choices\">[[Next|{END}]]</div>\\n')"),
    ("        ('Steam Ending', 'art_level2',",
     "        ('Bacteria Ending', 'art_bacteria', ['The bacteria pulls you into the vent.', 'It is very dark in there, and very, very wet.']),\n        ('Steam Ending', 'art_level2',"),
])
patch('hud.twee', [("  v.boilerCode = setup.newCode();\n};", "  v.boilerCode = setup.newCode(); v.virusStrong = false;\n};")])
# the new tendrils help in every battle after this
patch('battle.twee', [("    hp -= dmg; pad.data('hp', hp);",
     "    if (State.variables.virusStrong) { dmg += 1; log += 'The virus lashes it with its new tendrils (+1). '; }\n    hp -= dmg; pad.data('hp', hp);")])
patch('hotel.py', [("'<<if $virusWith>>[[Let the virus distract it|Hotel Virus Distracts]]<</if>>',",
     "'<<if $virusWith>>[[Let the virus distract it|Hotel Virus Distracts]]<</if>>',\n            '<<if $virusStrong>><span class=\"tip\">The virus flexes its new tendrils. It will hit harder in a fight now.</span><</if>>',")])
patch('bestiary.twee', [("  { id: 'crawler',",
     "  { id: 'bacteria', name: 'The Bacteria', tag: 'After Level !', img: 'art_bacteria',\n"
     "    seen: ['Bacteria Attack'], deaths: ['Bacteria Ending'], beat: ['Bacteria Absorb'],\n"
     "    desc: 'A giant green cell with whipping tails that crawls out of the vents. Cut a tail and two grow back.',\n"
     "    tip: 'Weapons only make more tails. Let the virus absorb it, and the virus grows stronger tendrils.' },\n  { id: 'crawler',")])
print('bacteria patched')
