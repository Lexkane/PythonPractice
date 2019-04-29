def main():
	pass

def coroutine(g):
	@functools.wraps(g)
	def inner(*args,**kwargs):
		gen=g(*args,**kwargs)
			next(gen)
			return(gen)
		return inner	
	