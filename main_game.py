import pygame
from settings import Settings
import game_functions as gf
from player import PlayerShip
import controls as ctrl
from pygame.sprite import Group


def run_game():
    pygame.init()
    stg = Settings()

    screen = pygame.display.set_mode((stg.screen_width, stg.screen_height))
    clock = pygame.time.Clock()
    pygame.display.set_caption("Space Action Shooter")
    #bg_color = stg.bg_color

    p_shot = Group()
    alien_1 = Group()

    #initialize player character
    player = PlayerShip(stg, screen)

    while True:
        clock.tick(stg.fps)
        #screen.blit(stg.bg_img, stg.bg_rect)
        gf.bg_scroll(stg, screen)
        ctrl.check_events(stg, screen, player, p_shot)

        player.update()
        gf.p_shot_update(stg, screen, player, p_shot)
        gf.update_screen(stg, screen, player, p_shot)


run_game()