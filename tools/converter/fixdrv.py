import os
G=os.path.dirname(os.path.abspath(__file__))
BS=chr(92)
for f in ('drive3.py','drive21.py'):
    p=os.path.join(G,f)
    L=open(p,encoding='utf8').read().split(chr(10))
    out=[];i=0
    while i<len(L):
        if L[i].endswith("write(':: Fx Styles [stylesheet]") and i+1<len(L):
            out.append(L[i]+BS+'n'+L[i+1]); i+=2
        else:
            out.append(L[i]); i+=1
    open(p,'w',encoding='utf8').write(chr(10).join(out))
print('fixed')
