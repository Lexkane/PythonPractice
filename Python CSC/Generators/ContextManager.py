from contextlib import contextmanager

def main():
	pass
	
@contextmanager
def cd(path):
	old_path=os.getcwd()
	os/chdir(path)
	try:
		yield
	finally:
		os.chdir(old_path)