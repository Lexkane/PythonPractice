from itertools import chain 
def main():
	pass

def chain2(*iterables):
		for iterable in iterables:
			yield from iterable
			
take(5,chain(range(2),range(5,10)))
it=(range(x,x**x) for x in range(@,4))
take(5,chain.from_iterable(it))			