import math
from ursina import *

app = Ursina(development_mode=True, use_ingame_console=True)

data={}


#cursor
Cursor(texture='cursor_test')
mouse.visible=False

with open('data.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
            data_parts = line.strip().split(':')
            setting_name = data_parts[0]
            array = data_parts[1:]
            data[setting_name] = array
#Deportovat nastaveni==================================
try:
    cam_movespeed=float(data['cam_movespeed'][0])
except KeyError:
    with open('data.txt', 'a') as f:
        f.write('cam_movespeed:1\n')
        cam_movespeed=1
try:
    zoom_speed=float(data['zoom_speed'][0])
except KeyError:
    with open('data.txt', 'a') as f:
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
MAP = Entity(model='quad', texture='macrowawe.jpg', scale=(640,360))
#tick
def update():
    move()
    

    
 


#EditorCamera() 



app.run()