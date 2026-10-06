# -*- coding: utf-8 -*-
"""Formato visual para K, 1.º y 2.º: "escucha y toca", con dibujos y con el adulto acompañando.
Cada tema define sus datos (ver grades/2/t51.py) y llama a build(globals()), que crea
TRACKS (audios) y BLOCKS (libro). Los mini-tests (TESTS) los escribe cada tema.

Datos que usa el tema:
  THEME_ID, THEME_TITLE, THEME_ES, SCENARIO, THEME_NUM ("Theme 1")
  GOALS            lista de "Yo puedo..." (texto, se muestran con dibujito de destreza)
  FAMILY           párrafo para la familia (qué aprende el niño)
  VOCAB            [(img, palabra, "/pron/", español, ejemplo)]
  PATTERN          {"rows": [[inglés...], [español...]], "note": texto}
  SONG             [(línea, gesto)]          SONG_TITLE
  STORY            [(img, oración)]          STORY_TITLE, STORY_QS [(pregunta, /pron/, respuesta)]
  LISTEN_PRACTICE  [(oración, [img, img, img], índice_correcto)]
  READ_PRACTICE    [(img, oración, True/False)]
  WRITE_PRACTICE   [img, ...]  (repasa y escribe la palabra)
  SPEAK_MODELS     [oración]
  SPEAK_TEST       [(img, pregunta, respuesta_esperada)]
  MEDIATION_PRACTICE texto
  SOUND            (texto) opcional: ¿con qué sonido empieza?
  VOICE            voz del cuento (opcional)
"""
from common import *

LISTEN_IMG, SPEAK_IMG, READ_IMG, WRITE_IMG = "i-listen", "i-speak", "i-read", "i-write"
NUMS = ["one", "two", "three", "four", "five", "six", "seven", "eight"]

def numbered(voice, items, pause_mid=1.5, pause_end=3.5):
    """'Number one. It's the park. ... It's the park.' (cada oración dos veces)"""
    segs = []
    for i, s in enumerate(items):
        segs += [(voice, f"Number {NUMS[i]}.", 0.5), (voice, s, pause_mid), (voice, s, pause_end)]
    return segs

