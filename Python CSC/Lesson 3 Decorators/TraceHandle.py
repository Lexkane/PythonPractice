from functools import wraps, update_wrapper


def main():
    pass


def trace(handle):
    def decorator(func):
        @wraps(func)
        def inner(*args, **kwargs):
            print(func.__name__, args, kwargs, file=handle)
            return func(*args, **kwargs)
        return inner
    return decorator


def with_arguments(deco):
    @wraps(deco)
    def wrapper(*dargs, **dkwargs):
        def decorator(func):
            result = deco(func, *dargs, **dkwargs)
            update_wrapper(result, func)
            return result
        return decorator
    return wrapper
