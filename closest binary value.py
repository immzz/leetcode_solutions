# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        div = root.val
        if target > root.val and root.right:
            div = min((div,self.closestValue(root.right,target)),key=lambda x:abs(x-target))
        elif target < root.val and root.left:
            div = min((div,self.closestValue(root.left,target)),key=lambda x:abs(x-target))
        return div
            