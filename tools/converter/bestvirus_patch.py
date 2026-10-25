# the virus bestiary card shows its black tendrils after it absorbs the Bacteria
import os
GEN = os.path.dirname(os.path.abspath(__file__))
def patch(f, pairs):
    p = os.path.join(GEN, f); s = open(p, encoding='utf8').read()
    for a, b in pairs:
        if b in s:
            continue
        assert a in s, (f, a[:80]); s = s.replace(a, b, 1)
    open(p, 'w', encoding='utf8').write(s)

TENDRILS = ('<svg class="btend" viewBox="0 0 100 100" preserveAspectRatio="none">'
            '<g fill="none" stroke="#050505" stroke-linecap="round">'
            '<path d="M50 40 C30 30 18 20 4 6" stroke-width="3.5"/><path d="M50 42 C70 30 82 22 96 8" stroke-width="3.5"/>'
            '<path d="M50 55 C28 60 14 72 2 92" stroke-width="3"/>'
            '<path d="M14 16 l-5 2 M24 26 l-3 -5 M84 18 l5 1 M74 28 l3 -5 M12 76 l-5 -2 M22 66 l-2 -5" stroke-width="2"/></g></svg>')

patch('bestiary.twee', [
    ("seen2: ['One reason my kind is (Q80)'],", "seen2: ['One reason my kind is (Q80)'], seen3: ['Bacteria Absorb'],"),
    ("    if (x.seen2 && x.seen2.indexOf(t) >= 0) { setup.bestMark(x.id, 'form2'); }",
     "    if (x.seen2 && x.seen2.indexOf(t) >= 0) { setup.bestMark(x.id, 'form2'); }\n"
     "    if (x.seen3 && x.seen3.indexOf(t) >= 0) { setup.bestMark(x.id, 'form2'); setup.bestMark(x.id, 'form3'); }"),
    ("<div class=\"bimg\"><img src=\"' + img + '\" alt=\"\"></div>",
     "<div class=\"bimg\"><img src=\"' + img + '\" alt=\"\">' + (e.form3 ? '" + TENDRILS + "' : '') + '</div>"),
])
# the extra line about the tendrils, shown once you have seen it absorb the Bacteria
s = open(os.path.join(GEN, 'bestiary.twee'), encoding='utf8').read()
i = s.index("setup.openBestiary")
j = s.index("x.desc", i)
print(s[j - 80:j + 80])
