from decimal import Decimal
from datetime import datetime
import requests
from bs4 import BeautifulSoup


def currency_rates(code: str):
    api_url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    response = requests.get(api_url)
    if response.ok:
        soup = BeautifulSoup(response.text, features="html.parser")
        node = soup.find('charcode', string=code.upper())
        if node:
            return float(node.parent.value.text.replace(',', '.'))
    return None


def currency_rates_adv(code: str):
    api_url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    response = requests.get(api_url)
    if response.ok:
        soup = BeautifulSoup(response.text, features="html.parser")
        node = soup.find('charcode', string=code.upper())
        if node:
            rate = Decimal(node.parent.value.text.replace(',', '.'))
            date = datetime.strptime(response.headers['Date'], '%a, %d %b %Y %H:%M:%S GMT').date()
            return rate, date
    return None, None


print(currency_rates('USD'))
print(currency_rates('eur'))
print(currency_rates('bYN'))
print(currency_rates('RUR'))
print()
print(currency_rates_adv('USD'))
print(currency_rates_adv('eur'))
print(currency_rates_adv('bYN'))
print(currency_rates_adv('RUR'))
