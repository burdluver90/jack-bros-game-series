# Level 5: The Grand Hotel. One big hub level between Level ! and "To be continued".
# Goal: get the brass key (Room 213) and the boiler code (4-1-7) and reach the boiler room exit.
import os, sys, random
GEN = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, GEN)
from levels2 import VIRUS, find, story
D = r'C:\Users\dahaw\OneDrive\Desktop\twine-games\part-3-1-backrooms\src\images'
END = 'To be continued... (Q83)'
random.seed(5)

def scene(bg, virus=None):
    v = ''
    if virus:
        left, top, k = virus
        v = f'<div class="pos" style="left:{left}%;top:{top}%;width:{k * 100:.1f}%;height:{k * 100:.1f}%">{VIRUS}</div>'
    return f'<div class="scene"><div class="pos bg">[img[{bg}]]</div>{v}</div>'

def withVirus(bg, spot):
    return f'<<if $virusWith>>{scene(bg, spot)}<<else>>{scene(bg)}<</if>>'

def choices(*links):
    return '<div class="choices">' + ''.join(links) + '</div>'

def timed(secs, fast, late_label, late_to):
    return ('<div id="opts" class="choices">' + ''.join(fast) + '</div>\n'
            f'<div class="timerbar"><span style="animation-duration:{secs}s"></span></div>\n'
            f'<<timed {secs}s>><<replace "#opts">><div class="caught">[[{late_label}|{late_to}]]</div><</replace>><<run $(".timerbar").remove()>><</timed>>')

def pickup(key, item, label):
    return (f'<<if !setup.isTaken("{key}")>><span id="pk{key}"><<link "{label}">><<if setup.take("{key}","{item}")>>'
            f'<<replace "#pk{key}">><</replace>><</if>><</link>></span><</if>>')

def V(line_with, line_without=''):
    return f'<<if $virusWith>>{line_with}<<else>>{line_without}<</if>>'

# ======================= ART =======================
VIGN = '    <radialGradient id="vign" cx=".5" cy=".5" r=".75"><stop offset=".5" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".7"/></radialGradient>\n'
COMMON = VIGN + '''    <pattern id="hwall" width="60" height="120" patternUnits="userSpaceOnUse"><rect width="60" height="120" fill="#5b1a1f"/><path d="M30 10 l14 20 l-14 20 l-14 -20 z M30 70 l14 20 l-14 20 l-14 -20 z" fill="#6e2329"/><path d="M0 0 v120" stroke="#4a1418" stroke-width="3"/></pattern>
    <pattern id="hcarpet" width="80" height="80" patternUnits="userSpaceOnUse"><rect width="80" height="80" fill="#3b1220"/><path d="M40 4 L76 40 L40 76 L4 40 Z" fill="none" stroke="#b08a3a" stroke-width="4"/><circle cx="40" cy="40" r="8" fill="#7a1f2b"/><circle cx="0" cy="0" r="6" fill="#b08a3a"/><circle cx="80" cy="80" r="6" fill="#b08a3a"/><circle cx="80" cy="0" r="6" fill="#b08a3a"/><circle cx="0" cy="80" r="6" fill="#b08a3a"/></pattern>
    <linearGradient id="gold" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#f6e27a"/><stop offset=".5" stop-color="#c9971c"/><stop offset="1" stop-color="#8a6410"/></linearGradient>
    <radialGradient id="candle"><stop offset="0" stop-color="#fff1b8" stop-opacity=".9"/><stop offset="1" stop-color="#ffb347" stop-opacity="0"/></radialGradient>
    <filter id="hglow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="6" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
    <filter id="hblur"><feGaussianBlur stdDeviation="2.5"/></filter>
    <g id="chand"><path d="M0 0 v60" stroke="#8a6410" stroke-width="4"/><ellipse cx="0" cy="80" rx="120" ry="26" fill="url(#gold)"/><ellipse cx="0" cy="110" rx="80" ry="18" fill="url(#gold)"/>
      <g fill="#e0f2fe" opacity=".85"><path d="M-110 90 l-6 40 l12 0 z"/><path d="M-70 96 l-6 44 l12 0 z"/><path d="M-30 100 l-6 46 l12 0 z"/><path d="M10 100 l-6 46 l12 0 z"/><path d="M50 96 l-6 44 l12 0 z"/><path d="M90 90 l-6 40 l12 0 z"/><path d="M-50 120 l-6 50 l12 0 z"/><path d="M30 120 l-6 50 l12 0 z"/></g>
      <g fill="#fff1b8" filter="url(#hglow)"><circle cx="-100" cy="66" r="7"/><circle cx="-50" cy="60" r="7"/><circle cx="0" cy="58" r="7"/><circle cx="50" cy="60" r="7"/><circle cx="100" cy="66" r="7"/></g>
      <ellipse cx="0" cy="90" rx="200" ry="90" fill="url(#candle)" opacity=".5"/></g>
    <g id="concierge">
      <ellipse cx="0" cy="6" rx="70" ry="12" fill="#000" opacity=".4"/>
      <path d="M-26 -300 L-34 -10 h22 L0 -200 L12 -10 h22 L26 -300 Z" fill="#111"/>
      <path d="M-14 -10 h-30 v10 h34 z M14 -10 h30 v10 h-34 z" fill="#050505"/>
      <path d="M-60 -560 Q-70 -420 -40 -290 L40 -290 Q70 -420 60 -560 Q0 -590 -60 -560 Z" fill="#9b1c1c" stroke="#5a0d0d" stroke-width="3"/>
      <path d="M0 -580 V-290" stroke="#5a0d0d" stroke-width="3"/>
      <g fill="url(#gold)"><circle cx="-14" cy="-540" r="6"/><circle cx="-14" cy="-500" r="6"/><circle cx="-14" cy="-460" r="6"/><circle cx="-14" cy="-420" r="6"/><circle cx="14" cy="-540" r="6"/><circle cx="14" cy="-500" r="6"/><circle cx="14" cy="-460" r="6"/><circle cx="14" cy="-420" r="6"/></g>
      <path d="M-60 -560 h120" stroke="url(#gold)" stroke-width="8"/>
      <path d="M-58 -550 Q-110 -420 -104 -200" stroke="#9b1c1c" stroke-width="26" fill="none" stroke-linecap="round"/><path d="M58 -550 Q110 -420 104 -200" stroke="#9b1c1c" stroke-width="26" fill="none" stroke-linecap="round"/>
      <g fill="#f8fafc"><ellipse cx="-104" cy="-186" rx="20" ry="26"/><ellipse cx="104" cy="-186" rx="20" ry="26"/><path d="M-116 -170 v40 M-104 -166 v48 M-92 -170 v40 M116 -170 v40 M104 -166 v48 M92 -170 v40" stroke="#f8fafc" stroke-width="8" stroke-linecap="round"/></g>
      <path d="M-10 -600 v-24 h20 v24" fill="#e7d9c4"/>
      <ellipse cx="0" cy="-660" rx="44" ry="56" fill="#efe5d6" stroke="#bfae96" stroke-width="2"/>
      <path d="M-18 -660 q4 4 8 0 M10 -660 q4 4 8 0 M-20 -636 Q0 -616 20 -636" stroke="#bfae96" stroke-width="3" fill="none" opacity=".6"/>
      <rect x="-34" y="-736" width="68" height="34" rx="4" fill="#9b1c1c"/><rect x="-36" y="-708" width="72" height="8" fill="url(#gold)"/><rect x="-6" y="-750" width="12" height="16" fill="url(#gold)"/>
    </g>
    <g id="manq">
      <ellipse cx="0" cy="4" rx="50" ry="10" fill="#000" opacity=".35"/>
      <path d="M-18 -200 L-26 0 h16 L0 -130 L10 0 h16 L18 -200 Z" fill="#1f2937"/>
      <path d="M-40 -380 Q-46 -280 -24 -200 L24 -200 Q46 -280 40 -380 Q0 -400 -40 -380 Z" fill="#1f2937"/>
      <path d="M-12 -380 L0 -330 L12 -380" fill="#f8fafc"/><path d="M-6 -360 l6 10 l6 -10 z" fill="#9b1c1c"/>
      <path d="M-40 -370 Q-70 -300 -60 -230" stroke="#1f2937" stroke-width="16" fill="none" stroke-linecap="round"/><path d="M40 -370 Q70 -300 60 -230" stroke="#1f2937" stroke-width="16" fill="none" stroke-linecap="round"/>
      <circle cx="-60" cy="-226" r="10" fill="#e8dccb"/><circle cx="60" cy="-226" r="10" fill="#e8dccb"/>
      <rect x="-8" y="-404" width="16" height="20" fill="#e8dccb"/>
      <ellipse cx="0" cy="-440" rx="30" ry="38" fill="#e8dccb"/><path d="M-14 -430 Q0 -418 14 -430" stroke="#9b8a72" stroke-width="2.5" fill="none"/>
    </g>
    <g id="manqd">
      <ellipse cx="0" cy="4" rx="70" ry="12" fill="#000" opacity=".35"/>
      <path d="M-30 -260 Q-90 -60 -80 0 H80 Q90 -60 30 -260 Z" fill="#7c3aed"/><path d="M-30 -260 Q-60 -120 -40 0" stroke="#6d28d9" stroke-width="4" fill="none"/>
      <path d="M-30 -380 Q-36 -300 -26 -260 L26 -260 Q36 -300 30 -380 Q0 -396 -30 -380 Z" fill="#7c3aed"/>
      <path d="M-30 -370 Q-66 -300 -56 -240" stroke="#e8dccb" stroke-width="10" fill="none" stroke-linecap="round"/><path d="M30 -370 Q66 -300 56 -240" stroke="#e8dccb" stroke-width="10" fill="none" stroke-linecap="round"/>
      <rect x="-7" y="-402" width="14" height="22" fill="#e8dccb"/>
      <ellipse cx="0" cy="-436" rx="28" ry="36" fill="#e8dccb"/><path d="M-12 -426 Q0 -414 12 -426" stroke="#9b8a72" stroke-width="2.5" fill="none"/>
    </g>
'''

