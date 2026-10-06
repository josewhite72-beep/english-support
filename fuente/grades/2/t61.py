# -*- coding: utf-8 -*-
"""2.º grado · Scenario 6, Theme 1 — It's the Rainforest.
Fuentes: planeamiento 2_6-1 y módulo GeMA 2_6-1. Dibujos: OpenMoji (CC BY-SA 4.0) y propios."""
from common import *
import kid

THEME_ID = "6-1"
THEME_NUM = "Theme 1"
THEME_TITLE = "It's the Rainforest."
THEME_ES = "Es la selva tropical."
SCENARIO = "Scenario 6: Discovering Nature's Wonders"

GOALS = ["Reconozco los animales de la selva cuando los escucho.",
         "Pregunto *What animal is it?* y respondo *It is a frog.*",
         "Digo el color de un animal: *It is a green frog.*",
         "Leo y escribo el nombre de los animales."]
FAMILY = ("En este tema su hijo/a aprende **animales de la selva de Panamá** y a decir su color: "
          "**What animal is it? — It is a green frog.** /uát Á-ni-mal is it — it is a grin frog/ (¿Qué animal es? — Es una rana verde.)")

VOCAB = [
    ("rainforest", "rainforest", "/RÉIN-fo-rest/", "selva tropical", "It's the rainforest."),
    ("sloth", "sloth", "/slouz/", "perezoso", "It is a brown sloth."),
    ("toucan", "toucan", "/TÚ-kan/", "tucán", "It is a black toucan."),
    ("monkey", "monkey", "/MÓN-ki/", "mono", "It is a brown monkey."),
    ("parrot", "parrot", "/PÁ-rot/", "loro", "It is a green parrot."),
    ("frog", "frog", "/frog/", "rana", "It is a green frog."),
    ("snake", "snake", "/sneik/", "serpiente", "It is a long snake."),
    ("jaguar", "jaguar", "/YÁ-guar/", "jaguar", "It is a yellow jaguar."),
]
SOUND = ["**sloth** y **snake** empiezan con /s/, **sin \"e\" al principio** (no \"eslouz\"). Digan juntos: **ssss-loth, ssss-nake**.",
         "Colores que vamos a usar: **green** /grin/ verde · **brown** /braun/ café · **black** /blak/ negro · **yellow** /YÉ-lou/ amarillo · **red** /red/ rojo."]

PATTERN = {"rows": [["**It is a**", "**green**", "**frog.**"], ["Es una", "rana", "verde."]],
           "note": "**Nota para la familia:** en inglés el **color va antes** del animal: *green frog* = rana verde. Para preguntar: **What animal is it?** /uát Á-ni-mal is it/ = ¿Qué animal es?"}

SONG_TITLE = "In the Rainforest"
SONG = [("It is a green frog,", "Salta como rana."),
        ("It is a brown monkey,", "Ráscate como mono."),
        ("It is a red parrot,", "Mueve los brazos como alas."),
        ("It is a long snake,", "Mueve los brazos como serpiente."),
        ("In the rainforest!", "Abre los brazos como árboles.")]

STORY_TITLE = "In the Rainforest"
STORY = [("rainforest", "It is a green rainforest."),
         ("sloth", "It is a brown sloth."),
         ("toucan", "It is a black toucan."),
         ("frog", "It is a green frog."),
         ("jaguar", "It is a yellow jaguar.")]
STORY_QS = [("What color is the sloth?", "/uát KÓ-lor is de slouz/", "Brown."),
            ("What color is the frog?", "/uát KÓ-lor is de frog/", "Green."),
            ("What color is the jaguar?", "/uát KÓ-lor is de YÁ-guar/", "Yellow.")]

LISTEN_PRACTICE = [("It is a frog.", ["frog", "snake", "sloth"], 0),
                   ("It is a toucan.", ["monkey", "toucan", "jaguar"], 1),
                   ("It is a brown monkey.", ["parrot", "frog", "monkey"], 2),
                   ("It is a green parrot.", ["parrot", "sloth", "toucan"], 0)]
READ_PRACTICE = [("sloth", "It is a sloth.", True), ("frog", "It is a snake.", False),
                 ("jaguar", "It is a jaguar.", True), ("toucan", "It is a monkey.", False)]
WRITE_PRACTICE = ["frog", "sloth", "snake", "monkey"]

SPEAK_MODELS = ["What animal is it?", "It is a frog.", "It is a green frog.", "It is a brown sloth.", "It's the rainforest."]
SPEAK_TEST = [("frog", "What animal is it?", "It is a frog. (It is a green frog.)"),
              ("monkey", "What animal is it?", "It is a monkey."),
              ("toucan", "What animal is it?", "It is a toucan."),
              ("sloth", "What color is the sloth?", "It is brown. (It is a brown sloth.)")]
MEDIATION_PRACTICE = ("El niño dibuja y **colorea** su animal favorito de la selva. Luego se lo muestra a un familiar y le dice en inglés "
                      "**It is a green frog.** El familiar pregunta en español \"¿Qué dijiste?\" y el niño lo explica.")

