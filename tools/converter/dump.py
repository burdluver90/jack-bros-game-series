import zipfile,re,sys
z=zipfile.ZipFile(sys.argv[1])
sl=sorted([n for n in z.namelist() if re.match(r'ppt/slides/slide\d+\.xml$',n)],key=lambda s:int(re.findall(r'\d+',s)[0]))
print(len(sl),'slides; media',len([n for n in z.namelist() if 'media/' in n]))
for n in sl:
    i=int(re.findall(r'\d+',n)[0])
    x=z.read(n).decode('utf8')
    rl=z.read(f'ppt/slides/_rels/slide{i}.xml.rels').decode()
    rels={}
    for m in re.finditer(r'<Relationship [^>]*>',rl):
        t=m.group(0); a=re.search(r'Id="([^"]+)"',t).group(1); b=re.search(r'Target="([^"]+)"',t).group(1)
        mm=re.search(r'slides/slide(\d+)\.xml|^slide(\d+)\.xml',b)
        if mm and 'slideLayout' not in b: rels[a]=mm.group(1) or mm.group(2)
    imgs=re.findall(r'media/(image\d+\.\w+)',rl)
    items=[]
    for sp in re.findall(r'<p:(?:sp|pic|cxnSp)>.*?</p:(?:sp|pic|cxnSp)>',x,flags=re.S):
        t=' '.join(s.strip() for s in re.findall(r'<a:t>([^<]*)</a:t>',sp) if s.strip())
        tg=[]
        for h in re.findall(r'<a:hlinkClick([^>]*)/?>',sp):
            r=re.search(r'r:id="(rId\d+)"',h); a=re.search(r'action="([^"]*)"',h)
            if r and r.group(1) in rels: tg.append(rels[r.group(1)])
            elif a: tg.append(a.group(1).split('?jump=')[-1].split('/')[-1])
        if t or tg: items.append(repr(t)+(f'->{tg}' if tg else ''))
    hidden=' HIDDEN' if 'show="0"' in x[:600] else ''
    if items or imgs: print(i,hidden,'|',' ; '.join(items),'| IMG',imgs if imgs else '')
