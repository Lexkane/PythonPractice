from functools import partial, singledispatch, reduce, merge


def main():
    pass


f = partial(sorted, key=lambda p: p[1])
g = partial(sorted, [2, 3, 1, 4])


@singledispatch
def pack(obj):
    type_name = type(obj).__name__
    assert False, "Unsupported type:"+type_name


@pack.register(int)
def _(obj):
    return b"I"+hex(obj).encode("ascii")


@pack.register(list)
def _(obj):
    return b"L"+b",".join(map(pack, obj))


reduce(lambda acc, x: acc*x, [1, 2, 3, 4])

reduce(lambda acc, d: 10*acc+int(d), "1914", initial=0)
reduce(merge, [[1, 2, 7], [5.6], [0]])
