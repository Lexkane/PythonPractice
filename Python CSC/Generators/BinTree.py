def main():
	pass

class BinaryTree:
		def __init__(self,value,left=None,right=None):
			self.value=value
			self.left,self.right=left,right
		def __iter__(self):
			for node in self.left:
				yield node.value
			for node in self.right:
				yield node.value