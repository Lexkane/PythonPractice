def main():
	pass

class trace:
		def __init__(self,handle):
			self.handle=handle
		def __call__(self,func):
			@functools.wraps(func)
			def inner(*args,**kwargs):
				print(func.__name__,args,kwargs,
				file=self.handle)
			return func(*args,**kwargs)
		return inner
	
@trace(sys.stderr)
def identity(x):
		return x