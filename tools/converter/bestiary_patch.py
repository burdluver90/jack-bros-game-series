import os
GEN = os.path.dirname(os.path.abspath(__file__))
def patch(f, pairs):
    p = os.path.join(GEN, f); s = open(p, encoding='utf8').read()
    for a, b in pairs:
        if b in s:
            continue
        assert a in s, (f, a[:80]); s = s.replace(a, b, 1)
    open(p, 'w', encoding='utf8').write(s)

# bestiary button in the hotbar
patch('hud.twee', [
    ("'<button class=\"hum' + (setup.hum && setup.hum.on ? ' on' : '') + '\" title=\"Fluorescent light hum\">'",
     "'<button class=\"bestbtn\" title=\"Bestiary\">\\u{1F4D6} Bestiary</button><button class=\"hum' + (setup.hum && setup.hum.on ? ' on' : '') + '\" title=\"Fluorescent light hum\">'"),
])
# beating a monster in battle marks it beaten
patch('battle.twee', [
    ("    setup.hud(); pad.find('.bacts').remove();\n    pad.find('.blog').html(log + '<br><b>You beat the '",
     "    setup.hud(); pad.find('.bacts').remove();\n    setup.BEASTS.forEach(function (x) { if (x.battle === pad.attr('data-b')) { setup.bestMark(x.id, 'beaten'); } });\n    pad.find('.blog').html(log + '<br><b>You beat the '"),
])
# a bestiary link on the title screen, and include the new passages
patch('drive31.py', [
    ("  '</div>')\ndef KEEP(label, item, to):",
     "  '</div><p class=\"bestlink\"><a href=\"#\">\\U0001F4D6 Open the bestiary</a></p>')\ndef KEEP(label, item, to):"),
    ("open(os.path.join(GEN,'battle.twee'),encoding='utf8').read()}",
     "open(os.path.join(GEN,'battle.twee'),encoding='utf8').read()+chr(10)+open(os.path.join(GEN,'bestiary.twee'),encoding='utf8').read()}"),
])
print('bestiary patched')
