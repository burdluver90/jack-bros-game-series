import os, re
p = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'levels3.py')
s = open(p, encoding='utf8').read()
bad = re.search(r'\n    "\n<p>Down the hall.*?</div>\n"\)', s, re.S)
assert bad, 'not found'
good = ('\n    "\\n<p>Down the hall, the lights are buzzing louder than they should.</p>" + '
        'f"\\n<div class=\\"choices\\">[[Check out the buzzing lights|Bacteria Attack]][[Keep going|{END}]]</div>\\n")')
s = s[:bad.start()] + good + s[bad.end():]
open(p, 'w', encoding='utf8').write(s)
print('fixed')
