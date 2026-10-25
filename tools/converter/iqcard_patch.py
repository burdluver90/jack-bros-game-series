# show each creature's IQ on its bestiary card too
import os
GEN = os.path.dirname(os.path.abspath(__file__))
p = os.path.join(GEN, 'bestiary.twee'); s = open(p, encoding='utf8').read()
a = "'<span class=\"btag\">' + x.tag + '</span><h3>' + x.name + '</h3><p>' + x.desc + '</p>' +"
b = "'<span class=\"btag\">' + x.tag + '</span><h3>' + x.name + '</h3>' + setup.iqTag(x.id) + '<p>' + x.desc + '</p>' +"
if b not in s:
    assert a in s; s = s.replace(a, b, 1)
a2 = "setup.openBestiary = function () {"
b2 = ("/* IQ badge on a bestiary card (the main virus page uses its mutated IQ) */\n"
      "setup.iqTag = function (id) { var n = setup.IQ && setup.IQ[id === 'virus' ? 'virus2' : id]; return n === undefined ? '' : '<div class=\"biq\">\\u{1F9E0} IQ ' + n + '</div>'; };\n"
      "setup.openBestiary = function () {")
if 'setup.iqTag' not in s:
    s = s.replace(a2, b2, 1)
if '.bcard .biq' not in s:
    s = s.replace("#bestiary .bcard .btip {", "#bestiary .bcard .biq { font: 700 .8rem Arial, sans-serif; color: #9db8ff; letter-spacing: .04em; }\n#bestiary .bcard .btip {", 1)
assert 'setup.iqTag' in s and '.bcard .biq' in s
open(p, 'w', encoding='utf8').write(s)
print('iq cards')
