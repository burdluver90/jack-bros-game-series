import os
GEN = os.path.dirname(os.path.abspath(__file__))
def patch(f, pairs):
    p = os.path.join(GEN, f); s = open(p, encoding='utf8').read()
    for a, b in pairs:
        if b in s:
            continue
        assert a in s, (f, a[:70]); s = s.replace(a, b, 1)
    open(p, 'w', encoding='utf8').write(s)

patch('modes.py', [
    ("def apply(text):",
     "# the few hints Hard mode still shows: the ones that stop a run from being unwinnable or a total guess\n"
     "HARD_TOO = {\"It's a sword! (Q42)\", 'How can i escape (Q53)', 'Left (Q35)', 'Run (Q49)',\n"
     "            'Level 6 Lights Out', 'Hotel Front Desk', 'Hotel Floor 3', 'Hotel Boiler Room'}\n\n"
     "def apply(text):"),
    ("        line = f'<<if setup.mode().hints>><p class=\"modehint\">{hint}</p><</if>>'",
     "        line = (f'<p class=\"modehint hardtoo\">{hint}</p>' if title in HARD_TOO\n"
     "                else f'<<if setup.mode().hints>><p class=\"modehint\">{hint}</p><</if>>')"),
])
patch('hud.twee', [
    ("if (!setup.mode().hints) { $('#passages .modehint').remove(); }",
     "if (!setup.mode().hints) { $('#passages .modehint:not(.hardtoo)').remove(); }"),
])
patch('drive31.py', [
    ("one wrong code is the end, and there are no hints. Good luck.",
     "one wrong code is the end, and only a few hints. Good luck."),
])
print('hard hints patched')
