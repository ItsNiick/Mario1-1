import pygame as pg
from pygame.locals import *
import menu
import sprites
from player import Player
from koopa import Koopa
#from sounds import sound_effect
#from camera import Camera

SCREEN_WIDTH, SCREEN_HEIGHT = 744, 672

pg.init()

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("Super Mario Bros 1-1")
menu_sound = pg.mixer.Sound('sounds/main_theme.ogg')
menu_sound.play()

player = Player(100,552)
camera_x = 0
camera_y = 0
#camera = Camera(SCREEN_WIDTH, SCREEN_HEIGHT)

background = sprites.background.convert()
background_x = 0

show_menu = True
while show_menu:
    show_menu = menu.display_menu(screen)
    

# Game loop
running = True
#clock = pg.time.Clock() #call to the clock
#start_time = pg.time.get_ticks() 

#koopa
koopa = Koopa(100,100)
spawn_timer = 0 
spawn_interval = 5000 #5000 = 5 seconds
koopas = []
clock = pg.time.Clock()

while running:
    for event in pg.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                player.move_left()
            elif event.key == K_RIGHT:
                player.move_right()
            elif event.key == K_UP:
                player.jump()
        elif event.type == KEYUP:
            if event.key == K_LEFT or event.key == K_RIGHT:
                player.stop_x_movement()

    player_position = player.update()
    camera_x = max(0, min(camera_x, 10176 - SCREEN_WIDTH))
    camrea_y = max(0, min(camera_y, 672 - SCREEN_HEIGHT))
    #camera_x = camera_x - SCREEN_WIDTH // 2
    #camrea_y = camera_y - SCREEN_HEIGHT // 2
    camera_x = player.rect.x - SCREEN_WIDTH // 2
    camrea_y = player.rect.y - SCREEN_HEIGHT // 2
    #camera_x = max(0, min(player.rect.x - SCREEN_WIDTH // 2, 10176 - SCREEN_WIDTH))
    #camera_y = max(0, min(player.rect.y - SCREEN_HEIGHT // 2, 672 - SCREEN_HEIGHT))
    scroll_speed = int(player.velocity_x)
    background_x -= scroll_speed




    if player.velocity_x > 0:
        background_x -= abs(player.velocity_x)
    elif player.velocity_x < 0:
        background_x += abs(player.velocity_x)

    if player.velocity_x != 0:
        velocity_int = int(player.velocity_x)
        background.scroll(-velocity_int, 0)
    if background_x < 0:
        background_x = 0
    elif background_x > background.get_width() - SCREEN_WIDTH:
        background_x = background.get_width() - SCREEN_WIDTH

    #screen.blit(background, (-background_x,0), (camera_x, camera_y, SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(background, (-background_x,0))

    player.check_collision()
    player.draw(screen, camera_x, camera_y)



    #calling to koopas
    spawn_timer += clock.tick()
    if spawn_timer >= spawn_interval:
        spawn_timer -= spawn_interval

        #spawn_koopa = Koopa(100,100)
        spawn_koopa = Koopa(800,535) #koopa spawn set to every 5 seconds on the very right side
        koopas.append(spawn_koopa)
    for koopa in koopas:
        koopa.update()
        koopa.draw(screen)


    pg.display.flip()

pg.quit()