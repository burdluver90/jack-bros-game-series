import zipfile,re,sys
def timers(path):
    z=zipfile.ZipFile(path); res={}
    for n in sorted([n for n in z.namelist() if re.match(r'ppt/slides/slide\d+\.xml$',n)],key=lambda s:int(re.findall(r'\d+',s)[0])):
        i=int(re.findall(r'\d+',n)[0]); x=z.read(n).decode('utf8')
        t=re.search(r'<p:timing.*?</p:timing>',x,flags=re.S)
        if not t: continue
        shapes={}
        for m in re.finditer(r'<p:(sp|pic)>(.*?)</p:\1>',x,flags=re.S):
            idm=re.search(r'<p:cNvPr[^>]*? id="(\d+)"',sp) or re.search(r'<p:cNvPr id="(\d+)"',sp)
            if not idm: continue
            txt=' '.join(s.strip() for s in re.findall(r'<a:t>([^<]*)</a:t>',sp) if s.strip())[:40]
            lk=re.search(r'<a:hlinkClick([^>]*)/?>',sp)
            shapes[idm.group(1)]=(m.group(1),txt,bool(lk))
        s=t.group(0); effects=[]
        # each effect node
        for m in re.finditer(r'<p:cTn [^>]*nodeType="(clickEffect|withEffect|afterEffect)"[^>]*>(.*?)(?=<p:cTn [^>]*nodeType="(?:clickEffect|withEffect|afterEffect)"|</p:timing>)',s,flags=re.S):
            kind,body=m.group(1),m.group(2)
            head=m.group(0)[:m.group(0).index('>')+1]
            pc=re.search(r'presetClass="(\w+)"',head); pid=re.search(r'presetID="(\d+)"',head)
            d=re.search(r'<p:stCondLst><p:cond delay="(\d+)"',body)
            delay=int(d.group(1)) if d else 0
            durs=[int(v) for v in re.findall(r'<p:cTn [^>]*dur="(\d+)"',body)]
            tg=re.findall(r'spid="(\d+)"',body)
            effects.append((kind,pc.group(1) if pc else '?',pid.group(1) if pid else '?',delay,max(durs) if durs else 0,tg[0] if tg else None))
        # timeline
        ps=0;pe=0;out=[]
        for kind,pcl,pid,delay,dur,sp in effects:
            st=(ps if kind=='withEffect' else pe)+delay
            en=st+dur; ps=st; pe=max(pe,en) if kind=='withEffect' else en
            out.append((sp,shapes.get(sp,('?','',False)),kind,pcl,pid,st,dur))
        res[i]=out
    return res
if __name__=='__main__':
    for fn in sys.argv[1:]:
        print('#####',fn)
        for i,out in timers('C:/Users/dahaw/Downloads/'+fn).items():
            for sp,(k,txt,lk),kind,pcl,pid,st,dur in out:
                if pcl=='entr' and st>0 or lk:
                    print(f'  slide {i}: shape {sp} {k} {txt!r} link={lk} {kind} {pcl}/{pid} starts {st}ms dur {dur}')
