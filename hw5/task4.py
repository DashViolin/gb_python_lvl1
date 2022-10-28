src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]


def greater_than_previous(iterable):
    previous = iterable[0]
    for item in iterable[1:]:
        if item > previous:
            yield item
        previous = item


if __name__ == '__main__':
    print([item for item in greater_than_previous(src)])
