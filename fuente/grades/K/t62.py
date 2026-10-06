# -*- coding: utf-8 -*-
"""Kínder · Scenario 6, Theme 2 — One Step In, Two Steps Out!
Fuentes: planeamiento K_6-2 y módulo GeMA K_6-2. Dibujos: OpenMoji (CC BY-SA 4.0) y propios."""
from common import *
import kid

THEME_ID, THEME_NUM = "6-2", "Theme 2"
THEME_TITLE, THEME_ES = "One Step In, Two Steps Out!", "¡Un paso adentro, dos pasos afuera!"
SCENARIO = "Scenario 6: Let's Dance!"
COPY = True
GOALS = ["Escucho **cuántos** pasos o saltos y los hago: *Two steps! One hop!*",
         "Digo *Two steps!* y *One hop!*",
         "Copio palabras del baile."]
FAMILY = ("En este tema su niño/a aprende a contar **one** (uno) y **two** (dos) mientras baila: **Two steps! One hop!** "
          "/tu steps — uan jop/. También repasa **dance, foot, circle, line** (línea) y **hop**.")
VOCAB = [("one", "one", "/uan/", "uno", "One hop!"),
         ("two", "two", "/tu/", "dos", "Two steps!"),
         ("dance", "dance", "/dans/", "bailar", "Dance in a circle!"),
         ("foot", "foot", "/fut/", "pie", "Foot on the line!"),
         ("line", "line", "/lain/", "línea", "Stand on the line."),
         ("hop", "hop", "/jop/", "saltar en un pie", "One hop!")]
SOUND = ["**Adulto:** pregunte **How many steps?** /jau MÉ-ni steps/ (¿Cuántos pasos?). El niño muestra con los dedos y dice **Two steps!**"]
SOUND_TITLE = "¿Cuántos?"
PATTERN = {"rows": [["**Two**", "**steps!**", ""], ["Dos", "pasos.", ""]],
           "note": "**Nota para la familia:** con **two** se agrega **-s**: *one step*, *two step**s***. Pongan una cinta o una cuerda en el piso: esa es **the line**."}
SONG_TITLE = "Two Steps, One Hop"
SONG = [("Two steps, two steps,", "Da dos pasos."), ("Dance in a circle,", "Gira bailando."), ("One hop, one hop,", "Salta en un pie."),
        ("Foot on the line!", "Pon el pie sobre una línea."), ("Two steps, one hop!", "Dos pasos y un salto.")]
STORY_TITLE = "The Dance Line"
STORY = [("line", "Look! A line."), ("foot", "Foot on the line."), ("two", "Two steps!"), ("one", "One hop!"), ("dance", "Let's dance!")]
STORY_QS = [("How many steps?", "/jau MÉ-ni steps/", "Two steps!"), ("How many hops?", "/jau MÉ-ni jops/", "One hop!"),
            ("Show me: foot on the line!", "/shou mi fut on de lain/", "El niño pone el pie sobre la línea.")]
LISTEN_PRACTICE = [("Two!", ["one", "two", "hop"], 1), ("Line.", ["line", "foot", "dance"], 0),
                   ("One!", ["two", "line", "one"], 2), ("Dance!", ["dance", "hop", "two"], 0)]
READ_PRACTICE = [("two", "two", True), ("one", "two", False), ("line", "line", True), ("hop", "foot", False)]
WRITE_PRACTICE = ["one", "two", "line", "hop"]
SPEAK_MODELS = ["One hop!", "Two steps!", "Foot on the line!", "Dance in a circle!", "Two steps, one hop!"]
SPEAK_TEST = [("two", "How many steps?", "Two steps!"), ("one", "How many hops?", "One hop!"),
              ("line", "What is it?", "Line! (A line.)"), ("dance", "What is it?", "Dance!")]
MEDIATION_PRACTICE = ("Pongan una línea en el piso. El niño da las órdenes en inglés (**Two steps! One hop!**) y la familia baila. "
                      "Si alguien no entiende, el niño le explica en español y le muestra con los dedos.")
TESTS = kid.make_tests(globals(),
    listen=[("Two steps!", ["one", "two", "line"], 1), ("One hop!", ["one", "dance", "two"], 0),
            ("Foot on the line!", ["two", "hop", "line"], 2), ("Dance!", ["dance", "one", "foot"], 0),
            ("Hop, hop!", ["line", "hop", "two"], 1)],
    listen_tip="Antes de cada número, **digan los 3 dibujos** en voz alta.",
    read_mc=[("two", ["one", "two", "hop"], 1), ("line", ["line", "dance", "foot"], 0), ("one", ["two", "hop", "one"], 2)],
    read_tip="**Adulto:** señale la palabra con el dedo y léanla juntos, letra por letra.",
    read_tf=[("one", "one", True, "Uno."), ("two", "line", False, "Es una línea: *line*.")],
    write_short=[("Copia: **one** → ______________", "one", "one"), ("Copia: **two** → ______________", "two", "two"),
                 ("Copia: **line** → ______________", "line", "line")],
    write_tip="**Adulto:** el niño copia la palabra mirando el modelo. Ayúdele a contar las letras.",
    write_open=("**Parte B.** Dibuja una línea con dos pies encima y **copia** debajo: *two*.", "two", "", "", "two"),
    write_open_checks=[{"text": "Dibujó la línea y los pies."}, {"text": "Copió *two*.", "auto": r"\btwo\b"}],
    speak_checks=["Picture 1: *Two steps!*", "Picture 2: *One hop!*", "Picture 3: *Line!*", "Picture 4: *Dance!*"],
    med_a=None, med_b=None,
    mediation=kid.k_mediation("Two steps! One hop!", "¡Dos pasos! ¡Un salto!", "El niño le enseña a un familiar el baile: dos pasos y un salto, dando las órdenes en inglés."))
kid.build(globals())
