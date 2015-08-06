# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {integer[]} nums
    # @return {TreeNode}
    def sortedArrayToBST(self, nums):
        return self.do(nums,0,len(nums)-1)
        
    def do(self,nums,l,r):
        if l > r:
            return None
        mid = int((l+r)/2)
        root = TreeNode(nums[mid])
        root.left = self.do(nums,l,mid-1)
        root.right = self.do(nums,mid+1,r)
        return root
        
        