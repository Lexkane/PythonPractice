from itertools import tee
def main():
	pass

it=range(3)
a,b,c=tee(it,3)

print(list(a),list(b),list(c))

it=iter(range(3))
a,b=tee(it,2)
used=list(it)
	