# -*- coding: utf-8 -*-
"""5.º · Scenario 5, Theme 2 — We Can Swim.
Fuentes: planeamiento 5_5-2 y módulo GeMA 5_5-2. Marcado: **negrita**, *cursiva*."""
from common import *
from tests_t52 import TESTS

THEME_ID = "5-2"
THEME_TITLE = "We Can Swim."
SCENARIO = "Scenario 5: Time for Exercise"

NAR, PED, SOF, ROS = "af_heart", "am_puck", "af_bella", "af_sarah"
SPEAKERS = {PED: "Pedro", SOF: "Sofía", ROS: "Miss Rosa"}

VOCAB = [
    ("swim", "suim", "nadar", "I can swim."),
    ("run fast", "ran fast", "correr rápido", "Pedro can run fast."),
    ("jump high", "yamp jai", "saltar alto", "Can you jump high?"),
    ("climb", "claim", "escalar, trepar", "I can't climb a tree."),
    ("dance", "dans", "bailar", "She can dance very well."),
    ("ride a bike", "raid a baik", "andar en bicicleta", "We can ride a bike."),
    ("play volleyball", "plei VÓ-li-bol", "jugar voleibol", "They can play volleyball."),
    ("well / very well", "uel / VÉ-ri uel", "bien / muy bien", "He can dance very well."),
    ("can", "can", "poder, saber hacer", "I can run fast."),
    ("can't", "cant", "no poder, no saber", "I can't climb."),
    ("team", "tim", "equipo", "Our team can win!"),
    ("sport", "sport", "deporte", "Volleyball is my favorite sport."),
]

READING = [
    "Today is Sports Day at my school. My name is Pedro, and I am on the blue team.",
    "My friend Sofía can swim very well. She is the fastest swimmer in our class. I can't swim very well, but I can run fast! Marcos can jump high, and Elena can play volleyball.",
    "Our teacher asks, \"Can you climb the rope?\" Marcos says, \"Yes, I can!\" I say, \"No, I can't.\" That is OK. We can all do something well.",
    "At the end of the day, our team wins! We can work together!",
]

CHANT = [
    "Can you swim? Yes, I can!",
    "Can you climb? No, I can't!",
    "I can run and I can jump,",
    "I can dance. Bump, bump, bump!",
    "We are a team, we work together,",
    "We can do it, now and forever!",
]

DIALOGUE_PRACTICE = [
    (SOF, "Pedro, can you play volleyball?"),
    (PED, "No, I can't. But I can play football very well."),
    (SOF, "Can you swim?"),
    (PED, "Yes, I can, but not very well."),
    (SOF, "I can swim very well! And I can ride a bike."),
    (PED, "Cool! Can you climb a tree?"),
    (SOF, "No, I can't. It's very difficult for me."),
    (PED, "My brother can climb trees. He's fast!"),
]

TEST_MONOLOGUE = [
    "Good morning, students! I'm Miss Rosa, the P.E. teacher. Let's make the teams for Sports Day.",
    "The red team can swim very well, so they are in the swimming race.",
    "The blue team can run fast. They are in the running race at nine o'clock.",
    "The green team can't run very fast, but they can jump high. They are in the jumping game.",
    "And the yellow team can play volleyball. Their game is at eleven o'clock.",
    "Remember: we can all do something well. Bring water and a cap!",
]

SPEAK_MODELS = [
    "I can swim.",
    "I can't climb a tree.",
    "She can dance very well.",
    "Can you ride a bike? Yes, I can.",
    "Can you jump high? No, I can't.",
    "We are a team. We can win!",
]

SPEAK_TEST_Q = [
    "Question one. Can you swim?",
    "Question two. What sport can you play?",
    "Question three. What can't you do?",
    "Question four. What can your best friend do very well?",
    "Question five. Can you ride a bike?",
]

