import glob,os,shutil
from PIL import Image, ImageSequence
P=r'C:\Users\dahaw\OneDrive\Desktop\twine-games\finding-milk-part-2'
def run(f,maxd,colors,step):
    name=os.path.basename(f); dst=os.path.join(P,'src','images',name)
    im=Image.open(f); frames=[];durs=[]
    for fr in ImageSequence.Iterator(im):
        frames.append(fr.convert('RGB')); durs.append(fr.info.get('duration',100) or 100)
    if step>1:
        nf=[];nd=[]
        for i in range(0,len(frames),step):
            nf.append(frames[i]); nd.append(sum(durs[i:i+step]))
        frames,durs=nf,nd
    w,h=frames[0].size; s=min(1,maxd/max(w,h))
    if s<1: frames=[x.resize((max(1,int(w*s)),max(1,int(h*s))),Image.LANCZOS) for x in frames]
    q=[x.quantize(colors,method=Image.MEDIANCUT,dither=Image.FLOYDSTEINBERG) for x in frames]
    q[0].save(dst,save_all=True,append_images=q[1:],duration=durs,loop=0,optimize=True,disposal=1)
    return len(frames)
for f in sorted(glob.glob(P+r'\originals-images\*.gif')):
    name=os.path.basename(f); dst=os.path.join(P,'src','images',name)
    if Image.open(f).n_frames==1: continue
    a=os.path.getsize(f); b=os.path.getsize(dst)
    if b>=a: shutil.copy(f,dst); print(name,'kept original'); continue
    if b>1.0e6:
        n=Image.open(f).n_frames
        k=run(f,320,64,3 if n>100 else 2)
        print(name,'tightened ->',k,'frames',round(os.path.getsize(dst)/1e6,2),'MB')
tot=sum(os.path.getsize(x) for x in glob.glob(P+r'\src\images\*'))
print('images total MB',round(tot/1e6,1))
