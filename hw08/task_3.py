def type_logger(func):
    def wrapper(*args):
        for arg in args:
            print(f'Arg: {arg}: {type(arg)}')
        result = func(*args)
        print(f'Result: {result}: {type(result)}')
        return result

    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3


@type_logger
def sum_to_str(x, y, z):
    return f'{x + y + z}'


calc_cube(5)
print()
sum_to_str(5, 7.0, True)
