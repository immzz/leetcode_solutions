
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[][]}
    def levelOrderBottom(self, root):
    	results = []
    	level = [root]
    	while len(level) > 0:
    		next_level = []
    		results.insert(0,[x.val for x in level])
    		for node in level:
    			if node.left:
    				next_level.append(node.left)
    			if node.right:
    				next_level.append(node.right)
    		level = next_level[:]
    	return results

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

sol = Solution()
print sol.levelOrderBottom(root)

