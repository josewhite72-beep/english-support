# -*- coding: utf-8 -*-
"""6.º · Scenario 5, Theme 1 — This Is My Amazing Community.
Fuentes: planeamiento 6_5-1 y módulo GeMA 6_5-1. Marcado: **negrita**, *cursiva*."""
from common import *
from tests_t51 import TESTS

THEME_ID = "5-1"
THEME_TITLE = "This Is My Amazing Community."
SCENARIO = "Scenario 5: Our Amazing Community"

NAR, SOF, TOM, LUI = "af_heart", "af_bella", "am_puck", "am_michael"
SPEAKERS = {SOF: "Sofía", TOM: "Tomás", LUI: "Luis"}

VOCAB = [
    ("community", "co-MIÚ-ni-ti", "comunidad", "My community is small."),
    ("amazing", "a-MÉI-sing", "increíble", "My community is amazing."),
    ("building", "BÍL-ding", "edificio", "The church is an old building."),
    ("market", "MAR-ket", "mercado", "The market is busy."),
    ("church", "cherch", "iglesia", "The church is the oldest building."),
    ("park", "park", "parque", "The park is quieter than the market."),
    ("busy", "BÍ-si", "con mucho movimiento", "The market is the busiest place."),
    ("quiet", "CUÁI-et", "tranquilo", "The park is quiet."),
    ("old", "ould", "antiguo, viejo", "The church is older than the school."),
    ("new", "niu", "nuevo", "The school is newer than the church."),
    ("famous", "FÉI-mos", "famoso", "The market is the most famous place."),
    ("important", "im-PÓR-tant", "importante", "The health center is very important."),
]

READING = [
    "My name is Sofía, and this is my amazing community. It is not very big, but it is beautiful. There is a market, a church, a park, and a school.",
    "The market is the busiest place in my community. Many people buy fruit and fish there every morning. The park is quieter than the market. Families walk and play there in the afternoon.",
    "The church is the oldest building in my community. It is older than the school. The school is newer than the church, and it is bigger.",
    "For me, the most beautiful place is the park, because it has big trees and flowers. The most famous place is the market. I love my community!",
]

CHANT = [
    "Busy, busier, the busiest!",
    "Quiet, quieter, the quietest!",
    "The church is old, the school is new,",
    "The park is more beautiful, it's true!",
    "Big and small, old and new,",
    "My community is amazing. How about you?",
]

DIALOGUE_PRACTICE = [
    (TOM, "Hi, Sofía! I'm new here. What is there in this community?"),
    (SOF, "Hi, Tomás! There is a market, a park, a church, and a school."),
    (TOM, "Which place is the busiest?"),
    (SOF, "The market. It's busier than the park, especially in the morning."),
    (TOM, "And which building is the oldest?"),
    (SOF, "The church. It's older than the school. The school is the newest building."),
    (TOM, "Is the park big?"),
    (SOF, "Yes! It's bigger than the market, and it's the most beautiful place, with big trees."),
    (TOM, "Cool! Where can I play soccer?"),
    (SOF, "In the park, in the afternoon. It's quieter then."),
]

TEST_MONOLOGUE = [
    "Hello! My name is Luis, and I'm your guide today. Welcome to my town, Las Tablas!",
    "There are many interesting places here. The plaza is the busiest place in town, because there are shops and restaurants around it.",
    "The church is the oldest building. It is older than the town hall, and it is more beautiful.",
    "The library is the newest building. It opened last year, and it is very quiet.",
    "The beach is not in the town. It is twenty minutes away, and it is quieter than the plaza.",
    "Las Tablas is the most famous town in Los Santos because of the Carnival. Enjoy your visit!",
]

SPEAK_MODELS = [
    "This is my amazing community.",
    "There is a park and a market.",
    "The market is busier than the park.",
    "The church is the oldest building.",
    "The park is the most beautiful place.",
    "My school is bigger than the church.",
]

