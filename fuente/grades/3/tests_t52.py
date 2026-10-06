# -*- coding: utf-8 -*-
"""Mini-tests del Tema 5.2 · 3.er grado (fuente única para el libro y la versión en línea)."""
from common import *

TESTS = {
 "listening": {"skill": "listening", "total": 6,
  "tip": ["Antes de escuchar, **lee las preguntas** con calma.",
          "En este audio hay **números de frutas** y **números de dólares**. ¡No los confundas!"],
  "review": "Vocabulario (audio 01) y la práctica con el audio 04 en velocidad lenta",
  "parts": [{"intro": "Escucha a Luis comprar frutas. Puedes escuchar **dos veces como máximo**.",
             "audio": "05", "qs": [
    {"t": "mc", "q": "How many apples does Luis want?", "opts": ["seven", "nine", "ten"], "a": 1, "exp": "*Can I have nine apples?*"},
    {"t": "mc", "q": "How much are the apples?", "opts": ["two dollars", "four dollars", "six dollars"], "a": 1, "exp": "*Nine apples are four dollars.*"},
    {"t": "short", "q": "Luis wants ______________ bananas.", "accept": [["10", "ten"]], "show": "**ten** (10)"},
    {"t": "mc", "q": "How much are the bananas?", "opts": ["two dollars", "ten dollars", "four dollars"], "a": 0, "exp": "*Ten bananas are two dollars.*"},
    {"t": "short", "q": "Luis pays ______________ dollars in total.", "accept": [["6", "six"]], "show": "**six** (6)", "exp": "4 + 2 = 6: *Six dollars.*"},
    {"t": "tf", "q": "The seller says: \"Have a nice day!\"", "a": True, "exp": "*Thank you! Have a nice day!*"},
  ]}]},

 "reading": {"skill": "reading", "total": 6,
  "tip": ["Lee el cartel con el dedo. Cada fruta tiene su **precio** al lado."],
  "review": "La lectura *Luis at the Fruit Stand* y la Gramática B",
  "parts": [{"intro": "Lee el cartel del puesto de frutas y responde.",
             "reading": {"title": "Tomás's Fruit Stand", "paras": [
                "**Pineapples:** two dollars",
                "**Mangoes:** one dollar for three mangoes",
                "**Oranges:** one dollar for eight oranges",
                "**Bananas:** one dollar for ten bananas",
                "Open every day. Please pay to Tomás. Thank you!"]},
             "qs": [
    {"t": "mc", "q": "How much is one pineapple?", "opts": ["one dollar", "two dollars", "eight dollars"], "a": 1, "exp": "*Pineapples: two dollars.*"},
    {"t": "short", "q": "One dollar = ______________ mangoes.", "accept": [["3", "three"]], "show": "**three** (3)"},
    {"t": "short", "q": "One dollar = ______________ oranges.", "accept": [["8", "eight"]], "show": "**eight** (8)"},
    {"t": "mc", "q": "What fruit is ten for one dollar?", "opts": ["oranges", "bananas", "mangoes"], "a": 1, "exp": "*Bananas: one dollar for ten bananas.*"},
    {"t": "tf", "q": "The fruit stand is open every day.", "a": True, "exp": "*Open every day.*"},
    {"t": "mc", "q": "Who is the seller?", "opts": ["Luis", "Ana", "Tomás"], "a": 2, "exp": "*Please pay to Tomás.*"},
  ]}]},

 "writing": {"skill": "writing", "total": 8,
  "tip": ["Revisa: **please** al final del pedido, y **dollars** con -s cuando son más de uno."],
  "review": "Gramática A y B, y los Errores comunes",
  "parts": [
   {"intro": "**Parte A. Completa con una palabra.** (1 punto cada una)", "qs": [
    {"t": "short", "q": "Can I have four mangoes, ______________?", "accept": [["please"]], "show": "**please**"},
    {"t": "short", "q": "How ______________ is it?", "accept": [["much"]], "show": "**much**"},
    {"t": "short", "q": "It's nine ______________. (dólares)", "accept": [["dollars"]], "show": "**dollars**", "exp": "más de uno: dollar**s**"},
    {"t": "short", "q": "Here ______________ are.", "accept": [["you"]], "show": "**you**"},
   ]},
   {"intro": "**Parte B. Escribe lo que dices en el puesto de frutas** (3 oraciones). (4 puntos)",
    "note": ["Situación", "Quieres comprar 7 guineos. Pregunta el precio y da las gracias."],
    "open": {"lines": 3, "min_sent": 3, "max_sent": 4, "check_intro": "**Revisa tu respuesta.** Marca un punto por cada casilla que cumpliste:",
             "checklist": [
               {"text": "Pedí **seven bananas** con *Can I have*.", "auto": r"\bcan i have\b.*\bseven bananas\b|\bseven bananas\b"},
               {"text": "Usé **please**.", "auto": r"\bplease\b"},
               {"text": "Pregunté **How much is it?**", "auto": r"\bhow much\b"},
               {"text": "Dije **Thank you**.", "auto": r"\bthank you\b|\bthanks\b"}],
             "sample": "Can I have seven bananas, please? How much is it? Thank you!"}},
  ]},

 "speaking": {"skill": "speaking", "total": 6,
  "tip": ["Habla despacio y claro. En las preguntas, **sube la voz** al final."],
  "review": "Audio 06: escucha, repite y grábate otra vez",
  "parts": [{"intro": "Prepara una grabadora (o usa la de esta página) y luego reproduce el audio. Escucharás 5 preguntas; responde cada una en voz alta **durante la pausa**.",
             "audio": "07",
             "open": {"record": True, "check_intro": "Después, escucha tu grabación y marca un punto por cada casilla:", "checklist": [
               {"text": "Conté del 7 al 10"},
               {"text": "Pedí guineos con *Can I have..., please?*"},
               {"text": "Pregunté *How much is it?*"},
               {"text": "Dije *Thank you*"},
               {"text": "Dije un precio con *dollars*"},
               {"text": "No usé español"}]}}]},

 "mediation": {"skill": "mediation", "total": 6,
  "tip": ["Un cartel de precios es corto: **fruta + precio**. Nada más."],
  "review": "La práctica de Mediation: carteles de precio",
  "parts": [
   {"intro": "**Parte A.** Tu abuelo vende frutas. Escribe su cartel **en inglés**.",
    "note": ["Cartel en español", "Piñas: tres dólares · Mangos: un dólar · Naranjas: dos dólares"],
    "open": {"lines": 3, "min_sent": 0, "max_sent": 0, "checklist": [
      {"text": "Escribí **Pineapples: three dollars**.", "auto": r"\bpineapples?\b.*\bthree dollars\b"},
      {"text": "Escribí **Mangoes: one dollar**.", "auto": r"\bmango(e?s)?\b.*\bone dollar\b"},
      {"text": "Escribí **Oranges: two dollars**.", "auto": r"\boranges?\b.*\btwo dollars\b"},
      {"text": "Puse **dollars** con -s cuando son más de uno."}],
     "sample": "Pineapples: three dollars. Mangoes: one dollar. Oranges: two dollars."}},
   {"intro": "**Parte B.** Un turista pregunta: *How much is the pineapple?* Escribe la respuesta.",
    "note": ["Ayuda", "*It's ... dollars.*"],
    "open": {"lines": 1, "min_sent": 1, "max_sent": 1, "checklist": [
      {"text": "Empecé con **It's**.", "auto": r"\bit'?s\b|\bit is\b"},
      {"text": "Dije **three dollars**.", "auto": r"\bthree dollars\b"}],
     "sample": "It's three dollars."}},
  ]},
}
