# -*- coding: utf-8 -*-
"""2.º grado · Scenario 6, Theme 2 — It's a Slow, Furry Sloth!
Fuentes: planeamiento 2_6-2 y módulo GeMA 2_6-2. Dibujos: OpenMoji (CC BY-SA 4.0) y propios."""
from common import *
import kid

THEME_ID = "6-2"
THEME_NUM = "Theme 2"
THEME_TITLE = "It's a Slow, Furry Sloth!"
THEME_ES = "¡Es un perezoso lento y peludo!"
SCENARIO = "Scenario 6: Discovering Nature's Wonders"

GOALS = ["Entiendo palabras que describen animales: *slow, fast, big, small...*",
         "Describo un animal: *It is a slow sloth.*",
         "Leo una descripción y encuentro el animal.",
         "Escribo una oración sobre un animal."]
FAMILY = ("En este tema su hijo/a aprende a **describir animales** con palabras como **slow** (lento), **fast** (rápido), "
          "**big** (grande), **small** (pequeño), **long** (largo) y **furry** (peludo): **It is a slow sloth.** /it is a slou slouz/")

VOCAB = [
    ("sloth", "slow", "/slou/", "lento", "It is a slow sloth."),
    ("jaguar", "fast", "/fast/", "rápido", "It is a fast jaguar."),
    ("snake", "long", "/long/", "largo", "It is a long snake."),
    ("frog", "small", "/smol/", "pequeño", "It is a small frog."),
    ("tree", "big", "/big/", "grande", "It is a big tree."),
    ("monkey", "furry", "/FÉ-ri/", "peludo", "It is a furry monkey."),
    ("leaf", "leaf", "/lif/", "hoja", "It is a big leaf."),
    ("butterfly", "butterfly", "/BÁ-ter-flai/", "mariposa", "It is a small butterfly."),
]
SOUND = ["**slow, small, snake** empiezan con /s/ **sin \"e\"**: ssss-low, ssss-mall, ssss-nake.",
         "**jaguar** y **jungle** empiezan con un sonido como la **y** de *yo*: /YÁ-guar/, /YÓN-gol/."]

PATTERN = {"rows": [["**It is a**", "**slow**", "**sloth.**"], ["Es un", "perezoso", "lento."]],
           "note": "**Nota para la familia:** la palabra que describe va **antes** del animal: *slow sloth* = perezoso lento. Se pueden usar dos: *a slow, furry sloth* = un perezoso lento y peludo."}

SONG_TITLE = "Slow Sloth, Fast Jaguar"
SONG = [("It is a slow sloth,", "Mueve los brazos muy despacio."),
        ("It is a fast jaguar,", "Corre en tu lugar."),
        ("It is a big jaguar,", "Abre los brazos grande."),
        ("It is a small monkey,", "Hazte pequeño."),
        ("In the rainforest, in the jungle!", "Señala alrededor y aplaude una vez.")]

STORY_TITLE = "Who Lives in the Rainforest?"
STORY = [("rainforest", "It is a big rainforest."),
         ("sloth", "It is a slow, furry sloth."),
         ("jaguar", "It is a fast jaguar."),
         ("snake", "It is a long snake."),
         ("butterfly", "It is a small butterfly.")]
STORY_QS = [("What animal is slow?", "/uát Á-ni-mal is slou/", "The sloth."),
            ("What animal is fast?", "/uát Á-ni-mal is fast/", "The jaguar."),
            ("What animal is long?", "/uát Á-ni-mal is long/", "The snake.")]

LISTEN_PRACTICE = [("It is a slow sloth.", ["sloth", "jaguar", "frog"], 0),
                   ("It is a long snake.", ["monkey", "snake", "butterfly"], 1),
                   ("It is a small frog.", ["toucan", "sloth", "frog"], 2),
                   ("It is a big leaf.", ["leaf", "parrot", "snake"], 0)]
READ_PRACTICE = [("jaguar", "It is a fast jaguar.", True), ("sloth", "It is a fast sloth.", False),
                 ("snake", "It is a long snake.", True), ("butterfly", "It is a big jaguar.", False)]
WRITE_PRACTICE = ["sloth", "snake", "leaf", "butterfly"]

SPEAK_MODELS = ["It is a slow sloth.", "It is a fast jaguar.", "It is a long snake.", "It is a small frog.", "It is a slow, furry sloth!"]
SPEAK_TEST = [("sloth", "Is the sloth slow or fast?", "It is slow. (It is a slow sloth.)"),
              ("jaguar", "Is the jaguar slow or fast?", "It is fast."),
              ("snake", "Is the snake long or small?", "It is long."),
              ("frog", "Is the frog big or small?", "It is small.")]
MEDIATION_PRACTICE = ("Juego **¿Qué animal es?**: el niño describe un animal en inglés (**It is slow and furry.**) y la familia adivina en español "
                      "(\"¡El perezoso!\"). Luego cambian: un familiar describe en español y el niño dice el animal en inglés.")

