import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep

def check_events(ai_settings, screen, stats, sb, start_button, ship, aliens, bullets):
    """ Responds to keypresses and mouse events """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_start_button(ai_settings, screen, stats, sb, start_button, ship, aliens, bullets, mouse_x, mouse_y)

def check_start_button(ai_settings, screen, stats, sb, start_button, ship, aliens, bullets, mouse_x, mouse_y):
    """ Starts a new game when the player hits Start. """
    button_clicked = start_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active: # we do this check in order to avoid the button area to still be clickable (could reset the game while playing)
        # Reset the game settings
        ai_settings.initialize_dynamic_settings()

        # Hide the mouse cursor
        pygame.mouse.set_visible(False)

        # Reset the game statistics.
        stats.reset_stats()
        stats.game_active = True

        # Reset the Scoreboard images.
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        # Empty the lists of aliens and bullets
        aliens.empty()
        bullets.empty()

        # Create a new fleet and center the ship
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """ Responds to keypresses. """
    if event.key == pygame.K_RIGHT:
        # Move the ship to the right
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # Move the ship to the left
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        # If the user hits the key Q
        sys.exit()

def check_keyup_events(event, ship):
    """ Responds to key releases. """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, start_button):
    """ Update images on the screen and flip to the new screen. """
    # Set the background color for the game.
    # Redraw the screen during each pass through the loop
    screen.fill(ai_settings.bg_color)

    # Make the ship and alien appear on screen
    ship.blitme()

    # When you call draw() on a group, Pygame automatically draws each element
    # in the group at the position defined by its rect attribute.
    aliens.draw(screen)

    # Redraw all bullets behind ships and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # Draw the core information
    sb.show_score()

    # Draw the Start button if the game is inactive
    if not stats.game_active:
        start_button.draw_button()

    # Make the most recent drawn screen visible
    pygame.display.flip()


def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """ Update position of bullets and get rid of old bullets. """
    # Update bullet positions.
    bullets.update()

    # Get rid of the bullets that disappeared from the top of the screen.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    # Check for any bullets that have hit aliens
    # If so get of the bullet and the alien.
    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)

def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """ Responds to bullet/alien collision. """
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    #The new line we added loops through each bullet in the group bullets and then loops through each alien in the group aliens. Whenever the rects of a bullet and alien overlap, groupcollide() adds a key-value pair to the dictionary
    #it returns. The two True arguments tell Pygame whether to delete the bullets and aliens that have collided. (To make a high-powered bullet that’s able to travel to the top of the screen, destroying every alien in its
    #path, you could set the first Boolean argument to False and keep the second Boolean argument set to True. The aliens hit would disappear, but all bullets would stay active until they disappeared off the top of the screen.)
    #We pass the argument aliens in the call to update_bullets():
    if collisions:
        # We loop through the collisions dictionary to make sure we award points for each alien hit
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score() # Create a new image of the updated score.
        check_high_score(stats, sb) # we check if we reached a highscore.

    if len(aliens) == 0:
        # If the entire aliens fleet is estroyed, start a new level
        bullets.empty()
        ai_settings.increase_speed()
        # Increase level
        stats.level += 1
        sb.prep_level()

        create_fleet(ai_settings, screen, ship, aliens)

def fire_bullet(ai_settings, screen, ship, bullets):
    """ Fire a bullet if the limit of possible bullets in the screen has not been reached yet. """
    # create a new bullet and add it to the bullets group.
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def create_fleet(ai_settings, screen, ship, aliens):
    """ Create a full fleet of aliens. """
    # Create an alien and find the number of aliens in a row
    # The spacing between each alien is equal to one alien width

    # we create an alien before we perform calculations.
    # This alien won’t be part of the fleet, so
    # don’t add it to the group aliens. (this is just to retrieve the width of the alien)
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width

    number_aliens_x = get_number_aliens_x(ai_settings, alien_width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    # Create the fleet of aliens
    # The inner loop creates the aliens in one row. The outer loop
    # counts from 0 to the number of rows we want; Python will use the code for
    # making a single row and repeat it number_rows times.
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def get_number_aliens_x(ai_settings, alien_width):
    """ Determine the number of aliens that fit in a row. """
    available_space_x = ai_settings.screen_width - (2 * alien_width)
    number_aliens_x = int(available_space_x / (2 * alien_width))
    # The int() function above drops the decimal part of a number, effectively
    # rounding down. (This is helpful because we’d rather have a little extra
    # space in each row than an overly crowded row.)

    return number_aliens_x

def get_number_rows(ai_settings, ship_height, alien_height):
    """ Determine the number of rows of aliens that fits on the screen. """
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))

    return number_rows

    # To calculate the number of rows we can fit on the screen, we write
    # our available_space_y and number_rows calculations into the function get_
    # number_rows()
    # We use int() because we don’t want to create a partial row of aliens.

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """ Create an alien and place it in the row. """
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + (2 * alien_width) * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + (2 * alien.rect.height) * row_number
    # Add the alien to the group
    aliens.add(alien)

def update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """ Check if the fleet is at an edge and then update the positions of all Aliens in the fleet. """
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # Look for alien-ship collision
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)

    # Look for aliens hitting the bottom of the screen
    check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets)

def check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """ Check if any alien has reached the bottom of the screen. """
    screen_rect = screen.get_rect()

    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Treat it as ths same as if the ship got hit
            ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
            break


def check_fleet_edges(ai_settings, aliens):
    """ Respond appropriately if an alien has reached an edge. """
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    """ Drop the entire fleet and change its direction. """
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def check_high_score(stats, sb):
    """ Check if there is any new high score. """
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()

def ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """ Respond to ship being hit by alien. """
    if stats.ships_left > 0:
        # Decrement ships_left
        stats.ships_left -= 1

        # Update Scoreboard
        sb.prep_ships()

        # Empty the list of aliens and bullets
        aliens.empty()
        bullets.empty()

        # Create a new fleet and center the ship
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # Pause
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)
