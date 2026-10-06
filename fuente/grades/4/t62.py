# -*- coding: utf-8 -*-
"""4.º · Scenario 6, Theme 2 — I Need an Umbrella.
Fuentes: planeamiento 4_6-2 y módulo GeMA 4_6-2. Marcado: **negrita**, *cursiva*."""
from common import *
from tests_t62 import TESTS

THEME_ID = "6-2"
THEME_TITLE = "I Need an Umbrella."
SCENARIO = "Scenario 6: It's the Rainy Season"

NAR, CAR, ANA, MOM, VAL = "af_heart", "am_puck", "af_bella", "af_sarah", "af_nova"
SPEAKERS = {CAR: "Carlos", ANA: "Ana", MOM: "Mom", VAL: "Valeria"}

VOCAB = [
    ("need", "nid", "necesitar", "I need an umbrella today."),
    ("wear", "uer", "usar, llevar puesto", "I wear boots in the rain."),
    ("umbrella", "am-BRÉ-la", "paraguas", "I need an umbrella."),
    ("raincoat", "RÉIN-cout", "impermeable", "She wears a raincoat in the rain."),
    ("boots", "buts", "botas", "My boots are wet."),
    ("sandals", "SÁN-dols", "sandalias", "I wear sandals on sunny days."),
    ("puddle", "PÁ-dol", "charco", "I jump in the puddle."),
    ("storm", "storm", "tormenta", "The storm is big and loud."),
    ("thunder", "ZÁN-der", "trueno", "Thunder is loud at night."),
    ("lightning", "LÁIT-ning", "relámpago", "Lightning is bright in the storm."),
    ("wet", "uet", "mojado", "My raincoat is wet."),
    ("dry", "drai", "seco", "My socks are dry."),
]

READING = [
    "Today is a rainy day. The sky is gray. I see a big cloud. The cloud is dark. It is raining now.",
    "I hear thunder. I see lightning in the sky. It is a storm. I need an umbrella. I wear my raincoat and my boots.",
    "My boots are wet. I jump in a puddle. Splash! My friend Ana has an umbrella too. She wears sandals, but her feet are wet.",
    "We go home. We drink hot soup. I like rainy days.",
]

CHANT = [
    "Rain, rain, on my head,",
    "I need my umbrella, the sky is gray.",
    "Boots and raincoat, off I go,",
    "Jump in a puddle, splash and flow.",
    "Thunder, lightning, what a storm!",
    "I am wet, but nice and warm.",
]

DIALOGUE_PRACTICE = [
    (MOM, "Carlos, look outside. It's raining. What do you need?"),
    (CAR, "I need my umbrella."),
    (MOM, "Yes, and what do you wear in the rain?"),
    (CAR, "I wear my raincoat and my boots."),
    (MOM, "Good. Don't wear your sandals today."),
    (CAR, "OK, Mom. Does Ana need an umbrella too?"),
    (MOM, "No, she doesn't. She has a raincoat with a hood."),
    (CAR, "Bye, Mom! See you after school."),
]

TEST_MONOLOGUE = [
    "Good morning! This is Valeria with the weather for today.",
    "Right now, it's raining in Penonomé, and the sky is very dark.",
    "In the afternoon, there is going to be a big storm, with thunder and lightning.",
    "You need an umbrella today. Wear your raincoat and your boots. Don't wear sandals!",
    "Tomorrow is going to be sunny and hot. You don't need an umbrella tomorrow. You need a hat and sunscreen.",
    "Have a great day!",
]

SPEAK_MODELS = [
    "It is raining now.",
    "I need an umbrella.",
    "What do you need?",
    "I wear my raincoat and my boots.",
    "What do you wear in the rain?",
    "My boots are wet.",
]

SPEAK_TEST_Q = [
    "Question one. It's raining. What do you need?",
    "Question two. What do you wear in the rain?",
    "Question three. What do you wear on sunny days?",
    "Question four. What do you see in a storm?",
    "Question five. Do you like rainy days? Why?",
]

