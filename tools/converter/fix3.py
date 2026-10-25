s=open('gen.py',encoding='utf8').read()
old='("Press only if you have gotten all 10 endings",133)'
new="""("",'<<if Object.keys(setup.endings).every(function (k) { return (recall("endings") || []).includes(k); })>>[[try for the SECRET ending?|Part 3 Coming Soon]]<</if>>')"""
assert old in s
open('gen.py','w',encoding='utf8').write(s.replace(old,new))
