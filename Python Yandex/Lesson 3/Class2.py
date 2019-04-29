def main():
    pass

class SecureGreeter:
    def __init__(self,name):
        self._name=name
    def greet(self):
        print(f'Hi my name is {self._name}')


SecureGreeter("Victor")
SecureGreeter.greet("Martin")


