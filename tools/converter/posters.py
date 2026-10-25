# pinned posters that hint at what comes later, built the same way as his hand-made poster on Q82:
# notebook paper (Qimage30), a red pin (Qimage28), the hazmat guy (Qimage44) and his Async label (Qimage58)
import os, re, glob
D = r'C:\Users\dahaw\OneDrive\Desktop\twine-games\part-3-1-backrooms\src\images'
for f in glob.glob(os.path.join(D, 'art_poster_*.svg')):   # older drawn posters are replaced by these
    os.remove(f)

RATIO = 0.754   # his paper's width / height inside a 16:9 scene

TEXT = {
    'almond': ('ALMOND WATER', ['Seeing smiles?', 'Feeling strange?', 'DRINK IT.', 'Then find more.']),
    'cake':   ('NO CAKE =)', ['Never eat food', 'you find here.', 'Especially cake.', 'ESPECIALLY at', 'a party.']),
    'red':    ('AVOID RED', ['Red water.', 'Red doors.', 'Red lights.', 'Black water is', 'weird, not deadly.']),
    'weapon': ('STAY ARMED', ['You WILL have', 'to fight.', 'Bare hands', 'are not enough.', 'Take the weapon.']),
    'down':   ('LOST?', ['Hallway splits?', 'The way DOWN', 'is the way out.', 'Left and right', 'go on forever.']),
    'smiles': ('IF IT SMILES', ['RUN.', 'Never walk', 'toward it.', 'Never say', 'hi back.']),
    'night':  ('AFTER DARK', ['Stay put.', 'Do NOT go', 'into the houses.', 'Do NOT look out', 'the window.']),
    'wait':   ('BE PATIENT', ['Ropes snap.', 'If you can', 'wait it out,', 'WAIT IT OUT.']),
    'party':  ('PARTY TONIGHT', ['Everyone is', 'invited =)', 'Wear a hat.', "Don't let them", 'hear you leave.']),
    'light':  ('BRING A LIGHT', ['Some levels', 'have no lights.', 'Things live', 'in the dark.', 'They HATE light.']),
    'hotel':  ('GRAND HOTEL', ['Ring the bell', 'ONCE.', 'Ask NICELY.', 'Lost on floor 3?', 'Walk backwards.']),
}

def poster(k, style):
    title, lines = TEXT[k]
    return (f'<div class="poster" style="{style}">'
            '<div class="pp" style="left:0;top:0;width:100%;height:100%">[img[img_Qimage30]]</div>'
            '<div class="pp" style="left:3.7%;top:35.7%;width:38.4%;height:60.3%">[img[img_Qimage44]]</div>'
            '<div class="pp" style="left:57.8%;top:72%;width:38.4%;height:23.9%">[img[img_Qimage58]]</div>'
            '<div class="pp clip" style="left:24.4%;top:5%;width:25.3%;height:21.4%;transform:rotate(-114.28deg)"><div class="crop" style="left:-36.94%;top:0;width:136.94%;height:121.76%">[img[img_Qimage28]]</div></div>'
            f'<div class="ptitle">{title}</div><div class="plines">' + '<br>'.join(lines) + '</div></div>')

# where each poster hangs: passage title -> (poster, left%, top%, width%)
PLACES = {
    'What is this place (Q7)': ('almond', 81, 3, 15),
    'He said he dies in (Q23)': ('cake', 2, 3, 15),
    "I don't have a bag (Q25)": ('red', 82, 3, 14),
    'Next (Q28)': ('weapon', 81, 3, 15),
    'Turn around (Q33)': ('down', 2, 4, 14),
    'Try to find the code (Q46)': ('smiles', 82, 3, 14),
    'You see a van (Q60)': ('night', 82, 3, 14),
    'You sit it out until (Q65)': ('wait', None, None, None),
    'Level 1 Hidden': ('party', 80, 4, 15),
    'Level 2 Pipe Dreams': ('light', 66, 4, 13),
    'Level 4 Abandoned Office': ('hotel', 66, 3, 14),
}

def add_posters(text):
    for title, (k, left, top, w) in PLACES.items():
        m = re.search(r'^:: ' + re.escape(title) + r'( \[[^\]]*\])?\n', text, re.M)
        assert m, title
        nxt = text.find('\n:: ', m.end())
        end = nxt if nxt > 0 else len(text)
        block = text[m.end():end]
        if 'class="poster"' in block:
            continue
        if '<div class="scene">' in block and left is not None:
            div = poster(k, f'left:{left}%;top:{top}%;width:{w}%;height:{w * 16 / 9 / RATIO:.1f}%')
            # every scene in the passage gets the poster (some passages have one per virus state)
            new = re.sub(r'(<div class="scene">.*?)(</div>)(?=\n|<<else>>|<</if>>)', lambda mm: mm.group(1) + div + mm.group(2), block)
        else:
            # slide without a picture: hang the poster above the text instead
            new = poster(k, 'position:relative;width:min(230px,42%);aspect-ratio:0.754;margin:0 auto 14px') + '\n' + block
        assert new != block, title
        text = text[:m.end()] + new + text[end:]
    return text
