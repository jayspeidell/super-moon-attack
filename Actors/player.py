import pygame
from pygame.sprite import Sprite
from time import sleep

class PlayerShip(Sprite):
    def __init__(self, stg, screen):
        super().__init__()
        self.screen = screen
        self.stg = stg
        self.image = pygame.image.load('images/player_ship.png')

        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.rect.centery = self.screen_rect.centery
        self.rect.left = self.screen_rect.left + self.rect.width

        self.y_axis = float(self.rect.centery)
        self.x_axis = float(self.rect.left)


        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x_axis += self.stg.player_speed
        if self.moving_left and self.rect.left > 0:
            self.x_axis -= self.stg.player_speed
        if self.moving_up and self.rect.top >= 0:
            self.y_axis -= self.stg.player_speed
        if self.moving_down and self.rect.bottom <= self.screen_rect.bottom:
            self.y_axis += self.stg.player_speed

        self.rect.centery = self.y_axis
        self.rect.left = self.x_axis


    def blitme(self):

        self.screen.blit(self.image, self.rect)

    def kill_ship(self, stg, screen, stats, sb):
        stats.ships_left -= 1
        self.y_axis = self.screen_rect.centery
        self.x_axis = self.screen_rect.left + self.rect.width
        sb.prep_lives(stg, screen, stats)


    '''
    def revive_ship(self, stg):
        self.y_axis = self.screen_rect.centery
        self.center = self.screen_rect.left + self.rect.width
        stg.dead = True
    '''

