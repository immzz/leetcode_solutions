# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        s = []
        while root or s:
            if root:
                s.append(root)
                root = root.left
            else:
                root = s.pop()
                k -= 1
                if k == 0:
                    return root.val
                root = root.right
            