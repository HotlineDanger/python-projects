import matplotlib.pyplot as plt

# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]
# Loop for generating data
x_values = list(range(1, 1001))
y_values = [x ** 2 for x in x_values]

plt.scatter(x_values, y_values, s = 100)

# Set chart title and axis labels
plt.title("Square Numbers", fontsize = 24)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Square of values", fontsize = 14)

# Set size of the tick labels
# The axis() function requires four values: the minimum and maximum values for the x-axis and
# the y-axis. Here, we run the x-axis from 0 to 1100 and the y-axis from 0 to 1,100,000
plt.axis([0, 1100, 0, 1100000])
plt.show()
