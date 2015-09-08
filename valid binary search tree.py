# Definition for a binary tree node.
import sys
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isValidBSTDo(root,-sys.maxint,sys.maxint)
    def isValidBSTDo(self,root,l,r):
        if not root:
            return True
        if root.val <= l or root.val >= r:
            return False
        return self.isValidBSTDo(root.left,l,min(root.val,r)) and self.isValidBSTDo(root.right,max(root.val,l),r)

root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.right.left = TreeNode(3)

sol = Solution()
print sol.isValidBST(root)