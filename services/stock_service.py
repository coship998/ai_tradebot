import yfinance as yf


# ---------- GET HISTORICAL DATA ----------
def get_stock_history(symbol, period="1mo"):
    try:
        data = yf.download(symbol, period=period, progress=False)

        if data is None or data.empty:
            return [], []

        # Fix MultiIndex if present
        if hasattr(data.columns, "levels"):
            data.columns = data.columns.get_level_values(0)

        if "Close" not in data.columns:
            return [], []

        close = data["Close"].dropna()

        dates = close.index.strftime('%Y-%m-%d').tolist()
        prices = [round(float(x), 2) for x in close.tolist()]

        return dates, prices

    except:
        return [], []


# ---------- GET CURRENT PRICE ----------
def get_current_price(symbol):
    try:
        stock = yf.Ticker(symbol)
        data = stock.history(period="1d")

        if data is None or data.empty:
            return None

        price = data["Close"].iloc[-1]

        return round(float(price), 2)

    except:
        return None