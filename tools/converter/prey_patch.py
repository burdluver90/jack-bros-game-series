# helpful prey: small creatures you meet in the levels that help you once per run
import os
GEN = os.path.dirname(os.path.abspath(__file__))
D = r'C:\Users\dahaw\OneDrive\Desktop\twine-games\part-3-1-backrooms\src\images'

def svg(bg, body):
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 300">'
            '<defs><radialGradient id="g" cx=".5" cy=".5" r=".7"><stop offset="0" stop-color="#fff8c4" stop-opacity=".9"/><stop offset="1" stop-color="#fff8c4" stop-opacity="0"/></radialGradient>'
            '<radialGradient id="v" cx=".5" cy=".5" r=".75"><stop offset=".5" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".7"/></radialGradient></defs>'
            f'<rect width="400" height="300" fill="{bg}"/>{body}<rect width="400" height="300" fill="url(#v)"/></svg>')

moth = lambda x, y, r: (f'<g transform="translate({x} {y}) rotate({r})"><ellipse cx="-14" cy="0" rx="16" ry="10" fill="#efe6c8"/><ellipse cx="14" cy="0" rx="16" ry="10" fill="#efe6c8"/>'
                        f'<ellipse cx="-11" cy="10" rx="10" ry="7" fill="#d9cfa9"/><ellipse cx="11" cy="10" rx="10" ry="7" fill="#d9cfa9"/><ellipse rx="4" ry="12" fill="#6b5d3a"/>'
                        f'<path d="M-2 -11 q-6 -10 -12 -12 M2 -11 q6 -10 12 -12" stroke="#6b5d3a" stroke-width="1.5" fill="none"/></g>')
moths = svg('#8f8a6a', '<rect x="0" y="210" width="400" height="90" fill="#5d5a45"/><rect x="180" y="40" width="40" height="170" fill="#2b2a20"/>'
            '<circle cx="200" cy="120" r="90" fill="url(#g)"/>' + moth(150, 90, -20) + moth(250, 110, 15) + moth(200, 60, 5) + moth(170, 160, 30) + moth(240, 175, -25) +
            '<ellipse cx="200" cy="240" rx="60" ry="10" fill="#e9dfb4" opacity=".6"/>')

mouse = lambda x, y, s, f: (f'<g transform="translate({x} {y}) scale({s * f} {s})"><path d="M30 6 q40 -2 50 20" stroke="#c9a0a0" stroke-width="3" fill="none"/>'
                            f'<ellipse cx="0" cy="0" rx="34" ry="20" fill="#8b8b8b"/><circle cx="-30" cy="-6" r="14" fill="#9a9a9a"/><circle cx="-26" cy="-20" r="9" fill="#c9a0a0"/>'
                            f'<circle cx="-40" cy="-8" r="2.5" fill="#000"/><circle cx="-44" cy="-2" r="3" fill="#e8a0a0"/></g>')
mice = svg('#2a1a10', '<rect x="0" y="150" width="400" height="40" fill="#2563eb"/><rect x="0" y="156" width="400" height="8" fill="#93c5fd" opacity=".6"/>'
           '<rect x="0" y="60" width="400" height="30" fill="#7a4a2a"/>' + mouse(120, 132, 1, 1) + mouse(220, 135, .8, 1) + mouse(300, 130, .9, 1) + '<rect x="0" y="190" width="400" height="110" fill="#1a100a"/>')

bugs = ''.join(f'<circle cx="{x}" cy="{y}" r="{r * 3}" fill="url(#g)"/><circle cx="{x}" cy="{y}" r="{r}" fill="#d9ff7a"/>'
               for x, y, r in ((120, 90, 4), (160, 140, 5), (200, 100, 6), (240, 150, 4), (280, 95, 5), (210, 190, 4), (150, 200, 3), (260, 210, 3), (190, 60, 3)))
glow = svg('#050505', bugs + '<path d="M150 260 q50 -40 100 0" stroke="#3a3a3a" stroke-width="10" fill="none"/>')

bell = svg('#3b1a1a', '<rect x="0" y="200" width="400" height="100" fill="#6b1d1d"/><path d="M0 230 h400 M0 260 h400" stroke="#b8860b" stroke-width="3" opacity=".5"/>'
           + mouse(200, 190, 1.6, 1) +
           '<g transform="translate(152 145)"><rect x="-16" y="-14" width="32" height="14" rx="3" fill="#b91c1c"/><rect x="-20" y="-2" width="40" height="5" fill="#7f1d1d"/><rect x="-6" y="-12" width="12" height="3" fill="#facc15"/></g>'
           '<text x="300" y="250" font-family="Georgia" font-size="40" fill="#fde68a" opacity=".8">?</text>')

for n, s in (('art_p_moths', moths), ('art_p_mice', mice), ('art_p_glow', glow), ('art_p_bellmouse', bell)):
    open(os.path.join(D, n + '.svg'), 'w', encoding='utf8').write(s)

