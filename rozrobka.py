import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

stocks = "CROX"

df = yf.download(stocks,start='2020-01-01',end='2025-12-31')
df = df.reset_index()
df.columns = df.columns.get_level_values(0)
#print(df)

for column in df.columns:
    for value in df[column]:
        if value != value:
            print("The dataset contains missing values.")
            break

df["MA20"] = df["Close"].rolling(window=20).mean()
df["MA50"] = df["Close"].rolling(window=50).mean()

signals = []

for i in range(len(df)):
    if df["MA20"][i] > df["MA50"][i]:
        signals.append(1)
    elif df["MA20"][i] < df["MA50"][i]:
        signals.append(-1)
    else:
        signals.append(0)

df["Signal"] = signals

#print(df)

status = ["Hold"]

for i in range(1, len(df)):
    today_signal = df["Signal"][i]
    yesterday_signal = df["Signal"][i - 1]

    if today_signal == 1 and yesterday_signal != 1:
        status.append("BUY")
    elif today_signal == -1 and yesterday_signal != -1:
        status.append("SELL")
    else:
        status.append("Hold")

df["Status"] = status
#print(df)

buy_price = 0
profits = []

for i in range(len(df)):
    if df["Status"][i] == "BUY" and buy_price == 0:
        buy_price = df["Close"][i]
        profits.append(0)
    elif df["Status"][i] == "SELL" and buy_price != 0:
        profit = df["Close"][i] - buy_price
        profits.append(profit)
        buy_price = 0
    else:
        profits.append(0)

df["Profit"] = profits
print(df)
print(sum(df["Profit"]))







