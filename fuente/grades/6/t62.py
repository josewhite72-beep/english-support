# -*- coding: utf-8 -*-
"""6.º · Scenario 6, Theme 2 — How Will the Weather Change Tomorrow?
Fuentes: planeamiento 6_6-2 y módulo GeMA 6_6-2. Marcado: **negrita**, *cursiva*."""
from common import *
from tests_t62 import TESTS

THEME_ID = "6-2"
THEME_TITLE = "How Will the Weather Change Tomorrow?"
SCENARIO = "Scenario 6: Our Weather Report"

NAR, VAL, DIE, ANA = "af_heart", "af_nova", "am_puck", "af_bella"
SPEAKERS = {VAL: "Valeria", DIE: "Diego", ANA: "Ana"}

VOCAB = [
    ("change", "cheinch", "cambiar", "The weather will change tomorrow."),
    ("tomorrow", "tu-MÓ-rou", "mañana (el día siguiente)", "Tomorrow will be sunny."),
    ("tonight", "tu-NÁIT", "esta noche", "Tonight will be cold."),
    ("cool", "cul", "fresco", "Today is cloudy and cool."),
    ("storm / stormy", "storm / STÓR-mi", "tormenta / tormentoso", "Tonight will be stormy."),
    ("cloud", "claud", "nube", "Look at the dark clouds!"),
    ("sky", "scai", "cielo", "The sky is gray."),
    ("all day", "ol dei", "todo el día", "It is going to rain all day."),
    ("go up / go down", "gou ap / gou daun", "subir / bajar", "The temperature will go down tonight."),
    ("first / then", "ferst / den", "primero / luego", "First it will be sunny, then cloudy."),
    ("jacket", "YÁ-ket", "chaqueta, suéter", "You should wear a jacket."),
    ("week", "uik", "semana", "The forecast for the week is rainy."),
]

READING = [
    "Hello, friends! This is the weather forecast for Coclé. Today is cloudy and cool. The temperature is 22 degrees.",
    "Tomorrow will be sunny in the morning. It is going to be hot at noon. The temperature will be 30 degrees. In the afternoon, it will be windy.",
    "There will be a storm at night. The forecast says it will rain. You should bring an umbrella. You should wear a jacket at night. It will be cold.",
    "On Friday, it is going to be rainy all day. The temperature will be 20 degrees. On Saturday, it will be sunny again. It will be a nice day for a walk. Thank you for listening!",
]

CHANT = [
    "What will the weather be?",
    "Sunny, cloudy, windy, rainy!",
    "Tomorrow will be hot and sunny.",
    "Tonight will be cold and stormy.",
    "Look at the clouds! It's going to rain!",
    "Bring your umbrella. The weather will change!",
]

DIALOGUE_PRACTICE = [
    (ANA, "Diego, look at the sky! The clouds are very dark."),
    (DIE, "Oh no! It's going to rain."),
    (ANA, "But we have soccer practice this afternoon."),
    (DIE, "Let's check the forecast on my phone. It says it will rain from three to five o'clock."),
    (ANA, "Will it rain tomorrow?"),
    (DIE, "No, it won't. Tomorrow will be sunny, but very hot. Thirty-three degrees!"),
    (ANA, "Then we should play tomorrow morning, before it gets hot."),
    (DIE, "Good idea. I'm going to tell the coach."),
]

TEST_MONOLOGUE = [
    "Good evening! I'm Valeria, and this is the weather for the week.",
    "On Monday, it will be sunny and hot, thirty-two degrees.",
    "On Tuesday, the weather will change. It will be cloudy in the morning, and there will be a storm in the afternoon.",
    "On Wednesday and Thursday, it's going to rain all day. The temperature will go down to twenty-three degrees. You should wear a jacket.",
    "On Friday, the rain will stop, and it will be sunny again.",
    "Will it be windy on the weekend? Yes, it will. It's a good weekend to fly a kite! Good night!",
]

