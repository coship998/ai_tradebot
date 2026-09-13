import requests, os
from datetime import datetime, timedelta

def get_stock_news(symbol):
    try:
        token = os.getenv("FINNHUB_API_KEY")
        if not token: return []
        
        today = datetime.now()
        past = today - timedelta(days=10)
        url = f"https://finnhub.io/api/v1/company-news?symbol={symbol}&from={past.date()}&to={today.date()}&token={token}"
        
        data = requests.get(url, timeout=5).json()
        if not isinstance(data, list): return []
        
        return [{"headline": i["headline"], "source": i["source"], "url": i["url"]} for i in data[:5]]
    except:
        return []