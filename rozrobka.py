import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

stocks = "CROX"

df = yf.download(stocks,start='2020-01-01',end='2025-12-31')
#print(df)




df["MA20"] = df["Close"].rolling(window=20).mean()
df"MA50"] = df["Close"].rolling(window=50).mean()








