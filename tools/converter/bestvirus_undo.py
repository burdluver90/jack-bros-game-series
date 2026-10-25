# undo the virus tendril overlay; the bestiary keeps the son's own virus pictures
import os, re
GEN = os.path.dirname(os.path.abspath(__file__))
p = os.path.join(GEN, 'bestiary.twee'); s = open(p, encoding='utf8').read()
s = s.replace(" seen3: ['Bacteria Absorb'],", "")
s = re.sub(r"\n    if \(x\.seen3 && .*?\n", "\n", s)
s = re.sub(r" \+ \(e\.form3 \? '<svg class=\"btend\".*?</svg>' : ''\)", "", s)
s = s.replace(" + (e.form3 && x.desc3 ? ' ' + x.desc3 : '')", "")
s = re.sub(r"    desc3: .*?\n", "", s)
s = re.sub(r"#bestiary \.bcard \.bimg \{ position: relative; \}\n#bestiary \.bcard \.bimg \.btend .*?\n", "", s)
assert 'form3' not in s and 'btend' not in s and 'desc3' not in s
open(p, 'w', encoding='utf8').write(s)
print('undone')
