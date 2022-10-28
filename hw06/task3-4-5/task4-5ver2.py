# задание 4 из методички, на сайте они немного отличаются
from itertools import zip_longest
import sys

users_file = 'users.csv'
hobbies_file = 'hobby.csv'
users_hobby_txt = 'users_hobby.txt'

if __name__ == '__main__':
    argv = sys.argv[1:]
    if argv:
        if len(argv) == 3:
            users_file, hobbies_file, users_hobby_txt = argv
        else:
            print('Неверное количество аргументов. Имена файлов установлены в значения по умолчанию.')

    with open(users_file, encoding='utf8') as users_file:
        with open(hobbies_file, encoding='utf8') as hobbies_file:
            with open(users_hobby_txt, mode='w', encoding='utf8') as result_file:
                for user, hobby in zip_longest(users_file, hobbies_file):
                    if user:
                        print(f'{user.replace(",", " ").strip()}: {str(hobby).strip()}', file=result_file)
                    else:
                        exit(1)
