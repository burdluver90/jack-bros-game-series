# the Bacteria scene can't kill you: the virus's rage makes it lunge and kill the Bacteria itself.
# the virus also tells you about virus hatchlings, prey you never see
import os, re
GEN = os.path.dirname(os.path.abspath(__file__))
D = r'C:\Users\dahaw\OneDrive\Desktop\twine-games\part-3-1-backrooms\src\images'
p = os.path.join(GEN, 'levels3.py'); s = open(p, encoding='utf8').read()

lines = s.split('\n')
start = next(i for i, l in enumerate(lines) if l.startswith("P.append(':: Bacteria Attack"))
end = next(i for i, l in enumerate(lines) if l.startswith("P.append(':: Bacteria Absorb"))
new_attack = [
    "P.append(':: Bacteria Attack\\n' + scene('art_bacteria', (4, 14, .75)) + '\\n' + story(",
    "    'The lights buzz louder. Something is standing at the end of the hall.',",
    "    'It is tall and thin and pitch black, with no face, and its body is made of jagged spikes. The Bacteria. It twitches, then sprints at you and wraps a black tendril around your leg.',",
    "    'The virus goes very still. Then every one of its tendrils starts to shake. \"Bacteria,\" it growls. \"My kind and its kind have been at war since the very first level. They hunted us when we were small. Not anymore.\"',",
    "    'Before you can even scream, the virus ROARS and lunges.') +",
    "    '\\n<div class=\"choices\">[[Watch the virus attack|Bacteria Absorb]]</div>\\n')",
]
lines[start:end] = new_attack
s = '\n'.join(lines)
# the virus tells you about the hatchlings after it wins
a = "Then it turns to you, calm again. \"Much better. Now I can fight with you.\"'"
b = ("Then it turns to you, calm again. \"Much better. Now I can fight with you.\"',\n"
     "    'It looks down the dark hall. \"When I was small, I had brothers and sisters. Hatchlings, tiny viruses that had not mutated yet. "
     "The Bacteria ate them like candy. A hatchling cannot fight back. Most of them never got as big as me.\" It goes quiet for a moment. "
     "\"Now you know why I hate them.\"'")
if b not in s:
    assert a in s; s = s.replace(a, b, 1)
# the Bacteria ending can't happen any more
s = re.sub(r"        \('Bacteria Ending', 'art_bacteria', \[.*?\]\),\n", "", s)
open(p, 'w', encoding='utf8').write(s)

# a silhouette for the hatchlings: you never actually see them
hatch = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 300">'
         '<rect width="400" height="300" fill="#0c0c0a"/>'
         '<g fill="#22221c">' + ''.join(
             f'<g transform="translate({x} {y}) scale({k})"><circle r="16"/>' +
             ''.join(f'<rect x="-2" y="-30" width="4" height="16" transform="rotate({a})"/>' for a in range(0, 360, 45)) + '</g>'
             for x, y, k in ((120, 170, 1), (200, 150, 1.3), (280, 175, .9), (165, 220, .7), (245, 225, .8))) + '</g>'
         '<text x="200" y="110" text-anchor="middle" font-family="Arial Black, Arial" font-size="56" fill="#3a3828">?</text>'
         '<text x="200" y="285" text-anchor="middle" font-family="Georgia" font-size="16" fill="#6b6850">only the virus has seen them</text></svg>')
open(os.path.join(D, 'art_p_hatch.svg'), 'w', encoding='utf8').write(hatch)

p = os.path.join(GEN, 'bestiary.twee'); s = open(p, encoding='utf8').read()
entry = ("  { id: 'hatchlings', name: 'Virus Hatchlings', tag: 'Prey (never seen)', friend: true, img: 'art_p_hatch',\n"
         "    seen: ['Bacteria Absorb'], deaths: [],\n"
         "    desc: 'Tiny viruses that have not mutated yet, like the virus was when it was small. You never see one: the virus told you about them. They cannot fight back, and the Bacteria eat them easily.',\n"
         "    tip: 'There is nothing you can do for them. But every Bacteria the virus kills is one less hunting the hatchlings.' },\n")
if "id: 'hatchlings'" not in s:
    s = s.replace("  { id: 'moths',", entry + "  { id: 'moths',", 1)
s = s.replace("deaths: ['You become lost becoming a (Q36)', 'Bacteria Ending']", "deaths: ['You become lost becoming a (Q36)']")
s = s.replace("list: ['doll', 'moths', 'mice', 'glowbugs', 'bellmouse']", "list: ['hatchlings', 'doll', 'moths', 'mice', 'glowbugs', 'bellmouse']")
s = s.replace("tip: 'Never wander off alone. Stay with the virus. If it attacks, let the virus absorb it: the virus gets its black tendrils and the Concierge fight gets easier.'",
              "tip: 'Never wander off alone. Stay with the virus. If one attacks, the virus will kill it and take its black tendrils, and the Concierge fight gets easier.'")
assert "'hatchlings', 'doll'" in s
open(p, 'w', encoding='utf8').write(s)
print('bacteria v3')
