# -*- coding: utf-8 -*-
"""6.º · Scenario 5, Theme 2 — This School Has Been Here a Long Time!
Fuentes: planeamiento 6_5-2 y módulo GeMA 6_5-2. Marcado: **negrita**, *cursiva*."""
from common import *
from tests_t52 import TESTS

THEME_ID = "5-2"
THEME_TITLE = "This School Has Been Here a Long Time!"
SCENARIO = "Scenario 5: Our Amazing Community"

NAR, MAR, GRA, CAR, ROS, CAS = "af_heart", "am_puck", "am_onyx", "af_sky", "af_sarah", "am_michael"
SPEAKERS = {MAR: "Marco", GRA: "Grandpa", CAR: "Carmen", ROS: "Miss Rosa", CAS: "Mr. Castillo"}

VOCAB = [
    ("history", "JÍS-to-ri", "historia", "Our school has a long history."),
    ("since", "sins", "desde", "It has been here since 1965."),
    ("for", "for", "por, durante", "It has been here for sixty years."),
    ("year", "iir", "año", "I have studied here for six years."),
    ("building", "BÍL-ding", "edificio", "The building has changed."),
    ("classroom", "CLÁS-rum", "salón de clases", "There are twelve classrooms."),
    ("principal", "PRÍN-si-pal", "director o directora", "The school has had eight principals."),
    ("student", "STIÚ-dent", "estudiante", "My grandfather was a student there."),
    ("grandfather", "GRÁND-fa-der", "abuelo", "My grandfather remembers the school."),
    ("remember", "ri-MÉM-ber", "recordar", "Do you remember your teacher?"),
    ("change", "cheinch", "cambiar", "Has the school changed?"),
    ("a long time", "a long taim", "mucho tiempo", "She has been a teacher for a long time."),
]

READING = [
    (MAR, "Grandpa, how long has our school been here?"),
    (GRA, "It has been here since 1965. That is a long time!"),
    (MAR, "Were you a student there?"),
    (GRA, "Yes! I was a student there for six years."),
    (MAR, "Has the building changed?"),
    (GRA, "Yes, it has. In 1965 there were only three classrooms. Now there are twelve classrooms."),
    (MAR, "Has the school had many principals?"),
    (GRA, "Yes, it has. It has had eight principals since 1965."),
    (MAR, "Do you remember your teacher?"),
    (GRA, "Of course! Miss Rosa. She was my teacher for two years."),
    (MAR, "Our school has a long history!"),
]

CHANT = [
    "For ten years, for twenty years,",
    "Since the day it opened here!",
    "Has it changed? Yes, it has!",
    "Twelve classrooms, not just three!",
    "Our school has a long history,",
    "A long, long history!",
]

DIALOGUE_PRACTICE = [
    (CAR, "Good morning, Miss Rosa. Can I ask you some questions for the school newspaper?"),
    (ROS, "Of course, Carmen!"),
    (CAR, "How long have you been a teacher?"),
    (ROS, "I have been a teacher for twenty-five years."),
    (CAR, "And how long have you worked at this school?"),
    (ROS, "I have worked here since 2010."),
    (CAR, "Has the school changed?"),
    (ROS, "Yes, it has. We have had a computer room since 2018, and the library is new."),
    (CAR, "What is your favorite place in the school?"),
    (ROS, "The garden. The students have planted many trees."),
    (CAR, "Thank you, Miss Rosa!"),
]

TEST_MONOLOGUE = [
    "Good morning, students and families. I'm Mr. Castillo, the principal.",
    "Today is a very special day. Our school has been here for fifty years! It opened in 1976.",
    "In 1976 there were only four classrooms and one hundred students. Now we have fourteen classrooms and five hundred students.",
    "The school has changed a lot. We have had a new cafeteria since 2015, and the computer room opened last year.",
    "I have been the principal since 2019, and I love this school.",
    "Thank you to all the teachers and families. Happy anniversary!",
]

