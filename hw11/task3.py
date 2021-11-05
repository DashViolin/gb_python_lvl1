import sys


class NotNumberInListError(Exception):
    def __init__(self, txt: str):
        self.txt = txt


print('Введите элементы списка. Допускаются только числовые значения.')
print('По окончании ввода оставьте значение пустым или наберите "stop"')
print('Для выхода из программы нажмите "CTRL+C" или наберите "exit".')

result = []
try:
    while True:
        value = input('Введите эелемент списка: ')
        if 'exit' in value:
            raise KeyboardInterrupt
        if not value or 'stop' in value:
            break
        try:
            if not value.replace('.', '').isnumeric() or value.count('.') > 1:
                raise NotNumberInListError('Значение должно быть числом.')
            else:
                result.append(float(value))
        except NotNumberInListError as ex:
            print(ex)
    print(f'Итоговый список: {result}')
except KeyboardInterrupt:
    sys.exit()
