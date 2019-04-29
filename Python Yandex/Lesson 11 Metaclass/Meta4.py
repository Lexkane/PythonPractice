def main():
    pass


class AddShortNames(type):
    def __init__(cls, name, bases, attrs):
        super(AddShortNames, cls).__init__(name, bases, attrs)
        for name, attr in attrs.items():
            if callable(attr):
                short_name = (attr.__name__[0].upper())
                setattr(cls, short_name, attr)
