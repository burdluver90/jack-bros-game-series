s=open('gen.py',encoding='utf8').read()
a="""'<<if Object.keys(setup.endings).every(function (k) { return (recall("endings") || []).includes(k); })>>[[try for the SECRET ending?|Part 3 Coming Soon]]<</if>>'"""
b="""'<<if Object.keys(setup.endings).every(function (k) { return k === "Secret Ending" || (recall("endings") || []).includes(k); })>>[[try for the SECRET ending?|Secret Ending]]<</if>>'"""
assert a in s
s=s.replace(a,b)
c='147:("Secret ending plus 6000 aura",[("To beginning",1)]'
assert c in s
s=s.replace(c,'147:("Secret ending plus 6000 aura",[("Continue",133),("To beginning",1)]')
open('gen.py','w',encoding='utf8').write(s)
