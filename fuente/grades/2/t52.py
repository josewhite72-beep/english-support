# -*- coding: utf-8 -*-
"""2.º grado · Scenario 5, Theme 2 — It's the Market!
Fuentes: planeamiento 2_5-2 y módulo GeMA 2_5-2 (dibujos del módulo)."""
from common import *
import kid

THEME_ID = "5-2"
THEME_NUM = "Theme 2"
THEME_TITLE = "It's the Market!"
THEME_ES = "¡Es el mercado!"
SCENARIO = "Scenario 5: Exploring My Community"

GOALS = ["Reconozco lugares del pueblo cuando los escucho.",
         "Pregunto *What place is it?* y respondo *It's the market.*",
         "Digo a dónde voy: *I go to the market.*",
         "Leo y escribo el nombre de los lugares."]
FAMILY = ("En este tema su hijo/a aprende **lugares del pueblo** y dos frases: **What place is it? — It's the gym.** "
          "/uát pleis is it — its de yim/ y **I go to the market.** /ai góu tu de MAR-ket/ (Voy al mercado.)")

VOCAB = [
    ("market", "market", "/MAR-ket/", "mercado", "I go to the market."),
    ("store", "store", "/stor/", "tienda", "It's the store."),
    ("office", "office", "/Ó-fis/", "oficina", "It's Dad's office."),
    ("gym", "gym", "/yim/", "gimnasio", "It's the gym."),
    ("school", "school", "/skul/", "escuela", "I go to the school."),
    ("park", "park", "/park/", "parque", "I go to the park."),
]
SOUND = ["Diga **s-tore** y **s-chool** **sin decir \"e\" al principio** (no \"estor\", no \"escul\"). Empiecen con un sonido de serpiente: **ssss-tore**, **ssss-chool**."]

PATTERN = {"rows": [["**I go to**", "**the**", "**market.**"], ["Voy", "al / a la", "mercado."]],
           "note": "**Nota para la familia:** para decir qué lugar es, seguimos usando **It's the...**: *It's the gym.* /its de yim/ = Es el gimnasio. Para preguntar: **What place is it?** /uát pleis is it/."}

SONG_TITLE = "What Place Is It?"
SONG = [("What place is it? What place is it?", "Encoge los hombros, como preguntando."),
        ("It's the market! It's the market!", "Carga una bolsa imaginaria."),
        ("It's the store! It's the store!", "Abre una puerta imaginaria."),
        ("It's the gym! It's the gym!", "Levanta pesas imaginarias."),
        ("I go to the park! I go to the park!", "Camina en tu lugar.")]

STORY_TITLE = "Saturday with Dad"
STORY = [("market", "Look, Dad! It's the market."),
         ("store", "It's the store."),
         ("office", "It's Dad's office."),
         ("gym", "It's the gym."),
         ("park", "I go to the park. I like the park!")]
STORY_QS = [("Number 1. What place is it?", "/NÁM-ber uan. uát pleis is it/", "It's the market."),
            ("Number 3. What place is it?", "/NÁM-ber zri. uát pleis is it/", "It's Dad's office."),
            ("Number 4. What place is it?", "/NÁM-ber for. uát pleis is it/", "It's the gym.")]

LISTEN_PRACTICE = [("It's the store.", ["office", "store", "park"], 1),
                   ("It's the gym.", ["gym", "school", "market"], 0),
                   ("It's the office.", ["market", "park", "office"], 2),
                   ("I go to the market.", ["store", "market", "gym"], 1)]
READ_PRACTICE = [("market", "It's the market.", True), ("gym", "It's the park.", False),
                 ("office", "It's the office.", True), ("store", "It's the school.", False)]
WRITE_PRACTICE = ["market", "store", "office", "gym"]

SPEAK_MODELS = ["What place is it?", "It's the market.", "It's the gym.", "I go to the store.", "I go to the park."]
SPEAK_TEST = [("market", "What place is it?", "It's the market."),
              ("gym", "What place is it?", "It's the gym."),
              ("office", "What place is it?", "It's the office."),
              ("store", "Where do you go?", "I go to the store.")]
MEDIATION_PRACTICE = ("El niño pregunta a cada familiar a dónde va durante la semana y lo dice en inglés: **Mom goes to the store.** "
                      "Si le cuesta, basta con **the store!** Después le explica a alguien en español qué dijo.")

