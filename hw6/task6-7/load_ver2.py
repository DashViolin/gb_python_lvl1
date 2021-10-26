import sys
from save_ver2 import file_name, get_line_length, get_upper_bound


def load_values(start=1, stop=None, raw_print=False):
    upper_bound = get_upper_bound()
    line_length = get_line_length()
    if not 1 <= start <= upper_bound:
        start = 1
    if not stop or stop > upper_bound:
        stop = upper_bound
    if start > stop:
        start, stop = stop, start
    with open(file_name, encoding='utf8') as file:
        start_byte = (start - 1) * line_length
        stop_byte = (stop - 1) * line_length
        current_byte = start_byte
        result = []
        file.seek(current_byte)
        while current_byte <= stop_byte:
            if raw_print:
                result.append(file.readline().strip())
            else:
                result.append(str(float(file.readline().strip())))
            current_byte = file.tell()
        return result


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
        print('Введите корректные числа.')
    except IOError:
        print('Ошибка доступа к файлу.')
    except Exception as ex:
        print(f'Ошибка: {ex}.')
