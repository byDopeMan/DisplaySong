from version import __version__

# Zerlege Version in 4 Teile, fehlende als 0 auffüllen
parts = __version__.split(".")
while len(parts) < 4:
    parts.append("0")
filever = tuple(int(p) for p in parts[:4])

content = f'''VSVersionInfo(
  ffi=FixedFileInfo(
    filevers={filever},
    prodvers={filever},
    mask=0x3f,
    flags=0x0,
    OS=0x40004,
    fileType=0x1,
    subtype=0x0,
    date=(0, 0)
  ),
  kids=[
    StringFileInfo(
      [
      StringTable(
        u'040904B0',
        [StringStruct(u'CompanyName', u'DisplaySong Inc.'),
        StringStruct(u'FileDescription', u'Display Your currently playing Track from Spotify via their API'),
        StringStruct(u'FileVersion', u'{__version__}'),
        StringStruct(u'InternalName', u'DisplaySong'),
        StringStruct(u'LegalCopyright', u'© 2025 DisplaySong Inc.'),
        StringStruct(u'OriginalFilename', u'DisplaySong.exe'),
        StringStruct(u'ProductName', u'DisplaySong'),
        StringStruct(u'ProductVersion', u'{__version__}')])
      ]), 
    VarFileInfo([VarStruct(u'Translation', [1033, 1200])])
  ]
)
'''

with open("version.txt", "w", encoding="utf-8") as f:
    f.write(content)

print(f"version.txt wurde erstellt mit Version {__version__}")
