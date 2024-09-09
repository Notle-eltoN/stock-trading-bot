import requests
import pandas as pd
from config.settings import ALPHA_VANTAGE_API_KEY, YAHOO_FINANCE_BASE_URL

def fetch_alpha_vantage_data(symbol, interval='1min'):
    """
    Fetch real-time stock data from Alpha Vantage API.

    :param symbol: Stock symbol (e.g., 'AAPL')
    :param interval: Time interval between data points (default: '1min')
    :return: Pandas DataFrame with stock data
    """
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval={interval}&apikey={ALPHA_VANTAGE_API_KEY}&datatype=csv"
    
    response = requests.get(url)
    if response.status_code == 200:
        data = pd.read_csv(pd.compat.StringIO(response.text))
        return data
    else:
        print(f"Error fetching data for {symbol}: {response.status_code}")
        return None

def fetch_yahoo_finance_data(symbol):
    """
    Fetch stock data from Yahoo Finance API.

    :param symbol: Stock symbol (e.g., 'AAPL')
    :return: Pandas DataFrame with stock data
    """
    url = f"{YAHOO_FINANCE_BASE_URL}quote?symbols={symbol}&fields=symbol,regularMarketPrice"
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return pd.DataFrame(data)
    else:
        print(f"Error fetching Yahoo Finance data for {symbol}: {response.status_code}")
        return None
