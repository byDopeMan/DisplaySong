"""
Hilfsfunktionen für die Spotify Now Playing App
"""
# Standardbibliotheken
import os
import sys
from io import BytesIO

# Drittanbieter-Bibliotheken
import requests
from PIL import Image
from app.gui_console import gui_console


def get_external_path(filename):
    """Pfad zur Datei neben der .exe (auch im Dev-Modus sinnvoll)"""
    if getattr(sys, 'frozen', False):
        base_path = os.path.dirname(sys.executable)
    else:
        base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    return os.path.join(base_path, filename)

def get_absolute_path(relative_path):
    """Ermöglicht Zugriff auf Dateien sowohl im Build als auch im Dev-Modus"""
    if getattr(sys, 'frozen', False):
        # PyInstaller-Modus
        base_path = os.path.dirname(sys.executable)
        # base_path = sys._MEIPASS if hasattr(sys, '_MEIPASS') else os.path.dirname(sys.executable)
    else:
        base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    return os.path.join(base_path, relative_path)

def get_dominant_color(img_url):
    """Extrahiert die dominante Farbe aus einem Bild-URL"""
    try:
        response = requests.get(img_url)
        img = Image.open(BytesIO(response.content))
        
        # Bild verkleinern für schnellere Verarbeitung
        img = img.resize((50, 50))
        
        # Extrahiere die häufigsten Farben
        colors = img.getcolors(2500)  # maxcolors = 50*50
        
        if not colors:
            return (29, 185, 84)  # Standard Spotify-Grün falls keine Farben
        
        # Sortiere nach Häufigkeit und nimm die häufigste Farbe
        colors.sort(reverse=True, key=lambda x: x[0])
        
        # Prüfe, ob die dominante Farbe zu dunkel oder zu hell ist
        dominant_color = colors[0][1]
        
        # Bei RGB-Bild
        if len(dominant_color) >= 3:
            r, g, b = dominant_color[:3]
            
            # Berechne Helligkeit
            brightness = (r * 299 + g * 587 + b * 114) / 1000
            
            # Wenn zu dunkel oder zu hell, verwende die nächste Farbe oder passe an
            if brightness < 50 or brightness > 200:
                # Wenn es weitere Farben gibt
                if len(colors) > 1:
                    for i in range(1, min(5, len(colors))):
                        next_color = colors[i][1]
                        if len(next_color) >= 3:
                            r, g, b = next_color[:3]
                            brightness = (r * 299 + g * 587 + b * 114) / 1000
                            if 50 <= brightness <= 200:
                                return (r, g, b)
                
                # Wenn keine passende gefunden wurde, passe die erste an
                r = max(30, min(230, r))
                g = max(30, min(230, g))
                b = max(30, min(230, b))
                
                # Stelle sicher, dass zumindest eine Komponente einen Mindestwert hat
                if max(r, g, b) < 100:
                    max_val = max(r, g, b)
                    factor = 100 / max_val if max_val > 0 else 1
                    r = min(255, int(r * factor))
                    g = min(255, int(g * factor))
                    b = min(255, int(b * factor))
                
                return (r, g, b)
            
            return (r, g, b)
        
        # Bei Graustufen-Bild
        return (dominant_color, dominant_color, dominant_color)
        
    except Exception as e:
        gui_console.write(f"Fehler bei der Farbextraktion: {e}", "error")
        return (29, 185, 84)  # Standard Spotify-Grün bei Fehler