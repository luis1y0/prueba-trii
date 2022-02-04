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
stock_prices = []

for option in options:
    response = requests.get(api_url.format(option))
    stock_price_items = response.json()
    try:
        if len(stock_price_items) > 0 and type(stock_price_items) is list:
            stock_price = stock_price_items[0]
            stock_prices.append(stock_price)
            total_spend += stock_price['price']
        else:
            print(response.status_code)
    except:
        print('Error')

stock_prices.sort(key=lambda x: x['price'], reverse=True)
for stock_price in stock_prices:
    print(stock_price)
print(' -- Calcular --')
budget = int(input('Cual es tu presupuesto para invertir: '))

stock_result_list = []
current_stock_index = 0
while budget > 0:
    spend_count = 0
    current_price = stock_prices[current_stock_index]['price']
    if budget > current_price:
        spend_count = budget % current_price
        budget = budget // current_price
    print(stock_prices[current_stock_index]['symbol'], spend_count, budget)
    if current_stock_index == len(stock_prices) - 1 and budget < current_price:
        break
    if current_stock_index < len(stock_prices) - 1:
        current_stock_index += 1
