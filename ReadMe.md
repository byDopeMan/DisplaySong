# 🎵 DisplaySong – Spotify Now Playing Display

**DisplaySong.exe** shows the currently playing song from your Spotify account on a local web page – perfect for OBS, live streams, or your own visual overlay.

---

## 📦 Included Files

- `DisplaySong.exe` – the main program  
- `.env` – for your Spotify credentials  
- `custom.txt` – optional: custom design template  
- `background.txt` – optional: background design

---

## 🔧 Requirements

- Spotify Premium  # I don't really know it
- Internet connection  
- Spotify must be open and actively playing music

---

## 🚀 Setup

### 1. Enter your Spotify credentials

1. Open the `.env` file with a text editor  
2. Add your credentials like this:
    CLIENT_ID=your_spotify_client_id
    CLIENT_SECRET=your_spotify_client_secret
    REDIRECT_URI=http://127.0.0.1:5000/callback
    FLASK_SECRET_KEY=TnV0dGVuc29obg== # can stay as is


### 2. Create a Spotify App

1. Go to: https://developer.spotify.com/dashboard  
2. Create a new app  
3. Add the following Redirect URI: http://127.0.0.1:5000/callback  


4. Copy `Client ID` and `Client Secret` into your `.env`

---

## ▶️ How to Use

