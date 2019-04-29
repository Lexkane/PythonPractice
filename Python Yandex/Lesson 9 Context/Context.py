def main():
    pass


class Context(object):
    def __init__(self, stop_exeption):
        print("__init__()")
        self.stop_exception = stop_exception

    def __enter__(self):
        print("__enter__")
        return "Some data"

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__({},{}).format'(exc_type.__name__, exc_val))
        return self.stop_exception


with Context(False) as x:
    print("Inside context,x=", x)
    raise RuntimeError("Smith is wrong")
