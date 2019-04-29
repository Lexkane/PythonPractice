def main():
    pass


class Context(object):
    def __enter__(self):
        print("__enter__")
        return "Some data"

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__({},{}).format'(exc_type.__name__, exc_val))


with Context(True) as x:
    print("Inside context,x= ", x)

pas = 'x/tmp'
with open(path, 'w') as fout:
    fout.write('Some stuff')

with open(path, 'w') as fin:
    x = fin.read('Some stuff')
