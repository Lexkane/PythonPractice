from itertools import combinations,\
combinations_with_replacement

def main():
	pass

list(itertools.product("AB",repeat=2))
list(itertools.product("AB",repeat=3))

list(itertools.permutations("AB"))

list(combinations("ABC",2))
list(combinations_with_replacement("ABC",2))	