def main():
    pass
class Vector2D:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other):
        return Vector2D(self.x+other.x,self.y+other.y)
    def __mul__(self,scalar):
        return Vector2D(self.x*scalar,self.y*scalar)
    def __str__(self):
      return (f"x={self.x},y={self.y}") 
    def __getitem__(self,index):
        if index==0:
            return self.x
        elif index==1:
            return self.y    
        print(f"Get {index}")
    def __setitem__(self,index,value):
        if index==0:
            self.x=value
        elif index==1:
            self.y=value     
        print(f"Set {index} {value}")

x=Vector2D (1,0)
print(x)
y=x*2   
print(y)