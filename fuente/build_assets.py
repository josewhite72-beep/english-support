# -*- coding: utf-8 -*-
"""Exporta el contenido a JSON, genera los MP3 (normal y lento) y los QR estáticos."""
import json, os, subprocess, sys, importlib
import numpy as np, soundfile as sf, qrcode

ROOT = os.path.dirname(os.path.abspath(__file__))
GRADE = os.environ.get("GRADE") or (sys.argv[1] if len(sys.argv) > 1 else "6")
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, "grades", GRADE))
front = importlib.import_module("front")
MODULES = [importlib.import_module(m) for m in front.MODULES]
SITE = __import__("common").SITE
SPEAKERS = {}
TTS_DIR = os.environ.get("TTS_DIR", os.path.join(ROOT, "tts-model"))
NAMES_EXTRA = getattr(front, "NAMES", {})

def make_qr(theme_id, n, prefix=""):
    path = os.path.join(ROOT, "qr", GRADE, f"{prefix}{theme_id}-{n}.png")
    url = f"https://{SITE}/{GRADE}/test/{theme_id}/{n}" if prefix else f"https://{SITE}/{GRADE}/{theme_id}/{n}"
    img = qrcode.make(url, box_size=10, border=2,
                      error_correction=qrcode.constants.ERROR_CORRECT_M)
    img.save(path)
    return path

