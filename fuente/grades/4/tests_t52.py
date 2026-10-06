# -*- coding: utf-8 -*-
"""Mini-tests del Tema 5.2 · 4.º (fuente única para el libro y la versión en línea)."""
from common import *

TESTS = {
 "listening": {"skill": "listening", "total": 6,
  "tip": ["Antes de escuchar, **lee todas las preguntas**. Así sabes qué información buscar.",
          "Pon atención a **always, usually, sometimes, never**: muchas preguntas dependen de esas palabras."],
  "review": "Vocabulario (audio 01) y la práctica con el audio 04 en velocidad lenta",
  "parts": [{"intro": "Escucha a Sofía hablar de su almuerzo. Puedes escuchar **dos veces como máximo**.",
             "audio": "05", "qs": [
    {"t": "short", "q": "Sofía always eats lunch at school at ______________ o'clock.", "accept": [["12", "twelve"]], "show": "**twelve** (12)"},
    {"t": "mc", "q": "What does she usually pack?", "opts": ["chicken", "rice and beans", "a sandwich"], "a": 1,
     "exp": "*I usually pack rice and beans, and I sometimes pack chicken.*"},
    {"t": "mc", "q": "What does she never pack?", "opts": ["fruit", "candy", "water"], "a": 1, "exp": "*I never pack candy, because it is bad for my teeth.*"},
    {"t": "tf", "q": "Sofía always packs fruit.", "a": True, "exp": "*I always pack fruit.*"},
    {"t": "short", "q": "Her favorite fruit is ______________.", "accept": [["pineapple", "pineapples"]], "show": "**pineapple**"},
    {"t": "mc", "q": "What does Carlos sometimes do?", "opts": ["He buys lunch at the school store.", "He packs candy.", "He never eats lunch."], "a": 0,
     "exp": "*My brother Carlos sometimes buys lunch at the school store.*"},
  ]}]},

 "reading": {"skill": "reading", "total": 6,
  "tip": ["Lee primero las preguntas y luego el texto. **Subraya** las palabras **always, usually, sometimes, never**."],
  "review": "La lectura *Carlos and His Lunchbox* y la Gramática A",
  "parts": [{"intro": "Lee lo que escribió Ana sobre su familia y responde.",
             "reading": {"title": "Lunch in My Family", "paras": [
                "Hi! I'm Ana. In my family, we always eat lunch together on Sundays.",
                "My mom always cooks rice and chicken. My dad usually makes a salad.",
                "My little brother never eats vegetables. He sometimes eats a banana.",
                "I usually drink water, but on Sundays I sometimes drink lemonade. Yum!"]},
             "qs": [
    {"t": "mc", "q": "When does Ana's family always eat lunch together?", "opts": ["on Saturdays", "on Sundays", "every day"], "a": 1,
     "exp": "*...we always eat lunch together on Sundays.*"},
    {"t": "mc", "q": "Who always cooks rice and chicken?", "opts": ["Ana's mom", "Ana's dad", "Ana"], "a": 0, "exp": "*My mom always cooks rice and chicken.*"},
    {"t": "short", "q": "Ana's dad usually makes a ______________.", "accept": [["salad"]], "show": "**salad**"},
    {"t": "tf", "q": "Ana's brother always eats vegetables.", "a": False, "exp": "*My little brother **never** eats vegetables.*"},
    {"t": "mc", "q": "What does Ana usually drink?", "opts": ["juice", "lemonade", "water"], "a": 2, "exp": "*I usually drink water...*"},
    {"t": "tf", "q": "On Sundays, Ana sometimes drinks lemonade.", "a": True, "exp": "*...on Sundays I sometimes drink lemonade.*"},
  ]}]},

 "writing": {"skill": "writing", "total": 10,
  "tip": ["Revisa: la palabra de frecuencia va **antes del verbo**, y con he / she el verbo lleva **-s**."],
  "review": "Gramática A y los Errores comunes",
  "parts": [
   {"intro": "**Parte A. Cada oración tiene un error. Escríbela correctamente.** (1 punto cada una)", "qs": [
    {"t": "fix", "q": "I pack always fruit.", "accept": ["i always pack fruit"], "show": "I **always pack** fruit.", "exp": "always va antes del verbo"},
    {"t": "fix", "q": "She never drink juice.", "accept": ["she never drinks juice"], "show": "She never **drinks** juice.", "exp": "con she: drinks"},
    {"t": "fix", "q": "He usually eat rice.", "accept": ["he usually eats rice"], "show": "He usually **eats** rice.", "exp": "con he: eats"},
    {"t": "fix", "q": "I don't never eat candy.", "accept": ["i never eat candy", "i dont ever eat candy"], "show": "I **never** eat candy.", "exp": "never ya es negativo"},
    {"t": "fix", "q": "We eat sometimes chicken.", "accept": ["we sometimes eat chicken"], "show": "We **sometimes eat** chicken.", "exp": "sometimes antes del verbo"},
   ]},
   {"intro": "**Parte B. Escríbele a Sofía sobre tu almuerzo** con 3 a 5 oraciones. (5 puntos)",
    "note": ["Mensaje de Sofía", "*Hi! What do you usually eat for lunch? What do you always drink?*"],
    "open": {"lines": 4, "min_sent": 3, "max_sent": 5, "check_intro": "**Revisa tu respuesta.** Marca un punto por cada casilla que cumpliste:",
             "checklist": [
               {"text": "Empecé con un saludo (*Hi, Sofía!*).", "auto": r"^\s*(hi|hello|hey|dear)\b"},
               {"text": "Usé **usually**.", "auto": r"\busually\b"},
               {"text": "Usé **always**.", "auto": r"\balways\b"},
               {"text": "Usé **sometimes** o **never**.", "auto": r"\b(sometimes|never)\b"},
               {"text": "Cada oración empieza con mayúscula y termina con punto.", "auto": "caps"}],
             "sample": "Hi, Sofía! I usually eat rice and chicken. I always drink water. I never drink juice."}},
  ]},

 "speaking": {"skill": "speaking", "total": 8,
  "tip": ["Responde siempre con **oración completa**: no solo *Rice*, sino *I usually eat rice.*"],
  "review": "Audio 06: escucha, repite y grábate otra vez",
  "parts": [{"intro": "Prepara una grabadora (o usa la de esta página) y luego reproduce el audio. Escucharás 5 preguntas; responde cada una en voz alta **durante la pausa**.",
             "audio": "07",
             "open": {"record": True, "check_intro": "Después, escucha tu grabación y marca un punto por cada casilla:", "checklist": [
               {"text": "Pregunta 1: *I usually eat...*"},
               {"text": "Pregunta 2: *I always drink...*"},
               {"text": "Pregunta 3: *I never eat...*"},
               {"text": "Pregunta 4: *Yes, I do. / No, I don't.*"},
               {"text": "Pregunta 5: *My friend sometimes eats...* (con -s)"},
               {"text": "Pronuncié *usually* y *sometimes*"},
               {"text": "Hablé sin leer"}, {"text": "No usé español"}]}}]},

 "mediation": {"skill": "mediation", "total": 8,
  "tip": ["Para pasar un mensaje: busca **quién**, **qué come** y **con qué frecuencia**. Usa oraciones cortas."],
  "review": "La práctica de Mediation y la Gramática A",
  "parts": [
   {"intro": "**Parte A.** Escríbele a Sofía (solo habla inglés) lo que dijo tu hermano, en **2 o 3 oraciones**.",
    "note": ["Lo que dijo tu hermano", "Siempre como arroz. A veces como pollo. Nunca tomo jugo."],
    "open": {"lines": 3, "min_sent": 2, "max_sent": 3, "checklist": [
      {"text": "Usé **He** con verbo + s (*He always eats*).", "auto": r"\bhe (always |usually |sometimes |never )?\w+s\b"},
      {"text": "Dije que siempre come arroz.", "auto": r"\balways\b.*\brice\b"},
      {"text": "Dije que a veces come pollo.", "auto": r"\bsometimes\b.*\bchicken\b"},
      {"text": "Dije que nunca toma jugo.", "auto": r"\bnever\b.*\bjuice\b"},
      {"text": "Usé oraciones cortas y claras."}],
     "sample": "My brother always eats rice. He sometimes eats chicken. He never drinks juice."}},
   {"intro": "**Parte B.** Simplifica este aviso en **1 o 2 oraciones**.",
    "note": ["Aviso", "*Students are kindly reminded that they should always bring a bottle of water and should never share their food with classmates who have allergies.*"],
    "open": {"lines": 2, "min_sent": 1, "max_sent": 2, "checklist": [
      {"text": "Dije que **siempre** traigan agua.", "auto": r"\balways\b.*\bwater\b|\bwater\b"},
      {"text": "Usé **never**.", "auto": r"\bnever\b"},
      {"text": "Mencioné compartir comida (*share food*).", "auto": r"\bshare\b"}],
     "sample": "Always bring water. Never share your food."}},
  ]},
}
