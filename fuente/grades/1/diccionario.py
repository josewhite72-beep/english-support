# -*- coding: utf-8 -*-
"""Mi diccionario de dibujos (al final del libro) — 1.er grado. Junta el vocabulario de todos los temas."""
from common import *
import importlib

def _vocab():
    out = []
    for m in ("t51", "t52", "t61", "t62"):
        try: mod = importlib.import_module(m)
        except ImportError: continue
        out += [(img, w, f"{pr} {es}") for img, w, pr, es, _ in mod.VOCAB if img == w and w not in [x[1] for x in out]]
    return out

BLOCKS = [
    H1("Mi diccionario de dibujos"),
    P("Todas las palabras del libro. **Adulto:** señale un dibujo y pregunte *What is it?* El niño responde en inglés."),
    PICS(_vocab(), cols=4, size=70),
]
