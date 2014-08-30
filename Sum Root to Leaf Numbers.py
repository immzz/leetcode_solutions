# Definition for a  binary tree node
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        if root is None:
            return 0
        return self.traverse(root,0)
    def traverse(self,root,current_sum):
        current_sum = current_sum * 10 + root.val
        if root.left is None and root.right is None:
            return current_sum
        else:
            s = 0
            if root.left is not None:
                s = s + self.traverse(root.left,current_sum)
            if root.right is not None:
                s = s + self.traverse(root.right,current_sum)
            return s
            
sol = Solution()
root = TreeNode(1)
#root.left = TreeNode(2)
#root.right = TreeNode(3)
print sol.sumNumbers(root)
        