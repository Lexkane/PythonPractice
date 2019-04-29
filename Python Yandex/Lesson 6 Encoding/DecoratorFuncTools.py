import functools


def main():
    pass


def notify_about_calls(func):
    @functools.wraps(func)
    def decorated(*args, **kwargs):
        print("Called", func.__name__)
        return func(*args, **kwargs)
    return decorated


class A(object):
    @staticmethod
    def f(a,b):
        return a+b