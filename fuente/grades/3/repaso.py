# -*- coding: utf-8 -*-
"""Repaso (al inicio) — lo que los temas del III Trimestre de 3.er grado dan por sabido."""
from common import *

BLOCKS = [
    H1("Antes de empezar: repaso"),
    P("Si algo de esta página no lo recuerdas, **repásalo antes de empezar**."),
    H2("1. Los números del 1 al 10"),
    TABLE([1960, 1960, 1960, 1960, 1960], ["1", "2", "3", "4", "5"], [
        ["one", "two", "three", "four", "five"],
    ]),
    TABLE([1960, 1960, 1960, 1960, 1960], ["6", "7", "8", "9", "10"], [
        ["six", "seven", "eight", "nine", "ten"],
    ]),
    H2("2. Los colores"),
    P("**red** rojo · **blue** azul · **yellow** amarillo · **green** verde · **orange** anaranjado · **brown** café · **white** blanco · **black** negro"),
    H2("3. I am / It is"),
    P("*I **am** happy.* (Yo estoy feliz.) · *It **is** big.* (Es grande.) · *The sky **is** blue.* (El cielo es azul.)"),
    H2("4. Palabras amables"),
    P("**please** por favor · **thank you** gracias · **good morning** buenos días · **goodbye** adiós"),
    H2("5. Mini-chequeo"),
    ITEMS("1. Escribe en inglés: 3 = ______________", "2. Escribe en inglés: 8 = ______________",
          "3. Traduce: *verde* = ______________", "4. Traduce: *gracias* = ______________",
          "5. I ______ (am / is) happy.", "6. The banana ______ (am / is) yellow."),
    P("*Respuestas: 1. three · 2. eight · 3. green · 4. thank you · 5. am · 6. is*"),
]
