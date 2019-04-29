def main():
    pass


class Parrot(object):
    def __init__(self):
        self.__voltage = 1000

    def __get_voltage(self):
        return self.__voltage

    def __set_voltage(self, value):
        assert isinstance(value, int)
        self.__voltage = value
        
    voltage = property(__get_voltage, __set_voltage)


class Parrot2(object):
    def __init__(self):
        self.__voltage = 1000

    @property
    def voltage(self):
        """Get the current voltage"""
        return self.__voltage

    @voltage.set_iterator
    def voltage(self, value):
        assert isinstance(value, int)
        self.__voltage = value
