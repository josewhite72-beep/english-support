# -*- coding: utf-8 -*-
"""Gramática de consulta rápida (al final del libro) — 3.er grado."""
from common import *

BLOCKS = [
    H1("Gramática de consulta rápida"),
    P("Usa estas páginas la noche antes de una prueba. Al lado de cada tema está **dónde se explica con más detalle**."),

    H2("Números 1–10 (Temas 5.1 y 5.2)"),
    TABLE([1960, 1960, 1960, 1960, 1960], ["1", "2", "3", "4", "5"], [
        ["one", "two", "three", "four", "five"],
        ["**6**", "**7**", "**8**", "**9**", "**10**"],
        ["six", "seven", "eight", "nine", "ten"],
    ]),

    H2("Número + fruta (Tema 5.1)"),
    P("**one** apple (sin -s) · **two** apple**s** · **five** banana**s** · *How many oranges? — **Three** oranges.*"),
    P("*I **have** two mangoes.* · *I **want** three apples.* · *I **don't have** bananas.*"),

    H2("En la tienda (Tema 5.2)"),
    TABLE([4900, 4900], ["Cliente", "Vendedor"], [
        ["*Can I have four mangoes, **please**?*", "*Here you are.*"],
        ["*How **much** is it?*", "*It's two **dollars**.* (*one dollar*, sin -s)"],
        ["*Thank you!*", "*Have a nice day!*"],
    ]),

    H2("can / can't (Temas 6.1 y 6.2)"),
    TABLE([3300, 3300, 3200], ["Puedo", "No puedo", "Pregunta"], [
        ["I **can** see a bird.", "I **can't** see the river.", "**Can** you see it? — Yes, I **can**."],
        ["The fish **can** swim.", "The fish **can't** walk.", "**Can** a bird fly? — Yes, it **can**."],
    ]),

    H2("in, on, under, near (Tema 6.1)"),
    P("**in** = dentro de · **on** = sobre · **under** = debajo de · **near** = cerca de  ·  *The bird **is** in the tree.*"),

    H2("I'm + lugar o sentimiento · We + acción (Tema 6.2)"),
    P("*I'**m** outside.* · *I'**m** happy.* · *We **walk** on the trail.* · *We **play** on the grass.*"),

    H2("Palabras que más se confunden en las pruebas"),
    TABLE([3000, 6800], ["Palabras", "Diferencia"], [
        ["**apple / apples**", "Una sola: sin -s. Más de una: con **-s** (*one dollar · two dollars*)."],
        ["**can / can't**", "En *can't* se oye la **t** al final. Escucha con atención en las pruebas."],
    ]),
]
