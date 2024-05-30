# stock_utils.py

import yfinance as yf
import plotly.express as px
import plotly.graph_objs as go
import plotly.io as pio
import pandas as pd



#def main():
#    print(fetch_stock_data("MSFT"))


def fetch_top_stocks():
    top_stocks = yf.Tickers('AAPL MSFT GOOGL AMZN META TSLA BRK-B JPM JNJ V')
    return top_stocks.tickers


def fetch_stock_data(symbols):
    data = {}
    for symbol in symbols:
        stock = yf.Ticker(symbol)
        data[symbol] = stock.history(period="1y")['Close']
    return pd.DataFrame(data)

def format_market_cap(market_cap):
    if market_cap >= 1e12:
        return f"${market_cap / 1e12:.2f} Trillion"
    elif market_cap >= 1e9:
        return f"${market_cap / 1e9:.2f} Billion"
    elif market_cap >= 1e6:
        return f"${market_cap / 1e6:.2f} Million"
    else:
        return f"${market_cap:.2f}"

def fetch_stock_info(symbol):
    stock = yf.Ticker(symbol)
    info = stock.info
    return {
        'name': info.get('longName', 'N/A'),
        'sector': info.get('sector', 'N/A'),
        'industry': info.get('industry', 'N/A'),
        'market_cap': format_market_cap(info.get('marketCap', 0)),
        'summary': info.get('longBusinessSummary', 'N/A')
        }


def create_stock_plot(data, symbol):
    fig = px.line(data, x=data.index, y=symbol, title=f'{symbol} Stock Prices')
    return fig


def create_comparison_plot(data):
    fig = go.Figure()
    for symbol in data.columns:
        fig.add_trace(go.Scatter(x=data.index, y=data[symbol], mode='lines', name=symbol))
    fig.update_layout(title=' ', xaxis_title='Date', yaxis_title='Stock Price')
    return fig

#if __name__ == "__main__":
#   main()