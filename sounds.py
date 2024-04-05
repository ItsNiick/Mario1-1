import pygame as pg
from os import path

pg.mixer.init()

class sound_effect:
    sounds_folder = path.join(path.dirname(__file__), 'sounds')

    small_jump = pg.mixer.Sound(path.join(sounds_folder, 'small_jump.ogg'))
    big_jump = pg.mixer.Sound(path.join(sounds_folder, 'big_jump.ogg'))
    brick_smash = pg.mixer.Sound(path.join(sounds_folder, 'brick_smash.ogg'))
    bump = pg.mixer.Sound(path.join(sounds_folder, 'bump.ogg'))
    coin = pg.mixer.Sound(path.join(sounds_folder, 'coin.ogg'))
    count_down = pg.mixer.Sound(path.join(sounds_folder, 'count_down.ogg'))
    death = pg.mixer.Sound(path.join(sounds_folder, 'death.wav'))
    flagpole = pg.mixer.Sound(path.join(sounds_folder, 'flagpole.wav'))
    kick = pg.mixer.Sound(path.join(sounds_folder, 'kick.ogg'))
    main_theme = pg.mixer.Sound(path.join(sounds_folder, 'main_theme.ogg'))
    main_theme_sped_up = pg.mixer.Sound(path.join(sounds_folder, 'main_theme_sped_up.ogg'))
    out_of_time = pg.mixer.Sound(path.join(sounds_folder, 'out_of_time.wav'))
    pipe = pg.mixer.Sound(path.join(sounds_folder, 'pipe.ogg'))
    powerup_appears = pg.mixer.Sound(path.join(sounds_folder, 'powerup_appears.ogg'))
    powerup = pg.mixer.Sound(path.join(sounds_folder, 'powerup.ogg'))
    stage_clear = pg.mixer.Sound(path.join(sounds_folder, 'stage_clear.wav'))
    stomp = pg.mixer.Sound(path.join(sounds_folder, 'stomp.ogg'))