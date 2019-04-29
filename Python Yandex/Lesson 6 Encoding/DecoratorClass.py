def main():
    pass

class Logger(object):
    def __init__(self,func):
        self.func=func
        self.log=[]
    def __call__(self,*args,**kwargs):
        self.log.append((args,kwargs))
        return self.func(*args,**kwargs) 

logger=Logger