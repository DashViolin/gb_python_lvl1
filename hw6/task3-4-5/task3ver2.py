from itertools import zip_longest
import json

users_file = 'users.csv'
hobbies_file = 'hobby.csv'
users_hobby_json = 'users_hobby.json'

with open(users_file, encoding='utf8') as users_file:
    with open(hobbies_file, encoding='utf8') as hobbies_file:
        user_hobby = {user.replace(',', ' ').strip(): str(hobby).strip() if user else exit(1)
                      for user, hobby in zip_longest(users_file, hobbies_file, fillvalue=None)}
        with open(users_hobby_json, mode='w', encoding='utf8') as json_file:
            json.dump(user_hobby, json_file, ensure_ascii=False)
