import re, os
D = r'C:\Users\dahaw\OneDrive\Desktop\twine-games\part-3-1-backrooms\src\images'
defs = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pg_defs.txt'), encoding='utf8').read()

p = os.path.join(D, 'art_levelfun.svg'); s = open(p, encoding='utf8').read()
s = re.sub(r'    <!-- partygoer: tall yellow figure.*?</g>\n  </defs>', lambda m: defs + '  </defs>', s, flags=re.S)
s = re.sub(r'  <!-- partygoers gathered.*?</svg>', lambda m: '''  <!-- partygoers gathered around the cake -->
  <use href="#pgDetailed" transform="translate(300 700) scale(.55)" opacity=".85"/>
  <use href="#pgDetailed" transform="translate(1440 690) scale(.6)" opacity=".85"/>
  <use href="#pgDetailed" transform="translate(470 790) scale(.92)"/>
  <use href="#pgDetailed" transform="translate(1160 800) scale(1.0)"/>
</svg>''', s, flags=re.S)
open(p, 'w', encoding='utf8').write(s)

p = os.path.join(D, 'art_partychase.svg'); s = open(p, encoding='utf8').read()
s = re.sub(r'    <!-- partygoer mid-run.*?</g>\n    </g>\n  </defs>', lambda m: defs + '  </defs>', s, flags=re.S)
s = re.sub(r'  <!-- the crowd running at you -->.*?(?=  <!-- the music stopped -->)', lambda m: '''  <!-- the crowd running at you, leaning in -->
  <use href="#pgDetailed" transform="translate(1390 700) rotate(-8) scale(.5)" filter="url(#blur)" opacity=".8"/>
  <use href="#pgDetailed" transform="translate(1180 760) rotate(-10) scale(.7)" filter="url(#blur)"/>
  <use href="#pgDetailed" transform="translate(880 860) rotate(-12) scale(1.0)"/>
  <use href="#pgDetailed" transform="translate(470 960) rotate(-14) scale(1.35)"/>
''', s, flags=re.S)
open(p, 'w', encoding='utf8').write(s)

for f in ('art_levelfun.svg', 'art_partychase.svg'):
    t = open(os.path.join(D, f), encoding='utf8').read()
    print(f, 'detailed figures:', t.count('href="#pgDetailed"'), '| old figure left:', ('id="partygoer"' in t) or ('id="runner"' in t))
