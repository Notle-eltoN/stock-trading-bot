from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from create_db import StockPrice

def get_latest_stock_prices(symbol, limit=10):
    """
    Get the latest stock prices for a given symbol.
    
    :param symbol: Stock symbol (e.g., 'AAPL')
    :param limit: Number of latest records to fetch
    :return: List of stock prices
    """
    engine = create_engine('sqlite:///stock_data.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    
    return session.query(StockPrice).filter_by(symbol=symbol).order_by(StockPrice.timestamp.desc()).limit(limit).all()

def calculate_moving_average(prices):
    """
    Calculate the moving average from a list of prices.
    
    :param prices: List of stock prices
    :return: Moving average of prices
    """
    if prices:
        return sum([price.price for price in prices]) / len(prices)
    return None

# Example usage
latest_prices = get_latest_stock_prices('AAPL', limit=10)
moving_average = calculate_moving_average(latest_prices)
print(f"Latest Moving Average for AAPL: {moving_average}")