def build(m):
    tid = m["THEME_ID"]
    nar = NAR
    story_v = m.get("VOICE", "af_bella")
    m.setdefault("SPEAKERS", {})
    lt = m["TESTS"]["listening"]["parts"][0]
    tracks = [
        {"n": "01", "title": "Palabras nuevas",
         "instr": "Escucha cada palabra y repítela en voz alta durante la pausa.",
         "segments": sum([[(nar, w, 1.4), (nar, ex, 1.8)] for _, w, _, _, ex in m["VOCAB"]], [])},
        {"n": "02", "title": "Cuento: " + m["STORY_TITLE"],
         "instr": "Escucha el cuento y señala cada dibujo en tu libro.",
         "segments": sum([[(story_v, f"{NUMS[i].capitalize()}.", 0.4), (story_v, s, 1.4)] for i, (_, s) in enumerate(m["STORY"])], [])},
        {"n": "03", "title": "Canción: " + m["SONG_TITLE"],
         "instr": "Escucha la canción, repítela y haz los gestos.",
         "segments": [(nar, l, 0.8) for l, _ in m["SONG"]] * 2},
        {"n": "04", "title": "Escucha y encierra (práctica)",
         "instr": "Escucha y encierra el dibujo correcto en tu libro.",
         "segments": numbered(nar, [s for s, _, _ in m["LISTEN_PRACTICE"]])},
        {"n": "05", "title": "Mini-test de Listening",
         "instr": "Escucha y toca (o encierra) el dibujo correcto.",
         "segments": numbered(nar, lt["said"])},
        {"n": "06", "title": "Escucha y repite",
         "instr": "Escucha cada oración y repítela en la pausa.",
         "segments": [(nar, s, 3.2) for s in m["SPEAK_MODELS"]]},
        {"n": "07", "title": "Mini-test de Speaking",
         "instr": "Mira los dibujos de tu libro. Responde cada pregunta en voz alta durante la pausa.",
         "segments": [(nar, "Speaking test. Look at the pictures in your book.", 1.5)]
                     + sum([[(nar, f"Picture {NUMS[i]}.", 0.4), (nar, q, 7.0)] for i, (_, q, _) in enumerate(m["SPEAK_TEST"])], [])},
    ]
    m["TRACKS"] = tracks

    def audio(n):
        t = next(t for t in tracks if t["n"] == n)
        return {"t": "audio", "id": f"{tid}/{n}", "label": f"Audio {tid.replace('-', '.')}-{n}", "title": t["title"]}

    T = m["TESTS"]
    lab = tid.replace("-", ".")
    V = m["VOCAB"]
    bl = [
        {"t": "theme_cover", "scenario": m["SCENARIO"], "theme": f"{m['THEME_NUM']}: {m['THEME_TITLE']}",
         "es": m["THEME_ES"], "goals": m["GOALS"]},
        NOTE("Para la familia", m["FAMILY"],
             "**Usted lee las instrucciones** y acompaña; no necesita saber inglés. Cada palabra trae su pronunciación entre barras: *park* /park/.",
             "Donde vea **AUDIO**, escanee el código con la cámara del celular: el audio dice cada palabra en inglés. Trabajen **15 a 20 minutos al día**."),
        PB,
        H1("1. Palabras nuevas"),
        P("**Adulto:** ponga el audio. El niño **señala** cada dibujo y **repite** la palabra. Luego usted señala un dibujo y el niño dice la palabra."),
        audio("01"),
        PICS([(img, w, f"{pr} {es}") for img, w, pr, es, _ in V], cols=4 if len(V) > 6 else 3, size=96 if len(V) > 6 else 116),
    ]
    if m.get("SOUND"):
        bl.append(NOTE("¿Con qué sonido empieza?", *m["SOUND"]))
    bl += [
        PB,
        H1("2. La frase del tema"),
        TABLE([3312] * 3, m["PATTERN"]["rows"][0], [m["PATTERN"]["rows"][1]]),
        P(m["PATTERN"]["note"]),
        H2("Canción: " + m["SONG_TITLE"]),
        P("**Adulto:** canten **tres veces**: 1) escuchen el audio; 2) canten juntos con los gestos; 3) el niño canta solo."),
        audio("03"),
        TABLE([5200, 4736], ["Canción", "Gesto"], [[f"**{l}**", g] for l, g in m["SONG"]]),
        PB,
        H1("3. Cuento: " + m["STORY_TITLE"]),
        P("**Adulto:** pongan el audio y el niño **señala** cada dibujo. La segunda vez, lean juntos. La tercera vez, el niño lee solo."),
        audio("02"),
        PICLINES(m["STORY"], size=64, num=True),
        P("**Preguntas (el adulto las lee en voz alta):**"),
        ITEMS(*[f"{i+1}. **{q}** *{pr}*" for i, (q, pr, _) in enumerate(m["STORY_QS"])]),
        PB,
        H1("4. Listening (Escuchar)"),
        H2("Práctica: escucha y encierra"),
        P("**Adulto:** ponga el audio. En cada fila, el niño **encierra** el dibujo que escuchó. **Ejemplo:** en la fila 1 se oye *" + m["LISTEN_PRACTICE"][0][0] + "*"),
        audio("04"),
        PICROWS([(str(i + 1), imgs) for i, (_, imgs, _) in enumerate(m["LISTEN_PRACTICE"])]),
        *test_blocks(T["listening"], audio),
        PB,
        H1("5. Reading (Leer)"),
        H2("Práctica: lee y marca ✓ o ✗"),
        P("**Adulto:** el niño lee la oración (con su ayuda) y mira el dibujo. Marca **✓** si dicen lo mismo y **✗** si no."),
        PICLINES([(img, f"{s}      ☐ ✓   ☐ ✗") for img, s, _ in m["READ_PRACTICE"]], size=56),
        *test_blocks(T["reading"], audio),
        PB,
        H1("6. Writing (Escribir)"),
        H2("Práctica: mira y escribe"),
        P("**Adulto:** el niño escribe el nombre de cada dibujo. Si lo necesita, puede copiarlo de la página de **Palabras nuevas**."),
        PICLINES([(img, "______________________") for img in m["WRITE_PRACTICE"]], size=56),
        *test_blocks(T["writing"], audio),
        PB,
        H1("7. Speaking (Hablar)"),
        H2("Práctica: escucha y repite"),
        P("**Adulto:** ponga el audio. El niño repite cada oración en la pausa. Si tiene celular, **grábelo** y escuchen juntos."),
        audio("06"),
        ITEMS(*[f"{i+1}. {s}" for i, s in enumerate(m["SPEAK_MODELS"])]),
        PB,
        H2(SKILL_TITLES["speaking"]),
        TIP("Responda con el niño una vez para practicar. La segunda vez, el niño responde **solo**."),
        P("**Adulto:** ponga el audio. El niño mira cada dibujo y responde en voz alta durante la pausa."),
        audio("07"),
        PICLINES([(img, f"**Picture {NUMS[i]}.** *{q}*") for i, (img, q, _) in enumerate(m["SPEAK_TEST"])], size=56),
    ]
    sp = T["speaking"]["parts"][0]["open"]
    bl += [P(T["speaking"]["parts"][0]["open"].get("check_intro", "Marque un punto por cada casilla:")),
           checklist(*[c["text"] for c in sp["checklist"]]),
           SCORE(f"Puntaje: ______ / {T['speaking']['total']}"),
           PB,
           H1("8. Mediation (Ayudar a otros a entender)"),
           P("Mediar es **ayudar a otra persona a entender**: explicar en español lo que dice en inglés, o al revés."),
           H2("Práctica: enseño a mi familia"),
           P(m["MEDIATION_PRACTICE"]),
           *test_blocks(T["mediation"], audio),
           PB,
           H1(f"¿Cómo me fue en el Tema {lab}?"),
           P("**Adulto:** lea cada frase. El niño marca la carita que muestra cómo se siente."),
           TABLE([5400, 1500, 1500, 1536], ["Yo puedo...", "¡Lo logré!", "Casi", "Necesito ayuda"],
                 [[g, "☐", "☐", "☐"] for g in m["GOALS"]]),
           TABLE([3000, 1800, 5136], ["Mini-test", "Puntaje", "Si salió bajo, repasen..."],
                 [[SKILL_TITLES[k].replace("Mini-test de ", "").replace(" (examen oral)", ""), f"___ / {t['total']}", t["review"]] for k, t in T.items()]),
           PB,
           H1(f"Respuestas del Tema {lab} (para el adulto)"),
           H3("Cuento"),
           ITEMS(*[f"{i+1}. {a}" for i, (_, _, a) in enumerate(m["STORY_QS"])]),
           H3("Listening — Práctica"),
           ITEMS("   ".join(f"{i+1}) **{chr(97 + c)}** ({s})" for i, (s, _, c) in enumerate(m["LISTEN_PRACTICE"]))),
           *answer_blocks(T["listening"]),
           H3("Reading — Práctica"),
           ITEMS("   ".join(f"{i+1}) **{'✓' if ok else '✗'}**" for i, (_, _, ok) in enumerate(m["READ_PRACTICE"]))),
           *answer_blocks(T["reading"]),
           H3("Writing — Práctica"),
           ITEMS("   ".join(f"{i+1}) **{w}**" for i, w in enumerate(m["WRITE_PRACTICE"]))),
           *answer_blocks(T["writing"]),
           *answer_blocks(T["mediation"]),
           H3("Speaking — respuestas esperadas"),
           ITEMS(*[f"{i+1}. *{a}*" for i, (_, _, a) in enumerate(m["SPEAK_TEST"])]),
           PB,
           H1(f"Transcripciones de los audios del Tema {lab}"),
           P("Si no puede escuchar un audio, **lea usted el texto en voz alta** (la pronunciación está en la página de Palabras nuevas)."),
           {"t": "transcripts"}]
    m["BLOCKS"] = bl
