# -*- coding: utf-8 -*-
"""3.er grado · Scenario 6, Theme 1 — I Can Relax and Listen.
Fuentes: planeamiento 3_6-1 y módulo GeMA 3_6-1. Marcado: **negrita**, *cursiva*."""
from common import *
from tests_t61 import TESTS

THEME_ID = "6-1"
THEME_TITLE = "I Can Relax and Listen."
SCENARIO = "Scenario 6: I Can Connect with Nature!"

NAR, SOF, TOM, LUI = "af_heart", "af_bella", "am_puck", "am_michael"
SPEAKERS = {SOF: "Sofía", TOM: "Tomás", LUI: "Luis"}

VOCAB = [
    ("tree", "tri", "árbol", "I can see a tree."),
    ("grass", "gras", "hierba, grama", "The grass is green."),
    ("flower", "FLÁU-er", "flor", "I can see a flower."),
    ("bird", "berd", "pájaro", "The bird is in the tree."),
    ("leaf", "lif", "hoja", "The leaf is on the grass."),
    ("park", "park", "parque", "I can play in the park."),
    ("trail", "treil", "sendero", "I can walk on the trail."),
    ("sun", "san", "sol", "The sun is in the sky."),
    ("sky", "scai", "cielo", "The sky is blue."),
    ("nature", "NÉI-cher", "naturaleza", "I love nature."),
    ("listen", "LÍ-sen", "escuchar", "I can listen to the bird."),
    ("relax", "ri-LÁX", "relajarse", "I can relax in the park."),
]

READING = [
    "Today is a sunny day. The sun is in the sky. My family is in the park. The park is big and green.",
    "I can see a tree. The tree is tall. A bird is in the tree. The bird can sing. I can listen to the bird.",
    "The grass is under the tree. A flower is on the grass. I can walk on the trail. The trail is near the tree.",
    "I can relax in the park. I love nature. I can listen and relax.",
]

CHANT = [
    "Sun in the sky, bird in the tree,",
    "Flower on the grass, look and see!",
    "I can relax, I can listen too,",
    "I can walk on the trail with you.",
    "Park and nature, leaf and tree,",
    "I love nature, come with me!",
]

DIALOGUE_PRACTICE = [
    (TOM, "Sofía, look! What can you see?"),
    (SOF, "I can see a big tree."),
    (TOM, "Can you see the bird?"),
    (SOF, "Yes, I can. The bird is in the tree."),
    (TOM, "And the flowers?"),
    (SOF, "The flowers are under the tree. They are red."),
    (TOM, "Shh! Listen. The bird can sing!"),
    (SOF, "I can relax here. I love the park."),
]

TEST_MONOLOGUE = [
    "Hi! I'm Luis. I am in the park with my dad.",
    "The sky is blue, and the sun is big.",
    "I can see two birds. The birds are in the tree.",
    "A yellow flower is near the trail.",
    "I can't see the river, but I can listen to the water.",
    "I can relax in the park. I love nature!",
]

SPEAK_MODELS = [
    "I can see a tree.",
    "The bird is in the tree.",
    "The flower is on the grass.",
    "I can listen to the bird.",
    "I can relax in the park.",
    "I love nature.",
]

SPEAK_TEST_Q = [
    "Question one. What can you see in a park?",
    "Question two. Where is the bird?",
    "Question three. What color is the sky?",
    "Question four. Can you listen to the birds at home?",
    "Question five. Where can you relax?",
]

