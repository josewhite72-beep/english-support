# -*- coding: utf-8 -*-
"""Gramática de consulta rápida (al final del libro) — 5.º."""
from common import *

BLOCKS = [
    H1("Gramática de consulta rápida"),
    P("Usa estas páginas la noche antes de una prueba. Al lado de cada tema está **dónde se explica con más detalle**."),

    H2("like + -ing (Tema 5.1)"),
    TABLE([3300, 3300, 3200], ["Afirmativa", "Negativa", "Pregunta"], [
        ["I / you / we **like** walking", "I **don't like** running", "**Do** you **like** swimming?"],
        ["he / she **likes** dancing", "she **doesn't like** running", "**Does** she **like** reading?"],
    ]),
    P("-ing: walk**ing** · danc**ing** (sin e) · swi**mm**ing (doble letra)  ·  *Yes, I do. / No, I don't.*"),

    H2("can / can't (Tema 5.2)"),
    TABLE([3300, 3300, 3200], ["Afirmativa", "Negativa", "Pregunta"], [
        ["I / she / we **can** swim", "I **can't** climb", "**Can** you swim? — Yes, I **can**."],
    ]),
    P("*can* nunca cambia y el verbo va solo: ✗ she cans · ✗ can swimming · ✗ can to swim"),
    P("**like** = gusto (*I like swimming*) · **can** = habilidad (*I can swim*)"),

    H2("Presente simple con we (Tema 6.1)"),
    P("*We **recycle** every day. We **put** bottles in the bin. We **don't throw** trash on the floor.*"),

    H2("There is / There are (Temas 6.1 y 6.2)"),
    P("There **is** + una cosa · There **are** + varias · **Is there...? / Are there...?**"),

    H2("can / could (Temas 6.1 y 6.2)"),
    TABLE([4900, 4900], ["can", "could"], [
        ["ahora: *We **can** make compost.*", "antes: *We **could** make compost last year.*"],
        ["", "cortesía: ***Could** you repeat that, please?*"],
    ]),

    H2("Pasos en orden (Tema 6.2)"),
    P("**First,** ... → **Then** ... → **Next,** ... → **Finally,** ..."),

    H2("Palabras que más se confunden en las pruebas"),
    TABLE([3000, 6800], ["Palabras", "Diferencia"], [
        ["**like / likes**", "*I like* · *you like* · *we like*, pero *he **likes*** · *she **likes***."],
        ["**do / can** (respuestas)", "*Do you like...? — Yes, I **do**.*  ·  *Can you...? — Yes, I **can**.*"],
        ["**can / can't**", "En *can't* se oye la **t** al final. Escucha con atención en las pruebas."],
    ]),
]
