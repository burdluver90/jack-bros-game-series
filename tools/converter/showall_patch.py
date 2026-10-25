# a "Show everything" toggle in the bestiary: reveals every creature, picture and tip without changing your saved progress
import os
GEN = os.path.dirname(os.path.abspath(__file__))
p = os.path.join(GEN, 'bestiary.twee'); s = open(p, encoding='utf8').read()
pairs = [
    ("setup.openBestiary = function () {\n  var b = setup.best(), found = 0, cards = '';",
     "setup.bestView = function () {\n"
     "  if (!setup.showAll) { return setup.best(); }\n"
     "  var all = {}; setup.BEASTS.forEach(function (x) { all[x.id] = { seen: true, form2: true, beaten: true }; }); return all;\n"
     "};\n"
     "setup.openBestiary = function () {\n  var b = setup.bestView(), found = 0, cards = '';"),
    ("setup.openFoodChain = function () {\n  var b = setup.best(), tiers = '';",
     "setup.openFoodChain = function () {\n  var b = setup.bestView(), tiers = '';"),
    ("<button class=\"btab\" data-t=\"chain\">\\u{1F356} Food chain</button></div>' +",
     "<button class=\"btab\" data-t=\"chain\">\\u{1F356} Food chain</button><button class=\"bshow' + (setup.showAll ? ' on' : '') + '\">\\u{1F441}\\u{FE0F} ' + (setup.showAll ? 'Hide what I have not found' : 'Show everything') + '</button></div>' +"),
    ("$(document).on('click', '#bestiary .bclose',",
     "$(document).on('click', '#bestiary .bshow', function () { setup.showAll = !setup.showAll; setup.openBestiary(); });\n"
     "$(document).on('click', '#bestiary .bclose',"),
    ("#bestiary .btab.on {",
     "#bestiary .bshow { margin-left: auto; padding: .35em 1em; border-radius: 99px; border: 1px solid #4a4528; background: #16140c; color: #9db8ff; cursor: pointer; }\n"
     "#bestiary .bshow.on { border-color: #9db8ff; background: #101a30; }\n"
     "#bestiary .btab.on {"),
]
for a, b2 in pairs:
    if b2 in s: continue
    assert a in s, a[:70]; s = s.replace(a, b2, 1)
open(p, 'w', encoding='utf8').write(s)
print('show all')
