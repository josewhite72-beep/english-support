# -*- coding: utf-8 -*-
"""Gramática de consulta rápida (al final del libro)."""
from common import *

BLOCKS = [
    H1("Gramática de consulta rápida"),
    P("Usa estas páginas la noche antes de una prueba. Al lado de cada tema está **dónde se explica con más detalle**."),

    H2("Comparativos y superlativos (Tema 5.1)"),
    TABLE([3000, 3400, 3400], ["Palabra", "Comparativo (2 cosas)", "Superlativo (el más)"], [
        ["corta: old, new, quiet", "old**er than**", "**the** old**est**"],
        ["corta con doble letra: big, hot", "bi**gger than**", "**the** bi**ggest**"],
        ["termina en y: busy, pretty", "bus**ier than**", "**the** bus**iest**"],
        ["larga: beautiful, famous", "**more** beautiful **than**", "**the most** beautiful"],
        ["irregular: good / bad", "**better / worse** than", "**the best / the worst**"],
    ]),
    P("✗ more busy · ✗ bigger **that** · ✗ is oldest  →  ✓ **busier** · ✓ bigger **than** · ✓ is **the** oldest"),

    H2("There is / There are (Tema 5.1)"),
    P("There **is** + una cosa · There **are** + varias · **Is there...? / Are there...?**"),

    H2("Presente perfecto (Tema 5.2)"),
    TABLE([3300, 3300, 3200], ["Afirmativa", "Negativa", "Pregunta"], [
        ["I / you / we / they **have** lived", "I **haven't** lived", "**Have** you lived...?"],
        ["he / she / it **has** been", "it **hasn't** changed", "**Has** it changed?"],
    ]),
    P("Participios: be → **been** · have → **had** · know → **known** · teach → **taught** · live → **lived** · work → **worked** · study → **studied** · change → **changed**"),

    H2("For y since (Tema 5.2)"),
    TABLE([4900, 4900], ["for + cantidad de tiempo", "since + momento"], [
        ["for ten years · for two weeks · for a long time", "since 1965 · since Monday · since first grade"],
    ]),
    P("**How long** has it been here? — It has been here **for** sixty years. / **since** 1965."),

    H2("Futuro con will (Tema 6.1)"),
    TABLE([3300, 3300, 3200], ["Afirmativa", "Negativa", "Pregunta y respuesta"], [
        ["It **will be** sunny.", "It **won't rain**.", "**Will** it rain? — Yes, it **will**. / No, it **won't**."],
    ]),
    P("Después de *will* y de *should*: verbo en forma base, sin *to* y sin *-s*: *It will **be** · You should **bring***"),

    H2("Should para consejos (Tema 6.1)"),
    P("*It will be rainy. You **should bring** an umbrella.* · *It's hot. You **should drink** water.* · *You **shouldn't go** to the beach.*"),

    H2("Going to para predicciones (Tema 6.2)"),
    P("am / is / are + **going to** + verbo, cuando **vemos** algo: *Look at the clouds! It**'s going to** rain.*"),
    P("**will** = pronóstico o lo que creemos · **going to** = lo que estamos viendo (evidencia)"),

    H2("Contar un cambio (Tema 6.2)"),
    P("**first** → **then** → **later** → **finally** · The temperature will **go up** / **go down**."),

    H2("El tiempo"),
    P("sun**ny** · rain**y** · cloud**y** · wind**y** · storm**y** · hot · cold · cool · *The temperature is 28 **degrees**.*"),

    H2("Cómo se leen los años"),
    P("1965 = nineteen sixty-five · 2010 = twenty ten · 2026 = twenty twenty-six · 2005 = two thousand five"),

    H2("Palabras que más se confunden en las pruebas"),
    TABLE([3000, 6800], ["Palabras", "Diferencia"], [
        ["**than / that**", "*than* = que (en comparaciones: *bigger than*). *that* = ese, eso, que (*that school*)."],
        ["**for / since**", "*for* + cantidad (*for 5 years*). *since* + momento (*since 2020*)."],
        ["**fifteen / fifty**", "fif**TEEN** (15), acento al final. **FIF**ty (50), acento al inicio."],
        ["**has / have**", "*has* con he, she, it (y *my family, the school*). *have* con I, you, we, they."],
        ["**was / has been**", "*It was old* = era viejo (ya no). *It has been here* = ha estado aquí (y sigue)."],
        ["**will / going to**", "*will* = pronóstico (*The forecast says it will rain*). *going to* = lo veo (*Look! It's going to rain*)."],
        ["**sun / sunny**", "*sun* = el sol (sustantivo). *sunny* = soleado (para describir el tiempo: *It is sunny*)."],
    ]),
]
