# app.py

from flask import Flask, render_template
from analysis import fetch_top_stocks, fetch_stock_data, fetch_stock_info, create_comparison_plot, create_stock_plot
import plotly.express as px
import plotly.graph_objs as go
import plotly.io as pio
import pandas as pd

app = Flask(__name__)



@app.route('/')
def index():
    stock_symbols = fetch_top_stocks()
    stock_data = fetch_stock_data(stock_symbols)
    comparison_plot = create_comparison_plot(stock_data)
    comparison_plot_html = pio.to_html(comparison_plot, full_html=False)
    return render_template('index.html', stocks=stock_symbols, comparison_plot=comparison_plot_html)

@app.route('/comparison')
def comparison():
    stock_symbols = fetch_top_stocks()
    stock_data = fetch_stock_data(stock_symbols)
    comparison_plot = create_comparison_plot(stock_data)
    comparison_plot_html = pio.to_html(comparison_plot, full_html=False)
    return render_template('comparison.html', comparison_plot=comparison_plot_html)

@app.route('/stock/<symbol>')
def stock(symbol):
    stock_data = fetch_stock_data([symbol])
    if symbol in stock_data.columns:
        stock_plot = create_stock_plot(stock_data, symbol)
        stock_plot_html = pio.to_html(stock_plot, full_html=False)
        stock_info = fetch_stock_info(symbol)
        return render_template('stock.html', stock_plot=stock_plot_html, symbol=symbol, stock_info=stock_info)
    else:
        return "Stock symbol not found", 404

if __name__ == '__main__':
    app.run(debug=True)
