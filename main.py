import math
from ursina import *

app = Ursina(development_mode=True, use_ingame_console=True)

Settings={}
Special_characters={}

#cursor
Cursor(texture='assets/textures/cursor_test',scale=(0.2,0.2))
mouse.visible=False
#importovat soubory=============================================
try:
    with open('Settings.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
                Settings_parts = line.strip().split(':')
                setting_name = Settings_parts[0]
                array = Settings_parts[1:]
                Settings[setting_name] = array
except FileNotFoundError:
    f=open('Settings.txt', 'x')

try:
    with open('Special_characters.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
                Special_characters_parts = line.strip().split(':')
                NPC_name = Special_characters_parts[0]
                array = Special_characters_parts[1:]
                Special_characters[NPC_name] = array
except FileNotFoundError:
    f=open('Special_characters.txt', 'x')
#importovat nastaveni==================================

with open('Settings.txt', 'a') as f:
    try:
        cam_movespeed=float(Settings['cam_movespeed'][0])
    except KeyError:
            f.write('cam_movespeed:1\n')
            cam_movespeed=1
    try:
        zoom_speed=float(Settings['zoom_speed'][0])
    except KeyError:
            f.write('zoom_speed:10\n')
            zoom_speed=10

#pohyb   
def move():
    if camera.z <= -30: camera.z += held_keys['+'] *zoom_speed
    if camera.z >= -900: camera.z -= held_keys['-'] *zoom_speed
    
    if camera.y <= 180: camera.y += held_keys['w'] *cam_movespeed
    if camera.y >= -180: camera.y -= held_keys['s'] *cam_movespeed
    
    if camera.x >= -320: camera.x -= held_keys['a'] *cam_movespeed
    if camera.x <= 320: camera.x += held_keys['d'] *cam_movespeed
#entity
MAP = Entity(model='quad', texture='assets/textures/macrowawe.jpg', scale=(640,360))
#tick
def update():
    move()

    

    
 


#EditorCamera() 



app.run()