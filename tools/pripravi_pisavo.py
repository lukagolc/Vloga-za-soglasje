#!/usr/bin/env python3
"""Vgradi pisave in logotipa ENSET v lib/viri.js.

- Liberation Sans (navadna, krepka) in lib/logo_enset.png: tehnicna dokumentacija
- Vloga Sans (Carlito, glej tools/pripravi_carlito.py) in lib/logo_enset_pooblastilo.png:
  pooblastilo po vzorcu ENSET

Brskalnik iz datoteke, odprte z diska (file://), ne more brati datotek ob strani,
zato so pisavi in logotip za PDF (pooblastilo, tehnicna dokumentacija) vgrajeni kot base64.
Pisava je potrebna za slovenske znake (c, s, z s stresico).

Uporaba: python3 tools/pripravi_pisavo.py   (ko zamenjate pisavo ali logotip)
"""
import base64
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
b = lambda p: base64.b64encode((ROOT / p).read_bytes()).decode('ascii')
data = {
    'VS_PISAVA': b('lib/fonts/LiberationSans-Regular.ttf'),
    'VS_PISAVA_B': b('lib/fonts/LiberationSans-Bold.ttf'),
    'VS_LOGO': b('lib/logo_enset.png'),
    'VS_VLOGA_R': b('lib/fonts/VlogaSans-Regular.ttf'),
    'VS_VLOGA_B': b('lib/fonts/VlogaSans-Bold.ttf'),
    'VS_VLOGA_I': b('lib/fonts/VlogaSans-Italic.ttf'),
    'VS_LOGO_P': b('lib/logo_enset_pooblastilo.png'),
}
out = ROOT / 'lib' / 'viri.js'
out.write_text('// Samodejno ustvarjeno s tools/pripravi_pisavo.py - ne urejajte rocno.\n'
               + ''.join(f'window.{k} = {json.dumps(v)};\n' for k, v in data.items()), encoding='ascii')
print(f'{out.relative_to(ROOT)}: {out.stat().st_size // 1024} KB')
