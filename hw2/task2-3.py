tokens = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

# Задание 2
new_tokens = []
for token in tokens:
    if not token[0].isalpha():
        new_token = f'{int(token):02d}'
        if token.startswith('+'):
            new_token = '+' + new_token
        new_tokens.append(f'"{new_token}"')
    else:
        new_tokens.append(token)
print(' '.join(new_tokens))

# Задание 3*
for index, token in enumerate(tokens):
    if not token[0].isalpha():
        new_token = f'{int(token):02d}'
        if token.startswith('+'):
            new_token = '+' + new_token
        tokens[index] = f'"{new_token}"'
print(' '.join(tokens))
