import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """ A Class to manage bullets fired from the ship """

    def __init__(self, ai_settings, screen, ship):
        """ Create a bullet object at the ship's current position """

        super(Bullet, self).__init__()
        self.screen = screen

        # Create a bullet rect at (0, 0) and then set correct position
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Store the bullet's position as a decimal value
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """ Move the bullet up the screen """
        # Update the decimal position of the bullet
        # The update() method manages the bullet’s position. When a bullet
        # is fired, it moves up the screen, which corresponds to a decreasing
        # y-coordinate value
        self.y -= self.speed_factor
        # Update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """ Draw the bullet to the screen. """
        pygame.draw.rect(self.screen, self.color, self.rect)

"""
At 1, we create the bullet’s rect attribute. The bullet is not based on an
image so we have to build a rect from scratch using the pygame.Rect() class.
This class requires the x- and y-coordinates of the top-left corner of the
rect, and the width and height of the rect. We initialize the rect at (0, 0),
but we’ll move it to the correct location in the next two lines, because the
bullet’s position is dependent on the ship’s position. We get the width and
height of the bullet from the values stored in ai_settings.
At 2, we set the bullet’s centerx to be the same as the ship’s rect.centerx.
The bullet should emerge from the top of the ship, so we set the top of the
bullet’s rect to match the top of the ship’s rect, making it look like the bullet
is fired from the ship w.
We store a decimal value for the bullet’s y-coordinate so we can make
fine adjustments to the bullet’s speed x. At 3, we store the bullet’s color
and speed settings in self.color and self.speed_factor.
"""
