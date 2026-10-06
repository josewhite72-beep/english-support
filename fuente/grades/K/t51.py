# -*- coding: utf-8 -*-
"""Kínder · Scenario 5, Theme 1 — The Cat Says Meow!
Fuentes: planeamiento K_5-1 y módulo GeMA K_5-1 (dibujos del módulo)."""
from common import *
import kid

THEME_ID, THEME_NUM = "5-1", "Theme 1"
THEME_TITLE, THEME_ES = "The Cat Says Meow!", "¡El gato dice miau!"
SCENARIO = "Scenario 5: What's that Sound?"
COPY = True
GOALS = ["Escucho el nombre de 6 animales y **señalo** el dibujo.",
         "Respondo *What does the cat say?* con *The cat says meow!*",
         "Copio el nombre de los animales."]
FAMILY = ("En este tema su niño/a aprende **6 animales** y **cómo \"hablan\" en inglés**: **What does the cat say? — The cat says meow!** "
          "/uát das de kat sei — de kat ses miáu/ (¿Qué dice el gato? — ¡El gato dice miau!)")
VOCAB = [("cat", "cat", "/kat/", "gato", "The cat says meow!"),
         ("dog", "dog", "/dog/", "perro", "The dog says woof, woof!"),
         ("bird", "bird", "/berd/", "pájaro", "The bird says tweet, tweet!"),
         ("duck", "duck", "/dak/", "pato", "The duck says quack, quack!"),
         ("pig", "pig", "/pig/", "cerdo", "The pig says oink, oink!"),
         ("cow", "cow", "/kau/", "vaca", "The cow says moo!")]
SOUND_TITLE = "¡Los animales hablan distinto en cada idioma!"
SOUND = ["**Adulto:** pregunte en español \"¿Qué dice el perro?\" (guau guau). Luego diga el sonido en inglés y ríanse juntos de la diferencia:",
         "gato **meow** /miáu/ · perro **woof** /guf/ · pájaro **tweet** /tuit/ · pato **quack** /kuak/ · cerdo **oink** /oink/ · vaca **moo** /mu/"]
PATTERN = {"rows": [["**The cat**", "**says**", "**meow!**"], ["El gato", "dice", "¡miau!"]],
           "note": "**Nota para la familia:** usted pregunta **What does the cat say?** /uát das de kat sei/ = ¿Qué dice el gato? Al principio basta con que el niño haga el sonido; después, que diga la frase completa."}
SONG_TITLE = "What Does the Cat Say?"
SONG = [("What does the cat say? Meow, meow, meow!", "Dibuja bigotes en tu cara."),
        ("What does the dog say? Woof, woof, woof!", "Pon las manos como patitas."),
        ("What does the bird say? Tweet, tweet, tweet!", "Mueve los brazos como alas."),
        ("What does the duck say? Quack, quack, quack!", "Abre y cierra las manos como un pico."),
        ("What does the pig say? Oink, oink, oink!", "Empuja tu nariz hacia arriba.")]
STORY_TITLE = "Who Says Moo?"
STORY = [("cat", "The cat says meow!"), ("dog", "The dog says woof, woof!"), ("duck", "The duck says quack, quack!"),
         ("pig", "The pig says oink, oink!"), ("cow", "And the cow says moo!")]
STORY_QS = [("What does the dog say?", "/uát das de dog sei/", "Woof, woof! (The dog says woof!)"),
            ("What does the duck say?", "/uát das de dak sei/", "Quack, quack!"),
            ("Who says moo?", "/ju ses mu/", "The cow!")]
LISTEN_PRACTICE = [("Cat.", ["dog", "cat", "pig"], 1), ("Cow.", ["cow", "duck", "bird"], 0),
                   ("Duck.", ["pig", "cat", "duck"], 2), ("Bird.", ["bird", "cow", "dog"], 0)]
READ_PRACTICE = [("cat", "cat", True), ("dog", "pig", False), ("cow", "cow", True), ("duck", "bird", False)]
WRITE_PRACTICE = ["cat", "dog", "pig", "cow"]
SPEAK_MODELS = ["Cat. Dog. Bird.", "Duck. Pig. Cow.", "The cat says meow!", "The dog says woof!", "The cow says moo!"]
SPEAK_TEST = [("cat", "What does the cat say?", "Meow! (The cat says meow!)"), ("dog", "What does the dog say?", "Woof, woof!"),
              ("duck", "What does the duck say?", "Quack, quack!"), ("cow", "What does the cow say?", "Moo!")]
MEDIATION_PRACTICE = ("El niño le enseña a un familiar cómo \"hablan\" los animales en inglés: hace el sonido en inglés y el familiar adivina el animal. "
                      "Luego le explica en español: \"En inglés, el perro dice *woof*\".")
TESTS = kid.make_tests(globals(),
    listen=[("The dog says woof, woof!", ["cat", "dog", "cow"], 1), ("Moo! The cow says moo!", ["cow", "pig", "duck"], 0),
            ("The pig says oink, oink!", ["bird", "duck", "pig"], 2), ("Tweet, tweet! It's a bird.", ["bird", "cat", "dog"], 0),
            ("Quack, quack! It's a duck.", ["pig", "duck", "cow"], 1)],
    listen_tip="Antes de cada número, **digan los 3 animales** y hagan su sonido.",
    read_mc=[("cat", ["dog", "cat", "cow"], 1), ("pig", ["pig", "duck", "bird"], 0), ("duck", ["cow", "cat", "duck"], 2)],
    read_tip="**Adulto:** señale la palabra con el dedo y léanla juntos, letra por letra.",
    read_tf=[("dog", "dog", True, "Es un perro."), ("cow", "pig", False, "Es un cerdo: *pig*.")],
    write_short=[("Copia: **cat** → ______________", "cat", "cat"), ("Copia: **dog** → ______________", "dog", "dog"),
                 ("Copia: **cow** → ______________", "cow", "cow")],
    write_tip="**Adulto:** el niño copia la palabra mirando el modelo. Ayúdele a contar las letras.",
    write_open=("**Parte B.** Dibuja tu animal favorito en tu cuaderno y **copia** su nombre debajo.", "pig",
                "", "", "duck"),
    write_open_checks=[{"text": "Dibujó un animal."}, {"text": "Copió su nombre en inglés.", "auto": r"\b(cat|dog|bird|duck|pig|cow)\b"}],
    speak_checks=["Picture 1: *Meow!*", "Picture 2: *Woof, woof!*", "Picture 3: *Quack, quack!*", "Picture 4: *Moo!*"],
    med_a=None, med_b=None,
    mediation=kid.k_mediation("The cat says meow!", "El gato dice miau.", "El niño le enseña a un familiar dos animales en inglés con su sonido."))
kid.build(globals())
