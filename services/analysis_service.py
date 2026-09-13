import yfinance as yf
from services.indicator_service import get_indicators
from services.news_service import get_stock_news
from services.ai_service import get_ai_analysis

def get_stock_analysis(symbol):
    res = {"symbol": symbol, "error": True}
    try:
        data = yf.download(symbol, period="6mo", progress=False)
        if hasattr(data.columns, "levels"): data.columns = data.columns.get_level_values(0)
        
        close, vol = data["Close"].dropna(), data["Volume"].dropna()
        if len(close) < 30: return res
        
        rsi, macd, sig, bb = get_indicators(close)
        
        curr_vol, avg_vol = int(vol.iloc[-1]), int(vol.mean())
        sma50 = close.rolling(50).mean().iloc[-1]
        trend = "Bullish" if close.iloc[-1] > sma50 else "Bearish"
        
        core_data = {
            "price": round(float(close.iloc[-1]), 2), "rsi": rsi, "macd": macd, "signal": sig,
            "bb_upper": bb[0], "bb_lower": bb[1], "trend": trend,
            "volume": curr_vol, "avg_volume": avg_vol
        }
        
        news = get_stock_news(symbol)
        core_data["ai"] = get_ai_analysis(symbol, core_data, news)
        core_data["news"] = news
        core_data["error"] = False
        return core_data
    except Exception as e:
        print(f"Analysis Error: {e}")
        return res