def main():
    
    class Ameta(type):
        def foo(clas):
            print("Ameta foo")

    class  A(object):
        __metaclass__=Ameta
    
    #A.foo()

   class Person(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
   
   guy=Person(name="Bob",age=35)
   print guy.age 


if __name__ == "__main__":
    pass
