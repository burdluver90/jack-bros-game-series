# detail pass for the new level art (run after levels3.py, which writes the base pictures)
import os, random
D = r'C:\Users\dahaw\OneDrive\Desktop\twine-games\part-3-1-backrooms\src\images'
VIGN = '<rect width="1600" height="900" fill="url(#vign)"/>'
random.seed(11)

def add(name, defs, layer, before=VIGN):
    p = os.path.join(D, name + '.svg')
    s = open(p, encoding='utf8').read()
    if '<!-- detail pass -->' in s:
        return
    s = s.replace('  </defs>', defs + '  </defs>', 1)
    s = s.replace(before, '<!-- detail pass -->\n' + layer + '\n  ' + before, 1)
    open(p, 'w', encoding='utf8').write(s)

def gauge(x, y, r, a):
    return (f'<g transform="translate({x} {y})"><circle r="{r + 6}" fill="#3b2414"/><circle r="{r}" fill="#f5efe0"/>'
            f'<path d="M{-r * .7:.0f} {r * .35:.0f} A{r * .8:.0f} {r * .8:.0f} 0 0 1 {r * .7:.0f} {r * .35:.0f}" stroke="#b91c1c" stroke-width="4" fill="none"/>'
            + ''.join(f'<path d="M0 {-r + 3} v6" stroke="#333" stroke-width="2" transform="rotate({t})"/>' for t in range(-120, 121, 30)) +
            f'<path d="M0 0 L0 {-r + 8}" stroke="#111" stroke-width="3" transform="rotate({a})"/><circle r="4" fill="#111"/></g>')

# ---------- Level 2: Pipe Dreams ----------
rivets = ''.join(f'<circle cx="{x}" cy="{y}" r="4" fill="#2a1a10"/>' for y in (126, 162, 306, 356, 706, 750) for x in range(30, 1600, 90))
drips = ''.join(f'<path d="M{x} {y} q-6 14 0 20 q6 -6 0 -20z" fill="#9cc6d8" opacity=".7"/>' for x, y in ((470, 250), (980, 360), (1180, 830), (720, 760), (140, 360)))
rust = ''.join(f'<ellipse cx="{random.randint(0, 1600)}" cy="{random.choice((140, 320, 720))}" rx="{random.randint(20, 60)}" ry="8" fill="#8a3b12" opacity=".5"/>' for _ in range(14))
grate = ''.join(f'<path d="M{x} 840 v60" stroke="#1a100a" stroke-width="5"/>' for x in range(0, 1600, 40))
add('art_level2', '''    <linearGradient id="beam" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#fff7c2" stop-opacity=".6"/><stop offset="1" stop-color="#fff7c2" stop-opacity="0"/></linearGradient>
    <radialGradient id="ember"><stop offset="0" stop-color="#ffb14a" stop-opacity=".9"/><stop offset="1" stop-color="#ff6a00" stop-opacity="0"/></radialGradient>
''', '''  <!-- rivets, rust and drips -->
  ''' + rivets + rust + drips + '''
  <!-- cable bundles sagging between the pipes -->
  <g fill="none" stroke-linecap="round"><path d="M0 250 Q400 300 800 250 T1600 260" stroke="#1f1a14" stroke-width="10"/><path d="M0 262 Q420 320 820 262 T1600 270" stroke="#3b3326" stroke-width="6"/><path d="M0 272 Q380 330 780 270 T1600 282" stroke="#7c2d12" stroke-width="4"/></g>
  <!-- pressure gauges, one in the red -->
  ''' + gauge(500, 470, 34, -60) + gauge(1130, 470, 40, 105) + gauge(1420, 230, 26, 20) + '''
  <!-- warning sign -->
  <g transform="translate(1100 560) rotate(-4)"><rect x="-90" y="-40" width="180" height="80" fill="#facc15" stroke="#111" stroke-width="5"/><text y="-6" font-family="Arial Black, Arial" font-size="26" text-anchor="middle" fill="#111">DANGER</text><text y="26" font-family="Arial Black, Arial" font-size="22" text-anchor="middle" fill="#b91c1c">HOT PIPES</text></g>
  <!-- the flashlight is easier to spot: it is switched on -->
  <path d="M410 668 L640 760 L640 860 Z" fill="url(#beam)" opacity=".8"/>
  <!-- glowing seams on the red-hot pipe -->
  <g fill="url(#ember)"><circle cx="1180" cy="620" r="40"/><circle cx="1380" cy="620" r="46"/><circle cx="1540" cy="620" r="36"/></g>
  <!-- metal grate floor -->
  <rect y="840" width="1600" height="60" fill="#2a1a10" opacity=".7"/>''' + grate + '''
  <!-- a footprint trail in the soot, leading toward the cold pipe -->
  <g fill="#120a05" opacity=".7"><ellipse cx="560" cy="870" rx="14" ry="7"/><ellipse cx="500" cy="882" rx="14" ry="7"/><ellipse cx="440" cy="868" rx="14" ry="7"/><ellipse cx="380" cy="880" rx="14" ry="7"/></g>''')

