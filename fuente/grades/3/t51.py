# -*- coding: utf-8 -*-
"""3.er grado · Scenario 5, Theme 1 — One, Two, Three Bananas!
Fuentes: planeamiento 3_5-1 y módulo GeMA 3_5-1. Marcado: **negrita**, *cursiva*."""
from common import *
from tests_t51 import TESTS

THEME_ID = "5-1"
THEME_TITLE = "One, Two, Three Bananas!"
SCENARIO = "Scenario 5: Let's Go Shopping!"

NAR, ANA, TOM, MOM = "af_heart", "af_bella", "am_puck", "af_sarah"
SPEAKERS = {ANA: "Ana", TOM: "Tomás", MOM: "Mom"}

VOCAB = [
    ("one", "uan", "uno", "I want one mango."),
    ("two", "tu", "dos", "I have two pineapples."),
    ("three", "zri", "tres", "I want three bananas."),
    ("four", "for", "cuatro", "I have four oranges."),
    ("five", "faiv", "cinco", "I have five apples."),
    ("six", "siks", "seis", "I want six bananas."),
    ("banana", "ba-NÁ-na", "guineo, banano", "The banana is yellow."),
    ("apple", "Á-pol", "manzana", "The apple is red."),
    ("orange", "Ó-ranch", "naranja", "I have four oranges."),
    ("pineapple", "PÁIN-a-pol", "piña", "The pineapple is big."),
    ("mango", "MÉN-gou", "mango", "I want one mango."),
    ("basket", "BÁS-quet", "canasta", "I have a big basket."),
]

READING = [
    "My name is Ana. I have a big basket. In my basket, I have fruit.",
    "I have one mango. I have two pineapples. I have three bananas. I have four oranges. I have five apples.",
    "I like bananas. I want six bananas! How many bananas? Six bananas, please!",
]

CHANT = [
    "One, two, three bananas,",
    "Four, five, six apples!",
    "How many oranges?",
    "Count with me: one, two, three!",
    "I want a mango,",
    "Yummy, yummy, yum!",
]

DIALOGUE_PRACTICE = [
    (MOM, "Tomás, let's go to the market. What fruit do you want?"),
    (TOM, "I want bananas!"),
    (MOM, "How many bananas?"),
    (TOM, "Four bananas, please."),
    (MOM, "OK. And apples?"),
    (TOM, "Yes! Two red apples."),
    (MOM, "Do you want a pineapple?"),
    (TOM, "No, thank you. I want one mango."),
]

TEST_MONOLOGUE = [
    "Hi! I'm Sofía. Look at my fruit basket!",
    "I have three yellow bananas.",
    "I have five red apples.",
    "I have two oranges and one big pineapple.",
    "I don't have mangoes. I want four mangoes!",
    "How many fruits do you have?",
]

SPEAK_MODELS = [
    "One, two, three bananas.",
    "I have four oranges.",
    "I want five apples.",
    "How many bananas?",
    "Six bananas, please.",
    "The pineapple is big.",
]

SPEAK_TEST_Q = [
    "Question one. Count from one to six.",
    "Question two. What fruit do you like?",
    "Question three. How many bananas do you want?",
    "Question four. What color is the apple?",
    "Question five. What fruit is big?",
]

TRACKS = [
    {"n": "01", "title": "Vocabulario clave",
     "instr": "Escucha cada palabra y su ejemplo. Repite en voz alta durante la pausa.",
     "segments": vocab_segments(VOCAB)},
    {"n": "02", "title": "Lectura: Ana's Fruit Basket",
     "instr": "Escucha el texto mientras lo sigues con el dedo en tu libro.",
     "segments": [(ANA, p, 1.0) for p in READING]},
    {"n": "03", "title": "Chant: One, Two, Three Bananas",
     "instr": "Escucha el chant y repítelo. Cuenta con los dedos.",
     "segments": [(NAR, l, 0.6) for l in CHANT]},
    {"n": "04", "title": "Listening — Práctica: At the Market",
     "instr": "Escucha el diálogo dos veces. La primera vez, solo escucha. La segunda vez, responde.",
     "segments": [(v, t, 0.7) for v, t in DIALOGUE_PRACTICE]},
    {"n": "05", "title": "Listening — Mini-test: Sofía's Basket",
     "instr": "Mini-test. Escucha dos veces como máximo y responde en tu libro.",
     "segments": [("af_nova", t, 0.9) for t in TEST_MONOLOGUE]},
    {"n": "06", "title": "Speaking — Oraciones modelo",
     "instr": "Escucha cada oración y repítela en la pausa. Después grábate y compara.",
     "segments": [(NAR, s, 3.0) for s in SPEAK_MODELS]},
    {"n": "07", "title": "Speaking — Mini-test (examen oral)",
     "instr": "Prepara una grabadora. Responde cada pregunta en voz alta durante la pausa.",
     "segments": [(NAR, "Speaking test. Answer each question.", 2.0)]
                 + [(NAR, q, 8.0) for q in SPEAK_TEST_Q]},
]
SPEAKERS["af_nova"] = "Sofía"

