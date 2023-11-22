import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Facebook (Meta Platforms, Inc.) IPO date: May 18, 2012
start_date = "2012-05-18"
end_date = "2023-11-21"

# Downloading Facebook (Meta Platforms, Inc.) stock data
fb = yf.download('META', start=start_date, end=end_date)  # Using the ticker 'META' for Meta Platforms, Inc.

# Convert string dates to pandas.Timestamp
start_date_ts = pd.Timestamp(start_date)
end_date_ts = pd.Timestamp(end_date)

# Adjust dates to the nearest valid trading days
start_date_adj = fb.loc[start_date_ts:end_date_ts].first_valid_index()
end_date_adj = fb.loc[start_date_ts:end_date_ts].last_valid_index()

# Get the closing price for the adjusted start and end dates
start_price_point = fb.loc[start_date_adj, 'Close']
current_price_point = fb.loc[end_date_adj, 'Close']

# Plotting the closing price of Facebook (Meta Platforms, Inc.) stock
plt.figure(figsize=(14,7))
plt.plot(fb['Close'], label='META Closing Price')

# Define a style for the background box
bbox_props = dict(boxstyle="round,pad=0.3", fc="yellow", ec="black", lw=2)

# Annotating with combined markers (price and date)
start_annotation = f'${start_price_point:.2f}\nIPO: {start_date_adj.strftime("%Y-%m-%d")}'
current_annotation = f'${current_price_point:.2f}\nCurrent: {end_date_adj.strftime("%Y-%m-%d")}'

plt.scatter([mdates.date2num(start_date_adj)], [start_price_point], color='green')
plt.annotate(start_annotation, (mdates.date2num(start_date_adj), start_price_point), textcoords="offset points", xytext=(-15,10), ha='center', bbox=bbox_props)

plt.scatter([mdates.date2num(end_date_adj)], [current_price_point], color='red')
plt.annotate(current_annotation, (mdates.date2num(end_date_adj), current_price_point), textcoords="offset points", xytext=(-15,10), ha='center', bbox=bbox_props)

plt.title('Facebook (Meta Platforms, Inc.) Stock Performance Since IPO')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid(True)
plt.show()
