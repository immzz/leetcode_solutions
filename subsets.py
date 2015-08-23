class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        current = []
        res = []
        nums.sort()
        self.do(nums,0,current,res)
        return res
    def do(self,nums,i,current,res):
        if i == len(nums):
            res.append(current[:])
            return
        current.append(nums[i])
        self.do(nums,i+1,current,res)
        current.pop()
        self.do(nums,i+1,current,res)
        