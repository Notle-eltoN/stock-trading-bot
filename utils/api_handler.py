import io
import requests
import pandas as pd
from config.settings import ALPHA_VANTAGE_API_KEY
import time

def fetch_alpha_vantage_data(symbol):
    """
    Fetch real-time stock price from Alpha Vantage.
    
    :param symbol: Stock symbol (e.g., 'AAPL')
    :return: Dictionary with stock price and symbol or None if API limit is hit
    """
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=1min&apikey={ALPHA_VANTAGE_API_KEY}&datatype=csv"
    response = requests.get(url)
    
    if response.status_code == 200:
        # Check if the response contains a rate limit message
        if "Thank you for using Alpha" in response.text:
            print(f"Rate limit exceeded for {symbol}. Waiting before retrying...")
            time.sleep(60)  # Wait for 60 seconds to avoid hitting the limit again
            return None  # Return None so no further processing is done for this symbol

        data = pd.read_csv(io.StringIO(response.text))

        # Check the DataFrame structure
        if 'close' not in data.columns:
            print(f"Error: Unable to find 'close' column in the response for {symbol}")
            return None

        latest_data = data.iloc[0]  # Get the latest price
        return {
            'symbol': symbol,
            'price': float(latest_data['close']),
            'timestamp': pd.to_datetime(latest_data['timestamp'])
        }
    else:
        print(f"Error fetching data for {symbol}: {response.status_code}")
        return None
