import sys
from save_ver2 import file_name, format_for_saving, get_upper_bound, get_line_length


def update_value(index, new_value):
    upper_bound = get_upper_bound()
    line_length = get_line_length()
    if not 1 <= index <= upper_bound:
        print(f'Длина файла - {upper_bound} записей.', end=' ')
        raise ValueError
    with open(file_name, mode='r+', encoding='utf8') as file:
        start_byte = (index - 1) * line_length
        value_to_write = format_for_saving(new_value)
        file.seek(start_byte)
        file.write(value_to_write)


if __name__ == '__main__':
    try:
        argv = sys.argv[1:]
        if len(argv) == 2:
            update_value(index=int(argv[0]), new_value=float(argv[1]))
        else:
            print('Слишком много аргументов.')
            update_value(index=20, new_value=99999.999)
    except ValueError:
        print('Введите корректное число.')
    except IOError:
        print('Ошибка доступа к файлу.')
    except Exception as ex:
        print(f'Ошибка: {ex}.')
