#!/usr/bin/env python3
"""Pripravi pisavo za pooblastilo (po vzorcu ENSET, ki je v pisavi Carlito).

Carlito (SIL OFL 1.1, rezervirano ime »Carlito«) zmanjša na latinične znake s
šumniki in ga zato preimenuje v »Vloga Sans« (OFL ne dovoli, da spremenjena
pisava nosi rezervirano ime). Izhod: lib/fonts/VlogaSans-{Regular,Bold,Italic}.ttf

Uporaba: pip install fonttools && python3 tools/pripravi_carlito.py [mapa s Carlito-*.ttf]
Privzeta mapa: /usr/share/fonts/truetype/crosextra (paket fonts-crosextra-carlito).
"""
import sys
from pathlib import Path
from fontTools import subset
from fontTools.ttLib import TTFont

ROOT = Path(__file__).resolve().parent.parent
SRC = Path(sys.argv[1] if len(sys.argv) > 1 else '/usr/share/fonts/truetype/crosextra')
ZNAKI = list(range(0x20, 0x7F)) + list(range(0xA0, 0x180)) + [0x2013, 0x2014, 0x2018, 0x2019, 0x201A, 0x201C, 0x201D, 0x201E, 0x2022, 0x2026, 0x20AC, 0x00B7]
for stil in ['Regular', 'Bold', 'Italic']:
    f = TTFont(SRC / f'Carlito-{stil}.ttf')
    opt = subset.Options(); opt.name_IDs = ['*']; opt.layout_features = ['kern', 'liga']
    s = subset.Subsetter(opt); s.populate(unicodes=ZNAKI); s.subset(f)
    for rec in f['name'].names:
        if rec.nameID in (1, 3, 4, 6, 16, 17):
            t = rec.toUnicode().replace('Carlito', 'Vloga Sans' if rec.nameID != 6 else 'VlogaSans')
            rec.string = t
    out = ROOT / 'lib' / 'fonts' / f'VlogaSans-{stil}.ttf'
    f.save(out)
    print(out.name, out.stat().st_size // 1024, 'KB')
