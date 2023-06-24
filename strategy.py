import time
import datetime as dt
import matplotlib.pyplot as plt
import yfinance as yf
plt.style.use("seaborn-v0_8-dark")

# plotting data

sma1 = 40
sma2 = 100

start = dt.datetime.now() - dt.timedelta(days=365*4)
end = dt.datetime.now()

data = yf.download('AMD', start=start, end=end)
data[f'SMA_{sma1}'] = data['Adj Close'].rolling(window=sma1).mean()
data[f'SMA_{sma2}'] = data['Adj Close'].rolling(window=sma2).mean()

'''
plt.plot(data['Adj Close'], label = "Share Price", color = 'black')
plt.plot(data[f'SMA_{sma1}'], label = f"SMA_{sma1}", color = 'orange')
plt.plot(data[f'SMA_{sma2}'], label = f"SMA_{sma2}", color = 'blue')
plt.legend(loc = 'upper left')
plt.show()
'''

# implement algorithmic strategy

buy_signals = []
sell_signals = []
buy_state = 0

for i in range(len(data)):
    if data[f'SMA_{sma1}'].iloc[i] > data[f'SMA_{sma2}'].iloc[i] and buy_state != 1:
        buy_signals.append(data['Adj Close'].iloc[i])
        sell_signals.append(float('nan'))
        buy_state = 1

    elif data[f'SMA_{sma1}'].iloc[i] < data[f'SMA_{sma2}'].iloc[i] and buy_state != -1:
        buy_signals.append(float('nan'))
        sell_signals.append(data['Adj Close'].iloc[i])
        buy_state = -1
    else:
        buy_signals.append(float('nan'))
        sell_signals.append(float('nan'))


data['Buy Signals'] = buy_signals
data['Sell Signals'] = sell_signals

print(data)

plt.plot(data['Adj Close'], label = "Share Price", color = "black", alpha = 0.5)
plt.plot(data[f'SMA_{sma1}'], label = f"SMA_{sma1}", color = 'orange', linestyle = "--")
plt.plot(data[f'SMA_{sma2}'], label = f"SMA_{sma2}", color = 'blue', linestyle = "--")
plt.scatter(data.index, data['Buy Signals'], label = "Buy Signal", marker = "^", color = "green")
plt.scatter(data.index, data['Sell Signals'], label = "Sell Signal", marker = "v", color = "red")
plt.legend(loc = "upper left")
plt.show()

