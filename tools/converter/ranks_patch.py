# food chain changes: Clown IQ 130, a Protected group (Doll, Bellhop Mouse), Partygoers become Hunters
import os
GEN = os.path.dirname(os.path.abspath(__file__))
p = os.path.join(GEN, 'bestiary.twee'); s = open(p, encoding='utf8').read()

s = s.replace("concierge: 170, clown: 95,", "concierge: 170, clown: 130,", 1)

a = "list: ['bacteria', 'virusyoung', 'poopers', 'lizard', 'whisperer', 'static', 'voice', 'smiler'] },"
b = "list: ['bacteria', 'virusyoung', 'poopers', 'partygoers', 'lizard', 'whisperer', 'static', 'voice', 'smiler'] },"
if b not in s:
    assert a in s; s = s.replace(a, b, 1)
s = s.replace("list: ['partygoers', 'mannequins', 'crawler', 'redeyes'] },", "list: ['mannequins', 'crawler', 'redeyes'] },", 1)

a = "list: ['hatchlings', 'humans', 'doll', 'moths', 'mice', 'glowbugs', 'bellmouse'] }\n];"
b = ("list: ['hatchlings', 'humans', 'moths', 'mice', 'glowbugs'] },\n"
     "  { name: 'Protected', side: true, note: 'Nothing hunts these two. The Doll is your friend, and the Concierge keeps the Bellhop Mouse safe.', list: ['doll', 'bellmouse'] }\n];")
if b not in s:
    assert a in s; s = s.replace(a, b, 1)

# card outline for the Protected group
a = "var names = ['apex', 'tophunt', 'hunter', 'scav', 'prey'], cls = '';"
if a in s:
    s = s.replace(a, "var names = ['apex', 'tophunt', 'hunter', 'scav', 'prey', 'protect'], cls = '';", 1)

# food chain tab: the Protected group sits apart, with no arrow pointing up into the chain
a = "tiers += (i ? '<div class=\"farrow\">\\u{25B2}</div>' : '') + '<div class=\"ftier' + (t.apex ? ' apex' : '') + '\">"
b = "tiers += (i ? (t.side ? '<div class=\"fsep\">\\u{1F6E1}\\uFE0F Outside the food chain</div>' : '<div class=\"farrow\">\\u{25B2}</div>') : '') + '<div class=\"ftier' + (t.apex ? ' apex' : '') + (t.side ? ' protect' : '') + '\">"
if b not in s:
    assert a in s; s = s.replace(a, b, 1)

if '.bcard.protect' not in s:
    s = s.replace("#bestiary .bcard.prey { border: 4px solid #4fd18b; }",
                  "#bestiary .bcard.prey { border: 4px solid #4fd18b; }\n#bestiary .bcard.protect { border: 4px solid #60a5fa; }", 1)
    s = s.replace("#bestiary .ftier .fnote {",
                  "#bestiary .ftier.protect { border-color: #60a5fa; background: #0d1626; }\n#bestiary .ftier.protect h3 { color: #93c5fd; }\n"
                  "#bestiary .fsep { width: 100%; text-align: center; margin: 14px 0 6px; font: 700 .8rem Arial, sans-serif; color: #93c5fd; letter-spacing: .08em; text-transform: uppercase; }\n"
                  "#bestiary .ftier .fnote {", 1)
assert 'clown: 130' in s and "'poopers', 'partygoers'" in s and "name: 'Protected'" in s and '.bcard.protect' in s and '.fsep' in s and "'prey', 'protect'" in s
open(p, 'w', encoding='utf8').write(s)
print('ranks')
