# def stringify(func):
#     return str(func)
#
#
# @stringify
# def multiply(a, b):
#     return a * b
#
#
# multiply(10, 2)


def get_multiplier(number):  # function closure
    def inner(a):
        return a * number

    return inner


multiplier_by_2 = get_multiplier(2)
multiplier_by_2(10)

import functools


def logger(func):
    @functools.wraps(func)  # keeps the name of source function
    def wrapped(*args, **kwargs):
        result = func(*args, **kwargs)
        print("log=", result)
        return result

    return wrapped


@logger
def summator(num_list):
    return sum(num_list)


summator([1, 2, 3, 4])
print(summator.__name__)


def logger2(filename):
    def decorator(func):
        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            result = func(*args, **kwargs)
            print("log {} = {}".format(filename, result))
            return result

        return wrapped

    return decorator


@logger2('testik')
def summator(num_list):
    return sum(num_list)


summator([1, 2, 3, 4, 7])
print(summator.__name__)


def first_decorator(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        print("1")
        result = func(*args, **kwargs)
        print("2")
        return result

    return wrapped


def second_decorator(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        print("3")
        result = func(*args, **kwargs)
        print("4")
        return result

    return wrapped


@first_decorator
@second_decorator
def test():
    print("ku-ku")


test()


def bold(func):
    def wrapped():
        return '<b>' + func() + '</b>'

    return wrapped


def italic(func):
    def wrapped():
        return '<i>' + func() + '</i>'

    return wrapped


@bold
@italic
def hello():
    return "my text"


print(hello())
