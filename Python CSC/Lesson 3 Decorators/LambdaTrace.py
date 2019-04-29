from functools import wraps
import sys


def main():
    pass


def trace(func=None, *, handle=sys.stdout):
    if func is None:
        return lambda func: trace(func, handle=handle)


@wraps(func)
def inner(*args, **kwargs):
    print(func.__name__, args, kwargs)
    return func(*args, **kwargs)
 return inner

# Calculate and print function time performance test
def timethis(func=None,*,n_iter=100):
    if func is None :
        return lambda func: timethis(func,n_iter=n_iter)

    @wraps(func)
    def inner(*args,**kwargs):
        print(func.__name__,end="...")
        acc=float("inf")
        for i in range (n_iter):
            tick=time.perf_counter()
            retuslt=func(*args,**kwargs)
            acc=min(acc,time.perf_counter()-tick)
            print(acc)
            return retuslt
    return inner        

def profiled(func):
    @wraps(func)
    def inner(*args,**kwargs):
        inner.ncalls +=1
        return func(*args,**kwargs)    

@profiled
def indentity(x):
    return x
