import requests
import json
# write your code here!

# conicoins = float(input('Please, enter the number of conicoins you have: '))
# exchange_rate = float(input('Please, enter the exchange rate: '))

# exchange_rate = {}
# exchange_rate['RUB'] = 2.98
# exchange_rate['ARS'] = 0.82
# exchange_rate['HNL'] = 0.17
# exchange_rate['AUD'] = 1.9622
# exchange_rate['MAD'] = 0.208
#
# conicoins = float(input())
#
# for (key,value) in exchange_rate.items():
#     print('I will get {} {} from the sale of {} conicoins.'.format(round(value * conicoins, 2), key, conicoins))

currency_code = str(input()).lower()
# print(requests.get('http://www.floatrates.com/daily/' + currency_code + '.json'))


r = requests.get('http://www.floatrates.com/daily/' + currency_code + '.json').content
json_obj = json.loads(r)
print(json_obj['usd'])

r = requests.get('http://www.floatrates.com/daily/' + currency_code + '.json').content
json_obj = json.loads(r)
print(json_obj['eur'])
