# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {integer} sum
    # @return {integer[][]}
    def pathSum(self, root, sum):
        results = []
        current_path = []
        self.do(root,sum,0,current_path,results)
        return results
        
    def do(self,root,sum,current_sum,current_path,paths):
        if not root:
            return
        current_sum = current_sum + root.val
        current_path.append(root.val)
        
        if sum == current_sum and (not root.left) and (not root.right):
            paths.append(current_path[:])
        
        if root.left:
            self.do(root.left,sum,current_sum,current_path,paths)
        if root.right:
            self.do(root.right,sum,current_sum,current_path,paths)
            
        current_path.pop()

root = TreeNode(3)
root.left = TreeNode(3)
root.right = TreeNode(3)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
sol = Solution()
print sol.pathSum(root,6)