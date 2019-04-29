from abc import ABCMeta,abstractmethod
def main():
    pass
class Shape(object):
    __metaclass__=ABCMeta

    @abstractmethod
    def area(self):
        pass
    
class Square(Shape):
    def area(self):
        def area(self):
            return self.w+self.h

t=Square()            