SPEAK_MODELS = [
    "Look at the clouds! It's going to rain.",
    "Tomorrow will be sunny.",
    "Will it rain tomorrow? No, it won't.",
    "First it will be sunny, then it will be cloudy.",
    "The temperature will go down tonight.",
    "You should wear a jacket.",
]

SPEAK_TEST_Q = [
    "Question one. Look outside. What is the weather like now?",
    "Question two. How will the weather change tomorrow?",
    "Question three. Will it rain tomorrow?",
    "Question four. The sky is very dark. What is going to happen?",
    "Question five. It will be cold tonight. What should you do?",
]

TRACKS = [
    {"n": "01", "title": "Vocabulario clave",
     "instr": "Escucha cada palabra y su ejemplo. Repite en voz alta durante la pausa.",
     "segments": vocab_segments(VOCAB)},
    {"n": "02", "title": "Lectura: Tomorrow's Weather in Coclé",
     "instr": "Escucha el pronóstico mientras lo sigues con el dedo en tu libro.",
     "segments": [(VAL, p, 1.0) for p in READING]},
    {"n": "03", "title": "Chant: The Weather Will Change!",
     "instr": "Escucha el chant y repítelo. Marca el ritmo con palmadas.",
     "segments": [(NAR, l, 0.5) for l in CHANT]},
    {"n": "04", "title": "Listening — Práctica: Dark Clouds",
     "instr": "Escucha el diálogo dos veces. La primera vez, solo escucha. La segunda vez, responde.",
     "segments": [(v, t, 0.6) for v, t in DIALOGUE_PRACTICE]},
    {"n": "05", "title": "Listening — Mini-test: The Weather for the Week",
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
     "es": "¿Cómo cambiará el tiempo mañana?",
     "goals": ["Predecir con lo que **ves**: *Look at the clouds! It's **going to** rain.*",
               "Describir cómo **cambia** el tiempo: *First it will be sunny, then cloudy. The temperature will go down.*",
               "Preguntar y responder: *Will it rain tomorrow? — Yes, it **will**. / No, it **won't**.*"]},

    # ---------------------------------------------------- EMPIEZA AQUÍ ----
    H1("¿Te sientes perdido? Empieza aquí"),
    P("Si en clase no entendiste el tema, lee esta página primero. Aquí está **lo esencial** en una sola hoja."),
    H3("1. Las 10 palabras que más vas a escuchar"),
    TABLE([2200, 2700, 2200, 2700], ["Inglés", "Español", "Inglés", "Español"], [
        ["change", "cambiar", "cloud", "nube"],
        ["tomorrow", "mañana", "sky", "cielo"],
        ["tonight", "esta noche", "go up / go down", "subir / bajar"],
        ["cool", "fresco", "first / then", "primero / luego"],
        ["stormy", "tormentoso", "all day", "todo el día"],
    ]),
    H3("2. Will o going to"),
    TABLE([4900, 4900], ["will = lo que dice el pronóstico", "going to = lo que ya estoy viendo"], [
        ["*The forecast says it **will** rain tomorrow.*", "*Look at the dark clouds! It**'s going to** rain.*"],
    ]),
    H3("3. Pregunta y respuesta corta"),
    P("*Will it rain tomorrow? — Yes, it **will**. / No, it **won't**.*", align="center"),
    H3("4. Cómo cambia el tiempo"),
    P("*First it will be sunny. Then it will be cloudy. Later, it will be rainy. The temperature will go down.*"),
    P("Escucha estas palabras en el **Audio 6.2-01** (página de Vocabulario)."),
    PB,

    # ---------------------------------------------------- VOCABULARIO ----
    H1("1. Vocabulario"),
    P("Escucha el audio, señala cada palabra y repítela en voz alta. La columna **Se pronuncia** te da una ayuda aproximada; el audio es la pronunciación correcta."),
    audio("01"),
    TABLE([2100, 1700, 2300, 3700], ["Inglés", "Se pronuncia", "Español", "Ejemplo"],
          [[f"**{w}**", p, s, f"*{ex}*"] for w, p, s, ex in VOCAB]),
    NOTE("Los días de la semana",
         "**Monday** lunes · **Tuesday** martes · **Wednesday** miércoles · **Thursday** jueves · **Friday** viernes · **Saturday** sábado · **Sunday** domingo  ·  *on Monday* = el lunes"),
    PB,

    # ---------------------------------------------------- LECTURA ----
    H1("2. Lectura: Tomorrow's Weather in Coclé"),
    P("Lee el texto dos veces. La primera vez, en silencio. La segunda, en voz alta o junto con el audio."),
    audio("02"),
    READ("Tomorrow's Weather in Coclé", READING),
    H2("Chant: The Weather Will Change!"),
    P("Escucha y repite. Marca el ritmo con palmadas."),
    audio("03"),
    POEM(CHANT),
    PB,

    # ---------------------------------------------------- GRAMÁTICA ----
    H1("3. Gramática del tema"),
    H2("A. Going to para predicciones con evidencia"),
    P("Usamos **be going to + verbo** cuando **vemos algo** que nos hace pensar que va a pasar."),
    TABLE([3300, 3300, 3200], ["Afirmativa", "Negativa", "Pregunta"], [
        ["It**'s going to** rain.", "It **isn't going to** rain.", "**Is** it **going to** rain?"],
        ["We**'re going to** get wet.", "We **aren't going to** play.", "**Are** we **going to** play?"],
    ]),
    P("Lleva el verbo **be**: I **am** going to · you / we / they **are** going to · he / she / it **is** going to."),
    H2("B. Will o going to: ¿cuál uso?"),
    TABLE([4900, 4900], ["will", "going to"], [
        ["Pronósticos y lo que **creemos**: *The forecast says it will be hot.*", "Lo que **vemos** ahora: *Look at the sky! It's going to rain.*"],
        ["Decisiones del momento: *I'll take my umbrella.*", "Planes ya decididos: *I'm going to tell the coach.*"],
    ]),
    P("En las pruebas casi siempre se aceptan las dos para el tiempo. La pista: si hay **evidencia** (*Look!*, nubes, cielo oscuro), usa **going to**."),
    H2("C. Will it...? Preguntas y respuestas cortas"),
    TABLE([4900, 4900], ["Pregunta", "Respuesta corta"], [
        ["**Will** it rain tomorrow?", "Yes, it **will**. / No, it **won't**."],
        ["**Will** it be cold tonight?", "Yes, it **will**. / No, it **won't**."],
        ["**How will** the weather **change**?", "First it will be sunny, then it will be cloudy."],
    ]),
    H2("D. Palabras para contar un cambio"),
    P("**first** (primero) → **then** (luego) → **later** (más tarde) → **finally** (al final)  ·  The temperature will **go up** (subirá) / **go down** (bajará)."),
    NOTE("Errores comunes",
         "✗ It going to rain.  ✓ It**'s** going to rain.   (falta *is*)",
         "✗ Will it rain? — Yes, it **is**.  ✓ Yes, it **will**.   (la respuesta corta repite *will*)",
         "✗ It will **to** change.  ✓ It will **change**."),
    PB,

    # ---------------------------------------------------- LISTENING ----
    H1("4. Listening (Escuchar)"),
    H2("Práctica: Dark Clouds"),
    P("Ana y Diego ven el cielo antes de su práctica de fútbol. **Primera vez:** solo escucha. **Segunda vez:** responde. Si lo necesitas, usa la velocidad lenta."),
    audio("04"),
    P("**Ejemplo:** The clouds are very ______. → **dark**"),
    ITEMS("1. What does Diego say?"),
    OPTS("a) It's going to be sunny.", "b) It's going to rain.", "c) It's going to be cold."),
    ITEMS("2. It will rain from three to ______________ o'clock."),
    ITEMS("3. Will it rain tomorrow?"),
    OPTS("a) Yes, it will.", "b) No, it won't.", "c) Yes, all day."),
    ITEMS("4. Tomorrow the temperature will be ______________ degrees."),
    ITEMS("5. When are they going to play?"),
    OPTS("a) this afternoon", "b) tomorrow morning", "c) tomorrow afternoon"),
    *test_blocks(TESTS["listening"], audio),
    PB,

    # ---------------------------------------------------- READING ----
    H1("5. Reading (Leer)"),
    H2("Práctica (texto: Tomorrow's Weather in Coclé)"),
    P("**A. Completa la tabla del pronóstico.**"),
    P("**Ejemplo:** Today → **cloudy and cool, 22 degrees**"),
    TABLE([2600, 7200], ["Día / momento", "El tiempo"], [
        ["Tomorrow morning", "______________________________"],
        ["Tomorrow at noon", "______________________________"],
        ["Tomorrow night", "______________________________"],
        ["Friday", "______________________________"],
        ["Saturday", "______________________________"],
    ]),
    P("**B. Responde con una respuesta corta** (*Yes, it will. / No, it won't.*)."),
    ITEMS("1. Will it be hot tomorrow at noon? ______________", "2. Will it be warm tomorrow night? ______________",
          "3. Will it be sunny on Friday? ______________"),
    *test_blocks(TESTS["reading"], audio),
    PB,

    # ---------------------------------------------------- WRITING ----
    H1("6. Writing (Escribir)"),
    H2("Práctica"),
    P("**A. ¿Will o going to?** Completa. Fíjate si hay evidencia (*Look!*)."),
    P("**Ejemplo:** Look at those black clouds! It ______ rain. → **is going to**"),
    ITEMS("1. The forecast says it ______________ be sunny on Monday.", "2. Look at the sky! It ______________ be a storm.",
          "3. ______ it rain tomorrow? — No, it ______________."),
    P("**B. Cuenta cómo cambia el tiempo** con *first, then, later*."),
    P("**Ejemplo:** sol → nubes → lluvia  →  **First it will be sunny, then it will be cloudy. Later, it will rain.**"),
    ITEMS("1. nubes → viento → tormenta → ______________________________________________",
          "2. lluvia → sol → calor → ______________________________________________"),
    P("**C. Tu pronóstico de la semana.** Escribe en tu cuaderno el tiempo de 3 días (*On Monday, it will be...*) y un consejo con *should*."),
    *test_blocks(TESTS["writing"], audio),
    PB,

    # ---------------------------------------------------- SPEAKING ----
    H1("7. Speaking (Hablar)"),
    H2("Práctica: escucha, repite y grábate"),
    P("**Paso 1.** Escucha cada oración y repítela en la pausa."),
    P("**Paso 2.** Graba en un celular las mismas oraciones."),
    P("**Paso 3.** Escucha tu grabación. Cuida la **r** de *rain, rainy*: en inglés la lengua **no toca** el paladar (no es la *r* de *perro*)."),
    audio("06"),
    ITEMS(*[f"{i+1}. {s}" for i, s in enumerate(SPEAK_MODELS)]),
    P("**Prepara tu \"Weekly Weather Report\".** Prepara un reporte de 30 a 60 segundos sobre el tiempo de 3 días, con *will*, *going to*, *first / then* y un consejo."),
    *test_blocks(TESTS["speaking"], audio),
    PB,

    # ---------------------------------------------------- MEDIATION ----
    H1("8. Mediation (Ayudar a otros a entender)"),
    P("Mediar es **ayudar a otra persona a entender un mensaje**: lo haces más corto y simple, lo pasas de un idioma a otro o lo explicas con dibujos."),
    H2("Práctica"),
    P("**A. Diario del tiempo.** Durante 3 días, anota en tu cuaderno el tiempo en inglés con una palabra clave y un dibujo (*Monday: sunny, hot*). Al final, explícale a tu familia **en español** cómo cambió."),
    P("**B. Explica en español.** Tu hermano pequeño no entiende este mensaje. Explícaselo en español."),
    NOTE("Mensaje", "*Look at the clouds! It's going to rain. We aren't going to play outside.*"),
    LINES(1),
    *test_blocks(TESTS["mediation"], audio),
    PB,

    # ---------------------------------------------------- CIERRE ----
    H1("¿Cómo me fue en el Tema 6.2?"),
    P("Anota tus puntajes. Te dicen qué repasar antes de una prueba."),
    TABLE([2600, 1600, 5600], ["Mini-test", "Puntaje", "Si tuviste menos de la mitad, repasa..."],
          [[SKILL_TITLES[k].split(" ")[-1] if k != "speaking" else "Speaking", f"___ / {t['total']}", t["review"]]
           for k, t in TESTS.items()]),
    TABLE([6400, 1100, 1100, 1200], ["Puedo...", "Sí", "Casi", "Todavía no"], [
        ["predecir con *going to* cuando veo algo", "☐", "☐", "☐"],
        ["contar cómo cambia el tiempo (*first, then, later*)", "☐", "☐", "☐"],
        ["preguntar y responder *Will it...? Yes, it will. / No, it won't.*", "☐", "☐", "☐"],
        ["entender un pronóstico de la semana", "☐", "☐", "☐"],
        ["explicar un pronóstico en español", "☐", "☐", "☐"],
    ]),
    PB,

    # ---------------------------------------------------- RESPUESTAS ----
    H1("Respuestas del Tema 6.2"),
    P("Corrige **solo después de terminar**. Si te equivocaste, lee la explicación: ahí está lo que necesitas aprender."),
    H3("Listening — Práctica"),
    ITEMS("1. **b) It's going to rain.** Diego lo dice porque **ve** las nubes oscuras.",
          "2. **five** (5). *from three to five o'clock.*",
          "3. **b) No, it won't.**",
          "4. **thirty-three** (33).",
          "5. **b) tomorrow morning.** *we should play tomorrow morning, before it gets hot.*"),
    *answer_blocks(TESTS["listening"]),
    H3("Reading — Práctica"),
    ITEMS("A. Tomorrow morning: **sunny** · at noon: **hot, 30 degrees** · night: **a storm, rain, cold** · Friday: **rainy all day, 20 degrees** · Saturday: **sunny again**",
          "B1. **Yes, it will.**   B2. **No, it won't.** (It will be cold.)   B3. **No, it won't.** (It is going to be rainy.)"),
    *answer_blocks(TESTS["reading"]),
    H3("Writing — Práctica"),
    ITEMS("A1. **will** (lo dice el pronóstico)   A2. **is going to** (hay evidencia: *Look!*)   A3. **Will** ... **won't**",
          "B1. *First it will be cloudy, then it will be windy. Later, there will be a storm.*",
          "B2. *First it will rain, then it will be sunny. Later, it will be hot.*",
          "C. Respuesta libre. Ejemplo: *On Monday, it will be sunny. On Tuesday, it will be cloudy. On Wednesday, it is going to rain. You should bring an umbrella.*"),
    *answer_blocks(TESTS["writing"]),
    H3("Mediation — ejemplos de respuesta"),
    ITEMS("Práctica A: respuesta libre.",
          "Práctica B: *¡Mira las nubes! Va a llover. No vamos a jugar afuera.*"),
    *answer_blocks(TESTS["mediation"]),
    PB,

    # ---------------------------------------------------- TRANSCRIPCIONES ----
    H1("Transcripciones de los audios del Tema 6.2"),
    P("Si no puedes escuchar un audio, pide a alguien que lo lea o léelo tú en voz alta. Úsalas también para revisar lo que no entendiste."),
    {"t": "transcripts"},
]
