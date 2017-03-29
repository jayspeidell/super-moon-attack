import pygame

class Button():
    def __init__(self, settings, screen):
        self.screen = screen
        self.image = pygame.image.load("images/play_button.png")

        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.rect.center = self.screen_rect.center

    def draw_button(self):
        self.screen.blit(self.image)