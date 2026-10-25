# detail pass for the Level 1 and Level Fun art; keeps clear the spots where the virus is overlaid in the game
import os, random, re
D = r'C:\Users\dahaw\OneDrive\Desktop\twine-games\part-3-1-backrooms\src\images'
random.seed(23)
MARK = '<!-- detail pass 2 -->'
DEFS = '''    <radialGradient id="d2lamp"><stop offset="0" stop-color="#fff6c8" stop-opacity=".55"/><stop offset="1" stop-color="#fff6c8" stop-opacity="0"/></radialGradient>
    <radialGradient id="d2ball" cx=".35" cy=".3" r=".8"><stop offset="0" stop-color="#ffffff"/><stop offset=".5" stop-color="#cbd5e1"/><stop offset="1" stop-color="#64748b"/></radialGradient>
    <filter id="d2glow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="5" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
'''
PARTY = ['#e8443a', '#3b82f6', '#22c55e', '#a855f7', '#f59e0b', '#ec4899', '#fde047']

def add(name, layer):
    p = os.path.join(D, name + '.svg')
    s = open(p, encoding='utf8').read()
    if MARK in s:
        return
    s = s.replace('  </defs>', DEFS + '  </defs>', 1)
    # draw under the final overlay (fog / vignette / red glow) when there is one
    m = list(re.finditer(r'  <rect width="1600" height="900" fill="url\(#(?:fog|vign|red)\)"/>\n', s))
    at = m[-1].start() if m else s.rindex('</svg>')
    s = s[:at] + '  ' + MARK + '\n' + layer + '\n' + s[at:]
    open(p, 'w', encoding='utf8').write(s)

def clear(x, y, avoid):
    return not any(a[0] <= x <= a[2] and a[1] <= y <= a[3] for a in avoid)

def confetti(n, box, avoid=()):
    out = []
    while len(out) < n:
        x, y = random.randint(box[0], box[2]), random.randint(box[1], box[3])
        if not clear(x, y, avoid):
            continue
        c = random.choice(PARTY)
        if random.random() < .5:
            out.append(f'<rect x="{x}" y="{y}" width="{random.randint(8, 14)}" height="{random.randint(4, 7)}" fill="{c}" transform="rotate({random.randint(0, 180)} {x} {y})"/>')
        else:
            out.append(f'<circle cx="{x}" cy="{y}" r="{random.randint(3, 6)}" fill="{c}"/>')
    return ''.join(out)

def bunting(x0, x1, y, sag=40):
    flags, n = [], int((x1 - x0) / 60)
    for i in range(n + 1):
        t = i / max(n, 1)
        x = x0 + (x1 - x0) * t
        yy = y + sag * 4 * t * (1 - t)
        flags.append(f'<path d="M{x - 22:.0f} {yy:.0f} L{x + 22:.0f} {yy:.0f} L{x:.0f} {yy + 40:.0f} Z" fill="{PARTY[i % len(PARTY)]}"/>')
    return f'<path d="M{x0} {y} Q{(x0 + x1) / 2} {y + sag * 2} {x1} {y}" stroke="#444" stroke-width="3" fill="none"/>' + ''.join(flags)

def frame(x, y, w, h, face='=)'):
    return (f'<g><rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#7c4a1e"/><rect x="{x + 8}" y="{y + 8}" width="{w - 16}" height="{h - 16}" fill="#fff6c8"/>'
            f'<circle cx="{x + w / 2}" cy="{y + h / 2}" r="{min(w, h) * .3:.0f}" fill="#ffd92e"/>'
            f'<text x="{x + w / 2}" y="{y + h / 2 + min(w, h) * .1:.0f}" font-family="Arial Black, Arial" font-size="{min(w, h) * .26:.0f}" text-anchor="middle" fill="#111">{face}</text></g>')

def present(x, y, w, h, c):
    return (f'<g><rect x="{x}" y="{y - h}" width="{w}" height="{h}" fill="{c}"/><rect x="{x + w / 2 - 5}" y="{y - h}" width="10" height="{h}" fill="#fff6da"/>'
            f'<rect x="{x}" y="{y - h / 2 - 5}" width="{w}" height="10" fill="#fff6da"/><path d="M{x + w / 2} {y - h} q-24 -26 -30 -4 q12 6 30 4 q24 -26 30 -4 q-12 6 -30 4" fill="#fff6da"/></g>')

