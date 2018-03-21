import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'sitka_weather_2014.csv'
# filename = 'sitka_weather_07-2014.csv'

# Get dates and high temperatures from file
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[0], '%Y-%m-%d')
        dates.append(current_date)
        # We convert the string to number to be read with matplotlib
        high = int(row[1])
        highs.append(high)

# for index, column_header in enumerate(header_row):
#     print(index, column_header)

 # Plot data.
fig = plt.figure(dpi = 128, figsize = (10, 6))
plt.plot(dates, highs, c = 'red')

# Format plot.
plt.title('Daily high temperatures - 2014', fontsize = 24)
# plt.title('Daily high temperatures, July 2014', fontsize = 24)
plt.xlabel('', fontsize = 16)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize = 16)
plt.tick_params(axis = 'both', which = 'major', labelsize = 16)

plt.show()
