# -*- coding: utf-8 -*-
"""Repaso (al inicio) — lo que los temas del III Trimestre de 6.º dan por sabido."""
from common import *

BLOCKS = [
    H1("Antes de empezar: repaso"),
    P("Si algo de esta página no lo recuerdas, **repásalo antes de empezar**: te ahorrará muchos errores."),
    H2("1. There is / There are (hay)"),
    TABLE([3300, 3300, 3200], ["Una cosa", "Varias cosas", "Pregunta"], [
        ["There **is** a park.", "There **are** two parks.", "**Is there** a market?"],
        ["There **isn't** a library.", "There **aren't** any shops.", "**Are there** many trees?"],
    ]),
    H2("2. El verbo to be en pasado: was / were"),
    P("Lo vas a necesitar en el Theme 2, para hablar de **cómo era antes** tu escuela."),
    TABLE([3300, 3300, 3200], ["Afirmativa", "Negativa", "Pregunta"], [
        ["I / he / she / it **was**", "It **wasn't** big.", "**Was** it old?"],
        ["you / we / they **were**", "They **weren't** here.", "**Were** you a student?"],
    ]),
    H2("3. Adjetivos para describir lugares"),
    TABLE([2450, 2450, 2450, 2450], ["Inglés", "Español", "Inglés", "Español"], [
        ["big", "grande", "small", "pequeño"],
        ["old", "viejo, antiguo", "new", "nuevo"],
        ["busy", "con mucho movimiento", "quiet", "tranquilo"],
        ["beautiful", "hermoso", "famous", "famoso"],
    ]),
    P("En inglés el adjetivo va **antes** del sustantivo y **no cambia** en plural: *a **big** park* · *two **big** parks*."),
    H2("4. Cómo se leen los años"),
    P("Los años se leen en **dos partes**: 1965 = *nineteen sixty-five* · 1998 = *nineteen ninety-eight* · 2010 = *twenty ten* · 2026 = *twenty twenty-six*. Excepción: 2005 = *two thousand five*."),
    H2("5. Mini-chequeo"),
    P("Responde rápido. Si fallas más de 2, vuelve a leer esta página."),
    ITEMS("1. There ______ (is / are) three classrooms.", "2. ______ there a church in your community?",
          "3. The school ______ (was / were) small in 1990.", "4. My grandparents ______ (was / were) students there.",
          "5. Escribe en palabras: 1985 = ______________________", "6. Traduce: *un parque tranquilo* = ______________________"),
    P("*Respuestas: 1. are · 2. Is · 3. was · 4. were · 5. nineteen eighty-five · 6. a quiet park*"),
]
