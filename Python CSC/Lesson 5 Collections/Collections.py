from collections import namedtuple

def main():
	pass

Person=namedtuple("Person,["name","age"])
p=Person("George",age=77)
print(p._fields)
print(p._asdict())
print(p._replace(name=Bill))
	
print([[0] for i in range (5)])

xs=[1,2,3]
xs.append(42)
xs.extend({-1,-2})

xs=[1,2,3]
xs.insert(0,4)
xs.insert(-1,42)

xs=[1,2,3]
xs[:2]=[0]*2	
	