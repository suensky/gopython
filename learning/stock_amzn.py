import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Andy Jassy became CEO of Amazon on July 5, 2021
start_date = "2021-07-05"
end_date = "2023-11-21"

# Downloading Amazon stock data
amzn = yf.download('AMZN', start=start_date, end=end_date)

# Convert string dates to pandas.Timestamp
start_date_ts = pd.Timestamp(start_date)
end_date_ts = pd.Timestamp(end_date)

# Adjust dates to the nearest valid trading days
start_date_adj = amzn.loc[start_date_ts:end_date_ts].first_valid_index()
end_date_adj = amzn.loc[start_date_ts:end_date_ts].last_valid_index()

# Get the closing price for the adjusted start and end dates
start_price_point = amzn.loc[start_date_adj, 'Close']
current_price_point = amzn.loc[end_date_adj, 'Close']

# Plotting the closing price of Amazon stock
plt.figure(figsize=(14,7))
plt.plot(amzn['Close'], label='AMZN Closing Price')

# Define a style for the background box
bbox_props = dict(boxstyle="round,pad=0.3", fc="yellow", ec="black", lw=2)

# Annotating with combined markers (price and date)
start_annotation = f'${start_price_point:.2f}\nStart: {start_date_adj.strftime("%Y-%m-%d")}'
current_annotation = f'${current_price_point:.2f}\nCurrent: {end_date_adj.strftime("%Y-%m-%d")}'

plt.scatter([mdates.date2num(start_date_adj)], [start_price_point], color='green')
plt.annotate(start_annotation, (mdates.date2num(start_date_adj), start_price_point), textcoords="offset points", xytext=(-15,10), ha='center', bbox=bbox_props)

plt.scatter([mdates.date2num(end_date_adj)], [current_price_point], color='red')
plt.annotate(current_annotation, (mdates.date2num(end_date_adj), current_price_point), textcoords="offset points", xytext=(-15,10), ha='center', bbox=bbox_props)

plt.title('Amazon Stock Performance Since Andy Jassy Became CEO')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid(True)
plt.show()
