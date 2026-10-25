SCENE_CSS=""".scene { position: relative; width: 100%; max-width: calc(46vh * 16 / 9); aspect-ratio: 16 / 9; margin: 0 auto 1em; background: #000; overflow: hidden; border-radius: 12px; box-shadow: 0 6px 24px rgba(0,0,0,.55); }
.scene .pos { position: absolute; }
.scene .pos img { width: 100%; height: 100%; display: block; }
.scene .pos.bg { left: 0; top: 0; width: 100%; height: 100%; }
.scene .pos.clip { overflow: hidden; }
.scene .crop { position: absolute; }
.scene .crop img { width: 100%; height: 100%; display: block; }
.choices a { display: inline-block; padding: .6em 1.4em; min-width: 7em; border-radius: 999px; border: 2px solid #5b8cff; background: #17233f; color: #fff; font-weight: bold; text-decoration: none; transition: transform .12s, background .12s; }
.choices a:hover { background: #5b8cff; transform: translateY(-2px) scale(1.04); }
body.ending .choices a { border-color: #ff6b6b; background: #3a1620; }
body.ending .choices a:hover { background: #ff6b6b; }
.choices a, .caught a { display: inline-block; padding: .6em 1.4em; min-width: 7em; border-radius: 999px; border: 2px solid #5b8cff; background: #17233f; color: #fff; font-weight: bold; text-decoration: none; transition: transform .12s, background .12s; }
.caught { display: flex; justify-content: center; flex-wrap: wrap; gap: 12px; }
.caught a { border-color: #ff6b6b; background: #3a1620; animation: pop .25s ease; }
.caught a:hover { background: #ff6b6b; }
@keyframes pop { from { transform: scale(.7); opacity: 0; } to { transform: none; opacity: 1; } }
.scene .pos.late { display: none; }
.timerbar { max-width: 320px; height: 8px; margin: .2em auto 1em; background: #26304d; border-radius: 99px; overflow: hidden; }
.timerbar span { display: block; height: 100%; background: #ff6b6b; transform-origin: left; animation-name: shrink; animation-timing-function: linear; animation-fill-mode: forwards; }
@keyframes shrink { from { transform: scaleX(1); } to { transform: scaleX(0); } }
.scene { container-type: inline-size; }
.scene .itext { position: absolute; padding: 1cqw; box-sizing: border-box; line-height: 1.2; font-family: Arial, Helvetica, sans-serif; overflow-wrap: break-word; text-align: left; }
.scene .itext a { color: inherit; text-decoration: inherit; cursor: pointer; }
"""
