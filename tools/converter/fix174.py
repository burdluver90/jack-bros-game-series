import os
p = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'levels3.py')
s = open(p, encoding='utf8').read()
a = "\n    'The lights buzz louder. Something is standing at the end of the hall.',"
if "P.append(':: Bacteria Attack" not in s:
    s = s.replace(a, "\nP.append(':: Bacteria Attack\\n' + scene('art_bacteria', (4, 14, .75)) + '\\n' + story(" + a, 1)
open(p, 'w', encoding='utf8').write(s)
print('fixed')
