import os
GEN = os.path.dirname(os.path.abspath(__file__))
p = os.path.join(GEN, 'hud.twee')
h = open(p, encoding='utf8').read()
if 'flashlight:' not in h:
    h = h.replace("  crowbar:{", "  flashlight: { name: 'Flashlight', short: 'Light', icon: '\\u{1F526}', desc: 'Some things in the dark hate light.' },\n  crowbar:{", 1)
h = h.replace("'virus-fun': 'Fun With The Virus' };", "'virus-fun': 'Fun With The Virus', 'level-2': 'Level 2 Pipe Dreams', 'level-4': 'Level 4 Abandoned Office', 'level-6': 'Level 6 Lights Out', 'level-run': 'Level Run For Your Life' };", 1)
open(p, 'w', encoding='utf8').write(h)
print('flashlight:' in h, 'level-run' in h)