TRACKS = [
    {"n": "01", "title": "Vocabulario clave",
     "instr": "Escucha cada palabra y su ejemplo. Repite en voz alta durante la pausa.",
     "segments": vocab_segments(VOCAB)},
    {"n": "02", "title": "Lectura: A Rainy Day",
     "instr": "Escucha el texto mientras lo sigues con el dedo en tu libro.",
     "segments": [(CAR, p, 1.0) for p in READING]},
    {"n": "03", "title": "Chant: Rain on My Head",
     "instr": "Escucha el chant y repítelo. Marca el ritmo con palmadas.",
     "segments": [(NAR, l, 0.5) for l in CHANT]},
    {"n": "04", "title": "Listening — Práctica: What Do You Need?",
     "instr": "Escucha el diálogo dos veces. La primera vez, solo escucha. La segunda vez, responde.",
     "segments": [(v, t, 0.6) for v, t in DIALOGUE_PRACTICE]},
    {"n": "05", "title": "Listening — Mini-test: The Weather Today",
     "instr": "Mini-test. Escucha dos veces como máximo y responde en tu libro.",
     "segments": [(VAL, t, 0.7) for t in TEST_MONOLOGUE]},
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
     "es": "Necesito un paraguas.",
     "goals": ["Decir lo que necesitas: *I **need** an umbrella.*  ·  ***What do you need?***",
               "Decir lo que usas: *I **wear** boots in the rain.*  ·  ***What do you wear** in the rain?*",
               "Contar lo que pasa ahora: *It **is raining** now.*"]},

    H1("¿Te sientes perdido? Empieza aquí"),
    P("Si en clase no entendiste el tema, lee esta página primero. Aquí está **lo esencial** en una sola hoja."),
    H3("1. Las 10 palabras que más vas a escuchar"),
    TABLE([2200, 2700, 2200, 2700], ["Inglés", "Español", "Inglés", "Español"], [
        ["need", "necesitar", "sandals", "sandalias"],
        ["wear", "usar (ropa)", "storm", "tormenta"],
        ["umbrella", "paraguas", "thunder", "trueno"],
        ["raincoat", "impermeable", "wet", "mojado"],
        ["boots", "botas", "dry", "seco"],
    ]),
    H3("2. Dos preguntas y sus respuestas"),
    TABLE([4900, 4900], ["Pregunta", "Respuesta"], [
        ["**What do you need?**", "I **need** an umbrella."],
        ["**What do you wear** in the rain?", "I **wear** a raincoat and boots."],
    ]),
    H3("3. a / an"),
    P("**an** antes de vocal: *an **u**mbrella* · **a** antes de consonante: *a **r**aincoat*, *a **h**at*", align="center"),
    P("Escucha estas palabras en el **Audio 6.2-01** (página de Vocabulario)."),
    PB,

    H1("1. Vocabulario"),
    P("Escucha el audio, señala cada palabra y repítela en voz alta. La columna **Se pronuncia** te da una ayuda aproximada; el audio es la pronunciación correcta."),
    audio("01"),
    TABLE([2100, 1700, 2300, 3700], ["Inglés", "Se pronuncia", "Español", "Ejemplo"],
          [[f"**{w}**", p, s, f"*{ex}*"] for w, p, s, ex in VOCAB]),
    NOTE("Contrarios", "**wet** mojado ↔ **dry** seco  ·  **rainy** lluvioso ↔ **sunny** soleado  ·  **hot** caliente ↔ **cold** frío"),
    PB,

    H1("2. Lectura: A Rainy Day"),
    P("Lee el texto dos veces. La primera vez, en silencio. La segunda, en voz alta o junto con el audio."),
    audio("02"),
    READ("A Rainy Day", READING),
    H2("Chant: Rain on My Head"),
    P("Escucha y repite. Marca el ritmo con palmadas."),
    audio("03"),
    POEM(CHANT),
    PB,

    H1("3. Gramática del tema"),
    H2("A. need y wear (presente simple)"),
    TABLE([3300, 3300, 3200], ["Afirmativa", "Negativa", "Pregunta"], [
        ["I / you / we **need** an umbrella.", "I **don't need** a hat.", "**What do** you **need**?"],
        ["She / he **needs** boots.", "He **doesn't need** an umbrella.", "**Does** she **need** a raincoat?"],
        ["I **wear** boots in the rain.", "I **don't wear** sandals.", "**What do** you **wear** in the rain?"],
    ]),
    H2("B. Lo que pasa ahora"),
    P("*It **is raining** now.* · *I **am wearing** my raincoat.* · *The sky **is getting** dark.*"),
    P("Compara: *I **wear** boots in the rain* (siempre) · *I **am wearing** boots* (ahora mismo)."),
    NOTE("Errores comunes",
         "✗ I need a umbrella.  ✓ I need **an** umbrella.",
         "✗ She need boots.  ✓ She **needs** boots.   (con she, -s)",
         "✗ What you need?  ✓ What **do** you need?"),
    PB,

    H1("4. Listening (Escuchar)"),
    H2("Práctica: What Do You Need?"),
    P("Mamá ayuda a Carlos antes de ir a la escuela. **Primera vez:** solo escucha. **Segunda vez:** responde."),
    audio("04"),
    P("**Ejemplo:** It's ______ outside. → **raining**"),
    ITEMS("1. Carlos needs his ______________."),
    ITEMS("2. What does Carlos wear in the rain?"),
    OPTS("a) a raincoat and boots", "b) sandals", "c) a hat"),
    ITEMS("3. Mom says: \"Don't wear your ______________ today.\""),
    ITEMS("4. Does Ana need an umbrella?"),
    OPTS("a) Yes, she does.", "b) No, she doesn't.", "c) Carlos doesn't know."),
    *test_blocks(TESTS["listening"], audio),
    PB,

    H1("5. Reading (Leer)"),
    H2("Práctica (texto: A Rainy Day)"),
    P("**A. True or False.** Escribe T o F."),
    P("**Ejemplo:** The sky is gray. → **T**"),
    ITEMS("1. The boy needs an umbrella. ______", "2. Ana wears boots. ______",
          "3. The boy jumps in a puddle. ______", "4. They drink cold juice at home. ______"),
    P("**B. Completa con una palabra del texto.**"),
    ITEMS("1. I hear ______________.", "2. I wear my ______________ and my boots.", "3. Ana's feet are ______________."),
    *test_blocks(TESTS["reading"], audio),
    PB,

    H1("6. Writing (Escribir)"),
    H2("Práctica"),
    P("**A. Completa con a o an.**"),
    ITEMS("1. I need ______ umbrella.", "2. She wears ______ raincoat.", "3. I see ______ big cloud."),
    P("**B. Responde con una oración completa.**"),
    P("**Ejemplo:** What do you need in the rain? → **I need an umbrella.**"),
    ITEMS("1. What do you wear in the rain?  ______________________________",
          "2. What do you wear on sunny days?  ______________________________",
          "3. What do you need at the beach?  ______________________________"),
    P("**C. Mi tarjeta del día lluvioso.** En tu cuaderno, dibuja un día de lluvia y escribe 3 oraciones con *I need... / I wear... / It is raining...*"),
    *test_blocks(TESTS["writing"], audio),
    PB,

    H1("7. Speaking (Hablar)"),
    H2("Práctica: escucha, repite y grábate"),
    P("**Paso 1.** Escucha cada oración y repítela en la pausa."),
    P("**Paso 2.** Graba en un celular las mismas oraciones."),
    P("**Paso 3.** Escucha tu grabación. *wear* suena /uer/ y *need* suena /nid/ con una i larga."),
    audio("06"),
    ITEMS(*[f"{i+1}. {s}" for i, s in enumerate(SPEAK_MODELS)]),
    P("**Prepara tu presentación: \"Weather Reporter\".** Sé el reportero del clima por un minuto: di cómo está el tiempo ahora, qué necesita la gente y qué debe usar."),
    *test_blocks(TESTS["speaking"], audio),
    PB,

    H1("8. Mediation (Ayudar a otros a entender)"),
    P("Mediar es **ayudar a otra persona a entender un mensaje**: lo haces más corto y simple, o lo pasas de un idioma a otro."),
    H2("Práctica"),
    P("**A. ¿Cuándo lo usas?** Explícale a un familiar en español cuándo usas *umbrella*, *boots* y *sandals*. Luego di cada palabra en inglés."),
    P("**B. Explica en español.** Tu hermanita no entiende este mensaje. Escribe en español qué dice."),
    NOTE("Mensaje", "*It's raining. You need an umbrella. Wear your boots, not your sandals.*"),
    LINES(1),
    *test_blocks(TESTS["mediation"], audio),
    PB,

    H1("¿Cómo me fue en el Tema 6.2?"),
    P("Anota tus puntajes. Te dicen qué repasar antes de una prueba."),
    TABLE([2600, 1600, 5600], ["Mini-test", "Puntaje", "Si tuviste menos de la mitad, repasa..."],
          [[SKILL_TITLES[k].split(" ")[-1] if k != "speaking" else "Speaking", f"___ / {t['total']}", t["review"]]
           for k, t in TESTS.items()]),
    TABLE([6400, 1100, 1100, 1200], ["Puedo...", "Sí", "Casi", "Todavía no"], [
        ["decir lo que necesito (*I need...*)", "☐", "☐", "☐"],
        ["decir lo que uso (*I wear...*)", "☐", "☐", "☐"],
        ["preguntar *What do you need / wear?*", "☐", "☐", "☐"],
        ["entender un reporte del clima", "☐", "☐", "☐"],
        ["explicar un mensaje en español", "☐", "☐", "☐"],
    ]),
    PB,

    H1("Respuestas del Tema 6.2"),
    P("Corrige **solo después de terminar**. Si te equivocaste, lee la explicación: ahí está lo que necesitas aprender."),
    H3("Listening — Práctica"),
    ITEMS("1. **umbrella.**   2. **a) a raincoat and boots.**   3. **sandals.**",
          "4. **b) No, she doesn't.** *She has a raincoat with a hood.*"),
    *answer_blocks(TESTS["listening"]),
    H3("Reading — Práctica"),
    ITEMS("A1. **T.**   A2. **F.** Ana wears **sandals**.   A3. **T.**   A4. **F.** They drink **hot soup**.",
          "B1. **thunder**   B2. **raincoat**   B3. **wet**"),
    *answer_blocks(TESTS["reading"]),
    H3("Writing — Práctica"),
    ITEMS("A1. **an** (u es vocal)   A2. **a**   A3. **a**",
          "B. Ejemplos: 1. *I wear a raincoat and boots.* · 2. *I wear sandals and a hat.* · 3. *I need sunscreen and a towel.*"),
    *answer_blocks(TESTS["writing"]),
    *answer_blocks(TESTS["mediation"]),
    PB,

    H1("Transcripciones de los audios del Tema 6.2"),
    P("Si no puedes escuchar un audio, pide a alguien que lo lea o léelo tú en voz alta. Úsalas también para revisar lo que no entendiste."),
    {"t": "transcripts"},
]
