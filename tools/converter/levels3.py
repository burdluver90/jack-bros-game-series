# more levels after Level Fun: Level 2 Pipe Dreams, Level 4 Abandoned Office, Level 6 Lights Out, Level ! Run For Your Life
import os, sys
GEN = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, GEN)
from levels2 import VIRUS, find, story
D = r'C:\Users\dahaw\OneDrive\Desktop\twine-games\part-3-1-backrooms\src\images'
END = 'Hotel Arrival'

def scene(bg, virus=None):
    v = ''
    if virus:
        left, top, k = virus
        v = f'<div class="pos" style="left:{left}%;top:{top}%;width:{k * 100:.1f}%;height:{k * 100:.1f}%">{VIRUS}</div>'
    return f'<div class="scene"><div class="pos bg">[img[{bg}]]</div>{v}</div>'

def withVirus(bg, spot):
    # the virus only shows up if it is still with you
    return f'<<if $virusWith>>{scene(bg, spot)}<<else>>{scene(bg)}<</if>>'

# ---------- art ----------
def svg(defs, body):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 900">\n  <defs>\n{defs}  </defs>\n{body}</svg>\n'

VIGN = '    <radialGradient id="vign" cx=".5" cy=".5" r=".75"><stop offset=".5" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".75"/></radialGradient>\n'

pipes = []
for i, (y, w, c) in enumerate(((120, 46, '#7a4a2a'), (200, 30, '#5c3a22'), (300, 60, '#8a5530'), (700, 54, '#6e4426'), (780, 34, '#5c3a22'))):
    pipes.append(f'<rect x="0" y="{y}" width="1600" height="{w}" fill="{c}"/><rect x="0" y="{y + 4}" width="1600" height="{w // 5}" fill="#c98a5a" opacity=".35"/>')
    for x in range(80 + i * 37, 1600, 260):
        pipes.append(f'<rect x="{x}" y="{y - 6}" width="22" height="{w + 12}" fill="#3b2414"/>')
level2 = svg(VIGN + '''    <linearGradient id="hot" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2a1a10"/><stop offset=".5" stop-color="#4a2c18"/><stop offset="1" stop-color="#1a100a"/></linearGradient>
    <filter id="steam"><feGaussianBlur stdDeviation="18"/></filter>
''', '''  <rect width="1600" height="900" fill="url(#hot)"/>
  <polygon points="560,380 1040,380 1040,560 560,560" fill="#0d0805"/>
  ''' + '\n  '.join(pipes) + '''
  <!-- vertical pipes and a valve wheel -->
  <rect x="300" y="0" width="56" height="900" fill="#6e4426"/><rect x="1240" y="0" width="70" height="900" fill="#7a4a2a"/>
  <g transform="translate(328 520)"><circle r="54" fill="none" stroke="#b91c1c" stroke-width="12"/><path d="M-54 0 H54 M0 -54 V54" stroke="#b91c1c" stroke-width="10"/><circle r="10" fill="#7f1d1d"/></g>
  <!-- the flashlight hanging on the valve -->
  <g transform="translate(400 560) rotate(18)"><rect x="-14" y="0" width="28" height="90" rx="6" fill="#1f2937"/><rect x="-20" y="84" width="40" height="26" rx="4" fill="#374151"/><circle cy="106" r="12" fill="#fde68a"/></g>
  <!-- steam -->
  <g fill="#f5efe6" opacity=".45" filter="url(#steam)"><ellipse cx="1275" cy="330" rx="120" ry="60"/><ellipse cx="900" cy="330" rx="90" ry="40"/><ellipse cx="180" cy="740" rx="140" ry="60"/></g>
  <!-- a cold blue pipe going left, a red-hot pipe going right -->
  <rect x="0" y="600" width="560" height="40" fill="#2563eb"/><rect x="0" y="606" width="560" height="8" fill="#93c5fd" opacity=".6"/>
  <rect x="1040" y="600" width="560" height="40" fill="#dc2626"/><rect x="1040" y="606" width="560" height="8" fill="#fca5a5" opacity=".7"/>
  <rect width="1600" height="900" fill="url(#vign)"/>
''')

