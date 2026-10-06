# -*- coding: utf-8 -*-
"""2.º grado · Scenario 5, Theme 1 — It's the Park!
Fuentes: planeamiento 2_5-1 y módulo GeMA 2_5-1 (dibujos del módulo)."""
from common import *
import kid

THEME_ID = "5-1"
THEME_NUM = "Theme 1"
THEME_TITLE = "It's the Park!"
THEME_ES = "¡Es el parque!"
SCENARIO = "Scenario 5: Exploring My Community"

GOALS = ["Reconozco 6 lugares de mi comunidad cuando los escucho.",
         "Pregunto *Where is it?* y respondo *It's the park.*",
         "Leo oraciones cortas y las uno con su dibujo.",
         "Escribo el nombre de los lugares."]
FAMILY = ("En este tema su hijo/a aprende **6 lugares de la comunidad** y a preguntar y responder "
          "**Where is it? — It's the park.** /uér is it — its de park/ (¿Dónde es? — Es el parque.)")

VOCAB = [
    ("park", "park", "/park/", "parque", "It's the park."),
    ("playground", "playground", "/PLÉI-graund/", "área de juegos", "It's the playground."),
    ("school", "school", "/skul/", "escuela", "It's the school."),
    ("church", "church", "/cherch/", "iglesia", "It's the church."),
    ("home", "home", "/joum/", "casa, hogar", "This is my home."),
    ("library", "library", "/LÁI-bre-ri/", "biblioteca", "It's the library."),
]
SOUND = ["Diga despacio: **p-p-park, p-p-playground**. ¿Suenan igual al principio? Busquen otra palabra con /p/ (por ejemplo, *pencil*)."]

PATTERN = {"rows": [["**It's**", "**the**", "**park.**"], ["Es", "el / la", "parque."]],
           "note": "**Nota para la familia:** *the* significa \"el\" o \"la\": *It's the school.* /its de skul/ = Es **la** escuela. Para preguntar qué lugar es: **Where is it?** /uér is it/."}

SONG_TITLE = "Where Is It?"
SONG = [("Where is it? Where is it?", "Mano sobre los ojos, como buscando."),
        ("It's the park! It's the park!", "Señala lejos."),
        ("Where is it? Where is it?", "Mano sobre los ojos."),
        ("It's the school! It's the school!", "Abre un libro imaginario."),
        ("It's the playground! I like the playground!", "Baja por un tobogán imaginario.")]

STORY_TITLE = "A Walk with Grandma"
STORY = [("home", "This is my home."),
         ("school", "Look, Grandma! It's the school."),
         ("church", "It's the church."),
         ("library", "It's the library."),
         ("park", "It's the park! I like the park.")]
STORY_QS = [("Number 2. Where is it?", "/NÁM-ber tu. uér is it/", "It's the school."),
            ("Number 4. Where is it?", "/NÁM-ber for. uér is it/", "It's the library."),
            ("Number 5. Where is it?", "/NÁM-ber faiv. uér is it/", "It's the park.")]

LISTEN_PRACTICE = [("It's the library.", ["library", "home", "park"], 0),
                   ("It's the playground.", ["church", "playground", "school"], 1),
                   ("It's the church.", ["park", "library", "church"], 2),
                   ("It's the school.", ["school", "home", "playground"], 0)]
READ_PRACTICE = [("park", "It's the park.", True), ("home", "It's the school.", False),
                 ("playground", "It's the playground.", True), ("church", "It's the library.", False)]
WRITE_PRACTICE = ["park", "home", "school", "church"]

SPEAK_MODELS = ["Where is it?", "It's the park.", "It's the school.", "It's the library.", "I like the park."]
SPEAK_TEST = [("park", "Where is it?", "It's the park."),
              ("school", "Where is it?", "It's the school."),
              ("church", "Where is it?", "It's the church."),
              ("playground", "Do you like the playground?", "Yes! I like the playground.")]
MEDIATION_PRACTICE = ("En una caminata o desde la ventana, el niño señala los lugares que conoce y dice **It's the school!** "
                      "Luego le **enseña a otro familiar** dos lugares en inglés y le explica en español qué significan.")

