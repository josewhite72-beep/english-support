# -*- coding: utf-8 -*-
"""1.er grado · Scenario 6, Theme 1 — I See a Rectangle.
Fuentes: planeamiento 1_6-1 y módulo GeMA 1_6-1. Dibujos propios de las figuras."""
from common import *
import kid

THEME_ID, THEME_NUM = "6-1", "Theme 1"
THEME_TITLE, THEME_ES = "I See a Rectangle.", "Veo un rectángulo."
SCENARIO = "Scenario 6: Shapes Around Us"
GOALS = ["Reconozco 5 figuras cuando las escucho.",
         "Digo lo que veo: *I see a circle.*",
         "Digo si es grande o pequeño: *I see a big square.*",
         "Leo y escribo el nombre de las figuras."]
FAMILY = ("En este tema su hijo/a aprende **5 figuras** (circle, square, triangle, rectangle, star), las palabras **big** y **small**, "
          "y a decir **I see a circle.** /ai si a SÉR-kol/ (Veo un círculo.)")
VOCAB = [("circle", "circle", "/SÉR-kol/", "círculo", "I see a circle."),
         ("square", "square", "/skuer/", "cuadrado", "I see a square."),
         ("triangle", "triangle", "/TRÁI-an-gol/", "triángulo", "I see a triangle."),
         ("rectangle", "rectangle", "/REK-tan-gol/", "rectángulo", "I see a rectangle."),
         ("star", "star", "/star/", "estrella", "I see a star."),
         ("big-small", "big / small", "/big/ /smol/", "grande / pequeño", "I see a big circle and a small circle.")]
SOUND = ["**star, square, small** empiezan con /s/, **sin \"e\" al principio** (no \"estar\"): ssss-tar, ssss-quare, ssss-mall."]
PATTERN = {"rows": [["**I see**", "**a**", "**circle.**"], ["Yo veo", "un", "círculo."]],
           "note": "**Nota para la familia:** el tamaño va **antes** de la figura: *a big square* = un cuadrado grande; *a small triangle* = un triángulo pequeño."}
SONG_TITLE = "I See Them All"
SONG = [("I see a circle,", "Dibuja un círculo en el aire."), ("I see a square,", "Dibuja un cuadrado."),
        ("I see a triangle,", "Junta las manos en punta."), ("I see a star,", "Abre y cierra los dedos."),
        ("Big and small, I see them all!", "Abre los brazos, júntalos y señala alrededor.")]
STORY_TITLE = "My Shapes"
STORY = [("circle", "I see a circle."), ("square", "I see a big square."), ("triangle", "I see a small triangle."),
         ("star", "I see a red star."), ("rectangle", "I see a blue rectangle.")]
STORY_QS = [("What shape is big?", "/uát sheip is big/", "The square."),
            ("What color is the star?", "/uát KÓ-lor is de star/", "Red."),
            ("What shape is small?", "/uát sheip is smol/", "The triangle.")]
LISTEN_PRACTICE = [("I see a circle.", ["square", "circle", "star"], 1), ("I see a triangle.", ["triangle", "rectangle", "circle"], 0),
                   ("I see a star.", ["square", "triangle", "star"], 2), ("I see a rectangle.", ["rectangle", "circle", "square"], 0)]
READ_PRACTICE = [("square", "I see a square.", True), ("circle", "I see a star.", False),
                 ("rectangle", "I see a rectangle.", True), ("triangle", "I see a circle.", False)]
WRITE_PRACTICE = ["circle", "square", "star", "triangle"]
SPEAK_MODELS = ["I see a circle.", "I see a square.", "I see a big star.", "I see a small triangle.", "I see a rectangle."]
SPEAK_TEST = [("circle", "What do you see?", "I see a circle."), ("star", "What do you see?", "I see a star."),
              ("rectangle", "What do you see?", "I see a rectangle."), ("big-small", "Which circle is big?", "This one! (señala) / The big circle.")]
MEDIATION_PRACTICE = ("**Cacería de figuras:** busquen en la casa cosas con forma de círculo, cuadrado, rectángulo y triángulo "
                      "(un plato, una ventana, una puerta...). El niño dice **I see a circle!** y le explica a un familiar qué significa.")
TESTS = kid.make_tests(globals(),
    listen=[("I see a square.", ["circle", "square", "star"], 1), ("I see a star.", ["star", "triangle", "rectangle"], 0),
            ("I see a rectangle.", ["square", "circle", "rectangle"], 2), ("I see a triangle.", ["triangle", "star", "square"], 0),
            ("I see a circle.", ["rectangle", "circle", "triangle"], 1)],
    read_mc=[("I see a triangle.", ["square", "triangle", "circle"], 1), ("I see a star.", ["star", "rectangle", "square"], 0),
             ("I see a rectangle.", ["circle", "star", "rectangle"], 2)],
    read_tf=[("I see a circle.", "circle", True, "Es un círculo."), ("I see a triangle.", "square", False, "Es un cuadrado: *I see a square.*")],
    write_short=[("I see a ______________.", "circle", "circle"), ("I see a ______________.", "star", "star"),
                 ("I see a ______________.", "square", "square")],
    write_open=("**Parte B.** Dibuja una figura grande o pequeña y escribe **1 oración** con *I see a...*", "I see a big star.",
                r"\bi see an? (big |small |red |blue |green |yellow )?(circle|square|triangle|rectangle|star)\b",
                "Escribió **I see a** + una figura.", "I see a small circle."),
    speak_checks=["Picture 1: *I see a circle.*", "Picture 2: *I see a star.*", "Picture 3: *I see a rectangle.*", "Picture 4: señaló el círculo grande"],
    med_a=("I see a big square.", "Veo un cuadrado grande.", "Escribió *cuadrado*.", "Escribió *grande* (big)."),
    med_b=("Tu hermanito dice: *«Veo una estrella»*.", "I see a star.", r"\bi see a star\b"))
kid.build(globals())
