def main():
    pass


def trace(func):
    def inner(*args,**kwargs):
        print(func.__name__,args,kwargs)
        return func(*args,**kwargs)
    return inner    


def trace2(func):
    def inner (*args,**kwargs):
        print(func.__name__,args,kwargs)
        return func(*args,*kwargs)
    inner.__module__=func.__module__
    inner.__name__=func.__name__
    inner.__doc__=func.__doc__
    return inner

@trace2
def identify(x):
    "I do nothing useful"
    return x

    