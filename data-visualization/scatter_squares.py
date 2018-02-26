import matplotlib.pyplot as plt

# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]
# Loop for generating data

x_values = list(range(1, 5001))
y_values = [x ** 2 for x in x_values] # squared numbers from the 5000 first items.

# x_values = list(range(1, 5001))
# y_values = [x ** 3 for x in x_values] # cubic numbers from the 5000 first items. Need to change c = y_values for (0, 0, 0.8) otherwise it won't print

# c is the color of the dot you
# A colormap is a series of colors in a gradient that moves from a starting to
# ending color. Colormaps are used in visualizations to emphasize a pattern
# in the data. For example, you might make low values a light color and high
# values a darker color.
# plt.scatter(x_values, y_values, c = (0, 0, 0.8), edgecolor = "none", s = 10)
plt.scatter(x_values, y_values, c = y_values, cmap = plt.cm.Blues, edgecolor = 'none', s = 10)

# Set chart title and axis labels
plt.title('Square Numbers', fontsize = 24)
plt.xlabel('Value', fontsize = 14)
plt.ylabel('Square of values', fontsize = 14)

# Set size of the tick labels
# The axis() function requires four values: the minimum and maximum values for the x-axis and
# the y-axis. Here, we run the x-axis from 0 to 1100 and the y-axis from 0 to 1,100,000
plt.axis([0, 1100, 0, 1100000])

# If we want to save the plot we call savefig
# Gonna be saved in the same folder if not specified
plt.savefig('squares_plot.png', bbox_inches = 'tight')

# load the graph in plot window
plt.show()
