# -*- coding: utf-8 -*-
"""Kínder · Scenario 5, Theme 2 — That's a Rooster!
Fuentes: planeamiento K_5-2 y módulo GeMA K_5-2 (dibujos del módulo)."""
from common import *
import kid

THEME_ID, THEME_NUM = "5-2", "Theme 2"
THEME_TITLE, THEME_ES = "That's a Rooster!", "¡Es un gallo!"
SCENARIO = "Scenario 5: What's that Sound?"
COPY = True
GOALS = ["Escucho y **señalo** 6 animales de la granja.",
         "Digo *That's a rooster!* y el sonido de cada animal.",
         "Copio el nombre de los animales."]
FAMILY = ("En este tema su niño/a aprende **animales de la granja** y a decir **What's this? — That's a rooster!** "
          "/uats dis — dats a RÚS-ter/ (¿Qué es esto? — ¡Es un gallo!)")
VOCAB = [("rooster", "rooster", "/RÚS-ter/", "gallo", "That's a rooster! Cock-a-doodle-doo!"),
         ("hen", "hen", "/jen/", "gallina", "That's a hen! Cluck, cluck!"),
         ("cow", "cow", "/kau/", "vaca", "That's a cow! Moo!"),
         ("duck", "duck", "/dak/", "pato", "That's a duck! Quack, quack!"),
         ("dog", "dog", "/dog/", "perro", "That's a dog! Woof, woof!"),
         ("farm", "farm", "/farm/", "granja", "I love the farm!")]
SOUND_TITLE = "¡Los animales hablan distinto en cada idioma!"
SOUND = ["gallo **cock-a-doodle-doo** /ká-ka-du-dol-DÚ/ (kikirikí) · gallina **cluck, cluck** /klak klak/ (coc coc) · vaca **moo** /mu/ · pato **quack** /kuak/ · perro **woof** /guf/"]
PATTERN = {"rows": [["**That's a**", "**rooster!**", ""], ["Es un", "¡gallo!", ""]],
           "note": "**Nota para la familia:** usted señala un animal y pregunta **What's this?** /uats dis/ = ¿Qué es esto? El niño responde **That's a cow!** y hace el sonido."}
SONG_TITLE = "On the Farm"
SONG = [("That's a rooster! Cock-a-doodle-doo!", "Mueve los brazos como alas."),
        ("That's a hen! Cluck, cluck, cluck!", "Picotea con la mano."),
        ("That's a cow! Moo, moo, moo!", "Haz cuernos con los dedos."),
        ("That's a duck! Quack, quack, quack!", "Abre y cierra las manos como un pico."),
        ("On the farm, on the farm, I love the farm!", "Aplaude y abrázate.")]
STORY_TITLE = "Good Morning, Farm!"
STORY = [("farm", "Good morning, farm!"), ("rooster", "That's a rooster. Cock-a-doodle-doo!"), ("hen", "That's a hen. Cluck, cluck!"),
         ("cow", "That's a cow. Moo!"), ("duck", "That's a duck. Quack, quack!")]
STORY_QS = [("Number 2. What's this?", "/NÁM-ber tu. uats dis/", "That's a rooster!"),
            ("Number 3. What's this?", "/NÁM-ber zri. uats dis/", "That's a hen!"),
            ("What does the cow say?", "/uát das de kau sei/", "Moo!")]
LISTEN_PRACTICE = [("That's a rooster!", ["hen", "rooster", "dog"], 1), ("That's a hen!", ["hen", "cow", "duck"], 0),
                   ("That's a cow!", ["duck", "dog", "cow"], 2), ("That's a farm!", ["farm", "rooster", "hen"], 0)]
READ_PRACTICE = [("hen", "hen", True), ("rooster", "cow", False), ("duck", "duck", True), ("dog", "hen", False)]
WRITE_PRACTICE = ["hen", "cow", "duck", "dog"]
SPEAK_MODELS = ["What's this?", "That's a rooster!", "That's a hen!", "That's a cow!", "I love the farm!"]
SPEAK_TEST = [("rooster", "What's this?", "That's a rooster!"), ("hen", "What's this?", "That's a hen!"),
              ("cow", "What's this?", "That's a cow!"), ("duck", "What does the duck say?", "Quack, quack!")]
MEDIATION_PRACTICE = ("Juego **¿Quién soy?**: un familiar hace el sonido en español (kikirikí). El niño dice el animal en inglés (**That's a rooster!**) "
                      "y hace el sonido en inglés. Luego cambian.")
TESTS = kid.make_tests(globals(),
    listen=[("That's a hen!", ["cow", "hen", "dog"], 1), ("Cock-a-doodle-doo! That's a rooster!", ["rooster", "duck", "cat"], 0),
            ("That's a dog!", ["hen", "cow", "dog"], 2), ("Moo! That's a cow!", ["cow", "rooster", "duck"], 0),
            ("That's a duck!", ["dog", "duck", "hen"], 1)],
    listen_tip="Antes de cada número, **digan los 3 animales** y hagan su sonido.",
    read_mc=[("hen", ["rooster", "hen", "cow"], 1), ("cow", ["cow", "dog", "duck"], 0), ("rooster", ["duck", "hen", "rooster"], 2)],
    read_tip="**Adulto:** señale la palabra con el dedo y léanla juntos, letra por letra.",
    read_tf=[("duck", "duck", True, "Es un pato."), ("dog", "cow", False, "Es una vaca: *cow*.")],
    write_short=[("Copia: **hen** → ______________", "hen", "hen"), ("Copia: **cow** → ______________", "cow", "cow"),
                 ("Copia: **duck** → ______________", "duck", "duck")],
    write_tip="**Adulto:** el niño copia la palabra mirando el modelo. Ayúdele a contar las letras.",
    write_open=("**Parte B.** Dibuja un animal de la granja y **copia** su nombre debajo.", "hen", "", "", "cow"),
    write_open_checks=[{"text": "Dibujó un animal de la granja."}, {"text": "Copió su nombre en inglés.", "auto": r"\b(rooster|hen|cow|duck|dog|cat|pig)\b"}],
    speak_checks=["Picture 1: *That's a rooster!*", "Picture 2: *That's a hen!*", "Picture 3: *That's a cow!*", "Picture 4: *Quack, quack!*"],
    med_a=None, med_b=None,
    mediation=kid.k_mediation("That's a rooster!", "¡Es un gallo!", "El niño le enseña a un familiar cómo dice el gallo en inglés: *cock-a-doodle-doo!*"))
kid.build(globals())
