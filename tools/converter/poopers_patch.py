# after Level Fun: the Partypoopers offer you a photo. A second "gear" slot holds the flashlight and the photo.
# carrying the photo makes you lose 1 less sanity every scene.
import os
GEN = os.path.dirname(os.path.abspath(__file__))
D = r'C:\Users\dahaw\OneDrive\Desktop\twine-games\part-3-1-backrooms\src\images'
def patch(f, pairs):
    p = os.path.join(GEN, f); s = open(p, encoding='utf8').read()
    for a, b in pairs:
        if b in s:
            continue
        assert a in s, (f, a[:80]); s = s.replace(a, b, 1)
    open(p, 'w', encoding='utf8').write(s)

# ---------- art: grey, gloomy party guests with frowns and droopy balloons, one holding an old camera ----------
def pooper(x, y, k, frown_tilt, hat):
    return (f'<g transform="translate({x} {y}) scale({k})">'
            f'<path d="M-46 260 L-40 70 Q0 40 40 70 L46 260 Z" fill="#6b7280"/>'
            f'<rect x="-30" y="150" width="60" height="10" fill="#4b5563"/>'
            f'<circle cy="20" r="52" fill="#9ca3af"/>'
            f'<circle cx="-18" cy="10" r="6" fill="#1f2937"/><circle cx="18" cy="10" r="6" fill="#1f2937"/>'
            f'<path d="M-16 -6 l12 6 M16 -6 l-12 6" stroke="#1f2937" stroke-width="4"/>'
            f'<path d="M-22 48 Q0 {30 + frown_tilt} 22 48" stroke="#1f2937" stroke-width="6" fill="none" stroke-linecap="round"/>'
            + (f'<path d="M-24 -26 L0 -90 L24 -26 Z" fill="#94a3b8" transform="rotate(-25)"/>' if hat else '') +
            '</g>')
camera = ('<g transform="translate(980 520)"><rect x="-70" y="-40" width="140" height="90" rx="10" fill="#374151"/>'
          '<rect x="-55" y="-58" width="40" height="20" fill="#4b5563"/><circle r="30" fill="#111827"/><circle r="18" fill="#60a5fa" opacity=".6"/>'
          '<rect x="30" y="-30" width="22" height="12" fill="#fde68a"/></g>')
balloons = ''.join(f'<path d="M{x} {y} q-4 120 10 220" stroke="#9ca3af" stroke-width="2" fill="none"/><ellipse cx="{x}" cy="{y}" rx="34" ry="26" fill="{c}" transform="rotate(20 {x} {y})"/>'
                   for x, y, c in ((260, 520, '#6b7280'), (330, 560, '#78716c'), (1330, 500, '#57534e')))
art = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 900">'
       '<defs><radialGradient id="v" cx=".5" cy=".5" r=".75"><stop offset=".5" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".75"/></radialGradient></defs>'
       '<rect width="1600" height="900" fill="#3f3f46"/><rect y="640" width="1600" height="260" fill="#27272a"/>'
       '<path d="M0 120 Q200 200 400 120 T800 120 T1200 120 T1600 120" stroke="#52525b" stroke-width="14" fill="none"/>'
       '<text x="800" y="96" text-anchor="middle" font-family="Arial Black, Arial" font-size="54" fill="#71717a">NO PARTY  :(</text>'
       + balloons + pooper(560, 420, 1.1, 18, True) + pooper(800, 400, 1.25, 22, False) + pooper(1180, 430, 1.05, 16, True) + camera +
       '<rect width="1600" height="900" fill="url(#v)"/></svg>')
open(os.path.join(D, 'art_partypoopers.svg'), 'w', encoding='utf8').write(art)

