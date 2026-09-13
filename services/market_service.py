import yfinance as yf

def get_trending_stocks():
    try:
        symbols = ["AAPL", "TSLA", "MSFT", "NVDA", "AMZN", "META", "GOOGL"]
        
        # Download 2 days of data for all symbols at once
        data = yf.download(symbols, period="2d", interval="1d", progress=False)

        stocks = []
        
        # In a multi-ticker download, data['Close'] gives a DataFrame 
        # where the columns are the actual ticker symbols.
        if "Close" in data:
            close_data = data['Close']
        else:
            return []

        for sym in symbols:
            try:
                # Extract the specific stock and drop empty rows
                if sym in close_data:
                    series = close_data[sym].dropna()
                else:
                    continue
                
                if len(series) < 2: 
                    continue
                
                prev = float(series.iloc[-2])
                curr = float(series.iloc[-1])
                change_pct = round(((curr - prev) / prev) * 100, 2)
                
                stocks.append({
                    "symbol": sym,
                    "price": round(curr, 2),
                    "change_pct": change_pct,
                    "sentiment": "Bullish" if change_pct > 0 else "Bearish"
                })
            except Exception as e:
                print(f"Error parsing {sym}: {e}")
                continue
                
        # Sort by the highest momentum first
        return sorted(stocks, key=lambda x: x['change_pct'], reverse=True)
        
    except Exception as e:
        print("Market Data Error:", e)
        return []