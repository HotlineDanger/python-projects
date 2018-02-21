import pygame.font
from pygame.sprite import Group

from modules.ship import Ship

class Scoreboard():
    """ A class to report the scoring information. """

    def __init__(self, ai_settings, screen, stats):
        """ Initialize scorekeepingattributes. """
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # Font settings for scoring information.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare the initial score images.
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships() # number of lives left to display on the screen

    def prep_score(self):
        """ Turn the score into a rendered image. """
        score = int(round(self.stats.score, -1))
        # The round() function normally rounds a decimal number to a set number of decimal places given as the second argument. However, if you pass
        # a negative number as the second argument, round() will round the value to
        # the nearest 10, 100, 1000,
        score_str = "{:,}".format(score) # format the score to a comma separated rounded number
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color) # To display the score clearly onscreen, we pass the screen’s background color to render() as well as a text color

        # Display the score at the top right of the screen
        # We’ll position the score in the upper-right corner
        # of the screen and have it expand to the left as the
        # score increases and the width of the number grows.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """ Turn the high score into a rendered image. """
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.ai_settings.bg_color)

        # Center the high score at the center of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        """ Turn the level into a rendered image. """
        level = str(self.stats.level)
        self.level_image = self.font.render(level, True, self.text_color, self.ai_settings.bg_color)

        # position the level below the score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        # Position the score image 10px below the score image
        self.level_rect.top = self.score_rect.bottom + 10

    def show_score(self):
        """ Draw scores to the screen. """
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)

        # Draw ships.
        self.ships.draw(self.screen)

    def prep_ships(self):
        """ Show how many ships are left. """
        self.ships = Group() # Empty group to hold the ships instance

        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.screen, self.ai_settings)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)