def cracks(n, box):
    out = []
    for _ in range(n):
        x, y = random.randint(box[0], box[2]), random.randint(box[1], box[3])
        d = f'M{x} {y}'
        for _ in range(4):
            x += random.randint(-30, 30); y += random.randint(6, 26); d += f' L{x} {y}'
        out.append(f'<path d="{d}" stroke="#111" stroke-width="2" fill="none" opacity=".45"/>')
    return ''.join(out)

def stains(n, box, c='#1a1f16', o=.25):
    return ''.join(f'<ellipse cx="{random.randint(box[0], box[2])}" cy="{random.randint(box[1], box[3])}" rx="{random.randint(20, 70)}" ry="{random.randint(10, 40)}" fill="{c}" opacity="{o}"/>' for _ in range(n))

# ---------- Level 1 ----------
add('art_level1', '''  <!-- water stains and cracks on the far wall and pillars -->
  ''' + stains(10, (300, 120, 1300, 520)) + cracks(9, (200, 140, 1400, 480)) + '''
  <!-- hanging cables and a broken light tube dangling on one wire -->
  <g fill="none" stroke="#111" stroke-linecap="round"><path d="M420 0 q30 120 -10 180" stroke-width="4"/><path d="M1180 0 q-40 100 6 150" stroke-width="4"/><path d="M1000 0 v60" stroke-width="3"/></g>
  <g transform="translate(1000 60) rotate(28)"><rect x="-4" y="0" width="8" height="120" fill="#e5e7eb"/><rect x="-4" y="0" width="8" height="120" fill="#fff" opacity=".4"/></g>
  <!-- stencilled level number on a pillar -->
  <text x="160" y="380" font-family="Arial Black, Arial" font-size="44" fill="#d4d4d4" opacity=".55" transform="rotate(-90 160 380)">LEVEL 1</text>
  <!-- painted arrow and a smudged warning -->
  <g fill="none" stroke="#facc15" stroke-width="10" opacity=".55" stroke-linecap="round"><path d="M620 600 h160 M740 570 l40 30 l-40 30"/></g>
  <text x="1560" y="470" font-family="Arial Black, Arial" font-size="26" fill="#ef4444" opacity=".55" text-anchor="end">DON'T FOLLOW THE LIGHTS</text>
  <!-- trash, a dropped bottle and footprints through the puddles -->
  <g fill="#2b2b2b"><rect x="520" y="830" width="30" height="10" transform="rotate(20 520 830)"/><rect x="1080" y="800" width="24" height="8" transform="rotate(-30 1080 800)"/><path d="M300 860 l40 -10 l6 18 z"/></g>
  <g transform="translate(900 840) rotate(70)"><rect x="-10" y="-34" width="20" height="56" rx="6" fill="#bfdbfe" opacity=".8"/><rect x="-6" y="-46" width="12" height="14" fill="#93c5fd"/></g>
  <g fill="#0b0d10" opacity=".55">''' + ''.join(f'<ellipse cx="{700 + i * 70}" cy="{880 - i * 26}" rx="16" ry="7"/>' for i in range(6)) + '''</g>''')

