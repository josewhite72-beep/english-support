# -*- coding: utf-8 -*-
"""4.º · Scenario 6, Theme 1 — Where's the Puddle?
Fuentes: planeamiento 4_6-1 y módulo GeMA 4_6-1. Marcado: **negrita**, *cursiva*."""
from common import *
from tests_t61 import TESTS

THEME_ID = "6-1"
THEME_TITLE = "Where's the Puddle?"
SCENARIO = "Scenario 6: It's the Rainy Season"

NAR, CAR, ANA, DAD = "af_heart", "am_puck", "af_bella", "am_michael"
SPEAKERS = {CAR: "Carlos", ANA: "Ana", DAD: "Dad"}

VOCAB = [
    ("puddle", "PÁ-dol", "charco", "The puddle is big."),
    ("rain", "rein", "lluvia; llover", "The rain is cold."),
    ("cloud", "claud", "nube", "The cloud is gray."),
    ("sky", "scai", "cielo", "The sky is dark."),
    ("storm", "storm", "tormenta", "The storm is here."),
    ("lightning", "LÁIT-ning", "relámpago", "I see lightning."),
    ("thunder", "ZÁN-der", "trueno", "I hear thunder."),
    ("umbrella", "am-BRÉ-la", "paraguas", "I have an umbrella."),
    ("raincoat", "RÉIN-cout", "impermeable", "She wears a raincoat."),
    ("boots", "buts", "botas", "He wears boots."),
    ("wet", "uet", "mojado", "The boots are wet."),
    ("jump", "yamp", "saltar", "Ana is jumping in the puddle."),
]

READING = [
    "Today the sky is dark. A big cloud is in the sky. The rain is here. It is a storm. I see lightning. I hear thunder.",
    "My sister Ana has an umbrella. She wears a raincoat. She wears boots. The boots are wet. I wear sandals. My sandals are wet too.",
    "Ana says: \"Where's the puddle?\" I look and I see a big puddle. The puddle is near the door.",
    "Ana jumps in the puddle. She is happy. I jump in the puddle too. We are happy in the rain.",
]

CHANT = [
    "Rain, rain, in the sky,",
    "Cloud and thunder, say goodbye!",
    "Boots and raincoat, wet and gray,",
    "Where's the puddle? Let's go play!",
    "Lightning, lightning, in the storm,",
    "Umbrella, umbrella, keep me warm!",
]

DIALOGUE_PRACTICE = [
    (ANA, "Carlos, look outside! It's raining."),
    (CAR, "Wow! The sky is very dark. What is Dad doing?"),
    (ANA, "He's closing the windows."),
    (CAR, "Where's my umbrella?"),
    (ANA, "It's under the table."),
    (CAR, "Thanks! Where's the puddle? I want to jump!"),
    (ANA, "It's next to the tree. But Mom is calling us. We are eating lunch now."),
    (CAR, "OK. I'm coming!"),
]

TEST_MONOLOGUE = [
    "Hi! I'm Carlos. It's a rainy day today, and I'm at home.",
    "Right now, I'm looking out the window. The sky is gray, and it's raining a lot.",
    "My sister Ana is wearing her yellow raincoat and her red boots. She's jumping in a big puddle!",
    "My dad is reading a book in the living room.",
    "My mom is cooking soup in the kitchen.",
    "And my dog? He's sleeping under the bed, because he doesn't like thunder!",
]

SPEAK_MODELS = [
    "It's raining today.",
    "Where's the puddle?",
    "The puddle is near the door.",
    "She is wearing a raincoat.",
    "I am jumping in the puddle.",
    "I see lightning and I hear thunder.",
]

SPEAK_TEST_Q = [
    "Question one. What is the weather like today?",
    "Question two. What are you wearing right now?",
    "Question three. What are you doing right now?",
    "Question four. What do you wear in the rain?",
    "Question five. Look at your house. Where is your bed?",
]

