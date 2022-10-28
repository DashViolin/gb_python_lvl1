import sys
from save import file_name


# Невозможно организовать чтение файла с произвольной строки, так как неизвестно заранее количество символов
# в одной строке (т.е. количество байт). В условии это явно не задано, следовательно оно может различаться,
# следовательно метод seek() нам не поможет, а другого способа нет.
def load_values(start=1, stop=None):
    with open(file_name, encoding='utf8') as file:
        lines = list(filter(bool, map(lambda x: x.strip(), file.readlines())))
        if not 1 <= start <= len(lines):
            start = 1
        if not stop or stop > len(lines):
            stop = len(lines)
        return lines[start - 1:stop]


if __name__ == '__main__':
    try:
        argv = list(map(int, sys.argv[1:]))
        if not argv:
            print('\n'.join(load_values()))
        elif len(argv) == 1:
            print('\n'.join(load_values(start=argv[0])))
        elif len(argv) == 2:
            print('\n'.join(load_values(start=argv[0], stop=argv[1])))
        else:
            print('Слишком много аргументов.')
    except ValueError:
        print('Введите корректные цифры!')
    except IOError:
        print('Ошибка доступа к файлу.')
    except Exception as ex:
        print(f'Ошибка: {ex}.')
