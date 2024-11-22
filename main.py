import math
from ursina import *

app = Ursina(development_mode=True, use_ingame_console=True)

data={}

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
        cam_movespeed=0.5
        


def update():
    if camera.z <= -20: camera.z += held_keys['+'] *20
    if camera.z >= -680: camera.z -= held_keys['-'] *20
    
    camera.y += held_keys['w'] *cam_movespeed
    camera.y -= held_keys['s'] *cam_movespeed
    
    camera.x += held_keys['d'] *cam_movespeed
    camera.x -= held_keys['a'] *cam_movespeed
 
MAPA = Entity(model='quad', texture='macrowawe.jpg', scale=(320,180),)


#EditorCamera()  # add camera controls for orbiting and moving the camera 

app.run()