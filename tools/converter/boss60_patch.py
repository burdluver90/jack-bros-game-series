# Concierge has 60 health; every turn the virus either holds it still (then rests a turn) or whips it.
# the virus bows when it walks into the hotel
import os, re
GEN = os.path.dirname(os.path.abspath(__file__))

p = os.path.join(GEN, 'battle.twee'); s = open(p, encoding='utf8').read()
s = s.replace("name: 'The Concierge', hp: 40,", "name: 'The Concierge', hp: 60,", 1)
# no more manual virus button: the virus acts on its own
s = re.sub(r"  if \(b\.boss && State\.variables\.virusWith\) \{ var cd = pad\.data\('vcd'\).*?\n", "", s, count=1)
old = ("  if (b.boss && v.virusWith && act !== 'virus') {\n"
       "    var vd = v.virusStrong ? 3 : 2; hp -= vd; pad.data('hp', hp);\n"
       "    log += 'The virus lunges in beside you and hits it for <b>' + vd + '</b>. ';\n"
       "  }\n"
       "  if (b.boss && pad.data('vcd') > 0 && act !== 'virus') { pad.data('vcd', pad.data('vcd') - 1); }\n")
new = ("  /* the virus's own turn: rest if it held the Concierge last turn, otherwise hold it (always when the tray is raised) or whip it */\n"
       "  if (b.boss && v.virusWith) {\n"
       "    if (pad.data('vrest')) { pad.data('vrest', false); log += 'The virus is catching its breath this turn. '; }\n"
       "    else if (pad.data('charge') || Math.random() < .35) {\n"
       "      pad.data('held', true).data('vrest', true);\n"
       "      log += '<b>The virus wraps every tendril it has around the Concierge and holds it still!</b> It will have to rest next turn. ';\n"
       "    } else {\n"
       "      var vd = v.virusStrong ? 4 : 3; hp -= vd; pad.data('hp', hp);\n"
       "      log += 'The virus whips it with its tendrils for <b>' + vd + '</b>. ';\n"
       "    }\n"
       "  }\n")
if new not in s:
    assert old in s; s = s.replace(old, new, 1)
s = s.replace("pad.data('hp', weak ? b.hp - 10 : b.hp).data('guard', false)", "pad.data('hp', weak ? b.hp - 10 : b.hp).data('vrest', false).data('held', false).data('guard', false)", 1)
assert "hp: 60" in s and "bbtn vir" not in s
open(p, 'w', encoding='utf8').write(s)

p = os.path.join(GEN, 'hotel.py'); s = open(p, encoding='utf8').read()
a = "V('The virus keeps low, sniffing the carpet. \"Find the brass key,\" it whispers. \"And find out the code.\"'"
b = ("V('As soon as it is through the door, the virus stops and bows low toward the reception desk. \"Manners,\" it whispers. \"The Concierge is always watching.\" "
     "Then it keeps low, sniffing the carpet. \"Find the brass key. And find out the code.\"'")
if b not in s:
    assert a in s; s = s.replace(a, b, 1)
open(p, 'w', encoding='utf8').write(s)
print('boss 60')
