import os,re,html,zipfile
from PIL import Image, ImageSequence
import pp
SW,SH=9144000,5143500
ZW='&#8203;'
def esc(t):
    t=html.escape(t,quote=False)
    for a in ['//',"''",'__','==','~~','@@','^^','{{{','[[','<<']:
        if a in t: t=t.replace(a,a[0]+ZW+a[1:])
    t=re.sub(r'\$(?=[A-Za-z_])','$'+ZW,t); t=re.sub(r'(?<![A-Za-z0-9])_(?=[A-Za-z])','_'+ZW,t)
    return t
def clean_label(t):
    t=re.sub(r'\s+',' ',t).strip()
    for a in '|[]<>': t=t.replace(a,' ')
    return re.sub(r'\s+',' ',t).strip()
def short(t):
    t=re.sub(r"[^A-Za-z0-9 '!?,.-]",' ',t); w=t.split()[:5]; s=' '.join(w)
    return s[:32].strip() or 'Scene'
def esc_html(t):
    import html as _h
    return _h.escape(t,quote=False)
def prefix_clean(p): return re.sub(r'\W','',p)

def gif_shrink(im,dst,maxd=420,colors=80):
    frames=[];durs=[];alpha=False
    for fr in ImageSequence.Iterator(im):
        f=fr.convert('RGBA')
        if f.getchannel('A').getextrema()[0]<200: alpha=True
        frames.append(f); durs.append(fr.info.get('duration',100) or 100)
    if alpha:
        step=3 if len(frames)>90 else (2 if len(frames)>24 else 1)
        if step>1:
            nf=[];nd=[]
            for i in range(0,len(frames),step):
                nf.append(frames[i]); nd.append(sum(durs[i:i+step]))
            frames,durs=nf,nd
        w,h=frames[0].size; s=min(1,maxd/max(w,h))
        if s<1: frames=[x.resize((max(1,int(w*s)),max(1,int(h*s))),Image.LANCZOS) for x in frames]
        qs=[]
        for f in frames:
            mask=f.getchannel('A').point(lambda a:255 if a<128 else 0)
            q=f.convert('RGB').quantize(colors-1,method=Image.MEDIANCUT,dither=Image.NONE)
            pal=q.getpalette()[:3*(colors-1)]; pal+= [0]*(768-len(pal)); q.putpalette(pal)
            q.paste(255,mask=mask); q.info['transparency']=255; qs.append(q)
        qs[0].save(dst,save_all=True,append_images=qs[1:],duration=durs,loop=0,disposal=2,transparency=255,optimize=False)
        return
    frames=[f.convert('RGB') for f in frames]
    step=3 if len(frames)>90 else (2 if len(frames)>24 else 1)
    if step>1:
        nf=[];nd=[]
        for i in range(0,len(frames),step):
            nf.append(frames[i]); nd.append(sum(durs[i:i+step]))
        frames,durs=nf,nd
    w,h=frames[0].size; s=min(1,maxd/max(w,h))
    if s<1: frames=[x.resize((max(1,int(w*s)),max(1,int(h*s))),Image.LANCZOS) for x in frames]
    q=[x.quantize(colors,method=Image.MEDIANCUT,dither=Image.FLOYDSTEINBERG) for x in frames]
    q[0].save(dst,save_all=True,append_images=q[1:],duration=durs,loop=0,optimize=True,disposal=1)

def load_fx(pptx):
    import timers2
    fx={}
    for i,out in timers2.timers(pptx).items():
        for sp,(k,txt,lk),kind,pcl,pid,st,dur in out:
            if sp is None or pcl not in ('entr','exit'): continue
            name={'1':'appear','10':'fade','23':'zoom','2':'fly'}.get(pid,'fade')
            fx.setdefault(i,{}).setdefault(sp,[]).append((pcl,name,st,dur))
    return fx
