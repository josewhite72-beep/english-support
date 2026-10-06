# -*- coding: utf-8 -*-
"""Mini-tests del Tema 6.1 · 3.er grado (fuente única para el libro y la versión en línea)."""
from common import *

TESTS = {
 "listening": {"skill": "listening", "total": 6,
  "tip": ["Antes de escuchar, **lee las preguntas** con calma.",
          "Escucha bien **can** y **can't**: en *can't* se oye una **t** al final."],
  "review": "Vocabulario (audio 01) y la práctica con el audio 04 en velocidad lenta",
  "parts": [{"intro": "Escucha a Luis en el parque. Puedes escuchar **dos veces como máximo**.",
             "audio": "05", "qs": [
    {"t": "mc", "q": "Luis is in the park with his...", "opts": ["mom", "dad", "sister"], "a": 1, "exp": "*I am in the park with my dad.*"},
    {"t": "mc", "q": "What color is the sky?", "opts": ["blue", "gray", "green"], "a": 0, "exp": "*The sky is blue.*"},
    {"t": "short", "q": "Luis can see ______________ birds.", "accept": [["2", "two"]], "show": "**two** (2)"},
    {"t": "mc", "q": "Where is the yellow flower?", "opts": ["in the tree", "near the trail", "under the tree"], "a": 1, "exp": "*A yellow flower is near the trail.*"},
    {"t": "tf", "q": "Luis can see the river.", "a": False, "exp": "*I **can't** see the river, but I can listen to the water.*"},
    {"t": "tf", "q": "Luis loves nature.", "a": True, "exp": "*I love nature!*"},
  ]}]},

 "reading": {"skill": "reading", "total": 6,
  "tip": ["Lee con el dedo. **Subraya** las palabras *in, on, under, near*."],
  "review": "La lectura *A Day in the Park* y la Gramática B",
  "parts": [{"intro": "Lee lo que escribió Sofía y responde.",
             "reading": {"title": "My Garden", "paras": [
                "I have a small garden at home.",
                "There is a big tree. A bird is in the tree. It can sing.",
                "Three red flowers are under the tree. A green leaf is on a flower.",
                "My cat is near the flowers. I can relax in my garden."]},
             "qs": [
    {"t": "mc", "q": "Sofía's garden is...", "opts": ["big", "small", "blue"], "a": 1, "exp": "*I have a small garden at home.*"},
    {"t": "mc", "q": "Where is the bird?", "opts": ["in the tree", "on the flower", "near the cat"], "a": 0, "exp": "*A bird is in the tree.*"},
    {"t": "short", "q": "How many flowers are there? ______________", "accept": [["3", "three", "three flowers"]], "show": "**three** (3)"},
    {"t": "short", "q": "The flowers are ______________ the tree.", "accept": [["under"]], "show": "**under**"},
    {"t": "tf", "q": "The cat is near the flowers.", "a": True, "exp": "*My cat is near the flowers.*"},
    {"t": "tf", "q": "The bird can't sing.", "a": False, "exp": "*It **can** sing.*"},
  ]}]},

 "writing": {"skill": "writing", "total": 8,
  "tip": ["Revisa: después de **can**, el verbo va solo (*can see*, no *can sees*)."],
  "review": "Gramática A y B, y los Errores comunes",
  "parts": [
   {"intro": "**Parte A. Completa con una palabra.** (1 punto cada una)", "qs": [
    {"t": "short", "q": "The sun is ______________ the sky.", "accept": [["in"]], "show": "**in**"},
    {"t": "short", "q": "The leaf is ______________ the grass. (sobre)", "accept": [["on"]], "show": "**on**"},
    {"t": "short", "q": "I ______________ see a bird. (puedo)", "accept": [["can"]], "show": "**can**"},
    {"t": "short", "q": "I ______________ see the river. (no puedo)", "accept": [["can't", "cant", "cannot", "can not"]], "show": "**can't**"},
   ]},
   {"intro": "**Parte B. Escribe 3 oraciones sobre un parque.** (4 puntos)",
    "note": ["Modelo", "*I can see a tree. The bird is in the tree. I can relax in the park.*"],
    "open": {"lines": 3, "min_sent": 3, "max_sent": 4, "check_intro": "**Revisa tu respuesta.** Marca un punto por cada casilla que cumpliste:",
             "checklist": [
               {"text": "Usé **I can**.", "auto": r"\bi can\b"},
               {"text": "Usé **in, on, under** o **near**.", "auto": r"\b(in|on|under|near) the\b"},
               {"text": "Usé 2 palabras de la naturaleza.", "auto": r"\b(tree|grass|flowers?|birds?|leaf|sun|sky|trail|park)\b.*\b(tree|grass|flowers?|birds?|leaf|sun|sky|trail|park)\b"},
               {"text": "Cada oración empieza con mayúscula y termina con punto.", "auto": "caps"}],
             "sample": "I can see a flower. The flower is on the grass. I can listen to the birds."}},
  ]},

 "speaking": {"skill": "speaking", "total": 6,
  "tip": ["Responde con **oraciones**: no solo *Tree*, sino *I can see a tree.*"],
  "review": "Audio 06: escucha, repite y grábate otra vez",
  "parts": [{"intro": "Prepara una grabadora (o usa la de esta página) y luego reproduce el audio. Escucharás 5 preguntas; responde cada una en voz alta **durante la pausa**.",
             "audio": "07",
             "open": {"record": True, "check_intro": "Después, escucha tu grabación y marca un punto por cada casilla:", "checklist": [
               {"text": "Pregunta 1: *I can see...*"},
               {"text": "Pregunta 2: *The bird is in the tree.*"},
               {"text": "Pregunta 3: *The sky is blue.*"},
               {"text": "Pregunta 4: *Yes, I can. / No, I can't.*"},
               {"text": "Pregunta 5: *I can relax in...*"},
               {"text": "No usé español"}]}}]},

 "mediation": {"skill": "mediation", "total": 6,
  "tip": ["Para explicar una palabra sin hablar, usa **gestos** o un **dibujo** sencillo."],
  "review": "La práctica de Mediation: mímica y explicación en español",
  "parts": [
   {"intro": "**Parte A.** Tu hermanito dice esto en español. Escríbelo **en inglés**.",
    "note": ["Lo que dice tu hermanito", "Puedo ver el sol. El pájaro está en el árbol."],
    "open": {"lines": 2, "min_sent": 2, "max_sent": 2, "checklist": [
      {"text": "Escribí **I can see the sun**.", "auto": r"\bi can see (the|a) sun\b"},
      {"text": "Escribí **The bird is in the tree**.", "auto": r"\bthe bird is in the tree\b"},
      {"text": "Empecé con mayúscula y terminé con punto.", "auto": "caps"},
      {"text": "No olvidé **is** en la segunda oración."}],
     "sample": "I can see the sun. The bird is in the tree."}},
   {"intro": "**Parte B.** Escribe en español qué significa esta oración.",
    "note": ["Oración", "*I can relax in the park.*"],
    "open": {"lines": 1, "min_sent": 0, "max_sent": 0, "checklist": [
      {"text": "Escribí *puedo* (can)."},
      {"text": "Escribí *relajarme en el parque*."}],
     "sample": "Puedo relajarme en el parque."}},
  ]},
}