# ---------- supply crates ----------
add('art_crates', '''  <!-- metal shelving in the background with more boxes -->
  <g fill="#3b3f46"><rect x="80" y="160" width="12" height="560"/><rect x="420" y="160" width="12" height="560"/><rect x="80" y="300" width="352" height="12"/><rect x="80" y="480" width="352" height="12"/></g>
  <g fill="#8b6b3e"><rect x="110" y="220" width="120" height="80"/><rect x="250" y="240" width="140" height="60"/><rect x="130" y="400" width="160" height="80"/></g>
  <g font-family="Arial" font-size="16" fill="#3b2a12"><text x="120" y="262">ALMOND W.</text><text x="140" y="446">CASE 7 / 12</text></g>
  <!-- a note taped to the crate -->
  <g transform="translate(980 540) rotate(-5)"><rect x="0" y="0" width="190" height="110" fill="#fef9c3"/><rect x="70" y="-10" width="50" height="20" fill="#e5e7eb" opacity=".8"/>
    <text x="12" y="34" font-family="Comic Sans MS, Arial" font-size="18" fill="#111">drink 1 when</text><text x="12" y="60" font-family="Comic Sans MS, Arial" font-size="18" fill="#111">things smile.</text><text x="12" y="88" font-family="Comic Sans MS, Arial" font-size="18" fill="#b91c1c">NOT THE RED ONE</text></g>
  <!-- straw packing spilling out, and a spilled puddle under the bottle -->
  <g stroke="#d6b25e" stroke-width="3" opacity=".8">''' + ''.join(f'<path d="M{random.randint(560, 1000)} {random.randint(760, 880)} l{random.randint(-30, 30)} {random.randint(-8, 8)}"/>' for _ in range(30)) + '''</g>
  <ellipse cx="1380" cy="870" rx="150" ry="18" fill="#bfdbfe" opacity=".35"/>
  <!-- one red bottle hidden among the rest -->
  <g transform="translate(1240 820) rotate(-10)"><rect x="-12" y="-60" width="24" height="60" rx="6" fill="#dc2626"/><rect x="-7" y="-74" width="14" height="14" fill="#7f1d1d"/></g>
  <!-- dust in the lamp light -->
  ''' + ''.join(f'<circle cx="{random.randint(600, 1000)}" cy="{random.randint(40, 500)}" r="2" fill="#fff6c8" opacity="{random.choice((.25, .4, .6))}"/>' for _ in range(40)))

# ---------- dark hall ----------
add('art_darkhall', '''  <!-- doors and panels along both walls -->
  <g fill="none" stroke="#1c1c1c" stroke-width="6"><path d="M120 800 V320 L300 400 V720"/><path d="M1480 800 V320 L1300 400 V720"/><path d="M450 640 V430 L540 460 V600"/><path d="M1150 640 V430 L1060 460 V600"/></g>
  <g fill="#262626"><circle cx="280" cy="560" r="7"/><circle cx="1320" cy="560" r="7"/></g>
  <!-- a second, dead light and hanging wires -->
  <rect x="740" y="150" width="120" height="12" fill="#262626"/><path d="M760 162 q-6 40 6 60 M840 162 q10 30 -4 56" stroke="#151515" stroke-width="3" fill="none"/>
  <!-- long scratch marks on the walls, at the figure's height -->
  <g stroke="#2e2e2e" stroke-width="3" stroke-linecap="round"><path d="M330 300 l60 180 M345 296 l60 182 M360 292 l58 184"/><path d="M1270 300 l-60 180 M1255 296 l-60 182"/></g>
  <!-- eyes much further back in the dark -->
  <g fill="#e5e7eb" opacity=".5"><circle cx="700" cy="420" r="3"/><circle cx="712" cy="420" r="3"/><circle cx="905" cy="440" r="2.5"/><circle cx="915" cy="440" r="2.5"/></g>
  <!-- wet footprints that are not yours leading toward you -->
  <g fill="#3a3a3a" opacity=".55">''' + ''.join(f'<path d="M{800 + (-1) ** i * 30} {640 + i * 40} q-10 -20 0 -30 q12 0 10 30 z" transform="scale(1 {1 + i * .05:.2f})"/>' for i in range(6)) + '''</g>''')

# ---------- Level Fun (the party) ----------
add('art_levelfun', '''  <!-- bunting, a disco ball and glints -->
  ''' + bunting(0, 520, 250) + bunting(1080, 1600, 250) + '''
  <path d="M800 0 v60" stroke="#555" stroke-width="3"/><circle cx="800" cy="96" r="38" fill="url(#d2ball)"/>
  <g stroke="#cbd5e1" stroke-width="1.5" opacity=".6"><path d="M762 96 h76 M768 76 h64 M768 116 h64 M800 58 v76 M780 62 v68 M820 62 v68"/></g>
  <g fill="#fff" filter="url(#d2glow)" opacity=".8"><circle cx="640" cy="300" r="4"/><circle cx="980" cy="360" r="4"/><circle cx="520" cy="470" r="3"/><circle cx="1110" cy="250" r="3"/></g>
  <!-- presents piled by the table and a sign on the wall -->
  ''' + present(1050, 720, 80, 60, '#3b82f6') + present(1120, 720, 60, 46, '#e8443a') + present(500, 720, 70, 54, '#22c55e') + '''
  <g transform="translate(660 340) rotate(4)"><rect x="-90" y="-30" width="180" height="60" fill="#fff6da" stroke="#a855f7" stroke-width="5"/><text y="10" font-family="Arial Black, Arial" font-size="24" text-anchor="middle" fill="#a855f7">NO FROWNS =)</text></g>
  <!-- confetti everywhere, party poppers and a balloon on the floor -->
  ''' + confetti(160, (0, 280, 1600, 900)) + '''
  <g transform="translate(220 820) rotate(-30)"><path d="M0 0 l60 -20 l-20 60 z" fill="#ec4899"/><path d="M60 -20 l30 -30 M70 -10 l40 -10 M50 -30 l10 -40" stroke="#fde047" stroke-width="4"/></g>
  <ellipse cx="1500" cy="840" rx="40" ry="34" fill="#22c55e"/><ellipse cx="1490" cy="830" rx="12" ry="9" fill="#fff" opacity=".5"/>''')