def svg(extra_defs, body):
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 900">\n  <defs>\n' + COMMON + extra_defs +
            '  </defs>\n' + body + '  <rect width="1600" height="900" fill="url(#vign)"/>\n</svg>\n')

def frame(x, y, w, h, inner):
    return f'<g><rect x="{x}" y="{y}" width="{w}" height="{h}" fill="url(#gold)"/><rect x="{x + 10}" y="{y + 10}" width="{w - 20}" height="{h - 20}" fill="#1a0f0a"/>{inner}</g>'

def portrait(x, y, w, h):
    cx, cy = x + w / 2, y + h / 2
    return frame(x, y, w, h, f'<ellipse cx="{cx}" cy="{cy - h * .05:.0f}" rx="{w * .2:.0f}" ry="{h * .22:.0f}" fill="#d8c8ae"/>'
                 f'<path d="M{cx - w * .3:.0f} {y + h - 10} Q{cx} {cy + h * .1:.0f} {cx + w * .3:.0f} {y + h - 10} Z" fill="#2a1a12"/>'
                 f'<path d="M{cx - w * .1:.0f} {cy:.0f} Q{cx} {cy + h * .08:.0f} {cx + w * .1:.0f} {cy:.0f}" stroke="#5a3a2a" stroke-width="3" fill="none"/>')

ART = {}
# --- hotel front, arriving ---
ART['art_h_arrive'] = svg('''    <linearGradient id="night" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#05070f"/><stop offset="1" stop-color="#1a1428"/></linearGradient>
''', '''  <rect width="1600" height="900" fill="url(#night)"/>
  ''' + ''.join(f'<circle cx="{random.randint(0, 1600)}" cy="{random.randint(0, 260)}" r="{random.choice((1, 1.5, 2))}" fill="#fff" opacity=".5"/>' for _ in range(60)) + '''
  <!-- the hotel building -->
  <rect x="260" y="140" width="1080" height="620" fill="#3a2a22"/><rect x="260" y="140" width="1080" height="30" fill="#2a1e18"/>
  ''' + ''.join(f'<rect x="{x}" y="{y}" width="70" height="90" fill="{random.choice(("#1a1208", "#1a1208", "#f6d27a", "#1a1208"))}" stroke="#5a4636" stroke-width="6"/>' for y in (200, 330) for x in range(300, 1300, 110)) + '''
  <!-- glowing sign -->
  <rect x="520" y="60" width="560" height="100" rx="12" fill="#1a0a0a" stroke="url(#gold)" stroke-width="6"/>
  <text x="800" y="128" font-family="Georgia, serif" font-size="60" font-weight="bold" text-anchor="middle" fill="#ffcf5a" filter="url(#hglow)">GRAND HOTEL</text>
  <!-- awning and revolving door -->
  <path d="M560 470 h480 l40 60 h-560 z" fill="#9b1c1c"/><path d="M560 470 h480" stroke="url(#gold)" stroke-width="6"/>
  <rect x="640" y="530" width="320" height="230" fill="#0d0a08"/><rect x="660" y="540" width="280" height="220" fill="#f6d27a" opacity=".3"/>
  <path d="M800 540 v220 M700 560 l200 180 M900 560 l-200 180" stroke="url(#gold)" stroke-width="6"/>
  <!-- banner -->
  <rect x="300" y="560" width="300" height="80" fill="#f3e9d2"/><text x="450" y="594" font-family="Georgia, serif" font-size="22" text-anchor="middle" fill="#5a0d0d">CHECK-IN ANYTIME</text><text x="450" y="626" font-family="Georgia, serif" font-size="22" text-anchor="middle" fill="#5a0d0d">CHECK-OUT NEVER =)</text>
  <!-- steps, lamps and the carpet -->
  <rect x="600" y="760" width="400" height="20" fill="#5a4636"/><rect x="570" y="780" width="460" height="20" fill="#4a3a2c"/><polygon points="700,800 900,800 1040,900 560,900" fill="url(#hcarpet)"/>
  <g><rect x="520" y="600" width="12" height="200" fill="#222"/><circle cx="526" cy="590" r="24" fill="#fff1b8" filter="url(#hglow)"/><rect x="1068" y="600" width="12" height="200" fill="#222"/><circle cx="1074" cy="590" r="24" fill="#fff1b8" filter="url(#hglow)"/></g>
  <rect y="800" width="1600" height="100" fill="#0f0d14"/>
''')
# --- lobby (hub) ---
ART['art_h_lobby'] = svg('', '''  <rect width="1600" height="560" fill="url(#hwall)"/>
  <rect y="540" width="1600" height="30" fill="#2a0c10"/><rect y="560" width="1600" height="340" fill="url(#hcarpet)"/>
  <rect y="0" width="1600" height="40" fill="#2a0c10"/><path d="M0 40 h1600" stroke="url(#gold)" stroke-width="6"/>
  <use href="#chand" transform="translate(800 40)"/>
  <!-- grand staircase on the left -->
  <g>''' + ''.join(f'<rect x="{60 + i * 22}" y="{560 - i * 34}" width="{300 - i * 22}" height="34" fill="#4a1a1e" stroke="#2a0c10" stroke-width="3"/>' for i in range(12)) + '''
    <path d="M60 560 L330 152" stroke="url(#gold)" stroke-width="8"/><path d="M360 560 L600 152" stroke="url(#gold)" stroke-width="8" opacity=".7"/></g>
  <!-- front desk with bell and guest book -->
  <rect x="600" y="430" width="400" height="150" fill="#3a1a0e"/><rect x="590" y="420" width="420" height="20" fill="url(#gold)"/>
  <rect x="620" y="460" width="360" height="100" fill="#4a2414"/><text x="800" y="525" font-family="Georgia, serif" font-size="30" text-anchor="middle" fill="url(#gold)">RECEPTION</text>
  <g transform="translate(900 418)"><ellipse rx="26" ry="6" fill="#8a6410"/><path d="M-22 0 Q0 -40 22 0 Z" fill="url(#gold)"/><circle cy="-34" r="5" fill="url(#gold)"/></g>
  <g transform="translate(680 410) rotate(-4)"><rect x="-50" y="-8" width="100" height="16" fill="#e7dcc6"/><path d="M0 -8 v16" stroke="#7a1f2b" stroke-width="3"/></g>
  <!-- key hooks behind the desk, all empty but one -->
  <rect x="660" y="250" width="280" height="120" fill="#3a1a0e" stroke="url(#gold)" stroke-width="4"/>
  ''' + ''.join(f'<circle cx="{690 + (i % 7) * 37}" cy="{280 + (i // 7) * 50}" r="5" fill="url(#gold)"/>' for i in range(14)) + '''
  <g transform="translate(764 330)"><path d="M0 0 v14" stroke="url(#gold)" stroke-width="3"/><circle cy="20" r="7" fill="none" stroke="url(#gold)" stroke-width="3"/><rect x="-10" y="26" width="20" height="14" fill="#9b1c1c"/></g>
  <!-- elevator doors on the right -->
  <rect x="1180" y="220" width="260" height="340" fill="url(#gold)"/><rect x="1196" y="236" width="228" height="324" fill="#6b5a3a"/><path d="M1310 236 v324" stroke="#3a2a1a" stroke-width="4"/>
  <path d="M1250 190 a60 30 0 0 1 120 0" fill="none" stroke="url(#gold)" stroke-width="6"/><path d="M1310 190 l30 -20" stroke="#111" stroke-width="4"/>
  <g font-family="Georgia, serif" font-size="16" fill="#111"><text x="1252" y="186">L</text><text x="1280" y="172">2</text><text x="1306" y="166">3</text><text x="1340" y="172">B</text></g>
  <rect x="1452" y="370" width="30" height="60" rx="6" fill="#3a2a1a"/><circle cx="1467" cy="390" r="7" fill="#7a1f2b"/><circle cx="1467" cy="412" r="7" fill="#444"/>
  <!-- ballroom doors at the back, paintings, plants -->
  <rect x="440" y="300" width="130" height="250" fill="#2a0c10" stroke="url(#gold)" stroke-width="5"/><path d="M505 300 v250" stroke="url(#gold)" stroke-width="3"/>
  <text x="505" y="290" font-family="Georgia, serif" font-size="20" text-anchor="middle" fill="url(#gold)">BALLROOM</text>
  ''' + portrait(1040, 150, 110, 140) + portrait(1460, 130, 100, 130) + '''
  <g transform="translate(1080 560)"><path d="M-30 0 h60 l-10 -50 h-40 z" fill="#3a2a1a"/><path d="M0 -50 q-40 -60 -60 -60 M0 -50 q10 -80 30 -100 M0 -50 q40 -40 60 -40" stroke="#14532d" stroke-width="12" fill="none" stroke-linecap="round"/></g>
  <!-- luggage cart left in the middle of the lobby -->
  <g transform="translate(980 760)"><path d="M-80 0 h160" stroke="url(#gold)" stroke-width="8"/><path d="M-70 0 v-160 a70 40 0 0 1 140 0 v160" stroke="url(#gold)" stroke-width="6" fill="none"/>
    <rect x="-60" y="-70" width="70" height="60" fill="#7a1f2b"/><rect x="0" y="-120" width="56" height="110" fill="#3b2a1a"/><circle cx="-60" cy="12" r="12" fill="#111"/><circle cx="60" cy="12" r="12" fill="#111"/></g>
''')
# --- concierge at the desk ---
ART['art_h_desk'] = svg('', '''  <rect width="1600" height="900" fill="url(#hwall)"/>
  <rect y="0" width="1600" height="40" fill="#2a0c10"/><path d="M0 40 h1600" stroke="url(#gold)" stroke-width="6"/>
  <rect x="460" y="120" width="680" height="300" fill="#3a1a0e" stroke="url(#gold)" stroke-width="5"/>
  ''' + ''.join(f'<circle cx="{510 + (i % 12) * 52}" cy="{170 + (i // 12) * 80}" r="7" fill="url(#gold)"/>' for i in range(36)) + '''
  <use href="#concierge" transform="translate(800 900) scale(1.05)"/>
  <rect x="0" y="640" width="1600" height="260" fill="#3a1a0e"/><rect x="0" y="626" width="1600" height="24" fill="url(#gold)"/>
  <text x="800" y="780" font-family="Georgia, serif" font-size="54" text-anchor="middle" fill="url(#gold)">RECEPTION</text>
  <g transform="translate(1120 624)"><ellipse rx="40" ry="9" fill="#8a6410"/><path d="M-34 0 Q0 -60 34 0 Z" fill="url(#gold)"/><circle cy="-52" r="8" fill="url(#gold)"/></g>
  <g transform="translate(420 620) rotate(-6)"><rect x="-90" y="-14" width="180" height="28" fill="#e7dcc6"/><path d="M0 -14 v28" stroke="#7a1f2b" stroke-width="4"/></g>
  <rect x="1300" y="560" width="60" height="70" fill="#f3e9d2"/><text x="1330" y="604" font-family="Georgia, serif" font-size="16" text-anchor="middle" fill="#5a0d0d">RING</text>
''')
# --- ballroom ---
dancers = ''
for i, (x, y, s, kind, rot) in enumerate(((330, 760, .9, 'manq', -6), (460, 770, .9, 'manqd', 8), (760, 730, .7, 'manq', 4), (860, 735, .7, 'manqd', -6),
                                         (1160, 770, .95, 'manq', 6), (1290, 765, .95, 'manqd', -8), (600, 680, .5, 'manqd', 0), (1000, 680, .5, 'manq', 0))):
    dancers += f'<use href="#{kind}" transform="translate({x} {y}) scale({s}) rotate({rot})"/>'
