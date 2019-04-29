def main():
  class Meta (type):
    def __new__(mcls,name,bases,attrs):
     print (f"creating new class ${name}")
     return super (Meta,mcls).__new__(mcls,name,bases,attrs)
    def __init__(clas,name,bases,attrs):
     print(f"initing new class ${name}")

    class A(object):
     __metaclass__=Meta

    a= A()
    print (a)

if __name__=="__main__":
    main()            