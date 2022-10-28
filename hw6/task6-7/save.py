import sys

file_name = 'bakery.csv'


def save_to_file(digits, mode='a'):
    if digits:
        with open(file_name, mode=mode, encoding='utf8') as file:
            lines = map(str, digits)
            text = '\n'.join(lines) + '\n'
            file.write(text)


if __name__ == '__main__':
    try:
        argv = map(lambda x: x.replace(',', '.'), sys.argv[1:])
        prices = list(map(float, argv))
        save_to_file(digits=prices)
    except ValueError:
        print('Введите корректные цифры!')
    except IOError:
        print('Ошибка доступа к файлу.')
    except Exception as ex:
        print(f'Неизвестная ошибка ({ex}).')
