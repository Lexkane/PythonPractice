def main():
    pass


for x in iterable:
    action(x)


def for_iterable(iterable, action):
    iterator = iter(iterable)
    try:
        while True:
            x = next(iterator)
            action(x)
    except StopIteration:
        pass


class MyRangeIterator(object):
    def __init__(self, end):
        self.end = end
        self.current = 0

    def next(self):
        if self.current == self.end:
            raise StopIteration()
        result = self.current
        self.current += 1
        return result

class MyRange(object):
    def __init__(self,end):
        self.end=end
    def __iter__(self):
        return MyRangeIterator(self.end)    