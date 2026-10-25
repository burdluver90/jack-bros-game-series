# one Bacteria entry: the son's picture, unlocked by his slide or the new attack
import os, re
GEN = os.path.dirname(os.path.abspath(__file__))
p = os.path.join(GEN, 'bestiary.twee'); s = open(p, encoding='utf8').read()
s = re.sub(r"  \{ id: 'bacteria', name: 'The Bacteria', tag: 'After Level !'.*?\},\n", "", s, flags=re.S)
old = ("    seen: [\"What's this Bacteria (Q5)\"], deaths: ['You become lost becoming a (Q36)'],\n"
       "    desc: 'Bacteriform life studied by the Async Research Institute. Bashful, but it hunts anyone who gets lost on their own.',\n"
       "    tip: 'Never wander off alone. Stay with the virus.' },")
new = ("    seen: [\"What's this Bacteria (Q5)\", 'Bacteria Attack'], deaths: ['You become lost becoming a (Q36)', 'Bacteria Ending'], beat: ['Bacteria Absorb'],\n"
       "    desc: 'Bacteriform life studied by the Async Research Institute. Bashful, but it hunts anyone who gets lost on their own. Cut one of its black tendrils and two grow back.',\n"
       "    tip: 'Never wander off alone. Stay with the virus. If it attacks, let the virus absorb it: the virus gets its black tendrils and the Concierge fight gets easier.' },")
if new not in s:
    assert old in s; s = s.replace(old, new, 1)
assert s.count("id: 'bacteria'") == 1
open(p, 'w', encoding='utf8').write(s)
print('merged')
