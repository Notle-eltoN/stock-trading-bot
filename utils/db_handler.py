from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.create_db import StockPrice, Portfolio
from sqlalchemy.exc import SQLAlchemyError
import datetime
import io

# Create the SQLite engine and session
engine = create_engine('sqlite:///db/stock_data.db')
Session = sessionmaker(bind=engine)
session = Session()

def store_stock_price(stock_data, session):
    """
    Store stock price data into the database.
    :param stock_data: Dictionary containing stock symbol, price, and timestamp
    :param session: SQLAlchemy session object
    :return: None
    """
    try:
        new_price = StockPrice(
            symbol=stock_data['symbol'],
            price=stock_data['price'],
            timestamp=stock_data.get('timestamp', datetime.datetime.utcnow())
        )
        session.add(new_price)
        session.commit()
        print(f"Stored data for {stock_data['symbol']} at {stock_data['price']}")
    except SQLAlchemyError as e:
        print(f"Error storing stock data for {stock_data['symbol']}: {e}")
        session.rollback()

def update_portfolio(session, symbol, quantity, trade_type='buy'):
    """
    Update portfolio based on buy/sell trade.
    :param session: SQLAlchemy session object
    :param symbol: Stock symbol (e.g., 'AAPL')
    :param quantity: Number of shares bought or sold
    :param trade_type: 'buy' or 'sell'
    :return: None
    """
    try:
        # Fetch current portfolio entry for the stock
        portfolio_entry = session.query(Portfolio).filter_by(symbol=symbol).first()

        if trade_type == 'buy':
            if portfolio_entry:
                portfolio_entry.quantity += quantity
            else:
                portfolio_entry = Portfolio(symbol=symbol, quantity=quantity)
                session.add(portfolio_entry)
        elif trade_type == 'sell':
            if portfolio_entry:
                portfolio_entry.quantity = max(0, portfolio_entry.quantity - quantity)
            else:
                print(f"Error: Trying to sell {quantity} shares of {symbol}, but no holdings exist.")

        session.commit()
        print(f"Portfolio updated: {symbol}, {trade_type}, quantity: {quantity}")
    except SQLAlchemyError as e:
        print(f"Error updating portfolio for {symbol}: {e}")
        session.rollback()
