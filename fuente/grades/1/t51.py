# -*- coding: utf-8 -*-
"""1.er grado · Scenario 5, Theme 1 — That's a Blue Bus!
Fuentes: planeamiento 1_5-1 y módulo GeMA 1_5-1 (dibujos del módulo)."""
from common import *
import kid

THEME_ID, THEME_NUM = "5-1", "Theme 1"
THEME_TITLE, THEME_ES = "That's a Blue Bus!", "¡Es un bus azul!"
SCENARIO = "Scenario 5: Colors of Things that Go"
GOALS = ["Reconozco 6 vehículos cuando los escucho.",
         "Pregunto *What's this?* y respondo *That's a bus.*",
         "Leo oraciones cortas y las uno con su dibujo.",
         "Escribo el nombre de los vehículos."]
FAMILY = ("En este tema su hijo/a aprende **6 vehículos** en inglés y a decir **What's this? — That's a bus.** "
          "/uats dis — dats a bas/ (¿Qué es esto? — Es un bus.)")
VOCAB = [("car", "car", "/kar/", "carro", "That's a car."),
         ("bus", "bus", "/bas/", "bus", "That's a bus."),
         ("taxi", "taxi", "/TÁK-si/", "taxi", "That's a taxi."),
         ("truck", "truck", "/trak/", "camión", "That's a truck."),
         ("train", "train", "/trein/", "tren", "That's a train."),
         ("bike", "bike", "/baik/", "bicicleta", "That's a bike.")]
SOUND = ["Diga despacio: **t-t-taxi, t-t-truck, t-t-train** y **b-b-bus, b-b-bike**. ¿Suenan igual al principio?"]
PATTERN = {"rows": [["**That's**", "**a**", "**bus.**"], ["Es", "un", "bus."]],
           "note": "**Nota para la familia:** para preguntar se dice **What's this?** /uats dis/ = ¿Qué es esto? Y se responde **That's a...** /dats a/ = Es un..."}
SONG_TITLE = "Beep, Beep, Beep!"
SONG = [("Blue bus, blue bus, beep, beep, beep!", "Aprieta la bocina."),
        ("Yellow taxi, yellow taxi, honk, honk, honk!", "Levanta la mano para pedir el taxi."),
        ("Red car, red car, vroom, vroom, vroom!", "Maneja con el volante."),
        ("Green truck, green truck, rumble, rumble!", "Mueve los hombros como un camión."),
        ("That's a blue bus! Beep, beep, beep!", "Di adiós con la mano.")]
STORY_TITLE = "Tom at the Bus Stop"
STORY = [("taxi", "Look! That's a taxi."), ("truck", "That's a truck."), ("car", "That's a car."),
         ("train", "That's a train."), ("bus", "Look, Mom! That's a blue bus!")]
STORY_QS = [("Number 1. What's this?", "/NÁM-ber uan. uats dis/", "That's a taxi."),
            ("Number 2. What's this?", "/NÁM-ber tu. uats dis/", "That's a truck."),
            ("Number 5. What's this?", "/NÁM-ber faiv. uats dis/", "That's a bus.")]
LISTEN_PRACTICE = [("That's a taxi.", ["car", "taxi", "bike"], 1), ("That's a train.", ["train", "bus", "truck"], 0),
                   ("That's a bike.", ["taxi", "truck", "bike"], 2), ("That's a bus.", ["bus", "car", "train"], 0)]
READ_PRACTICE = [("bus", "That's a bus.", True), ("car", "That's a train.", False),
                 ("bike", "That's a bike.", True), ("truck", "That's a taxi.", False)]
WRITE_PRACTICE = ["car", "bus", "bike", "taxi"]
SPEAK_MODELS = ["What's this?", "That's a car.", "That's a bus.", "That's a train.", "That's a blue bus!"]
SPEAK_TEST = [("car", "What's this?", "That's a car."), ("bus", "What's this?", "That's a bus."),
              ("train", "What's this?", "That's a train."), ("bike", "What's this?", "That's a bike.")]
MEDIATION_PRACTICE = ("Asómense a la ventana o salgan a la calle. Cada vez que pase un vehículo, el niño lo nombra en inglés "
                      "(**That's a car!**) y le enseña la palabra a otro familiar, diciéndole qué significa.")
TESTS = kid.make_tests(globals(),
    listen=[("That's a car.", ["truck", "car", "train"], 1), ("That's a bike.", ["bike", "taxi", "bus"], 0),
            ("That's a truck.", ["bus", "car", "truck"], 2), ("That's a train.", ["train", "bike", "taxi"], 0),
            ("That's a taxi.", ["car", "taxi", "truck"], 1)],
    read_mc=[("That's a bus.", ["train", "bus", "car"], 1), ("That's a bike.", ["bike", "truck", "taxi"], 0),
             ("That's a train.", ["car", "taxi", "train"], 2)],
    read_tf=[("That's a truck.", "truck", True, "Es un camión."), ("That's a car.", "bus", False, "Es un bus: *That's a bus.*")],
    write_short=[("That's a ______________.", "bus", "bus"), ("That's a ______________.", "car", "car"),
                 ("That's a ______________.", "bike", "bike")],
    write_open=("**Parte B.** Dibuja tu vehículo favorito y escribe **1 oración** con *That's a...*", "That's a train.",
                r"\bthat'?s a (car|bus|taxi|truck|train|bike)\b|\bthat is a (car|bus|taxi|truck|train|bike)\b",
                "Escribió **That's a** + un vehículo.", "That's a taxi."),
    speak_checks=["Picture 1: *That's a car.*", "Picture 2: *That's a bus.*", "Picture 3: *That's a train.*", "Picture 4: *That's a bike.*"],
    med_a=("That's a truck.", "Es un camión.", "Escribió *Es un camión*.", "Entendió *truck* = camión."),
    med_b=("Tu hermanito dice: *«Es un taxi»*.", "That's a taxi.", r"\b(that'?s|that is) a taxi\b"))
kid.build(globals())