ART['art_h_ballroom'] = svg('''    <pattern id="parquet" width="80" height="40" patternUnits="userSpaceOnUse"><rect width="80" height="40" fill="#6b4320"/><rect width="40" height="20" fill="#7a4e26"/><rect x="40" y="20" width="40" height="20" fill="#7a4e26"/></pattern>
''', '''  <rect width="1600" height="600" fill="#3a1418"/>
  ''' + ''.join(f'<rect x="{x}" y="60" width="60" height="540" fill="#4a1a1e"/><rect x="{x + 6}" y="60" width="8" height="540" fill="url(#gold)" opacity=".5"/>' for x in range(40, 1600, 220)) + '''
  <rect y="600" width="1600" height="300" fill="url(#parquet)"/>
  <use href="#chand" transform="translate(400 0) scale(.8)"/><use href="#chand" transform="translate(1200 0) scale(.8)"/><use href="#chand" transform="translate(800 0) scale(1.1)"/>
  <!-- stage with a band of mannequins and a piano -->
  <rect x="560" y="430" width="480" height="70" fill="#2a0c10"/><rect x="560" y="420" width="480" height="14" fill="url(#gold)"/>
  <path d="M520 120 Q560 300 560 430 L520 430 Z M1080 120 Q1040 300 1040 430 L1080 430 Z" fill="#9b1c1c"/>
  <use href="#manq" transform="translate(640 430) scale(.45)"/><use href="#manq" transform="translate(960 430) scale(.45)"/>
  <g transform="translate(800 420)"><path d="M-90 0 v-60 q0 -40 60 -40 h90 q30 0 30 30 v70" fill="#0b0b0b"/><rect x="-90" y="-30" width="180" height="12" fill="#f8fafc"/><g fill="#0b0b0b">''' + ''.join(f'<rect x="{-84 + k * 12}" y="-30" width="6" height="7"/>' for k in range(15)) + '''</g>
    <rect x="-20" y="-80" width="44" height="30" fill="#f3e9d2"/><g stroke="#111" stroke-width="1.5"><path d="M-16 -72 h36 M-16 -66 h36 M-16 -60 h36"/></g><text x="2" y="-55" font-family="Georgia" font-size="12" text-anchor="middle" fill="#7a1f2b">4 1 7</text></g>
  <!-- round tables with candles and almond water -->
  <g><ellipse cx="180" cy="640" rx="120" ry="30" fill="#f3e9d2"/><rect x="170" y="640" width="20" height="90" fill="#cfc0a0"/><rect x="150" y="604" width="14" height="30" fill="#bfdbfe"/><circle cx="200" cy="604" r="18" fill="url(#candle)"/></g>
  <g><ellipse cx="1430" cy="640" rx="120" ry="30" fill="#f3e9d2"/><rect x="1420" y="640" width="20" height="90" fill="#cfc0a0"/><circle cx="1400" cy="604" r="18" fill="url(#candle)"/><circle cx="1460" cy="604" r="18" fill="url(#candle)"/></g>
  <!-- the dancers -->
  ''' + dancers + '''
  <!-- numbered dance-floor tiles -->
  <g font-family="Georgia, serif" font-size="30" fill="#f6e27a" opacity=".35"><text x="520" y="860">4</text><text x="800" y="840">1</text><text x="1080" y="870">7</text></g>
''')
# --- floor 2 corridor ---
def hdoor(x, y, w, h, num, side):
    k = 1 if side == 'l' else -1
    pts = f'{x},{y} {x + w},{y + k * h * .06:.0f} {x + w},{y + h - k * h * .06:.0f} {x},{y + h}'
    return (f'<g><polygon points="{pts}" fill="#2a120a" stroke="url(#gold)" stroke-width="4"/>'
            f'<rect x="{x + w * .25:.0f}" y="{y - h * .12:.0f}" width="{w * .5:.0f}" height="{h * .09:.0f}" fill="url(#gold)"/>'
            f'<text x="{x + w * .5:.0f}" y="{y - h * .045:.0f}" font-family="Georgia, serif" font-size="{h * .07:.0f}" text-anchor="middle" fill="#1a0a0a">{num}</text>'
            f'<circle cx="{x + (w * .8 if side == "l" else w * .2):.0f}" cy="{y + h * .55:.0f}" r="{max(4, w * .05):.0f}" fill="url(#gold)"/></g>')
