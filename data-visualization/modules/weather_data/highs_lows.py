import csv
from matplotlib import pyplot as plt
from datetime import datetime

# filename = 'death_valley_2014.csv'
filename = 'sitka_weather_2014.csv'
# filename = 'sitka_weather_07-2014.csv'

# Get dates and high temperatures from file
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        try:     
            current_date = datetime.strptime(row[0], '%Y-%m-%d')
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            # We convert the string to number to be read with matplotlib
            highs.append(high)
            lows.append(low)
            
# for index, column_header in enumerate(header_row):
#     print(index, column_header)

 # Plot data.
fig = plt.figure(dpi = 128, figsize = (10, 6))
# alpha parameter is there to make the lines appear lighter
plt.plot(dates, highs, c = 'red', alpha = 0.5)
plt.plot(dates, lows, c = 'blue', alpha = 0.5)

# we shade the difference between highs and lows
plt.fill_between(dates, highs, lows, facecolor = 'blue', alpha = 0.1)

# Format plot.
plt.title('Daily high and low temperatures - 2014', fontsize = 24)
# plt.title('Daily high temperatures, July 2014', fontsize = 24)
plt.xlabel('', fontsize = 16)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize = 16)
plt.tick_params(axis = 'both', which = 'major', labelsize = 16)

plt.show()
