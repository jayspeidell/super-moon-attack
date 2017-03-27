import pygame
from pygame.sprite import Sprite

class PlayerShot(Sprite):

    def __init__(self, stg, screen, player):
        #create bullet onject
        super(PlayerShot, self).__init__()
        self.screen = screen

        #create bullet at (0,0) and correct its position
        self.rect = pygame.Rect(0, 0, stg.p_shot_width, stg.p_shot_height)
        self.rect.centery = player.rect.centery
        self.rect.right = player.rect.right

        #convert position to decimal value
        self.x = float(self.rect.x)

        self.color = stg.p_shot_color
        self.speed_factor = stg.p_shot_speed

    def update(self):

        #update position
        self.x += self.speed_factor

        #moves the bullets rectangle to the y position
        self.rect.x = self.x

    def draw_p_shot(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

