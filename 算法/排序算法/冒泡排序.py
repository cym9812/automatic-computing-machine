def bubble_sort_example1(a_list):
	for pass_num in range(len(a_list)-1, 0, -1):
		for i in range(0, pass_num):
			if a_list[i] > a_list[i+1]:
				a_list[i], a_list[i+1] = a_list[i+1], a_list[i]
		print(pass_num, "-", a_list) # comment/uncomment line to see/hide each pass


def bubble_sort(nums):
	unsort = len(nums) - 1
	fin = False
	while not fin:
		fin = True
		for i in range(unsort):
			if nums[i] > nums[i + 1]:
				fin = False
				nums[i], nums[i + 1] = nums[i + 1], nums[i]
		unsort -= 1
	return nums


a_list = [7,3,2,5,1]
print("Sorting a list with Bubble Sort")
print("before: ", a_list)
bubble_sort_example1(a_list)
print("after:  ", a_list)
print("算法复杂度：N^2")
print(bubble_sort(a_list))