TESTS = {
 "listening": {"skill": "listening", "total": 5,
  "tip": ["Antes de cada número, **miren los 3 dibujos** y digan el nombre de cada animal."],
  "review": "Palabras nuevas (audio 01) y la práctica de escucha (audio 04)",
  "parts": [{"intro": "**Adulto:** ponga el audio. El niño escucha cada número y **toca** (o encierra) el animal correcto. Puede escuchar **dos veces**.",
             "audio": "05",
             "said": ["It is a snake.", "It is a brown sloth.", "It is a green parrot.", "It is a yellow jaguar.", "It is a black toucan."],
             "qs": [
    {"t": "mc", "q": "", "opts": ["@frog", "@monkey", "@snake"], "a": 2, "exp": "*It is a snake.*"},
    {"t": "mc", "q": "", "opts": ["@sloth", "@toucan", "@jaguar"], "a": 0, "exp": "*It is a brown sloth.*"},
    {"t": "mc", "q": "", "opts": ["@monkey", "@parrot", "@frog"], "a": 1, "exp": "*It is a green parrot.*"},
    {"t": "mc", "q": "", "opts": ["@jaguar", "@snake", "@sloth"], "a": 0, "exp": "*It is a yellow jaguar.*"},
    {"t": "mc", "q": "", "opts": ["@parrot", "@frog", "@toucan"], "a": 2, "exp": "*It is a black toucan.*"},
  ]}]},

 "reading": {"skill": "reading", "total": 5,
  "tip": ["Lee la oración **en voz alta** antes de elegir. Busca **el nombre del animal**."],
  "review": "El cuento *In the Rainforest* y la práctica de lectura",
  "parts": [{"intro": "**Adulto:** el niño lee la oración y **toca** el dibujo correcto.", "qs": [
    {"t": "mc", "q": "It is a green frog.", "opts": ["@snake", "@frog", "@parrot"], "a": 1},
    {"t": "mc", "q": "It is a brown monkey.", "opts": ["@monkey", "@sloth", "@jaguar"], "a": 0},
    {"t": "mc", "q": "It is a black toucan.", "opts": ["@parrot", "@monkey", "@toucan"], "a": 2},
   ]},
   {"intro": "**Adulto:** el niño lee y mira el dibujo. ¿Dicen lo mismo? **True** (sí) o **False** (no).", "qs": [
    {"t": "tf", "q": "It is a snake.", "img": "snake", "a": True, "exp": "Es una serpiente."},
    {"t": "tf", "q": "It is a jaguar.", "img": "sloth", "a": False, "exp": "Es un perezoso: *It is a sloth.*"},
   ]}]},

 "writing": {"skill": "writing", "total": 5,
  "tip": ["Escribe el nombre del animal **letra por letra**. Revisa con la página de Palabras nuevas."],
  "review": "La práctica de escritura y la página de Palabras nuevas",
  "parts": [
   {"intro": "**Parte A.** Mira el dibujo y escribe el animal. (1 punto cada una)", "qs": [
    {"t": "short", "q": "It is a ______________.", "img": "frog", "accept": [["frog"]], "show": "**frog**"},
    {"t": "short", "q": "It is a ______________.", "img": "monkey", "accept": [["monkey"]], "show": "**monkey**"},
    {"t": "short", "q": "It is a ______________.", "img": "parrot", "accept": [["parrot"]], "show": "**parrot**"},
   ]},
   {"intro": "**Parte B.** Dibuja y colorea un animal de la selva. Escribe **1 oración**: *It is a* + color + animal. (2 puntos)",
    "note": ["Modelo", "*It is a green frog.*"],
    "open": {"lines": 1, "min_sent": 1, "max_sent": 2, "check_intro": "**Adulto:** marque un punto por cada casilla:",
             "checklist": [
               {"text": "Escribió **It is a** + color + animal.", "auto": r"\bit is a (green|brown|black|yellow|red|blue|orange) (sloth|toucan|monkey|parrot|frog|snake|jaguar)\b"},
               {"text": "Empezó con mayúscula y terminó con punto.", "auto": "caps"}],
             "sample": "It is a red parrot."}},
  ]},

 "speaking": {"skill": "speaking", "total": 5,
  "tip": ["Responda con el niño una vez para practicar. La segunda vez, el niño responde solo."],
  "review": "Audio 06: escucha y repite",
  "parts": [{"intro": "**Adulto:** ponga el audio. El niño mira cada dibujo y responde en voz alta en la pausa.",
             "audio": "07", "pics": [(img, f"Picture {kid.NUMS[i]}") for i, (img, _, _) in enumerate(SPEAK_TEST)],
             "open": {"record": True, "check_intro": "**Adulto:** escuche y marque un punto por cada casilla:", "checklist": [
               {"text": "Picture 1: *It is a frog.*"},
               {"text": "Picture 2: *It is a monkey.*"},
               {"text": "Picture 3: *It is a toucan.*"},
               {"text": "Picture 4: *It is brown.*"},
               {"text": "Respondió en inglés, sin ayuda"}]}}]},

 "mediation": {"skill": "mediation", "total": 4,
  "tip": ["Primero diga la oración en español; después busquen las palabras en inglés."],
  "review": "La práctica de Mediation: mi animal favorito",
  "parts": [
   {"intro": "**Parte A.** Tu abuelo no sabe inglés. Ayúdale: ¿qué significa? Escríbelo **en español**.",
    "note": ["Oración", "*It is a brown monkey.*"],
    "open": {"lines": 1, "min_sent": 0, "max_sent": 0, "checklist": [
      {"text": "Escribió *Es un mono café*."},
      {"text": "Puso el color **después** del animal, como en español."}],
     "sample": "Es un mono café."}},
   {"intro": "**Parte B.** Tu primo dice: *«Es una rana verde»*. Escríbelo **en inglés**.",
    "open": {"lines": 1, "min_sent": 1, "max_sent": 1, "checklist": [
      {"text": "Escribió **It is a green frog**.", "auto": r"\b(it is|it'?s) a green frog\b"},
      {"text": "Empezó con mayúscula y terminó con punto.", "auto": "caps"}],
     "sample": "It is a green frog."}},
  ]},
}

kid.build(globals())
