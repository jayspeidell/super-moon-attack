import pygame
from pygame.sprite import Sprite
from random import choice
import random

class AlienOne(Sprite):
    def __init__(self, stg, screen):
        super(AlienOne, self).__init__()
        self.screen = screen
        self.stg = stg
        self.image = pygame.image.load('images/alien_1.png')

        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.rect.centery = self.screen_rect.centery
        self.rect.left = self.screen_rect.right

        self.y_axis = float(self.rect.bottom)
        self.center = float(self.rect.centerx)

        self.y_dir = 1

    def update(self, stg, screen):
        self.y_var = choice(list(range(0, 50)))
        if self.rect.bottom > self.screen_rect.height:
            self.y_dir = self.y_dir * -1
        elif self.rect.top < 0:
            self.y_dir = self.y_dir * -1
        elif self.y_var == 3:
            self.y_dir = self.y_dir * -1

        '''
        self.x_dir = choice([1, -1])
        self.y_chance = choice([1, 2, 3, 4, 5])
        if self.y_chance < 4:
            self.y_dir = 0
        if self.y_chance < 5:
            self.y_dir = -1
        else:
            self.y_dir = 1
        '''
        self.y_axis += stg.alien_1_speed * self.y_dir
        self.center -= stg.bg_scroll_speed * 0.6 #(stg.bg_scroll_speed - self.y_dir * stg.alien_1_speed)

        self.rect.centerx = self.center
        self.rect.bottom = self.y_axis

    def blitme(self):
        #image, position. FIts the image inside the rectangle
        self.screen.blit(self.image, self.rect)