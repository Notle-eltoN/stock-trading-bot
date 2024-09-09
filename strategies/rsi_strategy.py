import pandas as pd

def calculate_rsi(data, window=14):
    """
    Calculate the Relative Strength Index (RSI).
    
    :param data: Pandas Series of stock prices
    :param window: Window size for RSI calculation
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

def rsi_strategy(data, lower_threshold=30, upper_threshold=70, window=14):
    """
    RSI Strategy to generate buy/sell signals.
    
    :param data: Pandas DataFrame with 'Close' column
    :param lower_threshold: RSI value below which the stock is considered oversold
    :param upper_threshold: RSI value above which the stock is considered overbought
    :param window: Window for RSI calculation
    :return: Pandas DataFrame with buy/sell signals
    """
    data['RSI'] = calculate_rsi(data['Close'], window)
    
    # Generate buy/sell signals
    data['Signal'] = 0
    data['Signal'] = np.where(data['RSI'] < lower_threshold, 1, data['Signal'])  # Buy when RSI is below 30
    data['Signal'] = np.where(data['RSI'] > upper_threshold, -1, data['Signal']) # Sell when RSI is above 70
    
    return data
