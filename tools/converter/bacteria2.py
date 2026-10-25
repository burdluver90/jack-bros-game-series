# the bacteria looks like the Backrooms entity: a tall, thin, jagged black figure; the virus absorbs black tendrils
import os, random
GEN = os.path.dirname(os.path.abspath(__file__))
D = r'C:\Users\dahaw\OneDrive\Desktop\twine-games\part-3-1-backrooms\src\images'
random.seed(7)

def jag(x0, y0, x1, y1, n, amp, w):
    # a jagged black spike-limb from (x0,y0) to (x1,y1)
    pts_l, pts_r = [], []
    for i in range(n + 1):
        t = i / n
        x = x0 + (x1 - x0) * t + random.uniform(-amp, amp)
        y = y0 + (y1 - y0) * t + random.uniform(-amp, amp)
        k = w * (1 - t) + 1
        pts_l.append(f'{x - k:.0f},{y:.0f}'); pts_r.append(f'{x + k:.0f},{y:.0f}')
    return '<polygon points="' + ' '.join(pts_l + pts_r[::-1]) + '"/>'

# Level 0 style hallway: yellow walls, wet carpet, buzzing lights
room = '''  <rect width="1600" height="900" fill="#b8a64a"/>
  <polygon points="0,0 1600,0 1100,300 500,300" fill="#d6c98a"/>
  <polygon points="0,900 1600,900 1100,620 500,620" fill="#6e6436"/>
  <polygon points="0,0 500,300 500,620 0,900" fill="#a4933c"/><polygon points="1600,0 1100,300 1100,620 1600,900" fill="#9a8a36"/>
  <rect x="500" y="300" width="600" height="320" fill="#8a7c34"/>
  <g fill="#fffbe0" opacity=".9"><rect x="640" y="90" width="320" height="26"/><rect x="700" y="230" width="200" height="14"/></g>
  <g stroke="#7d7030" stroke-width="3" opacity=".5"><path d="M0 120 L500 360 M0 300 L500 440 M1600 120 L1100 360 M1600 300 L1100 440"/></g>
'''
body = []
# torso and head: a thin, crooked silhouette with no face
body.append(jag(800, 230, 790, 640, 9, 10, 26))
body.append('<ellipse cx="800" cy="215" rx="34" ry="46"/>')
# spiky legs
body.append(jag(790, 600, 700, 860, 7, 10, 12)); body.append(jag(800, 600, 900, 870, 7, 10, 12))
# long jagged arms and the black tendrils coming off it
for (x1, y1) in ((420, 260), (360, 520), (1180, 240), (1260, 500), (560, 760), (1050, 780)):
    body.append(jag(800, 340, x1, y1, 10, 18, 9))
for i in range(14):
    a = random.uniform(-3.1, 0)
    import math
    body.append(jag(800, 230, 800 + math.cos(a) * random.uniform(120, 260), 230 + math.sin(a) * random.uniform(80, 200), 6, 8, 4))
bact = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 900">
  <defs><radialGradient id="vign" cx=".5" cy=".5" r=".75"><stop offset=".5" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".8"/></radialGradient></defs>
{room}  <g fill="#050505">{''.join(body)}</g>
  <rect width="1600" height="900" fill="url(#vign)"/>
</svg>
'''
# absorbing: the bacteria is half gone, its black tendrils stream left into the virus
random.seed(7)
small = []
small.append(jag(1150, 300, 1140, 620, 8, 10, 18)); small.append('<ellipse cx="1150" cy="290" rx="24" ry="32"/>')
for (x1, y1) in ((1350, 260), (1400, 500), (1250, 760)):
    small.append(jag(1150, 380, x1, y1, 8, 14, 6))
streams = ''.join(f'<path d="M1120 {y0} C 950 {y0 - 80} 800 {y1 + 60} 560 {y1}" stroke="#050505" stroke-width="{w}" fill="none" stroke-linecap="round"/>'
                  for y0, y1, w in ((330, 300, 16), (420, 430, 22), (500, 520, 14), (580, 620, 18), (380, 360, 8), (540, 700, 10)))
absorb = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 900">
  <defs><radialGradient id="vign" cx=".5" cy=".5" r=".75"><stop offset=".5" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".8"/></radialGradient></defs>
{room}  <g fill="#050505" opacity=".7">{''.join(small)}</g>
  {streams}
  <rect width="1600" height="900" fill="url(#vign)"/>
</svg>
'''
for n, s in (('art_bacteria', bact), ('art_absorb', absorb)):
    open(os.path.join(D, n + '.svg'), 'w', encoding='utf8').write(s)

def swap(f, pairs):
    p = os.path.join(GEN, f); s = open(p, encoding='utf8').read()
    for a, b in pairs:
        if b not in s:
            assert a in s, (f, a[:60]); s = s.replace(a, b, 1)
    open(p, 'w', encoding='utf8').write(s)
swap('levels3.py', [
    ("Something wet slaps against the carpet behind you.", "The lights buzz louder. Something is standing at the end of the hall."),
    ("A giant green bacteria oozes out of the vent, whipping its long tails. It lunges and wraps one around your leg.",
     "It is tall and thin and pitch black, with no face, and its body is made of jagged spikes. The Bacteria. It twitches, then sprints at you and wraps a black tendril around your leg."),
    ("You smash the tail. It lets go of your leg, but it splits into two new tails. Hitting it just makes more of it.",
     "You smash the tendril. It lets go of your leg, but two new spiky tendrils grow out of the stump. Hitting it just makes more of it."),
    ('Hit the tail with your ', 'Hit the tendril with your '),
    ("The virus shoots its tendrils straight into the bacteria. The green slime starts flowing up them, into the virus.",
     "The virus shoots its tendrils straight into the Bacteria. Its black tendrils start peeling off, one by one, and get pulled into the virus."),
    ("The bacteria shrinks... and shrinks... until it is nothing but a puddle on the carpet.",
     "The Bacteria shrinks... and shrinks... until it is nothing but a black stain on the carpet."),
    ("Three brand-new tendrils burst out of its back, thicker and longer than the others.",
     "Three brand-new tendrils burst out of its back, pitch black and covered in spikes, just like the ones on the Bacteria."),
    ("'The bacteria pulls you into the vent.', 'It is very dark in there, and very, very wet.'",
     "'The Bacteria drags you down the hall.', 'The lights buzz. Then they go out.'"),
])
swap('battle.twee', [("The virus lashes it with its new tendrils (+1).", "The virus lashes it with its black tendrils (+1).")])
swap('hotel.py', [("The virus flexes its new tendrils.", "The virus flexes its spiky black tendrils.")])
swap('bestiary.twee', [
    ("A giant green cell with whipping tails that crawls out of the vents. Cut a tail and two grow back.",
     "A tall, thin, faceless black figure made of jagged spikes. It twitches, then sprints. Cut a tendril and two grow back."),
    ("Weapons only make more tails. Let the virus absorb it, and the virus grows stronger tendrils.",
     "Weapons only make more tendrils. Let the virus absorb it, and the virus grows spiky black tendrils of its own."),
])
print('bacteria v2')
