class GameStats():
    def __init__(self, stg):
        self.stg = stg
        #self.reset_stats()
        self.game_active = False

        self.player_score = 0
        self.game_level = 1

        self.ships_left = stg.lives


    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit
        self.player_score = 0

