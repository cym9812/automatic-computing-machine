def my_insertion_sort(a_list):
	for index_number in range(1, len(a_list)):
		item_to_insert = a_list[index_number]
		index = index_number - 1
		while index >= 0 and a_list[index] > item_to_insert:
			a_list[index + 1] = a_list[index]
			index -= 1
		a_list[index + 1] = item_to_insert
		print(index_number, "-", a_list)

def insertion_sort(nums):
	for i in range(1, len(nums)):
		item_to_insert = nums.pop(i)
		index = i - 1
		while index >= 0 and nums[index] > item_to_insert:
			index -= 1
		nums.insert(index + 1,item_to_insert)
		print(nums)



a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print("\nSorting a list with Insertion Sort")
print("before: ", a_list)
insertion_sort(a_list)
print("after:  ", a_list)