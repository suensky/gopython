import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Tim Cook became CEO of Apple on August 24, 2011
start_date = "2011-08-24"
end_date = "2023-11-21"

# Downloading Apple stock data
aapl = yf.download('AAPL', start=start_date, end=end_date)

# Convert string dates to pandas.Timestamp
start_date_ts = pd.Timestamp(start_date)
end_date_ts = pd.Timestamp(end_date)

# Adjust dates to the nearest valid trading days
start_date_adj = aapl.loc[start_date_ts:end_date_ts].first_valid_index()
end_date_adj = aapl.loc[start_date_ts:end_date_ts].last_valid_index()

# Get the closing price for the adjusted start and end dates
start_price_point = aapl.loc[start_date_adj, 'Close']
current_price_point = aapl.loc[end_date_adj, 'Close']

# Plotting the closing price of Apple stock
plt.figure(figsize=(14,7))
plt.plot(aapl['Close'], label='AAPL Closing Price')

# Define a style for the background box
bbox_props = dict(boxstyle="round,pad=0.3", fc="yellow", ec="black", lw=2)

# Annotating with combined markers (price and date)
start_annotation = f'${start_price_point:.2f}\nStart: {start_date_adj.strftime("%Y-%m-%d")}'
current_annotation = f'${current_price_point:.2f}\nCurrent: {end_date_adj.strftime("%Y-%m-%d")}'

plt.scatter([mdates.date2num(start_date_adj)], [start_price_point], color='green')
plt.annotate(start_annotation, (mdates.date2num(start_date_adj), start_price_point), textcoords="offset points", xytext=(-15,10), ha='center', bbox=bbox_props)

plt.scatter([mdates.date2num(end_date_adj)], [current_price_point], color='red')
plt.annotate(current_annotation, (mdates.date2num(end_date_adj), current_price_point), textcoords="offset points", xytext=(-15,10), ha='center', bbox=bbox_props)

plt.title('Apple Stock Performance Since Tim Cook Became CEO')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid(True)
plt.show()