TESTS = {
 "listening": {"skill": "listening", "total": 5,
  "tip": ["Antes de cada número, **miren los 3 dibujos** y díganlos en voz alta."],
  "review": "Palabras nuevas (audio 01) y la práctica de escucha (audio 04)",
  "parts": [{"intro": "**Adulto:** ponga el audio. El niño escucha cada número y **toca** (o encierra) el dibujo correcto. Puede escuchar **dos veces**.",
             "audio": "05",
             "said": ["It's the gym.", "It's the market.", "I go to the store.", "It's the office.", "I go to the school."],
             "qs": [
    {"t": "mc", "q": "", "opts": ["@park", "@office", "@gym"], "a": 2, "exp": "*It's the gym.*"},
    {"t": "mc", "q": "", "opts": ["@market", "@store", "@school"], "a": 0, "exp": "*It's the market.*"},
    {"t": "mc", "q": "", "opts": ["@gym", "@store", "@office"], "a": 1, "exp": "*I go to the store.*"},
    {"t": "mc", "q": "", "opts": ["@office", "@market", "@park"], "a": 0, "exp": "*It's the office.*"},
    {"t": "mc", "q": "", "opts": ["@store", "@gym", "@school"], "a": 2, "exp": "*I go to the school.*"},
  ]}]},

 "reading": {"skill": "reading", "total": 5,
  "tip": ["Lee la oración **en voz alta** antes de elegir."],
  "review": "El cuento *Saturday with Dad* y la práctica de lectura",
  "parts": [{"intro": "**Adulto:** el niño lee la oración y **toca** el dibujo correcto.", "qs": [
    {"t": "mc", "q": "It's the gym.", "opts": ["@store", "@gym", "@market"], "a": 1},
    {"t": "mc", "q": "I go to the market.", "opts": ["@market", "@office", "@park"], "a": 0},
    {"t": "mc", "q": "It's Dad's office.", "opts": ["@school", "@gym", "@office"], "a": 2},
   ]},
   {"intro": "**Adulto:** el niño lee y mira el dibujo. ¿Dicen lo mismo? **True** (sí) o **False** (no).", "qs": [
    {"t": "tf", "q": "It's the store.", "img": "store", "a": True, "exp": "Es la tienda."},
    {"t": "tf", "q": "I go to the gym.", "img": "market", "a": False, "exp": "Es el mercado: *I go to the market.*"},
   ]}]},

 "writing": {"skill": "writing", "total": 5,
  "tip": ["Escribe la palabra **letra por letra**. Revisa con la página de Palabras nuevas."],
  "review": "La práctica de escritura y la página de Palabras nuevas",
  "parts": [
   {"intro": "**Parte A.** Mira el dibujo y completa la oración. (1 punto cada una)", "qs": [
    {"t": "short", "q": "I go to the ______________.", "img": "market", "accept": [["market"]], "show": "**market**"},
    {"t": "short", "q": "It's the ______________.", "img": "gym", "accept": [["gym"]], "show": "**gym**"},
    {"t": "short", "q": "It's the ______________.", "img": "store", "accept": [["store"]], "show": "**store**"},
   ]},
   {"intro": "**Parte B.** ¿A dónde vas el sábado? Escribe **1 oración** con *I go to the...* (2 puntos)",
    "note": ["Modelo", "*I go to the park.*"],
    "open": {"lines": 1, "min_sent": 1, "max_sent": 2, "check_intro": "**Adulto:** marque un punto por cada casilla:",
             "checklist": [
               {"text": "Escribió **I go to the** + un lugar.", "auto": r"\bi go to the (market|store|office|gym|school|park|playground|church|library)\b"},
               {"text": "Empezó con mayúscula y terminó con punto.", "auto": "caps"}],
             "sample": "I go to the market."}},
  ]},

 "speaking": {"skill": "speaking", "total": 5,
  "tip": ["Responda con el niño una vez para practicar. La segunda vez, el niño responde solo."],
  "review": "Audio 06: escucha y repite",
  "parts": [{"intro": "**Adulto:** ponga el audio. El niño mira cada dibujo y responde en voz alta en la pausa.",
             "audio": "07", "pics": [(img, f"Picture {kid.NUMS[i]}") for i, (img, _, _) in enumerate(SPEAK_TEST)],
             "open": {"record": True, "check_intro": "**Adulto:** escuche y marque un punto por cada casilla:", "checklist": [
               {"text": "Picture 1: *It's the market.*"},
               {"text": "Picture 2: *It's the gym.*"},
               {"text": "Picture 3: *It's the office.*"},
               {"text": "Picture 4: *I go to the store.*"},
               {"text": "Respondió en inglés, sin ayuda"}]}}]},

 "mediation": {"skill": "mediation", "total": 4,
  "tip": ["Primero diga la oración en español; después busquen las palabras en inglés."],
  "review": "La práctica de Mediation: a dónde va mi familia",
  "parts": [
   {"intro": "**Parte A.** Tu tío no sabe inglés. Ayúdale: ¿qué significa? Escríbelo **en español**.",
    "note": ["Oración", "*I go to the gym.*"],
    "open": {"lines": 1, "min_sent": 0, "max_sent": 0, "checklist": [
      {"text": "Escribió *Voy al gimnasio*."},
      {"text": "Entendió *I go* = voy."}],
     "sample": "Voy al gimnasio."}},
   {"intro": "**Parte B.** Tu hermanita dice: *«Es la tienda»*. Escríbelo **en inglés**.",
    "open": {"lines": 1, "min_sent": 1, "max_sent": 1, "checklist": [
      {"text": "Escribió **It's the store**.", "auto": r"\b(it'?s|it is) the store\b"},
      {"text": "Empezó con mayúscula y terminó con punto.", "auto": "caps"}],
     "sample": "It's the store."}},
  ]},
}

kid.build(globals())
