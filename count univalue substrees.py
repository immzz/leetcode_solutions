# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        count = [0]
        self.do(root,count)
        return count[0]
        
    def do(self,root,count):
        if not root:
            return True
        l = self.do(root.left,count)
        r = self.do(root.right,count)
        if l and r:
            if root.left and not root.left.val == root.val:
                return False
            if root.right and not root.right.val == root.val:
                return False
            count[0] += 1
            return True
        return False
        