# ---------- Level 4: Abandoned Office ----------
stains = ''.join(f'<rect x="{x}" y="{y}" width="100" height="60" fill="#a8946a" opacity=".45"/>' for x, y in ((200, 120), (1000, 180), (1300, 0), (500, 240)))
papers = ''.join(f'<rect x="{random.randint(250, 1450)}" y="{random.randint(600, 860)}" width="44" height="30" fill="#f8f6ee" transform="rotate({random.randint(-40, 40)} 800 700)" opacity=".9"/>' for _ in range(16))
carpet = ''.join(f'<path d="M{x} 900 L{800 + (x - 800) * .4:.0f} 420" stroke="#5a5d48" stroke-width="2" opacity=".5"/>' for x in range(-800, 2400, 120))
def chair(x, y, s, rot):
    return (f'<g transform="translate({x} {y}) scale({s}) rotate({rot})"><rect x="-34" y="-110" width="68" height="70" rx="12" fill="#1f2937"/><rect x="-40" y="-40" width="80" height="22" rx="8" fill="#273244"/>'
            '<path d="M0 -18 v30 M-34 30 L0 12 L34 30 M0 12 v22" stroke="#4b5563" stroke-width="6" fill="none"/><circle cx="-34" cy="32" r="6" fill="#111"/><circle cx="34" cy="32" r="6" fill="#111"/><circle cy="36" r="6" fill="#111"/></g>')
