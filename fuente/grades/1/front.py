# -*- coding: utf-8 -*-
"""1.er grado · III Trimestre — portada, introducción para la familia y orden del libro."""
from common import SITE

GRADE_LABEL = "1"
TRIMESTER = "III Trimestre"
MODULES = ["t51", "t52", "t61", "t62", "diccionario"]
NAMES = {"Luis": "luːˈiːs", "Sofía": "soʊfˈiːə"}

BLOCKS = [
    {"t": "book_cover",
     "title": "English 1",
     "subtitle": "English Support · III Trimestre",
     "desc": "Para aprender en casa, con dibujos, audios y la compañía de la familia.",
     "contents": ["Scenario 5: Colors of Things that Go", "   Theme 1: That's a Blue Bus!", "   Theme 2: That's a Red Bike!",
                  "Scenario 6: Shapes Around Us", "   Theme 1: I See a Rectangle.", "   Theme 2: That Is a Circle.",
                  "Mi diccionario de dibujos"],
     "author": "José White · PanaMentorLabs"},
    {"t": "h1", "text": "Para la familia: cómo usar este libro"},
    {"t": "p", "text": "Este libro sigue los temas del **III Trimestre de 1.er grado** del programa de inglés de MEDUCA. Cuando el maestro empiece un tema en clase, búsquenlo aquí por su nombre."},
    {"t": "p", "text": "**Usted no necesita saber inglés.** Las instrucciones están en español y cada palabra trae su pronunciación entre barras, por ejemplo *bus* /bas/. Usted lee las instrucciones; el niño o la niña **escucha, señala, repite, lee y escribe**."},
    {"t": "h3", "text": "Cada tema tiene estas partes"},
    {"t": "bullets", "items": [
        "**Palabras nuevas, la frase del tema, una canción y un cuento**, todo con dibujos y audio.",
        "**Listening, Reading, Writing, Speaking y Mediation:** una práctica y un **mini-test** corto de cada destreza.",
        "**¿Cómo me fue?:** el niño marca cómo se siente con cada logro.",
        "**Respuestas para el adulto** y el **texto de cada audio**, al final del tema."]},
    {"t": "h3", "text": "Los audios y los mini-tests en línea"},
    {"t": "p", "text": "Donde vea un código QR con la palabra **AUDIO**, abra la cámara del celular y apunte al código. El audio se puede repetir las veces que quieran y también en **velocidad lenta**."},
    {"t": "p", "text": "Al final de cada mini-test hay otro código: con él el niño hace el **mismo mini-test en el celular o la computadora**, tocando los dibujos. Se corrige solo."},
    {"t": "p", "text": f"Todo está en: **{SITE}** (elijan **1.er grado**)."},
    {"t": "h3", "text": "Consejos"},
    {"t": "bullets", "items": [
        "**15 a 20 minutos al día** rinden más que una hora seguida.",
        "Deje que el niño lo intente primero; ayude solo si se queda trabado unos segundos.",
        "No corrija con un \"no\": repita la respuesta correcta con alegría y pida que la diga otra vez.",
        "Usen lo que hay alrededor: en una caminata, señale algo y pregunte en inglés."]},
    {"t": "p", "text": "*Ilustraciones: dibujos de los módulos GeMA y OpenMoji (openmoji.org), licencia CC BY-SA 4.0.*"},
    {"t": "pb"},
]
