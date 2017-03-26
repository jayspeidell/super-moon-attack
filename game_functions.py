import pygame
from player import PlayerShip

def update_screen(stg, screen, player, p_shot):
    # it's refreshing the screen color each cycle
    #screen.fill(stg.bg_color)
    player.blitme()
    #aliens.draw(screen)

    #sb.show_score()

    for p_shot in p_shot.sprites():
        p_shot.draw_p_shot()

    #if not stats.game_active:
    #    play_button.draw_button()
    # redraw screen with updates
    pygame.display.flip()

def p_shot_update(stg, screen, player, p_shot):
    p_shot.update()
    collission_handling(stg, screen, player, p_shot)
    #repop(ai_settings, screen, ship, aliens, bullets)

def collission_handling(stg, screen, player, p_shot):
    for shot in p_shot.copy():
        if shot.rect.bottom <= 0:
            p_shot.remove(shot)
'''
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
'''
def repop(ai_settings, screen, ship, aliens, bullets):
    if len(aliens) == 0:
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)

def update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets):
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets)
    check_aliens_bottom(ai_settings, stats, screen, sb, ship, aliens, bullets)

def bg_scroll(stg, screen):
    stg.bg_y += stg.bg_scroll_speed
    stg.bg_y1 += stg.bg_scroll_speed
    screen.blit(stg.bg_img, (stg.bg_x, stg.bg_y))
    screen.blit(stg.bg_img, (stg.bg_x1, stg.bg_y1))
    if stg.bg_y > stg.bg_rect.height:
        stg.bg_y = -stg.bg_rect.height
    if stg.bg_y1 > stg.bg_rect.height:
        stg.bg_y1 = -stg.bg_rect.height


