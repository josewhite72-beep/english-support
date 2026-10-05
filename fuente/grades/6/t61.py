# -*- coding: utf-8 -*-
"""6.º · Scenario 6, Theme 1 — Today's Weather Will Be Sunny with Some Rain Later.
Fuentes: planeamiento 6_6-1 y módulo GeMA 6_6-1. Marcado: **negrita**, *cursiva*."""
from common import *
from tests_t61 import TESTS

THEME_ID = "6-1"
THEME_TITLE = "Today's Weather Will Be Sunny with Some Rain Later."
SCENARIO = "Scenario 6: Our Weather Report"

NAR, VAL, DIE, ANA, LUI = "af_heart", "af_nova", "am_puck", "af_bella", "am_michael"
SPEAKERS = {VAL: "Valeria", DIE: "Diego", ANA: "Ana", LUI: "Luis"}

VOCAB = [
    ("weather", "UÉ-der", "el clima, el tiempo", "The weather is nice today."),
    ("sunny", "SÁ-ni", "soleado", "It will be sunny in the morning."),
    ("rainy", "RÉI-ni", "lluvioso", "It will be rainy in the afternoon."),
    ("cloudy", "CLÁU-di", "nublado", "Tomorrow will be cloudy."),
    ("windy", "UÍN-di", "ventoso, con viento", "It is windy at the park."),
    ("storm", "storm", "tormenta", "There will be a storm at night."),
    ("forecast", "FÓR-cast", "pronóstico del tiempo", "The forecast says it will rain."),
    ("temperature", "TÉM-pe-ra-chur", "temperatura", "The temperature is 28 degrees."),
    ("degree", "di-GRÍ", "grado", "It will be 30 degrees today."),
    ("hot / cold", "jot / could", "caluroso / frío", "It will be cold at night."),
    ("umbrella", "am-BRÉ-la", "paraguas, sombrilla", "You should bring an umbrella."),
    ("later", "LÉI-ter", "más tarde", "Later, it will be rainy."),
]

READING = [
    "Good morning! This is the weather forecast for Barrigón, Coclé.",
    "Today the weather will be sunny in the morning. The temperature will be 28 degrees. It is hot, so you should drink water.",
    "In the afternoon, it will be cloudy and windy. Later, it will be rainy with a small storm. The temperature will go down to 22 degrees. It will be cold at night. You should bring an umbrella and a jacket.",
    "Tomorrow the weather will be sunny again. The forecast says it will not rain tomorrow. It will be a good day for a walk.",
]

CHANT = [
    "What will the weather be today?",
    "Sunny, cloudy, rainy. Let's say!",
    "It will be hot, then cold at night.",
    "Bring your umbrella, hold it tight!",
    "The forecast says the storm will go.",
    "Tomorrow, sunny. Watch it glow!",
]

DIALOGUE_PRACTICE = [
    (DIE, "Ana, let's go to the river on Saturday!"),
    (ANA, "Good idea! But what will the weather be like?"),
    (DIE, "The forecast says it will be sunny in the morning."),
    (ANA, "And in the afternoon?"),
    (DIE, "It will be cloudy, and later it will be rainy."),
    (ANA, "So we should go early. What time?"),
    (DIE, "At eight o'clock. It will be hot, about thirty degrees."),
    (ANA, "Then we should bring water and a hat."),
    (DIE, "And an umbrella, for the rain later!"),
    (ANA, "OK. See you on Saturday!"),
]

TEST_MONOLOGUE = [
    "Good morning, students! This is Luis with the weather for Sports Day.",
    "Today will be a great day for games. In the morning, it will be sunny and hot. The temperature will be thirty-one degrees, so you should drink a lot of water.",
    "At noon, it will be windy. Hold your hats!",
    "In the afternoon, it will be cloudy, and later there will be some rain. The games will end at two o'clock, before the rain.",
    "Tomorrow, Saturday, it will be rainy all day. You should stay home and read a book.",
    "Have a great Sports Day!",
]

SPEAK_MODELS = [
    "Today the weather will be sunny.",
    "It will be rainy in the afternoon.",
    "The temperature will be 28 degrees.",
    "It will be cold at night.",
    "You should bring an umbrella.",
    "It is hot, so you should drink water.",
]

SPEAK_TEST_Q = [
    "Question one. What is the weather like today?",
    "Question two. What will the weather be like tomorrow?",
    "Question three. It is very hot. What should you do?",
    "Question four. It will be rainy later. What should you bring?",
    "Question five. What is your favorite weather? Why?",
]

