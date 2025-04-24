import os
import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Basis-URL deiner Website
BASE_URL = "https://aios-geisenheim.de"

# Ziel-Verzeichnisse anlegen
os.makedirs("assets/images", exist_ok=True)
os.makedirs("assets/css", exist_ok=True)

# HTML abrufen
resp = requests.get(BASE_URL, timeout=10)
resp.raise_for_status()
html = resp.text

# HTML parsen
soup = BeautifulSoup(html, "html.parser")

# 1) Texte extrahieren
texts = []
for tag in soup.find_all(["h1", "h2", "h3", "p", "li"]):
    txt = tag.get_text(strip=True)
    if txt:
        texts.append(txt)
with open("assets/texts.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(texts))
print(f"Gespeicherte Texte: {len(texts)} Zeilen in assets/texts.txt")

# 2) Bilder herunterladen
for img in soup.find_all("img"):
    src = img.get("src")
    if not src:
        continue
    img_url = urljoin(BASE_URL, src)
    filename = os.path.basename(src.split("?")[0])
    out_path = os.path.join("assets/images", filename)
    try:
        r = requests.get(img_url, timeout=10)
        r.raise_for_status()
        with open(out_path, "wb") as f:
            f.write(r.content)
        print(f"Heruntergeladen: {filename}")
    except Exception as e:
        print(f"Fehler bei {img_url}: {e}")

# 3) CSS-Dateien suchen und Farbwerte extrahieren
colors = set()
for link in soup.find_all("link", rel="stylesheet"):
    href = link.get("href")
    css_url = urljoin(BASE_URL, href)
    try:
        r = requests.get(css_url, timeout=10)
        r.raise_for_status()
        css_text = r.text
        # CSS-Datei speichern
        name = os.path.basename(href.split("?")[0])
        with open(f"assets/css/{name}", "w", encoding="utf-8") as f:
            f.write(css_text)
        # Regex für hex- und rgb()-Farben
        for match in re.findall(r"(#(?:[0-9a-fA-F]{3}){1,2}|rgb\([^)]+\))", css_text):
            colors.add(match)
    except Exception as e:
        print(f"Fehler bei CSS {css_url}: {e}")

with open("assets/colors.txt", "w", encoding="utf-8") as f:
    for c in sorted(colors):
        f.write(c + "\n")
print(f"Gefundene Farben: {len(colors)} in assets/colors.txt")
