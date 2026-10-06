# -*- coding: utf-8 -*-
"""5.º · Scenario 6, Theme 1 — We Recycle Plastic Bottles Every Day.
Fuentes: planeamiento 5_6-1 y módulo GeMA 5_6-1. Marcado: **negrita**, *cursiva*."""
from common import *
from tests_t61 import TESTS

THEME_ID = "6-1"
THEME_TITLE = "We Recycle Plastic Bottles Every Day."
SCENARIO = "Scenario 6: Recycling for Our World"

NAR, ANA, DIE, CAS = "af_heart", "af_bella", "am_puck", "am_michael"
SPEAKERS = {ANA: "Ana", DIE: "Diego", CAS: "Mr. Castillo"}

VOCAB = [
    ("plastic", "PLÁS-tik", "plástico", "We recycle plastic every day."),
    ("bottles", "BÓ-tels", "botellas", "There are bottles in the bin."),
    ("recycle", "ri-SÁI-kel", "reciclar", "We recycle paper and plastic."),
    ("recycling", "ri-SÁI-cling", "reciclaje", "Recycling is good for the environment."),
    ("trash", "trash", "basura", "There is trash in the bin."),
    ("bin", "bin", "recipiente, tinaco de basura", "There is a bin in the classroom."),
    ("paper", "PÉI-per", "papel", "We put paper in the blue bin."),
    ("environment", "en-VÁI-ron-ment", "medio ambiente", "We can help the environment."),
    ("waste", "ueist", "desechos", "There is no waste in our classroom."),
    ("program", "PRÓU-gram", "programa", "There is a recycling program in my school."),
    ("compost", "CÓM-post", "abono, composta", "We can make compost with food scraps."),
    ("food scraps", "fud scraps", "restos de comida", "We use food scraps for compost."),
]

READING = [
    "Hello. My name is Ana. I am a student at C.E.B.G. Barrigón. There is a recycling program in my school.",
    "We recycle plastic bottles every day. There is a big bin in the classroom. We put plastic bottles and paper in the bin. There is also a bin for trash.",
    "We can recycle paper in the school. We can make compost with food scraps. There is a recycling center in the community. The recycling center helps the environment.",
    "We can help the environment too. We recycle plastic, paper, and food scraps. There is no waste in our classroom. We are happy with our recycling program.",
]

CHANT = [
    "Recycle, recycle, every day!",
    "Plastic bottles in the bin, hooray!",
    "Compost, compost, food scraps too,",
    "There is a program for me and you.",
    "We can help the environment, yes, we can!",
    "Recycling is good for everyone!",
]

DIALOGUE_PRACTICE = [
    (DIE, "Hi, Ana! I'm new here. Where do I put this plastic bottle?"),
    (ANA, "Put it in the blue bin. We recycle plastic bottles every day."),
    (DIE, "Could you repeat that, please?"),
    (ANA, "Sure! The blue bin is for plastic and paper."),
    (DIE, "And where do I put my banana peel?"),
    (ANA, "In the green bin. We make compost with food scraps."),
    (DIE, "Is there a bin for trash?"),
    (ANA, "Yes, there is. It's the black bin, next to the door."),
    (DIE, "Thanks! Your classroom is very clean."),
]

TEST_MONOLOGUE = [
    "Good morning, students. This is Mr. Castillo, the principal.",
    "Our school has a new recycling program! There are three bins in every classroom.",
    "The blue bin is for plastic bottles. The yellow bin is for paper. The green bin is for food scraps.",
    "We recycle plastic bottles every day, and on Fridays we take them to the recycling center in the community.",
    "Last month, we recycled two hundred bottles!",
    "We can all help the environment. Thank you!",
]

SPEAK_MODELS = [
    "We recycle plastic bottles every day.",
    "There is a bin in the classroom.",
    "There are bottles in the bin.",
    "We can make compost with food scraps.",
    "Could you repeat that, please?",
    "We can help the environment.",
]

SPEAK_TEST_Q = [
    "Question one. What do you recycle at home?",
    "Question two. Is there a recycling bin in your classroom?",
    "Question three. What can we make with food scraps?",
    "Question four. How can you help the environment?",
    "Question five. You don't understand your teacher. What can you say?",
]

