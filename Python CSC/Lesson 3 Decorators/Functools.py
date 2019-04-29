
from functools import wraps, update_wrapper


def main():
    pass


def trace(func):
    def inner(*args, **kwargs):
        print(func.__name__, args, kwargs)
        return func(*args, **kwargs)
    update_wrapper(inner, func)
    return inner


def trace2(func):
    @wraps(func)
    def inner(*args, **kwargs):
        print(func.__name__, args, kwargs)
        return func(*args, **kwargs)
    return inner


trace_enabled = False


def trace3(func):
    @wraps(func)
    def inner(*args, **kwargs):
        print(func.__name__, args, kwargs)
        return func(*args, **kwargs)
    return inner if trace_enabled else func


