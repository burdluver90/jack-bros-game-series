L=open('gen.py',encoding='utf8').read().split('\n')
new=r"""    if body: lines.append('<div class="story-text">\n\n'+body.replace('\n','\n\n')+'\n\n</div>')"""
L[64:71]=[new]
open('gen.py','w',encoding='utf8').write('\n'.join(L))
