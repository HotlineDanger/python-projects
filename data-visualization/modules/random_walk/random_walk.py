#!/usr/bin/python

from random import choice

class RandomWalk():
    """ A class to generate random walks. """

    def __init__(self, num_points = 5000):
        """ Initializes attributes of a walk. """

        self.num_points = num_points

        # All walks start at (0, 0)
        self.x_values = [0]
        self.y_values = [0]


    def fill_walk(self):
        """ Calculate all the points in the walk. """

        # Keep taking steps until the walk reaches the desired length
        while len(self.x_values) < self.num_points:
            # Decide which direction to go and how far to go in that direction
            # We use choice([1, -1]) to choose a value for x_direction,
            # which returns either 1 for right movement or '-1' for left
            x_direction = choice([1, -1])
            # Next, choice([0, 1, 2, 3, 4]) tells Python how far to move in that direction (x_distance) by randomly selecting an integer between 0 and 4.
            x_distance = choice([0, 1, 2, 3, 4])
            # we determine the length of each step in the x and y directions by multiplying the direction of movement by the distance
            # A positive result for x_step moves us right, a negative result moves us left, and 0 moves us vertically
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            # A positive result for y_step means move up, negative
            # means move down, and 0 means move horizontally. If the value of both
            # x_step and y_step are 0, the walk stops, but we continue the loop to prevent this
            y_step = y_direction * y_distance

            # Reject moves that go nowhere
            if x_step == 0 and y_step == 0:
                continue

            # calculate the next x and y values
            # To get the next x-value for our walk, we add the value in x_step to the
            # last value stored in x_values and do the same for the y-values
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            # Once we have these values, we append them to x_values and y_values.
            self.x_values.append(next_x)
            self.y_values.append(next_y)
