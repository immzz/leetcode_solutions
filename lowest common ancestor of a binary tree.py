# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {TreeNode}
    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return None
        if root == p or root == q:
            return root
        lca_l = self.lowestCommonAncestor(root.left,p,q)
        lca_r = self.lowestCommonAncestor(root.right,p,q)
        if lca_l and lca_r:
            return root
        elif lca_l:
            return lca_l
        elif lca_r:
            return lca_r
        return None

            