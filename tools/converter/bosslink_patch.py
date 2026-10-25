# index.html#concierge jumps straight into the Concierge battle with a sword and 3 almond water
import os
GEN = os.path.dirname(os.path.abspath(__file__))
p = os.path.join(GEN, 'hud.twee'); s = open(p, encoding='utf8').read()
a = "  var dest = setup.JUMPS[location.hash.slice(1)];\n  if (dest) {"
b = ("  var dest = setup.JUMPS[location.hash.slice(1)];\n"
     "  if (location.hash === '#concierge') {\n"
     "    setTimeout(function () {\n"
     "      setup.reset(); var v = State.variables;\n"
     "      v.inv = ['sword', 'almond', 'almond', 'almond']; v.virusWith = true;\n"
     "      Engine.play('Battle Concierge');\n"
     "    }, 0);\n"
     "  }\n"
     "  else if (dest) {")
if b not in s:
    assert a in s; s = s.replace(a, b, 1)
open(p, 'w', encoding='utf8').write(s)
print('boss link')
