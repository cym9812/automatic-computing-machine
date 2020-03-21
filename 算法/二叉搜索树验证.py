class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class VerifyTree:
    def __init__(self, root):
        self.temp = []
        print(self.verify(root))

    # 中序遍历整棵树并储存结果，复杂度O(n)
    def inorder_traversal(self, root):
        if root is None:
            return False
        else:
            self.inorder_traversal(root.left)
            self.temp.append(root.val)
            self.inorder_traversal(root.right)

    def verify(self, root):
        self.inorder_traversal(root)
        if self.temp:
            current = self.temp.pop(0)
            # 验证中序遍历结果是否为升序, 复杂度O(n)
            for i in self.temp:
                if i < current:
                    return False
                current = i
            return True


if __name__ == '__main__':
    test_tree1 = TreeNode(5, TreeNode(3, TreeNode(1), TreeNode(4)), TreeNode(10, TreeNode(7), TreeNode(15)))
    # 中序遍历：1，3，4，5，7，10，15

    test_tree2 = TreeNode(5, TreeNode(3, TreeNode(1), TreeNode(2)))
    # 中序遍历：1，3，2，5

    VerifyTree(test_tree1)
    VerifyTree(test_tree2)
