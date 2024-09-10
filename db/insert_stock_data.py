import requests
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from create_db import StockPrice
import sys
sys.path.append('../')
from config.settings import ALPHA_VANTAGE_API_KEY  # Ensure you have your API key here
import io


# Fetch stock data
def fetch_stock_price(symbol):
    """
    Fetch real-time stock price from Alpha Vantage.
    
    :param symbol: Stock symbol (e.g., 'AAPL')
    :return: Dictionary with stock price and symbol
    """
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=1min&apikey={ALPHA_VANTAGE_API_KEY}&datatype=csv"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = pd.read_csv(io.StringIO(response.text))
        latest_data = data.iloc[0]  # Get the latest price
        return {
            'symbol': symbol,
            'price': float(latest_data['close']),
            'timestamp': pd.to_datetime(latest_data['timestamp'])
        }
    else:
        print(f"Error fetching data for {symbol}: {response.status_code}")
        return None

# Store stock data in the database
def store_stock_price(stock_data):
    """
    Store stock price data into the database.

    :param stock_data: Dictionary containing stock symbol, price, and timestamp
    :return: None
    """
    engine = create_engine('sqlite:///stock_data.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    new_price = StockPrice(symbol=stock_data['symbol'], price=stock_data['price'], timestamp=stock_data['timestamp'])
    session.add(new_price)
    session.commit()
    print(f"Stored data for {stock_data['symbol']} at {stock_data['price']}")

# Example usage
stock_data = fetch_stock_price('AAPL')
if stock_data:
    store_stock_price(stock_data)
