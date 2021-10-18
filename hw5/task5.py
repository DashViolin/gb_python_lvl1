src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]


def uniques_in_order(iterable):
    for item in iterable:
        if iterable.count(item) == 1:
            yield item


def uniques_in_order_adv(iterable):
    return filter(lambda item: iterable.count(item) == 1, iterable)


if __name__ == '__main__':
    print('Вариант 1:')
    print([item for item in uniques_inb_order(src)])
    print('Вариант 2:')
    print([item for item in uniques_inb_order_adv(src)])