TRACKS = [
    {"n": "01", "title": "Vocabulario clave",
     "instr": "Escucha cada palabra y su ejemplo. Repite en voz alta durante la pausa.",
     "segments": vocab_segments(VOCAB)},
    {"n": "02", "title": "Lectura: Sports Day at School",
     "instr": "Escucha el texto mientras lo sigues con el dedo en tu libro.",
     "segments": [(PED, p, 1.0) for p in READING]},
    {"n": "03", "title": "Chant: Can You Swim?",
     "instr": "Escucha el chant y repítelo. Marca el ritmo con palmadas.",
     "segments": [(NAR, l, 0.5) for l in CHANT]},
    {"n": "04", "title": "Listening — Práctica: What Can You Do?",
     "instr": "Escucha el diálogo dos veces. La primera vez, solo escucha. La segunda vez, responde.",
     "segments": [(v, t, 0.6) for v, t in DIALOGUE_PRACTICE]},
    {"n": "05", "title": "Listening — Mini-test: The Sports Day Teams",
     "instr": "Mini-test. Escucha dos veces como máximo y responde en tu libro.",
     "segments": [(ROS, t, 0.7) for t in TEST_MONOLOGUE]},
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
     "es": "Podemos nadar.",
     "goals": ["Decir lo que puedes y no puedes hacer: *I **can** swim. I **can't** climb.*",
               "Preguntar y responder: *Can you ride a bike? — Yes, I **can**. / No, I **can't**.*",
               "Decir qué tan bien: *She can dance **very well**.*"]},

    H1("¿Te sientes perdido? Empieza aquí"),
    P("Si en clase no entendiste el tema, lee esta página primero. Aquí está **lo esencial** en una sola hoja."),
    H3("1. Las 10 palabras que más vas a escuchar"),
    TABLE([2200, 2700, 2200, 2700], ["Inglés", "Español", "Inglés", "Español"], [
        ["swim", "nadar", "ride a bike", "andar en bici"],
        ["run fast", "correr rápido", "well", "bien"],
        ["jump high", "saltar alto", "can", "puedo, sé"],
        ["climb", "trepar", "can't", "no puedo"],
        ["dance", "bailar", "team", "equipo"],
    ]),
    H3("2. La regla del tema"),
    P("**can** nunca cambia, y el verbo va **solo**, sin -s y sin -ing:  I can swim · She **can swim** · They can swim", align="center"),
    H3("3. Pregunta y respuesta corta"),
    P("*Can you swim? — Yes, I **can**. / No, I **can't**.*", align="center"),
    H3("4. No confundas"),
    P("*I **like** swimming* = me **gusta** nadar.   ·   *I **can** swim* = **sé** (puedo) nadar."),
    P("Escucha estas palabras en el **Audio 5.2-01** (página de Vocabulario)."),
    PB,

    H1("1. Vocabulario"),
    P("Escucha el audio, señala cada palabra y repítela en voz alta. La columna **Se pronuncia** te da una ayuda aproximada; el audio es la pronunciación correcta."),
    audio("01"),
    TABLE([2100, 1700, 2300, 3700], ["Inglés", "Se pronuncia", "Español", "Ejemplo"],
          [[f"**{w}**", p, s, f"*{ex}*"] for w, p, s, ex in VOCAB]),
    NOTE("Truco de pronunciación", "En **climb** la *b* final no suena: /claim/. **can't** se dice con fuerza para que se note el \"no\": /cant/."),
    PB,

    H1("2. Lectura: Sports Day at School"),
    P("Lee el texto dos veces. La primera vez, en silencio. La segunda, en voz alta o junto con el audio."),
    audio("02"),
    READ("Sports Day at School", READING),
    H2("Chant: Can You Swim?"),
    P("Escucha y repite. Marca el ritmo con palmadas."),
    audio("03"),
    POEM(CHANT),
    PB,

    H1("3. Gramática del tema"),
    H2("A. can / can't"),
    TABLE([3300, 3300, 3200], ["Afirmativa", "Negativa", "Pregunta"], [
        ["I **can** swim.", "I **can't** climb.", "**Can** you swim?"],
        ["She **can** dance.", "He **can't** jump high.", "**Can** she dance?"],
        ["We **can** win!", "They **can't** run fast.", "**Can** they play volleyball?"],
    ]),
    P("Respuestas cortas: *Yes, I **can**. / No, I **can't**.*  ·  *Yes, she **can**. / No, she **can't**.*"),
    H2("B. ¿Qué tan bien?"),
    P("Al final de la oración: *I can swim **well**.* · *She can dance **very well**.* · *I can swim, but **not very well**.*"),
    H2("C. like o can"),
    TABLE([4900, 4900], ["like + -ing (gusto)", "can + verbo (habilidad)"], [
        ["I **like swimming**.", "I **can swim**."],
        ["She **likes dancing**.", "She **can dance**."],
    ]),
    NOTE("Errores comunes",
         "✗ She **cans** swim.  ✓ She **can** swim.   (can nunca lleva -s)",
         "✗ I can **swimming**.  ✓ I can **swim**.   ✗ He can **to** run.  ✓ He can **run**.",
         "✗ Can you swim? — Yes, I **do**.  ✓ Yes, I **can**."),
    PB,

    H1("4. Listening (Escuchar)"),
    H2("Práctica: What Can You Do?"),
    P("Sofía y Pedro hablan de lo que pueden hacer. **Primera vez:** solo escucha. **Segunda vez:** responde. Si lo necesitas, usa la velocidad lenta."),
    audio("04"),
    P("**Ejemplo:** Pedro can't play ______. → **volleyball**"),
    ITEMS("1. Pedro can play ______________ very well."),
    ITEMS("2. Can Pedro swim?"),
    OPTS("a) Yes, very well.", "b) Yes, but not very well.", "c) No, he can't."),
    ITEMS("3. What can Sofía do?"),
    OPTS("a) swim and ride a bike", "b) climb trees", "c) play football"),
    ITEMS("4. Can Sofía climb a tree?  ______________"),
    ITEMS("5. Who can climb trees?"),
    OPTS("a) Sofía", "b) Pedro", "c) Pedro's brother"),
    *test_blocks(TESTS["listening"], audio),
    PB,

    H1("5. Reading (Leer)"),
    H2("Práctica (texto: Sports Day at School)"),
    P("**A. True or False.** Escribe T o F. Si es falso, corrige la oración."),
    P("**Ejemplo:** Pedro is on the blue team. → **T**"),
    ITEMS("1. Sofía can swim very well. ______", "2. Pedro can swim very well. ______",
          "3. Elena can play volleyball. ______", "4. Pedro can climb the rope. ______"),
    P("**B. Une cada persona con lo que puede hacer.** Escribe la letra."),
    TABLE([5600, 4200], ["Persona", "Puede..."], [
        ["1. Sofía  ___", "a) run fast"],
        ["2. Pedro  ___", "b) jump high and climb"],
        ["3. Marcos  ___", "c) play volleyball"],
        ["4. Elena  ___", "d) swim very well"],
    ]),
    *test_blocks(TESTS["reading"], audio),
    PB,

    H1("6. Writing (Escribir)"),
    H2("Práctica"),
    P("**A. Completa con can o can't** según los símbolos (✓ = sí, ✗ = no)."),
    P("**Ejemplo:** I ______ swim. (✓) → **can**"),
    ITEMS("1. Pedro ______ run fast. (✓)", "2. Sofía ______ climb a tree. (✗)", "3. We ______ play volleyball. (✓)",
          "4. My dog ______ ride a bike. (✗)", "5. ______ you dance? — Yes, I ______."),
    P("**B. Ordena las palabras.**"),
    P("**Ejemplo:** swim / can / I → **I can swim.**"),
    ITEMS("1. dance / She / very well / can  →  ______________________________",
          "2. you / Can / jump high / ?  →  ______________________________",
          "3. climb / can't / I  →  ______________________________"),
    P("**C. Escribe sobre ti.** En tu cuaderno: 2 cosas que **puedes** hacer y 1 que **no puedes** hacer."),
    *test_blocks(TESTS["writing"], audio),
    PB,

    H1("7. Speaking (Hablar)"),
    H2("Práctica: escucha, repite y grábate"),
    P("**Paso 1.** Escucha cada oración y repítela en la pausa."),
    P("**Paso 2.** Graba en un celular las mismas oraciones."),
    P("**Paso 3.** Escucha tu grabación. ¿Se nota la diferencia entre **can** y **can't**? En *can't*, di la *t* con fuerza."),
    audio("06"),
    ITEMS(*[f"{i+1}. {s}" for i, s in enumerate(SPEAK_MODELS)]),
    P("**Prepara tu presentación: \"I Can Do It!\".** Di 3 cosas que puedes hacer, 1 que no puedes y 1 que puede hacer alguien de tu familia. Practícala hasta decirla **sin leer**."),
    *test_blocks(TESTS["speaking"], audio),
    PB,

    H1("8. Mediation (Ayudar a otros a entender)"),
    P("Mediar es **ayudar a otra persona a entender un mensaje**: lo haces más corto y simple, o lo pasas de un idioma a otro."),
    H2("Práctica"),
    P("**A. ¿Qué puede hacer tu familia?** Pregunta a 2 familiares (en español): *¿Sabes nadar? ¿Sabes andar en bicicleta?* Escribe sus respuestas **en inglés**."),
    P("**Ejemplo:** *Mi papá sabe nadar, pero no sabe bailar.* → *My dad can swim, but he can't dance.*"),
    LINES(2),
    P("**B. Explica en español.** Tu hermanito no entiende este letrero de la piscina. Escribe en español qué significa."),
    NOTE("Letrero", "*Only students who can swim well can go in the big pool.*"),
    LINES(1),
    *test_blocks(TESTS["mediation"], audio),
    PB,

    H1("¿Cómo me fue en el Tema 5.2?"),
    P("Anota tus puntajes. Te dicen qué repasar antes de una prueba."),
    TABLE([2600, 1600, 5600], ["Mini-test", "Puntaje", "Si tuviste menos de la mitad, repasa..."],
          [[SKILL_TITLES[k].split(" ")[-1] if k != "speaking" else "Speaking", f"___ / {t['total']}", t["review"]]
           for k, t in TESTS.items()]),
    TABLE([6400, 1100, 1100, 1200], ["Puedo...", "Sí", "Casi", "Todavía no"], [
        ["decir lo que puedo y no puedo hacer (*can / can't*)", "☐", "☐", "☐"],
        ["preguntar *Can you...?* y responder *Yes, I can.*", "☐", "☐", "☐"],
        ["decir qué tan bien hago algo (*very well*)", "☐", "☐", "☐"],
        ["diferenciar *I like swimming* de *I can swim*", "☐", "☐", "☐"],
        ["explicar en español un letrero en inglés", "☐", "☐", "☐"],
    ]),
    PB,

    H1("Respuestas del Tema 5.2"),
    P("Corrige **solo después de terminar**. Si te equivocaste, lee la explicación: ahí está lo que necesitas aprender."),
    H3("Listening — Práctica"),
    ITEMS("1. **football.** *But I can play football very well.*",
          "2. **b) Yes, but not very well.** *Yes, I can, but not very well.*",
          "3. **a) swim and ride a bike.**   4. **No, she can't.**",
          "5. **c) Pedro's brother.** *My brother can climb trees.*"),
    *answer_blocks(TESTS["listening"]),
    H3("Reading — Práctica"),
    ITEMS("A1. **T.**   A3. **T.**",
          "A2. **F.** Pedro **can't** swim very well, but he can run fast.",
          "A4. **F.** Pedro **can't** climb the rope. Marcos can.",
          "B. 1-d · 2-a · 3-b · 4-c"),
    *answer_blocks(TESTS["reading"]),
    H3("Writing — Práctica"),
    ITEMS("A1. **can**   A2. **can't**   A3. **can**   A4. **can't**   A5. **Can** ... **can**",
          "B1. **She can dance very well.**   B2. **Can you jump high?**   B3. **I can't climb.**",
          "C. Ejemplo: *I can ride a bike. I can't swim.*"),
    *answer_blocks(TESTS["writing"]),
    H3("Mediation — ejemplos de respuesta"),
    ITEMS("Práctica B: *Solo los estudiantes que saben nadar bien pueden entrar a la piscina grande.*"),
    *answer_blocks(TESTS["mediation"]),
    PB,

    H1("Transcripciones de los audios del Tema 5.2"),
    P("Si no puedes escuchar un audio, pide a alguien que lo lea o léelo tú en voz alta. Úsalas también para revisar lo que no entendiste."),
    {"t": "transcripts"},
]
