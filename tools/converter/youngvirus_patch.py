# its own bestiary page for the virus before its mutation
import os
GEN = os.path.dirname(os.path.abspath(__file__))
p = os.path.join(GEN, 'bestiary.twee'); s = open(p, encoding='utf8').read()
entry = ("  { id: 'virusyoung', name: 'The Virus (before mutation)', tag: 'Hunter', friend: true, img: 'img_Qimage26',\n"
         "    seen: ['Fight (Q9)', \"Wait don't run (Q11)\", 'I am a virus basically (Q12)'], deaths: [],\n"
         "    desc: 'What the virus looked like when you first met it: smaller, quieter, and nowhere near the top of the food chain. "
         "At this stage a virus is almost the same as a bacteria, and the two are close to an even match. "
         "The Bacteria is just slightly stronger, because its tendrils are a little harder. But one good hit and they are equal again.',\n"
         "    tip: 'It is not the monster it looks like. Stay close to it, and one day it will be strong enough to protect you.' },\n")
if "id: 'virusyoung'" not in s:
    s = s.replace("  { id: 'bacteria',", entry + "  { id: 'bacteria',", 1)
# the food chain uses the new page for the pre-mutation virus
s = s.replace("list: ['bacteria', 'virus1',", "list: ['bacteria', 'virusyoung',", 1)
s = s.replace("name = id === 'virus1' ? 'The Virus (before mutation)' :", "name = id === 'virusyoung' ? x.name :", 1)
assert "'bacteria', 'virusyoung'" in s
open(p, 'w', encoding='utf8').write(s)
print('young virus')