TRACKS = [
    {"n": "01", "title": "Vocabulario clave",
     "instr": "Escucha cada palabra y su ejemplo. Repite en voz alta durante la pausa.",
     "segments": vocab_segments(VOCAB)},
    {"n": "02", "title": "Lectura: Our Recycling Program",
     "instr": "Escucha el texto mientras lo sigues con el dedo en tu libro.",
     "segments": [(ANA, p, 1.0) for p in READING]},
    {"n": "03", "title": "Chant: Recycle, Recycle!",
     "instr": "Escucha el chant y repítelo. Marca el ritmo con palmadas.",
     "segments": [(NAR, l, 0.5) for l in CHANT]},
    {"n": "04", "title": "Listening — Práctica: Which Bin?",
     "instr": "Escucha el diálogo dos veces. La primera vez, solo escucha. La segunda vez, responde.",
     "segments": [(v, t, 0.6) for v, t in DIALOGUE_PRACTICE]},
    {"n": "05", "title": "Listening — Mini-test: Our New Program",
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
    {"t": "theme_cover", "scenario": SCENARIO, "theme": "Theme 1: " + THEME_TITLE,
     "es": "Reciclamos botellas de plástico todos los días.",
     "goals": ["Decir lo que hacemos siempre: *We **recycle** plastic bottles every day.*",
               "Decir lo que hay: *There **is** a bin. There **are** two bins.*",
               "Decir lo que podemos hacer y pedir ayuda con cortesía: *We **can** help. **Could** you repeat that, please?*"]},

    H1("¿Te sientes perdido? Empieza aquí"),
    P("Si en clase no entendiste el tema, lee esta página primero. Aquí está **lo esencial** en una sola hoja."),
    H3("1. Las 10 palabras que más vas a escuchar"),
    TABLE([2200, 2700, 2200, 2700], ["Inglés", "Español", "Inglés", "Español"], [
        ["plastic", "plástico", "bin", "tinaco, recipiente"],
        ["bottles", "botellas", "paper", "papel"],
        ["recycle", "reciclar", "environment", "medio ambiente"],
        ["trash", "basura", "compost", "abono"],
        ["waste", "desechos", "food scraps", "restos de comida"],
    ]),
    H3("2. Tres estructuras del tema"),
    TABLE([3400, 6400], ["Estructura", "Ejemplo"], [
        ["We + verbo (siempre)", "*We **recycle** plastic bottles every day.*"],
        ["There is / There are (hay)", "*There **is** a bin. There **are** bottles in the bin.*"],
        ["can (se puede) / Could you...? (cortesía)", "*We **can** make compost.*  ·  ***Could** you repeat that, please?*"],
    ]),
    H3("3. Una descripción modelo"),
    P("*There is a recycling program in my school. We recycle plastic bottles every day. There are two bins in my classroom. We can help the environment.*"),
    P("Escucha estas palabras en el **Audio 6.1-01** (página de Vocabulario)."),
    PB,

    H1("1. Vocabulario"),
    P("Escucha el audio, señala cada palabra y repítela en voz alta. La columna **Se pronuncia** te da una ayuda aproximada; el audio es la pronunciación correcta."),
    audio("01"),
    TABLE([2100, 1700, 2300, 3700], ["Inglés", "Se pronuncia", "Español", "Ejemplo"],
          [[f"**{w}**", p, s, f"*{ex}*"] for w, p, s, ex in VOCAB]),
    NOTE("Aplaude las sílabas", "plas-tic (2) · bot-tles (2) · re-cy-cle (3) · en-vi-ron-ment (4) · pro-gram (2)"),
    PB,

    H1("2. Lectura: Our Recycling Program"),
    P("Lee el texto dos veces. La primera vez, en silencio. La segunda, en voz alta o junto con el audio."),
    audio("02"),
    READ("Our Recycling Program", READING),
    H2("Chant: Recycle, Recycle!"),
    P("Escucha y repite. Marca el ritmo con palmadas."),
    audio("03"),
    POEM(CHANT),
    PB,

    H1("3. Gramática del tema"),
    H2("A. Presente simple con we"),
    P("Para lo que hacemos **siempre o todos los días**. Con *we, you, they* el verbo va **sin cambio**."),
    TABLE([3300, 3300, 3200], ["Afirmativa", "Negativa", "Pregunta"], [
        ["We **recycle** paper.", "We **don't throw** trash on the floor.", "**Do** you **recycle** at home?"],
        ["We **put** bottles in the bin.", "We **don't waste** food.", "**Do** you **make** compost?"],
    ]),
    P("Palabras de frecuencia: *every day* (todos los días) · *on Fridays* (los viernes) · *always* (siempre)"),
    H2("B. There is / There are"),
    TABLE([3300, 3300, 3200], ["Una cosa", "Varias cosas", "Pregunta"], [
        ["There **is** a bin.", "There **are** three bins.", "**Is there** a bin for trash?"],
        ["There **isn't** any trash.", "There **aren't** any bottles.", "**Are there** bottles?"],
    ]),
    H2("C. can y could"),
    BULLETS("**can** = se puede, es posible: *We **can** recycle paper.* · *We **can** make compost.*",
            "**Could you...?** = pedir algo con **cortesía**: *Could you repeat that, please?* · *Could you help me, please?*"),
    NOTE("Errores comunes",
         "✗ There **is** two bins.  ✓ There **are** two bins.   ✗ There **are** a bin.  ✓ There **is** a bin.",
         "✗ We **recycles** paper.  ✓ We **recycle** paper.   (con *we*, sin -s)",
         "✗ We can **to** recycle.  ✓ We can **recycle**."),
    PB,

    H1("4. Listening (Escuchar)"),
    H2("Práctica: Which Bin?"),
    P("Diego es nuevo y le pregunta a Ana dónde poner la basura. **Primera vez:** solo escucha. **Segunda vez:** responde."),
    audio("04"),
    P("**Ejemplo:** Diego has a plastic ______. → **bottle**"),
    ITEMS("1. The plastic bottle goes in the ______________ bin."),
    ITEMS("2. What does Diego say when he doesn't understand?"),
    OPTS("a) What?", "b) Could you repeat that, please?", "c) I don't know."),
    ITEMS("3. The banana peel goes in the:"),
    OPTS("a) blue bin", "b) green bin", "c) black bin"),
    ITEMS("4. The bin for trash is next to the ______________."),
    ITEMS("5. Is there a bin for trash?  ______________"),
    *test_blocks(TESTS["listening"], audio),
    PB,

    H1("5. Reading (Leer)"),
    H2("Práctica (texto: Our Recycling Program)"),
    P("**A. True or False.** Escribe T o F. Si es falso, corrige la oración."),
    P("**Ejemplo:** Ana is a student at C.E.B.G. Barrigón. → **T**"),
    ITEMS("1. They recycle plastic bottles every day. ______", "2. There is a small bin in the classroom. ______",
          "3. They make compost with food scraps. ______", "4. There is a lot of waste in the classroom. ______"),
    P("**B. Completa con una palabra del texto.**"),
    ITEMS("1. There is a recycling ______________ in my school.", "2. We put plastic bottles and ______________ in the bin.",
          "3. The recycling center helps the ______________."),
    *test_blocks(TESTS["reading"], audio),
    PB,

    H1("6. Writing (Escribir)"),
    H2("Práctica"),
    P("**A. Completa con There is o There are.**"),
    P("**Ejemplo:** ______ a bin in the classroom. → **There is**"),
    ITEMS("1. ______________ two bins in the school yard.", "2. ______________ a recycling center in my community.",
          "3. ______________ plastic bottles in the blue bin.", "4. ______________ a program for recycling."),
    P("**B. Escribe una oración con We + verbo.**"),
    P("**Ejemplo:** recycle / paper → **We recycle paper.**"),
    ITEMS("1. put / bottles in the bin → ______________________________", "2. make / compost → ______________________________",
          "3. help / the environment → ______________________________"),
    P("**C. Mi salón.** En tu cuaderno, escribe 3 oraciones sobre el reciclaje en tu salón o tu casa (*There is... / We recycle... / We can...*)."),
    *test_blocks(TESTS["writing"], audio),
    PB,

    H1("7. Speaking (Hablar)"),
    H2("Práctica: escucha, repite y grábate"),
    P("**Paso 1.** Escucha cada oración y repítela en la pausa."),
    P("**Paso 2.** Graba en un celular las mismas oraciones."),
    P("**Paso 3.** Escucha tu grabación. Cuida *recycle* /ri-SÁI-kel/: el acento va en la segunda sílaba."),
    audio("06"),
    ITEMS(*[f"{i+1}. {s}" for i, s in enumerate(SPEAK_MODELS)]),
    P("**Prepara tu presentación: \"Our Recycling Program\".** Di 4 oraciones sobre el reciclaje en tu escuela o tu casa: qué hay, qué reciclan y qué pueden hacer. Practícala hasta decirla **sin leer**."),
    *test_blocks(TESTS["speaking"], audio),
    PB,

    H1("8. Mediation (Ayudar a otros a entender)"),
    P("Mediar es **ayudar a otra persona a entender un mensaje**: lo haces más corto y simple, o lo pasas de un idioma a otro."),
    H2("Práctica"),
    P("**A. Letreros para los tinacos.** Dibuja en tu cuaderno 3 tinacos y escribe un letrero corto en inglés para cada uno (*Plastic bottles · Paper · Food scraps*)."),
    P("**B. Explica en español.** Tu abuela no entiende este letrero. Escribe en español qué dice."),
    NOTE("Letrero", "*Please put plastic bottles in the blue bin. Thank you for helping the environment!*"),
    LINES(1),
    *test_blocks(TESTS["mediation"], audio),
    PB,

    H1("¿Cómo me fue en el Tema 6.1?"),
    P("Anota tus puntajes. Te dicen qué repasar antes de una prueba."),
    TABLE([2600, 1600, 5600], ["Mini-test", "Puntaje", "Si tuviste menos de la mitad, repasa..."],
          [[SKILL_TITLES[k].split(" ")[-1] if k != "speaking" else "Speaking", f"___ / {t['total']}", t["review"]]
           for k, t in TESTS.items()]),
    TABLE([6400, 1100, 1100, 1200], ["Puedo...", "Sí", "Casi", "Todavía no"], [
        ["decir lo que hacemos siempre (*We recycle...*)", "☐", "☐", "☐"],
        ["usar *There is / There are* correctamente", "☐", "☐", "☐"],
        ["decir lo que podemos hacer con *can*", "☐", "☐", "☐"],
        ["pedir algo con cortesía (*Could you...?*)", "☐", "☐", "☐"],
        ["hacer letreros simples en inglés", "☐", "☐", "☐"],
    ]),
    PB,

    H1("Respuestas del Tema 6.1"),
    P("Corrige **solo después de terminar**. Si te equivocaste, lee la explicación: ahí está lo que necesitas aprender."),
    H3("Listening — Práctica"),
    ITEMS("1. **blue.** *Put it in the blue bin.*",
          "2. **b) Could you repeat that, please?** Es la forma cortés de pedir que repitan.",
          "3. **b) green bin.** *We make compost with food scraps.*",
          "4. **door.**   5. **Yes, there is.**"),
    *answer_blocks(TESTS["listening"]),
    H3("Reading — Práctica"),
    ITEMS("A1. **T.**   A3. **T.**",
          "A2. **F.** There is a **big** bin in the classroom.",
          "A4. **F.** There is **no** waste in the classroom.",
          "B. 1. **program** · 2. **paper** · 3. **environment**"),
    *answer_blocks(TESTS["reading"]),
    H3("Writing — Práctica"),
    ITEMS("A1. **There are** (dos)   A2. **There is**   A3. **There are** (varias botellas)   A4. **There is**",
          "B1. **We put bottles in the bin.**   B2. **We make compost.**   B3. **We help the environment.**",
          "C. Ejemplo: *There is a blue bin in my classroom. We recycle paper. We can make compost at home.*"),
    *answer_blocks(TESTS["writing"]),
    H3("Mediation — ejemplos de respuesta"),
    ITEMS("Práctica A: respuesta libre.",
          "Práctica B: *Por favor, pongan las botellas de plástico en el tinaco azul. ¡Gracias por ayudar al medio ambiente!*"),
    *answer_blocks(TESTS["mediation"]),
    PB,

    H1("Transcripciones de los audios del Tema 6.1"),
    P("Si no puedes escuchar un audio, pide a alguien que lo lea o léelo tú en voz alta. Úsalas también para revisar lo que no entendiste."),
    {"t": "transcripts"},
]
