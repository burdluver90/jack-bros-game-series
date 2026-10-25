# Humans: plain prey (not helpful), population 100, IQ 100
import os
GEN = os.path.dirname(os.path.abspath(__file__))
D = r'C:\Users\dahaw\OneDrive\Desktop\twine-games\part-3-1-backrooms\src\images'

# art: a lone, scared human with a flashlight in a yellow Level 0 hallway, eyes glowing in the dark behind
svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 300">'
       '<defs><radialGradient id="v" cx=".5" cy=".5" r=".75"><stop offset=".45" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".8"/></radialGradient>'
       '<linearGradient id="beam" x1="0" x2="1"><stop offset="0" stop-color="#fff7b0" stop-opacity=".75"/><stop offset="1" stop-color="#fff7b0" stop-opacity="0"/></linearGradient></defs>'
       '<rect width="400" height="300" fill="#b89a3e"/>'
       '<rect width="400" height="40" fill="#d8c27a"/><rect x="60" y="10" width="70" height="14" fill="#fffbe0"/><rect x="270" y="10" width="70" height="14" fill="#fffbe0" opacity=".4"/>'
       '<rect y="230" width="400" height="70" fill="#8a7330"/>'
       '<path d="M0 60 H400 M0 120 H400 M0 180 H400" stroke="#a88a34" stroke-width="2"/>'
       '<rect x="300" y="70" width="80" height="160" fill="#1a1408"/>'
       '<circle cx="325" cy="130" r="4" fill="#ff2b2b"/><circle cx="343" cy="130" r="4" fill="#ff2b2b"/>'
       '<polygon points="196,150 320,110 320,200" fill="url(#beam)"/>'
       '<g transform="translate(160 0)">'
       '<rect x="-16" y="182" width="12" height="50" fill="#1e3a8a"/><rect x="4" y="182" width="12" height="50" fill="#1e3a8a"/>'
       '<rect x="-18" y="228" width="16" height="7" fill="#222"/><rect x="2" y="228" width="16" height="7" fill="#222"/>'
       '<rect x="-22" y="120" width="44" height="66" rx="8" fill="#6b7280"/>'
       '<path d="M18 132 L36 152" stroke="#6b7280" stroke-width="11" stroke-linecap="round"/>'
       '<rect x="30" y="144" width="16" height="9" rx="2" fill="#333"/>'
       '<path d="M-18 132 L-30 168" stroke="#6b7280" stroke-width="11" stroke-linecap="round"/>'
       '<circle cx="0" cy="100" r="20" fill="#e0b48c"/>'
       '<path d="M-20 96 Q0 70 20 96 Q10 84 -20 96" fill="#4a2e1a"/>'
       '<circle cx="6" cy="100" r="2.6" fill="#111"/><circle cx="15" cy="100" r="2.6" fill="#111"/>'
       '<path d="M6 112 Q11 109 16 112" stroke="#7a3b2a" stroke-width="2" fill="none"/>'
       '<circle cx="-12" cy="108" r="2" fill="#8ecae6" opacity=".8"/>'
       '</g>'
       '<rect width="400" height="300" fill="url(#v)"/></svg>')
open(os.path.join(D, 'art_p_human.svg'), 'w', encoding='utf8').write(svg)

p = os.path.join(GEN, 'bestiary.twee'); s = open(p, encoding='utf8').read()
entry = ("  { id: 'humans', name: 'Humans', tag: 'Prey', known: true, img: 'art_p_human',\n"
         "    seen: ['Start'], deaths: [],\n"
         "    desc: 'Lost people who fell into the Backrooms, just like you. Only about 100 of them are still alive in the levels. Humans are smart, with an IQ of 100, but they are slow and soft and have no claws or tendrils, so almost every hunter in the Backrooms eats them. Most of them are scared and alone, and they will not help you. Some will even steal your almond water. And sometimes the human waving at you is not a human at all.',\n"
         "    tip: 'Do not count on other humans. If someone waves at you in the dark, it might be a Skin Stealer.' },\n")
if "id: 'humans'" not in s:
    a = "  { id: 'bellmouse',"
    assert a in s; s = s.replace(a, entry + a, 1)

# prey tier: humans join it, and the note no longer promises every prey helps
a = "note: 'Small, weak, and hunted by nearly everything. Be kind to them and they help you.', list: ['hatchlings', 'doll', 'moths', 'mice', 'glowbugs', 'bellmouse'] }"
b = "note: 'Small, weak, and hunted by nearly everything. Some of them help you if you are kind.', list: ['hatchlings', 'humans', 'doll', 'moths', 'mice', 'glowbugs', 'bellmouse'] }"
if b not in s:
    assert a in s; s = s.replace(a, b, 1)

# prey that are not friends still get the green prey outline
a = "var names = ['apex', 'tophunt', 'hunter', 'scav', ''], cls = '';"
if a in s:
    s = s.replace(a, "var names = ['apex', 'tophunt', 'hunter', 'scav', 'prey'], cls = '';", 1)
if '.bcard.prey' not in s:
    s = s.replace("#bestiary .bcard.friend { border: 4px solid #4fd18b; }",
                  "#bestiary .bcard.friend { border: 4px solid #4fd18b; }\n#bestiary .bcard.prey { border: 4px solid #4fd18b; }", 1)

# known: true shows the tip right away (you already know what a human is)
a = "(learned || x.friend ? '\\u{1F4A1} '"
if a in s:
    s = s.replace(a, "(learned || x.friend || x.known ? '\\u{1F4A1} '", 1)

# IQ and population
if 'humans: 100,' not in s:
    s = s.replace("setup.IQ = { virus2: 170,", "setup.IQ = { humans: 100, virus2: 170,", 1)
    s = s.replace("setup.POP = { virus2: 25,", "setup.POP = { humans: 100, virus2: 25,", 1)
assert s.count('humans: 100,') == 2 and '.bcard.prey' in s and 'x.known' in s and "'scav', 'prey'" in s
open(p, 'w', encoding='utf8').write(s)
print('humans')