TESTS = {
 "listening": {"skill": "listening", "total": 5,
  "tip": ["Escucha la **palabra que describe**: *slow, fast, long, small, big*."],
  "review": "Palabras nuevas (audio 01) y la práctica de escucha (audio 04)",
  "parts": [{"intro": "**Adulto:** ponga el audio. El niño escucha cada número y **toca** (o encierra) el dibujo correcto. Puede escuchar **dos veces**.",
             "audio": "05",
             "said": ["It is slow and furry.", "It is fast.", "It is long and green.", "It is small and green. It can jump.", "It is a small butterfly."],
             "qs": [
    {"t": "mc", "q": "", "opts": ["@jaguar", "@sloth", "@snake"], "a": 1, "exp": "*It is slow and furry.* → the sloth"},
    {"t": "mc", "q": "", "opts": ["@jaguar", "@frog", "@leaf"], "a": 0, "exp": "*It is fast.* → the jaguar"},
    {"t": "mc", "q": "", "opts": ["@monkey", "@butterfly", "@snake"], "a": 2, "exp": "*It is long and green.* → the snake"},
    {"t": "mc", "q": "", "opts": ["@frog", "@sloth", "@tree"], "a": 0, "exp": "*It is small and green. It can jump.* → the frog"},
    {"t": "mc", "q": "", "opts": ["@leaf", "@butterfly", "@jaguar"], "a": 1, "exp": "*It is a small butterfly.*"},
  ]}]},

 "reading": {"skill": "reading", "total": 5,
  "tip": ["Lee la oración **en voz alta**. ¿Qué animal es así?"],
  "review": "El cuento *Who Lives in the Rainforest?* y la práctica de lectura",
  "parts": [{"intro": "**Adulto:** el niño lee la oración y **toca** el dibujo correcto.", "qs": [
    {"t": "mc", "q": "It is a slow, furry sloth.", "opts": ["@monkey", "@sloth", "@frog"], "a": 1},
    {"t": "mc", "q": "It is long. It is not small.", "opts": ["@snake", "@butterfly", "@frog"], "a": 0},
    {"t": "mc", "q": "It is a big, fast jaguar.", "opts": ["@parrot", "@sloth", "@jaguar"], "a": 2},
   ]},
   {"intro": "**Adulto:** el niño lee y mira el dibujo. ¿Es verdad? **True** (sí) o **False** (no).", "qs": [
    {"t": "tf", "q": "It is a small frog.", "img": "frog", "a": True, "exp": "La rana es pequeña."},
    {"t": "tf", "q": "It is a fast animal.", "img": "sloth", "a": False, "exp": "El perezoso es **lento**: *It is a slow animal.*"},
   ]}]},

 "writing": {"skill": "writing", "total": 5,
  "tip": ["Mira el dibujo y piensa: ¿cómo es? **slow, fast, long, small, big**."],
  "review": "La práctica de escritura y la página de Palabras nuevas",
  "parts": [
   {"intro": "**Parte A.** Completa con **slow, fast** o **long**. (1 punto cada una)", "qs": [
    {"t": "short", "q": "It is a ______________ sloth.", "img": "sloth", "accept": [["slow"]], "show": "**slow**"},
    {"t": "short", "q": "It is a ______________ jaguar.", "img": "jaguar", "accept": [["fast"]], "show": "**fast**"},
    {"t": "short", "q": "It is a ______________ snake.", "img": "snake", "accept": [["long"]], "show": "**long**"},
   ]},
   {"intro": "**Parte B.** Dibuja un animal de la selva. Escribe **1 oración** que lo describa. (2 puntos)",
    "note": ["Modelo", "*It is a small, green frog.*"],
    "open": {"lines": 1, "min_sent": 1, "max_sent": 2, "check_intro": "**Adulto:** marque un punto por cada casilla:",
             "checklist": [
               {"text": "Usó una palabra que describe (*slow, fast, big, small, long, furry*).", "auto": r"\b(slow|fast|big|small|long|furry)\b"},
               {"text": "Empezó con mayúscula y terminó con punto.", "auto": "caps"}],
             "sample": "It is a big, fast jaguar."}},
  ]},

 "speaking": {"skill": "speaking", "total": 5,
  "tip": ["Responda con el niño una vez para practicar. La segunda vez, el niño responde solo."],
  "review": "Audio 06: escucha y repite",
  "parts": [{"intro": "**Adulto:** ponga el audio. El niño mira cada dibujo y responde en voz alta en la pausa.",
             "audio": "07", "pics": [(img, f"Picture {kid.NUMS[i]}") for i, (img, _, _) in enumerate(SPEAK_TEST)],
             "open": {"record": True, "check_intro": "**Adulto:** escuche y marque un punto por cada casilla:", "checklist": [
               {"text": "Picture 1: *It is slow.*"},
               {"text": "Picture 2: *It is fast.*"},
               {"text": "Picture 3: *It is long.*"},
               {"text": "Picture 4: *It is small.*"},
               {"text": "Respondió en inglés, sin ayuda"}]}}]},

 "mediation": {"skill": "mediation", "total": 4,
  "tip": ["Primero diga la oración en español; después busquen las palabras en inglés."],
  "review": "La práctica de Mediation: el juego ¿Qué animal es?",
  "parts": [
   {"intro": "**Parte A.** Tu mamá quiere saber qué dice el libro. Escríbelo **en español**.",
    "note": ["Oración", "*It is a slow, furry sloth.*"],
    "open": {"lines": 1, "min_sent": 0, "max_sent": 0, "checklist": [
      {"text": "Escribió *perezoso*."},
      {"text": "Escribió *lento* y *peludo*."}],
     "sample": "Es un perezoso lento y peludo."}},
   {"intro": "**Parte B.** Tu primita dice: *«Es una serpiente larga»*. Escríbelo **en inglés**.",
    "open": {"lines": 1, "min_sent": 1, "max_sent": 1, "checklist": [
      {"text": "Escribió **It is a long snake**.", "auto": r"\b(it is|it'?s) a long snake\b"},
      {"text": "Empezó con mayúscula y terminó con punto.", "auto": "caps"}],
     "sample": "It is a long snake."}},
  ]},
}

kid.build(globals())
