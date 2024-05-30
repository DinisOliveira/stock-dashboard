# Stock Dashboard

This project is a Stock Dashboard built with Flask and Plotly. It fetches stock data from Yahoo Finance, displays individual stock prices, and provides a comparison of the top 10 stocks.

## Features

- Displays stock prices for the top 10 stocks.
- Provides detailed information about each stock.
- Comparison plot of the top 10 stock prices.
- Interactive plots with Plotly.

## Requirements

- Python 3.7 or higher
- Flask
- yfinance
- pandas
- plotly

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/stock-dashboard.git
    cd stock-dashboard
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

1. Start the Flask application:

    ```bash
    python webapp.py
    ```

2. Open your web browser and go to `http://127.0.0.1:5000/` to view the dashboard.

## Project Structure

- `webapp.py`: The main Flask application.
- `analysis.py`: Utility functions for fetching stock data and information.
- `templates/`: HTML templates for the Flask app.
  - `index.html`: The main dashboard page.
  - `comparison.html`: The comparison plot page.
  - `stock.html`: The individual stock detail page.
- `static/`: Static files (CSS).
  - `styles.css`: CSS file for styling the app.

## License

This project is licensed under the MIT License.
