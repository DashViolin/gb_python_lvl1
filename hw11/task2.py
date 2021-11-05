import sys


class MyZeroDivisionError(Exception):
    def __init__(self, txt: str):
        self.txt = txt


print('Для выхода нажмите "CTRL+C" или наберите "exit".')
str_numerator = str_denominator = ''

try:
    while True:
        try:
            print()
            str_numerator = input("Введите числитель: ")
            numerator = float(str_numerator)
            str_denominator = input("Введите знаменатель: ")
            denominator = float(str_denominator)
            if denominator == 0:
                raise MyZeroDivisionError('Знаменатель не должен быть равным 0.')
            print(f'Результат: {round(numerator / denominator, 4)}')
        except ValueError:
            if 'exit' in f'{str_numerator} {str_denominator}':
                raise KeyboardInterrupt
            print("Введите корректное число.")
        except MyZeroDivisionError as ex:
            print(ex)
except KeyboardInterrupt:
    sys.exit()
