# -*- coding: utf-8 -*-
"""1.er grado · Scenario 5, Theme 2 — That's a Red Bike!
Fuentes: planeamiento 1_5-2 y módulo GeMA 1_5-2 (dibujos del módulo: crayones de colores)."""
from common import *
import kid

THEME_ID, THEME_NUM = "5-2", "Theme 2"
THEME_TITLE, THEME_ES = "That's a Red Bike!", "¡Es una bicicleta roja!"
SCENARIO = "Scenario 5: Colors of Things that Go"
GOALS = ["Reconozco 5 colores cuando los escucho.",
         "Pregunto *What color is it?* y respondo *It's red.*",
         "Digo un vehículo con su color: *That's a red bike.*",
         "Leo y escribo los colores."]
FAMILY = ("En este tema su hijo/a aprende **5 colores** y a decir el color de un vehículo: **What color is it? — It's red. That's a red bike!** "
          "/uát KÓ-lor is it — its red. dats a red baik/")
VOCAB = [("red", "red", "/red/", "rojo", "It's red."),
         ("blue", "blue", "/blu/", "azul", "It's blue."),
         ("green", "green", "/grin/", "verde", "It's green."),
         ("yellow", "yellow", "/YÉ-lou/", "amarillo", "It's yellow."),
         ("orange", "orange", "/Ó-ranch/", "anaranjado", "It's orange."),
         ("bike", "bike", "/baik/", "bicicleta", "That's a red bike.")]
SOUND_TITLE = "Ojo"
SOUND = ["En inglés el **color va antes** del vehículo: **red bike** = bicicleta roja. Con **orange** se dice **an**: *That's an orange train.*"]
PATTERN = {"rows": [["**That's a**", "**red**", "**bike.**"], ["Es una", "bicicleta", "roja."]],
           "note": "**Nota para la familia:** para preguntar el color: **What color is it?** /uát KÓ-lor is it/ = ¿De qué color es? Respuesta: **It's red.** /its red/ = Es rojo."}
SONG_TITLE = "Ring, Ring, Ring!"
SONG = [("Red bike, red bike, ring, ring, ring!", "Toca el timbre de la bici."),
        ("Blue bus, blue bus, beep, beep, beep!", "Aprieta la bocina."),
        ("Green car, green car, vroom, vroom, vroom!", "Maneja con el volante."),
        ("Yellow truck, yellow truck, honk, honk, honk!", "Jala la bocina del camión."),
        ("Orange train, orange train, choo, choo, choo!", "Mueve los brazos como ruedas.")]
STORY_TITLE = "Ana's Red Bike"
STORY = [("bike", "Look! That's a bike."), ("red", "It's red. That's a red bike!"), ("bus", "That's a bus. It's blue."),
         ("car", "That's a car. It's green."), ("bike", "I like the red bike!")]
STORY_QS = [("What color is the bike?", "/uát KÓ-lor is de baik/", "It's red."),
            ("What color is the bus?", "/uát KÓ-lor is de bas/", "It's blue."),
            ("What color is the car?", "/uát KÓ-lor is de kar/", "It's green.")]
LISTEN_PRACTICE = [("It's red.", ["blue", "red", "green"], 1), ("It's yellow.", ["yellow", "orange", "blue"], 0),
                   ("It's green.", ["red", "yellow", "green"], 2), ("It's orange.", ["orange", "green", "red"], 0)]
READ_PRACTICE = [("blue", "It's blue.", True), ("red", "It's green.", False),
                 ("yellow", "It's yellow.", True), ("orange", "It's red.", False)]
WRITE_PRACTICE = ["red", "blue", "green", "yellow"]
SPEAK_MODELS = ["What color is it?", "It's red.", "It's blue.", "That's a red bike.", "That's an orange train."]
SPEAK_TEST = [("red", "What color is it?", "It's red."), ("green", "What color is it?", "It's green."),
              ("yellow", "What color is it?", "It's yellow."), ("bike", "What's this?", "That's a bike. (That's a red bike.)")]
MEDIATION_PRACTICE = ("**Cacería de colores:** busquen en la casa un objeto de cada color. El niño dice el color en inglés (**It's blue!**) "
                      "y le explica a otro familiar qué significa en español.")
TESTS = kid.make_tests(globals(),
    listen=[("It's blue.", ["green", "blue", "red"], 1), ("It's orange.", ["orange", "yellow", "red"], 0),
            ("It's green.", ["blue", "yellow", "green"], 2), ("That's a red bike.", ["red", "green", "blue"], 0),
            ("It's yellow.", ["orange", "yellow", "blue"], 1)],
    listen_tip="Antes de cada número, **digan los 3 colores** en voz alta.",
    read_mc=[("It's green.", ["red", "green", "yellow"], 1), ("It's orange.", ["orange", "blue", "green"], 0),
             ("It's blue.", ["yellow", "red", "blue"], 2)],
    read_tf=[("It's red.", "red", True, "Es rojo."), ("It's blue.", "yellow", False, "Es amarillo: *It's yellow.*")],
    write_short=[("It's ______________.", "red", "red"), ("It's ______________.", "blue", "blue"),
                 ("It's ______________.", "green", "green")],
    write_open=("**Parte B.** Colorea una bicicleta en tu cuaderno y escribe **1 oración**: *That's a* + color + *bike*.", "That's a blue bike.",
                r"\b(that'?s|that is) an? (red|blue|green|yellow|orange) (bike|bus|car|taxi|truck|train)\b",
                "Escribió **That's a** + color + vehículo.", "That's a yellow bike."),
    speak_checks=["Picture 1: *It's red.*", "Picture 2: *It's green.*", "Picture 3: *It's yellow.*", "Picture 4: *That's a bike.*"],
    med_a=("It's yellow.", "Es amarillo.", "Escribió *amarillo*.", "Entendió *It's* = es."),
    med_b=("Tu primita dice: *«Es una bicicleta roja»*.", "That's a red bike.", r"\b(that'?s|that is) a red bike\b"))
kid.build(globals())
