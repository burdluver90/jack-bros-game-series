import os
GEN = os.path.dirname(os.path.abspath(__file__))
p = os.path.join(GEN, 'drive31.py'); s = open(p, encoding='utf8').read()
def rep(a, b):
    global s
    if b in s:
        return
    assert a in s, a[:70]; s = s.replace(a, b, 1)

# pickups that would silently fail with a full inventory now stay put until there is room
rep(" 15:{'story':['What is this?','Drink it if things become distorted or you see smiles. Also avoid red things.'],'buttons':[('Drink it',16),('Save it',17)]},",
    " 15:{'story':['What is this?','Drink it if things become distorted or you see smiles. Also avoid red things.'],'buttons':[('Drink it',16),('',KEEP('Save it','almond',17))]},")
rep(" 27:{'story':['Drink it?'],'buttons':[('Drink it',28),('Store it',28)]},",
    " 27:{'story':['Drink it?'],'buttons':[('Drink it',28),('',KEEP('Store it','almond',28))]},")
rep(" 42:{'story':[\"It's a sword!\"],'buttons':[('Take the sword',43),('Leave it',43)]},",
    " 42:{'story':[\"It's a sword!\",'Remember the poster: you will have to fight.'],'buttons':[('',KEEP('Take the sword','sword',43)),('Leave it',43)]},")
rep("     'actions':{15:{'Drink it':'setup.fill(true)','Save it':'setup.addItem(\"almond\")'},\n                27:{'Drink it':'setup.fill(true)','Store it':'setup.addItem(\"almond\")'},\n                42:{'Take the sword':'setup.addItem(\"sword\")'}},",
    "     'actions':{15:{'Drink it':'setup.fill(true)'},27:{'Drink it':'setup.fill(true)'}},")
rep("OVER={", "def KEEP(label, item, to):\n    return f'<<link \"{label}\">><<if setup.addItem(\"{item}\")>><<goto \"@@T{to}@@\">><</if>><</link>>'\nOVER={")
# pinpad: hint after three misses
rep('data-answer=\"red blue green yellow\"></div>', 'data-answer=\"red blue green yellow\" data-hint=\"The virus whispers: four colours. It started with red... then blue.\"></div>')
# a baseball bat floating in the poolrooms
rep("'on_enter':{1:'<<run setup.reset()>>',51:'<<run setup.addItem(\"code\")>>',**{n:FIND(n) for n in WATER_AT}},",
    "'on_enter':{1:'<<run setup.reset()>>',51:'<<run setup.addItem(\"code\")>>',**{n:FIND(n) for n in WATER_AT},23:BAT},")
rep("cfg={'first'", "BAT=('<<if !setup.isTaken(\"bat\")>><div class=\"find\" id=\"fbat\"><<link \"\\U0001F3CF A baseball bat is floating in the water. Grab it\">>'\n     '<<if setup.take(\"bat\",\"bat\")>><<replace \"#fbat\">><</replace>><</if>><</link>></div><</if>>')\ncfg={'first'")
# posters go in after the passages are generated
rep("open(os.path.join(SRC,'Start.twee'),'w',encoding='utf8').write('\\n'.join(out))",
    "import posters\nopen(os.path.join(SRC,'Start.twee'),'w',encoding='utf8').write(posters.add_posters('\\n'.join(out)))")
open(p, 'w', encoding='utf8').write(s)
print('drive31 patched')
