# Normal / Hard: timers scale with the mode, and Normal shows a hint on the riskiest choices
import re

HINTS = {
    'Fight (Q9)': "You're not strong enough to fight this yet.",
    "Wait don't run (Q11)": 'It sounds like it wants to talk.',
    'I am a virus basically (Q12)': 'Going off alone in the Backrooms is never a good idea.',
    'You enter a large poolrooms (Q14)': 'The water looks dangerous. Maybe just listen.',
    "I don't have a bag (Q25)": 'Remember the poster: never eat the cake.',
    'One slide has black water (Q29)': 'Red means danger. Black is strange, but not deadly.',
    'Left (Q35)': 'Remember the poster: the way down is the way out.',
    "It's a sword! (Q42)": 'You will need a weapon later. Really.',
    'Run (Q49)': 'Remember: if it smiles, RUN.',
    'How can i escape (Q53)': 'Fighting only works if you have a weapon. Waiting never works.',
    'Wait here (Q63)': 'The poster said to stay put after dark.',
    'You hide and you hear (Q64)': 'Whatever you do, do not look out the window.',
    'You make it to the (Q66)': 'Be patient. Ropes snap.',
    'Whos him? Maybe the clown? (Q69)': 'Never take your eyes off him.',
    'As long as he thinks (Q76)': 'Rushing it will get you crushed.',
    'Level 1 Dark Hall': 'Hide. Now.',
    'Level Fun': 'They can hear you. Stay quiet, and do not eat anything.',
    'Level Fun Exits': 'Avoid red. And quiet doors are safer than fast ones.',
    'Party Chase': 'The table might hide you.',
    'Present Hallway': 'Presents here are not always presents.',
    'The Way Out': 'Partygoers like hats.',
    'Level 2 Pipe Dreams': 'The hot pipe is a bad idea. Grab what you can first.',
    'Level 6 Lights Out': 'Whispers in the dark are never friendly.',
    'Hotel Front Desk': 'Ring once. Only once.',
    'Hotel Concierge': 'Be polite. Do not ask about the exit.',
    'Hotel Room 211': 'The guest book warned you about this TV.',
    'Hotel Room 217': 'The guest book said not to answer.',
    'Hotel Floor 3': 'The guest book said to walk backwards.',
    'Hotel Room 213 Footsteps': 'Wardrobes are good hiding spots. Beds are not.',
    'Hotel Boiler Room': 'Polite guests get to check out.',
}

def apply(text):
    # <<timed 3s>> becomes mode-scaled
    text = re.sub(r'<<timed (\d+(?:\.\d+)?)s>>', lambda m: f'<<timed `setup.t({m.group(1)})`>>', text)
    for title, hint in HINTS.items():
        m = re.search(r'^:: ' + re.escape(title) + r'( \[[^\]]*\])?\n', text, re.M)
        assert m, title
        nxt = text.find('\n:: ', m.end())
        end = nxt if nxt > 0 else len(text)
        block = text[m.end():end]
        if 'class="modehint"' in block:
            continue
        line = f'<<if setup.mode().hints>><p class="modehint">{hint}</p><</if>>'
        # put the hint right before the choices
        i = block.find('<div class="choices"')
        if i < 0:
            i = block.find('<div id="opts"')
        assert i >= 0, ('no choices in', title)
        block = block[:i] + line + '\n' + block[i:]
        text = text[:m.end()] + block + text[end:]
    return text
