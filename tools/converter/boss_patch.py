# a harder Concierge: more health, two phases, and a telegraphed slam you have to block
import os
GEN = os.path.dirname(os.path.abspath(__file__))
def patch(f, pairs):
    p = os.path.join(GEN, f); s = open(p, encoding='utf8').read()
    for a, b in pairs:
        if b in s:
            continue
        assert a in s, (f, a[:80]); s = s.replace(a, b, 1)
    open(p, 'w', encoding='utf8').write(s)

patch('battle.twee', [
    ("concierge: { name: 'The Concierge', hp: 16, hit: 13,", "concierge: { name: 'The Concierge', hp: 40, hit: 14, boss: true,"),
    ("  pad.data('hp', b.hp).data('guard', false).data('stun', false).data('used', {});",
     "  pad.data('hp', b.hp).data('guard', false).data('stun', false).data('used', {}).data('turn', 0).data('phase', 1).data('charge', false);"),
    # bosses shrug off stuns
    ("    if (b.stun && w === b.stun) { pad.data('stun', true); }",
     "    if (b.stun && w === b.stun) { pad.data('stun', true); }\n"
     "    if (b.boss && pad.data('phase') === 2 && Math.random() < .25) { hp += 2; pad.data('hp', hp); log += 'Porcelain dust swirls back into the crack. <b>It heals 2.</b> '; }"),
    ("  /* the monster's turn */\n  if (pad.data('stun')) {",
     "  /* the monster's turn */\n"
     "  if (b.boss && setup.bossTurn(pad, b, act)) { return; }\n"
     "  if (pad.data('stun')) {"),
    ("$(document).on(':passagedisplay', function () { $('#passages .battle').each(",
     "/* the boss: at half health it cracks open and gets stronger, and every third turn it winds up a slam you must block */\n"
     "setup.bossTurn = function (pad, b, act) {\n"
     "  var v = State.variables, hp = pad.data('hp'), turn = pad.data('turn') + 1, log = pad.find('.blog').data('pending') || '';\n"
     "  pad.data('turn', turn);\n"
     "  var hard = setup.mode().label === 'Hard' ? 1.5 : 1, extra = '';\n"
     "  if (pad.data('phase') === 1 && hp <= b.hp / 2) {\n"
     "    pad.data('phase', 2); hp += 4; pad.data('hp', hp);\n"
     "    extra += '<br><b>CRACK.</b> Its porcelain face splits wide open. Something dark grins out from inside. It grows taller, and it heals 4. =) ';\n"
     "  }\n"
     "  var hit = Math.round((b.hit + (pad.data('phase') === 2 ? 4 : 0)) * hard);\n"
     "  if (pad.data('charge')) {\n"
     "    pad.data('charge', false);\n"
     "    var slam = act === 'block' ? Math.ceil(hit / 3) : hit * 2;\n"
     "    v.sanity = Math.max(0, v.sanity - slam);\n"
     "    extra += act === 'block' ? '<br>The silver tray SLAMS down on your guard. <b>-' + slam + ' sanity</b>. You held it!'\n"
     "                             : '<br>The silver tray SLAMS down on you. You did not block. <b>-' + slam + ' sanity</b>.';\n"
     "    pad.removeClass('hit'); void pad[0].offsetWidth; pad.addClass('hit');\n"
     "  } else if (turn % 3 === 0) {\n"
     "    pad.data('charge', true);\n"
     "    extra += '<br>It raises a silver tray high above its head. <b>\\u26A0\\uFE0F Block next turn!</b>';\n"
     "  } else {\n"
     "    var light = act === 'hit' && pad.data('lastw') && !setup.WSTATS[pad.data('lastw')].heavy;\n"
     "    if (light && Math.random() < .2) { extra += '<br>It swings, but you <b>dodge</b>!'; }\n"
     "    else { if (act === 'block') { hit = Math.ceil(hit / 2); } v.sanity = Math.max(0, v.sanity - hit); extra += '<br>It hits you. <b>-' + hit + ' sanity</b>.'; pad.removeClass('hit'); void pad[0].offsetWidth; pad.addClass('hit'); }\n"
     "  }\n"
     "  setup.hud();\n"
     "  var msg = pad.data('log') + extra;\n"
     "  if (v.sanity <= 0) { pad.find('.bacts').remove(); pad.find('.blog').html(msg); setTimeout(function () { Engine.play(b.lose); }, 900); return true; }\n"
     "  setup.drawBattle(pad, msg);\n"
     "  return true;\n"
     "};\n"
     "$(document).on(':passagedisplay', function () { $('#passages .battle').each("),
    # hand the player's log and weapon to the boss turn
    ("  if (b.boss && setup.bossTurn(pad, b, act)) { return; }",
     "  if (b.boss) { pad.data('log', log).data('lastw', w || ''); setup.bossTurn(pad, b, act); return; }"),
])
print('boss patched')

# the virus fights with you against the Concierge
patch('battle.twee', [
    ("  if (setup.has('almond')) { acts += '<a class=\"bbtn drink\"",
     "  if (b.boss && State.variables.virusWith) { var cd = pad.data('vcd') || 0; acts += cd > 0 ? '<a class=\"bbtn vir off\" data-act=\"wait\">\\u{1F9A0} Virus is resting (' + cd + ')</a>' : '<a class=\"bbtn vir\" data-act=\"virus\">\\u{1F9A0} Virus: hold it down</a>'; }\n"
     "  if (setup.has('almond')) { acts += '<a class=\"bbtn drink\""),
    ("  if (act === 'block') { pad.data('guard', true);",
     "  if (act === 'wait') { return; }\n"
     "  if (act === 'virus') { pad.data('held', true).data('vcd', 4); log = '<b>The virus wraps every tendril it has around the Concierge and holds it still!</b> '; }\n"
     "  if (act === 'block') { pad.data('guard', true);"),
    ("  if (hp <= 0) {\n    Object.keys(",
     "  if (b.boss && v.virusWith && act !== 'virus') {\n"
     "    var vd = v.virusStrong ? 3 : 2; hp -= vd; pad.data('hp', hp);\n"
     "    log += 'The virus lunges in beside you and hits it for <b>' + vd + '</b>. ';\n"
     "  }\n"
     "  if (b.boss && pad.data('vcd') > 0 && act !== 'virus') { pad.data('vcd', pad.data('vcd') - 1); }\n"
     "  if (hp <= 0) {\n    Object.keys("),
    ("  if (pad.data('charge')) {\n    pad.data('charge', false);",
     "  if (pad.data('held')) {\n"
     "    pad.data('held', false);\n"
     "    extra += pad.data('charge') ? '<br>The silver tray drops out of its hands. The virus saved you from the slam!' : '<br>It struggles in the tendrils and cannot hit you this turn.';\n"
     "    pad.data('charge', false);\n"
     "  } else if (pad.data('charge')) {\n    pad.data('charge', false);"),
])
print('virus helps')
