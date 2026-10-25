# swap newer emoji (shown as a box with a code on some computers) for ones every system has
import os, re
GEN = os.path.dirname(os.path.abspath(__file__))
p = os.path.join(GEN, 'hud.twee'); s = open(p, encoding='utf8').read()
NEW = {
    'sword': r"'⚔️'",        # crossed swords
    'roomkey': r"'\u{1F511}'",          # key
    'brasskey': r"'\u{1F510}'",         # lock with key
    'axe': r"'⛏️'",           # pick
    'hat': r"'\u{1F389}'",              # party popper
    'wrench': r"'\u{1F529}'",           # nut and bolt
}
for item, icon in NEW.items():
    s, n = re.subn(r"(\n  " + item + r":\s*\{[^\n]*?icon: )'[^']*'", lambda m: m.group(1) + icon, s, count=1)
    assert n == 1, item
s = s.replace("setup.toast('Picked up: ' + setup.ITEMS[id].name);", "setup.toast('Picked up: ' + setup.ITEMS[id].icon + ' ' + setup.ITEMS[id].name);", 1)
open(p, 'w', encoding='utf8').write(s)
print('icons swapped')
