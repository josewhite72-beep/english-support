# -*- coding: utf-8 -*-
"""5.º · Scenario 6, Theme 2 — Composting Is Easy.
Fuentes: planeamiento 5_6-2 y módulo GeMA 5_6-2. Marcado: **negrita**, *cursiva*."""
from common import *
from tests_t62 import TESTS

THEME_ID = "6-2"
THEME_TITLE = "Composting Is Easy."
SCENARIO = "Scenario 6: Recycling for Our World"

NAR, ANA, DIE, ROS = "af_heart", "af_bella", "am_puck", "af_sarah"
SPEAKERS = {ANA: "Ana", DIE: "Diego", ROS: "Mrs. Rosa"}

VOCAB = [
    ("compost", "CÓM-post", "abono, composta", "Compost is good for plants."),
    ("food scraps", "fud scraps", "restos de comida", "We put food scraps in the compost bin."),
    ("leaves", "livs", "hojas (de árbol)", "We can add dry leaves."),
    ("soil", "soil", "tierra", "Compost makes the soil rich."),
    ("water", "UÓ-ter", "agua; regar", "We water the compost every week."),
    ("mix", "mix", "mezclar", "Then we mix it with a stick."),
    ("plants", "plants", "plantas", "Compost helps the plants grow."),
    ("garden", "GÁR-den", "huerto, jardín", "We use compost in the school garden."),
    ("first / then / finally", "ferst / den / FÁI-na-li", "primero / luego / al final", "First, we collect food scraps."),
    ("waste", "ueist", "desechos", "Composting reduces waste."),
    ("easy", "Í-si", "fácil", "Composting is easy."),
    ("could", "cud", "podía, podíamos", "We could make compost last year."),
]

READING = [
    "My name is Ana. I am in Grade 5. My school is C.E.B.G. Barrigón. Our school has a recycling program. We recycle plastic bottles and paper.",
    "There is a big bin in the classroom. There are two bins in the school yard. We put food scraps in the compost bin. Compost is good for the environment.",
    "We can make compost with food scraps and leaves. We could make compost last year, too. Composting is easy. We recycle, we reduce waste, and we make compost.",
    "There is trash in the bin, not on the floor. There are bottles in the recycling bin. We can do it at home, too. Composting is easy for everyone.",
]

CHANT = [
    "Recycle, recycle, bottles and plastic,",
    "Compost, compost, food scraps and leaves,",
    "There is a bin, there are two bins,",
    "We can help, we can help the environment,",
    "First we mix, then we wait,",
    "Composting is easy, composting is great!",
]

DIALOGUE_PRACTICE = [
    (DIE, "Ana, how do you make compost?"),
    (ANA, "It's easy! First, we collect food scraps, like banana peels and egg shells."),
    (DIE, "Can I put plastic in the compost?"),
    (ANA, "No, you can't. Only food scraps and leaves."),
    (DIE, "OK. And then?"),
    (ANA, "Then we put them in the green bin and add dry leaves. We mix it every week."),
    (DIE, "How long does it take?"),
    (ANA, "About two months. Finally, we use the compost in the school garden."),
    (DIE, "Cool! I want to try at home."),
]

TEST_MONOLOGUE = [
    "Hello, students! I'm Mrs. Rosa, and I take care of the school garden.",
    "Today I can tell you how we make compost.",
    "First, we collect food scraps from the cafeteria every day. We don't use meat or plastic.",
    "Then we put the scraps in the compost bin with dry leaves and a little soil.",
    "Every Monday, we mix it and we water it.",
    "Finally, after three months, we have compost. We use it for our tomatoes and peppers.",
    "Last year we could make compost only in the dry season. Now we can make it all year!",
]

SPEAK_MODELS = [
    "Composting is easy.",
    "First, we collect food scraps.",
    "Then we add dry leaves.",
    "Finally, we use the compost in the garden.",
    "We could make compost last year.",
    "We can make compost at home.",
]

SPEAK_TEST_Q = [
    "Question one. What can we put in the compost?",
    "Question two. Can we put plastic in the compost?",
    "Question three. What is the first step to make compost?",
    "Question four. Where can we use compost?",
    "Question five. Is there a garden at your school or home?",
]

