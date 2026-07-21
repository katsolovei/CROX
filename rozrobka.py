import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

stocks = "CROX"

df = yf.download(stocks,start='2020-01-01',end='2025-12-31')
#print(df)

for column in df.columns:
    for value in df[column]:
        if value != value:
            print("The dataset contains missing values.")
            break


df["MA20"] = df["Close"].rolling(window=20).mean()
df["MA50"] = df["Close"].rolling(window=50).mean()

df["Signal"] = 0

for i in range(len(df)):
    if df["MA20"][i] > df["MA50"][i]:
        df["Signal"][i] = 1
    elif df["MA20"][i] < df["MA50"][i]:
        df["Signal"][i] = -1







