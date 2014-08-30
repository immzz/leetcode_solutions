# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        if root is None:
            return 0
        import collections
        q = collections.deque()
        q.append((root,1))
        while not len(q) == 0:
            (node,level) = q.popleft()
            if node.left is None and node.right is None:
                return level
            else:
                if node.left is not None:
                    q.append((node.left,level+1))
                if node.right is not None:
                    q.append((node.right,level+1))
            
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
sol = Solution()

print sol.minDepth(root)