# -*- coding: utf-8 -*-
"""4.º · Scenario 5, Theme 2 — I Always Pack Lunch.
Fuentes: planeamiento 4_5-2 y módulo GeMA 4_5-2. Marcado: **negrita**, *cursiva*."""
from common import *
from tests_t52 import TESTS

THEME_ID = "5-2"
THEME_TITLE = "I Always Pack Lunch."
SCENARIO = "Scenario 5: A Trip to the Beach"

NAR, CAR, SOF, ROS = "af_heart", "am_puck", "af_bella", "af_sarah"
SPEAKERS = {CAR: "Carlos", SOF: "Sofía", ROS: "Mrs. Rosa"}

VOCAB = [
    ("lunch", "lanch", "almuerzo", "I eat lunch at school."),
    ("lunchbox", "LÁNCH-box", "lonchera", "My lunchbox is blue."),
    ("sandwich", "SÁND-uich", "sándwich, emparedado", "I sometimes pack a sandwich."),
    ("rice", "rais", "arroz", "I usually eat rice."),
    ("chicken", "CHÍ-quen", "pollo", "Rice and chicken, please."),
    ("fruit", "frut", "fruta", "I always pack fruit."),
    ("water", "UÓ-ter", "agua", "I always drink water."),
    ("juice", "yus", "jugo", "I never pack juice."),
    ("always", "ÓL-ueis", "siempre", "I always pack lunch."),
    ("usually", "IÚ-shua-li", "casi siempre", "She usually eats rice."),
    ("sometimes", "SÁM-taims", "a veces", "I sometimes pack a sandwich."),
    ("never", "NÉ-ver", "nunca", "He never packs juice."),
]

READING = [
    "My name is Carlos. I go to school every day. I always pack lunch in my lunchbox.",
    "I usually pack rice and chicken. I sometimes pack a sandwich. I always pack fruit, like a banana or a mango.",
    "I never pack juice. I always drink water.",
    "My sister never packs lunch. She usually buys lunch at school. What do you pack for lunch?",
]

CHANT = [
    "Always, always, I pack my lunch!",
    "Usually rice and chicken. Munch, munch!",
    "Sometimes a sandwich, always fruit,",
    "Never, never juice. Only water, too!",
    "Do you pack lunch? Yes, I do!",
    "I always pack lunch. How about you?",
]

DIALOGUE_PRACTICE = [
    (SOF, "Carlos, what's in your lunchbox today?"),
    (CAR, "Rice and chicken. I usually eat rice and chicken."),
    (SOF, "Do you always pack fruit?"),
    (CAR, "Yes, I do. Today I have a mango."),
    (SOF, "I sometimes pack a sandwich, but today I have rice and beans."),
    (CAR, "Do you drink juice?"),
    (SOF, "No, I never drink juice at school. I always drink water."),
    (CAR, "Me too!"),
]

TEST_MONOLOGUE = [
    "Hi, I'm Sofía. Let me tell you about my lunch.",
    "I always eat lunch at school at twelve o'clock.",
    "I usually pack rice and beans, and I sometimes pack chicken.",
    "I never pack candy, because it is bad for my teeth.",
    "I always pack fruit. My favorite fruit is pineapple.",
    "My brother Carlos sometimes buys lunch at the school store. What do you usually eat for lunch?",
]

SPEAK_MODELS = [
    "I always pack lunch.",
    "I usually eat rice and chicken.",
    "I sometimes pack a sandwich.",
    "I never drink juice.",
    "She always drinks water.",
    "What do you pack for lunch?",
]

SPEAK_TEST_Q = [
    "Question one. What do you usually eat for lunch?",
    "Question two. What do you always drink?",
    "Question three. What food do you never eat?",
    "Question four. Do you pack lunch for school?",
    "Question five. What does your friend sometimes eat?",
]

