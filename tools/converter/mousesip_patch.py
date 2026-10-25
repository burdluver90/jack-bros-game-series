# the Bellhop Mouse wants a sip of almond water: it drinks 3/4 of a bottle and gives you the whole boiler code
import os
GEN = os.path.dirname(os.path.abspath(__file__))
p = os.path.join(GEN, 'bestiary.twee'); s = open(p, encoding='utf8').read()
pairs = [
    ("then points its nose at the ballroom.'; } }\n};",
     "then points its nose at the ballroom.'; },\n"
     "    /* a second choice: share your almond water */\n"
     "    btn2: 'Give the mouse a sip of almond water', need2: function () { return setup.has('almond'); },\n"
     "    use2: function () {\n"
     "      var v = State.variables, c = setup.boiler();\n"
     "      v.inv.splice(v.inv.indexOf('almond'), 1);\n"
     "      v.sanity = Math.min(100, v.sanity + 25);\n"
     "      return 'The mouse squeaks happily and drinks... and drinks... and drinks. It gulps down three quarters of the bottle! You finish the last little bit yourself (<b>+25 sanity</b> instead of a full bottle). '\n"
     "        + 'Then the mouse scratches three numbers into the carpet, one after another: <b>' + c.split('').join(' ') + '</b>. The whole boiler code.';\n"
     "    } }\n};"),
    ("  if (!v.preyUsed[p.id]) {\n"
     "    $('<a class=\"preybtn\">\\u{1F43E} ' + p.btn + '</a>').on('click', function () {\n"
     "      v.preyUsed[p.id] = true; box.find('.preybtn').remove();\n"
     "      box.append('<p class=\"preyout\">' + p.use() + '</p>'); setup.hud();\n"
     "    }).appendTo(box);\n"
     "  }",
     "  if (!v.preyUsed[p.id]) {\n"
     "    $('<a class=\"preybtn\">\\u{1F43E} ' + p.btn + '</a>').on('click', function () {\n"
     "      v.preyUsed[p.id] = true; box.find('.preybtn').remove();\n"
     "      box.append('<p class=\"preyout\">' + p.use() + '</p>'); setup.hud();\n"
     "    }).appendTo(box);\n"
     "    if (p.btn2 && p.need2()) {\n"
     "      $('<a class=\"preybtn\">\\u{1F4A7} ' + p.btn2 + '</a>').on('click', function () {\n"
     "        v.preyUsed[p.id] = true; box.find('.preybtn').remove();\n"
     "        box.append('<p class=\"preyout\">' + p.use2() + '</p>'); setup.hud();\n"
     "      }).appendTo(box);\n"
     "    }\n"
     "  }"),
    ("tip: 'Be kind to it. It scratches part of the boiler code into the carpet for you.'",
     "tip: 'Be kind to it and it scratches the first number of the boiler code into the carpet. Share a sip of almond water and it gives you the whole code, but it drinks three quarters of the bottle.'"),
    (".preybox .preyout { color: #bbf7d0; }", ".preybox .preyout { color: #bbf7d0; }\n.preybox .preybtn + .preybtn { margin-left: 8px; }"),
]
for a, b in pairs:
    if b in s: continue
    assert a in s, a[:60]; s = s.replace(a, b, 1)
open(p, 'w', encoding='utf8').write(s)
print('mouse sip')
