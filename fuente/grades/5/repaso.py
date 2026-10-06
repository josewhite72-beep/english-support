# -*- coding: utf-8 -*-
"""Repaso (al inicio) — lo que los temas del III Trimestre de 5.º dan por sabido."""
from common import *

BLOCKS = [
    H1("Antes de empezar: repaso"),
    P("Si algo de esta página no lo recuerdas, **repásalo antes de empezar**: te ahorrará muchos errores."),
    H2("1. Presente simple: I play / she plays"),
    TABLE([3300, 3300, 3200], ["Afirmativa", "Negativa", "Pregunta"], [
        ["I / you / we / they **play**.", "I **don't** play.", "**Do** you play?"],
        ["he / she / it **plays**.", "She **doesn't** play.", "**Does** she play?"],
    ]),
    P("Con **he, she, it** el verbo lleva **-s**: walk**s**, like**s**, swim**s**. Respuestas cortas: *Yes, I **do**. / No, I **don't**.*"),
    H2("2. There is / There are (hay)"),
    P("There **is** + una cosa: *There **is** a bin.*   ·   There **are** + varias: *There **are** two bins.*"),
    H2("3. Los días y los momentos del día"),
    P("**Monday** lunes · **Tuesday** martes · **Wednesday** miércoles · **Thursday** jueves · **Friday** viernes · **Saturday** sábado · **Sunday** domingo"),
    P("**in the morning** en la mañana · **in the afternoon** en la tarde · **in the evening** al anochecer · **at night** de noche · **on Saturdays** los sábados"),
    H2("4. La hora"),
    P("*at four o'clock* (4:00) · *at four thirty* (4:30) · **What time is it?** — *It's four o'clock.*"),
    H2("5. Mini-chequeo"),
    P("Responde rápido. Si fallas más de 2, vuelve a leer esta página."),
    ITEMS("1. My sister ______ (play) volleyball.", "2. ______ you like music? — Yes, I do.",
          "3. There ______ (is / are) three bottles.", "4. Traduce: *los sábados* = ______________",
          "5. He ______ (don't / doesn't) like running.", "6. Escribe en inglés: 4:30 = ______________"),
    P("*Respuestas: 1. plays · 2. Do · 3. are · 4. on Saturdays · 5. doesn't · 6. four thirty*"),
]
