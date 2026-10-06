# -*- coding: utf-8 -*-
"""Kínder · Scenario 6, Theme 1 — Move Around!
Fuentes: planeamiento K_6-1 y módulo GeMA K_6-1. Dibujos: OpenMoji (CC BY-SA 4.0) y propios."""
from common import *
import kid

THEME_ID, THEME_NUM = "6-1", "Theme 1"
THEME_TITLE, THEME_ES = "Move Around!", "¡Muévete!"
SCENARIO = "Scenario 6: Let's Dance!"
COPY = True
GOALS = ["Escucho una orden y **hago el movimiento**: *step, dance, spin, hop*.",
         "Digo *Step and dance! Spin and hop!*",
         "Copio palabras de movimiento."]
FAMILY = ("En este tema su niño/a aprende palabras para **moverse y bailar**: **step** (paso), **dance** (bailar), **spin** (girar), "
          "**hop** (saltar en un pie), **foot** (pie) y **circle** (círculo). ¡Todo se aprende con el cuerpo!")
VOCAB = [("step", "step", "/step/", "paso", "Step, step, step!"),
         ("dance", "dance", "/dans/", "bailar", "Dance, dance, dance!"),
         ("foot", "foot", "/fut/", "pie", "This is my foot."),
         ("circle", "circle", "/SÉR-kol/", "círculo", "Dance in a circle!"),
         ("spin", "spin", "/spin/", "girar", "Spin around!"),
         ("hop", "hop", "/jop/", "saltar en un pie", "Hop, hop, hop!")]
SOUND = ["**/d/** como en **dance** /dans/ · **/s/** como en **spin** /spin/ y **step** /step/ (sin \"e\" al principio: no \"estep\").",
         "**Adulto:** diga una palabra y el niño **hace el movimiento**. Luego cambien: el niño da la orden."]
PATTERN = {"rows": [["**Step**", "**and**", "**dance!**"], ["Da pasos", "y", "¡baila!"]],
           "note": "**Nota para la familia:** son **órdenes** cortas. Diga **Spin and hop!** /spin and jop/ y el niño gira y salta. ¡Háganlo juntos!"}
SONG_TITLE = "Step and Dance"
SONG = [("Step, step, step and dance!", "Da pasos y baila."), ("Foot, foot, foot and spin!", "Señala el pie y gira."),
        ("Circle, circle, hop, hop, hop!", "Dibuja un círculo y salta."), ("Step and dance! Spin and hop!", "Haz los cuatro movimientos.")]
STORY_TITLE = "Let's Move!"
STORY = [("foot", "This is my foot."), ("step", "Step, step, step!"), ("dance", "I dance!"),
         ("spin", "I spin around!"), ("hop", "Hop, hop, hop! Let's dance!")]
STORY_QS = [("Show me: step!", "/shou mi step/", "El niño da pasos."), ("Show me: spin!", "/shou mi spin/", "El niño gira."),
            ("Show me: hop!", "/shou mi jop/", "El niño salta en un pie.")]
LISTEN_PRACTICE = [("Spin!", ["hop", "spin", "foot"], 1), ("Dance!", ["dance", "step", "circle"], 0),
                   ("Hop!", ["foot", "dance", "hop"], 2), ("Foot.", ["foot", "spin", "step"], 0)]
READ_PRACTICE = [("hop", "hop", True), ("spin", "step", False), ("dance", "dance", True), ("foot", "hop", False)]
WRITE_PRACTICE = ["hop", "step", "foot", "spin"]
SPEAK_MODELS = ["Step and dance!", "Spin and hop!", "Step, step, step!", "Hop, hop, hop!", "This is my foot."]
SPEAK_TEST = [("step", "What is it?", "Step!"), ("spin", "What is it?", "Spin!"), ("hop", "What is it?", "Hop!"),
              ("foot", "What is it?", "Foot! (This is my foot.)")]
MEDIATION_PRACTICE = ("El niño **enseña un baile** a un familiar: da las órdenes en inglés (**Step! Spin! Hop!**) y el familiar las hace. "
                      "Si el familiar no entiende, el niño le explica en español.")
TESTS = kid.make_tests(globals(),
    listen=[("Step, step, step!", ["hop", "step", "spin"], 1), ("Spin around!", ["spin", "foot", "dance"], 0),
            ("Dance!", ["circle", "hop", "dance"], 2), ("Hop, hop, hop!", ["hop", "step", "foot"], 0),
            ("Dance in a circle!", ["foot", "circle", "spin"], 1)],
    listen_tip="Antes de cada número, **hagan los 3 movimientos** de los dibujos.",
    read_mc=[("spin", ["step", "spin", "hop"], 1), ("foot", ["foot", "dance", "circle"], 0), ("dance", ["hop", "foot", "dance"], 2)],
    read_tip="**Adulto:** señale la palabra con el dedo y léanla juntos, letra por letra.",
    read_tf=[("hop", "hop", True, "Saltar en un pie."), ("circle", "step", False, "Son pasos: *step*.")],
    write_short=[("Copia: **hop** → ______________", "hop", "hop"), ("Copia: **step** → ______________", "step", "step"),
                 ("Copia: **spin** → ______________", "spin", "spin")],
    write_tip="**Adulto:** el niño copia la palabra mirando el modelo. Ayúdele a contar las letras.",
    write_open=("**Parte B.** Dibuja tu pie (pon el pie sobre la hoja y marca su forma) y **copia** debajo: *foot*.", "foot", "", "", "foot"),
    write_open_checks=[{"text": "Dibujó su pie."}, {"text": "Copió *foot*.", "auto": r"\bfoot\b"}],
    speak_checks=["Picture 1: *Step!*", "Picture 2: *Spin!*", "Picture 3: *Hop!*", "Picture 4: *Foot!*"],
    med_a=None, med_b=None,
    mediation=kid.k_mediation("Spin and hop!", "¡Gira y salta!", "El niño da dos órdenes en inglés a un familiar (*Step! Hop!*) y el familiar las hace."))
kid.build(globals())
