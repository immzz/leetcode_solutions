# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        return self.do(1,n)
    def do(self,l,r):
        if l > r:
            return [None]
        if l == r:
            return [TreeNode(l)]
        res = []
        for i in xrange(l,r+1):
            left_roots = self.do(l,i-1)
            right_roots = self.do(i+1,r)
            for left_root in left_roots:
                for right_root in right_roots:
                    root = TreeNode(i)
                    root.left = left_root
                    root.right = right_root
                    res.append(root)
        return res
            