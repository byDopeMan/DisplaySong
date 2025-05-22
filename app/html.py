class Sites:
    AUTH_HTML = """
    <!DOCTYPE html>
    <html lang="de">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Spotify Auth Setup</title>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&display=swap');
            
            :root {
                --spotify-green: #1DB954;
                --dark-bg: #121212;
                --card-bg: #181818;
                --text-primary: #FFFFFF;
                --text-secondary: #B3B3B3;
            }
            
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            
            body {
                font-family: 'Montserrat', sans-serif;
                background: var(--dark-bg);
                color: var(--text-primary);
                display: flex;
                align-items: center;
                justify-content: center;
                min-height: 100vh;
                padding: 20px;
                position: relative;
                overflow: hidden;
            }
            
            /* Animated wave background */
            .wave-bg {
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                z-index: -1;
                opacity: 0.4;
            }
            
            .wave-bg::before,
            .wave-bg::after {
                content: '';
                position: absolute;
                width: 300%;
                height: 300%;
                top: -100%;
                left: -100%;
                background: 
                    radial-gradient(circle at 30% 30%, var(--spotify-green) 0%, transparent 10%),
                    radial-gradient(circle at 70% 60%, var(--spotify-green) 0%, transparent 15%),
                    radial-gradient(circle at 40% 80%, var(--spotify-green) 0%, transparent 12%);
                animation: wavePulse 15s infinite linear;
                opacity: 0.15;
            }
            
            .wave-bg::after {
                animation-delay: -7s;
                opacity: 0.1;
                background-size: 120% 120%;
            }
            
            @keyframes wavePulse {
                0% { transform: rotate(0deg); }
                100% { transform: rotate(360deg); }
            }
            
            .setup-container {
                background-color: var(--card-bg);
                border-radius: 20px;
                max-width: 500px;
                width: 100%;
                box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5);
                animation: fadeIn 0.8s ease-out;
                overflow: hidden;
            }
            
            .header {
                padding: 28px 0;
                text-align: center;
                position: relative;
            }
            
            .header::after {
                content: '';
                position: absolute;
                bottom: 0;
                left: 15%;
                width: 70%;
                height: 2px;
                background: linear-gradient(90deg, transparent, var(--spotify-green), transparent);
            }
            
            .header h1 {
                font-size: 26px;
                font-weight: 700;
                color: var(--text-primary);
                margin-bottom: 8px;
            }
            
            .header .spotify-logo {
                font-size: 24px;
                color: var(--spotify-green);
                margin-bottom: 12px;
                display: inline-block;
            }
            
            .setup-content {
                padding: 32px;
            }
            
            .setup-steps {
                margin: 20px 0 30px;
                counter-reset: step-counter;
            }
            
            .step-item {
                position: relative;
                margin-bottom: 24px;
                padding-left: 42px;
                counter-increment: step-counter;
            }
            
            .step-item::before {
                content: counter(step-counter);
                position: absolute;
                left: 0;
                top: 0;
                background-color: var(--spotify-green);
                color: var(--dark-bg);
                width: 28px;
                height: 28px;
                border-radius: 50%;
                display: flex;
                align-items: center;
                justify-content: center;
                font-weight: 600;
                font-size: 14px;
            }
            
            .step-item h3 {
                margin-bottom: 8px;
                font-size: 16px;
                font-weight: 600;
            }
            
            .step-item p {
                color: var(--text-secondary);
                font-size: 14px;
                line-height: 1.6;
            }
            
            code {
                background-color: rgba(255, 255, 255, 0.1);
                padding: 4px 8px;
                border-radius: 4px;
                font-family: monospace;
                font-size: 13px;
                word-break: break-all;
            }
            
            .spotify-btn {
                display: block;
                margin: 25px auto 10px;
                padding: 16px 32px;
                background-color: var(--spotify-green);
                color: var(--dark-bg);
                text-align: center;
                font-weight: 600;
                border-radius: 30px;
                text-decoration: none;
                width: fit-content;
                transition: all 0.3s;
                font-size: 16px;
                box-shadow: 0 6px 20px rgba(29, 185, 84, 0.3);
                position: relative;
                overflow: hidden;
            }
            
            .spotify-btn::after {
                content: '';
                position: absolute;
                top: 0;
                left: -100%;
                width: 100%;
                height: 100%;
                background: rgba(255, 255, 255, 0.2);
                transition: left 0.5s;
            }
            
            .spotify-btn:hover {
                transform: translateY(-3px);
                box-shadow: 0 10px 25px rgba(29, 185, 84, 0.4);
            }
            
            .spotify-btn:hover::after {
                left: 100%;
            }
            
            @keyframes fadeIn {
                from { opacity: 0; transform: translateY(30px); }
                to { opacity: 1; transform: translateY(0); }
            }
            
            a {
                color: var(--spotify-green);
                text-decoration: none;
                transition: all 0.2s;
            }
            
            a:hover {
                text-decoration: underline;
                opacity: 0.9;
            }
            
            .note {
                margin-top: 24px;
                padding: 12px 18px;
                background-color: rgba(29, 185, 84, 0.1);
                border-left: 3px solid var(--spotify-green);
                border-radius: 6px;
                font-size: 13px;
                color: var(--text-secondary);
            }
            
            /* Responsive styles */
            @media (max-width: 580px) {
                .setup-content {
                    padding: 24px 20px;
                }
                
                .header h1 {
                    font-size: 22px;
                }
                
                .spotify-btn {
                    width: 100%;
                    padding: 14px;
                }
            }
        </style>
    </head>
    <body>
        <div class="wave-bg"></div>
        
        <div class="setup-container">
            <div class="header">
                <div class="spotify-logo">
                    <svg width="40" height="40" viewBox="0 0 24 24" fill="currentColor">
                        <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm4.65 14.35c-.18.28-.56.35-.85.18-2.35-1.45-5.3-1.78-8.78-.97-.33.08-.65-.13-.73-.45-.08-.33.13-.65.45-.73 3.8-.87 7.1-.5 9.74 1.13.29.17.36.56.17.84zm1.24-2.75c-.23.35-.7.47-1.05.24-2.7-1.65-6.8-2.13-9.98-1.17-.42.16-.86-.05-1.02-.46-.15-.42.05-.86.46-1.02 3.64-1.1 8.17-.57 11.27 1.35.35.23.47.7.24 1.05zm.11-2.85c-3.22-1.92-8.56-2.09-11.64-1.15-.5.15-1.02-.13-1.17-.62-.15-.5.13-1.02.62-1.17 3.53-1.07 9.4-.86 13.12 1.34.45.26.6.85.33 1.3-.24.46-.84.6-1.3.33z"/>
                    </svg>
                </div>
                <h1>Spotify Now Playing Setup</h1>
            </div>
            
            <div class="setup-content">
                <div class="setup-steps">
                    <div class="step-item">
                        <h3>Spotify Developer App erstellen</h3>
                        <p>Besuche das <a href="https://developer.spotify.com/dashboard" target="_blank">Spotify Developer Dashboard</a> und erstelle eine neue Anwendung.</p>
                    </div>
                    
                    <div class="step-item">
                        <h3>Redirect URI eintragen</h3>
                        <p>Füge folgende Redirect URI in den Einstellungen deiner App hinzu:</p>
                        <code>{{ redirect_uri }}</code>
                    </div>
                    
                    <div class="step-item">
                        <h3>Client-Daten kopieren</h3>
                        <p>Kopiere deine <strong>Client ID</strong> und <strong>Client Secret</strong> von deiner erstellten App.</p>
                    </div>
                    
                    <div class="step-item">
                        <h3>Verbindung herstellen</h3>
                        <p>Klicke auf den Button unten, um dein Konto mit der Anwendung zu verbinden.</p>
                    </div>
                </div>
                
                <a href="{{ auth_url }}" class="spotify-btn">Mit Spotify verbinden</a>
                
                <div class="note">
                    <strong>Hinweis:</strong> Nach der Autorisierung wirst du automatisch zurück zur Anwendung geleitet. Deine Anmeldedaten werden sicher behandelt und nur für die Anzeige deiner aktuellen Wiedergabeinformationen verwendet.
                </div>
            </div>
        </div>
    </body>
    </html>
    """
    SELECTION_HTML = """
    <!DOCTYPE html>
    <html lang="de">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Spotify Now Playing - Design Auswahl</title>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700&display=swap');
            
            body {
                font-family: 'Montserrat', sans-serif;
                background: linear-gradient(135deg, #121212 0%, #181818 100%);
                color: #ffffff;
                margin: 0;
                padding: 0;
                display: flex;
                flex-direction: column;
                min-height: 100vh;
                align-items: center;
                justify-content: center;
            }
            
            .container {
                max-width: 900px;
                width: 90%;
                padding: 40px;
                text-align: center;
            }
            
            h1 {
                font-size: 2.5rem;
                margin-bottom: 10px;
                font-weight: 700;
                color: #1DB954; /* Spotify green */
            }
            
            p {
                font-size: 1.1rem;
                margin-bottom: 40px;
                opacity: 0.8;
            }
            
            .designs-container {
                display: flex;
                flex-wrap: wrap;
                gap: 30px;
                justify-content: center;
                margin-bottom: 40px;
            }
            
            .design-option {
                width: 380px;
                background: rgba(30, 30, 30, 0.7);
                border-radius: 12px;
                padding: 20px;
                transition: all 0.3s ease;
                border: 2px solid transparent;
                cursor: pointer;
                position: relative;
                overflow: hidden;
            }
            
            .design-option:hover {
                transform: translateY(-5px);
                box-shadow: 0 10px 20px rgba(0, 0, 0, 0.3);
                border-color: #1DB954;
            }
            
            .design-preview {
                width: 100%;
                height: 240px;
                border-radius: 8px;
                margin-bottom: 20px;
                background-color: #000;
                background-size: contain;
                background-position: center;
                background-repeat: no-repeat;
                box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
                display: flex;
                align-items: center;
                justify-content: center;
                overflow: hidden;
            }
            
            /* Modern Design Preview (now-playing2.txt) */
            .design-1-preview {
                background-color: #121212;
                position: relative;
            }

            .modern-widget {
                width: 90%;
                height: 110px;
                border-radius: 12px;
                background: linear-gradient(135deg, rgba(96,135,134,0.9) 0%, rgba(96,135,134,0.5) 50%, rgba(0,0,0,0.8) 100%);
                display: flex;
                flex-direction: row;
                padding: 15px;
                box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
            }

            .modern-cover {
                width: 80px;
                height: 80px;
                border-radius: 6px;
                background-color: #4a89dc;
                margin-right: 15px;
                box-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
                background-image: url('https://i.scdn.co/image/ab67616d0000b2739696c256ad5a8e5118792597');
                background-size: cover;
            }

            .modern-info {
                display: flex;
                flex-direction: column;
                justify-content: center;
                text-align: left;
            }

            .modern-label {
                font-size: 12px;
                font-weight: bold;
                text-transform: uppercase;
                letter-spacing: 1px;
                opacity: 0.8;
                margin-bottom: 5px;
            }

            .modern-title {
                font-size: 18px;
                font-weight: bold;
                margin-bottom: 4px;
                white-space: nowrap;
            }

            .modern-artist {
                font-size: 14px;
                opacity: 0.9;
            }

            .modern-album {
                font-size: 12px;
                opacity: 0.7;
                margin-top: 2px;
            }
            
            /* Vinyl Design Preview (now-playing.txt) */
            .design-2-preview {
                background-color: #121212;
                position: relative;
            }

            .vinyl-widget {
                width: 240px;
                background: linear-gradient(145deg, #1b1b1b, #121212);
                border-radius: 20px;
                padding: 24px;
                box-shadow: 0 0 30px rgba(96, 93, 100, 0.8);
                text-align: center;
                border: 1px solid rgba(96, 93, 100, 0.3);
                display: flex;
                flex-direction: column;
                align-items: center;
            }

            .vinyl-cover {
                width: 120px;
                height: 120px;
                margin-bottom: 16px;
                border-radius: 50%;
                background-image: url('https://i.scdn.co/image/ab67616d0000b273064bc491cd5b09c59dbf053c');
                background-size: cover;
                box-shadow: 0 0 20px rgba(96, 93, 100, 0.7);
                animation: spin 12s linear infinite;
            }

            @keyframes spin {
                0% { transform: rotate(0deg); }
                100% { transform: rotate(360deg); }
            }

            .vinyl-title {
                font-size: 16px;
                font-weight: bold;
                margin-bottom: 8px;
                color: #605D64;
            }

            .vinyl-artist, .vinyl-album {
                font-size: 14px;
                color: #605D64;
                margin-bottom: 4px;
            }
            
            .design-custom-preview {
                background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="380" height="240" viewBox="0 0 380 240"><rect width="380" height="240" fill="%23121212"/><text x="190" y="120" font-family="Arial" font-size="20" fill="%231DB954" text-anchor="middle">Benutzerdefiniertes Design</text><rect x="115" y="140" width="150" height="40" rx="8" stroke="%231DB954" stroke-width="2" stroke-dasharray="5 5" fill="none"/></svg>');
            }
            
            .design-title {
                font-size: 1.2rem;
                font-weight: 600;
                margin-bottom: 10px;
            }
            
            .design-desc {
                font-size: 0.9rem;
                opacity: 0.7;
                margin-bottom: 20px;
            }
            
            .select-btn {
                background-color: #1DB954;
                color: white;
                border: none;
                padding: 10px 20px;
                border-radius: 50px;
                font-size: 1rem;
                font-weight: 600;
                cursor: pointer;
                transition: all 0.2s ease;
            }
            
            .select-btn:hover {
                background-color: #1ed760;
                transform: scale(1.05);
            }
            
            footer {
                margin-top: 40px;
                font-size: 0.9rem;
                opacity: 0.6;
            }
            
            @media (max-width: 768px) {
                .container {
                    padding: 20px;
                }
                
                h1 {
                    font-size: 2rem;
                }
                
                .design-option {
                    width: 100%;
                }
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Spotify Now Playing</h1>
            <p>Wähle ein Design für deine Now Playing Anzeige</p>
            
            <div class="designs-container">
                <div class="design-option" onclick="window.location.href='/'">
                    <div class="design-preview design-1-preview">
                        <div class="modern-widget">
                            <div class="modern-cover"></div>
                            <div class="modern-info">
                                <div class="modern-label">JETZT LÄUFT</div>
                                <div class="modern-title">Swoosh</div>
                                <div class="modern-artist">JONNY5</div>
                                <div class="modern-album">5K / 2K EP</div>
                            </div>
                        </div>
                    </div>
                    <div class="design-title">Modern Design</div>
                    <div class="design-desc">Ein cleanes, modernes Design mit elegantem Farbverlauf-Hintergrund und schlichter Darstellung.</div>
                    <button class="select-btn">Auswählen</button>
                </div>
                
                <div class="design-option" onclick="window.location.href='/design2'">
                    <div class="design-preview design-2-preview">
                        <div class="vinyl-widget">
                            <div class="vinyl-cover"></div>
                            <div class="vinyl-title">Celebrate</div>
                            <div class="vinyl-artist">Lugatti</div>
                            <div class="vinyl-album">Cansado</div>
                        </div>
                    </div>
                    <div class="design-title">Vinyl Design</div>
                    <div class="design-desc">Ein Retro-Design mit rotierender Vinyl-Darstellung des Album-Covers und Neon-Effekten.</div>
                    <button class="select-btn">Auswählen</button>
                </div>
            </div>
            
            <div class="design-option" onclick="window.location.href='/custom'" style="max-width: 380px; margin: 0 auto;">
                <div class="design-preview design-custom-preview"></div>
                <div class="design-title">Benutzerdefiniertes Design</div>
                <div class="design-desc">Nutze dein eigenes benutzerdefiniertes Design-Template.</div>
                <button class="select-btn">Auswählen</button>
            </div>
            
            <footer>
                &copy; 2025 Spotify Now Playing Widget
            </footer>
        </div>
    </body>
    </html>
    """
    NOW_PLAYING2 = """
    <!DOCTYPE html>
    <html lang="de">
    <head>
        <meta charset="UTF-8">
        <title>Now Playing</title>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&display=swap');

            :root {
                --glow-r: 3;
                --glow-g: 136;
                --glow-b: 166;
                --text-color: #0388A6;
            }
            
            body {
                margin: 0;
                padding: 0;
                background: rgba(0, 0, 0, 0);
                font-family: 'Share Tech Mono', monospace;
                color: #f0f0f0;
                display: flex;
                align-items: center;
                justify-content: center;
                height: 100vh;
            }

            .now-playing-vinyl {
                background: linear-gradient(145deg, #1b1b1b, #121212);
                border-radius: 20px;
                padding: 24px;
                box-shadow: 0 0 30px rgba(var(--glow-r), var(--glow-g), var(--glow-b), 0.8);
                width: 300px;
                text-align: center;
                border: 1px solid rgba(var(--glow-r), var(--glow-g), var(--glow-b), 0.3);
                display: {{ 'flex' if is_playing else 'none' }};
                flex-direction: column;
                align-items: center;
            }

            .album-cover {
                width: 150px;
                height: 150px;
                margin-bottom: 16px;
                border-radius: 50%;
                background-size: cover;
                background-position: center;
                box-shadow: 0 0 20px rgba(var(--glow-r), var(--glow-g), var(--glow-b), 0.7);
                animation: pulseGlow 4s infinite alternate, spin 12s linear infinite;
            }

            @keyframes spin {
                0% { transform: rotate(0deg); }
                100% { transform: rotate(360deg); }
            }

            @keyframes pulseGlow {
                from { box-shadow: 0 0 10px rgba(0, 0, 0, 0.2); }
                to { box-shadow: 0 0 20px rgba(var(--glow-r), var(--glow-g), var(--glow-b), 0.7); }
            }

            .track-title {
                font-size: 18px;
                font-weight: bold;
                margin-bottom: 8px;
                color: var(--text-color);
                white-space: nowrap;
                overflow: hidden;
                text-overflow: ellipsis;
                max-width: 260px;
            }

            .artist-name, .album-name {
                font-size: 14px;
                color: var(--text-color);
                margin-bottom: 4px;
                white-space: nowrap;
                overflow: hidden;
                text-overflow: ellipsis;
                max-width: 260px;
            }

            .inactive-message {
                font-size: 16px;
                color: #999999;
                display: {{ 'none' if is_playing else 'block' }};
            }
        </style>

        <script>
            let currentTrack = {
                track: "{{ track }}",
                artist: "{{ artist }}",
                album: "{{ album }}",
                is_playing: {{ 'true' if is_playing else 'false' }},
                album_cover: "{{ album_cover }}"
            };

            function updateDisplay(data) {
                const nowPlaying = document.querySelector('.now-playing-vinyl');
                const inactive = document.querySelector('.inactive-message');
                const trackTitle = document.querySelector('.track-title');
                const artistName = document.querySelector('.artist-name');
                const albumName = document.querySelector('.album-name');
                const albumCover = document.querySelector('.album-cover');

                if (data.track !== currentTrack.track || data.artist !== currentTrack.artist || data.album !== currentTrack.album) {
                    trackTitle.style.opacity = '0';
                    artistName.style.opacity = '0';
                    albumName.style.opacity = '0';

                    setTimeout(() => {
                        trackTitle.textContent = data.track;
                        artistName.textContent = data.artist;
                        albumName.textContent = data.album;
                        trackTitle.style.opacity = '1';
                        artistName.style.opacity = '1';
                        albumName.style.opacity = '1';
                    }, 300);
                }

                if (data.album_cover !== currentTrack.album_cover) {
                    albumCover.style.opacity = '0';
                    setTimeout(() => {
                        albumCover.style.backgroundImage = `url("${data.album_cover}")`;
                        albumCover.style.opacity = '1';
                    }, 300);
                }

                if (data.is_playing !== currentTrack.is_playing) {
                    if (data.is_playing) {
                        nowPlaying.style.display = 'flex';
                        inactive.style.display = 'none';
                    } else {
                        nowPlaying.style.display = 'none';
                        inactive.style.display = 'block';
                    }
                }

                const glowR = data.color_r * 1.5;
                const glowG = data.color_g * 1.5;
                const glowB = data.color_b * 1.5;
                const artistAlbumColor = `rgb(${data.color_r}, ${data.color_g}, ${data.color_b})`;

                document.documentElement.style.setProperty('--glow-r', glowR);
                document.documentElement.style.setProperty('--glow-g', glowG);
                document.documentElement.style.setProperty('--glow-b', glowB);
                document.documentElement.style.setProperty('--text-color', artistAlbumColor);

                currentTrack = data;
            }

            function fetchCurrentTrack() {
                fetch('/api/current-track')
                    .then(response => response.json())
                    .then(data => {
                        updateDisplay(data);
                    })
                    .catch(error => {
                        console.error('Fehler beim Abrufen der Track-Informationen:', error);
                    })
                    .finally(() => {
                        setTimeout(fetchCurrentTrack, 3000);
                    });
            }

            document.addEventListener('DOMContentLoaded', () => {
                setTimeout(fetchCurrentTrack, 1000);
            });
        </script>
    </head>
    <body>
        <div class="now-playing-vinyl">
            <div class="album-cover" style="background-image: url('{{ album_cover }}');"></div>
            <div class="track-title">{{ track }}</div>
            <div class="artist-name">{{ artist }}</div>
            <div class="album-name">{{ album }}</div>
        </div>
        <div class="inactive-message">Kein Song wird abgespielt</div>
    </body>
    </html>
    """
    NOW_PLAYING = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <style>
            body {
                font-family: 'Arial', sans-serif;
                margin: 0;
                padding: 0;
                background-color: rgba(0, 0, 0, 0);
                color: white;
                overflow: hidden;
            }

            @keyframes fadeIn {
                from { opacity: 0; }
                to { opacity: 1; }
            }

            .now-playing-container {
                width: 450px;
                height: auto;
                padding: 15px;
                border-radius: 12px;
                background: linear-gradient(135deg, rgba({{ color_r }},{{ color_g }},{{ color_b }},0.9) 0%, rgba({{ color_r }},{{ color_g }},{{ color_b }},0.5) 50%, rgba(0,0,0,0.8) 100%);
                box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
                display: {{ 'flex' if is_playing else 'none' }};
                flex-direction: row;
                justify-content: flex-start;
                position: relative;
                overflow: hidden;
                transition: all 0.5s ease-in-out;
                backdrop-filter: blur(5px);
            }

            .album-cover {
                width: 80px;
                height: 80px;
                border-radius: 6px;
                margin-right: 15px;
                box-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
                background-size: cover;
                background-position: center;
                flex-shrink: 0;
                animation: pulseGlow 3s infinite alternate;
            }

            @keyframes pulseGlow {
                from { box-shadow: 0 2px 10px rgba(0, 0, 0, 0.3); }
                to { box-shadow: 0 2px 15px rgba({{ color_r }},{{ color_g }},{{ color_b }},0.7); }
            }

            .track-info {
                display: flex;
                flex-direction: column;
                justify-content: center;
                flex-grow: 1;
                overflow: hidden;
            }

            .label {
                font-size: 14px;
                font-weight: bold;
                text-transform: uppercase;
                letter-spacing: 1px;
                opacity: 0.8;
                margin-bottom: 5px;
            }

            .track-title {
                font-size: 20px;
                font-weight: bold;
                margin-bottom: 4px;
                white-space: nowrap;
                overflow: hidden;
                text-overflow: ellipsis;
                max-width: 320px;
                transition: all 0.3s ease-in-out;
            }

            .artist-name {
                font-size: 16px;
                margin-top: 0px;
                white-space: nowrap;
                overflow: hidden;
                text-overflow: ellipsis;
                max-width: 320px;
                opacity: 0.9;
                transition: all 0.3s ease-in-out;
            }

            .album-name {
                font-size: 14px;
                margin-top: 2px;
                white-space: nowrap;
                overflow: hidden;
                text-overflow: ellipsis;
                max-width: 320px;
                opacity: 0.7;
                transition: all 0.3s ease-in-out;
            }

            .not-playing {
                display: {{ 'flex' if not is_playing else 'none' }};
                width: 250px;
                height: 50px;
                padding: 10px;
                border-radius: 10px;
                background: rgba(0, 0, 0, 0.7);
                justify-content: center;
                align-items: center;
                transition: all 0.5s ease-in-out;
            }

            .fade-update {
                animation: fadeUpdate 0.5s ease-in-out;
            }

            @keyframes fadeUpdate {
                0% { opacity: 0.3; }
                100% { opacity: 1; }
            }
        </style>
        <script>
            let currentTrack = {
                track: "{{ track }}",
                artist: "{{ artist }}",
                album: "{{ album }}",
                is_playing: {{ 'true' if is_playing else 'false' }},
                album_cover: "{{ album_cover }}"
            };

            let currentColors = {
                r: {{ color_r }},
                g: {{ color_g }},
                b: {{ color_b }}
            };

            function updateDisplay(data) {
                const nowPlayingContainer = document.querySelector('.now-playing-container');
                const notPlayingContainer = document.querySelector('.not-playing');
                const trackTitle = document.querySelector('.track-title');
                const artistName = document.querySelector('.artist-name');
                const albumName = document.querySelector('.album-name');
                const albumCover = document.querySelector('.album-cover');

                if (data.track !== currentTrack.track || 
                    data.artist !== currentTrack.artist || 
                    data.album !== currentTrack.album) {
                    trackTitle.style.opacity = '0';
                    artistName.style.opacity = '0';
                    albumName.style.opacity = '0';

                    setTimeout(() => {
                        trackTitle.textContent = data.track;
                        artistName.textContent = data.artist;
                        albumName.textContent = data.album;
                        trackTitle.style.opacity = '1';
                        artistName.style.opacity = '1';
                        albumName.style.opacity = '1';
                    }, 300);
                }

                if (data.album_cover !== currentTrack.album_cover) {
                    albumCover.style.opacity = '0';
                    setTimeout(() => {
                        albumCover.style.backgroundImage = `url("${data.album_cover}")`;
                        albumCover.style.opacity = '1';
                    }, 300);
                }

                if (data.is_playing !== currentTrack.is_playing) {
                    if (data.is_playing) {
                        nowPlayingContainer.style.display = 'flex';
                        notPlayingContainer.style.display = 'none';
                        nowPlayingContainer.classList.add('fade-update');
                        setTimeout(() => nowPlayingContainer.classList.remove('fade-update'), 500);
                    } else {
                        nowPlayingContainer.style.display = 'none';
                        notPlayingContainer.style.display = 'flex';
                        notPlayingContainer.classList.add('fade-update');
                        setTimeout(() => notPlayingContainer.classList.remove('fade-update'), 500);
                    }
                }

                if (data.color_r !== currentColors.r || 
                    data.color_g !== currentColors.g || 
                    data.color_b !== currentColors.b) {
                    nowPlayingContainer.style.background = `linear-gradient(135deg, 
                        rgba(${data.color_r},${data.color_g},${data.color_b},0.9) 0%, 
                        rgba(${data.color_r},${data.color_g},${data.color_b},0.5) 50%, 
                        rgba(0,0,0,0.8) 100%)`;

                    document.styleSheets[0].insertRule(
                        `@keyframes pulseGlow {
                            from { box-shadow: 0 2px 10px rgba(0, 0, 0, 0.3); }
                            to { box-shadow: 0 2px 15px rgba(${data.color_r},${data.color_g},${data.color_b},0.7); }
                        }`, 
                        document.styleSheets[0].cssRules.length
                    );

                    currentColors = {
                        r: data.color_r,
                        g: data.color_g,
                        b: data.color_b
                    };
                }

                currentTrack = {
                    track: data.track,
                    artist: data.artist,
                    album: data.album,
                    is_playing: data.is_playing,
                    album_cover: data.album_cover
                };
            }

            function fetchCurrentTrack() {
                fetch('/api/current-track')
                    .then(response => response.json())
                    .then(data => updateDisplay(data))
                    .catch(error => console.error('Fehler beim Abrufen der Track-Informationen:', error))
                    .finally(() => setTimeout(fetchCurrentTrack, 3000));
            }

            document.addEventListener('DOMContentLoaded', function() {
                setTimeout(fetchCurrentTrack, 1000);
            });
        </script>
    </head>
    <body>
        <div class="now-playing-container">
            <div class="album-cover" style="background-image: url('{{ album_cover }}')"></div>
            <div class="track-info">
                <div class="label">JETZT LÄUFT</div>
                <div class="track-title">{{ track }}</div>
                <div class="artist-name">{{ artist }}</div>
                <div class="album-name">{{ album }}</div>
            </div>
        </div>

        <div class="not-playing">
            <div class="track-title">Kein Song wird abgespielt</div>
        </div>
    </body>
    </html>
    """
    BACKGROUND = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Cannabis Stream Background</title>
        <style>
            body {
                margin: 0;
                padding: 0;
                overflow: hidden;
                background-color: #0A0A0A;
                font-family: 'Arial', sans-serif;
            }
            
            .background-container {
                position: fixed;
                width: 100%;
                height: 100%;
                top: 0;
                left: 0;
                z-index: -1;
            }
            
            .gradient-bg {
                position: absolute;
                width: 100%;
                height: 100%;
                background: radial-gradient(circle at center, #101010 0%, #050505 100%);
                opacity: 0.8;
            }
            
            .smoke {
                position: absolute;
                width: 100%;
                height: 100%;
                background: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%"><filter id="n" x="0%" y="0%" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency="0.01" numOctaves="3" stitchTiles="stitch"/><feComponentTransfer><feFuncR type="linear" slope="0" intercept="0"/><feFuncG type="linear" slope="0.1" intercept="0"/><feFuncB type="linear" slope="0.1" intercept="0"/><feFuncA type="linear" slope="0.3" intercept="0"/></feComponentTransfer></filter><rect width="100%" height="100%" filter="url(%23n)" opacity="0.3"/></svg>');
                opacity: 0.4;
                mix-blend-mode: screen;
                animation: drift 60s linear infinite;
            }
            
            @keyframes drift {
                0% { transform: translateY(0) scale(1.5); }
                50% { transform: translateY(-10%) scale(1.7); }
                100% { transform: translateY(0) scale(1.5); }
            }
            
            .leaf {
                position: absolute;
                width: 60px;
                height: 60px;
                background-size: contain;
                background-repeat: no-repeat;
                background-position: center;
                opacity: 0;
                pointer-events: none;
                filter: drop-shadow(0 0 10px rgba(75, 161, 51, 0.7));
            }
            
            .leaf-svg {
                fill: currentColor;
                width: 100%;
                height: 100%;
            }
            
            .bubble {
                position: absolute;
                border-radius: 50%;
                background: radial-gradient(circle at 30% 30%, rgba(255, 255, 255, 0.3), rgba(50, 205, 50, 0.1));
                box-shadow: inset 0 0 15px rgba(255, 255, 255, 0.3), 0 0 10px rgba(75, 161, 51, 0.5);
                opacity: 0;
                pointer-events: none;
            }
            
            .floating-orb {
                position: absolute;
                border-radius: 50%;
                background: radial-gradient(circle, rgba(75, 161, 51, 0.2) 0%, rgba(35, 90, 25, 0.1) 50%, rgba(20, 50, 15, 0) 70%);
                filter: blur(15px);
                opacity: 0.4;
                mix-blend-mode: screen;
            }
            
            .wave {
                position: absolute;
                width: 150%;
                height: 150%;
                left: -25%;
                top: -25%;
                background: linear-gradient(45deg, 
                    rgba(75, 161, 51, 0.05), 
                    rgba(30, 90, 40, 0.07), 
                    rgba(20, 70, 20, 0.05), 
                    rgba(75, 161, 51, 0.08));
                border-radius: 40%;
                opacity: 0.3;
                mix-blend-mode: screen;
                transform-origin: center;
                animation: rotate 60s infinite linear;
            }
            
            @keyframes rotate {
                0% { transform: rotate(0deg); }
                100% { transform: rotate(360deg); }
            }
            
            .audio-bar {
                position: absolute;
                bottom: 0;
                background: linear-gradient(to top, #4BA133, rgba(10, 10, 10, 0));
                width: 10px;
                transform-origin: bottom;
                border-radius: 3px 3px 0 0;
                opacity: 0.7;
            }
            
            .glow {
                position: fixed;
                width: 200px;
                height: 200px;
                border-radius: 50%;
                background: radial-gradient(circle, rgba(75, 161, 51, 0.3) 0%, rgba(75, 161, 51, 0) 70%);
                filter: blur(20px);
                pointer-events: none;
                mix-blend-mode: screen;
                transform: translate(-50%, -50%);
                z-index: 100;
            }
            
            .particle {
                position: absolute;
                border-radius: 50%;
                background: radial-gradient(circle, rgba(255, 255, 255, 0.8), rgba(75, 161, 51, 0.5), rgba(75, 161, 51, 0));
                opacity: 0;
                pointer-events: none;
            }
        </style>
    </head>
    <body>
        <div class="background-container">
            <div class="gradient-bg"></div>
            <div class="smoke"></div>
            <div id="wave-container"></div>
            <div id="leaf-container"></div>
            <div id="bubble-container"></div>
            <div id="orb-container"></div>
            <div id="particle-container"></div>
            <div id="audio-visualizer"></div>
        </div>
        <div class="glow" id="glow"></div>
        
        <script>
            // Konfiguration
            const config = {
                leaves: {
                    count: 20,
                    minSize: 30,
                    maxSize: 80,
                    minDuration: 15000,
                    maxDuration: 30000,
                    rotationSpeed: 2,
                    colors: [
                        '#4BA133', // Grün
                        '#3D8929', // Dunkleres Grün
                        '#5BB545', // Helleres Grün
                        '#4F9A3D', // Mittleres Grün
                        '#2D7A19'  // Tiefes Grün
                    ]
                },
                bubbles: {
                    count: 30,
                    minSize: 5,
                    maxSize: 30,
                    minDuration: 5000,
                    maxDuration: 15000
                },
                orbs: {
                    count: 8,
                    minSize: 200,
                    maxSize: 500,
                    minDuration: 30000,
                    maxDuration: 60000
                },
                waves: {
                    count: 3,
                    speed: 60000, // ms für eine Rotation
                },
                particles: {
                    count: 40,
                    minSize: 3,
                    maxSize: 10,
                    minDuration: 3000,
                    maxDuration: 8000
                },
                audioBars: {
                    count: 40,
                    minHeight: 30,
                    maxHeight: 200,
                    updateInterval: 80,
                    gap: 5
                }
            };
            
            // DOM-Elemente
            const waveContainer = document.getElementById('wave-container');
            const leafContainer = document.getElementById('leaf-container');
            const bubbleContainer = document.getElementById('bubble-container');
            const orbContainer = document.getElementById('orb-container');
            const particleContainer = document.getElementById('particle-container');
            const glow = document.getElementById('glow');
            
            // Fenstergröße
            let windowWidth = window.innerWidth;
            let windowHeight = window.innerHeight;
            
            // Cannabis-Blatt SVG
            const leafSVG = `
                <svg class="leaf-svg" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
                    <path d="M50,7 C50,7 20,25 20,45 C20,52 27,60 35,60 C38,60 42,58 43,55 C43,55 42,65 40,70 C38,75 37,78 37,82 C37,85 38,88 40,90 C42,92 45,94 50,94 C55,94 58,92 60,90 C62,88 63,85 63,82 C63,78 62,75 60,70 C58,65 57,55 57,55 C58,58 62,60 65,60 C73,60 80,52 80,45 C80,25 50,7 50,7 Z M40,25 C40,25 37,35 37,43 C37,47 39,50 42,50 C44,50 45,49 45,47 C45,45 44,40 44,40 C44,40 44,45 47,45 C50,45 52,42 52,38 C52,30 45,20 45,20 C45,20 47,30 47,35 C47,37 46,38 45,38 C44,38 43,37 43,35 C43,30 40,25 40,25 Z M55,20 C55,20 48,30 48,38 C48,42 50,45 53,45 C56,45 56,40 56,40 C56,40 55,45 55,47 C55,49 56,50 58,50 C61,50 63,47 63,43 C63,35 60,25 60,25 C60,25 57,30 57,35 C57,37 56,38 55,38 C54,38 53,37 53,35 C53,30 55,20 55,20 Z" />
                </svg>
            `;
            
            // Wellen erstellen
            function createWaves() {
                for (let i = 0; i < config.waves.count; i++) {
                    const wave = document.createElement('div');
                    wave.className = 'wave';
                    wave.style.opacity = 0.15 + (i * 0.1);
                    wave.style.animationDelay = `${-i * 10}s`;
                    waveContainer.appendChild(wave);
                }
            }
            
            // Cannabis-Blätter erstellen und animieren
            function createLeaves() {
                for (let i = 0; i < config.leaves.count; i++) {
                    createLeaf();
                }
                
                // Regelmäßig neue Blätter erstellen
                setInterval(createLeaf, 2000);
            }
            
            function createLeaf() {
                const leaf = document.createElement('div');
                leaf.className = 'leaf';
                leaf.innerHTML = leafSVG;
                
                // Zufällige Größe und Position
                const size = Math.random() * (config.leaves.maxSize - config.leaves.minSize) + config.leaves.minSize;
                const x = Math.random() * windowWidth;
                const startY = windowHeight + size;
                
                leaf.style.width = `${size}px`;
                leaf.style.height = `${size}px`;
                leaf.style.left = `${x}px`;
                leaf.style.top = `${startY}px`;
                
                // Zufällige Farbe aus der Konfiguration
                const colorIndex = Math.floor(Math.random() * config.leaves.colors.length);
                leaf.style.color = config.leaves.colors[colorIndex];
                
                leafContainer.appendChild(leaf);
                
                // Animation
                const duration = Math.random() * (config.leaves.maxDuration - config.leaves.minDuration) + config.leaves.minDuration;
                const endY = -size;
                const rotationSpeed = Math.random() * config.leaves.rotationSpeed;
                const horizontalMovement = Math.random() * 100 - 50; // -50px bis +50px
                
                // Start time für Animation
                const startTime = performance.now();
                const animate = (currentTime) => {
                    const elapsed = currentTime - startTime;
                    const progress = Math.min(elapsed / duration, 1);
                    
                    // Easing-Funktionen für sanfte Bewegung
                    const easeInOut = t => t < 0.5 ? 2 * t * t : -1 + (4 - 2 * t) * t;
                    const fadeIn = Math.min(progress * 5, 0.8);
                    const fadeOut = Math.max(0, Math.min((1 - progress) * 5, 1));
                    
                    // Position, Rotation und Opazität aktualisieren
                    const currentY = startY + (endY - startY) * progress;
                    const currentX = x + Math.sin(progress * 5) * horizontalMovement;
                    const currentRotation = progress * 360 * rotationSpeed;
                    
                    leaf.style.top = `${currentY}px`;
                    leaf.style.left = `${currentX}px`;
                    leaf.style.transform = `rotate(${currentRotation}deg)`;
                    leaf.style.opacity = progress < 0.2 ? fadeIn : (progress > 0.8 ? fadeOut : 0.8);
                    
                    if (progress < 1) {
                        requestAnimationFrame(animate);
                    } else {
                        leaf.remove();
                    }
                };
                
                requestAnimationFrame(animate);
            }
            
            // Blasen/Bubbles erstellen und animieren
            function createBubbles() {
                for (let i = 0; i < config.bubbles.count; i++) {
                    createBubble();
                }
                
                // Regelmäßig neue Blasen erstellen
                setInterval(createBubble, 1000);
            }
            
            function createBubble() {
                const bubble = document.createElement('div');
                bubble.className = 'bubble';
                
                // Zufällige Größe und Position
                const size = Math.random() * (config.bubbles.maxSize - config.bubbles.minSize) + config.bubbles.minSize;
                const x = Math.random() * windowWidth;
                const startY = windowHeight + size;
                
                bubble.style.width = `${size}px`;
                bubble.style.height = `${size}px`;
                bubble.style.left = `${x}px`;
                bubble.style.top = `${startY}px`;
                
                bubbleContainer.appendChild(bubble);
                
                // Animation
                const duration = Math.random() * (config.bubbles.maxDuration - config.bubbles.minDuration) + config.bubbles.minDuration;
                const endY = -size;
                const horizontalMovement = Math.random() * 200 - 100; // -100px bis +100px
                
                const startTime = performance.now();
                const animate = (currentTime) => {
                    const elapsed = currentTime - startTime;
                    const progress = Math.min(elapsed / duration, 1);
                    
                    // Sanfte Bewegung
                    const currentY = startY + (endY - startY) * progress;
                    const currentX = x + Math.sin(progress * 3) * horizontalMovement;
                    
                    // Position und Opazität
                    bubble.style.top = `${currentY}px`;
                    bubble.style.left = `${currentX}px`;
                    bubble.style.opacity = progress < 0.2 ? progress * 5 : (progress > 0.8 ? (1 - progress) * 5 : 1);
                    
                    if (progress < 1) {
                        requestAnimationFrame(animate);
                    } else {
                        bubble.remove();
                    }
                };
                
                requestAnimationFrame(animate);
            }
            
            // Schwebende Orbs erstellen
            function createOrbs() {
                for (let i = 0; i < config.orbs.count; i++) {
                    createOrb();
                }
                
                // Regelmäßig neue Orbs erstellen
                setInterval(createOrb, 10000);
            }
            
            function createOrb() {
                const orb = document.createElement('div');
                orb.className = 'floating-orb';
                
                // Zufällige Größe und Position
                const size = Math.random() * (config.orbs.maxSize - config.orbs.minSize) + config.orbs.minSize;
                const x = Math.random() * windowWidth;
                const y = Math.random() * windowHeight;
                
                orb.style.width = `${size}px`;
                orb.style.height = `${size}px`;
                orb.style.left = `${x}px`;
                orb.style.top = `${y}px`;
                
                orbContainer.appendChild(orb);
                
                // Animation
                const duration = Math.random() * (config.orbs.maxDuration - config.orbs.minDuration) + config.orbs.minDuration;
                const targetX = Math.random() * windowWidth;
                const targetY = Math.random() * windowHeight;
                
                const startTime = performance.now();
                const animate = (currentTime) => {
                    const elapsed = currentTime - startTime;
                    const progress = Math.min(elapsed / duration, 1);
                    
                    // Easing-Funktionen für sanfte Bewegung
                    const easeInOut = t => t < 0.5 ? 2 * t * t : -1 + (4 - 2 * t) * t;
                    const fadeIn = Math.min(progress * 3, 1);
                    const fadeOut = Math.max(0, Math.min((1 - progress) * 3, 1));
                    
                    // Position und Opazität
                    const currentX = x + (targetX - x) * easeInOut(progress);
                    const currentY = y + (targetY - y) * easeInOut(progress);
                    
                    orb.style.left = `${currentX}px`;
                    orb.style.top = `${currentY}px`;
                    orb.style.opacity = progress < 0.3 ? fadeIn * 0.4 : (progress > 0.7 ? fadeOut * 0.4 : 0.4);
                    
                    if (progress < 1) {
                        requestAnimationFrame(animate);
                    } else {
                        orb.remove();
                    }
                };
                
                requestAnimationFrame(animate);
            }
            
            // Partikel erstellen für funkelnde Effekte
            function createParticles() {
                for (let i = 0; i < config.particles.count; i++) {
                    createParticle();
                }
                
                // Regelmäßig neue Partikel erstellen
                setInterval(createParticle, 500);
            }
            
            function createParticle() {
                const particle = document.createElement('div');
                particle.className = 'particle';
                
                // Zufällige Größe und Position
                const size = Math.random() * (config.particles.maxSize - config.particles.minSize) + config.particles.minSize;
                const x = Math.random() * windowWidth;
                const y = Math.random() * windowHeight;
                
                particle.style.width = `${size}px`;
                particle.style.height = `${size}px`;
                particle.style.left = `${x}px`;
                particle.style.top = `${y}px`;
                
                particleContainer.appendChild(particle);
                
                // Animation
                const duration = Math.random() * (config.particles.maxDuration - config.particles.minDuration) + config.particles.minDuration;
                const targetX = x + (Math.random() * 200 - 100);
                const targetY = y + (Math.random() * 200 - 100);
                
                const startTime = performance.now();
                const animate = (currentTime) => {
                    const elapsed = currentTime - startTime;
                    const progress = Math.min(elapsed / duration, 1);
                    
                    // Easing
                    const fadeIn = Math.min(progress * 5, 1);
                    const fadeOut = Math.max(0, Math.min((1 - progress) * 5, 1));
                    
                    // Position und Opazität
                    const currentX = x + (targetX - x) * progress;
                    const currentY = y + (targetY - y) * progress;
                    
                    particle.style.left = `${currentX}px`;
                    particle.style.top = `${currentY}px`;
                    particle.style.opacity = progress < 0.2 ? fadeIn * 0.7 : (progress > 0.8 ? fadeOut * 0.7 : 0.7);
                    
                    if (progress < 1) {
                        requestAnimationFrame(animate);
                    } else {
                        particle.remove();
                    }
                };
                
                requestAnimationFrame(animate);
            }
            
            // Glüheffekt folgt der Maus
            function initGlowEffect() {
                document.addEventListener('mousemove', (e) => {
                    glow.style.left = `${e.clientX}px`;
                    glow.style.top = `${e.clientY}px`;
                });
            }
            
            // Fenstergröße aktualisieren
            function updateWindowSize() {
                windowWidth = window.innerWidth;
                windowHeight = window.innerHeight;
            }
            
            // Event-Listener für Fenstergröße
            window.addEventListener('resize', updateWindowSize);
            
            // Initialisierung
            function init() {
                updateWindowSize();
                createWaves();
                createLeaves();
                createBubbles();
                createOrbs();
                createParticles();
                initGlowEffect();
            }
            
            // Starten
            window.addEventListener('DOMContentLoaded', init);
        </script>
    </body>
    </html>
    """
    CUSTOM = """
    <!DOCTYPE html>
    <html lang="de">
    <head>
        <meta charset="UTF-8">
        <title>Now Playing Custom Template</title>
        <style>
            /* --- FONT IMPORTS --- */
            /* Du kannst diesen Font durch deinen bevorzugten Font ersetzen */
            @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;600;700&display=swap');

            /* --- ROOT VARIABLES --- */
            /* Diese Variablen machen die Anpassung einfacher */
            :root {
                /* Hauptfarbschema - Standardmäßig werden Farben aus der API verwendet */
                --primary-color: {{ color_r }}, {{ color_g }}, {{ color_b }};   /* Aus API-Antwort */
                --secondary-color: {{ color_r + 40 }}, {{ color_g + 40 }}, {{ color_b + 40 }}; /* Hellere Variante */
                --accent-color: {{ 255 - color_r }}, {{ 255 - color_g }}, {{ 255 - color_b }}; /* Komplementärfarbe */
                --text-color: 255, 255, 255;      /* Weiß */
                --background-opacity: 0.75;       /* Hintergrund-Transparenz */
                
                /* Animationsgeschwindigkeiten */
                --transition-speed: 0.4s;
                --progress-speed: 0.5s;          /* Geschwindigkeit der Fortschrittsanzeige */
                
                /* Container-Dimensionen */
                --container-width: 450px;         /* Breite des Containers */
                --album-cover-size: 140px;        /* Größe des Album-Covers */
                --border-radius: 20px;            /* Rundung der Ecken */
            }
            
            /* --- ALLGEMEINE STILE --- */
            body {
                margin: 0;
                padding: 0;
                background: rgba(0, 0, 0, 0);     /* Transparenter Hintergrund für OBS */
                font-family: 'Montserrat', sans-serif;
                color: rgb(var(--text-color));
                display: flex;
                align-items: center;
                justify-content: center;
                height: 100vh;
            }

            /* --- HAUPTCONTAINER --- */
            .now-playing-container {
                /* Der Hauptwidget-Container */
                width: var(--container-width);
                padding: 25px;
                border-radius: var(--border-radius);
                
                /* Horizontaler Verlauf von dunkel nach hell */
                background: linear-gradient(110deg, 
                    rgba(var(--primary-color), var(--background-opacity)) 0%, 
                    rgba(var(--secondary-color), var(--background-opacity)) 100%);
                
                /* Glassmorphismus-Effekt - nach Bedarf anpassen oder entfernen */
                backdrop-filter: blur(10px);
                -webkit-backdrop-filter: blur(10px);
                
                /* Neuer Rahmen mit doppelter Linie */
                border: 2px solid rgba(var(--text-color), 0.15);
                box-shadow: 
                    0 10px 30px rgba(0, 0, 0, 0.4),
                    0 0 0 1px rgba(var(--primary-color), 0.1) inset;
                
                /* Layout als vertikaler Stapel */
                display: {{ 'flex' if is_playing else 'none' }};
                flex-direction: column;
                gap: 25px;
                position: relative;
                overflow: hidden;
                transition: all var(--transition-speed) ease;
            }

            /* --- HEADER-BEREICH --- */
            .header-area {
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin-bottom: 5px;
            }

            /* "JETZT LÄUFT" Label */
            .now-playing-label {
                font-size: 13px;
                text-transform: uppercase;
                letter-spacing: 2px;
                font-weight: 600;
                color: rgb(var(--text-color));
                background: rgba(var(--accent-color), 0.2);
                padding: 6px 12px;
                border-radius: 50px;
                box-shadow: 0 0 10px rgba(var(--accent-color), 0.3);
            }

            /* Musik-Icon */
            .music-icon {
                font-size: 24px;
                opacity: 0.8;
                animation: pulse 2s infinite ease-in-out;
            }

            @keyframes pulse {
                0%, 100% { transform: scale(1); opacity: 0.8; }
                50% { transform: scale(1.1); opacity: 1; }
            }

            /* --- CONTENT-BEREICH --- */
            .content-area {
                display: flex;
                flex-direction: row;
                align-items: center;
                gap: 25px;
            }

            /* --- ALBUM COVER --- */
            .album-cover {
                /* Album-Artwork-Anzeige */
                width: var(--album-cover-size);
                height: var(--album-cover-size);
                border-radius: 15px;
                background-size: cover;
                background-position: center;
                flex-shrink: 0;
                
                /* Neuer Effekt mit verbessertem Schatten und Rahmen */
                box-shadow: 
                    0 10px 20px rgba(0, 0, 0, 0.4),
                    0 0 0 1px rgba(var(--text-color), 0.1),
                    0 0 20px rgba(var(--primary-color), 0.5);
                
                /* Transformationseffekt für Interaktion */
                transform: rotate(-3deg);
                transition: all var(--transition-speed) ease;
                position: relative;
                z-index: 2;
            }

            /* Album-Cover-Hover-Effekt */
            .album-cover:hover {
                transform: rotate(0deg) scale(1.05);
                box-shadow: 
                    0 15px 30px rgba(0, 0, 0, 0.6),
                    0 0 0 1px rgba(var(--text-color), 0.2),
                    0 0 30px rgba(var(--primary-color), 0.7);
            }

            /* Album-Cover-Schein */
            .album-cover::after {
                content: '';
                position: absolute;
                top: -10px;
                left: -10px;
                right: -10px;
                bottom: -10px;
                background: radial-gradient(circle at center, 
                    rgba(var(--primary-color), 0.4) 0%, 
                    rgba(var(--primary-color), 0) 70%);
                z-index: -1;
                border-radius: 20px;
                opacity: 0.7;
                animation: glowPulse 3s infinite alternate;
            }

            @keyframes glowPulse {
                0% { opacity: 0.4; transform: scale(0.95); }
                100% { opacity: 0.8; transform: scale(1.05); }
            }

            /* --- TRACK-INFO-CONTAINER --- */
            .track-info {
                display: flex;
                flex-direction: column;
                justify-content: center;
                flex-grow: 1;
                overflow: hidden;
            }

            /* Song-Titel */
            .track-title {
                font-size: 26px;
                font-weight: 700;
                margin-bottom: 10px;
                white-space: nowrap;
                overflow: hidden;
                text-overflow: ellipsis;
                color: rgb(var(--text-color));
                transition: opacity var(--transition-speed) ease;
                text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
                position: relative;
            }

            /* Künstlername */
            .artist-name {
                font-size: 20px;
                margin-bottom: 6px;
                white-space: nowrap;
                overflow: hidden;
                text-overflow: ellipsis;
                opacity: 0.9;
                transition: opacity var(--transition-speed) ease;
                font-weight: 600;
            }

            /* Albumname */
            .album-name {
                font-size: 16px;
                white-space: nowrap;
                overflow: hidden;
                text-overflow: ellipsis;
                opacity: 0.7;
                transition: opacity var(--transition-speed) ease;
                font-weight: 300;
                font-style: italic;
            }

            /* --- PROGRESSBAR --- */
            .progress-section {
                width: 100%;
                margin-top: 5px;
            }

            .progress-bar {
                height: 4px;
                width: 100%;
                background: rgba(var(--text-color), 0.2);
                border-radius: 2px;
                overflow: hidden;
                position: relative;
            }

            .progress-fill {
                height: 100%;
                width: 35%; /* Nur ein Beispielwert - wird durch API aktualisiert */
                background: rgba(var(--accent-color), 0.8);
                position: absolute;
                left: 0;
                top: 0;
                border-radius: 2px;
                transition: width var(--progress-speed) linear;
            }

            /* --- INAKTIVER ZUSTAND --- */
            /* Meldung, wenn nichts abgespielt wird */
            .inactive-message {
                background: rgba(30, 30, 30, 0.8);
                padding: 20px 40px;
                border-radius: var(--border-radius);
                text-align: center;
                font-size: 18px;
                display: {{ 'flex' if not is_playing else 'none' }};
                flex-direction: column;
                align-items: center;
                gap: 15px;
                box-shadow: 0 8px 20px rgba(0, 0, 0, 0.3);
                transition: all var(--transition-speed) ease;
                border: 1px solid rgba(var(--text-color), 0.1);
            }

            .inactive-icon {
                font-size: 30px;
                opacity: 0.7;
                margin-bottom: 10px;
            }

            /* Animation für Content-Updates */
            .fade-update {
                animation: fadeIn var(--transition-speed) ease;
            }

            @keyframes fadeIn {
                from { opacity: 0; transform: translateY(10px); }
                to { opacity: 1; transform: translateY(0); }
            }

            /* Animationen für bewegliche Elemente */
            @keyframes float {
                0%, 100% { transform: translateY(0); }
                50% { transform: translateY(-5px); }
            }

            /* --- MEDIA QUERIES --- */
            /* Anpassungen für kleinere Bildschirme */
            @media (max-width: 600px) {
                :root {
                    --container-width: 320px;
                    --album-cover-size: 100px;
                }
                
                .content-area {
                    gap: 15px;
                }
                
                .track-title {
                    font-size: 20px;
                }
                
                .artist-name {
                    font-size: 16px;
                }
                
                .album-name {
                    font-size: 14px;
                }
            }
        </style>
        <script>
            // Aktuelle Track- und Farbdaten zum Vergleich
            let currentTrack = {
                track: "{{ track }}",
                artist: "{{ artist }}",
                album: "{{ album }}",
                is_playing: {{ 'true' if is_playing else 'false' }},
                album_cover: "{{ album_cover }}",
                // Neue Fortschrittsinformationen
                progress: 0,
                duration: 0
            };

            // RGB-Werte für dynamische Farbanpassungen
            let currentColors = {
                r: {{ color_r }},
                g: {{ color_g }},
                b: {{ color_b }}
            };

            // Funktion zum Aktualisieren der UI mit neuen Track-Daten
            function updateDisplay(data) {
                // Referenzen zu allen UI-Elementen
                const nowPlayingContainer = document.querySelector('.now-playing-container');
                const inactiveMessage = document.querySelector('.inactive-message');
                const trackTitle = document.querySelector('.track-title');
                const artistName = document.querySelector('.artist-name');
                const albumName = document.querySelector('.album-name');
                const albumCover = document.querySelector('.album-cover');
                const progressFill = document.querySelector('.progress-fill');
                const currentTime = document.querySelector('.current-time');
                const totalTime = document.querySelector('.total-time');

                // Track-Informationen mit Fade-Animation aktualisieren, wenn sich etwas geändert hat
                if (data.track !== currentTrack.track || 
                    data.artist !== currentTrack.artist || 
                    data.album !== currentTrack.album) {
                    
                    // Aktuelle Informationen ausblenden
                    trackTitle.style.opacity = '0';
                    artistName.style.opacity = '0';
                    albumName.style.opacity = '0';
                    
                    // Textinhalt nach kurzer Verzögerung aktualisieren
                    setTimeout(() => {
                        trackTitle.textContent = data.track;
                        artistName.textContent = data.artist;
                        albumName.textContent = data.album;
                        
                        // Mit neuem Inhalt wieder einblenden
                        trackTitle.style.opacity = '1';
                        artistName.style.opacity = '1';
                        albumName.style.opacity = '1';
                    }, 300);
                }

                // Album-Cover mit Fade-Animation aktualisieren, wenn sich etwas geändert hat
                if (data.album_cover !== currentTrack.album_cover) {
                    albumCover.style.opacity = '0';
                    setTimeout(() => {
                        albumCover.style.backgroundImage = `url("${data.album_cover}")`;
                        albumCover.style.opacity = '1';
                    }, 300);
                }

                // Zwischen spielendem und nicht spielendem Zustand wechseln
                if (data.is_playing !== currentTrack.is_playing) {
                    if (data.is_playing) {
                        nowPlayingContainer.style.display = 'flex';
                        inactiveMessage.style.display = 'none';
                        nowPlayingContainer.classList.add('fade-update');
                        setTimeout(() => nowPlayingContainer.classList.remove('fade-update'), 500);
                    } else {
                        nowPlayingContainer.style.display = 'none';
                        inactiveMessage.style.display = 'flex';
                        inactiveMessage.classList.add('fade-update');
                        setTimeout(() => inactiveMessage.classList.remove('fade-update'), 500);
                    }
                }


                // Farben aktualisieren, wenn sie sich geändert haben (für adaptives Farbschema)
                if (data.color_r !== currentColors.r || 
                    data.color_g !== currentColors.g || 
                    data.color_b !== currentColors.b) {
                    
                    // CSS-Variablen für die dynamischen Farben aktualisieren
                    document.documentElement.style.setProperty('--primary-color', 
                        `${data.color_r}, ${data.color_g}, ${data.color_b}`);
                    
                    // Hellere Variante für Sekundärfarbe
                    const complementaryR = Math.min(255, data.color_r + 40);
                    const complementaryG = Math.min(255, data.color_g + 40);
                    const complementaryB = Math.min(255, data.color_b + 40);
                    
                    document.documentElement.style.setProperty('--secondary-color', 
                        `${complementaryR}, ${complementaryG}, ${complementaryB}`);
                    
                    // Akzentfarbe als Komplementärfarbe
                    const accentR = 255 - data.color_r;
                    const accentG = 255 - data.color_g;
                    const accentB = 255 - data.color_b;
                    
                    document.documentElement.style.setProperty('--accent-color', 
                        `${accentR}, ${accentG}, ${accentB}`);
                    
                    // Tracking-Variablen aktualisieren
                    currentColors = {
                        r: data.color_r,
                        g: data.color_g,
                        b: data.color_b
                    };
                }

                // Aktuelle Track-Daten aktualisieren
                currentTrack = {
                    track: data.track,
                    artist: data.artist,
                    album: data.album,
                    is_playing: data.is_playing,
                    album_cover: data.album_cover,
                    progress: data.progress || 0,
                    duration: data.duration || 0
                };
            }

            // Funktion zum Abrufen aktueller Track-Daten von der API
            function fetchCurrentTrack() {
                fetch('/api/current-track')
                    .then(response => response.json())
                    .then(data => updateDisplay(data))
                    .catch(error => console.error('Fehler beim Abrufen der Track-Informationen:', error))
                    .finally(() => {
                        // Nach 3 Sekunden erneut abfragen
                        setTimeout(fetchCurrentTrack, 3000);
                    });
            }

            // Initialisieren, sobald die Seite geladen ist
            document.addEventListener('DOMContentLoaded', () => {
                // Kleine Verzögerung vor dem ersten API-Aufruf
                setTimeout(fetchCurrentTrack, 1000);
            });
        </script>
    </head>
    <body>
        <!-- Hauptcontainer für abspielende Musik -->
        <div class="now-playing-container">
            <!-- Header-Bereich mit Label und Icon -->
            <div class="header-area">
                <!-- "Jetzt Läuft" Label - Du kannst diesen Text anpassen -->
                <div class="now-playing-label">JETZT LÄUFT</div>
                
                <!-- Musik-Icon (HTML-Entity für Musiknote) -->
                <div class="music-icon">♪</div>
            </div>
            
            <!-- Content-Bereich mit Album-Cover und Informationen -->
            <div class="content-area">
                <!-- Album-Cover-Artwork -->
                <div class="album-cover" style="background-image: url('{{ album_cover }}');"></div>
                
                <!-- Track-Informationen -->
                <div class="track-info">
                    <!-- Song-Informationen -->
                    <div class="track-title">{{ track }}</div>
                    <div class="artist-name">{{ artist }}</div>
                    <div class="album-name">{{ album }}</div>
                </div>
            </div>
        </div>

        <!-- Meldung, wenn keine Musik abgespielt wird -->
        <div class="inactive-message">
            <!-- Pausensymbol -->
            <div class="inactive-icon">⏸</div>
            
            <!-- Inaktiver Text -->
            <div>Kein Song wird abgespielt</div>
        </div>
    </body>
    </html>
    """