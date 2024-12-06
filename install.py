import PyInstaller.__main__
import platform

PyInstaller.__main__.run([
    'main.py',
    '--clean',
    '--add-data=Assets/*.ttf:Assets',
    '--add-data=Assets/Rooms/*:Assets/Rooms',
    '--add-data=Assets/images/*:Assets/images',
    '--add-data=Assets/objects/*:Assets/objects',
    '--add-data=Assets/sprites/*:Assets/sprites',
    '--add-data=Entities/*.json:Entities',
    '--add-data=Sounds/*:Sounds',
    '-nDangeresque'
])
