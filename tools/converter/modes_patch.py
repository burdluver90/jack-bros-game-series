import os
GEN = os.path.dirname(os.path.abspath(__file__))
def patch(f, pairs):
    p = os.path.join(GEN, f); s = open(p, encoding='utf8').read()
    for a, b in pairs:
        if b in s:
            continue
        assert a in s, (f, a[:70]); s = s.replace(a, b, 1)
    open(p, 'w', encoding='utf8').write(s)

patch('hud.twee', [
    ("setup.DRAIN = 3;      /* sanity lost every scene */\nsetup.FUN_DRAIN = 6;  /* Level Fun drains sanity faster */",
     "/* Normal and Hard: sanity lost per scene (Level Fun drains twice as fast), how long timers last, wrong codes allowed */\n"
     "setup.MODES = {\n"
     "  normal: { label: 'Normal', drain: 2, timer: 1.5, codeTries: 3, hints: true },\n"
     "  hard:   { label: 'Hard',   drain: 4, timer: 0.75, codeTries: 1, hints: false }\n"
     "};\n"
     "setup.mode = function () { return setup.MODES[State.variables.mode] || setup.MODES.normal; };\n"
     "setup.t = function (secs) { return (secs * setup.mode().timer).toFixed(2) + 's'; };"),
    ("setup.drainFor = function (p) { return p.tags.indexOf('fun') >= 0 ? setup.FUN_DRAIN : setup.DRAIN; };",
     "setup.drainFor = function (p) { var d = setup.mode().drain; return p.tags.indexOf('fun') >= 0 ? d * 2 : d; };"),
    ("State.variables.sanity = 100 + (beforeMove ? setup.DRAIN : 0);",
     "State.variables.sanity = 100 + (beforeMove ? setup.mode().drain : 0);"),
    ("Engine.play(v.codeTries >= 2 ? 'Boiler Ending' : 'Hotel Keypad Wrong');",
     "Engine.play(v.codeTries >= setup.mode().codeTries ? 'Boiler Ending' : 'Hotel Keypad Wrong');"),
    ("(miss >= 3 && pad.attr('data-hint') ?", "(miss >= 3 && setup.mode().hints && pad.attr('data-hint') ?"),
])
# timer bars stretch to match the mode
patch('hud.twee', [
    ("$(document).on(':passagedisplay', function () { $('#passages .codepad').each(function () { setup.buildPad(this); }); });",
     "$(document).on(':passagedisplay', function () { $('#passages .codepad').each(function () { setup.buildPad(this); }); });\n"
     "$(document).on(':passagedisplay', function () {\n"
     "  $('#passages .timerbar span').each(function () { var d = parseFloat(this.style.animationDuration) || 3; this.style.animationDuration = setup.t(d); });\n"
     "  if (!setup.mode().hints) { $('#passages .modehint').remove(); }\n"
     "});"),
    # show the mode in the hotbar
    ("h.html('<div class=\"top\"><span class=\"lbl\">Sanity</span>",
     "h.html('<div class=\"top\"><span class=\"mode ' + (State.variables.mode || 'normal') + '\">' + setup.mode().label + '</span><span class=\"lbl\">Sanity</span>"),
    (".codepad .chint { color: #fde68a; font-weight: normal; }",
     ".codepad .chint { color: #fde68a; font-weight: normal; }\n"
     "#hud .mode { font-size: .7rem; letter-spacing: .1em; text-transform: uppercase; padding: .15em .6em; border-radius: 99px; border: 1px solid #4fd18b; color: #c9ffe0; }\n"
     "#hud .mode.hard { border-color: #ef4444; color: #fecaca; background: #3a1418; }\n"
     ".modehint { margin: 10px auto 0; max-width: 34em; text-align: center; font-size: .92rem; color: #fde68a; }\n"
     ".modehint::before { content: '\\1F4A1  '; }\n"
     ".modepick { display: flex; flex-wrap: wrap; gap: 14px; justify-content: center; margin: 8px 0 4px; }\n"
     ".modepick .mcard { width: 230px; padding: 14px 16px; border-radius: 14px; border: 2px solid #4fd18b; background: #10231a; text-align: center; }\n"
     ".modepick .mcard.hard { border-color: #ef4444; background: #2a0f12; }\n"
     ".modepick .mcard p { margin: 6px 0 12px; font-size: .88rem; color: #d6d3c4; }"),
])

# title screen: choose a mode
patch('drive31.py', [
    ("'buttons':[('Play',4)],'tags':['nodrain','nohud']},",
     "'buttons':[('',MODEPICK)],'tags':['nodrain','nohud']},"),
    ("def KEEP(label, item, to):",
     "MODEPICK=('<div class=\"modepick\">'\n"
     "  '<div class=\"mcard\"><<link \"Play on Normal\" \"@@T4@@\">><<set $mode to \"normal\">><</link>><p>Sanity drains slowly, timers give you extra time, 3 tries at codes, and hints show up when you need them.</p></div>'\n"
     "  '<div class=\"mcard hard\"><<link \"Play on Hard\" \"@@T4@@\">><<set $mode to \"hard\">><</link>><p>Sanity drains twice as fast, timers are short, one wrong code is the end, and there are no hints. Good luck.</p></div>'\n"
     "  '</div>')\n"
     "def KEEP(label, item, to):"),
    ("import posters\nopen(os.path.join(SRC,'Start.twee'),'w',encoding='utf8').write(posters.add_posters('\\n'.join(out)))",
     "import posters, modes\nopen(os.path.join(SRC,'Start.twee'),'w',encoding='utf8').write(modes.apply(posters.add_posters('\\n'.join(out))))"),
])
print('mode patches applied')
