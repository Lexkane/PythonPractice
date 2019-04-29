def main():
    pass


class M(type):
    def f(cls): pass


class C (object):
    __metaclass__ = M


c = C()
C.f()