TRACKS = [
    {"n": "01", "title": "Vocabulario clave",
     "instr": "Escucha cada palabra y su ejemplo. Repite en voz alta durante la pausa.",
     "segments": vocab_segments(VOCAB)},
    {"n": "02", "title": "Lectura: Composting Is Easy",
     "instr": "Escucha el texto mientras lo sigues con el dedo en tu libro.",
     "segments": [(ANA, p, 1.0) for p in READING]},
    {"n": "03", "title": "Chant: Composting Is Easy!",
     "instr": "Escucha el chant y repítelo. Marca el ritmo con palmadas.",
     "segments": [(NAR, l, 0.5) for l in CHANT]},
    {"n": "04", "title": "Listening — Práctica: How Do You Make Compost?",
     "instr": "Escucha el diálogo dos veces. La primera vez, solo escucha. La segunda vez, responde.",
     "segments": [(v, t, 0.6) for v, t in DIALOGUE_PRACTICE]},
    {"n": "05", "title": "Listening — Mini-test: The School Garden",
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
     "es": "Hacer abono es fácil.",
     "goals": ["Explicar pasos en orden: ***First**, we collect food scraps. **Then** we mix it.*",
               "Decir lo que podemos hacer ahora (*can*) y lo que podíamos antes (*could*).",
               "Describir un lugar con *There is / There are*: *There are two bins in the yard.*"]},

    H1("¿Te sientes perdido? Empieza aquí"),
    P("Si en clase no entendiste el tema, lee esta página primero. Aquí está **lo esencial** en una sola hoja."),
    H3("1. Las 10 palabras que más vas a escuchar"),
    TABLE([2200, 2700, 2200, 2700], ["Inglés", "Español", "Inglés", "Español"], [
        ["compost", "abono", "mix", "mezclar"],
        ["food scraps", "restos de comida", "plants", "plantas"],
        ["leaves", "hojas", "garden", "huerto"],
        ["soil", "tierra", "waste", "desechos"],
        ["water", "agua; regar", "easy", "fácil"],
    ]),
    H3("2. Los pasos para hacer abono"),
    TABLE([2400, 7400], ["Palabra de orden", "Paso"], [
        ["**First,**", "we collect food scraps. (*Primero, juntamos restos de comida.*)"],
        ["**Then**", "we put them in the bin with dry leaves. (*Luego...*)"],
        ["**Next,**", "we mix it and water it every week. (*Después...*)"],
        ["**Finally,**", "we use the compost in the garden. (*Al final...*)"],
    ]),
    H3("3. can y could"),
    P("*We **can** make compost now.* = Podemos (ahora).   ·   *We **could** make compost last year.* = Podíamos (antes)."),
    P("Escucha estas palabras en el **Audio 6.2-01** (página de Vocabulario)."),
    PB,

    H1("1. Vocabulario"),
    P("Escucha el audio, señala cada palabra y repítela en voz alta. La columna **Se pronuncia** te da una ayuda aproximada; el audio es la pronunciación correcta."),
    audio("01"),
    TABLE([2100, 1700, 2300, 3700], ["Inglés", "Se pronuncia", "Español", "Ejemplo"],
          [[f"**{w}**", p, s, f"*{ex}*"] for w, p, s, ex in VOCAB]),
    NOTE("Qué va y qué no va en el abono",
         "✓ cáscaras de fruta y verdura, hojas secas, cáscaras de huevo, café    ✗ plástico, vidrio, carne, huesos"),
    PB,

    H1("2. Lectura: Composting Is Easy"),
    P("Lee el texto dos veces. La primera vez, en silencio. La segunda, en voz alta o junto con el audio."),
    audio("02"),
    READ("Composting Is Easy", READING),
    H2("Chant: Composting Is Easy!"),
    P("Escucha y repite. Marca el ritmo con palmadas."),
    audio("03"),
    POEM(CHANT),
    PB,

    H1("3. Gramática del tema"),
    H2("A. Pasos en orden"),
    P("Para explicar cómo se hace algo usamos el **presente simple** y **palabras de orden**:"),
    P("**First,** ... → **Then** ... → **Next,** ... → **Finally,** ...", align="center"),
    P("*First, we collect food scraps. Then we add leaves. Next, we mix it. Finally, we use it in the garden.*"),
    H2("B. can (ahora) y could (antes)"),
    TABLE([3300, 3300, 3200], ["Ahora: can", "Antes: could", "Negativa"], [
        ["We **can** make compost.", "We **could** make compost last year.", "We **can't** / **couldn't** use plastic."],
        ["She **can** mix it.", "She **could** help in the garden.", "**Can** we put meat? — No, we **can't**."],
    ]),
    P("Recuerda: **Could you...?** también sirve para pedir algo con cortesía: *Could you help me, please?*"),
    H2("C. There is / There are"),
    P("*There **is** a compost bin.* (una) · *There **are** two bins in the school yard.* (varias)"),
    NOTE("Errores comunes",
         "✗ First we collect, after we mix.  ✓ First we collect, **then** we mix.",
         "✗ We could to make compost.  ✓ We could **make** compost.",
         "✗ There is two bins.  ✓ There **are** two bins."),
    PB,

    H1("4. Listening (Escuchar)"),
    H2("Práctica: How Do You Make Compost?"),
    P("Diego le pregunta a Ana cómo se hace el abono. **Primera vez:** solo escucha. **Segunda vez:** responde."),
    audio("04"),
    P("**Ejemplo:** Composting is ______. → **easy**"),
    ITEMS("1. First, they collect food scraps like banana peels and egg ______________."),
    ITEMS("2. Can you put plastic in the compost?"),
    OPTS("a) Yes, you can.", "b) No, you can't.", "c) Only on Mondays."),
    ITEMS("3. They mix the compost every:"),
    OPTS("a) day", "b) week", "c) month"),
    ITEMS("4. It takes about ______________ months."),
    ITEMS("5. Finally, they use the compost in the ______________."),
    *test_blocks(TESTS["listening"], audio),
    PB,

    H1("5. Reading (Leer)"),
    H2("Práctica (texto: Composting Is Easy)"),
    P("**A. True or False.** Escribe T o F. Si es falso, corrige la oración."),
    P("**Ejemplo:** Ana is in Grade 5. → **T**"),
    ITEMS("1. There is one bin in the school yard. ______", "2. They put food scraps in the compost bin. ______",
          "3. They could make compost last year. ______", "4. There is trash on the floor. ______"),
    P("**B. Responde con una oración completa.**"),
    ITEMS("1. What can they make compost with?  ______________________________",
          "2. Where can we make compost too?  ______________________________"),
    *test_blocks(TESTS["reading"], audio),
    PB,

    H1("6. Writing (Escribir)"),
    H2("Práctica"),
    P("**A. Completa con Then, Next o Finally** según el número del paso."),
    P("**Ejemplo:** ______, we collect food scraps. → **First**"),
    ITEMS("1. (Paso 2) ______ we put the scraps in the bin with leaves.", "2. (Paso 3) ______, we mix it and water it.",
          "3. (Paso 4) ______, we use the compost in the garden."),
    P("**B. Completa con can o could.**"),
    ITEMS("1. Last year, we ______ make compost only in the dry season.", "2. Now we ______ make compost all year.",
          "3. ______ you help me with the bin, please?"),
    P("**C. Mis pasos.** En tu cuaderno, escribe 4 pasos para hacer abono en tu casa con *First, Then, Next, Finally*."),
    *test_blocks(TESTS["writing"], audio),
    PB,

    H1("7. Speaking (Hablar)"),
    H2("Práctica: escucha, repite y grábate"),
    P("**Paso 1.** Escucha cada oración y repítela en la pausa."),
    P("**Paso 2.** Graba en un celular las mismas oraciones."),
    P("**Paso 3.** Escucha tu grabación. En *could* la **l** no se pronuncia: /cud/."),
    audio("06"),
    ITEMS(*[f"{i+1}. {s}" for i, s in enumerate(SPEAK_MODELS)]),
    P("**Prepara tu presentación: \"How to Make Compost\".** Explica los 4 pasos en orden, como si fueras el encargado del huerto. Puedes hacer dibujos para cada paso. Practícala hasta decirla **sin leer**."),
    *test_blocks(TESTS["speaking"], audio),
    PB,

    H1("8. Mediation (Ayudar a otros a entender)"),
    P("Mediar es **ayudar a otra persona a entender un mensaje**: lo haces más corto y simple, o lo pasas de un idioma a otro."),
    H2("Práctica"),
    P("**A. Pasos con dibujos.** Dibuja en tu cuaderno 4 cuadros con los pasos para hacer abono y escribe **una palabra clave** en inglés debajo de cada uno (*collect · leaves · mix · garden*)."),
    P("**B. Explica en español.** Tu mamá quiere hacer abono. Explícale en español lo que dice este letrero."),
    NOTE("Letrero del huerto", "*Compost bin: food scraps and dry leaves only. No plastic, no meat. Mix it every Monday.*"),
    LINES(2),
    *test_blocks(TESTS["mediation"], audio),
    PB,

    H1("¿Cómo me fue en el Tema 6.2?"),
    P("Anota tus puntajes. Te dicen qué repasar antes de una prueba."),
    TABLE([2600, 1600, 5600], ["Mini-test", "Puntaje", "Si tuviste menos de la mitad, repasa..."],
          [[SKILL_TITLES[k].split(" ")[-1] if k != "speaking" else "Speaking", f"___ / {t['total']}", t["review"]]
           for k, t in TESTS.items()]),
    TABLE([6400, 1100, 1100, 1200], ["Puedo...", "Sí", "Casi", "Todavía no"], [
        ["explicar pasos en orden (*First, Then, Next, Finally*)", "☐", "☐", "☐"],
        ["diferenciar *can* (ahora) y *could* (antes)", "☐", "☐", "☐"],
        ["decir qué va y qué no va en el abono", "☐", "☐", "☐"],
        ["entender instrucciones habladas en orden", "☐", "☐", "☐"],
        ["explicar un letrero a mi familia en español", "☐", "☐", "☐"],
    ]),
    PB,

    H1("Respuestas del Tema 6.2"),
    P("Corrige **solo después de terminar**. Si te equivocaste, lee la explicación: ahí está lo que necesitas aprender."),
    H3("Listening — Práctica"),
    ITEMS("1. **shells.** *banana peels and egg shells.*",
          "2. **b) No, you can't.** *Only food scraps and leaves.*",
          "3. **b) week.** *We mix it every week.*",
          "4. **two** (2).   5. **school garden.**"),
    *answer_blocks(TESTS["listening"]),
    H3("Reading — Práctica"),
    ITEMS("A1. **F.** There are **two** bins in the school yard.   A2. **T.**   A3. **T.**",
          "A4. **F.** The trash is **in the bin**, not on the floor.",
          "B1. *They can make compost with food scraps and leaves.*   B2. *We can make compost at home.*"),
    *answer_blocks(TESTS["reading"]),
    H3("Writing — Práctica"),
    ITEMS("A1. **Then**   A2. **Next** (también se acepta *Then*)   A3. **Finally**",
          "B1. **could** (last year = antes)   B2. **can** (now = ahora)   B3. **Could** (pedir con cortesía)",
          "C. Ejemplo: *First, we collect food scraps. Then we put them in a bin with dry leaves. Next, we mix it every week. Finally, we use it for our plants.*"),
    *answer_blocks(TESTS["writing"]),
    H3("Mediation — ejemplos de respuesta"),
    ITEMS("Práctica A: respuesta libre.",
          "Práctica B: *Tinaco del abono: solo restos de comida y hojas secas. Nada de plástico ni carne. Hay que mezclarlo todos los lunes.*"),
    *answer_blocks(TESTS["mediation"]),
    PB,

    H1("Transcripciones de los audios del Tema 6.2"),
    P("Si no puedes escuchar un audio, pide a alguien que lo lea o léelo tú en voz alta. Úsalas también para revisar lo que no entendiste."),
    {"t": "transcripts"},
]
