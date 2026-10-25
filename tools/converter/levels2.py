# Level Fun, part 2: after the virus mutates (between Q82 and "To be continued")
# the virus is always the same layout as on the mutation slide (Q80), just moved and scaled
import os
GEN = os.path.dirname(os.path.abspath(__file__))
VIRUS = ('<div class="pos clip" style="left:33.930%;top:17.297%;width:21.175%;height:80.481%"><div class="crop" style="left:-44.01%;top:-17.29%;width:190.37%;height:118.73%">[img[img_Qimage79]]</div></div>'
         '<div class="pos clip" style="left:25.454%;top:18.477%;width:6.622%;height:50.690%;transform:rotate(63.30deg)"><div class="crop" style="left:-130.83%;top:-61.77%;width:608.68%;height:188.50%">[img[img_Qimage79]]</div></div>'
         '<div class="pos clip" style="left:57.587%;top:28.067%;width:5.439%;height:49.521%;transform:rotate(-47.66deg)"><div class="crop" style="left:-431.55%;top:-80.61%;width:741.07%;height:221.97%">[img[img_Qimage79]]</div></div>')
END = 'Partypoopers'

def scene(bg, left, top, k):
    # a same-aspect box keeps the rotated arms exactly as he placed them
    return (f'<div class="scene"><div class="pos bg">[img[{bg}]]</div>'
            f'<div class="pos" style="left:{left}%;top:{top}%;width:{k * 100:.1f}%;height:{k * 100:.1f}%">{VIRUS}</div></div>')

def find(k):
    return (f'<<if !setup.isTaken("{k}")>><div class="find" id="f{k}"><<link "\U0001F4A7 There' + "'" + f's a bottle of almond water here. Take it">>'
            f'<<if setup.take("{k}","almond")>><<replace "#f{k}">><</replace>><</if>><</link>></div><</if>>')

def story(*ps):
    return '<div class="story-text">' + ''.join(f'<p>{p}</p>' for p in ps) + '</div>'

P = []
P.append(':: Fun With The Virus [fun]\n' + find('wv1') + '\n' + scene('art_funvirus', -14, 8, .75) + '\n' + story(
    'The music gets louder. Streamers, balloons, the smell of cake. You are back in Level Fun.',
    'The virus crouches beside you behind a balloon stand. "Since my mutation I can hear their hearts," it whispers. "Seven of them... no. Eight."',
    '"Stay close to me."') +
    '\n<div class="choices">[[Sneak behind the virus|Present Hallway]][[Pop a balloon to distract them|Balloon Distraction]][[Let the virus fight them|Virus Fight]]</div>\n')
P.append(':: Balloon Distraction [fun]\n' + scene('art_levelfun', 52, 10, .7) + '\n' + story(
    'You squeeze a balloon until it goes POP.',
    'Every partygoer turns at the same time, toward the sound. They shuffle over to it, giggling. =)',
    'The virus grabs your arm with one of its long claws and pulls you the other way.') +
    '\n<div class="choices">[[Slip away|Present Hallway]]</div>\n')
P.append(':: Virus Fight [fun]\n' + scene('art_funroar', 6, -2, 1) + '\n' + story(
    'The virus steps out from behind the balloons. Its tendrils flex, twelve times stronger than before.',
    'It throws three partygoers across the room like party favours.',
    'Then the music stops. Every smiling face in the room turns to look at YOU.') +
    '\n<div id="opts" class="choices">[[Run while the virus holds them off|Present Hallway]]</div>\n'
    '<div class="timerbar"><span style="animation-duration:3s"></span></div>\n'
    '<<timed 3s>><<replace "#opts">><div class="caught">[[They grab you|Party Forever Ending]]</div><</replace>><<run $(".timerbar").remove()>><</timed>>\n')
P.append(':: Present Hallway [fun]\n' + scene('art_funhall', 45, 14, .8) + '\n' + story(
    'A long hallway stacked with wrapped presents.',
    'One big yellow present has a tag on it: FOR YOU =)',
    'The virus sniffs it. Its tendrils curl back. "That one smells wrong."') +
    '\n<div class="choices">[[Open your present|Present Ending]][[Let the virus open it|Virus Opens The Present]][[Leave it and keep moving|The Way Out]]</div>\n')
P.append(':: Virus Opens The Present [fun]\n' + scene('art_funhall', 45, 14, .8) + '\n' + story(
    'The virus rips the paper open with one claw.',
    'A burst of confetti... and a party hat. Underneath is a note: YOU ARE INVITED. FOREVER. =)',
    'The virus eats the note. "Keep the hat," it says. "They like hats."') +
    '\n<div class="choices"><<link "Take the party hat" "The Way Out">><<run setup.addItem("hat")>><</link>>[[Leave it|The Way Out]]</div>\n')
P.append(':: The Way Out [fun]\n' + scene('art_funhold', 22, 10, .85) + '\n' + story(
    'At the end of the hallway is a grey door marked WAY OUT.',
    'In front of it stands the biggest partygoer you have ever seen. Its smile stretches all the way around its head.',
    'The virus moves in front of you.') +
    '\n<div class="choices"><<if setup.has("hat")>><<link "Put on the party hat and walk past" "Party Hat Escape">><</link>><</if>>'
    '[[Let the virus hold it back|The Virus Holds The Door]][[Run past it|Biggest Partygoer Ending]]</div>\n')
P.append(':: Party Hat Escape [fun]\n' + scene('art_funhold', 22, 10, .85) + '\n' + story(
    'You put on the party hat and smile the widest smile you can.',
    'The giant partygoer looks at you for a long time. Then it waves. =)',
    'You walk right past it. The virus follows, trying very hard to look like a balloon.<<set $virusWith to true>>') +
    f'\n<div class="choices">[[Through the door|{END}]]</div>\n')
P.append(':: The Virus Holds The Door [fun]\n' + scene('art_funhold', 22, 10, .85) + '\n' + story(
    'The virus wraps every tendril it has around the giant partygoer and holds on.',
    '"GO!" it shouts. "I always find you. I will find you again."',
    'You run through the door. Behind you the music starts again.<<set $virusWith to false>>') +
    f'\n<div class="choices">[[Keep running|{END}]]</div>\n')
for name, bg, lines in (
        ('Party Forever Ending', 'art_partychase', ['They pull you into the middle of the room and put a party hat on your head.', 'The party never ends. Neither do you. =)']),
        ('Present Ending', 'art_funhall', ['You pull the ribbon. The box opens by itself.', 'Something inside is smiling. Some surprises are not good surprises.']),
        ('Biggest Partygoer Ending', 'art_funhold', ['You try to duck under its arm.', 'Its arm is much, much longer than you thought.'])):
    P.append(f':: {name} [ending]\n<div class="scene"><div class="pos bg">[img[{bg}]]</div></div>\n' + story(*lines) +
             '\n<div class="choices">[[Try again|Start]]</div>\n')

open(os.path.join(GEN, 'levels2.twee'), 'w', encoding='utf8').write('\n'.join(P))
print(len(P), 'passages')
