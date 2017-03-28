import pygame
from pygame.sprite import Sprite

class PlayerShip(Sprite):
    def __init__(self, stg, screen):
        self.screen = screen
        self.stg = stg
        self.image = pygame.image.load('images/player_ship.png')

        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.y_axis = float(self.rect.bottom)
        self.center = float(self.rect.centerx)


        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.stg.player_speed
        if self.moving_left and self.rect.left > 0:
            self.center -= self.stg.player_speed
        if self.moving_up and self.rect.top >= 0:
            self.y_axis -= self.stg.player_speed
        if self.moving_down and self.rect.bottom <= self.screen_rect.bottom:
            self.y_axis += self.stg.player_speed

        self.rect.bottom = self.y_axis
        self.rect.centerx = self.center


    def blitme(self):
        self.screen.blit(self.image, self.rect)