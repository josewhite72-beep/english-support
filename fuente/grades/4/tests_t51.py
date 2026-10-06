# -*- coding: utf-8 -*-
"""Mini-tests del Tema 5.1 · 4.º (fuente única para el libro y la versión en línea)."""
from common import *

TESTS = {
 "listening": {"skill": "listening", "total": 6,
  "tip": ["Antes de escuchar, **lee todas las preguntas**. Así sabes qué información buscar.",
          "Fíjate en **quién** va a empacar cada cosa: el papá habla de toda la familia."],
  "review": "Vocabulario (audio 01) y la práctica con el audio 04 en velocidad lenta",
  "parts": [{"intro": "Escucha al papá explicar el plan del paseo. Puedes escuchar **dos veces como máximo**.",
             "audio": "05", "qs": [
    {"t": "mc", "q": "When are they going to go to the beach?", "opts": ["on Friday", "on Saturday", "on Sunday"], "a": 1,
     "exp": "*On Saturday, we are going to go to Coronado beach.*"},
    {"t": "short", "q": "They are going to leave at ______________ o'clock.", "accept": [["7", "seven"]], "show": "**seven** (7)"},
    {"t": "mc", "q": "What is Sofía going to pack?", "opts": ["her hat and her bucket", "her swimsuit and her towel", "the sandwiches"], "a": 1,
     "exp": "*Sofía, pack your swimsuit and your towel.*"},
    {"t": "mc", "q": "What is Carlos going to pack?", "opts": ["his hat and his bucket", "the umbrella", "the water"], "a": 0,
     "exp": "*Carlos, pack your hat and your bucket.*"},
    {"t": "tf", "q": "Mom is going to pack the umbrella.", "a": False,
     "exp": "Mamá va a empacar los sándwiches y el agua. **Papá** empaca la sombrilla: *I'm going to pack the big umbrella.*"},
    {"t": "tf", "q": "Dad says: \"Don't forget the sunscreen!\"", "a": True, "exp": "Así termina el mensaje."},
  ]}]},

 "reading": {"skill": "reading", "total": 6,
  "tip": ["Lee primero las preguntas y luego el texto. **Subraya** en el texto la parte donde está cada respuesta.",
          "En una lista de cosas, fíjate en el **nombre** de la persona que está antes."],
  "review": "La lectura *The Family Trip* y la Gramática A y B",
  "parts": [{"intro": "Lee la nota que dejó la maestra antes del paseo y responde.",
             "reading": {"title": "Our Class Trip", "paras": [
                "Hello, families! On Friday, Grade 4 is going to go to the river. We are going to have a picnic.",
                "Please pack: a swimsuit, a towel, a hat, and a bottle of water. Pack your lunch in a lunchbox.",
                "Don't bring toys or money. Don't forget sunscreen!",
                "The bus is going to leave at eight o'clock. We are going to come back at two o'clock."]},
             "qs": [
    {"t": "mc", "q": "Where is Grade 4 going to go?", "opts": ["to the beach", "to the river", "to the park"], "a": 1, "exp": "*Grade 4 is going to go to the river.*"},
    {"t": "short", "q": "They are going to have a ______________.", "accept": [["picnic"]], "show": "**picnic**"},
    {"t": "tf", "q": "Students can bring toys.", "a": False, "exp": "*Don't bring toys or money.*"},
    {"t": "mc", "q": "Where do students pack their lunch?", "opts": ["in a suitcase", "in a bucket", "in a lunchbox"], "a": 2, "exp": "*Pack your lunch in a lunchbox.*"},
    {"t": "short", "q": "The bus is going to leave at ______________ o'clock.", "accept": [["8", "eight"]], "show": "**eight** (8)"},
    {"t": "tf", "q": "They are going to come back at two o'clock.", "a": True, "exp": "*We are going to come back at two o'clock.*"},
  ]}]},

 "writing": {"skill": "writing", "total": 10,
  "tip": ["Revisa: las instrucciones empiezan con el **verbo**; *going to* siempre lleva **am, is o are** antes."],
  "review": "Gramática A y B, y los Errores comunes",
  "parts": [
   {"intro": "**Parte A. Cada oración tiene un error. Escríbela correctamente.** (1 punto cada una)", "qs": [
    {"t": "fix", "q": "I going to pack my hat.", "accept": ["im going to pack my hat", "i am going to pack my hat"], "show": "I**'m** going to pack my hat.", "exp": "falta am"},
    {"t": "fix", "q": "No forget the sunscreen!", "accept": ["dont forget the sunscreen"], "show": "**Don't** forget the sunscreen!", "exp": "para decir no: don't"},
    {"t": "fix", "q": "She are going to pack a towel.", "accept": ["shes going to pack a towel", "she is going to pack a towel"], "show": "She **is** going to pack a towel.", "exp": "con she: is"},
    {"t": "fix", "q": "We is going to go to the beach.", "accept": ["were going to go to the beach", "we are going to go to the beach"], "show": "We **are** going to go to the beach.", "exp": "con we: are"},
    {"t": "fix", "q": "Packs your swimsuit.", "accept": ["pack your swimsuit"], "show": "**Pack** your swimsuit.", "exp": "la instrucción usa el verbo sin -s"},
   ]},
   {"intro": "**Parte B. Escríbele a Carlos qué vas a empacar** para la playa, con 3 a 5 oraciones. (5 puntos)",
    "note": ["Mensaje de Carlos", "*Hi! We're going to the beach on Saturday. What are you going to pack?*"],
    "open": {"lines": 4, "min_sent": 3, "max_sent": 5, "check_intro": "**Revisa tu respuesta.** Marca un punto por cada casilla que cumpliste:",
             "checklist": [
               {"text": "Empecé con un saludo (*Hi, Carlos!*).", "auto": r"^\s*(hi|hello|hey|dear)\b"},
               {"text": "Usé **I'm going to pack**.", "auto": r"\b(i'?m|i am) going to\b"},
               {"text": "Nombré al menos 2 cosas de la playa.", "auto": r"\b(towel|hat|sunscreen|swimsuit|sandals|umbrella|bucket)\b.*\b(towel|hat|sunscreen|swimsuit|sandals|umbrella|bucket)\b"},
               {"text": "Escribí una instrucción (*Don't forget... / Pack...*).", "auto": r"\bdon'?t forget\b|\bpack your\b|\bbring\b"},
               {"text": "Cada oración empieza con mayúscula y termina con punto.", "auto": "caps"}],
             "sample": "Hi, Carlos! I'm going to pack my swimsuit and my towel. I'm going to pack my hat, too. Don't forget the sunscreen!"}},
  ]},

 "speaking": {"skill": "speaking", "total": 8,
  "tip": ["Responde siempre con **oración completa**: no solo *My hat*, sino *I'm going to pack my hat.*"],
  "review": "Audio 06: escucha, repite y grábate otra vez",
  "parts": [{"intro": "Prepara una grabadora (o usa la de esta página) y luego reproduce el audio. Escucharás 5 preguntas; responde cada una en voz alta **durante la pausa**.",
             "audio": "07",
             "open": {"record": True, "check_intro": "Después, escucha tu grabación y marca un punto por cada casilla:", "checklist": [
               {"text": "Pregunta 1: *I'm going to go to...*"},
               {"text": "Pregunta 2: *I'm going to pack...*"},
               {"text": "Pregunta 3: una instrucción con *Pack...*"},
               {"text": "Pregunta 4: oración completa"},
               {"text": "Pregunta 5: *My ... is going to go with me.*"},
               {"text": "Usé al menos 3 palabras del vocabulario"},
               {"text": "Hablé sin leer"}, {"text": "No usé español"}]}}]},

 "mediation": {"skill": "mediation", "total": 8,
  "tip": ["Para pasar un mensaje: quédate con **qué hacer** y **qué no hacer**. Usa instrucciones cortas."],
  "review": "La práctica de Mediation y la Gramática A",
  "parts": [
   {"intro": "**Parte A.** Escríbele a Carlos (solo habla inglés) lo que dijo tu mamá, en **2 o 3 oraciones**.",
    "note": ["Lo que dijo tu mamá", "Empaca tu toalla y tu sombrero. No olvides el bloqueador."],
    "open": {"lines": 3, "min_sent": 2, "max_sent": 3, "checklist": [
      {"text": "Empecé con el verbo **Pack**.", "auto": r"\bpack\b"},
      {"text": "Mencioné la toalla (*towel*).", "auto": r"\btowel\b"},
      {"text": "Mencioné el sombrero (*hat*).", "auto": r"\bhat\b"},
      {"text": "Dije **Don't forget the sunscreen**.", "auto": r"\bdon'?t forget\b.*\bsunscreen\b"},
      {"text": "Usé oraciones cortas y claras."}],
     "sample": "Pack your towel and your hat. Don't forget the sunscreen."}},
   {"intro": "**Parte B.** Simplifica este aviso en **1 o 2 oraciones**.",
    "note": ["Aviso", "*Visitors are kindly reminded to use sunscreen and to take all their trash with them when they leave the beach.*"],
    "open": {"lines": 2, "min_sent": 1, "max_sent": 2, "checklist": [
      {"text": "Dije que usen bloqueador (*Use sunscreen*).", "auto": r"\bsunscreen\b"},
      {"text": "Dije que se lleven la basura (*trash*).", "auto": r"\btrash\b"},
      {"text": "Usé instrucciones (empiezan con verbo).", "auto": r"^\s*(use|take|put|bring|pack|don'?t)\b"}],
     "sample": "Use sunscreen. Take your trash with you."}},
  ]},
}
