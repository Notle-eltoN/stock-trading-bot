import os
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
import datetime

Base = declarative_base()
# Define a base class for your models
class StockPrice(Base):
    __tablename__ = 'stock_prices'
    id = Column(Integer, primary_key=True, autoincrement=True)
    symbol = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

# Portfolio Table
class Portfolio(Base):
    __tablename__ = 'portfolio'
    id = Column(Integer, primary_key=True, autoincrement=True)
    symbol = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)

# Use an absolute path for SQLite
current_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(current_dir, 'stock_data.db')
engine = create_engine(f'sqlite:///{db_path}')

# Create the tables
Base.metadata.create_all(engine)

print("Database and tables created successfully.")
