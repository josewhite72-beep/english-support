# -*- coding: utf-8 -*-
"""5.º · Scenario 5, Theme 1 — I Like Walking in the Afternoon.
Fuentes: planeamiento 5_5-1 y módulo GeMA 5_5-1. Marcado: **negrita**, *cursiva*."""
from common import *
from tests_t51 import TESTS

THEME_ID = "5-1"
THEME_TITLE = "I Like Walking in the Afternoon."
SCENARIO = "Scenario 5: Time for Exercise"

NAR, ANA, LUI, CAR = "af_heart", "af_bella", "am_puck", "af_sky"
SPEAKERS = {ANA: "Ana", LUI: "Luis", CAR: "Carla"}

VOCAB = [
    ("walking", "UÓ-quin", "caminar", "I like walking."),
    ("running", "RÁ-nin", "correr", "Luis likes running."),
    ("swimming", "SUÍ-min", "nadar", "I like swimming on Saturdays."),
    ("dancing", "DÁN-sin", "bailar", "My sister likes dancing."),
    ("reading", "RÍ-din", "leer", "I like reading in the evening."),
    ("playing football", "PLÉI-in FUT-bol", "jugar fútbol", "We like playing football."),
    ("riding a bike", "RÁI-din a baik", "andar en bicicleta", "I like riding a bike."),
    ("exercise", "ÉK-ser-sais", "ejercicio", "Exercise is good for you."),
    ("morning", "MÓR-nin", "mañana", "I go to school in the morning."),
    ("afternoon", "af-ter-NUN", "tarde", "I walk in the afternoon."),
    ("evening", "ÍV-nin", "anochecer, noche temprano", "I read in the evening."),
    ("like / don't like", "laik / dount laik", "me gusta / no me gusta", "I don't like running."),
]

READING = [
    "My name is Ana. I am ten years old. I like walking in the afternoon. Every day at four o'clock, I walk to the park with my friend Luis.",
    "Luis likes running, but I don't like running. I like walking and talking!",
    "In the morning, I go to school. In the evening, I like reading a book with my mom.",
    "My brother likes playing football in the afternoon, and my sister likes dancing in the evening. On Saturdays, we all like swimming at the beach. What do you like doing?",
]

CHANT = [
    "I like walking in the afternoon,",
    "I like reading, reading soon!",
    "Do you like running? No, I don't!",
    "Do you like dancing? Yes, I do!",
    "Morning, afternoon, evening too,",
    "What do you like doing? How about you?",
]

DIALOGUE_PRACTICE = [
    (CAR, "Hi, Luis! What do you like doing after school?"),
    (LUI, "I like running in the park."),
    (CAR, "Do you like swimming?"),
    (LUI, "Yes, I do! I like swimming on Sundays."),
    (CAR, "Me too! And do you like dancing?"),
    (LUI, "No, I don't. But my sister likes dancing a lot."),
    (CAR, "When do you run?"),
    (LUI, "In the afternoon, at five o'clock."),
    (CAR, "Can I run with you tomorrow?"),
    (LUI, "Sure!"),
]

TEST_MONOLOGUE = [
    "Hi! My name is Diego. I'm eleven years old, and I love exercise.",
    "In the morning, I like riding my bike to school.",
    "In the afternoon, I like playing football with my friends. We play at the park at four o'clock.",
    "I don't like swimming. The water is cold!",
    "My mom likes walking in the evening, and my dad likes running on Sundays.",
    "What do you like doing?",
]

SPEAK_MODELS = [
    "I like walking in the afternoon.",
    "I don't like running.",
    "She likes dancing in the evening.",
    "What do you like doing?",
    "Do you like swimming? Yes, I do.",
    "Do you like reading? No, I don't.",
]

SPEAK_TEST_Q = [
    "Question one. What do you like doing in the afternoon?",
    "Question two. Do you like swimming?",
    "Question three. What don't you like doing?",
    "Question four. What does your best friend like doing?",
    "Question five. What do you like doing on Saturdays?",
]

