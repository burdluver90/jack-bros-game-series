import glob,os
from PIL import Image, ImageSequence
P=r'C:\Users\dahaw\OneDrive\Desktop\twine-games\finding-milk-part-2'
tot0=tot1=0
for f in sorted(glob.glob(P+r'\originals-images\*.gif')):
    name=os.path.basename(f); dst=os.path.join(P,'src','images',name)
    im=Image.open(f); n=im.n_frames
    if n==1: continue   # stills are already tiny
    frames=[];durs=[]
    for fr in ImageSequence.Iterator(im):
        frames.append(fr.convert('RGBA')); durs.append(fr.info.get('duration',100) or 100)
    # drop every other frame on long animations, keeping total timing
    if n>30:
        nf=[];nd=[]
        for i in range(0,len(frames),2):
            nf.append(frames[i]); nd.append(durs[i]+(durs[i+1] if i+1<len(durs) else 0))
        frames,durs=nf,nd
    w,h=frames[0].size; s=min(1,380/max(w,h))
    if s<1: frames=[x.resize((max(1,int(w*s)),max(1,int(h*s))),Image.LANCZOS) for x in frames]
    q=[x.convert('RGB').quantize(96,method=Image.MEDIANCUT,dither=Image.FLOYDSTEINBERG) for x in frames]
    q[0].save(dst,save_all=True,append_images=q[1:],duration=durs,loop=0,optimize=True,disposal=1)
    a,b=os.path.getsize(f),os.path.getsize(dst); tot0+=a; tot1+=b
    print(name,n,'->',len(frames),'frames',round(a/1e6,2),'->',round(b/1e6,2),'MB')
print('animated GIF total',round(tot0/1e6,1),'->',round(tot1/1e6,1),'MB')
