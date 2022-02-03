from typing import List
import requests

options = [
    'AAPL',
    'GOOGL',
    'AMZN',
    'TSLA',
    'FB',
    'TWTR',
    'UBER',
    'LYFT',
    'SNAP',
    'SHOP'
]

api_url = 'https://financialmodelingprep.com/api/v3/quote-short/{}?apikey=c13a5d2ecf7cc6b8c50c06d7e1dfce22'

total_spend = 0
for option in options:
    response = requests.get(api_url.format(option))
    stock_price_items = response.json()
    try:
        if len(stock_price_items) > 0 and type(stock_price_items) is list:
            stock_price = stock_price_items[0]
            total_spend += stock_price['price']
    except:
        print('Error')
print('El costo de comprar todos los stock disponibles es {} USD'.format(total_spend))