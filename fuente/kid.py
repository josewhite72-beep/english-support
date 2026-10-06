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
         "segments": sum([[(nar, w.replace(" / ", ", "), 1.4), (nar, ex, 1.8)] for _, w, _, _, ex in m["VOCAB"]], [])},
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
        bl.append(NOTE(m.get("SOUND_TITLE", "¿Con qué sonido empieza?"), *m["SOUND"]))
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
        H2("Práctica: mira y copia" if m.get("COPY") else "Práctica: mira y escribe"),
        P("**Adulto:** el niño **copia** cada palabra en la línea, letra por letra. Señale cada letra mientras la escribe." if m.get("COPY")
          else "**Adulto:** el niño escribe el nombre de cada dibujo. Si lo necesita, puede copiarlo de la página de **Palabras nuevas**."),
        PICLINES([(img, (f"**{img}**   →   " if m.get("COPY") else "") + "______________________") for img in m["WRITE_PRACTICE"]], size=56),
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


def make_tests(m, listen, read_mc, read_tf, write_short, write_open, speak_checks, med_a, med_b,
               listen_tip="Antes de cada número, **miren los 3 dibujos** y díganlos en voz alta.",
               read_tip="Lee la oración **en voz alta** antes de elegir.", write_open_checks=None, mediation=None,
               write_tip="Escribe la palabra **letra por letra**. Revisa con la página de Palabras nuevas."):
    """Mini-tests estándar de K–2 a partir de datos compactos.
    listen:      [(lo que dice el audio, [img, img, img], índice correcto)]
    read_mc:     [(oración, [img, img, img], índice)]
    read_tf:     [(oración, img, True/False, explicación)]
    write_short: [(oración con ______, img, respuesta)]
    write_open:  (consigna, modelo, regex, texto de la casilla, ejemplo)
    speak_checks:[casillas para el adulto] (se agrega "Respondió en inglés, sin ayuda")
    med_a:       (oración en inglés, traducción esperada, casilla1, casilla2)
    med_b:       (quién lo dice y la frase en español, respuesta en inglés, regex)"""
    sp = m["SPEAK_TEST"]
    return {
     "listening": {"skill": "listening", "total": len(listen), "tip": [listen_tip],
      "review": "Palabras nuevas (audio 01) y la práctica de escucha (audio 04)",
      "parts": [{"intro": "**Adulto:** ponga el audio. El niño escucha cada número y **toca** (o encierra) el dibujo correcto. Puede escuchar **dos veces**.",
                 "audio": "05", "said": [s for s, _, _ in listen],
                 "qs": [{"t": "mc", "q": "", "opts": ["@" + o for o in opts], "a": a, "exp": f"*{s}*"} for s, opts, a in listen]}]},
     "reading": {"skill": "reading", "total": len(read_mc) + len(read_tf), "tip": [read_tip],
      "review": f"El cuento *{m['STORY_TITLE']}* y la práctica de lectura",
      "parts": [{"intro": "**Adulto:** el niño lee la oración y **toca** el dibujo correcto.",
                 "qs": [{"t": "mc", "q": s, "opts": ["@" + o for o in opts], "a": a} for s, opts, a in read_mc]},
                {"intro": "**Adulto:** el niño lee y mira el dibujo. ¿Dicen lo mismo? **True** (sí) o **False** (no).",
                 "qs": [{"t": "tf", "q": s, "img": img, "a": ok, "exp": exp} for s, img, ok, exp in read_tf]}]},
     "writing": {"skill": "writing", "total": len(write_short) + 2, "tip": [write_tip],
      "review": "La práctica de escritura y la página de Palabras nuevas",
      "parts": [{"intro": "**Parte A.** Mira el dibujo y completa. (1 punto cada una)",
                 "qs": [{"t": "short", "q": q, "img": img, "accept": [[ans]], "show": f"**{ans}**"} for q, img, ans in write_short]},
                {"intro": write_open[0] + " (2 puntos)", "note": ["Modelo", f"*{write_open[1]}*"],
                 "open": {"lines": 1, "min_sent": 0 if write_open_checks else 1, "max_sent": 0 if write_open_checks else 2,
                          "check_intro": "**Adulto:** marque un punto por cada casilla:",
                          "checklist": write_open_checks or [{"text": write_open[3], "auto": write_open[2]},
                                        {"text": "Empezó con mayúscula y terminó con punto.", "auto": "caps"}],
                          "sample": write_open[4]}}]},
     "speaking": {"skill": "speaking", "total": len(speak_checks) + 1,
      "tip": ["Responda con el niño una vez para practicar. La segunda vez, el niño responde solo."],
      "review": "Audio 06: escucha y repite",
      "parts": [{"intro": "**Adulto:** ponga el audio. El niño mira cada dibujo y responde en voz alta en la pausa.",
                 "audio": "07", "pics": [(img, f"Picture {NUMS[i]}") for i, (img, _, _) in enumerate(sp)],
                 "open": {"record": True, "check_intro": "**Adulto:** escuche y marque un punto por cada casilla:",
                          "checklist": [{"text": t} for t in speak_checks] + [{"text": "Respondió en inglés, sin ayuda"}]}}]},
     "mediation": mediation or {"skill": "mediation", "total": 4,
      "tip": ["Primero diga la oración en español; después busquen las palabras en inglés."],
      "review": "La práctica de Mediation: enseño a mi familia",
      "parts": [{"intro": "**Parte A.** Alguien de tu familia no sabe inglés. Ayúdale: ¿qué significa? Escríbelo **en español**.",
                 "note": ["Oración", f"*{med_a[0]}*"],
                 "open": {"lines": 1, "min_sent": 0, "max_sent": 0, "checklist": [{"text": med_a[2]}, {"text": med_a[3]}], "sample": med_a[1]}},
                {"intro": f"**Parte B.** {med_b[0]} Escríbelo **en inglés**.",
                 "open": {"lines": 1, "min_sent": 1, "max_sent": 1,
                          "checklist": [{"text": f"Escribió **{med_b[1].rstrip('.!')}**.", "auto": med_b[2]},
                                        {"text": "Empezó con mayúscula y terminó con punto.", "auto": "caps"}],
                          "sample": med_b[1]}}]},
    }


def k_mediation(sentence, sample_es, teach):
    """Mediation para K: el niño explica en voz alta y el adulto anota; luego enseña a un familiar."""
    return {"skill": "mediation", "total": 4,
            "tip": ["En K no se escribe solo: **el niño habla y el adulto anota**."],
            "review": "La práctica de Mediation: enseño a mi familia",
            "parts": [{"intro": "**Parte A.** Lea la frase en inglés. El niño dice **en español** qué significa y usted lo anota.",
                       "note": ["Frase", f"*{sentence}*"],
                       "open": {"lines": 1, "min_sent": 0, "max_sent": 0,
                                "checklist": [{"text": "Explicó la frase en español."}, {"text": "Hizo el sonido o el gesto."}],
                                "sample": sample_es}},
                      {"intro": f"**Parte B.** {teach}",
                       "open": {"min_sent": 0, "max_sent": 0,
                                "checklist": [{"text": "Le enseñó la palabra a un familiar."}, {"text": "La dijo en inglés, sin ayuda."}],
                                "sample": ""}}]}
