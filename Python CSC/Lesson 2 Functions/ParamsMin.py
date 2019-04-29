def main ():
    pass

def min(first,*args):
    res=first
    for arg in args:
        if arg<res:
            res=arg
    return res            

def boundeed_min(first,*args,lo=float("-inf"),hi=float("inf")):
    res=hi
    for arg in (first,) +args:
        if arg<res and lo<arg<hi:
            res=arg
        return max(res,lo)       

def simplemin(x,y):
    return x if x<y else y