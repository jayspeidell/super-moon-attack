import pygame

class Settings():

    def __init__(self):

        '''screen settings'''
        self.screen_width = 1000 #1366 768
        self.screen_height = 500
        self.fps = 120
        self.bg_color = (230, 230, 230)

        self.bg_img = pygame.image.load('images/stone.png')
        self.bg_img = pygame.transform.scale(self.bg_img, (self.screen_width, self.screen_height))
        self.bg_rect = self.bg_img.get_rect()
        self.bg_size = self.bg_img.get_size()

        self.bg_scroll_speed = 3
        self.bg_x, self.bg_y = 0, 0
        self.bg_x1, self.bg_y1 = self.bg_rect.width, 0

        '''ship attributes'''
        self.player_speed = 8

        '''player bullet level 1 attributes'''
        self.p_shot_speed = 8
        self.p_shots_allowed = 30
        self.p_shot_width = 15
        self.p_shot_height = 6
        self.p_shot_color = 0, 255, 26

        '''alien_1 attributes'''
        self.alien_1_speed = 5