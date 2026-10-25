import os
GEN = os.path.dirname(os.path.abspath(__file__))
def patch(f, pairs):
    p = os.path.join(GEN, f); s = open(p, encoding='utf8').read()
    for a, b, must in pairs:
        if b in s:
            continue
        assert a in s, (f, a); s = s.replace(a, b, 1)
    open(p, 'w', encoding='utf8').write(s)
patch('levels3.py', [("END = 'To be continued... (Q83)'", "END = 'Hotel Arrival'", 1)])
patch('drive31.py', [
    (" 60:{'drop_text'", " 55:{'story':['Here is the pinpad','Type in the code.'],'buttons':[('','<div class=\"codepad\" data-kind=\"colors\" data-ok=\"@@T56@@\" data-answer=\"red blue green yellow\"></div>')]},\n 60:{'drop_text'", 1),
    ("open(os.path.join(GEN,'levels3.twee'),encoding='utf8').read()}", "open(os.path.join(GEN,'levels3.twee'),encoding='utf8').read()+chr(10)+open(os.path.join(GEN,'hotel.twee'),encoding='utf8').read()}", 1),
    ("'extra_edges':{53:[54],82:[83]}", "'extra_edges':{53:[54],55:[56],82:[83]}", 1)])
patch('hud.twee', [("'level-run': 'Level Run For Your Life' };", "'level-run': 'Level Run For Your Life', 'hotel': 'Hotel Arrival' };", 1)])
print('patched')
