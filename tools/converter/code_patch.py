# the hotel boiler code is new every run
import os
GEN = os.path.dirname(os.path.abspath(__file__))
def patch(f, pairs):
    p = os.path.join(GEN, f); s = open(p, encoding='utf8').read()
    for a, b in pairs:
        if b in s:
            continue
        assert a in s, (f, a[:80]); s = s.replace(a, b, 1)
    open(p, 'w', encoding='utf8').write(s)

patch('hud.twee', [
    ("  v.virusWith = false; v.power = false; v.codeTries = 0; v.knowCode = false; v.bell = 0;\n};",
     "  v.virusWith = false; v.power = false; v.codeTries = 0; v.knowCode = false; v.bell = 0;\n"
     "  v.boilerCode = setup.newCode();\n};\n"
     "/* the hotel boiler code: three different digits, new every run */\n"
     "setup.newCode = function () {\n"
     "  var d = [1, 2, 3, 4, 5, 6, 7, 8, 9], out = '';\n"
     "  for (var i = 0; i < 3; i++) { out += d.splice(Math.floor(Math.random() * d.length), 1)[0]; }\n"
     "  return out;\n"
     "};\n"
     "setup.boiler = function () { var v = State.variables; if (!v.boilerCode) { v.boilerCode = setup.newCode(); } return v.boilerCode; };\n"
     "setup.NUMWORDS = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'];\n"
     "setup.codeStr = function () { return setup.boiler().split('').join(' '); };\n"
     "setup.codeWords = function () {\n"
     "  var w = setup.boiler().split('').map(function (c) { return setup.NUMWORDS[+c]; }).join('... ') + '.';\n"
     "  return w.charAt(0).toUpperCase() + w.slice(1);\n"
     "};"),
    # the keypad checks against this run's code
    ("  var kind = pad.attr('data-kind') || 'digits', got = setup.normCode(kind, pad.find('.cin').val());",
     "  var kind = pad.attr('data-kind') || 'digits', got = setup.normCode(kind, pad.find('.cin').val());\n"
     "  var answer = pad.attr('data-answer') === '@boiler' ? setup.boiler() : pad.attr('data-answer');"),
    ("  if (got === setup.normCode(kind, pad.attr('data-answer'))) {", "  if (got === setup.normCode(kind, answer)) {"),
    ('data-fail="boiler" data-answer="417"></div> */', 'data-fail="boiler" data-answer="417 or @boiler"></div> */'),
])
patch('hotel.py', [
    ("'But as you spin you notice something: the dancers only ever step on three numbered tiles. Four... one... seven. Four... one... seven.')",
     "'But as you spin you notice something: the dancers only ever step on three numbered tiles. <<print setup.codeWords()>> <<print setup.codeWords()>>')"),
    ("'You creep up the steps. The sheet music has three big numbers written at the top: 4 1 7.',",
     "'You creep up the steps. The sheet music has three big numbers written at the top: <b><<print setup.codeStr()>></b>.',"),
    ('data-fail="boiler" data-answer="417"></div>', 'data-fail="boiler" data-answer="@boiler"></div>'),
    # the ballroom picture no longer has the old numbers drawn in
    ('<text x="2" y="-55" font-family="Georgia" font-size="12" text-anchor="middle" fill="#7a1f2b">4 1 7</text>', ''),
    ('  <!-- numbered dance-floor tiles -->\n  <g font-family="Georgia, serif" font-size="30" fill="#f6e27a" opacity=".35"><text x="520" y="860">4</text><text x="800" y="840">1</text><text x="1080" y="870">7</text></g>\n', ''),
])
# the playtest bot types this run's code
patch('bot.js', [
    ("pad.querySelector('.cin').value = right ? pad.getAttribute('data-answer') : '999';",
     "pad.querySelector('.cin').value = right ? (pad.getAttribute('data-answer') === '@boiler' ? S.setup.boiler() : pad.getAttribute('data-answer')) : '000';"),
])
print('random code patched')
