prices = [7.9, 52.13, 37.91, 37.4, 74.45, 19.45, 88.56, 96, 74.16, 34.14, 19.83, 72, 98.23, 46.5, 27.05, 20.4,
          49.23, 50.11, 0.33, 63.54]

# Пункт A, вариант 1
str_prices = []
for price in prices:
    rub = int(price)
    kop = int((round(price - rub, 2)) * 100)
    str_prices.append(f'{rub} руб {kop:02d} коп')
print(', '.join(str_prices), end='\n\n')

# Пункт A, вариант 2
str_prices = []
for price in prices:
    str_price = str(price)
    if '.' in str_price:
        rub, kop = str_price.split('.')
    else:
        rub, kop = str_price, '00'
    str_prices.append(f'{rub} руб {kop.ljust(2, "0")} коп')
print(', '.join(str_prices), end='\n\n')

# Пункт A, вариант 3
str_prices = []
for price in prices:
    str_price = str(float(price))
    rub, kop = str_price.split('.')
    str_prices.append(f'{rub} руб {kop.ljust(2, "0")} коп')
print(', '.join(str_prices), end='\n\n')

# Пункт B
print(id(prices), prices)
prices.sort()
print(id(prices), prices, end='\n\n')

# Пункт C
print(id(prices), prices)
prices_reversed = list(reversed(prices))
print(id(prices_reversed), prices_reversed, end='\n\n')

# Пункт D
print(prices[15:])
# or
print(prices_reversed[:5][::-1])
