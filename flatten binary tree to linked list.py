# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {void} Do not return anything, modify root in-place instead.
    def flatten(self, root):
        self.do(root)
    def do(self,root):
        if not root:
            return None
        last_of_left = None
        last_of_right = None
        if root.left:
            last_of_left = self.do(root.left)
        if root.right:
            last_of_right = self.do(root.right)
        if last_of_left:
            last_of_left.right = root.right
        if root.left:
            root.right = root.left
        root.left = None
        if last_of_right:
            return last_of_right
        elif last_of_left:
            return last_of_left
        else:
            return root

sol = Solution()
root = TreeNode(1)
root.left = None
root.right = TreeNode(2)
sol.flatten(root)
print root.val,root.left,root.right.val