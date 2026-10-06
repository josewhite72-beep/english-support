# -*- coding: utf-8 -*-
"""4.º · Scenario 5, Theme 1 — Let's Pack for a Trip.
Fuentes: planeamiento 4_5-1 y módulo GeMA 4_5-1. Marcado: **negrita**, *cursiva*."""
from common import *
from tests_t51 import TESTS

THEME_ID = "5-1"
THEME_TITLE = "Let's Pack for a Trip."
SCENARIO = "Scenario 5: A Trip to the Beach"

NAR, SOF, MOM, CAR, DAD = "af_heart", "af_bella", "af_sarah", "am_puck", "am_michael"
SPEAKERS = {SOF: "Sofía", MOM: "Mom", CAR: "Carlos", DAD: "Dad"}

VOCAB = [
    ("trip", "trip", "viaje, paseo", "We are going on a trip."),
    ("beach", "bich", "playa", "The beach is beautiful."),
    ("pack", "pak", "empacar", "Pack your bag."),
    ("suitcase", "SÚT-queis", "maleta", "My suitcase is big."),
    ("towel", "TÁU-el", "toalla", "Pack your towel."),
    ("sunscreen", "SÁN-scrin", "bloqueador solar", "Don't forget the sunscreen."),
    ("hat", "jat", "sombrero, gorra", "I'm going to pack my hat."),
    ("swimsuit", "SUÍM-sut", "vestido de baño", "Pack your swimsuit."),
    ("sandals", "SÁN-dols", "sandalias", "I have blue sandals."),
    ("umbrella", "am-BRÉ-la", "sombrilla", "Dad is going to pack the umbrella."),
    ("bucket", "BÁ-quet", "balde, cubeta", "I play with my bucket in the sand."),
    ("shell", "shel", "concha", "I'm going to find a shell."),
]

READING = [
    "Tomorrow, my family is going to go on a trip to the beach. Today, we are going to pack.",
    "Mom says, \"Pack your swimsuit and your towel.\" I am going to pack my hat and my sandals in my suitcase.",
    "My brother is going to pack a bucket for the sand. Dad is going to pack the big umbrella and the sunscreen.",
    "Mom says, \"Don't forget the map!\" We are going to have a great trip!",
]

CHANT = [
    "Pack, pack, pack your bag,",
    "Pack your towel and your hat!",
    "Sunscreen, sandals, swimsuit too,",
    "Let's go to the beach, me and you!",
    "Don't forget the map today,",
    "We're going on a trip. Hooray!",
]

DIALOGUE_PRACTICE = [
    (MOM, "Carlos, we're going to the beach tomorrow. Pack your bag, please."),
    (CAR, "OK, Mom! I'm going to pack my swimsuit."),
    (MOM, "Good. Pack your towel, too."),
    (CAR, "And my red hat!"),
    (MOM, "Yes. Don't forget the sunscreen."),
    (CAR, "Can I take my bucket?"),
    (MOM, "Yes, you can. And don't pack your shoes. Pack your sandals."),
    (CAR, "OK! I'm ready!"),
]

TEST_MONOLOGUE = [
    "Hello, kids! This is Dad. Listen, please.",
    "On Saturday, we are going to go to Coronado beach.",
    "We are going to leave at seven o'clock in the morning.",
    "Sofía, pack your swimsuit and your towel. Carlos, pack your hat and your bucket.",
    "Mom is going to pack the sandwiches and the water.",
    "I'm going to pack the big umbrella. Don't forget the sunscreen!",
]

SPEAK_MODELS = [
    "Pack your towel.",
    "Don't forget the sunscreen.",
    "I'm going to pack my hat.",
    "She's going to pack her swimsuit.",
    "We're going to go to the beach.",
    "What are you going to pack?",
]

SPEAK_TEST_Q = [
    "Question one. Where are you going to go on vacation?",
    "Question two. What are you going to pack?",
    "Question three. Give an instruction to your friend. Start with: Pack.",
    "Question four. What do you never forget for the beach?",
    "Question five. Who is going to go with you?",
]

