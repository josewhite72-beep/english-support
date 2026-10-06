# -*- coding: utf-8 -*-
"""Kínder · III Trimestre — portada, introducción para la familia y orden del libro."""
from common import SITE

GRADE_LABEL = "K"
TRIMESTER = "III Trimestre"
MODULES = ["t51", "t52", "t61", "t62", "diccionario"]
NAMES = {"Luis": "luːˈiːs", "Sofía": "soʊfˈiːə"}

BLOCKS = [
    {"t": "book_cover",
     "title": "English K",
     "subtitle": "English Support · III Trimestre",
     "desc": "Para aprender en casa, con dibujos, audios y la compañía de la familia.",
     "contents": ["Scenario 5: What's that Sound?", "   Theme 1: The Cat Says Meow!", "   Theme 2: That's a Rooster!",
                  "Scenario 6: Let's Dance!", "   Theme 1: Move Around!", "   Theme 2: One Step In, Two Steps Out!",
                  "Mi diccionario de dibujos"],
     "author": "José White · PanaMentorLabs"},
    {"t": "h1", "text": "Para la familia: cómo usar este libro"},
    {"t": "p", "text": "Este libro sigue los temas del **III Trimestre de Kínder** del programa de inglés de MEDUCA. Cuando el maestro empiece un tema en clase, búsquenlo aquí por su nombre."},
    {"t": "p", "text": "**Usted no necesita saber inglés.** Las instrucciones están en español y cada palabra trae su pronunciación entre barras, por ejemplo *cat* /kat/. Usted lee las instrucciones; el niño o la niña **escucha, señala, repite, se mueve y copia palabras**."},
    {"t": "h3", "text": "Cada tema tiene estas partes"},
    {"t": "bullets", "items": [
        "**Palabras nuevas, la frase del tema, una canción y un cuento**, todo con dibujos y audio.",
        "**Listening, Reading, Writing, Speaking y Mediation:** una práctica y un **mini-test** corto de cada destreza.",
        "**¿Cómo me fue?:** el niño marca cómo se siente con cada logro.",
        "**Respuestas para el adulto** y el **texto de cada audio**, al final del tema."]},
    {"t": "h3", "text": "Los audios y los mini-tests en línea"},
    {"t": "p", "text": "Donde vea un código QR con la palabra **AUDIO**, abra la cámara del celular y apunte al código. El audio se puede repetir las veces que quieran y también en **velocidad lenta**."},
    {"t": "p", "text": "Al final de cada mini-test hay otro código: con él el niño hace el **mismo mini-test en el celular o la computadora**, tocando los dibujos. Se corrige solo."},
    {"t": "p", "text": f"Todo está en: **{SITE}** (elijan **Kínder**)."},
    {"t": "h3", "text": "Consejos"},
    {"t": "bullets", "items": [
        "**10 a 15 minutos al día** rinden más que una hora seguida. En Kínder, ¡mejor jugando!",
        "Deje que el niño lo intente primero; ayude solo si se queda trabado unos segundos.",
        "No corrija con un \"no\": repita la respuesta correcta con alegría y pida que la diga otra vez.",
        "Usen lo que hay alrededor: en una caminata, señale algo y pregunte en inglés."]},
    {"t": "p", "text": "*Ilustraciones: dibujos de los módulos GeMA y OpenMoji (openmoji.org), licencia CC BY-SA 4.0.*"},
    {"t": "pb"},
]
