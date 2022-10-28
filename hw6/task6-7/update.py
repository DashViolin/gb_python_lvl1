import sys
from save import file_name, save_to_file


# Невозможно организовать чтение файла с произвольной строки, так как неизвестно заранее количество символов
# в одной строке (т.е. количество байт). В условии это явно не задано, следовательно оно может различаться,
# следовательно метод seek() нам не поможет, а другого способа нет.
def update_value(index, new_value):
    with open(file_name, encoding='utf8') as file:
        lines = list(filter(bool, map(lambda x: x.strip(), file.readlines())))
    if not 1 <= index <= len(lines):
        raise ValueError
    lines[index - 1] = str(new_value)
    save_to_file(lines, mode='w')


if __name__ == '__main__':
    try:
        argv = sys.argv[1:]
        if len(argv) == 2:
            update_value(index=int(argv[0]), new_value=float(argv[1]))
        else:
            print('Слишком много аргументов.')
    except ValueError:
        print('Введите корректные цифры!')
    except IOError:
        print('Ошибка доступа к файлу.')
    except Exception as ex:
        print(f'Ошибка: {ex}.')
