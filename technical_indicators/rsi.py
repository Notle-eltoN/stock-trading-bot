import pandas as pd

def calculate_rsi(data, window=14):
    """
    Calculate the Relative Strength Index (RSI).
    
    :param data: Pandas Series of stock prices
    :param window: Window size for RSI calculation (default: 14)
    :return: Pandas Series of RSI
    """
    delta = data.diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    avg_gain = gain.rolling(window=window).mean()
    avg_loss = loss.rolling(window=window).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))

    return rsi