add('art_level4', '''    <radialGradient id="lamp"><stop offset="0" stop-color="#fffbe6" stop-opacity=".5"/><stop offset="1" stop-color="#fffbe6" stop-opacity="0"/></radialGradient>
''', '''  <!-- stained ceiling tiles and pools of light -->
  ''' + stains + '''
  <g fill="url(#lamp)"><ellipse cx="400" cy="420" rx="260" ry="90"/><ellipse cx="800" cy="420" rx="260" ry="90"/></g>
  <!-- carpet lines and scattered paper -->
  ''' + carpet + papers + '''
  <!-- rolled-away office chairs -->
  ''' + chair(520, 760, 1.0, -12) + chair(1240, 720, .85, 18) + chair(980, 560, .55, 0) + '''
  <!-- filing cabinet with a drawer hanging open -->
  <g transform="translate(1420 760)"><rect x="-70" y="-300" width="140" height="300" fill="#9ca3af"/><rect x="-60" y="-290" width="120" height="86" fill="#b7bcc4"/><rect x="-60" y="-196" width="120" height="86" fill="#b7bcc4"/><rect x="-74" y="-110" width="148" height="70" fill="#d1d5db"/><rect x="-20" y="-250" width="40" height="8" fill="#4b5563"/><rect x="-20" y="-158" width="40" height="8" fill="#4b5563"/><rect x="-50" y="-128" width="100" height="22" fill="#f8f6ee"/></g>
  <!-- wall clock stuck at 3:33 -->
  <g transform="translate(1180 200)"><circle r="40" fill="#f8f6ee" stroke="#374151" stroke-width="6"/><path d="M0 0 L22 10 M0 0 L-12 -22" stroke="#111" stroke-width="4" stroke-linecap="round"/></g>
  <!-- whiteboard with someone's last notes -->
  <g transform="translate(420 200)"><rect x="-130" y="-70" width="260" height="140" fill="#f8fafc" stroke="#9ca3af" stroke-width="6"/>
    <text x="-110" y="-30" font-family="Comic Sans MS, Arial" font-size="24" fill="#1d4ed8">LEVEL 4 = SAFE</text>
    <text x="-110" y="6" font-family="Comic Sans MS, Arial" font-size="24" fill="#b91c1c">6 = NO LIGHTS!!</text>
    <text x="-110" y="42" font-family="Comic Sans MS, Arial" font-size="24" fill="#111">exit?? =)</text></g>
  <!-- a dead potted plant -->
  <g transform="translate(330 760)"><path d="M-30 0 h60 l-8 -60 h-44 z" fill="#9a3412"/><path d="M0 -60 q-30 -60 -50 -70 M0 -60 q10 -70 30 -90 M0 -60 q40 -30 60 -30" stroke="#6b5a2b" stroke-width="5" fill="none"/></g>
  <!-- a green exit sign that might be lying -->
  <g transform="translate(800 340)"><rect x="-60" y="-22" width="120" height="44" fill="#052e16"/><text y="12" font-family="Arial Black, Arial" font-size="28" text-anchor="middle" fill="#4ade80">EXIT</text></g>''')

# ---------- Level 6: Lights Out ----------
eyes = ''.join(f'<g fill="{c}" filter="url(#glow6)" opacity="{o}"><circle cx="{x}" cy="{y}" r="{r}"/><circle cx="{x + r * 4.5:.0f}" cy="{y}" r="{r}"/></g>'
               for x, y, r, c, o in ((230, 300, 4, '#f8fafc', .6), (600, 470, 3, '#f8fafc', .5), (1370, 260, 4, '#ef4444', .7), (1000, 470, 3, '#ef4444', .6), (120, 640, 5, '#f8fafc', .4), (1480, 620, 5, '#ef4444', .5)))
dust = ''.join(f'<circle cx="{random.randint(620, 980)}" cy="{random.randint(440, 880)}" r="{random.choice((1.5, 2, 2.5))}" fill="#fef9c3" opacity="{random.choice((.2, .3, .45))}"/>' for _ in range(40))
add('art_level6', '', '''  <!-- door frames you can only just make out -->
  <g fill="none" stroke="#111118" stroke-width="10"><path d="M140 820 V300 L300 380 V720"/><path d="M1460 820 V300 L1300 380 V720"/><path d="M420 640 V400 L520 440 V590"/><path d="M1180 640 V400 L1080 440 V590"/></g>
  <!-- tall shapes standing very still in the dark -->
  <g fill="#0b0b10"><path d="M380 700 q-10 -160 20 -230 q30 -40 50 0 q30 70 20 230 z"/><path d="M1240 700 q-14 -180 18 -260 q28 -40 50 0 q34 80 22 260 z"/><path d="M1100 560 q-6 -90 12 -130 q16 -24 28 0 q16 40 12 130 z"/></g>
  <!-- more eyes, near and far -->
  ''' + eyes + '''
  <!-- handprints scraped down the wall -->
  <g fill="#1d1d26"><path d="M240 520 q-4 -30 6 -34 q6 -18 12 0 q8 -20 14 0 q8 -14 12 4 q10 0 2 30 z"/><path d="M270 590 q-4 -30 6 -34 q6 -18 12 0 q8 -20 14 0 q8 -14 12 4 q10 0 2 30 z"/></g>
  <path d="M240 524 v80 M252 520 v90 M264 520 v70" stroke="#1d1d26" stroke-width="3"/>
  <!-- dust drifting in the faint light, and a lost shoe -->
  ''' + dust + '''
  <g transform="translate(860 820) rotate(-12)"><path d="M-50 0 q0 -30 40 -30 h20 q10 -14 30 -10 l10 40 z" fill="#1f1f29"/><path d="M-50 0 h100" stroke="#2c2c38" stroke-width="6"/></g>''', before='<!-- the faint hum of a light far away -->')

