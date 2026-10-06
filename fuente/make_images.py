# -*- coding: utf-8 -*-
"""Biblioteca de ilustraciones (K–2): fuente/img/<nombre>.png, 300×300, línea negra, fondo transparente.
Orígenes: (1) dibujos de los módulos GeMA (Word) · (2) OpenMoji, versión en línea negra
(CC BY-SA 4.0, https://openmoji.org) · (3) SVG propios en fuente/img/*.svg.
Uso: python3 make_images.py [carpeta_imagenes_modulos] [carpeta_openmoji_black_svg]"""
import os, sys, io
from PIL import Image
import cairosvg

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "img")
MODS = sys.argv[1] if len(sys.argv) > 1 else "/home/claude/support-src/img"
OM = sys.argv[2] if len(sys.argv) > 2 else "/home/claude/support-src/openmoji/package/black/svg"
S = 300

# nombre: (carpeta del módulo, prefijo del archivo)
MODULE = {
    "park": ("2_5-1_Its_the_Park", "190d9f32"), "playground": ("2_5-1_Its_the_Park", "6b5ccf52"),
    "school": ("2_5-1_Its_the_Park", "a0822008"), "church": ("2_5-1_Its_the_Park", "cc95b275"),
    "home": ("2_5-1_Its_the_Park", "4466d8b2"), "library": ("2_5-1_Its_the_Park", "69f55e43"),
    "market": ("2_5-2_Its_the_Market", "96a6f7a9"), "store": ("2_5-2_Its_the_Market", "9cdef67b"),
    "office": ("2_5-2_Its_the_Market", "607c5e33"), "gym": ("2_5-2_Its_the_Market", "bc596668"),
    # 1.º grado (vehículos y colores)
    "car": ("1_5-1_Thats_a_Blue_Bus", "c887bc44"), "bus": ("1_5-1_Thats_a_Blue_Bus", "87c4b7d2"),
    "taxi": ("1_5-1_Thats_a_Blue_Bus", "7545d73f"), "truck": ("1_5-1_Thats_a_Blue_Bus", "13a374bd"),
    "train": ("1_5-1_Thats_a_Blue_Bus", "c93785b3"), "bike": ("1_5-1_Thats_a_Blue_Bus", "a4b27eae"),
    "red": ("1_5-2_Thats_a_Red_Bike", "c47ece1a"), "blue": ("1_5-2_Thats_a_Red_Bike", "4471af74"),
    "green": ("1_5-2_Thats_a_Red_Bike", "83c9c2b2"), "yellow": ("1_5-2_Thats_a_Red_Bike", "4409c659"),
    "orange": ("1_5-2_Thats_a_Red_Bike", "c583c020"),
    # K (animales de la granja)
    "dog": ("K_5-1_The_Cat_Says_Meow", "5d0fdd1e"), "cat": ("K_5-1_The_Cat_Says_Meow", "f8a5e7a2"),
    "duck": ("K_5-1_The_Cat_Says_Meow", "985e23d9"), "pig": ("K_5-1_The_Cat_Says_Meow", "ec54246d"),
    "cow": ("K_5-1_The_Cat_Says_Meow", "f456ccf5"), "bird": ("K_5-1_The_Cat_Says_Meow", "7855422d"),
    "farm": ("K_5-2_Thats_a_Rooster", "5fff6e57"), "hen": ("K_5-2_Thats_a_Rooster", "bf759af0"),
    "rooster": ("K_5-2_Thats_a_Rooster", "d7c2b890"),
    "face-happy": ("2_5-1_Its_the_Park", "5231750a"), "face-ok": ("2_5-1_Its_the_Park", "78420360"),
    "face-sad": ("2_5-1_Its_the_Park", "e86a6669"),
    "i-listen": ("2_5-1_Its_the_Park", "e53b03ed"), "i-speak": ("2_5-1_Its_the_Park", "bd743a1d"),
    "i-read": ("2_5-1_Its_the_Park", "c8952070"), "i-write": ("2_5-1_Its_the_Park", "88dc9d4f"),
}
# nombre: código OpenMoji (o varios, que se dibujan juntos)
OPENMOJI = {
    "sloth": "1F9A5", "monkey": "1F412", "parrot": "1F99C", "frog": "1F438", "snake": "1F40D",
    "jaguar": "1F406", "leaf": "1F343", "tree": "1F333", "palm": "1F334", "butterfly": "1F98B",
    "fish": "1F41F",
    "step": "1F463", "dance": "1F483", "foot": "1F9B6", "hop": "1F407", "one": "261D", "two": "270C", "clap": "1F44F",
}

def fit(img):
    """Recorta al contenido y centra en un cuadro de 300 con margen."""
    img = img.convert("RGBA")
    bbox = img.split()[3].getbbox()
    if bbox: img = img.crop(bbox)
    img.thumbnail((S - 24, S - 24), Image.LANCZOS)
    out = Image.new("RGBA", (S, S), (255, 255, 255, 0))
    out.paste(img, ((S - img.width) // 2, (S - img.height) // 2), img)
    return out

def svg(path, w=600, stroke="2.6"):
    """OpenMoji usa trazo 2; lo engrosamos un poco para igualar los dibujos de los módulos."""
    src = open(path, encoding="utf-8").read().replace('stroke-width="2"', f'stroke-width="{stroke}"')
    return Image.open(io.BytesIO(cairosvg.svg2png(bytestring=src.encode(), output_width=w, output_height=w)))

def main():
    os.makedirs(OUT, exist_ok=True)
    for name, (mod, pre) in MODULE.items():
        d = os.path.join(MODS, mod)
        f = next(x for x in os.listdir(d) if x.startswith(pre))
        fit(Image.open(os.path.join(d, f))).save(os.path.join(OUT, name + ".png"))
    for name, code in OPENMOJI.items():
        if isinstance(code, list):
            parts = [svg(os.path.join(OM, c + ".svg")) for c in code]
            parts = [p.crop(p.split()[3].getbbox()) for p in parts]
            h = max(p.height for p in parts); w = sum(p.width for p in parts)
            row = Image.new("RGBA", (w, h), (255, 255, 255, 0)); x = 0
            for p in parts: row.paste(p, (x, h - p.height), p); x += int(p.width * 0.6)
            row = row.crop(row.split()[3].getbbox())
            fit(row).save(os.path.join(OUT, name + ".png"))
        else:
            fit(svg(os.path.join(OM, code + ".svg"))).save(os.path.join(OUT, name + ".png"))
    for f in os.listdir(OUT):
        if f.endswith(".svg"):
            fit(svg(os.path.join(OUT, f))).save(os.path.join(OUT, f[:-4] + ".png"))
    print(len([f for f in os.listdir(OUT) if f.endswith(".png")]), "imágenes en", OUT)

if __name__ == "__main__":
    main()
