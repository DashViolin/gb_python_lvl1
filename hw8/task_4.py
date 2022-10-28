from functools import wraps


def val_checker(predicate):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            for arg in args:
                if not predicate(arg):
                    raise ValueError(f'wrong value: {arg}')
            return function(*args, **kwargs)

        return wrapper

    return decorator


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


def check(arg):
    try:
        print(calc_cube(arg))
    except ValueError as ex:
        print(f'ValueError: {ex}')


check(5)
check(0)
check(-5)
