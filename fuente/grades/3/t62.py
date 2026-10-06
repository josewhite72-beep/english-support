# -*- coding: utf-8 -*-
"""3.er grado · Scenario 6, Theme 2 — I'm Outside. I'm Happy!
Fuentes: planeamiento 3_6-2 y módulo GeMA 3_6-2. Marcado: **negrita**, *cursiva*."""
from common import *
from tests_t62 import TESTS

THEME_ID = "6-2"
THEME_TITLE = "I'm Outside. I'm Happy!"
SCENARIO = "Scenario 6: I Can Connect with Nature!"

NAR, SOF, TOM, LUI = "af_heart", "af_nova", "am_puck", "am_michael"
SPEAKERS = {SOF: "Sofía", TOM: "Tomás", LUI: "Luis"}

VOCAB = [
    ("outside", "áut-SÁID", "afuera, al aire libre", "I'm outside."),
    ("happy", "JÁ-pi", "feliz", "I'm happy in the park."),
    ("sunny", "SÁ-ni", "soleado", "Today is a sunny day."),
    ("family", "FÁ-mi-li", "familia", "I go to the park with my family."),
    ("walk", "uok", "caminar", "We walk on the trail."),
    ("play", "plei", "jugar", "We play on the grass."),
    ("fly", "flai", "volar", "The bird can fly."),
    ("swim", "suim", "nadar", "The fish can swim."),
    ("butterfly", "BÁ-ter-flai", "mariposa", "The butterfly is on the flower."),
    ("fish", "fish", "pez", "The fish is in the river."),
    ("river", "RÍ-ver", "río", "I can see a river."),
    ("free", "fri", "libre", "I'm happy and free!"),
]

READING = [
    "Today is a sunny day. The sun is in the sky. I go to the park with my family.",
    "I can see a big tree. The tree is green. I can see grass under the tree. The grass is green too.",
    "I can see a red flower. A bird is on the tree. The bird can fly. I can see a leaf on the grass. The leaf is small.",
    "We walk on a trail. The trail is long. I am happy in nature. I love the park!",
]

CHANT = [
    "Sun, sun, up in the sky!",
    "Birds can fly, fly, fly so high!",
    "Trees and grass and flowers too,",
    "I can see nature, can you?",
    "Walk the trail, one, two, three,",
    "I am happy, happy and free!",
]

DIALOGUE_PRACTICE = [
    (LUI, "Hi, Sofía! Where are you?"),
    (SOF, "I'm outside. I'm in the garden."),
    (LUI, "Are you happy?"),
    (SOF, "Yes! I'm happy. It's a sunny day."),
    (LUI, "What can you see?"),
    (SOF, "I can see a butterfly. It's on a flower."),
    (LUI, "Can the butterfly fly?"),
    (SOF, "Yes, it can. Look! Now it's in the sky."),
]

TEST_MONOLOGUE = [
    "Hello! I'm Tomás. Today I'm outside with my family.",
    "We are at the river. It's a sunny day.",
    "I can see three fish. The fish are in the river. They can swim.",
    "A butterfly is on my hand! It is yellow.",
    "We walk on the trail, and we play on the grass.",
    "I can't swim in the river. But I'm happy!",
]

SPEAK_MODELS = [
    "I'm outside.",
    "I'm happy.",
    "We walk on the trail.",
    "The bird can fly.",
    "The fish can swim.",
    "I'm happy and free!",
]

SPEAK_TEST_Q = [
    "Question one. Where are you? Are you outside?",
    "Question two. How do you feel in the park?",
    "Question three. Can a bird fly?",
    "Question four. Can a fish walk?",
    "Question five. What do you do in the park with your family?",
]

