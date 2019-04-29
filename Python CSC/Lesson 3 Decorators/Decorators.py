from functools import wraps
from warnings import warn_explicit


def main():
    pass


def once(func):
    @wraps(func)
    def inner(*args, **kwargs):
        if not inner.called:
            func(*args, **kwargs)
            inner.called = True
    inner.called = False
    return inner


@once
def initialize_setting():
    print("Settings initialized")


def memoized(func):
    cache = {}

    @wraps(func)
    def inner(*args, **kwargs):
        key = args, kwargs
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return inner

    @memoized
    def ackermann(m, n):
        if not m:
            return n+1
        elif not n:
            return ackermann(m-1, 1)
        else:
            return ackermann(m-1, ackermann(m, n-1))

def deprecated (func):
    code=func.__code__
    warn_explicit(
        func.__name__+"is deprecated...",
        category=DeprecationWarning,
        filename=code.co_filename,
        lineno=code.co_firstlineno+1)
    return func

@deprecated
def identity(x):
    return x