SPEAK_MODELS = [
    "This school has been here for sixty years.",
    "It has been here since 1965.",
    "How long has it been here?",
    "Has the building changed? Yes, it has.",
    "I have lived here since 2015.",
    "My family has lived here for twenty years.",
]

SPEAK_TEST_Q = [
    "Question one. How long have you been at your school?",
    "Question two. How long have you lived in your community?",
    "Question three. Has your school changed? Say one change.",
    "Question four. How long have you known your best friend?",
    "Question five. Since when have you studied English?",
]

TRACKS = [
    {"n": "01", "title": "Vocabulario clave",
     "instr": "Escucha cada palabra y su ejemplo. Repite en voz alta durante la pausa.",
     "segments": vocab_segments(VOCAB)},
    {"n": "02", "title": "Lectura: Grandpa's School",
     "instr": "Escucha la entrevista mientras la sigues con el dedo en tu libro.",
     "segments": [(v, t, 0.7) for v, t in READING]},
    {"n": "03", "title": "Chant: For Ten Years",
     "instr": "Escucha el chant y repítelo. Marca el ritmo con palmadas.",
     "segments": [(NAR, l, 0.5) for l in CHANT]},
    {"n": "04", "title": "Listening — Práctica: The School Newspaper",
     "instr": "Escucha la entrevista dos veces. La primera vez, solo escucha. La segunda vez, responde.",
     "segments": [(v, t, 0.6) for v, t in DIALOGUE_PRACTICE]},
    {"n": "05", "title": "Listening — Mini-test: Happy Anniversary!",
     "instr": "Mini-test. Escucha dos veces como máximo y responde en tu libro.",
     "segments": [(CAS, t, 0.7) for t in TEST_MONOLOGUE]},
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
     "es": "¡Esta escuela ha estado aquí mucho tiempo!",
     "goals": ["Decir cuánto tiempo lleva algo: *The school **has been** here **for** sixty years.*",
               "Usar **for** (cuánto tiempo) y **since** (desde cuándo): *for ten years · since 1965*.",
               "Preguntar y responder: *How long **has** it **been** here? · Has it changed? — Yes, it **has**.*"]},

    # ---------------------------------------------------- EMPIEZA AQUÍ ----
    H1("¿Te sientes perdido? Empieza aquí"),
    P("Si en clase no entendiste el tema, lee esta página primero. Aquí está **lo esencial** en una sola hoja."),
    H3("1. Las 10 palabras que más vas a escuchar"),
    TABLE([2200, 2700, 2200, 2700], ["Inglés", "Español", "Inglés", "Español"], [
        ["history", "historia", "since", "desde"],
        ["building", "edificio", "for", "por, durante"],
        ["classroom", "salón de clases", "year", "año"],
        ["principal", "director/a", "remember", "recordar"],
        ["student", "estudiante", "change", "cambiar"],
    ]),
    H3("2. La idea del tema"),
    P("El **presente perfecto** (*has / have* + verbo) sirve para algo que **empezó en el pasado y sigue hoy**:"),
    P("*The school **has been** here for sixty years.* = La escuela **ha estado** aquí (y **sigue** aquí) por sesenta años.", align="center"),
    H3("3. For o since: la pregunta que más sale en las pruebas"),
    TABLE([4900, 4900], ["for = cuánto tiempo (una cantidad)", "since = desde cuándo (un momento)"], [
        ["for **ten years**", "since **1965**"],
        ["for **two months**", "since **Monday**"],
        ["for **a long time**", "since **first grade**"],
    ]),
    H3("4. Pregunta y respuesta modelo"),
    P("*How long **has** your school **been** here? — It **has been** here **since** 1990.*"),
    P("Escucha estas palabras en el **Audio 5.2-01** (página de Vocabulario)."),
    PB,

    # ---------------------------------------------------- VOCABULARIO ----
    H1("1. Vocabulario"),
    P("Escucha el audio, señala cada palabra y repítela en voz alta. La columna **Se pronuncia** te da una ayuda aproximada; el audio es la pronunciación correcta."),
    audio("01"),
    TABLE([2100, 1700, 2300, 3700], ["Inglés", "Se pronuncia", "Español", "Ejemplo"],
          [[f"**{w}**", p, s, f"*{ex}*"] for w, p, s, ex in VOCAB]),
    NOTE("Cómo se leen los años", "1965 = *nineteen sixty-five* · 1976 = *nineteen seventy-six* · 2010 = *twenty ten* · 2018 = *twenty eighteen* · 2005 = *two thousand five*"),
    PB,

    # ---------------------------------------------------- LECTURA ----
    H1("2. Lectura: Grandpa's School"),
    P("Marco entrevista a su abuelo. Lee dos veces: en silencio y luego en voz alta o con el audio."),
    audio("02"),
    READ("Grandpa's School (an interview)", [f"**{SPEAKERS[v]}:** {t}" for v, t in READING]),
    H2("Chant: For Ten Years"),
    audio("03"),
    POEM(CHANT),
    PB,

    # ---------------------------------------------------- GRAMÁTICA ----
    H1("3. Gramática del tema"),
    H2("A. Presente perfecto: has / have + participio"),
    P("Habla de algo que **empezó en el pasado y sigue hasta hoy**."),
    TABLE([3300, 3300, 3200], ["Afirmativa", "Negativa", "Pregunta"], [
        ["I / you / we / they **have** lived here.", "I **haven't** lived here.", "**Have** you lived here?"],
        ["he / she / it **has** been here.", "It **hasn't** changed.", "**Has** it changed?"],
    ]),
    P("Contracciones: I**'ve** · you**'ve** · we**'ve** · they**'ve** · he**'s** · she**'s** · it**'s**   ·   Respuestas cortas: *Yes, it **has**. / No, it **hasn't**.*"),
    H2("B. Participios que vas a usar"),
    TABLE([2450, 2450, 2450, 2450], ["Verbo", "Participio", "Verbo", "Participio"], [
        ["be (ser, estar)", "**been**", "live (vivir)", "**lived**"],
        ["have (tener)", "**had**", "work (trabajar)", "**worked**"],
        ["know (conocer)", "**known**", "study (estudiar)", "**studied**"],
        ["teach (enseñar)", "**taught**", "change (cambiar)", "**changed**"],
    ]),
    P("Los verbos regulares terminan en **-ed** (lived, worked, changed). Los irregulares hay que aprenderlos (been, had, known, taught)."),
    H2("C. For y since"),
    BULLETS("**for** + una **cantidad** de tiempo: *for six years · for two weeks · for a long time*",
            "**since** + el **momento** en que empezó: *since 1965 · since Monday · since 7:00 · since first grade*"),
    H2("D. How long...?"),
    P("Para preguntar **cuánto tiempo**: *How long **has** the school **been** here?* · *How long **have** you **lived** here?*"),
    NOTE("Errores comunes",
         "✗ It has been here **since** sixty years.  ✓ It has been here **for** sixty years.  (sixty years es una cantidad)",
         "✗ The school **have** been here...  ✓ The school **has** been here...  (con he / she / it se usa *has*)",
         "✗ I **am** here since 2015.  ✓ I **have been** here since 2015.  (con *since* y *for*, presente perfecto)"),
    PB,

    # ---------------------------------------------------- LISTENING ----
    H1("4. Listening (Escuchar)"),
    H2("Práctica: The School Newspaper"),
    P("Carmen entrevista a Miss Rosa para el periódico escolar. **Primera vez:** solo escucha. **Segunda vez:** responde. Si lo necesitas, usa la velocidad lenta."),
    audio("04"),
    P("**Ejemplo:** Carmen writes for the school ______. → **newspaper**"),
    ITEMS("1. Miss Rosa has been a teacher for ______________ years."),
    ITEMS("2. She has worked at this school:"),
    OPTS("a) for 2010 years", "b) since 2010", "c) since 2018"),
    ITEMS("3. Has the school changed?"),
    OPTS("a) Yes, it has.", "b) No, it hasn't.", "c) She doesn't know."),
    ITEMS("4. The school has had a computer room since ______________."),
    ITEMS("5. Miss Rosa's favorite place in the school is the ______________."),
    *test_blocks(TESTS["listening"], audio),
    PB,

    # ---------------------------------------------------- READING ----
    H1("5. Reading (Leer)"),
    H2("Práctica (texto: Grandpa's School)"),
    P("**A. Responde con una oración completa.**"),
    P("**Ejemplo:** Since when has the school been here? → **It has been here since 1965.**"),
    ITEMS("1. How many classrooms were there in 1965?  ______________________________",
          "2. How many classrooms are there now?  ______________________________",
          "3. How many principals has the school had?  ______________________________",
          "4. How long was Miss Rosa Grandpa's teacher?  ______________________________"),
    P("**B. True or False.** Escribe T o F."),
    ITEMS("1. Grandpa was a student at the school for six years. ______",
          "2. The building hasn't changed. ______",
          "3. Marco thinks the school has a long history. ______"),
    *test_blocks(TESTS["reading"], audio),
    PB,

    # ---------------------------------------------------- WRITING ----
    H1("6. Writing (Escribir)"),
    H2("Práctica"),
    P("**A. Completa con for o since.**"),
    P("**Ejemplo:** The school has been here ______ 1965. → **since**"),
    ITEMS("1. My family has lived here ______ twenty years.", "2. I have been in sixth grade ______ March.",
          "3. Miss Rosa has been a teacher ______ a long time.", "4. The market has been open ______ 7:00 a.m.",
          "5. We have been friends ______ three years."),
    P("**B. Completa con has o have y el participio.**"),
    P("**Ejemplo:** The school ______ (be) here for 50 years. → **has been**"),
    ITEMS("1. I ______________ (live) in this community since 2016.",
          "2. The building ______________ (change) a lot.",
          "3. ______ you ______________ (know) your best friend for a long time?"),
    P("**C. Escribe 3 preguntas de entrevista** para un familiar mayor. **Modelo:** *How long have you lived in this community? Has the school changed?*"),
    LINES(3),
    *test_blocks(TESTS["writing"], audio),
    PB,

    # ---------------------------------------------------- SPEAKING ----
    H1("7. Speaking (Hablar)"),
    H2("Práctica: escucha, repite y grábate"),
    P("**Paso 1.** Escucha cada oración y repítela en la pausa."),
    P("**Paso 2.** Graba en un celular las mismas oraciones."),
    P("**Paso 3.** Escucha tu grabación y compárala con el audio. Fíjate en la **h** de *has, have, history*: suena como una **j suave** del español."),
    audio("06"),
    ITEMS(*[f"{i+1}. {s}" for i, s in enumerate(SPEAK_MODELS)]),
    P("**Prepara tu presentación: \"Our School History\".** Haz una línea de tiempo con 4 fechas de tu escuela o comunidad y escribe 4 oraciones con *has been / has had / has changed* y *for* o *since*. Practícala hasta decirla **sin leer**."),
    *test_blocks(TESTS["speaking"], audio),
    PB,

    # ---------------------------------------------------- MEDIATION ----
    H1("8. Mediation (Ayudar a otros a entender)"),
    P("Mediar es **ayudar a otra persona a entender un mensaje**: lo haces más corto y simple, o lo pasas de un idioma a otro."),
    H2("Práctica"),
    P("**A. Entrevista en casa.** Pregunta a un familiar mayor (en español): *¿Desde cuándo existe la escuela? ¿Qué ha cambiado?* Escribe 3 datos **en inglés**."),
    P("**Ejemplo:** *Hay comedor nuevo desde 2015.* → *The school has had a new cafeteria since 2015.*"),
    LINES(3),
    P("**B. Explica en español.** Tu abuela no entiende esta placa de la escuela. Escribe en español qué dice."),
    NOTE("Placa", "*This school has served our community since 1965.*"),
    LINES(1),
    *test_blocks(TESTS["mediation"], audio),
    PB,

    # ---------------------------------------------------- CIERRE ----
    H1("¿Cómo me fue en el Tema 5.2?"),
    P("Anota tus puntajes. Te dicen qué repasar antes de una prueba."),
    TABLE([2600, 1600, 5600], ["Mini-test", "Puntaje", "Si tuviste menos de la mitad, repasa..."],
          [[SKILL_TITLES[k].split(" ")[-1] if k != "speaking" else "Speaking", f"___ / {t['total']}", t["review"]]
           for k, t in TESTS.items()]),
    TABLE([6400, 1100, 1100, 1200], ["Puedo...", "Sí", "Casi", "Todavía no"], [
        ["decir cuánto tiempo lleva algo (*has been here for...*)", "☐", "☐", "☐"],
        ["elegir entre **for** y **since**", "☐", "☐", "☐"],
        ["preguntar *How long has...?* y *Has it changed?*", "☐", "☐", "☐"],
        ["entender una entrevista o un discurso sobre una escuela", "☐", "☐", "☐"],
        ["entrevistar a un familiar y escribir los datos en inglés", "☐", "☐", "☐"],
    ]),
    PB,

    # ---------------------------------------------------- RESPUESTAS ----
    H1("Respuestas del Tema 5.2"),
    P("Corrige **solo después de terminar**. Si te equivocaste, lee la explicación: ahí está lo que necesitas aprender."),
    H3("Listening — Práctica"),
    ITEMS("1. **twenty-five** (25). *I have been a teacher for twenty-five years.*",
          "2. **b) since 2010.** 2010 es un **momento**, por eso va con *since*. (*for 2010 years* no tiene sentido.)",
          "3. **a) Yes, it has.**",
          "4. **2018** (*twenty eighteen*).",
          "5. **garden.** *The garden. The students have planted many trees.*"),
    *answer_blocks(TESTS["listening"]),
    H3("Reading — Práctica"),
    ITEMS("A1. *There were three classrooms.*   A2. *There are twelve classrooms.*",
          "A3. *It has had eight principals.*   A4. *She was his teacher for two years.*",
          "B1. **T.**   B2. **F.** It **has** changed: de 3 a 12 salones.   B3. **T.** *Our school has a long history!*"),
    *answer_blocks(TESTS["reading"]),
    H3("Writing — Práctica"),
    ITEMS("A1. **for** (cantidad)   A2. **since** (momento)   A3. **for** (cantidad)   A4. **since** (hora = momento)   A5. **for**",
          "B1. **have lived**   B2. **has changed**   B3. **Have** you **known**...?",
          "C. Ejemplos: *How long have you lived here? · Has the school changed? · Who was your teacher?*"),
    *answer_blocks(TESTS["writing"]),
    H3("Mediation — ejemplos de respuesta"),
    ITEMS("Práctica A: respuesta libre. Ejemplo: *The school has been here since 1980. It has had a new library since 2012.*",
          "Práctica B: *Esta escuela ha servido a nuestra comunidad desde 1965.*"),
    *answer_blocks(TESTS["mediation"]),
    PB,

    # ---------------------------------------------------- TRANSCRIPCIONES ----
    H1("Transcripciones de los audios del Tema 5.2"),
    P("Si no puedes escuchar un audio, pide a alguien que lo lea o léelo tú en voz alta. Úsalas también para revisar lo que no entendiste."),
    {"t": "transcripts"},
]
