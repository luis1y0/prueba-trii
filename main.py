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

response = requests.get(api_url.format(options[-1]))
print(response.json())