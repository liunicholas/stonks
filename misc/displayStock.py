# Python 3.8.6
# matplotlib 3.3.3
# numpy 1.19.4
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from yfinance import *

#very short documentation
#https://pypi.org/project/yfinance/

def getData(stockName, start, end):
    stock = Ticker(stockName)
    hist = stock.history(start=start, end=end)

    print(hist)

    # dates = pd.to_datetime(hist.index, format='%Y-%m-%d %H:%M:%S.%f')
    # hist.set_index(dates,inplace=True)

    # print(hist)
    return hist

def displayStock(data, ticker):
    hist = data

    histNP = hist.to_numpy()
    #to get columns
    histNP = np.transpose(histNP)
    open = histNP[0]
    high = histNP[1]
    low = histNP[2]
    close = histNP[3]

    # print(histNP)
    fig = plt.figure(f"{ticker} stock price", figsize=(10, 4))
    plt1 = fig.add_subplot(111)
    plt1.title.set_text("stock price")
    plt1.plot(hist.index, open, color="yellow", label="open")
    plt1.plot(hist.index, high, color="green", label="high")
    plt1.plot(hist.index, low, color="red", label="low")
    plt1.plot(hist.index, close, color="orange", label="close")
    plt1.legend(loc='upper left')
    plt.show()

def main():
    ticker = "TSLA"
    start = "2020-01-01"
    end = "2020-12-30"
    hist = getData(ticker, start, end)

    displayStock(hist, ticker)

main()
