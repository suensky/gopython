import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Satya Nadella became CEO of Microsoft on February 4, 2014
start_date = "2014-02-04"
end_date = "2023-11-21"

# Downloading Microsoft stock data
msft = yf.download('MSFT', start=start_date, end=end_date)

# Convert string dates to pandas.Timestamp
start_date_ts = pd.Timestamp(start_date)
end_date_ts = pd.Timestamp(end_date)

# Adjust dates to the nearest valid trading days
start_date_adj = msft.loc[start_date_ts:end_date_ts].first_valid_index()
end_date_adj = msft.loc[start_date_ts:end_date_ts].last_valid_index()

# Get the closing price for the adjusted start and end dates
start_price_point = msft.loc[start_date_adj, 'Close']
current_price_point = msft.loc[end_date_adj, 'Close']

# Plotting the closing price of Microsoft stock
plt.figure(figsize=(14,7))
plt.plot(msft['Close'], label='MSFT Closing Price')

# Define a style for the background box
bbox_props = dict(boxstyle="round,pad=0.3", fc="yellow", ec="black", lw=2)

# Annotating the start and current prices and dates with a background box
plt.scatter([mdates.date2num(start_date_adj)], [start_price_point], color='green')
plt.annotate(f'${start_price_point:.2f} {start_date_adj.strftime("%Y-%m-%d")}', (mdates.date2num(start_date_adj), start_price_point), textcoords="offset points", xytext=(-15,10), ha='center', bbox=bbox_props)
# plt.annotate(f'Start: {start_date_adj.strftime("%Y-%m-%d")}', (mdates.date2num(start_date_adj), start_price_point), textcoords="offset points", xytext=(-15,-20), ha='center', bbox=bbox_props)

plt.scatter([mdates.date2num(end_date_adj)], [current_price_point], color='red')
plt.annotate(f'${current_price_point:.2f} {end_date_adj.strftime("%Y-%m-%d")}', (mdates.date2num(end_date_adj), current_price_point), textcoords="offset points", xytext=(-15,10), ha='center', bbox=bbox_props)
# plt.annotate(f'Current: {end_date_adj.strftime("%Y-%m-%d")}', (mdates.date2num(end_date_adj), current_price_point), textcoords="offset points", xytext=(-15,-20), ha='center', bbox=bbox_props)

plt.title('Microsoft Stock Performance Since Satya Nadella Became CEO')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid(True)
plt.show()