# ---------- the two exits ----------
add('art_funexits', '''  ''' + bunting(0, 1600, 120, 30) + '''
  <!-- smiley pictures on the wall -->
  ''' + frame(140, 220, 120, 150) + frame(760, 230, 110, 120, '=D') + frame(1380, 220, 120, 150) + '''
  <!-- signs: one cheerful, one scratched -->
  <g transform="translate(860 560) rotate(-6)"><rect x="-80" y="-24" width="160" height="48" fill="#fff6da" stroke="#e8443a" stroke-width="4"/><text y="9" font-family="Arial Black, Arial" font-size="22" text-anchor="middle" fill="#e8443a">THIS WAY =)</text></g>
  <path d="M770 600 l-60 30" stroke="#e8443a" stroke-width="8" stroke-linecap="round"/>
  <g stroke="#555" stroke-width="3" stroke-linecap="round" opacity=".7"><path d="M1060 380 l30 70 M1072 376 l30 70 M1084 372 l30 70"/></g>
  <text x="1110" y="620" font-family="Comic Sans MS, Arial" font-size="20" fill="#333" opacity=".7">quietly...</text>
  <!-- confetti and a dropped slice of cake -->
  ''' + confetti(110, (0, 640, 1600, 900)) + '''
  <g transform="translate(900 830)"><path d="M0 0 l90 -20 l0 26 l-90 20 z" fill="#f8d6e3"/><path d="M0 0 l90 -20 l-30 -16 z" fill="#fff4f8"/><path d="M10 6 l70 -16" stroke="#9b1c1c" stroke-width="6" opacity=".6"/></g>''')

# ---------- party chase ----------
add('art_partychase', '''  ''' + bunting(0, 700, 60, 30) + '''
  <!-- knocked-over chair and table -->
  <g transform="translate(140 760) rotate(-70)"><rect x="-30" y="-80" width="60" height="80" fill="#cfc6b0"/><rect x="-36" y="0" width="72" height="14" fill="#e5dfcf"/><path d="M-30 14 v50 M30 14 v50" stroke="#a8a08c" stroke-width="8"/></g>
  <g transform="translate(1500 820) rotate(12)"><rect x="-120" y="-14" width="240" height="14" fill="#f3efe4"/><path d="M-100 0 v80 M100 0 v80" stroke="#cfc6b0" stroke-width="10"/></g>
  <!-- confetti flying past you -->
  ''' + confetti(120, (0, 0, 1600, 900)) + '''
  <!-- popped balloon bits -->
  <g fill="#a855f7"><path d="M1000 140 l20 -14 l8 22 z"/><path d="M1040 160 l14 6 l-10 12 z"/></g><g fill="#22c55e"><path d="M320 200 l24 -8 l-2 24 z"/></g>''')

# ---------- after the mutation: hiding behind the balloon stand (virus sits left, x 80-540) ----------
VZ = [(60, 160, 560, 760)]
add('art_funvirus', '''  ''' + bunting(560, 1600, 150, 40) + '''
  <!-- disco ball over the party -->
  <path d="M1200 0 v50" stroke="#555" stroke-width="3"/><circle cx="1200" cy="84" r="34" fill="url(#d2ball)"/>
  <!-- presents and a sign by the cake table -->
  ''' + present(940, 690, 70, 52, '#a855f7') + present(1420, 690, 64, 48, '#f59e0b') + '''
  <g transform="translate(1200 280)"><rect x="-110" y="-28" width="220" height="56" fill="#fff6da" stroke="#e8443a" stroke-width="5"/><text y="10" font-family="Arial Black, Arial" font-size="24" text-anchor="middle" fill="#e8443a">PARTY FOREVER =)</text></g>
  ''' + frame(820, 230, 100, 120) + '''
  <!-- confetti on the floor (not where the virus is crouching) -->
  ''' + confetti(130, (0, 650, 1600, 900), VZ))

