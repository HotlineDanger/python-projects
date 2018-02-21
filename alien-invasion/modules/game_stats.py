class GameStats():
    """ Track statistics for Alien Invasion. """

    def __init__(self, ai_settings):
        """ Initialize Statistics. """
        self.ai_settings = ai_settings
        self.reset_stats()

        # Start alien-invasion in an inactivate state
        # To give use the opportunity to add a start button
        self.game_active = False

        # High score track never to be reset
        self.high_score = 0


    def reset_stats(self):
        """ Initialize stats that can change during the game. """
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

        