TRACKS = [
    {"n": "01", "title": "Vocabulario clave",
     "instr": "Escucha cada palabra y su ejemplo. Repite en voz alta durante la pausa.",
     "segments": vocab_segments(VOCAB)},
    {"n": "02", "title": "Lectura: The Family Trip",
     "instr": "Escucha el texto mientras lo sigues con el dedo en tu libro.",
     "segments": [(SOF, p, 1.0) for p in READING]},
    {"n": "03", "title": "Chant: Pack Your Bag",
     "instr": "Escucha el chant y repítelo. Marca el ritmo con palmadas.",
     "segments": [(NAR, l, 0.5) for l in CHANT]},
    {"n": "04", "title": "Listening — Práctica: Carlos Packs His Bag",
     "instr": "Escucha el diálogo dos veces. La primera vez, solo escucha. La segunda vez, responde.",
     "segments": [(v, t, 0.6) for v, t in DIALOGUE_PRACTICE]},
    {"n": "05", "title": "Listening — Mini-test: Dad's Plan",
     "instr": "Mini-test. Escucha dos veces como máximo y responde en tu libro.",
     "segments": [(DAD, t, 0.7) for t in TEST_MONOLOGUE]},
    {"n": "06", "title": "Speaking — Oraciones modelo",
     "instr": "Escucha cada oración y repítela en la pausa. Después grábate y compara.",
     "segments": [(NAR, s, 3.0) for s in SPEAK_MODELS]},
    {"n": "07", "title": "Speaking — Mini-test (examen oral)",
     "instr": "Prepara una grabadora. Responde cada pregunta en voz alta durante la pausa.",
     "segments": [(NAR, "Speaking test. Answer each question with a complete sentence.", 2.0)]
                 + [(NAR, q, 9.0) for q in SPEAK_TEST_Q]},
]

def audio(n):
    t = next(t for t in TRACKS if t["n"] == n)
    return {"t": "audio", "id": f"{THEME_ID}/{n}", "label": f"Audio {THEME_ID.replace('-', '.')}-{n}", "title": t["title"]}