ART['art_h_hall2'] = svg('', '''  <polygon points="0,0 1600,0 980,330 620,330" fill="#2a0c10"/>
  <polygon points="0,0 620,330 620,560 0,900" fill="url(#hwall)"/><polygon points="1600,0 980,330 980,560 1600,900" fill="url(#hwall)"/>
  <polygon points="0,900 620,560 980,560 1600,900" fill="url(#hcarpet)"/>
  <rect x="620" y="330" width="360" height="230" fill="#14070a"/><rect x="760" y="400" width="80" height="160" fill="#2a120a" stroke="url(#gold)" stroke-width="3"/>
  ''' + hdoor(80, 300, 200, 420, '211', 'l') + hdoor(420, 330, 110, 250, '213', 'l') + hdoor(1320, 300, 200, 420, '217', 'r') + hdoor(1070, 330, 110, 250, '215', 'r') + '''
  <!-- wall lamps -->
  <g fill="#fff1b8" filter="url(#hglow)"><circle cx="340" cy="250" r="14"/><circle cx="1260" cy="250" r="14"/><circle cx="580" cy="330" r="8"/><circle cx="1020" cy="330" r="8"/></g>
  <g fill="url(#candle)"><circle cx="340" cy="250" r="80"/><circle cx="1260" cy="250" r="80"/></g>
  <!-- light under door 217, a room service tray, a do-not-disturb sign -->
  <path d="M1330 718 L1510 702" stroke="#ffcf5a" stroke-width="6" filter="url(#hglow)"/>
  <g transform="translate(1180 800)"><ellipse rx="70" ry="16" fill="#cbd5e1"/><path d="M-50 -4 a50 40 0 0 1 100 0" fill="#e2e8f0"/><circle cy="-46" r="6" fill="#94a3b8"/></g>
  <g transform="translate(240 520) rotate(8)"><rect x="-26" y="0" width="52" height="90" rx="6" fill="#f3e9d2"/><circle cy="12" r="10" fill="none" stroke="#7a1f2b" stroke-width="4"/><text y="56" font-family="Georgia" font-size="12" text-anchor="middle" fill="#7a1f2b">DO NOT</text><text y="72" font-family="Georgia" font-size="12" text-anchor="middle" fill="#7a1f2b">DISTURB</text></g>
''')
# --- room 213 ---
ART['art_h_room'] = svg('', '''  <rect width="1600" height="600" fill="url(#hwall)"/><rect y="580" width="1600" height="320" fill="url(#hcarpet)"/><rect y="570" width="1600" height="20" fill="#2a0c10"/>
  <!-- bed with a lumpy pillow -->
  <rect x="420" y="420" width="560" height="260" fill="#f3e9d2"/><rect x="400" y="300" width="600" height="140" fill="#4a1a10" stroke="url(#gold)" stroke-width="4"/>
  <rect x="420" y="520" width="560" height="160" fill="#7a1f2b"/><path d="M420 520 h560" stroke="url(#gold)" stroke-width="4"/>
  <ellipse cx="560" cy="460" rx="110" ry="40" fill="#fffbf0"/><ellipse cx="840" cy="460" rx="110" ry="40" fill="#fffbf0"/>
  <path d="M520 470 q40 -12 80 0" stroke="#d6c7a6" stroke-width="3" fill="none"/><rect x="590" y="476" width="24" height="10" fill="url(#gold)" opacity=".8"/>
  <!-- nightstand, lamp, telephone -->
  <rect x="1020" y="520" width="120" height="160" fill="#3a1a0e"/><path d="M1060 520 v-60 M1040 460 h40 l-10 -50 h-20 z" fill="#f3e9d2" stroke="#3a1a0e" stroke-width="4"/><circle cx="1060" cy="440" r="60" fill="url(#candle)"/>
  <g transform="translate(1110 512)"><rect x="-26" y="-14" width="52" height="16" rx="4" fill="#111"/><path d="M-22 -16 q22 -20 44 0" stroke="#111" stroke-width="8" fill="none"/></g>
  <!-- wardrobe slightly open -->
  <rect x="1200" y="160" width="260" height="520" fill="#3a1a0e" stroke="url(#gold)" stroke-width="4"/><path d="M1330 160 v520" stroke="#1a0a05" stroke-width="4"/>
  <polygon points="1330,160 1400,180 1400,660 1330,680" fill="#0b0503"/><circle cx="1316" cy="420" r="8" fill="url(#gold)"/>
  <g fill="#f8fafc" filter="url(#hglow)" opacity=".7"><circle cx="1352" cy="330" r="3"/><circle cx="1366" cy="330" r="3"/></g>
  <!-- bathroom door with a tub full of almond water -->
  <rect x="80" y="180" width="240" height="500" fill="#e7e1d4" stroke="url(#gold)" stroke-width="4"/>
  <rect x="100" y="200" width="200" height="470" fill="#cbd5e1"/><path d="M110 540 h180 q0 70 -50 70 h-80 q-50 0 -50 -70 z" fill="#f8fafc"/><path d="M118 548 h164" stroke="#93c5fd" stroke-width="10"/>
  <!-- painting, room number, a note on the carpet -->
  ''' + portrait(640, 120, 140, 150) + '''
  <text x="800" y="60" font-family="Georgia, serif" font-size="40" text-anchor="middle" fill="url(#gold)">213</text>
  <g transform="translate(880 790) rotate(-12)"><rect x="-50" y="-30" width="100" height="60" fill="#fef9c3"/><text y="0" font-family="Comic Sans MS, Arial" font-size="14" text-anchor="middle" fill="#111">check under</text><text y="18" font-family="Comic Sans MS, Arial" font-size="14" text-anchor="middle" fill="#111">the pillow</text></g>
''')
# --- floor 3: the hallway that stretches ---
ART['art_h_hall3'] = svg('', '''  <rect width="1600" height="900" fill="#14070a"/>
  ''' + ''.join(f'<rect x="{800 - 760 * (.82 ** i):.0f}" y="{450 - 430 * (.82 ** i):.0f}" width="{1520 * (.82 ** i):.0f}" height="{860 * (.82 ** i):.0f}" fill="none" stroke="url(#gold)" stroke-width="{max(1, 6 * (.82 ** i)):.1f}" opacity="{.25 + .5 * (.82 ** i):.2f}"/>' for i in range(18)) + '''
  <polygon points="0,0 780,440 780,460 0,900" fill="url(#hwall)" opacity=".85"/><polygon points="1600,0 820,440 820,460 1600,900" fill="url(#hwall)" opacity=".85"/>
  <polygon points="0,900 780,460 820,460 1600,900" fill="url(#hcarpet)"/>
  ''' + ''.join(f'<g transform="translate({800 + side * (720 * (.8 ** i)):.0f} {450 - 120 * (.8 ** i):.0f}) scale({.8 ** i:.3f})"><rect x="-40" y="0" width="80" height="220" fill="#2a120a" stroke="url(#gold)" stroke-width="5"/><text y="-12" font-family="Georgia" font-size="26" text-anchor="middle" fill="url(#gold)">3{i:02d}</text></g>' for i in range(1, 12) for side in (-1, 1)) + '''
  <!-- the walls are starting to smile -->
  <g stroke="#1a0a0a" stroke-width="7" fill="none" opacity=".7" stroke-linecap="round">
    <path d="M150 300 v40 M210 300 v40 M130 380 Q180 420 230 380"/><path d="M1390 300 v40 M1450 300 v40 M1370 380 Q1420 420 1470 380"/>
    <path d="M420 400 v22 M452 400 v22 M410 440 Q436 462 462 440" stroke-width="5"/><path d="M1148 400 v22 M1180 400 v22 M1138 440 Q1164 462 1190 440" stroke-width="5"/></g>
  <rect x="700" y="20" width="200" height="40" fill="#1a0a0a" stroke="url(#gold)" stroke-width="3"/><text x="800" y="50" font-family="Georgia" font-size="24" text-anchor="middle" fill="#9b1c1c">FLOOR 3</text>
''')
# --- power room ---
ART['art_h_power'] = svg('', '''  <rect width="1600" height="900" fill="#1c1d22"/><rect y="640" width="1600" height="260" fill="#111216"/>
  ''' + ''.join(f'<rect x="{x}" y="160" width="160" height="420" fill="#2b2f38" stroke="#444a57" stroke-width="4"/><g fill="{random.choice(("#22c55e", "#ef4444", "#facc15"))}">' + ''.join(f'<circle cx="{x + 30 + k * 34}" cy="{200}" r="6"/>' for k in range(4)) + f'</g><g stroke="#111" stroke-width="3">' + ''.join(f'<path d="M{x + 20} {260 + k * 30} h120"/>' for k in range(9)) + '</g>' for x in (120, 320, 1120, 1320)) + '''
  <!-- big lever -->
  <rect x="660" y="240" width="280" height="360" fill="#3a3f4b" stroke="#facc15" stroke-width="6"/><text x="800" y="290" font-family="Arial Black, Arial" font-size="32" text-anchor="middle" fill="#facc15">ELEVATOR</text>
  <rect x="780" y="330" width="40" height="220" fill="#111"/><path d="M800 520 L860 360" stroke="#9ca3af" stroke-width="20" stroke-linecap="round"/><circle cx="860" cy="360" r="26" fill="#ef4444"/>
  <text x="720" y="580" font-family="Arial" font-size="22" fill="#9ca3af">OFF</text><text x="840" y="580" font-family="Arial" font-size="22" fill="#9ca3af">ON</text>
  <!-- cables, sparks, warning stripes, and a single bulb -->
  <g fill="none" stroke="#0b0b0e" stroke-width="12" stroke-linecap="round"><path d="M0 120 Q400 200 660 300"/><path d="M1600 120 Q1200 200 940 300"/><path d="M800 240 V0"/></g>
  <g stroke="#fde047" stroke-width="3"><path d="M620 300 l-20 -20 M620 300 l-26 6 M620 300 l-6 -28"/></g>
  <g>''' + ''.join(f'<path d="M{x} 640 l40 0 l-40 40 l-40 0 z" fill="#facc15"/>' for x in range(0, 1640, 80)) + '''</g>
  <circle cx="800" cy="60" r="16" fill="#fff1b8" filter="url(#hglow)"/><circle cx="800" cy="60" r="200" fill="url(#candle)" opacity=".5"/>
''')
# --- basement stairs with the hound ---
ART['art_h_stairs'] = svg('', '''  <rect width="1600" height="900" fill="#0a0808"/>
  ''' + ''.join(f'<rect x="{300 + i * 30}" y="{120 + i * 52}" width="{1000 - i * 60}" height="52" fill="{"#2a1e18" if i % 2 else "#33251d"}" stroke="#120c0a" stroke-width="3"/>' for i in range(12)) + '''
  <path d="M300 120 L660 744 M1300 120 L940 744" stroke="#5a4636" stroke-width="10"/>
  <rect x="0" y="0" width="300" height="900" fill="#1a1210"/><rect x="1300" y="0" width="300" height="900" fill="#1a1210"/>
  <!-- the hound at the bottom of the stairs -->
  <g transform="translate(800 820)">
    <ellipse rx="220" ry="40" fill="#000" opacity=".6"/>
    <path d="M-200 0 Q-180 -120 -40 -130 Q80 -150 180 -90 Q220 -60 200 0 Z" fill="#0b0808"/>
    <path d="M-170 0 l-30 -70 M-120 0 l-10 -80 M120 0 l20 -80 M170 0 l40 -60" stroke="#0b0808" stroke-width="18" stroke-linecap="round"/>
    <ellipse cx="190" cy="-90" rx="60" ry="44" fill="#0b0808"/>
    <g fill="#f8fafc" filter="url(#hglow)"><circle cx="196" cy="-100" r="7"/><circle cx="226" cy="-96" r="7"/></g>
    <path d="M170 -66 l70 0" stroke="#e5e7eb" stroke-width="4"/>''' + ''.join(f'<path d="M{176 + k * 10} -66 l4 10 l4 -10" fill="#e5e7eb"/>' for k in range(6)) + '''
  </g>
  <rect x="680" y="760" width="240" height="20" fill="#9b1c1c" opacity=".0"/>
  <text x="800" y="90" font-family="Georgia" font-size="28" text-anchor="middle" fill="#9b1c1c" opacity=".7">BASEMENT</text>
  <g fill="#fff1b8" filter="url(#hglow)" opacity=".6"><circle cx="420" cy="200" r="8"/></g><circle cx="420" cy="200" r="120" fill="url(#candle)" opacity=".35"/>
''')
# --- boiler room door + keypad ---
ART['art_h_boilerdoor'] = svg('', '''  <rect width="1600" height="900" fill="#18120e"/><rect y="680" width="1600" height="220" fill="#0e0a08"/>
  ''' + ''.join(f'<rect x="0" y="{y}" width="1600" height="{h}" fill="#3a2418"/><rect x="0" y="{y + 3}" width="1600" height="{h // 4}" fill="#6b4226" opacity=".5"/>' for y, h in ((80, 40), (150, 26))) + '''
  <!-- the heavy door -->
  <rect x="560" y="200" width="480" height="480" fill="#5a1414" stroke="#2a0606" stroke-width="10"/>
  ''' + ''.join(f'<circle cx="{x}" cy="{y}" r="7" fill="#2a0606"/>' for x in (580, 1020) for y in range(230, 680, 50)) + '''
  <rect x="600" y="240" width="400" height="60" fill="#facc15"/><text x="800" y="282" font-family="Arial Black, Arial" font-size="34" text-anchor="middle" fill="#111">BOILER ROOM</text>
  <text x="800" y="360" font-family="Arial Black, Arial" font-size="22" text-anchor="middle" fill="#fca5a5">EMPLOYEES ONLY</text>
  <g transform="translate(700 500)"><circle r="36" fill="url(#gold)"/><path d="M-6 -10 a10 10 0 1 1 12 0 l6 30 h-24 z" fill="#1a0a0a"/></g>
  <!-- keypad -->
  <g transform="translate(900 470)"><rect x="-60" y="-80" width="120" height="170" rx="8" fill="#1f2937" stroke="#9ca3af" stroke-width="4"/><rect x="-46" y="-66" width="92" height="30" fill="#052e16"/><text x="0" y="-44" font-family="monospace" font-size="20" text-anchor="middle" fill="#4ade80">_ _ _</text>
    ''' + ''.join(f'<rect x="{-42 + (k % 3) * 30}" y="{-26 + (k // 3) * 28}" width="24" height="22" rx="3" fill="#374151"/><text x="{-30 + (k % 3) * 30}" y="{-10 + (k // 3) * 28}" font-family="monospace" font-size="14" text-anchor="middle" fill="#e5e7eb">{(k + 1) % 10}</text>' for k in range(10)) + '''</g>
  <!-- steam, pipes, a pressure gauge in the red, puddles -->
  <rect x="200" y="0" width="50" height="680" fill="#6b4226"/><rect x="1350" y="0" width="60" height="680" fill="#6b4226"/>
  <g transform="translate(260 420)"><circle r="46" fill="#3a2418"/><circle r="38" fill="#f5efe0"/><path d="M0 0 L26 -24" stroke="#b91c1c" stroke-width="5"/><circle r="5" fill="#111"/></g>
  <g fill="#e7e1d4" opacity=".35" filter="url(#hblur)"><ellipse cx="1380" cy="300" rx="120" ry="50"/><ellipse cx="230" cy="200" rx="110" ry="40"/></g>
  <ellipse cx="800" cy="760" rx="260" ry="26" fill="#2a1a12"/>
''')
# --- boiler room with the concierge waiting ---
ART['art_h_boiler'] = svg('''    <radialGradient id="fire"><stop offset="0" stop-color="#fff1b8"/><stop offset=".4" stop-color="#ff8a00"/><stop offset="1" stop-color="#7a1400" stop-opacity="0"/></radialGradient>
''', '''  <rect width="1600" height="900" fill="#1a0d08"/><rect y="700" width="1600" height="200" fill="#0e0705"/>
  <!-- the giant boiler -->
  <rect x="340" y="140" width="560" height="560" rx="80" fill="#4a2a1a" stroke="#2a1208" stroke-width="10"/>
  ''' + ''.join(f'<path d="M340 {y} h560" stroke="#2a1208" stroke-width="8"/>' for y in range(220, 700, 90)) + '''
  <circle cx="620" cy="520" r="120" fill="#2a1208"/><circle cx="620" cy="520" r="100" fill="url(#fire)"/>
  <g stroke="#2a1208" stroke-width="10"><path d="M520 520 h200 M620 420 v200 M550 450 l140 140 M690 450 l-140 140"/></g>
  <g transform="translate(780 260)"><circle r="50" fill="#2a1208"/><circle r="42" fill="#f5efe0"/><path d="M0 0 L30 -26" stroke="#b91c1c" stroke-width="6"/><circle r="6" fill="#111"/></g>
  <g fill="none" stroke="#6b4226" stroke-width="40"><path d="M620 140 V0"/><path d="M900 300 H1600"/><path d="M340 400 H0"/></g>
  <g fill="#e7e1d4" opacity=".35" filter="url(#hblur)"><ellipse cx="640" cy="80" rx="140" ry="50"/><ellipse cx="1100" cy="290" rx="120" ry="40"/></g>
  <!-- the real exit -->
  <rect x="1260" y="380" width="220" height="320" fill="#9ca3af" stroke="#4b5563" stroke-width="8"/><rect x="1270" y="330" width="200" height="44" fill="#052e16"/>
  <text x="1370" y="362" font-family="Arial Black, Arial" font-size="30" text-anchor="middle" fill="#4ade80" filter="url(#hglow)">EXIT</text><circle cx="1450" cy="550" r="10" fill="#374151"/>
  <!-- the concierge waiting beside it -->
  <use href="#concierge" transform="translate(1100 760) scale(.78)"/>
  <ellipse cx="800" cy="780" rx="500" ry="40" fill="#ff8a00" opacity=".12"/>
''')
# --- elevator inside ---
ART['art_h_elevator'] = svg('', '''  <rect width="1600" height="900" fill="#3a2a1a"/>
  <rect x="200" y="60" width="1200" height="780" fill="url(#gold)"/><rect x="220" y="80" width="1160" height="740" fill="#5a3a1e"/>
  ''' + ''.join(f'<rect x="{x}" y="120" width="160" height="660" fill="#6b4626" stroke="#3a2412" stroke-width="4"/>' for x in range(260, 1360, 220)) + '''
  <rect x="220" y="700" width="1160" height="120" fill="url(#hcarpet)"/>
  <rect x="1180" y="260" width="140" height="320" rx="10" fill="#2a1a0e" stroke="url(#gold)" stroke-width="5"/>
  <g font-family="Georgia, serif" font-size="30" text-anchor="middle">''' + ''.join(f'<circle cx="1250" cy="{320 + k * 62}" r="24" fill="{"#fde68a" if lbl == "B" else "url(#gold)"}" stroke="#3a2412" stroke-width="3"/><text x="1250" y="{331 + k * 62}" fill="#1a0a0a">{lbl}</text>' for k, lbl in enumerate(('3', '2', 'L', 'B'))) + '''</g>
  <rect x="640" y="90" width="320" height="60" fill="#111"/><text x="800" y="134" font-family="monospace" font-size="40" text-anchor="middle" fill="#ef4444" filter="url(#hglow)">L</text>
  <g fill="#fff1b8" filter="url(#hglow)"><rect x="600" y="80" width="400" height="6"/></g>
  <text x="420" y="660" font-family="Georgia" font-size="24" fill="#3a2412" opacity=".8">please enjoy your stay =)</text>
''')

