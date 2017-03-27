import pygame
from player import PlayerShip
from alien_1 import AlienOne
from random import choice

def update_screen(stg, screen, player, p_shot, aliens_1, sb):
    player.blitme()
    aliens_1.draw(screen)

    sb.show_score()

    for p_shot in p_shot.sprites():
        p_shot.draw_p_shot()

    #if not stats.game_active:
    #    play_button.draw_button()
    # redraw screen with updates
    pygame.display.flip()

def p_shot_update(stg, screen, player, p_shot, aliens_1, stats):
    p_shot.update()
    collission_handling(stg, screen, player, p_shot, aliens_1, stats)
    #repop(ai_settings, screen, ship, aliens, bullets)

def collission_handling(stg, screen, player, p_shot, aliens_1, stats):
    screen_width = screen.get_rect()
    for shot in p_shot.copy():
        if shot.rect.left > screen_width.width:
            p_shot.remove(shot)
    collisions = pygame.sprite.groupcollide(p_shot, aliens_1, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.player_score += stg.alien_1_points * len(aliens)
            #sb.prep_score()

'''
def repop(ai_settings, screen, ship, aliens, bullets):
    if len(aliens) == 0:
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)
'''
'''
def update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets):
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets)
    check_aliens_bottom(ai_settings, stats, screen, sb, ship, aliens, bullets)
'''

def bg_scroll(stg, screen):
    stg.bg_x -= stg.bg_scroll_speed
    stg.bg_x1 -= stg.bg_scroll_speed
    screen.blit(stg.bg_img, (stg.bg_x, stg.bg_y))
    screen.blit(stg.bg_img, (stg.bg_x1, stg.bg_y1))
    if stg.bg_x < -stg.bg_rect.width:
        stg.bg_x = stg.bg_rect.width
    if stg.bg_x1 < -stg.bg_rect.width:
        stg.bg_x1 = stg.bg_rect.width


def create_alien_1(stg, screen, aliens_1):
    alien_1 = AlienOne(stg, screen)
    alien_width = alien_1.rect.width
    alien_height = alien_1.rect.height
    right_pos = screen.get_rect()
    right_pos = right_pos.width
    alien_1.x = right_pos #alien_width * 2  # + (2 * alien_width * alien_number)
    alien_1.rect.x = alien_1.x
    alien_1.rect.y = alien_height * 5 # + 2 * alien_height * row_number
    aliens_1.add(alien_1)

def alien_1_random(stg, screen, aliens_1):
    chance = choice(list(range(1,80)))
    if chance == 6:
        create_alien_1(stg, screen, aliens_1)


def update_aliens_1(stg, screen, aliens_1):
    aliens_1.update(stg, screen)