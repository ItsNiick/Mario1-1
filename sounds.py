import pygame as pg
from os import path

pg.init()
pg.mixer.init(44100, 16, 2, 4096)

sounds_folder = path.join(path.dirname(__file__), 'sounds')

small_jump = pg.mixer.Sound(path.join(sounds_folder, 'small_jump.ogg'))