def anim_css(effs):
    parts=[]
    for cls,preset,st,dur in effs or []:
        d=max(dur,10)/1000; dl=st/1000
        if cls=='entr':
            nm={'appear':'fx-in-appear','fade':'fx-in-fade','zoom':'fx-in-zoom','fly':'fx-in-fly'}[preset]
            tim='steps(1,end)' if preset=='appear' else 'ease-out'
            parts.append(f'{nm} {d:.3f}s {tim} {dl:.3f}s backwards')
        else:
            nm={'appear':'fx-out-appear','fade':'fx-out-fade','zoom':'fx-out-fade','fly':'fx-out-fly'}[preset]
            tim='steps(1,end)' if preset=='appear' else 'linear'
            parts.append(f'{nm} {d:.3f}s {tim} {dl:.3f}s forwards')
    return ', '.join(parts)
def shape_text(sh): return ' '.join(t.strip() for p in sh['paras'] for t,l in p if t.strip())
def match_inscene(cfg,n,sh):
    if sh['k']!='txt': return None
    t=shape_text(sh)
    for e in cfg.get('inscene',{}).get(n,[]):
        if e['match'] in t: return e
    return None

class Game:
    def __init__(self,pptx,prefix,outdir,cfg):
        self.pptx=pptx; self.prefix=prefix; self.out=outdir; self.cfg=cfg
        self.d=pp.parse(pptx); self.z=zipfile.ZipFile(pptx); self.imgs={}; self.fx=load_fx(pptx)
        os.makedirs(os.path.join(outdir,'images'),exist_ok=True)
    def media(self,name):
        if name in self.imgs: return self.imgs[name]
        data=self.z.read('ppt/media/'+name); ext=name.split('.')[-1].lower()
        base='img_'+prefix_clean(self.prefix)+re.sub(r'\W','',name.split('.')[0])
        tmp=os.path.join(self.out,'images','_tmp.'+ext)
        open(tmp,'wb').write(data)
        im=Image.open(tmp)
        if ext=='gif' and getattr(im,'n_frames',1)>1:
            gif_shrink(im,os.path.join(self.out,'images',base+'.gif'))
        else:
            im.seek(0)
            alpha=('A' in im.getbands()) or im.mode in ('P','LA','PA')
            im=im.convert('RGBA' if alpha else 'RGB')
            im.thumbnail((1100,1100))
            im.save(os.path.join(self.out,'images',base+'.webp'),'WEBP',quality=80,method=6)
        im.close(); os.remove(tmp); self.imgs[name]=base; return base
    def scene(self,n):
        s=self.d[n]; layers=[]
        def pos(g,inner,rot=0,cls='pos'):
            x,y,w,h=g
            st=f'left:{x/SW*100:.3f}%;top:{y/SH*100:.3f}%;width:{w/SW*100:.3f}%;height:{h/SH*100:.3f}%'
            if rot: st+=f';transform:rotate({rot/60000:.2f}deg)'
            return f'<div class="{cls}" style="{st}">{inner}</div>'
        if s['bg'] and s['bg'][0]=='img' and s['bg'][1]:
            layers.append(f'<div class="pos bg">[img[{self.media(s["bg"][1])}]]</div>')
        for sh in s['shapes']:
            e=match_inscene(self.cfg,n,sh)
            if e and sh['geo']:
                st=sh['style']; pt=e.get('pt') or st['sz'] or (25.2 if st['title'] else 18)
                col=e.get('color') or st['color'] or '#000000'
                x,y,w,h=sh['geo']; txt=e.get('text') or shape_text(sh)
                inner=esc_html(txt)
                if e.get('link'): inner=f'[[{inner}|@@T{e["link"]}@@]]'
                deco='underline' if (st['u'] or e.get('underline')) else 'none'
                layers.append(f'<div class="itext" style="left:{x/SW*100:.3f}%;top:{y/SH*100:.3f}%;width:{w/SW*100:.3f}%;font-size:calc({pt/7.2:.3f}*1cqw);color:{col};text-decoration:{deco}">{inner}</div>')
                continue
            if sh['k']=='txt' and sh.get('link') is not None and not shape_text(sh) and sh['geo']:
                lk=sh['link']; tg=n+1 if lk=='next' else n-1 if lk=='prev' else self.cfg.get('first',1) if lk=='first' else lk
                x,y,w,h=sh['geo']
                layers.append(f'<a class="hotspot" data-passage="@@T{tg}@@" style="left:{x/SW*100:.3f}%;top:{y/SH*100:.3f}%;width:{w/SW*100:.3f}%;height:{h/SH*100:.3f}%"></a>')
                continue
            if sh['k']!='pic' or not sh['img'] or not sh['geo']: continue
            late=sh.get('id') in self.cfg.get('timers',{}).get(n,{}).get('late_pics',())
            b=self.media(sh['img']); c=sh['crop']
            l,r,t,bt=[c.get(k,0)/100000 for k in 'lrtb']
            an=anim_css(self.fx.get(n,{}).get(sh.get('id')))
            def wrapfx(x): return f'<div class="fx" style="animation:{an}">{x}</div>' if an else x
            if l or r or t or bt:
                fw,fh=max(1-l-r,.01),max(1-t-bt,.01)
                inner=f'<div class="crop" style="left:{-l/fw*100:.2f}%;top:{-t/fh*100:.2f}%;width:{100/fw:.2f}%;height:{100/fh:.2f}%">[img[{b}]]</div>'
                layers.append(pos(sh['geo'],wrapfx(inner),sh['rot'],'pos clip'+(' late' if late else '')))
            else:
                layers.append(pos(sh['geo'],wrapfx(f'[img[{b}]]'),sh['rot'],'pos late' if late else 'pos'))
        if not layers: return ''
        return '<div class="scene">'+''.join(layers)+'</div>'
    def model(self,n):
        cfg=self.cfg; s=self.d[n]; ov=cfg.get('over',{}).get(n,{})
        story=[];sid=[];btns=[];bid={}
        for sh in s['shapes']:
            if sh['k']!='txt': continue
            if match_inscene(cfg,n,sh): continue
            shid=sh.get('id')
            for para in sh['paras']:
                segs=[];cur=None
                for t,l in para:
                    if not t.strip() and cur is None: continue
                    if l is not None and cur is not None and cur[1]==l and n not in cfg.get('nomerge',()):
                        cur=(cur[0]+t,l)
                    else:
                        if cur: segs.append(cur)
                        cur=(t,l)
                if cur: segs.append(cur)
                has_link=any(l is not None for _,l in segs)
                plain=[]
                for t,l in segs:
                    t=cfg.get('fix',lambda x:x)(t)
                    if l is None:
                        if t.strip() and not (has_link and len(t.strip())<=3): plain.append(t.strip())
                    else:
                        lab=clean_label(t)
                        if not lab: continue
                        if len(lab)>48:
                            story.append(lab); sid.append(shid); btns.append(('Continue',l)); bid[('Continue',l)]=shid
                        else:
                            btns.append((lab,l)); bid[(lab,l)]=shid
                if plain:
                    story.append(' '.join(plain)); sid.append(shid)
        lab=ov.get('labels',{}); btns=[(lab.get(a,a),b) for a,b in btns]
        bid={(lab.get(a,a),b2):v for (a,b2),v in bid.items()}
        keep=[(x,i) for x,i in zip(story,sid) if x not in ov.get('drop_text',())]
        story=[x for x,i in keep]; sid=[i for x,i in keep]
        btns=[(a,b) for a,b in btns if a not in ov.get('drop_btn',())]
        seen=set();nb=[]
        for a,b in btns:
            if (a,b) in seen: continue
            seen.add((a,b)); nb.append((a,b))
        btns=nb
        if 'story' in ov: story=ov['story']; sid=[None]*len(story)
        pre=ov.get('pre_story',[]); add=ov.get('add_story',[])
        story=pre+story+add; sid=[None]*len(pre)+sid+[None]*len(add)
        if 'buttons' in ov: btns=ov['buttons']
        btns=btns+ov.get('add_btn',[])
        if not btns and not ov.get('no_continue') and (n+1) in self.d: btns=[('Continue','next')]
        return {'story':story,'story_ids':sid,'btn_ids':bid,'raw_story':ov.get('raw_story',''),'btns':btns,'scene':self.scene(n)}

