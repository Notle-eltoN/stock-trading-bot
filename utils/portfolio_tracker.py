def calculate_portfolio_value(portfolio, stock_prices):
    """
    Calculate the total value of the portfolio based on current stock prices.
    
    :param portfolio: List of portfolio holdings (stock symbol, quantity)
    :param stock_prices: Dictionary of current stock prices (symbol: price)
    :return: Total portfolio value
    """
    total_value = 0
    for stock in portfolio:
        symbol, quantity = stock['symbol'], stock['quantity']
        price = stock_prices.get(symbol, 0)
        total_value += quantity * price
    return total_value

def update_portfolio(portfolio, trade):
    """
    Update the portfolio after a trade.

    :param portfolio: Current portfolio holdings
    :param trade: Trade details (symbol, quantity, buy/sell)
    :return: Updated portfolio
    """
    symbol, quantity, trade_type = trade['symbol'], trade['quantity'], trade['type']
    
    if trade_type == 'buy':
        portfolio[symbol] = portfolio.get(symbol, 0) + quantity
    elif trade_type == 'sell':
        portfolio[symbol] = max(0, portfolio.get(symbol, 0) - quantity)
    
    return portfolio
