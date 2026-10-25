# the virus hates the Bacteria: their kinds have always fought
import os
GEN = os.path.dirname(os.path.abspath(__file__))
def patch(f, pairs):
    p = os.path.join(GEN, f); s = open(p, encoding='utf8').read()
    for a, b in pairs:
        if b in s:
            continue
        assert a in s, (f, a[:80]); s = s.replace(a, b, 1)
    open(p, 'w', encoding='utf8').write(s)

patch('levels3.py', [
    ("'The virus goes very still. \"That,\" it says, \"is a bacteria. I am basically one too. But it is not like me.\"'",
     "'The virus goes very still. Then every one of its tendrils starts to shake. \"Bacteria,\" it growls. \"My kind and its kind have been at war since the very first level. They hunted us when we were small. Not anymore.\"'"),
    ("'The virus pushes you behind it. \"My turn.\"'",
     "'The virus shoves you behind it, shaking with rage. \"Get back. This one is MINE.\"'"),
    ("'The virus shoots its tendrils straight into the Bacteria.",
     "'The virus lets out a roar you can feel in your teeth and slams into the Bacteria. It shoots its tendrils straight into it."),
    ("\"Much better,\" it says. \"Now I can fight with you.\"",
     "\"That is for every one of us your kind ever ate,\" it hisses at the stain. Then it turns to you, calm again. \"Much better. Now I can fight with you.\""),
])
patch('bestiary.twee', [
    ("Cut one of its black tendrils and two grow back.'",
     "Cut one of its black tendrils and two grow back. It and the virus\\'s kind have always been at war, and the virus hates it.'"),
])
print('rage')
