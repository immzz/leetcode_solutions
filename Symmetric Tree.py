# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        level = [root]
        while level:
            l = 0
            r = len(level)-1
            while l<r:
                if not ((not level[l] and not level[r]) or (level[l] and level[r] and level[l].val == level[r].val)):
                    return False
                l += 1
                r -= 1
            new_level = []
            for node in level:
                if node:
                    new_level.append(node.left)
                    new_level.append(node.right)
            level = new_level[:]
        return True
        