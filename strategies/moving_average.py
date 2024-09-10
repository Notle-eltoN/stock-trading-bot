import pandas as pd
import numpy as np


def calculate_sma(data, window):
    """
    Calculate the Simple Moving Average (SMA).
    
    :param data: List of stock prices
    :param window: Window size for SMA
    :return: Pandas Series of SMA
    """
    return pd.Series(data).rolling(window=window).mean()

def moving_average_strategy(prices, short_window=40, long_window=100):
    """
    Simple Moving Average Crossover Strategy.
    
    :param prices: List of stock prices
    :param short_window: Window size for short-term SMA
    :param long_window: Window size for long-term SMA
    :return: 'buy', 'sell', or None
    """
    if len(prices) < long_window:
        # Not enough data to calculate moving averages
        print("Not enough data to calculate moving averages.")
        return None

    # Convert prices list to a DataFrame
    data = pd.DataFrame(prices, columns=['Price'])
    
    # Calculate short-term and long-term SMAs
    data['Short_SMA'] = calculate_sma(data['Price'], short_window)
    data['Long_SMA'] = calculate_sma(data['Price'], long_window)
    
    # Signal generation logic
    if data['Short_SMA'].iloc[-1] > data['Long_SMA'].iloc[-1]:  # If short SMA is greater than long SMA
        return 'buy'
    elif data['Short_SMA'].iloc[-1] < data['Long_SMA'].iloc[-1]:  # If short SMA is less than long SMA
        return 'sell'
    else:
        return None
