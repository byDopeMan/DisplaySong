# Standardbibliotheken
import os
import sys

# Drittanbieter-Bibliotheken
from pystray import Icon, Menu, MenuItem
from PIL import Image

from app.utils import get_absolute_path
from app.gui_console import gui_console

def open_selectionURL(icon, item):
    os.startfile("http://127.0.0.1:5000/select")

def on_restore(icon, item):
    gui_console.show()
    icon.visible = False

def on_restart(icon, item):
    icon.visible = False
    python = sys.executable
    os.execl(python, python, *sys.argv)

def on_exit(icon, item):
    icon.stop()
    os._exit(0)

def setup_tray():
    icon = Icon('DisplaySong Tray')
    icon.icon = Image.open(
        get_absolute_path('_internal/app.ico') if getattr(sys, 'frozen', False) else 'app.ico'
    )
    icon.menu = Menu(
        MenuItem("Get Console", lambda icon, item: gui_console.show()),
        MenuItem("Open Selection Page", open_selectionURL),
        Menu.SEPARATOR,
        MenuItem("Restart Program", on_restart),
        MenuItem("Close Program", on_exit),
    )

    icon.run()