from itertools import zip_longest

tutors_1 = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
classes_1 = ['9А', '7В', '9Б', '9В', '8Б', '10А']

tutors_2 = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
classes_2 = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']


def tutors_and_classes(tutors, classes):
    if len(classes) > len(tutors):
        classes = classes[:len(tutors)]
    for tutor, klass in zip_longest(tutors, classes, fillvalue=None):
        yield tutor, klass


def proof(tutors, classes):
    generator = tutors_and_classes(tutors, classes)
    while True:
        try:
            print(next(generator))
        except StopIteration:
            break


if __name__ == '__main__':
    proof(tutors_1, classes_1)
    print()
    proof(tutors_2, classes_2)
