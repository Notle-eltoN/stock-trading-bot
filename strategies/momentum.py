import pandas as pd
import numpy as np

def momentum_strategy(data, window=10):
    """
    Momentum trading strategy based on price comparison with n days ago.
    
    :param data: Pandas DataFrame with 'Close' column
    :param window: Lookback window for momentum comparison
    :return: Pandas DataFrame with buy/sell signals
    """
    data['Momentum'] = data['Close'] - data['Close'].shift(window)
    
    # Generate buy/sell signals
    data['Signal'] = 0
    data['Signal'] = np.where(data['Momentum'] > 0, 1, -1)
    
    return data
