# -*- coding: utf-8 -*-
"""Repaso (al inicio) — lo que los temas del III Trimestre de 4.º dan por sabido."""
from common import *

BLOCKS = [
    H1("Antes de empezar: repaso"),
    P("Si algo de esta página no lo recuerdas, **repásalo antes de empezar**: te ahorrará muchos errores."),
    H2("1. El verbo to be: am, is, are"),
    TABLE([3300, 3300, 3200], ["Afirmativa", "Negativa", "Pregunta"], [
        ["I **am** happy.", "I'**m not** cold.", "**Am** I late?"],
        ["He / She / It **is** wet.", "It **isn't** big.", "**Is** it sunny?"],
        ["We / You / They **are** here.", "They **aren't** at home.", "**Are** you ready?"],
    ]),
    H2("2. Presente simple: I eat / she eats"),
    P("*I **eat** rice.* · *She **eats** rice.* (con he / she / it el verbo lleva **-s**) · *Do you like fruit? — Yes, I **do**.*"),
    H2("3. Palabras para preguntar"),
    TABLE([2400, 2400, 5000], ["Palabra", "Significa", "Ejemplo"], [
        ["**What**", "¿Qué?", "What is it? — It's a towel."],
        ["**Where**", "¿Dónde?", "Where is the map? — It's in the bag."],
        ["**Who**", "¿Quién?", "Who is she? — She's my sister."],
    ]),
    H2("4. Ropa y colores"),
    P("**hat** sombrero · **shirt** camisa · **shoes** zapatos · **dress** vestido  ·  **red, blue, yellow, green, black, white, gray**"),
    H2("5. Mini-chequeo"),
    P("Responde rápido. Si fallas más de 2, vuelve a leer esta página."),
    ITEMS("1. The sky ______ (is / are) blue.", "2. We ______ (is / are) at the beach.",
          "3. ______ is my hat? — It's on the table.", "4. My brother ______ (eat / eats) fruit.",
          "5. Traduce: *zapatos* = ______________", "6. ______ is he? — He's my dad."),
    P("*Respuestas: 1. is · 2. are · 3. Where · 4. eats · 5. shoes · 6. Who*"),
]