# ---------- the fight (virus in the middle, x 480-1120) ----------
VZ = [(470, 120, 1130, 900)]
add('art_funroar', '''  ''' + bunting(0, 460, 150, 30) + bunting(1140, 1600, 150, 30) + '''
  <!-- cracks in the floor from the impact -->
  <g stroke="#3f3412" stroke-width="5" fill="none" stroke-linecap="round" opacity=".8"><path d="M460 760 l-80 40 l-60 -10 l-90 60"/><path d="M1140 760 l80 30 l40 -20 l110 70"/><path d="M420 840 l-40 50 M1180 830 l60 60"/></g>
  <!-- a broken table, a squashed cake and torn streamers -->
  <g transform="translate(200 700) rotate(-20)"><rect x="-120" y="-12" width="240" height="14" fill="#f3efe4"/><path d="M-100 2 v60" stroke="#cfc6b0" stroke-width="10"/></g>
  <ellipse cx="1360" cy="820" rx="90" ry="20" fill="#f8d6e3"/><ellipse cx="1340" cy="806" rx="40" ry="10" fill="#fff4f8"/>
  <path d="M1500 0 q-20 120 30 200" stroke="#e8443a" stroke-width="10" fill="none"/><path d="M80 0 q30 110 -20 190" stroke="#3b82f6" stroke-width="10" fill="none"/>
  <!-- confetti blasted outward -->
  ''' + confetti(160, (0, 0, 1600, 900), VZ))

# ---------- the present hallway (virus on the right, x 1040-1560) ----------
VZ = [(1030, 220, 1600, 900)]
add('art_funhall', '''  <!-- smiley pictures on the left wall -->
  ''' + frame(140, 260, 110, 140) + frame(380, 330, 80, 100, '=D') + '''
  <!-- bunting down the hallway -->
  ''' + bunting(0, 600, 120, 60) + '''
  <!-- balloons tied to the presents and confetti on the carpet -->
  <g><path d="M300 680 q10 -80 -10 -160" stroke="#333" stroke-width="2" fill="none"/><ellipse cx="290" cy="490" rx="34" ry="42" fill="#ec4899"/><ellipse cx="280" cy="478" rx="10" ry="8" fill="#fff" opacity=".5"/></g>
  <g><path d="M660 600 q10 -60 -6 -120" stroke="#333" stroke-width="2" fill="none"/><ellipse cx="654" cy="456" rx="24" ry="30" fill="#22c55e"/></g>
  ''' + confetti(120, (0, 560, 1600, 900), VZ) + '''
  <!-- a trail of wrapping paper leading into the dark doorway -->
  <g fill="#e8443a" opacity=".85"><path d="M760 520 l30 -6 l6 14 l-30 4 z"/><path d="M790 560 l40 -6 l4 16 l-40 6 z"/><path d="M740 610 l46 -4 l2 18 l-46 4 z"/></g>''')

# ---------- the way out (virus over the giant, x 350-1030) ----------
VZ = [(340, 160, 1040, 900)]
add('art_funhold', '''  ''' + bunting(0, 340, 150, 30) + bunting(1040, 1600, 150, 30) + '''
  <!-- smiley pictures beside the door -->
  ''' + frame(80, 250, 110, 140) + frame(1460, 300, 100, 120, '=D') + '''
  <!-- warning scratched next to the door -->
  <text x="1300" y="700" font-family="Comic Sans MS, Arial" font-size="24" fill="#111" opacity=".7" text-anchor="middle">it doesn't blink</text>
  <!-- cracked floor and confetti -->
  <g stroke="#3f3412" stroke-width="4" fill="none" opacity=".7"><path d="M1060 760 l60 30 l30 -10 l80 60"/><path d="M320 780 l-60 40 l-40 -6 l-70 50"/></g>
  ''' + confetti(110, (0, 640, 1600, 900), VZ))
print('detail pass 2 applied')
