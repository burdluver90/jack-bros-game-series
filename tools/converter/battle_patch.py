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

W = '<<if setup.hasWeapon()>>'
E = '<</if>>'
patch('levels.twee', [
    ('[[Hide behind a pillar|Level 1 Hidden]]<<if setup.has("crowbar")>>',
     '[[Hide behind a pillar|Level 1 Hidden]]' + W + '[[Turn and fight it|Battle Skin Stealer]]' + E + '<<if setup.has("crowbar")>>'),
    ('<div id="opts" class="choices">[[Sprint for the grey door|Level 1 Stairwell]][[Dive under the party table|Under the Party Table]]</div>',
     '<div id="opts" class="choices">[[Sprint for the grey door|Level 1 Stairwell]][[Dive under the party table|Under the Party Table]]' + W + '[[Turn and fight them|Battle Partygoers]]' + E + '</div>'),
])
patch('levels3.py', [
    ("[[Follow the cold blue pipe|Level 4 Abandoned Office]]", "[[Follow the cold blue pipe|Level 2 Crawler]]"),
])
patch('hotel.py', [
    ("'<<if setup.hasWeapon()>>[[Fight the Concierge|Hotel Fight Concierge]]<</if>>'",
     "'<<if setup.hasWeapon()>>[[Fight the Concierge|Battle Concierge]]<</if>>'"),
    ("'The exit door is clear.<<run setup.useWeapon()>>') + '\\n' +", "'The exit door is clear.') + '\\n' +"),
    ("'You swing your <<print setup.weaponName()>>. The Concierge reaches for you with its long white gloves.',",
     "'One last swing of your <<print setup.weaponName()>>. The Concierge reaches for you with its long white gloves... too slow.',"),
    ("timed(4, ['<<if setup.has(\"axe\")>>[[Charge it with the fire axe|Hotel Hound Axe]]<</if>>',",
     "timed(4, ['<<if setup.has(\"axe\")>>[[Charge it with the fire axe|Hotel Hound Axe]]<</if>>', '<<if setup.hasWeapon()>>[[Fight the hound|Battle Hound]]<</if>>',"),
])
patch('drive31.py', [
    ("open(os.path.join(GEN,'hotel.twee'),encoding='utf8').read()}",
     "open(os.path.join(GEN,'hotel.twee'),encoding='utf8').read()+chr(10)+open(os.path.join(GEN,'battle.twee'),encoding='utf8').read()}"),
])

# the pipe crawler: a knot of rusty metal legs in a vent
legs = ''
import math, random
random.seed(9)
for i in range(14):
    a = -math.pi * .05 + i * (math.pi * 1.1 / 13)
    x1, y1 = 800 + math.cos(a) * 60, 470 + math.sin(a) * 40
    kx, ky = 800 + math.cos(a) * (180 + random.randint(0, 60)), 470 - abs(math.sin(a)) * (120 + random.randint(0, 80)) + 40
    fx, fy = 800 + math.cos(a) * (320 + random.randint(0, 80)), 600 + random.randint(0, 120)
    legs += f'<path d="M{x1:.0f} {y1:.0f} L{kx:.0f} {ky:.0f} L{fx:.0f} {fy:.0f}" stroke="#5b3a1f" stroke-width="{random.choice((12, 14, 16))}" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
    legs += f'<circle cx="{kx:.0f}" cy="{ky:.0f}" r="9" fill="#8a5530"/><circle cx="{kx:.0f}" cy="{ky:.0f}" r="4" fill="#2a1a10"/>'
eyes = ''.join(f'<circle cx="{800 + random.randint(-50, 50)}" cy="{470 + random.randint(-25, 25)}" r="{random.choice((4, 5, 6))}" fill="#ff3b3b" filter="url(#cg)"/>' for _ in range(11))
svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 900">
  <defs>
    <radialGradient id="cv" cx=".5" cy=".5" r=".75"><stop offset=".45" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".8"/></radialGradient>
    <linearGradient id="ct" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2a1a10"/><stop offset="1" stop-color="#120a05"/></linearGradient>
    <filter id="cg" x="-100%" y="-100%" width="300%" height="300%"><feGaussianBlur stdDeviation="4" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
  </defs>
  <rect width="1600" height="900" fill="url(#ct)"/>
  <!-- pipes along the walls -->
  <rect x="0" y="80" width="1600" height="50" fill="#6e4426"/><rect x="0" y="170" width="1600" height="30" fill="#5c3a22"/><rect x="0" y="780" width="1600" height="60" fill="#2563eb"/>
  <rect x="0" y="788" width="1600" height="10" fill="#93c5fd" opacity=".5"/>
  {''.join(f'<rect x="{x}" y="72" width="20" height="66" fill="#3b2414"/>' for x in range(60, 1600, 220))}
  <!-- the vent -->
  <rect x="560" y="300" width="480" height="340" rx="12" fill="#0a0604" stroke="#7a7a7a" stroke-width="14"/>
  {''.join(f'<path d="M{x} 300 v340" stroke="#4b4b4b" stroke-width="6"/>' for x in range(610, 1040, 60))}
  <path d="M560 300 L470 250 M1040 300 L1120 240" stroke="#7a7a7a" stroke-width="10"/>
  <!-- the crawler: legs, body, eyes -->
  {legs}
  <ellipse cx="800" cy="470" rx="110" ry="70" fill="#3b2414"/><ellipse cx="800" cy="460" rx="90" ry="50" fill="#5b3a1f"/>
  {''.join(f'<circle cx="{800 + dx}" cy="{470 + dy}" r="6" fill="#9ca3af"/>' for dx, dy in ((-70, -20), (60, -30), (-30, 40), (70, 30)))}
  {eyes}
  <!-- bent bolts on the floor -->
  {''.join(f'<rect x="{random.randint(200, 1400)}" y="{random.randint(700, 770)}" width="20" height="8" fill="#9ca3af" transform="rotate({random.randint(0, 180)} 800 740)"/>' for _ in range(10))}
  <rect width="1600" height="900" fill="url(#cv)"/>
</svg>
'''
open(os.path.join(D, 'art_crawler.svg'), 'w', encoding='utf8').write(svg)
print('battles wired in, crawler drawn')
