import os
GEN = os.path.dirname(os.path.abspath(__file__))
D = r'C:\Users\dahaw\OneDrive\Desktop\twine-games\part-3-1-backrooms\src\images'
PG = open(os.path.join(GEN, 'pg_defs.txt'), encoding='utf8').read()

ROOM_DEFS = '''    <pattern id="paper" width="80" height="80" patternUnits="userSpaceOnUse">
      <rect width="80" height="80" fill="#d9c45c"/>
      <path d="M0 40 Q20 25 40 40 T80 40" stroke="#c4ad47" stroke-width="4" fill="none"/>
      <circle cx="40" cy="12" r="4" fill="#c4ad47"/><circle cx="0" cy="68" r="4" fill="#c4ad47"/><circle cx="80" cy="68" r="4" fill="#c4ad47"/>
    </pattern>
    <linearGradient id="carpet" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#8f7a3a"/><stop offset="1" stop-color="#5e4f22"/></linearGradient>
    <radialGradient id="shine" cx=".35" cy=".3" r=".6"><stop offset="0" stop-color="#fff" stop-opacity=".6"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></radialGradient>
    <g id="balloon"><ellipse rx="42" ry="52"/><ellipse rx="42" ry="52" fill="url(#shine)"/><path d="M0 52 l-6 10 h12 z"/><path d="M0 62 q14 60 -6 120 q-14 60 8 120" stroke="#333" stroke-width="2" fill="none"/></g>
    <filter id="glow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="6" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
    <filter id="blur"><feGaussianBlur stdDeviation="3"/></filter>
    <radialGradient id="vign" cx=".5" cy=".5" r=".75"><stop offset=".55" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".6"/></radialGradient>
'''

# the virus after its mutation: a tangle of dark tendrils with a petal head and glowing green veins
# feet at 0,0, about 620 units tall. original drawing.
VIRUS = '''    <g id="virus">
      <ellipse cx="0" cy="6" rx="120" ry="18" fill="#000" opacity=".35"/>
      <g fill="none" stroke-linecap="round" stroke="#15110c">
        <!-- legs: bundles of twisted strands -->
        <path d="M-20 -250 C-40 -180 -30 -120 -60 -60 S-70 -10 -90 0" stroke-width="16"/>
        <path d="M-10 -250 C-30 -170 -10 -110 -40 -50 S-40 -10 -60 2" stroke-width="10"/>
        <path d="M20 -250 C40 -180 30 -120 60 -60 S70 -10 92 0" stroke-width="16"/>
        <path d="M10 -250 C34 -170 14 -110 44 -50 S44 -10 64 2" stroke-width="10"/>
        <!-- body: knotted trunk -->
        <path d="M-30 -460 C-60 -400 -10 -330 -30 -250" stroke-width="22"/>
        <path d="M30 -460 C60 -400 10 -330 30 -250" stroke-width="22"/>
        <path d="M0 -470 C-24 -390 24 -330 0 -250" stroke-width="14"/>
        <path d="M-30 -420 C0 -400 10 -380 34 -390 M-34 -330 C0 -350 20 -320 36 -330 M-28 -290 C0 -300 14 -280 30 -290" stroke-width="7"/>
        <!-- arms: long, splitting into claws -->
        <path d="M-30 -450 C-110 -430 -150 -360 -190 -270 S-220 -190 -230 -150" stroke-width="16"/>
        <path d="M-230 -150 l-30 40 M-230 -150 l-6 52 M-230 -150 l22 44" stroke-width="7"/>
        <path d="M30 -450 C110 -430 150 -360 190 -270 S220 -190 230 -150" stroke-width="16"/>
        <path d="M230 -150 l30 40 M230 -150 l6 52 M230 -150 l-22 44" stroke-width="7"/>
        <!-- mutation: extra arms and whipping tendrils -->
        <path d="M-20 -380 C-120 -380 -200 -440 -270 -520" stroke-width="9"/>
        <path d="M20 -380 C120 -380 200 -440 270 -520" stroke-width="9"/>
        <path d="M-270 -520 q-30 -10 -40 -40 M270 -520 q30 -10 40 -40" stroke-width="5"/>
        <path d="M-10 -300 C-90 -280 -130 -220 -160 -140" stroke-width="6"/>
        <path d="M10 -300 C90 -280 130 -220 160 -140" stroke-width="6"/>
        <!-- sensory hairs -->
        <path d="M-60 -400 l-14 -12 M-48 -350 l-16 -6 M60 -400 l14 -12 M48 -350 l16 -6 M-120 -330 l-10 -14 M120 -330 l10 -14 M-180 -280 l-16 -4 M180 -280 l16 -4" stroke-width="2.5"/>
      </g>
      <!-- glowing mutation veins -->
      <g fill="none" stroke="#7dff6b" stroke-linecap="round" filter="url(#glow)" opacity=".9">
        <path d="M-6 -460 C-20 -390 16 -330 -4 -260" stroke-width="4"/>
        <path d="M-30 -445 C-100 -425 -140 -360 -180 -280" stroke-width="3"/>
        <path d="M30 -445 C100 -425 140 -360 180 -280" stroke-width="3"/>
        <path d="M-16 -250 C-30 -180 -24 -120 -50 -60" stroke-width="3"/>
        <path d="M16 -250 C30 -180 24 -120 50 -60" stroke-width="3"/>
        <path d="M-20 -384 C-110 -384 -190 -440 -262 -516 M20 -384 C110 -384 190 -440 262 -516" stroke-width="2.5"/>
      </g>
      <!-- petal head with a maw in the folds -->
      <g transform="translate(0 -520)">
        <path d="M-90 10 C-120 -40 -70 -90 -30 -70 C-30 -120 30 -120 30 -70 C70 -90 120 -40 90 10 C120 50 60 80 30 50 C20 80 -20 80 -30 50 C-60 80 -120 50 -90 10 Z" fill="#1a140e" stroke="#0b0805" stroke-width="4"/>
        <path d="M-60 0 C-80 -30 -50 -60 -24 -46 M60 0 C80 -30 50 -60 24 -46 M-20 30 C-10 50 10 50 20 30" stroke="#3a2e1f" stroke-width="5" fill="none"/>
        <path d="M-36 6 Q0 40 36 6 Q0 22 -36 6 Z" fill="#7dff6b" filter="url(#glow)"/>
        <g fill="#e9ffe0"><path d="M-26 10 l5 12 l5 -11 z"/><path d="M-8 15 l5 12 l5 -12 z"/><path d="M10 15 l5 12 l5 -12 z"/><path d="M24 10 l-3 11 l-6 -9 z"/></g>
        <circle cx="-40" cy="-26" r="6" fill="#7dff6b" filter="url(#glow)"/><circle cx="40" cy="-26" r="6" fill="#7dff6b" filter="url(#glow)"/>
        <circle cx="-14" cy="-50" r="4" fill="#7dff6b" filter="url(#glow)"/><circle cx="14" cy="-50" r="4" fill="#7dff6b" filter="url(#glow)"/>
      </g>
    </g>
'''

