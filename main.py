import pygame as pg
from pygame.locals import *
import menu
import sprites
import map
import tiles
from player import Player
from koopa import Koopa
from coins import Coin
from timer import Timer

SCREEN_WIDTH, SCREEN_HEIGHT = 744, 672


pg.init()

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("Super Mario Bros 1-1")
menu_sound = pg.mixer.Sound('sounds/main_theme.ogg')
menu_sound.play()

player = Player(100,552)
camera_x = 0
camera_y = 0

background = sprites.background.convert()
background_x = 0

show_menu = True
while show_menu:
    show_menu = menu.display_menu(screen)
    


# Game loop
running = True

animation_counter = 0

koopa = Koopa(100,100)
spawn_timer = 0 
spawn_interval = 5000 #5000 = 5 seconds
koopas = []
coin_points = [] #calling to points
clock = pg.time.Clock()
#timer = Timer()
#timer.start()
timer = pg.time.get_ticks()
game_time = 60000 #60 seconds = 1 min for players to play the game before hitting game over

while running:
    for event in pg.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                player.move_left()
            elif event.key == K_RIGHT:
                player.move_right()
            elif event.key == K_UP or event.key == K_SPACE:
                player.jump()
        elif event.type == KEYUP:
            if event.key == K_LEFT or event.key == K_RIGHT:
                player.stop_x_movement()

    animation_counter += 1
    player_position = player.update()
    camera_x = max(0, min(player.x - SCREEN_WIDTH // 2, background.get_width() - SCREEN_WIDTH))
    camera_y = max(0, min(camera_y, 672 - SCREEN_HEIGHT))
    scroll_speed = int(player.velocity_x * 2)

    if player.velocity_x > 0:
        background_x -= abs(player.velocity_x)
    background_x = max(0, background_x)

    if background_x < 0:
        background_x = 0
    elif background_x > background.get_width() - SCREEN_WIDTH:
        pass


        #DRAWS COLLIDERS BEHIND THE BACKGROUND
    for collider in map.floor_colliders:
        pg.draw.rect(screen, (0, 255, 0), pg.Rect(collider.x - camera_x, collider.y - camera_y, collider.w, collider.h))
    for collider in map.pipe_colliders:
        pg.draw.rect(screen, 
        (255, 0, 0), pg.Rect(collider.x - camera_x, collider.y - camera_y, collider.w, collider.h))
    for collider in map.brick_colliders:
    
        pg.draw.rect(screen, (88, 57, 39), pg.Rect(collider.x - camera_x, collider.y - camera_y, collider.w, collider.h))
    for colliders in map.mystery_colliders:
        pg.draw.rect(screen, (255, 255, 0), pg.Rect(collider.x - camera_x, collider.y - camera_y, collider.w, collider.h))
    
    screen.blit(background, (-camera_x,0))

        #DRAWS COLLIDERS ON TOP OF BACKGROUND TO VISUALIZE THEM
    """for collider in map.floor_colliders:
        pg.draw.rect(screen, (0, 255, 0), pg.Rect(collider.x - camera_x, collider.y - camera_y, collider.w, collider.h))
    for collider in map.pipe_colliders:
        pg.draw.rect(screen, (255, 0, 0), pg.Rect(collider.x - camera_x, collider.y - camera_y, collider.w, collider.h))
    for collider in map.brick_colliders:
        pg.draw.rect(screen, (88, 57, 39), pg.Rect(collider.x - camera_x, collider.y - camera_y, collider.w, collider.h))
    for collider in map.mystery_colliders:
        pg.draw.rect(screen, (255, 255, 0), pg.Rect(collider.x - camera_x, collider.y - camera_y, collider.w, collider.h))"""
    
        #DRAWS THE ACTUAL BRICKS FOR BRICK/MYSTERY_BOX COLLIDERS
    tiles.draw_bricks(screen, camera_x, camera_y, map.brick_colliders)
    tiles.draw_mystery_boxes(screen, camera_x, camera_y, map.mystery_colliders, animation_counter)

    player.check_collision(map.floor_colliders, map.pipe_colliders, map.brick_colliders, map.mystery_colliders)
    player.draw(screen, camera_x, camera_y)
    if player.y >= 775:
        end_sound = pg.mixer.Sound('sounds/death.wav')
        end_sound.play()
        menu_sound.stop()
        print("Mama Mia, you fell! Game Over!")
        pg.time.delay(int(end_sound.get_length() * 1000))
        running = False
    elif player.x >= 9525:
        win_sound = pg.mixer.Sound('sounds/stage_clear.wav')
        win_sound.play()
        menu_sound.stop()
        print("Congratulations, you won!")
        pg.time.delay(int(win_sound.get_length() * 1000))
        running = False

    #coins (still need to modify)
    """for coin in coin_points:
    
        if player.rect.colliderect(coin.rect):
            coin_sound = pg.mixer.Sound('sounds/coin.ogg')
            coin_sound.play()
            coin_points.remove(coin)
        coin.update()
        coin.draw(screen)"""


    #time for the game
    elapsed_time = pg.time.get_ticks() - timer
    if elapsed_time >= game_time:
        end_sound = pg.mixer.Sound('sounds/death.wav')
        end_sound.play()
        menu_sound.stop()
        print("You ran out of time! Game Over!")
        #timer = pg.time.get_ticks() 
        while pg.mixer.get_busy():
            pass
        running = False #this should stop the game


    #calling to koopas
    """spawn_timer += clock.tick()
    if spawn_timer >= spawn_interval:
        spawn_timer -= spawn_interval

        #spawn_koopa = Koopa(100,100)
        spawn_koopa = Koopa(800,535) #koopa spawn set to every 5 seconds on the very right side
        koopas.append(spawn_koopa)
        coin = Coin(700,350)
        coin_points.append(coin)

        
    for koopa in koopas:
        koopa.update()
        koopa.draw(screen)"""

    pg.display.flip()
    clock.tick(5000)
pg.quit()
