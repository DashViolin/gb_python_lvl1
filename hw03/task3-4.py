from collections import defaultdict

names = ["Иван", "Мария", "Петр", "Илья"]
full_names = ["Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева", "Иван Алексеев",
              "Мария Савельева", "Петр Иванов", "Илья Сидоров"]


# вариант 1
def thesaurus(names):
    result = defaultdict(list)
    for name in sorted(names):
        result[name[0]] += [name]
    return dict(result)


# вариант 2
def thesaurus_2(names):
    result = {}
    for letter in sorted(set(map(lambda name: name[0], names))):
        result[letter] = list(filter(lambda name: name.startswith(letter), names))
    return result


def thesaurus_adv(full_names):
    result = {}
    for full_name in sorted(full_names, key=lambda x: x.split()[1]):
        sur_char = full_name.split()[1][0]
        result.setdefault(sur_char, {})
        result[sur_char].setdefault(full_name[0], []).append(full_name)
    for sur_char in result:
        for name_char in result[sur_char]:
            result[sur_char][name_char].sort()
    return result


print(thesaurus(names=names))
print()
print(thesaurus_2(names=names))
print()
print(thesaurus_adv(full_names))
