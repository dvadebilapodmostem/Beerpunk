import math
import pynput
from ursina import *

app = Ursina()

cube = Entity(model='sphere', texture='macrowawe.jpg', scale=2, collider='box')

def spin():
    cube.animate('rotation_y', cube.rotation_y+720, duration=5, curve=curve.in_out_expo)


cube.on_click = spin
EditorCamera()  # add camera controls for orbiting and moving the camera

app.run()