TESTS = {
 "listening": {"skill": "listening", "total": 5,
  "tip": ["Antes de cada número, **miren los 3 dibujos** y díganlos en voz alta."],
  "review": "Palabras nuevas (audio 01) y la práctica de escucha (audio 04)",
  "parts": [{"intro": "**Adulto:** ponga el audio. El niño escucha cada número y **toca** (o encierra) el dibujo correcto. Puede escuchar **dos veces**.",
             "audio": "05",
             "said": ["It's the park.", "This is my home.", "It's the library.", "It's the church.", "It's the playground."],
             "qs": [
    {"t": "mc", "q": "", "opts": ["@school", "@park", "@church"], "a": 1, "exp": "*It's the park.*"},
    {"t": "mc", "q": "", "opts": ["@home", "@library", "@playground"], "a": 0, "exp": "*This is my home.*"},
    {"t": "mc", "q": "", "opts": ["@church", "@school", "@library"], "a": 2, "exp": "*It's the library.*"},
    {"t": "mc", "q": "", "opts": ["@church", "@park", "@home"], "a": 0, "exp": "*It's the church.*"},
    {"t": "mc", "q": "", "opts": ["@library", "@playground", "@school"], "a": 1, "exp": "*It's the playground.*"},
  ]}]},

 "reading": {"skill": "reading", "total": 5,
  "tip": ["Lee la oración **en voz alta** antes de elegir."],
  "review": "El cuento *A Walk with Grandma* y la práctica de lectura",
  "parts": [{"intro": "**Adulto:** el niño lee la oración y **toca** el dibujo correcto.", "qs": [
    {"t": "mc", "q": "It's the school.", "opts": ["@home", "@school", "@park"], "a": 1},
    {"t": "mc", "q": "It's the library.", "opts": ["@library", "@church", "@playground"], "a": 0},
    {"t": "mc", "q": "This is my home.", "opts": ["@church", "@school", "@home"], "a": 2},
   ]},
   {"intro": "**Adulto:** el niño lee y mira el dibujo. ¿Dicen lo mismo? **True** (sí) o **False** (no).", "qs": [
    {"t": "tf", "q": "It's the park.", "img": "park", "a": True, "exp": "Es el parque."},
    {"t": "tf", "q": "It's the church.", "img": "playground", "a": False, "exp": "Es el área de juegos: *It's the playground.*"},
   ]}]},

 "writing": {"skill": "writing", "total": 5,
  "tip": ["Escribe la palabra **letra por letra**. Revisa con la página de Palabras nuevas."],
  "review": "La práctica de escritura y la página de Palabras nuevas",
  "parts": [
   {"intro": "**Parte A.** Mira el dibujo y completa la oración. (1 punto cada una)", "qs": [
    {"t": "short", "q": "It's the ______________.", "img": "park", "accept": [["park"]], "show": "**park**"},
    {"t": "short", "q": "It's the ______________.", "img": "school", "accept": [["school"]], "show": "**school**"},
    {"t": "short", "q": "It's the ______________.", "img": "library", "accept": [["library"]], "show": "**library**"},
   ]},
   {"intro": "**Parte B.** Dibuja tu lugar favorito en tu cuaderno y escribe **1 oración** con *I like the...* (2 puntos)",
    "note": ["Modelo", "*I like the park.*"],
    "open": {"lines": 1, "min_sent": 1, "max_sent": 2, "check_intro": "**Adulto:** marque un punto por cada casilla:",
             "checklist": [
               {"text": "Escribió **I like the** + un lugar.", "auto": r"\bi like the (park|playground|school|church|library|home)\b"},
               {"text": "Empezó con mayúscula y terminó con punto.", "auto": "caps"}],
             "sample": "I like the playground."}},
  ]},

 "speaking": {"skill": "speaking", "total": 5,
  "tip": ["Responda con el niño una vez para practicar. La segunda vez, el niño responde solo."],
  "review": "Audio 06: escucha y repite",
  "parts": [{"intro": "**Adulto:** ponga el audio. El niño mira cada dibujo y responde en voz alta en la pausa.",
             "audio": "07", "pics": [(img, f"Picture {kid.NUMS[i]}") for i, (img, _, _) in enumerate(SPEAK_TEST)],
             "open": {"record": True, "check_intro": "**Adulto:** escuche y marque un punto por cada casilla:", "checklist": [
               {"text": "Picture 1: *It's the park.*"},
               {"text": "Picture 2: *It's the school.*"},
               {"text": "Picture 3: *It's the church.*"},
               {"text": "Picture 4: *I like the playground.*"},
               {"text": "Respondió en inglés, sin ayuda"}]}}]},

 "mediation": {"skill": "mediation", "total": 4,
  "tip": ["Primero diga la oración en español; después busquen las palabras en inglés."],
  "review": "La práctica de Mediation: enseño a mi familia",
  "parts": [
   {"intro": "**Parte A.** La abuela no sabe inglés. Ayúdale: ¿qué significa? Escríbelo **en español**.",
    "note": ["Oración", "*It's the library.*"],
    "open": {"lines": 1, "min_sent": 0, "max_sent": 0, "checklist": [
      {"text": "Escribió *Es la biblioteca*."},
      {"text": "Usó *la* (the)."}],
     "sample": "Es la biblioteca."}},
   {"intro": "**Parte B.** Tu primito dice: *«Me gusta el parque»*. Escríbelo **en inglés**.",
    "open": {"lines": 1, "min_sent": 1, "max_sent": 1, "checklist": [
      {"text": "Escribió **I like the park**.", "auto": r"\bi like the park\b"},
      {"text": "Empezó con mayúscula y terminó con punto.", "auto": "caps"}],
     "sample": "I like the park."}},
  ]},
}

kid.build(globals())