def audio(n):
    t = next(t for t in TRACKS if t["n"] == n)
    return {"t": "audio", "id": f"{THEME_ID}/{n}", "label": f"Audio {THEME_ID.replace('-', '.')}-{n}", "title": t["title"]}

BLOCKS = [
    {"t": "theme_cover", "scenario": SCENARIO, "theme": "Theme 1: " + THEME_TITLE,
     "es": "¡Uno, dos, tres guineos!",
     "goals": ["Contar del 1 al 6 en inglés.",
               "Nombrar frutas: *banana, apple, orange, pineapple, mango*.",
               "Decir cuántas: *three banana**s***  ·  ***How many** apples? — Five apples.*"]},

    H1("¿Te sientes perdido? Empieza aquí"),
    P("Si en clase no entendiste el tema, lee esta página primero."),
    H3("1. Las palabras del tema"),
    TABLE([2200, 2700, 2200, 2700], ["Inglés", "Español", "Inglés", "Español"], [
        ["one", "1", "banana", "guineo"],
        ["two", "2", "apple", "manzana"],
        ["three", "3", "orange", "naranja"],
        ["four", "4", "pineapple", "piña"],
        ["five / six", "5 / 6", "mango", "mango"],
    ]),
    H3("2. La regla: más de uno lleva -s"),
    TABLE([4900, 4900], ["Uno", "Más de uno"], [
        ["one banana", "three banana**s**"],
        ["one apple", "five apple**s**"],
        ["one mango", "two mango**es**"],
    ]),
    H3("3. La pregunta del tema"),
    P("***How many** bananas? — **Three** bananas.*  (¿Cuántos guineos? — Tres guineos.)", align="center"),
    P("Escucha estas palabras en el **Audio 5.1-01**."),
    PB,

    H1("1. Vocabulario"),
    P("Escucha el audio, señala cada palabra y repítela en voz alta. La columna **Se pronuncia** es una ayuda; el audio es la pronunciación correcta."),
    audio("01"),
    TABLE([2100, 1700, 2300, 3700], ["Inglés", "Se pronuncia", "Español", "Ejemplo"],
          [[f"**{w}**", p, s, f"*{ex}*"] for w, p, s, ex in VOCAB]),
    NOTE("Truco", "En **three** /zri/ pon la lengua entre los dientes, como una **z** suave."),
    PB,

    H1("2. Lectura: Ana's Fruit Basket"),
    P("Lee el texto dos veces. La primera vez, junto con el audio. La segunda, tú solo en voz alta."),
    audio("02"),
    READ("Ana's Fruit Basket", READING),
    H2("Chant: One, Two, Three Bananas"),
    P("Escucha y repite. Cuenta con los dedos."),
    audio("03"),
    POEM(CHANT),
    PB,

    H1("3. Gramática del tema"),
    H2("A. Número + fruta"),
    P("En inglés el **número va primero**: *three bananas* (no *bananas three*)."),
    P("Si hay **más de uno**, agrega **-s**: banana → banana**s** · apple → apple**s** · orange → orange**s**. Mango → mango**es**."),
    H2("B. I have / I want"),
    TABLE([4900, 4900], ["Inglés", "Español"], [
        ["I **have** two apples.", "Yo **tengo** dos manzanas."],
        ["I **want** six bananas.", "Yo **quiero** seis guineos."],
    ]),
    H2("C. How many...?"),
    P("Para preguntar **cuántos**: *How many oranges? — Four oranges.*"),
    NOTE("Errores comunes",
         "✗ three banana  ✓ three banana**s**     ✗ one apples  ✓ one **apple**",
         "✗ bananas three  ✓ **three bananas**"),
    PB,

    H1("4. Listening (Escuchar)"),
    H2("Práctica: At the Market"),
    P("Tomás va al mercado con su mamá. **Primera vez:** solo escucha. **Segunda vez:** responde."),
    audio("04"),
    P("**Ejemplo:** Tomás wants ______. → **bananas**"),
    ITEMS("1. How many bananas?"),
    OPTS("a) two", "b) four", "c) six"),
    ITEMS("2. The apples are ______________."),
    OPTS("a) red", "b) green", "c) yellow"),
    ITEMS("3. Does Tomás want a pineapple?"),
    OPTS("a) Yes.", "b) No."),
    ITEMS("4. Tomás wants one ______________."),
    *test_blocks(TESTS["listening"], audio),
    PB,

    H1("5. Reading (Leer)"),
    H2("Práctica (texto: Ana's Fruit Basket)"),
    P("**A. ¿Cuántas tiene Ana?** Escribe el número."),
    P("**Ejemplo:** mangoes → **1**"),
    ITEMS("1. pineapples → ______", "2. bananas → ______", "3. oranges → ______", "4. apples → ______"),
    P("**B. True or False.**"),
    ITEMS("1. Ana has a small basket. ______", "2. Ana likes bananas. ______"),
    *test_blocks(TESTS["reading"], audio),
    PB,

    H1("6. Writing (Escribir)"),
    H2("Práctica"),
    P("**A. Escribe el número en inglés.**"),
    P("**Ejemplo:** 3 → **three**"),
    ITEMS("1. 1 → ______________", "2. 4 → ______________", "3. 5 → ______________", "4. 6 → ______________"),
    P("**B. Escribe la fruta con -s.**"),
    P("**Ejemplo:** two (banana) → **two bananas**"),
    ITEMS("1. three (apple) → ______________", "2. five (orange) → ______________", "3. two (pineapple) → ______________"),
    P("**C. Mi canasta.** Dibuja tu canasta en el cuaderno y escribe 3 oraciones: *I have...*"),
    *test_blocks(TESTS["writing"], audio),
    PB,

    H1("7. Speaking (Hablar)"),
    H2("Práctica: escucha, repite y grábate"),
    P("**Paso 1.** Escucha cada oración y repítela en la pausa."),
    P("**Paso 2.** Grábate con un celular."),
    P("**Paso 3.** Escucha tu grabación. ¿Dijiste la **-s** al final de *bananas*?"),
    audio("06"),
    ITEMS(*[f"{i+1}. {s}" for i, s in enumerate(SPEAK_MODELS)]),
    P("**Prepara tu presentación: \"My Fruit Basket\".** Dibuja tu canasta y di cuántas frutas tienes: *I have three bananas...*"),
    *test_blocks(TESTS["speaking"], audio),
    PB,

    H1("8. Mediation (Ayudar a otros a entender)"),
    P("Mediar es **ayudar a otra persona a entender**: pasar algo del español al inglés, o explicarlo con dibujos."),
    H2("Práctica"),
    P("**A. Lista del mercado.** Pregunta a tu familia (en español) qué frutas necesitan y escribe la lista **en inglés** con números."),
    P("**Ejemplo:** *tres naranjas* → *three oranges*"),
    LINES(2),
    P("**B. Explica en español.** ¿Qué dice esta nota?"),
    NOTE("Nota", "*Two pineapples and six bananas, please.*"),
    LINES(1),
    *test_blocks(TESTS["mediation"], audio),
    PB,

    H1("¿Cómo me fue en el Tema 5.1?"),
    P("Anota tus puntajes. Te dicen qué repasar."),
    TABLE([2600, 1600, 5600], ["Mini-test", "Puntaje", "Si tuviste menos de la mitad, repasa..."],
          [[SKILL_TITLES[k].split(" ")[-1] if k != "speaking" else "Speaking", f"___ / {t['total']}", t["review"]]
           for k, t in TESTS.items()]),
    TABLE([6400, 1100, 1100, 1200], ["Puedo...", "Sí", "Casi", "Todavía no"], [
        ["contar del 1 al 6 en inglés", "☐", "☐", "☐"],
        ["nombrar 5 frutas", "☐", "☐", "☐"],
        ["poner la -s cuando hay más de uno", "☐", "☐", "☐"],
        ["preguntar *How many...?*", "☐", "☐", "☐"],
    ]),
    PB,

    H1("Respuestas del Tema 5.1"),
    P("Corrige **solo después de terminar**. Lee la explicación de lo que fallaste."),
    H3("Listening — Práctica"),
    ITEMS("1. **b) four.** *Four bananas, please.*   2. **a) red.** *Two red apples.*",
          "3. **b) No.** *No, thank you.*   4. **mango.**"),
    *answer_blocks(TESTS["listening"]),
    H3("Reading — Práctica"),
    ITEMS("A1. **2**   A2. **3**   A3. **4**   A4. **5**",
          "B1. **F.** Ana has a **big** basket.   B2. **T.** *I like bananas.*"),
    *answer_blocks(TESTS["reading"]),
    H3("Writing — Práctica"),
    ITEMS("A1. **one**   A2. **four**   A3. **five**   A4. **six**",
          "B1. **three apples**   B2. **five oranges**   B3. **two pineapples**"),
    *answer_blocks(TESTS["writing"]),
    *answer_blocks(TESTS["mediation"]),
    PB,

    H1("Transcripciones de los audios del Tema 5.1"),
    P("Si no puedes escuchar un audio, pide a alguien que lo lea en voz alta."),
    {"t": "transcripts"},
]
