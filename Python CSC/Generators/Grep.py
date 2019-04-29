def main():
	pass

def grep(pattern):
		print("Looking for {!r}".format(pattern))
		while True:
		line=yield
		if pattern in line:
			print(line)