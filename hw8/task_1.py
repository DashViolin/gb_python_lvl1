import re


def email_parse(email):
    username = re.search(r'^.+(?=@)', email)
    domain = re.search(r'(?<=@).+\..+$', email)
    if username and domain:
        return {'username': username[0], 'domain': domain[0]}
    raise ValueError(f'wrong email: {email}')


def check_email_parse(email):
    try:
        print(email_parse(email))
    except ValueError as ex:
        print(f'ValueError: {ex}')


check_email_parse('someone@geekbrains.ru')
check_email_parse('someone@')
check_email_parse('@someone')
check_email_parse('someone@geekbrains')
