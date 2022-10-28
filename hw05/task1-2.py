def odd_nums(number):
    for num in range(number + 1):
        if num % 2:
            yield num


def odd_nums_adv(number):
    return (num for num in range(number + 1) if num % 2)


def proof(func, number, notification):
    print(notification)
    odds_gen = func(number)
    while True:
        try:
            print(next(odds_gen))
        except StopIteration:
            break


if __name__ == '__main__':
    proof(odd_nums, 15, 'With "yield":')
    print()
    proof(odd_nums_adv, 11, 'Without "yield":')
