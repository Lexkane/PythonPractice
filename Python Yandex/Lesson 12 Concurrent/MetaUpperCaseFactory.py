def main():
    pass


def upper_attr(future_class_name, future_class_parents, future_class_attr):
    """
      Transforming into upperclass
    """

    attrs = ((name, value) for name, value in future_class_attr.items()
             if not name.startswith('__'))
    uppercase_attr = dict((name.upper(), value) for name, value in attrs)

    return type(future_class_name, future_class_parents, uppercase_attr)


__metaclass__ = upper_attr


class Foo(object):
    bar = 'bip'


print(hasattr(Foo, 'bar'))
# Out False
print(hasattr(Foo, 'BAR'))
# Out: True
f = Foo()
print(f.bar)
