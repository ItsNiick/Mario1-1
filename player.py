import pygame as pg
from pygame.locals import *
import sprites

class Player:
    def __init__(self, x, y):
        self.x = x  # Initial x position
        self.y = y  # Initial y position
        self.width = 48  # Player width
        self.height = 48  # Player height

        self.is_jumping = False  # Flag to indicate if the player is jumping
        self.jump_speed = -0.5
        self.gravity = 1
        self.jump_height = 250
        self.can_jump = True
        self.initial_jump_y = 0

        self.velocity_x = 0  # Initial x velocity
        self.velocity_y = 0  # Initial y velocity
        
        self.animation_counter = 0
        self.animation_speed = 1000
        self.sprite = sprites.SMALL_MARIO_IDLE  # Initial sprite

        self.rect = pg.Rect(x, y, self.width, self.height)

    def update(self):
        # Update player position based on velocity
        self.x += self.velocity_x
        self.y += self.velocity_y

        # Update player collision rectangle
        self.rect.x = self.x
        self.rect.y = self.y

        if not self.is_jumping:
            self.velocity_y += self.gravity
            if self.velocity_y > 0.35:
                self.velocity_y = 0.35
        #if self.is_jumping and self.y <= self.jump_height:
        if self.is_jumping and self.y <= self.initial_jump_y - self.jump_height:
            self.is_jumping = False
            self.velocity_y = 0
            self.can_jump = True


        return self.x, self.y

    def jump(self):
        if self.can_jump and self.velocity_y == 0:
            self.is_jumping = True
            self.initial_jump_y = self.y
            self.velocity_y = self.jump_speed
            self.can_jump = False
            jump_sound = pg.mixer.Sound('sounds/big_jump.ogg')
            jump_sound.play()

    def move_left(self):
        self.velocity_x = -0.3  # Set horizontal velocity for moving left

    def move_right(self):
        self.velocity_x = 0.3  # Set horizontal velocity for moving right

    def stop_x_movement(self):
        self.velocity_x = 0  # Stop horizontal movement

    def stop_y_movement(self):
        self.velocity_y = 0  # Stop vertical movement

    def draw(self, screen, camera_x, camera_y):
        if self.is_jumping:
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


    def check_collision(self, floor_colliders, pipe_colliders, brick_colliders, mystery_colliders):
        for collider in floor_colliders:
            if self.rect.colliderect(collider):
                self.rect.bottom = collider.top
                self.is_jumping = False
                self.velocity_y = 0

        for collider in pipe_colliders:
            if self.rect.colliderect(collider):
                dx = self.rect.centerx - collider.centerx
                dy = self.rect.centery - collider.centery

                if abs(dx) > abs(dy):  # Horizontal collision
                    if dx > 0:  # Moving right; Hit the left side of the pipe
                        self.rect.right = collider.left
                    else:  # Moving left; Hit the right side of the pipe
                        self.rect.left = collider.right
                    self.velocity_x = 0
                else:  # Vertical collision
                    if dy > 0:  # Moving down; Hit the top side of the pipe
                        self.rect.bottom = collider.top
                        self.is_jumping = False
                        self.velocity_y = 0
                    else:  # Moving up; Hit the bottom side of the pipe
                        self.rect.top = collider.bottom
                        self.velocity_y = 0
        
        for collider in brick_colliders:
            if self.rect.colliderect(collider):
                dx = self.rect.centerx - collider.centerx
                dy = self.rect.centery - collider.centery
                if abs(dx) > abs(dy):  # Horizontal collision
                    if dx > 0:  # Moving right; Hit the left side of the brick
                        self.rect.right = collider.left
                    else:  # Moving left; Hit the right side of the brick
                        self.rect.left = collider.right
                else:  # Vertical collision
                    if dy > 0:  # Moving down; Hit the top side of the brick
                        self.rect.bottom = collider.top
                        self.is_jumping = False
                    else:  # Moving up; Hit the bottom side of the brick
                        self.rect.top = collider.bottom
                        self.velocity_y = 0
                
        for collider in mystery_colliders:
            if self.rect.colliderect(collider):
                dx = self.rect.centerx - collider.centerx
                dy = self.rect.centery - collider.centery
                if abs(dx) > abs(dy):  # Horizontal collision
                    if dx > 0:  # Moving right; Hit the left side of the brick
                        self.rect.right = collider.left
                    else:  # Moving left; Hit the right side of the brick
                        self.rect.left = collider.right
                else:  # Vertical collision
                    if dy > 0:  # Moving down; Hit the top side of the brick
                        self.rect.bottom = collider.top
                        self.is_jumping = False
                    else:  # Moving up; Hit the bottom side of the brick
                        self.rect.top = collider.bottom
                        self.velocity_y = 0