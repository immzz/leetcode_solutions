# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        return self.doPathSum(root,sum,0)
    def doPathSum(self,root,sum,csum):
        if root is None:
            return False
        csum = csum + root.val
        if root.left is None and root.right is None and csum == sum:
            return True
        else:
            return self.doPathSum(root.left,sum,csum) or self.doPathSum(root.right,sum,csum)
            
            
sol = Solution()
r = TreeNode(5)
r.left = TreeNode(4)
r.right = TreeNode(8)
r.left.left = TreeNode(11)
r.left.left.left = TreeNode(7)
r.left.left.right = TreeNode(2)
r.right.left = TreeNode(13)
r.right.right = TreeNode(4)
r.right.right.right = TreeNode(1)

print sol.hasPathSum(r,22)