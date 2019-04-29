def main():
    pass

class NamedGreeter:
    def __init__(self,name):
        self.name=name
    def greet(self):
        print(f"hi my name is {name}")

x= NamedGreeter("Guido")
x.greet            