for name, s in ART.items():
    open(os.path.join(D, name + '.svg'), 'w', encoding='utf8').write(s)

# ======================= PASSAGES =======================
VR = (58, 12, .8)     # virus on the right
VL = (-6, 14, .75)    # virus on the left
P = []
# reading and dead-end "look" scenes don't cost sanity, so going back and forth around the hub isn't punished
NODRAIN = {'Hotel Guest Book', 'Hotel Elevator Dead', 'Hotel Room 213 Locked', 'Hotel Room 211 Off', 'Hotel Room 217 Note',
           'Hotel Power On', 'Hotel Concierge Key', 'Hotel Room 213 Phone'}
def add(name, body, tags=''):
    if name in NODRAIN:
        tags = (tags + ' nodrain').strip()
    P.append(f':: {name}{" [" + tags + "]" if tags else ""}\n{body}\n')

add('Hotel Arrival', '<<set $virusWith to true>>' + scene('art_h_arrive', VL) + '\n' + story(
    'You crawl out of a vent into the cold night air. Across the street is a huge old hotel, every window glowing gold.',
    'Level 5: The Grand Hotel. A banner over the door says CHECK-IN ANYTIME. CHECK-OUT NEVER. =)',
    '"The real exit is in there," the virus says. "Down in the boiler room. I have smelled it before. But the door will be locked."') + '\n' +
    choices('[[Push through the revolving door|Hotel Lobby]]'))

