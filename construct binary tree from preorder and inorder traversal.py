# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        return self.do(preorder,0,len(preorder)-1,inorder,0,len(inorder)-1)
        
    def do(self,preorder,a,b,inorder,c,d):
        
        if a>b:
            return None
        root = TreeNode(preorder[a])
        in_index = inorder.index(root.val) - c
        #print a,b,c,in_index,root.val
        root.left = self.do(preorder,a+1,a+in_index,inorder,c,c+in_index-1)
        root.right = self.do(preorder,a+in_index+1,b,inorder,c+in_index+1,d)
        return root

sol = Solution()
print sol.buildTree([3,2,1],[3,2,1])