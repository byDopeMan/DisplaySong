"""
Flask-Routen für die Spotify Now Playing App
"""
# Drittanbieter-Bibliotheken
from flask import (
    jsonify,
    redirect,
    render_template_string,
    request,
    session,
)

# Eigene Module
from app import SPOTIFY_CONFIG, current_track_data
from app.html import Sites
from app.spotify_client import create_spotify_oauth
from app.utils import get_external_path


def register_routes(app):
    @app.route('/')
    def index():
        sp_oauth = create_spotify_oauth()
        token_info = sp_oauth.get_cached_token()
        color_r, color_g, color_b = current_track_data['cover_color']

        if not token_info:
            return redirect('/auth')
        session['authed'] = True

        return render_template_string(
            Sites.NOW_PLAYING,
            track=current_track_data['track'],
            artist=current_track_data['artist'],
            album=current_track_data['album'],
            album_cover=current_track_data['album_cover'],
            is_playing=current_track_data['is_playing'],
            color_r=color_r,
            color_g=color_g,
            color_b=color_b,
            preview_url=current_track_data.get('preview_url'),
            duration_ms=current_track_data.get('duration_ms')
        )
    
    @app.route('/select')
    def select_design():
        if not session.get('authed'):
            return redirect('/auth')
        return render_template_string(Sites.SELECTION_HTML)
    
    @app.route('/design2')
    def select_design2():
        sp_oauth = create_spotify_oauth()
        token_info = sp_oauth.get_cached_token()
        color_r, color_g, color_b = current_track_data['cover_color']

        if not token_info:
            return redirect('/auth')
        session['authed'] = True

        return render_template_string(
            Sites.NOW_PLAYING2,
            track=current_track_data['track'],
            artist=current_track_data['artist'],
            album=current_track_data['album'],
            album_cover=current_track_data['album_cover'],
            is_playing=current_track_data['is_playing'],
            color_r=color_r,
            color_g=color_g,
            color_b=color_b,
            preview_url=current_track_data.get('preview_url'),
            duration_ms=current_track_data.get('duration_ms')
        )
    
    @app.route('/auth')
    def auth():
        if SPOTIFY_CONFIG['CLIENT_ID'] is None:
            return render_template_string(
                Sites.AUTH_HTML,
                redirect_uri=SPOTIFY_CONFIG['REDIRECT_URI'],
                auth_url=None
            )
        
        sp_oauth = create_spotify_oauth()
        auth_url = sp_oauth.get_authorize_url()
        session['authed'] = True
        return render_template_string(
            Sites.AUTH_HTML,
            redirect_uri=sp_oauth.redirect_uri,
            auth_url=auth_url
        )
    
    @app.route('/custom')
    def select_custom():
        sp_oauth = create_spotify_oauth()
        token_info = sp_oauth.get_cached_token()
        color_r, color_g, color_b = current_track_data['cover_color']
        path = get_external_path("custom.txt")
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()

        if not token_info:
            return redirect('/auth')
        session['authed'] = True

        return render_template_string(
            content,
            track=current_track_data['track'],
            artist=current_track_data['artist'],
            album=current_track_data['album'],
            album_cover=current_track_data['album_cover'],
            is_playing=current_track_data['is_playing'],
            color_r=color_r,
            color_g=color_g,
            color_b=color_b,
            preview_url=current_track_data.get('preview_url'),
            duration_ms=current_track_data.get('duration_ms')
        )
    
    @app.route('/callback')
    def callback():
        sp_oauth = create_spotify_oauth()
        code = request.args.get('code')
        error = request.args.get('error')

        if error:
            return f"Fehler bei der Spotify-Anmeldung: {error}", 400
        
        try:
            token_info = sp_oauth.get_access_token(code)
        except Exception as e:
            return f"Token konnte nicht empfangen werden: {str(e)}", 400
        
        return redirect('/select')



    @app.route('/bg')
    def background():
        path = get_external_path("background.txt")
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        return render_template_string(content)

    @app.route('/api/current-track')
    def api_current_track():
        color_r, color_g, color_b = current_track_data['cover_color']
        return jsonify({
            'track': current_track_data['track'],
            'artist': current_track_data['artist'],
            'album': current_track_data['album'],
            'album_cover': current_track_data['album_cover'],
            'is_playing': current_track_data['is_playing'],
            'color_r': color_r,
            'color_g': color_g,
            'color_b': color_b,
            'preview_url': current_track_data.get('preview_url'),
            'duration_ms': current_track_data.get('duration_ms')
        })