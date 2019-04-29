def main():
    pass
class Rational:
    def __init__(self,num,denom=1):
        self.num=num
        self.denom=denom
    def __mul__(self,other):
        return  self.num*other.num ,self.denom*other.denom
    def __str__(self):
        return "num: "+self.num+" denum: "+self.denom    

r1=Rational(1,5)
r2=Rational(2,3)
c=r1*r2
print(c)