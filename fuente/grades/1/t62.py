# -*- coding: utf-8 -*-
"""1.er grado · Scenario 6, Theme 2 — That Is a Circle.
Fuentes: planeamiento 1_6-2 y módulo GeMA 1_6-2. Dibujos propios de las figuras."""
from common import *
import kid

THEME_ID, THEME_NUM = "6-2", "Theme 2"
THEME_TITLE, THEME_ES = "That Is a Circle.", "Eso es un círculo."
SCENARIO = "Scenario 6: Shapes Around Us"
GOALS = ["Reconozco 6 figuras cuando las escucho, también *oval* y *diamond*.",
         "Pregunto *What shape is it?* y respondo *That is a circle.*",
         "Leo oraciones cortas sobre figuras.",
         "Escribo el nombre de las figuras."]
FAMILY = ("En este tema su hijo/a repasa las figuras y aprende dos nuevas: **oval** (óvalo) y **diamond** (rombo). "
          "También aprende a decir **What shape is it? — That is a circle.** /uát sheip is it — dat is a SÉR-kol/")
VOCAB = [("circle", "circle", "/SÉR-kol/", "círculo", "That is a circle."),
         ("square", "square", "/skuer/", "cuadrado", "That is a square."),
         ("triangle", "triangle", "/TRÁI-an-gol/", "triángulo", "That is a triangle."),
         ("star", "star", "/star/", "estrella", "That is a star."),
         ("oval", "oval", "/ÓU-val/", "óvalo", "That is an oval."),
         ("diamond", "diamond", "/DÁI-mond/", "rombo", "That is a diamond.")]
SOUND_TITLE = "Ojo: a / an"
SOUND = ["Con **oval** se dice **an** en lugar de **a**, porque empieza con sonido de vocal: *That is **an** oval.*"]
PATTERN = {"rows": [["**That is a**", "**circle.**", ""], ["Eso es un", "círculo.", ""]],
           "note": "**Nota para la familia:** para preguntar se dice **What shape is it?** /uát sheip is it/ = ¿Qué figura es? Un círculo es **round** /raund/ (redondo)."}
SONG_TITLE = "Shapes, Shapes"
SONG = [("That is a circle, round and small.", "Dibuja un círculo pequeño."),
        ("That is a square, big and tall.", "Forma un cuadrado con las manos."),
        ("That is a triangle, one, two, three.", "Cuenta los tres lados con los dedos."),
        ("That is a star, look and see.", "Abre y cierra los dedos."),
        ("Shapes, shapes, all day and night!", "Aplaude al ritmo.")]
STORY_TITLE = "My Shape Book"
STORY = [("circle", "Look! That is a circle."), ("square", "That is a big square."), ("triangle", "I see a small triangle."),
         ("oval", "That is an oval."), ("diamond", "I see a diamond.")]
STORY_QS = [("What shape is number 1?", "/uát sheip is NÁM-ber uan/", "A circle."),
            ("What shape is big?", "/uát sheip is big/", "The square."),
            ("What shape is number 5?", "/uát sheip is NÁM-ber faiv/", "A diamond.")]
LISTEN_PRACTICE = [("That is an oval.", ["circle", "oval", "square"], 1), ("That is a diamond.", ["diamond", "star", "triangle"], 0),
                   ("That is a circle.", ["oval", "square", "circle"], 2), ("That is a star.", ["star", "diamond", "oval"], 0)]
READ_PRACTICE = [("diamond", "That is a diamond.", True), ("oval", "That is a circle.", False),
                 ("star", "That is a star.", True), ("square", "That is a triangle.", False)]
WRITE_PRACTICE = ["oval", "diamond", "circle", "star"]
SPEAK_MODELS = ["What shape is it?", "That is a circle.", "That is an oval.", "That is a diamond.", "A circle is round."]
SPEAK_TEST = [("oval", "What shape is it?", "That is an oval."), ("diamond", "What shape is it?", "That is a diamond."),
              ("triangle", "What shape is it?", "That is a triangle."), ("circle", "Is a circle round?", "Yes! A circle is round.")]
MEDIATION_PRACTICE = ("Juego **¿Qué figura es?**: un familiar dibuja una figura en el aire con el dedo. El niño adivina en inglés "
                      "(**That is a diamond!**) y luego le explica en español cómo se dice.")
TESTS = kid.make_tests(globals(),
    listen=[("That is a diamond.", ["oval", "diamond", "square"], 1), ("That is an oval.", ["oval", "circle", "star"], 0),
            ("That is a triangle.", ["diamond", "square", "triangle"], 2), ("That is a square.", ["square", "oval", "triangle"], 0),
            ("That is a star.", ["circle", "star", "diamond"], 1)],
    read_mc=[("That is an oval.", ["circle", "oval", "diamond"], 1), ("That is a diamond.", ["diamond", "triangle", "star"], 0),
             ("A circle is round.", ["square", "triangle", "circle"], 2)],
    read_tf=[("That is an oval.", "oval", True, "Es un óvalo."), ("That is a star.", "diamond", False, "Es un rombo: *That is a diamond.*")],
    write_short=[("That is an ______________.", "oval", "oval"), ("That is a ______________.", "diamond", "diamond"),
                 ("That is a ______________.", "triangle", "triangle")],
    write_open=("**Parte B.** Dibuja tu figura favorita y escribe **1 oración** con *That is a...*", "That is a star.",
                r"\bthat is an? (circle|square|triangle|rectangle|star|oval|diamond)\b|\bthat'?s an? (circle|square|triangle|rectangle|star|oval|diamond)\b",
                "Escribió **That is a** + una figura.", "That is a diamond."),
    speak_checks=["Picture 1: *That is an oval.*", "Picture 2: *That is a diamond.*", "Picture 3: *That is a triangle.*", "Picture 4: *Yes! A circle is round.*"],
    med_a=("That is an oval.", "Eso es un óvalo.", "Escribió *óvalo*.", "Entendió *That is* = eso es."),
    med_b=("Tu primo dice: *«Eso es un círculo»*.", "That is a circle.", r"\b(that is|that'?s) a circle\b"))
kid.build(globals())
