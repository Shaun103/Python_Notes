import pandas as pd
from datetime import datetime, timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates

plt.style.use('seaborn')
data = pd.read_csv('/Users/User/Desktop/Python/Python_MathPlotLib/chartData/timeseriesData.csv')

# _____________________________________________________

dates = [
    datetime(2019, 5, 24),
    datetime(2019, 5, 25),
    datetime(2019, 5, 26),
    datetime(2019, 5, 27),
    datetime(2019, 5, 28),
    datetime(2019, 5, 29),
    datetime(2019, 5, 30)
]

y = [0, 1, 3, 4, 6, 5, 7]

plt.plot_date(dates, y, linestyle='solid')
plt.gcf().autofmt_xdate()  # get current figure

date_format = mpl_dates.DateFormatter('%b, %d, %Y')  # documentation codes above

plt.gca().xaxis.set_major_formatter(date_format) # get current axis: Month, day, year

plt.tight_layout()
plt.show()

# _____________________________________________________


# price_date = data['Date']
# price_close = data['Close']

# data['Date'] = pd.to_datetime(data['Date'])  # converts time series to datetime
# data.sort_values('Date', inplace=True)       # sorts dates 

# plt.plot_date(price_date, price_close, linestyle='solid')

# plt.gcf().autofmt_xdate()  # get current figure

# plt.title('Bitcoin Prices')
# plt.xlabel('Date')
# plt.ylabel('Closing Price')

# plt.tight_layout()

# plt.show()