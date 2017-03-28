import pygame
from pygame.sprite import Sprite
from Weapons.weapons_settings import Weapons

class PlayerShot(Sprite):

    def __init__(self, stg, screen, player):
        #create bullet onject
        super(PlayerShot, self).__init__()

        weapon = Weapons()

        '''bullet attributes'''
        self.shot_speed = 8
        self.shots_allowed = 7
        self.shot_width = 15
        self.shot_height = 6
        self.shot_color = 0, 255, 26
        self.dmg = 5

        self.screen = screen

        #create bullet at (0,0) and correct its position
        self.rect = pygame.Rect(0, 0, self.shot_width, self.shot_height)
        self.rect.centery = player.rect.centery
        self.rect.right = player.rect.right

        #convert position to decimal value
        self.x = float(self.rect.x)

        self.color = self.shot_color
        self.speed_factor = self.shot_speed


    def update(self):

        #update position
        self.x += self.speed_factor

        #moves the bullets rectangle to the y position
        self.rect.x = self.x

    def draw_p_shot(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

