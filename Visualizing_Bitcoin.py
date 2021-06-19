import pandas_datareader as web
import matplotlib.pyplot as plt

import datetime as dt

crypto_btc = "BTC"

currency = "USD"

start = dt.datetime(2021, 1, 1)
end = dt.datetime.now()

btc = web.DataReader(f"{crypto_btc}-{currency}", "yahoo", start, end)

eth = web.DataReader(f"ETH-{currency}", "yahoo", start, end)

print(btc)

#plt.plot(btc['High'])
#plt.show()

plt.title("BTC-ETH Visualizing")
plt.plot(btc["Close"], label="BTC")
plt.plot(eth["Close"], label="ETH")
plt.xlabel("Time")
plt.ylabel("Price")
plt.legend(loc="upper left")
plt.yscale("log")
plt.grid()
plt.show()