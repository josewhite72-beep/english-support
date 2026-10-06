# -*- coding: utf-8 -*-
"""Mini-tests del Tema 6.1 · 4.º (fuente única para el libro y la versión en línea)."""
from common import *

TESTS = {
 "listening": {"skill": "listening", "total": 6,
  "tip": ["Antes de escuchar, **lee todas las preguntas**. Así sabes qué información buscar.",
          "Cada persona está haciendo algo distinto. Anota al margen: **Ana → ...**, **Dad → ...**, **Mom → ...**"],
  "review": "Vocabulario (audio 01) y la práctica con el audio 04 en velocidad lenta",
  "parts": [{"intro": "Escucha a Carlos contar qué pasa en su casa en un día de lluvia. Puedes escuchar **dos veces como máximo**.",
             "audio": "05", "qs": [
    {"t": "mc", "q": "What color is the sky?", "opts": ["blue", "gray", "black"], "a": 1, "exp": "*The sky is gray, and it's raining a lot.*"},
    {"t": "mc", "q": "What is Ana wearing?", "opts": ["a yellow raincoat and red boots", "a red raincoat and yellow boots", "sandals"], "a": 0,
     "exp": "*...her yellow raincoat and her red boots.*"},
    {"t": "short", "q": "Ana is jumping in a big ______________.", "accept": [["puddle"]], "show": "**puddle**"},
    {"t": "mc", "q": "What is Dad doing?", "opts": ["He's cooking.", "He's reading a book.", "He's sleeping."], "a": 1,
     "exp": "*My dad is reading a book in the living room.*"},
    {"t": "tf", "q": "Mom is cooking soup.", "a": True, "exp": "*My mom is cooking soup in the kitchen.*"},
    {"t": "mc", "q": "Where is the dog?", "opts": ["in the puddle", "in the kitchen", "under the bed"], "a": 2,
     "exp": "*He's sleeping under the bed, because he doesn't like thunder!*"},
  ]}]},

 "reading": {"skill": "reading", "total": 6,
  "tip": ["Lee primero las preguntas y luego el texto. **Subraya** en el texto la parte donde está cada respuesta.",
          "Si la pregunta empieza con **Where**, busca palabras de lugar: *in, on, under, near, next to*."],
  "review": "La lectura *Where's the Puddle?* y la Gramática A y C",
  "parts": [{"intro": "Lee el mensaje de Sofía y responde.",
             "reading": {"title": "A Message from Sofía", "paras": [
                "Hi, Carlos! It's raining a lot in my town today. There is a big storm.",
                "Right now, I'm looking out the window. My brother is playing in the yard. He is wearing his blue raincoat.",
                "My cat is sleeping on the sofa. She doesn't like the rain!",
                "Where's my umbrella? I don't know! I think it's in the car. Is it raining in your town?"]},
             "qs": [
    {"t": "tf", "q": "There is a big storm in Sofía's town.", "a": True, "exp": "*There is a big storm.*"},
    {"t": "mc", "q": "What is Sofía doing right now?", "opts": ["She's playing in the yard.", "She's looking out the window.", "She's sleeping."], "a": 1,
     "exp": "*Right now, I'm looking out the window.*"},
    {"t": "short", "q": "Her brother is wearing his ______________ raincoat.", "accept": [["blue"]], "show": "**blue**"},
    {"t": "mc", "q": "Where is the cat?", "opts": ["on the sofa", "in the car", "in the yard"], "a": 0, "exp": "*My cat is sleeping on the sofa.*"},
    {"t": "tf", "q": "The cat likes the rain.", "a": False, "exp": "*She **doesn't** like the rain!*"},
    {"t": "short", "q": "Sofía thinks her umbrella is in the ______________.", "accept": [["car", "the car"]], "show": "**car**"},
  ]}]},

 "writing": {"skill": "writing", "total": 10,
  "tip": ["Revisa: lo que pasa **ahora** lleva **am / is / are** y el verbo con **-ing**."],
  "review": "Gramática A y C, y los Errores comunes",
  "parts": [
   {"intro": "**Parte A. Cada oración tiene un error. Escríbela correctamente.** (1 punto cada una)", "qs": [
    {"t": "fix", "q": "She jumping in the puddle.", "accept": ["shes jumping in the puddle", "she is jumping in the puddle"], "show": "She **is** jumping in the puddle.", "exp": "falta is"},
    {"t": "fix", "q": "It is rain now.", "accept": ["it is raining now", "its raining now"], "show": "It is **raining** now.", "exp": "rain + ing"},
    {"t": "fix", "q": "I is wearing my boots.", "accept": ["i am wearing my boots", "im wearing my boots"], "show": "I **am** wearing my boots.", "exp": "con I: am"},
    {"t": "fix", "q": "Where the umbrella is?", "accept": ["where is the umbrella", "wheres the umbrella"], "show": "**Where is** the umbrella?", "exp": "en la pregunta, is va antes"},
    {"t": "fix", "q": "They is playing in the rain.", "accept": ["they are playing in the rain", "theyre playing in the rain"], "show": "They **are** playing in the rain.", "exp": "con they: are"},
   ]},
   {"intro": "**Parte B. Escríbele a Sofía qué está pasando en tu casa ahora** con 3 a 5 oraciones. (5 puntos)",
    "note": ["Mensaje de Sofía", "*Hi! Is it raining in your town? What are you doing right now?*"],
    "open": {"lines": 4, "min_sent": 3, "max_sent": 5, "check_intro": "**Revisa tu respuesta.** Marca un punto por cada casilla que cumpliste:",
             "checklist": [
               {"text": "Empecé con un saludo (*Hi, Sofía!*).", "auto": r"^\s*(hi|hello|hey|dear)\b"},
               {"text": "Dije cómo está el tiempo (*It is raining / It's sunny*).", "auto": r"\bit'?s\b|\bit is\b"},
               {"text": "Usé **I am / I'm + -ing**.", "auto": r"\b(i'?m|i am) \w+ing\b"},
               {"text": "Dije qué está haciendo otra persona (*My mom is...*).", "auto": r"\b(he|she|my \w+) is \w+ing\b|\b(he|she)'s \w+ing\b"},
               {"text": "Cada oración empieza con mayúscula y termina con punto.", "auto": "caps"}],
             "sample": "Hi, Sofía! Yes, it's raining in my town. I'm reading a book. My mom is cooking rice."}},
  ]},

 "speaking": {"skill": "speaking", "total": 8,
  "tip": ["Responde siempre con **oración completa**: no solo *Rainy*, sino *It's raining today.*"],
  "review": "Audio 06: escucha, repite y grábate otra vez",
  "parts": [{"intro": "Prepara una grabadora (o usa la de esta página) y luego reproduce el audio. Escucharás 5 preguntas; responde cada una en voz alta **durante la pausa**.",
             "audio": "07",
             "open": {"record": True, "check_intro": "Después, escucha tu grabación y marca un punto por cada casilla:", "checklist": [
               {"text": "Pregunta 1: *It's raining / It's sunny...*"},
               {"text": "Pregunta 2: *I'm wearing...*"},
               {"text": "Pregunta 3: *I'm ...ing*"},
               {"text": "Pregunta 4: *I wear...*"},
               {"text": "Pregunta 5: *It's in / near / next to...*"},
               {"text": "Pronuncié bien *rain* (r suave)"},
               {"text": "Hablé sin leer"}, {"text": "No usé español"}]}}]},

 "mediation": {"skill": "mediation", "total": 8,
  "tip": ["Para pasar un mensaje: busca **qué pasa** y **dónde**. Usa oraciones cortas."],
  "review": "La práctica de Mediation y la Gramática A",
  "parts": [
   {"intro": "**Parte A.** Escríbele a Sofía (solo habla inglés) lo que dijo tu mamá, en **2 o 3 oraciones**.",
    "note": ["Lo que dijo tu mamá", "Está lloviendo mucho. Tu paraguas está debajo de la mesa. Ponte las botas."],
    "open": {"lines": 3, "min_sent": 2, "max_sent": 3, "checklist": [
      {"text": "Dije **It's raining**.", "auto": r"\bit'?s raining\b|\bit is raining\b"},
      {"text": "Mencioné el paraguas (*umbrella*).", "auto": r"\bumbrella\b"},
      {"text": "Dije **under the table**.", "auto": r"\bunder the table\b"},
      {"text": "Mencioné las botas (*boots*).", "auto": r"\bboots\b"},
      {"text": "Usé oraciones cortas y claras."}],
     "sample": "It's raining a lot. Your umbrella is under the table. Put on your boots."}},
   {"intro": "**Parte B.** Simplifica este aviso en **1 o 2 oraciones**.",
    "note": ["Aviso", "*Because of the heavy storm, students are kindly asked to stay inside the classroom during recess and to keep away from the big puddles.*"],
    "open": {"lines": 2, "min_sent": 1, "max_sent": 2, "checklist": [
      {"text": "Mencioné la tormenta (*storm*).", "auto": r"\bstorm\b|\brain"},
      {"text": "Dije que se queden en el salón (*classroom*).", "auto": r"\bclassroom\b|\binside\b"},
      {"text": "Mencioné los charcos (*puddles*).", "auto": r"\bpuddles?\b"}],
     "sample": "There is a storm. Stay in the classroom. Don't go near the puddles."}},
  ]},
}
