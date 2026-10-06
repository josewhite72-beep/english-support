# -*- coding: utf-8 -*-
"""3.er grado · Scenario 5, Theme 2 — I Want Five Pineapples.
Fuentes: planeamiento 3_5-2 y módulo GeMA 3_5-2. Marcado: **negrita**, *cursiva*."""
from common import *
from tests_t52 import TESTS

THEME_ID = "5-2"
THEME_TITLE = "I Want Five Pineapples."
SCENARIO = "Scenario 5: Let's Go Shopping!"

NAR, LUI, SEL, ANA = "af_heart", "am_puck", "am_michael", "af_bella"
SPEAKERS = {LUI: "Luis", SEL: "Seller", ANA: "Ana"}

VOCAB = [
    ("seven", "SÉ-ven", "siete", "I have seven bananas."),
    ("eight", "eit", "ocho", "It's eight dollars."),
    ("nine", "nain", "nueve", "I want nine apples."),
    ("ten", "ten", "diez", "It's ten dollars."),
    ("dollar", "DÓ-lar", "dólar, balboa", "One dollar, two dollars."),
    ("money", "MÁ-ni", "dinero", "Here is the money."),
    ("price", "prais", "precio", "What is the price?"),
    ("seller", "SÉ-ler", "vendedor, vendedora", "The seller is friendly."),
    ("fruit stand", "frut stand", "puesto de frutas", "I go to the fruit stand."),
    ("please", "pliis", "por favor", "Can I have a mango, please?"),
    ("thank you", "zenk iu", "gracias", "Thank you!"),
    ("Here you are.", "jiir iu ar", "Aquí tiene.", "Here you are!"),
]

READING = [
    (SEL, "Good morning!"),
    (LUI, "Good morning! Can I have five pineapples, please?"),
    (SEL, "Yes. Here you are."),
    (LUI, "How much is it?"),
    (SEL, "It's ten dollars."),
    (LUI, "Can I have seven bananas, too?"),
    (SEL, "Sure! Seven bananas are two dollars."),
    (LUI, "Here is the money. Thank you!"),
    (SEL, "Thank you! Have a nice day!"),
]

CHANT = [
    "Seven, eight, nine, ten,",
    "Count the money once again!",
    "Can I have five pineapples, please?",
    "Yes, you can! Here you are!",
    "How much is it? Ten dollars, please.",
    "Thank you, thank you! Easy, easy!",
]

DIALOGUE_PRACTICE = [
    (ANA, "Hello! Can I have eight oranges, please?"),
    (SEL, "Yes. Here you are."),
    (ANA, "How much is it?"),
    (SEL, "It's three dollars."),
    (ANA, "And can I have one pineapple?"),
    (SEL, "Sure. The pineapple is two dollars."),
    (ANA, "Here is the money. Thank you!"),
    (SEL, "Thank you!"),
]

TEST_MONOLOGUE = [
    (SEL, "Good afternoon! Can I help you?"),
    (LUI, "Yes, please. Can I have nine apples?"),
    (SEL, "Sure. Here you are. Nine apples are four dollars."),
    (LUI, "And ten bananas, please."),
    (SEL, "Ten bananas are two dollars."),
    (LUI, "OK. Here is the money. Six dollars."),
    (SEL, "Thank you! Have a nice day!"),
]

SPEAK_MODELS = [
    "Seven, eight, nine, ten.",
    "Can I have five pineapples, please?",
    "How much is it?",
    "It's ten dollars.",
    "Here you are.",
    "Thank you!",
]

SPEAK_TEST_Q = [
    "Question one. Count from seven to ten.",
    "Question two. You want bananas. What do you say?",
    "Question three. You want to know the price. What do you ask?",
    "Question four. The seller gives you the fruit. What do you say?",
    "Question five. How much is a mango? Say a price.",
]

TRACKS = [
    {"n": "01", "title": "Vocabulario clave",
     "instr": "Escucha cada palabra y su ejemplo. Repite en voz alta durante la pausa.",
     "segments": vocab_segments(VOCAB)},
    {"n": "02", "title": "Lectura: Luis at the Fruit Stand",
     "instr": "Escucha el diálogo mientras lo sigues con el dedo en tu libro.",
     "segments": [(v, t, 0.8) for v, t in READING]},
    {"n": "03", "title": "Chant: Seven, Eight, Nine, Ten",
     "instr": "Escucha el chant y repítelo. Cuenta con los dedos.",
     "segments": [(NAR, l, 0.6) for l in CHANT]},
    {"n": "04", "title": "Listening — Práctica: Ana Buys Fruit",
     "instr": "Escucha el diálogo dos veces. La primera vez, solo escucha. La segunda vez, responde.",
     "segments": [(v, t, 0.7) for v, t in DIALOGUE_PRACTICE]},
    {"n": "05", "title": "Listening — Mini-test: Apples and Bananas",
     "instr": "Mini-test. Escucha dos veces como máximo y responde en tu libro.",
     "segments": [(v, t, 0.8) for v, t in TEST_MONOLOGUE]},
    {"n": "06", "title": "Speaking — Oraciones modelo",
     "instr": "Escucha cada oración y repítela en la pausa. Después grábate y compara.",
     "segments": [(NAR, s, 3.0) for s in SPEAK_MODELS]},
    {"n": "07", "title": "Speaking — Mini-test (examen oral)",
     "instr": "Prepara una grabadora. Responde cada pregunta en voz alta durante la pausa.",
     "segments": [(NAR, "Speaking test. Answer each question.", 2.0)]
                 + [(NAR, q, 8.0) for q in SPEAK_TEST_Q]},
]

