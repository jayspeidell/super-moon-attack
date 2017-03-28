import pygame
from Settings.settings import Settings
import Game_Functions.game_functions as gf
from Actors.player import PlayerShip
import Interface.controls as ctrl
from pygame.sprite import Group
from Actors.alien_1 import AlienOne
from Settings.stats import GameStats
from Settings.scoreboard import Scoreboard


def run_game():
    pygame.init()
    stg = Settings()
    stats = GameStats(stg)
    screen = pygame.display.set_mode((stg.screen_width, stg.screen_height))
    clock = pygame.time.Clock()
    pygame.display.set_caption("Super Moon Attack 0.3 Alpha")
    #bg_color = stg.bg_color
    sb = Scoreboard(stg, screen, stats)

    p_shot = Group()
    aliens_1 = Group()

    #initialize player character
    player = PlayerShip(stg, screen)
    gf.create_alien_1(stg, screen, aliens_1)

    while True:
        clock.tick(stg.fps)
        #screen.blit(stg.bg_img, stg.bg_rect)
        gf.bg_scroll(stg, screen)
        ctrl.check_events(stg, screen, player, p_shot)
        gf.alien_1_random(stg, screen, aliens_1)
        player.update()


        gf.p_shot_update(stg, screen, player, p_shot, aliens_1, stats)

        gf.update_aliens_1(stg, screen, aliens_1)
        gf.update_screen(stg, screen, player, p_shot, aliens_1, sb)


run_game()