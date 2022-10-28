for percent in range(1, 101):
    if percent in [11, 12, 13, 14]:
        print(percent, 'процентов')
    elif percent % 10 == 1:
        print(percent, 'процент')
    elif percent % 10 in [2, 3, 4]:
        print(percent, 'процента')
    else:
        print(percent, 'процентов')
