import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Make a random walk and plot the points.
'''rw = RandomWalk()
rw.fill_walk()

plt.scatter(rw.x_values, rw.y_values, s = 15)
plt.show()'''

# Keep making new walks as long as the program is active
while True:
    # Make a random walk and plot the points
    rw = RandomWalk(50000)
    rw.fill_walk()

    # Set the size of the plotting window so it fits nicely on the screen.
    plt.figure(figsize = (10, 6))

    point_numbers = list(range(rw.num_points))
    # Coloring the points
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c = point_numbers, cmap = plt.cm.Blues, edgecolor = 'none', s = 1)

    # plotting the starting and ending point
    plt.scatter(0, 0, c = 'green', edgecolors = 'none', s = 100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c = 'red', cmap = plt.cm.Blues, edgecolors = 'none', s = 100)

    # Removing the axis
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = str(input("Make another walk ? (y/n): "))

    if keep_running == 'n':
        break