TRACKS = [
    {"n": "01", "title": "Vocabulario clave",
     "instr": "Escucha cada palabra y su ejemplo. Repite en voz alta durante la pausa.",
     "segments": vocab_segments(VOCAB)},
    {"n": "02", "title": "Lectura: Carlos and His Lunchbox",
     "instr": "Escucha el texto mientras lo sigues con el dedo en tu libro.",
     "segments": [(CAR, p, 1.0) for p in READING]},
    {"n": "03", "title": "Chant: Always, Always!",
     "instr": "Escucha el chant y repítelo. Marca el ritmo con palmadas.",
     "segments": [(NAR, l, 0.5) for l in CHANT]},
    {"n": "04", "title": "Listening — Práctica: What's in Your Lunchbox?",
     "instr": "Escucha el diálogo dos veces. La primera vez, solo escucha. La segunda vez, responde.",
     "segments": [(v, t, 0.6) for v, t in DIALOGUE_PRACTICE]},
    {"n": "05", "title": "Listening — Mini-test: Sofía's Lunch",
     "instr": "Mini-test. Escucha dos veces como máximo y responde en tu libro.",
     "segments": [(SOF, t, 0.7) for t in TEST_MONOLOGUE]},
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
    {"t": "theme_cover", "scenario": SCENARIO, "theme": "Theme 2: " + THEME_TITLE,
     "es": "Siempre empaco almuerzo.",
     "goals": ["Nombrar comidas y bebidas del almuerzo: *rice, chicken, fruit, water...*",
               "Decir con qué frecuencia: *I **always** / **usually** / **sometimes** / **never** pack...*",
               "Hablar de otra persona: *She **packs** fruit.* (con -s)"]},

    H1("¿Te sientes perdido? Empieza aquí"),
    P("Si en clase no entendiste el tema, lee esta página primero. Aquí está **lo esencial** en una sola hoja."),
    H3("1. Las 10 palabras que más vas a escuchar"),
    TABLE([2200, 2700, 2200, 2700], ["Inglés", "Español", "Inglés", "Español"], [
        ["lunch", "almuerzo", "water", "agua"],
        ["lunchbox", "lonchera", "juice", "jugo"],
        ["sandwich", "sándwich", "rice", "arroz"],
        ["chicken", "pollo", "fruit", "fruta"],
        ["always", "siempre", "never", "nunca"],
    ]),
    H3("2. ¿Con qué frecuencia?"),
    TABLE([2400, 2400, 5000], ["Palabra", "Frecuencia", "Ejemplo"], [
        ["**always**", "100 % siempre", "I **always** pack fruit."],
        ["**usually**", "80 % casi siempre", "I **usually** eat rice."],
        ["**sometimes**", "50 % a veces", "I **sometimes** pack a sandwich."],
        ["**never**", "0 % nunca", "I **never** drink juice."],
    ]),
    H3("3. Dónde va la palabra"),
    P("La palabra de frecuencia va **antes del verbo**:  I **always** pack lunch.  ·  She **never** drinks juice.", align="center"),
    P("Escucha estas palabras en el **Audio 5.2-01** (página de Vocabulario)."),
    PB,

    H1("1. Vocabulario"),
    P("Escucha el audio, señala cada palabra y repítela en voz alta. La columna **Se pronuncia** te da una ayuda aproximada; el audio es la pronunciación correcta."),
    audio("01"),
    TABLE([2100, 1700, 2300, 3700], ["Inglés", "Se pronuncia", "Español", "Ejemplo"],
          [[f"**{w}**", p, s, f"*{ex}*"] for w, p, s, ex in VOCAB]),
    NOTE("Más comidas", "**beans** frijoles · **banana** guineo · **mango** mango · **pineapple** piña · **bread** pan · **candy** dulces · **milk** leche"),
    PB,

    H1("2. Lectura: Carlos and His Lunchbox"),
    P("Lee el texto dos veces. La primera vez, en silencio. La segunda, en voz alta o junto con el audio."),
    audio("02"),
    READ("Carlos and His Lunchbox", READING),
    H2("Chant: Always, Always!"),
    P("Escucha y repite. Marca el ritmo con palmadas."),
    audio("03"),
    POEM(CHANT),
    PB,

    H1("3. Gramática del tema"),
    H2("A. Palabras de frecuencia"),
    P("**always** (siempre) · **usually** (casi siempre) · **sometimes** (a veces) · **never** (nunca). Van **antes del verbo**."),
    TABLE([4900, 4900], ["Con I / you / we / they", "Con he / she (verbo + s)"], [
        ["I **always** pack fruit.", "She **always** pack**s** fruit."],
        ["We **usually** eat rice.", "He **usually** eat**s** rice."],
        ["They **never** drink juice.", "My sister **never** drink**s** juice."],
    ]),
    H2("B. Preguntas"),
    P("*What do you pack for lunch? — I usually pack rice.*  ·  *Do you always pack fruit? — Yes, I **do**. / No, I **don't**.*"),
    NOTE("Errores comunes",
         "✗ I pack always fruit.  ✓ I **always pack** fruit.   (la palabra va antes del verbo)",
         "✗ She never pack juice.  ✓ She never pack**s** juice.   (con she, el verbo lleva -s)",
         "✗ I don't never drink juice.  ✓ I **never** drink juice.   (never ya es negativo)"),
    PB,

    H1("4. Listening (Escuchar)"),
    H2("Práctica: What's in Your Lunchbox?"),
    P("Sofía y Carlos hablan de su almuerzo. **Primera vez:** solo escucha. **Segunda vez:** responde. Si lo necesitas, usa la velocidad lenta."),
    audio("04"),
    P("**Ejemplo:** Carlos has rice and ______ today. → **chicken**"),
    ITEMS("1. Does Carlos always pack fruit?"),
    OPTS("a) Yes, he does.", "b) No, he doesn't.", "c) Sometimes."),
    ITEMS("2. Today Carlos has a ______________."),
    ITEMS("3. What does Sofía have today?"),
    OPTS("a) a sandwich", "b) rice and beans", "c) chicken"),
    ITEMS("4. Sofía ______________ drinks juice at school."),
    ITEMS("5. What do they always drink?  ______________"),
    *test_blocks(TESTS["listening"], audio),
    PB,

    H1("5. Reading (Leer)"),
    H2("Práctica (texto: Carlos and His Lunchbox)"),
    P("**A. Completa con always, usually, sometimes o never** según el texto."),
    P("**Ejemplo:** Carlos ______ pack lunch. → **always**"),
    ITEMS("1. He ______________ packs rice and chicken.", "2. He ______________ packs a sandwich.",
          "3. He ______________ packs juice.", "4. His sister ______________ buys lunch at school."),
    P("**B. True or False.**"),
    ITEMS("1. Carlos always drinks water. ______", "2. His sister always packs lunch. ______"),
    *test_blocks(TESTS["reading"], audio),
    PB,

    H1("6. Writing (Escribir)"),
    H2("Práctica"),
    P("**A. Ordena las palabras.**"),
    P("**Ejemplo:** fruit / always / I / pack → **I always pack fruit.**"),
    ITEMS("1. usually / rice / eat / I  →  ______________________________",
          "2. never / juice / She / drinks  →  ______________________________",
          "3. sometimes / a sandwich / pack / We  →  ______________________________"),
    P("**B. Escribe la forma con -s.**"),
    ITEMS("1. I pack → She ______________", "2. I eat → He ______________", "3. I drink → My sister ______________"),
    P("**C. Mi almuerzo.** En tu cuaderno, escribe 4 oraciones sobre tu almuerzo con *always, usually, sometimes, never*."),
    *test_blocks(TESTS["writing"], audio),
    PB,

    H1("7. Speaking (Hablar)"),
    H2("Práctica: escucha, repite y grábate"),
    P("**Paso 1.** Escucha cada oración y repítela en la pausa."),
    P("**Paso 2.** Graba en un celular las mismas oraciones."),
    P("**Paso 3.** Escucha tu grabación. *usually* tiene 4 sílabas cortas: /IÚ-shua-li/."),
    audio("06"),
    ITEMS(*[f"{i+1}. {s}" for i, s in enumerate(SPEAK_MODELS)]),
    P("**Prepara tu presentación: \"My Lunchbox\".** Dibuja tu lonchera y di 4 oraciones con *always, usually, sometimes, never*."),
    *test_blocks(TESTS["speaking"], audio),
    PB,

    H1("8. Mediation (Ayudar a otros a entender)"),
    P("Mediar es **ayudar a otra persona a entender un mensaje**: lo haces más corto y simple, o lo pasas de un idioma a otro."),
    H2("Práctica"),
    P("**A. Encuesta.** Pregunta a 2 familiares (en español): *¿Qué comes siempre en el almuerzo?* Escribe sus respuestas **en inglés**."),
    P("**Ejemplo:** *Mi papá siempre come arroz.* → *My dad always eats rice.*"),
    LINES(2),
    P("**B. Explica en español.** Tu abuela no entiende este cartel de la cafetería. Escribe en español qué dice."),
    NOTE("Cartel", "*Always wash your hands before lunch. Never throw food on the floor.*"),
    LINES(1),
    *test_blocks(TESTS["mediation"], audio),
    PB,

    H1("¿Cómo me fue en el Tema 5.2?"),
    P("Anota tus puntajes. Te dicen qué repasar antes de una prueba."),
    TABLE([2600, 1600, 5600], ["Mini-test", "Puntaje", "Si tuviste menos de la mitad, repasa..."],
          [[SKILL_TITLES[k].split(" ")[-1] if k != "speaking" else "Speaking", f"___ / {t['total']}", t["review"]]
           for k, t in TESTS.items()]),
    TABLE([6400, 1100, 1100, 1200], ["Puedo...", "Sí", "Casi", "Todavía no"], [
        ["nombrar comidas y bebidas del almuerzo", "☐", "☐", "☐"],
        ["usar *always, usually, sometimes, never*", "☐", "☐", "☐"],
        ["poner la -s con he / she (*She packs*)", "☐", "☐", "☐"],
        ["entender a alguien que habla de su almuerzo", "☐", "☐", "☐"],
        ["pasar respuestas del español al inglés", "☐", "☐", "☐"],
    ]),
    PB,

    H1("Respuestas del Tema 5.2"),
    P("Corrige **solo después de terminar**. Si te equivocaste, lee la explicación: ahí está lo que necesitas aprender."),
    H3("Listening — Práctica"),
    ITEMS("1. **a) Yes, he does.**   2. **mango.**   3. **b) rice and beans.**",
          "4. **never.** *I never drink juice at school.*   5. **water.** *I always drink water. — Me too!*"),
    *answer_blocks(TESTS["listening"]),
    H3("Reading — Práctica"),
    ITEMS("A1. **usually**   A2. **sometimes**   A3. **never**   A4. **usually**",
          "B1. **T.**   B2. **F.** His sister **never** packs lunch."),
    *answer_blocks(TESTS["reading"]),
    H3("Writing — Práctica"),
    ITEMS("A1. **I usually eat rice.**   A2. **She never drinks juice.**   A3. **We sometimes pack a sandwich.**",
          "B1. **packs**   B2. **eats**   B3. **drinks**"),
    *answer_blocks(TESTS["writing"]),
    *answer_blocks(TESTS["mediation"]),
    PB,

    H1("Transcripciones de los audios del Tema 5.2"),
    P("Si no puedes escuchar un audio, pide a alguien que lo lea o léelo tú en voz alta. Úsalas también para revisar lo que no entendiste."),
    {"t": "transcripts"},
]
