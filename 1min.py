import yfinance as yf
import pandas as pd
import ta

# 下載 1 分鐘比特幣資料（最多近7天）
btc = yf.Ticker("BTC-USD").history(period="7d", interval="1m")

# 確保是 Series
close = btc["Close"].squeeze()
high = btc["High"].squeeze()
low = btc["Low"].squeeze()

# RSI 指標
btc["RSI"] = ta.momentum.RSIIndicator(close=close).rsi()

# MACD 指標
macd = ta.trend.MACD(close=close)
btc["MACD"] = macd.macd()
btc["MACD_signal"] = macd.macd_signal()

# Ichimoku 雲層指標
# Ichimoku 需要較長時間資料，短期內可能會有 NaN 較多
ichimoku = ta.trend.IchimokuIndicator(high=high, low=low)
btc["Ichimoku_base"] = ichimoku.ichimoku_base_line()
btc["Ichimoku_conversion"] = ichimoku.ichimoku_conversion_line()
btc["Ichimoku_span_a"] = ichimoku.ichimoku_a()
btc["Ichimoku_span_b"] = ichimoku.ichimoku_b()

# 布林通道
boll = ta.volatility.BollingerBands(close=close)
btc["Bollinger_upper"] = boll.bollinger_hband()
btc["Bollinger_lower"] = boll.bollinger_lband()

# 輸出結果（尾端5筆）
print(btc.tail())

# 儲存成 CSV
btc.to_csv("btc_1min_technical_analysis.csv")
print("技術分析已儲存為 btc_1min_technical_analysis.csv")