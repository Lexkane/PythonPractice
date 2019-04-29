def main():
    pass

[x**2 for x in range(10) if x%2==1]

list(map(lambda x:x**2, filter(lambda x:x%2==1,range(10))))


nested =[range(5), range(8,10)]
[x for xs in nested for x in xs]