TRACKS = [
    {"n": "01", "title": "Vocabulario clave",
     "instr": "Escucha cada palabra y su ejemplo. Repite en voz alta durante la pausa.",
     "segments": vocab_segments(VOCAB)},
    {"n": "02", "title": "Lectura: Today's Weather Forecast",
     "instr": "Escucha el pronóstico mientras lo sigues con el dedo en tu libro.",
     "segments": [(VAL, p, 1.0) for p in READING]},
    {"n": "03", "title": "Chant: What Will the Weather Be?",
     "instr": "Escucha el chant y repítelo. Marca el ritmo con palmadas.",
     "segments": [(NAR, l, 0.5) for l in CHANT]},
    {"n": "04", "title": "Listening — Práctica: A Trip to the River",
     "instr": "Escucha el diálogo dos veces. La primera vez, solo escucha. La segunda vez, responde.",
     "segments": [(v, t, 0.6) for v, t in DIALOGUE_PRACTICE]},
    {"n": "05", "title": "Listening — Mini-test: Sports Day Weather",
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
     "es": "Hoy el tiempo estará soleado con algo de lluvia más tarde.",
     "goals": ["Decir cómo **será** el tiempo: *It **will be** sunny in the morning.*",
               "Entender un pronóstico: temperatura, grados y momentos del día (*in the afternoon, later, at night*).",
               "Dar consejos según el tiempo: *You **should** bring an umbrella.*"]},

    # ---------------------------------------------------- EMPIEZA AQUÍ ----
    H1("¿Te sientes perdido? Empieza aquí"),
    P("Si en clase no entendiste el tema, lee esta página primero. Aquí está **lo esencial** en una sola hoja."),
    H3("1. Las 10 palabras que más vas a escuchar"),
    TABLE([2200, 2700, 2200, 2700], ["Inglés", "Español", "Inglés", "Español"], [
        ["weather", "el tiempo, el clima", "storm", "tormenta"],
        ["sunny", "soleado", "forecast", "pronóstico"],
        ["rainy", "lluvioso", "temperature", "temperatura"],
        ["cloudy", "nublado", "hot / cold", "caluroso / frío"],
        ["windy", "con viento", "umbrella", "paraguas"],
    ]),
    H3("2. El tiempo hoy y el tiempo mañana"),
    TABLE([4900, 4900], ["Ahora (presente)", "Después (futuro con will)"], [
        ["It **is** sunny.", "It **will be** sunny."],
        ["It **is** hot.", "It **will be** hot tomorrow."],
        ["There **is** a storm.", "There **will be** a storm at night."],
    ]),
    H3("3. Un consejo con should"),
    P("*It will be rainy. You **should** bring an umbrella.* = Va a llover. **Deberías** llevar paraguas."),
    H3("4. Un pronóstico modelo"),
    P("*Today the weather will be sunny in the morning. Later, it will be rainy. The temperature will be 28 degrees. You should bring an umbrella.*"),
    P("Escucha estas palabras en el **Audio 6.1-01** (página de Vocabulario)."),
    PB,

    # ---------------------------------------------------- VOCABULARIO ----
    H1("1. Vocabulario"),
    P("Escucha el audio, señala cada palabra y repítela en voz alta. La columna **Se pronuncia** te da una ayuda aproximada; el audio es la pronunciación correcta."),
    audio("01"),
    TABLE([2100, 1700, 2300, 3700], ["Inglés", "Se pronuncia", "Español", "Ejemplo"],
          [[f"**{w}**", p, s, f"*{ex}*"] for w, p, s, ex in VOCAB]),
    NOTE("Momentos del día",
         "**in the morning** en la mañana · **at noon** al mediodía · **in the afternoon** en la tarde · **in the evening** al anochecer · **at night** de noche · **later** más tarde · **tomorrow** mañana"),
    NOTE("De sustantivo a adjetivo: + y",
         "sun → sun**ny** · rain → rain**y** · cloud → cloud**y** · wind → wind**y**   (*The sun is hot. → It is sunny.*)"),
    PB,

    # ---------------------------------------------------- LECTURA ----
    H1("2. Lectura: Today's Weather Forecast"),
    P("Lee el texto dos veces. La primera vez, en silencio. La segunda, en voz alta o junto con el audio."),
    audio("02"),
    READ("Today's Weather Forecast", READING),
    H2("Chant: What Will the Weather Be?"),
    P("Escucha y repite. Marca el ritmo con palmadas."),
    audio("03"),
    POEM(CHANT),
    PB,

    # ---------------------------------------------------- GRAMÁTICA ----
    H1("3. Gramática del tema"),
    H2("A. Futuro con will"),
    P("Usamos **will + verbo** para decir lo que **va a pasar**: el pronóstico del tiempo, planes y predicciones."),
    TABLE([3300, 3300, 3200], ["Afirmativa", "Negativa", "Pregunta"], [
        ["It **will be** sunny.", "It **won't be** cold.", "**Will** it **be** hot?"],
        ["There **will be** a storm.", "It **won't rain** tomorrow.", "**Will** it **rain**?"],
    ]),
    P("*will* es igual para todas las personas: I will, you will, she will, it will... · Contracción: **won't** = will not · Respuestas cortas: *Yes, it **will**. / No, it **won't**.*"),
    H2("B. Should para dar consejos"),
    P("**should + verbo** = deberías / es buena idea. También es igual para todas las personas."),
    TABLE([4900, 4900], ["Situación", "Consejo"], [
        ["It will be rainy.", "You **should bring** an umbrella."],
        ["It is hot.", "You **should drink** water."],
        ["It will be cold at night.", "You **should wear** a jacket."],
        ["There will be a storm.", "You **shouldn't go** to the beach."],
    ]),
    H2("C. La temperatura"),
    P("*The temperature **is** 28 degrees.* · *It **will be** 30 degrees.* · *The temperature **will go down** to 22 degrees.* (bajará) · *...**will go up** to 32.* (subirá)"),
    NOTE("Errores comunes",
         "✗ It will **is** sunny.  ✓ It will **be** sunny.   (después de *will*, el verbo en forma base)",
         "✗ It will **rains**.  ✓ It will **rain**.   ·   ✗ You should **to** bring...  ✓ You should **bring**...",
         "✗ It is **sun**.  ✓ It is **sunny**.   (para describir el tiempo, el adjetivo con -y)"),
    PB,

    # ---------------------------------------------------- LISTENING ----
    H1("4. Listening (Escuchar)"),
    H2("Práctica: A Trip to the River"),
    P("Diego y Ana planean ir al río. **Primera vez:** solo escucha. **Segunda vez:** responde. Si lo necesitas, usa la velocidad lenta."),
    audio("04"),
    P("**Ejemplo:** They want to go to the ______ on Saturday. → **river**"),
    ITEMS("1. What will the weather be like in the morning?"),
    OPTS("a) rainy", "b) sunny", "c) cloudy"),
    ITEMS("2. In the afternoon it will be ______________, and later it will be rainy."),
    ITEMS("3. What time will they go?"),
    OPTS("a) at six o'clock", "b) at eight o'clock", "c) in the afternoon"),
    ITEMS("4. The temperature will be about ______________ degrees."),
    ITEMS("5. Why will they bring an umbrella?"),
    OPTS("a) for the sun", "b) for the wind", "c) for the rain later"),
    *test_blocks(TESTS["listening"], audio),
    PB,

    # ---------------------------------------------------- READING ----
    H1("5. Reading (Leer)"),
    H2("Práctica (texto: Today's Weather Forecast)"),
    P("**A. True or False.** Escribe T o F. Si es falso, corrige la oración."),
    P("**Ejemplo:** It will be sunny in the morning. → **T**"),
    ITEMS("1. The temperature will be 22 degrees in the morning. ______", "2. In the afternoon, it will be cloudy and windy. ______",
          "3. It will be hot at night. ______", "4. It will not rain tomorrow. ______"),
    P("**B. Completa con una palabra del banco:** *umbrella · storm · water · walk*"),
    ITEMS("1. It is hot, so you should drink ______________.", "2. Later, it will be rainy with a small ______________.",
          "3. You should bring an ______________ and a jacket.", "4. Tomorrow will be a good day for a ______________."),
    *test_blocks(TESTS["reading"], audio),
    PB,

    # ---------------------------------------------------- WRITING ----
    H1("6. Writing (Escribir)"),
    H2("Práctica"),
    P("**A. Escribe una oración con will** usando el tiempo y el momento del día."),
    P("**Ejemplo:** soleado · in the morning → **It will be sunny in the morning.**"),
    ITEMS("1. nublado · in the afternoon → ______________________________", "2. lluvioso · at night → ______________________________",
          "3. con viento · tomorrow → ______________________________", "4. 30 grados → The temperature ______________________________"),
    P("**B. Escribe un consejo con should.**"),
    P("**Ejemplo:** It will be rainy. → **You should bring an umbrella.**"),
    ITEMS("1. It will be very hot. → ______________________________", "2. It will be cold at night. → ______________________________",
          "3. There will be a storm. → ______________________________"),
    P("**C. Tu pronóstico.** Escribe en tu cuaderno el pronóstico de mañana para tu comunidad (3 a 5 oraciones con *will* y un consejo con *should*)."),
    *test_blocks(TESTS["writing"], audio),
    PB,

    # ---------------------------------------------------- SPEAKING ----
    H1("7. Speaking (Hablar)"),
    H2("Práctica: escucha, repite y grábate"),
    P("**Paso 1.** Escucha cada oración y repítela en la pausa."),
    P("**Paso 2.** Graba en un celular las mismas oraciones."),
    P("**Paso 3.** Escucha tu grabación. Cuida la **w** de *weather, windy, will*: junta los labios como para decir **u** (*uéder, uíndi, uil*)."),
    audio("06"),
    ITEMS(*[f"{i+1}. {s}" for i, s in enumerate(SPEAK_MODELS)]),
    P("**Prepara tu \"Weather Report\".** Mira por la ventana y prepara un reporte de 30 segundos: el tiempo de hoy, el de mañana, la temperatura y un consejo. Preséntalo como un reportero de televisión."),
    *test_blocks(TESTS["speaking"], audio),
    PB,

    # ---------------------------------------------------- MEDIATION ----
    H1("8. Mediation (Ayudar a otros a entender)"),
    P("Mediar es **ayudar a otra persona a entender un mensaje**: lo haces más corto y simple, lo pasas de un idioma a otro o lo explicas con dibujos."),
    H2("Práctica"),
    P("**A. Pronóstico con dibujos.** Dibuja en tu cuaderno 3 símbolos (sol, nube, lluvia) para el pronóstico de la lectura (mañana, tarde, noche) y escribe una **palabra clave** debajo de cada uno."),
    P("**B. Explica en español.** Tu abuela no entiende inglés. Explícale este mensaje en español."),
    NOTE("Mensaje", "*Tomorrow it will be rainy and windy. You should bring an umbrella.*"),
    LINES(1),
    *test_blocks(TESTS["mediation"], audio),
    PB,

    # ---------------------------------------------------- CIERRE ----
    H1("¿Cómo me fue en el Tema 6.1?"),
    P("Anota tus puntajes. Te dicen qué repasar antes de una prueba."),
    TABLE([2600, 1600, 5600], ["Mini-test", "Puntaje", "Si tuviste menos de la mitad, repasa..."],
          [[SKILL_TITLES[k].split(" ")[-1] if k != "speaking" else "Speaking", f"___ / {t['total']}", t["review"]]
           for k, t in TESTS.items()]),
    TABLE([6400, 1100, 1100, 1200], ["Puedo...", "Sí", "Casi", "Todavía no"], [
        ["decir cómo será el tiempo con *will*", "☐", "☐", "☐"],
        ["entender un pronóstico: temperatura y momentos del día", "☐", "☐", "☐"],
        ["dar consejos con *should*", "☐", "☐", "☐"],
        ["escribir un pronóstico corto", "☐", "☐", "☐"],
        ["explicar un pronóstico con dibujos y palabras clave", "☐", "☐", "☐"],
    ]),
    PB,

    # ---------------------------------------------------- RESPUESTAS ----
    H1("Respuestas del Tema 6.1"),
    P("Corrige **solo después de terminar**. Si te equivocaste, lee la explicación: ahí está lo que necesitas aprender."),
    H3("Listening — Práctica"),
    ITEMS("1. **b) sunny.** *It will be sunny in the morning.*",
          "2. **cloudy.** *It will be cloudy, and later it will be rainy.*",
          "3. **b) at eight o'clock.**",
          "4. **thirty** (30). *about thirty degrees.*",
          "5. **c) for the rain later.** *And an umbrella, for the rain later!*"),
    *answer_blocks(TESTS["listening"]),
    H3("Reading — Práctica"),
    ITEMS("A1. **F.** It will be **28** degrees in the morning. (22 es la temperatura más tarde.)",
          "A2. **T.**   A4. **T.** *The forecast says it will not rain tomorrow.*",
          "A3. **F.** It will be **cold** at night.",
          "B. 1. **water** · 2. **storm** · 3. **umbrella** · 4. **walk**"),
    *answer_blocks(TESTS["reading"]),
    H3("Writing — Práctica"),
    ITEMS("A1. **It will be cloudy in the afternoon.**   A2. **It will be rainy at night.**",
          "A3. **It will be windy tomorrow.**   A4. The temperature **will be 30 degrees.**",
          "B. Ejemplos: 1. *You should drink water.* · 2. *You should wear a jacket.* · 3. *You should stay home.*",
          "C. Respuesta libre. Ejemplo: *Tomorrow the weather will be cloudy in the morning. Later, it will be rainy. The temperature will be 25 degrees. You should bring an umbrella.*"),
    *answer_blocks(TESTS["writing"]),
    H3("Mediation — ejemplos de respuesta"),
    ITEMS("Práctica A: mañana: sol, *sunny / hot* · tarde: nube, *cloudy / windy* · noche: lluvia, *rainy / storm / cold*",
          "Práctica B: *Mañana va a llover y a hacer viento. Debes llevar paraguas.*"),
    *answer_blocks(TESTS["mediation"]),
    PB,

    # ---------------------------------------------------- TRANSCRIPCIONES ----
    H1("Transcripciones de los audios del Tema 6.1"),
    P("Si no puedes escuchar un audio, pide a alguien que lo lea o léelo tú en voz alta. Úsalas también para revisar lo que no entendiste."),
    {"t": "transcripts"},
]
