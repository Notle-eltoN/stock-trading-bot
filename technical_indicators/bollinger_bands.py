import pandas as pd

def calculate_bollinger_bands(data, window=20, num_std=2):
    """
    Calculate Bollinger Bands.
    
    :param data: Pandas Series of stock prices
    :param window: Window size for the moving average (default: 20)
    :param num_std: Number of standard deviations for the bands (default: 2)
    :return: Tuple of Pandas Series (middle_band, upper_band, lower_band)
    """
    middle_band = data.rolling(window=window).mean()
    rolling_std = data.rolling(window=window).std()

    upper_band = middle_band + (rolling_std * num_std)
    lower_band = middle_band - (rolling_std * num_std)

    return middle_band, upper_band, lower_band
