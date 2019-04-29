def main():
    pass


class A(object):
    def __init__(self):
        self.x = 1

    def __getattr__(self, name):
        return self.x+1


a = A()
print(a.x)
print(a.y, a.z, a.qwerty)


class B(object):
    def __init__(self):
        self.x = 1

    def __getattr__(self, name):
        if name == "doubled":
            return self.base*2
        else:
            raise AttributeError("Attribute not found")


class C(object):
    def __init__(self):
        self.x = 1

    def __setattr__(self, name, value):
        super(A, self).__setattr__("x,value")