TRACKS = [
    {"n": "01", "title": "Vocabulario clave",
     "instr": "Escucha cada palabra y su ejemplo. Repite en voz alta durante la pausa.",
     "segments": vocab_segments(VOCAB)},
    {"n": "02", "title": "Lectura: My Happy Day Outside",
     "instr": "Escucha el texto mientras lo sigues con el dedo en tu libro.",
     "segments": [(SOF, p, 1.0) for p in READING]},
    {"n": "03", "title": "Chant: Happy and Free",
     "instr": "Escucha el chant y repítelo. Mueve los brazos como un pájaro.",
     "segments": [(NAR, l, 0.6) for l in CHANT]},
    {"n": "04", "title": "Listening — Práctica: Sofía Is Outside",
     "instr": "Escucha el diálogo dos veces. La primera vez, solo escucha. La segunda vez, responde.",
     "segments": [(v, t, 0.7) for v, t in DIALOGUE_PRACTICE]},
    {"n": "05", "title": "Listening — Mini-test: Tomás at the River",
     "instr": "Mini-test. Escucha dos veces como máximo y responde en tu libro.",
     "segments": [(TOM, t, 0.9) for t in TEST_MONOLOGUE]},
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
     "es": "¡Estoy afuera. Estoy feliz!",
     "goals": ["Decir dónde estás y cómo te sientes: *I'**m** outside. I'**m** happy.*",
               "Decir lo que hacemos: *We **walk** on the trail.*",
               "Decir lo que pueden hacer los animales: *The bird **can** fly.*"]},

    H1("¿Te sientes perdido? Empieza aquí"),
    P("Si en clase no entendiste el tema, lee esta página primero."),
    H3("1. I'm = I am = yo estoy / yo soy"),
    TABLE([3300, 3300, 3200], ["Inglés", "Corto", "Español"], [
        ["I **am** outside.", "I'**m** outside.", "Estoy afuera."],
        ["I **am** happy.", "I'**m** happy.", "Estoy feliz."],
        ["We **are** in the park.", "We'**re** in the park.", "Estamos en el parque."],
    ]),
    H3("2. Lo que hacemos"),
    P("*I **walk**.* (Yo camino.)  ·  *We **play**.* (Nosotros jugamos.)", align="center"),
    H3("3. Los animales pueden..."),
    TABLE([3300, 3300, 3200], ["Animal", "can", "can't"], [
        ["bird (pájaro)", "The bird **can fly**.", "The bird **can't swim**."],
        ["fish (pez)", "The fish **can swim**.", "The fish **can't walk**."],
    ]),
    P("Escucha estas palabras en el **Audio 6.2-01**."),
    PB,

    H1("1. Vocabulario"),
    P("Escucha el audio, señala cada palabra y repítela en voz alta. La columna **Se pronuncia** es una ayuda; el audio es la pronunciación correcta."),
    audio("01"),
    TABLE([2100, 1700, 2300, 3700], ["Inglés", "Se pronuncia", "Español", "Ejemplo"],
          [[f"**{w}**", p, s, f"*{ex}*"] for w, p, s, ex in VOCAB]),
    NOTE("Truco", "**I'm** suena /aim/, como *\"aim\"*. **happy** empieza con una **h** suave, como una **j** suave."),
    PB,

    H1("2. Lectura: My Happy Day Outside"),
    P("Lee el texto dos veces. La primera vez, junto con el audio. La segunda, tú solo en voz alta."),
    audio("02"),
    READ("My Happy Day Outside", READING),
    H2("Chant: Happy and Free"),
    P("Escucha y repite. Mueve los brazos para *fly* y cuenta con los dedos *one, two, three*."),
    audio("03"),
    POEM(CHANT),
    PB,

    H1("3. Gramática del tema"),
    H2("A. I'm + lugar o sentimiento"),
    TABLE([4900, 4900], ["Dónde estoy", "Cómo me siento"], [
        ["I'm **outside**. · I'm **in the park**.", "I'm **happy**. · I'm **free**."],
        ["We're **at the river**.", "We're **happy**."],
    ]),
    H2("B. Lo que hacemos (presente simple)"),
    P("*I **walk** on the trail.* · *We **play** on the grass.* · *I **go** to the park with my family.*"),
    H2("C. can para los animales"),
    P("*The bird **can fly**.* · *The fish **can swim**.* · *The fish **can't walk**.*"),
    NOTE("Errores comunes",
         "✗ I outside.  ✓ I'**m** outside.     ✗ I'm go to the park.  ✓ I **go** to the park.",
         "✗ The fish can swims.  ✓ The fish can **swim**."),
    PB,

    H1("4. Listening (Escuchar)"),
    H2("Práctica: Sofía Is Outside"),
    P("Luis habla con Sofía. **Primera vez:** solo escucha. **Segunda vez:** responde."),
    audio("04"),
    P("**Ejemplo:** Sofía is ______. → **outside**"),
    ITEMS("1. Where is Sofía?"),
    OPTS("a) in the garden", "b) at the river", "c) at school"),
    ITEMS("2. Sofía is ______________. (feliz)"),
    ITEMS("3. What can Sofía see?"),
    OPTS("a) a bird", "b) a fish", "c) a butterfly"),
    ITEMS("4. The butterfly can ______________."),
    *test_blocks(TESTS["listening"], audio),
    PB,

    H1("5. Reading (Leer)"),
    H2("Práctica (texto: My Happy Day Outside)"),
    P("**A. True or False.**"),
    P("**Ejemplo:** Today is a sunny day. → **T**"),
    ITEMS("1. The flower is blue. ______", "2. The bird can fly. ______", "3. The trail is short. ______"),
    P("**B. Completa:** *family · leaf · happy*"),
    ITEMS("1. I go to the park with my ______________.", "2. The ______________ is small.", "3. I am ______________ in nature."),
    *test_blocks(TESTS["reading"], audio),
    PB,

    H1("6. Writing (Escribir)"),
    H2("Práctica"),
    P("**A. Completa con I'm o We.**"),
    P("**Ejemplo:** ______ happy. → **I'm**"),
    ITEMS("1. ______ outside.", "2. ______ walk on the trail.", "3. ______ in the park.", "4. ______ play on the grass."),
    P("**B. ¿Qué puede hacer? Escribe con can.**"),
    P("**Ejemplo:** bird / fly → **The bird can fly.**"),
    ITEMS("1. fish / swim → ______________________________", "2. butterfly / fly → ______________________________"),
    P("**C. Mi día afuera.** Dibuja en tu cuaderno un lugar al aire libre y escribe 3 oraciones con *I'm..., We..., I can see...*"),
    *test_blocks(TESTS["writing"], audio),
    PB,

    H1("7. Speaking (Hablar)"),
    H2("Práctica: escucha, repite y grábate"),
    P("**Paso 1.** Escucha cada oración y repítela en la pausa."),
    P("**Paso 2.** Grábate con un celular."),
    P("**Paso 3.** Escucha tu grabación. ¿Dijiste **I'm** completo (no solo *I*)?"),
    audio("06"),
    ITEMS(*[f"{i+1}. {s}" for i, s in enumerate(SPEAK_MODELS)]),
    P("**Prepara tu presentación: \"My Happy Day Outside\".** Muestra tu dibujo y di 3 oraciones: dónde estás, cómo te sientes y qué puede hacer un animal."),
    *test_blocks(TESTS["speaking"], audio),
    PB,

    H1("8. Mediation (Ayudar a otros a entender)"),
    P("Mediar es **ayudar a otra persona a entender**: pasar algo del español al inglés, o explicarlo con dibujos y gestos."),
    H2("Práctica"),
    P("**A. Caras.** Dibuja una cara feliz y escribe debajo: *I'm happy.* Enséñasela a alguien de tu familia y explícale qué significa."),
    P("**B. Explica en español.** ¿Qué dice esta oración?"),
    NOTE("Oración", "*We walk on the trail. I'm happy outside.*"),
    LINES(1),
    *test_blocks(TESTS["mediation"], audio),
    PB,

    H1("¿Cómo me fue en el Tema 6.2?"),
    P("Anota tus puntajes. Te dicen qué repasar."),
    TABLE([2600, 1600, 5600], ["Mini-test", "Puntaje", "Si tuviste menos de la mitad, repasa..."],
          [[SKILL_TITLES[k].split(" ")[-1] if k != "speaking" else "Speaking", f"___ / {t['total']}", t["review"]]
           for k, t in TESTS.items()]),
    TABLE([6400, 1100, 1100, 1200], ["Puedo...", "Sí", "Casi", "Todavía no"], [
        ["decir dónde estoy y cómo me siento (*I'm...*)", "☐", "☐", "☐"],
        ["decir lo que hacemos (*We walk...*)", "☐", "☐", "☐"],
        ["decir lo que puede hacer un animal (*can*)", "☐", "☐", "☐"],
        ["entender a alguien que habla de un día afuera", "☐", "☐", "☐"],
    ]),
    PB,

    H1("Respuestas del Tema 6.2"),
    P("Corrige **solo después de terminar**. Lee la explicación de lo que fallaste."),
    H3("Listening — Práctica"),
    ITEMS("1. **a) in the garden.**   2. **happy.**   3. **c) a butterfly.**   4. **fly.**"),
    *answer_blocks(TESTS["listening"]),
    H3("Reading — Práctica"),
    ITEMS("A1. **F.** The flower is **red**.   A2. **T.**   A3. **F.** The trail is **long**.", "B1. **family**   B2. **leaf**   B3. **happy**"),
    *answer_blocks(TESTS["reading"]),
    H3("Writing — Práctica"),
    ITEMS("A1. **I'm**   A2. **We**   A3. **I'm**   A4. **We**",
          "B1. **The fish can swim.**   B2. **The butterfly can fly.**"),
    *answer_blocks(TESTS["writing"]),
    *answer_blocks(TESTS["mediation"]),
    PB,

    H1("Transcripciones de los audios del Tema 6.2"),
    P("Si no puedes escuchar un audio, pide a alguien que lo lea en voz alta."),
    {"t": "transcripts"},
]
