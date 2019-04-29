def main():
    pass


class A(object):
    def __init__(self):
        self.x = 1

    def __getattribute__(self, name):
        return(super(A, self). __getattribute__('x')+1)


a = A()
print(a.x)
print(a.y)