# ---------- the gear slot ----------
patch('hud.twee', [
    ("  flashlight: { name: 'Flashlight', short: 'Light', icon: '\\u{1F526}', desc: 'Some things in the dark hate light.' },",
     "  flashlight: { name: 'Flashlight', short: 'Light', icon: '\\u{1F526}', desc: 'Some things in the dark hate light.' },\n"
     "  photo:  { name: 'Partypooper photo', short: 'Photo', icon: '\\u{1F4F7}', desc: 'You and three very grumpy Partypoopers. Looking at it keeps you calm: you lose 1 less sanity every scene.' },"),
    ("setup.SLOTS = 6;      /* inventory size */",
     "setup.SLOTS = 6;      /* inventory size */\n"
     "/* gear goes in its own little slots, not the main inventory */\n"
     "setup.GEAR = ['flashlight', 'photo'];"),
    ("var v = State.variables; v.sanity = 100; v.inv = []; v.taken = {};",
     "var v = State.variables; v.sanity = 100; v.inv = []; v.gear = []; v.taken = {};"),
    ("  return d + setup.HEAVY.filter(setup.has).length;   /* +1 for each heavy weapon you carry */",
     "  d += setup.HEAVY.filter(setup.has).length;   /* +1 for each heavy weapon you carry */\n"
     "  if (setup.has('photo')) { d -= 1; }          /* the Partypooper photo keeps you calm */\n"
     "  return Math.max(0, d);"),
    ("setup.has = function (id) { return (State.variables.inv || []).indexOf(id) >= 0; };",
     "setup.has = function (id) { var v = State.variables; return (v.inv || []).indexOf(id) >= 0 || (v.gear || []).indexOf(id) >= 0; };"),
    ("  if (setup.has(id) && id !== 'almond') { return false; }\n  if (v.inv.length >= setup.SLOTS)",
     "  if (setup.has(id) && id !== 'almond') { return false; }\n"
     "  if (setup.GEAR.indexOf(id) >= 0) { v.gear = v.gear || []; v.gear.push(id); setup.toast('Gear: ' + setup.ITEMS[id].icon + ' ' + setup.ITEMS[id].name); setup.hud(); return true; }\n"
     "  if (v.inv.length >= setup.SLOTS)"),
    ("    '<div class=\"slots\">' + slots + '</div><div class=\"info\">'",
     "    '<div class=\"slots\">' + slots + '</div>' + setup.gearRow() + '<div class=\"info\">'"),
    ("setup.hud = function () {",
     "setup.gearRow = function () {\n"
     "  var g = State.variables.gear || [], out = '';\n"
     "  setup.GEAR.forEach(function (id) {\n"
     "    var it = setup.ITEMS[id], have = g.indexOf(id) >= 0;\n"
     "    out += have ? '<span class=\"gslot full\" title=\"' + it.name + ': ' + it.desc.replace(/\"/g, '') + '\">' + it.icon + '<small>' + it.short + '</small></span>' : '<span class=\"gslot\"></span>';\n"
     "  });\n"
     "  return '<div class=\"gear\"><span class=\"glbl\">Gear</span>' + out + '</div>';\n"
     "};\n"
     "setup.hud = function () {"),
])
# move a flashlight carried in the old main inventory over to the gear slot
patch('hud.twee', [
    ("setup.gearRow = function () {\n  var g = State.variables.gear || [], out = '';",
     "setup.gearRow = function () {\n"
     "  var v = State.variables; v.gear = v.gear || [];\n"
     "  setup.GEAR.forEach(function (id) { var i = (v.inv || []).indexOf(id); if (i >= 0) { v.inv.splice(i, 1); if (v.gear.indexOf(id) < 0) { v.gear.push(id); } } });\n"
     "  var g = v.gear, out = '';"),
])

# ---------- styles ----------
p = os.path.join(GEN, 'bestiary.twee'); s = open(p, encoding='utf8').read()
css = ("#hud .gear { display: flex; align-items: center; justify-content: center; gap: 6px; margin-top: 6px; }\n"
       "#hud .gear .glbl { font-size: .7rem; letter-spacing: .12em; text-transform: uppercase; color: #a8a38a; margin-right: 4px; }\n"
       "#hud .gslot { width: 44px; height: 44px; border: 1px dashed #4a4528; border-radius: 8px; display: flex; flex-direction: column; align-items: center; justify-content: center; font-size: 1.2rem; }\n"
       "#hud .gslot.full { border: 1px solid #a16207; background: #2a2610; }\n"
       "#hud .gslot small { font-size: .55rem; color: #c7c2a4; }")
if '#hud .gear' not in s:
    s = s.replace(".bestlink { text-align: center; margin: 6px 0 0; }", ".bestlink { text-align: center; margin: 6px 0 0; }\n" + css, 1)

# ---------- bestiary entry and food chain ----------
entry = ("  { id: 'poopers', name: 'The Partypoopers', tag: 'Prey', friend: true, img: 'art_partypoopers',\n"
         "    seen: ['Partypoopers'], deaths: [],\n"
         "    desc: 'Grey, grumpy party guests who got kicked out of Level Fun for frowning. They hate balloons, cake and music, and they are the only creatures in the Backrooms who never smile. The Partygoers chase them off on sight.',\n"
         "    tip: 'Take a picture with them. Their frowns are so calming that carrying the photo makes you lose 1 less sanity every scene.' },\n")
if "id: 'poopers'" not in s:
    s = s.replace("  { id: 'moths',", entry + "  { id: 'moths',", 1)
s = s.replace("list: ['hatchlings', 'doll', 'moths',", "list: ['hatchlings', 'doll', 'poopers', 'moths',", 1)
assert "'poopers', 'moths'" in s
open(p, 'w', encoding='utf8').write(s)

# ---------- the scene, between Level Fun and Level 2 ----------
patch('levels2.py', [("END = 'Level 2 Pipe Dreams'", "END = 'Partypoopers'")])
patch('levels3.py', [
    ("P.append(':: Level 2 Valve\\n'",
     "P.append(':: Partypoopers\\n' + withVirus('art_partypoopers', (2, 14, .7)) + '\\n' + story(\n"
     "    'Behind the last door of Level Fun is a small grey room. The streamers are torn down and the balloons are all half deflated.',\n"
     "    'Three grey figures are sitting there, arms crossed, frowning as hard as they can. A sign on the wall says NO PARTY. :(',\n"
     "    '\"We are the Partypoopers,\" the tallest one grumbles. \"They kicked us out for not smiling. We do not do fun.\" It holds up an old camera. \"But we do take pictures. Want one? No smiling.\"') +\n"
     "    '\\n<div class=\"choices\"><span id=\"pp\"><<if !setup.has(\"photo\")>><<link \"Take a grumpy picture with them\">><<run setup.addItem(\"photo\")>><<replace \"#pp\">><p>FLASH. The photo slides out of the camera: you and three Partypoopers, all frowning. Looking at it makes you feel weirdly calm. It goes in your gear slot.</p><</replace>><</link>><</if>></span>'\n"
     "    '[[Say goodbye and drop down the hatch|Level 2 Pipe Dreams]]</div>\\n')\n"
     "P.append(':: Level 2 Valve\\n'"),
])
print('partypoopers')
