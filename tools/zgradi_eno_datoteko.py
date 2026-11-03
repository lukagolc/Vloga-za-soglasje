#!/usr/bin/env python3
"""Zgradi Vloga-za-soglasje.html: index.html z vgrajenimi knjiznicami in pisavo.

Ena datoteka deluje povsod (priponka v e-posti, kopija na namizje),
ker ne potrebuje mape lib/. Po vsaki spremembi index.html zazenite:
  python3 tools/zgradi_eno_datoteko.py
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
html = (ROOT / 'index.html').read_text(encoding='utf-8')


def inline(m):
    js = (ROOT / m.group(1)).read_text(encoding='utf-8')
    assert '</script' not in js.lower(), m.group(1)
    return '<script>\n' + js + '\n</script>'


out, n = re.subn(r'<script src="(lib/[^"]+)"></script>', lambda m: inline(m), html)
assert n == 3, f'pricakovane 3 knjiznice, najdenih {n}'
dest = ROOT / 'Vloga-za-soglasje.html'
dest.write_text(out, encoding='utf-8')
print(f'{dest.name}: {dest.stat().st_size // 1024} KB')