BLOCKS = [
    {"t": "theme_cover", "scenario": SCENARIO, "theme": "Theme 1: " + THEME_TITLE,
     "es": "¡Empaquemos para un viaje!",
     "goals": ["Nombrar lo que llevas a la playa: *towel, hat, sunscreen, swimsuit...*",
               "Dar instrucciones: ***Pack** your towel.* · ***Don't forget** the map.*",
               "Decir planes: *I'm **going to** pack my hat.*"]},

    H1("¿Te sientes perdido? Empieza aquí"),
    P("Si en clase no entendiste el tema, lee esta página primero. Aquí está **lo esencial** en una sola hoja."),
    H3("1. Las 10 palabras que más vas a escuchar"),
    TABLE([2200, 2700, 2200, 2700], ["Inglés", "Español", "Inglés", "Español"], [
        ["trip", "viaje", "sunscreen", "bloqueador"],
        ["beach", "playa", "hat", "sombrero"],
        ["pack", "empacar", "swimsuit", "vestido de baño"],
        ["suitcase", "maleta", "sandals", "sandalias"],
        ["towel", "toalla", "umbrella", "sombrilla"],
    ]),
    H3("2. Instrucciones"),
    P("Empiezan con el **verbo**:  ***Pack** your towel.*  ·  Para decir que **no**: ***Don't** forget the map.*", align="center"),
    H3("3. Planes con going to"),
    TABLE([4900, 4900], ["Inglés", "Español"], [
        ["I'**m going to** pack my hat.", "Voy a empacar mi sombrero."],
        ["She'**s going to** pack a towel.", "Ella va a empacar una toalla."],
        ["We'**re going to** go to the beach.", "Vamos a ir a la playa."],
    ]),
    P("Escucha estas palabras en el **Audio 5.1-01** (página de Vocabulario)."),
    PB,

    H1("1. Vocabulario"),
    P("Escucha el audio, señala cada palabra y repítela en voz alta. La columna **Se pronuncia** te da una ayuda aproximada; el audio es la pronunciación correcta."),
    audio("01"),
    TABLE([2100, 1700, 2300, 3700], ["Inglés", "Se pronuncia", "Español", "Ejemplo"],
          [[f"**{w}**", p, s, f"*{ex}*"] for w, p, s, ex in VOCAB]),
    NOTE("Más palabras de la playa", "**sand** arena · **wave** ola · **sun** sol · **picnic** comida al aire libre · **map** mapa · **sea** mar"),
    PB,

    H1("2. Lectura: The Family Trip"),
    P("Lee el texto dos veces. La primera vez, en silencio. La segunda, en voz alta o junto con el audio."),
    audio("02"),
    READ("The Family Trip", READING),
    H2("Chant: Pack Your Bag"),
    P("Escucha y repite. Marca el ritmo con palmadas."),
    audio("03"),
    POEM(CHANT),
    PB,

    H1("3. Gramática del tema"),
    H2("A. Instrucciones (imperativo)"),
    P("Para decirle a alguien qué hacer, **empieza con el verbo**. Sin *you*."),
    TABLE([4900, 4900], ["Haz esto", "No hagas esto"], [
        ["**Pack** your swimsuit.", "**Don't forget** the sunscreen."],
        ["**Bring** your towel, please.", "**Don't pack** your shoes."],
        ["**Put** on your hat.", "**Don't swim** alone."],
    ]),
    H2("B. Planes con going to"),
    TABLE([3300, 3300, 3200], ["Afirmativa", "Negativa", "Pregunta"], [
        ["I'**m going to** pack.", "I'**m not going to** pack.", "**Are** you **going to** swim?"],
        ["He / She'**s going to** pack.", "She **isn't going to** swim.", "**Is** he **going to** come?"],
        ["We / They'**re going to** go.", "They **aren't going to** go.", "**What are** you **going to** pack?"],
    ]),
    NOTE("Errores comunes",
         "✗ I going to pack.  ✓ I'**m** going to pack.   (falta *am*)",
         "✗ You pack your towel.  ✓ **Pack** your towel.   (la instrucción empieza con el verbo)",
         "✗ No forget the map.  ✓ **Don't** forget the map."),
    PB,

    H1("4. Listening (Escuchar)"),
    H2("Práctica: Carlos Packs His Bag"),
    P("Mamá ayuda a Carlos a empacar. **Primera vez:** solo escucha. **Segunda vez:** responde. Si lo necesitas, usa la velocidad lenta."),
    audio("04"),
    P("**Ejemplo:** They are going to the ______ tomorrow. → **beach**"),
    ITEMS("1. Carlos is going to pack his ______________ first."),
    ITEMS("2. What color is his hat?"),
    OPTS("a) blue", "b) red", "c) yellow"),
    ITEMS("3. Mom says: \"Don't forget the ______________.\""),
    ITEMS("4. Can Carlos take his bucket?"),
    OPTS("a) Yes, he can.", "b) No, he can't.", "c) Mom doesn't know."),
    ITEMS("5. Carlos is going to pack his ______________, not his shoes."),
    *test_blocks(TESTS["listening"], audio),
    PB,

    H1("5. Reading (Leer)"),
    H2("Práctica (texto: The Family Trip)"),
    P("**A. True or False.** Escribe T o F."),
    P("**Ejemplo:** The family is going to the beach. → **T**"),
    ITEMS("1. They are going to go on the trip today. ______", "2. Sofía is going to pack her hat. ______",
          "3. Dad is going to pack the bucket. ______", "4. Mom says: \"Don't forget the map!\" ______"),
    P("**B. ¿Quién lo va a empacar?** Une con una línea o escribe la letra."),
    TABLE([5600, 4200], ["Cosa", "Persona"], [
        ["1. the hat and the sandals  ___", "a) Dad"],
        ["2. the bucket  ___", "b) Sofía (I)"],
        ["3. the umbrella and the sunscreen  ___", "c) the brother"],
    ]),
    *test_blocks(TESTS["reading"], audio),
    PB,

    H1("6. Writing (Escribir)"),
    H2("Práctica"),
    P("**A. Escribe una instrucción** con la palabra entre paréntesis."),
    P("**Ejemplo:** (pack / towel) → **Pack your towel.**"),
    ITEMS("1. (pack / swimsuit) → ______________________________", "2. (don't forget / hat) → ______________________________",
          "3. (bring / sunscreen) → ______________________________"),
    P("**B. Completa con am, is o are.**"),
    P("**Ejemplo:** I ______ going to pack my sandals. → **am**"),
    ITEMS("1. She ______ going to pack a towel.", "2. We ______ going to go to the beach.", "3. Dad ______ going to pack the umbrella."),
    P("**C. Mi lista.** En tu cuaderno, escribe 4 cosas que **vas a empacar** para la playa: *I'm going to pack my...*"),
    *test_blocks(TESTS["writing"], audio),
    PB,

    H1("7. Speaking (Hablar)"),
    H2("Práctica: escucha, repite y grábate"),
    P("**Paso 1.** Escucha cada oración y repítela en la pausa."),
    P("**Paso 2.** Graba en un celular las mismas oraciones."),
    P("**Paso 3.** Escucha tu grabación. En *beach* la **ea** suena como una **i** larga: /bich/."),
    audio("06"),
    ITEMS(*[f"{i+1}. {s}" for i, s in enumerate(SPEAK_MODELS)]),
    P("**Prepara tu presentación: \"My Beach Bag\".** Dibuja tu maleta y di 4 cosas que vas a empacar (*I'm going to pack...*) y una instrucción para tu familia (*Don't forget...*)."),
    *test_blocks(TESTS["speaking"], audio),
    PB,

    H1("8. Mediation (Ayudar a otros a entender)"),
    P("Mediar es **ayudar a otra persona a entender un mensaje**: lo haces más corto y simple, o lo pasas de un idioma a otro."),
    H2("Práctica"),
    P("**A. Lista con dibujos.** Haz en tu cuaderno una lista de 5 cosas para la playa con un **dibujo** y la **palabra en inglés** al lado."),
    P("**B. Explica en español.** Tu hermanito no entiende esta nota. Escribe en español qué dice."),
    NOTE("Nota", "*Pack your swimsuit and your towel. Don't forget your hat!*"),
    LINES(1),
    *test_blocks(TESTS["mediation"], audio),
    PB,

    H1("¿Cómo me fue en el Tema 5.1?"),
    P("Anota tus puntajes. Te dicen qué repasar antes de una prueba."),
    TABLE([2600, 1600, 5600], ["Mini-test", "Puntaje", "Si tuviste menos de la mitad, repasa..."],
          [[SKILL_TITLES[k].split(" ")[-1] if k != "speaking" else "Speaking", f"___ / {t['total']}", t["review"]]
           for k, t in TESTS.items()]),
    TABLE([6400, 1100, 1100, 1200], ["Puedo...", "Sí", "Casi", "Todavía no"], [
        ["nombrar cosas para la playa", "☐", "☐", "☐"],
        ["dar instrucciones (*Pack... / Don't forget...*)", "☐", "☐", "☐"],
        ["decir planes con *going to*", "☐", "☐", "☐"],
        ["entender instrucciones habladas", "☐", "☐", "☐"],
        ["explicar una nota en español", "☐", "☐", "☐"],
    ]),
    PB,

    H1("Respuestas del Tema 5.1"),
    P("Corrige **solo después de terminar**. Si te equivocaste, lee la explicación: ahí está lo que necesitas aprender."),
    H3("Listening — Práctica"),
    ITEMS("1. **swimsuit.** *I'm going to pack my swimsuit.*", "2. **b) red.** *And my red hat!*",
          "3. **sunscreen.**   4. **a) Yes, he can.**   5. **sandals.** *Don't pack your shoes. Pack your sandals.*"),
    *answer_blocks(TESTS["listening"]),
    H3("Reading — Práctica"),
    ITEMS("A1. **F.** They are going to go **tomorrow**. Hoy van a empacar.   A2. **T.**",
          "A3. **F.** Dad is going to pack the **umbrella and the sunscreen**. El hermano lleva el balde.   A4. **T.**",
          "B. 1-b · 2-c · 3-a"),
    *answer_blocks(TESTS["reading"]),
    H3("Writing — Práctica"),
    ITEMS("A1. **Pack your swimsuit.**   A2. **Don't forget your hat.**   A3. **Bring your sunscreen.**",
          "B1. **is**   B2. **are**   B3. **is**",
          "C. Ejemplo: *I'm going to pack my towel. I'm going to pack my hat...*"),
    *answer_blocks(TESTS["writing"]),
    *answer_blocks(TESTS["mediation"]),
    PB,

    H1("Transcripciones de los audios del Tema 5.1"),
    P("Si no puedes escuchar un audio, pide a alguien que lo lea o léelo tú en voz alta. Úsalas también para revisar lo que no entendiste."),
    {"t": "transcripts"},
]
