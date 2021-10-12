from decimal import Decimal
from datetime import datetime
import requests
from bs4 import BeautifulSoup

API_URL = 'http://www.cbr.ru/scripts/XML_daily.asp'


def currency_rates(code: str):
    response = requests.get(API_URL)
    if response.ok:
        soup = BeautifulSoup(response.text, features="html.parser")
        node = soup.find('charcode', string=code.upper())
        if node:
            rate = Decimal(node.parent.value.text.replace(',', '.'))
            date = datetime.strptime(response.headers['Date'], '%a, %d %b %Y %H:%M:%S GMT').date()
            return rate, date
    return None, None
