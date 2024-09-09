import pandas as pd
from strategies.moving_average import moving_average_strategy
from strategies.rsi_strategy import rsi_strategy
from strategies.momentum import momentum_strategy

from config.settings import ALPHA_VANTAGE_API_KEY, DATABASE_URI, DEFAULT_STOCK_SYMBOLS, FETCH_INTERVAL

print(f"Using API Key: {ALPHA_VANTAGE_API_KEY}")
print(f"Database URI: {DATABASE_URI}")
print(f"Default Symbols: {DEFAULT_STOCK_SYMBOLS}")
print(f"Fetching stock data every {FETCH_INTERVAL} seconds.")

# Sample stock data (you would fetch this using an API)
data = pd.DataFrame({
    'Close': [150, 152, 151, 155, 157, 160, 162, 161, 159, 158]  # Sample stock prices
})

# Apply Moving Average Strategy
ma_data = moving_average_strategy(data)
print(ma_data[['Close', 'Short_SMA', 'Long_SMA', 'Position']])

# Apply RSI Strategy
rsi_data = rsi_strategy(data)
print(rsi_data[['Close', 'RSI', 'Signal']])

# Apply Momentum Strategy
momentum_data = momentum_strategy(data)
print(momentum_data[['Close', 'Momentum', 'Signal']])
