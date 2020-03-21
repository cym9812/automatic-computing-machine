class RefBinaryTree:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

	def create_string(self, indent):
		s=str(self.data) + "---+"
		if self.left != None:
			s=s+"\n(l)"+indent+self.left.create_string(indent+"    ")
		if self.right != None:
			s=s+"\n(r)"+indent+self.right.create_string(indent+"    ")
		return s
		
	def __str__(self):
		representation = self.create_string("   ")
		return representation 

	def insert_left(self, data):
		t = RefBinaryTree(data)
		if self.left == None:
			self.left = t	
		else:
			t.left = self.left
			self.left = t

	def insert_right(self, data):
		t = RefBinaryTree(data)
		if self.right == None:
			self.right = t
		else:
			t.right = self.right
			self.right = t

	def set_value(self, val):
		self.data = val

	def get_value(self):
		return self.data
		
	def get_left_subtree(self):
		return self.left

	def get_right_subtree(self):
		return self.right

	def get_node_sum(self):
		sum = self.data
		if self.left:
			sum += self.left.get_node_sum()
		if self.right:
			sum += self.right.get_node_sum()
		return sum
