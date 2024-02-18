import requests
from datetime import datetime, timedelta


# function to get the current price of bitcoin
def get_bitcoin_price():
    url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd'
    response = requests.get(url)
    data = response.json()
    return data['bitcoin']['usd']

# function to simulate getting historical prices
def get_historical_prices():
    end_date = datetime.now()  # getting today's date
    start_date = end_date - timedelta(days=30)  # 30 days before today

    # format dates in 'dd-mm-yyyy' format
    end_date = end_date.strftime('%d-%m-%Y')
    start_date = start_date.strftime('%d-%m-%Y')

    url = f'https://api.coingecko.com/api/v3/coins/bitcoin/market_chart/range?vs_currency=usd&from={(datetime.now() - timedelta(days=30)).timestamp()}&to={datetime.now().timestamp()}'
    response = requests.get(url)
    data = response.json()

    # Extract prices and calculate daily averages if needed
    prices = [price[1] for price in data['prices']]  # get only the price values

    return prices

# function to calculate the simple moving average (sma)
def calculate_sma(prices):
    return sum(prices) / len(prices)

# main function to run our trading bot simulation
def run_bot():
    current_price = get_bitcoin_price()
    historical_prices = get_historical_prices()
    sma = calculate_sma(historical_prices)

    print(f"current price: ${current_price}")
    print(f"simple moving average: ${sma}")

    # decision making
    if current_price > sma:
        decision = "buy"
    else:
        decision = "sell"

    # simulate trade (just printing what we'd do)
    print(f"bot decision: {decision}")

# run the bot
run_bot()
