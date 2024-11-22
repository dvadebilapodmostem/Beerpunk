import math
from ursina import *

app = Ursina(development_mode=True, use_ingame_console=True)

data={}

Cursor(texture='cursor_test')
mouse.visible=False

with open('data.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
            data_parts = line.strip().split(':')
            setting_name = data_parts[0]
            array = data_parts[1:]
            data[setting_name] = array

try:
    cam_movespeed=float(data['cam_movespeed'][0])
except KeyError:
    with open('data.txt', 'a') as f:
        f.write('cam_movespeed:0.5\n')
        cam_movespeed=1
        


def update():
    if camera.z <= -30: camera.z += held_keys['+'] *10
    if camera.z >= -1200: camera.z -= held_keys['-'] *10
    
    if camera.y <= 180: camera.y += held_keys['w'] *cam_movespeed
    if camera.y >= -180: camera.y -= held_keys['s'] *cam_movespeed
    
    if camera.x >= -320: camera.x -= held_keys['a'] *cam_movespeed
    if camera.x <= 320: camera.x += held_keys['d'] *cam_movespeed
 
MAPA = Entity(model='quad', texture='macrowawe.jpg', scale=(640,360))

#EditorCamera() 



app.run()