1. Double-click `DisplaySong.exe`  
2. Open your browser: (http://127.0.0.1:5000)  
3. On first use, you'll be redirected to Spotify for authorization  
4. The currently playing song will be displayed

---

## 🌈 Display Modes

- `/` → Default view  
- `/design2` → Alternate view  
- `/custom` → Your design from `custom.txt`  
- `/bg` → Background only from `background.txt`  
- `/select` → Design overview

You can customize `custom.txt` and `background.txt` using HTML and placeholders (see below).

---

## ✏️ Custom Design Placeholders

Use these placeholders in your `custom.txt` or `background.txt`:

| Placeholder         | Description                      |
|---------------------|----------------------------------|
| `{{ track }}`        | Song title                      |
| `{{ artist }}`       | Artist name                     |
| `{{ album }}`        | Album name                      |
| `{{ album_cover }}`  | Album cover image URL           |
| `{{ preview_url }}`  | 30s audio preview (if available)|
| `{{ duration_ms }}`  | Track duration in ms            |
| `{{ color_r }}`      | Dominant cover color (Red)      |
| `{{ color_g }}`      | Dominant cover color (Green)    |
| `{{ color_b }}`      | Dominant cover color (Blue)     |

---

## 🎥 Using in OBS

1. Run `DisplaySong.exe`  
2. Choose a design (e.g. `http://127.0.0.1:5000/custom`)  
3. In OBS:
   - Add new source → “Browser”
   - URL: `http://127.0.0.1:5000/custom`
   - Set width/height (e.g. 800x200)

   Available URLs:
   - `http://127.0.0.1:5000/`
   - `http://127.0.0.1:5000/design2`
   - `http://127.0.0.1:5000/custom`
   - `http://127.0.0.1:5000/bg`

---

## ❗ Troubleshooting

| Issue                            | Solution                                                  |
|----------------------------------|-----------------------------------------------------------|
| No music displayed               | Spotify must be running and actively playing              |
| Login page appears               | App not authorized yet → log in once                      |
| Preview not working              | Not all tracks provide a `preview_url`                    |
| Colors look odd                  | Dominant cover color is auto-extracted (RGB values usable)|

---

© All rights reserved. Distribution or publishing without permission is prohibited.

---


# 🎵 DisplaySong – Spotify Now Playing Anzeige

**DisplaySong.exe** zeigt den aktuell gespielten Song deines Spotify-Kontos auf einer lokalen Webseite an – ideal für OBS, Streams oder dein eigenes Display-Overlay.

---

## 📦 Enthaltene Dateien

- `DisplaySong.exe` – das Programm
- `.env` – für deine Spotify-Zugangsdaten
- `custom.txt` – optional: eigenes Design-Template
- `background.txt` – optional: eigener Hintergrund

---

## 🔧 Voraussetzungen

- Spotify Premium # Weiß ich nicht wirklich
- Internetverbindung
- Spotify-App muss geöffnet sein und Musik abspielen

---

## 🚀 Einrichtung

### 1. Spotify-Zugangsdaten eintragen

1. Öffne die Datei `.env` mit einem Texteditor.
2. Trage deine Zugangsdaten ein:
    CLIENT_ID=deine_spotify_client_id
    CLIENT_SECRET=dein_spotify_client_secret
    REDIRECT_URI=http://127.0.0.1:5000/callback
    FLASK_SECRET_KEY=TnV0dGVuc29obg== # kann so bleiben


### 2. Spotify-App erstellen

Wenn du noch keine Spotify-App hast:

1. Besuche: https://developer.spotify.com/dashboard
2. Erstelle eine neue App
3. Füge bei **Redirect URI** folgendes hinzu:http://127.0.0.1:5000/callback


4. Kopiere `Client ID` und `Client Secret` in deine `.env`

---

## ▶️ Verwendung

1. Doppelklicke auf `DisplaySong.exe`
2. Öffne im Browser: (http://127.0.0.1:5000)
3. Beim ersten Start wirst du zur Spotify-Anmeldung weitergeleitet
4. Danach wird automatisch der aktuell gespielte Titel angezeigt

---

## 🌈 Anzeige-Designs

- `/` → Standardansicht  
- `/design2` → Alternative Ansicht  
- `/custom` → Eigene Ansicht aus `custom.txt`  
- `/bg` → Nur Hintergrund aus `background.txt`  
- `/select` → Übersicht der Designs  

Du kannst `custom.txt` und `background.txt` selbst gestalten (HTML mit Platzhaltern, siehe unten).

---

## ✏️ Platzhalter für eigenes Design

In `custom.txt` und `background.txt` kannst du folgende Platzhalter nutzen:

| Platzhalter          | Beschreibung                   |
|----------------------|--------------------------------|
| `{{ track }}`        | Songtitel                      |
| `{{ artist }}`       | Künstlername                   |
| `{{ album }}`        | Albumname                      |
| `{{ album_cover }}`  | URL des Albumcovers            |
| `{{ preview_url }}`  | 30s-Vorschau (wenn verfügbar)  |
| `{{ duration_ms }}`  | Liedlänge in Millisekunden     |
| `{{ color_r }}`      | Coverfarbe – Rotwert           |
| `{{ color_g }}`      | Coverfarbe – Grünwert          |
| `{{ color_b }}`      | Coverfarbe – Blauwert          |

---

## 🎥 In OBS einbinden

1. Starte `DisplaySong.exe`
2. Wähle z. B. das Design unter `http://127.0.0.1:5000/custom`
3. In OBS:
   - Neue Quelle → „Browser“
   - URL: `http://127.0.0.1:5000/custom`
   - Breite/Höhe anpassen (z. B. 800x200)

   Nutzbare URLS:
        - `http://127.0.0.1:5000/`
        - `http://127.0.0.1:5000/design2`
        - `http://127.0.0.1:5000/custom`
        - `http://127.0.0.1:5000/bg`

---

## ❗ Tipps & Fehlerbehebung

| Problem                             | Lösung                                                   |
|------------------------------------|----------------------------------------------------------|
| Keine Musik wird angezeigt         | Spotify muss geöffnet sein und aktiv Musik abspielen     |
| Es erscheint eine Anmeldeseite     | App-Zugang wurde noch nicht autorisiert → Einloggen      |
| Vorschau funktioniert nicht        | Nicht alle Tracks haben eine `preview_url`               |
| Farben wirken komisch              | Coverfarbe wird automatisch erkannt (RGB-Werte nutzbar) |

---

© Alle Rechte vorbehalten. Die Weitergabe oder Veröffentlichung ohne Erlaubnis ist nicht gestattet.
