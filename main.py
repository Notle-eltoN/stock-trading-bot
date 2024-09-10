
import time
import schedule
from utils.api_handler import fetch_alpha_vantage_data
from utils.db_handler import store_stock_price, update_portfolio
from strategies.moving_average import moving_average_strategy
from strategies.rsi_strategy import rsi_strategy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.create_db import StockPrice, Portfolio  # Import the models
from utils.visualization import plot_stock_data
from config.settings import ALPHA_VANTAGE_API_KEY
import io

# Global symbols list
symbols = ['TQQQ','SPXL','UDOW','NVDA','AAPL', 'GOOGL', 'TSLA']


# Create the SQLite engine and session
engine = create_engine('sqlite:///db/stock_data.db')
Session = sessionmaker(bind=engine)
session = Session()

def fetch_store_analyze(symbol):
    """
    Fetch live stock data, store it in the database, and perform analysis.
    :param symbol: Stock symbol to fetch and analyze (e.g., 'AAPL')
    """
    # Step 1: Fetch stock data using API
    stock_data = fetch_alpha_vantage_data(symbol)
    
    # Step 2: Store the stock data in the database
    if stock_data:
        store_stock_price(stock_data, session)

    # Step 3: Fetch the latest 10 stock prices from the database for analysis
    latest_prices = session.query(StockPrice).filter_by(symbol=symbol).order_by(StockPrice.timestamp.desc()).limit(10).all()

    if latest_prices:
        prices = [price.price for price in latest_prices]
        
        # Step 4: Apply Moving Average Strategy
        ma_signals = moving_average_strategy(prices)
        if ma_signals == 'buy':
            print(f"Buying {symbol}")
            update_portfolio(session, symbol, 10, 'buy')  # Example: Buy 10 shares
        elif ma_signals == 'sell':
            print(f"Selling {symbol}")
            update_portfolio(session, symbol, 10, 'sell')  # Example: Sell 10 shares

        # Step 5: Visualize stock data (optional)
        plot_stock_data(prices, title=f"{symbol} Stock Data")

def fetch_and_analyze_all_symbols():
    """
    Fetch, store, and analyze stock data for all symbols.
    """
    for symbol in symbols:
        fetch_store_analyze(symbol)

# Schedule the job to run every minute
schedule.every(1).minutes.do(fetch_and_analyze_all_symbols)

# Main loop to keep the bot running
if __name__ == "__main__":
    print("Starting Stock Trading Bot...")

    while True:
        schedule.run_pending()
        time.sleep(1)
