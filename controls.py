import pygame
import sys
from player_shot import PlayerShot


def fire_p_shot(stg, screen, player, p_shot):
    if len(p_shot) < stg.p_shots_allowed:
        new_shot = PlayerShot(stg, screen, player)
        p_shot.add(new_shot)

""" INPUTS """
def check_keydown_events(event, stg, screen, player, p_shot):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            player.moving_right = True
        elif event.key == pygame.K_LEFT:
            player.moving_left = True
        elif event.key == pygame.K_UP:
            player.moving_up = True
        elif event.key == pygame.K_DOWN:
            player.moving_down = True
        elif event.key == pygame.K_SPACE:
            fire_p_shot(stg, screen, player, p_shot)
        elif event.key == pygame.K_q:
            sys.exit()

def check_keyup_events(event, player):
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            player.moving_right = False
        elif event.key == pygame.K_LEFT:
            player.moving_left = False
        elif event.key == pygame.K_UP:
            player.moving_up = False
        elif event.key == pygame.K_DOWN:
            player.moving_down = False

def check_events(stg, screen, player, p_shot):
    #respond to inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, stg, screen, player, p_shot)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, player)
#        elif event.type == pygame.MOUSEBUTTONDOWN:
#            mouse_x, mouse_y = pygame.mouse.get_pos()
#            check_play_button(ai_settings, stats, screen, ship, aliens, bullets, play_button, mouse_x, mouse_y)

#def check_play_button(ai_settings, stats, screen, ship, aliens, bullets, play_button, mouse_x, mouse_y):
#    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
#    if button_clicked and not stats.game_active:
#        pygame.mouse.set_visible(False)
#        stats.reset_stats()
#        stats.game_active = True
#        aliens.empty()
#        bullets.empty()
#        create_fleet(ai_settings, screen, ship, aliens)
#        ship.center_ship()
        #sb.prep_ships()