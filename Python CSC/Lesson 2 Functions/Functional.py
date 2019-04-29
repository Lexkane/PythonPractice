
def main():
    pass


print(list(map(lambda x,n:x**n,[2,3],range(1,8))))

print(list(filter(lambda x:x%2!=0 , range(10))))

xs=[0,None,[],{}, set(), "", 42]

print(list(filter(None,xs)))

list(zip ("abc", range(3),[42j,42j,42j]))
list (zip("abc",range(10)))