cubes = []
for row, (y, s) in enumerate(((520, 1.0), (440, .75), (390, .55))):
    for k in range(-3, 4):
        if k == 0:
            continue
        x = 800 + k * 260 * s - 110 * s
        cubes.append(f'<rect x="{x:.0f}" y="{y - 130 * s:.0f}" width="{220 * s:.0f}" height="{130 * s:.0f}" fill="#8b8f96"/>'
                     f'<rect x="{x + 10 * s:.0f}" y="{y - 120 * s:.0f}" width="{200 * s:.0f}" height="{20 * s:.0f}" fill="#a3a7ad"/>'
                     f'<rect x="{x + 60 * s:.0f}" y="{y - 100 * s:.0f}" width="{70 * s:.0f}" height="{46 * s:.0f}" fill="#1f2937"/>'
                     f'<rect x="{x + 64 * s:.0f}" y="{y - 96 * s:.0f}" width="{62 * s:.0f}" height="{38 * s:.0f}" fill="{"#7dff6b" if (k, row) == (1, 0) else "#334155"}" opacity=".9"/>')
level4 = svg(VIGN + '''    <pattern id="tiles" width="100" height="60" patternUnits="userSpaceOnUse"><rect width="100" height="60" fill="#d8d4c4"/><path d="M0 0 H100 M0 0 V60" stroke="#b9b4a2" stroke-width="3"/></pattern>
    <linearGradient id="officefloor" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#6b6f5a"/><stop offset="1" stop-color="#3f4234"/></linearGradient>
''', '''  <rect width="1600" height="330" fill="url(#tiles)"/>
  <g fill="#fffbe6" opacity=".9"><rect x="300" y="60" width="200" height="30"/><rect x="700" y="60" width="200" height="30"/><rect x="1100" y="60" width="200" height="30" opacity=".35"/></g>
  <rect y="330" width="1600" height="570" fill="url(#officefloor)"/>
  <rect y="300" width="1600" height="60" fill="#c8c2a8"/>
  ''' + '\n  '.join(cubes) + '''
  <!-- water cooler full of almond water -->
  <g transform="translate(170 700)">
    <rect x="-60" y="-220" width="120" height="220" fill="#e5e7eb"/><rect x="-50" y="-150" width="100" height="10" fill="#9ca3af"/>
    <path d="M-44 -220 Q-50 -340 0 -350 Q50 -340 44 -220 Z" fill="#bfdbfe" opacity=".85"/><path d="M-30 -230 Q-34 -320 0 -330" stroke="#fff" stroke-width="6" fill="none" opacity=".7"/>
    <rect x="-14" y="-120" width="28" height="16" fill="#3b82f6"/>
  </g>
  <!-- sticky note on the computer -->
  <rect x="1065" y="372" width="34" height="34" fill="#fde047" transform="rotate(8 1080 390)"/>
  <rect width="1600" height="900" fill="url(#vign)"/>
''')

level6 = svg('''    <radialGradient id="cone" cx=".5" cy="1" r="1"><stop offset="0" stop-color="#fffbe0" stop-opacity=".35"/><stop offset="1" stop-color="#fffbe0" stop-opacity="0"/></radialGradient>
    <filter id="glow6" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="5" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
''', '''  <rect width="1600" height="900" fill="#020203"/>
  <!-- barely visible walls -->
  <path d="M0 0 L600 360 L600 560 L0 900 Z" fill="#07070a"/><path d="M1600 0 L1000 360 L1000 560 L1600 900 Z" fill="#07070a"/>
  <!-- eyes in the dark, left and right -->
  <g fill="#f8fafc" filter="url(#glow6)"><circle cx="420" cy="430" r="7"/><circle cx="452" cy="432" r="7"/></g>
  <g fill="#ef4444" filter="url(#glow6)"><circle cx="1190" cy="400" r="6"/><circle cx="1222" cy="398" r="6"/><circle cx="1130" cy="520" r="5"/><circle cx="1158" cy="522" r="5"/></g>
  <!-- the faint hum of a light far away -->
  <rect x="770" y="420" width="60" height="8" fill="#fef9c3" opacity=".25" filter="url(#glow6)"/>
  <path d="M800 900 L620 430 L980 430 Z" fill="url(#cone)" opacity=".25"/>
''')

