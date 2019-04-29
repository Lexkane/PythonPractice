def main():
    pass


def unique(iterable, seen=set()):
    acc = []
    for item in iterable:
        if item not in seen:
            seen.add(item)
            acc.append(item)
    return acc


def unique2(iterable, seen=None):
    seen = set(seen or [])
    acc = []
    for item in iterable:
        if item not in seen:
            seen.add(item)
            acc.append(item)
    return acc


def flatten(xs, *, depth=None):
    pass


def runner(cmd, **kwargs):
    if kwargs.get("verbose", True):
        print("Logging enabled")


first, *rest = range(1, 5)
for first,*rest in [range(4),range(2)]:
    pass

print(first, rest)

#*_, (first, *rest) = [range(1, 5)]*5
print(first)

x, (x, y) = 1, (2, 3)
print(x)

import dis
print (dis.dis(*first,*rest,last =('a','b','c')))

defaults={"host":"0.0.0.0","port":8080}
print({**defaults,'port':80})


