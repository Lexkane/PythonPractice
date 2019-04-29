def main():
    pass

def make_min(*,lo,hi):
    def inner(frist,*args):
        res=hi
        for arg in (first,)+args:
            if arg<res and lo<arg<hi:
            res=arg
    return max(res,lo)
return inner                