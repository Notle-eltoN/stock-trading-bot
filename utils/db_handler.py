from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.settings import DATABASE_URI

engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

def store_trade(trade_data):
    """
    Store trade data in the database.

    :param trade_data: A dictionary containing trade information
    :return: None
    """
    # Assuming there's a Trade table defined elsewhere
    new_trade = Trade(**trade_data)
    session.add(new_trade)
    session.commit()
    
def fetch_portfolio():
    """
    Fetch the current portfolio from the database.

    :return: List of holdings (stocks and quantities)
    """
    # Assuming there's a Portfolio table defined elsewhere
    portfolio = session.query(Portfolio).all()
    return portfolio
