class BinHeap:
	def __init__(self, a_list = []): 
		self.heap_list = [0] + a_list
		start_index = self.size() // 2
		for i in range(start_index, 0, -1):
			self.perc_down(i)

	def size(self):
		return len(self.heap_list) - 1

	def is_empty(self):
		return self.size() == 0 

	def insert(self, item): 
		self.heap_list.append(item)
		last_position = len(self.heap_list) - 1  
		self.perc_up(last_position)

	def perc_up(self, i):
		parent_index = i // 2
		while parent_index > 0 and self.heap_list[i] < self.heap_list[parent_index]:
			self.heap_list[i], self.heap_list[parent_index] = self.heap_list[parent_index], self.heap_list[i]
			i = i // 2
			parent_index = i // 2 

	def min_child(self, i):         
		left_child_index = i * 2
		right_child_index = left_child_index + 1
		if right_child_index > self.size():
			return left_child_index
		if self.heap_list[left_child_index] < self.heap_list[right_child_index]:
			return left_child_index
		return right_child_index

	def perc_down(self, i):
		left_child_index = i * 2
		while left_child_index <= self.size():
			child = self.min_child(i)
			if self.heap_list[i] > self.heap_list[child]:
				self.heap_list[child], self.heap_list[i] = self.heap_list[i], self.heap_list[child]
			i = child
			left_child_index = i * 2

	def del_min(self): 
		return_value = self.heap_list[1]
		replacement = self.heap_list.pop()
		if self.size() > 0:
			self.heap_list[1] = replacement
			self.perc_down(1)
		return return_value

		
	def print(self):
		if len(self.heap_list)==1:
			print("Heap empty")
		else:
			print("Heap: ", end="")
			for i in range(1,len(self.heap_list)-1):
				print(self.heap_list[i], end=",")
			print(self.heap_list[len(self.heap_list)-1])
