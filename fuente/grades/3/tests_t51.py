# -*- coding: utf-8 -*-
"""Mini-tests del Tema 5.1 · 3.er grado (fuente única para el libro y la versión en línea)."""
from common import *

TESTS = {
 "listening": {"skill": "listening", "total": 6,
  "tip": ["Antes de escuchar, **lee las preguntas** con calma.",
          "Escucha bien los **números**: escríbelos al margen mientras escuchas."],
  "review": "Vocabulario (audio 01) y la práctica con el audio 04 en velocidad lenta",
  "parts": [{"intro": "Escucha a Sofía hablar de su canasta de frutas. Puedes escuchar **dos veces como máximo**.",
             "audio": "05", "qs": [
    {"t": "mc", "q": "How many bananas does Sofía have?", "opts": ["two", "three", "five"], "a": 1, "exp": "*I have three yellow bananas.*"},
    {"t": "mc", "q": "What color are the apples?", "opts": ["red", "green", "yellow"], "a": 0, "exp": "*I have five red apples.*"},
    {"t": "short", "q": "Sofía has ______________ apples.", "accept": [["5", "five"]], "show": "**five** (5)"},
    {"t": "mc", "q": "How many oranges does she have?", "opts": ["one", "two", "four"], "a": 1, "exp": "*I have two oranges and one big pineapple.*"},
    {"t": "tf", "q": "Sofía has mangoes.", "a": False, "exp": "*I don't have mangoes.*"},
    {"t": "mc", "q": "How many mangoes does she want?", "opts": ["three", "four", "six"], "a": 1, "exp": "*I want four mangoes!*"},
  ]}]},

 "reading": {"skill": "reading", "total": 6,
  "tip": ["Lee el texto con el dedo, palabra por palabra. **Subraya** los números."],
  "review": "La lectura *Ana's Fruit Basket* y la Gramática A",
  "parts": [{"intro": "Lee lo que dice Luis y responde.",
             "reading": {"title": "Luis Likes Fruit", "paras": [
                "Hello! I'm Luis. I like fruit.",
                "I have six oranges. I have two mangoes. I have one big pineapple.",
                "I don't have apples. I want three apples, please!"]},
             "qs": [
    {"t": "short", "q": "How many oranges does Luis have? ______________", "accept": [["6", "six", "six oranges"]], "show": "**six** (6)"},
    {"t": "mc", "q": "How many mangoes does he have?", "opts": ["one", "two", "three"], "a": 1, "exp": "*I have two mangoes.*"},
    {"t": "mc", "q": "The pineapple is...", "opts": ["big", "small", "red"], "a": 0, "exp": "*I have one big pineapple.*"},
    {"t": "tf", "q": "Luis has apples.", "a": False, "exp": "*I don't have apples.*"},
    {"t": "short", "q": "Luis wants ______________ apples.", "accept": [["3", "three"]], "show": "**three** (3)"},
    {"t": "tf", "q": "Luis likes fruit.", "a": True, "exp": "*I like fruit.*"},
  ]}]},

 "writing": {"skill": "writing", "total": 8,
  "tip": ["Revisa: el **número va primero**, y si hay más de uno, la fruta lleva **-s**."],
  "review": "Gramática A y los Errores comunes",
  "parts": [
   {"intro": "**Parte A. Escribe el número y la fruta en inglés.** (1 punto cada una)", "qs": [
    {"t": "short", "q": "2 manzanas → ______________", "accept": [["two apples", "2 apples"]], "show": "**two apples**", "exp": "más de una: apple**s**"},
    {"t": "short", "q": "1 piña → ______________", "accept": [["one pineapple", "1 pineapple", "a pineapple"]], "show": "**one pineapple**", "exp": "solo una: sin -s"},
    {"t": "short", "q": "4 naranjas → ______________", "accept": [["four oranges", "4 oranges"]], "show": "**four oranges**"},
    {"t": "short", "q": "6 guineos → ______________", "accept": [["six bananas", "6 bananas"]], "show": "**six bananas**"},
   ]},
   {"intro": "**Parte B. Escribe 3 oraciones sobre tu canasta de frutas.** (4 puntos)",
    "note": ["Modelo", "*I have two apples. I have one mango. I want three bananas.*"],
    "open": {"lines": 3, "min_sent": 3, "max_sent": 4, "check_intro": "**Revisa tu respuesta.** Marca un punto por cada casilla que cumpliste:",
             "checklist": [
               {"text": "Usé **I have**.", "auto": r"\bi have\b"},
               {"text": "Usé **I want**.", "auto": r"\bi want\b"},
               {"text": "Usé un número en inglés.", "auto": r"\b(one|two|three|four|five|six|seven|eight|nine|ten)\b"},
               {"text": "Cada oración empieza con mayúscula y termina con punto.", "auto": "caps"}],
             "sample": "I have three oranges. I have one pineapple. I want two mangoes."}},
  ]},

 "speaking": {"skill": "speaking", "total": 6,
  "tip": ["Responde con **oraciones**: no solo *Three*, sino *Three bananas, please.*"],
  "review": "Audio 06: escucha, repite y grábate otra vez",
  "parts": [{"intro": "Prepara una grabadora (o usa la de esta página) y luego reproduce el audio. Escucharás 5 preguntas; responde cada una en voz alta **durante la pausa**.",
             "audio": "07",
             "open": {"record": True, "check_intro": "Después, escucha tu grabación y marca un punto por cada casilla:", "checklist": [
               {"text": "Conté del 1 al 6 sin parar"},
               {"text": "Dije una fruta que me gusta (*I like...*)"},
               {"text": "Dije cuántos guineos quiero (*... bananas, please*)"},
               {"text": "Dije el color de la manzana (*It's red*)"},
               {"text": "Dije la **-s** en las frutas plurales"},
               {"text": "No usé español"}]}}]},

 "mediation": {"skill": "mediation", "total": 6,
  "tip": ["Para hacer una lista en inglés: primero el **número**, después la **fruta**."],
  "review": "La práctica de Mediation: la lista del mercado",
  "parts": [
   {"intro": "**Parte A.** Tu mamá te pidió estas frutas. Escribe la lista **en inglés** para el vendedor.",
    "note": ["Lista de mamá", "dos piñas · cinco guineos · tres naranjas"],
    "open": {"lines": 3, "min_sent": 0, "max_sent": 0, "checklist": [
      {"text": "Escribí **two pineapples**.", "auto": r"\btwo pineapples\b"},
      {"text": "Escribí **five bananas**.", "auto": r"\bfive bananas\b"},
      {"text": "Escribí **three oranges**.", "auto": r"\bthree oranges\b"},
      {"text": "Puse la **-s** en las tres frutas."}],
     "sample": "two pineapples, five bananas, three oranges"}},
   {"intro": "**Parte B.** Pide las frutas con **please**. Escribe 1 oración.",
    "note": ["Ayuda", "*... bananas, please.*"],
    "open": {"lines": 1, "min_sent": 1, "max_sent": 2, "checklist": [
      {"text": "Usé un número y una fruta.", "auto": r"\b(one|two|three|four|five|six)\b \w+"},
      {"text": "Usé **please**.", "auto": r"\bplease\b"}],
     "sample": "Five bananas, please."}},
  ]},
}
