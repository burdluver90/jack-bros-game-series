import os
GEN = os.path.dirname(os.path.abspath(__file__))
p = os.path.join(GEN, 'drive31.py'); s = open(p, encoding='utf8').read()
old = " 83:{'story':['To be continued...','Part 4 is coming in a month.'],'buttons':[('Back to the title',1)]},"
new = (" 83:{'story':[],'raw_story':'<div class=\"escape\"><h2>ESCAPE SUCCESSFUL</h2><p class=\"found\">You have found your way out.</p>"
       "<p class=\"tbc\">To be continued... Part 4 is coming in a month.</p></div>','buttons':[('Back to the title',1)]},")
if new not in s:
    assert old in s; s = s.replace(old, new, 1)
# keep the passage name the other levels link to
old2 = "'exact':{1:'Start'}"
if "83:'To be continued... (Q83)'" not in s:
    assert old2 in s; s = s.replace(old2, "'exact':{1:'Start',83:'To be continued... (Q83)'}", 1)
open(p, 'w', encoding='utf8').write(s)

h = os.path.join(GEN, 'hud.twee'); t = open(h, encoding='utf8').read()
css = (".escape { text-align: center; padding: 30px 10px; }\n"
       ".escape h2 { margin: 0 0 14px; font: 900 clamp(2rem, 7vw, 3.6rem)/1.05 \"Arial Black\", Arial, sans-serif; letter-spacing: .04em; color: #4ade80;\n"
       "  text-shadow: 0 0 18px rgba(74,222,128,.55), 0 0 2px #052e16; animation: escapeglow 2.4s ease-in-out infinite; }\n"
       ".escape .found { font-size: 1.35rem; color: #f8f6ee; margin: 0 0 26px; }\n"
       ".escape .tbc { font-style: italic; color: rgba(230,220,170,.7); }\n"
       "@keyframes escapeglow { 0%, 100% { text-shadow: 0 0 18px rgba(74,222,128,.55), 0 0 2px #052e16; } 50% { text-shadow: 0 0 34px rgba(74,222,128,.9), 0 0 2px #052e16; } }\n")
if '.escape h2' not in t:
    t = t.replace(".codepad .chint {", css + ".codepad .chint {", 1)
open(h, 'w', encoding='utf8').write(t)
print('ending patched')
