import csv
from matplotlib import pyplot as plt

filename = 'sitka_weather_07-2014.csv'

# Get high temperatures
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    highs = []
    for row in reader:
        # We convert the string to number to be read with matplotlib
        high = int(row[1])
        highs.append(high)

# for index, column_header in enumerate(header_row):
#     print(index, column_header)

 # Plot data.
fig = plt.figure(dpi = 128, figsize = (10, 6))
plt.plot(highs, c = 'red')

# Format plot.
plt.title('Daily high temperatures, July 2014', fontsize = 24)
plt.xlabel('', fontsize = 16)
plt.ylabel('Temperature (F)', fontsize = 16)
plt.tick_params(axis = 'both', which = 'major', labelsize = 16)

plt.show()
