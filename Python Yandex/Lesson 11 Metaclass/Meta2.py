def main():
    pass


class Meta(type):
    def __init__(cls, name, base, attrs):
        super(Meta, cls).__init__(name, base, attrs)
        cls.f = lambda self: 'qwerty'


class A(object):
    __metaclass__ = Meta
