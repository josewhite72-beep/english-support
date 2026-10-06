# -*- coding: utf-8 -*-
"""Mini-tests del Tema 6.2 · 4.º (fuente única para el libro y la versión en línea)."""
from common import *

TESTS = {
 "listening": {"skill": "listening", "total": 6,
  "tip": ["Antes de escuchar, **lee todas las preguntas**. Así sabes qué información buscar.",
          "El reporte habla de **hoy** y de **mañana**. Fíjate bien de qué día es cada pregunta."],
  "review": "Vocabulario (audio 01) y la práctica con el audio 04 en velocidad lenta",
  "parts": [{"intro": "Escucha a Valeria con el reporte del clima. Puedes escuchar **dos veces como máximo**.",
             "audio": "05", "qs": [
    {"t": "mc", "q": "What is the weather like right now?", "opts": ["It's sunny.", "It's raining.", "It's windy."], "a": 1,
     "exp": "*Right now, it's raining in Penonomé.*"},
    {"t": "mc", "q": "When is there going to be a big storm?", "opts": ["in the morning", "in the afternoon", "tomorrow"], "a": 1,
     "exp": "*In the afternoon, there is going to be a big storm.*"},
    {"t": "short", "q": "Today you need an ______________.", "accept": [["umbrella"]], "show": "**umbrella**"},
    {"t": "tf", "q": "Today you can wear sandals.", "a": False, "exp": "*Don't wear sandals!*"},
    {"t": "mc", "q": "What is the weather going to be like tomorrow?", "opts": ["rainy and cold", "sunny and hot", "stormy"], "a": 1,
     "exp": "*Tomorrow is going to be sunny and hot.*"},
    {"t": "mc", "q": "What do you need tomorrow?", "opts": ["an umbrella and boots", "a raincoat", "a hat and sunscreen"], "a": 2,
     "exp": "*You need a hat and sunscreen.* Mañana no se necesita paraguas."},
  ]}]},

 "reading": {"skill": "reading", "total": 6,
  "tip": ["Lee primero las preguntas y luego el texto. **Subraya** en el texto la parte donde está cada respuesta."],
  "review": "La lectura *A Rainy Day* y la Gramática A",
  "parts": [{"intro": "Lee la lista de Ana para el paseo y responde.",
             "reading": {"title": "Ana's Rainy Day List", "paras": [
                "Tomorrow is our school trip to the farm. The forecast says it's going to rain!",
                "What do I need? I need my umbrella and my raincoat. I need my green boots, too.",
                "I don't need my sandals, because the farm is wet and muddy.",
                "My brother Carlos needs a raincoat, but he doesn't have one. He's going to wear Dad's old raincoat. It's very big!"]},
             "qs": [
    {"t": "mc", "q": "Where is the school trip?", "opts": ["to the beach", "to the farm", "to the river"], "a": 1, "exp": "*Tomorrow is our school trip to the farm.*"},
    {"t": "tf", "q": "The forecast says it's going to be sunny.", "a": False, "exp": "*The forecast says it's going to rain!*"},
    {"t": "short", "q": "Ana needs her ______________ boots.", "accept": [["green"]], "show": "**green**"},
    {"t": "mc", "q": "Why doesn't Ana need her sandals?", "opts": ["They are old.", "The farm is wet and muddy.", "It's hot."], "a": 1,
     "exp": "*...because the farm is wet and muddy.*"},
    {"t": "tf", "q": "Carlos has a raincoat.", "a": False, "exp": "*He needs a raincoat, but he doesn't have one.*"},
    {"t": "mc", "q": "Whose raincoat is Carlos going to wear?", "opts": ["Ana's", "Mom's", "Dad's"], "a": 2, "exp": "*He's going to wear Dad's old raincoat.*"},
  ]}]},

 "writing": {"skill": "writing", "total": 10,
  "tip": ["Revisa: **an** antes de vocal (*an umbrella*), y con he / she el verbo lleva **-s** (*she needs*)."],
  "review": "Gramática A y los Errores comunes",
  "parts": [
   {"intro": "**Parte A. Cada oración tiene un error. Escríbela correctamente.** (1 punto cada una)", "qs": [
    {"t": "fix", "q": "I need a umbrella.", "accept": ["i need an umbrella"], "show": "I need **an** umbrella.", "exp": "an antes de vocal"},
    {"t": "fix", "q": "She need boots.", "accept": ["she needs boots"], "show": "She **needs** boots.", "exp": "con she: needs"},
    {"t": "fix", "q": "What you wear in the rain?", "accept": ["what do you wear in the rain"], "show": "What **do** you wear in the rain?", "exp": "falta do"},
    {"t": "fix", "q": "It is rain now.", "accept": ["it is raining now", "its raining now"], "show": "It is **raining** now.", "exp": "rain + ing"},
    {"t": "fix", "q": "My boots is wet.", "accept": ["my boots are wet"], "show": "My boots **are** wet.", "exp": "boots es plural: are"},
   ]},
   {"intro": "**Parte B. Responde el mensaje de Carlos** con 3 a 5 oraciones. (5 puntos)",
    "note": ["Mensaje de Carlos", "*Hi! It's raining a lot. What do you need today? What do you wear in the rain?*"],
    "open": {"lines": 4, "min_sent": 3, "max_sent": 5, "check_intro": "**Revisa tu respuesta.** Marca un punto por cada casilla que cumpliste:",
             "checklist": [
               {"text": "Empecé con un saludo (*Hi, Carlos!*).", "auto": r"^\s*(hi|hello|hey|dear)\b"},
               {"text": "Usé **I need**.", "auto": r"\bi need\b"},
               {"text": "Usé **I wear**.", "auto": r"\bi wear\b"},
               {"text": "Usé **an umbrella** (con *an*).", "auto": r"\ban umbrella\b"},
               {"text": "Cada oración empieza con mayúscula y termina con punto.", "auto": "caps"}],
             "sample": "Hi, Carlos! I need an umbrella today. I wear my raincoat and my boots. I don't wear sandals."}},
  ]},

 "speaking": {"skill": "speaking", "total": 8,
  "tip": ["Responde siempre con **oración completa**: no solo *Umbrella*, sino *I need an umbrella.*"],
  "review": "Audio 06: escucha, repite y grábate otra vez",
  "parts": [{"intro": "Prepara una grabadora (o usa la de esta página) y luego reproduce el audio. Escucharás 5 preguntas; responde cada una en voz alta **durante la pausa**.",
             "audio": "07",
             "open": {"record": True, "check_intro": "Después, escucha tu grabación y marca un punto por cada casilla:", "checklist": [
               {"text": "Pregunta 1: *I need an umbrella.*"},
               {"text": "Pregunta 2: *I wear...*"},
               {"text": "Pregunta 3: *I wear sandals / a hat...*"},
               {"text": "Pregunta 4: *I see lightning / I hear thunder.*"},
               {"text": "Pregunta 5: *Yes, I do / No, I don't* y *because*"},
               {"text": "Usé *an* antes de *umbrella*"},
               {"text": "Hablé sin leer"}, {"text": "No usé español"}]}}]},

 "mediation": {"skill": "mediation", "total": 8,
  "tip": ["Para pasar un mensaje: busca **qué necesita** y **qué debe usar** la persona. Usa oraciones cortas."],
  "review": "La práctica de Mediation y la Gramática A",
  "parts": [
   {"intro": "**Parte A.** Escríbele a Carlos (solo habla inglés) lo que dijo tu papá, en **2 o 3 oraciones**.",
    "note": ["Lo que dijo tu papá", "Va a llover. Necesitas un paraguas. Usa tus botas, no tus sandalias."],
    "open": {"lines": 3, "min_sent": 2, "max_sent": 3, "checklist": [
      {"text": "Mencioné la lluvia (*rain*).", "auto": r"\brain"},
      {"text": "Dije **You need an umbrella**.", "auto": r"\bneed an umbrella\b"},
      {"text": "Mencioné las botas (*boots*).", "auto": r"\bboots\b"},
      {"text": "Dije que no use sandalias.", "auto": r"\bsandals\b"},
      {"text": "Usé oraciones cortas y claras."}],
     "sample": "It's going to rain. You need an umbrella. Wear your boots, not your sandals."}},
   {"intro": "**Parte B.** Simplifica este aviso en **1 o 2 oraciones**.",
    "note": ["Aviso", "*During the rainy season, all students are encouraged to bring an umbrella or a raincoat and an extra pair of dry socks.*"],
    "open": {"lines": 2, "min_sent": 1, "max_sent": 2, "checklist": [
      {"text": "Mencioné paraguas o impermeable.", "auto": r"\bumbrella\b|\braincoat\b"},
      {"text": "Mencioné medias secas (*dry socks*).", "auto": r"\bsocks\b"},
      {"text": "Usé una instrucción (*Bring...*).", "auto": r"\bbring\b"}],
     "sample": "It's the rainy season. Bring an umbrella and dry socks."}},
  ]},
}