TRACKS = [
    {"n": "01", "title": "Vocabulario clave",
     "instr": "Escucha cada palabra y su ejemplo. Repite en voz alta durante la pausa.",
     "segments": vocab_segments(VOCAB)},
    {"n": "02", "title": "Lectura: A Day in the Park",
     "instr": "Escucha el texto mientras lo sigues con el dedo en tu libro.",
     "segments": [(SOF, p, 1.0) for p in READING]},
    {"n": "03", "title": "Chant: Sun in the Sky",
     "instr": "Escucha el chant y repítelo. Haz gestos con las manos.",
     "segments": [(NAR, l, 0.6) for l in CHANT]},
    {"n": "04", "title": "Listening — Práctica: In the Park",
     "instr": "Escucha el diálogo dos veces. La primera vez, solo escucha. La segunda vez, responde.",
     "segments": [(v, t, 0.7) for v, t in DIALOGUE_PRACTICE]},
    {"n": "05", "title": "Listening — Mini-test: Luis in the Park",
     "instr": "Mini-test. Escucha dos veces como máximo y responde en tu libro.",
     "segments": [(LUI, t, 0.9) for t in TEST_MONOLOGUE]},
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
    {"t": "theme_cover", "scenario": SCENARIO, "theme": "Theme 1: " + THEME_TITLE,
     "es": "Puedo relajarme y escuchar.",
     "goals": ["Nombrar cosas de la naturaleza: *tree, flower, bird, sun, sky...*",
               "Decir lo que puedes hacer: *I **can** see a bird. I **can** listen.*",
               "Decir dónde está algo: *The bird is **in** the tree.*"]},

    H1("¿Te sientes perdido? Empieza aquí"),
    P("Si en clase no entendiste el tema, lee esta página primero."),
    H3("1. Las palabras del tema"),
    TABLE([2200, 2700, 2200, 2700], ["Inglés", "Español", "Inglés", "Español"], [
        ["tree", "árbol", "sun", "sol"],
        ["grass", "grama", "sky", "cielo"],
        ["flower", "flor", "park", "parque"],
        ["bird", "pájaro", "trail", "sendero"],
        ["leaf", "hoja", "nature", "naturaleza"],
    ]),
    H3("2. can = puedo"),
    P("*I **can** see a tree.* (Puedo ver un árbol.)  ·  *I **can't** see the bird.* (No puedo ver el pájaro.)", align="center"),
    H3("3. ¿Dónde está?"),
    TABLE([2400, 2400, 5000], ["Palabra", "Significa", "Ejemplo"], [
        ["**in**", "dentro de, en", "The bird is **in** the tree."],
        ["**on**", "sobre, encima", "The leaf is **on** the grass."],
        ["**under**", "debajo de", "The grass is **under** the tree."],
        ["**near**", "cerca de", "The trail is **near** the tree."],
    ]),
    P("Escucha estas palabras en el **Audio 6.1-01**."),
    PB,

    H1("1. Vocabulario"),
    P("Escucha el audio, señala cada palabra y repítela en voz alta. La columna **Se pronuncia** es una ayuda; el audio es la pronunciación correcta."),
    audio("01"),
    TABLE([2100, 1700, 2300, 3700], ["Inglés", "Se pronuncia", "Español", "Ejemplo"],
          [[f"**{w}**", p, s, f"*{ex}*"] for w, p, s, ex in VOCAB]),
    NOTE("Truco", "**can** suena /kan/ con una **k** fuerte. **sun** suena /san/."),
    PB,

    H1("2. Lectura: A Day in the Park"),
    P("Lee el texto dos veces. La primera vez, junto con el audio. La segunda, tú solo en voz alta."),
    audio("02"),
    READ("A Day in the Park", READING),
    H2("Chant: Sun in the Sky"),
    P("Escucha y repite. Señala arriba para *sky* y abajo para *grass*."),
    audio("03"),
    POEM(CHANT),
    PB,

    H1("3. Gramática del tema"),
    H2("A. can / can't"),
    TABLE([3300, 3300, 3200], ["Puedo", "No puedo", "Pregunta"], [
        ["I **can** see a bird.", "I **can't** see a bird.", "**Can** you see a bird?"],
        ["The bird **can** sing.", "The fish **can't** fly.", "**Can** you relax? — Yes, I **can**."],
    ]),
    H2("B. in, on, under, near"),
    P("*The sun is **in** the sky.* · *The flower is **on** the grass.* · *The grass is **under** the tree.* · *The trail is **near** the tree.*"),
    NOTE("Errores comunes",
         "✗ I can to see.  ✓ I can **see**.     ✗ The bird can sings.  ✓ The bird can **sing**.",
         "✗ The bird in the tree.  ✓ The bird **is** in the tree."),
    PB,

    H1("4. Listening (Escuchar)"),
    H2("Práctica: In the Park"),
    P("Tomás y Sofía están en el parque. **Primera vez:** solo escucha. **Segunda vez:** responde."),
    audio("04"),
    P("**Ejemplo:** Sofía can see a big ______. → **tree**"),
    ITEMS("1. Where is the bird?"),
    OPTS("a) in the tree", "b) on the grass", "c) under the tree"),
    ITEMS("2. The flowers are ______________ the tree."),
    ITEMS("3. What color are the flowers?"),
    OPTS("a) yellow", "b) red", "c) blue"),
    ITEMS("4. The bird can ______________."),
    *test_blocks(TESTS["listening"], audio),
    PB,

    H1("5. Reading (Leer)"),
    H2("Práctica (texto: A Day in the Park)"),
    P("**A. True or False.**"),
    P("**Ejemplo:** The sun is in the sky. → **T**"),
    ITEMS("1. The park is small. ______", "2. The bird can sing. ______", "3. The flower is on the grass. ______"),
    P("**B. Completa:** *tree · grass · trail*"),
    ITEMS("1. The bird is in the ______________.", "2. The leaf is on the ______________.", "3. I can walk on the ______________."),
    *test_blocks(TESTS["reading"], audio),
    PB,

    H1("6. Writing (Escribir)"),
    H2("Práctica"),
    P("**A. Completa con in, on, under o near.** Mira la lectura."),
    P("**Ejemplo:** The sun is ______ the sky. → **in**"),
    ITEMS("1. The bird is ______ the tree.", "2. The flower is ______ the grass.", "3. The grass is ______ the tree.", "4. The trail is ______ the tree."),
    P("**B. Escribe con I can.**"),
    P("**Ejemplo:** see / a bird → **I can see a bird.**"),
    ITEMS("1. see / a flower → ______________________________", "2. listen / to the bird → ______________________________"),
    P("**C. Mi parque.** Dibuja un parque en tu cuaderno y escribe 3 oraciones con *I can see...*"),
    *test_blocks(TESTS["writing"], audio),
    PB,

    H1("7. Speaking (Hablar)"),
    H2("Práctica: escucha, repite y grábate"),
    P("**Paso 1.** Escucha cada oración y repítela en la pausa."),
    P("**Paso 2.** Grábate con un celular."),
    P("**Paso 3.** Escucha tu grabación. ¿Dijiste bien la **k** de *can*?"),
    audio("06"),
    ITEMS(*[f"{i+1}. {s}" for i, s in enumerate(SPEAK_MODELS)]),
    P("**Prepara tu presentación: \"My Nature Page\".** Dibuja un parque y di 3 oraciones: lo que puedes ver y dónde está cada cosa."),
    *test_blocks(TESTS["speaking"], audio),
    PB,

    H1("8. Mediation (Ayudar a otros a entender)"),
    P("Mediar es **ayudar a otra persona a entender**: pasar algo del español al inglés, o explicarlo con dibujos y gestos."),
    H2("Práctica"),
    P("**A. Mímica.** Sin hablar, enséñale a alguien de tu familia: *sun, bird, flower*. Él o ella adivina."),
    P("**B. Explica en español.** ¿Qué dice esta oración?"),
    NOTE("Oración", "*I can see a bird in the tree.*"),
    LINES(1),
    *test_blocks(TESTS["mediation"], audio),
    PB,

    H1("¿Cómo me fue en el Tema 6.1?"),
    P("Anota tus puntajes. Te dicen qué repasar."),
    TABLE([2600, 1600, 5600], ["Mini-test", "Puntaje", "Si tuviste menos de la mitad, repasa..."],
          [[SKILL_TITLES[k].split(" ")[-1] if k != "speaking" else "Speaking", f"___ / {t['total']}", t["review"]]
           for k, t in TESTS.items()]),
    TABLE([6400, 1100, 1100, 1200], ["Puedo...", "Sí", "Casi", "Todavía no"], [
        ["nombrar cosas de la naturaleza", "☐", "☐", "☐"],
        ["decir lo que puedo hacer (*I can...*)", "☐", "☐", "☐"],
        ["usar *in, on, under, near*", "☐", "☐", "☐"],
        ["entender a alguien que describe un parque", "☐", "☐", "☐"],
    ]),
    PB,

    H1("Respuestas del Tema 6.1"),
    P("Corrige **solo después de terminar**. Lee la explicación de lo que fallaste."),
    H3("Listening — Práctica"),
    ITEMS("1. **a) in the tree.**   2. **under.**   3. **b) red.**   4. **sing.**"),
    *answer_blocks(TESTS["listening"]),
    H3("Reading — Práctica"),
    ITEMS("A1. **F.** The park is **big**.   A2. **T.**   A3. **T.**", "B1. **tree**   B2. **grass**   B3. **trail**"),
    *answer_blocks(TESTS["reading"]),
    H3("Writing — Práctica"),
    ITEMS("A1. **in**   A2. **on**   A3. **under**   A4. **near**",
          "B1. **I can see a flower.**   B2. **I can listen to the bird.**"),
    *answer_blocks(TESTS["writing"]),
    *answer_blocks(TESTS["mediation"]),
    PB,

    H1("Transcripciones de los audios del Tema 6.1"),
    P("Si no puedes escuchar un audio, pide a alguien que lo lea en voz alta."),
    {"t": "transcripts"},
]
