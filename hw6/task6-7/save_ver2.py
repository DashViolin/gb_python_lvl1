import sys
import os

file_name = 'bakery.csv'

digit_capacity = 15  # Длина хранимой строки в символах
decimals_length = 3
new_line_symbol_length = 2  # Длина символа новой строки: 2 = CR+LF (Windows), 1 = LF (Unix) or CR (Macintosh)


def get_line_length():
    return digit_capacity + new_line_symbol_length


def format_for_saving(digit):
    return f'{digit:0{digit_capacity}.{decimals_length}f}'[:digit_capacity]


def get_upper_bound():
    return os.path.getsize(file_name) // get_line_length()


def save_to_file(digits, mode='a'):
    if digits:
        with open(file_name, mode=mode, encoding='utf8') as file:
            lines = map(lambda x: format_for_saving(x), digits)
            text = '\n'.join(lines) + '\n'
            file.write(text)


if __name__ == '__main__':
    try:
        argv = map(lambda x: x.replace(',', '.'), sys.argv[1:])
        prices = list(map(float, argv))
        save_to_file(digits=prices)
    except ValueError:
        print('Введите корректные числа.')
    except IOError:
        print('Ошибка доступа к файлу.')
    except Exception as ex:
        print(f'Неизвестная ошибка ({ex}).')