def room(extra_bg=''):
    return '''  <rect width="1600" height="640" fill="url(#paper)"/>
  <rect y="640" width="1600" height="260" fill="url(#carpet)"/>
  <rect y="630" width="1600" height="14" fill="#7a6630"/>
  <g fill="none" stroke-width="10" stroke-linecap="round">
    <path d="M0 40 Q200 140 400 40 T800 40 T1200 40 T1600 40" stroke="#e8443a"/>
    <path d="M0 70 Q200 170 400 70 T800 70 T1200 70 T1600 70" stroke="#3b82f6"/>
  </g>
''' + extra_bg

def svg(body):
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 900">\n  <defs>\n' + ROOM_DEFS + PG +
            '  </defs>\n' + body + '  <rect width="1600" height="900" fill="url(#vign)"/>\n</svg>\n')

# 1) hiding with the virus behind a balloon stand, partygoers at the cake in the distance
funvirus = svg(room() + '''  <!-- the party, far away -->
  <rect x="980" y="560" width="420" height="18" fill="#f3efe4"/>
  <rect x="1000" y="578" width="14" height="110" fill="#cfc6b0"/><rect x="1366" y="578" width="14" height="110" fill="#cfc6b0"/>
  <rect x="1110" y="470" width="180" height="90" rx="8" fill="#f8d6e3"/><rect x="1110" y="470" width="180" height="20" rx="8" fill="#fff4f8"/>
  <use href="#pgDetailed" transform="translate(1040 690) scale(.45)" opacity=".9"/>
  <use href="#pgDetailed" transform="translate(1200 700) scale(.5)" opacity=".9"/>
  <use href="#pgDetailed" transform="translate(1370 695) scale(.47)" opacity=".9"/>
  <!-- balloon stand you hide behind -->
  <use href="#balloon" transform="translate(620 300)" fill="#e8443a"/><use href="#balloon" transform="translate(700 260)" fill="#3b82f6"/>
  <use href="#balloon" transform="translate(770 320)" fill="#a855f7"/><use href="#balloon" transform="translate(680 360)" fill="#22c55e"/>
  <rect x="560" y="600" width="280" height="200" rx="10" fill="#e8443a"/><rect x="560" y="600" width="280" height="30" rx="10" fill="#ffd76b"/>
  <text x="700" y="730" font-family="Arial Black, Arial" font-weight="900" font-size="54" text-anchor="middle" fill="#fff6da">=)</text>
  <!-- the mutated virus crouching beside you, tendrils twitching -->
''')

