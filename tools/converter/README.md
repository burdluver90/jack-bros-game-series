# Converter and build scripts

These are the scripts that turned the Jack-Bros PowerPoint games into the Twine (SugarCube) games in this repo, plus everything added to Part 3.1.

The paths inside them point at folders on the computer they were written on (`C:\Users\dahaw\...`), so change those paths if you run them somewhere else.

## PowerPoint to Twine
- `pp.py` reads a .pptx: slides, pictures, text, links and backgrounds.
- `timers2.py` reads the slide animations (fade, zoom and so on).
- `build.py` is the general converter. It makes one Twine passage per slide with the pictures layered like the slide, and keeps the buttons and animations.
- `fx.css` holds the animation styles.
- `gen.py`, `shrink.py` and `shrink2.py` build Part 2 (Finding Milk) and compress its images.
- `drive21.py` builds Part 2.1 (the basement).
- `drive3.py` and `drive3_css.py` build Part 3 (Grown Up).
- `drive31.py` builds Part 3.1 (The Backrooms Escape).

## Part 3.1 extras
- `hud.twee`: sanity meter, 6-slot inventory, Normal and Hard modes, code pads, posters, liminal effects and hum.
- `levels.twee`: Level 1 and Level Fun.
- `levels2.py`: Level Fun after the virus mutates.
- `levels3.py`: Levels 2, 4, 6 and !.
- `hotel.py`: Level 5, the Grand Hotel.
- `posters.py`: hint posters built from the hand-made poster pieces.
- `modes.py`: Normal-mode hints and timer scaling.
- `virus_art.py`, `art_detail.py`, `art_detail2.py` and `pg_defs.txt`: the drawn SVG art.
- `bot.js`: the playtest bot. Paste it into the game page's console to play hundreds of runs automatically.

## Rebuilding Part 3.1
Run these in order: `levels2.py`, `levels3.py`, `art_detail.py`, `hotel.py`, `drive31.py`. Then build the story with Tweego (or the Twine MCP) into `part-3-1-backrooms/index.html`.
