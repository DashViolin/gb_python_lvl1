from utils import currency_rates

if __name__ == '__main__':
    while True:
        code = (input('Введите код валюты или "exit" для выхода: ')).strip()
        if code.lower() == 'exit':
            break
        rate, date = currency_rates(code)
        if rate and date:
            print(round(rate, 2), date.isoformat(), sep=', ')
        else:
            print('Введите корректный код валюты.')