BEASTS = r"""  { id: 'moths', name: 'Almond Moths', tag: 'Helpful prey', friend: true, img: 'art_p_moths',
    seen: ['Level 1'], deaths: [],
    desc: 'Pale, dusty moths that can smell almond water from a whole level away. They are harmless, and almost everything eats them.',
    tip: 'Follow them. They always fly toward almond water.' },
  { id: 'mice', name: 'Pipe Mice', tag: 'Helpful prey', friend: true, img: 'art_p_mice',
    seen: ['Level 2 Pipe Dreams'], deaths: [],
    desc: 'Tiny grey mice that live along the pipes of Pipe Dreams. They never, ever touch a hot pipe.',
    tip: 'Go where the mice go. They know which way is safe.' },
  { id: 'glowbugs', name: 'Glow Bugs', tag: 'Helpful prey', friend: true, img: 'art_p_glow',
    seen: ['Level 6 Lights Out'], deaths: [],
    desc: 'A drifting cloud of tiny glowing bugs in the darkness of Lights Out. The Light Haters cannot stand them.',
    tip: 'No flashlight? Cup a handful of glow bugs and use them as a light.' },
  { id: 'bellmouse', name: 'The Bellhop Mouse', tag: 'Helpful prey', friend: true, img: 'art_p_bellmouse',
    seen: ['Hotel Lobby'], deaths: [],
    desc: 'A mouse in a tiny red bellhop cap who lives under the front desk of the Grand Hotel. It hears everything the band plays.',
    tip: 'Be kind to it. It scratches part of the boiler code into the carpet for you.' },
"""
# what each prey offers in its level (once per run)
JS = r"""/* helpful prey: each one offers a little help once per run, in the passage where you meet it */
setup.PREY = {
  'Level 1': { id: 'moths', text: 'A few pale moths flutter past you and drift off toward a crack in the wall.', btn: 'Follow the moths',
    use: function () { State.variables.sanity = Math.min(100, State.variables.sanity + 15); return 'The moths lead you to a puddle of almond water dripping from the ceiling. You drink. <b>+15 sanity</b>.'; } },
  'Level 2 Pipe Dreams': { id: 'mice', text: 'Three tiny grey mice scurry past your feet, running along the cold blue pipe.', btn: 'Watch where the mice go',
    use: function () { State.variables.sanity = Math.min(100, State.variables.sanity + 5); return 'The mice run along the <b>cold blue pipe</b> and stay far away from the hot one. Smart mice. You feel a little calmer. <b>+5 sanity</b>.'; } },
  'Level 6 Lights Out': { id: 'glowbugs', text: 'A tiny green light blinks near your face. Then another. A cloud of glow bugs is drifting by.', btn: 'Cup a handful of glow bugs',
    use: function () { setTimeout(function () { Engine.play('Lights Out Flashlight'); }, 1400); return 'You cup them in your hands. They glow brighter, and the red eyes shriek and back away.'; } },
  'Hotel Lobby': { id: 'bellmouse', text: 'A mouse in a tiny red bellhop cap peeks out from under the front desk.', btn: 'Kneel down and be nice to the mouse',
    use: function () { var c = setup.boiler(); return 'The mouse sniffs your hand, then scratches a number into the carpet with its claw: <b>' + c.charAt(0) + '</b>. It taps it twice, then points its nose at the ballroom.'; } }
};
$(document).on(':passagedisplay', function (ev) {
  var p = setup.PREY[ev.passage.title], v = State.variables;
  if (!p) { return; }
  v.preyUsed = v.preyUsed || {};
  var box = $('<div class="preybox"><p>' + p.text + '</p></div>');
  if (!v.preyUsed[p.id]) {
    $('<a class="preybtn">\u{1F43E} ' + p.btn + '</a>').on('click', function () {
      v.preyUsed[p.id] = true; box.find('.preybtn').remove();
      box.append('<p class="preyout">' + p.use() + '</p>'); setup.hud();
    }).appendTo(box);
  }
  var ch = $('#passages .choices').first();
  if (ch.length) { box.insertBefore(ch); } else { box.appendTo('#passages .passage'); }
});
"""
CSS = """.preybox { margin: 10px auto; max-width: 640px; padding: 10px 14px; border: 1px dashed #86efac; border-radius: 10px; background: rgba(20, 50, 36, .55); }
.preybox p { margin: 0 0 6px; }
.preybox .preyout { color: #bbf7d0; }
.preybtn { display: inline-block; padding: .35em 1em; border-radius: 99px; border: 1px solid #4fd18b; background: #143224; color: #c9ffe0; cursor: pointer; text-decoration: none; }"""

p = os.path.join(GEN, 'bestiary.twee'); s = open(p, encoding='utf8').read()
pairs = [
    ("];\nsetup.best = function", BEASTS.rstrip('\n').rstrip(',') .join(['', '']) if False else None),
]
if "id: 'moths'" not in s:
    i = s.index("];\nsetup.best = function")
    s = s[:i].rstrip() + ",\n" + BEASTS.rstrip().rstrip(',') + "\n" + s[i:]
if 'setup.PREY' not in s:
    s = s.replace("setup.best = function", JS + "setup.best = function", 1)
if '.preybox' not in s:
    s = s.replace(".bestlink { text-align: center; margin: 6px 0 0; }", ".bestlink { text-align: center; margin: 6px 0 0; }\n" + CSS, 1)
old = "{ name: 'Prey', note: 'Small, weak, and hunted by nearly everything.', list: ['doll'] }"
new = "{ name: 'Prey', note: 'Small, weak, and hunted by nearly everything. Be kind to them and they help you.', list: ['doll', 'moths', 'mice', 'glowbugs', 'bellmouse'] }"
if new not in s:
    assert old in s; s = s.replace(old, new, 1)
open(p, 'w', encoding='utf8').write(s)
print('prey added')
