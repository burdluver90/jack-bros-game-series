import os
GEN = os.path.dirname(os.path.abspath(__file__))
def patch(f, pairs):
    p = os.path.join(GEN, f); s = open(p, encoding='utf8').read()
    for a, b in pairs:
        if b in s: continue
        assert a in s, (f, a[:80]); s = s.replace(a, b, 1)
    open(p, 'w', encoding='utf8').write(s)
# the Bacteria is a side path you can skip
# absorbing the Bacteria makes the Concierge easier: it starts hurt, and the virus can hold it more often
patch('battle.twee', [
    ("  pad.data('hp', b.hp).data('guard', false)",
     "  var weak = b.boss && State.variables.virusStrong;\n"
     "  pad.data('hp', weak ? b.hp - 10 : b.hp).data('guard', false)"),
    ("  setup.drawBattle(pad, b.intro);\n};",
     "  setup.drawBattle(pad, b.intro + (weak ? '<br><b>The virus strikes first with its black tendrils! The Concierge staggers (-10).</b>' : ''));\n};"),
    ("pad.data('held', true).data('vcd', 4);", "pad.data('held', true).data('vcd', State.variables.virusStrong ? 2 : 4);"),
])
print('optional bacteria')