add('Hotel Lobby', withVirus('art_h_lobby', VR) + '\n' + story(
    'The lobby is enormous. A chandelier the size of a car hangs over a red carpet that goes on and on.',
    'There is a reception desk with a little gold bell, a grand staircase, an elevator, and tall doors marked BALLROOM. Music drifts out from behind them.',
    '<<if $power>>The elevator light is on now.<<else>>The elevator is dark. Its OUT OF ORDER sign is swinging slowly, even though there is no wind.<</if>>',
    V('The virus bows. Then it keeps low, sniffing the carpet. "Find the brass key," it whispers. "And find out the code."', 'You are alone. The music gets louder, like it noticed.')) + '\n' +
    choices(pickup('wlobby', 'almond', 'Check the luggage cart for almond water'), '[[Go to the front desk|Hotel Front Desk]]', '[[Read the guest book|Hotel Guest Book]]', '[[Go into the ballroom|Hotel Ballroom]]',
            '[[Climb the grand staircase|Hotel Staircase]]',
            '<<if $power>>[[Take the elevator|Hotel Elevator]]<<else>>[[Press the elevator button|Hotel Elevator Dead]]<</if>>'), 'hotel')

add('Hotel Guest Book', withVirus('art_h_desk', VL) + '\n' + story(
    'The guest book is open. Most pages are blank. The last few have notes scribbled in different handwriting:',
    '"Room 211: whatever you do, DON\'T watch the TV."',
    '"Room 217: it sounds like someone you know. DO NOT ANSWER."',
    '"Floor 3: if the hallway gets longer, walk BACKWARDS."',
    '"The boiler room key is where you sleep. (213)"',
    '"The band knows the code. Listen to the band."',
    'The very last line is fresh, the ink still wet: "Welcome back. =)"') + '\n' +
    choices('[[Back to the lobby|Hotel Lobby]]'), 'hotel')

add('Hotel Front Desk', withVirus('art_h_desk', VL) + '\n' + story(
    'Nobody is behind the desk. Behind it, rows and rows of gold key hooks, all empty.',
    'A little card next to the bell says: RING ONCE FOR SERVICE. ONLY ONCE.',
    'Someone has scratched words into the wood of the desk: ASK NICELY.') + '\n' +
    choices('[[Ring the bell|Hotel Concierge]]', '[[Back to the lobby|Hotel Lobby]]'), 'hotel')

add('Hotel Concierge', '<<set $bell to ($bell || 0) + 1>>' + scene('art_h_desk') + '\n' + story(
    '<<if $bell gt 1>>DING. Again.<<else>>DING.<</if>>',
    'Something stands up from behind the desk. It keeps standing up. It is very, very tall, in a red uniform with gold buttons. Its face is smooth like an egg, except for a faint painted smile.',
    '"Welcome to the Grand Hotel," it says, though its mouth does not move. "How may I help you, guest? =)"') + '\n' +
    '<<if $bell gt 1>>' + choices('[[...|Bell Ending]]') + '<<else>>' +
    choices('<<if !setup.isTaken("roomkey")>><<link "Ask politely for a room" "Hotel Concierge Key">><<run setup.take("roomkey","roomkey")>><</link>><</if>>',
            '[[Ask where the exit is|Checkout Ending]]', '[[Ring the bell again|Bell Ending]]', '[[Back away slowly|Hotel Lobby]]') + '<</if>>', 'hotel')

add('Hotel Concierge Key', scene('art_h_desk') + '\n' + story(
    '"Of course," it says. One long white glove slides a key across the desk. Room 213.',
    '<<if setup.has("roomkey")>>You put the key in your inventory.<<else>>Your pockets are full. The key clatters onto the desk. You can come back for it after you make room.<</if>>',
    '"Enjoy your stay. Forever." It sinks back down behind the desk until you can\'t see it anymore.') + '\n' +
    choices('<<if !setup.has("roomkey")>><<link "Pick up the key" "Hotel Concierge Key">><<run setup.addItem("roomkey")>><</link>><</if>>', '[[Back to the lobby|Hotel Lobby]]'), 'hotel')

add('Hotel Ballroom', withVirus('art_h_ballroom', VR) + '\n' + story(
    'The ballroom is full of dancers. They are mannequins: smooth faces, painted smiles, perfect suits and gowns. They waltz in slow circles without making a sound.',
    'On the stage, a band of mannequins sits frozen around a black piano. There is sheet music on the piano.',
    'Round tables line the walls, set with candles and glasses.') + '\n' +
    choices(pickup('wball', 'almond', 'Search the tables for almond water'), '[[Sneak along the wall to the stage|Hotel Stage]]',
            '[[Join the dance|Hotel Dance]]', '[[Back to the lobby|Hotel Lobby]]'), 'hotel')

add('Hotel Dance', '<<set $sanity to Math.max(1, $sanity - 20)>><<set $knowCode to true>>' + scene('art_h_ballroom') + '\n' + story(
    'A cold hand takes yours. Then you are spinning, round and round, faster and faster.',
    'The music gets inside your head. You feel your mind slipping. (-20 sanity)',
    'But as you spin you notice something: the dancers only ever step on three numbered tiles. <<print setup.codeWords()>> <<print setup.codeWords()>>') + '\n' +
    choices('[[Pull free and stumble out of the dance|Hotel Ballroom]]'), 'hotel')

add('Hotel Stage', scene('art_h_ballroom') + '\n' + story(
    'You creep up the steps. The sheet music has three big numbers written at the top: <b><<print setup.codeStr()>></b>.',
    'The moment you touch it, the music STOPS. Every dancer turns its head toward you at exactly the same time.') + '\n' +
    timed(3, ['<<link "Grab the sheet music and run" "Hotel Lobby">><<run setup.addItem("sheet")>><<set $knowCode to true>><</link>>',
              '[[Freeze and pretend to be a mannequin|Dance Forever Ending]]'], 'They grab you', 'Dance Forever Ending'), 'hotel')

add('Hotel Elevator Dead', scene('art_h_lobby') + '\n' + story(
    'You press the button. Nothing. Then, very faintly, from inside the shaft, someone presses it back.',
    'A sticker on the panel says: POWER CONTROLS - FLOOR 3.') + '\n' +
    choices('<<if setup.has("crowbar")>>[[Pry the elevator doors open with the crowbar|Hotel Elevator Shaft]]<</if>>', '[[Back to the lobby|Hotel Lobby]]'), 'hotel')

add('Hotel Elevator Shaft', scene('art_h_stairs') + '\n' + story(
    'You force the crowbar between the doors and lean on it until they grind open.',
    'No elevator. Just a dark shaft and thick greasy cables going all the way down.',
    'At the very bottom you can see a faint light and the word BASEMENT.') + '\n' +
    choices('[[Climb down the cables|Hotel Boiler Door]]', '[[Back to the lobby|Hotel Lobby]]'), 'hotel')

