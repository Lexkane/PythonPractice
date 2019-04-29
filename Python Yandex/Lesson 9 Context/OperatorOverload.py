def main():
    pass


class Parrot(object):
    def __init__(self):
        self.__voltage = 1000

    def __getattr__(self, name):
        if name == 'voltage':
            return self.__voltage
        raise AttributeError(name+'not found')

    def __setattr__(self, name, value):
        if name == 'voltage':
            assert isinstance(value, int)
            self.__voltage = value
        else:
            super(Parrot, self).__setattr__(name, value)
