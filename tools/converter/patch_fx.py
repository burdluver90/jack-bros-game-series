import re
G=r'C:\Users\dahaw\AppData\Local\Temp\gen'
def rd(p): return open(G+'\\'+p,encoding='utf8').read()
def wr(p,s): open(G+'\\'+p,'w',encoding='utf8').write(s)
def rep(s,old,new,count=1):
    assert old in s, old[:80]
    return s.replace(old,new,count)

# ---- timers2: click effects start 1s after the previous effect
t=rd('timers2.py')
t=rep(t,"st=(ps if kind=='withEffect' else pe)+delay","st=(ps if kind=='withEffect' else pe)+delay+(1000 if kind=='clickEffect' else 0)")
wr('timers2.py',t)

# ---- pp.py: shape ids on text shapes
p=rd('pp.py')
p=rep(p,"shapes.append({'k':'txt','paras':paras,'geo':geo,'link':shape_link,'style':st})",
 "tid=re.search(r'<p:cNvPr[^>]*? id=\"(\\d+)\"',sp)\n                shapes.append({'k':'txt','id':tid.group(1) if tid else None,'paras':paras,'geo':geo,'link':shape_link,'style':st})")
wr('pp.py',p)

b=rd('build.py')
# ---- fx loading + css helper
b=rep(b,"def shape_text(sh):",'''def load_fx(pptx):
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
def shape_text(sh):''')
b=rep(b,"self.d=pp.parse(pptx); self.z=zipfile.ZipFile(pptx); self.imgs={}","self.d=pp.parse(pptx); self.z=zipfile.ZipFile(pptx); self.imgs={}; self.fx=load_fx(pptx)")
# ---- scene: wrap animated pictures
old="""            if l or r or t or bt:
                fw,fh=max(1-l-r,.01),max(1-t-bt,.01)
                inner=f'<div class="crop" style="left:{-l/fw*100:.2f}%;top:{-t/fh*100:.2f}%;width:{100/fw:.2f}%;height:{100/fh:.2f}%">[img[{b}]]</div>'
                layers.append(pos(sh['geo'],inner,sh['rot'],'pos clip'+(' late' if late else '')))
            else:
                layers.append(pos(sh['geo'],f'[img[{b}]]',sh['rot'],'pos late' if late else 'pos'))"""
new="""            an=anim_css(self.fx.get(n,{}).get(sh.get('id')))
            def wrapfx(x): return f'<div class="fx" style="animation:{an}">{x}</div>' if an else x
            if l or r or t or bt:
                fw,fh=max(1-l-r,.01),max(1-t-bt,.01)
                inner=f'<div class="crop" style="left:{-l/fw*100:.2f}%;top:{-t/fh*100:.2f}%;width:{100/fw:.2f}%;height:{100/fh:.2f}%">[img[{b}]]</div>'
                layers.append(pos(sh['geo'],wrapfx(inner),sh['rot'],'pos clip'+(' late' if late else '')))
            else:
                layers.append(pos(sh['geo'],wrapfx(f'[img[{b}]]'),sh['rot'],'pos late' if late else 'pos'))"""
b=rep(b,old,new)
# ---- model: carry shape ids
b=rep(b,"        story=[];btns=[]\n        for sh in s['shapes']:\n            if sh['k']!='txt': continue\n            if match_inscene(cfg,n,sh): continue",
 "        story=[];sid=[];btns=[];bid={}\n        for sh in s['shapes']:\n            if sh['k']!='txt': continue\n            if match_inscene(cfg,n,sh): continue\n            shid=sh.get('id')")
b=rep(b,"                            story.append(lab); btns.append(('Continue',l))\n                        else: btns.append((lab,l))\n                if plain: story.append(' '.join(plain))",
 "                            story.append(lab); sid.append(shid); btns.append(('Continue',l)); bid[('Continue',l)]=shid\n                        else:\n                            btns.append((lab,l)); bid[(lab,l)]=shid\n                if plain:\n                    story.append(' '.join(plain)); sid.append(shid)")
b=rep(b,"        lab=ov.get('labels',{}); btns=[(lab.get(a,a),b) for a,b in btns]\n        story=[x for x in story if x not in ov.get('drop_text',())]",
 "        lab=ov.get('labels',{}); btns=[(lab.get(a,a),b) for a,b in btns]\n        bid={(lab.get(a,a),b2):v for (a,b2),v in bid.items()}\n        keep=[(x,i) for x,i in zip(story,sid) if x not in ov.get('drop_text',())]\n        story=[x for x,i in keep]; sid=[i for x,i in keep]")
b=rep(b,"        if 'story' in ov: story=ov['story']\n        story=ov.get('pre_story',[])+story+ov.get('add_story',[])",
 "        if 'story' in ov: story=ov['story']; sid=[None]*len(story)\n        pre=ov.get('pre_story',[]); add=ov.get('add_story',[])\n        story=pre+story+add; sid=[None]*len(pre)+sid+[None]*len(add)")
b=rep(b,"        return {'story':story,'btns':btns,'scene':self.scene(n)}","        return {'story':story,'story_ids':sid,'btn_ids':bid,'raw_story':ov.get('raw_story',''),'btns':btns,'scene':self.scene(n)}")
# ---- generate: apply text/button animations
b=rep(b,"        if m['story']: lines.append('<div class=\"story-text\">'+''.join(f'<p>{esc(x)}</p>' for x in m['story'])+'</div>')",
"""        timed=n in cfg.get('timers',{})
        def tfx(spid):
            return '' if (timed or spid is None) else anim_css(g.fx.get(n,{}).get(spid))
        if m['story'] or m['raw_story']:
            ps=''
            for x,spid in zip(m['story'],m['story_ids']):
                a=tfx(spid); ps+=(f'<p style="animation:{a}">' if a else '<p>')+esc(x)+'</p>'
            lines.append('<div class="story-text">'+ps+m['raw_story']+'</div>')""")
b=rep(b,"""        def btn(a,l):
            if is_raw(l): return l
            t=resolve(n,l)
            return f'[[{esc(a)}|{names[t]}]]' if t in names else ''""","""        def btn(a,l):
            if is_raw(l): return l
            t=resolve(n,l)
            x=f'[[{esc(a)}|{names[t]}]]' if t in names else ''
            an=tfx(m['btn_ids'].get((a,l))) if x else ''
            return f'<span class="fxb" style="animation:{an}">{x}</span>' if an else x""")
wr('build.py',b)

# ---- drive3: timed slides no longer need JS-hidden pictures
d=rd('drive3.py')
d=re.sub(r"'late_pics':\[[^\]]*\]","'late_pics':[]",d)
wr('drive3.py',d)
print('patched')
