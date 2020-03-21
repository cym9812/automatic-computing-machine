def search(nums, target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        p = left + (right - left) // 2
        if nums[p] == target:
            return p
        elif nums[p] > target:
            right = p - 1
        else:
            left = p + 1
    return - 1

print(search([1,2,3,4,5,7,9,10], 5))
print(search([1,2,3,4,5,7,9,10], 100))
print(search([1,2,3,4,5,7,9,10], 1))