def main():
    pass


class A():
    pass


def creator(classname, bases, attrs):
    return A


class C(object):
    __metaclass__ = creator

    def f(self):
        print("hi")


x = C()
print(x.__class__)
print(C.__class__)
print(type.__class__)
