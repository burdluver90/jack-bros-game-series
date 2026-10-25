# the Partypoopers and the Partygoers are at war
import os
GEN = os.path.dirname(os.path.abspath(__file__))
p = os.path.join(GEN, 'levels3.py'); s = open(p, encoding='utf8').read()
a = 'We cannot STAND the Partygoers."'
b = 'We are at WAR with the Partygoers. We have been for as long as anyone can remember."'
if b not in s:
    assert a in s; s = s.replace(a, b, 1)
open(p, 'w', encoding='utf8').write(s)
p = os.path.join(GEN, 'bestiary.twee'); s = open(p, encoding='utf8').read()
a = "because they HATE the Partygoers and want nothing to do with their party."
b = "because the Partypoopers and the Partygoers have been at war for as long as anyone can remember."
if b not in s:
    assert a in s; s = s.replace(a, b, 1)
open(p, 'w', encoding='utf8').write(s)
print('war')
