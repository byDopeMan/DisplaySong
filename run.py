# Standardbibliotheken
import os
import subprocess
import sys
import threading
from datetime import datetime
from pathlib import Path

# Drittanbieter-Bibliotheken
import pkg_resources

# Eigene Module
from app.html import Sites
from app.utils import get_external_path
from app.gui_console import gui_console

VENV_DIR = Path(__file__).parent / "venv"

def write_crash_log(exc_type, exc_value, exc_traceback):
    log_dir = get_external_path("crash_logs")
    os.makedirs(log_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_path = os.path.join(log_dir, f"crash_{timestamp}.log")

    with open(log_path, "w", encoding="utf-8") as f:
        f.write("Uncaught exception:\n")
        import traceback
        traceback.gui_console.write_exception(exc_type, exc_value, exc_traceback, file=f)

    gui_console.write(f"Programm ist abgestürzt! Details im Log: {log_path}", "error")

def handle_exception(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return
    write_crash_log(exc_type, exc_value, exc_traceback)

def ensure_file(path, content=""):
    if not os.path.exists(path):
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

default_env = "CLIENT_ID=\nCLIENT_SECRET=\nREDIRECT_URI=http://127.0.0.1:5000/callback\nFLASK_SECRET_KEY=TnV0dGVuc29obg=="
default_bg = Sites.BACKGROUND
default_custom = Sites.CUSTOM

ensure_file(get_external_path(".env"), default_env)
ensure_file(get_external_path("background.txt"), default_bg)
ensure_file(get_external_path("custom.txt"), default_custom)

def install_requirements():
    req_path = Path(__file__).parent / "requirements.txt"
    if not req_path.exists():
        gui_console.write("⚠️ Keine requirements.txt gefunden.", "warning")
        return

    gui_console.write("🔍 Prüfe installierte Pakete...", "bold")

    missing = []

    with req_path.open() as f:
        for line in f:
            pkg = line.strip()
            if not pkg or pkg.startswith("#"):
                continue
            try:
                pkg_resources.require(pkg)
            except pkg_resources.DistributionNotFound:
                missing.append(pkg)
            except pkg_resources.VersionConflict:
                gui_console.write(f"⚠️ Versionskonflikt bei: {pkg} – wird neu installiert.", "debug")
                missing.append(pkg)

    if missing:
        gui_console.write(f"📦 Fehlen: {', '.join(missing)} – Installation startet...", "debug")
        subprocess.check_call([sys.executable, "-m", "pip", "install", *missing])
    else:
        gui_console.write("✅ Alle Pakete sind bereits installiert.", "success")

if __name__ == "__main__":
    from app import create_app
    from app.spotify_client import update_track_info
    if not getattr(sys, 'frozen', False):
        install_requirements()

    sys.excepthook = handle_exception
    app = create_app()

    threading.Thread(target=update_track_info, daemon=True).start()
    threading.Thread(target=lambda: app.run(host='127.0.0.1', port=5000, debug=False), daemon=True).start()

    gui_console.mainloop()