levelrun = svg(VIGN + '''    <linearGradient id="redwall" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#3b0a0a"/><stop offset=".5" stop-color="#8b1414"/><stop offset="1" stop-color="#3b0a0a"/></linearGradient>
    <filter id="glowr" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="8" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
''', '''  <rect width="1600" height="900" fill="#2a0606"/>
  <polygon points="0,0 1600,0 960,360 640,360" fill="#4a0c0c"/>
  <polygon points="0,0 640,360 640,540 0,900" fill="url(#redwall)"/>
  <polygon points="1600,0 960,360 960,540 1600,900" fill="url(#redwall)"/>
  <polygon points="0,900 640,540 960,540 1600,900" fill="#1a0404"/>
  <rect x="640" y="360" width="320" height="180" fill="#120202"/>
  <!-- red emergency lights -->
  <g fill="#ff2a2a" filter="url(#glowr)"><rect x="200" y="90" width="120" height="16"/><rect x="1280" y="90" width="120" height="16"/><rect x="500" y="250" width="70" height="10"/><rect x="1030" y="250" width="70" height="10"/></g>
  <!-- scrawled on the wall -->
  <text x="300" y="470" font-family="Arial Black, Arial" font-weight="900" font-size="64" fill="#fecaca" opacity=".85" transform="rotate(-6 300 470) skewY(14)">RUN FOR</text>
  <text x="1150" y="470" font-family="Arial Black, Arial" font-weight="900" font-size="64" fill="#fecaca" opacity=".85" text-anchor="middle" transform="rotate(6 1150 470) skewY(-14)">YOUR LIFE</text>
  <!-- the thing chasing you: a wall of black shapes far down the hall -->
  <g fill="#000"><ellipse cx="800" cy="470" rx="150" ry="70"/><path d="M660 470 l-30 -80 l40 50 z M940 470 l30 -80 l-40 50 z M740 420 l-6 -70 l26 54 z M860 420 l6 -70 l-26 54 z"/></g>
  <g fill="#fff" filter="url(#glowr)"><circle cx="760" cy="460" r="6"/><circle cx="840" cy="460" r="6"/><circle cx="720" cy="490" r="4"/><circle cx="880" cy="490" r="4"/></g>
  <!-- a heavy door slamming down at the end -->
  <rect x="660" y="360" width="280" height="40" fill="#525252"/><path d="M660 400 h280" stroke="#facc15" stroke-width="10" stroke-dasharray="30 20"/>
  <rect width="1600" height="900" fill="url(#vign)"/>
''')

for name, s in (('art_level2', level2), ('art_level4', level4), ('art_level6', level6), ('art_levelrun', levelrun)):
    open(os.path.join(D, name + '.svg'), 'w', encoding='utf8').write(s)

# ---------- passages ----------
V = (55, 12, .8)   # where the virus stands when it is with you
P = []
P.append(':: Level 2 Pipe Dreams\n' + find('wl2') + '\n' + withVirus('art_level2', V) + '\n' + story(
    'You fall through a hatch and land on hot metal. Level 2: Pipe Dreams.',
    'Pipes everywhere, hissing steam. The air is so hot it hurts to breathe.',
    '<<if $virusWith>>The virus shakes off the confetti. "Two ways out," it says. "One cold, one hot."<<else>>You are alone now. Somewhere behind you, the party music is still playing.<</if>>',
    'A flashlight hangs from a red valve wheel. A rusty pipe wrench is stuck on the valve next to it.') +
    '\n<div class="choices"><<if !setup.isTaken("wrench")>><span id="pkw"><<link "Take the pipe wrench off the valve">><<if setup.take("wrench","wrench")>><<replace "#pkw">><</replace>><</if>><</link>></span><</if>><<if !setup.isTaken("flashlight")>><span id="pkf"><<link "Take the flashlight">><<if setup.take("flashlight","flashlight")>><<replace "#pkf">><</replace>><</if>><</link>></span><</if>>'
    '<<if setup.has("wrench")>>[[Use the wrench to shut the hot pipe valve|Level 2 Valve]]<</if>>[[Follow the cold blue pipe|Level 2 Crawler]][[Follow the hot red pipe|Steam Ending]]</div>\n')
