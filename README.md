# Stock Trading Bot

This is an automated stock trading bot built with Python that fetches real-time stock price data, stores it in a database, performs technical analysis (like moving average and RSI strategies), and updates a portfolio based on buy/sell signals. The bot uses the Alpha Vantage API for fetching stock prices and SQLite for storing data.

## Features

- **Fetch real-time stock data** from Alpha Vantage API
- **Store stock price data** in an SQLite database
- **Implement technical analysis** such as Moving Averages and RSI
- **Automated trading strategies** based on technical indicators
- **Portfolio management**: Buy and sell signals update your portfolio


## Project Structure

```bash
stock-trading-bot/
│
├── config/                      # Configuration files
│   └── settings.py              # API key configuration
│
├── db/                          # Database-related scripts
│   ├── create_db.py             # Script to create the database and tables
│   ├── stock_data.db            # SQLite database file (auto-generated)
│   └── query_data.py            # Script to query the database for analysis
│
├── strategies/                  # Trading strategies
│   ├── moving_average.py        # Moving Average strategy implementation
│   └── rsi_strategy.py          # RSI strategy implementation
│
├── technical_indicators/        # Technical indicators (RSI, Bollinger Bands, etc.)
│   └── rsi.py                   # RSI calculation
│
├── utils/                       # Utility functions
│   ├── api_handler.py           # Functions to fetch stock data from the API
│   ├── db_handler.py            # Functions to handle database operations
│   ├── portfolio_tracker.py     # Portfolio management functions
│   └── visualization.py         # Functions to visualize stock data
│
├── .gitignore                  
├── main.py
└── requirements.txt             

