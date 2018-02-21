import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self, screen, ai_settings):
        """ Initialize the ship and its starting position """
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the ship image and gets its recent
        self.image = pygame.image.load('imgs/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value for the ship's center
        self.center = float(self.rect.centerx)
        # Movement Flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """ Update the ship's position based on the movement flag """
        # Checking if the ship is moving to the right and making sure
        # it stays within the screen size to avoid it disappearing to the right
        if self.moving_right and self.rect.right < self.screen_rect.right:
            # Update the ship's center value, not the rect
            self.center += self.ai_settings.ship_speed_factor

        # Checking if the ship is moving to the left and making sure
        # it stays within the screen size to avoid it disappearing to the left
        elif self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # Update rect object from self.center
        self.rect.centerx = self.center

    def blitme(self):
        """ Draw the ship at its current location """
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """ Center the ship on the screen. """
        self.center = self.screen_rect.centerx

"""
First, we import the pygame module. The __init__() method of Ship takes
two parameters: the self reference and the screen where we’ll draw the ship.
To load the image, we call pygame.image.load() u. This function returns a
surface representing the ship, which we store in self.image.
Once the image is loaded, we use get_rect() to access the surface’s rect
attribute v. One reason Pygame is so efficient is that it lets you treat game
elements like rectangles (rects), even if they’re not exactly shaped like rectangles.
Treating an element as a rectangle is efficient because rectangles
are simple geometric shapes. This approach usually works well enough that
no one playing the game will notice that we’re not working with the exact
shape of each game element.
When working with a rect object, you can use the x- and y-coordinates
of the top, bottom, left, and right edges of the rectangle, as well as the
center. You can set any of these values to determine the current position
of the rect.
When you’re centering a game element, work with the center, centerx, or
centery attributes of a rect. When you’re working at an edge of the screen,
work with the top, bottom, left, or right attributes. When you’re adjusting
the horizontal or vertical placement of the rect, you can just use the x and
y attributes, which are the x- and y-coordinates of its top-left corner. These
attributes spare you from having to do calculations that game developers
formerly had to do manually, and you’ll find you’ll use them often.

We’ll position the ship at the bottom center of the screen. To do so,
first store the screen’s rect in self.screen_rect w, and then make the value
of self.rect.centerx (the x-coordinate of the ship’s center) match the centerx
attribute of the screen’s rect x. Make the value of self.rect.bottom (the
y-coordinate of the ship’s bottom) equal to the value of the screen rect’s
bottom attribute. Pygame will use these rect attributes to position the ship
image so it’s centered horizontally and aligned with the bottom of the
screen.
At y we define the blitme() method, which will draw the image to the
screen at the position specified by self.rect.
"""
