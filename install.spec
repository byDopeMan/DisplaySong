# install.spec
# -- coding: utf-8 --

import os
import sys
sys.path.insert(0, os.path.abspath('.'))
from version import __version__

block_cipher = None

# Daten, die mit rein sollen: templates + .env (relativ zum Projektordner)
datas = [
    ('requirements.txt', '.'),
    ('app.ico', '.'),
]


a = Analysis(
    ['run.py'],
    pathex=['.'],
    binaries=[],
    datas=datas,
    hiddenimports=['dotenv'],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='DisplaySong',
    debug=False,
    bootloader_ignore_signals=False,
    strip=True,
    upx=True,
    console=False,
    icon='app.ico',
    version='version.txt'
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=True,
    upx=True,
    upx_exclude=[],
    name=f'DisplaySong[{__version__}]'
)