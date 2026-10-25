import zipfile,re
def parse(path):
    z=zipfile.ZipFile(path)
    names=z.namelist()
    sl=sorted([int(re.findall(r'\d+',n)[0]) for n in names if re.match(r'ppt/slides/slide\d+\.xml$',n)])
    out={}
    for i in sl:
        x=z.read(f'ppt/slides/slide{i}.xml').decode('utf8')
        rl=z.read(f'ppt/slides/_rels/slide{i}.xml.rels').decode()
        rels={}
        for m in re.finditer(r'<Relationship [^>]*>',rl):
            t=m.group(0); a=re.search(r'Id="([^"]+)"',t).group(1); b=re.search(r'Target="([^"]+)"',t).group(1)
            rels[a]=b
        def tgt(attrs):
            a=re.search(r'action="([^"]*)"',attrs); r=re.search(r'r:id="([^"]+)"',attrs)
            act=a.group(1) if a else ''
            if 'jump=' in act:
                j=act.split('jump=')[-1]; return {'nextslide':'next','previousslide':'prev','firstslide':'first','lastslide':'last'}.get(j,j)
            if r and r.group(1) in rels:
                m=re.search(r'slide(\d+)\.xml',rels[r.group(1)])
                if m and 'Layout' not in rels[r.group(1)]: return int(m.group(1))
            return None
        shapes=[]
        for m in re.finditer(r'<p:(sp|pic)>(.*?)</p:\1>',x,flags=re.S):
            kind,sp=m.group(1),m.group(2)
            off=re.search(r'<a:off x="(-?\d+)" y="(-?\d+)"',sp); ext=re.search(r'<a:ext cx="(\d+)" cy="(\d+)"',sp)
            geo=(int(off.group(1)),int(off.group(2)),int(ext.group(1)),int(ext.group(2))) if off and ext else None
            rot=re.search(r'<a:xfrm[^>]*rot="(-?\d+)"',sp)
            shape_link=None
            c=re.search(r'<p:cNvPr[^>]*>(.*?)</p:cNvPr>',sp,flags=re.S)
            if c:
                h=re.search(r'<a:hlinkClick([^>]*)/?>',c.group(1))
                if h: shape_link=tgt(h.group(1))
            if kind=='pic':
                emb=re.search(r'r:embed="([^"]+)"',sp)
                crop=re.search(r'<a:srcRect([^>]*)/>',sp)
                cr={k:int(v) for k,v in re.findall(r'(\w)="(-?\d+)"',crop.group(1))} if crop else {}
                img=re.search(r'media/(image\d+\.\w+)',rels.get(emb.group(1),'')) if emb else None
                pid=re.search(r'<p:cNvPr[^>]*? id="(\d+)"',sp)
                shapes.append({'k':'pic','id':pid.group(1) if pid else None,'img':img.group(1) if img else None,'geo':geo,'rot':int(rot.group(1)) if rot else 0,'crop':cr,'link':shape_link})
            else:
                paras=[]
                for p in re.findall(r'<a:p>(.*?)</a:p>',sp,flags=re.S):
                    runs=[]
                    for r in re.findall(r'<a:r>(.*?)</a:r>',p,flags=re.S):
                        t=''.join(re.findall(r'<a:t>([^<]*)</a:t>',r))
                        h=re.search(r'<a:hlinkClick([^>]*)/?>',r)
                        runs.append((t,tgt(h.group(1)) if h else None))
                    if runs: paras.append(runs)
                st={'sz':None,'u':False,'color':None,'title':'type="title"' in sp,'b':False}
                r0=re.search(r'<a:r>(.*?)</a:r>',sp,flags=re.S)
                if r0:
                    rp=re.search(r'<a:rPr([^>]*)>',r0.group(1))
                    if rp:
                        z1=re.search(r'sz="(\d+)"',rp.group(1)); st['sz']=int(z1.group(1))/100 if z1 else None
                        st['u']='u="sng"' in rp.group(1); st['b']='b="1"' in rp.group(1)
                    fill=re.search(r'<a:solidFill>(.*?)</a:solidFill>',r0.group(1),flags=re.S)
                    if fill:
                        c=re.search(r'srgbClr val="(\w+)"',fill.group(1)); sc=re.search(r'schemeClr val="(\w+)"',fill.group(1))
                        TH={'dk1':'000000','dk2':'158158','lt1':'FFFFFF','lt2':'F3F3F3','accent2':'50B432','hlink':'2200CC'}
                        st['color']='#'+(c.group(1) if c else TH.get(sc.group(1),'000000') if sc else '000000')
                tid=re.search(r'<p:cNvPr[^>]*? id="(\d+)"',sp)
                shapes.append({'k':'txt','id':tid.group(1) if tid else None,'paras':paras,'geo':geo,'link':shape_link,'style':st})
        bg=None
        b=re.search(r'<p:bg>(.*?)</p:bg>',x,flags=re.S)
        if b:
            e=re.search(r'<a:blip [^>]*r:embed="([^"]+)"',b.group(1))
            c=re.search(r'srgbClr val="(\w+)"',b.group(1))
            if e:
                m=re.search(r'media/(image\d+\.\w+)',rels.get(e.group(1),'')); bg=('img',m.group(1) if m else None)
            elif c: bg=('color','#'+c.group(1))
        adv=re.search(r'advTm="(\d+)"',x)
        out[i]={'shapes':shapes,'bg':bg,'adv':int(adv.group(1)) if adv else None,'hidden':'show="0"' in x[:800]}
    return out
def show(d,only=None):
    for i,s in d.items():
        if only and i not in only: continue
        parts=[]
        for sh in s['shapes']:
            if sh['k']=='txt':
                segs=[]
                for p in sh['paras']:
                    for t,l in p:
                        if t.strip(): segs.append(f'[{t.strip()}→{l}]' if l is not None else t.strip())
                if segs or sh['link'] is not None: parts.append(' '.join(segs)+(f' SHAPE→{sh["link"]}' if sh['link'] is not None else ''))
            elif sh['link'] is not None: parts.append(f'(pic {sh["img"]} →{sh["link"]})')
        pics=[sh['img'] for sh in s['shapes'] if sh['k']=='pic']
        if parts or pics: print(i,'bg',s['bg'],'adv',s['adv'],'|',' ; '.join(parts),'| pics',len(pics))
