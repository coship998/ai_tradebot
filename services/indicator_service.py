import pandas as pd

def get_indicators(close_series):
    if len(close_series) < 30: return None, None, None, None
    
    # RSI (Wilder's Smoothing)
    delta = close_series.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    rs = gain / loss
    rsi = round(float(100 - (100 / (1 + rs)).iloc[-1]), 2)
    
    # MACD
    exp1 = close_series.ewm(span=12, adjust=False).mean()
    exp2 = close_series.ewm(span=26, adjust=False).mean()
    macd = exp1 - exp2
    signal = macd.ewm(span=9, adjust=False).mean()
    
    # Bollinger Bands (NEW FEATURE for Volatility)
    sma20 = close_series.rolling(window=20).mean().iloc[-1]
    std20 = close_series.rolling(window=20).std().iloc[-1]
    upper_band = round(float(sma20 + (std20 * 2)), 2)
    lower_band = round(float(sma20 - (std20 * 2)), 2)
    
    return rsi, round(float(macd.iloc[-1]), 2), round(float(signal.iloc[-1]), 2), (upper_band, lower_band)