add('Hotel Staircase', withVirus('art_h_lobby', VR) + '\n' + story(
    'The grand staircase splits in three directions.',
    'Up to FLOOR 2. Further up to FLOOR 3, where the sign has been crossed out with red paint. And a narrow service stair going down to the BASEMENT.',
    '<<if !setup.isTaken("axe")>>On the landing there is a red glass case: FIRE AXE. IN CASE OF EMERGENCY, BREAK GLASS.<<else>>The fire axe case is empty and broken.<</if>>') + '\n' +
    choices(pickup('axe', 'axe', 'Break the glass and take the fire axe'), '[[Floor 2|Hotel Floor 2]]', '[[Floor 3|Hotel Floor 3]]', '[[Down to the basement|Hotel Basement Stairs]]', '[[Back to the lobby|Hotel Lobby]]'), 'hotel')

add('Hotel Floor 2', withVirus('art_h_hall2', (36, 22, .6)) + '\n' + story(
    'A long hallway of doors. Room 211. Room 213. Room 215 has no handle. Room 217 has light shining under the door... and knocking coming from inside.',
    'A room service tray sits on the carpet. The food on it is still warm.') + '\n' +
    choices('[[Room 211|Hotel Room 211]]',
            '<<if setup.has("roomkey")>>[[Unlock Room 213|Hotel Room 213]]<<elseif setup.has("crowbar")>>[[Pry open Room 213 with the crowbar|Hotel Room 213]]<<else>>[[Try Room 213|Hotel Room 213 Locked]]<</if>>',
            '<<if setup.has("crowbar")>>[[Pry open Room 215 with the crowbar|Hotel Room 215]]<</if>>', '[[Room 217|Hotel Room 217]]', '[[Back to the stairs|Hotel Staircase]]'), 'hotel')

add('Hotel Room 215', scene('art_h_room') + '\n' + story(
    'Room 215 has no handle because it is not a guest room. It is the maid\'s closet.',
    'Shelves of towels, tiny soaps, and a cleaning cart. Pinned to the wall is a staff notice:',
    '"STAFF REMINDER: the boiler code is the same as the band\'s song. Do NOT tell the guests."') + '\n' +
    choices(pickup('w215', 'almond', 'Take a bottle of almond water from the cart'), '[[Back to the hallway|Hotel Floor 2]]'), 'hotel')

add('Hotel Room 213 Locked', scene('art_h_hall2') + '\n' + story(
    'Locked. A little gold plate on the door says: KEYS AVAILABLE AT RECEPTION.') + '\n' +
    choices('[[Back to the hallway|Hotel Floor 2]]'), 'hotel')

add('Hotel Room 211', scene('art_h_room') + '\n' + story(
    'The room is dark except for an old TV playing static. The static is moving in shapes, like it is trying to show you something.',
    'You can almost see a face in it. A smiling face. It is getting clearer.') + '\n' +
    choices('[[Keep watching|Static Ending]]', '[[Turn off the TV|Hotel Room 211 Off]]'), 'hotel')

add('Hotel Room 211 Off', scene('art_h_room') + '\n' + story(
    'Click. The room goes quiet. Taped to the back of the TV is a note:',
    '"The power room is on floor 3. The hallway will try to keep you. Don\'t walk forward. WALK BACKWARDS."') + '\n' +
    choices('[[Back to the hallway|Hotel Floor 2]]'), 'hotel')

add('Hotel Room 217', scene('art_h_hall2') + '\n' + story(
    'Knock. Knock. Knock.',
    'A voice from inside. It sounds exactly like Theo. "Hey! It\'s me! Let me in, quick, before it comes back!"',
    V('The virus\'s tendrils go stiff. "That is not your friend," it whispers.', 'But Theo is not here. Is he?')) + '\n' +
    choices('[[Open the door|Knock Ending]]', '[[Knock back three times|Hotel Room 217 Note]]', '[[Walk away|Hotel Floor 2]]'), 'hotel')

add('Hotel Room 217 Note', scene('art_h_hall2') + '\n' + story(
    'Knock. Knock. Knock.',
    'The voice stops. After a long time, a folded note slides out under the door:',
    '"you passed the test. the boiler code is the song the band plays. 3 numbers. the dancers know it too, but dancing costs you."') + '\n' +
    choices('[[Back to the hallway|Hotel Floor 2]]'), 'hotel')

add('Hotel Room 213', withVirus('art_h_room', (54, 16, .7)) + '\n' + story(
    'Room 213 is neat and quiet. A made bed, a phone, a wardrobe with its door open a crack.',
    'In the bathroom, the bathtub is full to the top with almond water.',
    'Something hard is under one of the pillows.') + '\n' +
    choices('<<if !setup.isTaken("bathtub")>><span id="tub"><<link "Drink from the bathtub">><<run setup.fill(false)>><<run State.variables.taken.bathtub = true>><<replace "#tub">><</replace>><</link>></span><</if>>',
            '<<if !setup.isTaken("brasskey")>><<link "Look under the pillow" "Hotel Room 213 Footsteps">><<run setup.take("brasskey","brasskey")>><</link>><</if>>',
            '[[Answer the phone|Hotel Room 213 Phone]]', '[[Back to the hallway|Hotel Floor 2]]'), 'hotel')

add('Hotel Room 213 Phone', scene('art_h_room') + '\n' + story(
    'The phone wasn\'t ringing. You pick it up anyway.',
    '"Front desk," says a smooth voice. "Housekeeping is on its way to your room. Please stay where you are. =)"',
    'Click.') + '\n' +
    choices('[[Back to the room|Hotel Room 213]]'), 'hotel')

add('Hotel Room 213 Footsteps', scene('art_h_room') + '\n' + story(
    '<<if setup.has("brasskey")>>A heavy brass key, warm like someone was just holding it. You put it in your inventory.<<else>>A heavy brass key! But your inventory is full. You will have to come back for it.<</if>>',
    'Then you hear it. Squeak... squeak... squeak. A cleaning cart, rolling down the hall. It stops outside your door. The handle starts to turn.') + '\n' +
    timed(3, ['[[Hide in the wardrobe|Hotel Wardrobe]]', '[[Hide under the bed|Hotel Under Bed]]'], 'Housekeeping is here', 'Housekeeping Ending'), 'hotel')

add('Hotel Wardrobe', scene('art_h_room') + '\n' + story(
    'You squeeze into the wardrobe and pull the door almost shut.',
    'Through the crack you see long red sleeves and white gloves. It makes the bed perfectly. It fluffs the pillows. It turns toward the wardrobe... and stops.',
    '"Enjoy your stay," it says to no one, and leaves.') + '\n' +
    choices('<<if !setup.isTaken("brasskey")>><<link "Grab the key now" "Hotel Room 213">><<run setup.take("brasskey","brasskey")>><</link>><</if>>', '[[Sneak back out to the hallway|Hotel Floor 2]]'), 'hotel')

add('Hotel Under Bed', scene('art_h_room') + '\n' + story(
    'You slide under the bed. It is dusty and dark down here.',
    'Two very long legs walk in. Then the top of a smooth, smiling face lowers slowly into view, upside down, looking right at you.',
    '"Housekeeping," it whispers.') + '\n' +
    choices('[[...|Housekeeping Ending]]'), 'hotel')

add('Hotel Floor 3', withVirus('art_h_hall3', (40, 26, .45)) + '\n' + story(
    'Floor 3 looks like a normal hallway. Doors, lamps, carpet.',
    'You take a step. The hallway stretches. You take another. It stretches again. The door you came through is a tiny dot far behind you.',
    'The patterns on the wallpaper are starting to look like smiles.') + '\n' +
    choices('[[Keep walking forward|Hotel Floor 3 Deeper]]', '[[Walk backwards|Hotel Power Room]]', '[[Run back to the stairs|Hotel Staircase]]'), 'hotel')

add('Hotel Floor 3 Deeper', '<<set $sanity to Math.max(1, $sanity - 10)>>' + scene('art_h_hall3') + '\n' + story(
    'Forward. Forward. The hallway never ends. The room numbers go up and up: 340, 380, 399, 3000...',
    'The smiles on the wallpaper are definitely smiles now. (-10 sanity)',
    V('The virus wraps a tendril around your wrist. "Backwards," it says. "Now."', 'You remember something about walking backwards.')) + '\n' +
    choices('[[Keep going forward|Endless Hall Ending]]', '[[Walk backwards|Hotel Power Room]]'), 'hotel')

add('Hotel Power Room', withVirus('art_h_power', (-4, 14, .7)) + '\n' + story(
    'You walk backwards, one step at a time, eyes closed. When you open them you are standing in a humming room full of fuse boxes.',
    'A huge lever on the wall says ELEVATOR. It is pointing at OFF.',
    '<<if $power>>The lever is already pointing at ON.<</if>>') + '\n' +
    choices('<<if !$power>><<link "Pull the lever" "Hotel Power On">><<set $power to true>><</link>><</if>>', '[[Walk backwards out of the room|Hotel Staircase]]'), 'hotel')

