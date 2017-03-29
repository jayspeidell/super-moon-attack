import pygame
from Settings.settings import Settings
import Game_Functions.game_functions as gf
from Actors.player import PlayerShip
import Interface.controls as ctrl
from pygame.sprite import Group
from Settings.stats import GameStats
from Interface.scoreboard import Scoreboard
from Interface.button import Button

def run_game():
    pygame.init()
    stg = Settings()
    stats = GameStats(stg)
    screen = pygame.display.set_mode((stg.screen_width, stg.screen_height))
    clock = pygame.time.Clock()
    pygame.display.set_caption("Super Moon Attack")
    #bg_color = stg.bg_color
    p_shot = Group()
    aliens_1 = Group()
    #initialize player character
    sb = Scoreboard(stg, screen, stats)
    button = Button(stg, screen)
    player = PlayerShip(stg, screen)

    gf.create_alien_1(stg, screen, aliens_1)

    while True:
        clock.tick(stg.fps)
        #screen.blit(stg.bg_img, stg.bg_rect)
        gf.bg_scroll(stg, screen)

        ctrl.check_events(stg, screen, stats, player, p_shot, sb, button, aliens_1)
        gf.alien_1_random(stg, screen, aliens_1)


        gf.p_shot_update(stg, screen, player, p_shot, aliens_1, stats)
        '''break order and put enemies at end. *arg will recieve list'''
        gf.update_aliens(stg, screen, player, p_shot, stats, sb, aliens_1)
        player.update()
        gf.update_aliens_1(stg, screen, aliens_1)

        gf.update_screen(stg, screen, player, p_shot, aliens_1, sb)




run_game()