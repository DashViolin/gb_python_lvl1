# задание 4 из методички, на сайте они немного отличаются
import sys

users_file = 'users.csv'
hobbies_file = 'hobby.csv'
users_hobby_txt = 'users_hobby.txt'


def parse_users(file_name):
    with open(file_name, encoding='utf8') as file:
        for line in file:
            line = line.strip()
            if line:
                # Выбор кортежа обусловлен тем, что он сохраняет порядок, как и список (поэтому не подходит set),
                # но при этом занимает меньше места в памяти.
                yield tuple(line.split(','))


def parse_hobbies(file_name):
    with open(file_name, encoding='utf8') as file:
        for line in file:
            line = line.strip()
            if line:
                yield line


def save_to_txt(text, file_name):
    with open(file_name, mode='a', encoding='utf8') as file:
        file.write(f'{text.strip()}\n')


if __name__ == '__main__':
    argv = sys.argv[1:]
    if argv:
        if len(argv) == 3:
            users_file = argv[0]
            hobbies_file = argv[1]
            users_hobby_txt = argv[2]
        else:
            print('Неверное количество аргументов. Имена файлов установлены в значения по умолчанию.')

    # очищаем результирующий файл
    with open(users_hobby_txt, mode='w') as file:
        file.write('')

    users = parse_users(users_file)
    hobbies = parse_hobbies(hobbies_file)

    while True:
        try:
            hobby = next(hobbies)
        except StopIteration:
            hobby = None
        try:
            f, i, o = next(users)
        except StopIteration:
            break
        else:
            line = f'{f} {i} {o}: {hobby}'
            save_to_txt(line, users_hobby_txt)
