# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if root.left is None and root.right is None:
            return True
        elif root.left is not None and root.right is not None and root.left.val == root.right.val and self.isSymmetric(root.left) and self.isSymmetric(root.right):
                return True
        return False
    

sol = Solution()

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

print sol.isSymmetric(root)