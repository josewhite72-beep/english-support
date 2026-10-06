# -*- coding: utf-8 -*-
"""Mini-tests del Tema 6.2 · 3.er grado (fuente única para el libro y la versión en línea)."""
from common import *

TESTS = {
 "listening": {"skill": "listening", "total": 6,
  "tip": ["Antes de escuchar, **lee las preguntas** con calma.",
          "Escucha los **animales** y lo que **pueden** hacer: *fly, swim*."],
  "review": "Vocabulario (audio 01) y la práctica con el audio 04 en velocidad lenta",
  "parts": [{"intro": "Escucha a Tomás hablar de su día afuera. Puedes escuchar **dos veces como máximo**.",
             "audio": "05", "qs": [
    {"t": "mc", "q": "Where is Tomás?", "opts": ["at school", "at the river", "at home"], "a": 1, "exp": "*We are at the river.*"},
    {"t": "short", "q": "Tomás can see ______________ fish.", "accept": [["3", "three"]], "show": "**three** (3)"},
    {"t": "mc", "q": "What can the fish do?", "opts": ["fly", "walk", "swim"], "a": 2, "exp": "*They can swim.*"},
    {"t": "mc", "q": "What color is the butterfly?", "opts": ["yellow", "red", "blue"], "a": 0, "exp": "*It is yellow.*"},
    {"t": "tf", "q": "Tomás can swim in the river.", "a": False, "exp": "*I **can't** swim in the river.*"},
    {"t": "tf", "q": "Tomás is happy.", "a": True, "exp": "*But I'm happy!*"},
  ]}]},

 "reading": {"skill": "reading", "total": 6,
  "tip": ["Lee con el dedo. **Subraya** las palabras *I'm* y *can*."],
  "review": "La lectura *My Happy Day Outside* y la Gramática A y C",
  "parts": [{"intro": "Lee lo que escribió Luis y responde.",
             "reading": {"title": "At the Beach", "paras": [
                "Hi! I'm Luis. Today I'm outside. I'm at the beach with my family.",
                "It's a sunny day. The sky is blue.",
                "I can see two fish in the water. They can swim. A bird is on a rock. It can fly.",
                "We walk on the sand, and we play with a ball. I'm very happy!"]},
             "qs": [
    {"t": "mc", "q": "Where is Luis?", "opts": ["at the park", "at the beach", "at the river"], "a": 1, "exp": "*I'm at the beach with my family.*"},
    {"t": "short", "q": "How many fish can Luis see? ______________", "accept": [["2", "two", "two fish"]], "show": "**two** (2)"},
    {"t": "short", "q": "The bird is on a ______________.", "accept": [["rock"]], "show": "**rock**"},
    {"t": "mc", "q": "What do they play with?", "opts": ["a ball", "a kite", "a dog"], "a": 0, "exp": "*We play with a ball.*"},
    {"t": "tf", "q": "It's a rainy day.", "a": False, "exp": "*It's a **sunny** day.*"},
    {"t": "tf", "q": "Luis is happy.", "a": True, "exp": "*I'm very happy!*"},
  ]}]},

 "writing": {"skill": "writing", "total": 8,
  "tip": ["Revisa: **I'm** lleva el apóstrofo (*I'm*, no *Im*), y después de **can** el verbo va solo."],
  "review": "Gramática A, B y C, y los Errores comunes",
  "parts": [
   {"intro": "**Parte A. Completa con una palabra.** (1 punto cada una)", "qs": [
    {"t": "short", "q": "______________ outside. (Estoy)", "accept": [["I'm", "Im", "I am"]], "show": "**I'm**"},
    {"t": "short", "q": "The bird can ______________. (volar)", "accept": [["fly"]], "show": "**fly**"},
    {"t": "short", "q": "The fish can ______________. (nadar)", "accept": [["swim"]], "show": "**swim**"},
    {"t": "short", "q": "We ______________ on the trail. (caminamos)", "accept": [["walk"]], "show": "**walk**"},
   ]},
   {"intro": "**Parte B. Escribe 3 oraciones sobre tu día afuera.** (4 puntos)",
    "note": ["Modelo", "*I'm outside. I'm happy. The bird can fly.*"],
    "open": {"lines": 3, "min_sent": 3, "max_sent": 4, "check_intro": "**Revisa tu respuesta.** Marca un punto por cada casilla que cumpliste:",
             "checklist": [
               {"text": "Usé **I'm**.", "auto": r"\bi'?m\b|\bi am\b"},
               {"text": "Usé **happy** u **outside**.", "auto": r"\b(happy|outside)\b"},
               {"text": "Usé **can** con un animal.", "auto": r"\b(bird|fish|butterfly|dog|cat|it)\b can\b"},
               {"text": "Cada oración empieza con mayúscula y termina con punto.", "auto": "caps"}],
             "sample": "I'm in the park. I'm happy. The butterfly can fly."}},
  ]},

 "speaking": {"skill": "speaking", "total": 6,
  "tip": ["Di **I'm** completo, no solo *I*: *I'm outside.*"],
  "review": "Audio 06: escucha, repite y grábate otra vez",
  "parts": [{"intro": "Prepara una grabadora (o usa la de esta página) y luego reproduce el audio. Escucharás 5 preguntas; responde cada una en voz alta **durante la pausa**.",
             "audio": "07",
             "open": {"record": True, "check_intro": "Después, escucha tu grabación y marca un punto por cada casilla:", "checklist": [
               {"text": "Pregunta 1: *Yes, I'm outside. / I'm at home.*"},
               {"text": "Pregunta 2: *I'm happy.*"},
               {"text": "Pregunta 3: *Yes, it can.*"},
               {"text": "Pregunta 4: *No, it can't.*"},
               {"text": "Pregunta 5: *We walk... / We play...*"},
               {"text": "No usé español"}]}}]},

 "mediation": {"skill": "mediation", "total": 6,
  "tip": ["Primero piensa la oración en español; luego busca **las palabras del tema** en inglés."],
  "review": "La práctica de Mediation: caras y explicación en español",
  "parts": [
   {"intro": "**Parte A.** Tu primita dice esto en español. Escríbelo **en inglés**.",
    "note": ["Lo que dice tu primita", "Estoy afuera. Estoy feliz. El pez puede nadar."],
    "open": {"lines": 2, "min_sent": 3, "max_sent": 3, "checklist": [
      {"text": "Escribí **I'm outside**.", "auto": r"\b(i'?m|i am) outside\b"},
      {"text": "Escribí **I'm happy**.", "auto": r"\b(i'?m|i am) happy\b"},
      {"text": "Escribí **The fish can swim**.", "auto": r"\bthe fish can swim\b"},
      {"text": "Empecé con mayúscula y terminé con punto.", "auto": "caps"}],
     "sample": "I'm outside. I'm happy. The fish can swim."}},
   {"intro": "**Parte B.** Escribe en español qué significa esta oración.",
    "note": ["Oración", "*We play on the grass.*"],
    "open": {"lines": 1, "min_sent": 0, "max_sent": 0, "checklist": [
      {"text": "Escribí *jugamos* (we play)."},
      {"text": "Escribí *en la grama* o *en la hierba*."}],
     "sample": "Jugamos en la grama."}},
  ]},
}
