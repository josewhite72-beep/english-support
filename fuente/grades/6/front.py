# -*- coding: utf-8 -*-
"""6.º grado · III Trimestre — portada, introducción y orden del libro."""
from common import SITE

GRADE_LABEL = "6"
TRIMESTER = "III Trimestre"
MODULES = ["repaso", "t51", "t52", "t61", "t62", "referencia"]
NAMES = {"Marco": "mˈɑːɹkoʊ", "Rosa": "ɹˈoʊsɑː", "Ana": "ˈɑːnɑː", "Carmen": "kˈɑːɹmɛn", "Panamá": "pɑːnɑːmˈɑː", "Barrigón": "bɑːɹiːɡˈoʊn", "Valeria": "vɑːlˈɛɹiɑː", "Diego": "djˈeɪɡoʊ"}

BLOCKS = [
    {"t": "book_cover",
     "title": "English 6",
     "subtitle": "English Support · III Trimestre",
     "desc": "Tu libro de apoyo para estudiar en casa, a tu ritmo, cuando sientas que lo necesitas.",
     "contents": ["Antes de empezar: repaso", "Scenario 5: Our Amazing Community",
                  "   Theme 1: This Is My Amazing Community.", "   Theme 2: This School Has Been Here a Long Time!",
                  "Scenario 6: Our Weather Report", "   Theme 1: Today's Weather Will Be Sunny with Some Rain Later.",
                  "   Theme 2: How Will the Weather Change Tomorrow?",
                  "Gramática de consulta rápida"],
     "author": "José White · PanaMentorLabs"},
    {"t": "h1", "text": "Cómo usar este libro"},
    {"t": "p", "text": "Este libro sigue los temas del **III Trimestre de 6.º grado** del programa de inglés de MEDUCA. Cuando tu maestro empiece un tema en clase, búscalo aquí por su nombre (Scenario y Theme)."},
    {"t": "p", "text": "Está hecho para que **puedas estudiar solo**: las instrucciones están en español y cada actividad trae un ejemplo resuelto. Si alguien de tu familia puede acompañarte, mucho mejor, pero no es necesario."},
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
    {"t": "p", "text": f"Todo está en: **{SITE}** (elige **6.º grado**)."},
    {"t": "p", "text": "Si no tienes internet, al final de cada tema están las **transcripciones** (el texto de cada audio)."},
    {"t": "h3", "text": "Consejos para estudiar"},
    {"t": "bullets", "items": [
        "Estudia en sesiones cortas: **20 minutos** cada día rinden más que 3 horas un solo día.",
        "Escribe tus respuestas en tu cuaderno si quieres usar el libro otra vez.",
        "Para Speaking, usa la **grabadora de un celular**: escucharte es la mejor forma de mejorar.",
        "Equivocarse es parte de aprender. Lo importante es leer la explicación y volver a intentarlo."]},
    {"t": "pb"},
]
