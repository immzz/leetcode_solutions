class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums)
        return max(self.rob_no_circle(nums[1:]),nums[0]+self.rob_no_circle(nums[2:len(nums)-1]))
        
    def rob_no_circle(self,nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums)
        profits = [nums[0],max(nums[0:2])] + [0]*(len(nums)-2)
        for i in xrange(2,len(nums)):
            profits[i] = max(profits[i-1],profits[i-2]+nums[i])
        return profits[-1]