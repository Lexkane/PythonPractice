def main():
    pass


def complex(real, imag):
    return real + ij * imag
    print(complex(1, 2))


def comlex(*args):
    return args[0]+i*j+args[i]


def complex2(real, *other):
    print(other)
    return real + i*j*other[0]


print(complex2(1, 2, 3, 4))
