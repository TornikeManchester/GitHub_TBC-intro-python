'''
The error you're encountering indicates that the CoinGeckoApi
does not allow querying historical data beyond the past 365 days
for public API users his limitation is why you're receiving a 401 Unauthorized error
when trying to fetch historical Bitcoin prices for a date outside this range.
'''

import datetime
from pycoingecko import CoinGeckoAPI

year = int(input('Enter the year you bought Bitcoin: '))
month = int(input('Enter the month you bought Bitcoin: '))
day = int(input('Enter the day you bought Bitcoin: '))
amount_paid = float(input("Enter the dollar amount paid to buy Bitcoin: "))

purchase_date = datetime.datetime(year, month, day)
date_str = purchase_date.strftime('%d-%m-%Y')

cg = CoinGeckoAPI()
historical_data = cg.get_coin_history_by_id(id='bitcoin', date=date_str)
purchase_price = historical_data['market_data']['current_price']['usd']

current_data = cg.get_price(ids='bitcoin', vs_currencies='usd')
current_price = current_data['bitcoin']['usd']

if purchase_price:
    bitcoin_amount = amount_paid / purchase_price

    # Calculate current value of the Bitcoin
    current_value = bitcoin_amount * current_price

    # Calculate profit or loss
    profit_or_loss = current_value - amount_paid

print(purchase_date)
print(round(purchase_price, 2))
print(current_price)
print(round(current_value, 2))
print(amount_paid)
print(round(profit_or_loss, 2))




