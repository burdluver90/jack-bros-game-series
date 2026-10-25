import os,sys,re
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import build, drive3_css
P2=r'C:\Users\dahaw\OneDrive\Desktop\twine-games\finding-milk-part-2'
SRC=os.path.join(P2,'src')
P3LINK='<a class="p3link" href="../part-3-grown-up/">Continue to Part 3</a>'
def fix(t): return t.replace('\u2019',"'")
OVER={
 4:{'pre_story':['Part 2.1: The basement escape'],'add_story':['Content note: mild illegal activity (trespassing), horror, intense violence, blood, light gore.']},
 5:{'story':['You tryna escape, sonny?'],'buttons':[('Continue',6)]},
 6:{'labels':{'Beginning':'Try again'}},
 21:{'labels':{'Main menu':'Try again'}},
 23:{'labels':{'Main menu':'Try again'}},
 22:{'story':['You are now safe, for now.'],'buttons':[('',P3LINK),('Credits',25),('',"[[Main menu|Start]]")]},
 25:{'story':[],'raw_story':'<div class="credits">'+''.join('<p>'+build.esc(x)+'</p>' for x in ['Credits', 'Story creator - Lee Hawk', 'Main story designer - Braxton Bowen', 'Secondary story designer - Lee Hawk', 'The series creators - Lee Hawk, Alvin Eichstaedt, and Odin Stronach', 'Idea for part 2.1 - Braxton Bowen'])+'</div><p style="animation:fx-in-fade 1.5s ease-out 4s backwards">'+build.esc('BIG thanks to Braxton Bowen for our secondary series helper')+'</p><p style="animation:fx-in-fade 1.5s ease-out 5.5s backwards">Thank you!</p>','buttons':[('Back',22)]},
}
cfg={'first':4,'fix':fix,'over':OVER,'remap':{1:4,2:4,3:4},'exact':{4:'Basement Escape'},'endings':{6,21,22,23}}
g=build.Game(r'C:\Users\dahaw\Downloads\Part 2.1.pptx','B',SRC,cfg)
out,names,order,models=build.generate(g,[4])
open(os.path.join(SRC,'Basement.twee'),'w',encoding='utf8').write('\n'.join(out))
st=open(os.path.join(SRC,'Style.twee'),encoding='utf8').read()
if '.scene {' not in st:
    st=st.replace(':: Story JavaScript',drive3_css.SCENE_CSS+'\n:: Story JavaScript',1)
    open(os.path.join(SRC,'Style.twee'),'w',encoding='utf8').write(st)
unreached=[n for n,s in g.d.items() if n not in names and any((sh['k']=='txt' and any(t.strip() for p in sh['paras'] for t,l in p)) for sh in s['shapes'])]
print(len(order),'passages;',len(g.imgs),'images; unreachable text slides:',unreached)

open(os.path.join(SRC,'Fx.twee'),'w',encoding='utf8').write(':: Fx Styles [stylesheet]\n'+open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'fx.css'),encoding='utf8').read())