# ---------- Level !: Run For Your Life ----------
def door(x, y, w, h, n, left):
    return (f'<g><polygon points="{x},{y} {x + w},{y + (h * .08 if left else -h * .08):.0f} {x + w},{y + h + (-h * .08 if left else h * .08):.0f} {x},{y + h}" fill="#2a0505" stroke="#160202" stroke-width="4"/>'
            f'<text x="{x + w / 2:.0f}" y="{y - 10}" font-family="Arial Black, Arial" font-size="{h * .12:.0f}" text-anchor="middle" fill="#fca5a5" opacity=".7">{n}</text></g>')
doors = door(120, 420, 120, 320, '!13', True) + door(420, 410, 80, 200, '!12', True) + door(1360, 420, 120, 320, '!13B', False) + door(1100, 410, 80, 200, '!12B', False)
debris = ''.join(f'<rect x="{random.randint(300, 1300)}" y="{random.randint(700, 880)}" width="{random.randint(10, 40)}" height="{random.randint(6, 14)}" fill="#3a0a0a" transform="rotate({random.randint(-50, 50)} 800 800)"/>' for _ in range(18))
sparks = ''.join(f'<path d="M{x} {y} l{random.randint(-30, 30)} {random.randint(10, 40)}" stroke="#ffd166" stroke-width="3"/>' for x, y in ((260, 106), (1340, 106), (535, 260), (1065, 260)) for _ in range(3))
add('art_levelrun', '''    <linearGradient id="puddle" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ff3b3b" stop-opacity=".5"/><stop offset="1" stop-color="#ff3b3b" stop-opacity="0"/></linearGradient>
''', '''  <!-- numbered doors down both walls -->
  ''' + doors + '''
  <!-- red puddles reflecting the lights -->
  <g fill="url(#puddle)"><ellipse cx="520" cy="800" rx="160" ry="22"/><ellipse cx="1120" cy="760" rx="120" ry="16"/><ellipse cx="800" cy="610" rx="90" ry="10"/></g>
  <!-- more scrawls and arrows -->
  <text x="800" y="680" font-family="Arial Black, Arial" font-weight="900" font-size="54" text-anchor="middle" fill="#fecaca" opacity=".75">DON'T STOP</text>
  <g stroke="#fecaca" stroke-width="10" fill="none" opacity=".7" stroke-linecap="round"><path d="M640 760 l120 -60 M740 690 l20 10 l-10 20"/><path d="M960 760 l-120 -60 M860 690 l-20 10 l10 20"/></g>
  <!-- tendrils of the chaser reaching down the hall -->
  <g fill="none" stroke="#000" stroke-linecap="round"><path d="M700 480 C620 540 560 600 470 640" stroke-width="16"/><path d="M900 480 C990 540 1040 610 1130 650" stroke-width="16"/><path d="M760 500 C730 600 700 680 690 760" stroke-width="10"/><path d="M840 500 C870 600 900 690 920 770" stroke-width="10"/></g>
  <!-- sparks from the broken lights, junk on the floor, speed lines -->
  ''' + sparks + debris + '''
  <g stroke="#ff9b9b" stroke-width="4" opacity=".25" stroke-linecap="round"><path d="M0 300 L300 380"/><path d="M0 560 L320 520"/><path d="M1600 300 L1300 380"/><path d="M1600 560 L1280 520"/></g>''')
print('detail pass applied')
