def sortArray(nums):
    max_value = max(nums)
    min_value = min(nums)

    arr = [[] for x in range(max_value - min_value + 1)]
    for i in nums:
        arr[i - min_value] += [i]
    res = []
    for i in arr:
        res += i
    return res
print(sortArray([5,3,6,8,2,1,1,1,13,3,3]))