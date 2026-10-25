import os
GEN = os.path.dirname(os.path.abspath(__file__))
p = os.path.join(GEN, 'bestiary.twee'); s = open(p, encoding='utf8').read()
pairs = [
    ("'</span><h3>' + x.name + '</h3><p>' + x.desc + '</p>' +",
     "'</span><h3>' + x.name + '</h3><p>' + x.desc + (e.form3 && x.desc3 ? ' ' + x.desc3 : '') + '</p>' +"),
    ("    tip: 'Do not fight it and do not run. Listen to it, and follow it.' },",
     "    desc3: 'After absorbing the Bacteria it grew three pitch-black, spiky tendrils, and it hits much harder in a fight.',\n"
     "    tip: 'Do not fight it and do not run. Listen to it, and follow it.' },"),
    ("#bestiary .bcard .bimg img { width: 100%; height: 100%; object-fit: contain; }",
     "#bestiary .bcard .bimg img { width: 100%; height: 100%; object-fit: contain; }\n"
     "#bestiary .bcard .bimg { position: relative; }\n"
     "#bestiary .bcard .bimg .btend { position: absolute; inset: 0; width: 100%; height: 100%; pointer-events: none; }"),
]
for a, b in pairs:
    if b in s: continue
    assert a in s, a[:60]; s = s.replace(a, b, 1)
open(p, 'w', encoding='utf8').write(s)
print('ok')
