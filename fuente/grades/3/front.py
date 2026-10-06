# -*- coding: utf-8 -*-
"""3.er grado · III Trimestre — portada, introducción y orden del libro."""
from common import SITE

GRADE_LABEL = "3"
TRIMESTER = "III Trimestre"
MODULES = ["repaso", "t51", "t52", "t61", "t62", "referencia"]
NAMES = {"Luis": "luːˈiːs", "Sofía": "soʊfˈiːə", "Tomás": "toʊmˈɑːs", "Pedro": "pˈeɪdɹoʊ", "Marcos": "mˈɑːɹkoʊs", "Ana": "ˈɑːnɑː", "Barrigón": "bɑːɹiːɡˈoʊn",
         "Carla": "kˈɑːɹlɑː", "Rosa": "ɹˈoʊsɑː", "Diego": "djˈeɪɡoʊ", "Penonomé": "pˌɛnoʊnoʊmˈeɪ"}

BLOCKS = [
    {"t": "book_cover",
     "title": "English 3",
     "subtitle": "English Support · III Trimestre",
     "desc": "Tu libro de apoyo para estudiar en casa, a tu ritmo, cuando sientas que lo necesitas.",
     "contents": ["Antes de empezar: repaso",
                  "Scenario 5: Let's Go Shopping!", "   Theme 1: One, Two, Three Bananas!", "   Theme 2: I Want Five Pineapples.",
                  "Scenario 6: I Can Connect with Nature!", "   Theme 1: I Can Relax and Listen.", "   Theme 2: I'm Outside. I'm Happy!",
                  "Gramática de consulta rápida"],
     "author": "José White · PanaMentorLabs"},
    {"t": "h1", "text": "Cómo usar este libro"},
    {"t": "p", "text": "Este libro sigue los temas del **III Trimestre de 3.er grado** del programa de inglés de MEDUCA. Cuando tu maestro empiece un tema en clase, búscalo aquí por su nombre (Scenario y Theme)."},
    {"t": "p", "text": "Las instrucciones están en español y cada actividad trae un ejemplo resuelto. Puedes trabajar solo, pero **es mejor si alguien de tu familia te acompaña**, sobre todo en los audios y en Speaking."},
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
    {"t": "p", "text": f"Todo está en: **{SITE}** (elige **3.er grado**)."},
    {"t": "p", "text": "Si no tienes internet, al final de cada tema están las **transcripciones** (el texto de cada audio)."},
    {"t": "h3", "text": "Consejos para estudiar"},
    {"t": "bullets", "items": [
        "Estudia en sesiones cortas: **15 a 20 minutos** cada día rinden más que 3 horas un solo día.",
        "Escribe tus respuestas en tu cuaderno si quieres usar el libro otra vez.",
        "Para Speaking, usa la **grabadora de un celular**: escucharte es la mejor forma de mejorar.",
        "Equivocarse es parte de aprender. Lo importante es leer la explicación y volver a intentarlo."]},
    {"t": "pb"},
]
