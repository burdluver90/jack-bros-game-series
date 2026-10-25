import os
GEN = os.path.dirname(os.path.abspath(__file__))
p = os.path.join(GEN, 'drive31.py')
s = open(p, encoding='utf8').read()
s = s.replace(" 83:{'story'", " 82:{'buttons':[('','[[Next|Fun With The Virus]]')]},\n 83:{'story'", 1)
s = s.replace("'extra_edges':{53:[54]}", "'extra_edges':{53:[54],82:[83]}", 1)
s = s.replace("open(os.path.join(GEN,'levels.twee'),encoding='utf8').read()}",
              "open(os.path.join(GEN,'levels.twee'),encoding='utf8').read()+chr(10)+open(os.path.join(GEN,'levels2.twee'),encoding='utf8').read()}", 1)
open(p, 'w', encoding='utf8').write(s)
print("82:{'buttons'" in s, '82:[83]' in s, 'levels2' in s)
