"""
App-Initialisierung und Konfiguration
"""
# Standardbibliotheken
import os
import sys

# Drittanbieter-Bibliotheken
from dotenv import load_dotenv
from flask import Flask

# Eigene Module
from app.utils import get_external_path



env_path = get_external_path(".env")
load_dotenv(dotenv_path=env_path)

# Globale Variable für aktuelle Track-Informationen
current_track_data = {
    'track': '',
    'artist': '',
    'album': '',
    'album_cover': '',
    'is_playing': False,
    'cover_color': (29, 185, 84),
    'preview_url': None,
    'duration_ms': 0
}

# Spotify API Konfiguration
SPOTIFY_CONFIG = {
    'CLIENT_ID': os.getenv("CLIENT_ID"),
    'CLIENT_SECRET': os.getenv("CLIENT_SECRET"),
    'REDIRECT_URI': os.getenv('REDIRECT_URI'),  # Muss in Spotify Dashboard eingetragen sein
    'SCOPE': 'user-read-currently-playing user-read-playback-state user-read-recently-played',
    'CACHE_PATH': '.spotify_cache'
}

def get_script_type():
    if getattr(sys, 'frozen', False):
        return ".exe"
    else:
        return ".py"

def create_app():
    """Flask-App erstellen und konfigurieren"""
    app = Flask(__name__)
    
    # Wichtig für Sessions (Sitzungsdaten)
    app.secret_key = os.getenv('FLASK_SECRET_KEY')

    # Importiere Routen
    from app.routes import register_routes
    register_routes(app)
    
    return app