TRACKS = [
    {"n": "01", "title": "Vocabulario clave",
     "instr": "Escucha cada palabra y su ejemplo. Repite en voz alta durante la pausa.",
     "segments": vocab_segments(VOCAB)},
    {"n": "02", "title": "Lectura: Ana's Afternoons",
     "instr": "Escucha el texto mientras lo sigues con el dedo en tu libro.",
     "segments": [(ANA, p, 1.0) for p in READING]},
    {"n": "03", "title": "Chant: I Like Walking",
     "instr": "Escucha el chant y repítelo. Marca el ritmo con palmadas.",
     "segments": [(NAR, l, 0.5) for l in CHANT]},
    {"n": "04", "title": "Listening — Práctica: After School",
     "instr": "Escucha el diálogo dos veces. La primera vez, solo escucha. La segunda vez, responde.",
     "segments": [(v, t, 0.6) for v, t in DIALOGUE_PRACTICE]},
    {"n": "05", "title": "Listening — Mini-test: Diego Loves Exercise",
     "instr": "Mini-test. Escucha dos veces como máximo y responde en tu libro.",
     "segments": [("am_michael", t, 0.7) for t in TEST_MONOLOGUE]},
    {"n": "06", "title": "Speaking — Oraciones modelo",
     "instr": "Escucha cada oración y repítela en la pausa. Después grábate y compara.",
     "segments": [(NAR, s, 3.0) for s in SPEAK_MODELS]},
    {"n": "07", "title": "Speaking — Mini-test (examen oral)",
     "instr": "Prepara una grabadora. Responde cada pregunta en voz alta durante la pausa.",
     "segments": [(NAR, "Speaking test. Answer each question with a complete sentence.", 2.0)]
                 + [(NAR, q, 9.0) for q in SPEAK_TEST_Q]},
]
SPEAKERS["am_michael"] = "Diego"

def audio(n):
    t = next(t for t in TRACKS if t["n"] == n)
    return {"t": "audio", "id": f"{THEME_ID}/{n}", "label": f"Audio {THEME_ID.replace('-', '.')}-{n}", "title": t["title"]}

