# -*- coding: utf-8 -*-
"""Mini-tests del Tema 5.2 · 5.º (fuente única para el libro y la versión en línea)."""
from common import *

TESTS = {
 "listening": {"skill": "listening", "total": 6,
  "tip": ["Antes de escuchar, **lee todas las preguntas**. Así sabes qué información buscar.",
          "Escucha con atención **can** y **can't**: suenan parecido, pero en *can't* se oye una *t* al final."],
  "review": "Vocabulario (audio 01) y la práctica con el audio 04 en velocidad lenta",
  "parts": [{"intro": "Escucha a Miss Rosa, la profesora de Educación Física, organizar los equipos. Puedes escuchar **dos veces como máximo**.",
             "audio": "05", "qs": [
    {"t": "mc", "q": "Which team can swim very well?", "opts": ["the red team", "the blue team", "the green team"], "a": 0,
     "exp": "*The red team can swim very well.*"},
    {"t": "mc", "q": "What can the blue team do?", "opts": ["jump high", "run fast", "play volleyball"], "a": 1, "exp": "*The blue team can run fast.*"},
    {"t": "short", "q": "The running race is at ______________ o'clock.", "accept": [["9", "nine"]], "show": "**nine** (9)"},
    {"t": "tf", "q": "The green team can run very fast.", "a": False,
     "exp": "*The green team **can't** run very fast, but they can jump high.*"},
    {"t": "mc", "q": "When is the volleyball game?", "opts": ["at nine o'clock", "at ten o'clock", "at eleven o'clock"], "a": 2,
     "exp": "*Their game is at eleven o'clock.*"},
    {"t": "mc", "q": "What should students bring?", "opts": ["water and a cap", "a ball", "a bike"], "a": 0, "exp": "*Bring water and a cap!*"},
  ]}]},

 "reading": {"skill": "reading", "total": 6,
  "tip": ["Lee primero las preguntas y luego el texto. **Subraya** en el texto la parte donde está cada respuesta.",
          "Para responder **Can...?**, busca en el texto si dice *can* o *can't* junto a esa persona."],
  "review": "La lectura *Sports Day at School* y la Gramática A",
  "parts": [{"intro": "Lee lo que escribió Marcos sobre su familia y responde.",
             "reading": {"title": "My Sporty Family", "paras": [
                "Hello! I'm Marcos. My family loves sports!",
                "My mom can swim very well. She swims at the beach on Sundays. My dad can ride a bike, and he can run fast. He runs in the morning.",
                "My little sister Ana can dance, but she can't swim yet. She is only five years old.",
                "I can jump high and I can climb trees. I can't play volleyball very well, but I like it. Can you play volleyball?"]},
             "qs": [
    {"t": "mc", "q": "Who can swim very well?", "opts": ["Marcos's mom", "Marcos's dad", "Ana"], "a": 0, "exp": "*My mom can swim very well.*"},
    {"t": "short", "q": "Marcos's mom swims at the beach on ______________.", "accept": [["sundays", "sunday"]], "show": "**Sundays**"},
    {"t": "tf", "q": "Marcos's dad can run fast.", "a": True, "exp": "*...and he can run fast.*"},
    {"t": "tf", "q": "Ana can swim.", "a": False, "exp": "*...but she **can't** swim yet. She is only five years old.*"},
    {"t": "mc", "q": "What can Marcos do?", "opts": ["swim and dance", "jump high and climb trees", "play volleyball very well"], "a": 1,
     "exp": "*I can jump high and I can climb trees.*"},
    {"t": "mc", "q": "Marcos can't play volleyball very well, but...", "opts": ["he likes it", "he doesn't like it", "his sister can"], "a": 0,
     "exp": "*...but I like it.* Recuerda: *can* = habilidad; *like* = gusto."},
  ]}]},

 "writing": {"skill": "writing", "total": 10,
  "tip": ["Revisa: **can** nunca lleva -s, y el verbo después de *can* va **solo** (sin -s, sin -ing, sin *to*)."],
  "review": "Gramática A y C, y los Errores comunes",
  "parts": [
   {"intro": "**Parte A. Cada oración tiene un error. Escríbela correctamente.** (1 punto cada una)", "qs": [
    {"t": "fix", "q": "She cans swim very well.", "accept": ["she can swim very well"], "show": "She **can** swim very well.", "exp": "can nunca lleva -s"},
    {"t": "fix", "q": "I can swimming.", "accept": ["i can swim"], "show": "I can **swim**.", "exp": "después de can, verbo sin -ing"},
    {"t": "fix", "q": "He can to run fast.", "accept": ["he can run fast"], "show": "He can **run** fast.", "exp": "después de can, sin to"},
    {"t": "fix", "q": "Can you climb? — Yes, I do.", "accept": ["can you climb yes i can"], "show": "Can you climb? — Yes, I **can**.", "exp": "respuesta corta con can"},
    {"t": "fix", "q": "You can dance? ", "accept": ["can you dance"], "show": "**Can you** dance?", "exp": "en la pregunta, can va primero"},
   ]},
   {"intro": "**Parte B. Responde el mensaje de Pedro** con 3 a 5 oraciones. (5 puntos)",
    "note": ["Mensaje de Pedro", "*Hi! We need players for our team. What can you do? Can you swim? What can't you do?*"],
    "open": {"lines": 5, "min_sent": 3, "max_sent": 5, "check_intro": "**Revisa tu respuesta.** Marca un punto por cada casilla que cumpliste:",
             "checklist": [
               {"text": "Empecé con un saludo (*Hi, Pedro!*).", "auto": r"^\s*(hi|hello|hey|dear)\b"},
               {"text": "Dije algo que **puedo** hacer (*I can...*).", "auto": r"\bi can \w+"},
               {"text": "Respondí si sé nadar (*Yes, I can / No, I can't*).", "auto": r"\bswim\b|\byes,? i can\b|\bno,? i can'?t\b"},
               {"text": "Dije algo que **no puedo** hacer (*I can't...*).", "auto": r"\bcan'?t\b|\bcannot\b"},
               {"text": "Cada oración empieza con mayúscula y termina con punto.", "auto": "caps"}],
             "sample": "Hi, Pedro! I can run fast and I can jump high. Yes, I can swim. I can't play volleyball very well."}},
  ]},

 "speaking": {"skill": "speaking", "total": 8,
  "tip": ["Responde siempre con **oración completa**: no solo *Yes*, sino *Yes, I can. I can swim very well.*",
          "Si la pregunta empieza con **Can you...?**, empieza con *Yes, I can* o *No, I can't*."],
  "review": "Audio 06: escucha, repite y grábate otra vez",
  "parts": [{"intro": "Prepara una grabadora (o usa la de esta página) y luego reproduce el audio. Escucharás 5 preguntas; responde cada una en voz alta **durante la pausa**.",
             "audio": "07",
             "open": {"record": True, "check_intro": "Después, escucha tu grabación y marca un punto por cada casilla:", "checklist": [
               {"text": "Pregunta 1: *Yes, I can. / No, I can't.*"},
               {"text": "Pregunta 2: *I can play...*"},
               {"text": "Pregunta 3: *I can't...*"},
               {"text": "Pregunta 4: *He / She can...* (sin -s en can)"},
               {"text": "Pregunta 5: respuesta corta con can"},
               {"text": "Se nota la diferencia entre *can* y *can't*"},
               {"text": "Hablé sin leer"}, {"text": "No usé español"}]}}]},

 "mediation": {"skill": "mediation", "total": 8,
  "tip": ["Para pasar un mensaje a otro idioma: busca **quién**, **qué puede** y **qué no puede** hacer. Usa *can* y *can't*."],
  "review": "La práctica de Mediation y la Gramática A",
  "parts": [
   {"intro": "**Parte A.** Escríbele a Pedro (solo habla inglés) lo que dijo tu primo, en **2 o 3 oraciones**.",
    "note": ["Lo que dijo tu primo", "Sé jugar voleibol muy bien y sé nadar. No sé trepar árboles."],
    "open": {"lines": 3, "min_sent": 2, "max_sent": 3, "checklist": [
      {"text": "Usé **He can** (es mi primo).", "auto": r"\bhe can\b"},
      {"text": "Dije que juega voleibol muy bien.", "auto": r"\bvolleyball\b"},
      {"text": "Dije que sabe nadar.", "auto": r"\bswim\b"},
      {"text": "Dije que **no** sabe trepar (*can't climb*).", "auto": r"\bcan'?t climb\b|\bcannot climb\b"},
      {"text": "Usé oraciones cortas y claras."}],
     "sample": "My cousin can play volleyball very well. He can swim. He can't climb trees."}},
   {"intro": "**Parte B.** Simplifica este aviso en **1 o 2 oraciones**.",
    "note": ["Aviso", "*Children who cannot swim yet must stay in the small pool and always swim with an adult.*"],
    "open": {"lines": 2, "min_sent": 1, "max_sent": 2, "checklist": [
      {"text": "Dije **quién** (*children who can't swim*).", "auto": r"\bcan'?t swim\b|\bcannot swim\b"},
      {"text": "Dije **dónde** (*small pool*).", "auto": r"\bsmall pool\b"},
      {"text": "Dije **con quién** (*with an adult*).", "auto": r"\badult\b"}],
     "sample": "Can't swim? Stay in the small pool. Swim with an adult."}},
  ]},
}
