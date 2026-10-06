# -*- coding: utf-8 -*-
"""Mini-tests del Tema 5.1 · 5.º (fuente única para el libro y la versión en línea)."""
from common import *

TESTS = {
 "listening": {"skill": "listening", "total": 6,
  "tip": ["Antes de escuchar, **lee todas las preguntas**. Así sabes qué información buscar.",
          "Fíjate en **quién** hace cada cosa: el audio habla de varias personas (Diego, su mamá, su papá)."],
  "review": "Vocabulario (audio 01) y la práctica con el audio 04 en velocidad lenta",
  "parts": [{"intro": "Escucha a Diego hablar de las actividades que le gustan. Puedes escuchar **dos veces como máximo**, como en una prueba real.",
             "audio": "05", "qs": [
    {"t": "mc", "q": "How old is Diego?", "opts": ["10", "11", "12"], "a": 1, "exp": "*I'm eleven years old.*"},
    {"t": "mc", "q": "What does Diego like doing in the morning?", "opts": ["riding his bike", "swimming", "reading"], "a": 0,
     "exp": "*In the morning, I like riding my bike to school.*"},
    {"t": "short", "q": "In the afternoon, Diego likes playing ______________ with his friends.",
     "accept": [["football", "soccer"]], "show": "**football**"},
    {"t": "tf", "q": "Diego likes swimming.", "a": False, "exp": "*I don't like swimming. The water is cold!*"},
    {"t": "mc", "q": "Who likes walking in the evening?", "opts": ["Diego", "his mom", "his dad"], "a": 1,
     "exp": "*My mom likes walking in the evening.* Al papá le gusta correr los domingos."},
    {"t": "tf", "q": "Diego's dad likes running on Sundays.", "a": True, "exp": "*...and my dad likes running on Sundays.*"},
  ]}]},

 "reading": {"skill": "reading", "total": 6,
  "tip": ["Lee primero las preguntas y luego el texto. **Subraya** en el texto la parte donde está cada respuesta.",
          "Cuidado con **like** y **don't like**: una palabra cambia todo el significado."],
  "review": "La lectura *Ana's Afternoons* y la Gramática A",
  "parts": [{"intro": "Lee el mensaje de Carla y responde.",
             "reading": {"title": "Carla's Week", "paras": [
                "Hi! I'm Carla. I'm eleven years old, and I live in Penonomé.",
                "I like dancing very much. I go to dance class on Tuesdays and Thursdays in the afternoon.",
                "My brother Pedro likes playing football, but he doesn't like dancing. On Saturdays, we like riding our bikes in the morning.",
                "I don't like running because it's very hot in the afternoon. In the evening, I like reading comics. What about you?"]},
             "qs": [
    {"t": "short", "q": "Where does Carla live? In ______________.", "accept": [["penonome", "penonomé"]], "show": "**Penonomé**"},
    {"t": "mc", "q": "When does Carla go to dance class?", "opts": ["on Mondays", "on Tuesdays and Thursdays", "on Saturdays"], "a": 1,
     "exp": "*I go to dance class on Tuesdays and Thursdays in the afternoon.*"},
    {"t": "tf", "q": "Pedro likes dancing.", "a": False, "exp": "*...but he **doesn't like** dancing.* A Pedro le gusta el fútbol."},
    {"t": "mc", "q": "What do Carla and Pedro like doing on Saturdays?", "opts": ["playing football", "riding their bikes", "reading comics"], "a": 1,
     "exp": "*On Saturdays, we like riding our bikes in the morning.*"},
    {"t": "short", "q": "Why doesn't Carla like running? Because it's very ______________.", "accept": [["hot"]], "show": "**hot**"},
    {"t": "mc", "q": "What does Carla like doing in the evening?", "opts": ["dancing", "running", "reading comics"], "a": 2,
     "exp": "*In the evening, I like reading comics.*"},
  ]}]},

 "writing": {"skill": "writing", "total": 10,
  "tip": ["Revisa dos cosas: el verbo después de *like* lleva **-ing**, y con he / she se dice **likes**."],
  "review": "Gramática A y B, y los Errores comunes",
  "parts": [
   {"intro": "**Parte A. Cada oración tiene un error. Escríbela correctamente.** (1 punto cada una)", "qs": [
    {"t": "fix", "q": "I like walk in the afternoon.", "accept": ["i like walking in the afternoon"], "show": "I like **walking** in the afternoon.", "exp": "like + -ing"},
    {"t": "fix", "q": "She like dancing.", "accept": ["she likes dancing"], "show": "She **likes** dancing.", "exp": "con she: likes"},
    {"t": "fix", "q": "I like swiming on Saturdays.", "accept": ["i like swimming on saturdays"], "show": "I like **swimming** on Saturdays.", "exp": "swim → swimming, con doble m"},
    {"t": "fix", "q": "Do you like reading? — Yes, I like.", "accept": ["do you like reading yes i do"], "show": "Do you like reading? — Yes, I **do**.", "exp": "respuesta corta: Yes, I do"},
    {"t": "fix", "q": "He don't like running.", "accept": ["he doesnt like running", "he does not like running"], "show": "He **doesn't** like running.", "exp": "con he: doesn't"},
   ]},
   {"intro": "**Parte B. Responde el mensaje de Luis** con 3 a 5 oraciones. (5 puntos)",
    "note": ["Mensaje de Luis", "*Hi! What do you like doing in the afternoon? Do you like swimming? What don't you like doing?*"],
    "open": {"lines": 5, "min_sent": 3, "max_sent": 5, "check_intro": "**Revisa tu respuesta.** Marca un punto por cada casilla que cumpliste:",
             "checklist": [
               {"text": "Empecé con un saludo (*Hi, Luis!*).", "auto": r"^\s*(hi|hello|hey|dear)\b"},
               {"text": "Dije lo que me gusta con **like + -ing**.", "auto": r"\blike \w+ing\b"},
               {"text": "Respondí si me gusta nadar (*Yes, I do / No, I don't*).", "auto": r"\bswimming\b|\byes,? i do\b|\bno,? i don'?t\b"},
               {"text": "Dije algo que **no** me gusta (*I don't like...*).", "auto": r"\bdon'?t like\b|\bdo not like\b"},
               {"text": "Cada oración empieza con mayúscula y termina con punto.", "auto": "caps"}],
             "sample": "Hi, Luis! I like riding my bike in the afternoon. Yes, I do. I like swimming on Saturdays. I don't like running."}},
  ]},

 "speaking": {"skill": "speaking", "total": 8,
  "tip": ["Responde siempre con **oración completa**: no solo *Swimming*, sino *I like swimming.*",
          "Si la pregunta empieza con **Do you...?**, empieza tu respuesta con *Yes, I do* o *No, I don't*."],
  "review": "Audio 06: escucha, repite y grábate otra vez",
  "parts": [{"intro": "Prepara una grabadora (o usa la de esta página) y luego reproduce el audio. Escucharás 5 preguntas; responde cada una en voz alta **durante la pausa**.",
             "audio": "07",
             "open": {"record": True, "check_intro": "Después, escucha tu grabación y marca un punto por cada casilla:", "checklist": [
               {"text": "Pregunta 1: *I like ...ing in the afternoon.*"},
               {"text": "Pregunta 2: *Yes, I do. / No, I don't.*"},
               {"text": "Pregunta 3: *I don't like...*"},
               {"text": "Pregunta 4: usé **likes** (con -s)"},
               {"text": "Pregunta 5: oración completa"},
               {"text": "Pronuncié las palabras con -ing"},
               {"text": "Hablé sin leer"}, {"text": "No usé español"}]}}]},

 "mediation": {"skill": "mediation", "total": 8,
  "tip": ["Para pasar un mensaje a otro idioma: busca **quién**, **qué le gusta** y **cuándo**. Usa oraciones cortas."],
  "review": "La práctica de Mediation y la Gramática A",
  "parts": [
   {"intro": "**Parte A.** Escríbele a Luis (solo habla inglés) lo que dijo tu hermana, en **2 o 3 oraciones**.",
    "note": ["Lo que dijo tu hermana", "Me gusta bailar en la tarde. No me gusta correr. Los sábados me gusta nadar."],
    "open": {"lines": 3, "min_sent": 2, "max_sent": 3, "checklist": [
      {"text": "Usé **She likes** (es mi hermana).", "auto": r"\bshe likes\b"},
      {"text": "Dije que le gusta bailar en la tarde.", "auto": r"\bdancing\b"},
      {"text": "Dije que **no** le gusta correr (*doesn't like*).", "auto": r"\bdoesn'?t like\b|\bdoes not like\b"},
      {"text": "Dije lo de los sábados (*on Saturdays*).", "auto": r"\bsaturdays?\b"},
      {"text": "Usé oraciones cortas y claras."}],
     "sample": "My sister likes dancing in the afternoon. She doesn't like running. On Saturdays, she likes swimming."}},
   {"intro": "**Parte B.** Simplifica este aviso en **1 o 2 oraciones**.",
    "note": ["Aviso", "*Students who would like to join the afternoon walking club should come to the school gate on Wednesday at four o'clock.*"],
    "open": {"lines": 2, "min_sent": 1, "max_sent": 2, "checklist": [
      {"text": "Dije **qué** (*walking club*).", "auto": r"\bwalking\b|\bwalk\b"},
      {"text": "Dije **dónde** (*school gate*).", "auto": r"\bgate\b|\bschool\b"},
      {"text": "Dije **cuándo** (*Wednesday, four o'clock*).", "auto": r"\bwednesday\b"}],
     "sample": "Do you like walking? Come to the school gate on Wednesday at four o'clock."}},
  ]},
}
