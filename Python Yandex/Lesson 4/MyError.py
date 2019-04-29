def main():
 pass

class MyError(Exception):
    def __init__(self,value):
        self.value=value
    def __str__(self):
        return str(self.value)

try:
    raise MyError(2*2)
except MyError as e:
   print(f" My error,value: {e.value}")  