import time
import datetime as dt
import matplotlib.pyplot as plt
import yfinance as yf

plt.style.use("seaborn-v0_8-dark")

sma1 = 30
sma2 = 100

start = dt.datetime.now() - dt.timedelta(days=365*4)
end = dt.datetime.now()

data = yf.download('GOOG', start=start, end=end)
data[f'SMA_{sma1}'] = data['Adj Close'].rolling(window=sma1).mean()
data[f'SMA_{sma2}'] = data['Adj Close'].rolling(window=sma2).mean()


plt.plot(data['Adj Close'], label = "Share Price", color = 'black')
plt.plot(data[f'SMA_{sma1}'], label = f"SMA_{sma1}", color = 'blue')
plt.plot(data[f'SMA_{sma2}'], label = f"SMA_{sma2}", color = 'orange')
plt.legend(loc = 'upper left')
plt.show()

print(plt.style.available)