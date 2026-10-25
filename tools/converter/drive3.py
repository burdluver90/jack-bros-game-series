import os,sys,re
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import build
PROJ=r'C:\Users\dahaw\OneDrive\Desktop\twine-games\part-3-grown-up'
P2=r'C:\Users\dahaw\OneDrive\Desktop\twine-games\finding-milk-part-2'
SRC=os.path.join(PROJ,'src')

from drive3_css import SCENE_CSS
def style_text():
    s=open(os.path.join(P2,'src','Style.twee'),encoding='utf8').read()
    css=s.split(':: Story JavaScript')[0]
    # drop the tracker css block (Part 2 only)
    css=re.sub(r'\.tracker.*?\n(?=\n|\.tracker|$)','',css)
    css=css.replace('.choices a.link-internal','.choices a.link-internal-old')
    return css.rstrip()+'\n'+SCENE_CSS

def fix3(t):
    return t.replace('\u2019',"'")

OVER={
 1:{'story':['Part 3: Grown Up','Made by Jack-Bros','Rated T: crude humor, violence, and mild gore.','Email one of the Jack Bros (aka Odin, Lee, Vinny, Braxton) once you have the secret code. If you guess correctly, you can find out the truth.'],'labels':{'play':'Play'}},
 2:{'story':['Main menu'],'labels':{'play':'Play'}},
 6:{'drop_text':['on'],'labels':{'off':'Turn it off'}},
 9:{'story':['Processing... 100%']},
 10:{'story':['You: Where am I? What is that in the distance?']},
 37:{'story':['You lost! Aliens are gonna be released.'],'buttons':[('Continue',44)]},
 38:{'drop_text':['($200)'],'labels':{'Pay tax':'Pay tax ($200)'}},
 43:{'drop_text':['!','Look around']},
 63:{'labels':{'NeXt':'Next'}},
 65:{'labels':{'Look aroun':'Look around'},'drop_text':['d']},
 66:{'labels':{'Drawer':'Drawer Box'}},
 79:{'labels':{'Run Figh t':'Run / Fight'}},
 81:{'buttons':[('Open',82)]},
 82:{'drop_text':['.']},
 95:{'labels':{'W alk':'Walk'}},
 101:{'labels':{'Hi n t':'Hint'}},
 105:{'story':['Everything collapses into a liminal space. Good luck, wayward adventurer.','Part 3.1'],'buttons':[('','<a class="p3link" href="../part-3-1-backrooms/">Play Part 3.1</a>'),('Back to the title',1)]},
 114:{'story':['Eaten alive ending'],'buttons':[('Beginning',1)]},
 124:{'story':['Files opened','The fourth file: Creators note','Vinny\'s note'],'buttons':[('Read the note',131),('Back to the title',1)]},
}
TIMERS={
 11:{'secs':2.2,'fast':['RUN!!!'],'late':['You lost go to end'],'late_pics':[]},
 98:{'secs':2.5,'fast':['RUN'],'late':['It caught you'],'late_pics':[]},
 108:{'secs':2.5,'fast':['Over','UNDER','TO THE SIDE'],'late':['IT CAUGHT YOU'],'late_pics':[]},
 115:{'secs':2.5,'fast':['Under','To The Side','Over'],'late':['It caught you'],'late_pics':[]},
 117:{'secs':2.5,'fast':['Shoot it','Keep running'],'late':['IT CAUGHT YOU'],'late_pics':[]},
}
INSCENE={
 34:[{'match':'1230ht'}],
 35:[{'match':'1230ht','link':36}],
 61:[{'match':'Password'}],
 64:[{'match':'Password'}],
 56:[{'match':'1178'},{'match':'JBLVOB'}],
 78:[{'match':'1 178','link':80}],
 96:[{'match':'File','link':125}],
 98:[{'match':'Hint','link':130}],
 100:[{'match':'Hint','link':129}],
 101:[{'match':'Hi','link':127}],
 109:[{'match':'Hint','link':128}],
}
cfg={'inscene':INSCENE,'timers':TIMERS,'first':1,'fix':fix3,'over':OVER,'nomerge':{78},'exact':{1:'Start'},
     'endings':{39,44,63,75,76,91,105,109,114,116,123}}
g=build.Game(r'C:\Users\dahaw\Downloads\_Part 3 grown up (1).pptx','P',os.path.join(SRC),cfg)
# images go to src/images
out,names,order,models=build.generate(g,[1])
unreached=[n for n,s in g.d.items() if n not in names and any((sh['k']=='txt' and any(t.strip() for p in sh['paras'] for t,l in p)) for sh in s['shapes'])]
open(os.path.join(SRC,'Start.twee'),'w',encoding='utf8').write('\n'.join(out))
open(os.path.join(SRC,'Style.twee'),'w',encoding='utf8').write(style_text()+"\n:: Story JavaScript [script]\nConfig.ui.stowBarInitially = true;\nConfig.passages.transitionOut = 150;\n")
print(len(order),'passages;',len(g.imgs),'images; unreachable text slides:',unreached)

open(os.path.join(SRC,'Fx.twee'),'w',encoding='utf8').write(':: Fx Styles [stylesheet]\n'+open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'fx.css'),encoding='utf8').read())