P.append(':: Level 2 Valve\n' + scene('art_level2') + '\n' + story(
    'You clamp the pipe wrench onto the big red valve and pull with everything you have.',
    'SCREEEECH. The valve turns. The hissing stops. The red-hot pipe slowly fades to a dull grey.',
    'Now you can follow it. It goes straight down, a shortcut.') +
    '\n<div class="choices">[[Follow the cooled pipe down|Level 6 Lights Out]]</div>\n')
P.append(':: Level 4 Abandoned Office [nodrain]\n' + withVirus('art_level4', V) + '\n' + story(
    'The pipe ends at a vent. You crawl out into a quiet office. Level 4.',
    'Empty cubicles, humming lights, and a water cooler full of almond water. It feels... safe. Your sanity stops dropping here.',
    'One computer is still on. A sticky note on it says: "Lights out is next. Bring a light."') +
    '\n<div class="choices">' + '<<if setup.has("wrench")>><<if !setup.isTaken("coolerbottle")>><span id="pkcb"><<link "Unscrew the cooler tap with the wrench and fill a bottle">><<if setup.take("coolerbottle","almond")>><<replace "#pkcb">><</replace>><</if>><</link>></span><</if>><</if>>' + '<span id="cool"><<link "Drink from the water cooler">><<run setup.fill(false)>><<replace "#cool">><</replace>><</link>></span>'
    '[[Read the computer|Office Computer]][[Take the stairs down|Level 6 Lights Out]]</div>\n')
P.append(':: Office Computer [nodrain]\n' + withVirus('art_level4', V) + '\n' + story(
    'The screen flickers. Someone typed a message and never sent it:',
    '"THE LEVELS KEEP GOING DOWN. THE EXIT IS NOT ALWAYS AN EXIT. IF YOU HEAR WHISPERING IN THE DARK, GO THE OTHER WAY. IF THE LIGHTS TURN RED, RUN."',
    '<<if $virusWith>>The virus reads over your shoulder. "Good advice," it mutters.<<else>>Under it, someone has scratched a smiley face into the desk. =)<</if>>') +
    '\n<div class="choices">[[Take the stairs down|Level 6 Lights Out]]</div>\n')
P.append(':: Level 6 Lights Out\n' + scene('art_level6') + '\n' + story(
    'The stairs end. The lights go out. Level 6: Lights Out.',
    'You can\'t see your own hands. On your left, something is whispering. On your right, a pair of red eyes blinks... then another pair.',
    '<<if setup.has("flashlight")>>Your flashlight is in your inventory.<<else>>You wish you had a light.<</if>>') +
    '\n<div class="choices"><<if setup.has("flashlight")>>[[Turn on the flashlight|Lights Out Flashlight]]<</if>>'
    '<<if setup.hasWeapon()>><<link `"Swing your " + setup.weaponName() + " at the red eyes"` "Lights Out Swing">><</link>><</if>>[[Walk toward the whispering|Whispers Ending]][[Walk toward the faint hum of a light|Level Run For Your Life]]</div>\n')
P.append(':: Lights Out Swing\n' + scene('art_level6') + '\n' + story(
    'You swing blindly into the dark. CRACK. Something shrieks.',
    'The red eyes blink out one pair at a time. Under your feet you feel the floor slope toward a faint red glow.<<run setup.useWeapon()>>') +
    '\n<div class="choices">[[Follow the slope|Level Run For Your Life]]</div>\n')
P.append(':: Lights Out Flashlight\n' + withVirus('art_level6', (20, 14, .7)) + '\n' + story(
    'Click. The beam cuts through the dark.',
    'The red eyes belong to things that hate light. They scream and scatter.',
    'In the beam you see a narrow hallway with a door at the end, and the walls of the hallway are red.') +
    '\n<div class="choices">[[Go to the red hallway|Level Run For Your Life]]</div>\n')
P.append(':: Level Run For Your Life\n' + scene('art_levelrun') + '\n' + story(
    'The lights snap on. Every single one of them is red. Level !: Run For Your Life.',
    'Down the hall, the dark is moving. It is coming toward you, fast.',
    'At the far end, a heavy door is sliding shut.') +
    '\n<div id="opts" class="choices">[[RUN|Run For Your Life 2]]</div>\n'
    '<div class="timerbar"><span style="animation-duration:2.5s"></span></div>\n'
    '<<timed 2.5s>><<replace "#opts">><div class="caught">[[It catches you|Run For Your Life Ending]]</div><</replace>><<run $(".timerbar").remove()>><</timed>>\n')
