#Faça um programa que mostre as principais cotações

import yfinance as yf


def get_stock_quotes():
    stock_list = ['AAPL', 'GOOGL', 'AMZN', 'MSFT', 'TSLA']
    stock_data = yf.download(stock_list, period="1d")['Close']
    return stock_data

stock_quotes = get_stock_quotes()
print(stock_quotes)