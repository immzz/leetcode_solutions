# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        return self.do(inorder,0,len(inorder)-1,postorder,0,len(postorder)-1)
    def do(self,inorder,a,b,postorder,c,d):
        if a > b:
            return None
        root = TreeNode(postorder[d])
        p_index = inorder.index(root.val)-a
        root.left = self.do(inorder,a,a+p_index-1,postorder,c,c+p_index-1)
        root.right = self.do(inorder,a+p_index+1,b,postorder,c+p_index,d-1)
        return root
        