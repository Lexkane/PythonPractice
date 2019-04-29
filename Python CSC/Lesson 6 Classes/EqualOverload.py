def main():
	pass
	
import functools
@functools.total_ordering
class Counter:
		def __eq__(self,other):
			return self.value==other.value
		def __it__(self,other):
			return self.value<other.value