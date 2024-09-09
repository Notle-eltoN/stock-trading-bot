import matplotlib.pyplot as plt
import pandas as pd

def plot_stock_data(data, title='Stock Data'):
    """
    Plot stock price data.

    :param data: Pandas DataFrame with stock prices
    :param title: Title of the plot
    :return: None
    """
    plt.figure(figsize=(10, 6))
    plt.plot(data['timestamp'], data['close'], label='Close Price')
    plt.title(title)
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.legend()
    plt.show()

def plot_portfolio_performance(portfolio_values, title='Portfolio Performance'):
    """
    Plot the portfolio value over time.

    :param portfolio_values: List of portfolio values over time
    :param title: Title of the plot
    :return: None
    """
    plt.figure(figsize=(10, 6))
    plt.plot(range(len(portfolio_values)), portfolio_values, label='Portfolio Value')
    plt.title(title)
    plt.xlabel('Time')
    plt.ylabel('Portfolio Value')
    plt.legend()
    plt.show()