def audio(n):
    t = next(t for t in TRACKS if t["n"] == n)
    return {"t": "audio", "id": f"{THEME_ID}/{n}", "label": f"Audio {THEME_ID.replace('-', '.')}-{n}", "title": t["title"]}

BLOCKS = [
    {"t": "theme_cover", "scenario": SCENARIO, "theme": "Theme 2: " + THEME_TITLE,
     "es": "Quiero cinco piñas.",
     "goals": ["Contar del 7 al 10 en inglés.",
               "Pedir con cortesía: *Can I have five pineapples, **please**?*",
               "Preguntar el precio: ***How much** is it? — It's ten dollars.*"]},

    H1("¿Te sientes perdido? Empieza aquí"),
    P("Si en clase no entendiste el tema, lee esta página primero."),
    H3("1. Las palabras del tema"),
    TABLE([2200, 2700, 2200, 2700], ["Inglés", "Español", "Inglés", "Español"], [
        ["seven", "7", "dollar", "dólar"],
        ["eight", "8", "money", "dinero"],
        ["nine", "9", "price", "precio"],
        ["ten", "10", "seller", "vendedor"],
        ["please", "por favor", "thank you", "gracias"],
    ]),
    H3("2. Para comprar en el puesto de frutas"),
    TABLE([4900, 4900], ["Tú dices", "El vendedor dice"], [
        ["Can I have five pineapples, **please**?", "Yes. **Here you are.**"],
        ["**How much** is it?", "**It's** ten dollars."],
        ["Here is the money. **Thank you!**", "Thank you! Have a nice day!"],
    ]),
    P("Escucha estas palabras en el **Audio 5.2-01**."),
    PB,

    H1("1. Vocabulario"),
    P("Escucha el audio, señala cada palabra y repítela en voz alta. La columna **Se pronuncia** es una ayuda; el audio es la pronunciación correcta."),
    audio("01"),
    TABLE([2100, 1700, 2300, 3700], ["Inglés", "Se pronuncia", "Español", "Ejemplo"],
          [[f"**{w}**", p, s, f"*{ex}*"] for w, p, s, ex in VOCAB]),
    NOTE("Truco", "**thank you** /zenk iu/: empieza con la lengua entre los dientes. **dollar** → **dollars** cuando son más de uno."),
    PB,

    H1("2. Lectura: Luis at the Fruit Stand"),
    P("Lee el diálogo dos veces. La primera vez, junto con el audio. La segunda, en voz alta con alguien de tu familia: tú eres Luis."),
    audio("02"),
    READ("Luis at the Fruit Stand", [f"**{SPEAKERS[v]}:** {t}" for v, t in READING]),
    H2("Chant: Seven, Eight, Nine, Ten"),
    P("Escucha y repite. Cuenta con los dedos."),
    audio("03"),
    POEM(CHANT),
    PB,

    H1("3. Gramática del tema"),
    H2("A. Pedir algo con cortesía"),
    P("***Can I have** + número + fruta, **please**?*  →  *Can I have **nine apples**, please?*"),
    H2("B. Preguntar el precio"),
    TABLE([4900, 4900], ["Pregunta", "Respuesta"], [
        ["**How much** is it?", "**It's** one dollar."],
        ["**How much** is it?", "**It's** ten dollar**s**."],
    ]),
    H2("C. I want"),
    P("*I **want** five pineapples.* = Quiero cinco piñas.  ·  Más amable: *Can I have five pineapples, please?*"),
    NOTE("Errores comunes",
         "✗ It's ten dollar.  ✓ It's ten dollar**s**.",
         "✗ Can I have five pineapples?  →  mejor con **please**: *Can I have five pineapples, **please**?*"),
    PB,

    H1("4. Listening (Escuchar)"),
    H2("Práctica: Ana Buys Fruit"),
    P("Ana compra frutas. **Primera vez:** solo escucha. **Segunda vez:** responde."),
    audio("04"),
    P("**Ejemplo:** Ana wants ______ oranges. → **eight**"),
    ITEMS("1. How much are the oranges?"),
    OPTS("a) two dollars", "b) three dollars", "c) eight dollars"),
    ITEMS("2. Ana wants one ______________."),
    ITEMS("3. How much is the pineapple?"),
    OPTS("a) one dollar", "b) two dollars", "c) three dollars"),
    ITEMS("4. Ana says: \"Thank ______________!\""),
    *test_blocks(TESTS["listening"], audio),
    PB,

    H1("5. Reading (Leer)"),
    H2("Práctica (texto: Luis at the Fruit Stand)"),
    P("**A. Responde con un número.**"),
    P("**Ejemplo:** How many pineapples does Luis want? → **5**"),
    ITEMS("1. How much are the pineapples? ______ dollars", "2. How many bananas does Luis want? ______",
          "3. How much are the bananas? ______ dollars"),
    P("**B. ¿Quién lo dice?** Escribe Luis o Seller."),
    ITEMS("1. \"Here you are.\" ______________", "2. \"How much is it?\" ______________", "3. \"Have a nice day!\" ______________"),
    *test_blocks(TESTS["reading"], audio),
    PB,

    H1("6. Writing (Escribir)"),
    H2("Práctica"),
    P("**A. Escribe el número en inglés.**"),
    ITEMS("1. 7 → ______________", "2. 8 → ______________", "3. 9 → ______________", "4. 10 → ______________"),
    P("**B. Completa el diálogo** con: *please · How much · Here you are · Thank you*"),
    ITEMS("1. Can I have two mangoes, ______________?", "2. Seller: ______________.",
          "3. ______________ is it?", "4. ______________!"),
    P("**C. Mi compra.** En tu cuaderno, escribe un diálogo corto comprando tu fruta favorita."),
    *test_blocks(TESTS["writing"], audio),
    PB,

    H1("7. Speaking (Hablar)"),
    H2("Práctica: escucha, repite y grábate"),
    P("**Paso 1.** Escucha cada oración y repítela en la pausa."),
    P("**Paso 2.** Grábate con un celular."),
    P("**Paso 3.** Escucha tu grabación. ¿Sube tu voz al final de la pregunta *Can I have...?*"),
    audio("06"),
    ITEMS(*[f"{i+1}. {s}" for i, s in enumerate(SPEAK_MODELS)]),
    P("**Juego: \"The Fruit Stand\".** Haz un puesto de frutas en casa con dibujos y precios. Alguien de tu familia compra y tú vendes. Luego cambien."),
    *test_blocks(TESTS["speaking"], audio),
    PB,

    H1("8. Mediation (Ayudar a otros a entender)"),
    P("Mediar es **ayudar a otra persona a entender**: pasar algo del español al inglés, o explicarlo con dibujos."),
    H2("Práctica"),
    P("**A. Carteles de precio.** Dibuja 3 frutas y escribe su precio en inglés: *Mango: one dollar*."),
    P("**B. Explica en español.** ¿Qué dice este cartel?"),
    NOTE("Cartel", "*Pineapples: two dollars. Bananas: ten for one dollar.*"),
    LINES(1),
    *test_blocks(TESTS["mediation"], audio),
    PB,

    H1("¿Cómo me fue en el Tema 5.2?"),
    P("Anota tus puntajes. Te dicen qué repasar."),
    TABLE([2600, 1600, 5600], ["Mini-test", "Puntaje", "Si tuviste menos de la mitad, repasa..."],
          [[SKILL_TITLES[k].split(" ")[-1] if k != "speaking" else "Speaking", f"___ / {t['total']}", t["review"]]
           for k, t in TESTS.items()]),
    TABLE([6400, 1100, 1100, 1200], ["Puedo...", "Sí", "Casi", "Todavía no"], [
        ["contar del 7 al 10 en inglés", "☐", "☐", "☐"],
        ["pedir con *Can I have..., please?*", "☐", "☐", "☐"],
        ["preguntar el precio (*How much is it?*)", "☐", "☐", "☐"],
        ["decir *thank you* y *here you are*", "☐", "☐", "☐"],
    ]),
    PB,

    H1("Respuestas del Tema 5.2"),
    P("Corrige **solo después de terminar**. Lee la explicación de lo que fallaste."),
    H3("Listening — Práctica"),
    ITEMS("1. **b) three dollars.**   2. **pineapple.**   3. **b) two dollars.**   4. **you.** *Thank you!*"),
    *answer_blocks(TESTS["listening"]),
    H3("Reading — Práctica"),
    ITEMS("A1. **10**   A2. **7**   A3. **2**", "B1. **Seller**   B2. **Luis**   B3. **Seller**"),
    *answer_blocks(TESTS["reading"]),
    H3("Writing — Práctica"),
    ITEMS("A1. **seven**   A2. **eight**   A3. **nine**   A4. **ten**",
          "B1. **please**   B2. **Here you are**   B3. **How much**   B4. **Thank you**"),
    *answer_blocks(TESTS["writing"]),
    *answer_blocks(TESTS["mediation"]),
    PB,

    H1("Transcripciones de los audios del Tema 5.2"),
    P("Si no puedes escuchar un audio, pide a alguien que lo lea en voz alta."),
    {"t": "transcripts"},
]
