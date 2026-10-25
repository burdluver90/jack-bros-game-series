import os
G=os.path.dirname(os.path.abspath(__file__))
p=os.path.join(G,'build.py')
b=open(p,encoding='utf8').read()
def rep(old,new):
    global b
    assert old in b, old[:90]
    b=b.replace(old,new,1)

# 1) hotspots: invisible clickable areas for shapes that are links with no text
rep("""            if sh['k']!='pic' or not sh['img'] or not sh['geo']: continue
            late=""","""            if sh['k']=='txt' and sh.get('link') is not None and not shape_text(sh) and sh['geo']:
                lk=sh['link']; tg=n+1 if lk=='next' else n-1 if lk=='prev' else self.cfg.get('first',1) if lk=='first' else lk
                x,y,w,h=sh['geo']
                layers.append(f'<a class="hotspot" data-passage="@@T{tg}@@" style="left:{x/SW*100:.3f}%;top:{y/SH*100:.3f}%;width:{w/SW*100:.3f}%;height:{h/SH*100:.3f}%"></a>')
                continue
            if sh['k']!='pic' or not sh['img'] or not sh['geo']: continue
            late=""")

# 2) BFS: follow hotspots and extra edges
rep("""        for e in cfg.get('inscene',{}).get(n,[]):
            if e.get('link'): queue.append(cfg.get('remap',{}).get(e['link'],e['link']))""","""        for e in cfg.get('inscene',{}).get(n,[]):
            if e.get('link'): queue.append(cfg.get('remap',{}).get(e['link'],e['link']))
        for sh in g.d[n]['shapes']:
            if sh['k']=='txt' and sh.get('link') is not None and not shape_text(sh):
                t=resolve(n,sh['link'])
                if t: queue.append(t)
        for t in cfg.get('extra_edges',{}).get(n,[]): queue.append(t)""")

# 3) placeholder substitution helper used by scene, raw buttons and on-enter code
rep("""        if m['scene']:
            sc=m['scene']
            for mm in set(re.findall(r'@@T(\\d+)@@',sc)): sc=sc.replace(f'@@T{mm}@@',names.get(int(mm),'Start'))
            lines.append(sc)""","""        def subst(s):
            for mm in set(re.findall(r'@@T(\\d+)@@',s)):
                k=int(mm); k=cfg.get('remap',{}).get(k,k)
                s=s.replace(f'@@T{mm}@@',names.get(k,'Start'))
            return s
        if cfg.get('on_enter',{}).get(n): lines.append(subst(cfg['on_enter'][n]))
        if m['scene']: lines.append(subst(m['scene']))""")

# 4) buttons: raw strings get placeholders; buttons can run an action when clicked
rep("""        def btn(a,l):
            if is_raw(l): return l
            t=resolve(n,l)
            x=f'[[{esc(a)}|{names[t]}]]' if t in names else ''""","""        def btn(a,l):
            if is_raw(l): return subst(l)
            t=resolve(n,l)
            act=cfg.get('actions',{}).get(n,{}).get(a)
            if t in names:
                x=(f'<<link "{a.replace(chr(34),"")}" "{names[t]}">><<run {act}>><</link>>' if act else f'[[{esc(a)}|{names[t]}]]')
            else: x=''""")

# 5) extra hand-written passages
rep("    return out,names,order,models","    if cfg.get('extra'): out.append(cfg['extra'])\n    return out,names,order,models")
open(p,'w',encoding='utf8').write(b)
print('build.py patched')
