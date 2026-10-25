import zipfile,re,os
P=r'C:\Users\dahaw\OneDrive\Desktop\twine-games\finding-milk-part-2'
z=zipfile.ZipFile(r'C:\Users\dahaw\Downloads\Part 2 Finding Milk (1).pptx')
N={1:'Start',2:'Press Start',3:'Bike or Car',4:'Mysterious Man',5:'Go to the Store',6:'Nice Car',7:'Found a Bike',
66:'Motorcycle Ride',67:'Drive to Store',68:'Rusty Car',69:'Motorcycle',70:'In the Store',76:'Missing',77:'Woodmans',
78:'Meat Choice',79:'Food Poisoning Ending',81:'Run',82:'Caught Ending',83:'Lost in the Store Ending',
84:'Person From the Beginning',85:'Find Your Dad',86:'I Know Where He Is',87:'Sad Ending',89:'Vegan',90:'Vegan Ending',
111:'Hugged Him Ending',112:'You Wait',113:'Dad Find Me',114:'You Escaped',115:'Figure in the Distance',116:'Dad',
117:'Come Home Please',118:'OK',120:'Kidnapped Ending',121:'Ding Ding',122:'Chased',123:'You Hide',124:'Basement Ending',
133:'Part 3',147:'Secret Ending',149:'Happy Ending'}
T={ # slide: (body, [(label,target_slide)], tags)
1:("Part 2: Finding Milk\n''The Search''\nDad is alive, we must find him.\n\nMade by jack-bros\nE-10 rated",[("Begin",2),("",'<<if Object.keys(setup.endings).every(function (k) { return k === "Secret Ending" || (recall("endings") || []).includes(k); })>>[[try for the SECRET ending?|Secret Ending]]<</if>>')],''),
2:("Press Start\nAre you ready?",[("START",4)],''),
3:("He walks away. You are faced with a choice: go to the store on your bike or steal a car.",[("Bike",69),("Car",68)],''),
4:("You find a mysterious man. He says he can help. What do you do?",[("",'[[Go Alone|Bike or Car][$withMan to false]]'),("",'[[Go With Him|Go to the Store][$withMan to true]]')],''),
5:("Somehow you know he is here to help you. You must go to the store, Dad could be in danger. You must go fast!",[("Bike",7),("Steal Car",6)],''),
6:("You found the nicest car in the parking lot.",[("Click to drive",67)],''),
7:("You found a bike.",[("Click to ride",121)],''),
66:("BRRRRRRRRRRRRRRRRRRRR",[("Go to store",70)],''),
67:("BRRRRRRRRRRRRRRR",[("Go in store",70)],''),
68:("You found a rusty car.",[("Click to drive",67)],''),
69:("You find a sick motorcycle.",[("Drive to store",66)],''),
70:("",[("Go to dairy aisle",76),("Go back home to mom",87)],''),
76:("Missing.\nNo luck here, we have to go to Woodmans... but you saw your dad when he was younger.",[("Next",77)],''),
77:("Woodmans\nDad isn't here. Where to next?",[("Meat",78),("Produce",89)],''),
78:("You are faced with a choice.",[("Beef",81),("",'<<if $withMan>>[[Chicken|Person From the Beginning]]<<else>>[[Chicken|Lost in the Store Ending]]<</if>>'),("Pork",79)],''),
79:("You got food poisoning.",[("Start",1),("",'<a class="p3link" href="../part-3-grown-up/">Continue to Part 3</a>')],'ending'),
81:("RUN",[("Run",82)],''),
82:("It caught you.",[("Back to Start",1),("",'<a class="p3link" href="../part-3-grown-up/">Continue to Part 3</a>')],'ending'),
83:("You are lost in the store.",[("Go to beginning",1),("",'<a class="p3link" href="../part-3-grown-up/">Continue to Part 3</a>')],'ending'),
84:("You see the person from the beginning.",[("Next",85)],''),
85:("You want to find your dad?",[("Yes",86),("Yes!",86)],''),
86:("I know where he is.",[("Go alone",114),("Save dad?",120)],''),
87:("Sad ending.",[("GO BACK",1),("",'<a class="p3link" href="../part-3-grown-up/">Continue to Part 3</a>')],'ending'),
89:("You become a vegan so you can't drink milk.",[("Go home",90)],''),
90:("Vegan ending.",[("To beginning",1),("",'<a class="p3link" href="../part-3-grown-up/">Continue to Part 3</a>')],'ending'),
111:("YOU HUGGED HIM ONE last time... then he ran.",[("To beginning",1),("",'<a class="p3link" href="../part-3-grown-up/">Continue to Part 3</a>')],'ending'),
112:("You: wait!",[("Next",111)],''),
113:("Dad: find me!",[("Next",112)],''),
114:("He was gonna kidnap you. You escaped.",[("Look around",115)],''),
115:("You see a figure in the distance. It can't be...",[("Go after him",116)],''),
116:("Dad?",[("Hi kiddo",117),("RUNNNN!",113)],''),
117:("Come home please.",[("Next",118)],''),
118:("",[("OK",149)],''),
120:("You get kidnapped.\nSad ending NO. 2",[("",'[[Escape?|Basement Escape]]'),("To beginning",1)],'ending'),
121:("Ding Ding",[("Go to store",122)],''),
122:("A man tries to chase you.",[("Run",124),("Hide",123)],''),
123:("You hide.",[("Look around the store",70),("Go home",87)],''),
124:("He caught you.\nBasement ending",[("",'[[Escape?|Basement Escape]]'),("To beginning",1)],'ending'),
133:("Congrats, you have beaten this game!\nPart 3 is ready.",[("",'<a class="p3link" href="../part-3-grown-up/">Play Part 3</a>'),("Back to the title",1)],''),
147:("Secret ending plus 6000 aura",[("Continue",133),("To beginning",1),("",'<a class="p3link" href="../part-3-grown-up/">Continue to Part 3</a>')],'ending'),
149:("Happy ending",[("Restart",1),("",'<a class="p3link" href="../part-3-grown-up/">Continue to Part 3</a>')],'ending'),
}
os.makedirs(P+r'\src\images',exist_ok=True)
out=[]
for s,(body,links,tag) in T.items():
    rl=z.read(f'ppt/slides/_rels/slide{s}.xml.rels').decode()
    imgs=[]
    for m in re.findall(r'media/(image\d+\.\w+)',rl):
        ext=m.split('.')[-1]; nm=f's{s:03d}_{m.split(".")[0]}'
        open(f'{P}\src\images\{nm}.{ext}','wb').write(z.read('ppt/media/'+m)); imgs.append(nm)
    lines=[]
    if imgs: lines.append('<div class="pics n%d">'%len(imgs)+''.join(f'[img[{i}]]' for i in imgs)+'</div>')
    if body: lines.append('<div class="story-text">\n\n'+body.replace('\n','\n\n')+'\n\n</div>')
    lines.append('<div class="choices">')
    lines+= [(t if isinstance(t,str) else f'[[{l}|{N[t]}]]') for l,t in links]
    lines.append('</div>')
    tags=f' [{tag}]' if tag else ''
    out.append(f':: {N[s]}{tags}\n'+'\n'.join(lines)+'\n')
open(P+r'\src\Start.twee','w',encoding='utf8').write('\n'.join(out))
d=open(P+r'\src\StoryData.twee').read()
print(len(T),'passages')