# Pronunciación de nombres en español (IPA aproximado, como lo diría un hablante en Panamá)
NAMES = {
    "Martínez": "mɑːɹtˈiːnɛs", "David": "dɑːvˈiːd", "Sofía": "soʊfˈiːə", "Ríos": "ɹˈiːoʊs",
    "Penonomé": "pˌɛnoʊnoʊmˈeɪ", "Chiriquí": "tʃˌiːɹiːkˈiː", "Coclé": "koʊklˈeɪ", "Veraguas": "vɛɹˈɑːɡwɑːs",
    "Colón": "koʊlˈoʊn", "Lucía": "luːsˈiːə", "Darién": "dɑːɹjˈɛn", "Mateo": "mɑːtˈeɪoʊ", "Pérez": "pˈɛɹɛs",
    "Bocas": "bˈoʊkɑːs", "Castillo": "kɑːstˈiːjoʊ", "Tablas": "tˈɑːblɑːs", "Antón": "ɑːntˈoʊn", "Tomás": "toʊmˈɑːs", "Chitré": "tʃiːtɹˈeɪ", "Cañas": "kˈɑːnjɑːs", "Gamboa": "ɡɑːmbˈoʊɑː", "Javier": "hɑːvjˈɛɹ", "Elena": "ɛlˈeɪnɑː", "Luis": "luːˈiːs", "San San": "sˈɑːn sˈɑːn", "Sofía Ríos": "soʊfˈiːə ɹˈiːoʊs", "Valle de Antón": "vˈɑːjeɪ deɪ ɑːntˈoʊn", "Las Tablas": "lɑːs tˈɑːblɑːs", "Isla Cañas": "ˈiːslɑː kˈɑːnjɑːs", "Los Santos": "loʊs sˈɑːntoʊs", "Chorrera": "tʃoʊɹˈɛɹɑː", "Emberá": "ɛmbɛɹˈɑː", "Aguadulce": "ˌɑːɡwɑːdˈuːlseɪ",
}
_NAME_PH = {}
_ONES = "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split()
_TENS = "_ _ twenty thirty forty fifty sixty seventy eighty ninety".split()
def _two(n):
    if n < 20: return _ONES[n]
    return _TENS[n // 10] + ("" if n % 10 == 0 else "-" + _ONES[n % 10])
def _year(m):  # como en el libro: 1965 = nineteen sixty-five · 2010 = twenty ten · 2005 = two thousand five
    y = int(m.group(0)); hi, lo = divmod(y, 100)
    if 2000 <= y < 2010: return "two thousand" + ("" if lo == 0 else " " + _ONES[lo])
    return _two(hi) + " " + ("hundred" if lo == 0 else ("oh " + _ONES[lo] if lo < 10 else _two(lo)))
import re as _re
def speak(kokoro, text, voice, speed):
    NAMES.update(NAMES_EXTRA)
    text = _re.sub(r"\b(1[89]|20)\d\d\b", _year, text)
    ph = kokoro.tokenizer.phonemize(text, "en-us")
    for name, ipa in sorted(NAMES.items(), key=lambda kv: -len(kv[0])):
        if name in text:
            orig = _NAME_PH.setdefault(name, kokoro.tokenizer.phonemize(name, "en-us"))
            ph = ph.replace(orig, ipa)
    return kokoro.create(ph, voice=voice, speed=speed, is_phonemes=True)

def gen_audio(kokoro, theme_id, track):
    out_dir = os.path.join(ROOT, "audio", GRADE, theme_id); os.makedirs(out_dir, exist_ok=True)
    for suffix, speed, pause_k in (("", 1.0, 1.0), ("-slow", 0.8, 1.3)):
        mp3 = os.path.join(out_dir, f"{track['n']}{suffix}.mp3")
        if os.path.exists(mp3) and not os.environ.get("FORCE"):
            continue
        parts, sr = [np.zeros(int(24000 * 0.4), dtype=np.float32)], 24000
        prev_voice = None
        for voice, text, pause in track["segments"]:
            a, sr = speak(kokoro, text, voice, speed)
            parts += [a.astype(np.float32), np.zeros(int(sr * pause * pause_k), dtype=np.float32)]
        wav = mp3[:-4] + ".wav"
        sf.write(wav, np.concatenate(parts), sr)
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", wav, "-ac", "1", "-b:a", "48k", mp3], check=True)
        os.remove(wav)

def transcript(track, speakers):
    lines, multi = [], len({v for v, _, _ in track["segments"]}) > 1
    for voice, text, _ in track["segments"]:
        who = speakers.get(voice)
        lines.append(f"**{who}:** {text}" if multi and who else text)
    return lines

def main():
    for d in ("qr", "out", "audio"):
        os.makedirs(os.path.join(ROOT, d, GRADE), exist_ok=True)
    kokoro = None
    if not os.environ.get("NO_AUDIO"):
        from kokoro_onnx import Kokoro
        kokoro = Kokoro(os.path.join(TTS_DIR, "kokoro.onnx"), os.path.join(TTS_DIR, "voices.bin"))
    book = {"site": SITE, "grade": GRADE, "grade_label": front.GRADE_LABEL, "trimester": front.TRIMESTER, "blocks": list(front.BLOCKS), "tracks": {}, "tests": {}}
    titles = {v: k for k, v in __import__("common").SKILL_TITLES.items()}
    for th in MODULES:
        spk = getattr(th, "SPEAKERS", SPEAKERS)
        for tr in getattr(th, "TRACKS", []):
            key = f"{th.THEME_ID}/{tr['n']}"
            make_qr(th.THEME_ID, tr["n"])
            if kokoro: gen_audio(kokoro, th.THEME_ID, tr)
            book["tracks"][key] = {"title": tr["title"], "instr": tr["instr"], "theme": th.THEME_ID,
                                   "theme_title": th.THEME_TITLE, "scenario": th.SCENARIO,
                                   "transcript": transcript(tr, spk)}
        if getattr(th, "TESTS", None):
            book["tests"][th.THEME_ID] = {"title": th.THEME_TITLE, "scenario": th.SCENARIO, "tests": th.TESTS}
        skill = None
        for b in th.BLOCKS:
            if b.get("t") == "h2" and b.get("text") in titles:
                skill = titles[b["text"]]
            if b.get("t") == "score" and skill and getattr(th, "TESTS", None):
                book["blocks"].append(b)
                make_qr(th.THEME_ID, skill, prefix="test-")
                b = {"t": "online", "id": f"{th.THEME_ID}/{skill}"}
                skill = None
            if b.get("t") == "transcripts":
                b = {"t": "transcripts", "items": [
                    {"label": f"Audio {th.THEME_ID.replace('-', '.')}-{tr['n']} · {tr['title']}",
                     "lines": transcript(tr, spk)} for tr in th.TRACKS]}
            if (b.get("t") == "theme_cover" or b.get("text") == "Gramática de consulta rápida") and book["blocks"] and book["blocks"][-1].get("t") != "pb":
                book["blocks"].append({"t": "pb"})
            book["blocks"].append(b)
    with open(os.path.join(ROOT, "out", GRADE, "book.json"), "w", encoding="utf-8") as f:
        json.dump(book, f, ensure_ascii=False, indent=1)
    print("ok", len(book["blocks"]), "blocks,", len(book["tracks"]), "tracks")

main()
