from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

# Define a base class for your models
Base = declarative_base()

# Define a StockPrice table schema
class StockPrice(Base):
    __tablename__ = 'stock_prices'
    id = Column(Integer, primary_key=True, autoincrement=True)
    symbol = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

# Create a SQLite engine (this creates the database file)
engine = create_engine('sqlite:///stock_data.db')

# Create the stock_prices table
Base.metadata.create_all(engine)

# Output
print("Database and table created successfully.")
