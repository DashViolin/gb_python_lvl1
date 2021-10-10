from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(num):
    """
    Function makes a list of random jokes
    :param num: number of jokes
    :return: a list of random jokes
    """
    result = []
    for _ in range(num):
        result.append(f"{choice(nouns)} {choice(adverbs)} {choice(adjectives)}")
    return result


def get_jokes_adv(*, num, no_repeat=False):
    """
    Function makes a list of random jokes
    :param num: number of jokes
    :param no_repeat: repeat already used words in new jokes
    :return: a list of random jokes
    """
    result = []
    nouns_local = nouns.copy()
    adverbs_local = adverbs.copy()
    adjectives_local = adjectives.copy()
    for _ in range(num):
        if not all([nouns_local, adverbs_local, adjectives_local]):
            break
        noun = choice(nouns_local)
        adverb = choice(adverbs_local)
        adjective = choice(adjectives_local)
        if no_repeat:
            nouns_local.remove(noun)
            adverbs_local.remove(adverb)
            adjectives_local.remove(adjective)
        result.append(f"{noun} {adverb} {adjective}")

    return result


print(get_jokes(15))
print()
print(get_jokes_adv(num=15))
print()
print(get_jokes_adv(num=15, no_repeat=True))
