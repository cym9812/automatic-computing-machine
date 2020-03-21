class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self, root):
        self.ans = 1
        self.root = root

    def diameterOfBinaryTree(self):
        def depth(node):
            # 访问到空节点了，返回0
            if not node: return 0
            # 左儿子为根的子树的深度
            L = depth(node.left)
            # 右儿子为根的子树的深度
            R = depth(node.right)
            # 计算d_node即L+R+1 并更新ans
            self.ans = max(self.ans, L+R+1)
            # 返回该节点为根的子树的深度
            return max(L, R) + 1

        depth(self.root)
        print(self.ans - 1)


test_tree1 = TreeNode(5, TreeNode(3, TreeNode(1), TreeNode(4)), TreeNode(10, TreeNode(7), TreeNode(15)))
    # 中序遍历：1，3，4，5，7，10，15

test_tree2 = TreeNode(5, TreeNode(3, TreeNode(1), TreeNode(2)))

s = Solution(test_tree1)
s.diameterOfBinaryTree()