BLOCKS = [
    {"t": "theme_cover", "scenario": SCENARIO, "theme": "Theme 1: " + THEME_TITLE,
     "es": "Me gusta caminar en la tarde.",
     "goals": ["Decir lo que te gusta hacer: *I **like walking**.*  ·  *I **don't like** running.*",
               "Preguntar y responder: *What do you like doing?*  ·  *Do you like swimming? — Yes, I **do**.*",
               "Hablar de otra persona: *She **likes** dancing in the evening.*"]},

    H1("¿Te sientes perdido? Empieza aquí"),
    P("Si en clase no entendiste el tema, lee esta página primero. Aquí está **lo esencial** en una sola hoja."),
    H3("1. Las 10 palabras que más vas a escuchar"),
    TABLE([2200, 2700, 2200, 2700], ["Inglés", "Español", "Inglés", "Español"], [
        ["walking", "caminar", "reading", "leer"],
        ["running", "correr", "exercise", "ejercicio"],
        ["swimming", "nadar", "morning", "mañana"],
        ["dancing", "bailar", "afternoon", "tarde"],
        ["riding a bike", "andar en bici", "evening", "anochecer"],
    ]),
    H3("2. La regla del tema"),
    P("Después de **like**, el verbo lleva **-ing**:  I like walk**ing** · I like swimm**ing** · I like danc**ing**", align="center"),
    H3("3. Preguntas y respuestas"),
    TABLE([4900, 4900], ["Pregunta", "Respuesta"], [
        ["What do you like doing?", "I like **reading**."],
        ["Do you like swimming?", "Yes, I **do**. / No, I **don't**."],
        ["What does she like doing?", "She **likes** dancing."],
    ]),
    H3("4. Una presentación modelo"),
    P("*I like walking in the afternoon. I like reading in the evening. I don't like running.*"),
    P("Escucha estas palabras en el **Audio 5.1-01** (página de Vocabulario)."),
    PB,

    H1("1. Vocabulario"),
    P("Escucha el audio, señala cada palabra y repítela en voz alta. La columna **Se pronuncia** te da una ayuda aproximada; el audio es la pronunciación correcta."),
    audio("01"),
    TABLE([2100, 1700, 2300, 3700], ["Inglés", "Se pronuncia", "Español", "Ejemplo"],
          [[f"**{w}**", p, s, f"*{ex}*"] for w, p, s, ex in VOCAB]),
    NOTE("Truco de pronunciación", "En las palabras con **-ing** la *g* casi no se oye: walking /UÓ-quin/. Aplaude las sílabas: **af-ter-noon** (3) · **eve-ning** (2) · **danc-ing** (2)."),
    PB,

    H1("2. Lectura: Ana's Afternoons"),
    P("Lee el texto dos veces. La primera vez, en silencio. La segunda, en voz alta o junto con el audio."),
    audio("02"),
    READ("Ana's Afternoons", READING),
    H2("Chant: I Like Walking"),
    P("Escucha y repite. Marca el ritmo con palmadas."),
    audio("03"),
    POEM(CHANT),
    PB,

    H1("3. Gramática del tema"),
    H2("A. like + verbo con -ing"),
    TABLE([3300, 3300, 3200], ["Afirmativa", "Negativa", "Pregunta"], [
        ["I / you / we / they **like** walking.", "I **don't like** running.", "**Do** you **like** swimming?"],
        ["he / she **likes** walking.", "He **doesn't like** running.", "**Does** she **like** dancing?"],
    ]),
    P("Respuestas cortas: *Yes, I **do**. / No, I **don't**.*  ·  *Yes, she **does**. / No, she **doesn't**.*"),
    H2("B. Cómo se agrega -ing"),
    BULLETS("La mayoría: **+ ing** → walk**ing**, read**ing**, play**ing**.",
            "Terminan en **e**: quita la e → danc**e** → danc**ing**, rid**e** → rid**ing**.",
            "Corta con vocal + consonante: **dobla** la consonante → swi**m** → swi**mm**ing, ru**n** → ru**nn**ing."),
    H2("C. What do you like doing?"),
    P("Para preguntar **qué** te gusta hacer: *What do you like doing? — I like riding a bike.*"),
    P("Para decir **cuándo**: *in the morning · in the afternoon · in the evening · on Saturdays · at four o'clock*"),
    NOTE("Errores comunes",
         "✗ I like walk.  ✓ I like walk**ing**.     ✗ She like dancing.  ✓ She like**s** dancing.",
         "✗ Do you like swimming? — Yes, I like.  ✓ Yes, I **do**.",
         "✗ She doesn't likes...  ✓ She doesn't **like**...   (después de *doesn't*, sin -s)"),
    PB,

    H1("4. Listening (Escuchar)"),
    H2("Práctica: After School"),
    P("Carla y Luis hablan de lo que les gusta hacer. **Primera vez:** solo escucha. **Segunda vez:** responde. Si lo necesitas, usa la velocidad lenta."),
    audio("04"),
    P("**Ejemplo:** Luis likes ______ in the park. → **running**"),
    ITEMS("1. Does Luis like swimming?"),
    OPTS("a) Yes, he does.", "b) No, he doesn't.", "c) Only on Saturdays."),
    ITEMS("2. Luis likes swimming on ______________."),
    ITEMS("3. Who likes dancing?"),
    OPTS("a) Luis", "b) Carla", "c) Luis's sister"),
    ITEMS("4. Luis runs at ______________ o'clock."),
    ITEMS("5. When does Luis run?"),
    OPTS("a) in the morning", "b) in the afternoon", "c) in the evening"),
    *test_blocks(TESTS["listening"], audio),
    PB,

    H1("5. Reading (Leer)"),
    H2("Práctica (texto: Ana's Afternoons)"),
    P("**A. True or False.** Escribe T o F. Si es falso, corrige la oración."),
    P("**Ejemplo:** Ana is ten years old. → **T**"),
    ITEMS("1. Ana likes running. ______", "2. Ana walks to the park at four o'clock. ______",
          "3. Ana's sister likes dancing in the morning. ______", "4. On Saturdays, the family likes swimming. ______"),
    P("**B. Responde con una oración completa.**"),
    ITEMS("1. What does Ana like doing in the evening?  ______________________________",
          "2. What does her brother like doing?  ______________________________"),
    P("**C. Cazador de -ing.** Busca en el texto 5 palabras que terminen en **-ing**."),
    LINES(1),
    *test_blocks(TESTS["reading"], audio),
    PB,

    H1("6. Writing (Escribir)"),
    H2("Práctica"),
    P("**A. Escribe la forma con -ing.**"),
    P("**Ejemplo:** read → **reading**"),
    ITEMS("1. walk → ______________", "2. dance → ______________", "3. swim → ______________",
          "4. ride → ______________", "5. play → ______________"),
    P("**B. Ordena las palabras.**"),
    P("**Ejemplo:** like / I / reading → **I like reading.**"),
    ITEMS("1. likes / She / dancing  →  ______________________________",
          "2. you / Do / swimming / like / ?  →  ______________________________",
          "3. don't / I / running / like  →  ______________________________"),
    P("**C. Escribe sobre ti.** Completa el modelo en tu cuaderno."),
    P("*In the morning, I like ________. In the afternoon, I like ________. I don't like ________. My friend likes ________.*"),
    *test_blocks(TESTS["writing"], audio),
    PB,

    H1("7. Speaking (Hablar)"),
    H2("Práctica: escucha, repite y grábate"),
    P("**Paso 1.** Escucha cada oración y repítela en la pausa."),
    P("**Paso 2.** Graba en un celular las mismas oraciones."),
    P("**Paso 3.** Escucha tu grabación y compárala con el audio. ¿Se oye la **-s** de *likes* cuando hablas de otra persona?"),
    audio("06"),
    ITEMS(*[f"{i+1}. {s}" for i, s in enumerate(SPEAK_MODELS)]),
    P("**Prepara tu presentación: \"My Favorite Activities\".** Escribe 4 oraciones: qué te gusta hacer en la mañana, en la tarde, qué no te gusta y qué le gusta a alguien de tu familia. Practícala hasta decirla **sin leer**."),
    *test_blocks(TESTS["speaking"], audio),
    PB,

    H1("8. Mediation (Ayudar a otros a entender)"),
    P("Mediar es **ayudar a otra persona a entender un mensaje**: lo haces más corto y simple, o lo pasas de un idioma a otro."),
    H2("Práctica"),
    P("**A. Encuesta en casa.** Pregunta a 2 familiares (en español): *¿Qué te gusta hacer en la tarde?* Escribe sus respuestas **en inglés**."),
    P("**Ejemplo:** *A mi mamá le gusta caminar.* → *My mom likes walking.*"),
    LINES(2),
    P("**B. Explica en español.** Tu primo no entiende este mensaje. Escribe en español qué dice."),
    NOTE("Mensaje", "*I like playing football in the afternoon. I don't like swimming.*"),
    LINES(1),
    *test_blocks(TESTS["mediation"], audio),
    PB,

    H1("¿Cómo me fue en el Tema 5.1?"),
    P("Anota tus puntajes. Te dicen qué repasar antes de una prueba."),
    TABLE([2600, 1600, 5600], ["Mini-test", "Puntaje", "Si tuviste menos de la mitad, repasa..."],
          [[SKILL_TITLES[k].split(" ")[-1] if k != "speaking" else "Speaking", f"___ / {t['total']}", t["review"]]
           for k, t in TESTS.items()]),
    TABLE([6400, 1100, 1100, 1200], ["Puedo...", "Sí", "Casi", "Todavía no"], [
        ["decir lo que me gusta y no me gusta hacer (*I like walking*)", "☐", "☐", "☐"],
        ["preguntar *What do you like doing? / Do you like...?*", "☐", "☐", "☐"],
        ["usar *likes* con he / she", "☐", "☐", "☐"],
        ["entender a alguien que habla de sus actividades", "☐", "☐", "☐"],
        ["pasar una respuesta del español al inglés", "☐", "☐", "☐"],
    ]),
    PB,

    H1("Respuestas del Tema 5.1"),
    P("Corrige **solo después de terminar**. Si te equivocaste, lee la explicación: ahí está lo que necesitas aprender."),
    H3("Listening — Práctica"),
    ITEMS("1. **a) Yes, he does.** *Yes, I do! I like swimming on Sundays.*",
          "2. **Sundays.** Cuidado: no son los sábados.",
          "3. **c) Luis's sister.** *But my sister likes dancing a lot.*",
          "4. **five** (5).   5. **b) in the afternoon.**"),
    *answer_blocks(TESTS["listening"]),
    H3("Reading — Práctica"),
    ITEMS("A1. **F.** Ana **doesn't like** running. Le gusta caminar.   A2. **T.**",
          "A3. **F.** Her sister likes dancing **in the evening**.   A4. **T.**",
          "B1. *She likes reading a book with her mom.*   B2. *He likes playing football.*",
          "C. walking, running, talking, reading, playing, dancing, swimming, doing (cualquier 5)."),
    *answer_blocks(TESTS["reading"]),
    H3("Writing — Práctica"),
    ITEMS("A1. **walking**   A2. **dancing** (sin la e)   A3. **swimming** (doble m)   A4. **riding** (sin la e)   A5. **playing**",
          "B1. **She likes dancing.**   B2. **Do you like swimming?**   B3. **I don't like running.**",
          "C. Ejemplo: *In the morning, I like riding a bike. In the afternoon, I like playing football. I don't like swimming. My friend likes reading.*"),
    *answer_blocks(TESTS["writing"]),
    H3("Mediation — ejemplos de respuesta"),
    ITEMS("Práctica A: respuesta libre. Ejemplo: *My mom likes walking. My dad likes reading.*",
          "Práctica B: *Me gusta jugar fútbol en la tarde. No me gusta nadar.*"),
    *answer_blocks(TESTS["mediation"]),
    PB,

    H1("Transcripciones de los audios del Tema 5.1"),
    P("Si no puedes escuchar un audio, pide a alguien que lo lea o léelo tú en voz alta. Úsalas también para revisar lo que no entendiste."),
    {"t": "transcripts"},
]