# 2) the virus mutates again and throws partygoers across the room
funroar = svg(room() + '''  <g stroke="#7dff6b" stroke-width="5" opacity=".5" fill="none" filter="url(#glow)">
    <path d="M800 420 m-260 0 a260 260 0 1 0 520 0 a260 260 0 1 0 -520 0"/>
    <path d="M800 420 m-360 0 a360 360 0 1 0 720 0 a360 360 0 1 0 -720 0" opacity=".5"/>
  </g>
  <!-- flying partygoers and party debris -->
  <use href="#pgDetailed" transform="translate(260 520) rotate(-70) scale(.55)" filter="url(#blur)"/>
  <use href="#pgDetailed" transform="translate(1380 430) rotate(60) scale(.55)" filter="url(#blur)"/>
  <use href="#pgDetailed" transform="translate(1250 860) rotate(20) scale(.75)"/>
  <path d="M150 300 l40 -20 l10 36 z" fill="#e8443a"/><path d="M1460 640 l30 -18 l6 30 z" fill="#3b82f6"/><path d="M420 180 l26 -6 l-4 24 z" fill="#22c55e"/>
  <ellipse cx="560" cy="820" rx="80" ry="16" fill="#f8d6e3"/>
  <!-- the virus, bigger now -->
  <text x="800" y="130" font-family="Arial Black, Arial" font-weight="900" font-size="90" text-anchor="middle" fill="#111" opacity=".8">=( =( =(</text>
''')

# 3) the hallway of presents, one with your name on it
presents = []
import random
random.seed(7)
cols = ['#e8443a', '#3b82f6', '#22c55e', '#a855f7', '#f59e0b', '#ec4899']
for i in range(18):
    side = -1 if i % 2 == 0 else 1
    depth = i // 2
    s = 1.0 - depth * .1
    x = 800 + side * (520 - depth * 52) - 60 * s
    y = 800 - depth * 34
    w, h = 120 * s, (90 + random.randint(0, 50)) * s
    c = cols[i % len(cols)]
    presents.append(f'<rect x="{x:.0f}" y="{y - h:.0f}" width="{w:.0f}" height="{h:.0f}" fill="{c}"/>'
                    f'<rect x="{x + w / 2 - 6 * s:.0f}" y="{y - h:.0f}" width="{12 * s:.0f}" height="{h:.0f}" fill="#fff6da"/>'
                    f'<rect x="{x:.0f}" y="{y - h / 2 - 6 * s:.0f}" width="{w:.0f}" height="{12 * s:.0f}" fill="#fff6da"/>')
funhall = svg('''  <!-- a long party hallway shrinking into the distance -->
  <polygon points="0,0 1600,0 1000,330 600,330" fill="#cbb54f"/>
  <polygon points="0,0 600,330 600,520 0,900" fill="url(#paper)"/>
  <polygon points="1600,0 1000,330 1000,520 1600,900" fill="url(#paper)"/>
  <polygon points="0,900 600,520 1000,520 1600,900" fill="url(#carpet)"/>
  <rect x="600" y="330" width="400" height="190" fill="#3a3010"/>
  <rect x="740" y="380" width="120" height="140" fill="#14110a"/>
  <g stroke-width="8" fill="none" stroke-linecap="round">
    <path d="M0 60 Q300 160 600 340" stroke="#e8443a"/><path d="M1600 60 Q1300 160 1000 340" stroke="#3b82f6"/>
  </g>
  ''' + '\n  '.join(presents) + '''
  <!-- the present with your name on it -->
  <g transform="translate(800 820)">
    <rect x="-110" y="-170" width="220" height="170" fill="#ffd92e"/>
    <rect x="-14" y="-170" width="28" height="170" fill="#e8443a"/><rect x="-110" y="-100" width="220" height="28" fill="#e8443a"/>
    <path d="M0 -170 C-70 -240 -110 -170 -10 -168 M0 -170 C70 -240 110 -170 10 -168" stroke="#e8443a" stroke-width="16" fill="none"/>
    <rect x="40" y="-150" width="110" height="54" rx="6" fill="#fff6da" transform="rotate(12 40 -150)"/>
    <text x="96" y="-110" font-family="Arial Black, Arial" font-size="22" text-anchor="middle" fill="#111" transform="rotate(12 40 -150)">FOR YOU =)</text>
  </g>
  <!-- the virus leaning in to sniff it -->
''')

# 4) the virus wrapped around a giant partygoer in front of the way out
funhold = svg(room() + '''  <!-- the way out -->
  <rect x="1180" y="300" width="230" height="340" fill="#2b2b2b"/><rect x="1196" y="316" width="198" height="324" fill="#9ca3af"/>
  <circle cx="1370" cy="480" r="10" fill="#374151"/>
  <rect x="1200" y="250" width="190" height="44" fill="#111"/><text x="1295" y="282" font-family="Arial Black, Arial" font-size="30" text-anchor="middle" fill="#7dff6b">WAY OUT</text>
  <!-- a giant partygoer, held back by the virus -->
  <use href="#pgDetailed" transform="translate(760 880) scale(1.6)"/>
''')

for name, s in (('art_funvirus', funvirus), ('art_funroar', funroar), ('art_funhall', funhall), ('art_funhold', funhold)):
    open(os.path.join(D, name + '.svg'), 'w', encoding='utf8').write(s)
    print(name, len(s))