TRACKS = [
    {"n": "01", "title": "Vocabulario clave",
     "instr": "Escucha cada palabra y su ejemplo. Repite en voz alta durante la pausa.",
     "segments": vocab_segments(VOCAB)},
    {"n": "02", "title": "Lectura: Where's the Puddle?",
     "instr": "Escucha el texto mientras lo sigues con el dedo en tu libro.",
     "segments": [(CAR, p, 1.0) for p in READING]},
    {"n": "03", "title": "Chant: Rain, Rain!",
     "instr": "Escucha el chant y repítelo. Marca el ritmo con palmadas.",
     "segments": [(NAR, l, 0.5) for l in CHANT]},
    {"n": "04", "title": "Listening — Práctica: It's Raining!",
     "instr": "Escucha el diálogo dos veces. La primera vez, solo escucha. La segunda vez, responde.",
     "segments": [(v, t, 0.6) for v, t in DIALOGUE_PRACTICE]},
    {"n": "05", "title": "Listening — Mini-test: A Rainy Day at Home",
     "instr": "Mini-test. Escucha dos veces como máximo y responde en tu libro.",
     "segments": [(CAR, t, 0.7) for t in TEST_MONOLOGUE]},
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
     "es": "¿Dónde está el charco?",
     "goals": ["Nombrar cosas de la lluvia: *rain, cloud, storm, puddle, umbrella...*",
               "Decir lo que pasa **ahora**: *It **is raining**. She **is jumping**.*",
               "Preguntar con *Where, What, Who*: ***Where's** the puddle? — It's near the door.*"]},

    H1("¿Te sientes perdido? Empieza aquí"),
    P("Si en clase no entendiste el tema, lee esta página primero. Aquí está **lo esencial** en una sola hoja."),
    H3("1. Las 10 palabras que más vas a escuchar"),
    TABLE([2200, 2700, 2200, 2700], ["Inglés", "Español", "Inglés", "Español"], [
        ["rain", "lluvia", "umbrella", "paraguas"],
        ["cloud", "nube", "raincoat", "impermeable"],
        ["storm", "tormenta", "boots", "botas"],
        ["lightning", "relámpago", "puddle", "charco"],
        ["thunder", "trueno", "wet", "mojado"],
    ]),
    H3("2. Lo que pasa ahora"),
    P("**am / is / are + verbo con -ing**:  It **is raining**.  ·  I **am jumping**.  ·  We **are playing**.", align="center"),
    H3("3. Preguntas"),
    TABLE([4900, 4900], ["Pregunta", "Respuesta"], [
        ["**Where**'s the puddle? (¿Dónde?)", "It's **near** the door."],
        ["**What** is she wearing? (¿Qué?)", "She's wearing a raincoat."],
        ["**Who** has an umbrella? (¿Quién?)", "Ana has an umbrella."],
    ]),
    P("Escucha estas palabras en el **Audio 6.1-01** (página de Vocabulario)."),
    PB,

    H1("1. Vocabulario"),
    P("Escucha el audio, señala cada palabra y repítela en voz alta. La columna **Se pronuncia** te da una ayuda aproximada; el audio es la pronunciación correcta."),
    audio("01"),
    TABLE([2100, 1700, 2300, 3700], ["Inglés", "Se pronuncia", "Español", "Ejemplo"],
          [[f"**{w}**", p, s, f"*{ex}*"] for w, p, s, ex in VOCAB]),
    NOTE("¿Dónde está?", "**in** dentro de · **on** sobre · **under** debajo de · **near** cerca de · **next to** al lado de"),
    PB,

    H1("2. Lectura: Where's the Puddle?"),
    P("Lee el texto dos veces. La primera vez, en silencio. La segunda, en voz alta o junto con el audio."),
    audio("02"),
    READ("Where's the Puddle?", READING),
    H2("Chant: Rain, Rain!"),
    P("Escucha y repite. Marca el ritmo con palmadas."),
    audio("03"),
    POEM(CHANT),
    PB,

    H1("3. Gramática del tema"),
    H2("A. Presente continuo: lo que pasa ahora"),
    TABLE([3300, 3300, 3200], ["Afirmativa", "Negativa", "Pregunta"], [
        ["I **am** jump**ing**.", "I'**m not** sleep**ing**.", "**Are** you play**ing**?"],
        ["She / It **is** rain**ing**.", "It **isn't** rain**ing**.", "**Is** it rain**ing**?"],
        ["We / They **are** play**ing**.", "They **aren't** play**ing**.", "**What are** you do**ing**?"],
    ]),
    P("Palabras que te avisan: **now** (ahora) · **right now** (ahora mismo) · **Look!** (¡mira!)"),
    H2("B. Presente simple o continuo"),
    TABLE([4900, 4900], ["Siempre / normalmente", "Ahora mismo"], [
        ["I **wear** boots in the rain.", "I **am wearing** boots now."],
        ["It **rains** a lot in October.", "Look! It **is raining**."],
    ]),
    H2("C. Where, What, Who"),
    P("***Where** is the umbrella? — It's under the table.*  ·  ***What** is Ana doing? — She's jumping.*  ·  ***Who** is cooking? — Mom is cooking.*"),
    NOTE("Errores comunes",
         "✗ She jumping.  ✓ She **is** jumping.   (falta *is*)",
         "✗ It is rain.  ✓ It is **raining**.   (lleva -ing)",
         "✗ Where the puddle is?  ✓ **Where is** the puddle?"),
    PB,

    H1("4. Listening (Escuchar)"),
    H2("Práctica: It's Raining!"),
    P("Ana y Carlos miran la lluvia. **Primera vez:** solo escucha. **Segunda vez:** responde. Si lo necesitas, usa la velocidad lenta."),
    audio("04"),
    P("**Ejemplo:** It's ______ outside. → **raining**"),
    ITEMS("1. What is Dad doing?"),
    OPTS("a) He's cooking.", "b) He's closing the windows.", "c) He's reading."),
    ITEMS("2. The umbrella is ______________ the table."),
    ITEMS("3. Where's the puddle?"),
    OPTS("a) next to the tree", "b) near the door", "c) under the table"),
    ITEMS("4. What are they doing now?  They are ______________ lunch."),
    *test_blocks(TESTS["listening"], audio),
    PB,

    H1("5. Reading (Leer)"),
    H2("Práctica (texto: Where's the Puddle?)"),
    P("**A. True or False.** Escribe T o F."),
    P("**Ejemplo:** The sky is dark. → **T**"),
    ITEMS("1. Ana has an umbrella. ______", "2. Carlos wears boots. ______",
          "3. The puddle is near the door. ______", "4. They are sad in the rain. ______"),
    P("**B. Responde con una palabra o una oración corta.**"),
    ITEMS("1. Who has a raincoat?  ______________", "2. Where is the puddle?  ______________",
          "3. What does Carlos hear?  ______________"),
    *test_blocks(TESTS["reading"], audio),
    PB,

    H1("6. Writing (Escribir)"),
    H2("Práctica"),
    P("**A. Completa con am, is o are + -ing.**"),
    P("**Ejemplo:** It ______ (rain). → **is raining**"),
    ITEMS("1. Ana ______________ (jump) in the puddle.", "2. I ______________ (wear) my boots.",
          "3. We ______________ (play) in the rain.", "4. Dad ______________ (read) a book."),
    P("**B. Escribe la pregunta con Where, What o Who.**"),
    P("**Ejemplo:** ______ is the puddle? — It's near the door. → **Where**"),
    ITEMS("1. ______ is she wearing? — A raincoat.", "2. ______ has an umbrella? — Ana.", "3. ______ are my boots? — Under the bed."),
    P("**C. Un día de lluvia.** En tu cuaderno, escribe 3 oraciones sobre lo que tu familia **está haciendo ahora** (*My mom is...*)."),
    *test_blocks(TESTS["writing"], audio),
    PB,

    H1("7. Speaking (Hablar)"),
    H2("Práctica: escucha, repite y grábate"),
    P("**Paso 1.** Escucha cada oración y repítela en la pausa."),
    P("**Paso 2.** Graba en un celular las mismas oraciones."),
    P("**Paso 3.** Escucha tu grabación. En *rain* la **r** es suave: la lengua **no toca** el paladar."),
    audio("06"),
    ITEMS(*[f"{i+1}. {s}" for i, s in enumerate(SPEAK_MODELS)]),
    P("**Prepara tu presentación: \"A Rainy Day\".** Haz un dibujo de un día de lluvia y di 4 oraciones: el tiempo, lo que ves y lo que la gente está haciendo."),
    *test_blocks(TESTS["speaking"], audio),
    PB,

    H1("8. Mediation (Ayudar a otros a entender)"),
    P("Mediar es **ayudar a otra persona a entender un mensaje**: lo haces más corto y simple, o lo pasas de un idioma a otro."),
    H2("Práctica"),
    P("**A. Mímica.** Sin hablar, enséñale a un familiar estas palabras con gestos: *rain, thunder, umbrella, jump*. El familiar adivina en español."),
    P("**B. Explica en español.** Tu abuelo no entiende este mensaje. Escribe en español qué dice."),
    NOTE("Mensaje", "*It's raining. Where's my umbrella? It's near the door.*"),
    LINES(1),
    *test_blocks(TESTS["mediation"], audio),
    PB,

    H1("¿Cómo me fue en el Tema 6.1?"),
    P("Anota tus puntajes. Te dicen qué repasar antes de una prueba."),
    TABLE([2600, 1600, 5600], ["Mini-test", "Puntaje", "Si tuviste menos de la mitad, repasa..."],
          [[SKILL_TITLES[k].split(" ")[-1] if k != "speaking" else "Speaking", f"___ / {t['total']}", t["review"]]
           for k, t in TESTS.items()]),
    TABLE([6400, 1100, 1100, 1200], ["Puedo...", "Sí", "Casi", "Todavía no"], [
        ["nombrar cosas de la lluvia", "☐", "☐", "☐"],
        ["decir lo que pasa ahora (*It is raining*)", "☐", "☐", "☐"],
        ["preguntar con *Where, What, Who*", "☐", "☐", "☐"],
        ["decir dónde está algo (*near, under, next to*)", "☐", "☐", "☐"],
        ["explicar un mensaje en español", "☐", "☐", "☐"],
    ]),
    PB,

    H1("Respuestas del Tema 6.1"),
    P("Corrige **solo después de terminar**. Si te equivocaste, lee la explicación: ahí está lo que necesitas aprender."),
    H3("Listening — Práctica"),
    ITEMS("1. **b) He's closing the windows.**   2. **under.**",
          "3. **a) next to the tree.**   4. **eating.** *We are eating lunch now.*"),
    *answer_blocks(TESTS["listening"]),
    H3("Reading — Práctica"),
    ITEMS("A1. **T.**   A2. **F.** Carlos wears **sandals**. Ana wears boots.   A3. **T.**   A4. **F.** They are **happy**.",
          "B1. **Ana.**   B2. **Near the door.**   B3. **Thunder.**"),
    *answer_blocks(TESTS["reading"]),
    H3("Writing — Práctica"),
    ITEMS("A1. **is jumping**   A2. **am wearing**   A3. **are playing**   A4. **is reading**",
          "B1. **What**   B2. **Who**   B3. **Where**"),
    *answer_blocks(TESTS["writing"]),
    *answer_blocks(TESTS["mediation"]),
    PB,

    H1("Transcripciones de los audios del Tema 6.1"),
    P("Si no puedes escuchar un audio, pide a alguien que lo lea o léelo tú en voz alta. Úsalas también para revisar lo que no entendiste."),
    {"t": "transcripts"},
]
