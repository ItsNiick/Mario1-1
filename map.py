import pygame as pg
from sprites import level_1_1

map_width, map_height = level_1_1.size
TILE_SIZE = 48
VERTICAL_OFFSET = 0.5
PIPE_SIZE = 192

BLACK = (0,0,0,255)
RED = (255,0,0,255)
YELLOW = (255,255,0,255)
GRAY = (100,100,100,255)
GREEN = (100, 255, 100, 255)

floor_colliders = []
pipe_colliders = []
brick_colliders = []
mystery_colliders = []

for y in range(0, map_height):
    for x in range(0, map_width):
        pixel_color = level_1_1.getpixel((x, y))
        if pixel_color == BLACK:
            floor_colliders.append(pg.Rect(x * TILE_SIZE, (y + VERTICAL_OFFSET) * TILE_SIZE, TILE_SIZE, TILE_SIZE))
        elif pixel_color == RED:
            pipe_rect = pg.Rect(x * TILE_SIZE, (y + VERTICAL_OFFSET) * TILE_SIZE, TILE_SIZE * 2, PIPE_SIZE)
            pipe_colliders.append(pipe_rect)
            #pipe_colliders.append(pg.Rect(x * TILE_SIZE, (y + VERTICAL_OFFSET) * TILE_SIZE, TILE_SIZE, PIPE_SIZE))
            #pipe_colliders.append(pg.Rect((x + 1) * TILE_SIZE, (y + VERTICAL_OFFSET) * TILE_SIZE, TILE_SIZE, PIPE_SIZE))
        elif pixel_color == GRAY:
            brick_colliders.append(pg.Rect(x * TILE_SIZE, (y + VERTICAL_OFFSET) * TILE_SIZE, TILE_SIZE, TILE_SIZE))
        elif pixel_color == YELLOW or pixel_color == GREEN:
            mystery_colliders.append(pg.Rect(x * TILE_SIZE, (y + VERTICAL_OFFSET) * TILE_SIZE, TILE_SIZE, TILE_SIZE))
