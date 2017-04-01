import pygame
from Actors.alien_1 import AlienOne
from random import choice
from time import sleep
from Weapons.weapons_settings import Weapons

'''
Features to add:
0 Make collision detection generic
1 hitting alien hurts player
2 aliens can shoot
2a explode graphic
3 another type of alien
4 directories
5 main menu
6 mouse disappear
7 lives, health (hearts)
8 power ups
9 another type of bullet
10 stars
11 levels: background changes
12 obstacles

'''

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

'''add bullet attributes like speed and damage to class file'''

def p_shot_update(stg, screen, player, bullets, aliens_1, stats):
    bullets.update()
    collission_handling(stg, screen, player, bullets, aliens_1, stats)
    #repop(ai_settings, screen, ship, aliens, bullets)


'''
following two functions make collision handling and attack damage
generic, they work for any alien or weapon class
'''

def bullet_damage(bullets):
    for bullet in bullets:
        return bullet.dmg

def enemy_points(enemy):
    for i in enemy:
        return i.points

def collission_handling(stg, screen, player, bullets, enemy, stats):
    screen_width = screen.get_rect()
    dmg = bullet_damage(bullets)
    for shot in bullets.copy():
        if shot.rect.left > screen_width.width:
            bullets.remove(shot)
    attack_damage(stg, screen, player, bullets, enemy, stats, dmg)

def attack_damage(stg, screen, player, bullets, enemy, stats, dmg):
    collisions = pygame.sprite.groupcollide(bullets, enemy, True, False)
    points = enemy_points(enemy)
    if collisions:
        for aliens in collisions.values():
            for i in aliens:
                 #stats.player_score += stg.alien_1_points * len(aliens)
                i.hit_points -= dmg
                if i.hit_points <= 0:
                    enemy.remove(i)
                    stats.player_score += points * len(aliens)





def update_aliens(stg, screen, player, bullets, stats, sb, *enemies):
    enemies = list(enemies)
    for enemy in enemies:
        check_aliens_left(enemy)
        enemy.update(stg, screen)
        if pygame.sprite.spritecollideany(player, enemy):
            print("test")
            player.kill_ship(stg, screen, stats, sb)

"""hit ship, stats """
def ship_hit(stg, screen, player, bullets, stats, enemy):
    if stats.ships_left > 0:

        #sb.prep_sips()
        player.center_ship(stg, screen)


    '''
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)
    '''

def check_aliens_left(enemy):
    for baddy in enemy.sprites():
        if baddy.rect.right < 0:
            enemy.remove(baddy)


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