# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.do(root,0) >= 0
    def do(self,root,depth):
        if not root:
            return depth
        left_depth = self.do(root.left,depth+1)
        right_depth = self.do(root.right,depth+1)
        if abs(left_depth-right_depth) > 1:
            return -1
        return max(left_depth,right_depth)