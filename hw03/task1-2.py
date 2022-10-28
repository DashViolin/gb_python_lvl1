translation = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять',
}


def num_translate(num_eng):
    return translation.get(num_eng)


def num_translate_adv(num_eng):
    num_rus = translation.get(num_eng.lower())
    if num_eng.istitle():
        return num_rus.title()
    else:
        return num_rus


print(num_translate('seven'))
print(num_translate('one'))
print(num_translate('eleven'))
print()
print(num_translate_adv('six'))
print(num_translate_adv('Two'))
print(num_translate_adv('twelve'))
