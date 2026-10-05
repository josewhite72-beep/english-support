# Fuente de "English Support" (libros de apoyo por grado)

Todo lo necesario para regenerar, por grado, **el libro en Word, los audios, los QR y el sitio**.
Vercel no publica esta carpeta (ver `.vercelignore`).

## Estructura

| Archivo / carpeta | Qué es |
|---|---|
| `common.py` | Funciones compartidas y la dirección del sitio (`SITE`, impresa en los QR). |
| `grades/<grado>/front.py` | Portada, "Cómo usar este libro", trimestre, orden de los módulos (`MODULES`) y pronunciación de nombres propios del grado (`NAMES`). |
| `grades/<grado>/t51.py`, `t52.py`… | Cada tema (Scenario-Theme): vocabulario, lectura, gramática, prácticas, respuestas y textos de los audios (`TRACKS`). |
| `grades/<grado>/tests_t51.py`… | Los mini-tests como datos. **El libro y la versión en línea salen de aquí.** |
| `build_assets.py` | Audios (Kokoro, normal y lento), QR y `out/<grado>/book.json`. Lee los años como en el libro (1965 = nineteen sixty-five). |
| `build_docx.js` | Arma el Word del grado. |
| `build_site.py` | Arma `site/` con todos los grados que tengan `out/<grado>/book.json`, el selector de grado y un zip por grado. |
| `web/` | Mini-tests en línea (`tests.js`, `tests.css`). |

Direcciones de los QR: `/<grado>/<tema>/<pista>` (audio) y `/<grado>/test/<tema>/<destreza>` (mini-test).
**No cambies números de pista, nombres de destreza, carpetas de grado ni `SITE`.**

## Cómo regenerar un grado

```bash
pip install kokoro-onnx soundfile numpy "qrcode[pil]"   # y ffmpeg + node con el paquete docx
# modelo en tts-model/ (kokoro-v1.0.int8.onnx como kokoro.onnx, y voices-v1.0.bin como voices.bin)
mkdir -p audio && cp -r ../6/audio audio/6     # reutiliza los audios publicados
GRADE=6 python3 build_assets.py                # audios que falten + QR + book.json (NO_AUDIO=1 para saltar audios)
GRADE=6 node build_docx.js                     # out/6/English_Support_6_III_Trimestre.docx
python3 build_site.py && cp -r site/. ../       # publica
```