def generate(g,starts):
    cfg=g.cfg; names={}; order=[]; models={}
    def resolve(n,l):
        if l=='next': return n+1
        if l=='prev': return n-1
        if l=='first': return cfg['first']
        if isinstance(l,int): return cfg.get('remap',{}).get(l,l)
        return None
    def is_raw(l): return isinstance(l,str) and l not in ('next','prev','first')
    queue=list(starts); seen=set()
    while queue:
        n=queue.pop(0)
        if n in seen or n not in g.d: continue
        seen.add(n); m=g.model(n); models[n]=m; order.append(n)
        for e in cfg.get('inscene',{}).get(n,[]):
            if e.get('link'): queue.append(cfg.get('remap',{}).get(e['link'],e['link']))
        for sh in g.d[n]['shapes']:
            if sh['k']=='txt' and sh.get('link') is not None and not shape_text(sh):
                t=resolve(n,sh['link'])
                if t: queue.append(t)
        for t in cfg.get('extra_edges',{}).get(n,[]): queue.append(t)
        for a,l in m['btns']:
            if not is_raw(l):
                t=resolve(n,l)
                if t: queue.append(t)
    used=set()
    for n in order:
        m=models[n]
        base=cfg.get('names',{}).get(n) or short((m['story'][0] if m['story'] else '') or (m['btns'][0][0] if m['btns'] else 'Scene'))
        nm=cfg.get('exact',{}).get(n) or f'{base} ({g.prefix}{n})'
        names[n]=nm
    out=[]
    for n in order:
        m=models[n]; ov=cfg.get('over',{}).get(n,{}); tags=list(ov.get('tags',[]))
        if n in cfg.get('endings',()): tags.append('ending')
        lines=[]
        def subst(s):
            for mm in set(re.findall(r'@@T(\d+)@@',s)):
                k=int(mm); k=cfg.get('remap',{}).get(k,k)
                s=s.replace(f'@@T{mm}@@',names.get(k,'Start'))
            return s
        if cfg.get('on_enter',{}).get(n): lines.append(subst(cfg['on_enter'][n]))
        if m['scene']: lines.append(subst(m['scene']))
        timed=n in cfg.get('timers',{})
        def tfx(spid):
            return '' if (timed or spid is None) else anim_css(g.fx.get(n,{}).get(spid))
        if m['story'] or m['raw_story']:
            ps=''
            for x,spid in zip(m['story'],m['story_ids']):
                a=tfx(spid); ps+=(f'<p style="animation:{a}">' if a else '<p>')+esc(x)+'</p>'
            lines.append('<div class="story-text">'+ps+m['raw_story']+'</div>')
        def btn(a,l):
            if is_raw(l): return subst(l)
            t=resolve(n,l)
            act=cfg.get('actions',{}).get(n,{}).get(a)
            if t in names:
                x=(f'<<link "{a.replace(chr(34),"")}" "{names[t]}">><<run {act}>><</link>>' if act else f'[[{esc(a)}|{names[t]}]]')
            else: x=''
            an=tfx(m['btn_ids'].get((a,l))) if x else ''
            return f'<span class="fxb" style="animation:{an}">{x}</span>' if an else x
        T=cfg.get('timers',{}).get(n)
        if T:
            fast=[(a,l) for a,l in m['btns'] if a in T['fast']]
            late=[(a,l) for a,l in m['btns'] if a in T['late']]
            rest=[(a,l) for a,l in m['btns'] if a not in T['fast'] and a not in T['late']]
            secs=T['secs']
            lines.append('<div id="opts" class="choices">'+''.join(btn(a,l) for a,l in fast)+'</div>')
            lines.append(f'<div class="timerbar"><span style="animation-duration:{secs}s"></span></div>')
            if rest: lines.append('<div class="choices">'+''.join(btn(a,l) for a,l in rest)+'</div>')
            lines.append(f'<<timed {secs}s>><<replace "#opts">><div class="caught">'+''.join(btn(a,l) for a,l in late)+'</div><</replace>><<run $(".timerbar").remove(); $(".scene .late").show()>><</timed>>')
        else:
            lines.append('<div class="choices">')
            for a,l in m['btns']:
                x=btn(a,l)
                if x: lines.append(x)
            lines.append('</div>')
        out.append(f':: {names[n]}'+(f' [{" ".join(tags)}]' if tags else '')+'\n'+'\n'.join(lines)+'\n')
    if cfg.get('extra'):
        ex=cfg['extra']
        for mm in set(re.findall(r'@@T(\d+)@@',ex)):
            k=int(mm); k=cfg.get('remap',{}).get(k,k); ex=ex.replace(f'@@T{mm}@@',names.get(k,'Start'))
        out.append(ex)
    return out,names,order,models
