import os
G=os.path.dirname(os.path.abspath(__file__))
def edit(fn,pairs):
    p=os.path.join(G,fn); s=open(p,encoding='utf8').read()
    for old,new in pairs:
        assert old in s,(fn,old[:70]); s=s.replace(old,new,1)
    open(p,'w',encoding='utf8').write(s)

# builder: placeholders inside hand-written extra passages
edit('build.py',[("    if cfg.get('extra'): out.append(cfg['extra'])",
"""    if cfg.get('extra'):
        ex=cfg['extra']
        for mm in set(re.findall(r'@@T(\\d+)@@',ex)):
            k=int(mm); k=cfg.get('remap',{}).get(k,k); ex=ex.replace(f'@@T{mm}@@',names.get(k,'Start'))
        out.append(ex)""")])

# inventory/sanity script
edit('hud.twee',[
 ("  code:   { name: 'Code note', icon: '\\u{1F4DD}', desc: 'Red, blue, green, yellow.' }",
  "  code:   { name: 'Code note', icon: '\\u{1F4DD}', desc: 'Red, blue, green, yellow.' },\n  crowbar:{ name: 'Crowbar', icon: '\\u{1F527}', desc: 'Heavy and red. Good for prying doors, or hitting things.' }"),
 ("setup.reset = function () { var v = State.variables; v.sanity = 100; v.inv = []; };",
  "setup.reset = function () { var v = State.variables; v.sanity = 100; v.inv = []; v.taken = {}; };\nsetup.FUN_DRAIN = 5;  /* Level Fun drains sanity faster */\nsetup.drainFor = function (p) { return p.tags.indexOf('fun') >= 0 ? setup.FUN_DRAIN : setup.DRAIN; };\nsetup.isTaken = function (k) { return !!(State.variables.taken || {})[k]; };\nsetup.take = function (k, id) { var v = State.variables; v.taken = v.taken || {}; if (v.taken[k]) { return false; } if (setup.addItem(id)) { v.taken[k] = true; return true; } return false; };\nsetup.hasWeapon = function () { return setup.has('sword') || setup.has('crowbar'); };"),
 ("  if ((State.variables.sanity || 0) - setup.DRAIN <= 0) { return 'Lost Your Mind'; }",
  "  if ((State.variables.sanity || 0) - setup.drainFor(p) <= 0) { return 'Lost Your Mind'; }"),
 ("  v.sanity = Math.max(0, v.sanity - setup.DRAIN);","  v.sanity = Math.max(0, v.sanity - setup.drainFor(ev.passage));"),
 (".hotspot { position: absolute; display: block; cursor: pointer; }",
  ".hotspot { position: absolute; display: block; cursor: pointer; }\n@keyframes flicker { 0%, 17%, 19.5%, 21%, 58%, 61%, 100% { filter: none; } 18%, 20%, 59.5% { filter: brightness(.3); } }\nbody.flicker .scene { animation: flicker 5s infinite; }\n@keyframes partyhue { 0%, 100% { filter: none; } 50% { filter: hue-rotate(25deg) saturate(1.3); } }\nbody.fun .scene { animation: partyhue 3s ease-in-out infinite; }"),
 ("<div class=\"story-text\"><p>The yellow walls start smiling back at you.</p>",
  "<div class=\"scene\"><div class=\"pos bg\">[img[art_lostmind]]</div></div>\n<div class=\"story-text\"><p>The yellow walls start smiling back at you.</p>"),
 ("<p>It doesn't go well. Maybe you should have taken that sword.</p>","<p>It doesn't go well. Maybe you should have picked up a weapon.</p>"),
])

# driver: hook up the new branch
edit('drive31.py',[
 ("'remap':{2:1,3:1,19:23},","'remap':{2:1,3:1},"),
 (" 53:{'buttons':[('','<<if setup.has(\"sword\")>>[[Fight|@@T54@@]]<<else>>[[Fight|Unarmed]]<</if>>'),('Wait',84)]},",
  " 53:{'buttons':[('','<<if setup.hasWeapon()>>[[Fight|@@T54@@]]<<else>>[[Fight|Unarmed]]<</if>>'),('Wait',84)]},\n 17:{'buttons':[('Poolrooms','next'),('','[[Habitable zone|Level 1]]')]},"),
 ("     'extra':open(os.path.join(GEN,'hud.twee'),encoding='utf8').read()}",
  "     'extra':open(os.path.join(GEN,'hud.twee'),encoding='utf8').read()+chr(10)+open(os.path.join(GEN,'levels.twee'),encoding='utf8').read()}"),
])
print('ok')
