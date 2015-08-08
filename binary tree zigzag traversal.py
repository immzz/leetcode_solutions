# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[][]}
    def zigzagLevelOrder(self, root):
        results = []
        level = [root]
        current_level_index = 0
        while len(level) > 0:
            next_level = []
            current_level = []
            if current_level_index % 2 == 0:
                for i in xrange(len(level)):
                    current_level.append(level[i].val)
                    if level[i].left:
                        next_level.append(level[i].left)
                    if level[i].right:
                        next_level.append(level[i].right)
                results.append(current_level)
            else:
                for i in xrange(len(level)):
                    current_level.insert(0,level[i].val)
                    if level[i].left:
                        next_level.append(level[i].left)
                    if level[i].right:
                        next_level.append(level[i].right)
                results.append(current_level)
            level = next_level[:]
            current_level_index += 1
        return results
                        
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

sol = Solution()
print sol.zigzagLevelOrder(root)