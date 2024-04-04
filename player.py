import pygame as pg
from pygame.locals import *
import sprites

class Player:
    def __init__(self, x, y):
        self.x = x  # Initial x position
        self.y = y  # Initial y position
        self.width = 48  # Player width
        self.height = 48  # Player height
        self.velocity_x = 0  # Initial x velocity
        self.velocity_y = 0  # Initial y velocity
        self.is_jumping = False  # Flag to indicate if the player is jumping
        self.jump_speed = -0.1
        self.gravity = 0.2
        self.jump_height = y - 200
        self.animation_counter = 0
        self.animation_speed = 1000
        self.sprite = sprites.SMALL_MARIO_IDLE  # Initial sprite

    def update(self):
        # Update player position based on velocity
        self.x += self.velocity_x
        self.y += self.velocity_y

        if not self.is_jumping:
            self.velocity_y += self.gravity
            if self.velocity_y > 0.1:
                self.velocity_y = 0.1
        if self.is_jumping and self.y <= self.jump_height:
            self.is_jumping = False
            self.velocity_y = 0

        return self.x, self.y

    def jump(self):
        if not self.is_jumping:
            self.is_jumping = True
            self.velocity_y = self.jump_speed

    def move_left(self):
        self.velocity_x = -0.1  # Set horizontal velocity for moving left

    def move_right(self):
        self.velocity_x = 0.1  # Set horizontal velocity for moving right

    def stop_x_movement(self):
        self.velocity_x = 0  # Stop horizontal movement

    def stop_y_movement(self):
        self.velocity_y = 0  # Stop vertical movement

    def draw(self, screen, camera_x, camera_y):
        if self.is_jumping or self.y < 552 or self.y > 552:
            screen.blit(sprites.tile_set, (self.x - camera_x, self.y - camera_y), sprites.SMALL_MARIO_JUMP)
        elif self.velocity_x != 0:
            # Only update animation every few frames
            if self.animation_counter < self.animation_speed:
                sprite_index = (self.animation_counter // (self.animation_speed // 3)) % 3  # Calculate current frame index
                screen.blit(sprites.tile_set, (self.x - camera_x, self.y - camera_y), sprites.SMALL_MARIO_MOVE[sprite_index])
                self.animation_counter += 1
            else:
                self.animation_counter = 0  # Reset animation counter
        else:
            screen.blit(sprites.tile_set, (self.x - camera_x, self.y - camera_y), self.sprite)  # Draw player sprite on screen


    def check_collision(self):
        min_x = 0
        max_x = 10176
        min_y = 552

        if self.x < min_x:
            self.x = min_x
        elif self.x > max_x:
            self.x = max_x

        if self.y > min_y:
            self.y = min_y
            self.is_jumping = False
            self.velocity_y = 0