add('Hotel Power On', scene('art_h_power') + '\n' + story(
    'CLUNK. The lights flicker, then burn brighter. Far below you hear a cheerful DING.',
    'The elevator works now. It can take you straight down to the basement.') + '\n' +
    choices('[[Walk backwards out of the room|Hotel Staircase]]'), 'hotel')

add('Hotel Elevator', withVirus('art_h_elevator', (12, 16, .7)) + '\n' + story(
    'The elevator is gold and velvet and smells like old perfume. Soft music plays.',
    'The buttons say 3, 2, L and B. A tiny sign under the B says: STAFF ONLY.') + '\n' +
    choices('[[Press B|Hotel Boiler Door]]', '[[Press 2|Hotel Floor 2]]', '[[Press 3|Hotel Floor 3]]', '[[Press L|Hotel Lobby]]'), 'hotel')

add('Hotel Basement Stairs', scene('art_h_stairs') + '\n' + story(
    'The service stairs go down into the dark. At the bottom, something long and black is lying across the steps, breathing slowly.',
    'A hound. Its white eyes are open. It is listening.',
    '<<if setup.has("flashlight")>>Your flashlight might scare it. Or it might make it angry.<</if>>') + '\n' +
    timed(4, ['<<if setup.has("axe")>>[[Charge it with the fire axe|Hotel Hound Axe]]<</if>>', '<<if setup.hasWeapon()>>[[Fight the hound|Battle Hound]]<</if>>', '[[Hold your breath and tiptoe past it|Hotel Boiler Door]]',
              '<<if setup.has("flashlight")>>[[Shine the flashlight in its eyes|Hound Ending]]<</if>>',
              '[[Go back up|Hotel Staircase]]'], 'It smells you', 'Hound Ending'), 'hotel')

add('Hotel Hound Axe', scene('art_h_stairs') + '\n' + story(
    'You run down the stairs swinging the fire axe and yelling as loud as you can.',
    'The hound\'s white eyes go wide. It has never seen prey fight back. It scrambles away into the dark and does not come back.') + '\n' +
    choices('[[Keep going down|Hotel Boiler Door]]'), 'hotel')

add('Hotel Boiler Door', withVirus('art_h_boilerdoor', (-4, 14, .7)) + '\n' + story(
    'A heavy red steel door: BOILER ROOM. EMPLOYEES ONLY. It has a big brass keyhole and a keypad that wants a 3-digit code.',
    '<<if setup.has("brasskey")>>The brass key in your inventory is warm, almost hot.<<else>>You don\'t have a key for that keyhole.<</if>>',
    'You will have to type the code in yourself. Hope you remember it.') + '\n' +
    choices('<<if setup.has("brasskey")>>[[Unlock the door and use the keypad|Hotel Keypad]]<</if>>',
            '<<if $power>>[[Take the elevator back up|Hotel Elevator]]<<else>>[[Go back up the stairs|Hotel Staircase]]<</if>>'), 'hotel')

add('Hotel Keypad', scene('art_h_boilerdoor') + '\n' + story(
    'The brass key turns with a heavy CLUNK. The keypad lights up green: ENTER CODE.',
    'Behind the door, the boiler rumbles like it is waiting.') + '\n' +
    '<div class="codepad" data-kind="digits" data-len="3" data-ok="Hotel Boiler Room" data-fail="boiler" data-answer="@boiler"></div>\n' +
    choices('<<if $power>>[[Step away from the keypad|Hotel Elevator]]<<else>>[[Step away from the keypad|Hotel Staircase]]<</if>>'), 'hotel')

add('Hotel Keypad Wrong', scene('art_h_boilerdoor') + '\n' + story(
    'BZZZT. The keypad flashes red: WRONG.',
    'The whole door shakes. The pressure gauge needle swings into the red. Steam screams out of a pipe.',
    'A sign you didn\'t notice before: TWO WRONG CODES = PRESSURE RELEASE.') + '\n' +
    choices('<<if setup.has("wrench")>><<link "Bleed the pressure valve with the wrench" "Hotel Keypad">><<set $codeTries to 0>><<run setup.toast("Hissss. The pressure drops back to safe.")>><</link>><</if>>', '[[Try again, carefully|Hotel Keypad]]', '<<if $power>>[[Leave and find the code|Hotel Elevator]]<<else>>[[Leave and find the code|Hotel Staircase]]<</if>>'), 'hotel')

add('Hotel Boiler Room', withVirus('art_h_boiler', (8, 12, .8)) + '\n' + story(
    'BEEP. The door swings open onto a room full of fire and steam. A giant boiler roars in the middle.',
    'On the far wall: a plain grey door with a green EXIT sign. The real exit.',
    'And standing next to it, very tall, very patient, is the Concierge. "Checking out, guest? =)"') + '\n' +
    choices('<<if setup.has("roomkey")>>[[Hand back your room key|Hotel Checkout Polite]]<</if>>',
            '<<if setup.hasWeapon()>>[[Fight the Concierge|Battle Concierge]]<</if>>',
            '<<if $virusWith>>[[Let the virus distract it|Hotel Virus Distracts]]<</if>>',
            '<<if $virusStrong>><span class="tip">The virus flexes its spiky black tendrils. It will hit harder in a fight now.</span><</if>>',
            '[[Run for the exit|Checkout Ending]]'), 'hotel')

add('Hotel Checkout Polite', scene('art_h_boiler') + '\n' + story(
    'You walk up and hold out the key to Room 213. "I\'d like to check out, please."',
    'The Concierge looks at the key for a long time. Then it bows. "A polite guest. How rare." It opens the exit door for you.',
    '"Do come again. =)"') + '\n' +
    choices('[[Walk through the exit|Hotel Exit]]'), 'hotel')

add('Hotel Fight Concierge', scene('art_h_boiler') + '\n' + story(
    'One last swing of your <<print setup.weaponName()>>. The Concierge reaches for you with its long white gloves... too slow.',
    'You hit it right in its smooth smiling face. It cracks like porcelain. It stumbles back into the boiler... and the fire takes it.',
    'The exit door is clear.') + '\n' +
    choices('[[Run through the exit|Hotel Exit]]'), 'hotel')

add('Hotel Virus Distracts', withVirus('art_h_boiler', (8, 12, .8)) + '\n' + story(
    'The virus rises up to its full height, twelve times stronger, and wraps itself around the Concierge.',
    '"GO! Through the door!" It drags the tall thing toward the boiler as you run past.',
    'You hear a crash and a roar of fire. Then the virus comes limping through the steam after you, smoking but grinning.') + '\n' +
    choices('[[Through the exit together|Hotel Exit]]'), 'hotel')

add('Hotel Exit', scene('art_level4', (30, 10, .85)) + '\n' + story(
    'The exit door slams shut behind you. The heat, the music and the smiles are gone.',
    'You are standing on cool carpet under buzzing lights. Somewhere ahead, you can hear wind. Real wind.',
    '"We are close now," the virus says. "Closer than anyone."') + '\n' +
    choices(f'[[Next|{END}]]'))

for name, bg, lines in (
        ('Checkout Ending', 'art_h_desk', ['"The exit?" The Concierge leans down until its smooth face is right in front of yours.', '"Guests don\'t leave. Guests STAY." Your stay at the Grand Hotel lasts forever. =)']),
        ('Bell Ending', 'art_h_desk', ['DING. DING.', 'The Concierge\'s painted smile cracks open into a real mouth. "ONLY. ONCE."']),
        ('Static Ending', 'art_h_room', ['The face in the static smiles wider and wider.', 'When the TV turns off by itself, the room is empty. The face on the screen looks like yours now.']),
        ('Knock Ending', 'art_h_hall2', ['You open the door. It isn\'t Theo.', 'It just used his voice. It can use yours now too.']),
        ('Housekeeping Ending', 'art_h_room', ['The door opens. Long red sleeves, white gloves.', '"Housekeeping," it says, and tucks you in. Forever.']),
        ('Endless Hall Ending', 'art_h_hall3', ['You keep walking. Room 4000. Room 9000. Room ∞.', 'You never reach the end of floor 3. Nobody does.']),
        ('Dance Forever Ending', 'art_h_ballroom', ['Cold hands grab you and pull you onto the dance floor.', 'Your face goes smooth. Your smile gets painted on. You dance forever. =)']),
        ('Hound Ending', 'art_h_stairs', ['The hound\'s white eyes snap toward you.', 'It moves faster than anything that size should be able to move.']),
        ('Boiler Ending', 'art_h_boilerdoor', ['BZZZT. WRONG. The gauge spins into the red.', 'PRESSURE RELEASE. The whole basement fills with scalding steam.'])):
    P.append(f':: {name} [ending]\n<div class="scene"><div class="pos bg">[img[{bg}]]</div></div>\n' + story(*lines) +
             '\n<div class="choices">[[Try again|Start]]</div>\n')

open(os.path.join(GEN, 'hotel.twee'), 'w', encoding='utf8').write('\n'.join(P))
print(len(P), 'passages,', len(ART), 'pictures')
