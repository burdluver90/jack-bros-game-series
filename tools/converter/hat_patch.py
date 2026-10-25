import os
GEN = os.path.dirname(os.path.abspath(__file__))
p = os.path.join(GEN, 'hud.twee')
h = open(p, encoding='utf8').read()
if 'hat:' not in h:
    h = h.replace("  crowbar:{", "  hat:    { name: 'Party hat', short: 'Hat', icon: '\\u{1F973}', desc: 'Partygoers like hats. Maybe they will think you are one of them.' },\n  crowbar:{", 1)
h = h.replace("'dark-hall': 'Level 1 Dark Hall' };", "'dark-hall': 'Level 1 Dark Hall', 'virus-fun': 'Fun With The Virus' };", 1)
open(p, 'w', encoding='utf8').write(h)
print('hat:' in h, 'virus-fun' in h)
