import functools
import itertools
def main():
    pass

def all_equal(iterable):
    iterator=iter(iterable)
    first_element=next(iterator)
    for element in iterator:
        if element !=first_element:
            return False
    return True        

sequence =[1,2,3,4,5,6,7,8,9,10]
map(str,[1,2,3])    
map(lambda x:x+1,sequence)
[x+1 for x in sequence]

text =" bla bla bla"
map(len,text.split())


for index,el in enumerate (['a','b','c']):
    print(index,el)

filter(callable, [[],int , (),abs ])    

map(lambda x:x%2==0,sequence)

[x for x in sequence if x%2==0]

reduce (func,iterable)
reduce (lambda x,y:x+y,sequence)
reduce(lambda x, y: x*y, sequence)


print (list(product('AB',(1,2,3))))

#permutations
#combinations
#combinations_with_replacement

islice(iterable,begin,end,step)
print(list(islice(range(10),3,7,2)))


print(list(chain (range(3),'abc',range(5))))

#infinite loop
print(list(islice(count(10),5)))

print (list(islice(cycle('abc'),5)))



def smth_loops(width,height,depth):
    for i in range(width):
        for j in range(height):
            for k in range (depth):
               pass

def some_loop(width,height,depth):
    shape=[width,height,depth]
    for i,j,k in product(*map(range,shape)):
        pass


def  grouper(iterable,n,fillvalue=None):
    args[iter(iterable)]*n
    return izip_longest(*args,fillvalue=fillvalue)
list(grouper('ABCDEFG',3,'x'))    