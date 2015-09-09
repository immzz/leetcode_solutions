# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        current = root
        level_count = 0
        while current:
            current = current.left
            level_count += 1
        if level_count == 0:
            return 0
        if level_count == 1:
            return 1
        if level_count == 2:
            return 2 if not root.right else 3
        scout = root
        scout = scout.left
        for i in xrange(level_count-3):
            scout = scout.right
        if not scout.right:
            return 1+self.countNodes(root.left) + 2**(level_count-2) - 1
        return 1+(2**(level_count-1)-1) + self.countNodes(root.right)
        
                
        