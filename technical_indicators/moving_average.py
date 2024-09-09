import pandas as pd

def calculate_sma(data, window):
    """
    Calculate the Simple Moving Average (SMA).
    
    :param data: Pandas Series of stock prices
    :param window: Window size for the moving average
    :return: Pandas Series of SMA
    """
    return data.rolling(window=window).mean()

def calculate_ema(data, window):
    """
    Calculate the Exponential Moving Average (EMA).
    
    :param data: Pandas Series of stock prices
    :param window: Window size for the moving average
    :return: Pandas Series of EMA
    """
    return data.ewm(span=window, adjust=False).mean()
