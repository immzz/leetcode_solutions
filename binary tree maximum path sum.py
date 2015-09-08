# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        res = [root.val]
        self.maxPathSumDo(root,res)
        return res[0]
    def maxPathSumDo(self,root,res):
        if not root:
            return 0
        current = 0
        l_sum = self.maxPathSumDo(root.left,res)
        r_sum = self.maxPathSumDo(root.right,res)
        current = max(root.val,root.val+max(l_sum,r_sum))
        if current > res[0]:
            res[0] = current
        if root.val + l_sum + r_sum > res[0]:
            res[0] = root.val + l_sum + r_sum
        return current