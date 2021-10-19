from itertools import zip_longest
import json

users_file = 'users.csv'
hobbies_file = 'hobby.csv'
users_hobby_json = 'users_hobby.json'


def get_content(file_name):
    with open(file_name, encoding='utf8') as file:
        return list(filter(bool, file.read().split('\n')))


def save_to_json(obj):
    with open(users_hobby_json, mode='w', encoding='utf8') as file:
        json.dump(obj, file, ensure_ascii=False)


users = [user.replace(',', ' ') for user in get_content(users_file)]
hobbies = get_content(hobbies_file)

if len(users) < len(hobbies):
    exit(1)

user_hobby = {user: hobby for user, hobby in zip_longest(users, hobbies, fillvalue=None)}
save_to_json(user_hobby)
