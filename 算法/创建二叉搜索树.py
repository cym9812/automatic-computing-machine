class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def sortedArrayToBST(nums):
    if len(nums) == 0:
        return
    else:
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = sortedArrayToBST(nums[:mid])
        root.right = sortedArrayToBST(nums[mid + 1:]) # python切片时越界不会报错
        return root


print(sortedArrayToBST([1,3,5,7,9]))