P.append(':: Run For Your Life 2\n' + scene('art_levelrun', (2, 8, .9)) + '\n' + story(
    'You sprint. Your lungs burn. The door is closing faster.',
    '<<if $virusWith>>The virus grabs you with every tendril it has and throws you toward the gap.<<else>>Then the wall next to you splits open. The virus bursts out. "Told you," it says. "I always find you."<</if>>',
    'SLIDE!') +
    '\n<div id="opts" class="choices">[[Slide under the door|Level Run Escape]]</div>\n'
    '<div class="timerbar"><span style="animation-duration:2s"></span></div>\n'
    '<<timed 2s>><<replace "#opts">><div class="caught">[[The door slams shut|Run For Your Life Ending]]</div><</replace>><<run $(".timerbar").remove()>><</timed>>\n')
P.append(':: Level Run Escape\n' + scene('art_level4', (30, 10, .85)) + '\n' + story(
    'You slide under the door just before it slams shut. Behind it, something hits the metal again and again... then it stops.',
    'You are lying on cool carpet. The virus sits down next to you, breathing hard.',
    '<<set $virusWith to true>>"We are deeper than anyone has ever gone," it says. "And I think I know where the real exit is."') +
    "\n<p>Down the hall, the lights are buzzing louder than they should.</p>" + f"\n<div class=\"choices\">[[Next|Bacteria Attack]]</div>\n")
P.append(':: Bacteria Attack\n' + scene('art_bacteria', (4, 14, .75)) + '\n' + story(
    'The lights buzz louder. Something is standing at the end of the hall.',
    'It is tall and thin and pitch black, with no face, and its body is made of jagged spikes. The Bacteria. It twitches, then sprints at you and wraps a black tendril around your leg.',
    'The virus goes very still. Then every one of its tendrils starts to shake. "Bacteria," it growls. "My kind and its kind have been at war since the very first level. They hunted us when we were small. Not anymore."',
    'Before you can even scream, the virus ROARS and lunges.') +
    '\n<div class="choices">[[Watch the virus attack|Bacteria Absorb]]</div>\n')
P.append(':: Bacteria Absorb\n' + scene('art_absorb', (4, 14, .75)) + '\n' + story(
    'The virus lets out a roar you can feel in your teeth and slams into the Bacteria. It shoots its tendrils straight into it. Its black tendrils start peeling off, one by one, and get pulled into the virus.',
    'The Bacteria shrinks... and shrinks... until it is nothing but a black stain on the carpet.',
    '<<set $virusStrong to true>>The virus shudders. Three brand-new tendrils burst out of its back, pitch black and covered in spikes, just like the ones on the Bacteria. "That is for every one of us your kind ever ate," it hisses at the stain. Then it turns to you, calm again. "Much better. Now I can fight with you."',
    'It looks down the dark hall. "When I was small, I had brothers and sisters. Hatchlings, tiny viruses that had not mutated yet. The Bacteria ate them like candy. A hatchling cannot fight back. Most of them never got as big as me." It goes quiet for a moment. "Now you know why I hate them."') +
    f'\n<div class="choices">[[Next|{END}]]</div>\n')
for name, bg, lines in (
        ('Steam Ending', 'art_level2', ['The red pipe gets hotter and hotter.', 'A valve bursts. The steam is the last thing you ever feel.']),
        ('Whispers Ending', 'art_level6', ['The whispering knows your name.', 'It says it one more time, right behind your ear. Then the dark closes in.']),
        ('Run For Your Life Ending', 'art_levelrun', ['You were not fast enough.', 'The lights flicker red one last time. Then nothing.'])):
    P.append(f':: {name} [ending]\n<div class="scene"><div class="pos bg">[img[{bg}]]</div></div>\n' + story(*lines) +
             '\n<div class="choices">[[Try again|Start]]</div>\n')

open(os.path.join(GEN, 'levels3.twee'), 'w', encoding='utf8').write('\n'.join(P))
print(len(P), 'passages')
