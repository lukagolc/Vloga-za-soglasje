#!/usr/bin/env python3
"""Vgradi pisavo (Liberation Sans) v lib/pisava.js.

Brskalnik iz datoteke, odprte z diska (file://), ne more brati datotek ob strani,
zato je pisava za PDF (pooblastilo, tehnicna dokumentacija) vgrajena kot base64.
Pisava je potrebna za slovenske znake (c, s, z s stresico).

Uporaba: python3 tools/pripravi_pisavo.py   (samo, ce zamenjate pisavo)
"""
import base64
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
font = base64.b64encode((ROOT / 'lib' / 'fonts' / 'LiberationSans-Regular.ttf').read_bytes()).decode('ascii')
out = ROOT / 'lib' / 'pisava.js'
out.write_text('// Samodejno ustvarjeno s tools/pripravi_pisavo.py - ne urejajte rocno.\n'
               f'window.VS_PISAVA = "{font}";\n', encoding='ascii')
print(f'{out.relative_to(ROOT)}: {out.stat().st_size // 1024} KB')
