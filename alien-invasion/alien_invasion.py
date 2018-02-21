import pygame
import game_functions as gf

from settings import Settings
from ship import Ship
from pygame.sprite import Group
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button

def run_game():
    #Initialize game and create a screen object.
    #Initializes Background settings that pygame needs to work.
    pygame.init()
    ai_settings = Settings()
    # we create a display window called screen where we'll draw
    # all the elements of our game
    # the screen object is called a surface in pygame
    # Each element on the screen is called a surface (alien, ships)
    # When we activate the game loop, the surface is automatically
    # redrawn on every pass through the loop
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))

    pygame.display.set_caption(ai_settings.window_caption)

    # Make the start button
    start_button = Button(ai_settings, screen, "Start")

    # Create an instance to store game statistics and create a scoreboard
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Make a ship, a group of bullets and a group of aliens
    ship = Ship(screen, ai_settings)
    bullets = Group()
    aliens = Group()

    # We create the fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    #start the main loop for the game
    while True:
        # we check for any events (keypresses or mouse events)
        gf.check_events(ai_settings, screen, stats, sb, start_button, ship, aliens, bullets)
        # In the main loop, we always need to call check_events(), even if the game
        # is inactive. For example, we still need to know if the user presses Q to quit
        # the game or clicks the button to close the window

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
            # We update the aliens’ positions after the bullets have been updated,
            # because we’ll soon be checking to see whether any bullets hit any aliens
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, start_button)

run_game()
