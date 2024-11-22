import math
import pynput
from ursina import *

app = Ursina(development_mode=True, use_ingame_console=True)

heightmap1 = Terrain(heightmap='heightmap.jpg',skip=1)
MAPA = Entity(model=heightmap1, texture='heightmap_texture.jpg', scale=(100,2,100),)


EditorCamera()  # add camera controls for orbiting and moving the camera

app.run()