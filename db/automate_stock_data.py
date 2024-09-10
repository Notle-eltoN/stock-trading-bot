import schedule
import time
import requests
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from create_db import StockPrice  # Import your StockPrice model
import sys
sys.path.append('../')
from config.settings import ALPHA_VANTAGE_API_KEY  # Ensure you have your API key here
import io


# Create a session to interact with the database
engine = create_engine('sqlite:///stock_data.db')
Session = sessionmaker(bind=engine)
session = Session()

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

def store_stock_price(stock_data):
    """
    Store stock price data into the database.

    :param stock_data: Dictionary containing stock symbol, price, and timestamp
    :return: None
    """
    new_price = StockPrice(symbol=stock_data['symbol'], price=stock_data['price'], timestamp=stock_data['timestamp'])
    session.add(new_price)
    session.commit()
    print(f"Stored data for {stock_data['symbol']} at {stock_data['price']}")

def analyze_latest_prices(symbol):
    """
    Analyze the latest prices of a stock by calculating a moving average.
    """
    # Fetch the latest 10 stock prices for the symbol
    latest_prices = session.query(StockPrice).filter_by(symbol=symbol).order_by(StockPrice.timestamp.desc()).limit(10).all()
    
    if latest_prices:
        prices = [price.price for price in latest_prices]
        moving_average = sum(prices) / len(prices)
        print(f"Latest Moving Average for {symbol}: {moving_average}")
    else:
        print(f"No data available for {symbol}")

# Modify this function to fetch, store, and analyze data
def fetch_store_and_analyze():
    """
    Fetch stock prices, store them in the database, and analyze the latest prices for each symbol.
    """
    symbols = ['AAPL', 'GOOGL', 'TSLA']  # Add more symbols if needed
    for symbol in symbols:
        stock_data = fetch_stock_price(symbol)
        if stock_data:
            store_stock_price(stock_data)
            analyze_latest_prices(symbol)  # Perform analysis after storing

# Schedule the job to fetch, store, and analyze every minute
schedule.every(1).minutes.do(fetch_store_and_analyze)

# Keep running the schedule
while True:
    schedule.run_pending()
    time.sleep(1)

    