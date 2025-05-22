"""
Spotify API Client Funktionalitäten
"""
# Standardbibliotheken
import random
import time

# Drittanbieter-Bibliotheken
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Eigene Module
from app import SPOTIFY_CONFIG, current_track_data
from app.utils import get_dominant_color
from app.gui_console import gui_console

def create_spotify_oauth():
    return SpotifyOAuth(
        client_id=SPOTIFY_CONFIG['CLIENT_ID'],
        client_secret=SPOTIFY_CONFIG['CLIENT_SECRET'],
        redirect_uri=SPOTIFY_CONFIG['REDIRECT_URI'],
        scope=SPOTIFY_CONFIG['SCOPE'],
        cache_path=SPOTIFY_CONFIG['CACHE_PATH']
    )

def get_spotify_client():
    sp_oauth = create_spotify_oauth()
    token_info = sp_oauth.get_cached_token()
    
    if not token_info:
        gui_console.write("Keine Token-Informationen vorhanden. Bitte Authentifizierung durchführen.", "error")
        gui_console.write("Gehe auf http://127.0.0.1:5000/auth und verifiziere dich", "error")
        gui_console.spotify_status.config(text="○ Waiting for Auth", fg=gui_console.warning_color)
        return None

    if sp_oauth.is_token_expired(token_info):
        try:
            token_info = sp_oauth.refresh_access_token(token_info['refresh_token'])
        except Exception as e:
            gui_console.spotify_status.config(text="○ Error", fg=gui_console.error_color)
            gui_console.write(f"Fehler beim Aktualisieren des Tokens: {e}", "error")
            return None
    gui_console.spotify_status.config(text="○ Authed", fg=gui_console.success_color)
    return spotipy.Spotify(auth=token_info['access_token'])

def get_current_track(sp):
    if sp is None:
        return {
            'track': '',
            'artist': '',
            'album': '',
            'album_cover': '',
            'is_playing': False,
            'cover_color': (29, 185, 84),
            'preview_url': None,
            'duration_ms': 0
        }

    try:
        current_track = sp.current_playback()

        if current_track and current_track.get('is_playing', False) and current_track.get('item'):
            item = current_track['item']
            track_name = item['name']
            artist_name = item['artists'][0]['name']
            album_name = item['album']['name']
            album_cover = item['album']['images'][0]['url'] if item['album']['images'] else ''
            preview_url = item.get('preview_url')
            duration_ms = item.get('duration_ms', 0)

            cover_color = get_dominant_color(album_cover) if album_cover else (29, 185, 84)

            return {
                'track': track_name,
                'artist': artist_name,
                'album': album_name,
                'album_cover': album_cover,
                'is_playing': True,
                'cover_color': cover_color,
                'preview_url': preview_url,
                'duration_ms': duration_ms
            }

        else:
            try:
                recent_tracks = sp.current_user_recently_played(limit=1)
                if recent_tracks and recent_tracks.get('items'):
                    recent = recent_tracks['items'][0]['track']
                    track_name = recent['name']
                    artist_name = recent['artists'][0]['name']
                    album_name = recent['album']['name']
                    album_cover = recent['album']['images'][0]['url'] if recent['album']['images'] else ''
                    preview_url = recent.get('preview_url')
                    duration_ms = recent.get('duration_ms', 0)

                    cover_color = get_dominant_color(album_cover) if album_cover else (29, 185, 84)

                    return {
                        'track': track_name,
                        'artist': artist_name,
                        'album': album_name,
                        'album_cover': album_cover,
                        'is_playing': False,
                        'cover_color': cover_color,
                        'preview_url': preview_url,
                        'duration_ms': duration_ms
                    }
            except Exception as e:
                gui_console.write(f"Fehler beim Abrufen des zuletzt gespielten Tracks: {e}", "error")

        return {
            'track': '',
            'artist': '',
            'album': '',
            'album_cover': '',
            'is_playing': False,
            'cover_color': (29, 185, 84),
            'preview_url': None,
            'duration_ms': 0
        }

    except Exception as e:
        gui_console.write(f"Fehler beim Abrufen der Track-Informationen: {e}", "error")
        return {
            'track': '',
            'artist': '',
            'album': '',
            'album_cover': '',
            'is_playing': False,
            'cover_color': (29, 185, 84),
            'preview_url': None,
            'duration_ms': 0
        }

def update_track_info():
    global current_track_data
    gui_console.write("Spotify Track Monitor wird gestartet...", "success")
    gui_console.write("Starte Webserver auf http://127.0.0.1:5000/", "italic")
    last_track = None

    while True:
        try:
            sp = get_spotify_client()
            if sp:
                track_info = get_current_track(sp)
                track_id = f"{track_info['track']} - {track_info['artist']}"
                if track_info['is_playing'] and track_id != last_track:
                    gui_console.track_info.config(text=track_id)
                    last_track = track_id
                current_track_data.update(track_info)
            else:
                if random.random() < 0.05:
                    gui_console.track_info.config(text="")
                    gui_console.write("Keine Spotify-Verbindung. Bitte App öffnen und authentifizieren.", "error")
        except Exception as e:
            gui_console.write(f"Fehler bei Update: {e}", "error")
        time.sleep(3)