SPEAK_TEST_Q = [
    "Question one. What is your community called?",
    "Question two. What places are there in your community?",
    "Question three. Which place is the busiest? Why?",
    "Question four. Compare two places. Which is bigger?",
    "Question five. What is the most beautiful place in your community?",
]

TRACKS = [
    {"n": "01", "title": "Vocabulario clave",
     "instr": "Escucha cada palabra y su ejemplo. Repite en voz alta durante la pausa.",
     "segments": vocab_segments(VOCAB)},
    {"n": "02", "title": "Lectura: Sofía's Community",
     "instr": "Escucha el texto mientras lo sigues con el dedo en tu libro.",
     "segments": [(SOF, p, 1.0) for p in READING]},
    {"n": "03", "title": "Chant: Busy, Busier, the Busiest!",
     "instr": "Escucha el chant y repítelo. Marca el ritmo con palmadas.",
     "segments": [(NAR, l, 0.5) for l in CHANT]},
    {"n": "04", "title": "Listening — Práctica: A New Neighbor",
     "instr": "Escucha el diálogo dos veces. La primera vez, solo escucha. La segunda vez, responde.",
     "segments": [(v, t, 0.6) for v, t in DIALOGUE_PRACTICE]},
    {"n": "05", "title": "Listening — Mini-test: Welcome to Las Tablas",
     "instr": "Mini-test. Escucha dos veces como máximo y responde en tu libro.",
     "segments": [(LUI, t, 0.7) for t in TEST_MONOLOGUE]},
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
     "es": "Esta es mi increíble comunidad.",
     "goals": ["Describir los lugares de tu comunidad: *There is a market. The park is quiet.*",
               "Comparar **dos** lugares: *The market is **busier than** the park.*",
               "Decir cuál es **el más** de todos: *The church is **the oldest** building.*"]},

    # ---------------------------------------------------- EMPIEZA AQUÍ ----
    H1("¿Te sientes perdido? Empieza aquí"),
    P("Si en clase no entendiste el tema, lee esta página primero. Aquí está **lo esencial** en una sola hoja."),
    H3("1. Las 10 palabras que más vas a escuchar"),
    TABLE([2200, 2700, 2200, 2700], ["Inglés", "Español", "Inglés", "Español"], [
        ["community", "comunidad", "busy", "con mucho movimiento"],
        ["building", "edificio", "quiet", "tranquilo"],
        ["market", "mercado", "old / new", "antiguo / nuevo"],
        ["church", "iglesia", "famous", "famoso"],
        ["park", "parque", "beautiful", "hermoso"],
    ]),
    H3("2. Comparar: la regla en una tabla"),
    TABLE([3300, 3300, 3200], ["Palabra", "Comparo 2 (más ... que)", "El más de todos"], [
        ["old (corta)", "old**er than**", "**the** old**est**"],
        ["busy (termina en y)", "bus**ier than**", "**the** bus**iest**"],
        ["beautiful (larga)", "**more** beautiful **than**", "**the most** beautiful"],
    ]),
    H3("3. Dos oraciones modelo"),
    P("*The market is **busier than** the park.* = El mercado tiene más movimiento **que** el parque."),
    P("*The church is **the oldest** building.* = La iglesia es **el** edificio **más** antiguo."),
    H3("4. Una descripción modelo"),
    P("*This is my amazing community. There is a market, a park, and a school. The market is busier than the park. The school is the newest building.*"),
    P("Escucha estas palabras en el **Audio 5.1-01** (página de Vocabulario)."),
    PB,

    # ---------------------------------------------------- VOCABULARIO ----
    H1("1. Vocabulario"),
    P("Escucha el audio, señala cada palabra y repítela en voz alta. La columna **Se pronuncia** te da una ayuda aproximada; el audio es la pronunciación correcta."),
    audio("01"),
    TABLE([2100, 1700, 2300, 3700], ["Inglés", "Se pronuncia", "Español", "Ejemplo"],
          [[f"**{w}**", p, s, f"*{ex}*"] for w, p, s, ex in VOCAB]),
    NOTE("Más lugares de la comunidad",
         "**school** escuela · **health center** centro de salud · **plaza** plaza · **store** tienda · **library** biblioteca · **beach** playa · **river** río · **town hall** municipio"),
    PB,

    # ---------------------------------------------------- LECTURA ----
    H1("2. Lectura: Sofía's Community"),
    P("Lee el texto dos veces. La primera vez, en silencio. La segunda, en voz alta o junto con el audio."),
    audio("02"),
    READ("Sofía's Community", READING),
    H2("Chant: Busy, Busier, the Busiest!"),
    P("Escucha y repite. Marca el ritmo con palmadas. Fíjate cómo cambia la palabra: busy → bus**ier** → the bus**iest**."),
    audio("03"),
    POEM(CHANT),
    PB,

    # ---------------------------------------------------- GRAMÁTICA ----
    H1("3. Gramática del tema"),
    H2("A. Comparativos: comparar dos cosas"),
    P("Para decir que algo es **más ... que** otra cosa usamos el **comparativo + than**."),
    TABLE([3000, 3400, 3400], ["Tipo de palabra", "Regla", "Ejemplo"], [
        ["Corta (1 sílaba)", "**+ er**", "old → old**er** · quiet → quiet**er**"],
        ["Corta que termina en vocal + consonante", "**dobla** la última letra + er", "big → bi**gg**er · hot → ho**tt**er"],
        ["Termina en **y**", "**y → ier**", "busy → bus**ier** · pretty → prett**ier**"],
        ["Larga (2 o más sílabas)", "**more** + palabra", "**more** beautiful · **more** famous · **more** important"],
    ]),
    P("*The market is busi**er than** the park.*  ·  *The park is **more beautiful than** the market.*"),
    H2("B. Superlativos: el más de todos"),
    P("Para decir cuál es **el más** de un grupo (tres o más) usamos **the + superlativo**."),
    TABLE([3300, 3300, 3200], ["Palabra", "Comparativo (2)", "Superlativo (3 o más)"], [
        ["old", "older than", "**the oldest**"],
        ["new", "newer than", "**the newest**"],
        ["quiet", "quieter than", "**the quietest**"],
        ["busy", "busier than", "**the busiest**"],
        ["big", "bigger than", "**the biggest**"],
        ["beautiful", "more beautiful than", "**the most beautiful**"],
        ["famous", "more famous than", "**the most famous**"],
    ]),
    NOTE("Errores comunes",
         "✗ more busy  ✓ **busier**   ·   ✗ more old  ✓ **older**   (las palabras cortas no usan *more*)",
         "✗ bigger **that** the park  ✓ bigger **than** the park",
         "✗ The church is oldest.  ✓ The church is **the** oldest.   (el superlativo lleva **the**)"),
    NOTE("Dos irregulares que debes saber",
         "good → **better** → **the best**  ·  bad → **worse** → **the worst**",
         "*The park is the **best** place for families.*"),
    H2("C. There is / There are"),
    P("**There is** + una cosa · **There are** + varias cosas: *There **is** a church. There **are** two parks.*"),
    PB,

    # ---------------------------------------------------- LISTENING ----
    H1("4. Listening (Escuchar)"),
    H2("Práctica: A New Neighbor"),
    P("Tomás es nuevo en la comunidad y le pregunta a Sofía. **Primera vez:** solo escucha. **Segunda vez:** responde. Si lo necesitas, usa la velocidad lenta."),
    audio("04"),
    P("**Ejemplo:** Tomás is ______ in the community. → **new**"),
    ITEMS("1. Which place is the busiest?"),
    OPTS("a) the park", "b) the market", "c) the school"),
    ITEMS("2. The church is ______________ than the school."),
    ITEMS("3. Which building is the newest?"),
    OPTS("a) the church", "b) the market", "c) the school"),
    ITEMS("4. The park is ______________ than the market."),
    ITEMS("5. When is the park quieter?"),
    OPTS("a) in the morning", "b) in the afternoon", "c) at night"),
    *test_blocks(TESTS["listening"], audio),
    PB,

    # ---------------------------------------------------- READING ----
    H1("5. Reading (Leer)"),
    H2("Práctica (texto: Sofía's Community)"),
    P("**A. True or False.** Escribe T o F. Si es falso, corrige la oración."),
    P("**Ejemplo:** Sofía's community is very big. → **F**: It is not very big."),
    ITEMS("1. The market is the busiest place. ______", "2. The school is older than the church. ______",
          "3. Families walk in the park in the afternoon. ______", "4. The most famous place is the park. ______"),
    P("**B. Responde con una oración completa.**"),
    ITEMS("1. What do people buy at the market?  ______________________________",
          "2. Which is bigger: the school or the church?  ______________________________",
          "3. Why is the park the most beautiful place for Sofía?  ______________________________"),
    P("**C. Cazador de comparaciones.** Busca en el texto 2 comparativos (*-er than / more ... than*) y 2 superlativos (*the -est / the most*)."),
    ITEMS("Comparativos: ______________  ______________", "Superlativos: ______________  ______________"),
    *test_blocks(TESTS["reading"], audio),
    PB,

    # ---------------------------------------------------- WRITING ----
    H1("6. Writing (Escribir)"),
    H2("Práctica"),
    P("**A. Completa la tabla.**"),
    P("**Ejemplo:** quiet → quieter than → **the quietest**"),
    ITEMS("1. new → newer than → ______________", "2. busy → ______________ → the busiest",
          "3. big → bigger than → ______________", "4. famous → ______________ → the most famous",
          "5. small → ______________ → the smallest"),
    P("**B. Escribe una oración con la palabra entre paréntesis.**"),
    P("**Ejemplo:** the market / the park (busy) → **The market is busier than the park.**"),
    ITEMS("1. the church / the school (old) → ______________________________",
          "2. the park / the market (beautiful) → ______________________________",
          "3. the school / the building (new) → The school is ______________ building.  (superlativo)"),
    P("**C. Escribe sobre tu comunidad.** Completa el modelo en tu cuaderno."),
    P("*In my community there is a ________ and a ________. The ________ is busier than the ________. The ________ is the oldest building. For me, the most beautiful place is ________ because ________.*"),
    *test_blocks(TESTS["writing"], audio),
    PB,

    # ---------------------------------------------------- SPEAKING ----
    H1("7. Speaking (Hablar)"),
    H2("Práctica: escucha, repite y grábate"),
    P("**Paso 1.** Escucha cada oración y repítela en la pausa."),
    P("**Paso 2.** Graba en un celular las mismas oraciones."),
    P("**Paso 3.** Escucha tu grabación y compárala con el audio. Fíjate en **than** y **the**: se dicen con la punta de la lengua entre los dientes."),
    audio("06"),
    ITEMS(*[f"{i+1}. {s}" for i, s in enumerate(SPEAK_MODELS)]),
    P("**Prepara tu presentación: \"My Amazing Community\".** Escribe 5 oraciones sobre 3 lugares de tu comunidad (2 comparativos y 1 superlativo). Practícala hasta decirla **sin leer**, como si fueras guía turístico."),
    *test_blocks(TESTS["speaking"], audio),
    PB,

    # ---------------------------------------------------- MEDIATION ----
    H1("8. Mediation (Ayudar a otros a entender)"),
    P("Mediar es **ayudar a otra persona a entender un mensaje**: lo haces más corto y simple, o lo pasas de un idioma a otro."),
    H2("Práctica"),
    P("**A. Pregunta en casa.** Pregunta a un familiar (en español): *¿Cuál es el lugar más antiguo de la comunidad? ¿Cuál tiene más movimiento?* Escribe sus respuestas **en inglés**."),
    P("**Ejemplo:** *La iglesia es lo más antiguo.* → *The church is the oldest building.*"),
    LINES(2),
    P("**B. Explica en español.** Un primo pequeño no entiende este letrero. Escribe en español qué significa."),
    NOTE("Letrero", "*The park is the quietest place in town. Please keep it clean.*"),
    LINES(1),
    *test_blocks(TESTS["mediation"], audio),
    PB,

    # ---------------------------------------------------- CIERRE ----
    H1("¿Cómo me fue en el Tema 5.1?"),
    P("Anota tus puntajes. Te dicen qué repasar antes de una prueba."),
    TABLE([2600, 1600, 5600], ["Mini-test", "Puntaje", "Si tuviste menos de la mitad, repasa..."],
          [[SKILL_TITLES[k].split(" ")[-1] if k != "speaking" else "Speaking", f"___ / {t['total']}", t["review"]]
           for k, t in TESTS.items()]),
    TABLE([6400, 1100, 1100, 1200], ["Puedo...", "Sí", "Casi", "Todavía no"], [
        ["describir los lugares de mi comunidad (*There is / There are*)", "☐", "☐", "☐"],
        ["comparar dos lugares (*busier than, more beautiful than*)", "☐", "☐", "☐"],
        ["decir cuál es el más de todos (*the oldest, the most famous*)", "☐", "☐", "☐"],
        ["entender a un guía que describe un pueblo", "☐", "☐", "☐"],
        ["pasar información del español al inglés", "☐", "☐", "☐"],
    ]),
    PB,

    # ---------------------------------------------------- RESPUESTAS ----
    H1("Respuestas del Tema 5.1"),
    P("Corrige **solo después de terminar**. Si te equivocaste, lee la explicación: ahí está lo que necesitas aprender."),
    H3("Listening — Práctica"),
    ITEMS("1. **b) the market.** Sofía: *The market. It's busier than the park.*",
          "2. **older.** *The church... It's older than the school.*",
          "3. **c) the school.** *The school is the newest building.*",
          "4. **bigger.** *It's bigger than the market.* (big → bi**gg**er)",
          "5. **b) in the afternoon.** *In the park, in the afternoon. It's quieter then.*"),
    *answer_blocks(TESTS["listening"]),
    H3("Reading — Práctica"),
    ITEMS("A1. **T.**   A3. **T.**",
          "A2. **F.** The school is **newer** than the church. (La iglesia es la más antigua.)",
          "A4. **F.** The most famous place is the **market**. El parque es el más **bonito** para Sofía.",
          "B1. *They buy fruit and fish.*   B2. *The school is bigger.*   B3. *Because it has big trees and flowers.*",
          "C. Comparativos: *quieter than, older than, newer than*. Superlativos: *the busiest, the oldest, the most beautiful, the most famous*."),
    *answer_blocks(TESTS["reading"]),
    H3("Writing — Práctica"),
    ITEMS("A1. **the newest**   A2. **busier than**   A3. **the biggest** (dobla la g)   A4. **more famous than**   A5. **smaller than**",
          "B1. **The church is older than the school.**   B2. **The park is more beautiful than the market.**   B3. The school is **the newest** building.",
          "C. Respuesta libre. Ejemplo: *In my community there is a park and a market. The market is busier than the park. The church is the oldest building. For me, the most beautiful place is the river because it is quiet.*"),
    *answer_blocks(TESTS["writing"]),
    H3("Mediation — ejemplos de respuesta"),
    ITEMS("Práctica A: respuesta libre. Ejemplo: *The church is the oldest building. The market is the busiest place.*",
          "Práctica B: *El parque es el lugar más tranquilo del pueblo. Por favor, mantenlo limpio.*"),
    *answer_blocks(TESTS["mediation"]),
    PB,

    # ---------------------------------------------------- TRANSCRIPCIONES ----
    H1("Transcripciones de los audios del Tema 5.1"),
    P("Si no puedes escuchar un audio, pide a alguien que lo lea o léelo tú en voz alta. Úsalas también para revisar lo que no entendiste."),
    {"t": "transcripts"},
]
