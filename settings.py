import pygame as pg
from math import *
pg.init()

DISPLAY_HEIGHT, DISPLAY_WIDTH = D_H, D_W = 900, 1200

DISPLAY = pg.display.set_mode((D_W, D_H))

vec3 = pg.Vector3
vec2 = pg.Vector2
rad = radians

clock = pg.time.Clock()
FPS = 60

