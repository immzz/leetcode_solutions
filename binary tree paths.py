# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        path = []
        res = []
        self.do(root,path,res)
        return res
    def do(self,root,path,res):
        if not root:
            return
        path.append(root.val)
        if (not root.left) and (not root.right):
            s = "->".join([str(x) for x in path])
            if s:
                res.append(s)
        if root.left:
            self.do(root.left,path,res)
        if root.right:
            self.do(root.right,path,res)
        path.pop()
        