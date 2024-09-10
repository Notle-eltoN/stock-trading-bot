import pandas as pd
import numpy as np

def calculate_sma(data, window):
    """
    Calculate Simple Moving Average (SMA).
    
    :param data: Pandas Series of stock prices
    :param window: The window size for the moving average
    :return: Pandas Series of the SMA
    """
    return data.rolling(window=window).mean()

def moving_average_strategy(data, short_window=50, long_window=200):
    """
    Simple Moving Average Crossover Strategy.
    
    :param data: Pandas DataFrame with at least a 'Close' column
    :param short_window: Window for short-term SMA
    :param long_window: Window for long-term SMA
    :return: Pandas DataFrame with buy/sell signals
    """
    data['Short_SMA'] = calculate_sma(data['Close'], short_window)
    data['Long_SMA'] = calculate_sma(data['Close'], long_window)
    
    # Generate buy signals
    data['Signal'] = 0
    data['Signal'][short_window:] = np.where(data['Short_SMA'][short_window:] > data['Long_SMA'][short_window:], 1, 0)
    
    # Generate trade actions (1: buy, -1: sell)
    data['Position'] = data['Signal'].diff()
    
    return data
