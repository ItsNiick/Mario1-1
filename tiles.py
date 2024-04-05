import pygame as pg
import sprites

def draw_bricks(screen, camera_x, camera_y, brick_colliders):
    for collider in brick_colliders:
        screen.blit(sprites.tile_set, (collider.x - camera_x, collider.y - camera_y), sprites.BRICK)

def draw_mystery_boxes(screen, camera_x, camera_y, mystery_colliders, animation_counter):
    sprite_index = animation_counter // 400  # Adjust the divisor to control animation speed
    for collider in mystery_colliders:
        sprite = sprites.Q_BLOCK_CLOSED[sprite_index % len(sprites.Q_BLOCK_CLOSED)]
        screen.blit(sprites.tile_set, (collider.x - camera_x, collider.y - camera_y), sprite)