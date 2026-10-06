# -*- coding: utf-8 -*-
"""Gramática de consulta rápida (al final del libro) — 4.º."""
from common import *

BLOCKS = [
    H1("Gramática de consulta rápida"),
    P("Usa estas páginas la noche antes de una prueba. Al lado de cada tema está **dónde se explica con más detalle**."),

    H2("Instrucciones (Tema 5.1)"),
    P("Empiezan con el verbo: ***Pack** your towel.* · ***Bring** water.*  ·  Para decir no: ***Don't forget** the map.*"),

    H2("going to: planes (Tema 5.1)"),
    TABLE([3300, 3300, 3200], ["Afirmativa", "Negativa", "Pregunta"], [
        ["I'**m going to** pack.", "I'**m not going to** swim.", "**Are** you **going to** go?"],
        ["She'**s going to** pack.", "He **isn't going to** come.", "**What are** you **going to** pack?"],
    ]),

    H2("Frecuencia (Tema 5.2)"),
    P("**always** 100 % · **usually** 80 % · **sometimes** 50 % · **never** 0 %  ·  Van **antes del verbo**: *I **always** pack fruit.*"),
    P("Con he / she el verbo lleva **-s**: *She never drink**s** juice.*"),

    H2("Presente continuo: ahora (Temas 6.1 y 6.2)"),
    TABLE([3300, 3300, 3200], ["Afirmativa", "Negativa", "Pregunta"], [
        ["I **am** jump**ing**.", "It **isn't** rain**ing**.", "**Is** it rain**ing**?"],
        ["She **is** wear**ing** boots.", "They **aren't** play**ing**.", "**What are** you do**ing**?"],
    ]),

    H2("Where / What / Who (Tema 6.1)"),
    P("***Where** is the puddle? — Near the door.* · ***What** is she wearing? — A raincoat.* · ***Who** has an umbrella? — Ana.*"),

    H2("need / wear (Tema 6.2)"),
    P("*What do you **need**? — I need **an** umbrella.* · *What do you **wear** in the rain? — I wear boots.* · *She **needs** a raincoat.*"),

    H2("Palabras que más se confunden en las pruebas"),
    TABLE([3000, 6800], ["Palabras", "Diferencia"], [
        ["**a / an**", "*an* antes de vocal: *an umbrella*. *a* antes de consonante: *a raincoat*."],
        ["**is / are**", "*is* con una cosa o persona; *are* con varias: *My boots **are** wet.*"],
        ["**wear / wearing**", "*I wear boots* (siempre) · *I am wearing boots* (ahora)."],
        ["**rain / raining**", "*The rain is cold* (la lluvia) · *It is raining* (está lloviendo)."],
    ]),
]
