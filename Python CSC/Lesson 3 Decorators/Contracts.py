from functools import wraps
from math import isnan


def main():
    pass


@pre(lambda x: x >= 0, "negative argument")
def checked_log(x):
    pass


is_not_nan = post(lambda r: not isnan(r), "not a number")


@is_not_nan
def something_useful():
    pass


def post(cond, message):
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            result = func(*args, **kwargs)
            assert cond(result), message
            return result
        return inner
    return wrapper


@post(lambda x: not isnan(x), "not a  number")
def something_useful2():
    return float("nan")

def square(func ):
    return lambda x:func (x*x)

def addsome(func):
    return lambda x: func(x+42)

@square
@addsome
def identity(x):
    return x
