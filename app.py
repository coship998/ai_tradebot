from flask import Flask, render_template, jsonify, request
from dotenv import load_dotenv

# Load environment variables (.env)
load_dotenv()

# Services
from services.stock_service import get_stock_history, get_current_price
from services.analysis_service import get_stock_analysis
from services.market_service import get_trending_stocks

app = Flask(__name__)


# -------------------- PAGES --------------------

@app.route('/')
def home():
    stocks = get_trending_stocks()
    return render_template('index.html', stocks=stocks)


@app.route('/stock/<symbol>')
def stock(symbol):
    symbol = symbol.upper()

    dates, prices = get_stock_history(symbol, "1mo")
    price = get_current_price(symbol)

    return render_template(
        'stock.html',
        symbol=symbol,
        dates=dates,
        prices=prices,
        price=price
    )


# -------------------- APIs --------------------

# 🔹 Live Price
@app.route('/api/price/<symbol>')
def api_price(symbol):
    price = get_current_price(symbol.upper())
    return jsonify({"price": price})


# 🔹 History (for chart)
@app.route('/api/history/<symbol>')
def api_history(symbol):
    period = request.args.get('period', '1mo')

    dates, prices = get_stock_history(symbol.upper(), period)

    return jsonify({
        "dates": dates,
        "prices": prices
    })


# 🔥 MAIN FULL ANALYSIS API
@app.route('/api/stock-analysis/<symbol>')
def api_stock_analysis(symbol):
    data = get_stock_analysis(symbol.upper())
    return jsonify(data)


# -------------------- RUN --------------------

if __name__ == '__main__':
    app.run(debug=True)