import os,sys,re
GEN=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,GEN)
import build
def style_text():
    # reuse Part 3's look (stylesheet passage only)
    s=open(r'C:\Users\dahaw\OneDrive\Desktop\twine-games\part-3-grown-up\src\Style.twee',encoding='utf8').read()
    return s.split(':: Story JavaScript')[0].rstrip()
PROJ=r'C:\Users\dahaw\OneDrive\Desktop\twine-games\part-3-1-backrooms'
SRC=os.path.join(PROJ,'src')
def fix(t): return t.replace('\u2019',"'").replace('\u201c','"').replace('\u201d','"')
DEATHS={10,13,26,31,36,39,40,52,71,72,73,74,84}
MODEPICK=('<div class="modepick">'
  '<div class="mcard"><<link "Play on Normal" "@@T4@@">><<set $mode to "normal">><</link>><p>Sanity drains slowly, timers give you extra time, 3 tries at codes, and hints show up when you need them.</p></div>'
  '<div class="mcard hard"><<link "Play on Hard" "@@T4@@">><<set $mode to "hard">><</link>><p>Sanity drains twice as fast, timers are short, one wrong code is the end, and only a few hints. Good luck.</p></div>'
  '</div>')
def KEEP(label, item, to):
    return f'<<link "{label}">><<if setup.addItem("{item}")>><<goto "@@T{to}@@">><</if>><</link>>'
OVER={
 1:{'story':['Part 3.1: The Backrooms Escape','A Slide Games production, made by Jack-Bros','This game is most likely M 17+ due to gore and mental horror.','@2026 all rights reserved'],'buttons':[('',MODEPICK)],'tags':['nodrain','nohud']},
 15:{'story':['What is this?','Drink it if things become distorted or you see smiles. Also avoid red things.'],'buttons':[('Drink it',16),('',KEEP('Save it','almond',17))]},
 27:{'story':['Drink it?'],'buttons':[('Drink it',28),('',KEEP('Store it','almond',28))]},
 42:{'story':["It's a sword!",'Remember the poster: you will have to fight.'],'buttons':[('',KEEP('Take the sword','sword',43)),('Leave it',43)]},
 53:{'buttons':[('','<<if setup.hasWeapon()>>[[Fight|@@T54@@]]<<else>>[[Fight|Unarmed]]<</if>>'),('Wait',84)]},
 17:{'buttons':[('Poolrooms','next'),('','[[Habitable zone|Level 1]]')]},
 55:{'story':['Here is the pinpad','Type in the code.'],'buttons':[('','<div class="codepad" data-kind="colors" data-ok="@@T56@@" data-answer="red blue green yellow" data-hint="The virus whispers: four colours. It started with red... then blue."></div>')]},
 60:{'drop_text':['Keep walking']},
 63:{'labels':{'Wait here or':'Wait here'}},
 82:{'buttons':[('','[[Next|Fun With The Virus]]')]},
 83:{'story':[],'raw_story':'<div class="escape"><h2>ESCAPE SUCCESSFUL</h2><p class="found">You have found your way out.</p><p class="tbc">To be continued... Part 4 is coming in a month.</p></div>','buttons':[('Back to the title',1)]},
}
for d in DEATHS: OVER.setdefault(d,{}).setdefault('labels',{})['Continue']='Try again'
# extra almond water bottles to find along the main route (one-time pickups)
WATER_AT=[18,33,45,59,68,78]
def FIND(n):
    k='w%d'%n
    return ('<<if !setup.isTaken("%s")>><div class="find" id="f%s"><<link "💧 There' + "'" + 's a bottle of almond water here. Take it">>'
            '<<if setup.take("%s","almond")>><<replace "#f%s">><</replace>><</if>><</link>></div><</if>>')%(k,k,k,k)
BAT=('<<if !setup.isTaken("bat")>><div class="find" id="fbat"><<link "\U0001F3CF A baseball bat is floating in the water. Grab it">>'
     '<<if setup.take("bat","bat")>><<replace "#fbat">><</replace>><</if>><</link>></div><</if>>')
cfg={'first':1,'fix':fix,'over':OVER,'exact':{1:'Start',83:'To be continued... (Q83)'},'remap':{2:1,3:1},
     'endings':DEATHS|{83},
     'timers':{49:{'secs':3.0,'fast':['Run','Approach'],'late':['It catches you'],'late_pics':[]}},
     'inscene':{54:[{'match':'V'}]},
     'actions':{15:{'Drink it':'setup.fill(true)'},27:{'Drink it':'setup.fill(true)'}},
     'on_enter':{1:'<<run setup.reset()>>',54:'<<run setup.useWeapon()>>',51:'<<run setup.addItem("code")>>',**{n:FIND(n) for n in WATER_AT},23:BAT},
     'extra_edges':{1:[4],53:[54],55:[56],82:[83]},
     'extra':open(os.path.join(GEN,'hud.twee'),encoding='utf8').read()+chr(10)+open(os.path.join(GEN,'levels.twee'),encoding='utf8').read()+chr(10)+open(os.path.join(GEN,'levels2.twee'),encoding='utf8').read()+chr(10)+open(os.path.join(GEN,'levels3.twee'),encoding='utf8').read()+chr(10)+open(os.path.join(GEN,'hotel.twee'),encoding='utf8').read()+chr(10)+open(os.path.join(GEN,'battle.twee'),encoding='utf8').read()}
g=build.Game(r'C:\Users\dahaw\Downloads\Part 3.1.pptx','Q',SRC,cfg)
out,names,order,models=build.generate(g,[1])
import posters, modes
open(os.path.join(SRC,'Start.twee'),'w',encoding='utf8').write(modes.apply(posters.add_posters('\n'.join(out))))
open(os.path.join(SRC,'Style.twee'),'w',encoding='utf8').write(style_text()+"\n:: Story JavaScript [script]\nConfig.ui.stowBarInitially = true;\nConfig.passages.transitionOut = 150;\n")
open(os.path.join(SRC,'Fx.twee'),'w',encoding='utf8').write(':: Fx Styles [stylesheet]'+chr(10)+open(os.path.join(GEN,'fx.css'),encoding='utf8').read())
unreached=[n for n,s in g.d.items() if n not in names and any((sh['k']=='txt' and any(t.strip() for p in sh['paras'] for t,l in p)) for sh in s['shapes'])]
print(len(order),'passages;',len(g.imgs),'images; unreachable text slides:',unreached)
