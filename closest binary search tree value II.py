# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        s1 = []
        s2 = []
        self.traverse(False,root,s1,target)
        self.traverse(True,root,s2,target)
        res = []
        while k > 0:
            if not s1:
                res.append(s2.pop())
            elif not s2:
                res.append(s1.pop())
            else:
                if abs(s1[-1]-target) > abs(s2[-1]-target):
                    res.append(s2.pop())
                else:
                    res.append(s1.pop())
            k -= 1
        return res
    def traverse(self,reverse,root,s,target):
        if not root:
            return
        if reverse:
            self.traverse(reverse,root.right,s,target)
            if root.val <= target:
                return
            s.append(root.val)
            self.traverse(reverse,root.left,s,target)
        else:
            self.traverse(reverse,root.left,s,target)
            if root.val > target:
                return
            s.append(root.val)
            self.traverse(reverse,root.right,s,target)
            