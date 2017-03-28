import pygame.font
from Actors.player import PlayerShip
from pygame.sprite import Group

class Scoreboard():

    def __init__(self, stg, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stg = stg
        self.stats = stats

        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None, 48)

        #initial score image
        self.prep_score()
        #self.prep_ships()

    def prep_score(self):
        score_str = "Score:  " + str(self.stats.player_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.stg.sb_color)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        self.prep_score()
        self.screen.blit(self.score_image, self.score_rect)

    '''
    def prep_ships(self):
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)
    '''