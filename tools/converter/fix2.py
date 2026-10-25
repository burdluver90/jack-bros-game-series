s=open('gen.py',encoding='utf8').read()
s=s.replace("""[("Go Alone",3),("Go With Him",5)]""","""[("",'[[Go Alone|Bike or Car][$withMan to false]]'),("",'[[Go With Him|Go to the Store][$withMan to true]]')]""")
s=s.replace("""[("Beef",81),("Chicken",80),("Pork",79)]""","""[("Beef",81),("",'<<if $withMan>>[[Chicken|Person From the Beginning]]<<else>>[[Chicken|Lost in the Store Ending]]<</if>>'),("Pork",79)]""")
import re
s=re.sub(r"\n80:\(.*?\n","\n",s,count=1)
s=s.replace("80:'Mysterious Man Check',","")
s=s.replace("lines+= [f'[[{l}|{N[t]}]]' for l,t in links]","lines+= [(t if isinstance(t,str) else f'[[{l}|{N[t]}]]') for l,t in links]")
open('gen.py','w',encoding='utf8').write(s)
