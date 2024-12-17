from flask import Flask, request, jsonify
import random
import yfinance as yf
from flask_cors import CORS

app = Flask(__name__, static_url_path='/static')
CORS(app)

@app.route('/')
def hello():
    return "Welcome to Stock Portfolio Suggestion Engine"

# Updated stock options
stock_options = {
    'ethical': ['AAPL', 'MSFT', 'TSLA', 'ENPH', 'SBUX'],  # Companies with strong ESG practices
    'growth': ['NVDA', 'AMZN', 'META', 'SHOP', 'SNOW'],   # High-growth technology and e-commerce
    'index': ['VOO', 'SPY', 'VTI', 'IVV', 'QQQ', 'DIA'],  # Top-performing index funds
    'quality': ['PG', 'JNJ', 'PEP', 'COST', 'MSFT'],      # Stable companies with consistent performance
    'value': ['WMT', 'INTC', 'F', 'CVX', 'T'],            # Undervalued stocks with strong fundamentals
}


def fetch_stock_data(symbol):
    """
    Fetch stock details and historical data for a given symbol using yfinance.
    """
    stock = yf.Ticker(symbol)
    data = stock.history(period="5d")
    latest_price = data['Close'].iloc[-1] if not data.empty else 0

    # Convert weekly data index (Timestamp) to string
    weekly_data = {str(date): round(price, 2) for date, price in data['Close'].items()}

    return {
        "symbolName": symbol,
        "companyName": stock.info.get('longName', "N/A"),
        "latestPrice": round(latest_price, 2),
        "changePercentage": round(((data['Close'].iloc[-1] - data['Close'].iloc[-2]) / data['Close'].iloc[-2]) * 100, 2)
        if len(data) > 1 else 0,
        "weeklyData": weekly_data  # Keys converted to strings
    }


@app.route('/suggest', methods=['POST'])
def suggest_stocks():
    req_data = request.get_json()
    strategy_1 = req_data['strategy_1']
    amount = req_data['amount']

    resp_obj = {}
    stock_info = []

    options = random.sample(range(0, len(stock_options[strategy_1])), 3)

    for i, option in enumerate(options):
        perc = [0.36, 0.24, 0.4][i]
        symbol = stock_options[strategy_1][option]
        try:
            stock_data = fetch_stock_data(symbol)
            stock_data['investAmount'] = round(amount * perc, 2)
            stock_info.append(stock_data)
        except Exception as e:
            print(f"Error fetching data for {symbol}: {e}")
            return "failed", 500

    resp_obj['stock_info'] = stock_info
    return jsonify(resp_obj)

@app.route('/suggest2', methods=['POST'])
def suggest_stocks2():
    req_data = request.get_json()
    strategy_1 = req_data['strategy_1']
    strategy_2 = req_data['strategy_2']
    amount = req_data['amount']

    resp_obj = {}
    stock_info = []

    options = random.sample(range(0, len(stock_options[strategy_1])), 3)

    for i, option in enumerate(options):
        perc = [0.12, 0.18, 0.4][i]
        for strategy in [strategy_1, strategy_2]:
            symbol = stock_options[strategy][option]
            try:
                stock_data = fetch_stock_data(symbol)
                stock_data['investAmount'] = round(amount * perc, 2)
                stock_info.append(stock_data)
            except Exception as e:
                print(f"Error fetching data for {symbol}: {e}")
                return "failed", 500

    resp_obj['stock_info'] = stock_info
    return jsonify(resp_obj)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
