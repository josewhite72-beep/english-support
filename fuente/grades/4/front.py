# -*- coding: utf-8 -*-
"""4.º grado · III Trimestre — portada, introducción y orden del libro."""
from common import SITE

GRADE_LABEL = "4"
TRIMESTER = "III Trimestre"
MODULES = ["repaso", "t51", "t52", "t61", "t62", "referencia"]
NAMES = {"Carlos": "kˈɑːɹloʊs", "Sofía": "soʊfˈiːə", "Coronado": "kˌɔɹoʊnˈɑːdoʊ", "Pedro": "pˈeɪdɹoʊ", "Marcos": "mˈɑːɹkoʊs", "Ana": "ˈɑːnɑː", "Barrigón": "bɑːɹiːɡˈoʊn",
         "Carla": "kˈɑːɹlɑː", "Rosa": "ɹˈoʊsɑː", "Diego": "djˈeɪɡoʊ", "Penonomé": "pˌɛnoʊnoʊmˈeɪ"}

BLOCKS = [
    {"t": "book_cover",
     "title": "English 4",
     "subtitle": "English Support · III Trimestre",
     "desc": "Tu libro de apoyo para estudiar en casa, a tu ritmo, cuando sientas que lo necesitas.",
     "contents": ["Antes de empezar: repaso",
                  "Scenario 5: A Trip to the Beach", "   Theme 1: Let's Pack for a Trip.", "   Theme 2: I Always Pack Lunch.",
                  "Scenario 6: It's the Rainy Season", "   Theme 1: Where's the Puddle?", "   Theme 2: I Need an Umbrella.",
                  "Gramática de consulta rápida"],
     "author": "José White · PanaMentorLabs"},
    {"t": "h1", "text": "Cómo usar este libro"},
    {"t": "p", "text": "Este libro sigue los temas del **III Trimestre de 4.º grado** del programa de inglés de MEDUCA. Cuando tu maestro empiece un tema en clase, búscalo aquí por su nombre (Scenario y Theme)."},
    {"t": "p", "text": "Está hecho para que **puedas estudiar solo**: las instrucciones están en español y cada actividad trae un ejemplo resuelto. Si alguien de tu familia puede acompañarte, mucho mejor."},
    {"t": "h3", "text": "Cada tema tiene estas partes"},
    {"t": "bullets", "items": [
        "**¿Te sientes perdido? Empieza aquí:** lo esencial del tema en una página.",
        "**Vocabulario, Lectura y Gramática:** lo que necesitas saber, explicado en español.",
        "**Listening, Reading, Writing, Speaking y Mediation:** una práctica y un **mini-test** de cada destreza, como los de una prueba.",
        "**¿Cómo me fue?:** anota tus puntajes y descubre qué repasar.",
        "**Respuestas:** al final de cada tema, con la explicación de cada error. Corrige **solo después de terminar**."]},
    {"t": "h3", "text": "Los audios y los mini-tests en línea"},
    {"t": "p", "text": "Donde veas un código QR con la palabra **AUDIO**, hay un audio. Ábrelo con la cámara de un celular o escribe la dirección que aparece al lado. Puedes escucharlo las veces que quieras y también **en velocidad lenta**."},
    {"t": "p", "text": "Al final de cada mini-test hay otro código: con él haces el **mismo mini-test en línea**, que se corrige solo y te explica cada respuesta."},
    {"t": "p", "text": f"Todo está en: **{SITE}** (elige **4.º grado**)."},
    {"t": "p", "text": "Si no tienes internet, al final de cada tema están las **transcripciones** (el texto de cada audio)."},
    {"t": "h3", "text": "Consejos para estudiar"},
    {"t": "bullets", "items": [
        "Estudia en sesiones cortas: **20 minutos** cada día rinden más que 3 horas un solo día.",
        "Escribe tus respuestas en tu cuaderno si quieres usar el libro otra vez.",
        "Para Speaking, usa la **grabadora de un celular**: escucharte es la mejor forma de mejorar.",
        "Equivocarse es parte de aprender. Lo importante es leer la explicación y volver a intentarlo."]},
    {"t": "pb"},
]
